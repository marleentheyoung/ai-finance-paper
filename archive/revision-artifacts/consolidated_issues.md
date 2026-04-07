# Consolidated Issue Tracker
Date: 2026-03-12
Source: 8 referee reports (3 specialist Round 2 + 5 general modes)

---

## Theme 1: Assumption A1 -- Binary-Action Uniqueness Transfer

**Priority: P1 (Blocking)**

The Morris-Shin (2003) uniqueness condition alpha_SC * sqrt(rho/(1-rho)) < 1 is derived for linear-quadratic games. Assumption A1 transfers it to the binary-action Goldstein-Pauzner game without a complete proof. The model_equations.md working notes show the authors struggled with this derivation (conflicting formulas: 1/(1+alpha_SC^2) vs sqrt(2*pi)/(alpha_SC+sqrt(2*pi))). Hellwig (2002) Theorem 1 is cited as justification but applies to continuous-action games. The current "explicit assumption" approach (from Theory Builder R02) is a start but needs strengthening.

**Source reports:** A2, G-02(general), G-01(method), G-03(method)

**What needs to happen:** Either (a) provide a formal proof that the GP binary-action game has the same critical ratio, (b) cite a result establishing equivalence, (c) provide numerical verification for the GP game specifically, or (d) strengthen the current assumption statement with a bound on the approximation error. The method referee notes two conflicting formulas in the working notes that must be resolved.

---

## Theme 2: Assumption A2 -- g_1 Aggregation Form Microfoundation

**Priority: P1 (Blocking)**

The mapping rho_eff = 1 - (1-rho)(N_eff/N) is the critical link from Channel 3 to Channel 1. It is asserted as an assumption with a robustness claim that "any alternative satisfying the same boundary conditions yields qualitatively identical results." This claim is not verified. The functional form determines the strength of the feedback loop and therefore the location of rho*. A different curvature (concave or convex g_1) could shift rho* materially.

**Source reports:** A7, G-01(general), G-02(method), G-08(relevance)

**What needs to happen:** Either (a) derive g_1 from an equilibrium price-impact model, or (b) verify the bifurcation inequality rho* < min(rho_i*) under at least one alternative specification (e.g., concave and convex g_1), or (c) provide an explicit robustness proposition showing the qualitative result survives a parametric family. The current Assumption A2 label (from TB R09) is necessary but insufficient.

---

## Theme 3: Saddle-Node Bifurcation Non-Degeneracy

**Priority: P1 (Blocking)**

The saddle-node bifurcation argument in the amplification section requires three Guckenheimer-Holmes non-degeneracy conditions to be verified. The proof sketch asserts they hold but does not verify them explicitly. The original proof contained a self-contradictory passage (fixed by TB R01), but the non-degeneracy conditions themselves remain unverified. The naive scalar computation gives dG/d(theta*) = 1, not 0. The 2x2 Jacobian approach (from R01) is correct in structure but the conditions need explicit verification.

**Source reports:** A3 (partially resolved by R01), G-04(method), G-07(general)

**What needs to happen:** Explicitly verify all three saddle-node non-degeneracy conditions in Appendix B, or provide numerical evidence that the conditions hold for representative parameter values. The current proof sketch references the conditions but does not check them.

---

## Theme 4: Withdrawal Correlation Approximation (Corr(W_i,W_j) = rho)

**Priority: P1 (Blocking)**

The paper states Corr(W_i, W_j) = rho as an identity, but it is an approximation that is exact only when the withdrawal threshold is at the median of the distribution. For general thresholds, the tetrachoric correlation formula applies and Corr(W_i, W_j) != rho. The N_eff formula inherits this approximation.

**Source reports:** G-04(general), G-07(method)

**What needs to happen:** Either (a) state the median-threshold assumption explicitly and add it as an assumption, (b) derive the exact relationship using the tetrachoric correlation and bound the approximation error, or (c) show that the qualitative results (monotonicity, convexity of N_eff) survive the exact treatment.

---

