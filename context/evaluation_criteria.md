# Evaluation Criteria — Research Plan Rubric

> **Mandatory evaluator instruction:**
> Every score must be justified with concrete reasoning that references
> specific elements of the research plan. Scores without justification
> are invalid. When in doubt, score lower — false passes are more
> costly than false revisions in this pipeline.

---

## Purpose

This rubric defines the evaluation logic used by the Research Evaluator to gate research plans. It is not a writing quality rubric. It evaluates **research viability**: whether a plan, if executed, would produce a novel, feasible, and publishable result at the target standard (top-5 journal in the relevant field).

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

**What is being assessed:** Whether the proposed contributions are genuinely new relative to the threat papers in `context/threat_map.md` and the prior art listed in `context/research_context.md`. A contribution is novel only if no existing paper shares its **formal mechanism** — surface-level topic overlap is not sufficient to classify a contribution as redundant.

**Checks:**
- Does each contribution have a precise mechanism-level differentiator from the threat map?
- Are differentiators stated in terms of formal objects (equilibrium conditions, comparative statics, model primitives) rather than vague topic-level distinctions?
- Is the paper's integrating contribution (if any) wholly novel?

| Score | Standard |
|-------|----------|
| 5 | All contributions clearly differentiated at the mechanism level; integrating contribution is wholly novel; differentiators are precise and verifiable |
| 4 | All contributions differentiated; one differentiator is less sharp but still defensible at a seminar |
| 3 | Core contributions differentiated but one component has a close threat paper that is not yet fully addressed |
| 2 | One or more contributions substantially overlap with existing work at the mechanism level; differentiators are vague or asserted without evidence |
| 1 | A published paper already derives the same formal mechanism; the plan does not acknowledge or address this |

---

### 2. Mechanism Clarity

**What is being assessed:** Whether the core economic mechanism is precisely defined with clear causal logic. The plan must specify the unifying primitive, how it activates each channel or component of the model, and how the components interact (if applicable).

**Check:** Can an informed reader trace the causal path from a change in the key primitive to a change in the equilibrium outcome in each component? Is the direction and mechanism of each inter-component link stated explicitly?

| Score | Standard |
|-------|----------|
| 5 | Key primitive defined; all model components specified with causal logic; interaction structure stated with equilibrium objects |
| 4 | Key primitive defined; components specified; one interaction link is stated informally but is logically sound |
| 3 | Key primitive defined; components present but one component's mechanism is underspecified or not yet connected to the interaction structure |
| 2 | Mechanism is described verbally without formal objects; it is unclear what an equilibrium looks like or how the primitive maps to outcomes |
| 1 | No coherent mechanism stated; the paper is a collection of intuitions without a unifying formal structure |

---

### 3. Theoretical Feasibility

**What is being assessed:** Whether the proposed model can be derived and solved within the stated scope constraints (as defined in `research_context.md`). A plan is infeasible if it requires results that cannot be obtained analytically within these constraints.

**Scope constraints from `research_context.md` (treat as binding):**
- Read the scope constraints section of the research context and treat all stated constraints as deliberate design choices.

**Check:** Are equilibrium conditions well-posed? Is the model tractable enough to yield clean comparative statics in the key primitive? Does combining multiple components simultaneously prevent analytic results?

| Score | Standard |
|-------|----------|
| 5 | Each component is solvable as a standalone model; integration is well-defined; comparative statics in the key primitive are tractable |
| 4 | Each component is solvable; integration is plausible but may require an additional simplifying assumption that is not yet stated |
| 3 | Components are solvable separately; integration approach is sketched but not yet specified; some risk of intractability |
| 2 | One component has an unclear equilibrium definition or requires a framework beyond the stated scope constraints |
| 1 | The proposed model cannot be solved within the stated constraints; equilibrium existence is in doubt for at least one component |

---

### 4. Literature Positioning

**What is being assessed:** Whether the plan correctly engages the foundational papers and differentiates from the closest threat papers. Engagement means citing specific results, propositions, or theorems — not just naming papers.

**Checks:**
- Are foundational papers (as identified in `research_context.md`) named and engaged with specific results?
- Are threat papers (from `threat_map.md`) addressed with precise mechanism-level differentiators?
- Is each contribution framed relative to the relevant literature strand?

| Score | Standard |
|-------|----------|
| 5 | All foundational papers engaged with specific results; threat papers addressed with precise differentiators; contribution framed relative to each relevant literature |
| 4 | Foundational papers named with specific results; one threat paper addressed only at the topic level rather than the mechanism level |
| 3 | Most foundational papers present; one foundational paper missing or cited only by name without engaging its result; differentiators for threat papers partially stated |
| 2 | Key foundational papers missing or engaged only superficially; differentiators from threat papers absent or asserted without reasoning |
| 1 | Literature positioning absent; contributions are not framed relative to any prior work |

