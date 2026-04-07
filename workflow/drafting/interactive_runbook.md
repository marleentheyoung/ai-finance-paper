# Interactive Pipeline Runbook

Step-by-step guide for running the research pipeline interactively in a Claude Code session (Option A). Each step includes the exact prompt to paste.

**Before you start:**
1. Open the devcontainer and run `just install`
2. Authenticate Claude Code (`claude` in the terminal, follow the browser login)
3. Fill in `context/research_context.md` with your research idea

**How to use this runbook:**
- Open a Claude Code session: `claude`
- Copy-paste each prompt below into the session
- Wait for the step to complete before moving to the next
- Check the output files after each step to verify they look right
- Each step is a self-contained prompt — you can stop and resume at any point

> **Tip:** Each prompt is designed for a fresh Claude Code session. If your session gets long or sluggish, exit with `/exit` and start a new `claude` session. State is persisted to `context/` files, so nothing is lost.

---

## Phase 1: Pre-Loop

### Step 1.1 — Literature Guardian: Quick Scan

**What it does:** Scans the literature for papers related to your research idea and produces an initial threat map.

**Files produced:** `context/literature/threat_map_v1.md`, `context/literature/threat_map.md`, `context/literature/constraints.md`, `context/literature/search_log.md`

```
You are running the research pipeline Phase 1, step 1.
Read context/research_context.md.
Use the literature-guardian agent in Mode 1 (Quick Scan).
Follow the instructions in .claude/skills/literature-review/light/SKILL.md exactly.
Produce: context/literature/threat_map_v1.md, context/literature/threat_map.md, context/literature/constraints.md, and context/literature/search_log.md.
The search log must record every search query you ran and every paper you reviewed, so future iterations can avoid duplicate work.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
Do not stop until all four files are written.
```

**Verify before continuing:** All four files exist in `context/`. The threat map should list specific papers and their threat level (HIGH/MODERATE/LOW).

---

### Step 1.1b — HUMAN CHECKPOINT: Review the Threat Map

> **This is the most important human checkpoint in the pipeline.** The quality of everything downstream depends on the threat map being accurate and complete.

**Review `context/literature/threat_map_v1.md` and take action:**

1. **Add missing papers.** If you know of papers the scan missed, add them to the threat map in the correct channel section using the paper entry schema. You do not need to fill every field — the Literature Guardian will complete them in later passes.

2. **Correct misclassifications.** If a paper is classified as HIGH but you know its mechanism is different from yours, downgrade it (or vice versa). Add a note explaining why.

3. **Check the aggregate assessment.** Does the "Core contribution status" section match your intuition? If the scan says your core contribution is threatened and you disagree, note why.

4. **Consider updating your research idea.** If the threat map reveals that your core mechanism is already published, you may want to update `context/research_context.md` before proceeding — adjusting the research question, sharpening the mechanism, or adding a differentiating scope constraint.

You can edit the threat map directly or create `context/human_feedback_phase1.md` with your notes. If you create this file, the Research Director will read it alongside the threat map.

**When satisfied**, proceed to Step 1.2.

---

### Step 1.2 — Research Director: Initial Plan

**What it does:** Creates the initial research plan based on your research idea and the threat map.

**Files produced:** `context/planning/research_plan.md`

```
You are running the research pipeline Phase 1, step 2.
Read context/research_context.md, context/literature/threat_map_v1.md, and context/literature/constraints.md.
If context/human_feedback_phase1.md exists, read it too — it contains human corrections to the threat map.
Use the research-director agent in Mode 1 (Initial Research Plan).
Follow the research plan schema defined in the agent file.
Use the literature constraints (especially the gap analysis) to inform which contributions are most defensible.
Produce: context/planning/research_plan.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
Do not stop until the file is written.
```

**Verify before continuing:** `context/planning/research_plan.md` exists and contains numbered contributions, scope constraints, and a channel breakdown.

### Step 1.3 — Initialise loop state

Before entering Phase 2, create the loop state file. Run this in your terminal (not in Claude Code):

```bash
mkdir -p context/archives
cat > context/loop_state.md << 'EOF'
# Loop State
iteration: 0
current_score: 0.0
decision: pending
threshold: 4.0
status: running

## History
| Iteration | Score | Decision |
|-----------|-------|----------|
EOF
```

---

## Phase 2: Planning Loop

Phase 2 iterates up to 5 times. Each iteration has 3 steps. You exit the loop when the score reaches 4.0/5.0 or after 5 iterations.

Replace `{N}` in the prompts below with the current iteration number (1, 2, 3, ...).

### Step 2.1 — Research Director: Plan Revision (iteration {N})

**What it does:** Revises the research plan based on evaluator feedback and the threat map.

**Files updated:** `context/planning/research_plan.md`

