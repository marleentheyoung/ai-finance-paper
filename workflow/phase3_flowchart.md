# Phase 3: Post-Loop Execution — Pipeline Flowchart

## Overview

Phase 3 executes the research program produced by the planning loop. It runs
once, in a fixed sequence: finalise the plan, conduct the deep literature
review, derive the model, verify it, evaluate the outputs, and write the paper.

**Agents involved:** Research Director (M3), Literature Guardian (M3), Theory Builder (M1, M2), Model Verifier, Research Evaluator (M2), Paper Writer (M1–M4)

---

## Flowchart

```
┌──────────────────────────────────────────────────────────┐
│              PHASE 3 — POST-LOOP EXECUTION               │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 3.1: Research Director [M3 — Final Program] │   │
│  │  Inputs: planning/research_plan.md                │   │
│  │          literature/threat_map.md                  │   │
│  │          research_context.md                      │   │
│  │          literature/constraints.md                │   │
│  │          evaluator_feedback.md (if present)       │   │
│  │  Outputs: planning/research_plan_final.md         │   │
│  │           planning/paper_structure.md             │   │
│  │           planning/task_queue.md                  │   │
│  │           planning/novelty_claims.md              │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 3.2: Literature Guardian [M3 — Deep Review] │   │
│  │  Skill: literature-review/deep (web search)       │   │
│  │  Inputs: research_context.md                      │   │
│  │          literature/threat_map.md                  │   │
│  │          planning/novelty_claims.md               │   │
│  │          planning/research_plan_final.md          │   │
│  │          literature/notes.md (if present)         │   │
│  │          literature/search_log.md (if present)    │   │
│  │          literature/constraints.md (if present)   │   │
│  │  Outputs: literature/threat_map_final.md          │   │
│  │           literature/notes.md (updated)           │   │
│  │           literature/constraints.md (finalised)   │   │
│  │           literature/review.md                    │   │
│  │           literature/search_log.md (appended)     │   │
│  │                                             can be│   │
│  └──────────────────────┬──────────────────── parallel│  │
│                         │                            │   │
│                         ▼                            │   │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 3.3: Theory Builder [M1 — Initial Deriv.]   │   │
│  │  Inputs: planning/research_plan_final.md          │   │
│  │          planning/task_queue.md                   │   │
│  │          research_context.md                      │   │
│  │          model_equations.md (if prior work exists)│   │
│  │  Output: model_equations.md                      │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌──────────────────────────────────────────────────┐    │
│  │  Step 3.4: VERIFY-FIX LOOP (max 1 fix round)    │    │
│  │                                                  │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  Step 3.4a: Model Verifier               │    │    │
│  │  │  Inputs: model_equations.md              │    │    │
│  │  │          planning/research_plan_final.md │    │    │
│  │  │          research_context.md             │    │    │
│  │  │          planning/task_queue.md          │    │    │
│  │  │  Output: model_verifier_report.md        │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │              verdict?                            │    │
│  │             /   |   \                            │    │
│  │          PASS  COND  FAIL                        │    │
│  │           │   PASS    │                          │    │
│  │           │    │      └──► escalate to human     │    │
│  │           │    ▼                                 │    │
│  │           │  ┌──────────────────────────────┐    │    │
│  │           │  │  Step 3.4b: Theory Builder   │    │    │
│  │           │  │  [M2 — Verification Fix]     │    │    │
│  │           │  │  Inputs: model_verifier_     │    │    │
│  │           │  │          report.md            │    │    │
│  │           │  │          model_equations.md  │    │    │
│  │           │  │          research_context.md │    │    │
│  │           │  │  Output: model_equations.md  │    │    │
│  │           │  │          (edited in place)   │    │    │
│  │           │  └──────────────┬───────────────┘    │    │
│  │           │                 │                    │    │
│  │           │                 ▼                    │    │
│  │           │  ┌──────────────────────────────┐    │    │
│  │           │  │  Step 3.4c: Model Verifier   │    │    │
│  │           │  │  (Re-check)                  │    │    │
│  │           │  │  Output: model_verifier_     │    │    │
│  │           │  │          report.md (overwrite)│    │    │
│  │           │  └──────────────┬───────────────┘    │    │
│  │           │                 │                    │    │
│  │           │          still failing?              │    │
│  │           │          YES → escalate to human     │    │
│  │           │          NO  ──┐                     │    │
│  │           │                │                     │    │
│  └───────────┴────────────────┘─────────────────────┘    │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 3.5: Research Evaluator [M2 — Output Eval]  │   │
│  │  Inputs: planning/research_plan_final.md          │   │
│  │          literature/threat_map_final.md            │   │
│  │          model_equations.md                       │   │
│  │          model_verifier_report.md                  │   │
│  │          research_context.md                      │   │
│  │  Output: evaluator_feedback.md                    │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌──────────────────────────────────────────────────┐    │
│  │  Step 3.6: PAPER WRITER (four sequential passes) │    │
│  │                                                  │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  Pass 1 — Structure                      │    │    │
│  │  │  Draft all .tex sections from:           │    │    │
│  │  │    planning/paper_structure.md            │    │    │
│  │  │    literature/review.md                  │    │    │
│  │  │    model_equations.md                    │    │    │
│  │  │    planning/research_plan_final.md       │    │    │
│  │  │    literature/threat_map_final.md        │    │    │
│  │  │    research_context.md                   │    │    │
│  │  │  Skill: academic-writing                 │    │    │
│  │  │  Output: paper/sections/*.tex            │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │                     ▼                            │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  Pass 2 — Clarity                        │    │    │
│  │  │  Simplify prose, break long sentences,   │    │    │
│  │  │  remove hedging and jargon               │    │    │
│  │  │  Output: paper/sections/*.tex (edited)   │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │                     ▼                            │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  Pass 3 — Flow and Voice                 │    │    │
│  │  │  Transitions, narrative arc, paragraph   │    │    │
│  │  │  rhythm, main result as climax           │    │    │
│  │  │  Output: paper/sections/*.tex (edited)   │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │                     ▼                            │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  Pass 4 — Technical Audit                │    │    │
│  │  │  Verify equations, citations, cross-refs │    │    │
│  │  │  against model_equations.md and          │    │    │
│  │  │  threat_map_final.md                     │    │    │
│  │  │  Outputs: paper/sections/*.tex (edited)  │    │    │
│  │  │           context/technical_audit.md     │    │    │
│  │  └──────────────────────────────────────────┘    │    │
│  │                                                  │    │
│  └──────────────────────────────────────────────────┘    │
│                         │                                │
└─────────────────────────┼────────────────────────────────┘
                          │
                          ▼
                    ── Phase 4 ──
```

