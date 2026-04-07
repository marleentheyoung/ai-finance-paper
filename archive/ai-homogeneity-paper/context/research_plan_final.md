# Final Research Program

## Research Question

How does cross-sectional homogeneity in AI-generated financial signals -- parameterised by the signal correlation coefficient rho -- create systemic fragility through the joint interaction of coordination failure, information acquisition collapse, and correlated liquidity withdrawal, and at what level of rho does the integrated system bifurcate from a stable interior equilibrium to a fragile one?

---

## Unifying Primitive

The paper's unifying primitive is rho-parameterised signal homogeneity. Each agent i observes:

> epsilon_i = sqrt(rho) * eta + sqrt(1-rho) * xi_i

where eta is the common AI model error (shared training data, shared architecture) and xi_i is agent-specific idiosyncratic noise. At rho = 0: the standard heterogeneous-signal benchmark (Morris-Shin uniqueness). At rho = 1: perfectly homogeneous AI output, all agents observe the same signal. The entire paper is organised as comparative statics in rho.

---

## Three Channels

### Channel 1 -- Coordination Failure

**Mechanism.** In a Goldstein-Pauzner (2005) bank-run framework, rising rho converts heterogeneous private signals into near-public common signals. By the Hellwig (2002) result, this progressively restores the multiplicity region in the global game. The crisis threshold theta*(rho) is non-monotone: fragility rises in rho up to a critical rho*, above which the uniqueness property fails entirely and self-fulfilling crises re-emerge. Welfare analysis follows Angeletos-Pavan (2007).

**Key result.** Proposition 1 (theta*(rho) characterisation): In the Goldstein-Pauzner (2005) bank-run framework with rho-parameterised AI signals, the crisis threshold theta*(rho) is non-monotone in rho, and the uniqueness/multiplicity boundary rho* is characterised analytically as a function of rho, the fraction of AI-equipped agents, and the degree of strategic complementarity.

**Foundational papers used.** Morris-Shin (1998, 2002) for the global games framework and uniqueness conditions. Goldstein-Pauzner (2005) for the bank-run application. Hellwig (2002) for the multiplicity restoration result under precise public information. Angeletos-Pavan (2007) for the welfare framework characterising the social cost of public information.

**Differentiators from threat map papers.**

- *Yang (2024, Working paper, Swiss Finance Institute):* Yang's mechanism is purely RL-based -- Q-learning agents learn attack thresholds through repeated behavioural interaction. No signal correlation parameter rho exists in that model; the crisis threshold is learned computationally via Q-value convergence, not derived analytically from the signal structure. Yang does not model information acquisition or market making. The two approaches are complementary: Yang demonstrates the coordination phenomenon computationally; this project characterises it formally through the signal structure.

- *Danielsson and Uthemann (2025, JFS):* Three-part differentiator. (1) **Primitive:** rho (signal correlation, intensive margin of AI output homogeneity) vs. mu (AI agent fraction, extensive margin of AI penetration). Their theta*(mu) = (c/b)[(1-mu)p + mu] captures the AI execution-speed advantage (AI agents always succeed at running with probability 1, raising the threshold). This project's theta*(rho) captures the information-theoretic mechanism where correlated signals restore Hellwig (2002) multiplicity. High mu with diverse AI models (low rho) does not trigger our mechanism; low mu with a single dominant model (high rho among AI users) does. (2) **Analytical characterisation of the uniqueness/multiplicity boundary.** Danielsson-Uthemann (2025) discuss the Hellwig (2002) multiplicity result qualitatively (Section 2.2.2) but do not integrate it into their formal model -- their theta*(mu) is derived under standard Morris-Shin uniqueness conditions. This project derives the boundary rho* at which uniqueness fails as a function of signal correlation. (3) **Connection to Channels 2 and 3.** Danielsson-Uthemann (2025) formalise only the coordination/run channel. They discuss information processing, common data, and speed as separate qualitative channels but do not model information acquisition collapse, market-making fragility, N_eff, or the amplification loop.

