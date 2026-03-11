# Threat Map -- Final

## Metadata
Date: 2026-03-10
Planning loop iterations: 2
Total papers assessed: 38
Searches conducted (this pass): 22
Unresolved entries: none

---

## Channel 1 -- Coordination Failure (Global Games + rho)

### HIGH threat

- **Yang (2024)** -- *AI Coordination and Self-Fulfilling Financial Crises*, Working paper, Swiss Finance Institute / USI Lugano
  - Mechanism: Q-learning agents learn attack thresholds through repeated interaction in a Morris-Shin (1998) speculative attack game. AI speculators coordinate more effectively on the crisis equilibrium than Nash predictions or human subjects. Under low information accuracy, AI agents overestimate others' attack probability, raising crisis likelihood.
  - Overlap: Directly models AI-driven coordination failure in a global games setting. Shows AI participation raises crisis probability, which is the core Channel 1 claim.
  - Differentiator: Mechanism is entirely RL-based (Q-learning behavioural convergence through repeated interaction). No signal correlation parameter rho. The crisis threshold is learned computationally via Q-value convergence, not derived analytically as theta*(rho). No information acquisition model (Channel 2), no market-making model (Channel 3). Computational/experimental approach (1,000 simulation sessions per parametrisation), not a formal equilibrium characterisation.
  - Status: VERIFIED (full paper read; 102 pages; mechanism confirmed as purely RL-based)
  - Engagement strategy: Cite and differentiate. Acknowledge Yang as a computational demonstration of AI-driven coordination failure, then distinguish the project's contribution as an analytical characterisation of the information-theoretic mechanism (correlated signals restoring Hellwig 2002 multiplicity) with the rho parameterisation. Frame the two approaches as complementary: Yang shows the phenomenon computationally; this project characterises it formally through the signal structure.

- **Danielsson and Uthemann (2025)** -- *Artificial Intelligence and Financial Crises*, Journal of Financial Stability, Vol. 80
  - Mechanism: Global games framework (Morris-Shin 1998) with AI agents. Crisis threshold theta*(mu) = (c/b)[(1-mu)p + mu] where mu is the fraction of AI agents and p < 1 is the probability humans successfully execute a run. AI agents always succeed (probability 1), so increasing mu raises theta* and makes crises more likely. Four channels discussed qualitatively (information processing, common data, speed, strategic complementarities) but only the speed channel is formally modelled.
  - Overlap: Formal game-theoretic model of AI-driven coordination failure. Published in a peer-reviewed journal. Derives an analytical crisis threshold as a function of AI penetration.
  - Differentiator: Three-part differentiator. (1) Primitive is mu (AI fraction, extensive margin) not rho (signal correlation, intensive margin). High mu with diverse AI models (low rho) does not trigger our mechanism; low mu with a single dominant model (high rho) does. (2) Does not integrate Hellwig (2002) multiplicity result into the formal model. Discusses it qualitatively (Section 2.2.2) but derives theta*(mu) under standard Morris-Shin uniqueness conditions. This project characterises the uniqueness/multiplicity boundary as a function of signal correlation. (3) Only the coordination/run channel is formally modelled. No information acquisition model, no market-making equilibrium, no N_eff, no amplification loop, no fixed-point.
  - Status: VERIFIED (full HTML version read on arXiv; equation 4 confirmed; no formal propositions or theorems stated)
  - Engagement strategy: Cite and build on. Acknowledge Danielsson-Uthemann as the closest formal predecessor in the AI + global games space. Frame this project as formalising the information-theoretic mechanism (rho) that they identify qualitatively but do not model, and as extending their single-channel model to the three-channel amplification loop.

### MODERATE threat

- **Hellwig (2002)** -- *Public Information, Private Information, and the Multiplicity of Equilibria in Coordination Games*, JET
  - Mechanism: Proves sufficiently precise public information reinstates multiple equilibria in Morris-Shin global games.
  - Overlap: Channel 1 logic (rho -> common signal -> multiplicity) is a direct application of Hellwig's result.
  - Differentiator: Does not model AI, does not endogenise signal precision or correlation through technology adoption, does not connect to Channels 2 or 3.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Hellwig provides the formal foundation; the project applies it to the AI context with rho parameterisation.

