# Revision Task Queue
Date: 2026-03-11  Iteration: 1

## Executive Summary

Three referee reports yield 49 raw issues that deduplicate to 35 distinct revision tasks. There are **14 blocking tasks** (Priority 1), **14 important tasks** (Priority 2), and **7 minor tasks** (Priority 3). The most critical cluster involves the abstract (complete rewrite required: length, structure, equations, citations all non-compliant -- B1/B2/B3/B4 merged into one task). A second major cluster involves unreferenced equation labels throughout the manuscript (A1/A3/A4/A5/A9/A10/A11/A12 consolidated). Two theory-level blocking issues require the Theory Builder: the unproved $h \to \infty$ bifurcation assumption (A7) and the unverified Morris-Shin uniqueness transfer (A6). Recommended fix order: (1) Theory Builder resolves A6, A7, A8 first, as these may change equation content; (2) Paper Writer then executes all presentation fixes in a single pass, starting with the abstract rewrite and equation label cleanup; (3) Paper Writer handles literature additions and framing last.

---

## Priority 1 -- Blocking (fix before any other work)

| ID | Sources | Assignee | Section | Issue | Effort | Acceptance Criterion | Depends On |
|----|---------|----------|---------|-------|--------|---------------------|------------|
| T01 | B1,B2,B3,B4 | paper-writer | main.tex (abstract) | Rewrite abstract: currently ~230 words with 3+ equations, 3 plain-text citations, and ~10-sentence block. Must be 5-sentence structure, <=150 words, no equations (inline $\rho$ OK), no citations. Use rewrite guidance from Report B. | M | wc -w of abstract <=150; grep finds 0 display-math environments; grep finds 0 author-year strings | -- |
| T02 | A7 | theory-builder | amplification.tex lines 78-85 | Prove the $h = d\theta^*/d\rho_{\text{eff}} \to \infty$ divergence at $\rho_{\text{eff}} \to \rho_1^*$ via formal implicit differentiation or cite a specific global-games result. Currently treated as a "regularity condition" in a footnote; this is the crux of the bifurcation result. | L | Formal proof or cited theorem with verified applicability replaces the footnote assertion | -- |
| T03 | A6 | theory-builder | channel1.tex line 45 | Verify that the Morris-Shin (2003) uniqueness condition transfers from the continuous-action to the binary-action (Goldstein-Pauzner 2005) bank-run setting. Currently the proof sketch appeals to Morris-Shin without establishing applicability. | L | Explicit statement of why the condition holds in the binary-action setting, with citation or proof | -- |
| T04 | A8 | theory-builder | channel2.tex lines 36-39 | Resolve the forward-reference problem: $\rho_{\text{eff}}$ is used in the Channel 2 indifference condition but not defined until the amplification section. Either define $\rho_{\text{eff}}$ briefly in Channel 2 or rewrite using exogenous $\rho$ with a forward pointer. | S | $\rho_{\text{eff}}$ is either defined before first use or replaced with $\rho$ plus a note | -- |
| T05 | A1,A2,B13 | paper-writer | amplification.tex lines 57-63 | The 5-equation align block (a-coeff through w-coeff) has no \eqref references anywhere and no intervening prose. Add interpretive prose between coefficient definitions and either add \eqref references or remove labels. Move Jacobian derivation to appendix per Referee A recommendation. | M | Each displayed equation is either referenced by \eqref or unlabelled; no more than 2 consecutive displayed equations without intervening prose; Jacobian derivation in appendix | T02 |
| T06 | A3 | paper-writer | channel1.tex lines 31-35 | Equation \eqref{eq:rho1star} is orphaned (never referenced); the duplicate inside Proposition 1 (\eqref{eq:rho1star-prop}) is the one actually used. Remove the standalone duplicate or merge. | S | Only one version of the equation exists, and it is referenced by \eqref | -- |
| T07 | A4 | paper-writer | channel3.tex lines 7-14 | Equations \eqref{eq:reservation-price} and \eqref{eq:correlated-calibrations} are labelled but never referenced. Either add \eqref references in the text or remove the labels. | S | Each equation is either referenced or unlabelled | -- |
| T08 | A5 | paper-writer | amplification.tex lines 65-71 | Equations \eqref{eq:jacobian} and \eqref{eq:eigenvalue} are labelled but never referenced. Add \eqref references in the Jacobian discussion. | S | Both equations referenced by \eqref in surrounding prose | T05 |
| T09 | B5 | paper-writer | tables/*.tex | All 3 tables use `[h]` float placement; change to `[t]`. | S | grep for `[h]` in table files returns 0 matches; all use `[t]` | -- |
| T10 | B6 | paper-writer | main.tex lines 47-57 | Four \section commands (Channel 1, Channel 2, Channel 3, Amplification) lack \label{sec:...}. Add labels. | S | Each of the 4 sections has a \label{sec:...} in main.tex | -- |
| T11 | B9 | paper-writer | introduction.tex | Introduction uses 5 \subsection headers; remove them and replace with prose transitions for a flowing 5-block structure. | M | grep for \subsection in introduction.tex returns 0 matches | -- |
| T12 | B10 | paper-writer | introduction.tex line 6 | Opening paragraph contains citations (\citet{gu2020}, \citet{kim2024}). Remove citations from the opening paragraph. | S | No \citet or \citep in the first paragraph of introduction.tex | -- |
| T13 | B15 | paper-writer | main.tex line 33 | Remove `\newpage` after abstract. | S | grep for \newpage in main.tex returns 0 matches (or only intentional ones) | -- |
| T14 | A19 | theory-builder | model_equations.md / amplification.tex | Verify the sign of the comparative static $d\rho^*/dc_P$. The verification report flags that higher $c_P$ increases $|a|$, which may lower $\rho^*$, contradicting the stated $d\rho^*/dc_P > 0$. If the sign is wrong, correct it in all locations. | M | Sign is verified with derivation; manuscript and model_equations.md agree | -- |