---

## Sequence Table

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 3.1 | Research Director M3 | Consolidate plan; produce novelty claims | `research_plan_final.md`, `paper_structure.md`, `task_queue.md`, `novelty_claims.md` | None |
| 3.2 | Literature Guardian M3 | Deep review; verify novelty claims | `threat_map_final.md`, `review.md`, `notes.md`, `constraints.md` | Step 3.1 |
| 3.3 | Theory Builder M1 | Derive formal results | `model_equations.md` | Step 3.1 |
| 3.4a | Model Verifier | Verify propositions, run computational checks | `model_verifier_report.md`, `code/verification/*.py` | Step 3.3 |
| 3.4b | Theory Builder M2 | Fix critical issues (only if CONDITIONAL PASS) | `model_equations.md` (edited) | Step 3.4a |
| 3.4c | Model Verifier | Re-check after fixes (only if 3.4b ran) | `model_verifier_report.md` (overwrite) | Step 3.4b |
| 3.5 | Research Evaluator M2 | Full quality assessment; simulated referee report | `evaluator_feedback.md` | Steps 3.2, 3.4 |
| 3.6a | Paper Writer Pass 1 | Structure draft: all content into LaTeX | `paper/sections/*.tex` | Steps 3.2, 3.4, 3.5 |
| 3.6b | Paper Writer Pass 2 | Clarity edit: simplify prose | `paper/sections/*.tex` (edited) | Step 3.6a |
| 3.6c | Paper Writer Pass 3 | Flow and voice: transitions, narrative arc | `paper/sections/*.tex` (edited) | Step 3.6b |
| 3.6d | Paper Writer Pass 4 | Technical audit: verify equations, citations, cross-refs | `paper/sections/*.tex` (edited), `technical_audit.md` | Step 3.6c |

