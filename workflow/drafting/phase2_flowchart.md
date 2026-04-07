# Phase 2: Planning Loop — Pipeline Flowchart

## Overview

Phase 2 iteratively refines the research plan until it passes a quality gate
(overall score >= 4.0) or reaches the maximum of 5 iterations. Each iteration
runs three agents in sequence: the Research Director revises the plan, the
Literature Guardian checks it against the literature, and the Research Evaluator
scores it.

**Agents involved:** Research Director (M2), Literature Guardian (M2), Research Evaluator (M1), Human (optional checkpoint)

---

## Flowchart

```
┌──────────────────────────────────────────────────────────┐
│              PHASE 2 — PLANNING LOOP                     │
│              (repeat up to 5 iterations)                 │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 2.1: Research Director [M2 — Plan Revision] │   │
│  │  Inputs: planning/research_plan.md (current)      │   │
│  │          literature/threat_map.md (prev iter)     │   │
│  │          evaluator_feedback.md (prev iter)        │   │
│  │          archives/evaluator_feedback_i{N}.md      │   │
│  │          research_context.md                      │   │
│  │          literature/constraints.md (if present)   │   │
│  │  Output: planning/research_plan.md (updated)      │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 2.2: Literature Guardian [M2 — Targeted]    │   │
│  │  Skill: literature-review/targeted (web search)   │   │
│  │  Inputs: planning/research_plan.md (revised)      │   │
│  │          literature/threat_map.md (update in place)│   │
│  │          research_context.md                      │   │
│  │          literature/constraints.md                │   │
│  │          literature/search_log.md (if present)    │   │
│  │          evaluator_feedback.md (if present)       │   │
│  │  Outputs: literature/threat_map.md (updated)      │   │
│  │           literature/constraints.md (updated)     │   │
│  │           literature/search_log.md (appended)     │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 2.3: Research Evaluator [M1 — Plan Eval]    │   │
│  │  Inputs: planning/research_plan.md                │   │
│  │          literature/threat_map.md                  │   │
│  │          research_context.md                      │   │
│  │          evaluation_criteria.md                   │   │
│  │          literature/constraints.md (if present)   │   │
│  │  Outputs: evaluator_feedback.md                   │   │
│  │           loop_state.md (score + decision + iter) │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 2.3b: HUMAN CHECKPOINT (recommended)        │   │
│  │  Review evaluator_feedback.md                     │   │
│  │                                                   │   │
│  │  Check for:                                       │   │
│  │    - Hard failures (core criterion ≤ 2)           │   │
│  │    - Score regression from previous iteration     │   │
│  │    - New HIGH threats from Literature Guardian     │   │
│  │                                                   │   │
│  │  (Skipped in overnight mode; use --pause-on-reject│   │
│  │   to stop on hard failures)                       │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│                  ┌────────────┐                          │
│                  │ Archive    │                          │
│                  │ feedback   │                          │
│                  │ to i{N}.md │                          │
│                  └──────┬─────┘                          │
│                         │                                │
│                  overall_score ≥ 4.0?                    │
│                 /                  \                     │
│               YES                  NO (and iter < 5)    │
│                │                    │                    │
│                │                    └──► loop back       │
│                │                        to Step 2.1     │
│                │                        with iter {N+1} │
└────────────────┼─────────────────────────────────────────┘
                 │
                 ▼
           ── Phase 3 ──
```

---

## Sequence Table

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 2.1 | Research Director M2 | Revise plan using prior threat map + prior evaluator feedback | `research_plan.md` | None (iter 1) or Step 2.3 of prev iter |
| 2.2 | Literature Guardian M2 | Check the Director's revision; update threat map | `threat_map.md`, `constraints.md`, `search_log.md` | Step 2.1 |
| 2.3 | Research Evaluator M1 | Score the revised plan against the updated threat map | `evaluator_feedback.md`, `loop_state.md` | Step 2.2 |
| 2.3b | Human (optional) | Review feedback for hard failures, regressions, new threats | — | Step 2.3 |

On iteration 1, `evaluator_feedback.md` does not yet exist; the Director revises using the threat map and research context only.

---

## Step-by-step detail

### Step 2.1 — Research Director M2 (Plan Revision)

| | |
|---|---|
| **Agent** | Research Director, Mode 2 |
| **Reads** | `context/planning/research_plan.md`, `context/literature/threat_map.md`, `context/research_context.md`, `context/evaluator_feedback.md` (if present), `context/archives/evaluator_feedback_i{N}.md` (all prior), `context/literature/constraints.md` (if present) |
| **Updates** | `context/planning/research_plan.md` (in place, with changelog entry) |