---

### 5. Expected Contribution

**What is being assessed:** Whether, if executed, the paper would make a contribution at the level appropriate for the target venue. A contribution must be stateable as a single proposition or formal result — not a directional claim.

**Acceptable contribution forms:**
- A characterisation of an equilibrium object and its comparative statics
- A formal threshold or boundary condition for equilibrium existence
- A bifurcation or phase-transition result in the interaction of model components
- A welfare result distinguishing distinct equilibrium regimes

**Not acceptable:** Directional claims without formal content (e.g., "X increases Y" or "Z reduces market quality" without specifying the formal mechanism).

| Score | Standard |
|-------|----------|
| 5 | Each contribution stated as a formal result; integrating contribution is the centrepiece; results would be publishable at the target venue |
| 4 | Contributions stated as formal results for at least two components; integrating contribution present but not yet fully characterised |
| 3 | Some contributions stated formally; others still at the verbal level; the integrating contribution is mentioned but underspecified |
| 2 | Contributions are directional claims; no formal propositions identified; it is unclear what the paper would prove |
| 1 | No distinct contribution identifiable; the plan is a description of related work and a research agenda rather than a set of results |

---

### 6. Testability

**What is being assessed:** Whether the model's predictions can be tested, calibrated, or mapped to observable data. If the project includes an empirical component, assess whether it connects to the theory. If the empirical section is motivating rather than causal, this is a deliberate scope choice, not a weakness.

**Check:** Do the theory's comparative statics produce predictions that the empirical design can speak to? Is the proxy for the key primitive credible? Does the empirical section connect to the theory or float independently?

| Score | Standard |
|-------|----------|
| 5 | Theory produces at least two clean predictions mapped to observable proxies; empirical design speaks directly to these predictions; connection between theory and empirics is explicit |
| 4 | Theory produces testable predictions; empirical design is credible; one connection between a theoretical prediction and the empirical test is informal |
| 3 | Empirical section present and broadly connected to theory; the proxy for the key primitive is not fully justified; or only one component's predictions are tested |
| 2 | Empirical section appears disconnected from the theoretical mechanism; proxy is unclear; or the empirical design does not speak to the theory's predictions |
| 1 | No empirical section; or empirical design is fundamentally misaligned with the theoretical mechanism |

---

### 7. Scope Calibration

**What is being assessed:** Whether the plan is realistically achievable within the stated constraints. The question is whether the proposed scope is feasible as a single paper.

**Check:** Are the phases ordered so that each produces a stand-alone result? Could the paper be submitted with fewer components if time runs short? Is the plan trying to solve problems that fall outside the stated scope?

| Score | Standard |
|-------|----------|
| 5 | Each phase produces a self-contained result; extensions are clearly labelled as optional; the core paper is achievable |
| 4 | Core paper is achievable; one extension may be difficult to execute fully but is not on the critical path |
| 3 | Core paper is achievable but extensions are on the critical path; some risk that complexity prevents clean results in the integrating contribution |
| 2 | The plan requires results that are out of scope or combines too many mechanisms without a clear simplification strategy |
| 1 | The plan is unfeasibly ambitious; it could not be executed as a single paper at PhD standard within any reasonable time horizon |

---

### 8. Expository Economy

**What is being assessed:** Whether every paragraph earns its place. Could a section be cut by 30% without losing content?

**Risks to check:**
- Model sections with multiple components are prone to repeating the setup for each component.
- The literature review should stay within its target word count; exceeding it signals poor discipline.
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
   - "Differentiate contribution X from [threat paper] by showing that the proposed parameterisation produces a qualitatively different equilibrium region — specifically, that [stated condition] generates an outcome absent from their framework."
   - "Specify the fixed-point equation for the interaction structure and state the condition under which it bifurcates."
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

- The target venue is defined in `research_context.md`. Calibrate all scores to that standard, not a working paper or conference standard.
- The scope constraints in `research_context.md` are **deliberate design choices**, not weaknesses. Do not penalise the plan for constraints that were intentionally adopted.
- The integrating contribution (if any) is the paper's **non-negotiable core contribution**. A plan that does not clearly specify how it will be characterised cannot score above 3 on Expected Contribution.
- If the threat map has not been populated (`context/threat_map.md` is empty), the Novelty score cannot exceed 3. Flag this explicitly.
