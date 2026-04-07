#!/usr/bin/env bash
# ── Overnight Pipeline Runner ─────────────────────────────────────────────
# Runs the full research pipeline autonomously using Claude Code in headless
# mode. All state is persisted to context/ files between calls.
#
# Usage:
#   chmod +x workflow/run_pipeline.sh
#
#   Full pipeline from scratch:
#     ./workflow/run_pipeline.sh
#
#   Resume Phase 2 loop from a specific iteration (skips Phase 1):
#     ./workflow/run_pipeline.sh --start-iteration 2
#
#   Jump directly to Phase 3 (skips Phase 1 and loop entirely):
#     ./workflow/run_pipeline.sh --start-phase 3
#
#   All flags:
#     --start-iteration N   Start Phase 2 loop at iteration N (1–5). Skips Phase 1.
#                           Preserves existing context/ files.
#     --start-phase N       Start at phase N (1, 2, or 3). Phase 2 starts at iter 1.
#                           --start-phase 2 is equivalent to --start-iteration 1.
#     --skip-permissions    Pass --dangerously-skip-permissions to every claude call.
#                           Enabled by default; use --no-skip-permissions to disable.
#
# Each `claude -p` call is a fresh session. Agents read/write context/ files
# on disk, so state carries across sessions automatically.
# ──────────────────────────────────────────────────────────────────────────

set -euo pipefail

# ── Argument parsing ──────────────────────────────────────────────────────

MAX_ITERATIONS=5
THRESHOLD=4.0
START_ITERATION=1   # first loop iteration to run (1 = normal start)
START_PHASE=1       # first phase to run (1, 2, or 3)
SKIP_PERMS="--dangerously-skip-permissions"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --start-iteration)
            START_ITERATION="${2:?--start-iteration requires a value}"
            START_PHASE=2   # implies skipping Phase 1
            shift 2
            ;;
        --start-phase)
            START_PHASE="${2:?--start-phase requires a value}"
            # If jumping to phase 3, no loop iterations needed
            if [[ "$START_PHASE" -eq 3 ]]; then START_ITERATION=$((MAX_ITERATIONS + 1)); fi
            shift 2
            ;;
        --no-skip-permissions)
            SKIP_PERMS=""
            shift
            ;;
        --skip-permissions|--dangerously-skip-permissions)
            SKIP_PERMS="--dangerously-skip-permissions"
            shift
            ;;
        *)
            echo "Unknown flag: $1" >&2
            echo "Usage: $0 [--start-iteration N] [--start-phase N] [--no-skip-permissions]" >&2
            exit 1
            ;;
    esac
done

# ── Logging helpers ───────────────────────────────────────────────────────

LOG_FILE="workflow/research-log.md"

log() { echo "[$(date '+%H:%M:%S')] $1"; }

log_research() {
    local agent="$1" message="$2"
    echo "- **$(date '+%Y-%m-%d %H:%M')** [$agent] $message" >> "$LOG_FILE"
}

# Common instruction appended to every claude -p prompt
LOG_INSTRUCTION="After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done."

PHASE_STATE_INSTRUCTION="Read context/phase_state.md to understand your current position in the pipeline."

# ── Error trapping ────────────────────────────────────────────────────────

CURRENT_TASK=""  # set before each claude call for error context

on_error() {
    local exit_code=$?
    log "ERROR: Pipeline failed (exit code $exit_code) during: $CURRENT_TASK"
    log_research "Pipeline" "FAILED during '$CURRENT_TASK' at $(date) (exit code $exit_code)"
    # Leave phase_state.md reflecting the failure
    cat > context/phase_state.md << ERREOF
# Phase State
phase: ERROR
step: $CURRENT_TASK
timestamp: $(date -Iseconds)
error: exit code $exit_code
ERREOF
}

trap on_error ERR

# ── Pipeline state writer ─────────────────────────────────────────────────