- *Hansen-Lee (2025, Fed FEDS WP):* Their finding that AI reduces herding applies to independently queried LLMs (diverse AI, low rho). The experiment does not test the high-rho case (agents sharing the same model output). This actually supports the non-monotonicity claim: at low rho (diverse AI), AI may reduce herding; fragility activates only at high rho.

### Channel 2 -- Information Acquisition Collapse

**Mechanism.** Extending Grossman-Stiglitz (1980) with two information types: (i) AI-processed signals at near-zero cost with cross-sectional correlation rho, and (ii) genuinely private fundamental research at cost c_P > 0 with rho approximately 0. As rho rises, competitive returns to AI-derived information collapse via the Holden-Subrahmanyam (1992) competition result (correlated information yields zero rents). The equilibrium fraction of agents acquiring private information falls. Price informativeness degrades through Goldstein-Yang's (2015) information diversity mechanism. The welfare analysis distinguishes forecasting price efficiency (FPE) from revelatory price efficiency (RPE) via Bond-Edmans-Goldstein (2012): AI may improve FPE while degrading RPE and hence real investment efficiency.

**Key result.** Proposition 2 (Cross-sectional information diversity collapse): In the correlated-signal Grossman-Stiglitz extension, the equilibrium fraction of agents acquiring genuinely private information is decreasing in rho beyond a threshold, and price informativeness (measured by RPE) is non-monotone in rho -- improving at low rho but degrading at high rho as information diversity collapses.

**Foundational papers used.** Grossman-Stiglitz (1980) for the information acquisition paradox. Holden-Subrahmanyam (1992) for the competition result among correlated informed traders. Goldstein-Yang (2015) for the information diversity mechanism. Bond-Edmans-Goldstein (2012) for the FPE/RPE distinction.

**Differentiators from threat map papers.**

- *Dugast-Foucault (2018, JFE):* Their mechanism is a speed-precision tradeoff for a single data source over time (temporal dimension). This project's mechanism operates in the cross-sectional dimension: rho parameterises the correlation structure across N agents using the same AI model. When N agents share a signal with pairwise correlation rho, the effective information content collapses even though each individual signal is precise. This cross-sectional information diversity collapse is absent from the Dugast-Foucault framework.

- *Dugast-Foucault (2025, JF):* Their mechanism is about search intensity and data mining thresholds, not about cross-sectional signal correlation. No Grossman-Stiglitz information aggregation or RPE/FPE distinction.

- *Farboodi-Veldkamp (2020, AER):* Their mechanism is about the long-run growth of data processing technology over time, not the cross-sectional homogeneity of AI outputs. No rho parameterisation or connection to coordination/market-making channels.

### Channel 3 -- Correlated Liquidity Withdrawal

**Mechanism.** AI market makers calibrated on shared data produce near-identical spread-widening functions via the Avellaneda-Stoikov (2008) framework. The effective number of independent liquidity providers is N_eff(rho) = N / (1 + (N-1)*rho), which collapses to 1 as rho approaches 1. The equilibrium bid-ask spread is convex in rho. A threshold rho** exists above which no interior market-making equilibrium with finite spreads exists, analogous to Pagano's (1989) low-liquidity trap. The model nests Danielsson-Shin-Zigrand (2012) common VaR constraints as a limiting case.

**Key result.** Proposition 3 (Liquidity fragility index): The effective number of independent liquidity providers N_eff(rho) = N / (1 + (N-1)*rho) is decreasing and convex in rho. There exists a threshold rho** above which no interior market-making equilibrium with finite spreads exists.

**Foundational papers used.** Avellaneda-Stoikov (2008) for the market-making stochastic control framework. Glosten-Milgrom (1985) and Kyle (1985) for market microstructure foundations. Greenwood-Thesmar (2011) for the stock fragility measure (analogy). Pagano (1989) for the low-liquidity trap. Danielsson-Shin-Zigrand (2012) for common VaR constraints (limiting case). Brunnermeier-Pedersen (2009) for margin spiral mechanics.