- **Angeletos, Hellwig, and Pavan (2006)** -- *Signaling in a Global Game: Coordination and Policy Traps*, AER
  - Mechanism: Endogenous policy signals restore multiplicity in global games even without exogenous public information.
  - Overlap: Demonstrates that information structure endogeneity can undermine uniqueness.
  - Differentiator: Signaling is by a policy-maker, not a common technology. No AI, no rho parameterisation, no connection to information acquisition or market making.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge the endogenous information channel but distinguish the source (policy vs. technology adoption).

- **Szkup and Trevino (2015)** -- *Information Acquisition in Global Games of Regime Change*, JET
  - Mechanism: Endogenises information acquisition in global games coordination. Provides sufficient conditions for uniqueness; shows strategic complementarities in actions do not always translate into complementarities in information acquisition.
  - Overlap: Connects information acquisition to coordination failure equilibrium in global games. Directly relevant to the Channel 1-Channel 2 interaction.
  - Differentiator: Does not model correlated signals from a common source (AI). Signal correlation is not parameterised by rho. Does not study market making (Channel 3) or the amplification loop.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Use Szkup-Trevino as a building block for the Channel 1-2 interaction. Note that their sufficient conditions for uniqueness may be violated when signals are correlated through a common AI source at high rho.

- **Hansen and Lee (2025)** -- *Financial Stability Implications of Generative AI: Taming the Animal Spirits*, Fed FEDS WP 2025-090 (arXiv 2510.01451)
  - Mechanism: Laboratory-style experiments using LLMs to replicate classic herding studies. Finds AI agents make more rational decisions than humans, reducing animal-spirits-driven herding.
  - Overlap: Studies AI agents in financial coordination settings. Finding that AI reduces herding is a potential counterargument to Channel 1.
  - Differentiator: Each AI agent receives independent prompts and processes information independently. Does not test the high-rho case where all agents share the same model output. The "reduced herding" finding applies to independently queried AI agents (low rho), not to agents receiving correlated signals. Not a direct refutation but a boundary condition that actually supports the non-monotonicity argument: at low rho diverse AI may stabilise; fragility activates only at high rho.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge that at low rho diverse AI may reduce herding, which strengthens the non-monotonicity claim. Distinguish the high-rho regime that Hansen-Lee do not test.

### LOW threat / Foundational

- **Morris and Shin (1998, 2002)** -- *Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks* (AER); *Social Value of Public Information* (AER)
  - Mechanism: Global games framework; heterogeneous private signals yield unique threshold equilibrium; public information has disproportionate impact on coordination.
  - Overlap: Foundational for Channel 1.
  - Differentiator: Foundational. Does not model AI, signal homogeneity, or rho.
  - Status: VERIFIED

- **Goldstein and Pauzner (2005)** -- *Demand Deposit Contracts and the Probability of Bank Runs*, JF
  - Mechanism: Global games applied to bank runs in Diamond-Dybvig framework; unique crisis threshold.
  - Overlap: The project embeds rho into this specific framework.
  - Differentiator: Foundational. The project extends this model with rho parameterisation.
  - Status: VERIFIED

- **Angeletos and Pavan (2007)** -- *Efficient Use of Information and Social Value of Information*, Econometrica
  - Mechanism: Characterises welfare implications of public vs. private information in coordination games.
  - Overlap: Welfare analysis of Channel 1 uses this framework.
  - Differentiator: Foundational. Provides the welfare toolkit, not the AI application.
  - Status: VERIFIED

- **Margaretic and Pasten (2014)** -- *Correlated Bank Runs, Interbank Markets and Reserve Requirements*, JBF
  - Mechanism: Extends Goldstein-Pauzner (2005) to account for correlation in the quality of banks' long-term investments when banks are linked through cross deposits.
  - Overlap: Extends the same foundational model with a correlation structure.
  - Differentiator: Correlation is in bank fundamentals (investment quality), not in signals received by agents. The model examines inter-bank contagion through correlated fundamental quality and cross deposits, not homogeneity of private signals driven by AI. No rho parameterisation of signal correlation, no AI, no information acquisition or market-making channels.
  - Status: VERIFIED

---

## Channel 2 -- Information Acquisition (Grossman-Stiglitz + rho)

### HIGH threat

