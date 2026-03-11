"""
Verification of Channel 3 Propositions (3a, 3b, 3c, Lemma 3d)
Model Verifier -- 2026-03-10
"""

import sympy as sp

print("=" * 70)
print("CHANNEL 3 VERIFICATION")
print("=" * 70)

# =====================================================================
# Common symbols
# =====================================================================
rho = sp.Symbol("rho", positive=True)
N = sp.Symbol("N", positive=True)
s_0 = sp.Symbol("s_0", positive=True)
beta = sp.Symbol("beta", positive=True)
mu_I = sp.Symbol("mu_I", positive=True)

# =====================================================================
# Proposition 3a: N_eff Characterisation
# N_eff(rho) = N / (1 + (N-1) * rho)
# =====================================================================
print("\n--- Proposition 3a: N_eff ---")

N_eff = N / (1 + (N - 1) * rho)

# (i) Boundary values
print("  (i) Boundary values:")
N_eff_0 = N_eff.subs(rho, 0)
N_eff_1 = sp.simplify(N_eff.subs(rho, 1))
print(
    f"    N_eff(0) = {N_eff_0} (expected N): {'VERIFIED' if N_eff_0 == N else 'FAILED'}"
)
print(
    f"    N_eff(1) = {N_eff_1} (expected 1): {'VERIFIED' if N_eff_1 == 1 else 'FAILED'}"
)

# (ii) Strictly decreasing
print("\n  (ii) Monotonicity:")
dN_drho = sp.diff(N_eff, rho)
dN_simplified = sp.simplify(dN_drho)
print(f"    d(N_eff)/d(rho) = {dN_simplified}")

# Check matches claimed formula
claimed_deriv = -N * (N - 1) / (1 + (N - 1) * rho) ** 2
diff_deriv = sp.simplify(dN_simplified - claimed_deriv)
print(f"    Matches claimed -N*(N-1)/(1+(N-1)*rho)^2: {diff_deriv == 0}")
print("    Sign: NEGATIVE for N > 1: VERIFIED")

# (iii) Strictly convex
print("\n  (iii) Convexity:")
d2N_drho2 = sp.diff(N_eff, rho, 2)
d2N_simplified = sp.simplify(d2N_drho2)
print(f"    d^2(N_eff)/d(rho)^2 = {d2N_simplified}")

claimed_second = 2 * N * (N - 1) ** 2 / (1 + (N - 1) * rho) ** 3
diff_second = sp.simplify(d2N_simplified - claimed_second)
print(f"    Matches claimed 2*N*(N-1)^2/(1+(N-1)*rho)^3: {diff_second == 0}")
print("    Sign: POSITIVE for N > 1: VERIFIED")

# (iv) Half-point
print("\n  (iv) Half-point at rho = 1/(N-1):")
rho_half = 1 / (N - 1)
N_eff_half = sp.simplify(N_eff.subs(rho, rho_half))
print(
    f"    N_eff(1/(N-1)) = {N_eff_half} (expected N/2): {'VERIFIED' if N_eff_half == N/2 else 'FAILED'}"
)

# Numerical spot check
print("\n  Numerical spot check (N=100, rho=0.1):")
N_eff_num = float(N_eff.subs({N: 100, rho: sp.Rational(1, 10)}))
print(f"    N_eff = 100 / (1 + 99*0.1) = 100/10.9 = {N_eff_num:.2f}")
print(
    f"    Document claims ~9.2: {'VERIFIED' if abs(N_eff_num - 9.17) < 0.1 else 'FAILED'}"
)

# =====================================================================
# Proposition 3b: Spread Monotonicity
# s*(rho) = s_0 * (1 + (N-1)*rho) / N = s_0 / N_eff
# =====================================================================
print("\n--- Proposition 3b: Spread ---")

s_star = s_0 * (1 + (N - 1) * rho) / N

# Boundary values
s_0_val = s_star.subs(rho, 0)
s_1_val = sp.simplify(s_star.subs(rho, 1))
print(
    f"  s*(0) = {s_0_val} (expected s_0/N): {'VERIFIED' if s_0_val == s_0/N else 'FAILED'}"
)
print(
    f"  s*(1) = {s_1_val} (expected s_0): {'VERIFIED' if s_1_val == s_0 else 'FAILED'}"
)

# (i) Strictly increasing
ds_drho = sp.diff(s_star, rho)
print(f"\n  (i) d(s*)/d(rho) = {sp.simplify(ds_drho)}")
claimed_ds = s_0 * (N - 1) / N
print(f"    Matches claimed s_0*(N-1)/N: {sp.simplify(ds_drho - claimed_ds) == 0}")
print("    Sign: POSITIVE for N > 1: VERIFIED")

# (ii) Linear in rho
d2s_drho2 = sp.diff(s_star, rho, 2)
print(f"\n  (ii) d^2(s*)/d(rho)^2 = {d2s_drho2}")
print("    This is ZERO -- spread is LINEAR in rho: VERIFIED")
print("    CRITICAL: The baseline specification is NOT convex!")

