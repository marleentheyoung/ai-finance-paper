# AI Finance Paper — Pipeline Infrastructure Map

**Project:** AI Model Homogeneity and Financial Fragility
**Target:** Formal theory paper at JF / RFS / Econometrica standard
**Mapped:** 2026-03-10 · Updated: 2026-03-11 (v5 — directory reorganization, archives/, boundary cleanup)

---

## Directory Structure

```
context/                  # Research content — agents read/write (see context/README.md)
  README.md               # File index grouped by lifecycle
  archives/               # Auto-generated iteration snapshots
    evaluator_feedback_i{N}.md
  referee_reports/        # Phase 4 referee reports (A, B, C)
  *.md                    # All shared state files (inputs, loop state, outputs)

workflow/                 # Pipeline orchestration (see workflow/README.md)
  run_pipeline.sh         # Overnight pipeline runner
  research-log.md         # Append-only process log
```

---

## Overview

The pipeline is a **multi-agent academic paper production system** with three distinct phases:

1. **Pre-loop** — initialise context; produce initial threat map and research plan
2. **Planning loop** — iteratively refine the plan until it passes a quality gate (score ≥ 4.0 on a 1-5 scale, max 5 iterations)
3. **Post-loop** — execute research, verify, write the paper, simulate final referee

Each phase uses a defined set of agents, each agent has bounded responsibilities, and all inter-agent communication happens through shared context files in `context/`.

---

## Pipeline Flowchart