- **Dugast and Foucault (2018)** -- *Data Abundance and Asset Price Informativeness*, JFE
  - Mechanism: Cheap, fast (imprecise) signals crowd out demand for costly precise signals, reducing price informativeness even as data becomes abundant.
  - Overlap: Directly models crowding-out of fundamental information by cheap data signals. Closely parallels Channel 2 where cheap AI signals crowd out costly private research.
  - Differentiator: Models the speed-precision tradeoff of a single data source over time (temporal dimension), not the cross-sectional correlation of signals across agents using the same AI. No rho equivalent as signal correlation; the tradeoff is cost vs. precision. Does not model Grossman-Stiglitz information aggregation with correlated AI outputs destroying diversity. No connection to coordination failure or market making.
  - Status: VERIFIED
  - Engagement strategy: Cite and differentiate. Acknowledge Dugast-Foucault as the closest model of technology-driven information crowding. Distinguish the temporal speed-precision mechanism from the cross-sectional signal correlation mechanism. Frame the project as addressing the complementary dimension that Dugast-Foucault leave unexplored.

- **Dugast and Foucault (2025)** -- *Equilibrium Data Mining and Data Abundance*, JF
  - Mechanism: Speculators search for predictors through trials; computing power and data abundance affect the threshold signal-to-noise ratio. Crowding reduces data mining value.
  - Overlap: Models endogenous information production with technology-driven crowding.
  - Differentiator: Mechanism is about search intensity and data mining thresholds, not cross-sectional signal correlation (rho). No Grossman-Stiglitz information aggregation, no FPE/RPE distinction, no connection to Channels 1 or 3.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge as a complementary analysis of technology-driven information production. Distinguish the search/data mining mechanism from the signal correlation mechanism.

### MODERATE threat

- **Farboodi and Veldkamp (2020)** -- *Long-Run Growth of Financial Data Technology*, AER
  - Mechanism: Models how technological improvement in data processing affects the choice between processing public data and producing private signals. Technology can shift information production toward already-available data.
  - Overlap: Technology-driven shift in information acquisition, conceptually similar to AI driving agents toward common signals.
  - Differentiator: Does not model cross-sectional signal correlation. The mechanism is about the growth of data technology over time, not homogeneity of AI outputs. No price informativeness consequences via Grossman-Stiglitz, no connection to coordination/market-making channels.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge the technology-driven information shift but distinguish the temporal growth mechanism from the cross-sectional correlation mechanism.

- **Farboodi, Matray, Veldkamp, and Venkateswaran (2022)** -- *Where Has All the Data Gone?*, RFS
  - Mechanism: Data abundance concentrates on large firms, leaving small firms informationally impoverished.
  - Overlap: Empirically documents that data technology creates information concentration rather than diffusion.
  - Differentiator: Mechanism is about cross-sectional asset coverage, not cross-agent signal correlation. No formal rho parameterisation, no GS extension, no connection to coordination or market making.
  - Status: VERIFIED
  - Engagement strategy: Cite as empirical support. The concentration of data on large firms is consistent with the rho -> 1 mechanism for covered assets.

- **Goldstein and Yang (2015)** -- *Information Diversity and Complementarities in Trading and Information Acquisition*, JF
  - Mechanism: Diversity of information dimensions creates strategic complementarities in information acquisition. When one dimension is publicly known, traders invest more in other dimensions.
  - Overlap: Channel 2 uses the Goldstein-Yang information diversity mechanism. When AI homogenises one dimension, complementarities break down.
  - Differentiator: Foundational for Channel 2. Does not model AI or signal correlation driven by a common technology. Establishes the complementarity result that the project applies.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Use Goldstein-Yang as a building block for the Channel 2 mechanism. Show that AI homogenisation breaks down their complementarity structure.

- **Banerjee, Davis, and Gondhi (2018)** -- *When Transparency Improves, Must Prices Reflect Fundamentals Better?*, RFS
  - Mechanism: Increasing transparency (cheaper fundamental information) can decrease price informativeness because investors shift toward learning about others' beliefs.
  - Overlap: Cheaper information paradoxically reducing informativeness. Related to Channel 2's AI-driven information paradox.
  - Differentiator: Mechanism is about composition of what investors learn (fundamentals vs. beliefs), not cross-sectional signal correlation from AI. No rho parameterisation, no connection to coordination/market-making.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge the paradox of cheaper information reducing informativeness but distinguish the channel (belief learning vs. signal correlation).

