# Revision Task Queue -- Round 3
Date: 2026-03-12
Source: Consolidated issues from 8 referee reports

## Execution Notes
- Tasks within the same priority and batch can run in parallel unless a dependency is noted.
- "TB" = theory-builder, "PW" = paper-writer, "LG" = literature-guardian, "MV" = model-verifier.
- Input/output paths are relative to /workspaces/ai-finance-paper/.

---

## Priority 1 -- Blocking (must fix before any other work)

### Batch 1A: Theory Tasks (parallel)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-01 | TB | **Strengthen Assumption A1 (binary-action uniqueness transfer).** The current Assumption A1 states that the GP binary-action game has the same critical ratio as the MS linear-quadratic game. Add a formal verification: (a) Write out the GP equilibrium system's Jacobian at the uniqueness boundary. (b) Show that the determinant condition det(J)=0 produces rho_1* = 1/(1+alpha_SC^2) for the binary-action case, or provide numerical verification for 3+ parameter configurations. (c) Resolve the conflicting formula sqrt(2*pi)/(alpha_SC+sqrt(2*pi)) from the working notes -- explain which applies and why. (d) Update Assumption A1 statement to reference the verification. Write the verification in appendix.tex as a new Appendix C. | paper/sections/channel1.tex, paper/sections/appendix.tex, context/model_equations.md (lines 370-465) | paper/sections/channel1.tex (updated A1 statement), paper/sections/appendix.tex (new Appendix C), context/model_equations.md (updated) | None | Large |
| T-02 | TB | **Verify saddle-node non-degeneracy conditions.** The bifurcation argument invokes Guckenheimer-Holmes Theorem 3.4.1 with three non-degeneracy conditions. Explicitly state and verify all three conditions in Appendix B: (1) the zero eigenvalue condition (already done via det(J)=0); (2) the transversality condition d(det(J))/d(rho_eff) != 0 at the bifurcation; (3) the non-degeneracy of the quadratic term in the normal form. For each, provide the computation or a reference to where it is verified. If any condition cannot be verified analytically, provide numerical evidence for the paper's baseline parameters. | paper/sections/amplification.tex, paper/sections/appendix.tex, context/model_equations.md (lines 1803-1823) | paper/sections/appendix.tex (updated Appendix B) | None | Large |
| T-03 | TB | **Address withdrawal correlation approximation.** The claim Corr(W_i, W_j) = rho for binary withdrawal indicators is an approximation exact only at the median threshold. (a) State the median-threshold assumption explicitly in channel3.tex as Assumption A3 (or equivalent). (b) In a footnote or appendix remark, note the tetrachoric correlation formula applies for general thresholds and bound the approximation error: show |Corr(W_i,W_j) - rho| is small for thresholds within one standard deviation of the median. (c) Verify that N_eff monotonicity and convexity survive the exact treatment (or state they hold under A3). | paper/sections/channel3.tex, context/model_equations.md (lines 1076-1079) | paper/sections/channel3.tex (updated with A3), context/model_equations.md (updated) | None | Medium |
| T-04 | TB | **g_1 robustness verification.** The claim that "any alternative g_1 satisfying boundary conditions yields qualitatively identical results" is unverified. (a) Define a one-parameter family g_1^alpha(rho, N_eff) = 1 - (1-rho)*(N_eff/N)^alpha for alpha in {0.5, 1, 2} (concave, linear, convex). (b) For each, verify that the bifurcation inequality rho* < min(rho_i*) holds (analytically if possible, numerically otherwise). (c) Report how rho* varies with alpha. (d) Add the result as a Remark or Corollary after Proposition 9 in amplification.tex. | paper/sections/amplification.tex, context/model_equations.md | paper/sections/amplification.tex (new Remark), context/model_equations.md (updated) | None | Large |

### Batch 1B: Verification (after Batch 1A)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-05 | MV | **Independent verification of T-01 through T-04.** Re-derive the key results from Batch 1A: (a) Check the GP Jacobian determinant computation from T-01. (b) Verify the three saddle-node conditions from T-02. (c) Confirm the tetrachoric correlation bound from T-03. (d) Verify the g_1 robustness computations from T-04. Produce a verification report with pass/fail for each. | Outputs of T-01 through T-04, context/model_equations.md | context/verification_report_r3.md | T-01, T-02, T-03, T-04 | Large |

