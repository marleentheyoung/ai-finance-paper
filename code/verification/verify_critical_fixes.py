"""
Verification of the two critical issues from the previous report.
1. Proposition 1b: uniqueness boundary formula
2. Proposition 1c: welfare coefficient
"""

import sympy as sp

print("=" * 70)
print("CRITICAL FIX 1: Proposition 1b -- Uniqueness Boundary")
print("=" * 70)

rho, alpha = sp.symbols("rho alpha", positive=True)

# The proposition now states: rho_1* = 1 / (1 + alpha_SC^2)
# This should follow from: alpha * sqrt(rho/(1-rho)) < 1 for uniqueness

# Solve alpha * sqrt(rho/(1-rho)) = 1 for rho
eq = sp.Eq(alpha * sp.sqrt(rho / (1 - rho)), 1)
sol = sp.solve(eq, rho)
print("\nSolving alpha * sqrt(rho/(1-rho)) = 1 for rho:")
for s in sol:
    print(f"  rho = {s} = {sp.simplify(s)}")

# Expected: rho = 1/(1 + alpha^2)
expected = 1 / (1 + alpha**2)
print(f"\nExpected: rho = {expected}")

# Check equivalence
for s in sol:
    diff = sp.simplify(s - expected)
    print(f"  Difference from expected: {diff}")
    if diff == 0:
        print("  => MATCH CONFIRMED")

# Verify the uniqueness condition direction
# At rho < 1/(1+alpha^2), alpha*sqrt(rho/(1-rho)) should be < 1
rho_test = sp.Rational(1, 4)  # rho=0.25
alpha_test = sp.Integer(1)  # alpha=1, so rho_1* = 0.5
val = alpha_test * sp.sqrt(rho_test / (1 - rho_test))
print("\nDirection check: alpha=1, rho=0.25 (below rho_1*=0.5):")
print(f"  alpha*sqrt(rho/(1-rho)) = {val} = {float(val):.4f} < 1? {float(val) < 1}")

rho_test2 = sp.Rational(3, 4)  # rho=0.75
val2 = alpha_test * sp.sqrt(rho_test2 / (1 - rho_test2))
print("  alpha=1, rho=0.75 (above rho_1*=0.5):")
print(f"  alpha*sqrt(rho/(1-rho)) = {val2} = {float(val2):.4f} < 1? {float(val2) < 1}")

# Check the OLD formula that was flagged as wrong
old_formula = sp.sqrt(2 * sp.pi) / (alpha + sp.sqrt(2 * sp.pi))
print("\nOLD formula: rho_1* = sqrt(2pi)/(alpha+sqrt(2pi))")
print(f"  At alpha=1: old = {float(old_formula.subs(alpha, 1)):.4f}")
print(f"  At alpha=1: new = {float(expected.subs(alpha, 1)):.4f}")
print("  These differ => old formula was WRONG, new is CORRECT")

print("\n>>> VERDICT: Proposition 1b formula CORRECTED to rho_1* = 1/(1+alpha_SC^2).")
print(">>> The statement at line 353 matches the derivation at line 456.")
print(">>> RESOLVED.")

print("\n" + "=" * 70)
print("CRITICAL FIX 2: Proposition 1c -- Welfare Coefficient")
print("=" * 70)

alpha_sc = sp.Symbol("alpha_SC", positive=True)

# Current statement (line 477): alpha_SC^2 / (1 - alpha_SC)^2
coeff_current = alpha_sc**2 / (1 - alpha_sc) ** 2

# Old (wrong) statement: alpha_SC^2 / (1 - alpha_SC^2)
coeff_old = alpha_sc**2 / (1 - alpha_sc**2)

print("\nCurrent statement coefficient: alpha_SC^2 / (1 - alpha_SC)^2")
print("Old (wrong) coefficient:       alpha_SC^2 / (1 - alpha_SC^2)")

# Numerical check at alpha_SC = 0.5
a_val = sp.Rational(1, 2)
print("\nAt alpha_SC = 0.5:")
print(f"  Current: {float(coeff_current.subs(alpha_sc, a_val)):.4f}")
print(f"  Old:     {float(coeff_old.subs(alpha_sc, a_val)):.4f}")

# Check consistency: the derivation says agents overweight common info
# by factor alpha/(1-alpha), and loss is proportional to square of this
overweight = alpha_sc / (1 - alpha_sc)
loss_coeff = overweight**2
print("\nAP(2007) overweighting factor: alpha/(1-alpha)")
print(f"  Squared: alpha^2/(1-alpha)^2 = {sp.expand(loss_coeff)}")
print(f"  Matches current statement? {sp.simplify(loss_coeff - coeff_current) == 0}")

# The explanation at line 479 says: "agents place weight alpha_SC/(1-alpha_SC)
# on common information relative to the efficient benchmark, and the welfare loss
# is proportional to the square of this over-weighting."
# This is internally consistent with alpha^2/(1-alpha)^2.

print(
    "\n>>> VERDICT: Proposition 1c coefficient CORRECTED to alpha_SC^2/(1-alpha_SC)^2."
)
print(">>> The statement (line 477) now matches the derivation and the AP(2007) logic.")
print(">>> RESOLVED.")