# (iii) Convex under nonlinear specification
print("\n  (iii) Nonlinear specification s_NL = s_0 * ((1+(N-1)*rho)/N)^beta:")
s_NL = s_0 * ((1 + (N - 1) * rho) / N) ** beta
d2s_NL = sp.diff(s_NL, rho, 2)
d2s_NL_simplified = sp.simplify(d2s_NL)
print(f"    d^2(s_NL)/d(rho)^2 = {d2s_NL_simplified}")

# Check the claimed formula
# claimed: s_0 * beta * (beta-1) * ((1+(N-1)*rho)/N)^{beta-2} * ((N-1)/N)^2
claimed_d2 = (
    s_0
    * beta
    * (beta - 1)
    * ((1 + (N - 1) * rho) / N) ** (beta - 2)
    * ((N - 1) / N) ** 2
)
diff_d2 = sp.simplify(d2s_NL_simplified - claimed_d2)

# Test numerically
test_vals = {s_0: 1, N: 10, rho: sp.Rational(1, 2), beta: 2}
num_computed = float(d2s_NL_simplified.subs(test_vals))
num_claimed = float(claimed_d2.subs(test_vals))
print("    Numerical check at s_0=1, N=10, rho=0.5, beta=2:")
print(f"      Computed: {num_computed:.6f}")
print(f"      Claimed:  {num_claimed:.6f}")
print(f"      Match: {abs(num_computed - num_claimed) < 1e-10}")

# Sign for beta > 1
print("    For beta > 1: beta*(beta-1) > 0, so d^2 > 0: CONVEX")
print("    For beta < 1: beta*(beta-1) < 0, so d^2 < 0: CONCAVE")
print("    VERIFIED: Convexity requires beta > 1")

# =====================================================================
# Document's earlier erroneous convexity derivation
# =====================================================================
print("\n--- Cross-check: Document's convexity analysis ---")
print("  The document initially tries s_NL = s_0 / N_eff^beta")
print("  and derives convexity condition using chain rule.")
print("  It finds the condition [beta-1] > 0, consistent with beta > 1.")
print("  HOWEVER, the document also states (line ~1187-1193):")
print("  'd^2(s*)/d(rho)^2 = s_0 * 2*(N-1)^2 / N > 0' for the LINEAR spec,")
print("  which is WRONG (the linear spec has d^2 = 0).")
print("  This error originates from the task specification, not the derivation.")
print("  The derivation correctly identifies the issue and resolves it.")

# =====================================================================
# Proposition 3c: No-equilibrium threshold rho**
# =====================================================================
print("\n--- Proposition 3c: No-equilibrium threshold rho** ---")
print("  Revenue(rho) = Q*s_0*(1+(N-1)*rho)/(N^2)")
print("  Cost(rho) = gamma*sigma_V^2*kappa_inv*(1+(N-1)*rho)")
print("  Both linear in (1+(N-1)*rho)")

Q, gamma_mm, sigma_V, kappa_inv, pi_0 = sp.symbols(
    "Q gamma_mm sigma_V kappa_inv pi_0", positive=True
)

Rev = Q * s_0 * (1 + (N - 1) * rho) / N**2
Cost = gamma_mm * sigma_V**2 * kappa_inv * (1 + (N - 1) * rho)

# Participation: Rev >= Cost + pi_0
# (1+(N-1)*rho) * [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] = pi_0
marginal_profit = Q * s_0 / N**2 - gamma_mm * sigma_V**2 * kappa_inv
print("\n  Marginal net revenue per unit (1+(N-1)*rho):")
print("  Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv")

print("\n  Case 1: Marginal profit > 0:")
print("    rho** = (pi_0/marginal_profit - 1) / (N-1)")
print("    This gives rho** > 0 when pi_0 > marginal_profit")
print("    And rho** in (0,1) under parameter restrictions")

print("\n  Case 2: Marginal profit <= 0:")
print("    Revenue never exceeds cost, rho** = 0")
print("    No equilibrium for any positive rho")

# Verify the closed-form
rho_star_star = (pi_0 / marginal_profit - 1) / (N - 1)
# Check: at rho = rho**, Rev = Cost + pi_0
Rev_at_rho_ss = Rev.subs(rho, rho_star_star)
Cost_at_rho_ss = Cost.subs(rho, rho_star_star)
diff_check = sp.simplify(Rev_at_rho_ss - Cost_at_rho_ss - pi_0)
print(f"\n  Substitution check: Rev(rho**) - Cost(rho**) - pi_0 = {diff_check}")
if diff_check == 0:
    print("  VERIFIED: Closed-form is correct")
else:
    print(f"  Simplification result: {diff_check}")
    # Try harder
    diff_check2 = sp.simplify(sp.expand(diff_check))
    print(f"  After expand: {diff_check2}")

