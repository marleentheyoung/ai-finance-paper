# Literature Notes

Structured summaries of all papers in the final threat map, grouped by channel.

---

## Channel 1 -- Coordination Failure

### Yang (2024) -- *AI Coordination and Self-Fulfilling Financial Crises*

**Journal:** Working paper, Swiss Finance Institute / USI Lugano
**Core question:** Do AI agents coordinate more effectively on crisis equilibria in global games than human agents or Nash equilibrium predictions?
**Model structure:** Morris-Shin (1998) speculative attack game with two Q-learning agents. Standard private signals with exogenous precision. Agents learn attack thresholds through repeated interaction over 1,000 simulation sessions per parametrisation. No analytical equilibrium derivation.
**Key mechanism:** Q-learning agents converge on crisis equilibria more effectively than Nash predictions because they overestimate opponents' attack probability under low information accuracy. This is a behavioural convergence mechanism through repeated interaction, not an information-theoretic mechanism through signal structure.
**Key result:** AI speculators coordinate on higher attack thresholds than Nash equilibrium predicts, raising the probability of self-fulfilling crises. Under public information, AI speculators coordinate on higher thresholds but with higher variance.
**Relation to this project:** Directly relevant to Channel 1 as it demonstrates AI-driven coordination failure in global games. However, the mechanism (RL behavioural convergence) is fundamentally different from the project's mechanism (correlated signals restoring Hellwig multiplicity). The two approaches are complementary.
**Threat level:** HIGH

### Danielsson and Uthemann (2025) -- *Artificial Intelligence and Financial Crises*

**Journal:** Journal of Financial Stability, Vol. 80
**Core question:** How does AI adoption amplify financial vulnerabilities through coordination failure?
**Model structure:** Global games (Morris-Shin 1998) with two agent types: AI agents (fraction mu) who always successfully execute a run (probability 1), and human agents (fraction 1-mu) who succeed with probability p < 1. Standard Morris-Shin private signals with exogenous precision. No signal correlation parameter.
**Key mechanism:** AI agents have a speed/execution advantage: they always succeed at running while humans may fail. This makes the coordination game easier to sustain, raising the crisis threshold. The mechanism is about the extensive margin (how many agents are AI) not the intensive margin (how correlated are AI outputs).
**Key result:** Crisis threshold theta*(mu) = (c/b)[(1-mu)p + mu] is increasing in mu. No formal propositions or theorems stated; the main results are comparative statics on the threshold formula. Hellwig (2002) multiplicity is discussed qualitatively (Section 2.2.2) but not integrated into the formal model.
**Relation to this project:** The closest formal predecessor in the AI + global games space. The project extends beyond this paper in three dimensions: (1) rho (signal correlation) vs. mu (AI fraction) as primitive, (2) analytical uniqueness/multiplicity boundary, (3) connection to Channels 2 and 3 through amplification loop.
**Threat level:** HIGH

### Hellwig (2002) -- *Public Information, Private Information, and the Multiplicity of Equilibria in Coordination Games*

**Journal:** Journal of Economic Theory
**Core question:** Under what conditions does public information restore multiple equilibria in global games?
**Model structure:** Morris-Shin global game with both private and public signals. Agents observe a public signal and a private signal, each with varying precision.
**Key mechanism:** Sufficiently precise public information allows agents to coordinate on the public signal, restoring the multiplicity of equilibria that private signal heterogeneity had eliminated.
**Key result:** There exists a threshold precision of public information above which the global game admits multiple equilibria. Below this threshold, the standard uniqueness result obtains.
**Relation to this project:** Foundational for Channel 1. The project's core Channel 1 mechanism is that rising rho converts private signals into near-public signals, progressively activating Hellwig's multiplicity result. The contribution is connecting this mechanism to AI model homogeneity and parameterising it through rho.
**Threat level:** MODERATE

### Szkup and Trevino (2015) -- *Information Acquisition in Global Games of Regime Change*

