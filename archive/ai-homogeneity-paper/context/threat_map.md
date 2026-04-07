# Threat Map v1 -- Initial Scan

## Scan metadata
Date: 2026-03-10
Inputs read: context/research_context.md, context/literature_notes.md (template only), context/literature_constraints.md (empty)
Papers assessed: 30
Coverage gaps: Amplification loop (no existing paper models the three-channel fixed-point interaction)

---

## Channel 1 -- Coordination Failure (Global Games + rho)

### HIGH threat

- **Yang (2024)** -- *AI Coordination and Self-Fulfilling Financial Crises*, Working paper (Swiss Finance Institute / USI Lugano)
  - Mechanism: Uses a Morris-Shin (1998) speculative attack framework with two Q-learning agents who learn attack thresholds through repeated interaction. AI speculators coordinate more effectively on the crisis equilibrium than both Nash equilibrium predictions and human experimental subjects. Under low information accuracy, AI agents overestimate others' attack probability, raising crisis likelihood. Under public information, AI speculators coordinate on higher thresholds (reducing crisis probability) but with higher variance (less predictable crises).
  - Overlap: Directly models AI-driven coordination failure in a global games setting. Shows that AI participation raises the probability of self-fulfilling crises, which is the core Channel 1 claim.
  - Differentiator: Yang's mechanism is entirely RL-based (Q-learning behavioural convergence through repeated interaction), not information-theoretic. There is no signal correlation parameter rho -- the model uses standard Morris-Shin private signals with exogenous precision. The crisis threshold is learned computationally via Q-value convergence, not derived analytically as theta*(rho). Yang does not model information acquisition (Channel 2) or market making (Channel 3). The paper is computational/experimental (1,000 simulation sessions per parametrisation), not a formal equilibrium characterisation. The project's Channel 1 contribution is analytically deriving theta*(rho) from the signal structure itself, which Yang does not attempt.
  - Status: VERIFIED (full paper read; 102 pages; mechanism confirmed as purely RL-based with no rho parameterisation or analytical threshold derivation)

- **Danielsson and Uthemann (2025)** -- *Artificial Intelligence and Financial Crises*, Journal of Financial Stability, Vol. 80
  - Mechanism: Uses a global games framework (Morris-Shin 1998) to model how AI amplifies financial vulnerabilities. Derives a crisis threshold theta* = (c/b)[(1-mu)p + mu] where mu is the fraction of AI agents and p < 1 is the probability that humans successfully execute a run. Since AI agents always succeed at running (probability 1), increasing mu raises theta* and makes crises more likely. Discusses four qualitative channels: superior information processing, common data, speed, and strategic complementarities. Only the speed channel (heterogeneous success probabilities) is formally modelled in the equilibrium.
  - Overlap: This is a formal game-theoretic model of AI-driven coordination failure -- directly competes with Channel 1. Derives an analytical crisis threshold as a function of AI penetration. Published in a peer-reviewed journal.
  - Differentiator: (1) The parameterisation is mu (fraction of AI agents), not rho (signal correlation). The model does not formalise signal homogeneity or cross-sectional correlation. The threshold theta*(mu) captures AI speed advantage, not the information-theoretic mechanism where correlated signals restore multiplicity a la Hellwig (2002). (2) Despite discussing four channels qualitatively, only the coordination/run channel is formally modelled. No information acquisition (Channel 2), no market-making equilibrium (Channel 3), no N_eff, no amplification loop or fixed-point. (3) No formal propositions or theorems are stated; the main results are comparative statics on the threshold formula. (4) The Hellwig (2002) multiplicity result is discussed qualitatively but not integrated into the formal model -- the model does not characterise the boundary between uniqueness and multiplicity as a function of signal correlation.
  - Status: VERIFIED (full HTML version read on arXiv; published in JFS 2025; formal model confirmed as single-channel with mu parameterisation)

  **Implication for the research plan:** This paper narrows the novelty gap for Channel 1. The plan must now differentiate not only from Yang (2024) but also from Danielsson-Uthemann (2025). The key differentiators are: (a) rho (signal correlation) vs. mu (AI fraction) as the primitive, (b) the information-theoretic mechanism (common signal restoring multiplicity per Hellwig 2002) vs. the speed mechanism (heterogeneous execution probabilities), (c) analytical characterisation of the uniqueness/multiplicity boundary as a function of rho, which neither Yang nor Danielsson-Uthemann provide, and (d) connection to Channels 2 and 3 through the amplification loop.

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

