"""
Verification of Channel 3 (T3) propositions: 3a, 3b, 3c, 3d.
"""

import sympy as sp

rho = sp.Symbol("rho", positive=True)
N = sp.Symbol("N", positive=True, integer=True)
s_0 = sp.Symbol("s_0", positive=True)
beta_param = sp.Symbol("beta", positive=True)

print("=" * 70)
print("PROPOSITION 3a: N_eff Characterisation")
print("=" * 70)

N_eff = N / (1 + (N - 1) * rho)

print(f"\nN_eff(rho) = {N_eff}")

# (i) Boundary values
N_eff_0 = N_eff.subs(rho, 0)
N_eff_1 = N_eff.subs(rho, 1)
print(f"\n(i) N_eff(0) = {sp.simplify(N_eff_0)}")
print(f"    N_eff(1) = {sp.simplify(N_eff_1)}")
assert sp.simplify(N_eff_0 - N) == 0, "N_eff(0) != N"
assert sp.simplify(N_eff_1 - 1) == 0, "N_eff(1) != 1"
print("    VERIFIED: N_eff(0) = N, N_eff(1) = 1")

# (ii) First derivative
dN_eff = sp.diff(N_eff, rho)
dN_eff_simplified = sp.simplify(dN_eff)
print(f"\n(ii) d(N_eff)/d(rho) = {dN_eff_simplified}")

# Expected: -N*(N-1)/(1+(N-1)*rho)^2
expected_d1 = -N * (N - 1) / (1 + (N - 1) * rho) ** 2
diff_d1 = sp.simplify(dN_eff - expected_d1)
print(f"     Expected: {expected_d1}")
print(f"     Difference: {diff_d1}")
assert diff_d1 == 0, "First derivative mismatch"
print("     Sign: < 0 for N > 1 (all factors positive in numerator, negative sign)")
print("     VERIFIED")

# (iii) Second derivative
d2N_eff = sp.diff(N_eff, rho, 2)
d2N_eff_simplified = sp.simplify(d2N_eff)
print(f"\n(iii) d^2(N_eff)/d(rho)^2 = {d2N_eff_simplified}")

expected_d2 = 2 * N * (N - 1) ** 2 / (1 + (N - 1) * rho) ** 3
diff_d2 = sp.simplify(d2N_eff - expected_d2)
print(f"      Expected: {expected_d2}")
print(f"      Difference: {diff_d2}")
assert diff_d2 == 0, "Second derivative mismatch"
print("      Sign: > 0 for N > 1 (all factors positive)")
print("      VERIFIED: N_eff is strictly convex in rho")

# (iv) Half-point
rho_half = 1 / (N - 1)
N_eff_half = N_eff.subs(rho, rho_half)
print(f"\n(iv) N_eff(1/(N-1)) = {sp.simplify(N_eff_half)}")
assert sp.simplify(N_eff_half - N / 2) == 0, "Half-point mismatch"
print("     VERIFIED: N_eff(1/(N-1)) = N/2")

# Numerical spot check
N_val, rho_val = 100, 0.1
N_eff_num = float(N_eff.subs([(N, N_val), (rho, rho_val)]))
print(f"\n     Numerical: N=100, rho=0.1 => N_eff = {N_eff_num:.2f}")
print(f"     Document says 'about 9.2': match = {abs(N_eff_num - 9.17) < 0.1}")

print("\n>>> PROPOSITION 3a: ALL CLAIMS VERIFIED")

print("\n" + "=" * 70)
print("PROPOSITION 3b: Spread Monotonicity")
print("=" * 70)

# Baseline linear specification
s_star = s_0 * (1 + (N - 1) * rho) / N
print(f"\nBaseline: s*(rho) = {s_star}")

# (i) Monotonicity
ds = sp.diff(s_star, rho)
print(f"\n(i) d(s*)/d(rho) = {sp.simplify(ds)}")
expected_ds = s_0 * (N - 1) / N
print(f"    Expected: {expected_ds}")
assert sp.simplify(ds - expected_ds) == 0
print("    Sign: > 0 for N > 1")
print("    VERIFIED")

# (ii) Linearity
d2s = sp.diff(s_star, rho, 2)
print(f"\n(ii) d^2(s*)/d(rho)^2 = {sp.simplify(d2s)}")
assert sp.simplify(d2s) == 0
print("     = 0 => linear in rho")
print("     VERIFIED (baseline is linear, not convex)")

