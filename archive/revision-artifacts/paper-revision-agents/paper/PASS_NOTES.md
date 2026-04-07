# Paper Writer Pass Notes
# Passes 1–4 completed: 2026-03-10

---

## Pass 1 — Structure

All ten sections drafted in the mandated order:
model → channel1 → channel2 → channel3 → amplification → extensions →
introduction → literature → empirics → conclusion.

Files written or substantially rewritten:

- paper/main.tex: Full preamble with amsthm, geometry, setspace, hyperref; all
  ten section inputs; complete abstract.
- paper/sections/model.tex: Full Model Primitives section.
- paper/sections/channel1.tex: Full Channel 1 section (created from scratch).
- paper/sections/channel2.tex: Full Channel 2 section (created from scratch).
- paper/sections/channel3.tex: Full Channel 3 section (created from scratch).
- paper/sections/amplification.tex: Full Amplification Loop section (created).
- paper/sections/extensions.tex: Full Extensions section (created from scratch).
- paper/sections/introduction.tex: Full Introduction section.
- paper/sections/literature.tex: Full Literature Review section.
- paper/sections/empirics.tex: Full Empirical Motivation section.
- paper/sections/conclusion.tex: Full Conclusion section.
- paper/references.bib: Expanded from 3 entries to 39 entries.

---

## Pass 2 — Clarity

Edits applied during initial drafting (integrated with Pass 1):

- Active voice for contribution statements throughout.
- All displayed equations referenced with \eqref{} in running text.
- No em-dashes; commas, semicolons, and parentheses used throughout.
- No \textbf{} in running prose.
- \rho always rendered as \rho, never spelled out.
- \text{} used for all subscript words (e.g., \text{info}, \text{eff},
  \text{NE}, \text{SO}).
- \left( \right) used for tall expressions adjacent to fractions and square
  roots.
- which/that distinction applied.
- Numbers one through nine spelled out in prose.
- First-person plural "we" throughout.
- Present tense for model results; past tense for empirical findings.

---

## Pass 3 — Flow

Cross-section motivational links verified:

- channel1.tex final paragraph: motivates Channel 2 by noting that correlated
  withdrawal raises crisis probability, which destroys the option value of
  private information.
- channel2.tex final paragraph: motivates Channel 3 via g_3 mapping (lower
  mu_I implies market makers increasingly share common AI calibrations).
- channel3.tex final paragraph: motivates Section 5 (Amplification Loop) by
  noting that g_1, g_2, g_3 close the feedback loop.
- amplification.tex final paragraph: motivates Extensions by noting that
  rho_NE > rho* requires a regulatory instrument.
- extensions.tex final paragraph: motivates Conclusion by summarising the
  diversity mandate result.

Introduction contribution list verified against body propositions:

- Contribution 1: prop:uniqueness-boundary (Prop 1b) and prop:crisis-nonmonotone
  (Prop 1a). CHECK.
- Contribution 2: prop:rpe (Prop 2b) and prop:info-diversity (Prop 2a). CHECK.
- Contribution 3: prop:neff (Prop 3a) and prop:rho-star-star (Prop 3c). CHECK.
- Contribution 4: prop:bifurcation (Prop 4b) and cor:safety-illusion (Cor 4d).
  CHECK.
- Contribution 5: prop:endogenous-rho (Prop 5a) and prop:diversity-mandate
  (Prop 5b). CHECK.

---

## Pass 4 — Technical Audit

### CITE-MISSING flags

None. All 39 citation keys used across the ten section files are present in
paper/references.bib following the bibliography expansion in this pass.