```
┌──────────────────────────────────────────────────────────┐
│                   PHASE 1 — PRE-LOOP                     │
│                                                          │
│  Human provides research_context.md                      │
│         │                                                │
│         ▼                                                │
│  Literature Guardian [Mode 1 — Quick Scan]               │
│  Skill: literature-review-light (web search)             │
│  Input:  context/research_context.md                     │
│  Outputs: context/threat_map_v1.md         (archive)     │
│           context/threat_map.md            (loop copy)   │
│           context/literature_constraints.md (initial)    │
│         │                                                │
│         ▼                                                │
│  Research Director [Mode 1 — Initial Plan]               │
│  Inputs: research_context.md + threat_map_v1.md          │
│  Output: context/research_plan.md                        │
└──────────────────────────┬───────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│              PHASE 2 — PLANNING LOOP                     │
│              (repeat up to 5 iterations)                 │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Research Director [Mode 2 — Plan Revision]       │   │
│  │  Inputs:  research_plan.md (current)              │   │
│  │           threat_map.md (prev iteration)          │   │
│  │           evaluator_feedback.md (prev iteration)  │   │
│  │           research_context.md                     │   │
│  │  Output:  research_plan.md (updated in place)     │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Literature Guardian [Mode 2 — Targeted Check]    │   │
│  │  Skill: literature-review-targeted (web search)   │   │
│  │  Inputs:  research_plan.md (Director's revision)  │   │
│  │           threat_map.md (update in place)         │   │
│  │           research_context.md                     │   │
│  │           literature_constraints.md               │   │
│  │  Outputs: threat_map.md (updated)                 │   │
│  │           literature_constraints.md (updated)     │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Research Evaluator [Mode 1 — Plan Eval]          │   │
│  │  Skill: referee-simulator                         │   │
│  │  Inputs:  research_plan.md, threat_map.md         │   │
│  │           research_context.md                     │   │
│  │           evaluation_criteria.md                  │   │
│  │  Outputs: evaluator_feedback.md                   │   │
│  │           loop_state.md (score + iteration)       │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                  overall_score ≥ 4.0?                    │
│                 /                  \                     │
│               YES                  NO (and iter < 5)    │
│                │                    │                    │
│                │                    └──► loop back       │
└────────────────┼─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│              PHASE 3 — POST-LOOP EXECUTION               │
│                                                          │
│  Step 1: Research Director M3 (Final Program)            │
│  Outputs: research_plan_final.md, paper_structure.md,    │
│           task_queue.md, novelty_claims.md                │
│                     │                                    │
│                     ▼                                    │
│  Step 2: Literature Guardian M3 (Deep Review)  ─────┐   │
│  Outputs: threat_map_final.md, literature_review.md  │   │
│                     │                            parallel │
│                     ▼                                │   │
│  Step 3: Theory Builder M1 (Derive T1-T5)      ─────┘   │
│  Outputs: model_equations.md                             │
│                     │                                    │
│                     ▼                                    │
│  ┌──────────────────────────────────────────────────┐    │
│  │  Step 4: VERIFY-FIX LOOP (max 2 rounds)         │    │
│  │                                                  │    │
│  │  Model Verifier ──► verification_report.md       │    │
│  │       │                                          │    │
│  │  PASS? ──► YES ──► proceed to Step 5             │    │
│  │       │                                          │    │
│  │       NO (critical issues found)                 │    │
│  │       │                                          │    │
│  │  Theory Builder M2 (Verification Fix)            │    │
│  │  ──► fixes model_equations.md in place           │    │
│  │  ──► re-run Model Verifier                       │    │
│  │                                                  │    │
│  │  After 2 failed rounds ──► escalate to human     │    │
│  └──────────────────────────────────────────────────┘    │
│                     │                                    │
│                     ▼                                    │
│  Step 5: Research Evaluator M2 (Output Eval)             │
│  Outputs: evaluator_feedback.md                          │
│                     │                                    │
│                     ▼                                    │
│  ┌──────────────────────────────────────────────────┐    │
│  │  Step 6: PAPER WRITER (four sequential passes)   │    │
│  │                                                  │    │
│  │  Pass 1 — Structure: draft all .tex sections     │    │
│  │           from model_equations.md +              │    │
│  │           literature_review.md +                 │    │
│  │           paper_structure.md                     │    │
│  │                     │                            │    │
│  │  Pass 2 — Clarity: simplify prose, break long    │    │
│  │           sentences, remove hedging              │    │
│  │                     │                            │    │
│  │  Pass 3 — Flow: transitions, narrative arc,      │    │
│  │           paragraph rhythm, safety illusion      │    │
│  │           corollary as climax                    │    │
│  │                     │                            │    │
│  │  Pass 4 — Technical audit: verify all equations, │    │
│  │           citations, cross-refs against source   │    │
│  │           files; produce technical_audit.md      │    │
│  │                                                  │    │
│  │  Outputs: paper/sections/*.tex (9 files)         │    │
│  │           context/technical_audit.md             │    │
│  └──────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│           PHASE 4 — MANUSCRIPT REVISION LOOP             │
│           (max 2 iterations)                             │
│                                                          │
│  Step 1: Three Referees IN PARALLEL                      │
│    ├── referee-A-theory    → context/referee_reports/    │
│    ├── referee-B-presentation                report_A.md │
│    └── referee-C-literature                  report_B.md │
│                                              report_C.md │
│                          │                              │
│                          ▼                              │
│  Step 2: Research Director [Mode 4 — Revision Synthesis] │
│    Reads reports A+B+C → deduplicates → prioritises      │
│    Output: context/revision_task_queue.md                │
│                          │                              │
│                          ▼                              │
│  Step 3: Execute revision tasks by assignee              │
│    ├── paper-writer [Mode 5 — Revision Pass]             │
│    │   (prose, layout, abstract, framing)                │
│    └── theory-builder [Mode 3 — Restructure] (if needed) │
│        (move proofs to appendix, restructure equations)  │
│                          │                              │
│                          ▼                              │
│  Step 4: Recompile → just render-paper                   │
│          Verify: no new LaTeX errors                     │
│                          │                              │
│              all P1 tasks resolved?                      │
│            YES → exit  │  NO (iter < 2) → loop back     │
└──────────────────────────────────────────────────────────┘
```

---

## Phase 4 — Pipeline Commands

Each step maps to a single agent invocation. Run them in this order.

### Step 1 — Three referees in parallel (single message, three Agent calls)

```
Use the Agent tool with subagent_type "referee-A-theory":
  Read all paper/sections/*.tex (model, channel1, channel2, channel3, amplification,
  extensions, conclusion), context/model_equations.md (in chunks), and
  context/verification_report.md. Produce context/referee_reports/report_A.md.
  Today's date is [DATE].

Use the Agent tool with subagent_type "referee-B-presentation":
  Read paper/main.tex and all paper/sections/*.tex. Run wc -w paper/sections/*.tex.
  Produce context/referee_reports/report_B.md.
  Today's date is [DATE].

Use the Agent tool with subagent_type "referee-C-literature":
  Read context/threat_map_final.md, context/literature_review.md,
  paper/sections/introduction.tex, paper/sections/literature.tex,
  paper/sections/conclusion.tex, and paper/references.bib.
  Produce context/referee_reports/report_C.md.
  Today's date is [DATE].
```

