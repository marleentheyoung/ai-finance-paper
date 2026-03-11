# Evaluation Criteria — Research Plan Rubric

> **Mandatory evaluator instruction:**
> Every score must be justified with concrete reasoning that references
> specific elements of the research plan. Scores without justification
> are invalid. When in doubt, score lower — false passes are more
> costly than false revisions in this pipeline.

---

## Purpose

This rubric defines the evaluation logic used by the Research Evaluator to gate research plans. It is not a writing quality rubric. It evaluates **research viability**: whether a plan, if executed, would produce a novel, feasible, and publishable result at the target standard (JF / RFS / Econometrica).

**Decision function:**

```
Input:  research_plan.md (+ threat_map.md + research_context.md)
Output: ACCEPT / REVISE / REJECT
```

---

## Scoring Scale

All criteria use a 1–5 integer scale. No half points.

| Score | Label | Interpretation |
|-------|-------|----------------|
| 5 | Exceptional | No revision needed on this dimension |
| 4 | Strong | Minor issues only; plan can proceed |
| 3 | Adequate | Meaningful but addressable weaknesses; must be noted |
| 2 | Weak | Serious concerns that must be resolved before proceeding |
| 1 | Failing | Fundamental problem; plan cannot proceed on this dimension |

---

## The Eight Criteria

### 1. Novelty

**What is being assessed:** Whether the proposed contributions are genuinely new relative to the threat papers in `context/threat_map.md` and the prior art listed in `context/research_context.md` §5. A contribution is novel only if no existing paper shares its **formal mechanism** — surface-level topic overlap is not sufficient to classify a contribution as redundant.

**Project-specific threats to check:**
- Channel 1 (coordination failure): Danielsson–Uthemann and related global-games papers. Differentiator must be the ρ-parameterisation of the signal structure and its effect on θ*(ρ).
- Channel 2 (information acquisition): Any paper extending Grossman–Stiglitz (1980) with correlated signals. Differentiator must be the simultaneous collapse of the FPE-vs-RPE distinction and the near-zero cost AI case.
- Channel 3 (market making): Papers on correlated algorithmic or HFT liquidity withdrawal. Differentiator must be the N_eff(ρ) fragility index and the no-equilibrium threshold ρ**.
- Amplification loop: The joint fixed-point characterisation in (ρ_eff, θ*, N_eff) is the primary novelty defence. No paper is known to characterise this interaction.

| Score | Standard |
|-------|----------|
| 5 | All contributions clearly differentiated at the mechanism level; amplification loop is wholly novel; differentiators are precise and verifiable |
| 4 | All contributions differentiated; one differentiator is less sharp but still defensible at a seminar |
| 3 | Core contributions differentiated but one channel has a close threat paper that is not yet fully addressed |
| 2 | One or more contributions substantially overlap with existing work at the mechanism level; differentiators are vague or asserted without evidence |
| 1 | A published paper already derives the same formal mechanism; the plan does not acknowledge or address this |

---

### 2. Mechanism Clarity

**What is being assessed:** Whether the core economic mechanism is precisely defined with clear causal logic. The project's unifying primitive is ρ-parameterised signal homogeneity: εᵢ = √ρ · η + √(1−ρ) · ξᵢ. The plan must specify how ρ activates each of the three channels and how the channels interact in the amplification loop.

**Check:** Can an informed reader trace the causal path from a change in ρ to a change in the equilibrium outcome in each channel? Is the direction and mechanism of each channel-to-channel link in the amplification loop stated explicitly?

| Score | Standard |
|-------|----------|
| 5 | ρ primitive defined; all three channels specified with causal logic; amplification loop links stated with equilibrium objects (θ*, N_eff, informed fraction) |
| 4 | ρ primitive defined; channels specified; one amplification link is stated informally but is logically sound |
| 3 | ρ primitive defined; channels present but one channel's mechanism is underspecified or not yet connected to the amplification loop |
| 2 | Mechanism is described verbally without formal objects; it is unclear what an equilibrium looks like or how ρ maps to outcomes |
| 1 | No coherent mechanism stated; the paper is a collection of intuitions without a unifying formal structure |

---

### 3. Theoretical Feasibility

**What is being assessed:** Whether the proposed model can be derived and solved within the stated scope constraints (static or two-period framework, ρ exogenous in the baseline, no full dynamic model). A plan is infeasible if it requires results that cannot be obtained analytically within these constraints.

**Scope constraints from `research_context.md` §6 (treat as binding):**
- ρ is exogenous in the main model
- Static or two-period model only
- No full dynamic model
- Endogenous ρ is restricted to the prisoner's dilemma extension

**Check:** Are equilibrium conditions well-posed? Is the model tractable enough to yield clean comparative statics in ρ? Does combining three channels simultaneously prevent analytic results?

