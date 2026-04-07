# Post-Referee Literature Review
Date: 2026-03-12
Task queue version: Round 3 (2026-03-12)

## Summary

This review addresses literature-related tasks T-17 through T-22 and T-25 from the revision task queue, responding to gaps flagged by the connections, relevance, and general referee reports. The searches focused on six missing references (Verrecchia 1982, Katz-Shapiro 1985, Farrell-Saloner 1985, Allen-Gale 2000, Brunnermeier-Pedersen 2009, Shleifer-Vishny 1997), orphan citation engagement, Channel 3 empirical grounding, and precedents for how top-journal theory papers handle testable implications. The novelty picture is unchanged: none of the newly examined papers threatens the core contributions. All recommended citations are positioning or engagement citations, not threat responses.

## Findings by Task

### Task T-17: Add citations to extensions section (Katz-Shapiro 1985, Farrell-Saloner 1985, Gans 2023)

**Search targets:** Technology adoption externality literature; network effects and compatibility; AI adoption models with externalities.

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Katz and Shapiro (1985) | Network Externalities, Competition, and Compatibility, AER 75(3):424-440 | The adoption externality in the extensions section (Proposition 10) is structurally analogous to a network externality: each firm's payoff from adopting the AI model increases with the number of other adopters (through reduced tracking error). Katz-Shapiro establish that market failures arise when adoption confers positive externalities on others but the adopter does not internalise the systemic cost. The distinction is that in this paper the externality operates through signal correlation (higher rho) rather than network compatibility. | Cite and engage |
| Farrell and Saloner (1985) | Standardization, Compatibility, and Innovation, RAND J. Econ. 16:70-83 | Their "excess inertia" result -- where an installed base of an inferior standard prevents efficient adoption of a superior alternative -- maps to the prisoner's dilemma: once firms have adopted the common AI model (high rho_bar), individual deviation is costly even if aggregate welfare would improve. Their "excess momentum" result is also relevant: once adoption begins, the process may overshoot the social optimum. | Cite and engage |
| Gans (2023) | Artificial Intelligence Adoption in a Competitive Market, Economica 90(358):690-705 | Models AI adoption as a complement to variable inputs with externalities on non-adopters. The externality structure differs: Gans's externality operates through competitive product market dynamics, while this paper's operates through signal correlation and financial fragility. However, Gans's finding that AI does not operate as a standard process innovation supports the broader argument that AI adoption externalities require non-standard modelling. | Cite and acknowledge |

**Guidance for Paper Writer:** In extensions.tex, at the start of Section 8.1 (endogenous rho), add: "The coordination failure in AI adoption resembles the technology adoption externalities studied by Katz and Shapiro (1985) and Farrell and Saloner (1985), with the distinction that the externality here operates through signal correlation rather than network compatibility. The excess inertia result of Farrell and Saloner (1985) -- where an installed base prevents efficient switching -- maps to the equilibrium lock-in at rho_NE > rho* in Proposition 10." Add Gans (2023) with a brief clause: "Gans (2023) shows AI adoption in product markets generates non-standard externalities; the financial-market analog here is the systemic fragility externality." Bib entries for Katz-Shapiro and Farrell-Saloner must be added (not currently in references.bib). Gans (2023) is already in the bib.

---

### Task T-18: Add amplification positioning citations (Brunnermeier-Pedersen 2009, Shleifer-Vishny 1997, Allen-Gale 2000)

**Search targets:** Amplification and feedback mechanisms in financial economics; margin spirals; contagion through interbank linkages; limits of arbitrage feedback.

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Brunnermeier and Pedersen (2009) | Market Liquidity and Funding Liquidity, RFS 22(6):2201-2238 | The margin/loss spiral -- where declining asset prices tighten funding constraints, forcing further sales -- is the closest structural analog to the amplification loop in this paper. Both feature positive feedback between two state variables (here: rho_eff and N_eff; there: market liquidity and funding liquidity). The key distinction is the trigger: Brunnermeier-Pedersen's spiral is driven by funding constraints and margin requirements, while this paper's is driven by information homogeneity. | Cite and engage |
| Shleifer and Vishny (1997) | The Limits of Arbitrage, JF 52(1):35-55 | The limits-of-arbitrage feedback -- where mispricing causes capital withdrawal, which worsens mispricing -- provides another structural analog. In this paper, signal correlation reduces the value of private information (Channel 2), causing information withdrawal, which increases effective correlation. The distinction is that Shleifer-Vishny's constraint is capital-based (performance-sensitive fund flows), while this paper's is information-based (declining informational rents). | Cite and engage |
| Allen and Gale (2000) | Financial Contagion, JPE 108(1):1-33 | Models contagion through interbank claims: a liquidity shock in one region propagates through the network. The phase transition result -- where network completeness determines whether shocks are absorbed or amplified -- is conceptually related to the bifurcation at rho*. The distinction is that Allen-Gale's contagion channel is balance-sheet linkages, while this paper's is information homogeneity. No network topology appears in this paper. | Cite and acknowledge |