The Research Director revises the plan based on evaluator feedback and the
current threat map. It reads all archived feedback (not just the latest) to
avoid repeating past mistakes.

**Conflict priority rule (from agent file):**
1. Hard failure conditions take absolute precedence
2. New HIGH threats override evaluator directives to expand that contribution
3. Evaluator directives apply after MODERATE threats are resolved
4. Scope constraints override both

---

### Step 2.2 — Literature Guardian M2 (Targeted Check)

| | |
|---|---|
| **Agent** | Literature Guardian, Mode 2 |
| **Skill** | `.claude/skills/literature-review/targeted/SKILL.md` |
| **Reads** | `context/planning/research_plan.md` (revised), `context/literature/threat_map.md`, `context/research_context.md`, `context/literature/constraints.md`, `context/literature/search_log.md` (if present), `context/evaluator_feedback.md` (if present) |
| **Updates** | `context/literature/threat_map.md` (in place, with changelog), `context/literature/constraints.md`, `context/literature/search_log.md` (appended) |

The Literature Guardian checks the specific claims and mechanisms introduced or
changed this iteration. It does not re-review papers already covered. It reads
the search log to avoid duplicate searches and the evaluator feedback for
literature positioning concerns.

---

### Step 2.3 — Research Evaluator M1 (Plan Evaluation)

| | |
|---|---|
| **Agent** | Research Evaluator, Mode 1 |
| **Reads** | `context/planning/research_plan.md`, `context/literature/threat_map.md`, `context/research_context.md`, `context/evaluation_criteria.md`, `context/literature/constraints.md` (if present) |
| **Produces** | `context/evaluator_feedback.md` (from scratch), `context/loop_state.md` (updated) |

The Research Evaluator scores the plan on 8 criteria using the rubric in
`evaluation_criteria.md`. It updates `loop_state.md` with the iteration number,
overall score, and decision (ACCEPT / REVISE / REJECT).

**Scoring formula:**
```
overall_score = min(novelty, mechanism_clarity, feasibility) × 0.6
              + mean(all_eight) × 0.4
```

**Hard failures (force REJECT):** Novelty ≤ 2, Mechanism Clarity ≤ 2, or
Theoretical Feasibility ≤ 2.

---

### Step 2.3b — Human Checkpoint (recommended)

| | |
|---|---|
| **Actor** | Human researcher |
| **Reads** | `context/evaluator_feedback.md`, `context/loop_state.md` |

Review the evaluator feedback before continuing. Check for:
1. **Hard failures** (core criterion ≤ 2) — consider updating `research_context.md`
2. **Score regression** — if the score dropped, the loop may be oscillating
3. **HIGH threat escalation** — verify new HIGH threats before the RD responds

In overnight mode (`run_pipeline.sh`), this checkpoint is skipped. Use
`--pause-on-reject` to stop the pipeline on hard failures.

---

## Loop Exit Logic

```
loop_state.md tracks:
  iteration:     current iteration number (starts at 0)
  current_score: evaluator's overall_score (1-5 scale)
  decision:      ACCEPT, REVISE, or REJECT
  threshold:     4.0
  history:       table of all past scores

EXIT conditions (OR):
  current_score >= 4.0  →  ACCEPT, proceed to Phase 3
  iteration == 5        →  max iterations reached, proceed to Phase 3

On EXIT:
  Archive evaluator_feedback.md to archives/evaluator_feedback_i{N}.md
  Proceed to Phase 3
```

---

## Feedback Archival

Before each iteration (except iteration 1), the pipeline archives the previous
iteration's evaluator feedback:

```
cp context/evaluator_feedback.md context/archives/evaluator_feedback_i{N-1}.md
```

This ensures the Research Director has access to the full history of evaluator
concerns across all iterations, preventing amnesia and oscillation.

---

## Data Flow Summary (Single Iteration)

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
  constraints.md                           │
                                    ▼
                         Literature Guardian M2 ──► threat_map.md (updated)
                                                    constraints.md (updated)
                                                    search_log.md (appended)
                                    │
                                    ▼
                         Research Evaluator M1 ──► evaluator_feedback.md
                                                   loop_state.md
                                    │
                          overall_score ≥ 4.0?
                          YES → Phase 3  |  NO → next iteration
```