- **Vives (2014)** -- *On the Possibility of Informationally Efficient Markets*, JEEA
  - Mechanism: Establishes conditions for informational efficiency when correlation in traders' valuations is not too large. Shows a privately revealing equilibrium obtains in a competitive framework and incentives to acquire information are preserved when correlation is bounded.
  - Overlap: Directly addresses information aggregation under correlated valuations. Shows that high correlation undermines the Grossman-Stiglitz resolution.
  - Differentiator: Models correlation in valuations, not in AI-generated signals. Does not study the specific mechanism where AI model homogeneity drives correlation. Does not connect to coordination failure or market making. Provides a foundational result that the project can build on: as AI drives rho -> 1, Vives's conditions for efficiency are violated.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Use Vives's result as theoretical support: when AI drives signal correlation high enough, the conditions for informationally efficient markets fail.

- **Barucca and Morone (2025)** -- *How Low-Cost AI Universal Approximators Reshape Market Efficiency*, arXiv 2501.07489
  - Mechanism: Discusses how AI as universal approximators pushes markets toward a generalized notion of efficiency. Argues that cheap AI enables increasingly sophisticated strategies, potentially making markets harder for inefficient traders.
  - Overlap: Discusses AI and market efficiency in the context of Grossman-Stiglitz. Relevant to the broad Channel 2 theme.
  - Differentiator: Conceptual/review paper, not a formal GS extension. No rho parameterisation, no correlated signal structure, no formal model of information acquisition with cross-sectional correlation. Does not derive price informativeness results. Does not connect to coordination or market making.
  - Status: VERIFIED
  - Engagement strategy: Cite as context. Reference as part of the emerging literature on AI and market efficiency, but note the absence of formal modelling of the signal correlation mechanism.

### LOW threat / Foundational

- **Grossman and Stiglitz (1980)** -- *On the Impossibility of Informationally Efficient Markets*, AER
  - Mechanism: Informational paradox: costly information acquisition is incompatible with full price efficiency.
  - Overlap: Foundational for Channel 2.
  - Differentiator: Foundational. The project extends GS with correlated AI signals (rho).
  - Status: VERIFIED

- **Holden and Subrahmanyam (1992)** -- *Long-Lived Private Information and Imperfect Competition*, JF
  - Mechanism: Competition among identically informed traders leads to aggressive trading and rapid information revelation.
  - Overlap: Used in Channel 2 to show correlated AI information (rho -> 1) yields zero rents.
  - Differentiator: Foundational. Provides the competition mechanism applied to correlated AI signals.
  - Status: VERIFIED

- **Bond, Edmans, and Goldstein (2012)** -- *The Real Effects of Financial Markets*, ARFE
  - Mechanism: Distinguishes FPE from RPE; establishes the real-effects feedback channel.
  - Overlap: Welfare analysis of Channel 2 uses FPE/RPE distinction.
  - Differentiator: Foundational. Provides the welfare framework.
  - Status: VERIFIED

---

## Channel 3 -- Market Making (Correlated Liquidity Withdrawal)

### HIGH threat

None identified. No paper formally models correlated AI-driven market-maker withdrawal with an N_eff(rho) index or rho** threshold.

### MODERATE threat

- **Colliard, Foucault, and Lovo (2025)** -- *Algorithmic Pricing and Liquidity in Securities Markets*, forthcoming RFS
  - Mechanism: Q-learning algorithmic market makers in Glosten-Milgrom (1985) adverse selection framework. Q-learning market makers charge markups that increase when adverse selection costs decrease, contrary to Nash predictions.
  - Overlap: Formally models AI-driven market making with learning algorithms. Directly relevant to Channel 3's domain.
  - Differentiator: Mechanism is about RL-based pricing by individual market makers learning in a strategic environment. No cross-sectional correlation among multiple market makers, no rho parameterisation, no N_eff formula, no simultaneous withdrawal mechanism. Focus is single market maker's learning dynamics, not correlated behaviour of N market makers sharing the same AI model.
  - Status: VERIFIED
  - Engagement strategy: Cite and differentiate. Acknowledge Colliard-Foucault-Lovo as modelling how AI changes individual market-maker pricing. Distinguish the project's contribution as characterising how AI homogeneity destroys the diversification benefit of having multiple market makers (the N_eff mechanism).

