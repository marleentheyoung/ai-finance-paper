# Research Plan

## Research Question

How does cross-sectional homogeneity in AI-generated financial signals -- parameterised by the signal correlation coefficient rho -- create systemic fragility through the joint interaction of coordination failure, information acquisition collapse, and correlated liquidity withdrawal, and at what level of rho does the integrated system bifurcate from a stable interior equilibrium to a fragile one?

## Mechanism

The unifying primitive is rho-parameterised signal homogeneity. Each agent i observes epsilon_i = sqrt(rho) * eta + sqrt(1-rho) * xi_i, where eta is the common AI model error and xi_i is idiosyncratic noise. The entire paper is organised as comparative statics in rho, which activates three distinct fragility channels:

**Channel 1 -- Coordination failure.** In a Goldstein-Pauzner (2005) bank-run framework, rising rho converts heterogeneous private signals into near-public common signals. By the Hellwig (2002) result, this progressively restores the multiplicity region in the global game. The crisis threshold theta*(rho) is non-monotone: fragility rises in rho up to a critical rho*, above which the uniqueness property fails entirely and self-fulfilling crises re-emerge. Welfare analysis follows Angeletos-Pavan (2007).

**Differentiator from Yang (2024):** Yang studies emergent coordination by RL agents through repeated behavioural interaction. Our mechanism is information-theoretic: rho parameterises the cross-sectional correlation of the signal structure itself, enabling an analytical characterisation of theta*(rho) that Yang's computational approach does not provide. The two approaches are complementary -- Yang demonstrates the phenomenon computationally; we characterise it formally through the signal structure.

**Differentiator from Danielsson and Uthemann (2025, JFS):** Danielsson and Uthemann (2025) provide a formal game-theoretic model of AI-driven coordination failure, deriving a crisis threshold theta*(mu) = (c/b)[(1-mu)p + mu] where mu is the fraction of AI agents and p is the probability that humans successfully execute a run. Their model formalises the AI *speed advantage* channel: AI agents always succeed at running (probability 1), so increasing mu mechanically raises the threshold. The project differs on three dimensions:

1. **Primitive: rho (signal correlation) vs. mu (AI agent fraction).** Danielsson-Uthemann's theta*(mu) captures the execution-probability mechanism -- AI agents are faster and more reliable runners. Our theta*(rho) captures the *information-theoretic* mechanism: when agents share a common AI signal with pairwise correlation rho, the signal structure progressively restores the public-information regime of Hellwig (2002), reintroducing equilibrium multiplicity. The two primitives are economically distinct: mu measures AI penetration (an extensive margin), while rho measures AI output homogeneity (an intensive margin). High mu with diverse AI models (low rho) does not trigger our mechanism; low mu with a single dominant model (high rho among AI users) does.

2. **Analytical characterisation of the uniqueness/multiplicity boundary as a function of signal correlation.** Danielsson-Uthemann (2025) discuss the Hellwig (2002) multiplicity result qualitatively (noting that common data could restore multiple equilibria) but do not integrate it into their formal model. Their theta*(mu) is derived under standard Morris-Shin uniqueness conditions. The project derives the boundary rho* at which the uniqueness property of the global game fails -- that is, the critical signal correlation at which the Goldstein-Pauzner (2005) unique threshold equilibrium gives way to multiple self-fulfilling equilibria. This is an analytical characterisation that neither Danielsson-Uthemann (2025) nor Yang (2024) provide.

3. **Connection to Channels 2 and 3 through the amplification loop.** Danielsson-Uthemann (2025) formalise only the coordination/run channel. They discuss information processing, common data, and speed as separate qualitative channels but do not model information acquisition collapse (Channel 2), market-making fragility (Channel 3), N_eff, or the fixed-point interaction across channels. The project's Channel 1 model feeds into the amplification loop: theta*(rho) determines crisis probability, which affects information acquisition incentives (Channel 2), which in turn affects market-maker signal correlation (Channel 3), closing the loop. This integration is absent from the Danielsson-Uthemann framework.

**Channel 2 -- Information acquisition collapse.** Extending Grossman-Stiglitz (1980) with two information types: (i) AI-processed signals at near-zero cost with cross-sectional correlation rho, and (ii) genuinely private fundamental research at cost c_P > 0 with rho approximately 0. As rho rises, competitive returns to AI-derived information collapse via the Holden-Subrahmanyam (1992) competition result (correlated information yields zero rents). The equilibrium fraction of agents acquiring private information falls. Price informativeness degrades through Goldstein-Yang's (2015) information diversity mechanism. The welfare analysis distinguishes forecasting price efficiency (FPE) from revelatory price efficiency (RPE) via Bond-Edmans-Goldstein (2012): AI may improve FPE while degrading RPE and hence real investment efficiency.

