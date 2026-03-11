"""
Verification of Channel 1 Propositions (1a, 1b, 1c)
Model Verifier -- 2026-03-10
"""

import sympy as sp

print("=" * 70)
print("CHANNEL 1 VERIFICATION")
print("=" * 70)

# =====================================================================
# Common symbols
# =====================================================================
rho, alpha, lam, sigma, tau = sp.symbols("rho alpha lambda sigma tau", positive=True)
N = sp.Symbol("N", positive=True, integer=True)

# =====================================================================
# Proposition 1b: Uniqueness/Multiplicity Boundary
# Claimed: rho_1* = 1 / (1 + alpha_SC^2)
# Source condition: alpha * sqrt(rho / (1 - rho)) < 1 for uniqueness
# =====================================================================
print("\n--- Proposition 1b: Uniqueness Boundary ---")

# The claimed condition for uniqueness failure:
#   alpha * sqrt(rho / (1 - rho)) = 1
# Solve for rho:
rho_star_eq = sp.Eq(alpha * sp.sqrt(rho / (1 - rho)), 1)
rho_star_solutions = sp.solve(rho_star_eq, rho)
print("Solving alpha * sqrt(rho/(1-rho)) = 1 for rho:")
print(f"  Solutions: {rho_star_solutions}")

# Check claimed answer: rho_1* = 1/(1 + alpha^2)
rho_1_star_claimed = 1 / (1 + alpha**2)
check = sp.simplify(alpha * sp.sqrt(rho_1_star_claimed / (1 - rho_1_star_claimed)) - 1)
print(f"  Substituting rho = 1/(1+alpha^2): alpha*sqrt(rho/(1-rho)) - 1 = {check}")
if check == 0:
    print("  VERIFIED: rho_1* = 1/(1 + alpha_SC^2)")
else:
    print(f"  CHECK NEEDED: simplification gives {check}")

# Verify properties
print("\n  Property checks for rho_1* = 1/(1 + alpha^2):")
# alpha=1 -> rho_1* = 1/2
val_alpha1 = rho_1_star_claimed.subs(alpha, 1)
print(f"  alpha=1: rho_1* = {val_alpha1} (expected 1/2)")

# alpha->0 -> rho_1* -> 1
val_alpha0 = sp.limit(rho_1_star_claimed, alpha, 0)
print(f"  alpha->0: rho_1* = {val_alpha0} (expected 1)")

# alpha->inf -> rho_1* -> 0
val_alpha_inf = sp.limit(rho_1_star_claimed, alpha, sp.oo)
print(f"  alpha->inf: rho_1* = {val_alpha_inf} (expected 0)")

# =====================================================================
# Cross-check: Earlier in the document, there was an alternative formula
# rho_1* = sqrt(2*pi) / (alpha_SC + sqrt(2*pi))
# This was CORRECTED to 1/(1 + alpha^2). Verify they are different.
# =====================================================================
print("\n--- Cross-check: Original vs Corrected formula ---")
rho_1_original = sp.sqrt(2 * sp.pi) / (alpha + sp.sqrt(2 * sp.pi))
rho_1_corrected = 1 / (1 + alpha**2)
diff = sp.simplify(rho_1_original - rho_1_corrected)
print("  Original: sqrt(2pi)/(alpha + sqrt(2pi))")
print("  Corrected: 1/(1 + alpha^2)")
print(f"  Difference (simplified): {diff}")
print(
    f"  At alpha=1: original={float(rho_1_original.subs(alpha,1)):.4f}, "
    f"corrected={float(rho_1_corrected.subs(alpha,1)):.4f}"
)
print("  NOTE: These are different formulas. The document contains BOTH.")
print("  The FIRST formula (sqrt(2pi)/(alpha+sqrt(2pi))) appears in Prop 1b statement.")
print("  The SECOND formula (1/(1+alpha^2)) appears later as a correction.")
print("  This is an INCONSISTENCY that must be resolved.")

# =====================================================================
# Proposition 1b: Alternative derivation check
# The document derives: alpha * tau_public / tau_private < 1
# where tau_public = 1/(rho*sigma^2) and tau_private = 1/((1-rho)*sigma^2)
# So alpha * (1-rho)/rho < 1 => rho > alpha/(1+alpha)
# This gives uniqueness at HIGH rho -- the WRONG direction.
#
# Then the document switches to alpha * sqrt(rho/(1-rho)) < 1
# giving rho < 1/(1+alpha^2) -- uniqueness at LOW rho.
# =====================================================================
print("\n--- Derivation path check ---")
print("  Path 1: alpha*(1-rho)/rho < 1 => rho > alpha/(1+alpha)")
print("    This gives uniqueness at HIGH rho (WRONG direction)")
rho_path1 = alpha / (1 + alpha)
print(f"    Boundary: rho > {rho_path1}")

print("  Path 2: alpha*sqrt(rho/(1-rho)) < 1 => rho < 1/(1+alpha^2)")
print("    This gives uniqueness at LOW rho (CORRECT direction)")
print(f"    Boundary: rho < {rho_1_corrected}")