## Theme 5: Barucca-Morone Citation Integrity

**Priority: P1 (Blocking)**

The bib entry for Barucca-Morone (2025) has fabricated metadata: title "AI in Financial Risk Management: A Survey" in "Journal of Financial Risk Management" does not match the actual paper (arXiv 2501.07489, titled "How Low-Cost AI Universal Approximators Reshape Market Efficiency"). The literature.tex characterisation also mismatches.

**Source reports:** C1, C2

**Status:** RESOLVED by Paper Writer R04 (corrected bib entry and literature.tex characterisation).

---

## Theme 6: Amplification Section Overweight and Equation Density

**Priority: P2 (Important)**

The amplification section was 2,601 words (+801 over 1,800 ceiling) with 12 displayed equation environments (limit: 8). The Jacobian derivation and saddle-node verification were the main sources of bloat.

**Source reports:** B2, B3, B4, G-07(narrative)

**Status:** LARGELY RESOLVED by Paper Writer R03 (Jacobian and saddle-node moved to appendix; section now has 8 displayed equations). Verify current word count is within target.

---

## Theme 7: Introduction Bloat -- Excessive Inline Math and Channel Previews

**Priority: P2 (Important)**

The introduction contains ~15 substantive inline math expressions (signal decomposition, N_eff formula, rho_1* formula), a five-contribution enumerated catalogue with proposition references, and ~500 words of literature discussion. The channel descriptions are full-paragraph previews that duplicate the body. The five-contribution catalogue teaches nothing (terms not yet defined) and creates redundancy.

**Source reports:** B8, B11, B16, G-01(narrative), G-02(narrative), G-12(narrative), G-14(relevance)

**Status:** PARTIALLY RESOLVED (R13 reduced inline math to ~5; R12 moved ~200 words of lit to literature section). Remaining: the five-contribution catalogue and full-paragraph channel previews still create redundancy. The narrative referee flags these as blocking.

**What needs to happen:** (a) Compress the five-contribution catalogue to a single 3-sentence paragraph stating main results in economic (not model-internal) terms. (b) Trim each channel preview from a full paragraph to 1-2 sentences. (c) Add one sentence per contribution stating the real-world implication in plain language.

---

## Theme 8: Redundancy Across Sections

**Priority: P2 (Important)**

Multiple ideas are restated 3-5 times across sections: amplification loop mechanism (4 times), D-U differentiation (5 times), numerical N_eff example (2 places), safety illusion (4 times), non-monotonicity with wisdom/herding framing (5 times). Each channel section ends with a formulaic backward-looking summary paragraph that repeats what was just proved.

**Source reports:** G-03(narrative), G-04(narrative), G-05(narrative), G-06(narrative), G-07(narrative), G-08(narrative), G-10(narrative)

**What needs to happen:** (a) Cut backward-looking summary paragraphs at end of each channel section; keep only forward-looking transitions. (b) Remove the third restatement of the amplification loop (after the Jacobian). (c) Consolidate D-U comparison to introduction + literature review only. (d) Remove duplicate N_eff numerical example from introduction (keep in Channel 3). (e) Reduce non-monotonicity interpretation from three paragraphs to one (keep wisdom/herding framing).

---

## Theme 9: Unreferenced Equations and Equation Labelling

**Priority: P2 (Important)**

Twenty-two displayed equations had labels but were never referenced by \eqref{}. Some core results used unnumbered \[...\] displays. Jacobian coefficients were unnumbered.

**Source reports:** A1, A4, A5, A13, B10

**Status:** RESOLVED by Paper Writer R06 (all 22 labels now referenced), R15 (rho_1* numbered), R07 (Jacobian coefficients labelled in appendix), R22 (local expansion numbered).

---

## Theme 10: Trading Profit Formulas k_A, k_P -- Derivation Transparency

**Priority: P2 (Important)**