**Differentiators from threat map papers.**

- *Cespa-Vives (forthcoming, AER):* Their liquidity fragility arises from market opacity and hedger behaviour. This project's mechanism is driven by algorithmic similarity: rho parameterises the correlation of market-maker signals, yielding the N_eff(rho) fragility index and the rho** threshold. The complementarity arises from correlated AI outputs, not from opacity in the price formation process.

- *Colliard-Foucault-Lovo (2025, RFS):* Their mechanism concerns the RL-based learning dynamics of a single algorithmic market maker in a Glosten-Milgrom adverse selection framework. This project's Channel 3 operates through a distinct mechanism: N market makers sharing the same AI model produce correlated spread-widening functions, collapsing the effective number of independent liquidity providers. No rho parameterisation, no N_eff formula, and no simultaneous withdrawal mechanism appear in Colliard-Foucault-Lovo. The two approaches are complementary: they characterise how AI changes individual market-maker pricing; we characterise how AI homogeneity destroys the diversification benefit of having multiple market makers.

- *Danielsson-Shin-Zigrand (2012, NBER):* Their homogeneity arises from regulatory VaR constraints, not from AI model outputs. This project nests their framework as a limiting case but adds the AI-specific rho parameterisation and connects to Channels 1 and 2.

---

## Fixed-Point Specification (Amplification Loop)

### Amplification Logic

The three channels interact and mutually amplify:

- **Channel 1 -> Channel 2:** High rho raises crisis probability (theta*(rho) falls), reducing expected returns to private information acquisition.
- **Channel 2 -> Channel 3:** As private information acquisition falls, market makers rely more heavily on the common AI signal, raising rho on the market-making side.
- **Channel 3 -> Channel 1:** Correlated liquidity withdrawal amplifies price dislocations, validating the adverse common signal and raising the probability of coordinating on the crisis equilibrium.

### State Variables

The amplification loop is defined over three state variables, each produced by one channel:

- **rho_eff in [0, 1]** -- the effective signal correlation in the coordination game, reflecting both the exogenous AI model correlation rho and the endogenous information acquisition decisions of agents.
- **theta* in [theta_L, theta_H]** -- the crisis threshold in the Goldstein-Pauzner (2005) bank-run game, determined by the signal structure (and hence by rho_eff).
- **N_eff in [1, N]** -- the effective number of independent liquidity providers, determined by the correlation of market-maker signals.

### Three Equilibrium Mappings

**Mapping 1 (Channel 3 -> Channel 1): N_eff determines rho_eff.**

When the effective number of independent liquidity providers N_eff is low, correlated liquidity withdrawal amplifies price dislocations, validating the adverse common signal. This raises the effective signal correlation in the coordination game. Formally:

> rho_eff = g_1(rho, N_eff)

where g_1 is increasing in rho (exogenous AI model correlation) and decreasing in N_eff (fewer independent market makers raise the effective correlation of the crisis signal). At the limit N_eff = 1, all market makers act identically and rho_eff approaches 1. At N_eff = N (full independence), rho_eff = rho (the exogenous level).

**Mapping 2 (Channel 1 -> Channel 2): theta* determines the equilibrium informed fraction, which updates rho_eff.**

The crisis threshold theta*(rho_eff) determines the expected probability of crisis. This affects the expected returns to private information acquisition: when crisis probability is high, the option value of fundamental research falls (since the coordination outcome dominates the fundamental outcome). In the Grossman-Stiglitz extension, the equilibrium fraction of agents acquiring genuinely private information is:

> mu_I = g_2(theta*(rho_eff), rho_eff, c_P)

where mu_I is the fraction of agents who pay cost c_P to acquire private (uncorrelated) signals rather than relying on AI signals with correlation rho. As theta* falls (crisis becomes more likely) or rho_eff rises (AI signals become more correlated and hence less profitable via Holden-Subrahmanyam competition), mu_I falls. The effective signal correlation is then updated:

> rho_eff' = rho * (1 - mu_I)

since privately informed agents contribute uncorrelated signals (rho = 0) while AI-reliant agents contribute correlated signals (pairwise correlation rho).

**Mapping 3 (Channel 2 -> Channel 3): mu_I determines N_eff.**

As the fraction of privately informed agents mu_I falls, market makers increasingly rely on the common AI signal for pricing and inventory management. The effective number of independent liquidity providers is:

> N_eff = g_3(mu_I, rho, N) = N / (1 + (N-1) * rho * (1 - mu_I)^2)

where (1 - mu_I) is the fraction of market-maker information derived from the common AI signal. When mu_I = 0 (all agents use AI), this reduces to N_eff = N / (1 + (N-1)*rho), the baseline Channel 3 formula. When mu_I = 1 (all agents acquire private information), N_eff = N (full independence).

### Composite Operator and Fixed-Point Existence

Define the composite operator T: K -> K where K = [0,1] x [theta_L, theta_H] x [1, N] is a compact convex subset of R^3, and:

> T(rho_eff, theta*, N_eff) = (rho_eff', theta*', N_eff')

where:
- rho_eff' = g_1(rho, g_3(g_2(theta*(rho_eff), rho_eff, c_P), rho, N))
- theta*' = theta*(rho_eff')
- N_eff' = g_3(g_2(theta*', rho_eff', c_P), rho, N)

Each component mapping is continuous (standard regularity from the underlying economic models), and K is compact and convex. By **Brouwer's fixed-point theorem**, T admits at least one fixed-point (rho_eff^*, theta^{**}, N_eff^*).

**Proof sketch:** Continuity of T follows from: (i) theta*(rho_eff) is continuous in rho_eff by the implicit function theorem applied to the Goldstein-Pauzner (2005) indifference condition; (ii) g_2 is continuous in its arguments by standard Grossman-Stiglitz equilibrium characterisation; (iii) g_3 is a continuous algebraic function; (iv) g_1 is continuous by construction. T maps K into K because each output variable is bounded in its respective interval by the structure of the economic model (rho_eff is a convex combination bounded in [0,1]; theta* is bounded by the support of fundamentals; N_eff is bounded in [1,N] by the N_eff formula). Hence Brouwer applies.

### Bifurcation Proposition (Sketch)

**Proposition 4 (Amplification Bifurcation).** Let rho_1* denote the critical signal correlation at which Channel 1 alone loses its stable interior equilibrium (uniqueness fails in the global game), rho_2* the level at which Channel 2 alone yields mu_I = 0 (complete information acquisition collapse), and rho_3* the level at which Channel 3 alone yields N_eff = 1 (complete liquidity concentration). Let rho* denote the critical signal correlation at which the integrated three-channel system T loses its stable interior fixed-point. Then:

> rho* < min(rho_1*, rho_2*, rho_3*)

**Proof approach:** The amplification loop makes the composite mapping T steeper than any individual channel mapping considered in isolation. In each channel, the endogenous feedback from the other two channels amplifies the response to rho: a marginal increase in rho raises rho_eff (via reduced mu_I and reduced N_eff), which further raises theta* and further reduces mu_I and N_eff. Formally, the Jacobian of T evaluated at the interior fixed-point has spectral radius that exceeds the spectral radius of any individual channel's mapping, because the off-diagonal terms (cross-channel feedbacks) are strictly positive. The interior fixed-point becomes unstable (the system bifurcates to the fragile corner equilibrium) when the spectral radius of DT crosses unity. Since the cross-channel amplification terms are strictly positive, this crossing occurs at a strictly lower rho than would be required for any individual channel. The formal proof proceeds by showing that d(rho_eff)/d(rho) evaluated at the fixed-point exceeds 1 at rho* < min(rho_i*), using the chain rule across the three mappings.

