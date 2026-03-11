---
name: literature-review-targeted
description: Checks specific claims and mechanisms in a research plan iteration against the academic literature and updates the threat map in place. Use when inside a planning loop and the research plan has been created or revised, and the threat map needs to be checked against the new plan content. Also use when asked to do a "targeted literature check", "plan-specific novelty check", or "update the threat map for this iteration". Do NOT use for initial broad scans (use literature-review-light instead) or for final exhaustive reviews (use literature-review-deep instead).
---

# Literature Review — Targeted (Per-Iteration Check)

## Purpose

Check whether the current iteration of the research plan introduces claims, mechanisms, or contributions that are at risk given the existing literature. Update the threat map in place. Do not repeat work already done — focus only on what is new or changed since the last iteration.

This skill runs inside the planning loop, potentially up to 5 times. Be efficient. Every search should have a reason.

Calibrate all output to a finance PhD / top-journal standard. Cite by author-year. Reference specific propositions, theorems, and mechanisms.

---

## Inputs

Read all of these before doing anything else:

1. `context/research_plan.md` — the current iteration's plan (check the changelog at the bottom to identify what changed this iteration)
2. `context/threat_map.md` — the existing threat map (this is the file you will update)
3. `context/research_context.md` — the permanent project specification
4. `context/literature_constraints.md` — if present, constraints on what the literature has and has not addressed

---

## Workflow

### Step 1 — Diff the Research Plan

Identify what is new or changed in this iteration of `research_plan.md`. Look for:

- New contributions added or existing contributions reframed
- New mechanisms or model components introduced
- Changes to the amplification loop structure
- New empirical strategies or identification arguments
- Contributions that were sharpened in response to prior evaluator feedback

If the plan has a changelog at the bottom, start there. If not, compare the current plan against what the threat map already covers.

Produce a short internal list of **check targets**: the specific claims or mechanisms that need literature verification this iteration. If nothing substantive changed, state this explicitly and skip to Step 4 (changelog-only update).

### Step 2 — Search for New Threats

For each check target, search the literature. Use web search to find papers that could overlap with the new or revised claims.

Search strategy:

- One targeted search per check target (not per channel — only search what changed)
- If a check target refines an existing mechanism (e.g., tightens the differentiator for Channel 2), search for papers that occupy the narrower space the plan now claims
- If a check target introduces a new element (e.g., a policy extension, a new comparative static), search for that specific element
- When a search surfaces a potentially threatening paper, fetch the abstract or introduction to assess mechanism-level overlap

Do not re-search for papers already in the threat map unless the plan revision changes the overlap assessment.

### Step 3 — Classify and Update

For each new paper found, classify it using the same schema and threat level definitions as the initial threat map:

- **HIGH** — Same formal mechanism with overlapping comparative statics. Contribution may not survive.
- **MODERATE** — Same economic question or related model structure, but formal mechanism differs. Contribution survives if differentiator is clear.
- **LOW** — Same broad literature, different mechanism. Positioning only.
- **NONE** — Foundational. Must cite, not a threat.

When uncertain, classify as MODERATE and flag with `[UNVERIFIED]`.

Additionally, reassess any existing threat map entries that are affected by the plan revision:

- If the plan sharpened a differentiator, a previously HIGH paper may now be MODERATE
- If the plan broadened a contribution's scope, a previously MODERATE paper may now be HIGH
- If the plan dropped a contribution, its threat entries can be marked `[DEPRIORITISED]` but not deleted

### Step 4 — Write Changelog and Update File

Update `context/threat_map.md` in place. Do not rewrite the entire file. Make only these changes:

1. **Add new papers** to the appropriate channel section, in the correct threat level subsection
2. **Reclassify existing papers** if the plan revision changes the overlap assessment (move them between HIGH/MODERATE/LOW and note why in the differentiator field)
3. **Update the Aggregate Novelty Assessment** section if the overall picture changed
4. **Append a changelog entry** at the bottom of the file using this format:

```markdown
---

## Changelog

### Iteration [N] — [YYYY-MM-DD]
**Plan changes checked:**
- [brief description of each check target]

**New papers added:**
- [Author (Year)] → [Channel X] → [Threat level]
- ...

**Reclassifications:**
- [Author (Year)]: [OLD level] → [NEW level]. Reason: [why]
- ...

**No-change confirmation:**
- [List any check targets where no new threats were found]

**Assessment change:** [Yes/No. If yes, explain how the overall threat picture shifted.]
```

---

## Output

Single file, updated in place: `context/threat_map.md`

No other files are produced. The Literature Guardian Mode 2 does not write literature notes or reviews — those are Mode 3 outputs.

---

## Quality Criteria

The update must:

- Address only what changed in this iteration — do not redo the full scan
- Classify every new paper at the mechanism level, not the topic level
- Never assert novelty — only flag threats and differentiators
- Flag uncertainty with `[UNVERIFIED]`
- Preserve all existing threat map content (do not delete prior entries)
- Include a changelog entry even if nothing changed (confirm "no new threats found for [check targets]")
- Be efficient — this runs inside a loop, so avoid unnecessary searches

---

## Anti-patterns

Do not:

- Rewrite the entire threat map from scratch (that destroys the accumulated state)
- Re-review papers already covered unless the plan revision changes their relevance
- Produce separate output files (no `literature_notes.md`, no `mechanism_map.md`)
- Skip the changelog (downstream agents and the human need to track what changed per iteration)
- Search broadly when the plan change is narrow — match search scope to diff scope
- Classify a paper as HIGH based on topic overlap alone — the formal mechanism must match
- Ignore `literature_constraints.md` if it exists — it records what has already been ruled out