The reduced-form trading profit formulas pi_A = k_A*sqrt(1-rho)/mu_A and pi_P = k_P/mu_I use constants that were expressed in terms of primitives (k_A = tau_s/(2*gamma*sigma_u), k_P = tau_P/(2*gamma*sigma_u)) after TB R08. However, these are approximations from the "large N" limit of a Kyle-type model, not exact GS expressions. The reduction requires equilibrium linearity assumptions not stated in the text.

**Source reports:** A6, G-10(general), G-05(method), G-06(method)

**What needs to happen:** Add a statement (inline or footnote) that these are linear-equilibrium approximations valid under the stated CARA-normal setup. The derivation conditions should be explicit even if brief.

---

## Theme 11: Welfare Formula Transfer (Binary vs. Continuous Action)

**Priority: P2 (Important)**

The welfare loss formula W_loss(rho) from Angeletos-Pavan (2007) applies to linear-quadratic games with continuous actions. Channel 1 uses a binary-action GP game. The relevant welfare measure for binary games is the probability of inefficient bank failure times deadweight loss, not quadratic action-dispersion cost.

**Source reports:** G-10(method), G-13(relevance)

**What needs to happen:** Either (a) re-derive the welfare result for the binary-action setting, (b) add an explicit assumption that the linear-quadratic welfare approximation applies with a bound on the error, or (c) replace with a welfare measure native to the GP game (e.g., probability of inefficient run * loss).

---

## Theme 12: Testable Implications Underdeveloped

**Priority: P2 (Important)**

The model produces several predictions (non-monotonicity of theta*, RPE declining, N_eff collapse, safety illusion) but none is developed into a testable empirical statement. No observable proxy for rho is specified. No cross-sectional or event-study design is suggested. The paper does not specify what data pattern would distinguish this model from competitors.

**Source reports:** G-01(relevance), G-04(relevance)

**What needs to happen:** Add a subsection (or expand the empirical section) with 2-3 specific testable predictions: (a) identify observable proxies for rho (portfolio overlap, forecast revision correlation), (b) state predicted relationships (e.g., non-monotonicity implies a hump-shaped crisis probability in the proxy), (c) name data sources and empirical designs.

---

## Theme 13: Policy Claims Overclaimed

**Priority: P2 (Important)**

The diversity mandate recommendation exceeds what the model earns. "Mandatory diversity requirements are necessary" is too strong for a two-period model with exogenous information structure. The paper does not discuss costs of the mandate, alternative instruments (Pigouvian taxes, subsidies to private research, position limits), or implementation feasibility.

**Source reports:** G-02(relevance), G-03(relevance)

**What needs to happen:** (a) Replace "necessary" with "welfare-improving under the stated conditions." (b) Add a paragraph discussing alternative instruments and implementation challenges. (c) Distinguish the model's earned insight (bound rho below rho*) from specific instrument recommendations (not earned).

---

## Theme 14: Extensions Section Citation-Free

**Priority: P2 (Important)**

The extensions section contains zero citations. The prisoner's dilemma in AI adoption has well-known antecedents in the technology adoption externality literature (Katz-Shapiro 1985, Farrell-Saloner 1985) and the tracking error literature. These are not referenced.

**Source reports:** G-01(connections), G-09(general)

**What needs to happen:** Add citations to Katz-Shapiro (1985), Farrell-Saloner (1985), and optionally Gans (2023) within the extensions section where the adoption game is developed. Add a sentence positioning the prisoner's dilemma relative to the technology adoption externality literature.

---

## Theme 15: Amplification Section Citation-Sparse

**Priority: P2 (Important)**

The amplification section has only one economic citation (Danielsson 2022). No existing amplification mechanisms are referenced (Brunnermeier-Pedersen 2009 margin spirals, Allen-Gale 2000 contagion, Shleifer-Vishny 1997 limits of arbitrage). The paper does not explain how its feedback loop differs from these.

**Source reports:** G-05(connections)

**What needs to happen:** Add 2-3 sentences at the start of the amplification section positioning the feedback loop relative to existing amplification mechanisms. State: "Unlike margin spirals (Brunnermeier-Pedersen 2009) or contagion through network links (Allen-Gale 2000), the trigger here is information homogeneity rather than funding constraints or balance sheet linkages."

