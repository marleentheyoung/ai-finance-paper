# Literature Constraints

## What the literature has addressed

### Channel 1 -- Coordination Failure
- Morris-Shin (1998, 2002) established that heterogeneous private signals produce unique threshold equilibria in global games, eliminating sunspot multiplicity.
- Hellwig (2002) proved that sufficiently precise public information reinstates multiple equilibria, providing the formal mechanism that underlies the Channel 1 claim.
- Goldstein-Pauzner (2005) applied global games to bank runs, deriving a unique crisis threshold as a function of contract terms.
- Angeletos-Pavan (2007) characterised the welfare cost of public information in coordination games with strategic complementarity.
- Szkup-Trevino (2015) endogenised information acquisition in global games, showing that strategic complementarities in actions do not always translate into complementarities in information acquisition.
- Yang (2024) studied how AI (RL) speculators endogenously coordinate on crisis equilibrium in a global games setting, showing AI raises the probability of self-fulfilling crises. Uses Q-learning in Morris-Shin (1998) framework; purely computational/RL mechanism, no rho parameter, no analytical threshold derivation.
- Danielsson and Uthemann (2025, JFS) derived a formal game-theoretic model of AI-driven coordination failure using global games. The crisis threshold theta*(mu) = (c/b)[(1-mu)p + mu] is a function of the AI agent fraction mu and the human execution probability p. The formal model covers only the coordination/run channel; three other channels (information processing, common data, speed) are discussed qualitatively. Uses mu (AI fraction), not rho (signal correlation), as the primitive. Does not integrate the Hellwig (2002) multiplicity result into the formal model.

### Channel 2 -- Information Acquisition
- Grossman-Stiglitz (1980) established the impossibility of informationally efficient markets when information is costly.
- Holden-Subrahmanyam (1992) showed that competition among identically informed traders leads to aggressive revelation and zero rents.
- Goldstein-Yang (2015) demonstrated that information diversity creates strategic complementarities in information acquisition.
- Bond-Edmans-Goldstein (2012) distinguished FPE from RPE, establishing the real-effects feedback channel.
- Vives (2014, JEEA) showed that a privately revealing equilibrium obtains when correlation in traders' valuations is not too large, establishing that high correlation undermines the Grossman-Stiglitz resolution. This provides foundational support for the Channel 2 claim that as rho rises, informational efficiency conditions are violated.
- Dugast-Foucault (2018) showed that cheap, fast signals crowd out demand for costly precise signals, reducing price informativeness. This is the closest existing model to the Channel 2 mechanism but operates through speed-precision tradeoffs rather than cross-sectional signal correlation.
- Dugast-Foucault (2025) extended the data mining framework to show how computing power affects predictor search.
- Farboodi-Veldkamp (2020) modelled the long-run growth of financial data technology.
- Farboodi et al. (2022) documented data concentration on large firms.
- Banerjee-Davis-Gondhi (2018) showed that transparency can reduce informativeness by shifting learning from fundamentals to beliefs.
- Barucca-Morone (2025, arXiv) conceptually discussed how AI as universal approximators reshapes market efficiency, but without a formal GS extension or rho parameterisation.

### Channel 3 -- Market Making
- Glosten-Milgrom (1985), Kyle (1985), and Avellaneda-Stoikov (2008) provide the foundational market-making frameworks.
- Greenwood-Thesmar (2011) defined stock fragility as covariance of holders' demand shocks.
- Pagano (1989) established the low-liquidity trap (multiple equilibria in market participation).
- Brunnermeier-Pedersen (2009) modelled margin spirals between market and funding liquidity.
- Danielsson-Shin-Zigrand (2012) formalised endogenous risk from common VaR constraints.
- Cespa-Vives (forthcoming) showed that market opacity creates strategic complementarity in liquidity demand, yielding multiple equilibria.
- Danielsson-Macrae-Uthemann (2022) qualitatively argued that AI homogenises risk perceptions and increases procyclicality.
- Colliard-Foucault-Lovo (2025, RFS) formally modelled Q-learning algorithmic market makers in a Glosten-Milgrom adverse selection framework. Single-agent RL pricing dynamics, not cross-sectional correlation among market makers.

### Amplification Loop
- No existing paper models the joint fixed-point interaction across coordination failure, information acquisition, and market making through a common parameterisation of signal homogeneity.
- Danielsson et al. (2022) make the qualitative argument but without formal modelling.
- Dou-Goldstein-Ji (2025a, 2025b) model AI-driven market fragility through RL-based collusion mechanisms, not signal correlation.
- Goldstein-Huang-Yang (2025) survey the theoretical foundations of market fragility across multiple channels but do not model AI-specific mechanisms.