```
You are running the research pipeline Phase 2, iteration {N}, step 1.
Read context/planning/research_plan.md, context/literature/threat_map.md, context/research_context.md.
If context/literature/constraints.md exists, read it — this is the accumulated gap analysis from the Literature Guardian.
If context/evaluator_feedback.md exists, read it — this is the most recent evaluator feedback.
Also read any prior archived feedback files in context/archives/ (evaluator_feedback_i1.md, evaluator_feedback_i2.md, etc.) to understand the full history of evaluator concerns.
Use the research-director agent in Mode 2 (Plan Revision).
Update context/planning/research_plan.md in place with a changelog entry for iteration {N}.
Follow the conflict priority rule in .claude/agents/research-director.md if feedback and threats conflict.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 2.2 — Literature Guardian: Targeted Check (iteration {N})

**What it does:** Checks the revised plan against the literature and updates the threat map.

**Files updated:** `context/literature/threat_map.md`, `context/literature/constraints.md`, `context/literature/search_log.md`

```
You are running the research pipeline Phase 2, iteration {N}, step 2.
Read context/planning/research_plan.md (just revised by the Director), context/literature/threat_map.md, context/research_context.md, and context/literature/constraints.md.
If context/literature/search_log.md exists, read it to avoid repeating previous searches.
If context/evaluator_feedback.md exists, read it for literature positioning concerns the evaluator flagged.
Use the literature-guardian agent in Mode 2 (Targeted Check).
Follow the instructions in .claude/skills/literature-review/targeted/SKILL.md exactly.
Update context/literature/threat_map.md in place with a changelog entry for iteration {N}.
Update context/literature/constraints.md if new constraints are found.
Append any new searches and papers reviewed to context/literature/search_log.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 2.3 — Research Evaluator: Score the Plan (iteration {N})

**What it does:** Scores the plan on 8 criteria. If the overall score >= 4.0, you can exit the loop.

**Files produced:** `context/evaluator_feedback.md`, `context/loop_state.md` (updated)

```
You are running the research pipeline Phase 2, iteration {N}, step 3.
Read context/planning/research_plan.md, context/literature/threat_map.md, context/research_context.md, and context/evaluation_criteria.md.
If context/literature/constraints.md exists, read it for confirmed literature gaps.
Use the research-evaluator agent in Mode 1 (Plan Evaluation).
Write context/evaluator_feedback.md from scratch using the evaluation report schema.
Update context/loop_state.md: set iteration: to {N}, set current_score: to the overall score (one decimal place), set decision: to ACCEPT/REVISE/REJECT. Append a row to the History table: | {N} | {score} | {decision} |
Apply the scoring formula: overall_score = min(novelty, mechanism_clarity, feasibility) * 0.6 + mean(all_eight) * 0.4
Apply hard failure conditions from context/evaluation_criteria.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

**After this step:**
- Check `context/loop_state.md` for the score
- If `current_score >= 4.0` — archive feedback (`cp context/evaluator_feedback.md context/archives/evaluator_feedback_i{N}.md`), then proceed to Phase 3
- If `current_score < 4.0` and iteration < 5 — archive feedback and loop back:
  ```bash
  cp context/evaluator_feedback.md context/archives/evaluator_feedback_i{N}.md
  ```
  Then repeat steps 2.1–2.3 with `{N+1}`
- If iteration = 5 — archive feedback (`cp context/evaluator_feedback.md context/archives/evaluator_feedback_i5.md`), then proceed to Phase 3 regardless of score

### Step 2.3b — HUMAN CHECKPOINT (recommended)

> Review `context/evaluator_feedback.md` before continuing to the next iteration. Check for:
> 1. **Hard failures** (Novelty/Mechanism Clarity/Feasibility ≤ 2) — consider updating `context/research_context.md` before the next iteration
> 2. **Score regression** — if the score dropped from the previous iteration, the loop may be oscillating; review the revision directives
> 3. **HIGH threat escalation** — if the LG surfaced a new HIGH threat this iteration, verify it before the RD responds to it
>
> In overnight mode (`run_pipeline.sh`), this checkpoint is skipped. Use `--pause-on-reject` to stop the pipeline on hard failures.

---

## Phase 3: Post-Loop Execution

### Step 3.1 — Research Director: Final Program

**What it does:** Consolidates the plan into a final program with paper structure and task queue.

**Files produced:** `context/planning/research_plan_final.md`, `context/planning/paper_structure.md`, `context/planning/task_queue.md`, `context/planning/novelty_claims.md`

```
You are running the research pipeline Phase 3, step 1.
Read context/planning/research_plan.md, context/literature/threat_map.md, context/research_context.md, and context/literature/constraints.md.
If context/evaluator_feedback.md exists, read it for the evaluator's final assessment of the plan.
Use the research-director agent in Mode 3 (Final Research Program).
Produce: context/planning/research_plan_final.md, context/planning/paper_structure.md, context/planning/task_queue.md, and context/planning/novelty_claims.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 3.2 — Literature Guardian: Deep Review

