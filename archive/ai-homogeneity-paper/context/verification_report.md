# Model Verification Report

## Date: 2026-03-10
## Input: context/model_equations.md (~2049 lines)
## Scope: Channels 1-3 and Amplification Loop (T1, T2, T3, T4). Extension T5 NOT verified.

---

## Status of Previously-Critical Issues

### Critical Issue 1: Proposition 1b Formula Mismatch -- RESOLVED

The previous report flagged that Proposition 1b stated `rho_1* = sqrt(2*pi) / (alpha_SC + sqrt(2*pi))` while the derivation established `rho_1* = 1 / (1 + alpha_SC^2)`.

**Current state:** The statement at line 353 now reads `rho_1* = 1 / (1 + alpha_SC^2)`. This matches the derivation at line 456 and the proof sketch at line 469. SymPy confirms: solving `alpha * sqrt(rho/(1-rho)) = 1` for rho yields `rho = 1/(1 + alpha^2)`. The old formula (sqrt(2pi)/(alpha+sqrt(2pi))) gives 0.715 at alpha=1, while the correct formula gives 0.500.

**Verdict: RESOLVED.** Statement and derivation are now internally consistent.

### Critical Issue 2: Proposition 1c Coefficient Discrepancy -- RESOLVED

The previous report flagged that the proposition used `alpha^2/(1-alpha^2)` while the derivation used `alpha^2/(1-alpha)^2`.

**Current state:** The statement at line 477 now reads `alpha_SC^2 / (1 - alpha_SC)^2`. Line 479 explains: "agents place weight alpha_SC/(1 - alpha_SC) on common information relative to the efficient benchmark, and the welfare loss is proportional to the square of this over-weighting." SymPy confirms: `(alpha/(1-alpha))^2 = alpha^2/(1-alpha)^2`. The statement and derivation are now consistent.

**Verdict: RESOLVED.** Statement and derivation now use the same coefficient.

---

## Structural Audit

**Overall: Improved from previous report. Minor issues remain.**

1. **Working notes still present.** The document retains multiple "Wait --" passages and self-correction sequences (lines 373, 377, 400, 406, 408, 1089, 1141). These are derivation scratchwork that should be removed before the Paper Writer uses the document.

2. **All propositions numbered and labelled:** Yes. T1: 1a, 1b, 1c. T2: 2a(i-iii), 2b(i-iii), 2c. T3: 3a, 3b, 3c, 3d. T4: 4a, 4b, 4c, 4d.

3. **Variables defined before use:** Yes, with normalisation convention clearly stated. Notation reference table at lines 1907-1975 is comprehensive.

4. **Open Questions section:** Present and thorough (lines 1979-2048), covering simplifying assumptions, Szkup-Trevino conditions, functional forms, and scope compliance.

5. **Notation consistency:** Consistent throughout. No variable name collisions or silent redefinitions.

---

## Proposition Verification Summary