---

## Theme 16: Two-Fundamental Structure (theta vs V)

**Priority: P2 (Important)**

Channel 1 uses theta ~ Uniform[0,1]; Channels 2-3 use V ~ N(v_bar, 1/tau_v). The amplification loop connects models with different fundamentals. The economic link between the bank-run outcome in theta-space and trading in V-space is not explicit. The mapping g_2 implicitly assumes bank crises destroy trading opportunities.

**Source reports:** A14 (partially resolved by R19), G-08(general)

**Status:** PARTIALLY RESOLVED (R19 added V vs theta distinction). Remaining: the economic assumption that bank crises affect asset markets needs to be stated and defended explicitly, especially at the amplification loop where the channels connect.

**What needs to happen:** Add 2-3 sentences in the amplification section setup explaining the economic link: e.g., "Bank crises degrade collateral values and destroy trading opportunities in the risky asset market, providing the economic channel through which theta* affects V-space decisions."

---

## Theme 17: Literature Review Catalogue Style

**Priority: P2 (Important)**

Several passages adopt "X did A. Y did B. Z did C." format without stating relationships. Orphan citations (Kleinberg-Raghavan, Peng et al., Gans 2023 in cross-channel subsection; Acemoglu et al. 2015 in conclusion; Farboodi et al. 2022) appear once with no stated relationship to the paper.

**Source reports:** G-02(connections), G-11(narrative), G-13(connections), G-14(connections)

**What needs to happen:** (a) Convert catalogue sentences to grouped citations with stated relationships. (b) Either engage orphan citations (one sentence explaining relationship to the present paper) or remove them. (c) Specifically: engage or remove Kleinberg-Raghavan, Peng et al., Farboodi et al.; engage Acemoglu et al. with one sentence on how network topology would interact with the rho mechanism.

---

## Theme 18: RPE Monotonicity Qualifier Missing in Introduction

**Priority: P2 (Important)**

The claim "RPE is monotonically decreasing in rho" omits the qualifier "for c_P > 0" that appears in the proposition.

**Source reports:** C3

**Status:** RESOLVED by Paper Writer R16 (added "for c_P > 0" qualifier).

---

## Theme 19: N_{\emph{info}} Formatting Bug

**Priority: P2 (resolved)**

N_{\emph{info}} used instead of N_{\text{info}} in model.tex.

**Source reports:** A8, B1

**Status:** RESOLVED by Paper Writer R05.

---

## Theme 20: Channel 2-3 Sections Overweight

**Priority: P2 (Important)**

Channel 2 at 1,731 words (+231 over 1,500 ceiling). Extensions at 1,475 words (+275 over 1,200 ceiling).

**Source reports:** B5, B6

**Status:** RESOLVED by Paper Writer R10 (channel2 to ~1,518) and R11 (extensions to ~1,207).

---

## Theme 21: Literature Review Underweight

**Priority: P2 (Important)**

Literature review at 845 words (-155 below 1,000 floor), with ~500 words of literature discussion in the introduction.

**Source reports:** B7

**Status:** RESOLVED by Paper Writer R12 (moved ~200 words from intro; lit review now 1,068).

---

## Theme 22: Global Uniqueness / Behaviour Above rho*

**Priority: P2 (Important)**

Local uniqueness is established below rho* but global uniqueness is not. For rho > rho*, the paper says the stable interior fixed point "may be" absorbed by the unstable manifold. The word "may" is doing heavy lifting. The bifurcation narrative requires knowing what the system transitions to.

**Source reports:** G-05(general), G-09(method)

**What needs to happen:** Add a remark characterising what happens above rho*. Either (a) prove the corner fixed point is the unique attractor for rho > rho*, (b) provide numerical evidence, or (c) explicitly state this as a conjecture supported by the saddle-node normal form.

---

## Theme 23: Missing Intellectual Chains and References

