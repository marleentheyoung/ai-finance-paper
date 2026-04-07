# Task Queue

---

## Active Tasks

### T5 -- Theory Builder: Extension (Phase 5)

- **Responsible agent:** Theory Builder
- **Input files:** context/research_plan_final.md (Contribution 5), context/model_equations.md (Amplification Loop section)
- **Output files:** context/model_equations.md (Extension section)
- **Blocking reason:** Was blocked by T4 (now completed); moved to Active
- **Deliverables:**
  - Proposition 5: In the AI adoption game, the Nash equilibrium rho_NE exceeds rho* (the fragility threshold), while the social optimum rho_SO < rho*
  - Characterisation of adoption game payoffs: private benefit of adopting the dominant model vs. social cost of reduced signal diversity
  - Diversity mandate: regulatory bound on rho that restores efficiency; characterisation of the optimal bound

### T6 -- Model Verifier: Verification (Phase 6)

- **Responsible agent:** Model Verifier
- **Input files:** context/model_equations.md (all sections)
- **Output files:** context/verification_report.md
- **Blocking reason:** Blocked by T5 (requires all propositions and derivations to be complete)
- **Deliverables:**
  - Verification of all five propositions: check equilibrium derivations, sign conditions on comparative statics, boundary conditions
  - Verification of fixed-point existence proof: check that T maps K into K, that continuity holds for all component mappings, that Brouwer conditions are satisfied
  - Verification of bifurcation proof: check Jacobian computation, spectral radius argument, inequality rho* < min(rho_i*)
  - Verification of uniqueness argument (if present) or characterisation of multiplicity
  - Flag any errors, gaps in arguments, or unstated assumptions that must be addressed before paper writing

### T7 -- Empirical Agent: Empirical Motivation (Phase 7)

- **Responsible agent:** Empirical Agent
- **Input files:** context/research_plan_final.md (Empirical Motivation in Phases, Open Question 7), context/model_equations.md (Channels 1-3 and Amplification Loop sections for theoretical predictions)
- **Output files:** code/empirical_motivation.py, context/empirical_notes.md
- **Blocking reason:** Blocked by T4 (requires theoretical predictions from the amplification loop to map to empirical tests)
- **Deliverables:**
  - DiD design specification: treatment (high-AI-exposure stocks) vs. control (low-exposure stocks); event date: November 30, 2022 (ChatGPT release)
  - Construction of rho proxy 1: 13F portfolio correlation (pairwise correlation of institutional holdings changes around AI adoption)
  - Construction of rho proxy 2: I/B/E/S forecast revision correlation (pairwise correlation of analyst forecast revisions)
  - Formal mapping from portfolio overlap / forecast correlation to signal correlation rho (Open Question 7)
  - Reduced-form evidence: regression specifications testing the model's comparative statics predictions
  - Justification for ChatGPT release as relevant for institutional financial decision-making (Execution Risk 3)
  - Python code implementing all data construction and analysis

### T8 -- Paper Writer: Manuscript Draft (Phase 8)

- **Responsible agent:** Paper Writer
- **Input files:** context/research_plan_final.md, context/paper_structure.md, context/model_equations.md (all sections), context/verification_report.md, context/empirical_notes.md
- **Output files:** paper/main.tex
- **Blocking reason:** Blocked by T6 + T7 (requires verified model and empirical results)
- **Deliverables:**
  - Complete LaTeX manuscript following the 10-section structure in paper_structure.md
  - All five propositions stated formally with proofs or proof sketches
  - Literature review engaging all threat map papers with mechanism-level differentiators
  - Empirical motivation section integrating reduced-form evidence
  - Conclusion with policy implications and future work

---

## Completed Tasks

### TC1 -- Literature Guardian Mode 1: Quick Scan
- **Output produced:** context/threat_map_v1.md, context/threat_map.md (initial version), context/literature_constraints.md (initial version)
- **Iteration completed:** Pre-loop (Iteration 0)

### TC2 -- Research Director Mode 1: Initial Research Plan
- **Output produced:** context/research_plan.md (initial version)
- **Iteration completed:** Pre-loop (Iteration 0)

### TC3 -- Literature Guardian Mode 2: Targeted Check (Iteration 1)
- **Output produced:** context/threat_map.md (Iteration 1 update), context/literature_constraints.md (Iteration 1 update)
- **Iteration completed:** Loop Iteration 1

### TC4 -- Research Evaluator Mode 1: Plan Evaluation (Iteration 1)
- **Output produced:** context/evaluator_feedback.md (Iteration 1), context/loop_state.md (Iteration 1)
- **Iteration completed:** Loop Iteration 1

### TC5 -- Research Director Mode 2: Plan Revision (Iteration 2)
- **Output produced:** context/research_plan.md (Iteration 1 changelog: Danielsson-Uthemann engagement, fixed-point specification)
- **Iteration completed:** Loop Iteration 2

### TC6 -- Literature Guardian Mode 2: Targeted Check (Iteration 2)
- **Output produced:** context/threat_map.md (Iteration 2 update), context/literature_constraints.md (Iteration 2 update)
- **Iteration completed:** Loop Iteration 2

### TC7 -- Research Evaluator Mode 1: Plan Evaluation (Iteration 2)
- **Output produced:** context/evaluator_feedback.md (Iteration 2), context/loop_state.md (Iteration 2, ACCEPT)
- **Iteration completed:** Loop Iteration 2

### TC8 -- Research Director Mode 3: Final Research Program
- **Output produced:** context/research_plan_final.md, context/paper_structure.md, context/task_queue.md, context/novelty_claims.md
- **Iteration completed:** Post-loop (Phase 3)

### TC9 -- Theory Builder: Channel 1 Model (T1, Phase 1)
- **Output produced:** context/model_equations.md (Channel 1 section: Propositions 1a, 1b, 1c; uniqueness boundary rho_1* = 1/(1+alpha_SC^2); non-monotonicity of theta*(rho); Danielsson-Uthemann comparison case; Szkup-Trevino resolution; Angeletos-Pavan welfare result)
- **Completed:** 2026-03-10

### TC10 -- Theory Builder: Channel 2 Model (T2, Phase 2)
- **Output produced:** context/model_equations.md (Channel 2 section: Propositions 2a, 2b, Corollary 2c; information collapse result; GS indifference condition with crisis risk; FPE/RPE decomposition; g_2 functional form for T4; Goldstein-Yang complementarity breakdown)
- **Completed:** 2026-03-10

### TC11 -- Theory Builder: Channel 3 Model (T3, Phase 3)
- **Output produced:** context/model_equations.md (Channel 3 section: Propositions 3a, 3b, 3c, Lemma 3d; N_eff formula; equilibrium spread; rho** no-equilibrium threshold; DSZ limiting case; g_3 functional form for T4)
- **Completed:** 2026-03-10

### TC12 -- Theory Builder: Amplification Loop (T4, Phase 4)
- **Output produced:** context/model_equations.md (Amplification Loop section: Proposition 4a fixed-point existence via Brouwer; Proposition 4b amplification bifurcation rho* < min(rho_1*, rho_2*, rho_3*); Proposition 4c local uniqueness below rho*; Corollary 4d safety illusion; g_1 functional form justified; composite operator T defined; Jacobian DT computed with spectral radius lambda_1 = w*m*(h*|a| - b); positive feedback loop characterised; comparative statics of rho* in model parameters; contraction mapping attempt for uniqueness -- local uniqueness established, global uniqueness not)
- **Completed:** 2026-03-10