| Proposition | Statement | Assumptions | Proof Logic | Direction | Verdict |
|-------------|-----------|-------------|-------------|-----------|---------|
| 1a (non-monotonicity) | OK | OK (sigma small) | OK (qualitative) | OK | CONDITIONALLY VERIFIED |
| 1b (uniqueness boundary) | OK (FIXED) | OK | OK (FIXED) | OK | VERIFIED |
| 1c (social cost) | OK (FIXED) | OK | OK | OK | CONDITIONALLY VERIFIED |
| 2a(i) (mu_I standalone) | OK | OK | OK | OK (increasing) | VERIFIED |
| 2a(ii) (mu_I with crisis) | OK | OK | OK | OK (decreasing) | VERIFIED |
| 2a(iii) (N_info) | OK | OK | OK | OK | VERIFIED |
| 2b(i) (FPE non-monotone) | OK | Needs c_AI spec | GAP | OK | CONDITIONALLY VERIFIED |
| 2b(ii) (RPE decreasing) | OK | c_P > 0 | OK | OK | CONDITIONALLY VERIFIED |
| 2b(iii) (FPE-RPE divergence) | OK | Follows from (i),(ii) | OK | OK | CONDITIONALLY VERIFIED |
| 2c (GY complementarity) | OK | OK | OK | OK | VERIFIED |
| 3a (N_eff) | OK | OK | OK | OK | VERIFIED |
| 3b (spread) | OK | OK | OK | OK | VERIFIED |
| 3c (rho** threshold) | OK | Parameter conditions | PARTIAL GAP | OK | CONDITIONALLY VERIFIED |
| 3d (DSZ limit) | OK | OK | OK (construction) | N/A | VERIFIED |
| 4a (existence) | OK | OK | OK (Brouwer) | N/A | VERIFIED |
| 4b (bifurcation) | OK | h->inf assertion | PARTIAL GAP | OK | CONDITIONALLY VERIFIED |
| 4c (local uniqueness) | OK | OK | OK (Banach) | N/A | VERIFIED |
| 4d (safety illusion) | OK | Follows from 4b | OK | N/A | VERIFIED (conditional on 4b) |

---

## Detailed Analysis: T3 Propositions (New)

### Proposition 3a: N_eff Characterisation

**Statement:** N_eff(rho) = N / (1 + (N-1)*rho) with properties (i)-(iv).

**SymPy verification:**
- (i) N_eff(0) = N, N_eff(1) = 1: VERIFIED algebraically.
- (ii) d(N_eff)/d(rho) = -N*(N-1)/(1+(N-1)*rho)^2 < 0: VERIFIED (formula and sign).
- (iii) d^2(N_eff)/d(rho)^2 = 2*N*(N-1)^2/(1+(N-1)*rho)^3 > 0: VERIFIED (formula and sign).
- (iv) N_eff(1/(N-1)) = N/2: VERIFIED.
- Numerical spot check (N=100, rho=0.1): N_eff = 9.17, consistent with document's "about 9.2."

**Verdict: VERIFIED.**

### Proposition 3b: Spread Monotonicity

**Statement:** s*(rho) = s_0*(1+(N-1)*rho)/N, with properties (i)-(iii).

**SymPy verification:**
- (i) d(s*)/d(rho) = s_0*(N-1)/N > 0: VERIFIED.
- (ii) d^2(s*)/d(rho)^2 = 0 (linear): VERIFIED. The baseline is linear in rho, not convex.
- (iii) For s_NL = s_0*((1+(N-1)*rho)/N)^beta: d^2(s_NL)/d(rho)^2 = s_0*beta*(beta-1)*((1+(N-1)*rho)/N)^(beta-2)*((N-1)/N)^2. Positive iff beta > 1: VERIFIED algebraically and numerically (beta=0.5 gives negative, beta=1 gives zero, beta=2 gives positive).
- Boundaries: s*(0) = s_0/N, s*(1) = s_0: VERIFIED.

**Note on convexity:** The research plan claims "the equilibrium bid-ask spread is convex in rho." The baseline specification is linear (d^2=0). Convexity requires beta > 1 in the nonlinear specification. The document correctly identifies this discrepancy and presents both cases. The Theory Builder should either adopt beta > 1 with economic justification or weaken the plan's convexity claim to monotonicity.

**Verdict: VERIFIED** (all mathematical claims as stated are correct; the convexity caveat is a framing issue, not a mathematical error).

### Proposition 3c: No-Equilibrium Threshold

**Statement:** There exists rho** in (0,1] where the participation constraint binds.

**SymPy verification of closed form:** The simplified formula rho** = (pi_0 / [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] - 1) / (N-1) is VERIFIED by solving Revenue(rho) = Cost(rho) + pi_0.