- **Colliard, Foucault, and Lovo (2025)** -- *Algorithmic Pricing and Liquidity in Securities Markets*, forthcoming Review of Financial Studies
  - Mechanism: Studies Q-learning algorithmic market makers in a Glosten-Milgrom (1985) adverse selection framework. Shows that Q-learning market makers charge markups that increase when adverse selection costs decrease -- contrary to Nash equilibrium predictions. Identifies behavioural "footprints" of ML-based pricing in trading data.
  - Overlap: Formally models AI-driven market making with learning algorithms, directly relevant to Channel 3's domain. Demonstrates that algorithmic market makers can produce non-competitive pricing behaviour.
  - Differentiator: The mechanism is about RL-based pricing by individual market makers learning in a strategic environment, not about cross-sectional correlation of AI signals among multiple market makers. There is no rho parameterisation, no N_eff formula, no simultaneous withdrawal mechanism, and no connection to information acquisition or coordination failure channels. The focus is on a single market maker's learning dynamics, not on the correlated behaviour of N market makers sharing the same AI model.
  - Status: VERIFIED (mechanism confirmed via SSRN page and search results)

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
  - Note: The Danielsson-Uthemann research programme has since produced a 2025 paper with a formal game-theoretic model (see Channel 1 HIGH threat entry for Danielsson and Uthemann 2025, JFS). However, the 2022 JBF paper remains the primary reference for the multi-channel qualitative narrative, as the 2025 paper formalises only the coordination/run channel.
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

- **Dou, Goldstein, and Ji (2025b)** -- *Financial Market Fragility in the Era of AI Planning*, SSRN WP 5763222 (November 2025)
  - Mechanism: AI speculators with planning capability (agentic AI) learn intertemporal collusive strategies, creating and exploiting negative bubbles. Dynamic trading framework with positive-feedback investors, constrained arbitrageurs, and oligopolistic informed speculators who coordinate intertemporally -- trading aggressively in tandem to generate negative bubbles and unwinding in a coordinated manner.
  - Overlap: Models AI-driven market fragility -- directly related to the overall thesis. Addresses feedback effects and coordinated destabilisation by AI agents.
  - Differentiator: The mechanism is intertemporal collusion via planning-capable RL agents, not signal homogeneity or the rho parameterisation. No global games (Channel 1), no Grossman-Stiglitz information acquisition (Channel 2), no N_eff formula (Channel 3). The AI agents are strategic oligopolists, not price-taking agents with correlated signals. The fragility arises from AI planning capability (looking ahead), not from signal correlation (looking at the same data).
  - Status: VERIFIED (abstract and mechanism confirmed via SSRN page; November 2025 release confirmed)

- **Danielsson, Macrae, and Uthemann (2022)** -- *Artificial Intelligence and Systemic Risk*, JBF / **Danielsson and Uthemann (2025)** -- *Artificial Intelligence and Financial Crises*, JFS
  - Mechanism: The 2022 paper qualitatively argues that AI creates procyclicality via model monoculture across multiple channels. The 2025 paper adds a formal global games model for the coordination channel (theta*(mu)), but the other channels (information processing, common data) remain qualitative.
  - Overlap: The Danielsson-Uthemann programme is the closest published competitor to the multi-channel narrative. The 2025 paper now partially formalises one channel.
  - Differentiator: Even combining both papers, only the coordination/run channel is formally modelled, and via mu (AI fraction) not rho (signal correlation). No formal information acquisition model, no formal market-making model, no N_eff, no amplification loop or fixed-point characterisation. The project's core contribution -- the three-channel fixed-point in (rho_eff, theta*, N_eff) -- remains unaddressed by this research programme.
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