- **Cespa and Vives (forthcoming)** -- *Market Opacity and Fragility: Why Liquidity Evaporates When It Is Most Needed*, conditionally accepted AER
  - Mechanism: Market opacity creates strategic complementarity in liquidity demand, yielding multiple equilibria where liquidity evaporates suddenly.
  - Overlap: Models endogenous liquidity fragility via strategic complementarity. Related to Channel 3's correlated withdrawal.
  - Differentiator: Fragility operates through opacity and hedger behaviour, not correlated AI signals among market makers. No rho parameterisation, no N_eff formula, no AI model homogeneity. Complementarity arises from information structure, not algorithmic similarity.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge as a parallel fragility mechanism (opacity-driven vs. AI-correlation-driven). Note that the two mechanisms could compound in practice.

- **Greenwood and Thesmar (2011)** -- *Stock Price Fragility*, JFE
  - Mechanism: Stock fragility as covariance of holders' demand shocks. High fragility implies correlated selling and price instability.
  - Overlap: N_eff(rho) is constructed as an analogue of Greenwood-Thesmar fragility applied to algorithmic market makers.
  - Differentiator: Measures correlation of demand shocks from mutual fund flows, not AI-driven market-making decisions. No formal market-maker equilibrium model with algorithmic homogeneity.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Frame N_eff(rho) as extending the Greenwood-Thesmar fragility concept from demand-side correlation to supply-side (market-maker) algorithmic correlation.

- **Danielsson, Macrae, and Uthemann (2022)** -- *Artificial Intelligence and Systemic Risk*, JBF
  - Mechanism: Qualitatively argues AI homogenises risk perceptions and increases procyclicality. AI settles on homogeneous risk management; similar perceptions lead to similar actions; lower volatility but fatter tails.
  - Overlap: Makes the same broad argument as this project: AI homogeneity -> correlated actions -> systemic risk. Discusses procyclicality and model monoculture.
  - Differentiator: Entirely qualitative/narrative. No formal model, no equilibrium analysis, no rho parameterisation, no channel decomposition. Does not model coordination games, information acquisition, or market-making equilibrium. The project formalises these qualitative insights.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Frame the project as providing the formal equilibrium characterisation of the multi-channel mechanism that Danielsson-Macrae-Uthemann describe qualitatively.

- **Danielsson, Shin, and Zigrand (2012)** -- *Endogenous and Systemic Risk*, NBER chapter
  - Mechanism: Common VaR constraints produce endogenous risk: correlated risk management leads to procyclical selling and amplified price impact.
  - Overlap: Common VaR constraints are a special case of Channel 3 (correlated risk limits -> simultaneous withdrawal).
  - Differentiator: Homogeneity arises from regulatory constraints (VaR), not AI model outputs. The project nests this as a limiting case but adds AI-specific rho parameterisation and connects to Channels 1 and 2.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Acknowledge as a precursor. Frame Channel 3 as generalising the Danielsson-Shin-Zigrand common-constraint mechanism to AI-driven signal correlation, with N_eff(rho) as the formal index.

### LOW threat / Foundational

- **Glosten and Milgrom (1985)** -- *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*, JFE
  - Mechanism: Market makers widen spreads in response to adverse selection.
  - Overlap: Foundational for Channel 3.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Kyle (1985)** -- *Continuous Auctions and Insider Trading*, Econometrica
  - Mechanism: Linear equilibrium in a market with informed trading and noise traders.
  - Overlap: Foundational for Channel 3.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Avellaneda and Stoikov (2008)** -- *High-Frequency Trading in a Limit Order Book*, QF
  - Mechanism: Optimal market-making via stochastic control; reservation price formula.
  - Overlap: Channel 3 uses this framework to show shared calibration produces identical spread-widening functions.
  - Differentiator: Foundational. Provides the market-making framework.
  - Status: VERIFIED

- **Pagano (1989)** -- *Trading Volume and Asset Liquidity*, QJE
  - Mechanism: Multiple equilibria in market participation; low-liquidity traps.
  - Overlap: Channel 3 threshold rho** is analogous to Pagano's low-liquidity trap.
  - Differentiator: Foundational.
  - Status: VERIFIED