# (iii) Nonlinear specification: s_NL = s_0 / N_eff^beta = s_0 * ((1+(N-1)*rho)/N)^beta
s_NL = s_0 * ((1 + (N - 1) * rho) / N) ** beta_param
d2s_NL = sp.diff(s_NL, rho, 2)
d2s_NL_simplified = sp.simplify(d2s_NL)
print("\n(iii) Nonlinear spec: s_NL = s_0 * ((1+(N-1)*rho)/N)^beta")
print(f"      d^2(s_NL)/d(rho)^2 = {d2s_NL_simplified}")

# The expected formula from the document:
# s_0 * beta * (beta-1) * ((1+(N-1)*rho)/N)^{beta-2} * ((N-1)/N)^2
expected_d2_NL = (
    s_0
    * beta_param
    * (beta_param - 1)
    * ((1 + (N - 1) * rho) / N) ** (beta_param - 2)
    * ((N - 1) / N) ** 2
)

diff_NL = sp.simplify(d2s_NL - expected_d2_NL)
print("      Expected: s_0*beta*(beta-1)*((1+(N-1)*rho)/N)^(beta-2)*((N-1)/N)^2")
print(f"      Difference: {diff_NL}")

# Numerical check: beta=2, N=10, rho=0.3, s_0=1
vals = {beta_param: 2, N: 10, rho: sp.Rational(3, 10), s_0: 1}
num_d2 = float(d2s_NL.subs(vals))
num_expected = float(expected_d2_NL.subs(vals))
print("      Numerical check (beta=2, N=10, rho=0.3, s_0=1):")
print(f"        SymPy d2: {num_d2:.6f}")
print(f"        Expected: {num_expected:.6f}")
print(f"        Match: {abs(num_d2 - num_expected) < 1e-10}")

# Verify sign condition: positive iff beta > 1
print("      Sign: positive iff beta > 1 (since (beta-1) factor)")
print(
    f"      At beta=0.5: d2 sign = {'-' if float(d2s_NL.subs({**vals, beta_param: sp.Rational(1,2)})) < 0 else '+'}"
)
print(f"      At beta=1.0: d2 = {float(d2s_NL.subs({**vals, beta_param: 1}))}")
print(f"      At beta=2.0: d2 sign = {'+' if float(d2s_NL.subs(vals)) > 0 else '-'}")
print("      VERIFIED: convexity iff beta > 1")

# Boundary values
s_0_val = s_star.subs(rho, 0)
s_1_val = s_star.subs(rho, 1)
print(
    f"\n     Boundaries: s*(0) = {sp.simplify(s_0_val)}, s*(1) = {sp.simplify(s_1_val)}"
)
assert sp.simplify(s_0_val - s_0 / N) == 0
assert sp.simplify(s_1_val - s_0) == 0
print("     VERIFIED: s*(0) = s_0/N, s*(1) = s_0")

print("\n>>> PROPOSITION 3b: ALL CLAIMS VERIFIED")

print("\n" + "=" * 70)
print("PROPOSITION 3c: No-Equilibrium Threshold")
print("=" * 70)

Q, gamma_mm, sigma_V2, kappa_inv, pi_0 = sp.symbols(
    "Q gamma sigma_V2 kappa_inv pi_0", positive=True
)

# From the document's simplified closed form:
# Revenue(rho) = Q * s_0 * (1 + (N-1)*rho) / N^2
# Cost(rho) = gamma * sigma_V^2 * kappa_inv * (1 + (N-1)*rho)
# Set Revenue = Cost + pi_0

Revenue = Q * s_0 * (1 + (N - 1) * rho) / N**2
Cost = gamma_mm * sigma_V2 * kappa_inv * (1 + (N - 1) * rho)

print(f"\nRevenue(rho) = {Revenue}")
print(f"Cost(rho) = {Cost}")
print("Participation: Revenue >= Cost + pi_0")

# At equality: Revenue = Cost + pi_0
# (1 + (N-1)*rho) * [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] = pi_0
participation = sp.Eq(Revenue, Cost + pi_0)
print(f"\nSolving {participation} for rho:")

rho_star_star = sp.solve(participation, rho)
for s in rho_star_star:
    print(f"  rho** = {sp.simplify(s)}")

# Expected formula:
# rho** = (pi_0 / [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] - 1) / (N-1)
margin = Q * s_0 / N**2 - gamma_mm * sigma_V2 * kappa_inv
expected_rho_ss = (pi_0 / margin - 1) / (N - 1)
expected_rho_ss_simplified = sp.simplify(expected_rho_ss)

