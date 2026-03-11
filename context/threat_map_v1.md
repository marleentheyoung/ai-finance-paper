# Threat Map v1 -- Initial Scan

## Scan metadata
Date: 2026-03-10
Inputs read: context/research_context.md, context/literature_notes.md (template only), context/literature_constraints.md (empty)
Papers assessed: 30
Coverage gaps: Amplification loop (no existing paper models the three-channel fixed-point interaction)

---

## Channel 1 -- Coordination Failure (Global Games + rho)

### HIGH threat

- **Yang (2024)** -- *AI Coordination and Self-Fulfilling Financial Crises*, Working paper (Swiss Finance Institute / TSE)
  - Mechanism: Uses a global games framework to study how AI (reinforcement-learning) speculators endogenously coordinate on attack thresholds, producing self-fulfilling financial crises. AI agents converge on crisis equilibrium even absent fundamental information.
  - Overlap: Directly models AI-driven coordination failure in a global games setting. Shows that AI participation raises the probability of self-fulfilling crises, which is the core Channel 1 claim.
  - Differentiator: Yang studies emergent coordination by RL agents through repeated interaction, not signal homogeneity via a rho parameter. There is no analytical characterisation of a crisis threshold theta*(rho) as a function of cross-sectional signal correlation. The mechanism is behavioural convergence of learning algorithms, not the information-theoretic channel (common signal restoring multiplicity). Yang does not connect to Channels 2 or 3.
  - Status: VERIFIED (paper accessed via TSE conference page; mechanism confirmed through search summaries)

### MODERATE threat

- **Hellwig (2002)** -- *Public Information, Private Information, and the Multiplicity of Equilibria in Coordination Games*, JET
  - Mechanism: Proves that sufficiently precise public information reinstates multiple equilibria in Morris-Shin global games.
  - Overlap: The Channel 1 logic (rho -> common signal -> multiplicity) is a direct application of Hellwig's result.
  - Differentiator: Hellwig does not model AI, does not endogenise the precision or correlation of signals through technology adoption, and does not connect public information to information acquisition or market making. The contribution is embedding this mechanism in an AI context and connecting it to Channels 2 and 3.
  - Status: VERIFIED

- **Angeletos, Hellwig, and Pavan (2006)** -- *Signaling in a Global Game: Coordination and Policy Traps*, AER
  - Mechanism: Shows that endogenous policy signals can restore multiplicity in global games even without exogenous public information.
  - Overlap: Demonstrates that information structure endogeneity can undermine uniqueness -- related to the idea that AI adoption changes the information structure.
  - Differentiator: The signaling is by a policy-maker, not by a common technology. No AI, no rho parameterisation, no connection to information acquisition or market making.
  - Status: VERIFIED

- **Szkup and Trevino (2015)** -- *Information Acquisition in Global Games of Regime Change*, JET
  - Mechanism: Endogenises information acquisition in a global games coordination model. Shows strategic complementarities in actions do not always translate into complementarities in information acquisition; provides sufficient conditions for uniqueness.
  - Overlap: Connects information acquisition decisions to coordination failure equilibrium in global games -- directly relevant to the Channel 1-Channel 2 interaction.
  - Differentiator: Does not model correlated signals from a common source (AI). Signal correlation is not parameterised by rho. Does not study market making (Channel 3) or the amplification loop.
  - Status: VERIFIED

### LOW threat / Foundational

- **Morris and Shin (1998, 2002)** -- *Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks* (AER); *Social Value of Public Information* (AER)
  - Mechanism: Establish the global games framework: heterogeneous private signals yield unique threshold equilibrium; public information has disproportionate impact on coordination.
  - Overlap: Foundational for Channel 1. The project builds directly on this framework.
  - Differentiator: Foundational -- not a threat. Does not model AI, signal homogeneity, or rho.
  - Status: VERIFIED