### Step 2 — Research Director synthesis

```
Use the Agent tool with subagent_type "research-director" in Mode 4 (Revision Synthesis).
Read context/referee_reports/report_A.md, report_B.md, and report_C.md.
Deduplicate, prioritise, and produce context/revision_task_queue.md.
Today's date is [DATE].
```

### Step 3a — Theory Builder restructure pass (skip if no Theory Builder tasks in queue)

Run this BEFORE Paper Writer so Paper Writer sees the restructured equations.

```
Use the Agent tool with subagent_type "theory-builder" in Mode 3 (Equation Restructuring).
Read .claude/agents/theory-builder.md first. Then read context/revision_task_queue.md.
Execute only tasks assigned to Theory Builder in priority order.
Mark each task complete in revision_task_queue.md as you finish it.
Today's date is [DATE].
```

### Step 3b — Paper Writer revision pass

```
Use the Agent tool with subagent_type "paper-writer" in Mode 5 (Revision Pass).
Read .claude/agents/paper-writer.md first. Then read context/revision_task_queue.md
and skills/manuscript-layout/SKILL.md.
Execute all tasks assigned to Paper Writer in priority order.
If you encounter an equation-related task you cannot resolve with prose alone, mark it
NEEDS-TB in revision_task_queue.md and move on — do not block on it.
Mark all other completed tasks in revision_task_queue.md as you finish them.
Today's date is [DATE].
```

### Step 3c — Theory Builder follow-up (only if any tasks were marked NEEDS-TB in Step 3b)

```
Use the Agent tool with subagent_type "theory-builder" in Mode 3 (Equation Restructuring).
Read .claude/agents/theory-builder.md first. Then read context/revision_task_queue.md.
Execute only tasks marked NEEDS-TB. Mark each complete when done.
Today's date is [DATE].
```

### Step 4 — Recompile

```
Run: just render-paper
Verify: no Fatal errors in output. Citation and reference warnings are acceptable.
```

---

## Sequence Tables

### Phase 2 — Planning Loop (per iteration)

| Step | Agent | Action | Key files written |
|------|-------|--------|-------------------|
| 1 | Research Director M2 | Revise plan using prior threat map + prior evaluator feedback | `research_plan.md` |
| 2 | Literature Guardian M2 | Check the Director's revision; update threat map | `threat_map.md`, `literature_constraints.md` |
| 3 | Research Evaluator M1 | Score the revised plan against the updated threat map | `evaluator_feedback.md`, `loop_state.md` |

On iteration 1, `evaluator_feedback.md` does not yet exist; the Director revises using the threat map and research context only.

### Phase 3 — Post-Loop Execution (fixed sequence)

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 1 | Research Director M3 | Consolidate plan; produce novelty claims | `research_plan_final.md`, `paper_structure.md`, `task_queue.md`, `novelty_claims.md` | None |
| 2 | Literature Guardian M3 | Deep review; verify novelty claims | `threat_map_final.md`, `literature_review.md`, `literature_notes.md` | Step 1 |
| 3 | Theory Builder M1 | Derive models T1-T5 (can run parallel with Step 2) | `model_equations.md` | Step 1 |
| 4a | Model Verifier | Verify propositions, run SymPy checks | `verification_report.md` | Step 3 |
| 4b | Theory Builder M2 | Fix critical issues if any (max 2 rounds back to 4a) | `model_equations.md` (edited) | Step 4a (if issues found) |
| 5 | Research Evaluator M2 | Full referee simulation on completed outputs | `evaluator_feedback.md` | Steps 2, 4 |
| 6a | Paper Writer Pass 1 | Structure draft: all content into LaTeX | `paper/sections/*.tex` | Steps 2, 4, 5 |
| 6b | Paper Writer Pass 2 | Clarity edit: simplify prose | `paper/sections/*.tex` (edited) | Step 6a |
| 6c | Paper Writer Pass 3 | Flow and voice: transitions, narrative arc | `paper/sections/*.tex` (edited) | Step 6b |
| 6d | Paper Writer Pass 4 | Technical audit: verify equations, citations, cross-refs | `paper/sections/*.tex` (edited), `technical_audit.md` | Step 6c |