---

## Priority 2 -- Important (fix in this revision cycle)

### Batch 2A: Theory Tasks (parallel, after Batch 1A)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-06 | TB | **Welfare formula adaptation for binary-action game.** The Angeletos-Pavan (2007) welfare formula applies to continuous-action games. Either (a) re-derive the welfare loss for the GP binary-action setting (W_loss = Prob(inefficient run) * deadweight loss L), or (b) add an explicit assumption that the linear-quadratic welfare approximation applies, with a bound on the approximation error, or (c) present both the AP welfare measure and the binary-action measure as upper and lower bounds. Update channel1.tex Prop 3 and extensions.tex where welfare enters the prisoner's dilemma. | paper/sections/channel1.tex, paper/sections/extensions.tex, context/model_equations.md | paper/sections/channel1.tex, paper/sections/extensions.tex, context/model_equations.md | T-01 (needs verified rho_1*) | Medium |
| T-07 | TB | **Characterise behaviour above rho*.** Add a Remark after Prop 9 (or extend the existing Remark on global uniqueness) stating: (a) By the saddle-node normal form, the interior fixed point ceases to exist for rho > rho* (it collides with the unstable fixed point and both vanish). (b) The corner fixed point (rho_eff=1, N_eff=1) becomes the unique attractor. (c) If this cannot be proved analytically, state it as a conjecture supported by the normal form analysis and verify numerically for baseline parameters. | paper/sections/amplification.tex, context/model_equations.md | paper/sections/amplification.tex (updated Remark) | T-02 | Medium |
| T-08 | TB | **Add transparency statement for trading profit formulas.** In channel2.tex, after eqs for pi_A and pi_P, add a sentence: "These reduced forms obtain in the linear equilibrium of the CARA-normal REE with a continuum of agents (Verrecchia 1982), under the large-N limit where individual agents are price-takers. The approximation is exact in the competitive limit." If this is not exact, state the conditions. | paper/sections/channel2.tex, context/model_equations.md | paper/sections/channel2.tex | None | Small |

### Batch 2B: Writing Tasks -- Introduction and Narrative (parallel, no theory dependencies)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-09 | PW | **Compress introduction five-contribution catalogue.** Replace the enumerated "First... Second... Third..." catalogue with a single paragraph of 3-4 sentences stating the main results in economic (not model-internal) terms. For each of the 2-3 most important results, add one sentence stating the real-world implication. Remove proposition references (reader cannot evaluate them yet). Target: net reduction of ~300 words from this passage. | paper/sections/introduction.tex | paper/sections/introduction.tex | None | Medium |
| T-10 | PW | **Trim channel preview paragraphs in introduction.** Each channel currently gets a full preview paragraph. Reduce each to 1-2 sentences stating the economic insight, not the model mechanics. Remove inline math beyond $\rho$. Target: net reduction of ~200 words. | paper/sections/introduction.tex | paper/sections/introduction.tex | None | Medium |
| T-11 | PW | **Cut backward-looking summary paragraphs at end of each channel section.** Each of channel1.tex, channel2.tex, channel3.tex ends with a paragraph summarising what was just proved. Remove these; keep only the forward-looking transition paragraph. Target: ~100 words saved per section, ~300 total. | paper/sections/channel1.tex, paper/sections/channel2.tex, paper/sections/channel3.tex | Same three files | None | Small |
| T-12 | PW | **Remove redundant amplification loop restatement.** In amplification.tex, after the Jacobian analysis, there is a paragraph restating the feedback loop step-by-step in prose. Remove it -- the loop was already described in the section opener and formalised by the Jacobian. Target: ~80 words saved. | paper/sections/amplification.tex | paper/sections/amplification.tex | None | Small |
| T-13 | PW | **Consolidate D-U comparison to two locations.** The Danielsson-Uthemann differentiation appears in the introduction, model section, channel1.tex, literature review, and conclusion. Remove the comparison from model.tex (Sec 3.2) and conclusion.tex. Keep introduction (headline differentiator, 2-3 sentences max) and literature review (detailed comparison). Sharpen D-U/Hellwig distinction per Theme 34: add clause "D-U discuss Hellwig qualitatively but do not integrate it into their formal theta*(mu) derivation." | paper/sections/model.tex, paper/sections/introduction.tex, paper/sections/literature.tex, paper/sections/conclusion.tex | Same four files | None | Small |
| T-14 | PW | **Consolidate N_eff numerical example.** The N=100, rho=0.1, N_eff~9.2 example appears in both the introduction and channel3.tex. Remove from introduction; keep in Channel 3 where the formula is derived. | paper/sections/introduction.tex, paper/sections/channel3.tex | paper/sections/introduction.tex | None | Small |
| T-15 | PW | **Reduce non-monotonicity interpretation to one paragraph.** In channel1.tex, the non-monotonicity is interpreted three times (proof sketch, interpretive paragraph, wisdom/herding paragraph). Keep only the wisdom/herding paragraph; absorb the key economic content from the other two into it. Target: ~150 words saved. | paper/sections/channel1.tex | paper/sections/channel1.tex | None | Small |
| T-16 | PW | **Rewrite conclusion summary.** Replace the "Summary of Results" paragraph (which restates the introduction) with a single synthesising sentence: "The central finding is that moderate AI signal correlation -- well below the threshold of any individual fragility channel -- is sufficient to destabilise the integrated financial system." Then proceed directly to policy implications. Use freed space for one concrete testable prediction (e.g., the non-monotonicity implies a hump-shaped crisis probability as a function of AI model overlap). This maintains the 500-word minimum. | paper/sections/conclusion.tex | paper/sections/conclusion.tex | None | Small |