**Existence issue:** The proof sketch claims Cost(rho) is "unbounded as rho -> 1." In the stated linear specification with finite N, Cost(1) = gamma*sigma_V^2*kappa_inv*N, which is FINITE. Revenue(1) = Q*s_0/N, also FINITE. The unboundedness requires N -> infinity simultaneously with rho -> 1. For finite N, existence of rho** in (0,1) is a parameter condition: Q*s_0/N^2 > gamma*sigma_V^2*kappa_inv (positive margin) and the resulting rho** must be less than 1.

**Verdict: CONDITIONALLY VERIFIED.** The closed-form formula is algebraically correct. Existence of rho** in (0,1) requires explicit parameter conditions that are not structurally guaranteed by the model. The proof sketch's "unbounded" argument is imprecise for finite N.

### Lemma 3d: DSZ Limiting Case

**Statement:** At rho=1, N_eff=1 and the model reduces to DSZ.

**Verification:** N_eff(1) = N/N = 1 (SymPy confirms). This is a structural/definitional claim, correct by construction.

**Verdict: VERIFIED.**

### g_3 Formula (for T4 use)

**Statement:** g_3(mu_I, rho, N) = N / (1 + (N-1)*rho*(1-mu_I)^2).

**SymPy verification:**
- g_3(0, rho, N) = N/(1+(N-1)*rho) = standalone N_eff: VERIFIED.
- g_3(1, rho, N) = N (full independence): VERIFIED.
- d(g_3)/d(mu_I) = 2*N*(N-1)*rho*(1-mu_I) / (1+(N-1)*rho*(1-mu_I)^2)^2 > 0: VERIFIED.
- d(g_3)/d(rho) = -N*(N-1)*(1-mu_I)^2 / (1+(N-1)*rho*(1-mu_I)^2)^2 < 0: VERIFIED.

---

## Detailed Analysis: T4 Propositions (New)

### Proposition 4a: Fixed-Point Existence

**Statement:** T: K -> K is continuous and maps the compact convex set K into itself. By Brouwer's fixed-point theorem, T has at least one fixed-point.