**Differentiator from Dugast-Foucault (2018, 2025):** Dugast-Foucault model a speed-precision tradeoff for a single data source over time (temporal dimension). Our mechanism operates in the cross-sectional dimension: rho parameterises the correlation structure across N agents using the same AI model. When N agents share a signal with pairwise correlation rho, the effective information content collapses even though each individual signal is precise. This cross-sectional information diversity collapse is absent from the Dugast-Foucault framework.

**Channel 3 -- Correlated liquidity withdrawal.** AI market makers calibrated on shared data produce near-identical spread-widening functions via the Avellaneda-Stoikov (2008) framework. The effective number of independent liquidity providers is N_eff(rho) = N / (1 + (N-1)*rho), which collapses to 1 as rho approaches 1. The equilibrium bid-ask spread is convex in rho. A threshold rho** exists above which no interior market-making equilibrium with finite spreads exists, analogous to Pagano's (1989) low-liquidity trap. The model nests Danielsson-Shin-Zigrand (2012) common VaR constraints as a limiting case.

**Differentiator from Cespa-Vives (forthcoming):** Cespa-Vives derive liquidity fragility from market opacity and hedger behaviour. Our mechanism is driven by algorithmic similarity: rho parameterises the correlation of market-maker signals, yielding the N_eff(rho) fragility index and the rho** threshold. The complementarity arises from correlated AI outputs, not from opacity in the price formation process.

**Differentiator from Colliard-Foucault-Lovo (2025, RFS):** Colliard, Foucault, and Lovo (2025) study a single Q-learning algorithmic market maker in a Glosten-Milgrom (1985) adverse selection framework, showing that RL-based pricing produces non-competitive markups. Their mechanism concerns the *learning dynamics* of an individual market maker, not the *cross-sectional correlation* of signals among multiple market makers. The project's Channel 3 operates through a distinct mechanism: N market makers sharing the same AI model produce correlated spread-widening functions, collapsing the effective number of independent liquidity providers to N_eff(rho) = N / (1 + (N-1)*rho). No rho parameterisation, no N_eff formula, and no simultaneous withdrawal mechanism appear in Colliard-Foucault-Lovo. The two approaches are complementary: they characterise how AI changes individual market-maker pricing; we characterise how AI homogeneity destroys the diversification benefit of having multiple market makers.

**Amplification loop -- the core contribution.** The three channels interact and mutually amplify:
- Channel 1 -> Channel 2: High rho raises crisis probability (theta*(rho) falls), reducing expected returns to private information acquisition.
- Channel 2 -> Channel 3: As private information acquisition falls, market makers rely more heavily on the common AI signal, raising rho on the market-making side.
- Channel 3 -> Channel 1: Correlated liquidity withdrawal amplifies price dislocations, validating the adverse common signal and raising the probability of coordinating on the crisis equilibrium.

The joint system admits a fixed-point equilibrium in (rho_eff, theta*, N_eff). The key proposition: the joint rho* at which the integrated system becomes fragile is strictly lower than the rho* implied by any single channel in isolation. Moderate model correlation that appears safe under any individual channel may be systemically dangerous under the compound mechanism.

## Contributions

1. **Analytical characterisation of theta*(rho) in a global games bank-run model (Channel 1).** Embed rho-parameterised signal homogeneity into Goldstein-Pauzner (2005) and derive the non-monotone crisis threshold as a closed-form function of rho, the fraction of AI-equipped agents, and the degree of strategic complementarity. Show that sufficiently high rho restores the multiplicity region. Differentiated from Yang (2024) by the information-theoretic mechanism (signal correlation vs. RL behavioural convergence) and the analytical theta*(rho) characterisation. Differentiated from Danielsson and Uthemann (2025, JFS) on three dimensions: (a) the primitive is rho (signal correlation) not mu (AI agent fraction) -- their theta*(mu) captures execution speed advantage while our theta*(rho) captures the information-theoretic mechanism where correlated signals restore Hellwig (2002) multiplicity; (b) the project analytically characterises the uniqueness/multiplicity boundary as a function of signal correlation, which Danielsson-Uthemann (2025) discuss qualitatively but do not derive; (c) the Channel 1 model connects to Channels 2 and 3 through the amplification loop, whereas Danielsson-Uthemann formalise only the coordination/run channel.