**Steps 3.2 and 3.3 can run in parallel** (they write to different files) but are run sequentially in the default pipeline.

**Step 3.4 verify-fix loop:** Model Verifier checks `model_equations.md`. If critical issues found, Theory Builder M2 fixes them and the Verifier re-checks. Maximum 1 fix round (verify → fix → re-verify → escalate if still failing).

**Step 3.6 four-pass sequence:** Each pass reads the output of the previous pass. Passes are never combined or run in parallel.

---

## Step-by-step detail

### Step 3.1 — Research Director M3 (Final Program)

| | |
|---|---|
| **Agent** | Research Director, Mode 3 |
| **Reads** | `context/planning/research_plan.md`, `context/literature/threat_map.md`, `context/research_context.md`, `context/literature/constraints.md`, `context/evaluator_feedback.md` (if present) |
| **Produces** | `context/planning/research_plan_final.md`, `context/planning/paper_structure.md`, `context/planning/task_queue.md`, `context/planning/novelty_claims.md` |

Consolidates the iteratively refined plan into a definitive research program.
Produces the paper structure map (section-by-section blueprint for the Paper
Writer), a task queue with dependencies for the Theory Builder, and an explicit
list of novelty claims for the Literature Guardian to verify.

---

### Step 3.2 — Literature Guardian M3 (Deep Review)

| | |
|---|---|
| **Agent** | Literature Guardian, Mode 3 |
| **Skill** | `.claude/skills/literature-review/deep/SKILL.md` |
| **Reads** | `context/research_context.md`, `context/literature/threat_map.md`, `context/planning/novelty_claims.md`, `context/planning/research_plan_final.md`, `context/literature/notes.md` (if present), `context/literature/search_log.md` (if present), `context/literature/constraints.md` (if present) |
| **Produces** | `context/literature/threat_map_final.md`, `context/literature/notes.md`, `context/literature/constraints.md`, `context/literature/review.md`, `context/literature/search_log.md` (appended) |

Exhaustive literature review. Consolidates all prior threat map versions into a
clean final document. Verifies every novelty claim. Writes the prose literature
review for conversion to LaTeX by the Paper Writer. Does NOT produce `.tex`
files.

---

### Step 3.3 — Theory Builder M1 (Model Derivation)

| | |
|---|---|
| **Agent** | Theory Builder, Mode 1 |
| **Reads** | `context/planning/research_plan_final.md`, `context/planning/task_queue.md`, `context/research_context.md`, `context/model_equations.md` (if prior work exists) |
| **Produces** | `context/model_equations.md` |

Derives the formal model: primitives, equilibrium definitions, propositions,
proof sketches, and comparative statics. Works through each channel sequentially
per `task_queue.md`. Does not attempt the cross-channel interaction mechanism
until all individual channels have closed equilibria.

---

### Step 3.4a — Model Verifier (Completeness Check)

| | |
|---|---|
| **Agent** | Model Verifier |
| **Reads** | `context/model_equations.md`, `context/planning/research_plan_final.md`, `context/research_context.md`, `context/planning/task_queue.md` |
| **Produces** | `context/model_verifier_report.md`, `code/verification/*.py` |

