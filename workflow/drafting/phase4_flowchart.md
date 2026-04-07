# Phase 4: Quality Assurance Loop — Pipeline Flowchart

## Overview

Phase 4 runs a self-critique and improvement loop on the completed manuscript.
Three specialist lenses review the paper in parallel, the Research Director
synthesises their findings into a prioritised task queue, and the Theory Builder
and Paper Writer execute the improvements. The loop runs up to 2 iterations.

**Agents involved:** Theory Lens, Presentation Lens, Framing Lens, Research Director (M4), Theory Builder (M3), Paper Writer (M5), Literature Guardian (M4, optional)

---

## Flowchart

```
┌──────────────────────────────────────────────────────────┐
│           PHASE 4 — QUALITY ASSURANCE LOOP               │
│           (max 2 iterations)                             │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 4.1: Three Self-Review Lenses IN PARALLEL   │   │
│  │                                                   │   │
│  │  ┌─────────────────────────────────────────────┐  │   │
│  │  │  4.1a: Theory Lens                          │  │   │
│  │  │  Inputs: paper/sections/*.tex               │  │   │
│  │  │          model_equations.md                  │  │   │
│  │  │          model_verifier_report.md            │  │   │
│  │  │  Output: self_reviews/review_theory.md      │  │   │
│  │  └─────────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌─────────────────────────────────────────────┐  │   │
│  │  │  4.1b: Presentation Lens                    │  │   │
│  │  │  Inputs: paper/main.tex                     │  │   │
│  │  │          paper/sections/*.tex               │  │   │
│  │  │  Output: self_reviews/review_presentation.md│  │   │
│  │  └─────────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌─────────────────────────────────────────────┐  │   │
│  │  │  4.1c: Framing Lens                         │  │   │
│  │  │  Inputs: literature/threat_map_final.md     │  │   │
│  │  │          literature/review.md               │  │   │
│  │  │          paper/sections/introduction.tex    │  │   │
│  │  │          paper/sections/literature.tex      │  │   │
│  │  │          paper/sections/conclusion.tex      │  │   │
│  │  │          paper/references.bib               │  │   │
│  │  │  Output: self_reviews/review_framing.md     │  │   │
│  │  └─────────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  (All three launched in a single message)         │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 4.2: Research Director [M4 — Improvement    │   │
│  │            Synthesis]                             │   │
│  │  Inputs: self_reviews/review_theory.md            │   │
│  │          self_reviews/review_presentation.md      │   │
│  │          self_reviews/review_framing.md           │   │
│  │  Output: improvement_task_queue.md               │   │
│  │                                                   │   │
│  │  Actions: deduplicate → prioritise (P1/P2/P3)    │   │
│  │           → assign to Paper Writer or TB          │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌──────────────────────────────────────────────────┐    │
│  │  Step 4.3: Execute Improvement Tasks             │    │
│  │  (sequential: 4.3a → 4.3b → 4.3c)               │    │
│  │                                                  │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  4.3a: Theory Builder [M3 — Equation     │    │    │
│  │  │        Improvement]                      │    │    │
│  │  │  (skip if no Theory Builder tasks)       │    │    │
│  │  │  Inputs: improvement_task_queue.md       │    │    │
│  │  │          model_equations.md              │    │    │
│  │  │          specific .tex files per task    │    │    │
│  │  │  Outputs: paper/sections/*.tex (edited)  │    │    │
│  │  │           paper/appendix.tex (if created)│    │    │
│  │  │           improvement_task_queue.md      │    │    │
│  │  │           (TB tasks marked complete)     │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │                     ▼                            │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  4.3b: Paper Writer [M5 — Improvement]   │    │    │
│  │  │  Skill: manuscript-layout                │    │    │
│  │  │  Inputs: improvement_task_queue.md       │    │    │
│  │  │          paper/sections/*.tex            │    │    │
│  │  │          paper/main.tex                  │    │    │
│  │  │          model_equations.md              │    │    │
│  │  │          literature/threat_map_final.md  │    │    │
│  │  │          self_reviews/review_*.md        │    │    │
│  │  │  Outputs: paper/sections/*.tex (edited)  │    │    │
│  │  │           improvement_task_queue.md      │    │    │
│  │  │           (PW tasks marked complete;     │    │    │
│  │  │            equation tasks → NEEDS-TB)    │    │    │
│  │  └──────────────────┬───────────────────────┘    │    │
│  │                     │                            │    │
│  │                     ▼                            │    │
│  │  ┌──────────────────────────────────────────┐    │    │
│  │  │  4.3c: Theory Builder [M3 — Follow-up]   │    │    │
│  │  │  (skip if no NEEDS-TB tasks)             │    │    │
│  │  │  Inputs: improvement_task_queue.md       │    │    │
│  │  │          (NEEDS-TB tasks only)           │    │    │
│  │  │  Outputs: paper/sections/*.tex (edited)  │    │    │
│  │  │           improvement_task_queue.md      │    │    │
│  │  │           (NEEDS-TB tasks marked done)   │    │    │
│  │  └──────────────────────────────────────────┘    │    │
│  │                                                  │    │
│  └──────────────────────┬───────────────────────────┘    │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 4.4: Recompile                              │   │
│  │  Command: just render-paper                       │   │
│  │  Verify: no fatal LaTeX errors                    │   │
│  │  Output: paper/main.pdf                           │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                  all P1 tasks resolved?                   │
│                 /                  \                      │
│               YES                  NO (and iter < 2)     │
│                │                    │                     │
│                │                    └──► loop back        │
│                │                        to Step 4.1      │
└────────────────┼─────────────────────────────────────────┘
                 │
                 ▼
           ── Pipeline Complete ──
```