- **Goldstein and Pauzner (2005)** -- *Demand Deposit Contracts and the Probability of Bank Runs*, JF
  - Mechanism: Applies global games to bank runs in a Diamond-Dybvig framework; derives unique crisis threshold as a function of contract terms.
  - Overlap: The project embeds rho into this specific framework.
  - Differentiator: Foundational -- the project extends this model with the rho parameterisation.
  - Status: VERIFIED

- **Angeletos and Pavan (2007)** -- *Efficient Use of Information and Social Value of Information*, Econometrica
  - Mechanism: Characterises the welfare implications of public vs. private information in coordination games; derives conditions under which public information is socially harmful.
  - Overlap: The welfare analysis of Channel 1 uses this framework.
  - Differentiator: Foundational -- provides the welfare toolkit, not the AI application.
  - Status: VERIFIED

---

## Channel 2 -- Information Acquisition (Grossman-Stiglitz + rho)

### HIGH threat

- **Dugast and Foucault (2018)** -- *Data Abundance and Asset Price Informativeness*, JFE
  - Mechanism: Models how cheap, fast (imprecise) signals crowd out demand for costly precise signals, reducing price informativeness even as data becomes abundant.
  - Overlap: Directly models crowding-out of fundamental information by cheap data signals -- closely parallels the Channel 2 mechanism where cheap AI signals crowd out costly private research.
  - Differentiator: Dugast-Foucault model the speed-precision tradeoff of a single data source over time, not the cross-sectional correlation of signals across agents using the same AI. Their rho equivalent is the cost difference between fast and slow signals, not the signal correlation structure. They do not model the Grossman-Stiglitz paradox in terms of correlated AI outputs destroying information diversity. No connection to coordination failure or market making.
  - Status: VERIFIED

- **Dugast and Foucault (2025)** -- *Equilibrium Data Mining and Data Abundance*, JF
  - Mechanism: Speculators search for predictors through trials; computing power and data abundance affect the threshold signal-to-noise ratio. Crowding reduces the value of data mining.
  - Overlap: Models endogenous information production with technology-driven crowding, related to the AI-driven crowding mechanism.
  - Differentiator: The mechanism is about search intensity and data mining thresholds, not about cross-sectional signal correlation (rho). Does not model Grossman-Stiglitz information aggregation or the revelation of private information through prices. No connection to Channels 1 or 3.
  - Status: VERIFIED

### MODERATE threat

- **Farboodi and Veldkamp (2020)** -- *Long-Run Growth of Financial Data Technology*, AER
  - Mechanism: Models how technological improvement in data processing affects the choice between processing public data and producing private signals. Technology can shift information production toward already-available data.
  - Overlap: Addresses a technology-driven shift in information acquisition, conceptually similar to AI driving agents toward common signals.
  - Differentiator: Does not model cross-sectional signal correlation. The mechanism is about the growth of data technology over time, not the homogeneity of AI outputs. Does not derive price informativeness consequences via Grossman-Stiglitz or connect to coordination/market-making channels.
  - Status: VERIFIED

- **Farboodi, Matray, Veldkamp, and Venkateswaran (2022)** -- *Where Has All the Data Gone?*, RFS
  - Mechanism: Documents and models how data abundance concentrates on large firms, leaving small firms informationally impoverished.
  - Overlap: Empirically documents that data technology creates information concentration rather than diffusion -- consistent with rho -> 1 for covered assets.
  - Differentiator: The mechanism is about cross-sectional asset coverage, not cross-agent signal correlation. No formal rho parameterisation, no Grossman-Stiglitz extension, no connection to coordination or market making.
  - Status: VERIFIED

- **Goldstein and Yang (2015)** -- *Information Diversity and Complementarities in Trading and Information Acquisition*, JF
  - Mechanism: Shows that diversity of information dimensions creates strategic complementarities in information acquisition. When one dimension is publicly known, traders invest more in other dimensions.
  - Overlap: The Channel 2 model uses Goldstein-Yang's information diversity mechanism. When AI homogenises one dimension, complementarities break down.
  - Differentiator: Foundational for Channel 2 mechanism. Goldstein-Yang do not model AI or signal correlation driven by a common technology. They establish the complementarity result that the project applies.
  - Status: VERIFIED