**Economic interpretation:** A level of AI model correlation that appears safe when assessed against coordination failure alone, or information acquisition alone, or market-making fragility alone, may be systemically dangerous when all three channels interact. The amplification loop creates a "safety illusion" -- regulators examining any single channel would conclude the system is stable, while the compound mechanism has already crossed the bifurcation threshold.

---

## Five Contributions

### Contribution 1: theta*(rho) Characterisation (Channel 1)

**Proposition form:** In the Goldstein-Pauzner (2005) bank-run framework with rho-parameterised AI signals, the crisis threshold theta*(rho) is non-monotone in rho and the uniqueness/multiplicity boundary rho* is characterised analytically as a function of rho.

**Threat map differentiators:**
- From Yang (2024): RL behavioural convergence vs. information-theoretic signal correlation; computational vs. analytical characterisation.
- From Danielsson-Uthemann (2025, JFS): rho (signal correlation) vs. mu (AI fraction); uniqueness/multiplicity boundary derivation vs. threshold formula under maintained uniqueness; three-channel connection vs. single-channel model.

**Coverage gap filled:** Gap 1.1 (no paper derives theta*(rho) as a function of signal correlation), Gap 1.3 (non-monotonicity of theta*(rho) in an AI context).

### Contribution 2: Cross-Sectional GS Extension with RPE Collapse (Channel 2)

**Proposition form:** In the correlated-signal extension of Grossman-Stiglitz (1980), the equilibrium fraction of agents acquiring genuinely private information is decreasing in rho, and price informativeness measured by RPE is non-monotone in AI adoption -- improving at low rho but collapsing at high rho as information diversity is destroyed.

**Threat map differentiators:**
- From Dugast-Foucault (2018, JFE): cross-sectional signal correlation dimension vs. temporal speed-precision tradeoff.
- From Dugast-Foucault (2025, JF): signal correlation structure vs. data mining thresholds.

**Coverage gap filled:** Gap 2.1 (no paper extends GS with two information types differentiated by correlation), Gap 2.2 (Holden-Subrahmanyam competition + Goldstein-Yang complementarities interaction not formalised), Gap 2.3 (FPE/RPE distinction under AI not modelled).

### Contribution 3: N_eff(rho) Liquidity Fragility Index with rho** Threshold (Channel 3)

**Proposition form:** The effective number of independent liquidity providers N_eff(rho) = N / (1 + (N-1)*rho) is decreasing and convex in rho. There exists a threshold rho** above which no interior market-making equilibrium with finite spreads exists.

**Threat map differentiators:**
- From Cespa-Vives (forthcoming, AER): algorithmic similarity mechanism vs. market opacity mechanism.
- From Colliard-Foucault-Lovo (2025, RFS): N-market-maker correlated withdrawal vs. single-agent RL pricing dynamics.

**Coverage gap filled:** Gap 3.1 (no N_eff formula for AI market makers), Gap 3.2 (no rho** no-equilibrium threshold), Gap 3.3 (convexity of spread in rho not established).

### Contribution 4: Fixed-Point Amplification Loop with Bifurcation Result (Centrepiece)

**Proposition form:** The joint three-channel system admits a fixed-point equilibrium in (rho_eff, theta*, N_eff) by Brouwer's theorem. The bifurcation threshold rho* of the integrated system is strictly below the minimum of the individual channel thresholds: rho* < min(rho_1*, rho_2*, rho_3*).

**Threat map differentiators:**
- From Danielsson-Uthemann (2025, JFS): three-channel fixed-point in (rho_eff, theta*, N_eff) with rho as unifying primitive vs. single-channel model with mu.
- From Danielsson-Macrae-Uthemann (2022, JBF): formal equilibrium characterisation vs. qualitative narrative.
- From Dou-Goldstein-Ji (2025a, 2025b): information-theoretic signal correlation mechanism vs. RL-based collusion mechanism.
- From Goldstein-Huang-Yang (2025, ARFE survey): specific AI-driven three-channel model vs. general fragility survey.