### Batch 2C: Writing Tasks -- Citations and Framing (parallel)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-17 | PW | **Add citations to extensions section.** Add references to Katz-Shapiro (1985) and Farrell-Saloner (1985) for technology adoption externalities. Add a sentence positioning the prisoner's dilemma: "The coordination failure in AI adoption resembles the technology adoption externalities studied by Katz and Shapiro (1985) and Farrell and Saloner (1985), with the distinction that the externality here operates through signal correlation rather than network compatibility." Also reference Gans (2023) if the tracking error concept connects to his AI adoption framework. Add bib entries if missing. | paper/sections/extensions.tex, paper/references.bib | paper/sections/extensions.tex, paper/references.bib | None | Small |
| T-18 | PW | **Add amplification positioning citations.** Add 2-3 sentences at the start of the amplification section: "The positive feedback mechanism studied here is structurally analogous to margin spirals (Brunnermeier and Pedersen 2009), liquidity spirals (Shleifer and Vishny 1997), and contagion through interbank links (Allen and Gale 2000). The distinguishing feature is that the trigger is information homogeneity -- the common AI signal -- rather than funding constraints or balance sheet linkages." Add bib entries if missing. | paper/sections/amplification.tex, paper/references.bib | paper/sections/amplification.tex, paper/references.bib | None | Small |
| T-19 | PW | **State Morris-Shin -> Hellwig -> GP intellectual chain.** Add one sentence at the start of Channel 1: "Channel 1 builds on the global games framework of Morris and Shin (1998, 2002), incorporating Hellwig's (2002) result that sufficiently precise public information restores equilibrium multiplicity, applied to the Goldstein and Pauzner (2005) bank-run setting." | paper/sections/channel1.tex | paper/sections/channel1.tex | None | Small |
| T-20 | PW | **Add Verrecchia (1982) citation and Kyle distinction.** (a) In channel2.tex setup, add Verrecchia (1982) as the reference for the CARA-normal GS equilibrium with a continuum of agents. (b) In channel3.tex, state which foundation is inherited: "The market-making framework descends from the Kyle (1985) inventory-management tradition, adapted by Avellaneda and Stoikov (2008), rather than the Glosten and Milgrom (1985) adverse-selection framework." Add bib entries if missing. | paper/sections/channel2.tex, paper/sections/channel3.tex, paper/references.bib | Same files | None | Small |
| T-21 | PW | **Fix orphan and catalogue citations in literature review.** (a) Engage Kleinberg-Raghavan, Peng et al., and Gans (2023) in the cross-channel subsection: add one sentence per paper stating relationship to the present work, or remove from the parenthetical cluster. (b) Engage Acemoglu et al. (2015) in conclusion: "The network fragility results of Acemoglu et al. (2015) suggest that the compound threshold rho* may depend on network topology -- a question we leave for future work." (c) Engage Farboodi et al. (2022): state whether data concentration on large firms increases rho for those firms. (d) Engage BDG (2018): "Our mechanism is distinct: BDG's paradox operates through the composition of learning targets, while ours operates through cross-sectional signal correlation." (e) Specify the Vives (2014) condition that is violated. (f) Expand the Pagano analogy: "analogous to the low-liquidity trap where the expectation of thin markets deters participation, validating the expectation." | paper/sections/literature.tex, paper/sections/conclusion.tex, paper/sections/channel3.tex | Same files | None | Medium |
| T-22 | PW | **Add two-fundamental economic link.** In the amplification section setup (before the mappings), add 2-3 sentences: "The three channels operate on different fundamentals: theta (bank asset quality) in Channel 1 and V (risky asset value) in Channels 2-3. The economic link is that bank crises degrade collateral values and destroy trading opportunities in the risky asset market, providing the channel through which theta* affects V-space decisions. Formally, we capture this through the discount factor in g_2, which reduces the expected value of private information about V when crisis probability is high." | paper/sections/amplification.tex | paper/sections/amplification.tex | None | Small |