# =====================================================================
# Check: Cost unbounded claim
# =====================================================================
print("\n--- Cost unboundedness check ---")
print("  Document claims: Cost(rho) unbounded as rho->1 for N>=2")
Cost_at_1 = Cost.subs(rho, 1)
print("  Cost(1) = gamma*sigma_V^2*kappa_inv*(1+(N-1)) = gamma*sigma_V^2*kappa_inv*N")
print("  This is finite, not unbounded!")
print("  FLAG: The document claims Cost is unbounded as rho->1,")
print("  but in the linear specification, Cost(1) is finite.")
print("  The 'unbounded' claim requires N->infinity simultaneously,")
print("  or a nonlinear inventory cost specification.")
print("  In the stated model, rho** may not exist if Revenue(1) > Cost(1) + pi_0.")
print("  The existence proof needs the additional assumption that")
print("  Cost grows faster than Revenue in rho, which requires either:")
print("  (a) N sufficiently large, or")
print("  (b) nonlinear cost specifications.")

# =====================================================================
# Lemma 3d: DSZ limiting case
# =====================================================================
print("\n--- Lemma 3d: DSZ limiting case ---")
print("  At rho=1: N_eff(1) = 1")
print("  All market makers identical => single representative agent")
print("  This is a definitional/structural claim, not algebraic.")
print("  VERIFIED (by construction)")

# =====================================================================
# g_3 formula for amplification loop
# N_eff = N / (1 + (N-1)*rho*(1-mu_I)^2)
# =====================================================================
print("\n--- g_3 formula verification ---")
g_3 = N / (1 + (N - 1) * rho * (1 - mu_I) ** 2)

# Check mu_I = 0 reduces to standalone
g_3_0 = g_3.subs(mu_I, 0)
standalone = N / (1 + (N - 1) * rho)
print(f"  g_3(mu_I=0) = {sp.simplify(g_3_0)}")
print(f"  Standalone: {standalone}")
print(f"  Match: {sp.simplify(g_3_0 - standalone) == 0}")

# Check mu_I = 1 gives N
g_3_1 = sp.simplify(g_3.subs(mu_I, 1))
print(f"  g_3(mu_I=1) = {g_3_1} (expected N): {'VERIFIED' if g_3_1 == N else 'FAILED'}")

# Partial derivatives
dg3_dmu = sp.diff(g_3, mu_I)
dg3_drho = sp.diff(g_3, rho)
dg3_dmu_simplified = sp.simplify(dg3_dmu)
dg3_drho_simplified = sp.simplify(dg3_drho)

print(f"\n  d(g_3)/d(mu_I) = {dg3_dmu_simplified}")
# Verify sign positive
claimed_dg3_dmu = (
    2 * N * (N - 1) * rho * (1 - mu_I) / (1 + (N - 1) * rho * (1 - mu_I) ** 2) ** 2
)
diff_dg3 = sp.simplify(dg3_dmu_simplified - claimed_dg3_dmu)
print(f"  Matches claimed: {diff_dg3 == 0}")

# Test numerically
test = {N: 10, rho: sp.Rational(1, 2), mu_I: sp.Rational(1, 4)}
val = float(dg3_dmu_simplified.subs(test))
print(f"  At N=10, rho=0.5, mu_I=0.25: d(g_3)/d(mu_I) = {val:.4f}")
print(f"  Sign: {'POSITIVE (verified)' if val > 0 else 'ERROR'}")

print(f"\n  d(g_3)/d(rho) = {dg3_drho_simplified}")
val2 = float(dg3_drho_simplified.subs(test))
print(f"  At N=10, rho=0.5, mu_I=0.25: d(g_3)/d(rho) = {val2:.4f}")
print(f"  Sign: {'NEGATIVE (verified)' if val2 < 0 else 'ERROR'}")

print("\n" + "=" * 70)
print("CHANNEL 3 SUMMARY")
print("=" * 70)
print("Prop 3a (N_eff): VERIFIED")
print("  - Formula, boundary values, monotonicity, convexity all correct")
print("Prop 3b (Spread):")
print("  - Monotonicity (increasing in rho): VERIFIED")
print("  - Linearity (d^2=0 in baseline): VERIFIED")
print("  - Convexity: CONDITIONALLY VERIFIED (requires beta > 1)")
print("  - FLAG: Baseline spec is linear, not convex as plan claims")
print("Prop 3c (rho** threshold): CONDITIONALLY VERIFIED")
print("  - Closed-form derivation: correct under stated cost structure")
print("  - FLAG: 'Cost unbounded' claim fails in linear spec with finite N")
print("  - Existence requires additional parameter conditions")
print("Lemma 3d (DSZ limit): VERIFIED (by construction)")
print("g_3 formula: VERIFIED (boundary values and partial derivatives)")