## What the literature has NOT addressed (gaps)

### Channel 1 -- Coordination Failure
- **Gap 1.1:** No paper derives the crisis threshold theta*(rho) as a function of cross-sectional signal correlation in a global games framework. Hellwig (2002) treats public information precision as exogenous; Danielsson-Uthemann (2025) derive theta*(mu) as a function of AI fraction but not signal correlation; Yang (2024) learns the threshold computationally via Q-learning but does not derive it analytically. This project parameterises the threshold through rho (AI signal correlation), which is a distinct primitive from both mu and RL convergence.
- **Gap 1.2:** No paper connects the global games coordination failure mechanism to information acquisition (Channel 2) or market making (Channel 3) through a common rho parameter.
- **Gap 1.3:** The non-monotonicity of theta*(rho) -- fragility rising in rho up to rho* before uniqueness fails entirely -- has not been characterised in an AI context.

### Channel 2 -- Information Acquisition
- **Gap 2.1:** No paper extends Grossman-Stiglitz with two information types (AI-processed at low cost with correlation rho, and genuinely private at high cost with rho near 0) to show how AI homogeneity destroys information diversity.
- **Gap 2.2:** The interaction between Holden-Subrahmanyam competition (correlated signals -> zero rents) and Goldstein-Yang information complementarities (homogenisation of one dimension -> breakdown of complementarities) has not been formalised.
- **Gap 2.3:** No paper distinguishes the effect of AI on FPE vs. RPE in a model where AI improves FPE while degrading RPE.

### Channel 3 -- Market Making
- **Gap 3.1:** No paper derives N_eff(rho) = N(1+(N-1)rho)^{-1} as a liquidity fragility index grounded in algorithmic similarity among market makers.
- **Gap 3.2:** No paper derives the threshold rho** above which no interior market-making equilibrium with finite spreads exists, as an analogue of Pagano's low-liquidity trap driven by AI homogeneity.
- **Gap 3.3:** The convexity of the equilibrium bid-ask spread in rho has not been established.

### Amplification Loop
- **Gap 4.1:** No paper characterises the fixed-point equilibrium in (rho_eff, theta*, N_eff) where the three channels mutually amplify.
- **Gap 4.2:** The key proposition -- that the joint rho* at which the integrated system becomes fragile is strictly lower than the rho* implied by any single channel -- has not been established.
- **Gap 4.3:** No paper shows that moderate model correlation that appears safe under any individual risk framework may be wholly inadequate against the compound mechanism.

## Coverage gaps requiring deeper search