**Priority: P2 (Important)**

Several intellectual chains are implicit: Morris-Shin -> Hellwig -> Goldstein-Pauzner backbone of Channel 1 never stated as a chain. Kyle vs Glosten-Milgrom distinction unstated. Missing references: Verrecchia (1982) for CARA-normal GS equilibrium. Various vague connectors (Vives condition unspecified, BDG relationship unstated, Pagano analogy imprecise).

**Source reports:** G-03(connections), G-04(connections), G-06(connections), G-07(connections), G-08(connections), G-11(connections)

**What needs to happen:** (a) Add one sentence at start of Channel 1 stating the MS->Hellwig->GP chain. (b) Add Verrecchia (1982) citation in Channel 2 setup. (c) State which foundation (Kyle vs GM) Channel 3 inherits. (d) Sharpen vague connectors: specify Vives condition, state BDG relationship explicitly, expand Pagano analogy.

---

## Theme 24: Dynamic Extensions Subsection Redundant

**Priority: P3 (Minor)**

The "Discussion of Dynamic Extensions" subsection (~170 words) is vague and duplicates the conclusion's future work section.

**Source reports:** B6, G-09(narrative), G-11(relevance)

**What needs to happen:** Cut entirely or compress to 1-2 sentences folded into the preceding subsection.

---

## Theme 25: Conclusion Summary Restates Introduction

**Priority: P3 (Minor)**

The conclusion's "Summary of Results" paragraph is near-verbatim restatement of the introduction. A good conclusion synthesises rather than re-summarises.

**Source reports:** G-10(narrative)

**What needs to happen:** Replace the summary subsection with a single synthesising sentence, then proceed directly to policy implications.

---

## Theme 26: Prop 2 Regularity Condition Robustness

**Priority: P3 (Minor)**

The regularity condition on sigma for the non-monotonicity result is stated as "sufficient but not necessary." The robustness to the parameter space is not established. The condition is not checked against the numerical example parameters.

**Source reports:** A9, G-06(general), G-15(method)

**What needs to happen:** Verify the condition is satisfied for the paper's numerical example (lambda=0.5, alpha_SC=1). Add a sentence stating whether the non-monotonicity is generic (open set of parameters) or parametrically fragile.

---

## Theme 27: Prop 8(iii) Conditional Claim

**Priority: P3 (Minor -- partially resolved)**

Prop 8(iii) claims rho^NE > rho* "when kappa_sys is large enough" without quantifying.

**Source reports:** A10

**Status:** PARTIALLY RESOLVED by Paper Writer R14 (added explicit kappa_sys* bound). Verify the bound is stated in the proposition itself.

---

## Theme 28: Channel 3 Empirical Grounding

**Priority: P2 (Important)**

Channel 3 has the weakest real-world grounding. No citation documents that market-making firms use similar AI models or that their calibration errors are correlated. Channels 1-2 can point to Gu et al. (2020) and Kim et al. (2024); Channel 3 has no analogous evidence.

**Source reports:** G-05(relevance)

**What needs to happen:** Find and cite evidence of convergent AI use among market makers (industry reports, practitioner surveys, or academic papers on algorithmic trading homogeneity). Alternatively, strengthen the connection to Danielsson-Shin-Zigrand (2012) evidence on VaR model homogeneity as a precedent.

---

## Theme 29: Tracking Error Cost Functional Form

**Priority: P3 (Minor)**

The tracking error cost TE_i = c_TE(1-rho_i)*rho_bar is imposed without economic derivation. The multiplicative form ensures strategic complementarity by construction. The prisoner's dilemma may not survive alternative specifications.

**Source reports:** G-09(general), G-06(relevance), G-11(method)

**What needs to happen:** Add a footnote or remark acknowledging that the functional form is chosen for tractability, noting that the strategic complementarity is a consequence of the multiplicative structure, and stating that the qualitative result (rho_NE > rho_SO) holds for any specification generating strategic complementarity in rho.

---