**What it does:** Exhaustive literature review to verify all novelty claims and produce the literature review prose.

**Files produced:** `context/literature/threat_map_final.md`, `context/literature/notes.md`, `context/literature/constraints.md`, `context/literature/review.md`

```
You are running the research pipeline Phase 3, step 2.
Read context/research_context.md, context/literature/threat_map.md, context/planning/novelty_claims.md.
Read context/planning/research_plan_final.md for the finalized research plan.
If context/literature/notes.md exists, read it too.
If context/literature/search_log.md exists, read it to see all prior searches and avoid duplication.
If context/literature/constraints.md exists, read it as the accumulated gap analysis from prior iterations.
Use the literature-guardian agent in Mode 3 (Deep Review).
Follow the instructions in .claude/skills/literature-review/deep/SKILL.md exactly.
Produce: context/literature/threat_map_final.md, context/literature/notes.md, context/literature/constraints.md, and context/literature/review.md.
Append final search queries to context/literature/search_log.md.
Do NOT produce any .tex files.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 3.3 — Theory Builder: Model Derivation

**What it does:** Derives the formal model — equilibrium conditions, propositions, comparative statics.

**Files produced:** `context/model_equations.md`

```
You are running the research pipeline Phase 3, step 3.
Read context/planning/research_plan_final.md, context/planning/task_queue.md, context/research_context.md.
If context/model_equations.md exists and is non-empty, read it too.
Use the theory-builder agent.
Follow the workflow in .claude/agents/theory-builder.md.
Work through each model component sequentially. Do not attempt the integrating section until all components have closed equilibria.
Write all output to context/model_equations.md.
Include the Open Questions section even if everything closed cleanly.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 3.4 — Model Verifier: Completeness Check

**What it does:** Verifies the model for correctness, completeness, and scope compliance. Produces a PASS/CONDITIONAL PASS/FAIL verdict.

**Files produced:** `context/model_verifier_report.md`

```
You are running the research pipeline Phase 3, step 4.
Read context/model_equations.md, context/planning/research_plan_final.md, context/research_context.md, and context/planning/task_queue.md.
Use the model-verifier agent as described in .claude/agents/model-verifier.md.
Assess completeness, derivation integrity, and scope compliance.
Write your verdict (PASS / CONDITIONAL PASS / FAIL) and full report to context/model_verifier_report.md.
If CONDITIONAL PASS or FAIL, list every specific issue the Theory Builder must fix.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

**After this step:**
- **PASS** — continue to Step 3.5
- **CONDITIONAL PASS** — run the correction round (Step 3.4b), then re-verify (Step 3.4c)
- **FAIL** — review `context/model_verifier_report.md` manually; you may need to simplify scope constraints in `context/research_context.md` and re-run from Step 3.3

---

### Step 3.4b — Theory Builder: Correction Round (only if CONDITIONAL PASS)

```
You are running the research pipeline Phase 3, Theory Builder correction round.
Read context/model_verifier_report.md carefully — it contains specific issues you must fix.
Read context/model_equations.md, context/planning/research_plan_final.md, context/research_context.md.
Fix every issue listed in the CONDITIONAL PASS report.
Update context/model_equations.md in place.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

### Step 3.4c — Model Verifier: Re-check (only if CONDITIONAL PASS)

```
You are running the research pipeline Phase 3, Model Verifier re-check.
Read context/model_equations.md, context/planning/research_plan_final.md, context/research_context.md, and context/planning/task_queue.md.
Use the model-verifier agent. This is a re-check after a correction round.
Write your updated verdict and report to context/model_verifier_report.md (overwrite).
If still CONDITIONAL PASS or FAIL, escalate — write 'ESCALATE TO HUMAN' as the first line.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 3.5 — Research Evaluator: Output Evaluation

**What it does:** Simulates a full referee report on the completed research outputs.

**Files produced:** `context/evaluator_feedback.md`

```
You are running the research pipeline Phase 3, step 5.
Read context/planning/research_plan_final.md, context/literature/threat_map_final.md, context/model_equations.md, and context/model_verifier_report.md.
Read context/research_context.md for scope constraints.
Use the research-evaluator agent in Mode 2 (Output Evaluation).
Simulate a full referee report for the target venue.
Write the full referee simulation to context/evaluator_feedback.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

---

### Step 3.6 — Paper Writer: Academic Writing

**What it does:** Writes all manuscript sections as LaTeX files in four sequential passes (structure, clarity, flow, technical audit).

**Files produced:** `paper/sections/*.tex`