| Score | Standard |
|-------|----------|
| 5 | Each channel is solvable as a standalone model; integration via fixed-point is well-defined; comparative statics in ρ are tractable |
| 4 | Each channel is solvable; integration is plausible but may require an additional simplifying assumption that is not yet stated |
| 3 | Channels are solvable separately; integration approach is sketched but not yet specified; some risk of intractability |
| 2 | One channel has an unclear equilibrium definition or requires a dynamic model to solve; plan does not respect the static/two-period constraint |
| 1 | The proposed model cannot be solved within the stated constraints; equilibrium existence is in doubt for at least one channel |

---

### 4. Literature Positioning

**What is being assessed:** Whether the plan correctly engages the foundational papers and differentiates from the closest threat papers. Engagement means citing specific results, propositions, or theorems — not just naming papers.

**Foundational papers that must be named and engaged:**
- Morris–Shin (1998 AER, 2002 AER): threshold equilibrium and uniqueness conditions
- Goldstein–Pauzner (2005 JF): bank-run framework being extended
- Grossman–Stiglitz (1980 AER): information acquisition paradox being extended
- Glosten–Milgrom (1985 JFE) and Kyle (1985 Econometrica): market-making foundations
- Angeletos–Pavan (2007 Econometrica): welfare framework for public information

| Score | Standard |
|-------|----------|
| 5 | All foundational papers engaged with specific results; threat papers addressed with precise differentiators; contribution framed relative to each relevant literature |
| 4 | Foundational papers named with specific results; one threat paper addressed only at the topic level rather than the mechanism level |
| 3 | Most foundational papers present; one foundational paper missing or cited only by name without engaging its result; differentiators for threat papers partially stated |
| 2 | Key foundational papers missing or engaged only superficially; differentiators from threat papers absent or asserted without reasoning |
| 1 | Literature positioning absent; contributions are not framed relative to any prior work |

---

### 5. Expected Contribution

**What is being assessed:** Whether, if executed, the paper would make a contribution at the level appropriate for the target venue (JF / RFS / Econometrica). A contribution must be stateable as a single proposition or formal result — not a directional claim.

**Acceptable contribution forms:**
- A characterisation of θ*(ρ) and its non-monotone comparative statics
- A formal threshold ρ** above which no market-making equilibrium with finite spreads exists
- The bifurcation of the joint fixed-point in (ρ_eff, θ*, N_eff)
- A welfare result distinguishing FPE and RPE degradation as a function of ρ

**Not acceptable:** "AI increases systemic risk" or "homogeneous signals reduce market quality" — these are intuitions, not contributions.

| Score | Standard |
|-------|----------|
| 5 | Each contribution stated as a formal result; amplification loop contribution is the centrepiece; results would be publishable at the target venue |
| 4 | Contributions stated as formal results for at least two channels; amplification loop contribution present but not yet fully characterised |
| 3 | Some contributions stated formally; others still at the verbal level; the amplification loop contribution is mentioned but underspecified |
| 2 | Contributions are directional claims; no formal propositions identified; it is unclear what the paper would prove |
| 1 | No distinct contribution identifiable; the plan is a description of related work and a research agenda rather than a set of results |

---

### 6. Testability

**What is being assessed:** Whether the model's predictions can be tested, calibrated, or mapped to observable data. The project specifies a DiD empirical motivation section using the ChatGPT release (November 2022) as an AI adoption shock, with ρ proxied via 13F portfolio correlation and I/B/E/S forecast revision correlation. The empirical section is motivating, not causal — this is a deliberate scope choice, not a weakness.

**Check:** Do the theory's comparative statics in ρ produce predictions that the DiD design can speak to? Is the proxy for ρ credible? Does the empirical section connect to the theory or float independently?

| Score | Standard |
|-------|----------|
| 5 | Theory produces at least two clean predictions mapped to observable proxies for ρ; DiD design speaks directly to these predictions; connection between theory and empirics is explicit |
| 4 | Theory produces testable predictions; DiD design is credible; one connection between a theoretical prediction and the empirical test is informal |
| 3 | Empirical section present and broadly connected to theory; the ρ proxy is not fully justified; or only one channel's predictions are tested |
| 2 | Empirical section appears disconnected from the theoretical mechanism; ρ proxy is unclear; or the DiD design does not speak to the theory's predictions |
| 1 | No empirical section; or empirical design is fundamentally misaligned with the theoretical mechanism |

---

### 7. Scope Calibration

**What is being assessed:** Whether the plan is realistically achievable within the stated constraints. The project proposes three channels, an amplification loop, extensions (endogenous ρ, diversity mandates), and an empirical section — in a static or two-period model. This is ambitious; the question is whether it is feasible as a single paper.

**Check:** Are the phases ordered so that each produces a stand-alone result? Could the paper be submitted with fewer components if time runs short? Is the plan trying to solve problems that fall outside the stated scope (§6)?

| Score | Standard |
|-------|----------|
| 5 | Each phase produces a self-contained result; extensions are clearly labelled as optional; the core paper (three channels + amplification loop) is achievable |
| 4 | Core paper is achievable; one extension may be difficult to execute fully but is not on the critical path |
| 3 | Core paper is achievable but extensions are on the critical path; some risk that complexity prevents clean results in the amplification loop |
| 2 | The plan requires results that are out of scope (dynamic model, endogenous ρ in the baseline) or combines too many mechanisms without a clear simplification strategy |
| 1 | The plan is unfeasibly ambitious; it could not be executed as a single paper at PhD standard within any reasonable time horizon |