2. **Cross-sectional information diversity collapse in a correlated-signal extension of Grossman-Stiglitz (Channel 2).** Derive the equilibrium fraction of agents acquiring genuinely private information as a function of rho and the AI signal cost. Show that price informativeness (measured by RPE) is non-monotone in AI adoption: RPE improves at low rho but degrades at high rho as information diversity collapses. Differentiated from Dugast-Foucault (2018) by the cross-sectional correlation dimension (N agents sharing a signal) vs. the temporal speed-precision tradeoff.

3. **N_eff(rho) liquidity fragility index and the rho** no-equilibrium threshold (Channel 3).** Derive the effective number of independent liquidity providers as a function of signal correlation. Show that the equilibrium bid-ask spread is convex in rho and that a threshold rho** exists above which no interior market-making equilibrium exists. This contribution has no HIGH threat in the threat map.

4. **Fixed-point characterisation of the amplification loop in (rho_eff, theta*, N_eff) -- the paper's centrepiece.** Characterise the joint equilibrium of the three-channel system. Prove that the bifurcation threshold rho* of the integrated system is strictly below the minimum of the individual channel thresholds. This is the paper's primary novelty claim: no existing paper connects coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a single signal correlation parameterisation. Differentiated from Danielsson and Uthemann (2025, JFS) by the three-channel integration: the 2025 paper formalises only the coordination/run channel via mu (AI fraction); the project delivers the fixed-point in (rho_eff, theta*, N_eff) across all three channels with rho as the unifying primitive. Differentiated from Danielsson-Macrae-Uthemann (2022, JBF) by formal modelling of all three channels vs. qualitative narrative. Differentiated from Dou-Goldstein-Ji (2025a,b) by the information-theoretic mechanism (signal correlation driving the fixed-point) vs. RL-based collusion (emergent coordination through repeated strategic interaction). See the Fixed-Point Specification section below for the formal structure of the equilibrium.

5. **Endogenous rho via a prisoner's dilemma in AI adoption (Extension).** Show that competitive adoption incentives drive rho above the socially optimal level: each agent's private incentive to adopt the dominant AI model exceeds the social cost of reduced signal diversity. Characterise the diversity mandate that restores efficiency.

## Fixed-Point Specification (Amplification Loop)

### State Variables

The amplification loop is defined over three state variables, each produced by one channel:

- **rho_eff in [0, 1]** -- the effective signal correlation in the coordination game, reflecting both the exogenous AI model correlation rho and the endogenous information acquisition decisions of agents.
- **theta* in [theta_L, theta_H]** -- the crisis threshold in the Goldstein-Pauzner (2005) bank-run game, determined by the signal structure (and hence by rho_eff).
- **N_eff in [1, N]** -- the effective number of independent liquidity providers, determined by the correlation of market-maker signals.

### Equilibrium Conditions

The fixed-point is characterised by three mappings, one per channel, that must hold simultaneously.

**Mapping 1 (Channel 3 -> Channel 1): N_eff determines rho_eff.**
When the effective number of independent liquidity providers N_eff is low, correlated liquidity withdrawal amplifies price dislocations, validating the adverse common signal. This raises the effective signal correlation in the coordination game. Formally:

> rho_eff = g_1(rho, N_eff)

where g_1 is increasing in rho (exogenous AI model correlation) and decreasing in N_eff (fewer independent market makers raise the effective correlation of the crisis signal). At the limit N_eff = 1, all market makers act identically and rho_eff approaches 1. At N_eff = N (full independence), rho_eff = rho (the exogenous level).

**Mapping 2 (Channel 1 -> Channel 2): theta* determines the equilibrium informed fraction, which updates rho_eff.**
The crisis threshold theta*(rho_eff) determines the expected probability of crisis. This affects the expected returns to private information acquisition: when crisis probability is high, the option value of fundamental research falls (since the coordination outcome dominates the fundamental outcome). In the Grossman-Stiglitz extension, the equilibrium fraction of agents acquiring genuinely private information is:

> mu_I = g_2(theta*(rho_eff), rho_eff, c_P)

where mu_I is the fraction of agents who pay cost c_P to acquire private (uncorrelated) signals rather than relying on AI signals with correlation rho. As theta* falls (crisis becomes more likely) or rho_eff rises (AI signals become more correlated and hence less profitable via Holden-Subrahmanyam competition), mu_I falls. The effective signal correlation is then updated:

> rho_eff' = rho * (1 - mu_I) + 0 * mu_I = rho * (1 - mu_I)

since privately informed agents contribute uncorrelated signals (rho = 0) while AI-reliant agents contribute correlated signals (pairwise correlation rho).

**Mapping 3 (Channel 2 -> Channel 3): mu_I determines N_eff.**
As the fraction of privately informed agents mu_I falls, market makers increasingly rely on the common AI signal for pricing and inventory management. The effective number of independent liquidity providers is:

> N_eff = g_3(mu_I, rho, N) = N / (1 + (N-1) * rho * (1 - mu_I)^2)

where (1 - mu_I) is the fraction of market-maker information derived from the common AI signal. When mu_I = 0 (all agents use AI), this reduces to N_eff = N / (1 + (N-1)*rho), the baseline Channel 3 formula. When mu_I = 1 (all agents acquire private information), N_eff = N (full independence).

### Composite Operator and Fixed-Point Existence

Define the composite operator T: K -> K where K = [0,1] x [theta_L, theta_H] x [1, N] is a compact convex subset of R^3, and:

> T(rho_eff, theta*, N_eff) = (rho_eff', theta*', N_eff')

where:
- rho_eff' = g_1(rho, g_3(g_2(theta*(rho_eff), rho_eff, c_P), rho, N))  [Mappings 3 -> 1]
- theta*' = theta*(rho_eff')  [Channel 1 equilibrium]
- N_eff' = g_3(g_2(theta*', rho_eff', c_P), rho, N)  [Mappings 2 -> 3]

Each component mapping is continuous (standard regularity from the underlying economic models), and K is compact and convex. By **Brouwer's fixed-point theorem**, T admits at least one fixed-point (rho_eff^*, theta^{**}, N_eff^*).

**Proof sketch:** Continuity of T follows from: (i) theta*(rho_eff) is continuous in rho_eff by the implicit function theorem applied to the Goldstein-Pauzner (2005) indifference condition; (ii) g_2 is continuous in its arguments by standard Grossman-Stiglitz equilibrium characterisation; (iii) g_3 is a continuous algebraic function; (iv) g_1 is continuous by construction. T maps K into K because each output variable is bounded in its respective interval by the structure of the economic model (rho_eff is a convex combination bounded in [0,1]; theta* is bounded by the support of fundamentals; N_eff is bounded in [1,N] by the N_eff formula). Hence Brouwer applies.

### Bifurcation Proposition (Sketch)

**Proposition (Amplification Bifurcation).** Let rho_1* denote the critical signal correlation at which Channel 1 alone loses its stable interior equilibrium (uniqueness fails in the global game), rho_2* the level at which Channel 2 alone yields mu_I = 0 (complete information acquisition collapse), and rho_3* the level at which Channel 3 alone yields N_eff = 1 (complete liquidity concentration). Let rho* denote the critical signal correlation at which the integrated three-channel system T loses its stable interior fixed-point. Then:

> rho* < min(rho_1*, rho_2*, rho_3*)

**Proof approach:** The amplification loop makes the composite mapping T steeper than any individual channel mapping considered in isolation. In each channel, the endogenous feedback from the other two channels amplifies the response to rho: a marginal increase in rho raises rho_eff (via reduced mu_I and reduced N_eff), which further raises theta* and further reduces mu_I and N_eff. Formally, the Jacobian of T evaluated at the interior fixed-point has spectral radius that exceeds the spectral radius of any individual channel's mapping, because the off-diagonal terms (cross-channel feedbacks) are strictly positive. The interior fixed-point becomes unstable (the system bifurcates to the fragile corner equilibrium) when the spectral radius of DT crosses unity. Since the cross-channel amplification terms are strictly positive, this crossing occurs at a strictly lower rho than would be required for any individual channel. The formal proof proceeds by showing that d(rho_eff)/d(rho) evaluated at the fixed-point exceeds 1 at rho* < min(rho_i*), using the chain rule across the three mappings.

**Economic interpretation:** A level of AI model correlation that appears safe when assessed against coordination failure alone, or information acquisition alone, or market-making fragility alone, may be systemically dangerous when all three channels interact. The amplification loop creates a "safety illusion" -- regulators examining any single channel would conclude the system is stable, while the compound mechanism has already crossed the bifurcation threshold.

## Phases