Verifies derivations for correctness, completeness, and scope compliance.
Produces a verdict:
- **PASS** — proceed to Step 3.5
- **CONDITIONAL PASS** — run the correction round (Steps 3.4b, 3.4c)
- **FAIL** — escalate to human; may need to simplify scope in `research_context.md`

---

### Step 3.4b — Theory Builder M2 (Correction Round)

*Only runs if Step 3.4a returned CONDITIONAL PASS.*

| | |
|---|---|
| **Agent** | Theory Builder, Mode 2 |
| **Reads** | `context/model_verifier_report.md`, `context/model_equations.md`, `context/planning/research_plan_final.md`, `context/research_context.md` |
| **Updates** | `context/model_equations.md` (in place, with changelog appended) |

Fixes every issue listed in the CONDITIONAL PASS report. Does not rederive
passing propositions, add new results, or restructure the document.

---

### Step 3.4c — Model Verifier (Re-check)

*Only runs if Step 3.4b ran.*

| | |
|---|---|
| **Agent** | Model Verifier |
| **Reads** | `context/model_equations.md`, `context/planning/research_plan_final.md`, `context/research_context.md`, `context/planning/task_queue.md` |
| **Produces** | `context/model_verifier_report.md` (overwrite) |

Re-checks the corrected model. If still CONDITIONAL PASS or FAIL, writes
`ESCALATE TO HUMAN` as the first line and the pipeline stops.

---

### Step 3.5 — Research Evaluator M2 (Output Evaluation)

| | |
|---|---|
| **Agent** | Research Evaluator, Mode 2 |
| **Reads** | `context/planning/research_plan_final.md`, `context/literature/threat_map_final.md`, `context/model_equations.md`, `context/model_verifier_report.md`, `context/research_context.md` |
| **Produces** | `context/evaluator_feedback.md` |

Simulates a full referee report for the target venue. Evaluates whether
delivered outputs match the promises of the final research plan. Checks
propositions, comparative statics direction, and empirical coherence with
theory.

---

### Step 3.6 — Paper Writer (Four Sequential Passes)

| | |
|---|---|
| **Agent** | Paper Writer, Modes 1–4 |
| **Skill** | `.claude/skills/academic-writing/SKILL.md` |
| **Reads** | `context/planning/paper_structure.md`, `context/literature/review.md`, `context/model_equations.md`, `context/research_context.md`, `context/evaluator_feedback.md`, `context/planning/research_plan_final.md`, `context/literature/threat_map_final.md`, `context/model_verifier_report.md` (Pass 4 only) |
| **Produces** | `paper/sections/*.tex`, `context/technical_audit.md` (Pass 4) |

**Pass 1 — Structure:** Draft all sections into LaTeX. Every proposition,
citation, and contribution must be placed. Completeness over polish.

**Pass 2 — Clarity:** Simplify prose, break long sentences, remove hedging and
jargon. No content changes.

**Pass 3 — Flow and Voice:** Transitions, narrative arc, paragraph rhythm. Main
result as climax. First person plural throughout. No content changes.

**Pass 4 — Technical Audit:** Verify every equation, citation, and cross-reference
against source files. Correct errors. Produce `technical_audit.md`.

After this step, compile with `just render-paper` to verify the LaTeX builds.

---

## Data Flow Summary

```
  research_plan.md ──► Director M3 ──► research_plan_final.md
  threat_map.md                        paper_structure.md
  constraints.md                       task_queue.md
  evaluator_feedback.md                novelty_claims.md
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                    Lit. Guardian M3           Theory Builder M1
                              │                         │
                    threat_map_final.md       model_equations.md
                    review.md                           │
                    notes.md                            ▼
                    constraints.md           Model Verifier
                              │                    │
                              │              model_verifier_report.md
                              │                    │
                              │              PASS? ─┬─ NO → TB M2 → re-verify
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
                                        │
                                        ▼
                                  ── Phase 4 ──
```