- **Banerjee, Davis, and Gondhi (2018)** -- *When Transparency Improves, Must Prices Reflect Fundamentals Better?*, RFS
  - Mechanism: Shows that increasing transparency (cheaper fundamental information) can decrease price informativeness because investors shift toward learning about others' beliefs rather than fundamentals.
  - Overlap: Demonstrates that cheaper information can paradoxically reduce informativeness -- related to the AI-driven information paradox in Channel 2.
  - Differentiator: The mechanism is about the composition of what investors learn (fundamentals vs. beliefs), not about cross-sectional signal correlation from AI. Does not use rho parameterisation or connect to coordination/market-making.
  - Status: VERIFIED

### LOW threat / Foundational

- **Grossman and Stiglitz (1980)** -- *On the Impossibility of Informationally Efficient Markets*, AER
  - Mechanism: Establishes the informational paradox: costly information acquisition is incompatible with full price efficiency.
  - Overlap: Foundational for Channel 2.
  - Differentiator: Foundational -- the project extends GS with correlated AI signals (rho).
  - Status: VERIFIED

- **Holden and Subrahmanyam (1992)** -- *Long-Lived Private Information and Imperfect Competition*, JF
  - Mechanism: Shows that competition among identically informed traders leads to aggressive trading and rapid information revelation.
  - Overlap: Used in Channel 2 to show that correlated AI information (rho -> 1) yields zero rents via the HS competition result.
  - Differentiator: Foundational -- provides the competition mechanism that the project applies to correlated AI signals.
  - Status: VERIFIED

- **Bond, Edmans, and Goldstein (2012)** -- *The Real Effects of Financial Markets*, ARFE
  - Mechanism: Distinguishes forecasting price efficiency (FPE) from revelatory price efficiency (RPE); establishes the real-effects feedback channel.
  - Overlap: The welfare analysis of Channel 2 uses the FPE/RPE distinction.
  - Differentiator: Foundational -- provides the welfare framework.
  - Status: VERIFIED

---

## Channel 3 -- Market Making (Correlated Liquidity Withdrawal)

### HIGH threat

None identified.

### MODERATE threat

- **Cespa and Vives (forthcoming)** -- *Market Opacity and Fragility: Why Liquidity Evaporates When It Is Most Needed*, conditionally accepted AER
  - Mechanism: Market opacity creates strategic complementarity in liquidity demand, yielding multiple equilibria where liquidity can evaporate suddenly (flash crash). Lack of transparency makes hedgers' price impact strategic complements.
  - Overlap: Models endogenous liquidity fragility via strategic complementarity in trading -- directly related to Channel 3's mechanism of correlated liquidity withdrawal.
  - Differentiator: The fragility mechanism operates through opacity and hedger behaviour, not through correlated AI signals among market makers. There is no rho parameterisation, no N_eff formula, and no connection to AI model homogeneity. The complementarity arises from the information structure of the market, not from algorithmic similarity.
  - Status: VERIFIED

- **Greenwood and Thesmar (2011)** -- *Stock Price Fragility*, JFE
  - Mechanism: Defines stock fragility as the covariance of holders' demand shocks. High fragility implies correlated selling and price instability.
  - Overlap: N_eff(rho) in Channel 3 is constructed as an analogue of Greenwood-Thesmar fragility applied to algorithmic market makers.
  - Differentiator: Greenwood-Thesmar measure correlation of demand shocks from mutual fund flows, not from AI-driven market-making decisions. No formal model of market maker equilibrium with algorithmic homogeneity.
  - Status: VERIFIED

- **Danielsson, Macrae, and Uthemann (2022)** -- *Artificial Intelligence and Systemic Risk*, JBF
  - Mechanism: Argues qualitatively that AI homogenises risk perceptions and increases procyclicality. AI settles on a small homogeneous set of risk management techniques; similar perceptions lead to similar actions; result is lower volatility but fatter tails.
  - Overlap: Makes the same broad argument as this project: AI homogeneity -> correlated actions -> systemic risk. Discusses procyclicality, trust in AI, and model monoculture.
  - Differentiator: Entirely qualitative/narrative -- no formal model, no equilibrium analysis, no rho parameterisation, no specific channel decomposition. Does not model coordination games, information acquisition, or market-making equilibrium. The project's contribution is formalising these qualitative insights.
  - Status: VERIFIED

