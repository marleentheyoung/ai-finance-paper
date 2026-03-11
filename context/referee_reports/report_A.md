# Referee A Report -- Theory and Rigor
Date: 2026-03-11
Sections reviewed: model.tex, channel1.tex, channel2.tex, channel3.tex, amplification.tex, extensions.tex, conclusion.tex

## Summary

The manuscript has improved materially since Round 1. The two previously blocking issues (Proposition 1b formula mismatch and Proposition 1c coefficient discrepancy) are resolved. The mathematical presentation is generally clear, propositions are self-contained, and proof sketches are present throughout. However, several issues remain: (1) a large number of displayed equations lack any \eqref{} cross-reference, (2) the uniqueness-boundary formula rho_1* is derived from the Morris-Shin (2003) linear-quadratic framework but applied to the binary-action Goldstein-Pauzner game without adequate justification, (3) the saddle-node bifurcation argument in Proposition 5 (amplification bifurcation) contains a self-contradictory passage, and (4) the g_1 mapping remains assumed rather than derived.

## Issues

### Priority 1 -- Blocking (must fix before submission)

| ID  | File | Location | Issue | Severity |
|-----|------|----------|-------|----------|
| A1  | channel1.tex | lines 33-35 | The displayed equation for rho_1* uses `\[...\]` (unnumbered) instead of `\begin{equation}\label{...}`. This is the first appearance of rho_1* outside a proposition and should be numbered and labelled, especially since the same formula is re-stated in eq:rho1star-prop at line 40. Either label the first occurrence or remove the duplication. | Critical |
| A2  | channel1.tex | lines 30-35 | The derivation of rho_1* applies the Morris-Shin (2003) uniqueness condition alpha_SC * sqrt(rho/(1-rho)) < 1 to the binary-action Goldstein-Pauzner game. The proof sketch at lines 44-45 cites Hellwig (2002, Theorem 1) and claims the condition "transfers" because of monotone threshold strategies and dominance regions. This is not rigorous: the Morris-Shin condition is derived for linear-quadratic payoffs, and the mapping to the binary-action game requires showing that the GP equilibrium system has the same saddle-node structure at the same critical ratio. The verification report (Warning 8) also flags this gap. Either provide a formal proof for the binary case (possibly in an appendix), cite a result that establishes equivalence, or state the formula as holding under the additional assumption that the binary-action uniqueness boundary coincides with the linear-quadratic one. | Critical |
| A3  | amplification.tex | lines 97-108 | The saddle-node bifurcation argument in Proposition 5 (Amplification Bifurcation) proof sketch, Step 2, is internally contradictory. At line 101, the text computes dG/d(theta*) at the bifurcation and initially gets "= 1 - (phi(0)/phi(Phi^{-1}(theta*))) * 0 = 1 - 0", concluding non-zero. It then states "More carefully" and attempts to show dG/d(theta*) vanishes at theta* = 1/2. The passage at line 108 concludes that dG/d(theta*) "vanishes to first order, confirming the saddle-node structure." But the algebra shown still yields dG/d(theta*) -> 1 (not 0) in the stated limit. The proof needs to clearly demonstrate that the zero eigenvalue of the 2x2 equilibrium system (x*, theta*) maps to dG/d(theta*) = 0 for the reduced scalar equation, or alternatively cite the Frankel-Morris-Payne (2003) result directly. The current presentation will confuse any reviewer with bifurcation theory background. | Critical |

### Priority 2 -- Important (fix in this revision cycle)