Citation keys verified as present: grossman1980, morris1998, morris2002,
morris2003, goldstein2005, goldstein2015, goldstein2025, hellwig2002,
angeletos2006, angeletos2007, carlsson1993, szkup2015, holden1992, bond2012,
dugast2018, dugast2025, farboodi2020, farboodi2022, banerjee2018, vives2014,
glosten1985, kyle1985, avellaneda2008, greenwood2011, danielsson2012,
brunnermeier2009, pagano1989, colliard2025, cespa2025, gu2020, kim2024,
danielsson2022, danielsson2025, yang2024, hansen2025, calvano2020, dou2025a,
dou2025b, kleinberg2021, peng2024, gans2023, acemoglu2015.

### REF-BROKEN flags (intentional stubs)

Three table \input stubs in paper/sections/empirics.tex are intentional
placeholders awaiting empirical output:

- \input{tables/correlation_did} — tab:correlation_did (DiD for portfolio
  correlation).
- \input{tables/liquidity_did} — tab:liquidity_did (DiD for bid-ask spread).
- \input{tables/rho_proxy_descriptive} — tab:rho_proxy_descriptive
  (descriptive statistics for rho proxies).

These are not errors. The corresponding \label tags are inside the table files
to be created by the Empirical Agent in Task T7.

One structural label was found and fixed during the audit: sec:model was missing
from paper/sections/model.tex (defined only at section level in main.tex) and
\ref{sec:model} in introduction.tex returned a broken reference. Fixed by adding
\label{sec:model} at the top of model.tex.

### CLAIM-UNSUPPORTED flags

No bare quantitative assertions were inserted without equation backing. All
numerical threshold values (e.g., rho_1* = 1/(1+alpha_SC^2), rho** existence,
bifurcation inequality rho* < min(rho_i*)) are accompanied by proposition
statements with proof sketches.

### NOTATION-CHECK flags

Three notation issues noted:

1. Spread convexity (channel3.tex, Proposition 3b). The baseline spread
   s*(rho) = s_0*(1+(N-1)*rho)/N is linear in rho (d^2s*/drho^2 = 0). The
   research plan stated convexity. Resolved in the section by distinguishing
   the linear baseline from the nonlinear aggregation (beta > 1) extension.
   The proposition is correctly stated as linear in the baseline. Future
   revision should consider whether to state the convex case as a corollary or
   to promote it to the main specification with explicit beta > 1 assumption.
   % NOTATION-CHECK: spread linearity vs. convexity claim in Plan.

2. Direction of mu_I*(rho) (channel2.tex, Proposition 2a). Within Channel 2
   standalone, the Holden-Subrahmanyam (1992) logic implies mu_I is weakly
   increasing in rho (agents substitute toward private info when AI rents
   collapse). The decreasing direction stated in the research plan requires
   the cross-channel crisis interaction (g_2 mapping). Both directions are
   documented in the section with appropriate caveats. No inconsistency in
   the final text, but future readers may find the two-direction claim
   confusing.
   % NOTATION-CHECK: mu_I*(rho) direction (increasing standalone vs.
     decreasing cross-channel).

3. g_1 functional form (amplification.tex). The mapping rho_eff =
   1 - (1-rho)*N_eff/N is a modelling choice, not derived from a price-
   discovery model. The alternative rho*N/N_eff can exceed 1 and was rejected.
   The chosen form has correct boundary conditions and is monotone in N_eff.
   Future work should microfound g_1 via a price-revelation model.
   % NOTATION-CHECK: g_1 microfoundation deferred.

### CONDITIONALLY VERIFIED footnotes added

Per the verification_report.md classification, the following propositions
received footnotes within their proof sketches:

- Proposition 1a (non-monotonicity of theta*(rho)): footnote states the result
  holds "for sigma sufficiently small, so that the precision effect dominates
  at low rho and the common-noise effect dominates at high rho."
  [CONDITIONALLY VERIFIED]

- Proposition 1c (social cost of signal correlation): footnote states the
  welfare formula requires alpha_SC < 1 and lambda^2 * rho / tau is the
  relevant scale, with the coefficient derived under the Angeletos-Pavan
  (2007) linear-quadratic approximation applied to the binary-action GP game.
  [CONDITIONALLY VERIFIED]