**Steps 2 and 3 run in parallel** (Literature Guardian and Theory Builder write to different files).

**Step 4 verify-fix loop:** Model Verifier checks `model_equations.md`. If critical issues are found, Theory Builder M2 fixes them and the Verifier re-checks. Maximum 2 rounds. After 2 failed rounds, escalate to human.

**Step 6 four-pass sequence:** Each pass reads the output of the previous pass. Passes are never combined or run in parallel.

### Phase 4 — Manuscript Revision Loop (per iteration, max 2)

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 1a | referee-A-theory | Review math presentation; flag equation density, notation, proof quality | `referee_reports/report_A.md` | Phase 3 complete |
| 1b | referee-B-presentation | Review layout; flag abstract, section balance, paragraph structure | `referee_reports/report_B.md` | Phase 3 complete |
| 1c | referee-C-literature | Review framing; flag differentiators, citations, positioning | `referee_reports/report_C.md` | Phase 3 complete |
| 2 | Research Director M4 | Synthesise all three reports into a prioritised task queue | `revision_task_queue.md` | Steps 1a, 1b, 1c |
| 3a | Theory Builder M3 | Restructure equations, move proofs to appendix (skip if no TB tasks) | `paper/sections/*.tex` (edited), `paper/appendix.tex` (if created) | Step 2 |
| 3b | Paper Writer M5 | Execute all Paper Writer tasks; mark NEEDS-TB for any equation task it cannot resolve alone | `paper/sections/*.tex` (edited), `revision_task_queue.md` (updated) | Step 3a |
| 3c | Theory Builder M3 | Follow-up on any tasks marked NEEDS-TB by Paper Writer (skip if none) | `paper/sections/*.tex` (edited) | Step 3b |
| 4 | (shell) | `just render-paper` — verify no fatal errors | `paper/main.pdf` | Steps 3b, 3c |

**Steps 1a, 1b, 1c run in parallel** — launch all three in a single message using three Agent tool calls.
**Steps 3a → 3b → 3c are sequential.** Theory Builder restructures first so Paper Writer sees the final equation layout. Paper Writer can escalate back to Theory Builder via NEEDS-TB flags.
**Loop exit:** All Priority 1 tasks resolved, or maximum 2 iterations reached.

---

## Agent Catalogue

### 1. Literature Guardian

| Property | Detail |
|----------|--------|
| Role | Novelty risk analyst and literature mapper |
| Modes | 3 (Quick Scan → Targeted → Deep Review) |
| Skills | `literature-review-light`, `literature-review-targeted`, `literature-review-deep` |
| Does NOT | Design the research plan, score plans, write paper sections, produce LaTeX |

**Mode summary:**

| Mode | When | Input | Output |
|------|------|-------|--------|
| 1 — Quick Scan | Project start | `research_context.md` | `threat_map_v1.md`, `threat_map.md` (copy), `literature_constraints.md` (initial), `search_log.md` (initial) |
| 2 — Targeted | After Director M2 each iteration | Director's revised `research_plan.md`, `threat_map.md`, `research_context.md`, `literature_constraints.md`, `search_log.md` | `threat_map.md` (updated), `literature_constraints.md` (updated), `search_log.md` (appended) |
| 3 — Deep Review | Post-loop Step 2, after Director M3 | `research_context.md`, `threat_map.md`, `literature_notes.md`, `novelty_claims.md`, `search_log.md` | `threat_map_final.md`, `literature_notes.md`, `literature_constraints.md`, `literature_review.md`, `search_log.md` (appended) |

---

### 2. Research Director

| Property | Detail |
|----------|--------|
| Role | Principal investigator — strategic planning and task decomposition |
| Modes | 3 (Initial Plan → Revision → Final Program) |
| Does NOT | Search literature, derive models, verify math, write paper sections, score plans |

**Mode summary:**

| Mode | When | Input | Output |
|------|------|-------|--------|
| 1 — Initial Plan | Project start (after quick scan) | `research_context.md`, `threat_map_v1.md` | `research_plan.md` (new) |
| 2 — Plan Revision | Start of each loop iteration | `research_plan.md`, `threat_map.md` (prev iter), `evaluator_feedback.md` (current) + `evaluator_feedback_i{N}.md` (all prior archives), `research_context.md` | `research_plan.md` (updated) |
| 3 — Final Program | Post-loop Step 1 | `research_plan.md`, `threat_map.md` (accumulated), `research_context.md` | `research_plan_final.md`, `paper_structure.md`, `task_queue.md`, `novelty_claims.md` |

