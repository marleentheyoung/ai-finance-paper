---
name: literature-review-deep
description: Conducts an exhaustive, systematic literature review after the planning loop exits, producing the definitive threat map, consolidated literature notes, and a structured prose literature review. Use when the research plan has been finalised and a comprehensive, publication-ready literature analysis is needed. Also use when asked for a "deep review", "full literature review", "systematic review", "final literature assessment", or "consolidate the literature". Do NOT use for initial scans (use literature-review-light) or per-iteration checks (use literature-review-targeted).
---

# Literature Review — Deep (Post-Loop Systematic Review)

## Purpose

Produce the definitive literature analysis for the paper. This skill runs once, after the planning loop has exited. It consolidates all knowledge accumulated across iterations into three outputs: the final threat map, updated literature notes, and a structured prose literature review ready for conversion to LaTeX by the academic-writing skill.

This is the most thorough pass. Every relevant paper must be accounted for. Every threat classification must be verified. Every differentiator must be stated precisely enough to survive referee scrutiny.

Calibrate all output to a top-journal standard. Cite by author-year. Reference specific propositions, theorems, and results.

---

## Inputs

Read all of these before doing anything else:

1. `context/research_context.md` — the permanent project specification
2. `context/threat_map.md` — the accumulated threat map from all prior iterations (includes changelogs)
3. `context/literature_notes.md` — any paper summaries accumulated during the project
4. `context/research_plan_final.md` — the finalised research plan (if not yet available, use `context/research_plan.md`)
5. `context/literature_constraints.md` — if present, constraints on what the literature has and has not addressed

---

## Workflow

### Step 1 — Audit the Accumulated Threat Map

Read the full threat map including all changelog entries. Identify:

1. **Gaps in coverage**: channels or sub-mechanisms that were never properly searched. The targeted reviews only checked what changed per iteration — mechanisms that were stable across iterations may have received only the initial light scan.
2. **Unverified entries**: any paper still flagged `[UNVERIFIED]`. These must be resolved.
3. **Stale classifications**: papers classified early in the loop whose threat level may have changed given the final research plan (contributions may have been sharpened, dropped, or reframed).
4. **Missing foundational papers**: check the final research plan's contributions against the foundational literatures identified in `research_context.md`. Are there canonical papers that should appear in the threat map but do not?

Produce an internal audit list of what needs to be searched, verified, or reclassified.

### Step 2 — Systematic Search

Conduct a comprehensive literature search to fill the gaps identified in Step 1. This is broader than the targeted skill's searches.

Search strategy:

- Search each channel's mechanism space comprehensively, not just incrementally
- Search for the cross-mechanism interaction specifically
- Search for recent working papers (last 2-3 years) that may have appeared since the initial scan
- Search for survey papers and handbook chapters that might reference work the earlier scans missed
- For every HIGH or MODERATE threat, fetch the paper's abstract and ideally the introduction or model section to verify mechanism-level overlap

Minimum searches:

- 2-3 per channel (matching the channels defined in `research_context.md`)
- 2-3 for the cross-mechanism interaction
- 2-3 for the empirical / applied domain
- 1-2 for any extensions or policy implications described in the research plan
- 1-2 for any gap identified in the audit

This is the last literature pass before the paper is written. Be thorough.

### Step 3 — Resolve All Unverified Entries

For every paper currently flagged `[UNVERIFIED]` in the threat map:

1. Search for the paper by title and authors
2. Fetch the abstract and, if possible, the model description
3. Reclassify as HIGH, MODERATE, LOW, or NONE based on mechanism-level comparison
4. Remove the `[UNVERIFIED]` flag and replace with `[VERIFIED]`

If a paper cannot be found or its mechanism cannot be determined from available information, flag it as `[UNRESOLVED]` with a note explaining what is missing. Do not silently drop entries.

### Step 4 — Write Final Threat Map

Produce `context/threat_map_final.md`. This is a clean, consolidated document — not a copy of the accumulated threat map with changelogs. Write it from scratch using the schema below.

Every paper that appeared in any prior version of the threat map must appear here (unless it was determined to be entirely irrelevant). New papers found in Step 2 are added.

**Schema:**

Use the channel names and mechanism labels from `research_context.md`.

```markdown
# Threat Map — Final

## Metadata
Date: [YYYY-MM-DD]
Planning loop iterations: [N]
Total papers assessed: [number]
Searches conducted (this pass): [number]
Unresolved entries: [number, or "none"]

---

## [Mechanism Area 1] — Channel 1

### HIGH threat

- **[Authors (Year)]** — *[Title]*, [Journal/Working paper]
  - Mechanism: [what the paper models]
  - Overlap: [what specifically overlaps with Channel 1]
  - Differentiator: [what the paper does NOT do]
  - Status: [VERIFIED]
  - Engagement strategy: [how the paper introduction should handle this paper — cite and differentiate / cite and build on / acknowledge and distinguish]

### MODERATE threat
[Same format]

### LOW threat / Foundational
[Same format]

---

## [Mechanism Area 2] — Channel 2
[Same structure]

---

## [Mechanism Area 3] — Channel 3
[Same structure]

---

## Cross-Mechanism Interaction ([CORE_CONTRIBUTION])
[Same structure]

---

## [Applied / Empirical Domain]
[Same structure]

---

## Extensions
[Same structure — include papers relevant to any extensions or policy implications in the research plan]

---

## Aggregate Novelty Assessment

### Overall threat level: [HIGH / MODERATE / LOW]

### Channel-level summary
| Channel | HIGH | MODERATE | Strongest differentiator |
|---------|------|----------|------------------------|
| [Mechanism Area 1] | [n] | [n] | [one sentence] |
| [Mechanism Area 2] | [n] | [n] | [one sentence] |
| [Mechanism Area 3] | [n] | [n] | [one sentence] |
| Cross-Mechanism Interaction | [n] | [n] | [one sentence] |
| Extensions | [n] | [n] | [one sentence] |

### Core contribution status
[Is the cross-mechanism interaction — [CORE_CONTRIBUTION] — threatened? Definitive 3-5 sentence assessment.]

### Novelty verdict
[For each numbered contribution in the final research plan, state: NOVEL / NOVEL WITH CAVEAT / AT RISK. One sentence of justification each.]

### Unresolved items
[List any papers that could not be fully assessed. State what additional information would be needed.]
```