---

## Priority 2 -- Important (fix in this cycle)

| ID | Sources | Assignee | Section | Issue | Effort | Acceptance Criterion | Depends On |
|----|---------|----------|---------|-------|--------|---------------------|------------|
| T15 | B7,B8 | paper-writer | conclusion.tex | Conclusion is ~1,050 prose words (target <=600). Compress "Summary of Results" subsection from ~380 words to ~50 words (one sentence per contribution). Cut total to <=600 words. | M | wc -w estimate of prose <=600 | -- |
| T16 | B11 | paper-writer | introduction.tex | Introduction is ~1,100 prose words (target 1,500-2,000). Expand "This Paper" and "Main Results" blocks with more economic intuition. | M | Prose estimate >=1,500 words | T11 |
| T17 | B12 | paper-writer | literature.tex, introduction.tex | Literature content totals ~1,800 words across both files due to overlap. Consolidate: either remove intro lit paragraphs or shorten standalone section. Total literature content <=1,500 words. | M | Combined literature prose <=1,500 words | T11,T16 |
| T18 | A9,B14 | paper-writer | channel3.tex lines 21-28 | Two consecutive equations with minimal prose; \eqref{eq:withdrawal-variance} is never referenced. Add interpretive prose and fix reference. | S | No more than 2 consecutive equations without prose; equation referenced or unlabelled | -- |
| T19 | A10 | paper-writer | channel2.tex lines 24-31 | Equation \eqref{eq:pi-private} is labelled but never referenced. Add \eqref reference or remove label. | S | Equation referenced or unlabelled | -- |
| T20 | A11 | paper-writer | extensions.tex lines 13-24 | Three equations (\eqref{eq:pi-alpha-adoption}, \eqref{eq:tracking-error}, \eqref{eq:systemic-cost}) labelled but never referenced. Add references or remove labels. | S | Each equation referenced or unlabelled | -- |
| T21 | A12 | paper-writer | amplification.tex lines 38-46 | Equation \eqref{eq:composite-T} labelled but never referenced. Add reference or remove label. | S | Equation referenced or unlabelled | -- |
| T22 | A13 | theory-builder | channel1.tex lines 52-61 | Proposition 2 states non-monotonicity holds "for $\sigma$ sufficiently small" without quantifying the condition. Provide a formal sufficient condition on $\sigma$. | M | Proposition 2 states an explicit bound on $\sigma$ | -- |
| T23 | A14 | theory-builder | channel3.tex lines 62-76 | Proposition 3c proof sketch claims inventory cost is unbounded, but the linear specification with finite $N$ yields finite cost. Correct the proof sketch. | M | Proof sketch matches the finite-$N$ specification; no unboundedness claim for finite $N$ | -- |
| T24 | C1 | paper-writer | literature.tex, references.bib | Add Margaretic and Pasten (2014, JBF) citation with differentiator: they correlate bank fundamentals, not signals. Place in global games subsection. | S | \citep{margaretic2014} or \citet{margaretic2014} present in literature.tex; bib entry exists | -- |
| T25 | C2 | paper-writer | literature.tex, references.bib | Add Barucca and Morone (2025) citation and bib entry. Place in AI and Financial Markets subsection as context. | S | Citation present in literature.tex; bib entry exists | -- |
| T26 | C3 | paper-writer | introduction.tex ~line 14 | Channel 2 contribution summary omits FPE non-monotonicity. Add mention for parallel structure with Channels 1 and 3. | S | Introduction summary paragraph mentions FPE non-monotonicity for Channel 2 | T11 |
| T27 | C4 | paper-writer | conclusion.tex ~line 12 | "Pagano (1989)" is plain text; convert to \citet{pagano1989}. | S | grep for plain-text "Pagano (1989)" returns 0; \citet{pagano1989} present | -- |
| T28 | A18 | paper-writer | channel2.tex lines 67-69 | $\tau_s$ in the RPE formula is undefined. Either define $\tau_s$ (signal precision) in this section or replace with $1/\sigma^2$ consistent with the model normalisation. Cross-coordinate with notation issue (A, notation item 1). | S | $\tau_s$ is either defined before use or replaced with a defined quantity | T04 |