| ID  | File | Location | Issue | Severity |
|-----|------|----------|-------|----------|
| A4  | multiple | throughout | Twenty-two displayed equations have labels but are never referenced by \eqref{}. These include core results: eq:signal-correlation, eq:withdrawal-ai, eq:withdrawal-total, eq:crisis-threshold, eq:effective-fundamental, eq:theta-star-monotonicity, eq:welfare-loss, eq:ninfo-full, eq:rpe, eq:gy-complementarity, eq:neff-decreasing, eq:neff-convex, eq:rho-star-star, eq:g1, eq:g2, eq:g3, eq:bifurcation, eq:h-divergence, eq:systemic-cost, eq:nash-eq, eq:ninfo. Unreferenced equation labels suggest the equations are decorative rather than load-bearing. Each should be referenced at least once in the surrounding text or in a later section. | Serious |
| A5  | amplification.tex | lines 59-70 | The five Jacobian coefficients (a, b, m, h, w) are defined in unnumbered align blocks using `\notag`. These are the core quantities of the amplification analysis and should be numbered and labelled for reference. At minimum, the eigenvalue discussion at line 78 and Proposition 5 should reference them by equation number. | Serious |
| A6  | channel2.tex | lines 22-27 | Equations eq:pi-ai and eq:pi-private introduce reduced-form trading profit functions (pi_A = k_A * sqrt(1-rho)/mu_A, pi_P = k_P/mu_I) with unexplained constants k_A and k_P. The text says k_A > 0 "depends on market microstructure parameters" but never specifies what these parameters are or how they relate to the primitives (gamma, sigma_u, tau_s, tau_P) of the GS framework. This makes Proposition 3 (Information Diversity Collapse) difficult to verify independently. The constants should be expressed in terms of the model primitives, at least in an appendix. | Serious |
| A7  | amplification.tex | lines 19-21 | The g_1 mapping rho_eff = 1 - (1-rho)(N_eff/N) is assumed rather than derived. The verification report (Warning 7) flags this. It is presented as a "convex combination" with correct boundary properties, but the economic mechanism (correlated liquidity withdrawal functioning as a common signal) should produce a specific functional form from the price-discovery process. Without microfoundation, the quantitative content of the bifurcation threshold rho* is model-specific in a way that limits external validity. State this as an assumption explicitly, or provide a derivation. | Serious |
| A8  | model.tex | lines 54-62 | Lemma 1 (Information Collapse) uses N_{\emph{info}} with \emph inside the subscript, producing italic "info" in math mode. This should be N_{\text{info}} for consistency with the rest of the paper (which uses \text{} for multi-letter subscripts). The same issue appears in eq:ninfo. | Serious |
| A9  | channel1.tex | lines 52-60 | Proposition 2 (Crisis Threshold Non-Monotonicity) states a regularity condition on sigma involving theta_H, theta_L, and rho_1*, but these bounds are never used again in the paper. The condition is stated as sufficient but it is not clear whether it is necessary. Clarify the role of this condition and whether the non-monotonicity result holds more generally. | Serious |
| A10 | extensions.tex | lines 30-44 | Proposition 8 (Endogenous Signal Correlation) part (iii) claims rho^NE > rho^SO and, "when kappa_sys is large enough," rho^NE > rho*. This is a conditional claim masquerading as a proposition. The condition "kappa_sys large enough" is not quantified. Either provide an explicit bound on kappa_sys in terms of other parameters, or weaken the statement to a corollary that holds under a stated parameter condition. | Serious |

### Priority 3 -- Minor (fix if time permits)

| ID  | File | Location | Issue | Severity |
|-----|------|----------|-------|----------|
| A11 | channel1.tex | lines 11-17 | Three consecutive displayed equations (eq:withdrawal-ai, eq:withdrawal-total, eq:crisis-threshold) with minimal intervening prose. Lines 14 and 18 have one sentence each, but the density is high for a passage that is not in an appendix. Consider moving the derivation of the withdrawal fractions to a proof appendix and stating only the crisis threshold condition in the main text. | Minor |
| A12 | channel3.tex | lines 36-43 | Two consecutive displayed equations (eq:neff-decreasing, eq:neff-convex) inside Proposition 4 with no intervening prose between them. Add a sentence between (ii) and (iii) interpreting the monotonicity before stating convexity. | Minor |
| A13 | amplification.tex | lines 103-106 | The local expansion theta*(rho_eff) = theta*(rho_1*) - C*sqrt(rho_1* - rho_eff) + O(...) uses an unnumbered display `\[...\]`. Since this is the key asymptotic result that drives the divergence of h, it should be numbered and referenced. | Minor |
| A14 | channel2.tex | line 7 | The fundamental V is defined as V ~ N(v_bar, 1/tau_v), but in Channel 1 the fundamental is theta ~ U[0,1]. The paper should note explicitly at the start of Channel 2 that V is a different random variable from theta (or unify notation). Currently the distinction is implicit. | Minor |
| A15 | extensions.tex | lines 13-23 | Three consecutive displayed equations (eq:pi-alpha-adoption, eq:tracking-error, eq:systemic-cost) with one-sentence descriptions between them. The density is acceptable but the descriptions could be expanded to improve readability. | Minor |
| A16 | channel3.tex | lines 62-73 | Proposition 5 (No-Equilibrium Threshold) states a parameter condition Qs_0/N^2 > gamma*sigma_V^2*kappa_inv in the assumptions. The variables Q and kappa_inv are introduced for the first time here without prior definition. Define them before the proposition statement. | Minor |
| A17 | model.tex | line 14 | The text states "We write tau_s = 1/sigma^2 for the precision" and "this notation is used interchangeably with sigma^2 throughout." Later (channel2.tex line 70), tau_s appears in the RPE formula. However, Channel 2 introduces tau_P = 1/sigma_P^2 separately, and the model section uses tau = 1/sigma^2. The subscript conventions (tau, tau_s, tau_P, tau_v) should be collected in a notation table. | Minor |
| A18 | amplification.tex | line 78 | The eigenvalue is called lambda_1. This conflicts with the standard use of lambda for the fraction of AI-equipped agents (used throughout model.tex and channel1.tex). Consider using a different symbol (e.g., mu_1 or ell_1) for the eigenvalue to avoid confusion. | Minor |