**Coverage gap filled:** Gap 4.1 (no fixed-point in (rho_eff, theta*, N_eff)), Gap 4.2 (joint rho* < min of individual thresholds not established), Gap 4.3 (safety illusion from moderate correlation not shown formally).

### Contribution 5: Endogenous rho via Prisoner's Dilemma in AI Adoption (Extension)

**Proposition form:** In the AI adoption game, each agent's private incentive to adopt the dominant AI model exceeds the social cost of reduced signal diversity, driving rho above the socially optimal level. The competitive equilibrium rho exceeds rho*, creating a fragility externality. A diversity mandate that bounds rho below rho* restores efficiency.

**Threat map differentiators:**
- No HIGH or MODERATE threat paper models endogenous rho via a prisoner's dilemma in AI adoption in financial markets.

**Coverage gap filled:** This extends the main model; no specific gap number in literature_constraints.md but the Literature Guardian confirmed (Iteration 1) that no competing paper exists.

---

## Phases

| Phase | Description | Responsible Agent | Dependencies | Deliverables |
|-------|-------------|-------------------|--------------|--------------|
| 1 | Channel 1: Embed rho into Goldstein-Pauzner (2005); derive theta*(rho); characterise uniqueness/multiplicity boundary; welfare analysis via Angeletos-Pavan (2007) | Theory Builder | None | Proposition 1 (theta*(rho) characterisation with non-monotonicity and rho* boundary); LaTeX equation for theta*(rho) as implicit function of the Goldstein-Pauzner indifference condition with rho-parameterised signals; comparative statics d(theta*)/d(rho); welfare result using Angeletos-Pavan (2007) framework |
| 2 | Channel 2: Extend Grossman-Stiglitz (1980) with correlated AI signals; derive equilibrium informed fraction as function of rho; characterise RPE degradation via Goldstein-Yang (2015) and Bond-Edmans-Goldstein (2012) | Theory Builder | None (parallel with Phase 1) | Proposition 2 (information diversity collapse and RPE non-monotonicity); LaTeX equation for equilibrium mu_I(rho, c_P) from the modified GS indifference condition; price informativeness as function of rho; FPE/RPE decomposition |
| 3 | Channel 3: Derive N_eff(rho); characterise market-making equilibrium with correlated AI signals; derive rho** threshold; connect to Danielsson-Shin-Zigrand (2012) as limiting case | Theory Builder | None (parallel with Phases 1-2) | Proposition 3 (N_eff(rho) with convexity and rho** threshold); LaTeX derivation of N_eff(rho) = N / (1 + (N-1)*rho) from the Avellaneda-Stoikov framework with correlated signals; equilibrium spread as function of rho; rho** existence proof |
| 4 | Amplification loop: Define the joint system in (rho_eff, theta*, N_eff); characterise the fixed-point; prove bifurcation result | Theory Builder | Phases 1, 2, 3 | Proposition 4 (Bifurcation); LaTeX specification of composite operator T with the three mappings g_1, g_2, g_3 from the Fixed-Point Specification section above; Brouwer existence proof; Jacobian DT computation; spectral radius argument for rho* < min(rho_i*); attempt contraction mapping for uniqueness |
| 5 | Extension: Prisoner's dilemma in AI adoption; endogenous rho; diversity mandate | Theory Builder | Phase 4 | Proposition 5 (endogenous rho exceeds rho*); LaTeX characterisation of the adoption game payoffs; Nash equilibrium rho_NE; social optimum rho_SO; diversity mandate characterisation |
| 6 | Model verification: Check all equilibrium derivations, comparative statics signs, and fixed-point existence/uniqueness conditions | Model Verifier | Phases 1-5 | Verification report confirming or flagging errors in all propositions and derivations |
| 7 | Empirical motivation: DiD using ChatGPT release (November 2022) as AI adoption shock; construct rho proxies from 13F portfolio correlation and I/B/E/S forecast revision correlation | Empirical Agent | Phase 4 | Python code for empirical analysis; empirical notes documenting the DiD design, proxy construction, and reduced-form results |
| 8 | Paper writing: Integrate all outputs into manuscript following paper structure map | Paper Writer | Phases 4, 6, 7 | Complete LaTeX manuscript (paper/main.tex) |

