---
name: literature-review-light
description: Conducts a rapid literature scan to identify novelty threats for a formal theory paper, working primarily from provided context files with targeted web search to fill gaps. Use when starting a new research project and needing an initial threat map before the planning loop begins. Also use when asked to do a "quick scan", "initial literature check", "threat map", or "novelty scan" for a research idea. Do NOT use for deep or exhaustive literature reviews (use literature-review-deep instead) or for targeted checks of a specific research plan iteration (use literature-review-targeted instead).
---

# Literature Review — Light (Quick Scan)

## Purpose

Perform a fast, high-signal sweep of the academic literature to surface the papers most likely to threaten the novelty of a proposed research project. This is not an exhaustive review. The goal is to produce an initial threat map that the Research Director can use to write the first research plan.

Calibrate all output to a PhD / top-journal standard. Cite by author-year. Reference specific propositions, theorems, and mechanisms.

---

## Inputs

Read before doing anything else:

- `context/research_context.md` — the full research specification including the core contribution, theoretical channels, cross-mechanism interactions, and stated scope constraints
- `context/literature/notes.md` — if present, any paper summaries already accumulated
- `context/literature/constraints.md` — if present, constraints already identified

Web search is permitted for papers that cannot be identified from the context files alone. Prefer targeted, specific searches (author + title or author + year) over broad topic searches. The goal is to fill gaps in coverage, not to build an exhaustive bibliography. When in doubt about a paper's mechanism, fetch its abstract before classifying it.

---

## Workflow

### Step 1 — Extract Search Targets

From `research_context.md`, identify the mechanisms that require literature coverage. At minimum, extract:

1. Channel 1 — [CHANNEL_NAME] (the first theoretical mechanism defined in `research_context.md`)
2. Channel 2 — [CHANNEL_NAME] (the second theoretical mechanism)
3. Channel 3 — [CHANNEL_NAME] (the third theoretical mechanism, if applicable)
4. Cross-mechanism interaction ([CORE_CONTRIBUTION] — the paper's main unifying contribution)
5. Empirical and applied literature relevant to the project's setting

Adapt the number of channels and their labels to match what `research_context.md` specifies.

For each mechanism, note the foundational papers already listed in `research_context.md`. These are known — the scan focuses on finding papers NOT already listed that may pose a threat.

### Step 2 — Extract and Supplement Papers

For search strategy guidance (databases, search patterns, false positive patterns), see `.claude/skills/literature-review/references/finance_theory_search_heuristics.md`.

First, identify all papers already referenced across the context files.

Sources to mine:
- Papers explicitly cited in `research_context.md` (foundational papers and empirical motivation)
- Papers listed in `context/literature/notes.md` (if present)
- Any papers mentioned in `context/literature/constraints.md` (if present)

For each mechanism area, compile the relevant papers already known:
1. [Mechanism Area 1] (Channel 1)
2. [Mechanism Area 2] (Channel 2)
3. [Mechanism Area 3] (Channel 3)
4. Cross-mechanism interaction
5. Empirical / applied literature

Note any mechanism areas where no papers are yet on record. For these gaps, perform targeted web searches (author + title, or mechanism keywords) to identify the most likely threats. Fetch abstracts for any papers that could be HIGH or MODERATE threats before classifying them.

### Step 3 — Classify Each Paper

For every paper identified (including those already in `research_context.md`), determine:

1. **Which channel(s) it relates to** (1, 2, 3, cross-mechanism interaction, or multiple)
2. **Threat level**: one of HIGH, MODERATE, LOW, or NONE
3. **The precise differentiator**: what the paper does NOT do that the current project does

Threat level definitions and paper entry schema are defined in `.claude/skills/literature-review/shared-schemas.md`. Read that file for the canonical definitions of HIGH, MODERATE, LOW, and NONE, and the required fields per paper entry.

### Step 4 — Assess Aggregate Novelty Risk

After classifying all papers, make a brief overall assessment:

- How many HIGH-threat papers exist per channel?
- Is the cross-mechanism interaction (the core contribution) threatened?
- Are there any channels where the project's mechanism is already well-studied?
- What is the strongest differentiator the project has?

---

## Output

Produce four files:

**1. `context/literature/threat_map_v1.md`** — the versioned initial threat map (permanent record of the starting state)

**2. `context/literature/threat_map.md`** — identical copy of `threat_map_v1.md`. This is the file the targeted skill reads and updates in the loop. Writing it here avoids the need for an orchestrator rename step between Phase 1 and Phase 2.

**3. `context/literature/constraints.md`** — initial constraints file, using this schema:

```markdown
# Literature Constraints

## What the literature has addressed

[Per channel: brief statement of what existing models have established, based on papers in research_context.md]

## What the literature has NOT addressed (gaps)

[Per channel: the specific gaps this project claims to fill; must correspond to the differentiators in the threat map]

## Coverage gaps requiring deeper search

[Mechanism areas where no papers were found — flag for deep review]

## Changelog

### Quick Scan — [YYYY-MM-DD]
Initial version produced from research_context.md and light scan.
```

---

**`context/literature/threat_map_v1.md` schema:**

Use exactly this schema, adapting channel names from `research_context.md`:

```markdown
# Threat Map v1 — Initial Scan

## Scan metadata
Date: [YYYY-MM-DD]
Inputs read: context/research_context.md + any present context files
Papers assessed: [number]
Coverage gaps: [mechanism areas with no papers on record]

---

## [Mechanism Area 1] — Channel 1

### HIGH threat
[For each paper:]
- **[Authors (Year)]** — *[Title]*, [Journal/Working paper]
  - Mechanism: [one-sentence description of what the paper models]
  - Overlap: [what specifically overlaps with the proposed Channel 1 contribution]
  - Differentiator: [what the paper does NOT do that this project does]
  - Status: [VERIFIED / UNVERIFIED]

### MODERATE threat
[Same format]

### LOW threat / Foundational
[Same format]

---

## [Mechanism Area 2] — Channel 2

[Same structure as Channel 1]

---

## [Mechanism Area 3] — Channel 3

[Same structure as Channel 1]

---

## Cross-Mechanism Interaction ([CORE_CONTRIBUTION])

[Same structure as Channel 1]

---

## [Applied / Empirical Domain]

[Same structure as Channel 1]

---

## Aggregate Novelty Assessment

### Overall threat level: [HIGH / MODERATE / LOW]

### Channel-level summary
| Channel | HIGH threats | Strongest differentiator |
|---------|-------------|------------------------|
| [Mechanism Area 1] | [n] | [one sentence] |
| [Mechanism Area 2] | [n] | [one sentence] |
| [Mechanism Area 3] | [n] | [one sentence] |
| Cross-Mechanism Interaction | [n] | [one sentence] |

### Core contribution status
[Is the cross-mechanism interaction — [CORE_CONTRIBUTION] — threatened? Explain in 2-3 sentences.]

### Key risks for the Research Director
[Bulleted list of the 2-4 most important things the Research Director must address when writing the initial research plan.]

### Papers requiring deeper investigation
[List any papers classified as MODERATE or HIGH where the abstract was insufficient to make a definitive assessment. These will be checked in the targeted review.]
```

**4. `context/literature/search_log.md`** — a log of every search query run and every paper reviewed, so future iterations can avoid duplicate work. Use this schema:

```markdown
# Search Log

## Quick Scan — [YYYY-MM-DD]

### Searches performed
| # | Query / source | Papers found | Notes |
|---|---------------|-------------|-------|
| 1 | [search query or "mined from research_context.md"] | [n] | [brief note] |

### Papers reviewed
| Author-Year | Title | Source | Classified as | Channel |
|-------------|-------|--------|--------------|---------|
| [Author (Year)] | [Title] | [how found] | [threat level] | [channel] |
```

---

## Quality Criteria

The threat map must:

- Cover all channels and the cross-mechanism interaction separately
- Classify every paper at the mechanism level, not the topic level
- Never assert novelty — only flag threats and differentiators
- Flag uncertainty explicitly with `[UNVERIFIED]`
- Include papers already listed in `research_context.md` (they are known threats that still need classification)
- Provide actionable input for the Research Director — vague statements like "some overlap exists" are not acceptable

---

## Anti-patterns

Do not:

- Produce a flat list of paper summaries (that is `literature_notes.md`, a different output)
- Organise by journal or date instead of by channel
- Skip the cross-mechanism interaction section (it is the core contribution)
- Classify a paper as HIGH threat based on topic overlap alone — the formal mechanism must match
- Include papers unrelated to the identified channels or the cross-mechanism interaction