### Step 5 — Update Literature Notes

Update `context/literature_notes.md` with structured summaries of all papers in the final threat map that do not already have entries. Use this format for each paper:

```markdown
## [Authors (Year)] — *[Title]*

**Journal:** [journal or working paper series]
**Core question:** [what economic problem the paper addresses]
**Model structure:** [primitives, agents, information structure, equilibrium concept]
**Key mechanism:** [the main theoretical channel, in 2-3 sentences]
**Key result:** [the main proposition or theorem, stated precisely]
**Relation to this project:** [which channel(s) it relates to and how]
**Threat level:** [HIGH / MODERATE / LOW / NONE — must match threat_map_final.md]
```

Do not rewrite existing entries unless they contain errors. Append new entries at the end, grouped by channel.

### Step 6 — Write Literature Review

Produce `context/literature_review.md` — a structured prose literature review suitable for conversion to LaTeX by the academic-writing skill.

This is an analytical document, not a list of paper summaries. It must:

1. **Position the paper** within the intersection of the relevant literatures
2. **Build the case for the contribution** by showing what the literature has done and what it has not
3. **Engage the closest threat papers** directly, with precise differentiators
4. **Establish the gap** that the cross-mechanism interaction fills

**Structure:**

Use the literature strands identified in `research_context.md` to define section headers. The generic template is:

```markdown
# Literature Review

## Introduction to the literature landscape
[2-3 paragraphs framing the literatures the paper draws on and why their intersection is underexplored.]

## [LITERATURE_STRAND_1]
[Review of foundational and recent work in the first literature strand relevant to Channel 1. Establish what is known about the mechanism this channel addresses. Identify the gap the project claims to fill.]

## [LITERATURE_STRAND_2]
[Review of foundational and recent work in the second literature strand relevant to Channel 2. Establish what is known. Identify the gap.]

## [LITERATURE_STRAND_3]
[Review of foundational and recent work in the third literature strand relevant to Channel 3. Establish what is known. Identify the gap.]

## [APPLIED_OR_EMPIRICAL_DOMAIN]
[Review of empirical and applied work relevant to the project's setting. Establish the empirical basis for the project's assumptions.]

## Cross-mechanism interaction and [BROADER_THEME]
[Review of work that connects multiple channels or addresses the broader theme (e.g., systemic risk, welfare, policy). Establish that no paper characterises the joint interaction across the channels this project unifies.]

## Summary of contributions relative to the literature
[Concise restatement of each contribution and its precise differentiator from the closest threat paper.]
```

**Writing standards:**

- Flowing academic prose, not bullet points
- Every claim about the literature must reference a specific paper
- Differentiators must be stated at the mechanism level
- No em-dashes
- No bold paragraph headers within sections (use the section headers above, then write in paragraphs)
- Tone and register of top-journal literature review sections
- Length: approximately 2,000-3,000 words

---

## Outputs

Three files:

1. `context/threat_map_final.md` — clean, consolidated final threat map (new file, does not overwrite the accumulated `threat_map.md`)
2. `context/literature_notes.md` — updated in place with new paper summaries
3. `context/literature_review.md` — structured prose literature review for conversion to LaTeX

This skill does **not** produce `paper/sections/literature.tex`. LaTeX conversion is handled by the academic-writing skill.

---

## Quality Criteria

The outputs must:

- Account for every paper that appeared in any prior threat map version
- Resolve all `[UNVERIFIED]` entries (or explicitly flag as `[UNRESOLVED]` with justification)
- Classify every paper at the mechanism level, not the topic level
- Never assert novelty without evidence — state the differentiator or flag uncertainty
- Provide engagement strategies (cite and differentiate / cite and build on / acknowledge and distinguish) for every HIGH and MODERATE threat
- Produce a literature review in flowing academic prose, not a structured list of summaries
- Match the writing standards expected by the academic-writing skill downstream

---

## Anti-patterns

Do not:

- Copy the accumulated threat map with changelogs as the final version (write `threat_map_final.md` clean)
- Skip the audit step — the targeted reviews were incremental and may have gaps
- Write the literature review as a paper-by-paper summary ("X did this, Y did that") — it must be organised by intellectual contribution, building the case for the gap
- Produce LaTeX output (that is the academic-writing skill's responsibility)
- Drop papers from earlier threat map versions without explanation
- Write differentiators as vague comparisons ("our paper is different because it focuses on X") — state the formal mechanism that differs
- Exceed 3,000 words in the literature review — it must be tight enough to fit a theory paper, not a survey