write_phase_state() {
    local phase="$1" step="$2" detail="${3:-}"
    cat > context/phase_state.md << PSEOF
# Phase State
phase: $phase
step: $step
detail: $detail
timestamp: $(date -Iseconds)
PSEOF
}

# ── Run claude with error context ─────────────────────────────────────────

run_claude() {
    local task_label="$1"
    shift
    CURRENT_TASK="$task_label"
    log_research "Pipeline" "Starting: $task_label"
    claude "$@"
    log_research "Pipeline" "Completed: $task_label"
}

log "Pipeline starting — phase: $START_PHASE, first loop iteration: $START_ITERATION"

# ── PHASE 1: PRE-LOOP ────────────────────────────────────────────────────

if [[ "$START_PHASE" -le 1 ]]; then
    log "═══ PHASE 1: PRE-LOOP ═══"
    write_phase_state 1 "Literature Guardian M1" "Quick Scan"

    log "Running Literature Guardian Mode 1 (Quick Scan)..."
    run_claude "Phase 1 — Literature Guardian M1" -p "You are running the research pipeline Phase 1, step 1.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_context.md.
Use the literature-guardian agent in Mode 1 (Quick Scan).
Follow the instructions in skills/literature-review-light/SKILL.md exactly.
Produce: context/threat_map_v1.md, context/threat_map.md, context/literature_constraints.md, and context/search_log.md.
The search log must record every search query you ran and every paper you reviewed, so future iterations can avoid duplicate work.
$LOG_INSTRUCTION
Do not stop until all four files are written." $SKIP_PERMS

    write_phase_state 1 "Research Director M1" "Initial Plan"

    log "Running Research Director Mode 1 (Initial Plan)..."
    run_claude "Phase 1 — Research Director M1" -p "You are running the research pipeline Phase 1, step 2.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_context.md and context/threat_map_v1.md.
Use the research-director agent in Mode 1 (Initial Research Plan).
Follow the research plan schema defined in the agent file.
Produce: context/research_plan.md.
$LOG_INSTRUCTION
Do not stop until the file is written." $SKIP_PERMS

    # Ensure archives directory exists for feedback snapshots
    mkdir -p context/archives

    # Initialise loop state fresh when starting from Phase 1
    cat > context/loop_state.md << 'EOF'
# Loop State
iteration: 0
current_score: 0.0
threshold: 4.0
status: running

## History
| Iteration | Score | Decision |
|-----------|-------|----------|
EOF

else
    log "Skipping Phase 1 (existing context files preserved)."

    # If resuming the loop, verify required files exist before proceeding
    for f in context/research_plan.md context/threat_map.md context/research_context.md context/loop_state.md; do
        if [[ ! -f "$f" ]]; then
            echo "ERROR: Required file '$f' not found. Cannot resume from iteration $START_ITERATION." >&2
            echo "Run without --start-iteration to generate it first." >&2
            exit 1
        fi
    done
    log "All required context files present. Resuming from iteration $START_ITERATION."
fi

# ── PHASE 2: PLANNING LOOP ───────────────────────────────────────────────

if [[ "$START_PHASE" -le 2 ]]; then
    log "═══ PHASE 2: PLANNING LOOP (iterations $START_ITERATION–$MAX_ITERATIONS) ═══"

    ACTUAL_EXIT_ITER=0

    for i in $(seq "$START_ITERATION" "$MAX_ITERATIONS"); do
        ACTUAL_EXIT_ITER=$i
        log "── Iteration $i of $MAX_ITERATIONS ──"
        write_phase_state 2 "Iteration $i" "Research Director M2"

        # ── Archive prior evaluator feedback before overwrite ──
        if [[ -f context/evaluator_feedback.md && "$i" -gt 1 ]]; then
            mkdir -p context/archives
            cp context/evaluator_feedback.md "context/archives/evaluator_feedback_i$((i - 1)).md"
            log "  Archived evaluator feedback from iteration $((i - 1))"
        fi

        # Build the list of all prior feedback files for the Director to read
        FEEDBACK_FILES=""
        for prev in $(seq 1 $((i - 1))); do
            if [[ -f "context/archives/evaluator_feedback_i${prev}.md" ]]; then
                FEEDBACK_FILES="${FEEDBACK_FILES}context/archives/evaluator_feedback_i${prev}.md, "
            fi
        done

        # Step 1: Research Director M2 — revise the plan
        log "  Research Director M2 (Plan Revision)..."
        run_claude "Phase 2 iter $i — Research Director M2" -p "You are running the research pipeline Phase 2, iteration $i, step 1.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan.md, context/threat_map.md, context/research_context.md.