**Journal:** Journal of Economic Theory
**Core question:** What are the implications of endogenous information acquisition for equilibrium in global games of regime change?
**Model structure:** Global game with a preliminary information acquisition stage. Agents choose signal precision before playing the coordination game.
**Key mechanism:** Strategic complementarities in actions do not always translate into complementarities in information acquisition. Provides sufficient conditions for uniqueness when agents can choose how much information to acquire.
**Key result:** Under specific conditions on the cost function and the coordination structure, the game with endogenous information acquisition has a unique equilibrium.
**Relation to this project:** Directly relevant to the Channel 1-Channel 2 interaction. The project should assess whether Szkup-Trevino's sufficient conditions for uniqueness are violated when signals are correlated through a common AI source at high rho.
**Threat level:** MODERATE

### Hansen and Lee (2025) -- *Financial Stability Implications of Generative AI: Taming the Animal Spirits*

**Journal:** Fed FEDS Working Paper 2025-090
**Core question:** Do AI agents herd or make more rational decisions in financial coordination settings?
**Model structure:** Laboratory-style experiments using LLMs replicating classic information cascade studies (sequential investment decisions).
**Key mechanism:** AI agents rely predominantly on private information over market trends, making more rational decisions than humans. AI can be guided to herd optimally.
**Key result:** AI reduces animal-spirits-driven bubbles and herding in the experimental setting.
**Relation to this project:** Each AI agent receives independent prompts and processes information independently (low rho). The "reduced herding" finding applies to diverse AI, not homogeneous AI (high rho). This actually supports the non-monotonicity claim: at low rho, AI stabilises; at high rho, AI destabilises. Useful as a boundary condition.
**Threat level:** MODERATE

### Morris and Shin (1998, 2002) -- *Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks*; *Social Value of Public Information*

**Journal:** American Economic Review (both)
**Core question:** How do private signals affect coordination and the role of public information?
**Model structure:** Coordination game with incomplete information; agents receive noisy private signals about fundamentals.
**Key mechanism:** Heterogeneous private signals produce unique threshold equilibrium, eliminating sunspot multiplicity. Public information has disproportionate impact on coordination.
**Key result:** Unique threshold equilibrium exists when private signal noise is sufficiently small relative to prior uncertainty. Social value of public information can be negative under strategic complementarity.
**Relation to this project:** Foundational for Channel 1. The global games framework upon which the entire Channel 1 model is built.
**Threat level:** LOW / Foundational

### Goldstein and Pauzner (2005) -- *Demand Deposit Contracts and the Probability of Bank Runs*

**Journal:** Journal of Finance
**Core question:** What determines the probability of bank runs when agents have private information?
**Model structure:** Diamond-Dybvig model with global games information structure.
**Key mechanism:** Private signals yield unique threshold equilibrium; crisis occurs when fundamentals fall below the threshold.
**Key result:** Unique crisis threshold determined by contract terms. Higher returns to early withdrawers increase bank run probability.
**Relation to this project:** The specific framework into which rho is embedded. Channel 1 extends this model.
**Threat level:** LOW / Foundational

### Angeletos and Pavan (2007) -- *Efficient Use of Information and Social Value of Information*

**Journal:** Econometrica
**Core question:** What is the welfare cost of public vs. private information in coordination games?
**Model structure:** Coordination game with beauty-contest payoff structure and both public and private signals.
**Key mechanism:** Public information has a disproportionate effect on welfare because it coordinates actions, potentially away from the efficient allocation.
**Key result:** Social value of public information depends on the interaction of coordination motives and strategic complementarity. Conditions under which public information is socially harmful are characterised.
**Relation to this project:** Provides the welfare framework for Channel 1. The social cost of AI-driven signal correlation is evaluated using this framework.
**Threat level:** LOW / Foundational

### Margaretic and Pasten (2014) -- *Correlated Bank Runs, Interbank Markets and Reserve Requirements*