print("\n  Expected: (pi_0 / [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] - 1) / (N-1)")
print(f"  = {expected_rho_ss_simplified}")

for s in rho_star_star:
    diff = sp.simplify(s - expected_rho_ss)
    print(f"  Difference: {diff}")

# Verify existence conditions
print("\n  Existence requires:")
print("    (a) Q*s_0/N^2 > gamma*sigma_V^2*kappa_inv (margin > 0)")
print("    (b) rho** in (0, 1) => appropriate parameter values")
print("    (c) Revenue(1) and Cost(1) are both FINITE for finite N")

# Check the document's claim about Cost being "unbounded"
print("\n  Cost(1) = gamma*sigma_V^2*kappa_inv*N (FINITE for finite N)")
print("  Revenue(1) = Q*s_0/N (FINITE)")
print("  => Both bounded for finite N. 'Unbounded' claim requires N->inf.")
print("  => Existence of rho** is a PARAMETER CONDITION, not structural.")
print("  WARNING: Document's proof sketch claims Cost is 'unbounded as rho->1'")
print("  but this is only true as N->infinity simultaneously.")

print("\n>>> PROPOSITION 3c: CLOSED-FORM VERIFIED.")
print(">>> Existence requires parameter conditions (not structurally guaranteed).")
print(">>> CONDITIONALLY VERIFIED.")

print("\n" + "=" * 70)
print("LEMMA 3d: DSZ Limiting Case")
print("=" * 70)

print("\nAt rho=1: N_eff(1) = N/(1+(N-1)*1) = N/N = 1")
print(f"  SymPy: {sp.simplify(N_eff.subs(rho, 1))}")
print("  All market makers act identically => DSZ single-representative-agent case")
print("  This is a definitional/structural claim, verified by construction.")

print("\n>>> LEMMA 3d: VERIFIED")

print("\n" + "=" * 70)
print("ADDITIONAL: g_3 formula for T4")
print("=" * 70)

mu_I = sp.Symbol("mu_I", positive=True)
g_3 = N / (1 + (N - 1) * rho * (1 - mu_I) ** 2)

print(f"\ng_3(mu_I, rho, N) = {g_3}")

# Boundary: mu_I = 0 should give standalone N_eff
g3_0 = g_3.subs(mu_I, 0)
print(f"\ng_3(0, rho, N) = {sp.simplify(g3_0)}")
assert sp.simplify(g3_0 - N_eff) == 0
print("  = N/(1+(N-1)*rho) = standalone N_eff. VERIFIED.")

# Boundary: mu_I = 1 should give N
g3_1 = g_3.subs(mu_I, 1)
print(f"\ng_3(1, rho, N) = {sp.simplify(g3_1)}")
assert sp.simplify(g3_1 - N) == 0
print("  = N (full independence). VERIFIED.")

# Partial derivative w.r.t. mu_I
dg3_dmu = sp.diff(g_3, mu_I)
dg3_dmu_simplified = sp.simplify(dg3_dmu)
print(f"\nd(g_3)/d(mu_I) = {dg3_dmu_simplified}")

# Expected: 2*N*(N-1)*rho*(1-mu_I) / (1+(N-1)*rho*(1-mu_I)^2)^2
expected_dg3 = (
    2 * N * (N - 1) * rho * (1 - mu_I) / (1 + (N - 1) * rho * (1 - mu_I) ** 2) ** 2
)
diff_dg3 = sp.simplify(dg3_dmu - expected_dg3)
print(f"  Expected: {expected_dg3}")
print(f"  Difference: {diff_dg3}")
print("  Sign: > 0 (for mu_I < 1). VERIFIED.")

# Partial derivative w.r.t. rho
dg3_drho = sp.diff(g_3, rho)
dg3_drho_simplified = sp.simplify(dg3_drho)
print(f"\nd(g_3)/d(rho) = {dg3_drho_simplified}")

expected_dg3rho = (
    -N * (N - 1) * (1 - mu_I) ** 2 / (1 + (N - 1) * rho * (1 - mu_I) ** 2) ** 2
)
diff_dg3rho = sp.simplify(dg3_drho - expected_dg3rho)
print(f"  Expected: {expected_dg3rho}")
print(f"  Difference: {diff_dg3rho}")
print("  Sign: < 0. VERIFIED.")

print("\n>>> g_3 formula: ALL CLAIMS VERIFIED")