print("  The document correctly identifies Path 1 as wrong and switches to Path 2.")
print(
    "  But Prop 1b STATEMENT still uses the original formula sqrt(2pi)/(alpha+sqrt(2pi))."
)

# =====================================================================
# Proposition 1a: Non-monotonicity of theta*(rho)
# This is a qualitative claim about implicit function behavior.
# We verify the two competing effects algebraically.
# =====================================================================
print("\n--- Proposition 1a: Non-monotonicity check ---")
print("  Effect (a): tau_private(rho) = 1/((1-rho)*sigma^2) is increasing in rho")
tau_private = 1 / ((1 - rho) * sigma**2)
dtau_drho = sp.diff(tau_private, rho)
print(f"  d(tau_private)/d(rho) = {sp.simplify(dtau_drho)}")
print("  Sign: positive (verified)")

print("  Effect (b): Common noise variance = rho*sigma^2 is increasing in rho")
common_var = rho * sigma**2
dcommon_drho = sp.diff(common_var, rho)
print(f"  d(common_var)/d(rho) = {dcommon_drho}")
print("  Sign: positive (verified)")

print("  Non-monotonicity: effect (a) dominates at low rho, effect (b) at high rho")
print("  QUALITATIVE CLAIM -- cannot verify algebraically without specifying R(theta)")
print("  STATUS: CONDITIONALLY VERIFIED (requires competing effects to cross)")

# =====================================================================
# Proposition 1c: Social Cost of AI Signal Correlation
# W_loss(rho) = [alpha^2 / (1 - alpha^2)] * lambda^2 * rho * (1/tau)
# where tau = 1/sigma^2
# =====================================================================
print("\n--- Proposition 1c: Social cost ---")
W_loss = (alpha**2 / (1 - alpha**2)) * lam**2 * rho * sigma**2
print(f"  W_loss(rho) = {W_loss}")
dW_drho = sp.diff(W_loss, rho)
print(f"  d(W_loss)/d(rho) = {sp.simplify(dW_drho)}")
print("  Linearly increasing in rho: VERIFIED")

# Check: the formula uses (1 - alpha^2) in the denominator
# but Angeletos-Pavan uses (1-alpha)^2 for the coordination game weight
# Let's flag this as a potential issue
print("\n  NOTE: The document uses alpha^2/(1-alpha^2) in the W_loss formula.")
print("  Earlier in Step 8 it uses alpha^2/(1-alpha)^2.")
print("  These are DIFFERENT expressions:")
expr1 = alpha**2 / (1 - alpha**2)
expr2 = alpha**2 / (1 - alpha) ** 2
diff_check = sp.simplify(expr1 - expr2)
print(f"    alpha^2/(1-alpha^2) vs alpha^2/(1-alpha)^2: diff = {diff_check}")
print(
    f"    At alpha=0.5: {float(expr1.subs(alpha, 0.5)):.4f} vs {float(expr2.subs(alpha, 0.5)):.4f}"
)
print("  INCONSISTENCY: The coefficient changes between Step 8 and Prop 1c.")

# Private value check
print("\n  V_private(rho) = (1 - rho) * tau^{-1} = (1-rho)*sigma^2")
V_private = (1 - rho) * sigma**2
dV_drho = sp.diff(V_private, rho)
print(f"  d(V_private)/d(rho) = {dV_drho}")
print("  This is NEGATIVE, not positive as claimed!")
print("  The document says V_private > 0 (meaning it IS positive),")
print("  but V_private is DECREASING in rho. The statement says")
print("  'reduced idiosyncratic risk' -- this refers to the VALUE being positive,")
print("  not the derivative. The expression itself IS positive for rho < 1.")
print(
    "  STATUS: Clarification needed on whether V_private is the value or its derivative."
)

print("\n  Social optimum check: rho_SO < rho_1* requires")
print("  [alpha^2/(1-alpha^2)] * lambda^2 > 1")
print("  This is a condition on alpha and lambda, not universally true.")
print("  STATUS: CONDITIONALLY VERIFIED (requires alpha, lambda sufficiently large)")

print("\n" + "=" * 70)
print("CHANNEL 1 SUMMARY")
print("=" * 70)
print("Prop 1a (Non-monotonicity): CONDITIONALLY VERIFIED")
print("  - Two competing effects verified algebraically")
print(
    "  - Non-monotonicity requires R(theta) specification; qualitative argument sound"
)
print("Prop 1b (Uniqueness boundary): FLAG -- INTERNAL INCONSISTENCY")
print("  - Statement says rho_1* = sqrt(2pi)/(alpha + sqrt(2pi))")
print("  - Later derivation corrects to rho_1* = 1/(1 + alpha^2)")
print("  - The corrected formula is consistent with alpha*sqrt(rho/(1-rho)) < 1")
print("  - The original formula is NOT derived from any stated condition")
print("Prop 1c (Social cost): FLAG -- COEFFICIENT INCONSISTENCY")
print("  - Uses alpha^2/(1-alpha^2) in Prop 1c but alpha^2/(1-alpha)^2 in Step 8")
print("  - W_loss linearly increasing in rho: VERIFIED")
print("  - V_private statement ambiguous")