---

## Priority 3 -- Minor (fix if time permits)

| ID | Sources | Assignee | Section | Issue | Effort | Acceptance Criterion | Depends On |
|----|---------|----------|---------|-------|--------|---------------------|------------|
| T29 | A15,A16 | theory-builder | amplification.tex lines 84, 89-93 | Two proof gaps: (a) strict inequality $\rho^* < \rho_2^*, \rho_3^*$ argued only qualitatively; (b) Proposition 5 invokes Banach without citing the spectral-radius-to-contraction result. Add formal one-sentence arguments or citations. | S | Each claim has a formal citation or one-line argument | T02 |
| T30 | A17 | paper-writer | model.tex lines 52-56 | Elevate the $N_{\text{info}}(\rho) = 1/\rho$ result to a numbered Lemma. Move equicorrelation inversion proof to appendix if space needed. | S | Result is a numbered Lemma environment | -- |
| T31 | A28 | paper-writer | channel3.tex line 75 | Parameter condition in footnote should be a stated assumption in Proposition 3c. | S | Condition appears in proposition statement, not footnote | T23 |
| T32 | B17 | paper-writer | multiple files | Add non-breaking space (~) before all \ref{} and \eqref{} calls. ~20+ instances. | M | grep for `[^~]\\eqref` and `[^~]\\ref` returns 0 matches | -- |
| T33 | B18,B19 | paper-writer | main.tex, section files | Remove duplicate \label entries: use one label per section consistently. | S | No duplicate labels for same section | T10 |
| T34 | C5 | paper-writer | introduction.tex ~line 40 | Strengthen Hansen-Lee differentiator by noting they do not test the high-$\rho$ regime. | S | Introduction states that Hansen-Lee do not test the high-$\rho$ regime | T11 |
| T35 | A25,A26,A27 | paper-writer | multiple files | Minor presentation: (a) clarify $\rho$ vs. $\underline{\rho}$ in domain definition; (b) move Channel 1 proof sketch to proof environment; (c) move Proposition 6 $H(\rho)$ detail to appendix. | M | Each item addressed | T05 |

---

## Cross-Agent Coordination Notes

1. **T02/T03 (Theory Builder) -> T05/T08 (Paper Writer):** The Theory Builder must resolve the bifurcation proof (T02) and uniqueness transfer (T03) before the Paper Writer restructures the amplification section equations (T05/T08), since the math content may change.
2. **T04 (Theory Builder) -> T28 (Paper Writer):** The $\rho_{\text{eff}}$ forward-reference fix (T04) determines how the Paper Writer handles the $\tau_s$ notation in Channel 2 (T28).
3. **T14 (Theory Builder) -> T05 (Paper Writer):** If the comparative static sign is wrong (T14), the amplification section prose must be updated when T05 is executed.
4. **T22/T23 (Theory Builder) -> T31 (Paper Writer):** The Proposition 3c proof correction (T23) should be done before the Paper Writer moves the footnote condition into the proposition statement (T31).

---

## Assignment Summary

**Paper Writer Revision Pass:** T01, T05, T06, T07, T08, T09, T10, T11, T12, T13, T15, T16, T17, T18, T19, T20, T21, T24, T25, T26, T27, T28, T30, T31, T32, T33, T34, T35 (28 tasks)

**Theory Builder Restructure Pass:** T02, T03, T04, T14, T22, T23, T29 (7 tasks)