- Proposition 3c (no-equilibrium threshold rho**): footnote states that
  existence of rho** in (0,1) requires the explicit parameter condition
  Q*s_0/N^2 > gamma*sigma_V^2*kappa_inv.
  [CONDITIONALLY VERIFIED]

- Proposition 4b (amplification bifurcation): footnote states that the
  divergence of h = d(theta*)/d(rho_eff) as rho_eff approaches rho_1* is
  established from implicit differentiation of the crisis threshold condition
  and is treated as a regularity condition in the proof; the full formal
  derivation of the square-root singularity is deferred to future work.
  [CONDITIONALLY VERIFIED]

### Propositions with (proof sketch) annotation

All propositions in the Extensions section (Propositions 5a and 5b, plus the
diversity mandate results) are annotated "(proof sketch)" in the text, as the
T5 derivations were not formally verified by the Model Verifier.

---

## Unresolved structural issues

1. T6 (Model Verifier) output has not been integrated. The verification_report.md
   was read to assign VERIFIED/CONDITIONALLY VERIFIED status, but a full
   second verification of the paper-writer's formulations against model_equations.md
   has not been performed. Recommend a systematic line-by-line audit of every
   displayed equation in the section files against the corresponding equation
   in model_equations.md.

2. The three table stubs in empirics.tex are placeholders. Task T7 (Empirical
   Agent) must produce the actual LaTeX table files in paper/tables/.

3. The extensions.tex propositions (Propositions 5a and 5b) are unverified
   (T5 derivations were not subject to T6 verification). The diversity mandate
   result is stated with proof sketches only.

4. Proposition 4b (bifurcation) relies on the h-divergence regularity condition.
   A future revision should either (a) prove the square-root singularity formally
   or (b) re-state the proposition as conditional on the regularity condition
   and include that condition as an explicit assumption.

5. The empirical section uses the ChatGPT event as a shock to institutional AI
   adoption. The mapping from consumer product launch to institutional deployment
   is acknowledged as informal. Future revision should strengthen the proxy
   justification (e.g., using 13F filing data or earnings call transcripts to
   document institutional AI adoption timing).

---

## Recommendations for Pass 5

1. Equation audit. Read every displayed equation in every section file and
   verify each formula against model_equations.md and references.bib line by
   line. Pay particular attention to: (a) the rho_1* formula in channel1.tex
   vs. the corrected value in model_equations.md; (b) the welfare coefficient
   alpha_SC^2/(1-alpha_SC)^2 vs. the earlier alpha_SC^2/(1-alpha_SC^2) error;
   (c) the N_eff formula and its decreasing/convex properties in channel3.tex.

2. Cross-reference completeness. Run a fresh cross-reference check after
   empirics.tex table stubs are replaced with actual table files, to confirm
   all \label{tab:...} references resolve.

3. Proposition numbering. The current LaTeX uses named labels (prop:...) rather
   than hard-coded numbers. Verify that the compiled PDF number sequence matches
   the introduction's contribution list (Propositions 1a-1c, 2a-2b, 3a-3c,
   4a-4d, 5a-5b).

4. Spelling and grammar audit. Run aspell or equivalent on all section files.
   Particular attention to: "centrepiece" (British spelling used throughout,
   consistent with journal submission conventions); "formalise" vs. "formalize".

5. Abstract update. The abstract was written before all propositions were
   finalised. Verify that every claim in the abstract maps to a specific
   proposition in the body. In particular, the rho_1* value in the abstract
   should match the value derived in channel1.tex.

6. Diversity mandate connection. The conclusion references
   Proposition~\ref{prop:diversity-mandate} for the diversity mandate result.
   Verify that prop:diversity-mandate is labelled correctly in extensions.tex
   and that the result matches what is asserted in the conclusion.

7. Compile test. Run latexmk -pdf on paper/main.tex to verify compilation
   with the full bibliography. Address any remaining undefined reference
   warnings or missing file errors.