- **Hansen and Lee (2025)** -- *Financial Stability Implications of Generative AI: Taming the Animal Spirits*, Fed FEDS WP 2025-090 (September 2025; arXiv 2510.01451)
  - Mechanism: Laboratory-style experiments using LLMs to replicate classic herding studies (information cascades in sequential investment decisions). Finds that AI agents make more rational decisions than humans, relying predominantly on private information over market trends. AI can be induced to herd optimally when explicitly guided to maximise profits. Overall, increased reliance on AI-powered advice could reduce animal-spirits-driven bubbles.
  - Overlap: Directly studies AI agents in financial coordination/herding settings. The finding that AI reduces herding is a potential counterargument to Channel 1.
  - Differentiator: Experimental/simulation approach; does not build a formal equilibrium model. Crucially, each AI agent in the experiment receives independent prompts and processes information independently -- the experiment does not test the case where all agents share the same underlying model output (rho near 1). The "reduced herding" finding applies to independently queried AI agents, not to agents receiving the correlated signal epsilon_i = sqrt(rho)*eta + sqrt(1-rho)*xi_i with high rho. The paper does not distinguish between "diverse AI" (low rho, many independent models) and "homogeneous AI" (high rho, same model/data). The project's Channel 1 mechanism specifically concerns the high-rho case that Hansen-Lee do not test.
  - Counterargument assessment: The Hansen-Lee finding is not a direct refutation of Channel 1 but is a relevant boundary condition. The research plan should acknowledge that at low rho (diverse AI agents), AI may indeed reduce herding, and the fragility mechanism activates only at high rho. This actually strengthens the non-monotonicity argument: low rho is stabilising, high rho is destabilising.
  - Status: VERIFIED (abstract, mechanism, and scope confirmed via Federal Reserve page and arXiv)

### LOW threat / Foundational

- **Gu, Kelly, and Xiu (2020)** -- *Empirical Asset Pricing via Machine Learning*, RFS
  - Mechanism: Documents that diverse ML methods converge on the same dominant predictors (momentum, liquidity, volatility).
  - Overlap: Empirical foundation for rho -> 1 claim. Demonstrates convergence of ML outputs.
  - Differentiator: Empirical asset pricing paper -- no theoretical model of consequences. Used as empirical motivation.
  - Status: VERIFIED

---

## Aggregate Novelty Assessment

### Overall threat level: MODERATE-HIGH (upgraded from MODERATE)

The threat level has been raised from MODERATE to MODERATE-HIGH due to the identification of Danielsson and Uthemann (2025, JFS), which provides a formal game-theoretic model of AI-driven coordination failure -- making it a second HIGH threat for Channel 1 alongside Yang (2024). However, neither paper uses signal correlation (rho) as the primitive, and neither connects to Channels 2 or 3. The core amplification loop contribution remains unthreatened.

### Channel-level summary
| Channel | HIGH threats | Strongest differentiator |
|---------|-------------|------------------------|
| 1 -- Coordination | 2 (Yang 2024; Danielsson-Uthemann 2025) | Both use non-rho mechanisms (RL behavioural convergence; AI speed/execution probability). Neither derives theta*(rho) as a function of signal correlation or characterises the uniqueness/multiplicity boundary driven by AI signal homogeneity |
| 2 -- Information  | 1 (Dugast-Foucault 2018) | DF model speed-precision tradeoff over time, not cross-sectional signal correlation destroying information diversity |
| 3 -- Market Making | 0 | No paper models N_eff(rho) for AI-driven correlated market-maker withdrawal. Colliard-Foucault-Lovo (2025) models RL market-making but single-agent, no correlation |
| Amplification Loop | 0 | No paper models the three-channel fixed-point in (rho_eff, theta*, N_eff) |

### Core contribution status
The amplification loop -- the fixed-point in (rho_eff, theta*, N_eff) across the three channels -- is NOT directly threatened by any identified paper. No existing work connects coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a single parameterisation of signal homogeneity.

Channel 1 now faces two HIGH threats, but both operate through fundamentally different mechanisms from the project's information-theoretic approach. Yang (2024) uses RL behavioural convergence. Danielsson-Uthemann (2025) uses AI execution speed advantage (mu parameterisation). Neither derives the crisis threshold as a function of signal correlation rho, and neither characterises how the Hellwig (2002) multiplicity result is activated by AI model homogeneity. The project's Channel 1 contribution (analytical theta*(rho) in a Goldstein-Pauzner bank-run framework) remains differentiated at the mechanism level.

The Grossman-Stiglitz extension with cross-sectional signal correlation (Channel 2), the N_eff(rho) liquidity fragility index (Channel 3), and the three-channel amplification loop (Contribution 4) have no competitors. These remain the strongest novelty claims.