If context/evaluator_feedback.md exists, read it — this is the most recent evaluator feedback.
Also read any prior archived feedback files to understand the full history of evaluator concerns: ${FEEDBACK_FILES:-none from prior iterations}.
Use the research-director agent in Mode 2 (Plan Revision).
Update context/research_plan.md in place with a changelog entry for iteration $i.
Follow the conflict priority rule in .claude/agents/research-director.md if feedback and threats conflict.
$LOG_INSTRUCTION" $SKIP_PERMS

        write_phase_state 2 "Iteration $i" "Literature Guardian M2"

        # Step 2: Literature Guardian M2 — targeted check
        log "  Literature Guardian M2 (Targeted Check)..."
        run_claude "Phase 2 iter $i — Literature Guardian M2" -p "You are running the research pipeline Phase 2, iteration $i, step 2.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan.md (just revised by the Director), context/threat_map.md, context/research_context.md, and context/literature_constraints.md.
If context/search_log.md exists, read it to avoid repeating previous searches.
Use the literature-guardian agent in Mode 2 (Targeted Check).
Follow the instructions in skills/literature-review-targeted/SKILL.md exactly.
Update context/threat_map.md in place with a changelog entry for iteration $i.
Update context/literature_constraints.md if new constraints are found.
Append any new searches and papers reviewed to context/search_log.md.
$LOG_INSTRUCTION" $SKIP_PERMS

        write_phase_state 2 "Iteration $i" "Research Evaluator M1"

        # Step 3: Research Evaluator M1 — score the plan
        log "  Research Evaluator M1 (Plan Evaluation)..."
        run_claude "Phase 2 iter $i — Research Evaluator M1" -p "You are running the research pipeline Phase 2, iteration $i, step 3.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan.md, context/threat_map.md, context/research_context.md, and context/evaluation_criteria.md.
Use the research-evaluator agent in Mode 1 (Plan Evaluation).
Write context/evaluator_feedback.md from scratch using the evaluation report schema.
Update context/loop_state.md: set iteration to $i, update current_score, append to the history table.
Apply the scoring formula: overall_score = min(novelty, mechanism_clarity, feasibility) * 0.6 + mean(all_seven) * 0.4
Apply hard failure conditions from context/evaluation_criteria.md.
$LOG_INSTRUCTION" $SKIP_PERMS

        # Check exit condition by reading loop_state.md
        SCORE=$(grep -oP 'current_score:\s*\K[0-9.]+' context/loop_state.md 2>/dev/null || echo "0.0")
        log "  Score: $SCORE (threshold: $THRESHOLD)"

        if python3 -c "import sys; sys.exit(0 if float('${SCORE}') >= float('${THRESHOLD}') else 1)"; then
            log "  Score meets threshold. Exiting loop."
            sed -i "s/^status: .*/status: accepted/" context/loop_state.md
            # Archive the final iteration's feedback
            cp context/evaluator_feedback.md "context/archives/evaluator_feedback_i${i}.md"
            break
        fi

        if [[ "$i" -eq "$MAX_ITERATIONS" ]]; then
            log "  Max iterations reached. Proceeding to Phase 3."
            sed -i "s/^status: .*/status: max_iterations/" context/loop_state.md
        fi
    done

    # ── Mark skipped iterations in loop_state ──
    if [[ "$ACTUAL_EXIT_ITER" -lt "$MAX_ITERATIONS" ]]; then
        for j in $(seq $((ACTUAL_EXIT_ITER + 1)) "$MAX_ITERATIONS"); do
            echo "| $j | — | SKIPPED |" >> context/loop_state.md
        done
        log "Marked iterations $((ACTUAL_EXIT_ITER + 1))–$MAX_ITERATIONS as SKIPPED in loop_state.md"
    fi