**Guidance for Paper Writer:** At the start of the amplification section (before the channel mappings), add 2-3 sentences: "The positive feedback mechanism studied here is structurally analogous to margin spirals (Brunnermeier and Pedersen 2009), limits-of-arbitrage feedback (Shleifer and Vishny 1997), and contagion through interbank linkages (Allen and Gale 2000). The distinguishing feature is that the trigger is information homogeneity -- the common AI signal -- rather than funding constraints, capital withdrawal, or balance-sheet linkages. The compound threshold rho* plays a role analogous to the critical margin level in Brunnermeier-Pedersen: below it, the system absorbs shocks; above it, the feedback loop drives the system to a corner." All three papers are already in references.bib.

---

### Task T-19: State Morris-Shin -> Hellwig -> GP intellectual chain

**Search targets:** No new search needed. This is an engagement/positioning task for existing citations.

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Morris and Shin (1998) | Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks, AER | Established uniqueness via heterogeneous private signals | Already cited; reposition |
| Morris and Shin (2002) | Social Value of Public Information, AER | Showed public information has disproportionate effect on coordination | Already cited; reposition |
| Hellwig (2002) | Public Information, Private Information, and the Multiplicity of Equilibria in Coordination Games, JET | Proved sufficiently precise public information restores multiplicity | Already cited; reposition |
| Goldstein and Pauzner (2005) | Demand Deposit Contracts and the Probability of Bank Runs, JF | Applied global games to bank runs; unique crisis threshold | Already cited; reposition |

**Guidance for Paper Writer:** Add one sentence at the start of Channel 1 (channel1.tex): "Channel 1 builds on the global games framework of Morris and Shin (1998, 2002), incorporating Hellwig's (2002) result that sufficiently precise public information restores equilibrium multiplicity, applied to the Goldstein and Pauzner (2005) bank-run setting. The key insight is that correlated AI signals function as an endogenous public signal: as rho increases, the effective precision of the common component rises, eventually crossing Hellwig's multiplicity threshold." No new bib entries needed.

---

### Task T-20: Add Verrecchia (1982) citation and Kyle distinction

**Search targets:** Verrecchia (1982) CARA-normal REE with continuum of agents; Kyle (1985) vs. Glosten-Milgrom (1985) intellectual lineage for market-making models.

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Verrecchia (1982) | Information Acquisition in a Noisy Rational Expectations Economy, Econometrica 50(6):1415-1430 | The standard reference for the CARA-normal Grossman-Stiglitz equilibrium with a continuum of agents and endogenous information acquisition. Channel 2 uses exactly this setup (continuum of CARA agents, normal signals, endogenous information choice) but cites only Grossman-Stiglitz (1980), which uses a two-agent model. A microstructure referee will expect the Verrecchia citation. | Cite and engage |

**Guidance for Paper Writer:** (a) In channel2.tex setup paragraph, add after the Grossman-Stiglitz citation: "following the CARA-normal competitive equilibrium of Verrecchia (1982) with a continuum of agents." (b) In channel3.tex, add a sentence distinguishing foundations: "The market-making framework descends from the Kyle (1985) inventory-management tradition, adapted by Avellaneda and Stoikov (2008), rather than the Glosten and Milgrom (1985) adverse-selection framework. The relevant distinction is that our market makers manage inventory risk from correlated position limits, not adverse selection from informed order flow." (c) Add Verrecchia (1982) bib entry to references.bib (currently missing).

---

### Task T-21: Fix orphan and catalogue citations