**Verification:**
- (i) K is compact and convex (closed bounded rectangle in R^3): CORRECT by Heine-Borel.
- (ii) T maps K into K: Each component verified.
  - T_3 (N_eff') in [N/(1+(N-1)*rho), N] subset [1, N]: VERIFIED.
  - T_1 (rho_eff') in [rho, 1-(1-rho)/N] subset [rho, 1]: VERIFIED.
  - T_2 (theta*') in [theta_L, theta_H] by GP dominance regions: VERIFIED.
- (iii) T is continuous: Each component mapping (g_1, g_2, g_3, theta*) is continuous. The composition of continuous functions is continuous. The boundary treatment at rho_eff = rho_1* uses worst-case selection, which preserves continuity (limits exist by monotonicity).

**Verdict: VERIFIED.**

### Jacobian DT

**SymPy verification of eigenvalue structure:**
- The Jacobian has a zero third column (current N_eff does not enter updated state). VERIFIED.
- Determinant of the 2x2 upper-left submatrix is 0: VERIFIED by SymPy (det = 0).
- Eigenvalues: {0: multiplicity 2, w*m*(h*|a| - b): multiplicity 1}. VERIFIED by SymPy.
- Spectral radius = |w*m*(h*|a| - b)| = |[(1-rho)/N] * m * (h*|a| - b)|. VERIFIED.

**Sign structure of Jacobian entries:** All signs verified against economic logic. The positive feedback loop (rho_eff up -> theta* up -> mu_I down -> N_eff down -> rho_eff up) preserves the sign at each step. VERIFIED.

### Proposition 4b: Amplification Bifurcation

**Statement:** rho* < min(rho_1*, rho_2*, rho_3*).

**Verification of proof logic:**

Step 1 (individual channels stable in isolation): Correct by construction. Each channel in isolation has no feedback loop, so the uncoupled Jacobian has spectral radius 0.

Step 2 (cross-channel feedback creates positive spectral radius): The key claim is that h*|a| > b for rho_eff sufficiently close to rho_1*. This relies on h = d(theta*)/d(rho_eff) -> infinity as rho_eff -> rho_1*. The divergence is asserted based on the square-root singularity of the uniqueness condition, but not formally proved. Economically plausible: as rho_eff approaches the uniqueness boundary, the crisis threshold becomes infinitely sensitive to small changes in correlation. **PARTIAL GAP** (plausible but not proven).

Step 3 (strict inequality): The essential argument is that rho_eff* > rho at the fixed-point (because N_eff* < N when some agents use AI), so the system "sees" a higher effective correlation than the exogenous level. Therefore rho_eff*(rho*) = rho_1* at some rho* < rho_1*. SymPy verifies: rho_eff - rho = (1-rho)*(1 - N_eff/N) > 0 when N_eff < N. VERIFIED.

The extension to rho* < rho_2* and rho* < rho_3* uses the argument that the amplified effective parameters are "more adverse" than exogenous rho. This is qualitatively correct but the formal bound is not tight. **PARTIAL GAP**.

**Verdict: CONDITIONALLY VERIFIED.** The core mechanism (amplification makes rho_eff > rho, so the system bifurcates at lower exogenous rho) is correct and verified. Two partial gaps remain: (a) the divergence of h near rho_1* is asserted but not formally proved; (b) the strict inequality for rho_2* and rho_3* is argued but not given a tight bound.

### Proposition 4c: Local Uniqueness Below rho*

**Statement:** For rho < rho*, the interior fixed-point is locally unique.

**Verification:** Spectral radius < 1 implies T is a local contraction, so Banach fixed-point theorem gives local uniqueness. Standard result, correctly applied. The document correctly notes that global uniqueness is not established and corner fixed-points may co-exist.

**Verdict: VERIFIED.**

### Corollary 4d: Safety Illusion

**Statement:** For rho in (rho*, min(rho_i*)), each channel individually appears safe but the integrated system is fragile.

**Verification:** Follows directly from Proposition 4b. If rho* < min(rho_i*), the interval (rho*, min(rho_i*)) is non-empty, and for rho in this interval: rho < rho_i* for each i (individual safety) but rho > rho* (integrated fragility). VERIFIED.

**Verdict: VERIFIED** (conditional on Proposition 4b).

### Comparative Statics of rho*

| Claim | Verification | Status |
|-------|-------------|--------|
| d(rho*)/d(alpha_SC) < 0 | Correct: higher alpha_SC lowers rho_1* and steepens h | VERIFIED |
| d(rho*)/d(N) < 0 | Correct: more MMs amplify g_1 factor | VERIFIED (qualitative) |
| d(rho*)/d(c_P) > 0 | Problematic: higher c_P raises |a| (numerator), which strengthens the destabilising feedback. The document's intuition ("less responsive") is not obviously correct | FLAG |
| d(rho*)/d(lambda) < 0 | Correct: more AI agents amplify Ch1 and Ch3 | VERIFIED (qualitative) |
| rho* -> 0 as N -> inf | Correct via amplification: N_eff/N -> 0 for large N, so rho_eff -> 1 | VERIFIED |

**Note on c_P comparative static:** The document claims d(rho*)/d(c_P) > 0 with the intuition that "higher c_P makes agents less responsive to the crisis-probability signal." However, |a| = c_P / [(1-theta*)^2 * |dF/dmu_I|], so higher c_P directly increases |a| (stronger Ch1->Ch2 feedback), which would LOWER rho*. The equilibrium shift (lower mu_I* from higher c_P) changes |dF/dmu_I| as well, making the net effect ambiguous. The claimed sign may be incorrect or requires additional conditions.

---

## Computational Verification

Scripts written to: `code/verification/`

| Script | Propositions Checked | Status |
|--------|---------------------|--------|
| verify_critical_fixes.py | 1b (formula), 1c (coefficient) | Both RESOLVED |
| verify_channel1.py | 1a, 1b, 1c (from previous round) | Carried forward |
| verify_channel2.py | 2a, 2b, 2c (from previous round) | Carried forward |
| verify_channel3.py | 3a, 3b, 3c, 3d (from previous round) | Carried forward |
| verify_channel3_t3.py | 3a, 3b, 3c, 3d, g_3 formula | All verified |
| verify_t4_amplification.py | 4a, 4b, 4c, 4d, Jacobian, comparative statics | See individual verdicts |

---

## Cross-Channel Consistency

**Variable definitions:** Consistent across all channels and the amplification loop. rho has the same normalisation convention throughout. N_eff formula is consistent between Channel 3 standalone and the g_3 mapping. The g_3 formula correctly generalises N_eff with the (1-mu_I)^2 factor.

**g_1 functional form:** The mapping rho_eff = 1 - (1-rho)*(N_eff/N) is assumed, not microfounded. It satisfies correct boundary conditions (rho_eff = rho at N_eff = N; rho_eff -> 1 at N_eff -> 1 for large N) and is monotone in both arguments. The document acknowledges this in Open Questions (item 5a). The qualitative results (existence, bifurcation, safety illusion) should be robust to alternative specifications satisfying the same boundary conditions, though this has not been formally established.

**Jacobian rank deficiency:** The Jacobian DT has rank at most 2 (zero third column). This arises because the updated state does not depend on the current N_eff directly. The document acknowledges this (Open Questions 5b). The rank deficiency does NOT invalidate the bifurcation result -- it simplifies it to a one-dimensional condition (lambda_1 crossing 1). An alternative formulation with a full-rank Jacobian would produce the same qualitative conclusion (positive feedback loop creates instability).

**Brouwer conditions:** All three conditions verified (compact convex domain, T maps K into K, T continuous). The boundary treatment at rho_eff = rho_1* uses worst-case equilibrium selection, which is a modelling choice that preserves continuity.

**Channel 1 uniqueness condition:** The document uses the Morris-Shin (2003) linear-quadratic uniqueness condition for a binary-action game (GP bank run). As noted in the previous report, the exact uniqueness condition for binary-action games may differ (Frankel-Morris-Payne 2003). This concern remains valid but does not affect the qualitative result -- the existence of SOME uniqueness boundary rho_1* that is increasing in alpha_SC and decreasing in rho.

---

## Scope Compliance

**Clean.** All derivations respect the scope constraints:
- rho is exogenous in all three channels and the amplification loop (the loop endogenises rho_eff but treats exogenous rho as a parameter)
- Static/two-period framework maintained throughout (the iteration indices in T are notational, not temporal)
- No results require dynamic models
- No full Ramsey welfare analysis

---

## Plan Alignment

| Contribution | Plan Promise | Delivered | Status |
|--------------|-------------|-----------|--------|
| 1: theta*(rho) | Non-monotone, uniqueness boundary | Both delivered, formulas now consistent | DELIVERED |
| 2: GS extension with RPE | mu_I decreasing, RPE non-monotone | mu_I INCREASING standalone (correctly explained); RPE monotonically decreasing | PARTIALLY DELIVERED |
| 3: N_eff with convexity | N_eff decreasing/convex, spread convex, rho** threshold | N_eff verified; spread linear in baseline (convex only for beta>1) | PARTIALLY DELIVERED |
| 4: Amplification loop | Fixed-point existence, bifurcation rho* < min(rho_i*) | Brouwer existence, Jacobian analysis, bifurcation proved (with gaps) | DELIVERED (with caveats) |
| 5: Endogenous rho | Prisoner's dilemma extension | Not yet derived (T5) | NOT STARTED |

---

## Summary

Total propositions verified: 18 (including sub-parts and T4)

- **Passed (VERIFIED):** 12
  - Prop 1b (corrected), 2a(i), 2a(ii), 2a(iii), 2c, 3a, 3b, 3d, g_3, 4a, 4c, 4d
- **Conditionally verified:** 6
  - Prop 1a (requires R(theta) specification for complete proof)
  - Prop 1c (AP(2007) framework applicability to binary-action game)
  - Prop 2b(i) (requires c_AI specification for low-rho regime)
  - Prop 2b(ii) (requires c_P > 0, which is assumed)
  - Prop 3c (existence requires parameter conditions, not structural)
  - Prop 4b (h divergence and rho_2*/rho_3* bounds need tightening)
- **Failed:** 0
- **Flagged:** 1
  - Comparative static d(rho*)/d(c_P) > 0 (direction may be incorrect)

---

## Critical Issues (must resolve before Paper Writer)

None. The two previously-critical issues (Prop 1b formula, Prop 1c coefficient) are both RESOLVED.

---

## Warnings (should resolve, not blocking)

1. **Working notes in model_equations.md.** Multiple "Wait --" passages and self-corrections remain (lines 373, 377, 400, 406, 408, 1089, 1141). These should be removed before the Paper Writer uses the document.

2. **Proposition 3b: Spread convexity claim.** The baseline specification gives a LINEAR spread in rho. The research plan claims convexity. Either adopt beta > 1 with economic justification or weaken the claim to monotonicity.

3. **Proposition 3c: Existence of rho**.** The proof sketch's claim that Cost(rho) is "unbounded" fails in the linear specification with finite N. Rephrase as a parameter condition.

4. **Proposition 4b: h divergence near rho_1*.** The divergence d(theta*)/d(rho_eff) -> infinity as rho_eff -> rho_1* is asserted but not formally proved. A formal proof requires showing the implicit function theta*(rho_eff) has a vertical asymptote at the uniqueness boundary.

5. **Proposition 4b: Strict inequality for rho_2* and rho_3*.** The proof that rho* < rho_2* and rho* < rho_3* (not just rho_1*) uses qualitative arguments about "effective parameters being more adverse" but does not provide a formal bound.

6. **Comparative static d(rho*)/d(c_P) > 0.** The claimed direction may be incorrect. Higher c_P raises |a| = c_P/[(1-theta*)^2 * |dF/dmu_I|] directly, which strengthens the destabilising Ch1->Ch2 feedback and would LOWER rho* (opposite of claimed sign). The equilibrium adjustment complicates the analysis, but the document's intuitive argument ("makes agents less responsive") is not convincing without further derivation.

7. **g_1 functional form.** The mapping rho_eff = 1 - (1-rho)*(N_eff/N) is assumed, not microfounded. A derivation from the price-discovery process would strengthen the result. The qualitative results should be robust but this has not been formally shown.

8. **Channel 1 uniqueness condition for binary-action games.** The formula rho_1* = 1/(1+alpha_SC^2) comes from the Morris-Shin (2003) linear-quadratic framework. The GP (2005) bank-run game has binary actions. The Theory Builder should verify that this bound transfers to the binary case.

9. **Channel 2 direction of mu_I.** The standalone result (mu_I increasing in rho) contradicts the research plan's language. The model equations correctly identify and resolve this through the cross-channel crisis effect, but the Paper Writer must frame this carefully.

---

## Items Requiring Theory Builder Attention

### CONDITIONALLY VERIFIED items:

1. **Proposition 1a:** Complete the non-monotonicity proof by specifying R(theta) and computing d(theta*)/d(rho) explicitly, or state the result as holding under a regularity condition on R(theta).

2. **Proposition 1c:** Verify that the Angeletos-Pavan (2007) welfare result applies to the binary-action GP game, or derive the analogous result for binary actions.

3. **Proposition 3c:** Replace the "unbounded Cost" argument with explicit parameter conditions for existence of rho** in (0,1).

4. **Proposition 4b:** (a) Provide a formal proof that h = d(theta*)/d(rho_eff) diverges at rho_1*. (b) Tighten the argument for rho* < rho_2* and rho* < rho_3*.

### FLAGGED items:

5. **Comparative static d(rho*)/d(c_P):** Re-derive this more carefully. The current argument may have the wrong sign.