**Journal:** Journal of Banking and Finance
**Core question:** How does correlation in bank investment quality affect bank run equilibria when banks are linked through interbank markets?
**Model structure:** Goldstein-Pauzner (2005) extended with correlated bank fundamentals and interbank cross-deposits.
**Key mechanism:** Correlation in the quality of banks' long-term investments, combined with interbank linkages, can generate correlated bank runs.
**Key result:** Unique Bayesian equilibrium exists; bank run threshold depends on correlation in investment quality and interbank market structure.
**Relation to this project:** Extends the same foundational model (Goldstein-Pauzner) with a correlation structure, but the correlation is in fundamentals (investment quality), not in signals received by agents. Distinct from the rho parameterisation of AI signal correlation.
**Threat level:** LOW / Foundational

### Angeletos, Hellwig, and Pavan (2006) -- *Signaling in a Global Game: Coordination and Policy Traps*

**Journal:** American Economic Review
**Core question:** Can endogenous policy signals restore multiplicity in global games?
**Model structure:** Global game with a policy-maker who can send signals.
**Key mechanism:** Endogenous policy signals restore multiplicity even without exogenous public information.
**Key result:** Policy traps arise when the policy-maker's signal coordinates agents on an undesirable equilibrium.
**Relation to this project:** Demonstrates that endogenous information structure changes can undermine uniqueness. Related to the idea that AI adoption changes the information structure, but the source is a policy-maker, not a common technology.
**Threat level:** MODERATE

---

## Channel 2 -- Information Acquisition

### Dugast and Foucault (2018) -- *Data Abundance and Asset Price Informativeness*

**Journal:** Journal of Financial Economics
**Core question:** How does the abundance of cheap data affect price informativeness?
**Model structure:** Asset pricing model with two signal types differing in speed and precision. Fast signals available early at low cost; slow signals available later at high cost.
**Key mechanism:** Cheap, fast but imprecise signals crowd out demand for costly precise signals. The speed-precision tradeoff reduces price informativeness even as data becomes abundant.
**Key result:** Price informativeness can decrease as data costs fall because the cheap-fast signal crowds out the expensive-precise signal. This is a temporal crowding-out, not cross-sectional correlation.
**Relation to this project:** Closest existing model to Channel 2's crowding-out mechanism. However, operates in the temporal dimension (speed vs. precision over time) rather than the cross-sectional dimension (correlation across agents). Does not model Grossman-Stiglitz information aggregation with correlated AI outputs.
**Threat level:** HIGH

### Dugast and Foucault (2025) -- *Equilibrium Data Mining and Data Abundance*

**Journal:** Journal of Finance
**Core question:** How do computing power and data abundance affect equilibrium data mining and market outcomes?
**Model structure:** Speculators search for predictors through trials; computing power determines the number of trials.
**Key mechanism:** Data abundance and computing power lower the threshold signal-to-noise ratio for inclusion, generating more signals but also more false discoveries. Crowding reduces the value of data mining.
**Key result:** Equilibrium data mining intensity increases with computing power but subject to diminishing returns due to crowding. Market outcomes depend on the balance between genuine signal discovery and overfitting.
**Relation to this project:** Related to Channel 2 through the technology-driven information production mechanism. However, the specific mechanism (search intensity/data mining thresholds) is distinct from cross-sectional signal correlation (rho). No Grossman-Stiglitz framework, no FPE/RPE distinction.
**Threat level:** HIGH

### Farboodi and Veldkamp (2020) -- *Long-Run Growth of Financial Data Technology*

**Journal:** American Economic Review
**Core question:** How does long-run improvement in data processing technology affect information choices?
**Model structure:** Dynamic model where agents choose between processing public data and producing private signals, with technology improving over time.
**Key mechanism:** As data processing technology improves, agents shift toward processing already-available (public) data rather than producing new private signals.
**Key result:** Technology growth can reduce private information production, shifting the composition of information in markets.
**Relation to this project:** Conceptually related to Channel 2's AI-driven shift from private to common signals. However, the mechanism is about temporal technology growth, not cross-sectional signal correlation. No rho parameterisation or Grossman-Stiglitz extension.
**Threat level:** MODERATE

### Farboodi, Matray, Veldkamp, and Venkateswaran (2022) -- *Where Has All the Data Gone?*