```
You are running the research pipeline Phase 3, step 6.
Read context/planning/paper_structure.md, context/literature/review.md, context/model_equations.md, and context/research_context.md.
Read context/evaluator_feedback.md for referee concerns to address.
Read any existing paper/sections/*.tex files before writing.
Use the academic-writing skill in skills/academic-writing/SKILL.md.
Write all paper sections as .tex files in paper/sections/.
Start with literature.tex (convert literature_review.md to LaTeX).
Then write all remaining sections as defined in context/planning/paper_structure.md.
After completing your task, append a one-line summary to workflow/research-log.md in the format:
- **YYYY-MM-DD HH:MM** [Agent Name] Summary of what was done.
```

**After this step:** Compile with `just render-paper` to verify the LaTeX builds. You may need to add `\input{sections/...}` lines to `paper/main.tex`.

---

## Phase 4: Quality Assurance

Phase 4 uses Claude Code's subagent dispatch. Run these prompts in an interactive session.

### Step 4.1 — Three Self-Review Lenses (parallel)

**What it does:** Three specialist lenses critique the manuscript simultaneously.

**Files produced:** `context/self_reviews/review_theory.md`, `context/self_reviews/review_presentation.md`, `context/self_reviews/review_framing.md`

```
Run three self-review lenses in parallel using the Agent tool:

1. Use the Agent tool with subagent_type "theory-lens":
   Read all paper/sections/*.tex (model sections and conclusion),
   context/model_equations.md (in chunks), and
   context/model_verifier_report.md. Produce context/self_reviews/review_theory.md.

2. Use the Agent tool with subagent_type "presentation-lens":
   Read paper/main.tex and all paper/sections/*.tex. Run wc -w paper/sections/*.tex.
   Produce context/self_reviews/review_presentation.md.

3. Use the Agent tool with subagent_type "framing-lens":
   Read context/literature/threat_map_final.md, context/literature/review.md,
   paper/sections/introduction.tex, paper/sections/literature.tex,
   paper/sections/conclusion.tex, and paper/references.bib.
   Produce context/self_reviews/review_framing.md.
```

---

### Step 4.2 — Research Director: Improvement Synthesis

**What it does:** Reads all three reviews, deduplicates, and produces a prioritised task queue.

**Files produced:** `context/improvement_task_queue.md`

```
Use the Agent tool with subagent_type "research-director" in Mode 4 (Improvement Synthesis).
Read context/self_reviews/review_theory.md, review_presentation.md, and review_framing.md.
Deduplicate, prioritise, and produce context/improvement_task_queue.md.
```

---

### Step 4.3a — Theory Builder: Equation Improvement (skip if no Theory Builder tasks)

**What it does:** Restructures equations, moves proofs to appendix if needed.

```
Use the Agent tool with subagent_type "theory-builder" in Mode 3 (Equation Improvement).
Read .claude/agents/theory-builder.md first. Then read context/improvement_task_queue.md.
Execute only tasks assigned to Theory Builder in priority order.
Mark each task complete in improvement_task_queue.md as you finish it.
```

---

### Step 4.3b — Paper Writer: Improvement Pass

**What it does:** Executes prose, layout, abstract, and framing improvements.

```
Use the Agent tool with subagent_type "paper-writer" in Mode 5 (Improvement Pass).
Read .claude/agents/paper-writer.md first. Then read context/improvement_task_queue.md
and skills/manuscript-layout/SKILL.md.
Execute all tasks assigned to Paper Writer in priority order.
If you encounter an equation-related task you cannot resolve with prose alone, mark it
NEEDS-TB in improvement_task_queue.md and move on — do not block on it.
Mark all other completed tasks in improvement_task_queue.md as you finish them.
```

---

### Step 4.3c — Theory Builder: Follow-up (only if NEEDS-TB tasks exist)

```
Use the Agent tool with subagent_type "theory-builder" in Mode 3 (Equation Improvement).
Read .claude/agents/theory-builder.md first. Then read context/improvement_task_queue.md.
Execute only tasks marked NEEDS-TB. Mark each complete when done.
```

---

### Step 4.4 — Recompile

Run in your terminal:

```bash
just render-paper
```

Verify no fatal errors. Citation and reference warnings are acceptable.

**Loop exit:** If all Priority 1 tasks are resolved, you're done. Otherwise, repeat Phase 4 (max 2 iterations).

---

## After the Pipeline

1. **Compile the final PDF:** `just render-paper`
2. **Review the manuscript** in `paper/sections/*.tex`
3. **Check the research log** in `workflow/research-log.md` for a timeline of what each agent did
4. **Review evaluator feedback** in `context/evaluator_feedback.md` for outstanding concerns
5. **Wire sections into main.tex** — add `\input{sections/...}` lines to `paper/main.tex` if not already done