**Conflict priority rule (Mode 2):**
1. Hard failure conditions take absolute precedence
2. New HIGH threats override evaluator directives to expand that contribution
3. Evaluator directives apply after MODERATE threats are resolved
4. Scope constraints override both

---

### 3. Research Evaluator

| Property | Detail |
|----------|--------|
| Role | Skeptical co-author and early referee — scores plans and outputs |
| Modes | 2 (Plan Evaluation → Output Evaluation) |
| Skill | `referee-simulator` |
| Does NOT | Revise plans, search literature, build models, write the paper |

**Scoring rubric (Mode 1) — 1-5 integer scale, 7 criteria:**

| Criterion | Role in formula |
|-----------|----------------|
| Novelty | Core floor |
| Mechanism Clarity | Core floor |
| Theoretical Feasibility | Core floor |
| Literature Positioning | Mean component |
| Expected Contribution | Mean component |
| Testability | Mean component |
| Scope Calibration | Mean component |

`overall_score = min(novelty, mechanism_clarity, feasibility) × 0.6 + mean(all_seven) × 0.4`

**Hard failures (force REJECT):** Novelty ≤ 2, Mechanism Clarity ≤ 2, or Theoretical Feasibility ≤ 2.

**Mode summary:**

| Mode | When | Input | Output |
|------|------|-------|--------|
| 1 — Plan Eval | After Guardian M2 each iteration | `research_plan.md`, `threat_map.md`, `research_context.md`, `evaluation_criteria.md` | `evaluator_feedback.md`, `loop_state.md` |
| 2 — Output Eval | Post-loop Step 5 (after Model Verifier) | `research_plan_final.md`, `threat_map_final.md`, `model_equations.md`, `verification_report.md` | `evaluator_feedback.md` |

---

### 4. Theory Builder

| Property | Detail |
|----------|--------|
| Role | Formal model development and equilibrium derivation |
| Modes | 2 (Initial Derivation → Verification Fix) |
| Skill | `economic-model-builder` |
| Phase | Post-loop Step 3 (M1) and Step 4b (M2, if verification issues found) |
| Outputs | `model_equations.md` — **formal content only; no `.tex` files** |
| Does NOT | Produce LaTeX; evaluate quality; write prose |

**Mode summary:**

| Mode | When | Input | Output |
|------|------|-------|--------|
| 1 — Initial Derivation | Post-loop Step 3 | `research_plan_final.md`, `task_queue.md`, `research_context.md`, `model_equations.md` (if prior work exists) | `model_equations.md` |
| 2 — Verification Fix | After Model Verifier flags critical issues | `verification_report.md`, `model_equations.md`, `research_context.md` | `model_equations.md` (edited in place, changelog appended) |

**Mode 2 rules:** Fix only what the verifier flagged. Do not rederive passing propositions. Do not add new results. Do not restructure the document. Append a changelog.

**Task sequence (Mode 1):** T1 (Channel 1) → T2 (Channel 2) → T3 (Channel 3) → T4 (Amplification Loop) → T5 (Extensions). Channels 1-3 can run in a single session. T4 blocks on T1-T3. T5 blocks on T4.

---

### 5. Empirical Agent

| Property | Detail |
|----------|--------|
| Role | Dataset assembly and empirical analysis |
| Skill | `empirical-design` *(SKILL.md is currently a stub)* |
| Phase | Post-loop (parallel with Theory Builder) |
| Inputs | `research_plan_final.md`, `task_queue.md`, model predictions, `code/`, `data/` |
| Outputs | Clean datasets, regression summaries, `paper/figures/`, `paper/tables/` |
| Status | **Deferred** — empirical section can be added after initial manuscript draft |

**Empirical design:** DiD using ChatGPT release (Nov 2022) as AI adoption shock; ρ proxied via 13F portfolio correlation and I/B/E/S forecast revision correlation. Motivating only — not causal identification.

---

### 6. Model Verifier