### Key risks for the Research Director
- **Channel 1 is now the most contested space.** Two formal papers (Yang 2024; Danielsson-Uthemann 2025) model AI-driven coordination failure. The research plan must clearly differentiate on three dimensions: (a) rho vs. mu/RL as the primitive, (b) analytical characterisation of the uniqueness/multiplicity boundary vs. computational/formula-based threshold, (c) connection to Channels 2 and 3. Consider framing Channel 1 as extending and formalising the information-theoretic mechanism that Danielsson-Uthemann (2025) discuss qualitatively but do not model.
- **Danielsson-Uthemann (2025) must be cited prominently.** The research plan currently references only the 2022 JBF paper. The 2025 JFS paper is a published, peer-reviewed formal model that occupies adjacent space. The introduction must engage it directly.
- **Dugast and Foucault (2018, 2025) remain the primary threats to Channel 2.** No change from v1.
- **Hansen-Lee (2025) is not a refutation of Channel 1** but provides a useful boundary condition: at low rho (diverse AI), AI may reduce herding. The plan should incorporate this as evidence for the non-monotonicity claim.
- **The Dou-Goldstein-Ji research program is confirmed as RL/collusion-based, not information-theoretic.** The rho-based approach is complementary, not competing.
- **Colliard-Foucault-Lovo (2025, RFS)** introduces formal AI market-making models. While the mechanism differs (single-agent RL pricing, not correlated withdrawal), the paper demonstrates active interest in AI market-making from top researchers. The Channel 3 model should cite this paper.

### Papers requiring deeper investigation
- **Szkup and Trevino (2015)** -- *Information Acquisition in Global Games of Regime Change*: Their sufficient conditions for uniqueness may be violated when signals are correlated through a common AI source. The Theory Builder must assess this in Phase 1 -- if Szkup-Trevino's uniqueness conditions break down at high rho, this strengthens the Channel 1 result but requires careful handling to avoid contradicting their equilibrium characterisation. [VERIFIED -- mechanism confirmed, but interaction with rho not yet assessed by Theory Builder]
- **Cespa and Vives (forthcoming)** -- *Market Opacity and Fragility*: Their strategic complementarity in liquidity demand operates through opacity, not algorithmic similarity. The mechanism is conceptually distinct from Channel 3's rho-driven correlated withdrawal. Not a direct threat but should be cited as a parallel fragility mechanism. [VERIFIED -- mechanism confirmed as opacity-driven, not AI-driven]

---

## Changelog

### Iteration 0 -- 2026-03-10 (Mode 1: Quick Scan)
Initial threat map produced. 30 papers assessed. Five papers flagged for deeper investigation.

### Iteration 1 -- 2026-03-10 (Mode 2: Targeted Check)
**Plan changes checked:**
- Verified all five novelty claims in the initial research plan (Contributions 1-5)
- Investigated all seven open questions flagged in the plan
- Resolved all five "partially assessed" / UNVERIFIED papers from the Mode 1 scan
- Searched for papers combining all three channels through rho or equivalent signal correlation parameterisation
- Searched for N_eff or effective-number-of-providers concepts in AI market-making literature
- Searched for Grossman-Stiglitz extensions with cross-sectional AI signal correlation
- Searched for prisoner's dilemma / competitive AI adoption models in finance
- Searched for bifurcation / phase transition characterisations in AI-driven financial fragility

**New papers added:**
- Danielsson and Uthemann (2025, JFS) -> Channel 1 -> HIGH. This is a newly identified formal game-theoretic model (global games with AI agents) that derives theta*(mu). Major finding for the threat assessment.
- Colliard, Foucault, and Lovo (2025, RFS) -> Channel 3 -> MODERATE. Q-learning algorithmic market makers in Glosten-Milgrom framework.

**Reclassifications:**
- None reclassified in threat level, but multiple status upgrades from UNVERIFIED to VERIFIED.

**Status upgrades:**
- Yang (2024): UNVERIFIED-partial -> VERIFIED. Full paper read (102 pages). Confirmed as purely RL-based Q-learning in Morris-Shin framework. No rho parameter, no analytical theta*(rho), no information acquisition or market-making channels.
- Dou-Goldstein-Ji (2025b): UNVERIFIED -> VERIFIED. Mechanism confirmed as RL-based intertemporal collusion by oligopolistic AI planners. No information-theoretic channel, no rho.
- Hansen-Lee (2025): UNVERIFIED -> VERIFIED. Confirmed as experimental study with independently queried LLMs. Does not test the high-rho case (same model/signal). Not a direct refutation of Channel 1.
- Cespa-Vives (forthcoming): UNVERIFIED -> VERIFIED. Mechanism confirmed as opacity-driven, not AI-driven. Distinct from Channel 3.