### Batch 2D: Writing Tasks -- Relevance and Policy (parallel)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-23 | PW | **Develop testable implications.** Add a subsection to the empirical section (or a new subsection 8.X "Testable Predictions") with 2-3 specific predictions: (1) Non-monotonicity: as AI model overlap (measured by portfolio return correlation or forecast revision correlation) increases, crisis probability first decreases then increases -- testable via panel regression with a quadratic term. (2) FPE-RPE divergence: AI adoption improves forecast accuracy (FPE) while reducing the information content of prices for real decisions (RPE) -- testable by comparing forecast accuracy with real investment sensitivity to prices. (3) N_eff collapse: markets with higher AI penetration among market makers exhibit higher bid-ask spread comovement -- testable via cross-sectional variation in algorithmic market-making share. For each, name data sources (CRSP, TAQ, I/B/E/S, 13F). | paper/sections/extensions.tex or paper/sections/empirics.tex, context/research_plan_final.md | paper/sections/empirics.tex (or new subsection) | None | Medium |
| T-24 | PW | **Scale back policy claims.** (a) In extensions.tex, replace "mandatory diversity requirements are necessary" with "diversity requirements that bound aggregate signal correlation below rho* are welfare-improving under the stated conditions." (b) Add a paragraph discussing alternative instruments: Pigouvian taxes on signal correlation, subsidies to private research, position limits calibrated to N_eff. Note implementation challenges (measuring rho_i in practice). (c) In conclusion.tex, apply the same qualifier and add one sentence: "The optimal regulatory instrument depends on observability and enforcement costs not modelled here." | paper/sections/extensions.tex, paper/sections/conclusion.tex | Same files | None | Small |
| T-25 | PW | **Strengthen Channel 3 empirical grounding.** Add 1-2 sentences citing evidence of AI/algorithmic convergence among market makers. Options: (a) Danielsson-Shin-Zigrand (2012) as precedent for VaR model homogeneity; (b) Kirilenko et al. (2017) flash crash evidence on correlated algorithmic withdrawal; (c) BIS/FSB reports on AI in market-making. If no specific citation is available, state: "While direct evidence on AI calibration correlation among market makers is limited, the VaR model homogeneity documented by Danielsson et al. (2012) and the correlated algorithmic withdrawal observed during flash crashes (Kirilenko et al. 2017) suggest the mechanism is empirically plausible." | paper/sections/channel3.tex, paper/references.bib | paper/sections/channel3.tex, paper/references.bib | None | Small |
| T-26 | PW | **Add FPE-RPE actionable implication.** In channel2.tex, after the FPE-RPE divergence discussion, add 2-3 sentences: "The divergence suggests that regulators should supplement forecast accuracy metrics with measures of information novelty -- e.g., the conditional mutual information between prices and fundamentals after conditioning on the common AI signal. A declining ratio of RPE to FPE would signal increasing redundancy in price signals even as forecast accuracy improves." | paper/sections/channel2.tex | paper/sections/channel2.tex | None | Small |

