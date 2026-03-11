---
name: literature-review-light
description: Conducts a rapid literature scan to identify novelty threats for a formal theory paper in financial economics, working entirely from provided context files — no web search. Use when starting a new research project and needing an initial threat map before the planning loop begins. Also use when asked to do a "quick scan", "initial literature check", "threat map", or "novelty scan" for an economics/finance research idea. Do NOT use for deep or exhaustive literature reviews (use literature-review-deep instead) or for targeted checks of a specific research plan iteration (use literature-review-targeted instead).
---

# Literature Review — Light (Quick Scan)

## Purpose

Perform a fast, high-signal sweep of the academic literature to surface the papers most likely to threaten the novelty of a proposed research project. This is not an exhaustive review. The goal is to produce an initial threat map that the Research Director can use to write the first research plan.

Calibrate all output to a finance PhD / top-journal standard. Cite by author-year. Reference specific propositions, theorems, and mechanisms.

---

## Inputs

Read before doing anything else:

- `context/research_context.md` — the full research specification including the unifying primitive, three theoretical channels, amplification loop, and stated scope constraints
- `context/literature_notes.md` — if present, any paper summaries already accumulated
- `context/literature_constraints.md` — if present, constraints already identified

Web search is permitted for papers that cannot be identified from the context files alone. Prefer targeted, specific searches (author + title or author + year) over broad topic searches. The goal is to fill gaps in coverage, not to build an exhaustive bibliography. When in doubt about a paper's mechanism, fetch its abstract before classifying it.

---

## Workflow

### Step 1 — Extract Search Targets

From `research_context.md`, identify the mechanisms that require literature coverage. For this project, the minimum set is:

1. Signal correlation and coordination games (Channel 1: ρ → global games uniqueness)
2. Information acquisition with correlated signals (Channel 2: ρ → Grossman-Stiglitz)
3. Correlated liquidity withdrawal (Channel 3: ρ → market making equilibrium)
4. Interaction / amplification across channels (the fixed-point contribution)
5. AI and financial markets (empirical and applied)

For each mechanism, note the foundational papers already listed in `research_context.md`. These are known — the scan focuses on finding papers NOT already listed that may pose a threat.

### Step 2 — Extract and Supplement Papers

First, identify all papers already referenced across the context files.

Sources to mine:
- Papers explicitly cited in `research_context.md` (foundational papers and empirical motivation)
- Papers listed in `context/literature_notes.md` (if present)
- Any papers mentioned in `context/literature_constraints.md` (if present)

For each mechanism area, compile the relevant papers already known:
1. Signal correlation and coordination games (Channel 1)
2. Information acquisition with correlated signals (Channel 2)
3. Correlated liquidity withdrawal (Channel 3)
4. Interaction / amplification across channels
5. AI and financial markets (empirical and applied)

Note any mechanism areas where no papers are yet on record. For these gaps, perform targeted web searches (author + title, or mechanism keywords) to identify the most likely threats. Fetch abstracts for any papers that could be HIGH or MODERATE threats before classifying them.

### Step 3 — Classify Each Paper

For every paper identified (including those already in `research_context.md`), determine:

1. **Which channel(s) it relates to** (1, 2, 3, amplification loop, or multiple)
2. **Threat level**: one of HIGH, MODERATE, LOW, or NONE
3. **The precise differentiator**: what the paper does NOT do that the current project does

Threat level definitions:

- **HIGH** — The paper models the same formal mechanism with overlapping comparative statics. The proposed contribution may not survive.
- **MODERATE** — The paper addresses the same economic question or uses a related model structure, but the formal mechanism differs. The contribution survives if the differentiator is clearly stated.
- **LOW** — The paper is in the same broad literature but does not model the specific mechanism. Useful for positioning, not a threat.
- **NONE** — Foundational paper that the project builds on. Not a threat but must be cited and engaged.

When uncertain, classify as MODERATE and flag with `[UNVERIFIED]`.

### Step 4 — Assess Aggregate Novelty Risk

After classifying all papers, make a brief overall assessment:

- How many HIGH-threat papers exist per channel?
- Is the amplification loop (the core contribution) threatened?
- Are there any channels where the project's mechanism is already well-studied?
- What is the strongest differentiator the project has?

---

## Output

Produce three files:

**1. `context/threat_map_v1.md`** — the versioned initial threat map (permanent record of the starting state)

**2. `context/threat_map.md`** — identical copy of `threat_map_v1.md`. This is the file the targeted skill reads and updates in the loop. Writing it here avoids the need for an orchestrator rename step between Phase 1 and Phase 2.

**3. `context/literature_constraints.md`** — initial constraints file, using this schema:

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

**`context/threat_map_v1.md` schema:**

Use exactly this schema:

```markdown
# Threat Map v1 — Initial Scan

## Scan metadata
Date: [YYYY-MM-DD]
Inputs read: context/research_context.md + any present context files
Papers assessed: [number]
Coverage gaps: [mechanism areas with no papers on record]

---

## Channel 1 — Coordination Failure (Global Games + ρ)

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

## Channel 2 — Information Acquisition (Grossman-Stiglitz + ρ)

[Same structure as Channel 1]

---

## Channel 3 — Market Making (Correlated Liquidity Withdrawal)

[Same structure as Channel 1]

---

## Amplification Loop (Fixed-Point Interaction)

[Same structure as Channel 1]

---

## AI and Financial Markets (Empirical / Applied)

[Same structure as Channel 1]

---

## Aggregate Novelty Assessment

### Overall threat level: [HIGH / MODERATE / LOW]

### Channel-level summary
| Channel | HIGH threats | Strongest differentiator |
|---------|-------------|------------------------|
| 1 — Coordination | [n] | [one sentence] |
| 2 — Information  | [n] | [one sentence] |
| 3 — Market Making | [n] | [one sentence] |
| Amplification Loop | [n] | [one sentence] |

### Core contribution status
[Is the amplification loop — the fixed-point in (ρ_eff, θ*, N_eff) — threatened? Explain in 2-3 sentences.]

### Key risks for the Research Director
[Bulleted list of the 2-4 most important things the Research Director must address when writing the initial research plan.]

### Papers requiring deeper investigation
[List any papers classified as MODERATE or HIGH where the abstract was insufficient to make a definitive assessment. These will be checked in the targeted review.]
```

---

## Quality Criteria

The threat map must:

- Cover all three channels and the amplification loop separately
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
- Skip the amplification loop section (it is the core contribution)
- Classify a paper as HIGH threat based on topic overlap alone — the formal mechanism must match
- Include papers unrelated to the three channels or the amplification loop