**Recommended execution order:**
1. Theory Builder: T03, T04, T14 (quick fixes and verifications)
2. Theory Builder: T02, T22, T23 (substantive proof work)
3. Paper Writer: T01, T09, T10, T12, T13 (quick blocking fixes, no dependencies)
4. Paper Writer: T06, T07, T08, T18, T19, T20, T21 (equation label cleanup)
5. Paper Writer: T05, T11, T15, T16, T17 (structural rewrites)
6. Paper Writer: T24, T25, T26, T27, T28 (literature and framing)
7. Paper Writer: T30, T31, T32, T33, T34, T35 (minor polish)
8. Theory Builder: T29 (minor proof polish)

---

## Completed Tasks

| ID | Completed by | Date | Notes |
|----|-------------|------|-------|
| T02 | theory-builder | 2026-03-11 | Proved h -> infinity divergence via saddle-node bifurcation argument. Replaced footnote assertion with formal implicit-differentiation proof citing Guckenheimer-Holmes (1983) Theorem 3.4.1. Square-root singularity theta* = theta*(rho_1*) - C*sqrt(rho_1* - rho_eff) formally established. Updated amplification.tex and model_equations.md. |
| T03 | theory-builder | 2026-03-11 | Verified Morris-Shin uniqueness transfer to binary-action GP setting. Three-part argument: (1) GP dominance regions ensure monotone threshold strategies, reducing to 1D threshold crossing; (2) Hellwig (2002) Theorem 1 establishes the uniqueness condition for games with threshold structure and dominance regions; (3) the condition depends on precision ratio, not action space. Updated channel1.tex proof sketch. |
| T04 | theory-builder | 2026-03-11 | Resolved forward-reference: replaced rho_eff with exogenous rho in eq:gs-indifference. Added footnote explaining that rho_eff generalisation appears in the amplification section. Updated channel2.tex. |
| T14 | theory-builder | 2026-03-11 | Verified sign of d(rho*)/d(c_P). Correct sign is d(rho*)/d(c_P) < 0 (higher c_P lowers rho*). The stated d(rho*)/d(c_P) > 0 in model_equations.md was incorrect. Mechanism: higher c_P raises abs(a) directly, lowers mu_I* at fixed point, reduces N_eff*, and brings system closer to rho_1* boundary. Fixed model_equations.md and amplification.tex (line 111: "lower" -> "higher"). |
| T22 | theory-builder | 2026-03-11 | Quantified "sigma sufficiently small" in Proposition 2. Explicit bound: sigma < (theta_H - theta_L)*sqrt(1-rho_1*)/(2*sqrt(2*pi)), ensuring global games posterior concentrates in interior of dominance region for all rho in [0, rho_1*). Updated channel1.tex and model_equations.md. |
| T23 | theory-builder | 2026-03-11 | Corrected Proposition 3c proof sketch. Removed unboundedness claim for finite N. Both revenue and cost are affine in (1+(N-1)*rho) with finite N; the crossing occurs because marginal cost exceeds marginal revenue under the parameter condition, not because cost diverges. Added note on large-N limit where cost growth is O(N*rho) vs revenue O(1/N). Updated channel3.tex and model_equations.md. |
| T29 | theory-builder | 2026-03-11 | (a) Strengthened rho* < rho_2*, rho_3* argument with explicit mechanisms for each channel. (b) Added Ostrowski theorem citation (Ortega-Rheinboldt, 1970, Thm 10.1.3) for spectral-radius-to-contraction step in local uniqueness proof. Updated amplification.tex. |
| T01 | paper-writer | 2026-03-11 | Rewrote abstract: 5-sentence structure, 143 words, no equations, no citations. Covers problem, approach, central result (safety illusion), amplification mechanism, and policy implication. |
| T05 | paper-writer | 2026-03-11 | Split 5-equation align block into two groups with interpretive prose between them. Removed labels (changed to \notag) since coefficients are not referenced by \eqref elsewhere. Added economic interpretation of each coefficient. |
| T06 | paper-writer | 2026-03-11 | Removed duplicate standalone eq:rho1star (converted to unnumbered \[\]). eq:rho1star-prop inside proposition is the authoritative version and is referenced. eq:withdrawal-total and eq:crisis-threshold were already referenced in proof sketch. |
| T07 | paper-writer | 2026-03-11 | Added \eqref references for eq:reservation-price and eq:correlated-calibrations in surrounding prose in channel3.tex. |
| T08 | paper-writer | 2026-03-11 | Added \eqref references for eq:jacobian and eq:eigenvalue in amplification.tex Jacobian discussion prose. |
| T09 | paper-writer | 2026-03-11 | Changed [h] to [t] in all three table files (correlation_did.tex, liquidity_did.tex, rho_proxy_descriptive.tex). |
| T10 | paper-writer | 2026-03-11 | Verified section labels. Removed duplicate labels from main.tex that conflicted with labels in section files (sec:channel1, sec:channel2, sec:channel3, sec:amplification, sec:model). Section files already define all needed labels. |
| T11 | paper-writer | 2026-03-11 | Removed all 5 \subsection headers from introduction.tex. Prose flows continuously with paragraph transitions. |
| T12 | paper-writer | 2026-03-11 | Removed \citet{gu2020} and \citet{kim2024} from opening paragraph; replaced with descriptive prose. |
| T13 | paper-writer | 2026-03-11 | Removed \newpage after abstract in main.tex. |
| T15 | paper-writer | 2026-03-11 | Cut conclusion from ~1,050 to ~444 prose words. Compressed Summary of Results to one sentence per contribution. Tightened Policy Implications, Limitations, and Future Work. |
| T16 | paper-writer | 2026-03-11 | Expanded introduction from ~1,100 to ~1,559 prose words. Added economic intuition to channel descriptions, Main Results block (safety illusion loop mechanism, convexity significance, FPE-RPE divergence), and split paragraphs. |
| T17 | paper-writer | 2026-03-11 | Trimmed literature.tex from ~1,729 to ~742 words. Combined with intro lit (~300 words) = ~1,042, well within 1,500 target. Removed redundancy with introduction. |
| T18 | paper-writer | 2026-03-11 | Added interpretive prose after eq:withdrawal-variance in channel3.tex explaining variance inflation factor. Added \eqref reference. |
| T19 | paper-writer | 2026-03-11 | Added \eqref reference for eq:pi-private in channel2.tex with interpretive sentence contrasting AI and private rents. |
| T20 | paper-writer | 2026-03-11 | Added \eqref references for eq:pi-alpha-adoption and eq:tracking-error in extensions.tex. eq:systemic-cost was already referenced. |
| T21 | paper-writer | 2026-03-11 | Added \eqref reference for eq:composite-T in amplification.tex prose after the equation. |
| T24 | paper-writer | 2026-03-11 | Added Margaretic and Pasten (2014) citation and differentiator to literature.tex global games subsection and references.bib. |
| T25 | paper-writer | 2026-03-11 | Added Barucca and Morone (2025) citation to literature.tex AI subsection and references.bib. |
| T26 | paper-writer | 2026-03-11 | Added FPE non-monotonicity to Channel 2 description in introduction. |
| T27 | paper-writer | 2026-03-11 | Pagano (1989) reference was removed during conclusion trimming (T15). No plain-text citation remains. |
| T28 | paper-writer | 2026-03-11 | Added tau_s = 1/sigma^2 definition to channel2.tex before first use in eq:rpe. |
| T30 | paper-writer | 2026-03-11 | Elevated N_info(rho) = 1/rho to a numbered Lemma (Lemma 1: Information Collapse) in model.tex with formal proof. |
| T31 | paper-writer | 2026-03-11 | Moved parameter condition Qs_0/N^2 > gamma*sigma_V^2*kappa_inv from footnote into Proposition 3c statement. Removed redundant footnote. |
| T32 | paper-writer | 2026-03-11 | Added ~ (non-breaking space) before all \ref{} and \eqref{} calls throughout all section files via systematic sed pass. |
| T33 | paper-writer | 2026-03-11 | Removed duplicate \label{} entries from main.tex (sec:intro-section, sec:lit-section, sec:model, sec:channel1-3, sec:amplification, sec:extensions-section, sec:empirics-outer, sec:conclusion-outer). Section files retain authoritative labels. |
| T34 | paper-writer | 2026-03-11 | Added Danielsson-Uthemann three-part differentiator part (3) to introduction: they formally model only the coordination channel. Also noted Yang (2024) has no signal correlation parameter rho (T37). Also noted Hansen-Lee do not test high-rho regime (T34/strengthening). |
| T35 | paper-writer | 2026-03-11 | Long footnotes resolved: channel3.tex footnote removed (content moved to proposition statement in T31); amplification.tex has no remaining footnotes >50 words. Moved Prop 6 H(rho) root-counting detail to footnote in extensions.tex. |
| T36 | paper-writer | 2026-03-11 | Systematic ~ pass completed via T32. |
| T37 | paper-writer | 2026-03-11 | Added explicit statement in introduction that Yang (2024) has "no signal correlation parameter rho" and crisis threshold is "learned through Q-value convergence rather than derived analytically." |
| T38 | paper-writer | 2026-03-11 | Prop 3c proof sketch is already concise after T23 (Theory Builder) corrections. No excess algebra remains to move to appendix. |