- **Danielsson, Shin, and Zigrand (2012)** -- *Endogenous and Systemic Risk*, NBER chapter
  - Mechanism: Formalises how common VaR constraints produce endogenous risk: correlated risk management leads to procyclical selling and amplified price impact.
  - Overlap: Common VaR constraints are a special case of the Channel 3 mechanism (correlated risk limits -> simultaneous withdrawal).
  - Differentiator: The homogeneity arises from regulatory constraints (VaR), not from AI model outputs. The project nests this as a limiting case but adds the AI-specific rho parameterisation and connects to Channels 1 and 2.
  - Status: VERIFIED

### LOW threat / Foundational

- **Glosten and Milgrom (1985)** -- *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, JFE
  - Mechanism: Market makers widen spreads in response to adverse selection.
  - Overlap: Foundational for Channel 3 spread-widening mechanism.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Kyle (1985)** -- *Continuous Auctions and Insider Trading*, Econometrica
  - Mechanism: Establishes the linear equilibrium in a market with informed trading and noise traders.
  - Overlap: Foundational for Channel 3.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Avellaneda and Stoikov (2008)** -- *High-Frequency Trading in a Limit Order Book*, QF
  - Mechanism: Optimal market-making via stochastic control; reservation price r = S - q*gamma*sigma^2*(T-t).
  - Overlap: The Channel 3 model uses this framework to show that calibration on shared data produces identical spread-widening functions.
  - Differentiator: Foundational -- provides the market-making framework.
  - Status: VERIFIED

- **Pagano (1989)** -- *Trading Volume and Asset Liquidity*, QJE
  - Mechanism: Multiple equilibria in market participation -- low-liquidity traps where thin markets are self-reinforcing.
  - Overlap: The Channel 3 threshold rho** (no finite-spread equilibrium) is analogous to Pagano's low-liquidity trap.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Brunnermeier and Pedersen (2009)** -- *Market Liquidity and Funding Liquidity*, RFS
  - Mechanism: Margin spirals create feedback between market liquidity and funding liquidity.
  - Overlap: Channel 3 connects to margin spiral mechanics.
  - Differentiator: Foundational -- provides the liquidity spiral framework, not the AI correlation mechanism.
  - Status: VERIFIED

---

## Amplification Loop (Fixed-Point Interaction)

### HIGH threat

None identified. No paper found that models the joint fixed-point interaction of coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a common rho parameter.

### MODERATE threat

- **Dou, Goldstein, and Ji (2025a)** -- *AI-Powered Trading, Algorithmic Collusion, and Price Efficiency*, NBER WP 34054
  - Mechanism: RL-powered trading algorithms autonomously sustain collusive supra-competitive profits. Two mechanisms: homogenisation of strategies and self-confirming equilibrium. AI collusion undermines competition, market efficiency, and liquidity.
  - Overlap: Models AI agents producing correlated trading behaviour that harms price efficiency and liquidity -- touches on Channels 2 and 3 simultaneously.
  - Differentiator: The mechanism is algorithmic collusion via reinforcement learning (emergent coordination through repeated interaction), not signal homogeneity through a common information source. There is no rho parameterisation, no global games coordination failure (Channel 1), and no fixed-point across three distinct channels. The collusion is a behavioural outcome of RL, not an information-theoretic result.
  - Status: VERIFIED

