# Literature Review — Shared Schemas

This file defines the shared classification schemas, paper entry formats, and threat level definitions used across all three literature review skills (light, targeted, deep). Each skill references this file rather than duplicating these definitions.

---

## Threat Level Definitions

- **HIGH** — The paper models the same formal mechanism with overlapping comparative statics. The proposed contribution may not survive.
- **MODERATE** — The paper addresses the same economic question or uses a related model structure, but the formal mechanism differs. The contribution survives if the differentiator is clearly stated.
- **LOW** — The paper is in the same broad literature but does not model the specific mechanism. Useful for positioning, not a threat.
- **NONE** — Foundational paper that the project builds on. Not a threat but must be cited and engaged.

When uncertain, classify as MODERATE and flag with `[UNVERIFIED]`.

---

## Paper Entry Schema

Use this format for every paper in the threat map:

```markdown
- **[Authors (Year)]** — *[Title]*, [Journal/Working paper]
  - Mechanism: [one-sentence description of what the paper models]
  - Overlap: [what specifically overlaps with the proposed contribution]
  - Differentiator: [what the paper does NOT do that this project does]
  - Status: [VERIFIED / UNVERIFIED / UNRESOLVED]
```

The deep review adds one additional field per entry:

```markdown
  - Engagement strategy: [how the paper introduction should handle this — cite and differentiate / cite and build on / acknowledge and distinguish]
```

---

## Threat Map Section Structure

Organise the threat map by channel/mechanism area, not by journal or date. Each channel section contains subsections for HIGH, MODERATE, and LOW/Foundational threats.

```markdown
## [Mechanism Area N] — Channel N

### HIGH threat
[paper entries]

### MODERATE threat
[paper entries]

### LOW threat / Foundational
[paper entries]
```

Always include a section for the **Cross-Mechanism Interaction** — this is the paper's core contribution and must be assessed separately.

---

## Aggregate Novelty Assessment Schema

Every threat map version must end with:

```markdown
## Aggregate Novelty Assessment

### Overall threat level: [HIGH / MODERATE / LOW]

### Channel-level summary
| Channel | HIGH threats | Strongest differentiator |
|---------|-------------|------------------------|
| [Mechanism Area 1] | [n] | [one sentence] |
| ...     | ...         | ...                    |

### Core contribution status
[Is the cross-mechanism interaction threatened? 2-5 sentence assessment.]

### Key risks for the Research Director
[Bulleted list of the 2-4 most important things to address in the research plan.]
```

---

## Quality Principles (All Modes)

- Classify every paper at the **mechanism level**, not the topic level
- Never assert novelty — only flag threats and differentiators
- Flag uncertainty explicitly with `[UNVERIFIED]`
- Provide actionable input for downstream agents — vague statements like "some overlap exists" are not acceptable
- Calibrate to finance PhD / top-journal standard
- Cite by author-year; reference specific propositions, theorems, and mechanisms