| Phase | Description | Responsible Agent | Dependencies |
|-------|-------------|-------------------|--------------|
| 1 | Channel 1: Embed rho into Goldstein-Pauzner (2005); derive theta*(rho); characterise uniqueness/multiplicity boundary; welfare analysis via Angeletos-Pavan (2007) | Theory Builder | None |
| 2 | Channel 2: Extend Grossman-Stiglitz (1980) with correlated AI signals; derive equilibrium informed fraction as function of rho; characterise RPE degradation via Goldstein-Yang (2015) and Bond-Edmans-Goldstein (2012) | Theory Builder | None (parallel with Phase 1) |
| 3 | Channel 3: Derive N_eff(rho); characterise market-making equilibrium with correlated AI signals; derive rho** threshold; connect to Danielsson-Shin-Zigrand (2012) as limiting case | Theory Builder | None (parallel with Phases 1-2) |
| 4 | Amplification loop: Define the joint system in (rho_eff, theta*, N_eff); characterise the fixed-point; prove bifurcation result (joint rho* < min of individual thresholds) | Theory Builder | Phases 1, 2, 3 |
| 5 | Extension: Prisoner's dilemma in AI adoption; endogenous rho; diversity mandate | Theory Builder | Phase 4 |
| 6 | Model verification: Check all equilibrium derivations, comparative statics signs, and fixed-point existence/uniqueness conditions | Model Verifier | Phases 1-5 |
| 7 | Empirical motivation: DiD using ChatGPT release (November 2022) as AI adoption shock; construct rho proxies from 13F portfolio correlation and I/B/E/S forecast revision correlation | Empirical Agent | Phase 4 (needs theoretical predictions to test) |
| 8 | Paper writing: Integrate all outputs into manuscript following paper structure map | Paper Writer | Phases 4, 6, 7 |

## Paper Structure Map

| Paper Section | Source Phase | Content |
|---------------|-------------|---------|
| Introduction | All phases | Contribution framing; position relative to Yang (2024), Danielsson-Uthemann (2025, JFS), Dugast-Foucault (2018, 2025), Danielsson-Macrae-Uthemann (2022, JBF), Colliard-Foucault-Lovo (2025, RFS), Dou-Goldstein-Ji (2025a,b); preview of amplification result |
| Literature Review | All phases | Positioning across three domains: (i) global games and coordination (Morris-Shin, Hellwig, Goldstein-Pauzner, Yang), (ii) information acquisition (Grossman-Stiglitz, Goldstein-Yang, Dugast-Foucault, Farboodi-Veldkamp), (iii) market making and liquidity fragility (Kyle, Glosten-Milgrom, Brunnermeier-Pedersen, Greenwood-Thesmar, Danielsson-Shin-Zigrand) |
| Model Primitives (Section 3) | Setup | rho parameterisation; signal structure; agent types; timing; equilibrium definition |
| Channel 1 (Section 4) | Phase 1 | theta*(rho) characterisation; uniqueness/multiplicity boundary; welfare |
| Channel 2 (Section 5) | Phase 2 | Correlated GS extension; equilibrium informed fraction; RPE vs. FPE |
| Channel 3 (Section 6) | Phase 3 | N_eff(rho); market-making equilibrium; rho** threshold |
| Amplification Loop (Section 7) | Phase 4 | Fixed-point in (rho_eff, theta*, N_eff); bifurcation result; comparative statics |
| Extensions (Section 8) | Phase 5 | Endogenous rho; prisoner's dilemma; diversity mandate |
| Empirical Motivation (Section 9) | Phase 7 | DiD design; rho proxies; reduced-form evidence |
| Conclusion (Section 10) | Phase 8 | Policy implications; limitations; future work (dynamic models, architecture heterogeneity) |

## Open Questions

1. ~~**Fixed-point tractability.**~~ **RESOLVED (Iteration 1).** The fixed-point existence is established via Brouwer's theorem on the compact convex set K = [0,1] x [theta_L, theta_H] x [1, N]. Closed-form solution is not required; the bifurcation result is proved by showing that the spectral radius of the Jacobian DT crosses unity at rho* < min(rho_i*). The Theory Builder should assess in Phase 4 whether a contraction mapping argument can additionally deliver uniqueness of the interior fixed-point (which would strengthen the result but is not required for the bifurcation proposition). See the Fixed-Point Specification section above.