### Batch 2E: Writing Tasks -- Remaining Cleanup (parallel)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-27 | PW | **Add scope limitations.** Add to the limitations subsection in conclusion.tex: (a) "The equicorrelation assumption (a single rho for all AI-equipped agents) is a significant simplification. In practice, rho varies across firms, models, and asset classes. A bimodal distribution of rho could produce fragility in a subset of agents even when the aggregate rho is below rho*." (b) "Agents do not learn about rho from prices. In a dynamic model, inference about the degree of signal correlation could alter equilibrium strategies." | paper/sections/conclusion.tex | paper/sections/conclusion.tex | None | Small |
| T-28 | PW | **Compress model timing subsection.** Reduce the 4-sentence timing subsection to 1 sentence or fold into agent-types. | paper/sections/model.tex | paper/sections/model.tex | None | Small |
| T-29 | PW | **Add tracking error robustness footnote.** Add to extensions.tex: "The multiplicative form of the tracking error cost ensures strategic complementarity. The qualitative result rho_NE > rho_SO holds for any specification generating strategic complementarity in adoption, including additive costs with sufficient cross-partial in (rho_i, rho_bar)." | paper/sections/extensions.tex | paper/sections/extensions.tex | None | Small |
| T-30 | PW | **Migrate Channel 1 withdrawal derivation to appendix.** Move the three equations (eq:withdrawal-ai, eq:withdrawal-total, eq:crisis-threshold) and their derivation from channel1.tex to appendix.tex as Appendix D. Keep only the crisis threshold condition in the main text with a reference to the appendix. This addresses the equation density issue and trims channel1.tex toward the 1,500-word target. | paper/sections/channel1.tex, paper/sections/appendix.tex | Same files | None | Medium |

---

## Priority 3 -- Minor (fix if time permits)

### Batch 3A: Final Polish (parallel)

