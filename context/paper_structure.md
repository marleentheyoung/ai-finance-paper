# Paper Structure Map

---

## Section 1: Introduction

**Subsections:**
1. Motivating observation (AI model convergence and the rho primitive)
2. Preview of the three channels and the amplification result
3. Contribution summary and relation to the literature
4. Paper outline

**Key results to present:**
- Preview of Proposition 4 (Bifurcation): rho* < min(rho_1*, rho_2*, rho_3*) -- the "safety illusion" result
- Preview of the non-monotonicity of fragility in rho across all channels

**Literature to cite:**
- Gu-Kelly-Xiu (2020, RFS): empirical evidence that ML methods converge on the same predictors (motivating rho -> 1)
- Kim-Muhn-Nikolaev (2024, arXiv): GPT-4 produces near-identical financial analyses (motivating belief homogenisation)
- Danielsson-Macrae-Uthemann (2022, JBF): qualitative argument that AI homogenises risk perceptions -- claim: this project formalises their qualitative insights
- Danielsson-Uthemann (2025, JFS): formal model of AI-driven coordination failure via mu -- claim: complementary but distinct primitive (rho vs. mu)
- Yang (2024, WP): RL-based AI coordination in global games -- claim: complementary computational approach vs. analytical characterisation
- Goldstein-Huang-Yang (2025, ARFE): fragility survey -- claim: this project contributes a specific AI-driven multi-channel model to the framework they survey

**Differentiators to state:**
- From Danielsson-Uthemann (2025): rho (signal correlation, intensive margin) vs. mu (AI penetration, extensive margin); three-channel integration vs. single-channel model
- From Yang (2024): analytical characterisation vs. RL simulation
- From Dou-Goldstein-Ji (2025a,b): information-theoretic mechanism vs. RL-based collusion
- From Danielsson-Macrae-Uthemann (2022): formal equilibrium model vs. qualitative narrative

**Handoff from:** All phases (contribution framing requires the complete set of results)

---

## Section 2: Literature Review

**Subsections:**
1. Global games and coordination failure (Morris-Shin, Hellwig, Goldstein-Pauzner, Angeletos-Pavan, Yang, Danielsson-Uthemann)
2. Information acquisition and price efficiency (Grossman-Stiglitz, Holden-Subrahmanyam, Goldstein-Yang, Bond-Edmans-Goldstein, Dugast-Foucault, Farboodi-Veldkamp)
3. Market making and liquidity fragility (Kyle, Glosten-Milgrom, Avellaneda-Stoikov, Brunnermeier-Pedersen, Greenwood-Thesmar, Danielsson-Shin-Zigrand, Pagano, Cespa-Vives, Colliard-Foucault-Lovo)
4. AI and financial markets (Danielsson-Macrae-Uthemann, Dou-Goldstein-Ji, Calvano et al., Hansen-Lee)

**Key results to present:**
- No formal results; this section positions the paper relative to each literature strand

**Literature to cite:**

*Subsection 1:*
- Morris-Shin (1998, 2002): established uniqueness in global games via heterogeneous private signals
- Hellwig (2002): proved that precise public information reinstates multiplicity -- the formal mechanism underlying Channel 1
- Goldstein-Pauzner (2005): applied global games to bank runs -- the framework being extended
- Angeletos-Pavan (2007): welfare cost of public information in coordination games -- the welfare framework used
- Angeletos-Hellwig-Pavan (2006): endogenous signals can restore multiplicity -- related but distinct (policy signaling vs. technology adoption)
- Szkup-Trevino (2015): endogenous information acquisition in global games -- uniqueness conditions may break under correlated AI signals
- Yang (2024): AI coordination via RL in global games -- claim: computational approach, no signal correlation
- Danielsson-Uthemann (2025, JFS): formal model with theta*(mu) -- claim: distinct primitive (mu vs. rho), single channel