---

### 8. Expository Economy

**What is being assessed:** Whether every paragraph earns its place. Could a section be cut by 30% without losing content?

**Project-specific risks:**
- The model section with three channels and an amplification loop is prone to repeating the setup for each channel.
- The literature review is scoped at 2,500–3,500 words; exceeding this signals poor discipline.
- The introduction must state contributions as results, not as topic previews — topic previews are a verbosity signal.

| Score | Standard |
|-------|----------|
| 5 | Every sentence advances the argument. No redundancy. A reader can absorb the paper in one sitting. |
| 4 | Tight overall, but one or two passages could be compressed without loss. |
| 3 | Several sections are noticeably padded — hedging, setup repetition, or over-elaborate derivation walkthroughs. A referee would say "this paper is too long." |
| 2 | Multiple sections read like first drafts. The reader has to work to find the point. |
| 1 | The paper buries its contributions in prose. |

---

## Aggregation Rule

```
overall_score = min(novelty, mechanism_clarity, feasibility) * 0.6
              + mean(all_eight_scores) * 0.4
```

The first term ensures that a critical failure in any core dimension cannot be masked by overall strength. The second term rewards plans that are strong across all dimensions. Expository Economy is included in the mean but not the core floor — a verbose but correct paper is better than a concise but wrong one, but poor economy will still drag the overall score toward REVISE.

**Compute as follows:**
1. Record the eight individual scores.
2. Compute `core_floor = min(score_novelty, score_mechanism_clarity, score_feasibility)`.
3. Compute `mean_all = (sum of all eight scores) / 8`.
4. `overall_score = core_floor * 0.6 + mean_all * 0.4`.
5. Round to one decimal place.

---

## Decision Thresholds

| Overall score | Decision |
|---------------|----------|
| ≥ 4.0 | **ACCEPT** |
| 3.0 – 3.9 | **REVISE** |
| < 3.0 | **REJECT** |

### Hard Failure Conditions

Regardless of overall score, force **REJECT** if any of the following hold:

- Novelty ≤ 2
- Mechanism Clarity ≤ 2
- Theoretical Feasibility ≤ 2

**Rationale:** These three are the core floor dimensions in the aggregation formula. A score of 1 or 2 on any of them collapses the overall score regardless of strength elsewhere, and signals a problem fundamental enough that further iteration is pointless without addressing it first. Scope Calibration and other mean-component criteria can cause a REJECT through the formula itself if sufficiently low; they do not require a separate hard-failure rule.

State which hard failure condition was triggered in the evaluation output.

---

## Revision Directives

When the decision is **REVISE**, the evaluator must output:

1. The 1–2 dimensions with the lowest scores.
2. For each, a **specific and actionable** directive. Not "improve novelty" but, for example:
   - "Differentiate Channel 2 from Goldstein–Yang (2015) by showing that the ρ-parameterisation produces a qualitatively different equilibrium region — specifically, that the near-zero cost AI case generates an informational collapse that is absent from their multi-dimensional acquisition framework."
   - "Specify the fixed-point equation for the amplification loop in (ρ_eff, θ*, N_eff) and state the condition under which it bifurcates."
3. The score each directive must achieve for the plan to pass.

---

## Output Format

The evaluator's output must follow this exact structure:

```markdown
## Evaluation

| Criterion                | Score | Justification |
|--------------------------|-------|---------------|
| Novelty                  | X     | ...           |
| Mechanism clarity        | X     | ...           |
| Theoretical feasibility  | X     | ...           |
| Literature positioning   | X     | ...           |
| Expected contribution    | X     | ...           |
| Testability              | X     | ...           |
| Scope calibration        | X     | ...           |
| Expository economy       | X     | ...           |

**Core floor (min of novelty, mechanism clarity, feasibility):** X
**Mean (all eight):** X.X
**Overall score:** X.X
**Decision:** ACCEPT / REVISE / REJECT
**Hard failure triggered:** [None / state which condition]

### Revision directives (if REVISE or REJECT)
1. [Dimension]: [specific directive]. Target score: X.
2. [Dimension]: [specific directive]. Target score: X.

### Meta-check
In one sentence, state why a reader should care about this paper's result.
If you cannot write a compelling sentence, the plan needs revision regardless of numeric scores.
```

---

## Calibration Notes

- The target venue is **JF / RFS / Econometrica**. Calibrate all scores to that standard, not a working paper or conference standard.
- The scope constraints in `research_context.md` §6 are **deliberate design choices**, not weaknesses. Do not penalise the plan for being static, for treating ρ as exogenous in the baseline, or for not establishing causal identification in the empirical section.
- The amplification loop is the paper's **non-negotiable core contribution**. A plan that does not clearly specify how the joint fixed-point will be characterised cannot score above 3 on Expected Contribution.
- If the threat map has not been populated (`context/threat_map.md` is empty), the Novelty score cannot exceed 3. Flag this explicitly.