**Search targets:** Engagement guidance for Kleinberg-Raghavan (2021), Peng et al. (2024), Gans (2023), Acemoglu et al. (2015), Farboodi et al. (2022), Banerjee-Davis-Gondhi (2018), Vives (2014), Pagano (1989).

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Kleinberg and Raghavan (2021) | Algorithmic Monoculture and Social Welfare, PNAS | Formalises the cost of algorithmic monoculture in general decision-making. The paper's N_eff result is the financial-market analog: monoculture (rho -> 1) collapses the effective number of independent decision-makers. | Cite and engage (one sentence) |
| Peng et al. (2024) | Monoculture in Matching Markets, NeurIPS | Extends monoculture costs to two-sided matching. Less directly relevant than Kleinberg-Raghavan but supports the broader monoculture argument. | Cite and acknowledge (group with K-R) |
| Gans (2023) | AI Adoption in a Competitive Market, Economica | See T-17 above. The cross-channel subsection should state the relationship: Gans models AI adoption externalities in product markets; this paper models them in financial markets through the signal correlation channel. | Cite and engage (one sentence) |
| Acemoglu et al. (2015) | Systemic Risk and Stability in Financial Networks, AER 105(2):564-608 | Their phase-transition result (dense networks absorb small shocks but amplify large ones) suggests rho* may depend on network topology among financial institutions. This is a natural extension direction but not modelled here. | Cite and engage in conclusion |
| Farboodi et al. (2022) | Where Has All the Data Gone?, RFS 35(7):3101-3138 | Data concentration on large firms implies rho may be heterogeneous across assets: higher for heavily covered stocks (many AI models trained on abundant data) and lower for small-cap stocks with scarce data. | Cite and engage (one sentence) |
| Banerjee, Davis, and Gondhi (2018) | When Transparency Improves, Must Prices Reflect Fundamentals Better?, RFS 31(6):2377-2414 | BDG's paradox operates through the composition of learning targets (fundamentals vs. beliefs). This paper's Channel 2 operates through cross-sectional signal correlation. Both produce the paradox of better information reducing price informativeness, but through distinct channels. | Cite and engage (one sentence distinguishing) |
| Vives (2014) | On the Possibility of Informationally Efficient Markets, JEEA 12(5):1200-1239 | Vives shows a privately revealing equilibrium obtains when correlation in traders' valuations is bounded. Specifically, the equilibrium exists when correlation is sufficiently low that traders retain incentives to acquire information. As AI drives rho toward 1, this condition is progressively violated: the high correlation in AI-generated valuations destroys the diversity that sustains Vives's equilibrium. | Cite and engage (specify the condition) |
| Pagano (1989) | Trading Volume and Asset Liquidity, QJE 104(2):255-274 | The low-liquidity trap: expectation of thin markets deters participation, validating the expectation. Channel 3's rho** threshold is a direct analog: expectation of correlated market-maker withdrawal raises effective adverse selection, deterring remaining market makers. | Cite and engage (expand analogy) |

**Guidance for Paper Writer:**
- **Kleinberg-Raghavan + Peng et al.:** In literature.tex cross-channel subsection, replace the parenthetical cluster with: "Kleinberg and Raghavan (2021) formalise the aggregate accuracy cost of algorithmic monoculture in general decision-making; Peng et al. (2024) extend this to two-sided matching markets. Our N_eff result is the financial-market analog: signal monoculture (rho -> 1) collapses the effective number of independent market makers from N to 1."
- **Gans (2023):** In literature.tex cross-channel subsection, add: "Gans (2023) models AI adoption externalities in product markets through competitive dynamics; the financial-market analog here is the systemic fragility externality operating through signal correlation."
- **Acemoglu et al. (2015):** In conclusion.tex future work, replace the current vague engagement with: "The network fragility results of Acemoglu, Ozdaglar, and Tahbaz-Salehi (2015) -- where dense interconnections absorb small shocks but amplify large ones -- suggest that the compound threshold rho* may depend on the network topology of financial institutions, a question we leave for future work."
- **Farboodi et al. (2022):** In literature.tex information subsection, add: "Farboodi et al. (2022) document that data technology concentrates information on large firms, implying that rho may be higher for heavily covered stocks where many AI models train on abundant overlapping data, and lower for small-cap stocks with scarce data."
- **BDG (2018):** In literature.tex information subsection, add: "Our Channel 2 mechanism is distinct from Banerjee, Davis, and Gondhi (2018): their paradox operates through the composition of learning targets (fundamentals vs. beliefs), while ours operates through cross-sectional signal correlation among agents using the same AI model."
- **Vives (2014):** In literature.tex information subsection, sharpen to: "Vives (2014) shows a privately revealing equilibrium obtains when correlation in traders' valuations is bounded below a critical threshold; as AI drives signal correlation toward one, this bound is violated and the conditions for informational efficiency break down."
- **Pagano (1989):** In channel3.tex, expand: "analogous to the Pagano (1989) low-liquidity trap, where the expectation of thin markets deters participation, validating the expectation. Here, the expectation of correlated market-maker withdrawal raises effective adverse selection costs for remaining market makers, reinforcing the withdrawal."