**Journal:** Review of Financial Studies
**Core question:** Why does data abundance concentrate on large firms?
**Model structure:** Empirical analysis of data technology adoption across firms of different sizes, with a theoretical model of data concentration.
**Key mechanism:** Large firms generate more data through economic activity. As data processing improves, the data advantage compounds, attracting more analysis to large firms and leaving small firms informationally impoverished.
**Key result:** Data technology adoption is concentrated among large firms. Small firms experience relative information decline.
**Relation to this project:** Empirical evidence that data technology creates information concentration rather than diffusion, consistent with rho -> 1 for covered assets. However, the mechanism is about cross-sectional asset coverage, not cross-agent signal correlation.
**Threat level:** MODERATE

### Goldstein and Yang (2015) -- *Information Diversity and Complementarities in Trading and Information Acquisition*

**Journal:** Journal of Finance
**Core question:** How does information diversity affect trading and information acquisition incentives?
**Model structure:** Multi-asset model where traders can acquire different types of information at different costs.
**Key mechanism:** Diversity of information dimensions creates strategic complementarities in information acquisition. When one dimension is publicly known, traders invest more in other dimensions.
**Key result:** Positive endogenous values for acquiring different signals; information diversity enhances complementarities.
**Relation to this project:** Channel 2 applies the Goldstein-Yang complementarity mechanism. When AI homogenises one information dimension, complementarities break down, reducing incentives to acquire private information on other dimensions.
**Threat level:** MODERATE

### Banerjee, Davis, and Gondhi (2018) -- *When Transparency Improves, Must Prices Reflect Fundamentals Better?*

**Journal:** Review of Financial Studies
**Core question:** Does cheaper fundamental information always improve price informativeness?
**Model structure:** Asset pricing model with two types of learning: fundamentals-based and belief-based.
**Key mechanism:** When transparency increases (fundamental information becomes cheaper), investors shift toward learning about others' beliefs rather than fundamentals, reducing overall informativeness.
**Key result:** Price informativeness can decrease with transparency because of the composition shift in information acquisition.
**Relation to this project:** Demonstrates the paradox of cheaper information reducing informativeness. Related to Channel 2 but through a different channel (belief learning vs. signal correlation).
**Threat level:** MODERATE

### Vives (2014) -- *On the Possibility of Informationally Efficient Markets*

**Journal:** Journal of the European Economic Association
**Core question:** Under what conditions can informationally efficient markets exist?
**Model structure:** Competitive market with asymmetric information and correlated valuations.
**Key mechanism:** A privately revealing equilibrium obtains when correlation in traders' valuations is not too large. Information acquisition incentives are preserved under bounded correlation.
**Key result:** Conditions for resolving the Grossman-Stiglitz paradox require that correlation in valuations not exceed a threshold.
**Relation to this project:** Directly relevant as a foundational result. As AI drives signal correlation (rho) high, Vives's conditions for informational efficiency are violated, supporting Channel 2's claim that high rho destroys information diversity and efficiency.
**Threat level:** MODERATE

### Barucca and Morone (2025) -- *How Low-Cost AI Universal Approximators Reshape Market Efficiency*

**Journal:** arXiv preprint 2501.07489
**Core question:** How do low-cost AI systems, as universal function approximators, affect market efficiency?
**Model structure:** Conceptual framework using generalised market efficiency defined through equilibrium price processes. Not a formal GS extension.
**Key mechanism:** AI as universal approximators enables more sophisticated trading strategies. Markets approach "AI-efficiency" where even AI cannot identify profitable strategies.
**Key result:** Markets may converge toward "asymptotic-AI-efficiency" as AI costs decline.
**Relation to this project:** Discusses AI and market efficiency in the Grossman-Stiglitz context but does not formally model cross-sectional signal correlation, information acquisition incentives, or RPE. Conceptual rather than formal.
**Threat level:** MODERATE

### Grossman and Stiglitz (1980) -- *On the Impossibility of Informationally Efficient Markets*