**No-change confirmation:**
- No paper found combining all three channels (coordination failure, information acquisition, correlated liquidity withdrawal) through a signal correlation parameterisation. Contribution 4 (amplification loop) remains unthreatened.
- No paper found deriving N_eff(rho) for correlated AI market makers. Contribution 3 remains unthreatened.
- No paper found extending Grossman-Stiglitz with cross-sectional AI signal correlation destroying information diversity. Contribution 2 remains unthreatened.
- No paper found modelling endogenous rho via a prisoner's dilemma in AI adoption in financial markets. Contribution 5 remains unthreatened.
- No paper found deriving the bifurcation threshold of a multi-channel AI fragility system. The phase transition characterisation is novel.

**Assessment change:** Yes. Overall threat level upgraded from MODERATE to MODERATE-HIGH due to the addition of Danielsson-Uthemann (2025) as a second HIGH threat for Channel 1. However, the core contribution (amplification loop, Contribution 4) and the strongest individual channel contributions (Contributions 2, 3) remain unthreatened. The increased threat to Channel 1 means the research plan must now differentiate from two formal models (Yang 2024; Danielsson-Uthemann 2025), both of which use non-rho mechanisms. The rho-based information-theoretic approach to Channel 1 remains distinct but must be articulated more carefully.

**Total papers assessed:** 32 (30 from Mode 1 + 2 new)

### Iteration 2 -- 2026-03-10 (Mode 2: Targeted Check)
**Plan changes checked:**
- Verified the Danielsson-Uthemann (2025, JFS) three-part differentiator added to Channel 1 and Contribution 4. Read the full paper (arXiv HTML) and confirmed: (a) theta*(mu) = (c/b)[(1-mu)p + mu] is the exact formula in equation (4); (b) the Hellwig (2002) multiplicity result is discussed qualitatively in Section 2.2.2 but not integrated into the formal equilibrium; (c) only the coordination/run channel is formally modelled; no information acquisition, market-making, N_eff, or amplification loop; (d) no rho parameter for signal correlation; (e) no formal propositions or theorems stated, only comparative statics.
- Verified the fixed-point specification in (rho_eff, theta*, N_eff) with three mappings (g_1, g_2, g_3), composite operator T, and Brouwer existence argument. Searched for competing multi-channel fixed-point models in financial fragility literature. No paper found.
- Verified the Colliard-Foucault-Lovo (2025, RFS) differentiator. Confirmed as single-agent Q-learning in Glosten-Milgrom framework with no cross-sectional correlation, no N_eff, no simultaneous withdrawal mechanism.
- Checked Dou-Goldstein-Ji (2025a, 2025b) and Goldstein-Huang-Yang (2025 survey) for any three-equation fixed-point system or rho-like parameterisation. None found.

**New papers added:**
- None. No new threatening papers identified in this iteration.

**Reclassifications:**
- None. All existing threat levels remain appropriate given the plan revisions.

**No-change confirmation:**
- The Danielsson-Uthemann (2025) three-part differentiator is verified as accurate and defensible against the full paper text. The plan correctly characterises what this paper does and does not do.
- The fixed-point specification in (rho_eff, theta*, N_eff) is confirmed novel. No paper in the threat map or broader literature search models a three-channel fixed-point linking coordination failure, information acquisition, and market liquidity through signal correlation.
- The Colliard-Foucault-Lovo (2025) differentiator is verified as accurate. Single-agent RL pricing dynamics are clearly distinct from N-market-maker correlated withdrawal.
- The Brouwer fixed-point existence argument on a compact convex subset of R^3 for a multi-channel financial fragility system is confirmed as a novel application. No competing paper uses this approach.
- The bifurcation result (joint rho* < min of individual channel thresholds) has no competitor in the identified literature.

**Assessment change:** No. Overall threat level remains MODERATE-HIGH. The Iteration 2 plan revisions successfully addressed the two binding problems from the Evaluator (Danielsson-Uthemann engagement and fixed-point specification) without introducing new threats. The core contribution (amplification loop, Contribution 4) remains unthreatened. All channel-level threat assessments are unchanged.

**Total papers assessed:** 32 (unchanged from Iteration 1)