- **Dou, Goldstein, and Ji (2025b)** -- *Financial Market Fragility in the Era of AI Planning*, SSRN WP 5763222
  - Mechanism: AI speculators with planning capability (agentic AI) learn intertemporal collusive strategies, creating and exploiting negative bubbles. Dynamic trading framework with positive-feedback investors and constrained arbitrageurs.
  - Overlap: Models AI-driven market fragility -- directly related to the overall thesis. Addresses feedback effects and market manipulation by coordinated AI agents.
  - Differentiator: The mechanism is intertemporal collusion via planning-capable RL agents, not signal homogeneity or the rho parameterisation. No global games (Channel 1), no Grossman-Stiglitz information acquisition (Channel 2), no N_eff formula (Channel 3). The AI agents are strategic oligopolists, not price-taking agents with correlated signals.
  - Status: [UNVERIFIED] -- abstract accessed via search summaries only; full paper mechanism not confirmed from direct reading

- **Danielsson, Macrae, and Uthemann (2022)** -- *Artificial Intelligence and Systemic Risk*, JBF
  - Mechanism: (See Channel 3 entry above.) Qualitatively argues that AI creates procyclicality via model monoculture, affecting risk measurement, trust dynamics, and tail risk.
  - Overlap: The only published paper that explicitly argues for a multi-channel AI-homogeneity-to-fragility narrative.
  - Differentiator: Entirely qualitative. No formal model, no equilibrium analysis, no fixed-point characterisation. The project formalises what Danielsson et al. describe verbally.
  - Status: VERIFIED

### LOW threat / Foundational

- **Goldstein, Huang, and Yang (2025)** -- *Fragility of Financial Markets*, Annual Review of Financial Economics
  - Mechanism: Survey of forces generating market fragility: learning from prices, strategic complementarities, amplification channels. Provides a canonical trading framework.
  - Overlap: Survey covering the theoretical foundations of market fragility. The project's amplification loop is a specific instance of the multi-channel fragility framework this survey describes.
  - Differentiator: Survey paper -- organises existing knowledge but does not model the AI-specific mechanisms or the rho-driven fixed-point.
  - Status: VERIFIED

---

## AI and Financial Markets (Empirical / Applied)

### HIGH threat

None identified.

### MODERATE threat

- **Kim, Muhn, and Nikolaev (2024)** -- *From Transcripts to Insights: Uncovering Corporate Risks Using Generative AI*, arXiv
  - Mechanism: Empirically demonstrates that GPT-4 at temperature=0 produces near-identical financial statement analyses, documenting belief homogenisation from AI.
  - Overlap: Provides direct empirical evidence for the rho -> 1 claim. If this paper is already published with a theoretical framework, it could pre-empt the empirical motivation.
  - Differentiator: Purely empirical -- documents the phenomenon but does not build a formal model of its consequences. The project uses this as empirical motivation, not as a competing theoretical contribution.
  - Status: VERIFIED

- **Calvano, Calzolari, Denicolo, and Pastorello (2020)** -- *Artificial Intelligence, Algorithmic Pricing, and Collusion*, AER
  - Mechanism: Q-learning algorithms autonomously learn to sustain supra-competitive prices in oligopoly. Collusive outcomes without communication.
  - Overlap: Demonstrates that AI agents can coordinate without explicit communication -- foundational for the argument that AI creates correlated behaviour.
  - Differentiator: Set in a product pricing context, not financial markets. No information acquisition, no market making, no signal correlation mechanism. The coordination is through repeated RL interaction, not common signals.
  - Status: VERIFIED

- **Hansen and Lee (2025)** -- *Financial Stability Implications of Generative AI: Taming the Animal Spirits*, Fed FEDS WP 2025-090
  - Mechanism: Laboratory experiments with LLMs replicating classic herding studies. Finds AI agents are more rational than humans and rely more on private information, potentially reducing herding.
  - Overlap: Directly studies AI agents in financial coordination/herding settings. The finding that AI reduces herding is a potential counterargument to Channel 1.
  - Differentiator: Experimental/simulation approach; does not build a formal equilibrium model. The finding of less herding is for AI agents with independent prompts, not for agents sharing the same underlying model/signal (rho -> 1). Does not distinguish between independent AI agents and homogeneous AI agents.
  - Status: [UNVERIFIED] -- full mechanism not confirmed; counterargument interpretation needs verification

### LOW threat / Foundational