*Subsection 2:*
- Grossman-Stiglitz (1980): information paradox being extended
- Holden-Subrahmanyam (1992): competition among identically informed traders yields zero rents -- applied to correlated AI signals
- Goldstein-Yang (2015): information diversity creates complementarities -- these break down under AI homogenisation
- Bond-Edmans-Goldstein (2012): FPE vs. RPE distinction -- used for welfare analysis
- Dugast-Foucault (2018, JFE): cheap fast signals crowd out precise signals -- claim: temporal tradeoff, not cross-sectional correlation
- Dugast-Foucault (2025, JF): data mining thresholds -- claim: search intensity mechanism, not signal correlation
- Farboodi-Veldkamp (2020, AER): long-run data technology growth -- claim: technology growth over time, not AI output homogeneity
- Farboodi et al. (2022, RFS): data concentration on large firms -- empirical complement
- Banerjee-Davis-Gondhi (2018, RFS): transparency can reduce informativeness -- related mechanism but via beliefs vs. fundamentals, not cross-sectional AI correlation

*Subsection 3:*
- Kyle (1985), Glosten-Milgrom (1985): foundational market microstructure
- Avellaneda-Stoikov (2008): stochastic control market-making framework -- the framework used
- Brunnermeier-Pedersen (2009): margin spirals -- complementary liquidity feedback mechanism
- Greenwood-Thesmar (2011): stock fragility measure -- analogy for N_eff(rho)
- Danielsson-Shin-Zigrand (2012): common VaR constraints as endogenous risk -- nested as limiting case
- Pagano (1989): low-liquidity trap -- analogy for rho** threshold
- Cespa-Vives (forthcoming, AER): opacity-driven liquidity fragility -- claim: distinct mechanism (opacity vs. algorithmic similarity)
- Colliard-Foucault-Lovo (2025, RFS): Q-learning market makers -- claim: single-agent RL pricing vs. N-market-maker correlated withdrawal

*Subsection 4:*
- Danielsson-Macrae-Uthemann (2022, JBF): qualitative multi-channel argument -- claim: this project provides the formal model
- Dou-Goldstein-Ji (2025a, NBER WP): AI collusion -- claim: RL mechanism, not information-theoretic
- Dou-Goldstein-Ji (2025b, SSRN): AI planning and bubbles -- claim: intertemporal collusion, not signal correlation
- Calvano et al. (2020, AER): algorithmic collusion in pricing -- foundational for AI coordination argument
- Hansen-Lee (2025, Fed WP): AI reduces herding in low-rho settings -- claim: supports non-monotonicity (diverse AI is stabilising; homogeneous AI is destabilising)

**Differentiators to state:**
- For each threat paper: restate the mechanism-level differentiator from the Three Channels section of research_plan_final.md

**Handoff from:** All phases (literature review must reflect the final set of results and differentiators)

---

## Section 3: Model Primitives

**Subsections:**
1. Signal structure: epsilon_i = sqrt(rho) * eta + sqrt(1-rho) * xi_i; interpretation of rho as AI model homogeneity
2. Agent types: AI-equipped agents (signal correlation rho), privately informed agents (correlation 0), market makers
3. Timing: two-period structure; information acquisition decision, trading, coordination game resolution
4. Equilibrium definition: competitive rational expectations equilibrium (Channels 2-3); threshold equilibrium in the global game (Channel 1)

**Key results to present:**
- Definition of the rho primitive and its economic interpretation
- Formal statement of the signal structure and its statistical properties (Cov(epsilon_i, epsilon_j) = rho)
- N_eff formula derivation as a preliminary result

**Literature to cite:**
- Morris-Shin (1998, 2002): signal structure in global games
- Grossman-Stiglitz (1980): information acquisition framework
- Avellaneda-Stoikov (2008): market-making framework

**Differentiators to state:**
- rho as a sufficient statistic for AI model homogeneity, distinct from mu (AI fraction) used by Danielsson-Uthemann (2025)

**Handoff from:** research_plan_final.md (Unifying Primitive section). The Theory Builder formalises the signal structure as the first step of all three channel models.

---

## Section 4: Channel 1 -- Coordination Failure

**Subsections:**
1. Setup: Goldstein-Pauzner (2005) bank-run game with rho-parameterised signals
2. Equilibrium characterisation: theta*(rho) derivation via indifference condition
3. Non-monotonicity and uniqueness/multiplicity boundary rho*
4. Welfare analysis: social cost of AI signal homogeneity via Angeletos-Pavan (2007)