- **Brunnermeier and Pedersen (2009)** -- *Market Liquidity and Funding Liquidity*, RFS
  - Mechanism: Margin spirals create feedback between market liquidity and funding liquidity.
  - Overlap: Channel 3 connects to margin spiral mechanics.
  - Differentiator: Foundational. Provides the liquidity spiral framework, not the AI correlation mechanism.
  - Status: VERIFIED

---

## Amplification Loop (Fixed-Point Interaction)

### HIGH threat

None identified. No paper models the joint fixed-point interaction of coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a common rho parameter. No paper applies Brouwer's fixed-point theorem to a multi-channel financial fragility system. No paper derives a compound fragility threshold strictly below individual channel thresholds.

### MODERATE threat

- **Dou, Goldstein, and Ji (2025a)** -- *AI-Powered Trading, Algorithmic Collusion, and Price Efficiency*, NBER WP 34054
  - Mechanism: RL-powered trading algorithms autonomously sustain collusive supra-competitive profits. Homogenisation of strategies and self-confirming equilibrium. AI collusion undermines competition, market efficiency, and liquidity.
  - Overlap: Models AI agents producing correlated trading behaviour harming price efficiency and liquidity. Touches Channels 2 and 3 simultaneously.
  - Differentiator: Mechanism is algorithmic collusion via reinforcement learning (emergent coordination through repeated interaction), not signal homogeneity through a common information source. No rho parameterisation, no global games coordination failure (Channel 1), no fixed-point across three channels. Collusion is a behavioural outcome of RL, not an information-theoretic result.
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Acknowledge Dou-Goldstein-Ji as modelling a complementary mechanism (RL-based algorithmic collusion) that operates alongside the signal correlation mechanism. Frame the two as addressing different sources of AI-driven fragility: this project addresses signal homogeneity; DGJ address strategic learning.

- **Dou, Goldstein, and Ji (2025b)** -- *Financial Market Fragility in the Era of AI Planning*, SSRN WP 5763222 (November 2025)
  - Mechanism: AI speculators with planning capability (agentic AI) learn intertemporal collusive strategies, creating and exploiting negative bubbles. Dynamic trading with positive-feedback investors, constrained arbitrageurs, and oligopolistic informed speculators.
  - Overlap: Models AI-driven market fragility. Addresses feedback effects and coordinated destabilisation.
  - Differentiator: Mechanism is intertemporal collusion via planning-capable RL agents, not signal homogeneity or rho parameterisation. No global games (Channel 1), no Grossman-Stiglitz (Channel 2), no N_eff (Channel 3). AI agents are strategic oligopolists, not price-takers with correlated signals. Fragility arises from AI planning capability (looking ahead), not from signal correlation (looking at the same data).
  - Status: VERIFIED
  - Engagement strategy: Cite and distinguish. Frame as addressing a distinct AI fragility mechanism (planning/lookahead vs. signal homogeneity). Note that the two mechanisms could interact in practice but are formally independent.

- **Danielsson and Uthemann (2025)** / **Danielsson, Macrae, and Uthemann (2022)** -- combined assessment for amplification
  - Mechanism: The 2022 paper qualitatively argues multi-channel AI-driven procyclicality. The 2025 paper adds formal coordination/run model but other channels remain qualitative.
  - Overlap: The Danielsson-Uthemann programme is the closest published competitor to the multi-channel narrative.
  - Differentiator: Even combining both papers, only the coordination/run channel is formally modelled, via mu not rho. No formal information acquisition model, no formal market-making model, no N_eff, no amplification loop, no fixed-point characterisation. The project's core contribution (three-channel fixed-point in (rho_eff, theta*, N_eff)) remains unaddressed by this programme.
  - Status: VERIFIED
  - Engagement strategy: Cite and build on. Frame the project as delivering the formal multi-channel analysis that the Danielsson-Uthemann programme motivates qualitatively.

### LOW threat / Foundational

- **Goldstein, Huang, and Yang (2025)** -- *Fragility of Financial Markets*, Annual Review of Financial Economics
  - Mechanism: Survey of forces generating market fragility: learning from prices, strategic complementarities, amplification channels. Provides a canonical trading framework.
  - Overlap: Survey covering theoretical foundations of market fragility. The project's amplification loop is a specific instance of multi-channel fragility.
  - Differentiator: Survey paper. Organises existing knowledge but does not model AI-specific mechanisms or the rho-driven fixed-point.
  - Status: VERIFIED