else
    log "Skipping Phase 2 loop."
fi

# ── PHASE 3: POST-LOOP EXECUTION ─────────────────────────────────────────

log "═══ PHASE 3: POST-LOOP EXECUTION ═══"

# Verify inputs for Phase 3
for f in context/research_plan.md context/threat_map.md context/research_context.md; do
    if [[ ! -f "$f" ]]; then
        echo "ERROR: Required file '$f' not found for Phase 3." >&2
        exit 1
    fi
done

write_phase_state 3 "Step 1" "Research Director M3 — Final Program"

log "Step 1: Research Director Mode 3 (Final Program)..."
run_claude "Phase 3 — Research Director M3" -p "You are running the research pipeline Phase 3, step 1.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan.md, context/threat_map.md, and context/research_context.md.
Use the research-director agent in Mode 3 (Final Research Program).
Produce: context/research_plan_final.md, context/paper_structure.md, context/task_queue.md, and context/novelty_claims.md.
$LOG_INSTRUCTION" $SKIP_PERMS

write_phase_state 3 "Step 2" "Literature Guardian M3 — Deep Review"

log "Step 2: Literature Guardian Mode 3 (Deep Review)..."
run_claude "Phase 3 — Literature Guardian M3" -p "You are running the research pipeline Phase 3, step 2.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_context.md, context/threat_map.md, context/novelty_claims.md.
If context/literature_notes.md exists, read it too.
If context/search_log.md exists, read it to see all prior searches and avoid duplication.
Use the literature-guardian agent in Mode 3 (Deep Review).
Follow the instructions in skills/literature-review-deep/SKILL.md exactly.
Produce: context/threat_map_final.md, context/literature_notes.md, context/literature_constraints.md, and context/literature_review.md.
Append final search queries to context/search_log.md.
Do NOT produce any .tex files.
$LOG_INSTRUCTION" $SKIP_PERMS

write_phase_state 3 "Step 3" "Theory Builder — Model Derivation"

log "Step 3: Theory Builder (model derivation)..."
run_claude "Phase 3 — Theory Builder" -p "You are running the research pipeline Phase 3, step 3.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan_final.md, context/task_queue.md, context/research_context.md.
If context/model_equations.md exists and is non-empty, read it too.
Use the theory-builder agent.
Follow the workflow in .claude/agents/theory-builder.md.
Work through each model component sequentially. Do not attempt the integrating section until all components have closed equilibria.
Write all output to context/model_equations.md.
Include the Open Questions section even if everything closed cleanly.
$LOG_INSTRUCTION" $SKIP_PERMS

write_phase_state 3 "Step 4" "Model Verifier — Completeness Check"

log "Step 4: Model Verifier (completeness check)..."
run_claude "Phase 3 — Model Verifier" -p "You are running the research pipeline Phase 3, step 4.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/model_equations.md, context/research_plan_final.md, context/research_context.md, and context/task_queue.md.
Use the model-verifier agent as described in .claude/agents/model-verifier.md.
Assess completeness, derivation integrity, and scope compliance.
Write your verdict (PASS / CONDITIONAL PASS / FAIL) and full report to context/model_verifier_report.md.
If CONDITIONAL PASS or FAIL, list every specific issue the Theory Builder must fix.
$LOG_INSTRUCTION" $SKIP_PERMS

# Read verifier verdict
VERDICT=$(grep -oiP '^\*\*(PASS|CONDITIONAL PASS|FAIL)\*\*|^verdict:\s*\K\S+' context/model_verifier_report.md 2>/dev/null | head -1 || echo "UNKNOWN")
log "  Model Verifier verdict: $VERDICT"