| ID | Assignee | Description | Input Files | Output Files | Dependencies | Complexity |
|----|----------|-------------|-------------|--------------|--------------|------------|
| T-31 | PW | **Cut Dynamic Extensions subsection.** Remove the "Discussion of Dynamic Extensions" subsection from extensions.tex entirely (or compress to 1-2 sentences absorbed into the preceding subsection). The conclusion's future work section covers the same ground. | paper/sections/extensions.tex | paper/sections/extensions.tex | None | Small |
| T-32 | PW | **Verify Prop 2 regularity condition.** Check the regularity condition against baseline parameters (lambda=0.5, alpha_SC=1, rho_1*=0.5). Add a sentence: "For the baseline parameters, the condition is satisfied for sigma in [X, Y], confirming that the non-monotonicity obtains for an open set of parameters." | paper/sections/channel1.tex | paper/sections/channel1.tex | T-01 | Small |
| T-33 | PW | **Sharpen future work directions.** For the most tractable direction (dynamic rho), add: "A dynamic model with rho_t following a diffusion process driven by AI adoption rates would predict whether the bifurcation threshold is approached gradually or crossed discontinuously. The key modelling choice is whether rho is a state variable (with inertia from training data overlap) or a control variable (adjustable through model selection). The testable prediction: if rho is a state variable, crisis risk increases with the persistence of AI model architectures." | paper/sections/conclusion.tex | paper/sections/conclusion.tex | None | Small |
| T-34 | PW | **Passive voice cleanup.** Search for "it is shown that," "it can be verified," "it is important to note," "the result is established." Convert to active voice ("we show," "the proof verifies," "Proposition X establishes"). Remove "The economic intuition is that" and start with the actual intuition. | All paper/sections/*.tex files | Same files | None | Small |
| T-35 | PW | **Verify empirical section reference.** Check that introduction references to "Section 8/9" (empirical evidence) point to an existing, populated section. If the section is preliminary, add the qualifier "preliminary motivating evidence." | paper/sections/introduction.tex, paper/sections/empirics.tex | paper/sections/introduction.tex | None | Small |
| T-36 | PW | **Move Hansen-Lee citation to Channel 1.** The Hansen-Lee (2025) finding directly supports the "wisdom of AI" effect at low rho. Add a citation in channel1.tex near the non-monotonicity discussion: "Hansen and Lee (2025) find that independently queried AI agents reduce herding, consistent with the low-rho regime of Proposition 2." | paper/sections/channel1.tex | paper/sections/channel1.tex | None | Small |
| T-37 | PW | **Fix "coordination trap" terminology.** In extensions.tex, replace "coordination trap" with "prisoner's dilemma" for consistency with the established framing. | paper/sections/extensions.tex | paper/sections/extensions.tex | None | Small |
| T-38 | PW | **Verify tau/tau_s consistency.** Search all tex files for tau, tau_s, tau_P, tau_v usage. Ensure the notation table in model.tex covers all variants. Fix any inconsistencies. | paper/sections/*.tex | Same files | None | Small |

---

## Assignment Summary

### Theory Builder (T-01 through T-04, T-06 through T-08): 7 tasks
- **Batch 1A (parallel, start immediately):** T-01, T-02, T-03, T-04
- **Batch 2A (after 1A):** T-06, T-07, T-08

### Model Verifier (T-05): 1 task
- **Batch 1B (after 1A):** T-05

### Paper Writer (T-09 through T-38): 27 tasks
- **Batch 2B (parallel, start immediately):** T-09, T-10, T-11, T-12, T-13, T-14, T-15, T-16
- **Batch 2C (parallel, start immediately):** T-17, T-18, T-19, T-20, T-21, T-22
- **Batch 2D (parallel, start immediately):** T-23, T-24, T-25, T-26
- **Batch 2E (parallel, start immediately):** T-27, T-28, T-29, T-30
- **Batch 3A (after all above):** T-31 through T-38

### Parallelisation
- **All Batch 1A tasks** (T-01 to T-04) can run in parallel.
- **All PW Batch 2B-2E tasks** (T-09 to T-30) can run in parallel with Batch 1A (no theory dependencies except T-06, T-07 which wait).
- **T-05** (verification) must wait for T-01 to T-04.
- **T-06, T-07** must wait for T-01, T-02 respectively.
- **T-32** must wait for T-01 (needs verified rho_1*).
- **Batch 3A** can start as soon as Batch 2 is complete.

### Critical Path
T-01/T-02/T-03/T-04 (parallel) -> T-05 (verification) -> T-06/T-07 -> Final check

The PW tasks (T-09 to T-30) run on a parallel track and do not block or depend on the theory tasks (except T-32).

---

## Completed Tasks (from prior rounds)
| ID | Completed by | Date | Notes |
|----|-------------|------|-------|
| R01 | theory-builder | 2026-03-11 | Saddle-node proof restructured (A3 partially resolved) |
| R02 | theory-builder | 2026-03-11 | Assumption A1 introduced (A2 partially resolved) |
| R04 | paper-writer | 2026-03-11 | Barucca-Morone bib fix (C1/C2 resolved) |
| R05 | paper-writer | 2026-03-11 | N_{\emph{info}} -> N_{\text{info}} (A8/B1 resolved) |
| R08 | theory-builder | 2026-03-11 | k_A/k_P expressed in primitives (A6 partially resolved) |
| R09 | theory-builder | 2026-03-11 | g_1 labelled as Assumption A2 (A7 partially resolved) |
| R10 | paper-writer | 2026-03-11 | Channel 2 trimmed (B5 resolved) |
| R11 | paper-writer | 2026-03-11 | Extensions trimmed (B6 resolved) |
| R12 | paper-writer | 2026-03-11 | Lit review expanded from intro material (B7 resolved) |
| R13 | paper-writer | 2026-03-11 | Intro inline math reduced (B8 partially resolved) |
| R14 | paper-writer | 2026-03-11 | Prop 8(iii) kappa_sys bound added (A10 resolved) |
| R15 | paper-writer | 2026-03-11 | rho_1* numbered equation (A1/B10 resolved) |
| R16 | paper-writer | 2026-03-11 | RPE qualifier added (C3 resolved) |
| R19 | paper-writer | 2026-03-11 | V vs theta distinction added (A14 partially resolved) |
| R28 | paper-writer | 2026-03-11 | lambda_1 renamed to ell_1 (A18 resolved) |
| R03 | paper-writer | 2026-03-11 | Amplification restructured with appendix (B2/B3/B4 largely resolved) |
| R06 | paper-writer | 2026-03-11 | All unreferenced equations now referenced (A4 resolved) |
| R07 | paper-writer | 2026-03-11 | Jacobian coefficients labelled (A5 resolved) |
| T-09 | paper-writer | 2026-03-12 | Introduction five-contribution catalogue compressed to 3-sentence results paragraph |
| T-10 | paper-writer | 2026-03-12 | Channel preview paragraphs trimmed to 1-2 sentences each |
| T-11 | paper-writer | 2026-03-12 | Backward-looking summary paragraphs cut from all three channel sections |
| T-12 | paper-writer | 2026-03-12 | Redundant amplification loop restatement removed from Jacobian subsection |
| T-13 | paper-writer | 2026-03-12 | D-U comparison consolidated to introduction + literature review; removed from model.tex and conclusion.tex; Hellwig distinction sharpened |
| T-14 | paper-writer | 2026-03-12 | N_eff numerical example removed from introduction; kept in channel3.tex |
| T-15 | paper-writer | 2026-03-12 | Proof sketch interpretation compressed; wisdom/herding paragraph retained as primary |
| T-16 | paper-writer | 2026-03-12 | Conclusion summary replaced with synthesising sentence + testable prediction |
| T-17 | paper-writer | 2026-03-12 | Katz-Shapiro (1985), Farrell-Saloner (1985), Gans (2023) added to extensions.tex; bib entries added |
| T-18 | paper-writer | 2026-03-12 | Brunnermeier-Pedersen, Shleifer-Vishny, Allen-Gale positioning added to amplification.tex; bib entries added |
| T-19 | paper-writer | 2026-03-12 | Morris-Shin -> Hellwig -> GP chain stated at start of Channel 1 |
| T-20 | paper-writer | 2026-03-12 | Verrecchia (1982) added to channel2.tex; Kyle vs GM distinction added to channel3.tex; bib entry added |
| T-21 | paper-writer | 2026-03-12 | Orphan citations engaged: Kleinberg-Raghavan, Peng et al., Gans, Acemoglu, Farboodi et al., BDG, Vives, Pagano |
| T-22 | paper-writer | 2026-03-12 | Two-fundamental economic link (theta vs V) added before channel mappings in amplification.tex |
| T-23 | paper-writer | 2026-03-12 | Testable Predictions subsection added to empirics.tex with three specific predictions and data sources |
| T-24 | paper-writer | 2026-03-12 | Policy claims scaled back in extensions.tex and conclusion.tex; alternative instruments discussed |
| T-25 | paper-writer | 2026-03-12 | Channel 3 empirical grounding added: DSZ, Kirilenko et al., Liu et al., FSB; bib entries added |
| T-26 | paper-writer | 2026-03-12 | FPE-RPE actionable implication added to channel2.tex |
| T-27 | paper-writer | 2026-03-12 | Equicorrelation and learning-about-rho limitations added to conclusion.tex |
| T-28 | paper-writer | 2026-03-12 | Timing subsection compressed to one sentence folded into agent-types subsection |
| T-29 | paper-writer | 2026-03-12 | Tracking error robustness footnote added to extensions.tex |
| T-30 | paper-writer | 2026-03-12 | Withdrawal derivation (eqs withdrawal-ai, withdrawal-total) migrated to Appendix D |
| T-31 | paper-writer | 2026-03-12 | Dynamic Extensions subsection removed from extensions.tex |
| T-32 | paper-writer | 2026-03-12 | Regularity condition verified for baseline parameters; sigma in (0, 0.141) |
| T-33 | paper-writer | 2026-03-12 | Dynamic rho future work direction sharpened with state vs control variable distinction |
| T-34 | paper-writer | 2026-03-12 | Passive voice audit: no instances of flagged constructions found (prior passes resolved) |
| T-35 | paper-writer | 2026-03-12 | Empirical section reference verified: points to existing populated section with "motivating evidence" qualifier |
| T-36 | paper-writer | 2026-03-12 | Hansen-Lee (2025) citation added to Channel 1 near wisdom-of-AI discussion |
| T-37 | paper-writer | 2026-03-12 | "coordination trap" replaced with "prisoner's dilemma" in extensions.tex |
| T-38 | paper-writer | 2026-03-12 | tau/tau_s/tau_P/tau_v notation verified consistent across all sections; notation table covers all primitives |
