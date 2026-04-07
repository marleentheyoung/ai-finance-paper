# Phase 1: Pre-Loop — Pipeline Flowchart

## Overview

Phase 1 bootstraps the research project. It runs once before the planning loop
begins. The output is an initial research plan informed by a literature scan and
(optionally) human corrections.

**Agents involved:** Literature Guardian (M1), Research Director (M1), Human

---

## Flowchart

```
┌──────────────────────────────────────────────────────────┐
│                   PHASE 1 — PRE-LOOP                     │
│                                                          │
│  Human provides research_context.md                      │
│         │                                                │
│         ▼                                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 1.1: Literature Guardian [M1 — Quick Scan]  │   │
│  │  Skill: literature-review/light (web search)      │   │
│  │  Input:  context/research_context.md              │   │
│  │  Outputs: literature/threat_map_v1.md  (archive)  │   │
│  │           literature/threat_map.md     (loop copy) │  │
│  │           literature/constraints.md   (initial)   │   │
│  │           literature/search_log.md    (initial)   │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 1.1b: HUMAN CHECKPOINT                      │   │
│  │  Review threat_map_v1.md                          │   │
│  │                                                   │   │
│  │  Actions:                                         │   │
│  │    - Add missing papers                           │   │
│  │    - Correct misclassified threat levels          │   │
│  │    - Check aggregate assessment                   │   │
│  │    - Consider updating research_context.md        │   │
│  │                                                   │   │
│  │  Output (optional): human_feedback_phase1.md      │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 1.2: Research Director [M1 — Initial Plan]  │   │
│  │  Inputs: research_context.md                      │   │
│  │          literature/threat_map_v1.md               │   │
│  │          literature/constraints.md                │   │
│  │          human_feedback_phase1.md (if present)    │   │
│  │  Output: planning/research_plan.md               │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Step 1.3: Initialise Loop State                  │   │
│  │  Actor: pipeline script / human                   │   │
│  │  Outputs: loop_state.md, archives/ directory      │   │
│  └──────────────────────┬────────────────────────────┘   │
│                         │                                │
└─────────────────────────┼────────────────────────────────┘
                          │
                          ▼
                    ── Phase 2 ──
```

---

## Sequence Table

| Step | Agent | Action | Key files written | Blocking dependencies |
|------|-------|--------|-------------------|-----------------------|
| 1.1 | Literature Guardian M1 | Quick scan for novelty threats | `threat_map_v1.md`, `threat_map.md`, `constraints.md`, `search_log.md` | None |
| 1.1b | Human | Review threat map; optionally provide corrections | `human_feedback_phase1.md` (optional) | Step 1.1 |
| 1.2 | Research Director M1 | Create initial research plan using threat map and gap analysis | `research_plan.md` | Steps 1.1, 1.1b |
| 1.3 | Pipeline / Human | Initialise loop state tracker and archives directory | `loop_state.md`, `archives/` | Step 1.2 |

---

## Step-by-step detail

### Step 1.1 — Literature Guardian M1 (Quick Scan)

| | |
|---|---|
| **Agent** | Literature Guardian, Mode 1 |
| **Skill** | `.claude/skills/literature-review/light/SKILL.md` |
| **Reads** | `context/research_context.md` |
| **Produces** | `context/literature/threat_map_v1.md`, `context/literature/threat_map.md`, `context/literature/constraints.md`, `context/literature/search_log.md` |

The Literature Guardian scans the literature for papers related to the research
idea. It classifies each paper as HIGH / MODERATE / LOW threat based on
mechanism overlap. The threat map and gap analysis become the primary inputs for
the Research Director.

### Step 1.1b — Human Checkpoint

| | |
|---|---|
| **Actor** | Human researcher |
| **Reads** | `context/literature/threat_map_v1.md` |
| **Optionally produces** | `context/human_feedback_phase1.md` |

The most important checkpoint in the pipeline. The human reviews the threat map
for:
1. Missing papers the scan didn't find
2. Misclassified threat levels
3. Whether the aggregate assessment matches intuition
4. Whether `research_context.md` itself needs updating

If corrections are needed, they go into `human_feedback_phase1.md`.

### Step 1.2 — Research Director M1 (Initial Plan)

| | |
|---|---|
| **Agent** | Research Director, Mode 1 |
| **Reads** | `context/research_context.md`, `context/literature/threat_map_v1.md`, `context/literature/constraints.md`, `context/human_feedback_phase1.md` (if present) |
| **Produces** | `context/planning/research_plan.md` |

The Research Director creates the initial research plan. The plan uses the
literature constraints (especially the gap analysis) to identify which
contributions are most defensible. Each contribution must be differentiated from
the threat map at the mechanism level.

**Plan schema sections:** Research Question, Mechanism, Contributions, Phases,
Paper Structure Map, Testable Predictions (if applicable), Open Questions.

### Step 1.3 — Initialise loop state

| | |
|---|---|
| **Actor** | Pipeline script / human |
| **Produces** | `context/loop_state.md`, `context/archives/` directory |

Creates the loop state tracker (iteration counter, score, threshold) and the
archives directory for storing evaluator feedback snapshots across iterations.

---

## Data Flow Summary

```
  research_context.md
         │
         ▼
  Literature Guardian M1 ──► literature/threat_map_v1.md
                              literature/threat_map.md
                              literature/constraints.md
                              literature/search_log.md
                                    │
                                    ▼
                            HUMAN CHECKPOINT
                            (review threat map)
                                    │
                              human_feedback_phase1.md (optional)
                                    │
                                    ▼
  research_context.md ──► Research Director M1 ◄── threat_map_v1.md
  constraints.md ─────►          │                  human_feedback_phase1.md
                                 │
                                 ▼
                          planning/research_plan.md
                                 │
                                 ▼
                          Initialise loop state
                          (loop_state.md, archives/)
                                 │
                                 ▼
                           ── Phase 2 ──
```