---

## Sequence Table

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 4.1a | Theory Lens | Review math presentation; flag equation density, notation, proof quality | `self_reviews/review_theory.md` | Phase 3 complete |
| 4.1b | Presentation Lens | Review layout; flag abstract, section balance, paragraph structure | `self_reviews/review_presentation.md` | Phase 3 complete |
| 4.1c | Framing Lens | Review framing; flag differentiators, citations, positioning | `self_reviews/review_framing.md` | Phase 3 complete |
| 4.2 | Research Director M4 | Synthesise all three reviews into a prioritised task queue | `improvement_task_queue.md` | Steps 4.1a, 4.1b, 4.1c |
| 4.3a | Theory Builder M3 | Improve equations, move proofs to appendix (skip if no TB tasks) | `paper/sections/*.tex` (edited), `paper/appendix.tex` (if created) | Step 4.2 |
| 4.3b | Paper Writer M5 | Execute all PW tasks; mark NEEDS-TB for equation tasks it cannot resolve | `paper/sections/*.tex` (edited), `improvement_task_queue.md` (updated) | Step 4.3a |
| 4.3c | Theory Builder M3 | Follow-up on NEEDS-TB tasks (skip if none) | `paper/sections/*.tex` (edited) | Step 4.3b |
| 4.4 | (shell) | `just render-paper` — verify no fatal errors | `paper/main.pdf` | Steps 4.3b, 4.3c |

**Steps 4.1a, 4.1b, 4.1c run in parallel** — launch all three in a single message using three Agent tool calls.

**Steps 4.3a → 4.3b → 4.3c are sequential.** Theory Builder restructures equations first so Paper Writer sees the final layout. Paper Writer can escalate back to Theory Builder via NEEDS-TB flags.

**Loop exit:** All Priority 1 tasks resolved, or maximum 2 iterations reached.

---

## Step-by-step detail

### Step 4.1a — Theory Lens (Self-Review)

| | |
|---|---|
| **Agent** | Theory Lens (subagent) |
| **Reads** | `paper/sections/*.tex` (model sections and conclusion), `context/model_equations.md`, `context/model_verifier_report.md` |
| **Produces** | `context/self_reviews/review_theory.md` |

Reviews mathematical presentation quality: equation structure, proposition
completeness, proof sketch quality, notation consistency, and equation-to-prose
balance. Flags derivations that should move to an appendix. Does not fix issues
or edit `.tex` files.

---

### Step 4.1b — Presentation Lens (Self-Review)

| | |
|---|---|
| **Agent** | Presentation Lens (subagent) |
| **Reads** | `paper/main.tex`, all `paper/sections/*.tex` |
| **Produces** | `context/self_reviews/review_presentation.md` |

Reviews abstract structure and length, section balance (word counts via
`wc -w`), paragraph density, equation crowding, and LaTeX layout conventions.
Does not fix issues or edit `.tex` files.

---

### Step 4.1c — Framing Lens (Self-Review)

| | |
|---|---|
| **Agent** | Framing Lens (subagent) |
| **Reads** | `context/literature/threat_map_final.md`, `context/literature/review.md`, `paper/sections/introduction.tex`, `paper/sections/literature.tex`, `paper/sections/conclusion.tex`, `paper/references.bib` |
| **Produces** | `context/self_reviews/review_framing.md` |

Reviews contribution positioning, differentiator accuracy against the threat
map, citation coverage, literature review completeness, and introduction
framing. Does not fix issues or edit `.tex` files.

---

### Step 4.2 — Research Director M4 (Improvement Synthesis)

| | |
|---|---|
| **Agent** | Research Director, Mode 4 |
| **Reads** | `context/self_reviews/review_theory.md`, `context/self_reviews/review_presentation.md`, `context/self_reviews/review_framing.md` |
| **Produces** | `context/improvement_task_queue.md` |

Reads all three self-review reports, deduplicates overlapping findings, and
produces a prioritised task queue. Each task is assigned to either Paper Writer
or Theory Builder, has a priority level (P1/P2/P3), and an acceptance criterion.

**Task queue priority levels:**
- **P1 — Blocking:** Must fix before submission (errors, missing content, broken references)
- **P2 — Important:** Fix in this QA cycle (clarity, density, framing issues)
- **P3 — Minor:** Fix if time permits (stylistic preferences, minor improvements)