| Property | Detail |
|----------|--------|
| Role | Mathematical auditor — verifies derivation integrity, proposition correctness, and scope compliance |
| Phase | Post-loop Step 4 (after Theory Builder; before Evaluator M2 and Paper Writer) |
| Inputs | `model_equations.md`, `research_plan_final.md`, `research_context.md` |
| Outputs | `verification_report.md`, `code/verification/*.py` (SymPy scripts) |
| Does NOT | Derive new results; revise the plan; write prose; fix errors (that is Theory Builder M2's job) |

**Verification workflow:**
1. Structural audit (notation, completeness, variable definitions)
2. Proposition verification (statement, assumptions, proof logic, direction)
3. Computational verification (SymPy scripts for equilibrium conditions and comparative statics)
4. Cross-channel consistency (fixed-point well-definedness, Brouwer conditions)
5. Scope compliance (no dynamics, ρ exogenous in main model)
6. Plan alignment (each contribution has a corresponding proposition)

**Verdicts:** PASS (proceed), CONDITIONAL PASS (Theory Builder M2 fixes, max 2 rounds), FAIL (escalate to human).

---

### 7. Paper Writer

| Property | Detail |
|----------|--------|
| Role | Converts all research outputs into publication-quality LaTeX manuscript |
| Modes | 4 sequential passes (Structure → Clarity → Flow → Technical Audit) |
| Skill | `academic-writing` |
| Phase | Post-loop Step 6 (final step) |
| Inputs | `paper_structure.md`, `literature_review.md`, `model_equations.md`, `threat_map_final.md`, `evaluator_feedback.md`, `paper/figures/`, `paper/tables/` |
| Outputs | `paper/sections/*.tex` (9 files), `context/technical_audit.md` |
| Does NOT | Derive models; search literature; invent results |

**Four-pass structure:**

| Pass | Objective | Edits content? | Edits style? |
|------|-----------|----------------|--------------|
| 1 — Structure | Get all content into LaTeX with correct structure, propositions, citations | Yes | No |
| 2 — Clarity | Simplify prose, break long sentences, remove hedging and jargon | No | Yes |
| 3 — Flow | Transitions between sections, narrative arc, paragraph rhythm, voice | No | Yes |
| 4 — Technical Audit | Verify equations, citations, cross-references against source files | Corrections only | No |

**Pass rules:** Passes are strictly sequential. Each reads the output of the previous. Never combined or parallelised. Pass 1 creates; Passes 2-3 refine; Pass 4 verifies.

**Target sections:**
```
introduction.tex    → contribution framing; threat map differentiators
literature.tex      → converted from literature_review.md
model.tex           → primitives, timing, equilibrium definition
channel1.tex        → coordination failure; θ*(ρ)
channel2.tex        → information acquisition; GS extension
channel3.tex        → market making; N_eff(ρ)
amplification.tex   → fixed-point; safety illusion corollary
extensions.tex      → endogenous ρ; diversity mandate
conclusion.tex      → policy implications; future work
```

---

### 8. Referee A — Theory and Rigor

| Property | Detail |
|----------|--------|
| Role | Mathematical presentation reviewer — equation density, notation, proof quality |
| Phase | Phase 4 Step 1a (parallel with B and C) |
| Color | Purple |
| Inputs | `paper/sections/*.tex` (model through conclusion), `model_equations.md`, `verification_report.md` |
| Outputs | `context/referee_reports/report_A.md` |
| Does NOT | Fix issues; re-derive math; edit `.tex` files |

---

### 9. Referee B — Presentation and Layout

| Property | Detail |
|----------|--------|
| Role | Layout and formatting reviewer — abstract, section balance, equation density, LaTeX conventions |
| Phase | Phase 4 Step 1b (parallel with A and C) |
| Color | Blue |
| Inputs | `paper/main.tex`, all `paper/sections/*.tex` |
| Outputs | `context/referee_reports/report_B.md` |
| Does NOT | Fix issues; rewrite abstract; edit `.tex` files |

---

### 10. Referee C — Literature and Framing

| Property | Detail |
|----------|--------|
| Role | Framing and citation reviewer — differentiator accuracy, positioning, citation coverage |
| Phase | Phase 4 Step 1c (parallel with A and B) |
| Color | Green |
| Inputs | `context/threat_map_final.md`, `context/literature_review.md`, introduction, literature, conclusion sections, `references.bib` |
| Outputs | `context/referee_reports/report_C.md` |
| Does NOT | Fix issues; search for new papers; edit `.tex` files |

---

### 11. Memory Manager

| Property | Detail |
|----------|--------|
| Role | Cross-session state management *(stub — agent file exists but contains no instructions)* |
| Status | Not needed for single-session runs; needed if pipeline spans multiple days |

---

## Context File Registry

| File | Written by | Read by | Purpose |
|------|-----------|---------|---------|
| `research_context.md` | Human (permanent) | All agents | Research spec, ρ primitive, 3 channels, scope constraints |
| `threat_map_v1.md` | Lit. Guardian M1 | Research Director M1 | Versioned initial threat map (archive) |
| `threat_map.md` | Lit. Guardian M1 (copy), M2 (updates) | Dir. M2, Guardian M2, Evaluator M1 | Accumulated threat map with changelogs |
| `threat_map_final.md` | Lit. Guardian M3 | Evaluator M2, Paper Writer | Definitive, clean threat map |
| `literature_notes.md` | Lit. Guardian M3 | Paper Writer | Structured paper summaries |
| `literature_constraints.md` | Lit. Guardian M1/M2/M3 | Lit. Guardian M2, Research Director | What the literature has and has not addressed |
| `literature_review.md` | Lit. Guardian M3 | Paper Writer | Prose literature review for LaTeX conversion |
| `research_plan.md` | Research Director M1/M2 | All agents in loop | Current research plan with changelog |
| `research_plan_final.md` | Research Director M3 | Theory Builder, Evaluator M2, Paper Writer | Definitive research plan |
| `task_queue.md` | Research Director M3 (once) | Theory Builder, Empirical Agent | Executable task queue with dependencies |
| `paper_structure.md` | Research Director M3 | Paper Writer | Section-by-section paper map |
| `novelty_claims.md` | Research Director M3 | Lit. Guardian M3 | Contributions list for verification |
| `evaluator_feedback.md` | Evaluator M1/M2 | Research Director M2 | Current iteration's scored critique and revision directives |
| `archives/evaluator_feedback_i{N}.md` | Pipeline (archived copy) | Research Director M2 | Archived evaluator feedback from iteration N; prevents amnesia across loop iterations |
| `search_log.md` | Lit. Guardian M1/M2/M3 | Lit. Guardian M2/M3 | Persistent search query log to prevent duplicate literature searches |
| `phase_state.md` | Pipeline shell script | All agents | Current pipeline phase, step, and timestamp for agent orientation |
| `loop_state.md` | Evaluator M1 | Loop controller | Iteration counter, score (1-5), threshold (4.0) |
| `evaluation_criteria.md` | Human (permanent) | Evaluator M1 | 7-criterion scoring rubric |
| `model_equations.md` | Theory Builder M1/M2 | Model Verifier, Evaluator M2, Paper Writer | Formal derivations and propositions |
| `verification_report.md` | Model Verifier | Theory Builder M2, Evaluator M2 | Verification results, SymPy output, verdicts |
| `technical_audit.md` | Paper Writer Pass 4 | Human | Final manuscript consistency check |
| `referee_reports/report_A.md` | Referee A | Research Director M4 | Theory and rigor review |
| `referee_reports/report_B.md` | Referee B | Research Director M4 | Presentation and layout review |
| `referee_reports/report_C.md` | Referee C | Research Director M4 | Literature and framing review |
| `revision_task_queue.md` | Research Director M4 | Paper Writer M5, Theory Builder M3 | Prioritised revision tasks with acceptance criteria |

---

## Agent Catalogue (summary)

| Agent | Modes | Skills | Phase |
|-------|-------|--------|-------|
| Literature Guardian | 3 (Quick Scan, Targeted, Deep) | `lit-review-light`, `lit-review-targeted`, `lit-review-deep` | 1, 2, 3 |
| Research Director | 3 (Initial, Revision, Final) | — | 1, 2, 3 |
| Research Evaluator | 2 (Plan Eval, Output Eval) | `referee-simulator` | 2, 3 |
| Theory Builder | 2 (Initial Derivation, Verification Fix) | `economic-model-builder` | 3 |
| Model Verifier | 1 (Verify) | — | 3 |
| Paper Writer | 4 passes (Structure, Clarity, Flow, Technical) | `academic-writing` | 3 |
| Empirical Agent | 1 (deferred) | `empirical-design` (stub) | 3 |

---

## Skill Catalogue

| Skill | Used by | Purpose | Web search? |
|-------|---------|---------|------------|
| `literature-review-light` | Lit. Guardian M1 | Fast threat identification | Yes |
| `literature-review-targeted` | Lit. Guardian M2 | Per-iteration check of new claims | Yes |
| `literature-review-deep` | Lit. Guardian M3 | Exhaustive final review | Yes |
| `referee-simulator` | Evaluator M1 + M2 | Simulate referee report | No |
| `economic-model-builder` | Theory Builder | 6-step model derivation workflow | No |
| `academic-writing` | Paper Writer | LaTeX conversion, style rules, citation conventions | No |
| `empirical-design` | Empirical Agent | Dataset assembly and regressions *(stub)* | No |

---

## Loop Exit Logic

```
loop_state.md tracks:
  iteration:     current iteration number (starts at 0)
  current_score: evaluator's overall_score (1-5 scale)
  threshold:     4.0
  history:       table of all past scores

EXIT conditions (OR):
  current_score >= 4.0
  iteration == 5 (max iterations reached)

On EXIT → proceed to Phase 3
```

---

## Key Architectural Constraints

1. **ρ is exogenous** in the main model (endogenous only in prisoner's dilemma extension)
2. **Static or two-period model only** — no full dynamic model
3. **Channel sequencing:** Channels 1-3 before the amplification loop
4. **Amplification loop is non-negotiable core** — deprioritising it scores ≤ 3 on Expected Contribution
5. **Empirical section is motivating, not causal**
6. **Novelty at mechanism level** — topic overlap is not a threat; the formal mechanism must match
7. **Theory Builder produces no LaTeX** — Paper Writer converts all content
8. **Verification before writing** — Model Verifier must pass before Paper Writer begins
9. **Four-pass writing** — passes are sequential and never combined

---

## Infrastructure Status

| Item | Status |
|------|--------|
| `literature-guardian.md` | Complete (3 modes) |
| `research-director.md` | Complete (3 modes) |
| `research-evaluator.md` | Complete (2 modes) |
| `theory-builder.md` | Complete (2 modes: derivation + verification fix) |
| `model-verifier.md` | Complete (SymPy verification workflow) |
| `paper-writer.md` | Complete (4-pass sequential structure) |
| `empirical-design/SKILL.md` | Stub — deferred |
| `memory-manager.md` | Stub — not needed for single-session runs |
| `evaluate-plan/` | Superseded by `referee-simulator` — delete |

---

## Data Flow Summary (Single Loop Iteration)

```
                    ┌─────────────────────────────┐
                    │   research_context.md        │ (permanent)
                    └──────────┬──────────────────┘
                               │ (read by all)
                               ▼
  evaluator_feedback.md ──► Research Director M2 ──► research_plan.md (revised)
  (current + all archived                  │
   evaluator_feedback_i{N}.md)             │
  threat_map.md                            │
  (previous iteration)                     │
                                    ▼
                         Literature Guardian M2 ──► threat_map.md (updated)
                                                    literature_constraints.md (updated)
                                    │
                                    ▼
                         Research Evaluator M1 ──► evaluator_feedback.md
                                                   loop_state.md
                                    │
                          overall_score ≥ 4.0?
                          YES → Phase 3  |  NO → next iteration
```

## Data Flow Summary (Phase 3 Post-Loop)

```
  research_plan.md ──► Director M3 ──► research_plan_final.md
  threat_map.md                        paper_structure.md
                                       task_queue.md
                                       novelty_claims.md
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                    Lit. Guardian M3           Theory Builder M1
                              │                         │
                    literature_review.md      model_equations.md
                    threat_map_final.md                  │
                              │                         ▼
                              │               Model Verifier ──► verification_report.md
                              │                    │
                              │              PASS? ─┬─ NO → Theory Builder M2 → re-verify
                              │                     │
                              │                    YES
                              │                     │
                              └─────────┬───────────┘
                                        ▼
                              Research Evaluator M2 ──► evaluator_feedback.md
                                        │
                                        ▼
                              Paper Writer (4 passes) ──► paper/sections/*.tex
                                                          technical_audit.md
```