2. **Channel 1-2 interaction specification.** The link from Channel 1 to Channel 2 (crisis anticipation reduces information acquisition incentives) requires a specific functional form for how the crisis probability theta*(rho) enters the Grossman-Stiglitz informed-fraction decision. The Theory Builder must specify this before Phase 4 begins.

3. ~~**Yang (2024) and Danielsson-Uthemann (2025) engagement.**~~ **RESOLVED (Iteration 1).** Yang (2024) verified as purely RL-based with no rho parameterisation or analytical threshold derivation. Danielsson-Uthemann (2025, JFS) verified as using mu (AI fraction) with execution-speed mechanism, not signal correlation. Both papers are now explicitly differentiated in the Channel 1 mechanism description and Contribution 1 statement. The three-part differentiator from Danielsson-Uthemann (2025) is: (a) rho vs. mu as primitive, (b) analytical uniqueness/multiplicity boundary, (c) connection to Channels 2-3 via the amplification loop.

4. **Dou-Goldstein-Ji (2025b) mechanism verification.** Only search summaries are available. The Literature Guardian must verify whether this paper contains any information-theoretic channel or rho-like parameterisation. If it does, Contribution 4's differentiator must be sharpened.

5. **Hansen-Lee (2025) counterargument.** Their finding that AI reduces herding could challenge Channel 1. The Literature Guardian should verify whether their result holds when agents share the same model (rho near 1) vs. independent AI agents. If it does, the plan must address this directly.

6. **Szkup-Trevino (2015) interaction with rho.** Their sufficient conditions for uniqueness in global games with endogenous information acquisition may be violated when signals are correlated through a common AI source. The Theory Builder should check this in Phase 1.

7. **Empirical proxy credibility.** The DiD design uses ChatGPT release as an AI adoption shock. The Empirical Agent must justify why this event is relevant for institutional financial decision-making (as opposed to retail or text-processing applications). The 13F portfolio correlation proxy for rho needs a formal mapping from portfolio overlap to signal correlation.

---

## Changelog

### Iteration 1 -- Phase 2 Revision (2026-03-10)
- **Problem 1 (Danielsson-Uthemann 2025 engagement) -- RESOLVED.** Added a three-part differentiator from Danielsson and Uthemann (2025, JFS) in: (a) Channel 1 mechanism description (new "Differentiator from Danielsson and Uthemann (2025, JFS)" paragraph with rho vs. mu, uniqueness/multiplicity boundary, and three-channel connection); (b) Contribution 1 statement (added the three-dimension differentiator); (c) Contribution 4 statement (replaced the "Danielsson-Macrae-Uthemann (2022) qualitative narrative" differentiator with the precise three-channel integration differentiator referencing the 2025 JFS paper).
- **Problem 1b (Colliard-Foucault-Lovo 2025) -- RESOLVED.** Added a "Differentiator from Colliard-Foucault-Lovo (2025, RFS)" paragraph in the Channel 3 mechanism description, distinguishing single-agent RL pricing dynamics from cross-sectional correlation of N market makers.
- **Problem 2 (Fixed-point specification) -- RESOLVED.** Added a new section "Fixed-Point Specification (Amplification Loop)" between Contributions and Phases, containing: (a) three state variables (rho_eff, theta*, N_eff) with domains; (b) three equilibrium conditions / mappings (g_1: N_eff -> rho_eff, g_2: theta* -> mu_I -> rho_eff, g_3: mu_I -> N_eff) with functional forms; (c) composite operator T and Brouwer fixed-point existence argument with proof sketch; (d) Bifurcation Proposition with proof approach via spectral radius of the Jacobian DT.
- **Open Question 1 (fixed-point tractability) -- CLOSED.** Brouwer existence established; contraction mapping for uniqueness deferred to Theory Builder in Phase 4.
- **Open Question 3 (Yang/Danielsson-Uthemann engagement) -- CLOSED.** Both papers now fully verified and differentiated in the plan.
- Updated Paper Structure Map introduction to include Danielsson-Uthemann (2025, JFS) and Colliard-Foucault-Lovo (2025, RFS).

### Iteration 0 -- Initial Plan (2026-03-10)
- Created initial research plan from research_context.md and threat_map_v1.md.
- Five contributions defined (three channels + amplification loop + extension).
- Eight phases defined with sequencing constraints.
- Seven open questions flagged for Literature Guardian and Theory Builder.
- Key threat differentiators articulated for Yang (2024), Dugast-Foucault (2018, 2025), Danielsson et al. (2022), and Dou-Goldstein-Ji (2025a,b).
