# Finance Theory Search Heuristics

Guidance for conducting literature searches in formal finance theory. Use these heuristics to improve search coverage and reduce false positives.

---

## Recommended Search Databases

| Database | Best for | Access notes |
|----------|----------|-------------|
| Google Scholar | Broadest coverage, citation counts, "cited by" for forward chaining | Free; use author-year or exact title for precision |
| SSRN | Working papers, pre-publication drafts | Free; search by abstract keyword or JEL code |
| NBER Working Papers | US-focused macro-finance, policy-relevant theory | Free search; some full texts require subscription |
| RePEc / IDEAS | Economics working papers, author pages | Free; good for finding all work by a specific author |
| Journal websites (JF, RFS, JFE, Econometrica, AER, RES) | Published, peer-reviewed results | Search within journal for precision when a topic is common |

## Search String Patterns

**For mechanism-level searches (preferred):**
- `"[mechanism keyword]" AND "equilibrium" AND "[asset class or setting]"`
- `"[author last name]" AND "[year]"` (when you have a specific citation to verify)
- `"[model primitive]" AND "information" AND "financial"` (for information-based models)

**For broader coverage:**
- `"[economic force]" AND "model" AND "[journal abbreviation]"` (restricts to formal theory)
- `"survey" OR "handbook" AND "[topic]"` (finds review articles that reference key papers)

**For forward citation chaining:**
- Google Scholar: search for the paper, click "Cited by", then filter by date or keyword

## Common False Positive Patterns

These paper types often share keywords with finance theory papers but are not mechanism-level threats:

- **Empirical papers** that test predictions of existing models without proposing new theory — classify as LOW unless they propose a competing mechanism
- **Survey/handbook chapters** — not threats, but valuable for discovering papers the direct search missed
- **Papers in adjacent fields** (e.g., pure macro, industrial organisation) that use similar model structures for different economic questions — only classify as threats if the mechanism and setting both overlap
- **Papers with similar titles but different formalisms** (e.g., "information and asset prices" could be rational expectations, behavioral, or computational) — always check the model section before classifying

## Assessing Mechanism Overlap

When deciding whether a paper is a genuine threat:

1. **Check the primitives** — do agents have the same type of information? Same objective function?
2. **Check the equilibrium concept** — same solution concept? (Nash, Bayesian, competitive)
3. **Check the comparative statics** — do the key results move in the same direction for the same parameter changes?
4. **Check the interaction structure** — does the paper model multi-channel interactions, or just one channel in isolation?

A paper is only HIGH threat if it matches on all four dimensions. Matching on 1-2 is typically MODERATE or LOW.