---

### Task T-22: Add two-fundamental economic link

**Search targets:** No new literature search needed. This is a framing task using existing model structure.

**Papers found:** N/A -- this task requires positioning prose, not new citations.

**Guidance for Paper Writer:** In amplification.tex, before the channel mappings, add: "The three channels operate on different fundamentals: theta (bank asset quality) in Channel 1 and V (risky asset value) in Channels 2-3. The economic link is that bank crises degrade collateral values and destroy trading opportunities in the risky asset market, providing the channel through which theta-space outcomes affect V-space decisions. Formally, we capture this through the discount factor delta(theta*) in g_2, which reduces the expected value of private information about V when crisis probability is high."

---

### Task T-25: Strengthen Channel 3 empirical grounding

**Search targets:** Evidence of AI/algorithmic convergence among market makers; VaR model homogeneity; correlated algorithmic withdrawal during market stress events.

**Papers found:**

| Author-Year | Title | Relationship to this paper | Recommendation |
|-------------|-------|---------------------------|----------------|
| Danielsson, Shin, and Zigrand (2012) | Endogenous and Systemic Risk, in Quantifying Systemic Risk (UChicago Press) | Documents that common VaR constraints cause market participants to "act in harmony, shedding the same risky assets and buying the same safe assets" during stress. This is a direct precedent for the Channel 3 mechanism: VaR model homogeneity is a special case of AI calibration homogeneity. | Cite and engage (already in bib) |
| Kirilenko, Kyle, Samadi, and Tuzun (2017) | The Flash Crash: High-Frequency Trading in an Electronic Market, JF 72(3):967-998 | Using audit-trail data from the May 6, 2010 flash crash, documents trading patterns of high-frequency intermediaries during the crash. While the paper finds HFT behaviour did not change during the crash, the broader literature interprets the flash crash as evidence of correlated algorithmic behaviour and withdrawal during stress. The episode illustrates the fragility of markets with homogeneous algorithmic intermediation. | Cite and acknowledge |
| FSB (2024) | The Financial Stability Implications of Artificial Intelligence | Identifies "market correlations" as a key vulnerability from AI adoption in financial services, noting that widespread use of similar AI models could amplify systemic vulnerabilities during stress. | Cite and acknowledge |
| Bank of England (2025) | Financial Stability in Focus: Artificial Intelligence in the Financial System | Notes "widespread use of similar AI models potentially amplifying systemic vulnerabilities, particularly under market stress." Reports 11% of surveyed firms use AI for algorithmic trading with 9% planning adoption. | Cite and acknowledge |
| Liu, Miao, Wang, and Wang (2025) | Strategic Homogeneity in Trading: Amplifying Market Volatility and the Emergence of Mini-Crashes, SSRN WP 5239024 | Introduces a Multi-Dimensional Homogeneous Trading Indicator (MD-HTI) and shows elevated strategic homogeneity substantially increases mini-crash risk. Empirical evidence using high-frequency data that trading strategy convergence amplifies volatility. | Cite and acknowledge |

**Guidance for Paper Writer:** In channel3.tex, near the setup or after the N_eff result, add: "While direct evidence on AI calibration correlation among market makers is still emerging, the VaR model homogeneity documented by Danielsson, Shin, and Zigrand (2012) -- where common risk constraints cause market participants to 'act in harmony' during stress -- provides a direct precedent for the mechanism modelled here. Kirilenko et al. (2017) document the fragility of algorithmic intermediation during the May 2010 flash crash. More recently, Liu et al. (2025) show empirically that strategic homogeneity among algorithmic traders amplifies market volatility and increases mini-crash risk, and the FSB (2024) identifies correlated AI model use as a key financial stability vulnerability." Bib entries needed for: Kirilenko et al. (2017), FSB (2024), Bank of England (2025), Liu et al. (2025).

---

## Threat Map Updates

No changes -- novelty picture unchanged. None of the newly examined papers (Katz-Shapiro 1985, Farrell-Saloner 1985, Allen-Gale 2000, Shleifer-Vishny 1997, Verrecchia 1982, Kirilenko et al. 2017, FSB 2024, Bank of England 2025, Liu et al. 2025) model the core mechanism (signal homogeneity driving three-channel financial fragility through a fixed-point amplification loop). All recommended citations are for positioning, intellectual lineage, or empirical grounding -- not threat mitigation.