---

## Execution Risks

### Risk 1 (Medium): Channel 1 derivation must produce qualitatively distinct dynamics from theta*(mu)

The three-part differentiator from Danielsson-Uthemann (2025, JFS) is stated at the mechanism level but not yet proved. If the Theory Builder derives theta*(rho) and it turns out to be structurally isomorphic to theta*(mu) (e.g., just a relabelling), the novelty claim for Contribution 1 collapses. The Theory Builder must show that the rho parameterisation produces qualitatively different equilibrium dynamics -- specifically, the non-monotonicity and the uniqueness/multiplicity boundary transition that the mu model does not generate.

**Mitigation:** The mechanisms are economically distinct (rho activates the Hellwig 2002 multiplicity channel; mu activates the execution-speed channel). The Theory Builder should produce a comparison case showing that high mu with low rho is safe but low mu with high rho is dangerous.

### Risk 2 (Medium): Fixed-point uniqueness

The Brouwer argument guarantees existence of at least one fixed-point but not uniqueness. If multiple interior fixed-points exist, the bifurcation result must be restated carefully (which fixed-point bifurcates?). This could complicate the "safety illusion" narrative.

**Mitigation:** The Theory Builder should attempt a contraction mapping argument in Phase 4. If uniqueness fails, multiplicity of fixed-points is itself an interesting result (additional equilibrium fragility) that can be interpreted economically.

### Risk 3 (Medium): Empirical proxy justification

The DiD design uses the ChatGPT release (November 2022) as an AI adoption shock. The ChatGPT release is primarily a consumer product; the mapping to institutional financial decision-making requires justification. The 13F portfolio correlation proxy for rho needs a formal mapping from portfolio overlap to signal correlation.

**Mitigation:** Frame the empirical section as motivating evidence, not causal identification (consistent with scope constraints in research_context.md Section 6). The Empirical Agent should explore alternative proxies or provide institutional adoption evidence to support the ChatGPT event.

---

## Open Questions for Execution

**Open Question 2:** Channel 1-2 interaction specification. The link from Channel 1 to Channel 2 (crisis anticipation reduces information acquisition incentives) requires a specific functional form for how the crisis probability theta*(rho) enters the Grossman-Stiglitz informed-fraction decision. The mapping g_2 is sketched in the Fixed-Point Specification but the Theory Builder must specify this before Phase 4 begins.

**Open Question 4:** Dou-Goldstein-Ji (2025b) mechanism verification. Only search summaries are available for this November 2025 paper. The Literature Guardian should verify in Mode 3 whether this paper contains any information-theoretic channel or rho-like parameterisation. If it does, Contribution 4's differentiator must be sharpened.

**Open Question 5:** Hansen-Lee (2025) counterargument. Their finding that AI reduces herding applies to independently queried LLMs. The paper should acknowledge that at low rho (diverse AI agents), AI may indeed reduce herding, and the fragility mechanism activates only at high rho. This strengthens the non-monotonicity argument.

**Open Question 6:** Szkup-Trevino (2015) interaction with rho. Their sufficient conditions for uniqueness in global games with endogenous information acquisition may be violated when signals are correlated through a common AI source. The Theory Builder should check this in Phase 1. If Szkup-Trevino's uniqueness conditions break down at high rho, this strengthens the Channel 1 result.

**Open Question 7:** Empirical proxy credibility. The DiD design uses ChatGPT release as an AI adoption shock. The Empirical Agent must justify why this event is relevant for institutional financial decision-making and provide a formal mapping from 13F portfolio overlap to signal correlation rho.