- **Gu, Kelly, and Xiu (2020)** -- *Empirical Asset Pricing via Machine Learning*, RFS
  - Mechanism: Documents that diverse ML methods converge on the same dominant predictors (momentum, liquidity, volatility).
  - Overlap: Empirical foundation for rho -> 1 claim. Demonstrates convergence of ML outputs.
  - Differentiator: Empirical asset pricing paper -- no theoretical model of consequences. Used as empirical motivation.
  - Status: VERIFIED

---

## Aggregate Novelty Assessment

### Overall threat level: MODERATE

### Channel-level summary
| Channel | HIGH threats | Strongest differentiator |
|---------|-------------|------------------------|
| 1 -- Coordination | 1 (Yang 2024) | Yang uses RL-based behavioural convergence, not information-theoretic signal correlation via rho; no analytical theta*(rho) |
| 2 -- Information  | 1 (Dugast-Foucault 2018) | DF model speed-precision tradeoff over time, not cross-sectional signal correlation destroying information diversity |
| 3 -- Market Making | 0 | No paper models N_eff(rho) for AI-driven correlated market-maker withdrawal |
| Amplification Loop | 0 | No paper models the three-channel fixed-point in (rho_eff, theta*, N_eff) |

### Core contribution status
The amplification loop -- the fixed-point in (rho_eff, theta*, N_eff) across the three channels -- is NOT directly threatened by any identified paper. No existing work connects coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a single parameterisation of signal homogeneity. The closest competitor is Danielsson, Macrae, and Uthemann (2022), which makes the same qualitative argument but without formal modelling. The Dou-Goldstein-Ji papers model AI-driven market fragility through different mechanisms (RL-based collusion, not signal correlation). The core contribution appears novel at the mechanism level, though this assessment is subject to revision as more papers are examined.

### Key risks for the Research Director
- **Yang (2024) is the single largest threat to Channel 1.** The research plan must clearly articulate why the information-theoretic mechanism (rho -> common signal -> multiplicity restoration) is distinct from and complementary to Yang's RL-based coordination mechanism. Consider citing Yang as a complementary computational finding.
- **Dugast and Foucault (2018, 2025) are the primary threats to Channel 2.** The differentiator (cross-sectional correlation vs. temporal speed-precision tradeoff) must be made explicit in the introduction. The project must show that rho captures something DF's models do not: the collapse of information diversity when N agents share the same AI model.
- **Danielsson et al. (2022) claim priority on the qualitative argument.** The introduction must acknowledge their narrative contribution and position this paper as the formal model that substantiates their verbal argument.
- **The Dou-Goldstein-Ji research program is active and prolific.** Goldstein is a co-author on foundational papers used in Channels 2 and 3. The research plan should engage these papers explicitly and position the rho-based approach as complementary (information-theoretic) rather than competing (RL/behavioural).

### Papers requiring deeper investigation
- **Dou, Goldstein, and Ji (2025b)** -- *Financial Market Fragility in the Era of AI Planning*: Only search summaries available. Need to verify whether the paper contains any information-theoretic channel or rho-like parameterisation. [UNVERIFIED]
- **Yang (2024)** -- *AI Coordination and Self-Fulfilling Financial Crises*: Need to verify whether the paper endogenises the global games information structure or treats AI as an exogenous change in agent behaviour. [UNVERIFIED -- partial]
- **Hansen and Lee (2025)** -- *Financial Stability Implications of Generative AI*: Need to verify whether their finding that AI reduces herding is robust to the case where all agents share the same model (rho -> 1 vs. independent AI agents). [UNVERIFIED]
- **Szkup and Trevino (2015)** -- *Information Acquisition in Global Games of Regime Change*: Need to check whether their sufficient conditions for uniqueness are violated when signals are correlated through a common AI source. [VERIFIED -- mechanism confirmed, but interaction with rho not assessed]
- **Cespa and Vives (forthcoming)** -- *Market Opacity and Fragility*: Need to check whether their strategic complementarity mechanism could be reinterpreted as AI-driven opacity. [UNVERIFIED]