---

## AI and Financial Markets (Empirical / Applied)

### HIGH threat

None identified.

### MODERATE threat

- **Kim, Muhn, and Nikolaev (2024)** -- *From Transcripts to Insights: Uncovering Corporate Risks Using Generative AI*, arXiv
  - Mechanism: Empirically demonstrates GPT-4 at temperature=0 produces near-identical financial statement analyses, documenting belief homogenisation.
  - Overlap: Direct empirical evidence for rho -> 1 claim.
  - Differentiator: Purely empirical. Documents the phenomenon but does not build a formal model of its consequences.
  - Status: VERIFIED
  - Engagement strategy: Cite as empirical motivation. Use as primary evidence for the rho -> 1 assumption.

- **Calvano, Calzolari, Denicolo, and Pastorello (2020)** -- *Artificial Intelligence, Algorithmic Pricing, and Collusion*, AER
  - Mechanism: Q-learning algorithms learn to sustain supra-competitive prices in oligopoly without communication.
  - Overlap: Demonstrates AI agents coordinate without explicit communication. Foundational for the argument that AI creates correlated behaviour.
  - Differentiator: Product pricing context, not financial markets. No information acquisition, no market making, no signal correlation mechanism. Coordination through repeated RL interaction, not common signals.
  - Status: VERIFIED
  - Engagement strategy: Cite as context. Reference as demonstrating AI coordination in economic settings. Distinguish the financial markets application with signal correlation.

### LOW threat / Foundational

- **Gu, Kelly, and Xiu (2020)** -- *Empirical Asset Pricing via Machine Learning*, RFS
  - Mechanism: Diverse ML methods converge on same dominant predictors (momentum, liquidity, volatility).
  - Overlap: Empirical foundation for rho -> 1.
  - Differentiator: Empirical asset pricing paper. No theoretical model of consequences.
  - Status: VERIFIED

---

## Extensions (Endogenous rho / Diversity Mandate)

### HIGH threat

None identified.

### MODERATE threat

None identified at HIGH or MODERATE threat level for the specific endogenous rho / prisoner's dilemma / diversity mandate contribution.

### LOW threat / Contextual

- **Gans (2023)** -- *Artificial Intelligence Adoption in a Competitive Market*, Economica
  - Mechanism: Models AI adoption as a complement to variable inputs. Shows externalities in AI adoption: adoption can reduce profits of non-adoptees. AI does not operate as a standard process innovation.
  - Overlap: Models competitive AI adoption with externalities. Relevant to the endogenous rho extension.
  - Differentiator: Set in a product market context with demand prediction, not financial markets. The externality is on firm profits through competitive dynamics, not on signal diversity or financial fragility. No signal correlation mechanism, no coordination games, no information acquisition or market making.
  - Status: VERIFIED

- **Kleinberg and Raghavan (2021)** -- *Algorithmic Monoculture and Social Welfare*, PNAS
  - Mechanism: When multiple decision-makers use the same algorithm, decision quality can decrease even under normal operations. Monoculture reduces aggregate accuracy relative to polyculture.
  - Overlap: Formalises the cost of algorithmic monoculture. Conceptually related to the diversity mandate.
  - Differentiator: Set in a general decision-making context (hiring, admissions), not financial markets. No signal correlation mechanism, no financial fragility channels, no equilibrium model of financial market participants.
  - Status: VERIFIED

- **Peng, Kleinberg, Raghavan, and Lipton (2024)** -- *Monoculture in Matching Markets*, NeurIPS 2024
  - Mechanism: Extends Kleinberg-Raghavan to two-sided matching markets. Shows polyculture outperforms monoculture in firm welfare even when idiosyncratic processes are noisier than the shared algorithm.
  - Overlap: Formalises monoculture costs in a market setting with strategic interaction.
  - Differentiator: Matching market context, not financial markets. No financial fragility channels, no signal correlation in the sense of AI-generated trading signals.
  - Status: VERIFIED