**Journal:** American Economic Review
**Core question:** Can markets be informationally efficient when information is costly?
**Model structure:** Competitive asset market with costly information acquisition. Fraction of agents choose to become informed.
**Key mechanism:** If prices fully reflect information, no agent pays to acquire it; but without acquisition, prices are uninformative. Equilibrium requires noise and partial revelation.
**Key result:** Informationally efficient markets are impossible with costly information. Equilibrium involves partial information revelation.
**Relation to this project:** Foundational for Channel 2. The project extends GS by introducing correlated AI signals (rho) alongside costly private signals.
**Threat level:** LOW / Foundational

### Holden and Subrahmanyam (1992) -- *Long-Lived Private Information and Imperfect Competition*

**Journal:** Journal of Finance
**Core question:** What happens when multiple traders have the same long-lived private information?
**Model structure:** Kyle-type model with multiple identically informed traders and long-lived information.
**Key mechanism:** Competition among identically informed traders leads to aggressive trading, rapid information revelation, and zero rents.
**Key result:** With N identically informed traders, information is revealed in the first period. Rents collapse as N grows.
**Relation to this project:** Used in Channel 2 to show that when AI produces correlated signals (rho -> 1), competitive returns collapse via the Holden-Subrahmanyam result.
**Threat level:** LOW / Foundational

### Bond, Edmans, and Goldstein (2012) -- *The Real Effects of Financial Markets*

**Journal:** Annual Review of Financial Economics
**Core question:** How do financial markets affect real investment decisions?
**Model structure:** Survey and framework distinguishing forecasting price efficiency (FPE) from revelatory price efficiency (RPE).
**Key mechanism:** RPE measures the extent to which prices reveal information not otherwise available to decision-makers. FPE measures predictive accuracy. The two can diverge.
**Key result:** Financial markets affect real decisions primarily through RPE. FPE can improve while RPE degrades.
**Relation to this project:** Channel 2 welfare analysis uses the FPE/RPE distinction: AI may improve FPE (better predictions) while degrading RPE (less information diversity revealed to corporate decision-makers).
**Threat level:** LOW / Foundational

---

## Channel 3 -- Market Making

### Colliard, Foucault, and Lovo (2025) -- *Algorithmic Pricing and Liquidity in Securities Markets*

**Journal:** Review of Financial Studies (forthcoming)
**Core question:** How do algorithmic market makers using reinforcement learning price securities?
**Model structure:** Glosten-Milgrom (1985) adverse selection framework with a Q-learning market maker.
**Key mechanism:** Q-learning market makers charge markups that increase when adverse selection costs decrease, contrary to Nash equilibrium predictions. Identifies behavioural "footprints" of ML-based pricing.
**Key result:** Algorithmic market makers produce non-competitive pricing behaviour detectable through specific trading data patterns.
**Relation to this project:** Relevant to Channel 3 as it models AI-driven market making. However, the mechanism (single-agent RL pricing dynamics) is distinct from Channel 3's mechanism (N market makers with correlated AI signals producing simultaneous withdrawal).
**Threat level:** MODERATE

### Cespa and Vives (forthcoming) -- *Market Opacity and Fragility: Why Liquidity Evaporates When It Is Most Needed*

**Journal:** American Economic Review (conditionally accepted)
**Core question:** Why does liquidity evaporate precisely when it is most needed?
**Model structure:** Market microstructure model with opaque markets and hedger trading.
**Key mechanism:** Market opacity creates strategic complementarity in liquidity demand. Lack of transparency makes hedgers' price impact strategic complements, yielding multiple equilibria.
**Key result:** Flash-crash-type equilibria where liquidity evaporates suddenly, driven by opacity rather than fundamentals.
**Relation to this project:** Parallel fragility mechanism to Channel 3. However, the complementarity arises from opacity, not from algorithmic similarity. The two mechanisms could compound.
**Threat level:** MODERATE

### Greenwood and Thesmar (2011) -- *Stock Price Fragility*