## Theme 30: Notation Inconsistencies

**Priority: P3 (Minor -- partially resolved)**

tau vs tau_s used interchangeably. Subscript conventions not fully unified. lambda_1 eigenvalue vs lambda AI fraction conflict.

**Source reports:** A17, A18

**Status:** LARGELY RESOLVED (R28 renamed lambda_1 to ell_1; R27 added notation table; R19 added V vs theta note). Remaining: verify tau/tau_s consistency throughout.

---

## Theme 31: Equation Density in Channel 1

**Priority: P3 (Minor)**

Three consecutive displayed equations (lines 11-21) with minimal prose. The withdrawal fraction derivation is mechanical.

**Source reports:** A11, B13

**Status:** DEFERRED (R20 -- migrate to appendix). Appendix.tex exists; this migration is now feasible.

---

## Theme 32: Passive Voice and Filler Phrases

**Priority: P3 (Minor)**

~8-10 passive constructions ("it is shown that," "it can be verified"). One instance of "The economic intuition is that" (a crutch phrase).

**Source reports:** G-16(narrative)

**What needs to happen:** Convert passive constructions to active voice in a final editing pass.

---

## Theme 33: Model Section Timing Subsection

**Priority: P3 (Minor)**

The timing subsection is four sentences, two of which are trivial. Could be compressed to one sentence.

**Source reports:** G-14(general), G-13(method)

**What needs to happen:** Compress to one sentence or fold into agent-types subsection.

---

## Theme 34: D-U Hellwig Integration Distinction

**Priority: P3 (Minor)**

The distinction that D-U do not integrate Hellwig (2002) into their formal model is implicit. One clause would sharpen it.

**Source reports:** C4

**What needs to happen:** Add a clause in the introduction's D-U comparison: "Danielsson-Uthemann discuss the Hellwig (2002) multiplicity result qualitatively but do not integrate it into their formal theta*(mu) derivation."

---

## Theme 35: Future Work Directions Generic

**Priority: P3 (Minor)**

Three future directions stated at high abstraction. No concrete modelling choices or specific predictions specified.

**Source reports:** G-12(general), G-18(narrative), G-11(relevance)

**What needs to happen:** For at least one direction, name the specific modelling choice and the prediction it would generate.

---

## Theme 36: Empirical Section Reference

**Priority: P3 (Minor)**

The introduction references "Section 8/9" for motivating evidence. If the section exists, verify the reference. If empirics are incomplete, qualify the reference.

**Source reports:** G-15(general), G-10(relevance)

**What needs to happen:** Verify the empirical section exists and is properly referenced. If incomplete, add "preliminary" qualifier.

---

## Theme 37: Equicorrelation Limitation

**Priority: P3 (Minor)**

The single-rho assumption (all AI agents have same rho) is a significant abstraction not acknowledged. Heterogeneous rho across firms/assets could produce different welfare implications.

**Source reports:** G-12(method), G-07(relevance)

**What needs to happen:** Add 1-2 sentences to the limitations subsection acknowledging single-rho as a simplification and noting that heterogeneous rho is a natural extension.

---

## Conflict Notes

**Conflict 1:** Narrative referee says introduction is bloated (P1 blocking -- cut five-contribution catalogue and channel previews). Relevance referee says introduction needs more real-world implications per contribution (P2 -- add plain-language implications). **Resolution:** Compress the catalogue but add one-sentence real-world implications for the 2-3 most important results. Net reduction, not expansion.

**Conflict 2:** Narrative referee says conclusion summary should be cut (restates introduction). Presentation referee says conclusion is 14 words below 500 minimum. **Resolution:** Replace summary paragraph with synthesis sentence; use freed space for a concrete testable prediction, maintaining the word count.

**Conflict 3:** Narrative referee says lit review uses catalogue style (cut). Presentation referee says lit review is underweight (expand). **Resolution:** Both are resolved by replacing catalogue sentences with engaged citations -- fewer words per paper but more intellectual content. Already partially addressed by R12.