- **Danielsson, Macrae, and Uthemann (2022)** -- see Channel 3 / Amplification Loop entries above. Their qualitative discussion of AI monoculture driving systemic risk is the closest published articulation of the diversity mandate motivation, but it is entirely informal.

---

## Aggregate Novelty Assessment

### Overall threat level: MODERATE-HIGH

The overall threat level is MODERATE-HIGH, driven by the two HIGH threats in Channel 1 (Yang 2024; Danielsson-Uthemann 2025). However, both HIGH threats operate through mechanisms fundamentally distinct from the project's information-theoretic rho parameterisation. No HIGH threats exist for Channels 2, 3, the amplification loop, or the extensions. The centrepiece contribution (three-channel fixed-point) has no direct competitor at any threat level.

### Channel-level summary
| Channel | HIGH | MODERATE | Strongest differentiator |
|---------|------|----------|------------------------|
| 1 -- Coordination | 2 | 4 | Both HIGH threats use non-rho mechanisms (RL convergence; AI speed). Neither derives theta*(rho) from signal correlation or characterises the uniqueness/multiplicity boundary. |
| 2 -- Information  | 2 | 5 | Dugast-Foucault model temporal speed-precision tradeoff, not cross-sectional signal correlation destroying information diversity via GS. |
| 3 -- Market Making | 0 | 5 | No paper models N_eff(rho) for AI-driven correlated market-maker withdrawal. |
| Amplification Loop | 0 | 3 | No paper models three-channel fixed-point in (rho_eff, theta*, N_eff) or derives compound threshold below individual thresholds. |
| Extensions | 0 | 0 | No paper models endogenous rho via prisoner's dilemma in AI adoption in financial markets with diversity mandate. |

### Core contribution status
The amplification loop, characterised as a fixed-point in (rho_eff, theta*, N_eff) with Brouwer existence and the bifurcation result rho* < min(rho_1*, rho_2*, rho_3*), is NOT directly threatened by any identified paper. No existing work connects coordination failure, information acquisition collapse, and correlated liquidity withdrawal through a single parameterisation of signal homogeneity. The closest competitors are the Danielsson-Uthemann research programme (which formalises only one channel via a different primitive) and the Dou-Goldstein-Ji programme (which uses RL-based collusion mechanisms rather than information-theoretic signal correlation). Neither programme attempts a multi-channel fixed-point or derives a compound fragility threshold.

### Novelty verdict

1. **Contribution 1 (theta*(rho) characterisation): NOVEL WITH CAVEAT.** The analytical derivation of theta*(rho) from signal correlation in a Goldstein-Pauzner framework is novel. The caveat is that Channel 1 is the most contested space (two HIGH threats) and the Theory Builder must demonstrate that the rho parameterisation produces qualitatively distinct dynamics from Danielsson-Uthemann's theta*(mu), specifically the uniqueness/multiplicity boundary transition.

2. **Contribution 2 (Cross-sectional GS extension with RPE collapse): NOVEL.** No paper extends Grossman-Stiglitz with cross-sectional AI signal correlation (rho) to derive information diversity collapse and RPE non-monotonicity. Dugast-Foucault operate in the temporal dimension. Verified through 22 systematic searches.

3. **Contribution 3 (N_eff(rho) liquidity fragility index): NOVEL.** No paper derives an effective-number-of-independent-providers formula for correlated algorithmic market makers or a no-equilibrium threshold driven by AI signal correlation. Verified through 22 systematic searches.

4. **Contribution 4 (Fixed-point amplification with bifurcation): NOVEL.** No paper models a multi-channel fixed-point linking coordination, information, and liquidity through signal correlation, derives a compound fragility threshold below individual thresholds, or applies Brouwer's theorem to a multi-channel financial fragility system. This is the paper's centrepiece and its strongest novelty claim.

5. **Contribution 5 (Endogenous rho via prisoner's dilemma): NOVEL.** No paper models competitive AI adoption as a prisoner's dilemma driving signal correlation above a fragility threshold in financial markets. Related work on algorithmic monoculture (Kleinberg-Raghavan 2021; Peng et al. 2024) and AI adoption externalities (Gans 2023) exists in non-financial contexts but does not address financial fragility channels.

### Unresolved items
None. All papers identified in prior threat map versions and in the current deep review have been assessed and classified. No papers remain at UNVERIFIED or UNRESOLVED status.
