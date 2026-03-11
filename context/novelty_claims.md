# Novelty Claims

This document lists the paper's five contributions in formal proposition form, cross-referenced to threat map entries, with differentiators and coverage gaps. The Literature Guardian M3 should verify each claim against the threat map and conduct targeted searches as indicated by the risk flags.

---

## Claim 1: theta*(rho) Characterisation (Channel 1)

**Formal result:** Proposition 1: In the Goldstein-Pauzner (2005) bank-run framework with rho-parameterised AI signals epsilon_i = sqrt(rho)*eta + sqrt(1-rho)*xi_i, the crisis threshold theta*(rho) is non-monotone in rho and the uniqueness/multiplicity boundary rho* is characterised analytically as a function of rho, the fraction of AI-equipped agents, and the degree of strategic complementarity.

**Threat map entries to differentiate from:**
- Yang (2024), Working paper, Swiss Finance Institute -- HIGH threat, Channel 1
- Danielsson and Uthemann (2025), Journal of Financial Stability, Vol. 80 -- HIGH threat, Channel 1

**Differentiator from Yang (2024):** Yang's mechanism is purely RL-based (Q-learning agents learn crisis thresholds through repeated behavioural interaction in a Morris-Shin 1998 speculative attack game). No signal correlation parameter rho exists in that model; no analytical characterisation of the crisis threshold as a function of signal structure. The project derives theta*(rho) analytically from the information-theoretic mechanism where correlated signals restore Hellwig (2002) multiplicity.

**Differentiator from Danielsson-Uthemann (2025, JFS):** The primitive is rho (signal correlation, intensive margin of AI output homogeneity) vs. mu (AI agent fraction, extensive margin of AI penetration). Their theta*(mu) = (c/b)[(1-mu)p + mu] captures the AI execution-speed advantage under maintained Morris-Shin uniqueness conditions. The project's theta*(rho) captures the information-theoretic mechanism where correlated signals progressively restore the Hellwig (2002) multiplicity region. The project analytically characterises the uniqueness/multiplicity boundary as a function of signal correlation, which Danielsson-Uthemann discuss qualitatively (Section 2.2.2) but do not derive formally.

**Coverage gap filled:** Gap 1.1 (no paper derives theta*(rho) as a function of cross-sectional signal correlation in a global games framework); Gap 1.3 (non-monotonicity of theta*(rho) in an AI context not characterised).

**Risk flag for Literature Guardian M3:** Verify that no paper derives theta*(rho) in a Goldstein-Pauzner bank-run setting with correlated signals. Specifically search for: (1) any extension of Goldstein-Pauzner (2005) or Morris-Shin (1998) with a signal correlation parameter, (2) any paper that analytically characterises the uniqueness/multiplicity boundary as a function of signal correlation in a coordination game with AI agents, (3) any 2025-2026 working papers by Danielsson, Uthemann, or co-authors that extend the 2025 JFS model with signal correlation.

---

## Claim 2: Cross-Sectional GS Extension with RPE Collapse (Channel 2)

**Formal result:** Proposition 2: In the correlated-signal extension of Grossman-Stiglitz (1980) with two information types (AI-processed at near-zero cost with pairwise correlation rho, and genuinely private at cost c_P with correlation approximately 0), the equilibrium fraction of agents acquiring genuinely private information is decreasing in rho, and price informativeness measured by RPE is non-monotone in AI adoption -- improving at low rho but collapsing at high rho as information diversity is destroyed.

**Threat map entries to differentiate from:**
- Dugast and Foucault (2018), Journal of Financial Economics -- HIGH threat, Channel 2
- Dugast and Foucault (2025), Journal of Finance -- HIGH threat, Channel 2

**Differentiator from Dugast-Foucault (2018, JFE):** Their mechanism is a speed-precision tradeoff for a single data source over time (temporal dimension): agents choose between fast-imprecise and slow-precise signals. The project's mechanism operates in the cross-sectional dimension: when N agents share a signal with pairwise correlation rho, the effective information content collapses even though each individual signal is precise. The cross-sectional information diversity collapse through the Grossman-Stiglitz framework with correlated AI signals is absent from Dugast-Foucault.