**Key results to present:**
- Proposition 1 (theta*(rho) characterisation): non-monotonicity in rho; uniqueness/multiplicity boundary rho*
- Comparative statics: d(theta*)/d(rho) with sign characterisation
- Welfare result: social cost of increasing rho

**Literature to cite:**
- Goldstein-Pauzner (2005): framework being extended
- Hellwig (2002): multiplicity restoration mechanism being applied
- Angeletos-Pavan (2007): welfare framework
- Szkup-Trevino (2015): uniqueness conditions and their interaction with correlated signals

**Differentiators to state:**
- From Yang (2024): analytical theta*(rho) vs. computational Q-learning threshold
- From Danielsson-Uthemann (2025, JFS): rho vs. mu; Hellwig multiplicity boundary vs. maintained uniqueness; show a comparison case where high mu / low rho is safe but low mu / high rho is dangerous

**Handoff from:** Phase 1 (Theory Builder output in context/model_equations.md, Channel 1 section)

---

## Section 5: Channel 2 -- Information Acquisition

**Subsections:**
1. Setup: Grossman-Stiglitz with two information types (AI at cost c_AI with correlation rho; private at cost c_P with correlation 0)
2. Equilibrium informed fraction mu_I(rho, c_P): derivation and comparative statics
3. Price informativeness: non-monotonicity of RPE in rho; FPE/RPE decomposition
4. Information diversity collapse: Holden-Subrahmanyam competition and Goldstein-Yang complementarity breakdown

**Key results to present:**
- Proposition 2 (information diversity collapse): mu_I decreasing in rho; RPE non-monotone in rho
- Equilibrium characterisation: modified GS indifference condition with correlated signals
- Welfare decomposition: AI improves FPE while degrading RPE

**Literature to cite:**
- Grossman-Stiglitz (1980): framework being extended
- Holden-Subrahmanyam (1992): competition result applied to correlated AI signals
- Goldstein-Yang (2015): information diversity mechanism being applied
- Bond-Edmans-Goldstein (2012): FPE/RPE distinction for welfare analysis

**Differentiators to state:**
- From Dugast-Foucault (2018): cross-sectional signal correlation vs. temporal speed-precision tradeoff
- From Farboodi-Veldkamp (2020): AI output homogeneity vs. data technology growth

**Handoff from:** Phase 2 (Theory Builder output in context/model_equations.md, Channel 2 section)

---

## Section 6: Channel 3 -- Market Making

**Subsections:**
1. Setup: N market makers with Avellaneda-Stoikov framework; shared AI calibration with correlation rho
2. N_eff(rho) derivation and properties (decreasing, convex)
3. Equilibrium spread characterisation: convexity in rho
4. No-equilibrium threshold rho**: existence proof and analogy to Pagano (1989) low-liquidity trap

**Key results to present:**
- Proposition 3 (liquidity fragility index): N_eff(rho) formula, convexity, rho** threshold
- Equilibrium spread as function of rho
- Nesting of Danielsson-Shin-Zigrand (2012) common VaR constraints as limiting case

**Literature to cite:**
- Avellaneda-Stoikov (2008): market-making framework
- Greenwood-Thesmar (2011): fragility measure analogy
- Pagano (1989): low-liquidity trap analogy
- Danielsson-Shin-Zigrand (2012): common VaR constraints (limiting case)
- Brunnermeier-Pedersen (2009): margin spiral connection

**Differentiators to state:**
- From Cespa-Vives (forthcoming): algorithmic similarity vs. market opacity
- From Colliard-Foucault-Lovo (2025): N-market-maker correlated withdrawal vs. single-agent RL pricing

**Handoff from:** Phase 3 (Theory Builder output in context/model_equations.md, Channel 3 section)

---

## Section 7: Amplification Loop

**Subsections:**
1. Joint system definition: three state variables (rho_eff, theta*, N_eff); three mappings (g_1, g_2, g_3)
2. Fixed-point existence: composite operator T on compact convex K; Brouwer argument
3. Bifurcation result: Proposition 4 (rho* < min(rho_i*)); spectral radius argument
4. Comparative statics of the joint equilibrium; economic interpretation ("safety illusion")