## Equation Density Summary

| Section | Approx pages | Displayed equations | Density flag |
|---------|-------------|--------------------:|-------------|
| model.tex | 1.7 | 4 | OK |
| channel1.tex | 2.3 | 8 | HIGH |
| channel2.tex | 2.5 | 7 | OK |
| channel3.tex | 2.5 | 8 | HIGH |
| amplification.tex | 3.6 | 9 + 4 unnumbered | HIGH |
| extensions.tex | 2.1 | 5 | OK |
| conclusion.tex | 0.6 | 0 | OK |

Channel 1 (lines 11-21: three equations in 10 lines) and the amplification Jacobian section (lines 59-78: two align blocks plus two equations in 20 lines) are the densest passages.

## Notation Issues

1. **N_{\emph{info}} vs N_{\text{info}}**: model.tex line 55 uses \emph inside math subscript; rest of paper uses \text.
2. **lambda (eigenvalue) vs lambda (AI fraction)**: amplification.tex line 78 defines lambda_1 as the eigenvalue of DT; model.tex line 27 and channel1.tex line 6 use lambda for the fraction of AI-equipped agents.
3. **tau vs tau_s**: model.tex defines tau = 1/sigma^2 (line 14) and tau_s = 1/sigma^2 (same line). Channel 2 uses tau_s in eq:rpe (line 70). Channel 3 uses sigma_V^2 without relating it to sigma^2 from the model section.
4. **V vs theta**: Channel 1 uses theta as the fundamental; Channels 2-3 use V. The relationship is implicit (they are different fundamentals in different settings), but this could be stated explicitly.
5. **alpha_SC vs alpha**: The strategic complementarity parameter is consistently alpha_SC throughout the manuscript. Good.

## Appendix Recommendation

1. **Channel 1 withdrawal fraction derivation (lines 11-21)**: The three equations defining l_AI, l, and the crisis threshold are standard given the signal structure. Move to an appendix and state only the crisis threshold condition in the main text.
2. **Channel 3 N_eff derivatives (Proposition 4, parts ii-iii)**: The first and second derivatives are direct computation. Move to an appendix; state only the monotonicity and convexity properties in the proposition.
3. **Amplification Jacobian algebra (lines 59-78)**: The full Jacobian matrix and eigenvalue computation are mechanical once the five coefficients are defined. Move the matrix computation to an appendix and keep only the eigenvalue formula and its economic interpretation in the main text.
4. **Saddle-node bifurcation argument (Proposition 5, Step 2, lines 97-112)**: This is the longest proof sketch in the paper and contains the self-contradictory passage flagged in A3. A clean version should go in a formal appendix with the main text containing only the statement and a one-paragraph intuition.

## Recommendation
MINOR REVISION
The mathematical framework is sound and the results are correct conditional on the identified gaps (binary-action uniqueness transfer, g_1 microfoundation, saddle-node algebra). The blocking issues are fixable within one revision cycle. The unreferenced equations and notation inconsistencies are cosmetic but numerous enough to warrant systematic cleanup before submission.