**Differentiator from Dugast-Foucault (2025, JF):** Their mechanism concerns search intensity and data mining thresholds. No Grossman-Stiglitz information aggregation, no FPE/RPE distinction, no cross-sectional signal correlation structure.

**Coverage gap filled:** Gap 2.1 (no paper extends GS with two information types differentiated by correlation); Gap 2.2 (Holden-Subrahmanyam competition + Goldstein-Yang complementarities interaction not formalised); Gap 2.3 (FPE/RPE distinction under AI not modelled).

**Risk flag for Literature Guardian M3:** Verify that no paper extends Grossman-Stiglitz (1980) with cross-sectional signal correlation from AI or a common technology source. Specifically search for: (1) any GS extension with correlated signals where the correlation is driven by a common technology, (2) any paper that derives the non-monotonicity of RPE in AI adoption or data technology, (3) recent working papers by Dugast, Foucault, or co-authors that add cross-sectional correlation to their framework.

---

## Claim 3: N_eff(rho) Liquidity Fragility Index with rho** Threshold (Channel 3)

**Formal result:** Proposition 3: The effective number of independent liquidity providers N_eff(rho) = N / (1 + (N-1)*rho) is decreasing and convex in rho. There exists a threshold rho** above which no interior market-making equilibrium with finite spreads exists.

**Threat map entries to differentiate from:**
- Cespa and Vives (forthcoming), American Economic Review -- MODERATE threat, Channel 3
- Colliard, Foucault, and Lovo (2025), Review of Financial Studies -- MODERATE threat, Channel 3
- Greenwood and Thesmar (2011), Journal of Financial Economics -- MODERATE threat, Channel 3

**Differentiator from Cespa-Vives (forthcoming, AER):** Their liquidity fragility mechanism operates through market opacity and hedger behaviour, not through algorithmic similarity. No rho parameterisation, no N_eff formula, no connection to AI model homogeneity.

**Differentiator from Colliard-Foucault-Lovo (2025, RFS):** Their mechanism concerns a single algorithmic market maker's RL-based pricing dynamics in a Glosten-Milgrom framework. No cross-sectional correlation among multiple market makers, no N_eff formula, no simultaneous withdrawal mechanism.

**Differentiator from Greenwood-Thesmar (2011, JFE):** They measure stock fragility as covariance of mutual fund flow shocks. N_eff(rho) is an analogue grounded in algorithmic similarity among market makers, not demand shock correlation from fund flows. No formal market-making equilibrium model.

**Coverage gap filled:** Gap 3.1 (no N_eff formula for AI market makers); Gap 3.2 (no rho** no-equilibrium threshold); Gap 3.3 (convexity of spread in rho not established).

**Risk flag for Literature Guardian M3:** Verify that no paper derives an effective-number-of-independent-providers formula (N_eff or equivalent) for correlated algorithmic market makers. Specifically search for: (1) any market microstructure paper with N_eff or effective diversity measures for market makers, (2) any paper deriving a no-equilibrium threshold for market making driven by algorithmic correlation, (3) recent working papers on correlated algorithmic liquidity provision or AI-driven market-maker withdrawal.

---

## Claim 4: Fixed-Point Amplification Loop with Bifurcation Result (Centrepiece)

**Formal result:** Proposition 4 (Amplification Bifurcation): The joint three-channel system admits a fixed-point equilibrium in (rho_eff, theta*, N_eff) by Brouwer's fixed-point theorem on the compact convex set K = [0,1] x [theta_L, theta_H] x [1, N]. The bifurcation threshold rho* of the integrated system is strictly below the minimum of the individual channel thresholds: rho* < min(rho_1*, rho_2*, rho_3*).

**Threat map entries to differentiate from:**
- Danielsson and Uthemann (2025), Journal of Financial Stability -- HIGH threat, Channel 1 / MODERATE threat, Amplification Loop
- Danielsson, Macrae, and Uthemann (2022), Journal of Banking and Finance -- MODERATE threat, Amplification Loop
- Dou, Goldstein, and Ji (2025a), NBER Working Paper 34054 -- MODERATE threat, Amplification Loop
- Dou, Goldstein, and Ji (2025b), SSRN Working Paper 5763222 -- MODERATE threat, Amplification Loop
- Goldstein, Huang, and Yang (2025), Annual Review of Financial Economics -- LOW threat, Amplification Loop