1. **AI and global games (Channel 1):** Two papers found (Yang 2024; Danielsson-Uthemann 2025), but neither uses signal correlation (rho) as the primitive. The information-theoretic mechanism (rho -> common signal -> Hellwig multiplicity restoration) remains unmodelled. Margaretic-Pasten (2014) extend Goldstein-Pauzner with correlated bank fundamentals, but this is fundamental correlation, not signal correlation. Hansen-Lee (2025) test AI herding but only with independently queried agents (low rho). [RESOLVED -- gap confirmed open after 22 systematic searches in Mode 3]
2. **Correlated AI market making (Channel 3):** Colliard-Foucault-Lovo (2025) models RL market-making but single-agent. No paper found that formally models correlated AI-driven market making with N_eff(rho) or an equivalent effective diversity measure. [RESOLVED -- gap confirmed open after Mode 3 deep search]
3. **Multi-channel systemic risk models:** No paper found that connects coordination failure, information acquisition, and liquidity provision through a common parameterisation, even outside the AI context. Acemoglu-Ozdaglar-Tahbaz-Salehi (2015) and network systemic risk models address propagation through networks, not through signal correlation across channels. [RESOLVED -- gap confirmed open after Mode 3 deep search]
4. **Empirical AI homogeneity:** Beyond Gu-Kelly-Xiu (2020) and Kim-Muhn-Nikolaev (2024), no additional academic papers found rigorously measuring cross-sectional correlation of AI/ML trading signals or portfolio positions. Policy reports from IMF, FSB, and BIS discuss AI herding qualitatively but do not provide formal measurement. [RESOLVED -- gap persists in the academic literature but is not the project's primary contribution]
5. **Endogenous rho / diversity mandate:** Gans (2023, Economica) models AI adoption externalities in product markets. Kleinberg-Raghavan (2021, PNAS) and Peng et al. (2024, NeurIPS) model algorithmic monoculture costs in general and matching market settings. No paper models competitive AI adoption as a prisoner's dilemma driving signal correlation above a fragility threshold in financial markets. [RESOLVED -- gap confirmed open after Mode 3 deep search]

## Changelog

### Quick Scan -- 2026-03-10
Initial version produced from research_context.md and web search. 30 papers assessed across all channels. Key new papers identified: Yang (2024), Dugast-Foucault (2018, 2025), Dou-Goldstein-Ji (2025a, 2025b), Cespa-Vives (forthcoming), Farboodi-Veldkamp (2020), Banerjee-Davis-Gondhi (2018), Danielsson-Macrae-Uthemann (2022), Calvano et al. (2020), Hansen-Lee (2025), Goldstein-Huang-Yang (2025). Five papers flagged for deeper investigation.

### Iteration 1 Targeted Check -- 2026-03-10
- Added Danielsson-Uthemann (2025, JFS) to Channel 1 constraints. This paper formally models AI-driven coordination failure with theta*(mu) but does not use rho or model Channels 2-3.
- Added Colliard-Foucault-Lovo (2025, RFS) to Channel 3 constraints. RL market-making model, single-agent.
- Updated Gap 1.1 to reflect that two papers now exist in the AI + global games space but neither uses signal correlation as the primitive.
- Resolved five UNVERIFIED papers: Yang (2024), Dou-Goldstein-Ji (2025b), Hansen-Lee (2025), Cespa-Vives (forthcoming) all confirmed as using mechanisms distinct from the project's.
- All gaps in Channels 2, 3, and the Amplification Loop remain open. No new competing papers found for Contributions 2-5.

### Iteration 2 Targeted Check -- 2026-03-10
- Verified the Danielsson-Uthemann (2025, JFS) formula theta*(mu) = (c/b)[(1-mu)p + mu] against the full paper text (equation 4). Confirmed correct. The paper presents no formal propositions or theorems, discusses Hellwig (2002) multiplicity only qualitatively (Section 2.2.2), and contains no rho parameter for signal correlation.
- Verified the Colliard-Foucault-Lovo (2025, RFS) characterisation as single-agent Q-learning in Glosten-Milgrom framework. Confirmed: no cross-sectional correlation, no N_eff, no simultaneous withdrawal.
- Confirmed that Dou-Goldstein-Ji (2025a, 2025b) and Goldstein-Huang-Yang (2025 survey) contain no three-equation fixed-point system and no rho-like signal correlation parameterisation.
- Confirmed that the fixed-point specification in (rho_eff, theta*, N_eff) with Brouwer existence is novel. No competing paper found in targeted search.
- Confirmed that the bifurcation result (joint rho* < min of individual channel thresholds) has no competitor.
- All gaps (1.1-1.3, 2.1-2.3, 3.1-3.3, 4.1-4.3) remain open. No new coverage gaps identified.

### Final (Mode 3) -- 2026-03-10
- Conducted 22 systematic web searches covering all five novelty claims, all risk flags from novelty_claims.md, and additional coverage areas (global games + AI, GS extensions, AI market making, macroprudential + AI, systemic risk + model diversity).
- Added six new papers to the literature mapping: Margaretic-Pasten (2014, JBF) on correlated bank fundamentals in Goldstein-Pauzner; Vives (2014, JEEA) on information efficiency under correlated valuations; Barucca-Morone (2025, arXiv) on AI and market efficiency; Gans (2023, Economica) on AI adoption externalities; Kleinberg-Raghavan (2021, PNAS) on algorithmic monoculture; Peng et al. (2024, NeurIPS) on monoculture in matching markets.
- No new papers found that extend Goldstein-Pauzner with signal correlation (rho) or derive theta*(rho). Margaretic-Pasten (2014) extend with fundamental correlation, which is distinct.
- No new papers found extending Grossman-Stiglitz with cross-sectional AI signal correlation. No Dugast-Foucault extension adding cross-sectional correlation found.
- No new papers found deriving N_eff or equivalent effective diversity measure for correlated algorithmic market makers.
- No new papers found modelling a multi-channel fixed-point in three or more financial fragility state variables, or applying Brouwer's theorem to such a system.
- No new papers found by Danielsson, Uthemann, Dou, Goldstein, Ji, or co-authors extending their models toward multi-channel integration or signal correlation parameterisation.
- Confirmed all 12 gaps (1.1-1.3, 2.1-2.3, 3.1-3.3, 4.1-4.3) remain open in the published literature.
- Resolved all five coverage gaps from prior iterations. All gaps marked as RESOLVED (confirmed open).
- All UNVERIFIED papers resolved. No UNRESOLVED entries remain.
- Document status: Final (Mode 3).