if [[ "$VERDICT" == *"FAIL"* && "$VERDICT" != *"CONDITIONAL"* ]]; then
    log "ERROR: Model Verifier returned FAIL. Human review required before proceeding."
    log "See context/model_verifier_report.md for details."
    exit 1
fi

if [[ "$VERDICT" == *"CONDITIONAL"* ]]; then
    write_phase_state 3 "Step 4b" "Theory Builder — Correction Round"

    log "  Conditional pass — running Theory Builder correction round..."
    run_claude "Phase 3 — Theory Builder correction" -p "You are running the research pipeline Phase 3, Theory Builder correction round.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/model_verifier_report.md carefully — it contains specific issues you must fix.
Read context/model_equations.md, context/research_plan_final.md, context/research_context.md.
Fix every issue listed in the CONDITIONAL PASS report.
Update context/model_equations.md in place.
$LOG_INSTRUCTION" $SKIP_PERMS

    write_phase_state 3 "Step 4c" "Model Verifier — Re-check"

    log "  Re-running Model Verifier after correction..."
    run_claude "Phase 3 — Model Verifier re-check" -p "You are running the research pipeline Phase 3, Model Verifier re-check.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/model_equations.md, context/research_plan_final.md, context/research_context.md, and context/task_queue.md.
Use the model-verifier agent. This is a re-check after a correction round.
Write your updated verdict and report to context/model_verifier_report.md (overwrite).
If still CONDITIONAL PASS or FAIL, escalate — write 'ESCALATE TO HUMAN' as the first line.
$LOG_INSTRUCTION" $SKIP_PERMS

    VERDICT2=$(grep -oiP '^\*\*(PASS|CONDITIONAL PASS|FAIL)\*\*|^verdict:\s*\K\S+|^ESCALATE' context/model_verifier_report.md 2>/dev/null | head -1 || echo "UNKNOWN")
    log "  Re-check verdict: $VERDICT2"
    if [[ "$VERDICT2" != "PASS" && "$VERDICT2" != *"PASS"* ]]; then
        log "ERROR: Model still failed after correction round. Human review required."
        log "See context/model_verifier_report.md."
        exit 1
    fi
fi

write_phase_state 3 "Step 5" "Research Evaluator M2 — Output Evaluation"

log "Step 5: Research Evaluator Mode 2 (Output Evaluation)..."
run_claude "Phase 3 — Research Evaluator M2" -p "You are running the research pipeline Phase 3, step 5.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/research_plan_final.md, context/threat_map_final.md, context/model_equations.md, and context/model_verifier_report.md.
Use the research-evaluator agent in Mode 2 (Output Evaluation).
Simulate a full referee report for the target venue.
Write the full referee simulation to context/evaluator_feedback.md.
$LOG_INSTRUCTION" $SKIP_PERMS

write_phase_state 3 "Step 6" "Paper Writer — Academic Writing"

log "Step 6: Paper Writer (Academic Writing)..."
run_claude "Phase 3 — Paper Writer" -p "You are running the research pipeline Phase 3, step 6.
Read context/phase_state.md to understand your current position in the pipeline.
Read context/paper_structure.md, context/literature_review.md, context/model_equations.md, and context/research_context.md.
Read context/evaluator_feedback.md for referee concerns to address.
Read any existing paper/sections/*.tex files before writing.
Use the academic-writing skill in skills/academic-writing/SKILL.md.
Write all paper sections as .tex files in paper/sections/.
Start with literature.tex (convert literature_review.md to LaTeX).
Then write all remaining sections as defined in context/paper_structure.md.
$LOG_INSTRUCTION" $SKIP_PERMS

write_phase_state 3 "COMPLETE" "Pipeline finished successfully"

log "═══ PIPELINE COMPLETE ═══"
log "Intermediate outputs: context/"
log "Manuscript sections:  paper/sections/"
log "Evaluator feedback:   context/evaluator_feedback.md"
log "Model verifier:       context/model_verifier_report.md"