## Missing Reference Resolutions

| Reference | Status | Rationale |
|-----------|--------|-----------|
| Verrecchia (1982) | FOUND -- add to bib and cite in channel2.tex | Standard CARA-normal GS reference for continuum of agents. Missing from channel2.tex despite using this exact setup. |
| Katz and Shapiro (1985) | FOUND -- add to bib and cite in extensions.tex | Network externalities in technology adoption. Missing from extensions section despite prisoner's dilemma having adoption externality structure. |
| Farrell and Saloner (1985) | FOUND -- add to bib and cite in extensions.tex | Standardization and excess inertia. Missing from extensions section; excess inertia maps to equilibrium lock-in at rho_NE > rho*. |
| Allen and Gale (2000) | FOUND -- already in bib as implied by threat map but needs bib entry | Contagion through interbank linkages. Missing from amplification section. Bib entry must be added. |
| Brunnermeier and Pedersen (2009) | FOUND -- already in bib (brunnermeier2009) | Margin spirals. Already in bib but not cited in amplification section where it belongs. |
| Shleifer and Vishny (1997) | FOUND -- add to bib | Limits of arbitrage feedback. Missing from amplification section. Bib entry must be added. |
| Kirilenko, Kyle, Samadi, and Tuzun (2017) | FOUND -- add to bib | Flash crash empirical evidence. Missing from Channel 3 empirical grounding. |

### New bib entries required:

1. `verrecchia1982` -- Econometrica 50(6):1415-1430
2. `katz1985` -- AER 75(3):424-440
3. `farrell1985` -- RAND J. Econ. 16:70-83
4. `allen2000` -- JPE 108(1):1-33
5. `shleifer1997` -- JF 52(1):35-55
6. `kirilenko2017` -- JF 72(3):967-998
7. `fsb2024` -- FSB report, November 2024
8. `boe2025` -- Bank of England, Financial Stability in Focus, April 2025
9. `liu2025` -- SSRN WP 5239024

## Testable Implications Precedents

Three examples of how comparable theory papers at JF/RFS handle testable implications sections:

1. **Brunnermeier and Pedersen (2009), RFS.** Section VI ("Empirical Implications") lists five specific empirically documented features that the model explains: (i) sudden liquidity dry-ups, (ii) commonality across securities, (iii) relation to volatility, (iv) flight to quality, (v) co-movement with the market. Each prediction is stated as a qualitative relationship between observable quantities (e.g., "market liquidity co-moves across securities" maps to the model's shared funding constraint). They also identify novel testable predictions: speculators' capital as a driver of market liquidity and risk premiums. The approach is: state the observable regularity, cite existing empirical evidence where available, and identify the model mechanism that generates it.

2. **Goldstein and Yang (2015), JF.** Section V ("Empirical Implications") derives three testable predictions from the model's comparative statics: (i) stock price informativeness increases with information diversity across trader groups, (ii) complementarities in trading imply that improving one dimension of information increases trading on the other, (iii) information diversity effects are stronger when strategic complementarities are stronger. Each prediction names the observable proxy (e.g., analyst coverage diversity as a proxy for information diversity) and the predicted relationship. The approach is more directly connected to specific cross-sectional variation than Brunnermeier-Pedersen.

3. **Cespa and Vives (forthcoming AER).** The paper connects its opacity-driven fragility mechanism to flash crashes and liquidity dry-ups, using the May 2010 flash crash as a motivating case. Empirical implications are woven into the model development rather than isolated in a separate section. The sufficient conditions for fragility (overlapping cohorts, enough opacity, risk-averse dealers) are stated in terms that map to observable market characteristics. The approach is: identify observable market features that correspond to model parameters, state the predicted relationship, and connect to specific market episodes.

**Recommendation for this paper:** Follow the Brunnermeier-Pedersen approach: add a subsection listing 2-3 predictions, each structured as (i) observable proxy for rho (portfolio return correlation, forecast revision correlation, algorithmic strategy overlap), (ii) predicted relationship (non-monotone crisis probability, declining RPE, N_eff collapse), (iii) data source (CRSP, TAQ, I/B/E/S, 13F), (iv) empirical design sketch (panel regression with quadratic term for non-monotonicity; cross-sectional variation in AI market-making share for N_eff). This format is established at RFS and would satisfy the relevance referee's demand for specificity.