**Journal:** Journal of Financial Economics
**Core question:** How does the covariance of institutional demand shocks affect stock price stability?
**Model structure:** Empirical measure of stock fragility based on covariance of mutual fund flow shocks.
**Key mechanism:** When holders of a stock experience correlated demand shocks (e.g., correlated fund flows), the stock price is fragile and prone to large non-fundamental moves.
**Key result:** Stock fragility (covariance of holders' demand shocks) predicts future return volatility and non-fundamental price moves.
**Relation to this project:** N_eff(rho) is an analogue of Greenwood-Thesmar fragility applied to the supply side (market-maker algorithmic similarity) rather than the demand side (fund flow correlation).
**Threat level:** MODERATE

### Danielsson, Macrae, and Uthemann (2022) -- *Artificial Intelligence and Systemic Risk*

**Journal:** Journal of Banking and Finance
**Core question:** How does AI affect systemic risk?
**Model structure:** Qualitative/narrative analysis. No formal model.
**Key mechanism:** AI homogenises risk perceptions across financial institutions. Similar perceptions lead to similar actions. Procyclicality increases; lower volatility but fatter tails.
**Key result:** AI creates a monoculture in risk management that amplifies systemic risk. Four channels discussed: information processing, common data, speed, strategic complementarities.
**Relation to this project:** The most direct qualitative predecessor. The project formalises these qualitative insights into three formal channels with an amplification loop. The 2022 paper motivates the project; the project delivers the formal analysis.
**Threat level:** MODERATE

### Danielsson, Shin, and Zigrand (2012) -- *Endogenous and Systemic Risk*

**Journal:** NBER chapter (Quantifying Systemic Risk)
**Core question:** How do common risk management constraints generate endogenous systemic risk?
**Model structure:** Multi-agent model where institutions use common VaR constraints to manage risk.
**Key mechanism:** Common VaR constraints produce procyclical selling. When volatility rises, all institutions simultaneously reduce exposure, amplifying price impact.
**Key result:** Endogenous risk from common constraints exceeds exogenous risk. Procyclical regulation amplifies crises.
**Relation to this project:** Channel 3 nests the Danielsson-Shin-Zigrand common VaR mechanism as a limiting case. The project generalises from regulatory-driven homogeneity (VaR) to AI-driven signal homogeneity (rho), with N_eff(rho) as the formal index.
**Threat level:** MODERATE

### Glosten and Milgrom (1985) -- *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*

**Journal:** Journal of Financial Economics
**Core question:** How do bid-ask spreads reflect adverse selection?
**Key mechanism:** Market makers widen spreads when the probability of trading with an informed agent increases.
**Relation to this project:** Foundational for Channel 3 spread-widening mechanism.
**Threat level:** LOW / Foundational

### Kyle (1985) -- *Continuous Auctions and Insider Trading*

**Journal:** Econometrica
**Core question:** How does informed trading affect market prices in continuous time?
**Key mechanism:** Linear equilibrium where the market maker adjusts the price in response to order flow, balancing information revelation and noise trading.
**Relation to this project:** Foundational for Channel 3.
**Threat level:** LOW / Foundational

### Avellaneda and Stoikov (2008) -- *High-Frequency Trading in a Limit Order Book*

**Journal:** Quantitative Finance
**Core question:** What is the optimal market-making strategy in a limit order book?
**Key mechanism:** Stochastic control framework; reservation price r = S - q*gamma*sigma^2*(T-t).
**Relation to this project:** Channel 3 uses this framework to show that shared AI calibration produces near-identical spread-widening functions across market makers.
**Threat level:** LOW / Foundational

### Pagano (1989) -- *Trading Volume and Asset Liquidity*

**Journal:** Quarterly Journal of Economics
**Key mechanism:** Multiple equilibria in market participation. Low-liquidity traps where thin markets are self-reinforcing.
**Relation to this project:** Channel 3 threshold rho** (no finite-spread equilibrium) is analogous to Pagano's low-liquidity trap.
**Threat level:** LOW / Foundational

### Brunnermeier and Pedersen (2009) -- *Market Liquidity and Funding Liquidity*

**Journal:** Review of Financial Studies
**Key mechanism:** Margin spirals create feedback between market liquidity and funding liquidity.
**Relation to this project:** Channel 3 connects to margin spiral mechanics. AI-driven correlated liquidity withdrawal could trigger Brunnermeier-Pedersen spirals.
**Threat level:** LOW / Foundational

---

## Amplification Loop

### Dou, Goldstein, and Ji (2025a) -- *AI-Powered Trading, Algorithmic Collusion, and Price Efficiency*

**Journal:** NBER Working Paper 34054
**Core question:** Can AI-powered trading algorithms autonomously sustain collusive outcomes?
**Model structure:** Simulation framework with RL-powered speculators replacing traditional informed traders in a Kyle-type market.
**Key mechanism:** Homogenisation of RL strategies and self-confirming equilibrium lead to emergent collusion. AI speculators sustain supra-competitive profits without communication.
**Key result:** AI collusion undermines competition, market efficiency, and liquidity.
**Relation to this project:** Addresses AI-driven fragility through a complementary mechanism (RL collusion vs. signal correlation). No rho parameterisation, no global games, no three-channel fixed-point.
**Threat level:** MODERATE

### Dou, Goldstein, and Ji (2025b) -- *Financial Market Fragility in the Era of AI Planning*

**Journal:** SSRN Working Paper 5763222
**Core question:** How does agentic AI with planning capability affect market stability?
**Model structure:** Dynamic trading with positive-feedback investors, constrained arbitrageurs, and oligopolistic AI speculators with planning capability.
**Key mechanism:** AI speculators with planning capability learn intertemporal collusive strategies, creating and exploiting negative bubbles.
**Key result:** Agentic AI introduces new fragility through coordinated destabilisation based on lookahead planning.
**Relation to this project:** Addresses AI fragility through planning/lookahead, not signal correlation. No Channel 1 (global games), no Channel 2 (GS information acquisition), no Channel 3 (N_eff). Formally independent mechanism.
**Threat level:** MODERATE

### Goldstein, Huang, and Yang (2025) -- *Fragility of Financial Markets*

**Journal:** Annual Review of Financial Economics
**Core question:** What forces generate financial market fragility?
**Model structure:** Survey paper providing canonical trading frameworks for analysing fragility.
**Key mechanism:** Multiple forces: learning from prices, strategic complementarities, amplification channels.
**Key result:** Systematic taxonomy of fragility forces and their interactions.
**Relation to this project:** Survey of the theoretical foundations. The project's amplification loop is a specific instance of multi-channel fragility. The survey does not model AI-specific mechanisms.
**Threat level:** LOW / Foundational

---

## AI and Financial Markets (Empirical / Applied)

### Kim, Muhn, and Nikolaev (2024) -- *From Transcripts to Insights: Uncovering Corporate Risks Using Generative AI*

**Journal:** arXiv preprint
**Core question:** Can generative AI produce useful financial statement analysis?
**Key mechanism:** GPT-4 at temperature=0 produces near-identical analyses across runs and analysts, documenting belief homogenisation.
**Key result:** AI-generated financial analyses exhibit extremely high cross-sectional correlation.
**Relation to this project:** Primary empirical evidence for rho -> 1.
**Threat level:** MODERATE

### Calvano, Calzolari, Denicolo, and Pastorello (2020) -- *Artificial Intelligence, Algorithmic Pricing, and Collusion*

**Journal:** American Economic Review
**Core question:** Can AI algorithms learn to collude in pricing without explicit communication?
**Key mechanism:** Q-learning algorithms in repeated oligopoly games autonomously learn to sustain supra-competitive prices.
**Key result:** Collusive outcomes emerge from independent RL agents without communication or pre-programming.
**Relation to this project:** Demonstrates AI coordination without communication. Set in product pricing (not financial markets) with a different mechanism (RL repeated game, not signal correlation).
**Threat level:** MODERATE

### Gu, Kelly, and Xiu (2020) -- *Empirical Asset Pricing via Machine Learning*

**Journal:** Review of Financial Studies
**Core question:** Which ML methods best predict stock returns?
**Key mechanism:** Diverse ML methods (penalised regressions, trees, neural networks) converge on the same dominant predictors.
**Key result:** All methods select momentum, liquidity, and volatility as dominant predictors.
**Relation to this project:** Empirical foundation for rho -> 1. Demonstrates convergence of ML outputs.
**Threat level:** LOW / Foundational

---

## Extensions (Endogenous rho / Diversity Mandate)

### Gans (2023) -- *Artificial Intelligence Adoption in a Competitive Market*

**Journal:** Economica, Vol. 90, Issue 358, pp. 690-705
**Core question:** How does AI adoption work as a competitive strategy, and what externalities arise?
**Model structure:** Competitive market model where firms adopt AI for demand prediction. AI is a complement to variable inputs.
**Key mechanism:** AI adoption generates externalities: it reduces profits of non-adoptees when variable inputs are important. AI does not operate as a standard process innovation.
**Key result:** AI adoption creates competitive pressure but with non-standard externality structure.
**Relation to this project:** Related to Contribution 5 (endogenous rho). Models competitive AI adoption with externalities, but in product markets, not financial markets. No signal correlation, no financial fragility channels.
**Threat level:** LOW / Contextual

### Kleinberg and Raghavan (2021) -- *Algorithmic Monoculture and Social Welfare*

**Journal:** Proceedings of the National Academy of Sciences
**Core question:** Does algorithmic monoculture reduce aggregate decision quality?
**Model structure:** Multiple decision-makers use the same or different algorithms to screen candidates.
**Key mechanism:** Monoculture (same algorithm) can reduce aggregate accuracy relative to polyculture (diverse algorithms) because errors become correlated.
**Key result:** Even under normal operations (no shocks or correlated failures), monoculture decreases decision quality.
**Relation to this project:** Conceptually related to the diversity mandate. Formalises the welfare cost of algorithmic monoculture. However, set in a general decision-making context, not financial markets.
**Threat level:** LOW / Contextual

### Peng, Kleinberg, Raghavan, and Lipton (2024) -- *Monoculture in Matching Markets*

**Journal:** NeurIPS 2024
**Core question:** How does algorithmic monoculture affect outcomes in two-sided matching markets?
**Model structure:** Two-sided matching market with many participants. Decision-makers evaluate applicants using either a common algorithm (monoculture) or independent processes (polyculture).
**Key mechanism:** Monoculture concentrates competition on the same applicants, reducing total match quality. Polyculture spreads demand across applicants, improving aggregate welfare.
**Key result:** Polyculture significantly outperforms monoculture in firm welfare, even when idiosyncratic evaluations are noisier.
**Relation to this project:** Extends the monoculture argument to market settings. Related to Contribution 5 but in a non-financial matching market context.
**Threat level:** LOW / Contextual

---

## Synthesis Notes

### Cross-paper themes

1. **Information-theoretic vs. RL/behavioural mechanisms:** A clear divide exists between papers using RL/learning-based mechanisms for AI coordination (Yang 2024; Dou-Goldstein-Ji 2025a,b; Calvano et al. 2020; Colliard-Foucault-Lovo 2025) and the project's information-theoretic approach (correlated signals through rho). No existing paper uses the rho parameterisation.

2. **Temporal vs. cross-sectional dimension:** Dugast-Foucault (2018, 2025) and Farboodi-Veldkamp (2020) operate in the temporal dimension (how information technology evolves over time). The project operates in the cross-sectional dimension (correlation across agents at a point in time). This is the key differentiator for Channel 2.

3. **Qualitative vs. formal multi-channel analysis:** Danielsson-Macrae-Uthemann (2022) and policy reports make qualitative arguments about multi-channel AI-driven systemic risk. No paper provides formal analysis connecting coordination, information, and liquidity channels through a common parameterisation. The amplification loop fills this gap.

4. **Monoculture costs established outside finance:** Kleinberg-Raghavan (2021) and Peng et al. (2024) establish monoculture welfare costs in general and matching market settings. The financial markets application with fragility channels is novel.

### Where this project differs from all identified competitors

The project's distinctive feature is the triple combination of: (a) the rho parameterisation as a unifying primitive across three channels, (b) formal equilibrium analysis of each channel linking rho to fragility, and (c) the fixed-point interaction characterising compound fragility. No existing paper combines any two of these three elements.