**Differentiator from Danielsson-Uthemann (2025, JFS):** Their formal model covers only the coordination/run channel via mu (AI fraction). Despite discussing information processing, common data, and speed qualitatively, they do not model information acquisition collapse, market-making fragility, N_eff, or the fixed-point interaction across channels. The project delivers the fixed-point in (rho_eff, theta*, N_eff) across all three channels with rho as the unifying primitive.

**Differentiator from Danielsson-Macrae-Uthemann (2022, JBF):** Their paper is entirely qualitative/narrative. The project provides the formal equilibrium characterisation of the multi-channel mechanism they describe.

**Differentiator from Dou-Goldstein-Ji (2025a, NBER WP):** Their mechanism is algorithmic collusion via reinforcement learning (emergent coordination through repeated strategic interaction). No information-theoretic signal correlation, no global games, no Grossman-Stiglitz information acquisition, no N_eff. The AI agents are strategic oligopolists, not price-taking agents with correlated signals.

**Differentiator from Dou-Goldstein-Ji (2025b, SSRN):** Their mechanism is intertemporal collusion via planning-capable RL agents. The fragility arises from AI planning capability (looking ahead), not from signal correlation (looking at the same data). No three-channel fixed-point.

**Differentiator from Goldstein-Huang-Yang (2025, ARFE):** Survey paper organising existing knowledge on market fragility. Does not model AI-specific mechanisms or the rho-driven three-channel fixed-point.

**Coverage gap filled:** Gap 4.1 (no fixed-point in (rho_eff, theta*, N_eff)); Gap 4.2 (joint rho* < min of individual thresholds not established); Gap 4.3 (safety illusion from moderate correlation not shown formally).

**Risk flag for Literature Guardian M3:** This is the paper's centrepiece claim. Verify with high confidence that no paper models a multi-channel fixed-point interaction linking coordination failure, information acquisition, and market liquidity through a common signal correlation parameterisation. Specifically search for: (1) any multi-channel financial fragility model with a fixed-point in three or more state variables, (2) any paper showing that a compound fragility threshold is below individual channel thresholds (amplification / super-additivity result), (3) any 2025-2026 working papers by Danielsson, Uthemann, Dou, Goldstein, Ji, or co-authors that extend their models toward multi-channel integration, (4) any paper applying Brouwer's fixed-point theorem to a multi-channel financial fragility system.

---

## Claim 5: Endogenous rho via Prisoner's Dilemma in AI Adoption (Extension)

**Formal result:** Proposition 5: In the AI adoption game, each agent's private incentive to adopt the dominant AI model exceeds the social cost of reduced signal diversity, driving the competitive equilibrium rho_NE above the social optimum rho_SO. The competitive equilibrium rho_NE exceeds the fragility threshold rho*, creating a fragility externality. A diversity mandate that bounds rho below rho* restores efficiency.

**Threat map entries to differentiate from:**
- No HIGH or MODERATE threat paper identified for this specific claim.

**Differentiator:** No existing paper models endogenous rho (AI output homogeneity) via a prisoner's dilemma in competitive AI adoption in financial markets. The closest related work is Calvano et al. (2020, AER), which studies algorithmic collusion in product pricing, but in a non-financial context with a different mechanism (RL-based tacit collusion vs. information-theoretic adoption externality).

**Coverage gap filled:** No specific gap number in literature_constraints.md; the Literature Guardian confirmed in Iteration 1 that no competing paper models endogenous rho via competitive AI adoption.

**Risk flag for Literature Guardian M3:** Verify that no paper models competitive AI adoption as a prisoner's dilemma driving signal correlation above a fragility threshold in financial markets. Specifically search for: (1) AI adoption externality models in finance, (2) model monoculture or technology homogeneity as a competitive outcome in financial markets, (3) diversity mandate / regulation models for AI in finance.