---

### Step 4.3a — Theory Builder M3 (Equation Improvement)

*Skip if no Theory Builder tasks in the improvement queue.*

| | |
|---|---|
| **Agent** | Theory Builder, Mode 3 |
| **Reads** | `context/improvement_task_queue.md`, `context/model_equations.md`, specific `.tex` files named in tasks |
| **Updates** | `paper/sections/*.tex` (edited), `paper/appendix.tex` (if created), `context/improvement_task_queue.md` (TB tasks marked complete) |

Restructures the presentation of mathematics in `.tex` files as directed by the
task queue. Permitted actions: move derivations to appendix, reorder derivation
steps, add introductory prose before equations, split propositions into
proposition + corollary. Does NOT change equations, proposition statements, or
comparative static results.

**Appendix rule:** If `paper/appendix.tex` is created, adds
`\input{appendix}` to `paper/main.tex`.

Runs BEFORE Paper Writer so that the Paper Writer sees the restructured
equation layout.

---

### Step 4.3b — Paper Writer M5 (Improvement Pass)

| | |
|---|---|
| **Agent** | Paper Writer, Mode 5 |
| **Skill** | `.claude/skills/manuscript-layout/SKILL.md` |
| **Reads** | `context/improvement_task_queue.md`, `paper/sections/*.tex`, `paper/main.tex`, `context/model_equations.md`, `context/literature/threat_map_final.md`, `context/self_reviews/review_*.md` |
| **Updates** | `paper/sections/*.tex` (edited), `context/improvement_task_queue.md` (PW tasks marked complete; equation tasks marked NEEDS-TB) |

Executes all Paper Writer tasks from the improvement queue in priority order.
For equation-related tasks that cannot be resolved with prose alone, marks
them NEEDS-TB and moves on.

---

### Step 4.3c — Theory Builder M3 (Follow-up)

*Skip if no tasks were marked NEEDS-TB in Step 4.3b.*

| | |
|---|---|
| **Agent** | Theory Builder, Mode 3 |
| **Reads** | `context/improvement_task_queue.md` (NEEDS-TB tasks only) |
| **Updates** | `paper/sections/*.tex` (edited), `context/improvement_task_queue.md` (NEEDS-TB tasks marked complete) |

Handles any equation-related tasks that the Paper Writer could not resolve.

---

### Step 4.4 — Recompile

| | |
|---|---|
| **Actor** | Shell / human |
| **Command** | `just render-paper` |
| **Verify** | No fatal LaTeX errors. Citation and reference warnings are acceptable. |
| **Output** | `paper/main.pdf` |

---

## Loop Exit Logic

```
EXIT conditions (OR):
  All Priority 1 tasks in improvement_task_queue.md are resolved
  Maximum 2 QA iterations reached

On EXIT → pipeline complete
```

If Priority 1 tasks remain after 2 iterations, they require human attention.
Review `context/improvement_task_queue.md` for unresolved items.

---

## Optional: Literature Guardian M4 (Post-Review Gap Search)

The Literature Guardian Mode 4 can run before or in parallel with Step 4.3 if
the self-reviews flagged literature gaps (missing citations, orphan references,
positioning concerns). It is not part of the default pipeline but can be
triggered manually.

| | |
|---|---|
| **Agent** | Literature Guardian, Mode 4 |
| **Reads** | `context/improvement_task_queue.md` (literature-tagged tasks), `context/self_reviews/review_connections.md`, `context/self_reviews/review_relevance.md`, `context/self_reviews/review_general.md`, `context/literature/threat_map_final.md` |
| **Produces** | `context/literature/review_post_review.md`, `context/literature/threat_map_final.md` (updated if novelty picture changes) |

---

## Data Flow Summary (Single QA Iteration)

```
  paper/sections/*.tex ──────────────────────────────────────┐
  paper/main.tex ────────────────────────────────────────────┤
  model_equations.md ────────────────────────────────────────┤
  model_verifier_report.md ──────────────────────────────────┤
  literature/threat_map_final.md ────────────────────────────┤
  literature/review.md ──────────────────────────────────────┤
  paper/references.bib ──────────────────────────────────────┘
         │
         ▼
  Three Self-Review Lenses (parallel)
  ├── Theory Lens       ──► self_reviews/review_theory.md
  ├── Presentation Lens ──► self_reviews/review_presentation.md
  └── Framing Lens      ──► self_reviews/review_framing.md
                                    │
                                    ▼
                         Research Director M4
                         (deduplicate, prioritise)
                                    │
                                    ▼
                         improvement_task_queue.md
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
          Theory Builder M3              Paper Writer M5
          (equation restructure)         (prose improvements)
                    │                               │
                    │       NEEDS-TB ───────────────►│
                    │◄──────────────────────────────┘
                    │
                    ▼
          Theory Builder M3 follow-up
          (NEEDS-TB tasks)
                    │
                    ▼
          just render-paper ──► paper/main.pdf
                    │
          all P1 resolved?
          YES → done  |  NO (iter < 2) → loop back
```