**Key results to present:**
- Proposition 4 (Amplification Bifurcation): rho* < min(rho_1*, rho_2*, rho_3*)
- Fixed-point existence theorem
- Jacobian DT computation and spectral radius analysis
- If available: uniqueness result via contraction mapping (or discussion of multiplicity if uniqueness fails)

**Literature to cite:**
- Danielsson-Macrae-Uthemann (2022, JBF): formalisation of their qualitative multi-channel argument
- Danielsson-Uthemann (2025, JFS): the three-channel integration absent from their single-channel model
- Goldstein-Huang-Yang (2025, ARFE): contribution to the fragility framework they survey

**Differentiators to state:**
- From Danielsson-Uthemann (2025): three-channel fixed-point vs. single-channel model
- From Dou-Goldstein-Ji (2025a,b): information-theoretic signal correlation vs. RL-based collusion
- State explicitly that no existing paper models this three-channel fixed-point

**Handoff from:** Phase 4 (Theory Builder output in context/model_equations.md, Amplification Loop section)

---

## Section 8: Extensions

**Subsections:**
1. Endogenous rho: AI adoption as a prisoner's dilemma; competitive equilibrium rho_NE > rho_SO
2. Diversity mandate: regulatory instrument that bounds rho below rho*; efficiency restoration
3. Discussion: dynamic extensions (qualitative); architecture heterogeneity (future work)

**Key results to present:**
- Proposition 5 (endogenous rho): rho_NE > rho* (competitive adoption drives rho above the fragility threshold)
- Characterisation of the diversity mandate

**Literature to cite:**
- Calvano et al. (2020, AER): algorithmic coordination without communication (analogy for AI adoption externality)
- Danielsson-Macrae-Uthemann (2022, JBF): their qualitative discussion of model monoculture (now formalised)

**Differentiators to state:**
- No competing paper models endogenous rho via a prisoner's dilemma in AI adoption

**Handoff from:** Phase 5 (Theory Builder output in context/model_equations.md, Extension section)

---

## Section 9: Empirical Motivation

**Subsections:**
1. Event: ChatGPT release (November 2022) as an AI adoption shock
2. Proxy construction: 13F portfolio correlation as rho proxy; I/B/E/S forecast revision correlation as alternative proxy
3. DiD design: high-AI-exposure stocks (treatment) vs. low-exposure stocks (control)
4. Reduced-form evidence: effect on portfolio correlation, forecast correlation, and liquidity measures post-event

**Key results to present:**
- Descriptive evidence on AI signal homogeneity (time series of rho proxies)
- DiD estimates for the effect of AI adoption on correlation and liquidity measures
- Mapping from reduced-form evidence to the model's comparative statics predictions

**Literature to cite:**
- Gu-Kelly-Xiu (2020, RFS): ML method convergence on same predictors
- Kim-Muhn-Nikolaev (2024, arXiv): GPT-4 financial analysis homogeneity
- Farboodi et al. (2022, RFS): data concentration patterns

**Differentiators to state:**
- Frame as motivating evidence, not causal identification (per scope constraints)
- Acknowledge that ChatGPT is a consumer product; discuss institutional AI adoption timing

**Handoff from:** Phase 7 (Empirical Agent output in code/empirical_motivation.py and context/empirical_notes.md)

---

## Section 10: Conclusion

**Subsections:**
1. Summary of results and the "safety illusion" finding
2. Policy implications: the case for diversity mandates; rho* as a regulatory threshold
3. Limitations: static model, exogenous rho in baseline, empirical section is motivating
4. Future work: dynamic models with evolving rho, architecture heterogeneity, international contagion

**Key results to present:**
- Restate the bifurcation result (rho* < min(rho_i*)) and its regulatory implications
- Restate the diversity mandate from Proposition 5

**Literature to cite:**
- Reference back to Danielsson-Macrae-Uthemann (2022) for the policy discussion they initiated
- Reference Hansen-Lee (2025) as supporting evidence for the non-monotonicity (low rho is stabilising)

**Differentiators to state:**
- The paper's unique contribution is the formal demonstration that single-channel risk assessment creates a safety illusion

**Handoff from:** Phase 8 (Paper Writer integrates all upstream outputs)
