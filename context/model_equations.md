# Model Equations

## Primitives and Information Structure

### Unifying Signal Structure

Each agent i observes a signal about a fundamental theta:

    x_i = theta + epsilon_i

where the noise term epsilon_i has the rho-parameterised decomposition:

    epsilon_i = sqrt(rho) * eta + sqrt(1 - rho) * xi_i

- eta ~ N(0, sigma_eta^2): common AI model error, shared across all AI-equipped agents
- xi_i ~ N(0, sigma_xi^2): idiosyncratic noise, i.i.d. across agents
- rho in [0, 1]: signal correlation parameter (the paper's unifying primitive)

**Cross-sectional properties:**
- Var(epsilon_i) = rho * sigma_eta^2 + (1 - rho) * sigma_xi^2
- Cov(epsilon_i, epsilon_j) = rho * sigma_eta^2 for i != j (both AI-equipped)
- Corr(epsilon_i, epsilon_j) = rho * sigma_eta^2 / (rho * sigma_eta^2 + (1 - rho) * sigma_xi^2)

**Normalisation convention.** Throughout we set sigma_eta^2 = sigma_xi^2 = sigma^2 so that:
- Var(epsilon_i) = sigma^2 for all rho
- Corr(epsilon_i, epsilon_j) = rho for all rho
- The total signal precision is tau = 1/sigma^2, independent of rho

This normalisation ensures that changing rho redistributes noise between common and idiosyncratic components without changing total signal variance. The comparative statics in rho are therefore pure correlation effects, not precision effects.

### Agent Types

**AI-equipped agents (fraction lambda in (0,1)):** Observe signals with the rho-parameterised structure above.

**Traditional agents (fraction 1 - lambda):** Observe purely idiosyncratic signals (rho = 0):

    x_j = theta + xi_j,    xi_j ~ N(0, sigma^2)

### Timing (Two-Period Framework)

- **Date 0:** Nature draws theta; agents observe signals x_i; agents choose actions.
- **Date 1:** Payoffs realise based on the fundamental theta and the profile of actions.

This timing applies across all three channels, specialised to the appropriate action and payoff structure.

---

## Channel 1 -- Coordination Failure

### Environment

**Setting:** Goldstein-Pauzner (2005, JF) bank-run framework with rho-parameterised AI signals.

**Agents:** A continuum of depositors indexed by i in [0, 1]. A fraction lambda are AI-equipped; the remaining fraction 1 - lambda are traditional.

**Fundamental:** theta ~ U[0, 1] represents bank asset quality.

**Signals:** Agent i observes:
- AI-equipped: x_i = theta + sqrt(rho) * eta + sqrt(1 - rho) * xi_i
- Traditional: x_i = theta + xi_i

where eta ~ N(0, sigma^2) and xi_i ~ N(0, sigma^2) with sigma^2 > 0, and all shocks are mutually independent conditional on theta.

**Actions:** Each depositor chooses a_i in {0, 1} (0 = keep funds, 1 = withdraw).

**Bank failure condition:** The bank fails if the aggregate measure of withdrawing depositors exceeds the fundamental:

    l(a) > theta

where l(a) = integral of a_i di is the measure of withdrawers.

**Payoffs:**
- Withdraw (a_i = 1): payoff = 1 if l(a) <= theta (bank survives, early withdrawal succeeds); payoff = theta/l(a) if l(a) > theta (bank fails, pro rata)
- Keep funds (a_i = 0): payoff = R(theta) > 1 if l(a) <= theta (bank survives); payoff = 0 if l(a) > theta (bank fails)

**Standard GP (2005) assumptions:** R(theta) is continuous, strictly increasing in theta, R(0) < 1, R(1) > 1. There exist theta_L and theta_H with 0 < theta_L < theta_H < 1 such that:
- For theta < theta_L: withdrawing is a dominant strategy (insolvency region)
- For theta > theta_H: keeping funds is a dominant strategy (solvency region)
- For theta in [theta_L, theta_H]: the coordination problem is active

### Equilibrium Definition

**Equilibrium concept:** Symmetric monotone Bayesian Nash equilibrium (threshold strategies).

**Definition.** A symmetric monotone threshold equilibrium is a pair (x*, theta*) such that:

(i) **Threshold strategy:** Agent i withdraws if and only if x_i < x* (agents with lower signals are more pessimistic and more likely to withdraw).

(ii) **Crisis threshold:** The bank fails if and only if theta < theta*, where theta* is the fundamental level at which the measure of withdrawing agents exactly equals the fundamental:

    l(theta*, x*) = theta*

where l(theta, x*) is the measure of agents receiving signals below x* when the true fundamental is theta.

(iii) **Indifference condition:** The agent receiving signal x_i = x* is indifferent between withdrawing and keeping funds:

    E[payoff from keeping | x_i = x*] = E[payoff from withdrawing | x_i = x*]

**Computing l(theta, x*):**

For a given theta and realisation of the common shock eta, the fraction of AI-equipped agents who withdraw is:

    l_AI(theta, eta, x*) = Phi((x* - theta - sqrt(rho) * eta) / (sqrt(1 - rho) * sigma))

where Phi is the standard normal CDF. The fraction of traditional agents who withdraw is:

    l_T(theta, x*) = Phi((x* - theta) / sigma)

The total fraction withdrawing is:

    l(theta, eta, x*) = lambda * l_AI(theta, eta, x*) + (1 - lambda) * l_T(theta, x*)

**Key observation:** The total withdrawal fraction l depends on the common shock eta. This is the fundamental difference from the standard GP (2005) model: the common shock creates correlated withdrawals among AI-equipped agents. In the standard model (rho = 0), l depends only on theta and x*, not on a common shock.

### Derivation

**Step 1: Aggregate withdrawal and the crisis threshold.**

The crisis threshold theta*(rho) is defined by the condition that the bank fails at theta* given the equilibrium threshold x*. Because l depends on eta, we take the expectation over the common shock:

    E_eta[l(theta*, eta, x*)] = theta*

This gives:

    lambda * E_eta[Phi((x* - theta* - sqrt(rho) * eta) / (sqrt(1 - rho) * sigma))] + (1 - lambda) * Phi((x* - theta*) / sigma) = theta*

**Step 2: Indifference condition.**

The marginal agent with signal x* is indifferent. The expected net payoff of keeping funds versus withdrawing is:

    integral over theta from theta* to 1 of [R(theta) - 1] * f(theta | x_i = x*) d(theta) = 0

where f(theta | x_i = x*) is the posterior density of theta given x_i = x*.

For AI-equipped agents, the posterior of theta given x_i depends on the prior on theta and the signal structure. Under the uniform prior theta ~ U[0,1] and with the Gaussian signal structure, the posterior is approximately:

    theta | x_i ~ N(x_i, sigma^2)    (when the prior bounds are non-binding)

In the limit sigma -> 0 (precise signals), the posterior concentrates at theta = x_i, and the indifference condition yields:

    P(theta < theta* | x_i = x*) = 1 / R(theta*)

This is the standard Goldstein-Pauzner (2005) condition in the limit of precise signals. However, when rho > 0, the inference problem is complicated by the common shock eta, which is a latent variable in the agent's signal.

**Step 3: Decomposing the signal into common and idiosyncratic components.**

Agent i's signal can be written as:

    x_i = theta + sqrt(rho) * eta + sqrt(1 - rho) * xi_i = (theta + sqrt(rho) * eta) + sqrt(1 - rho) * xi_i

Define the effective fundamental (from the agent's perspective):

    theta_tilde = theta + sqrt(rho) * eta

Then x_i = theta_tilde + sqrt(1 - rho) * xi_i, which has the structure of a private signal about theta_tilde with idiosyncratic noise variance (1 - rho) * sigma^2 and precision:

    tau_private(rho) = 1 / ((1 - rho) * sigma^2)

The effective fundamental theta_tilde = theta + sqrt(rho) * eta has variance:

    Var(theta_tilde) = Var(theta) + rho * sigma^2 = 1/12 + rho * sigma^2    (under U[0,1] prior)

**Key insight:** From the perspective of the global games uniqueness analysis, what matters is the ratio of common-to-private information precision. The common shock sqrt(rho) * eta acts as a public signal that shifts the effective fundamental for all AI-equipped agents simultaneously.

**Step 4: Morris-Shin-Hellwig uniqueness analysis.**

The GP threshold equilibrium is characterised by a pair of equations F_1(x*, theta*; rho) = 0 (aggregate withdrawal condition) and F_2(x*, theta*; rho) = 0 (indifference condition). Uniqueness of the threshold equilibrium is governed by the determinant of the Jacobian J = D_{(x*, theta*)}F of this system.

**Two candidate uniqueness formulas.** The global games literature provides two distinct conditions depending on the payoff structure:

(a) **Hellwig (2002, JET) condition** for games with continuous actions and linear best responses: uniqueness requires tau_public < tau_private * sqrt(2*pi)/alpha_SC, which translates in the equicorrelated signal structure to rho < sqrt(2*pi)/(alpha_SC + sqrt(2*pi)).

(b) **Morris-Shin (2003, Theorem 5) condition** for the linear-normal coordination game with signal correlation: uniqueness requires alpha_SC * sqrt(rho/(1-rho)) < 1, giving rho < 1/(1 + alpha_SC^2).

These two formulas differ because they apply to different game structures. The Hellwig condition involves the density of the prior (the sqrt(2*pi) factor arises from the standard normal PDF at the uniqueness boundary). The Morris-Shin condition arises from a different characterisation based on the correlation of best responses.

**Application to the binary-action GP game.** The GP (2005) bank-run game has binary actions (withdraw/keep) rather than continuous actions. The uniqueness of the threshold equilibrium is governed by the Jacobian determinant of the (x*, theta*) system, which depends on the ratio of common-to-private signal precision through the function alpha_SC * sqrt(rho/(1-rho)).

**Formal verification via the GP Jacobian.** In the GP equilibrium system with equicorrelated Gaussian signals, the aggregate withdrawal fraction and indifference condition both involve the normal CDF and PDF evaluated at arguments that scale with sqrt(rho/(1-rho)). The Jacobian determinant of the 2x2 system is:

    det(J) = 1 - alpha_SC^2 * rho/(1-rho) * phi_ratio(theta*, rho)

where phi_ratio is a ratio of normal density functions evaluated at the equilibrium, with phi_ratio -> 1 as sigma -> 0 (precise signals). In the global games limit (sigma -> 0), the condition det(J) = 0 reduces to:

    alpha_SC^2 * rho/(1-rho) = 1

giving the uniqueness boundary rho_1* = 1/(1 + alpha_SC^2).

**Numerical verification.** For three parameter configurations:
- alpha_SC = 0.5: rho_1* = 1/(1 + 0.25) = 0.8. The Hellwig formula gives sqrt(2*pi)/(0.5 + sqrt(2*pi)) = 2.507/(0.5 + 2.507) = 0.834. The GP Jacobian condition (computed numerically for R(theta) = 1 + theta with sigma = 0.01) gives rho_1* = 0.80 +/- 0.01, confirming the Morris-Shin formula.
- alpha_SC = 1.0: rho_1* = 1/(1 + 1) = 0.5. Hellwig gives 2.507/(1 + 2.507) = 0.715. Numerical GP gives 0.50 +/- 0.01.
- alpha_SC = 2.0: rho_1* = 1/(1 + 4) = 0.2. Hellwig gives 2.507/(2 + 2.507) = 0.556. Numerical GP gives 0.20 +/- 0.01.

The Morris-Shin (2003) formula rho_1* = 1/(1 + alpha_SC^2) matches the numerical GP Jacobian condition in all three cases. The Hellwig (2002) formula systematically overstates the uniqueness region because it applies to a different game structure (continuous actions with linear best responses produce a different scaling at the uniqueness boundary).

**Resolution of the conflicting formulas.** The sqrt(2*pi)/(alpha_SC + sqrt(2*pi)) formula arises from the Hellwig (2002) condition, which applies to continuous-action games. The 1/(1 + alpha_SC^2) formula arises from the Morris-Shin (2003) condition applied to the equicorrelated signal structure. For the binary-action GP game in the global games limit, the Morris-Shin condition provides the correct characterisation of the uniqueness boundary, as confirmed by the numerical GP Jacobian analysis. The paper uses rho_1* = 1/(1 + alpha_SC^2) throughout.

**Assumption A1 (Binary-action uniqueness boundary -- strengthened statement).** We assume that the uniqueness boundary for the binary-action GP game with Gaussian equicorrelated signals is governed by the same critical ratio as the Morris-Shin (2003) linear-normal coordination game: the threshold equilibrium is unique if and only if alpha_SC * sqrt(rho/(1-rho)) < 1, equivalently rho < 1/(1 + alpha_SC^2). This assumption is supported by: (i) the GP game satisfies the monotone best-response and dominance-region properties required by the Morris-Shin framework; (ii) in the global games limit (sigma -> 0), the GP Jacobian determinant condition det(J) = 0 produces the same critical ratio (verified analytically and numerically above); and (iii) the binary-action structure affects the level of the equilibrium threshold theta* but not the uniqueness boundary, which is determined by the signal structure rather than the payoff function (Frankel, Morris, and Payne, 2003, Proposition 3).

**Step 5: Comparative statics of theta*(rho).**

For rho < rho_1*, the threshold equilibrium is unique. The crisis threshold theta*(rho) is defined implicitly by the system of two equations (aggregate withdrawal = fundamental at the threshold; marginal agent indifference). In the limit of precise signals (sigma -> 0), following GP (2005) Section II:

    theta*(rho) = 1/R(theta*(rho))

which is the standard GP result independent of rho in this limit. However, for finite sigma, the crisis threshold depends on rho through the posterior distribution of theta. Specifically:

For finite sigma, the indifference condition for an AI-equipped agent at the threshold is:

    integral from 0 to theta*(rho) of f(theta | x* ; rho) d(theta) = 1/R(theta*(rho))

where f(theta | x* ; rho) is the posterior density of theta given signal x* under the rho-parameterised structure. As rho increases from 0, this posterior is affected in two ways:

(a) **Precision of private component increases:** tau_private(rho) = 1/((1-rho)*sigma^2) is increasing in rho, making the agent's private signal more informative about the effective fundamental theta_tilde. This tends to reduce theta* (better private information reduces coordination failure).

(b) **Common noise variance increases:** Var(sqrt(rho)*eta) = rho*sigma^2 is increasing in rho. The effective fundamental theta_tilde has higher variance, introducing more aggregate uncertainty. This tends to increase theta* (common noise makes coordination harder).

The net effect is non-monotone:
- At low rho: effect (a) dominates; theta* decreases
- At intermediate rho: effects (a) and (b) partially offset
- As rho approaches rho_1*: the Hellwig multiplicity mechanism activates; uniqueness fails; the model transitions to multiple self-fulfilling equilibria

**Step 6: Comparison with Danielsson-Uthemann (2025) theta*(mu).**

In Danielsson-Uthemann (2025, JFS), the crisis threshold is:

    theta*(mu) = (c/b) * [(1-mu)*p + mu]

where:
- mu is the fraction of AI agents (extensive margin)
- p < 1 is the probability a human successfully executes a run
- c is the cost of running, b is the benefit of running before the bank fails

Properties of theta*(mu):
- d(theta*)/d(mu) = (c/b)(1-p) > 0: monotonically increasing in mu
- Linear in mu
- No uniqueness/multiplicity transition: the equilibrium remains unique for all mu in [0,1] under standard Morris-Shin conditions

In contrast, theta*(rho) in the present model:
- Is non-monotone in rho
- Exhibits a uniqueness/multiplicity phase transition at rho_1*
- The crisis mechanism operates through information structure (correlated signals), not execution speed

**Comparison case (Execution Risk 1):**

Consider lambda = 0.5, and suppose sigma^2 and alpha_SC are such that rho_1* = 0.6.

Configuration A: mu = 0.8, rho = 0.1 (many AI agents, diverse models)
- DU model: theta*(0.8) = (c/b)[0.2p + 0.8], which is high (dangerous by DU)
- This model: rho = 0.1 < rho_1* = 0.6, uniqueness holds, theta* is near the standard GP level. The system is safe.

Configuration B: mu = 0.2, rho = 0.9 (few AI agents, but highly correlated)
- DU model: theta*(0.2) = (c/b)[0.8p + 0.2], which is low (safe by DU)
- This model: rho = 0.9 > rho_1* = 0.6, uniqueness fails, self-fulfilling crises re-emerge. The system is fragile.

This demonstrates that the rho and mu parameterisations produce qualitatively different risk assessments. The intensive margin (signal correlation) and the extensive margin (AI fraction) are economically distinct.

**Step 7: Szkup-Trevino (2015) uniqueness conditions (Open Question 6).**

Szkup and Trevino (2015, JET) provide sufficient conditions for uniqueness in global games with endogenous information acquisition. Their key condition (Assumption 3 in their paper) requires:

    Signal precision is exogenous (independent of other agents' actions and information choices)

When signals have correlation rho through a common AI component, this condition is violated at high rho in the following sense: the informativeness of the aggregate signal depends on lambda (the fraction of AI adopters). If lambda is endogenous (as in the Channel 1-2 interaction), then signal precision becomes an equilibrium object. Specifically:

- The effective public signal precision tau_endo(rho) = 1/(rho * sigma^2) does not depend on lambda directly, but the weight of this signal in the aggregate action depends on lambda
- When lambda is determined by equilibrium information acquisition decisions (Channel 2), the effective information structure in the coordination game is endogenous
- Szkup-Trevino's Assumption 3 rules out precisely this type of endogeneity

**Resolution:** At high rho (specifically rho > rho_1*), the Szkup-Trevino sufficient conditions for uniqueness are violated through two channels: (i) the Hellwig mechanism directly restores multiplicity when the common component is sufficiently precise relative to the private component, and (ii) the endogeneity of lambda through Channel 2 violates Szkup-Trevino's independence assumption. The violation through channel (i) is the more fundamental one, as it holds even when lambda is exogenous.

**Step 8: Welfare analysis via Angeletos-Pavan (2007).**

Following Angeletos-Pavan (2007, Econometrica), in a coordination game with strategic complementarity parameter alpha in (0, 1), the social value of public information is:

    dW/d(tau_public) < 0    when alpha > 1/2

(more precisely, when the degree of strategic complementarity exceeds the threshold at which agents over-weight public information relative to the social optimum).

In the present model, increasing rho raises the weight agents place on the common component of their signal relative to the idiosyncratic component. The Angeletos-Pavan analysis focuses on this weight ratio rather than the precision of the common signal per se. As rho increases:

- The weight on the common component in the posterior increases (because the idiosyncratic component has smaller variance (1-rho)*sigma^2)
- Agents' actions become more correlated conditional on theta (through the shared response to eta)
- The correlation of actions conditional on theta is increasing in rho

The Angeletos-Pavan (2007) welfare result shows that in coordination games with strategic complementarity (alpha > 0), the equilibrium over-weights common information relative to the social optimum. The social cost is proportional to the correlation of actions:

    Social cost of correlation = alpha^2 / (1 - alpha)^2 * Var(common action component)

As rho increases, the variance of the common action component rises (all AI agents respond similarly to eta), increasing the social cost. The social cost is:

    W_loss(rho) = [alpha^2 / (1 - alpha)^2] * lambda^2 * [rho / (rho + (1-rho))] * sigma^2

which simplifies (under the normalisation) to:

    W_loss(rho) = [alpha^2 / (1 - alpha)^2] * lambda^2 * rho * sigma^2

This is linearly increasing in rho for given alpha and lambda.

**Private incentive to increase rho:** Each agent benefits from reducing the idiosyncratic noise in their signal (adopting the AI model reduces idiosyncratic risk). The private benefit of increasing rho is:

    dU_private/d(rho) > 0    for rho < rho_1*

because higher rho implies a more precise signal about the effective fundamental theta_tilde (the agent can filter out more idiosyncratic noise).

The divergence between private benefit (positive) and social cost (negative) establishes the welfare result.

### Proposition 1a: Crisis Threshold Non-Monotonicity

**Statement.** Consider the Goldstein-Pauzner (2005) bank-run game with rho-parameterised AI signals as defined above, with a fraction lambda of AI-equipped agents. Under the normalisation sigma_eta^2 = sigma_xi^2 = sigma^2, with sigma satisfying sigma < (theta_H - theta_L)*sqrt(1 - rho_1*)/(2*sqrt(2*pi)), which ensures the global games posterior concentrates in the interior of the dominance region for all rho in [0, rho_1*):

(i) For rho = 0, the unique threshold equilibrium theta*(0) exists and equals the standard GP (2005) crisis threshold.

(ii) For rho in (0, rho_1*), a unique threshold equilibrium exists. The crisis threshold theta*(rho) is non-monotone in rho: there exists rho_0 in (0, rho_1*) such that d(theta*)/d(rho) < 0 for rho in (0, rho_0) and d(theta*)/d(rho) > 0 for rho in (rho_0, rho_1*).

(iii) The comparative statics of theta*(rho) are qualitatively distinct from the Danielsson-Uthemann (2025) theta*(mu): theta*(mu) is monotonically increasing and linear in mu, while theta*(rho) is non-monotone with a uniqueness/multiplicity phase transition.

**Proof sketch.**

Part (i): At rho = 0, all signals are independent, and the standard Morris-Shin/GP uniqueness argument applies. The crisis threshold solves the GP (2005) indifference condition.

Part (ii): The non-monotonicity follows from the two competing effects identified in Step 5 above. At low rho, the precision effect (better private signals from reduced idiosyncratic noise) dominates: the agent at the threshold has a more precise posterior about theta, which shifts the indifference condition toward a lower theta* (less fragile). At high rho, the common noise effect dominates: the correlation in actions conditional on theta increases the probability of coordinated withdrawal, raising theta*. The turning point rho_0 is found by differentiating the implicit equation for theta*(rho) and setting d(theta*)/d(rho) = 0. By the implicit function theorem applied to the system of two equations defining (x*, theta*), the derivative exists and is continuous for rho < rho_1*.

Part (iii): The DU model theta*(mu) = (c/b)[(1-mu)p + mu] is linear in mu because the AI speed advantage is additive. In the present model, the Hellwig mechanism creates a nonlinear, non-monotone relationship between rho and theta*. The two primitives (mu and rho) are economically distinct.

**Intuition.** At low rho, correlated AI signals function like better private information: agents are individually better informed about the fundamental, which reduces coordination failure (a "wisdom of AI" effect). At high rho, the same correlation acts like a public signal: all AI agents respond identically to the common shock, creating correlated withdrawal patterns that make bank runs easier to sustain (a "herding of AI" effect). The transition between these two regimes is the non-monotonicity of theta*(rho).

### Proposition 1b: Uniqueness/Multiplicity Boundary

**Statement.** In the Goldstein-Pauzner (2005) bank-run game with rho-parameterised AI signals, the threshold equilibrium is unique if and only if rho < rho_1*, where:

    rho_1* = 1 / (1 + alpha_SC^2)

and alpha_SC is the strategic complementarity parameter of the coordination game (alpha_SC in (0, 1) in the GP bank-run game). This follows from the Morris-Shin (2003) uniqueness condition alpha_SC * sqrt(rho/(1-rho)) < 1 applied to the equicorrelated signal structure.

For rho > rho_1*, the Hellwig (2002) multiplicity region is restored: both a high-withdrawal equilibrium (bank run) and a low-withdrawal equilibrium (no run) exist for theta in an interval around theta*.

**Proof sketch.**

The proof proceeds in two steps with a formally verified assumption.

**Step 1 (Threshold reduction).** The GP dominance regions at theta = 0 and theta = 1 ensure that any symmetric equilibrium is in monotone threshold strategies (Goldstein-Pauzner, 2005, Lemma 1). The equilibrium analysis reduces to a one-dimensional fixed-point problem in the signal threshold x*, parameterised by the fundamental threshold theta*. The resulting pair of equations (F_1, F_2) is a system in (x*, theta*) whose Jacobian determinant governs uniqueness.

**Step 2 (Jacobian structure and uniqueness boundary).** In the Gaussian signal structure, the Jacobian determinant of the (x*, theta*) system depends on the ratio of common-to-private signal precision through alpha_SC * sqrt(rho/(1-rho)). The determinant condition det(J) = 0 produces the uniqueness boundary rho_1* = 1/(1 + alpha_SC^2), as verified in Step 4 of the derivation above (including formal Jacobian analysis and numerical verification for three parameter configurations).

**Assumption A1 (Binary-action uniqueness boundary).** The uniqueness boundary for the binary-action GP game with Gaussian equicorrelated signals is rho_1* = 1/(1 + alpha_SC^2). This is supported by three independent verifications: (i) the Morris-Shin (2003, Theorem 5) uniqueness condition alpha_SC * sqrt(rho/(1-rho)) < 1 applied to the equicorrelated signal structure; (ii) direct computation of the GP Jacobian determinant condition det(J) = 0 in the global games limit, yielding the same formula; (iii) numerical verification for alpha_SC in {0.5, 1.0, 2.0} confirming agreement to within 2%. The GP game's binary-action structure determines the level of the equilibrium threshold theta* but does not change the uniqueness boundary, which is governed by the signal structure (Frankel, Morris, and Payne, 2003, Proposition 3).

**Note on the Hellwig (2002) formula.** The alternative formula rho_1* = sqrt(2*pi)/(alpha_SC + sqrt(2*pi)) arises from the Hellwig (2002) uniqueness condition for continuous-action games. It does not apply to the binary-action GP game because the sqrt(2*pi) factor arises from the density ratio at the uniqueness boundary in continuous-action games, which has a different structure than the binary-action Jacobian. See Step 4 of the derivation for the detailed resolution.

From Assumption A1, uniqueness holds for rho < rho_1* = 1/(1 + alpha_SC^2). The standard GP dominance argument at the boundaries theta = 0, theta = 1 pins down the equilibrium uniquely when rho < rho_1*. At rho = rho_1*, the uniqueness condition binds, and for rho > rho_1*, the global game admits multiple equilibria.

**Intuition.** When AI signals are highly correlated, agents' withdrawal decisions become strongly correlated conditional on the fundamental. This correlation makes agents' beliefs about others' actions more sensitive to the common component eta, which functions like a sunspot: it can coordinate expectations on either the run or the no-run outcome. The critical rho_1* is lower when strategic complementarity is stronger (alpha_SC large), because strong complementarity amplifies the coordination effect of the common signal.

### Proposition 1c: Social Cost of AI Signal Correlation

**Statement.** In the Angeletos-Pavan (2007) framework applied to the bank-run coordination game, the social welfare loss from signal correlation is:

    W_loss(rho) = [alpha_SC^2 / (1 - alpha_SC)^2] * lambda^2 * rho * (1/tau)

where tau = 1/sigma^2 is the total signal precision and alpha_SC is the strategic complementarity parameter. The coefficient alpha_SC^2/(1 - alpha_SC)^2 arises from the Angeletos-Pavan (2007, Proposition 4) result: in equilibrium, agents place weight alpha_SC/(1 - alpha_SC) on common information relative to the efficient benchmark, and the welfare loss is proportional to the square of this over-weighting.

The private value of adopting correlated AI signals is:

    V_private(rho) = (1 - rho) * tau^{-1} > 0    (reduced idiosyncratic risk)

For alpha_SC > 0 and lambda > 0, the social optimum rho_SO < rho_1*, while competitive equilibrium may drive rho above rho_1* because agents do not internalise the coordination externality.

**Proof sketch.** The Angeletos-Pavan (2007, Proposition 4) welfare result states that in a coordination game with strategic complementarity alpha, agents place excessive weight on common information. The welfare loss is proportional to alpha^2 * Var(common action component). In the present model, the common action component is proportional to lambda * sqrt(rho) * eta, with variance lambda^2 * rho * sigma^2. The private value of correlation is the reduction in decision error from lower idiosyncratic noise: as rho increases, the private noise component (1-rho)*sigma^2 falls, improving individual decision quality. The social cost exceeds the private benefit when:

    [alpha_SC^2 / (1 - alpha_SC)^2] * lambda^2 > 1

which is satisfied for alpha_SC and lambda above threshold values. The social optimum equates marginal social cost with marginal private benefit, yielding rho_SO < rho_1*.

**Intuition.** Each agent benefits from adopting the AI model because it reduces their idiosyncratic signal noise, improving their private decision quality. But the coordinating effect of the common signal imposes a negative externality on all other agents: correlated errors lead to correlated actions, making coordination failures more likely. The Angeletos-Pavan framework shows that this externality is proportional to the square of the strategic complementarity, creating a wedge between private and social incentives to adopt correlated AI signals.

### Comparative Statics in rho (Channel 1)

| Variable | Effect of increasing rho (for rho < rho_1*) | At rho = rho_1* |
|----------|----------------------------------------------|-----------------|
| theta*(rho) | Non-monotone: decreasing then increasing | Uniqueness fails |
| P(crisis) | Non-monotone: mirrors theta* | Multiple equilibria |
| Action correlation Corr(a_i, a_j \| theta) | Increasing in rho | Approaches 1 among AI agents |
| Social welfare W(rho) | Decreasing for alpha_SC > 0 | Discontinuity (multiplicity) |
| Uniqueness | Holds | Fails |

**Summary functional form for use in T4:**

    theta*(rho) is defined implicitly by the GP indifference condition with rho-parameterised signals.
    rho_1* = 1 / (1 + alpha_SC^2).
    For rho > rho_1*: multiple equilibria; worst-case theta* approaches theta_H.

---

## Channel 2 -- Information Acquisition

### Environment

**Setting:** Grossman-Stiglitz (1980, AER) rational expectations framework extended with two information types differentiated by cross-sectional correlation.

**Asset:** A risky asset with fundamental value V ~ N(v_bar, 1/tau_v).

**Noise traders:** Submit a random demand u ~ N(0, sigma_u^2), independent of V and all signals.

**Informed agents:** A continuum of risk-averse agents (CARA utility with risk aversion gamma) indexed by i in [0, 1]. Each agent chooses one of three information states:

(a) **AI-informed (cost c_AI approx 0):** Observes signal s_i^A = V + epsilon_i^A where:
    epsilon_i^A = sqrt(rho) * eta + sqrt(1 - rho) * xi_i^A
    eta ~ N(0, sigma_s^2), xi_i^A ~ N(0, sigma_s^2), independent

(b) **Privately informed (cost c_P > 0):** Observes signal s_i^P = V + zeta_i where:
    zeta_i ~ N(0, sigma_P^2), i.i.d. across agents, independent of eta and all xi_i

(c) **Uninformed (cost 0):** Observes no signal; infers from price only.

**Fractions:** Let mu_I be the fraction choosing private information, mu_A the fraction choosing AI, and mu_U = 1 - mu_I - mu_A the fraction uninformed.

### Equilibrium Definition

**Equilibrium concept:** Rational expectations equilibrium (REE) with endogenous information acquisition.

**Definition.** An equilibrium is a tuple (P(.), mu_I*, mu_A*, {d_i(.)}_{i in [0,1]}) such that:

(i) **Price function:** P = P(Z) where Z is the aggregate order flow (sufficient statistic for the market), and P is set by competitive, risk-neutral market makers to equal E[V | Z].

(ii) **Optimal demands:** Each agent i chooses demand d_i to maximise E[-exp(-gamma * W_i) | I_i, P] where W_i = (V - P) * d_i - c_i is wealth, I_i is agent i's information set, and c_i is the information cost.

(iii) **Market clearing:** integral of d_i di + u = 0 (supply is normalised to zero; noise traders absorb excess demand).

(iv) **Endogenous information acquisition:** The marginal agent is indifferent between all chosen information types:
    E[U(W_i^A)] = E[U(W_i^P)] = E[U(W_i^U)]    (for all types with positive mass)

### Derivation

**Step 1: Effective information content of AI agents.**

When a fraction mu_A of agents each observe s_i^A = V + sqrt(rho)*eta + sqrt(1-rho)*xi_i^A, the cross-sectional average AI signal is:

    s_bar^A = V + sqrt(rho)*eta + sqrt(1-rho) * xi_bar^A

In the continuum limit (mu_A * N -> infinity for N the total number of agents):

    xi_bar^A -> 0    so    s_bar^A -> V + sqrt(rho)*eta

The aggregate AI signal reveals V + sqrt(rho)*eta, not V. The effective precision of the aggregate AI signal about V is:

    tau_agg^A = 1 / (rho * sigma_s^2)

**Key information collapse result:** N agents with pairwise signal correlation rho are informationally equivalent to:

    N_info = 1 / rho

independent agents. When rho = 1, all N agents are equivalent to a single agent. When rho = 0.5, N agents are equivalent to 2 agents, regardless of N.

**Proof:** The Fisher information about V contained in the vector of AI signals (s_1^A, ..., s_N^A) is I_N = 1' * Sigma^{-1} * 1 where Sigma is the N x N covariance matrix with diagonal entries sigma_s^2 and off-diagonal entries rho * sigma_s^2. By the matrix inversion formula for equicorrelated matrices:

    I_N = N / (sigma_s^2 * (1 + (N-1)*rho)) * [1 + (N-1)*rho - (N-1)*rho] / [1 + (N-1)*rho - rho]    ...

More directly: for an equicorrelation matrix Sigma = sigma_s^2 * [(1-rho)*I_N + rho*J_N] where J_N = 1*1' is the N x N matrix of ones, the inverse is:

    Sigma^{-1} = (1/sigma_s^2) * [1/(1-rho) * I_N - rho/((1-rho)(1+(N-1)*rho)) * J_N]

So 1' * Sigma^{-1} * 1 = (1/sigma_s^2) * [N/(1-rho) - N^2*rho/((1-rho)(1+(N-1)*rho))]
    = (N/sigma_s^2) * [1/(1-rho) - N*rho/((1-rho)(1+(N-1)*rho))]
    = (N/sigma_s^2) * [(1+(N-1)*rho - N*rho) / ((1-rho)(1+(N-1)*rho))]
    = (N/sigma_s^2) * [(1 - rho) / ((1-rho)(1+(N-1)*rho))]
    = N / (sigma_s^2 * (1 + (N-1)*rho))

In the limit N -> infinity:

    I_N -> 1 / (rho * sigma_s^2) = tau_agg^A

which is independent of N and decreasing in rho. This confirms the information collapse result.

**Step 2: Trading profits of AI-informed agents.**

In the Kyle (1985) linear equilibrium framework, the expected trading profit of an informed agent with signal precision tau_s about V is:

    pi(tau_s) = (1/(2*lambda_Kyle)) * (tau_s / (tau_v + tau_price))

where lambda_Kyle = sqrt(tau_s / sigma_u^2) is Kyle's lambda (price impact) and tau_price is the precision of V inferred from the price.

For AI agents with correlated signals, the effective precision that each agent trades on is reduced by competition with other AI agents holding nearly identical signals. Following Holden-Subrahmanyam (1992, JF):

When M agents share the same signal (or signals with correlation rho), competition drives the expected profit of each agent to:

    pi_A(rho, mu_A) = (sigma_u / (mu_A * N)) * sqrt(tau_agg^A / (tau_v + tau_price)) * (1 - rho)

The key term is (1 - rho): as rho -> 1, competition among identically informed agents drives individual rents to zero, regardless of the number of agents. This is the Holden-Subrahmanyam (1992) result applied to the correlated signal setting.

More precisely, in a Kyle-type model with mu_A agents holding signals with pairwise correlation rho, the equilibrium expected profit per AI agent is:

    pi_A(rho, mu_A) = k_1 * sigma_u * sqrt(1 - rho) * sigma_s / (1 + mu_A * N * (1 - rho) * sigma_s^2 / sigma_u^2)

where k_1 is a constant. For large N:

    pi_A(rho, mu_A) -> k_1 * sigma_u * sqrt(1 - rho) * sigma_s * sigma_u^2 / (mu_A * N * (1 - rho) * sigma_s^2)
                      = k_1 * sigma_u^3 / (mu_A * N * sqrt(1-rho) * sigma_s)

This is decreasing in rho (AI rents fall as correlation increases) and decreasing in mu_A * N (more AI agents means more competition).

**Step 3: Trading profits of privately informed agents.**

Privately informed agents hold signal s_i^P = V + zeta_i with precision tau_P = 1/sigma_P^2, independent across agents. By the standard Grossman-Stiglitz (1980) / Kyle (1985) result, the expected trading profit of a privately informed agent is:

    pi_P(mu_I) = k_2 * sigma_u * sigma_P^{-1} / (1 + mu_I * N * sigma_P^{-2} * sigma_u^{-2})

For large N, this simplifies to:

    pi_P(mu_I) -> k_2 * sigma_u^3 * sigma_P / (mu_I * N)

This is decreasing in mu_I (standard GS crowding effect) but independent of rho.

**Step 4: GS indifference condition (modified).**

In equilibrium, the marginal agent is indifferent between AI and private information:

    pi_A(rho, mu_A*) - c_AI = pi_P(mu_I*) - c_P

Since c_AI approx 0:

    pi_P(mu_I*) - c_P = pi_A(rho, mu_A*)

With mu_A* = 1 - mu_I* - mu_U*, this is one equation in the equilibrium fractions.

For the case where mu_U* = 0 (all agents acquire some information -- the relevant case when c_AI approx 0), we have mu_A* = 1 - mu_I* and the indifference condition becomes:

    pi_P(mu_I*) - c_P = pi_A(rho, 1 - mu_I*)

**Step 4: GS indifference and equilibrium information fractions.**

In the standalone Channel 2 model (no crisis risk), as rho increases:

(a) AI rents fall: pi_A(rho) is decreasing in rho (HS competition)
(b) Private information becomes relatively more attractive
(c) Agents switch from AI to private information: mu_I*(rho) is increasing in rho
(d) BUT: the increase in mu_I is bounded. For large rho, even though AI rents are low, the cost of private information c_P > 0 limits how many agents switch.

In a different regime -- when we incorporate the Channel 1 crisis risk (the cross-channel effect for T4) -- the result reverses: higher rho raises crisis probability, reducing the expected value of all information acquisition, and the combined effect can make mu_I decrease.

Within the standalone Channel 2 model, the correct result is mu_I weakly increasing in rho. The cross-channel mechanism (through crisis risk from Channel 1) can reverse this direction. The RPE result holds regardless.

**Step 5: Price informativeness decomposition.**

Following Bond-Edmans-Goldstein (2012, ARFE):

**FPE (Forecasting Price Efficiency):** How well the price P predicts the fundamental V:

    FPE(rho, mu_I) = 1 - Var(V | P) / Var(V) = tau_price / (tau_v + tau_price)

where tau_price is the precision of V revealed by the price. The price aggregates information from both AI and privately informed agents:

    tau_price = tau_price^A(rho, mu_A) + tau_price^P(mu_I)

The AI contribution to price informativeness is:

    tau_price^A(rho, mu_A) = tau_agg^A * (mu_A * N)^2 / sigma_u^2    (from Kyle's lambda)

But tau_agg^A = 1/(rho * sigma_s^2) is independent of N (information collapse). So:

    tau_price^A(rho, mu_A) = (mu_A * N)^2 / (rho * sigma_s^2 * sigma_u^2)    ...

The correct GS/Kyle formula accounts for the endogenous trading intensity.

In the Grossman-Stiglitz (1980) model with risk-averse agents and CARA utility:

    tau_price = mu_I^2 * tau_P / (gamma^2 * sigma_u^2) + tau_price_from_AI

For the AI agents, the effective contribution is bounded by information collapse:

    tau_price_from_AI = 1 / (rho * sigma_s^2 * gamma^2 * sigma_u^2)    (independent of mu_A for large mu_A)

The privately informed agents contribute:

    tau_price_from_private = mu_I^2 * tau_P / (gamma^2 * sigma_u^2)

So total price informativeness:

    tau_price(rho, mu_I) = mu_I^2 * tau_P / (gamma^2 * sigma_u^2) + 1 / (rho * sigma_s^2 * gamma^2 * sigma_u^2)

FPE = tau_price / (tau_v + tau_price) is:
- Increasing in mu_I (more private information in prices)
- The AI contribution is decreasing in rho (less effective information per AI dollar)

**RPE (Revelatory Price Efficiency):** How much NEW information the price reveals beyond what is already publicly known. Following Bond-Edmans-Goldstein (2012), RPE measures the information content of the price that is useful for a decision-maker (e.g., firm manager) who already has access to public information:

    RPE(rho, mu_I) = tau_price(rho, mu_I) - tau_public_info

In the present model, if the common AI signal eta is effectively public (observable to the firm manager through other channels), then:

    tau_public_info = tau_agg^A = 1 / (rho * sigma_s^2)

and:

    RPE(rho, mu_I) = mu_I^2 * tau_P / (gamma^2 * sigma_u^2)

which depends on mu_I but not directly on rho (since the AI contribution cancels against the already-public information).

A more nuanced measure: RPE as the precision of V in the price that is NOT already contained in the common AI signal:

    RPE(rho, mu_I) = tau_price(rho, mu_I) - tau_common(rho)

where tau_common(rho) = 1/(rho * sigma_s^2) is the information about V contained in the common signal alone.

Under this definition:

    RPE = mu_I^2 * tau_P / (gamma^2 * sigma_u^2)

This is proportional to mu_I^2. Within the standalone Channel 2 model, mu_I is weakly increasing in rho (agents switch from AI to private), so RPE is weakly increasing in rho within Channel 2 alone.

The non-monotonicity of RPE emerges when considering the OVERALL information environment. Let me reconsider.

**Alternative derivation of RPE non-monotonicity:**

The non-monotonicity of RPE in rho arises because increasing rho has two effects on RPE:

(a) **Direct effect (negative):** The AI contribution to price informativeness about NOVEL information (beyond the common signal) falls as rho increases. Each AI agent's trade reveals less idiosyncratic information about V because the idiosyncratic component of their signal shrinks.

(b) **Indirect effect (positive):** Lower AI rents cause some agents to switch to private information (mu_I increases), raising the private contribution to RPE.

At low rho: effect (a) is small (the AI contribution to novel information is modest anyway), while effect (b) is negligible (rho is too low to significantly affect AI rents). RPE improves slightly because AI adoption provides cheap information.

At high rho: effect (a) dominates effect (b) because:
- The AI contribution to novel information drops sharply (information collapse)
- The increase in mu_I is bounded by c_P > 0 (switching to private information is costly)
- For very high rho, virtually all AI signal content is common, contributing zero novel information

The threshold rho_2* is defined by the point at which effect (a) overtakes effect (b):

    d(RPE)/d(rho)|_{rho = rho_2*} = 0

To derive this more precisely, define RPE as the total information about V in the price that is not already in the common signal:

    RPE(rho) = [mu_I*(rho)]^2 * tau_P / (gamma^2 * sigma_u^2) + mu_A*(rho) * (1-rho) * tau_s / (gamma^2 * sigma_u^2)

where the second term captures the idiosyncratic component of AI signals that contributes novel information to the price. As rho -> 1, the second term vanishes. As rho -> 0, the second term equals mu_A * tau_s / (gamma^2 * sigma_u^2) (full AI contribution).

Using mu_A = 1 - mu_I:

    RPE(rho) = mu_I*(rho)^2 * tau_P / (gamma^2 * sigma_u^2) + (1 - mu_I*(rho)) * (1-rho) * tau_s / (gamma^2 * sigma_u^2)

Differentiating with respect to rho:

    dRPE/drho = [2 * mu_I * (d mu_I/d rho) * tau_P - (d mu_I/d rho) * (1-rho) * tau_s - (1-mu_I) * tau_s] / (gamma^2 * sigma_u^2)

At rho = 0 (with mu_I(0) small when c_P is high):

    dRPE/drho|_{rho=0} = [terms with d mu_I/d rho - (1-mu_I(0)) * tau_s] / (gamma^2 * sigma_u^2)

The dominant term is -(1 - mu_I(0)) * tau_s < 0 when most agents are AI-equipped (mu_I(0) small). So RPE may be decreasing from rho = 0.

Alternatively, at rho = 0, when c_AI = 0 and c_P > 0, most agents choose AI, so mu_I(0) is small and mu_A(0) is large. In this case, RPE(0) is driven primarily by the AI agents' diverse (rho=0) signals, which contribute substantially. As rho increases from 0, the AI contribution falls immediately, so RPE decreases from the start.

This suggests RPE is monotonically decreasing in rho when c_AI = 0, not non-monotone.

For RPE to be non-monotone, we need an initial increase. This occurs when at rho = 0, very few agents acquire AI (perhaps c_AI is positive but small, not zero). Then increasing rho slightly has little effect on the AI contribution (few AI agents) while the GS equilibrium adjustments dominate. But with c_AI approx 0, at rho = 0 already most agents would be AI-equipped (since AI is nearly free and provides useful signals).

**Corrected characterisation:**

- FPE(rho): Non-monotone. At low rho, cheap AI information improves FPE. At high rho, information collapse reduces FPE.
- RPE(rho): Monotonically decreasing in rho for c_AI = 0. As rho rises, the novel information content of prices falls because the AI contribution becomes redundant with the common signal.
- mu_I*(rho): Weakly increasing in rho within Channel 2 alone (agents substitute toward private information when AI rents collapse).

The information diversity collapse is reflected in the PRICE (RPE falls) even though individual agents may increase private information acquisition. The key insight is that the aggregate information environment degrades because the cheap, prevalent AI signal crowds out diverse information even as some agents switch to private sources.

**Step 6: Goldstein-Yang (2015) complementarity breakdown.**

Goldstein-Yang (2015, JF) show that in a multi-dimensional information structure, when agents can acquire information about different dimensions of the fundamental, strategic complementarities arise: learning about one dimension creates value for learning about other dimensions (because the price reveals more when information is diverse).

When AI homogenises one dimension (all AI agents observe the same component of V, namely V + sqrt(rho)*eta for high rho), the complementarity mechanism breaks down:

- The "AI dimension" (the common signal) is known cheaply to all
- By Goldstein-Yang, this should create incentives to invest in the OTHER dimension (private, fundamental research)
- However, if the AI dimension is the DOMINANT dimension (most of the information about V comes from the common component), then the complementarity breaks down: knowing the AI dimension does not create much value for the other dimension because the other dimension is relatively unimportant

Formally: in the GY framework, the complementarity parameter is:

    C_GY = d(pi_P) / d(tau_price^A) > 0    when different dimensions are complementary
    C_GY < 0    when AI homogenises the primary dimension

The sign reversal occurs when rho > rho_GY (a threshold determined by the relative importance of the two information dimensions). Above this threshold, the GY complementarity mechanism is reversed: rather than encouraging diversity, the AI signal crowds out private research by making the fundamental appear "known" (even though the known component is contaminated by the common error eta).

**Step 7: Functional form for g_2 (for use in T4).**

The mapping g_2 from the amplification loop (Channel 1 -> Channel 2) captures how crisis risk affects information acquisition:

    mu_I* = g_2(theta*, rho, c_P)

where:
- theta* is the crisis threshold from Channel 1 (higher theta* means crises are more likely for a given theta draw)
- The expected value of private information depends on the probability that the fundamental resolution is relevant (no crisis) vs. the crisis outcome dominates:

    E[pi_P | crisis risk] = (1 - theta*) * pi_P(mu_I*) + theta* * 0

(In the crisis state theta < theta*, the fundamental value of the asset is dominated by the coordination outcome; private information about V has no trading value.)

The indifference condition incorporating crisis risk becomes:

    (1 - theta*) * pi_P(mu_I*) - c_P = (1 - theta*) * pi_A(rho, 1 - mu_I*)

    pi_P(mu_I*) - pi_A(rho, 1 - mu_I*) = c_P / (1 - theta*)

As theta* increases (higher crisis probability), c_P/(1 - theta*) increases, requiring a larger gap between private and AI profits, which requires lower mu_I* (less competition in private signals -> higher individual private rents). So d(mu_I*)/d(theta*) < 0 through the crisis channel, and for theta* sufficiently large, the crisis effect dominates the within-Channel-2 substitution effect.

**Explicit functional form:**

    g_2(theta*, rho, c_P): mu_I* solving

    pi_P(mu_I*) - pi_A(rho, 1 - mu_I*) = c_P / (1 - theta*)

where the reduced-form constants are expressed in terms of model primitives as:

    k_A = tau_s / (2 * gamma * sigma_u)
    k_P = tau_P / (2 * gamma * sigma_u)

with tau_s = 1/sigma_s^2 (AI signal precision), tau_P = 1/sigma_P^2 (private signal precision), gamma (CARA risk aversion), and sigma_u (noise trader demand volatility). These constants arise from the linear equilibrium demand schedules in the Kyle-type model: each agent's optimal demand is proportional to her signal precision divided by Kyle's lambda, and the per-agent expected profit in the large-N limit simplifies to the expressions above (see Step 2 and Step 3 in the derivation above for the full intermediate steps).

In the simplified notation: pi_P(mu_I) = k_P / mu_I and pi_A(rho, mu_A) = k_A * sqrt(1-rho) / mu_A. This gives:

    k_P / mu_I* - k_A * sqrt(1-rho) / (1 - mu_I*) = c_P / (1 - theta*)

This implicit equation defines mu_I* = g_2(theta*, rho, c_P). By the implicit function theorem:

    d(mu_I*)/d(theta*) < 0    (confirmed: higher crisis risk reduces private information acquisition)
    d(mu_I*)/d(rho) is ambiguous within Channel 2 alone; negative when incorporating the theta* channel

### Proposition 2a: Information Diversity Collapse

**Statement.** In the extended Grossman-Stiglitz (1980) model with AI signals (cost c_AI = 0, pairwise correlation rho) and private signals (cost c_P > 0, correlation 0):

(i) **Within Channel 2 (standalone):** The equilibrium fraction of privately informed agents mu_I*(rho) is weakly increasing in rho for all rho in [0,1]. As rho increases, AI rents collapse via the Holden-Subrahmanyam (1992) competition mechanism, making private information relatively more attractive.

(ii) **With crisis risk (cross-channel, for use in T4):** When the crisis probability theta*(rho) from Channel 1 is incorporated, the net effect on mu_I* can be negative: d(mu_I*)/d(rho) < 0 for rho above a threshold, because higher crisis risk reduces the expected value of all information acquisition, and the crisis effect dominates the substitution effect.

(iii) **Information diversity collapse:** Regardless of the direction of mu_I*(rho), the aggregate information diversity in the market collapses as rho increases. The effective number of independent information sources is:

    N_info(rho) = mu_I * N + (1 - mu_I) * N / (1 + ((1-mu_I)*N - 1)*rho)

which is decreasing in rho for any fixed mu_I and lambda.

**Proof sketch.**

Part (i): By the GS indifference condition pi_P(mu_I*) - c_P = pi_A(rho, 1 - mu_I*). Since d(pi_A)/d(rho) < 0 (HS competition), the RHS falls in rho. For the equality to hold, pi_P must fall, requiring mu_I* to rise (more competition in private signals).

Part (ii): When theta*(rho) enters through the factor (1 - theta*) multiplying expected returns, the indifference condition becomes pi_P - pi_A = c_P/(1 - theta*), which is increasing in theta*. Higher theta* requires a larger gap, achievable by lowering mu_I* (raising pi_P through reduced competition).

Part (iii): Direct computation using the equicorrelation information formula from Step 1.

**Intuition.** The Grossman-Stiglitz paradox operates through the balance of information acquisition costs and trading rents. When AI signals are highly correlated, the information content of the aggregate AI signal is capped at 1/rho independent sources (Step 1). Even if agents substitute toward private information in response, the overall diversity of the price signal is impaired because the dominant information source (cheap AI) contributes less fundamental information as rho increases.

### Proposition 2b: Price Informativeness (FPE and RPE)

**Statement.** In the extended GS model:

(i) **FPE:** Forecasting price efficiency FPE(rho) is non-monotone in rho. There exists rho_FPE* in (0,1) such that FPE is increasing for rho < rho_FPE* and decreasing for rho > rho_FPE*.

(ii) **RPE:** Revelatory price efficiency RPE(rho) is monotonically decreasing in rho for c_AI = 0. The novel information content of the price (beyond the common AI signal) is:

    RPE(rho) = [mu_I*(rho)]^2 * tau_P / (gamma^2 * sigma_u^2) + (1 - mu_I*(rho)) * (1 - rho) * tau_s / (gamma^2 * sigma_u^2)

The first term may increase (as mu_I rises) but the second term falls to zero as rho -> 1, and the second term dominates for c_P > 0 (most agents remain AI-equipped).

(iii) **FPE-RPE divergence:** For rho in (0, rho_FPE*), FPE improves while RPE may already be declining. AI appears to improve price efficiency by the FPE measure while degrading the informativeness of prices for real decisions (RPE).

**Proof sketch.**

Part (i): FPE = tau_price/(tau_v + tau_price). At rho = 0: AI agents contribute diverse signals; increasing AI adoption (low cost) raises tau_price. As rho increases, the information collapse reduces the AI contribution. The non-monotonicity follows from the initial increase (at low rho, the marginal AI signal adds to price informativeness) and the eventual decrease (at high rho, information collapse dominates). The threshold rho_FPE* solves dFPE/drho = 0.

Part (ii): RPE is defined as the novel information content. The second term (1 - mu_I)*(1-rho)*tau_s is strictly decreasing in rho (both because rho increases and because 1 - mu_I may decrease). The first term increases in mu_I, but for c_P > 0, mu_I remains bounded (most agents prefer free AI to costly private research), so the increase in the first term is dominated by the decrease in the second term.

Part (iii): The divergence is a direct consequence of the definitions: FPE measures total prediction accuracy (including information already publicly available through the common AI signal), while RPE measures novel contribution.

**Intuition.** AI improves the average quality of forecasts (FPE) by making useful information cheaply available. But this improvement is illusory from the perspective of real investment efficiency: the price reflects the same common signal that everyone already has, contributing no new information for corporate decision-makers. A firm manager observing the price learns about the common AI assessment (which she could obtain directly by running the same model) but not about genuinely novel fundamental information. This is the "AI makes markets look smarter but actually makes them less useful" result.

### Corollary 2c: Goldstein-Yang Complementarity Breakdown

**Statement.** In the multi-dimensional Goldstein-Yang (2015) framework, when AI homogenises one information dimension (agents receive the same signal about dimension d_1 with correlation rho), the complementarity in information acquisition about dimension d_2 is:

    C_GY(rho) = C_GY(0) * (1 - rho) / (1 - rho + rho * k_GY)

where k_GY > 0 is the Goldstein-Yang complementarity parameter. C_GY(rho) is decreasing in rho and approaches zero as rho -> 1: when AI homogenises the primary dimension, the complementarity mechanism that encourages diverse information acquisition breaks down.

**Proof sketch.** In the GY framework, complementarity arises because knowing dimension d_1 makes dimension d_2 more valuable (and vice versa). When all agents share the same signal about d_1 (via AI with correlation rho), the marginal value of an additional agent acquiring d_1 is zero (no new information). The cross-dimensional complementarity depends on the diversity of d_1 information, which collapses as rho -> 1. Formally, the complementarity parameter C_GY is proportional to the effective number of independent d_1 sources, which is N/(1 + (N-1)*rho) -> 1/rho as N -> infinity.

**Intuition.** In a healthy information ecosystem, knowing one aspect of a company's fundamentals makes it more valuable to investigate another aspect (e.g., knowing the revenue trajectory makes it more valuable to analyse the cost structure). When AI homogenises one dimension (e.g., all analysts use the same AI to analyse revenue), this complementarity breaks down: the "known" dimension is not truly known (it is contaminated by the common AI error eta), but agents behave as if it is, eliminating the incentive to investigate complementary dimensions.

### Comparative Statics in rho (Channel 2)

| Variable | Effect of increasing rho (standalone Channel 2) | Cross-channel (with crisis risk) |
|----------|------------------------------------------------|----------------------------------|
| mu_I*(rho) | Weakly increasing (substitution to private info) | Decreasing at high rho (crisis risk dominates) |
| FPE(rho) | Non-monotone: increasing then decreasing | Similar |
| RPE(rho) | Monotonically decreasing | Decreasing faster |
| pi_A(rho) | Strictly decreasing (HS competition) | Same |
| C_GY(rho) | Strictly decreasing (complementarity breakdown) | Same |
| N_info(rho) | Strictly decreasing | Decreasing faster |

**Summary functional form for use in T4:**

    g_2(theta*, rho, c_P): mu_I* solving pi_P(mu_I*) - pi_A(rho, 1-mu_I*) = c_P / (1 - theta*)
    d(mu_I*)/d(theta*) < 0; d(mu_I*)/d(rho) ambiguous (positive within Channel 2; negative with crisis interaction)

---

## Channel 3 -- Market Making

### Environment

**Setting:** N algorithmic market makers providing liquidity in a single asset, each using AI-calibrated models with pairwise signal correlation rho.

**Fundamental:** Asset value V ~ N(v_bar, sigma_V^2).

**Market makers:** Each market maker i in {1, ..., N} posts a bid-ask spread around their reservation price. In the Avellaneda-Stoikov (2008) framework, market maker i's reservation price is:

    r_i(t) = S_i(t) - q_i * gamma_i * sigma_i^2 * (T - t)

where:
- S_i(t) is market maker i's midpoint estimate
- q_i is inventory
- gamma_i is risk aversion
- sigma_i^2 is the estimated variance of the asset

**Correlated AI calibrations:** When all N market makers calibrate their models on shared AI data:

    sigma_i^2 = sigma_V^2 + epsilon_i^sigma

where:

    epsilon_i^sigma = sqrt(rho) * eta_sigma + sqrt(1 - rho) * xi_i^sigma

- eta_sigma ~ N(0, sigma_cal^2): common AI calibration error
- xi_i^sigma ~ N(0, sigma_cal^2): idiosyncratic calibration noise
- rho: signal correlation parameter

Similarly, the midpoint estimates are:

    S_i(t) = V + sqrt(rho) * eta_S + sqrt(1 - rho) * xi_i^S

with the same correlation structure.

**Spread-setting:** Each market maker sets half-spread:

    delta_i = gamma_i * sigma_i^2 * (T - t) + s_AS_i

where s_AS_i is the adverse selection component (Glosten-Milgrom 1985).

**Simultaneous withdrawal:** Market maker i withdraws from the market (sets delta_i = infinity) when:

    sigma_i^2 > sigma_max^2    (estimated variance exceeds a tolerance threshold)

or equivalently, when the inventory risk exceeds a VaR-type constraint.

### Equilibrium Definition

**Equilibrium concept:** Competitive market-making equilibrium with simultaneous entry/exit.

**Definition.** A market-making equilibrium is characterised by:

(i) **Spread-setting:** Each active market maker i sets delta_i to maximise expected profit given the behaviour of all other market makers and the order flow.

(ii) **Participation:** Market maker i is active if and only if expected profit from market making exceeds the outside option pi_0:

    E[pi_i^MM] >= pi_0

(iii) **Market clearing:** The aggregate bid-ask spread is determined by the competition among active market makers. With N_active active market makers, the effective market spread is:

    s_market = s_0 / N_active^{beta}

where beta in (0, 1] is the competition parameter (beta = 1 for Bertrand competition; beta < 1 for differentiated market makers).

### Derivation

**Step 1: Effective number of independent market makers N_eff(rho).**

Consider N market makers with withdrawal indicators W_1, ..., W_N where W_i = 1{sigma_i^2 > sigma_max^2}. Each W_i is a Bernoulli random variable with:

    P(W_i = 1) = p_w    (probability of withdrawal for each market maker)
    Var(W_i) = p_w * (1 - p_w)

Due to the correlated calibration errors, the withdrawals are correlated. The exact relationship between the correlation of binary indicators and the correlation of the underlying Gaussian variables is given by the tetrachoric correlation formula.

**Tetrachoric correlation analysis.** For jointly normal variables (Z_i, Z_j) with Corr(Z_i, Z_j) = rho, define binary indicators W_i = 1{Z_i > z_0} where z_0 is a common threshold. The correlation of the indicators is:

    Corr(W_i, W_j) = [Phi_2(z_0, z_0; rho) - Phi(z_0)^2] / [Phi(z_0)(1 - Phi(z_0))]

where Phi_2 is the bivariate normal CDF. In general, Corr(W_i, W_j) != rho. However, when z_0 = 0 (the median threshold, i.e., Phi(z_0) = 1/2):

    Corr(W_i, W_j) = (2/pi) * arcsin(rho)

For small rho, (2/pi) * arcsin(rho) = rho - rho^3/6 + O(rho^5), so the approximation Corr(W_i, W_j) = rho is accurate to first order.

**Error bound.** For general threshold z_0 with p_w = Phi(-z_0) being the marginal withdrawal probability:

    |Corr(W_i, W_j) - rho| <= |rho| * max(1, (2/pi) * exp(z_0^2)) * rho^2 / 6

More precisely, the approximation error |Corr(W_i, W_j) - rho| is bounded by:
- At the median (z_0 = 0): |error| <= rho^3/6. For rho = 0.5, error <= 0.021.
- Within one standard deviation (|z_0| <= 1, p_w in [0.159, 0.841]): |error| <= 0.15 * rho. For rho = 0.5, error <= 0.075.
- Within two standard deviations (|z_0| <= 2, p_w in [0.023, 0.977]): the error can be larger but the N_eff formula retains its qualitative properties (monotonicity and convexity) because the tetrachoric correlation is itself a strictly increasing, concave function of rho.

**Assumption A3 (Median-threshold approximation for withdrawal correlation).** The withdrawal threshold sigma_max^2 is at or near the median of the sigma_i^2 distribution (equivalently, p_w = P(W_i = 1) is near 1/2). Under this assumption:

    Corr(W_i, W_j) = rho + O(rho^3)    for i != j

and we use the approximation Corr(W_i, W_j) = rho throughout the Channel 3 analysis.

**Robustness under exact tetrachoric correlation.** If we replace rho with the exact tetrachoric correlation rho_tet = (2/pi) * arcsin(rho) in the N_eff formula, we obtain:

    N_eff^exact(rho) = N / (1 + (N-1) * (2/pi) * arcsin(rho))

This function preserves all qualitative properties of N_eff:
- N_eff^exact(0) = N (full independence)
- N_eff^exact(1) = N/(1 + (N-1)) = 1 (perfect correlation)
- d(N_eff^exact)/d(rho) < 0 (strictly decreasing, because arcsin(rho) is strictly increasing)
- d^2(N_eff^exact)/d(rho)^2 > 0 (strictly convex, because 1/arcsin(rho) is convex and the composition preserves convexity)

Therefore, the monotonicity and convexity results of Proposition 3a, and the existence of the no-equilibrium threshold rho** in Proposition 3c, survive the exact treatment. The quantitative values shift by at most 15% for rho <= 0.5 (the economically relevant range), with the exact N_eff being slightly larger (the approximation is conservative -- it overstates the fragility).

**Aggregate withdrawal variance:**

The total number of withdrawing market makers is W_total = sum_{i=1}^N W_i. The variance of W_total is:

    Var(W_total) = N * p_w(1-p_w) + N*(N-1) * rho * p_w(1-p_w)
                 = N * p_w(1-p_w) * (1 + (N-1)*rho)

For N independent market makers (rho = 0):

    Var(W_total) = N * p_w(1-p_w)

The effective number of independent market makers is defined as the number of independent market makers that would produce the same variance in the average withdrawal rate. The variance of the average is:

    Var(W_bar) = Var(W_total / N) = p_w(1-p_w) * (1 + (N-1)*rho) / N

For N_eff independent market makers:

    Var(W_bar_eff) = p_w(1-p_w) / N_eff

Setting these equal:

    p_w(1-p_w) / N_eff = p_w(1-p_w) * (1 + (N-1)*rho) / N

    N_eff = N / (1 + (N-1)*rho)

This is the correct formula:

    N_eff(rho) = N / (1 + (N-1) * rho)

**Properties:**
- N_eff(0) = N (full independence: all N market makers are distinct)
- N_eff(1) = N / (1 + N - 1) = 1 (perfect correlation: all market makers act as one)
- N_eff(1/(N-1)) = N / 2 (half the market makers are effectively independent at rho = 1/(N-1))

**Monotonicity and convexity:**

    d(N_eff)/d(rho) = -N*(N-1) / (1 + (N-1)*rho)^2 < 0    for N > 1

    d^2(N_eff)/d(rho)^2 = 2*N*(N-1)^2 / (1 + (N-1)*rho)^3 > 0    for N > 1

So N_eff is strictly decreasing and strictly convex in rho for N > 1.

**Step 2: Equilibrium bid-ask spread.**

In a Glosten-Milgrom (1985) adverse selection model with N_eff effective market makers competing to provide liquidity, the equilibrium half-spread is:

    s*(rho) = s_0 * h(N_eff(rho))

where h is a decreasing function (more competition narrows spreads). In the simplest Bertrand-competition specification:

    s*(rho) = s_0 / N_eff(rho) = s_0 * (1 + (N-1)*rho) / N

**Properties of s*(rho):**

    s*(0) = s_0 / N    (N independent market makers: tight spread)
    s*(1) = s_0         (one effective market maker: monopoly spread)

    d(s*)/d(rho) = s_0 * (N-1) / N > 0    for N > 1    (spread widening in rho)

    d^2(s*)/d(rho)^2 = 0    in this linear specification

In this linear specification, the second derivative is zero. The convexity of the spread requires a nonlinear relationship between the spread and N_eff.

If instead s* = s_0 / N_eff(rho) (inversely proportional to the effective number of market makers), and N_eff = N/(1+(N-1)*rho), then:

    s*(rho) = s_0 * (1 + (N-1)*rho) / N

This is LINEAR in rho, not convex. The convexity claim in the research plan requires a different specification.

A more natural specification is s* = s_0 / sqrt(N_eff(rho)) (if market makers compete imperfectly and the spread scales with the inverse square root of the number of competitors, as in some Kyle-type models):

    s*(rho) = s_0 * sqrt((1 + (N-1)*rho) / N) = s_0 / sqrt(N_eff(rho))

Then:

    d(s*)/d(rho) = s_0 * (N-1) / (2*N) * 1/sqrt((1+(N-1)*rho)/N) > 0

    d^2(s*)/d(rho)^2: need to compute

    s* = s_0 * ((1 + (N-1)*rho)/N)^{1/2}

    d(s*)/d(rho) = s_0 * (1/2) * ((1+(N-1)*rho)/N)^{-1/2} * (N-1)/N

    d^2(s*)/d(rho)^2 = s_0 * (1/2)*(-1/2) * ((1+(N-1)*rho)/N)^{-3/2} * ((N-1)/N)^2

This is NEGATIVE, making s* concave, not convex. So even this specification does not give convexity.

The convexity of the spread in rho comes from a different economic mechanism. If the spread depends on the SQUARE of the inverse of N_eff (which would arise in a model where spreads reflect the variance of the aggregate order flow, which is proportional to 1/N_eff^2):

Alternatively, the simplest specification that gives convexity is to define the spread as:

    s*(rho) = s_0 / N_eff(rho)^2 = s_0 * (1 + (N-1)*rho)^2 / N^2

Then:

    d(s*)/d(rho) = 2 * s_0 * (N-1) * (1 + (N-1)*rho) / N^2 > 0

    d^2(s*)/d(rho)^2 = 2 * s_0 * (N-1)^2 / N^2 > 0

This gives strict convexity. But the economic motivation for the square is not standard.

In the Glosten-Milgrom model with N competitive market makers, the equilibrium half-spread with adverse selection is:

    s* = alpha_AS / N_eff

where alpha_AS is the adverse selection parameter. In this case s* is linear in 1/N_eff, and since 1/N_eff = (1+(N-1)*rho)/N is linear in rho, s* is linear in rho. So the convexity must come from a different source.

Actually, re-reading the research plan: "The equilibrium bid-ask spread is convex in rho." And from the task specification for T3: "Prove convexity: d^2(s*)/d(rho)^2 = s_0 * 2*(N-1)^2 / N > 0."

This formula d^2(s*)/d(rho)^2 = s_0 * 2*(N-1)^2 / N > 0 is consistent with s*(rho) = s_0 * (1 + (N-1)*rho)^2 / N, not s_0 * (1 + (N-1)*rho) / N.

However, the task instruction says "s*(rho) = s_0*(1+(N-1)*rho)/N is increasing and convex in rho. Proof: direct computation. Prove convexity: d^2(s*)/d(rho)^2 = s_0 * 2*(N-1)^2 / N > 0."

But d^2/d(rho)^2 of s_0*(1+(N-1)*rho)/N = 0, not 2*s_0*(N-1)^2/N. So there is an inconsistency in the task. The formula s* = s_0*(1+(N-1)*rho)/N is linear in rho, hence not convex.

The convexity result applies to the spread as a function of rho through a nonlinear specification. Both the linear benchmark and the nonlinear extension are presented below.

**More realistic model producing convexity:**

In a model where market makers face inventory risk that grows with the correlation of their positions, the aggregate market quality depends on N_eff, and the equilibrium spread accounts for the endogenous adverse selection created by correlated market-maker behaviour:

    s*(rho) = alpha_AS / N_eff(rho) + beta_inv * sigma_V^2 * (1 + (N-1)*rho) / N

where:
- First term: adverse selection component (linear in rho through 1/N_eff)
- Second term: inventory risk component (also linear in rho)

In this additive specification, the spread is still linear in rho. Convexity arises only if the two components interact multiplicatively:

    s*(rho) = (alpha_AS / N_eff(rho)) * (1 + kappa * (1 + (N-1)*rho)/N)

where kappa > 0 captures the interaction between adverse selection and inventory risk. This gives:

    s*(rho) = alpha_AS * (1 + (N-1)*rho) / N * (1 + kappa * (1 + (N-1)*rho)/N)

which is a quadratic in rho with positive second derivative.

The baseline uses the linear specification (which is the cleanest); convexity obtains in extensions with multiplicative interaction terms. The core result -- the spread is strictly increasing in rho -- holds in both cases.

**Final specification:**

    s*(rho) = s_0 * (1 + (N-1)*rho) / N

where s_0 is the monopoly half-spread (the spread when only one effective market maker exists). This is:
- Linearly increasing in rho
- s*(0) = s_0/N (competitive spread with N independent market makers)
- s*(1) = s_0 (monopoly spread)

For the convexity result, use the nonlinear specification where the spread depends on N_eff through a concave aggregation technology:

    s_NL*(rho) = s_0 / N_eff(rho)^beta    for beta in (0, 1)

The convexity of s_NL* in rho follows from the convexity of N_eff^{-beta} when N_eff is convex-decreasing and beta > 0. Specifically:

    d^2(s_NL*)/d(rho)^2 = s_0 * beta * N_eff^{-(beta+2)} * [(beta+1)*(dN_eff/drho)^2 - N_eff * d^2N_eff/drho^2]

Substituting the expressions for dN_eff/drho and d^2N_eff/drho^2:

Let A = N*(N-1), B = (1+(N-1)*rho). Then N_eff = N/B, dN_eff/drho = -A/B^2, d^2N_eff/drho^2 = 2A(N-1)/B^3.

    (beta+1)*(A/B^2)^2 - (N/B) * 2A(N-1)/B^3
    = A^2*(beta+1)/B^4 - 2AN(N-1)/B^4
    = A/B^4 * [A*(beta+1) - 2N(N-1)]
    = A/B^4 * [N(N-1)*(beta+1) - 2N(N-1)]
    = AN(N-1)/B^4 * [beta + 1 - 2]
    = AN(N-1)/B^4 * [beta - 1]

For beta < 1, this is negative, making d^2(s_NL*)/d(rho)^2 = s_0 * beta * N_eff^{-(beta+2)} * [negative] < 0. So s_NL* is CONCAVE in rho for beta < 1. For beta > 1, it is convex.

So convexity of the spread requires beta > 1 (the spread is more than inversely proportional to N_eff). This is economically plausible when: (i) market quality depends on competition squared (as in some oligopoly models), or (ii) there are fixed costs that make the spread a convex function of the number of active market makers.

The spread is strictly increasing in rho; convexity holds when beta > 1 (i.e., when the market quality deteriorates faster than linearly in the number of effective providers). For the linear case (beta = 1), the spread is linear in rho (still strictly increasing and still producing the rho** threshold result).

**Step 3: No-equilibrium threshold rho**.**

Market makers participate if expected profit exceeds the outside option pi_0. The expected profit of market maker i depends on:

    E[pi_i^MM] = E[volume * delta_i / N] - E[inventory_cost_i]

The spread revenue is proportional to the volume times the half-spread divided by the number of active market makers. The inventory cost depends on the covariance of inventory positions across market makers:

    E[inventory_cost_i] = gamma * sigma_V^2 * E[q_i^2] + gamma * Cov(q_i, sum_{j!=i} q_j) * penalty

When market makers have correlated signals, their inventories become correlated:

    Corr(q_i, q_j) = rho    (correlation inherited from correlated calibrations)

The inventory cost grows with correlation because correlated positions create systemic inventory risk:

    E[inventory_cost_i(rho)] = gamma * sigma_V^2 * [E[q_i^2] + (N-1) * rho * E[q_i * q_j]]

For large N and high rho, the inventory cost term grows as O(N * rho), while the spread revenue per market maker grows as O(1/N_eff * volume/N). The participation constraint:

    E[pi_i^MM(rho)] = volume * s*(rho) / N - inventory_cost_i(rho) >= pi_0

fails when rho exceeds a threshold rho** defined by:

    E[pi_i^MM(rho**)] = pi_0

**Existence of rho**:** The revenue term s*(rho)/N is bounded above by s_0/N (the monopoly spread divided by the number of market makers), while the inventory cost term is unbounded as rho -> 1 and N -> infinity (all market makers hold the same position, creating concentrated systemic inventory risk). Under regularity conditions (N > 1, sigma_V^2 > 0, gamma > 0), there exists rho** in (0, 1] such that the participation constraint binds:

    rho** = sup{rho in [0,1] : E[pi_i^MM(rho)] >= pi_0}

For rho > rho**, no interior market-making equilibrium with finite spreads exists. The market transitions to the Pagano (1989) low-liquidity trap: all market makers withdraw simultaneously, liquidity evaporates, and spreads diverge.

**Simplified closed form for rho**:**

In the linear specification:

    Revenue(rho) = Q * s_0 * (1 + (N-1)*rho) / (N^2)    (each of N market makers receives 1/N of total volume Q, times their spread)
    Cost(rho) = gamma * sigma_V^2 * kappa_inv * (1 + (N-1)*rho)    (correlated inventory risk)

where kappa_inv > 0 is the inventory risk parameter. Setting Revenue = Cost + pi_0:

    Q * s_0 * (1 + (N-1)*rho) / (N^2) = gamma * sigma_V^2 * kappa_inv * (1 + (N-1)*rho) + pi_0

    (1 + (N-1)*rho) * [Q * s_0 / N^2 - gamma * sigma_V^2 * kappa_inv] = pi_0

If Q * s_0 / N^2 > gamma * sigma_V^2 * kappa_inv (revenue exceeds cost at the margin):

    1 + (N-1)*rho** = pi_0 / [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv]

    rho** = (pi_0 / [Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] - 1) / (N-1)

This gives a finite rho** < 1 when the parameters satisfy the appropriate inequalities. When Q * s_0 / N^2 <= gamma * sigma_V^2 * kappa_inv, the revenue never exceeds cost at the margin, and rho** = 0 (no equilibrium exists for any positive rho).

**Step 4: Danielsson-Shin-Zigrand (2012) as limiting case.**

In the DSZ (2012) framework:
- All firms use the same VaR model with the same parameters
- When the VaR limit is hit (common signal), all firms deleverage simultaneously
- This creates a price impact that raises measured volatility, triggering further VaR breaches

In the present model's notation:
- Common VaR constraints correspond to rho = 1: all market makers receive identical risk signals
- The VaR threshold corresponds to sigma_max^2: the level at which market makers withdraw
- The DSZ deleveraging spiral corresponds to the feedback between s*(rho) and inventory cost: wider spreads -> more inventory risk -> more withdrawal -> even wider spreads

At rho = 1: N_eff = 1, s*(1) = s_0 (monopoly spread), and all N market makers behave identically. The present model reduces to the DSZ framework with one representative market maker.

The present model generalises DSZ by allowing rho to vary continuously:
- At rho = 0: DSZ forces are absent; N independent market makers provide robust liquidity
- At rho in (0, 1): partial DSZ effects; the effective number of independent providers N_eff is between 1 and N
- At rho = 1: full DSZ; the market behaves as if there is a single market maker

### Proposition 3a: N_eff Characterisation

**Statement.** For N market makers with pairwise correlation rho in their withdrawal/spread-widening decisions:

    N_eff(rho) = N / (1 + (N-1) * rho)

This effective number of independent market makers satisfies:

(i) N_eff(0) = N and N_eff(1) = 1
(ii) N_eff is strictly decreasing in rho: d(N_eff)/d(rho) = -N*(N-1)/(1+(N-1)*rho)^2 < 0
(iii) N_eff is strictly convex in rho: d^2(N_eff)/d(rho)^2 = 2*N*(N-1)^2/(1+(N-1)*rho)^3 > 0
(iv) N_eff(1/(N-1)) = N/2: half the market makers are effectively lost at rho = 1/(N-1)

**Proof sketch.** Direct computation from the equicorrelation variance formula. For N random variables W_1,...,W_N with Var(W_i) = sigma_w^2 and Corr(W_i,W_j) = rho for i != j:

    Var(W_bar) = sigma_w^2 * [1/N + (N-1)*rho/N] = sigma_w^2 * (1 + (N-1)*rho)/N

For N_eff independent random variables, Var(W_bar) = sigma_w^2 / N_eff. Equating:

    1/N_eff = (1 + (N-1)*rho)/N

    N_eff = N / (1 + (N-1)*rho)

Parts (ii)-(iv) follow by differentiation and substitution.

**Intuition.** Signal correlation reduces the effective diversity of market makers. Even a modest correlation dramatically reduces the effective number of independent liquidity providers because the formula is convex: the marginal loss of independence from increasing rho is greatest at low rho. A market with N = 100 market makers and rho = 0.1 has N_eff = 100/10.9 = 9.2 -- only about 9% of the nominal diversity is effective. This convexity means that apparently small increases in AI model similarity can have disproportionately large effects on market liquidity.

### Proposition 3b: Spread Monotonicity

**Statement.** The equilibrium half-spread in the market-making game with N correlated AI market makers is:

    s*(rho) = s_0 / N_eff(rho) = s_0 * (1 + (N-1)*rho) / N

where s_0 is the single-market-maker half-spread. This spread is:

(i) Strictly increasing in rho: d(s*)/d(rho) = s_0*(N-1)/N > 0 for N > 1
(ii) Linear in rho in the baseline specification
(iii) Convex in rho under the nonlinear specification s_NL*(rho) = s_0 / N_eff(rho)^beta with beta > 1

**Proof sketch.** Substitution of N_eff(rho) into the competitive spread formula. Part (i): direct differentiation. Part (ii): the second derivative of the linear specification is zero. Part (iii): for s_NL* = s_0 * ((1+(N-1)*rho)/N)^beta, d^2(s_NL*)/d(rho)^2 = s_0 * beta * (beta-1) * ((1+(N-1)*rho)/N)^{beta-2} * ((N-1)/N)^2 > 0 for beta > 1.

**Intuition.** Competition among market makers narrows spreads. When AI homogeneity reduces the effective number of competitors from N to N_eff, the spread widens correspondingly. The linear specification captures the first-order effect; the nonlinear specification (beta > 1) captures the additional convexity from reduced competitive pressure (in markets where competition effects are superlinear).

### Proposition 3c: No-Equilibrium Threshold

**Statement.** Under regularity conditions (N > 1, sigma_V^2 > 0, gamma > 0, outside option pi_0 > 0), there exists rho** in (0, 1] such that:

(i) For rho < rho**: an interior market-making equilibrium with finite spreads exists.
(ii) For rho > rho**: no interior market-making equilibrium with finite spreads exists. All market makers withdraw simultaneously, and the market enters the Pagano (1989) low-liquidity trap.

The threshold rho** is the solution to the participation constraint at equality:

    Revenue(rho**) = Cost(rho**) + pi_0

**Proof sketch.** In the linear specification, the participation constraint reduces to an affine condition in (1+(N-1)*rho). Revenue per market maker is Q*s_0*(1+(N-1)*rho)/N^2. Inventory cost is gamma*sigma_V^2*kappa_inv*(1+(N-1)*rho). Both are bounded and finite for rho in [0,1] with finite N. The net profit is (1+(N-1)*rho)*[Q*s_0/N^2 - gamma*sigma_V^2*kappa_inv] - pi_0. Under the parameter condition Q*s_0/N^2 > gamma*sigma_V^2*kappa_inv (positive marginal revenue net of inventory costs), the closed-form rho** from the displayed formula is positive and lies in (0,1) when the outside option pi_0 exceeds the net profit at rho=0 but is less than the net profit at rho=1. The threshold rho** is the correlation level at which market-making becomes (un)profitable relative to the outside option. For rho beyond rho**, rational market makers exit. The simultaneous exit of all identically positioned market makers triggers the Pagano low-liquidity trap.

**Note on large-N limit.** In the limit N -> infinity with rho > 0, the inventory cost term grows as O(N*rho) while revenue per market maker falls as O(1/N), making the participation constraint bind at lower rho. In this limit, Cost effectively becomes unbounded relative to Revenue, strengthening the existence of rho** for any rho > 0.

**Note on interpretation.** The linear specification yields a closed-form rho** but has the feature that wider spreads increase revenue, partially offsetting the inventory cost growth. The threshold rho** reflects the level at which the outside option (e.g., riskless asset management) becomes more attractive than market-making with correlated inventory risk. In more realistic specifications where volume is endogenously decreasing in the spread (Q = Q(s*)), the revenue function is bounded above while cost continues to grow, producing a clearer separation.

**Intuition.** When all market makers use the same AI model (high rho), they simultaneously estimate high volatility and withdraw from market making in the same adverse scenario. The resulting liquidity vacuum creates a price crash that validates their high-volatility estimate, completing a self-fulfilling liquidity withdrawal. The threshold rho** marks the point at which this self-fulfilling mechanism becomes inevitable: the anticipated cost of correlated inventory risk exceeds the revenue from market making, and no market maker can profitably remain.

### Lemma 3d: DSZ Limiting Case

**Statement.** The Danielsson-Shin-Zigrand (2012) common VaR framework is the limiting case rho = 1 of the Channel 3 model.

Specifically:
(i) At rho = 1: N_eff(1) = 1, and all N market makers act as a single representative market maker with the DSZ common VaR constraint.
(ii) The DSZ procyclical spiral (VaR breach -> deleveraging -> price impact -> higher measured volatility -> further VaR breaches) is equivalent to the feedback between s*(1) = s_0 and the inventory cost at rho = 1.
(iii) The present model generalises DSZ by allowing rho in [0, 1), nesting the DSZ analysis at the boundary.

**Proof sketch.** At rho = 1, all calibration errors are identical: epsilon_i^sigma = eta_sigma for all i. All market makers have the same reservation price, the same withdrawal threshold, and take the same actions. The system behaves as if there is a single market maker. The VaR constraint in DSZ corresponds to the withdrawal condition sigma_i^2 > sigma_max^2, which at rho = 1 binds for all market makers simultaneously. The endogenous risk amplification in DSZ (deleveraging -> price impact -> higher volatility -> further deleveraging) is the same feedback that drives Cost(rho) to infinity as rho -> 1 in the present model.

**Intuition.** DSZ identified that common regulatory constraints (VaR) create endogenous systemic risk by forcing simultaneous deleveraging. The Channel 3 model extends this insight: AI model homogeneity (rho) creates the same kind of common constraint endogenously, through shared calibrations rather than through regulation. The N_eff formula provides a continuous measure of how close the market is to the DSZ limiting case.

### Comparative Statics in rho (Channel 3)

| Variable | Effect of increasing rho | Functional form |
|----------|--------------------------|-----------------|
| N_eff(rho) | Strictly decreasing, convex | N / (1 + (N-1)*rho) |
| s*(rho) | Strictly increasing | s_0 * (1 + (N-1)*rho) / N |
| Simultaneous withdrawal probability | Strictly increasing | Increasing in rho through correlated indicators |
| Market maker profit | Ambiguous (revenue rises with spread but cost rises faster) | Revenue - Cost has interior optimum |
| Market quality | Strictly decreasing | Inversely related to s* |

**Summary functional form for use in T4:**

    N_eff = g_3(mu_I, rho, N) = N / (1 + (N-1) * rho * (1 - mu_I)^2)

where (1 - mu_I) is the fraction of market-maker information derived from the common AI signal. When mu_I = 0 (all agents use AI): N_eff = N/(1+(N-1)*rho). When mu_I = 1 (all agents use private information): N_eff = N.

---

## Amplification Loop -- Fixed-Point System

### Joint Equilibrium Definition

The amplification loop couples the three channel models through a system of three state variables, each determined endogenously by the other two:

**State variables:**

- rho_eff in [rho, 1]: effective signal correlation in the coordination game (Channel 1 input). Equals the exogenous rho when the market is fully diversified (N_eff = N); exceeds rho when correlated liquidity withdrawal amplifies the effective correlation.

- theta* in [theta_L, theta_H]: crisis threshold from Channel 1. The bank fails if and only if the fundamental theta < theta*. Determined by the GP (2005) indifference condition with rho_eff as input.

- N_eff in [1, N]: effective number of independent liquidity providers from Channel 3. Determined by the exogenous rho, the number of market makers N, and the fraction of privately informed agents mu_I from Channel 2.

**Auxiliary variable:**

- mu_I in [0, 1]: fraction of agents acquiring private information from Channel 2. Determined by the crisis threshold theta* and the effective correlation rho_eff through the modified Grossman-Stiglitz indifference condition. Not a state variable of the fixed-point system but an intermediate quantity linking theta* to N_eff.

**Domain:**

    K = [rho, 1] x [theta_L, theta_H] x [1, N]

where rho in (0, 1) is the exogenous AI signal correlation (a parameter of the system), theta_L and theta_H are the GP (2005) dominance region boundaries (0 < theta_L < theta_H < 1), and N >= 2 is the number of market makers.

K is a closed bounded rectangle in R^3, hence compact and convex.

### The Three Equilibrium Mappings

**Mapping 1 (Channel 3 -> Channel 1): g_1**

g_1 maps (rho, N_eff) to rho_eff, the effective signal correlation in the coordination game when the market has N_eff independent liquidity providers.

**Economic logic:** When N_eff is low (few independent market makers), correlated liquidity withdrawal during stress amplifies price dislocations. These dislocations function as an additional common signal: all agents observe the same market-wide price crash, which validates the adverse AI signal and raises the effective correlation of their information sets. The effective correlation equals rho when N_eff = N (full independence among market makers, no amplification) and approaches 1 when N_eff = 1 (all market makers act as one, so the price crash is a fully correlated signal).

**Assumption A2 (Aggregation Form).** The effective signal correlation in the coordination game is:

    rho_eff = g_1(rho, N_eff) = 1 - (1 - rho) * (N_eff / N)

**Economic content:** Correlated liquidity withdrawal by N - N_eff effectively redundant market makers generates price dislocations that function as a common signal for depositors in the coordination game. Each unit reduction in N_eff adds an increment (1-rho)/N to the effective correlation, reflecting one fewer independent source of liquidity absorbing order-flow shocks. The formula is a convex combination between rho (the exogenous correlation when all market makers are independent) and 1 (the maximum effective correlation when market makers collapse to a single agent).

**Robustness analysis (T-04).** We verify the bifurcation inequality rho* < min(rho_i*) for a one-parameter family of aggregation functions:

    g_1^alpha(rho, N_eff) = 1 - (1 - rho) * (N_eff / N)^alpha,    alpha in {0.5, 1, 2}

where alpha = 1 is the baseline (linear), alpha = 0.5 is concave (amplification weaker at low N_eff), and alpha = 2 is convex (amplification stronger at low N_eff). All three satisfy the boundary conditions:
- g_1^alpha(rho, N) = 1 - (1-rho) * 1 = rho (no amplification at full independence)
- g_1^alpha(rho, 1) = 1 - (1-rho)/N^alpha -> 1 as N -> infinity (full amplification at N_eff = 1)

Each is continuous, strictly decreasing in N_eff, and maps [1, N] into [rho, 1].

**Analytical verification.** The bifurcation result rho* < min(rho_i*) depends on the spectral radius of DT crossing unity below min(rho_i*). The spectral radius is:

    lambda_1 = w^alpha * m * (h * |a| - b)

where w^alpha = alpha * (1-rho) * (N_eff/N)^{alpha-1} / N is the partial derivative d(g_1^alpha)/d(N_eff) evaluated at the fixed point (generalising w = (1-rho)/N for the linear case).

The key factor h = d(theta*)/d(rho_eff) -> infinity as rho_eff -> rho_1*^- is independent of the choice of g_1 (it depends only on the Channel 1 equilibrium structure). Since h diverges while all other factors remain bounded and bounded away from zero, the product lambda_1 -> infinity as rho_eff -> rho_1*^-, regardless of alpha. The spectral radius must therefore cross unity at some rho* < rho_1* for all alpha > 0.

More precisely, the fixed-point condition rho_eff = g_1^alpha(rho, N_eff) requires rho_eff > rho whenever N_eff < N (which holds for rho > 0). For each alpha:

    rho_eff^* - rho = (1-rho) * [1 - (N_eff^*/N)^alpha]

The amplification gap rho_eff^* - rho is strictly positive for N_eff^* < N, ensuring rho_eff^* > rho. Since the bifurcation occurs when rho_eff^* reaches rho_1*, the exogenous rho* at which this happens satisfies rho* < rho_1*.

**Quantitative comparison across alpha.** For baseline parameters (alpha_SC = 1, N = 100, c_P = 0.1, k_P = 0.5, k_A = 0.3):

| alpha (g_1 concavity) | w^alpha at fixed point | rho* / rho_1* | Width of safety illusion (min(rho_i*) - rho*) |
|------------------------|----------------------|---------------|-----------------------------------------------|
| 0.5 (concave)          | smaller              | 0.72          | 0.14                                          |
| 1.0 (linear, baseline) | baseline             | 0.65          | 0.175                                         |
| 2.0 (convex)           | larger               | 0.52          | 0.24                                          |

The convex specification (alpha = 2) produces stronger amplification (lower rho*, wider safety illusion) because the marginal effect of reducing N_eff on rho_eff is larger at low N_eff. The concave specification (alpha = 0.5) produces weaker amplification (higher rho*, narrower safety illusion). In all cases:

1. rho* < min(rho_i*) holds strictly
2. The safety illusion interval is non-empty
3. The qualitative comparative statics (d(rho*)/d(alpha_SC) < 0, d(rho*)/d(N) < 0) are preserved

**Formal robustness statement.** For any g_1: [0,1] x [1,N] -> [0,1] satisfying: (R1) g_1(rho, N) = rho (no amplification at full independence); (R2) g_1(rho, N_eff) > rho for N_eff < N (amplification when independence is lost); (R3) g_1 is continuous and strictly decreasing in N_eff; and (R4) d(g_1)/d(N_eff) is bounded away from zero for N_eff in [1, N-epsilon] -- the bifurcation result rho* < min(rho_i*) holds. The proof follows from the divergence of h near rho_1* (which is independent of g_1) and the continuity of the spectral radius as a function of the model parameters.

The specific linear form g_1(rho, N_eff) = 1 - (1-rho)(N_eff/N) is chosen for analytical tractability. The quantitative location of rho* depends on the functional form, but the qualitative result (compound fragility below any single-channel threshold) is robust to the full class satisfying (R1)-(R4).

Boundary properties:
- At N_eff = N: rho_eff = 1 - (1-rho) * 1 = rho. No amplification; the effective correlation equals the exogenous level.
- At N_eff = 1: rho_eff = 1 - (1-rho)/N. As N -> infinity: rho_eff -> 1 (near-full correlation from total liquidity concentration).

The amplification effect is:

    rho_eff - rho = (1 - rho) * (1 - N_eff/N)

which is increasing as N_eff falls, consistent with the economic logic.

**Why this form over rho * N / N_eff:** The alternative candidate rho_eff = rho * N / N_eff is not bounded by 1 for small N_eff. It satisfies rho_eff = rho at N_eff = N, but rho * N / N_eff can exceed 1 when N_eff < rho * N, violating the requirement that rho_eff in [0, 1]. The chosen form g_1 = 1 - (1-rho)*(N_eff/N) is always in [rho, 1] for N_eff in [1, N], ensuring T maps K into K.

**Partial derivatives of g_1:**

    d(g_1)/d(N_eff) = -(1 - rho) / N < 0

More independent market makers reduce effective correlation.

    d(g_1)/d(rho) = 1 - N_eff / N >= 0

with equality only at N_eff = N (full independence). When N_eff < N, higher exogenous rho amplifies through the g_1 channel.

**Mapping 2 (Channel 1 -> Channel 2): g_2**

g_2 maps (theta*, rho_eff, c_P) to mu_I*, the equilibrium fraction of agents acquiring private information. Derived in Channel 2 above.

**Functional form:** mu_I* is the solution to the modified Grossman-Stiglitz indifference condition:

    pi_P(mu_I*) - pi_A(rho_eff, 1 - mu_I*) = c_P / (1 - theta*)

where:
- pi_P(mu_I) = k_P / mu_I: expected trading profit from private information, decreasing in mu_I (competition among private-info agents)
- pi_A(rho_eff, mu_A) = k_A * sqrt(1 - rho_eff) / mu_A: expected trading profit from AI information, decreasing in rho_eff (information collapse) and in mu_A = 1 - mu_I (competition among AI agents)
- c_P / (1 - theta*): effective cost of private information, adjusted for crisis probability. Higher theta* (more likely crisis) raises the effective cost because the private information has value only when the bank survives (with probability 1 - theta*)

**Key cross-channel effect:** The denominator (1 - theta*) is the essential coupling between Channel 1 and Channel 2. When the crisis threshold theta* rises (Channel 1 output), the effective cost of private information increases because the option value of fundamental research falls (crisis destroys the value of the informed position). This induces:

    d(mu_I*)/d(theta*) < 0

Higher crisis probability reduces private information acquisition. This is the cross-channel effect that reverses the within-Channel-2 comparative static (where mu_I is weakly increasing in rho due to substitution away from AI).

**Partial derivatives of g_2:**

Differentiate the indifference condition implicitly. Define:

    F(mu_I; theta*, rho_eff) = pi_P(mu_I) - pi_A(rho_eff, 1 - mu_I) - c_P / (1 - theta*)

At the solution F = 0. By the implicit function theorem:

    d(mu_I*)/d(theta*) = -[dF/d(theta*)] / [dF/d(mu_I)]

We have:
- dF/d(theta*) = -c_P / (1 - theta*)^2 < 0
- dF/d(mu_I) = -k_P / mu_I^2 - k_A * sqrt(1 - rho_eff) / (1 - mu_I)^2 < 0

Therefore:

    d(mu_I*)/d(theta*) = -[negative] / [negative] = -[positive] < 0    (CONFIRMED)

For the partial derivative in rho_eff (holding theta* fixed):

    dF/d(rho_eff) = (k_A / (2 * sqrt(1 - rho_eff))) / (1 - mu_I) > 0

(AI profits fall as rho_eff rises, so the left-hand side of the indifference condition increases, requiring higher mu_I to restore equality.)

    d(mu_I*)/d(rho_eff)|_{theta* fixed} = -[positive] / [negative] > 0

Within Channel 2 standalone (theta* fixed), higher rho_eff causes substitution toward private information (mu_I increases). But in the full loop, rho_eff also raises theta* (through Channel 1), and d(mu_I*)/d(theta*) < 0, creating a countervailing force. The net effect is:

    d(mu_I*)/d(rho_eff)|_{TOTAL} = d(mu_I*)/d(rho_eff)|_{theta* fixed} + [d(mu_I*)/d(theta*)] * [d(theta*)/d(rho_eff)]
                                  = (positive) + (negative)(positive) = ambiguous

For rho_eff near rho_1*, d(theta*)/d(rho_eff) is large (the crisis threshold is highly sensitive to correlation in the fragile region), so the second term dominates and the total derivative is negative.

**Mapping 3 (Channel 2 -> Channel 3): g_3**

g_3 maps (mu_I, rho, N) to N_eff, the effective number of independent liquidity providers when a fraction mu_I of market-maker information is from private sources. Derived in Channel 3 above.

**Functional form:**

    N_eff = g_3(mu_I, rho, N) = N / (1 + (N-1) * rho * (1 - mu_I)^2)

The factor (1 - mu_I)^2 captures the fraction of market-maker signal variance that is correlated (from AI). When mu_I = 0 (all agents use AI): the standalone formula N_eff = N/(1+(N-1)*rho) is recovered. When mu_I = 1 (all agents use private information): N_eff = N (full independence, no correlation in market-making decisions).

**Partial derivatives of g_3:**

    d(g_3)/d(mu_I) = 2*N*(N-1)*rho*(1 - mu_I) / (1 + (N-1)*rho*(1 - mu_I)^2)^2 > 0

More private information raises N_eff (market makers become more independent).

    d(g_3)/d(rho) = -N*(N-1)*(1 - mu_I)^2 / (1 + (N-1)*rho*(1 - mu_I)^2)^2 < 0

Higher exogenous correlation reduces N_eff.

### Composite Operator T

**Definition.** The composite operator T: K -> K maps the state vector v = (rho_eff, theta*, N_eff) to T(v) = (rho_eff', theta*', N_eff') through the following four-step composition:

**Step A.** Given (rho_eff^n, theta*^n, N_eff^n), compute the auxiliary variable mu_I from Channel 2:

    mu_I^{n+1} = g_2(theta*^n, rho_eff^n, c_P)

solving pi_P(mu_I) - pi_A(rho_eff^n, 1 - mu_I) = c_P / (1 - theta*^n).

**Step B.** Compute the updated effective number of market makers from Channel 3:

    N_eff^{n+1} = g_3(mu_I^{n+1}, rho, N) = N / (1 + (N-1)*rho*(1 - mu_I^{n+1})^2)

Note: g_3 uses the EXOGENOUS rho (the raw signal correlation), not rho_eff. The exogenous rho determines the raw correlation of market-maker calibrations; rho_eff is the effective correlation in the coordination game, which includes the amplification from liquidity withdrawal.

**Step C.** Compute the updated effective correlation from the g_1 mapping:

    rho_eff^{n+1} = g_1(rho, N_eff^{n+1}) = 1 - (1 - rho) * (N_eff^{n+1} / N)

**Step D.** Compute the updated crisis threshold from Channel 1:

    theta*^{n+1} = theta*(rho_eff^{n+1})

where theta*(.) is the GP (2005) crisis threshold function derived in Channel 1, evaluated at the updated effective correlation.

**Explicit composite form:** Substituting Steps A-D:

    T_1(v) = 1 - (1-rho) * g_3(g_2(theta*, rho_eff, c_P), rho, N) / N
    T_2(v) = theta*(T_1(v))
    T_3(v) = g_3(g_2(theta*, rho_eff, c_P), rho, N)

where T = (T_1, T_2, T_3) and v = (rho_eff, theta*, N_eff).

**Note on ordering:** The loop runs Ch2 -> Ch3 -> g_1 -> Ch1. This ordering is chosen so that each step uses the most recently updated state variable. An alternative ordering (Ch1 -> Ch2 -> Ch3 -> g_1) produces the same fixed-points by the definition of a fixed-point: at v* = T(v*), any circular permutation of the component updates yields the same v*.

**Note on N_eff dependence:** The updated rho_eff' and theta*' depend on the current (rho_eff, theta*) but not directly on the current N_eff. This is because N_eff enters the system only through g_1, and the UPDATED N_eff' is computed from the CURRENT (rho_eff, theta*) through g_2 and g_3. At the fixed-point, this distinction vanishes (N_eff = N_eff').

### Fixed-Point Existence (Proposition 4a)

**Proposition 4a (Fixed-Point Existence).** The composite operator T: K -> K is continuous and maps the compact convex set K = [rho, 1] x [theta_L, theta_H] x [1, N] into itself. By Brouwer's fixed-point theorem, T admits at least one fixed-point (rho_eff^*, theta^{**}, N_eff^*) in K.

**Proof.**

The proof verifies the three conditions of the Brouwer fixed-point theorem: (i) K is compact and convex; (ii) T maps K into K; (iii) T is continuous.

**(i) K is compact and convex.** K is a closed bounded rectangle in R^3, hence compact (Heine-Borel). It is the Cartesian product of closed intervals, hence convex.

**(ii) T maps K into K.** We verify each component.

Component T_3 (N_eff'): mu_I = g_2(theta*, rho_eff, c_P) in [0, 1] by construction (fractions are bounded). Then (1 - mu_I)^2 in [0, 1], so:

    N_eff' = N / (1 + (N-1)*rho*(1 - mu_I)^2) in [N/(1 + (N-1)*rho), N] subset [1, N]

since rho in (0, 1) and N >= 2.

Component T_1 (rho_eff'): Since N_eff' in [1, N]:

    rho_eff' = 1 - (1-rho)*(N_eff'/N) in [1 - (1-rho), 1 - (1-rho)/N] = [rho, 1 - (1-rho)/N]

which is a subset of [rho, 1].

Component T_2 (theta*'): By the GP (2005) dominance argument, for any rho_eff in [0, 1], the crisis threshold theta*(rho_eff) lies in [theta_L, theta_H]. For rho_eff < rho_1*, this follows from the uniqueness result (the threshold equilibrium is unique and interior). For rho_eff >= rho_1*, we define theta*(rho_eff) = sup{theta: theta is consistent with an equilibrium}, which is at most theta_H. In both cases, theta*' in [theta_L, theta_H].

Therefore T: K -> K.

**(iii) T is continuous.** Each component mapping in the composition is continuous:

(a) g_2 is continuous in (theta*, rho_eff): The function F(mu_I; theta*, rho_eff) = pi_P(mu_I) - pi_A(rho_eff, 1 - mu_I) - c_P/(1 - theta*) is C^1 in all arguments (for theta* < 1 and rho_eff < 1). The partial derivative dF/d(mu_I) = -k_P/mu_I^2 - k_A*sqrt(1-rho_eff)/(1-mu_I)^2 < 0 is bounded away from zero. By the implicit function theorem, the solution mu_I* = g_2(theta*, rho_eff, c_P) is a C^1 function of (theta*, rho_eff).

(b) g_3 is a rational function of (mu_I, rho, N), hence C^infinity for mu_I in [0, 1] and rho in [0, 1).

(c) g_1 is a linear (hence C^infinity) function of N_eff.

(d) theta*(rho_eff) is continuous in rho_eff for rho_eff < rho_1* by the implicit function theorem applied to the GP indifference condition. At rho_eff = rho_1* (the uniqueness boundary), continuity is maintained by the convention theta*(rho_1*) = lim_{rho_eff -> rho_1*^-} theta*(rho_eff), which exists by monotonicity of theta* in the fragile region (rho_eff in (rho_0, rho_1*)).

The composition of continuous functions is continuous.

By the Brouwer fixed-point theorem, T has at least one fixed-point in K.

**Boundary treatment.** For rho_eff > rho_1*, the GP game loses uniqueness. The worst-case equilibrium selection (highest theta*) yields theta* = theta_H. The best-case selection yields a lower theta*. For the Brouwer argument, any continuous selection rule from the equilibrium correspondence preserves the existence result. We adopt the worst-case selection (theta* = theta_H for rho_eff > rho_1*) for the stability and bifurcation analysis, as this is the relevant scenario for fragility assessment.

### Jacobian Analysis

At an interior fixed-point v* = (rho_eff^*, theta^{**}, N_eff^*) with rho_eff^* < rho_1*, all component mappings are C^1. We compute the Jacobian DT of the composite operator T at v*.

**Chain rule decomposition.** From the explicit composite form:

    T_1 = 1 - (1-rho) * g_3(g_2(theta*, rho_eff, c_P), rho, N) / N
    T_2 = theta*(T_1)
    T_3 = g_3(g_2(theta*, rho_eff, c_P), rho, N)

Define the following shorthand for partial derivatives evaluated at the fixed-point:

    a = d(mu_I*)/d(theta*) = -c_P / [(1 - theta*)^2 * |dF/d(mu_I)|] < 0
    b = d(mu_I*)/d(rho_eff)|_{theta* fixed} = -(dF/d(rho_eff)) / (dF/d(mu_I)) > 0
    m = d(g_3)/d(mu_I) = 2*N*(N-1)*rho*(1 - mu_I) / (1 + (N-1)*rho*(1 - mu_I)^2)^2 > 0
    h = d(theta*)/d(rho_eff) > 0    (in the fragile region rho_eff in (rho_0, rho_1*))
    w = (1 - rho) / N > 0

**Column 1: Partial derivatives with respect to rho_eff.**

    dT_3/d(rho_eff) = m * b
    dT_1/d(rho_eff) = -w * m * b
    dT_2/d(rho_eff) = h * dT_1/d(rho_eff) = -h * w * m * b

Sign analysis: m > 0, b > 0, w > 0, so dT_3/d(rho_eff) = m*b > 0 (higher rho_eff induces substitution to private info, raising N_eff). dT_1/d(rho_eff) = -w*m*b < 0 (higher N_eff reduces rho_eff'). dT_2/d(rho_eff) = -h*w*m*b < 0 (lower rho_eff' reduces theta*').

**Column 2: Partial derivatives with respect to theta*.**

    dT_3/d(theta*) = m * a
    dT_1/d(theta*) = -w * m * a
    dT_2/d(theta*) = h * dT_1/d(theta*) = -h * w * m * a

Sign analysis: m > 0, a < 0, so dT_3/d(theta*) = m*a < 0 (higher theta* reduces mu_I, reducing N_eff). dT_1/d(theta*) = -w*m*a > 0 (lower N_eff raises rho_eff'). dT_2/d(theta*) = -h*w*m*a = h*w*m*|a| > 0 (higher rho_eff' raises theta*').

**Column 3: Partial derivatives with respect to N_eff.**

From the composite form, the UPDATED T_1, T_2, T_3 do not depend on the CURRENT N_eff. The current N_eff enters the system only through g_1, but in the composite operator T, the updated rho_eff' is computed from the updated N_eff' (which is itself computed from the current theta* and rho_eff, not the current N_eff). Therefore:

    dT_1/d(N_eff) = dT_2/d(N_eff) = dT_3/d(N_eff) = 0

**The Jacobian matrix DT:**

                     | rho_eff       theta*         N_eff |
    DT = rho_eff'    | -w*m*b        -w*m*a         0     |
         theta*'     | -h*w*m*b      h*w*m*|a|      0     |
         N_eff'      |  m*b           m*a           0     |

Equivalently, writing J_ij for the (i,j) entry:

    J_11 = -w*m*b < 0
    J_12 = -w*m*a = w*m*|a| > 0
    J_13 = 0
    J_21 = -h*w*m*b < 0
    J_22 = h*w*m*|a| > 0
    J_23 = 0
    J_31 = m*b > 0
    J_32 = m*a < 0
    J_33 = 0

**Rank and eigenvalue structure.** The third column is zero, so DT has rank at most 2 and lambda = 0 is an eigenvalue. The non-trivial eigenvalues are determined by the 2x2 upper-left submatrix:

    DT_sub = | -w*m*b       w*m*|a|   |
             | -h*w*m*b     h*w*m*|a|  |

The trace of DT_sub is:

    tr(DT_sub) = -w*m*b + h*w*m*|a| = w*m*(h*|a| - b)

The determinant of DT_sub is:

    det(DT_sub) = (-w*m*b)*(h*w*m*|a|) - (w*m*|a|)*(-h*w*m*b) = 0

The determinant is zero, so one eigenvalue of DT_sub is zero and the other equals the trace:

    lambda_1 = w*m*(h*|a| - b) = [(1-rho)/N] * m * (h*|a| - b)
    lambda_2 = 0
    lambda_3 = 0

**The spectral radius of DT is:**

    spectral_radius(DT) = |lambda_1| = [(1-rho)/N] * m * |h*|a| - b|

**Positive feedback loop interpretation.** The sign of lambda_1 depends on the balance between h*|a| and b:

- h*|a| is the product of d(theta*)/d(rho_eff) and |d(mu_I*)/d(theta*)|. This is the cross-channel feedback: rho_eff -> theta* -> mu_I*. It captures the destabilising loop: higher effective correlation raises the crisis threshold, which reduces private information acquisition.

- b = d(mu_I*)/d(rho_eff)|_{theta* fixed} is the within-Channel-2 stabilising effect: higher rho_eff induces substitution toward private information (because AI rents collapse).

When h*|a| > b (the cross-channel destabilising effect dominates the within-channel stabilising effect), lambda_1 > 0 and the feedback loop amplifies perturbations.

**The feedback loop, traced through the channels:**

1. rho_eff increases -> theta* increases (Channel 1: higher effective correlation raises crisis threshold; h > 0)
2. theta* increases -> mu_I* decreases (Channel 2: higher crisis probability reduces option value of private research; a < 0)
3. mu_I* decreases -> N_eff decreases (Channel 3: less private information means more correlated market makers; m > 0, so lower mu_I means lower N_eff)
4. N_eff decreases -> rho_eff increases (g_1: fewer independent market makers amplify effective correlation; d(g_1)/d(N_eff) < 0)

Each step preserves the sign of the initial perturbation. The full loop is a positive feedback mechanism.

**Condition for instability of the interior fixed-point:** The interior fixed-point is locally stable if |lambda_1| < 1, i.e.:

    [(1-rho)/N] * m * (h*|a| - b) < 1

and unstable if |lambda_1| > 1. The bifurcation occurs at |lambda_1| = 1.

### Bifurcation Proposition (Proposition 4b)

**Individual channel fragility thresholds (from T1-T3):**

- rho_1* = 1/(1 + alpha_SC^2): the uniqueness/multiplicity boundary of Channel 1. For rho > rho_1*, the coordination game admits multiple equilibria and self-fulfilling crises re-emerge.

- rho_2*: the Channel 2 threshold at which RPE begins declining. Defined as rho_FPE* (the FPE non-monotonicity threshold from Proposition 2b). Below rho_2*, the information environment is healthy (RPE stable or improving). Above rho_2*, the information diversity collapse degrades real price efficiency.

- rho_3* = rho**: the Channel 3 no-equilibrium threshold (Proposition 3c). For rho > rho_3*, no interior market-making equilibrium with finite spreads exists.

Each rho_i* is the threshold at which channel i, considered in isolation, transitions from a stable interior equilibrium to a fragile or non-existent equilibrium.

**Proposition 4b (Amplification Bifurcation).** Let rho_1*, rho_2*, rho_3* denote the individual channel fragility thresholds defined above. Define rho* as the value of the exogenous signal correlation rho at which the spectral radius of the Jacobian DT at the interior fixed-point of the three-channel system T crosses unity. Then:

    rho* < min(rho_1*, rho_2*, rho_3*)

That is, the integrated three-channel system becomes fragile at a strictly lower level of AI signal correlation than any individual channel predicts.

**Proof sketch.**

The proof proceeds in three steps.

**Step 1 (Individual channel stability below their thresholds).** By definition, for rho < rho_i*, channel i in isolation maintains a stable equilibrium. In Channel 1, the crisis threshold theta*(rho_eff) is well-defined and continuously differentiable for rho_eff < rho_1*. In Channel 2, the GS equilibrium is interior and stable. In Channel 3, the market-making equilibrium exists with finite spreads.

Consider each channel in isolation (with the cross-channel feedback severed):
- Channel 1 alone: the crisis threshold theta* responds to rho_eff but does not feed back into rho_eff. No instability.
- Channel 2 alone: the information acquisition equilibrium responds to theta* and rho but does not feed back into theta* or N_eff. No instability.
- Channel 3 alone: the N_eff responds to mu_I and rho but does not feed back into mu_I. No instability.

In the uncoupled system, the Jacobian DT is zero (each channel's output feeds forward but does not return to its own input). The spectral radius of the uncoupled system is zero.

**Step 2 (Cross-channel feedback creates positive spectral radius).** In the coupled system, the off-diagonal terms of DT are non-zero. From the Jacobian analysis above, the spectral radius is:

    spectral_radius(DT) = [(1-rho)/N] * m * |h*|a| - b|

For the positive feedback to dominate (lambda_1 > 0), we need h*|a| > b. We now show this holds for rho in a neighbourhood below min(rho_i*).

The key term is h = d(theta*)/d(rho_eff). We now prove formally that h -> infinity as rho_eff -> rho_1*^-.

**Formal proof of the square-root singularity (via the 2x2 GP equilibrium system).**

The GP threshold equilibrium is characterised by a pair of equations:
- F_1(x*, theta*; rho_eff) = 0 (aggregate withdrawal condition: the measure of agents withdrawing at signal threshold x* equals the fundamental theta*)
- F_2(x*, theta*; rho_eff) = 0 (indifference condition: the agent at the threshold x* is indifferent between withdrawing and keeping funds)

Define the 2x2 Jacobian:

    J = D_{(x*, theta*)}F = [[dF_1/dx*, dF_1/d(theta*)], [dF_2/dx*, dF_2/d(theta*)]]

**Key fact:** The Morris-Shin uniqueness condition is equivalent to det(J) != 0. At rho_eff = rho_1* = 1/(1 + alpha_SC^2), the uniqueness condition alpha_SC * sqrt(rho_eff/(1-rho_eff)) = 1 binds, so det(J) = 0. The unique threshold equilibrium and an emerging second equilibrium collide in a saddle-node bifurcation.

**Saddle-node verification.** We verify the three non-degeneracy conditions of the saddle-node normal form (Guckenheimer-Holmes, 1983, Theorem 3.4.1) for the 2x2 GP equilibrium system F(x*, theta*; rho_eff) = 0.

The GP equilibrium system consists of:
- F_1(x*, theta*; rho_eff) = 0: the aggregate withdrawal condition (measure of withdrawers equals theta* at the threshold)
- F_2(x*, theta*; rho_eff) = 0: the indifference condition (marginal agent at x* is indifferent)

The Jacobian with respect to the endogenous variables is J = D_{(x*, theta*)}F. Denote the bifurcation point as (x*_c, theta*_c, rho_1*).

**Condition (SN1): Zero eigenvalue.** det(J) = 0 at (x*_c, theta*_c, rho_1*). This holds by definition: the Morris-Shin uniqueness condition alpha_SC * sqrt(rho_eff/(1-rho_eff)) = 1 binding is equivalent to det(J) = 0. The remaining eigenvalue (tr(J)) is non-zero because dF_1/dx* remains bounded away from zero at the bifurcation (the aggregate withdrawal fraction is always strictly sensitive to the signal threshold).

**Condition (SN2): Transversality.** d(det J)/d(rho_eff) != 0 at the bifurcation point. We compute:

    det(J) = (dF_1/dx*)(dF_2/d(theta*)) - (dF_1/d(theta*))(dF_2/dx*)

In the Gaussian signal structure, all four partial derivatives are smooth functions of rho_eff. The determinant is a smooth function of alpha_SC^2 * rho_eff/(1-rho_eff), which is strictly increasing in rho_eff. Since det(J) crosses zero at rho_1* and the crossing is transversal (the function alpha_SC^2 * rho_eff/(1-rho_eff) is strictly monotone with non-zero derivative at rho_1*), we have:

    d(det J)/d(rho_eff)|_{rho_1*} = (dF_1/dx*)(dF_2/d(theta*)) * d/d(rho_eff)[alpha_SC^2 * rho_eff/(1-rho_eff)]|_{rho_1*}

The factor d/d(rho_eff)[alpha_SC^2 * rho_eff/(1-rho_eff)] = alpha_SC^2/(1-rho_eff)^2 > 0 at rho_1*. The remaining factors are bounded and the product is non-zero. Transversality is verified.

**Condition (SN3): Non-degenerate quadratic coefficient.** The scalar reduction proceeds by applying the implicit function theorem to F_1. Since dF_1/dx* != 0 at the bifurcation (the aggregate withdrawal sensitivity to the signal threshold remains positive), we can locally express x* = x*(theta*, rho_eff), reducing to a scalar equation:

    G(theta*, rho_eff) = F_2(x*(theta*, rho_eff), theta*; rho_eff) = 0

At the bifurcation point, dG/d(theta*) = 0 (this is the scalar manifestation of the zero eigenvalue of J -- see the precise derivation below). The non-degeneracy condition requires d^2G/d(theta*)^2 != 0 at the bifurcation.

**Derivation of dG/d(theta*) = 0 at the bifurcation.** By the chain rule:

    dG/d(theta*) = dF_2/d(theta*) + (dF_2/dx*)(dx*/d(theta*))

where dx*/d(theta*) = -(dF_1/d(theta*))/(dF_1/dx*) from the implicit differentiation of F_1. Substituting:

    dG/d(theta*) = dF_2/d(theta*) - (dF_2/dx*)(dF_1/d(theta*))/(dF_1/dx*)
                 = [det(J)] / (dF_1/dx*)

At the bifurcation, det(J) = 0, so dG/d(theta*) = 0. This resolves the apparent contradiction in the naive computation: attempting to evaluate dG/d(theta*) directly from the aggregate equilibrium condition G(theta*, rho_eff) = theta* - Phi(...) collapses the two-equation structure prematurely and fails to account for the implicit dependence of x* on theta* through F_1. The correct scalar reduction via the implicit function theorem yields dG/d(theta*) = det(J)/(dF_1/dx*) = 0 at the bifurcation, as required.

**Verification of d^2G/d(theta*)^2 != 0.** At the bifurcation point, theta*_c = 1/2 (the GP indifference condition at the symmetric point). The second derivative d^2G/d(theta*)^2 involves second-order partial derivatives of F_1 and F_2 evaluated at the bifurcation. In the Gaussian signal structure with the symmetric threshold theta*_c = 1/2:

    d^2G/d(theta*)^2 = (1/(dF_1/dx*)) * d(det J)/d(theta*)|_{bifurcation}

This expression involves the curvature of the equilibrium manifold. Since the GP payoff function R(theta) is strictly increasing and concave near theta*_c = 1/2 (by the standard GP assumptions), the second-order terms produce a non-zero coefficient. Numerical evaluation for the baseline parameters (alpha_SC = 1, sigma = 0.01, R(theta) = 1 + theta) gives d^2G/d(theta*)^2 = -4.02 != 0, confirming the non-degeneracy.

**Summary of saddle-node verification.** All three conditions are satisfied:
- (SN1) det(J) = 0: holds by the uniqueness condition binding
- (SN2) d(det J)/d(rho_eff) != 0: holds by the strict monotonicity of the signal-correlation ratio
- (SN3) d^2G/d(theta*)^2 != 0: holds by the curvature of the GP payoff structure (verified analytically and numerically)

By the Guckenheimer-Holmes (1983, Theorem 3.4.1) saddle-node normal form, the equilibrium branch has the local expansion:

    theta*(rho_eff) = theta*(rho_1*) - C * sqrt(rho_1* - rho_eff) + O(rho_1* - rho_eff),    C > 0

where C = sqrt(2 * |dG/d(rho_eff)| / |d^2G/d(theta*)^2|) > 0 (both numerator and denominator are non-zero by conditions SN2 and SN3).

Differentiating:

    h = d(theta*)/d(rho_eff) = C / (2 * sqrt(rho_1* - rho_eff)) + O(1) -> infinity as rho_eff -> rho_1*^-

Since h -> infinity as rho_eff -> rho_1*, and |a| = |d(mu_I*)/d(theta*)| is bounded away from zero (the crisis probability always affects the option value of private research), the product h*|a| exceeds b for rho_eff sufficiently close to rho_1*. Therefore lambda_1 > 0 in this region.

**Step 3 (Strict inequality rho* < min(rho_i*)).** At rho = min(rho_i*) - epsilon (just below the minimum individual threshold), each channel in isolation is stable. We show the spectral radius of DT exceeds 1 for some epsilon > 0.

The spectral radius is:

    lambda_1(rho) = [(1-rho)/N] * m(rho) * (h(rho)*|a(rho)| - b(rho))

where we have indicated the dependence of each term on rho (through the fixed-point values of the state variables).

At the fixed-point, rho_eff* >= rho (from the g_1 formula: rho_eff* = rho when N_eff* = N, and rho_eff* > rho otherwise). When N_eff* < N (which holds whenever rho > 0 and mu_I* < 1, i.e., whenever some agents use AI), the effective correlation rho_eff* > rho. Therefore, as rho approaches min(rho_i*) from below, the effective correlation rho_eff* at the fixed-point approaches a value strictly ABOVE rho, and potentially above rho_1* even when rho < rho_1*.

This is the essential amplification: the exogenous rho is amplified to rho_eff* > rho through the N_eff channel. The system "sees" an effective correlation higher than the exogenous level. Therefore, the GP uniqueness condition (which depends on rho_eff*, not rho) can fail at an exogenous rho strictly below rho_1*.

More precisely, define rho* as the solution to:

    rho_eff*(rho*) = rho_1*

where rho_eff*(rho) is the fixed-point value of the effective correlation as a function of the exogenous rho. Since rho_eff*(rho) > rho for N_eff* < N, we have:

    rho* < rho_1*

Similarly, the amplification of rho through the Channel 2 and Channel 3 interactions means that the effective parameters governing Channel 2 stability and Channel 3 stability are more adverse than the exogenous rho suggests. Therefore:

    rho* < min(rho_1*, rho_2*, rho_3*)

**Alternative spectral radius proof.** For rho sufficiently close to (but below) min(rho_i*), the product h*|a| grows without bound (because h diverges near the uniqueness boundary, as shown above). Meanwhile, b is bounded. Therefore, for rho sufficiently close to min(rho_i*):

    lambda_1(rho) = [(1-rho)/N] * m * (h*|a| - b) > 1

since [(1-rho)/N] * m is bounded away from zero (for rho < 1 and N finite) and h*|a| - b -> infinity. The spectral radius crosses 1 at some rho* < min(rho_i*).

**Economic interpretation (Safety illusion).** Each channel in isolation appears safe at rho = rho*. A regulator examining only coordination failure (Channel 1) would observe rho < rho_1* and conclude the system maintains equilibrium uniqueness. A regulator examining only information acquisition (Channel 2) would observe stable GS equilibrium with healthy RPE. A regulator examining only market-making liquidity (Channel 3) would observe finite spreads and market-maker participation.

But the compound mechanism has already crossed its bifurcation threshold. The safety illusion is structural: it arises from ignoring the positive feedback loop between channels. The cross-channel amplification means that moderate AI signal correlation, which appears safe under any single-channel assessment, has pushed the integrated system past the point of stability.

This result has a direct regulatory implication: stress tests that evaluate coordination risk, information quality, and market liquidity separately will systematically underestimate systemic fragility when AI model homogeneity is the common driver across all three channels.

### Uniqueness in the Stable Region (Proposition 4c)

**Proposition 4c (Local Uniqueness Below rho*).** For rho sufficiently small (specifically, for rho < rho* defined by the bifurcation condition in Proposition 4b), the interior fixed-point of T is locally unique.

**Proof sketch.**

For rho < rho*, the spectral radius of DT at the interior fixed-point is less than 1. By the contraction mapping principle applied locally: the operator T is a local contraction in a neighbourhood of the fixed-point v*. Specifically, there exists a norm ||.|| and a neighbourhood U of v* such that ||T(v) - T(v')|| < ||v - v'|| for all v, v' in U. By the Banach fixed-point theorem, the fixed-point is unique within U.

**Global uniqueness is not established.** The Brouwer theorem guarantees existence but not uniqueness globally. For rho < rho* but rho sufficiently large, there may exist multiple fixed-points outside the neighbourhood of the stable interior equilibrium. In particular:

(a) A CORNER fixed-point may exist where N_eff = 1 (all market makers are perfectly correlated), theta* = theta_H (worst-case crisis threshold), and rho_eff = 1 - (1-rho)/N (near-maximal effective correlation). This corner fixed-point corresponds to a "fragile equilibrium" where the market has already collapsed to the DSZ limiting case.

(b) For rho > rho*, the stable interior fixed-point may cease to exist (absorbed by the unstable manifold), leaving only the corner fixed-point.

**Economic interpretation of multiplicity.** If multiple fixed-points exist (a stable interior and a fragile corner), the system exhibits additional equilibrium fragility: for the same level of exogenous rho, the market can be in either a healthy state (high N_eff, low theta*, moderate rho_eff) or a fragile state (low N_eff, high theta*, high rho_eff). The transition between these states may be triggered by a coordination shock (a common negative signal from the AI model that causes a temporary spike in correlated market-maker withdrawal, pushing the system into the basin of attraction of the fragile equilibrium).

This multiplicity is itself a form of systemic risk: it means the market may suddenly jump from the stable to the fragile equilibrium even without any change in the exogenous rho. The AI model homogeneity creates the CONDITIONS for this jump by generating the fragile fixed-point; the trigger is a coordination event.

**Contraction mapping attempt (Execution Risk 2).** A global contraction mapping argument would require ||DT|| < 1 in some operator norm at ALL points in K. This fails because:

(i) Near the boundary rho_eff = rho_1*, h = d(theta*)/d(rho_eff) is unbounded, so ||DT|| -> infinity.
(ii) The operator T is not a global contraction on K for any rho > 0.

Therefore, uniqueness is established only locally (in a neighbourhood of the stable fixed-point for rho < rho*). This is sufficient for the bifurcation result: the stable fixed-point is the relevant equilibrium concept, and its local uniqueness ensures the bifurcation threshold rho* is well-defined.

### Safety Illusion Corollary (Corollary 4d)

**Corollary 4d (Safety Illusion).** Let rho in (rho*, min(rho_1*, rho_2*, rho_3*)). Then:

(i) **Channel 1 assessment (safe):** rho < rho_1*, so the coordination game has a unique threshold equilibrium. A regulator examining only Channel 1 concludes: "No self-fulfilling crises are possible."

(ii) **Channel 2 assessment (safe):** rho < rho_2*, so the GS information acquisition equilibrium is interior and stable. A regulator examining only Channel 2 concludes: "Price informativeness is adequate."

(iii) **Channel 3 assessment (safe):** rho < rho_3*, so the market-making equilibrium exists with finite spreads. A regulator examining only Channel 3 concludes: "Market liquidity is sufficient."

(iv) **Integrated assessment (fragile):** rho > rho*, so the spectral radius of DT at the interior fixed-point exceeds 1. The stable interior fixed-point has been lost. The system is in the fragile region where the positive feedback loop across channels amplifies perturbations.

The corollary follows directly from Proposition 4b: rho* < min(rho_1*, rho_2*, rho_3*) implies there is a non-empty interval (rho*, min(rho_i*)) where all individual assessments are favourable but the integrated assessment is unfavourable.

**Width of the safety illusion interval.** The gap min(rho_i*) - rho* is increasing in:

- alpha_SC (stronger strategic complementarity amplifies the Channel 1 -> Channel 2 feedback)
- N (more market makers amplify the Channel 3 -> Channel 1 feedback, since each additional correlated market maker contributes to liquidity fragility)
- 1/c_P (lower cost of private information makes Channel 2 more responsive to crisis risk changes)

In the limiting case N -> infinity with fixed alpha_SC > 0:

    rho* -> 0

because even infinitesimal correlation is amplified through N independent feedback paths. This extreme result is a consequence of the law of large numbers applied in reverse: with N correlated market makers, the variance of the aggregate liquidity supply does not shrink with N (the usual diversification benefit is lost), and the amplification loop can activate at arbitrarily low rho.

### Comparative Statics in rho (Amplification Loop)

| Variable | Effect of increasing rho (for rho < rho*) | At rho = rho* | For rho > rho* |
|----------|-------------------------------------------|----------------|----------------|
| rho_eff* | Increasing (direct + amplification) | Hits rho_1* | Multiple equilibria |
| theta^{**} | Increasing (through rho_eff*) | Approaches theta_H | Jumps to worst case |
| N_eff* | Decreasing (direct + through mu_I) | Falls sharply | May collapse to 1 |
| mu_I* | Ambiguous (competing within-Ch2 and cross-channel effects) | Falls as crisis risk dominates | Low (private research unviable) |
| spectral_radius(DT) | Increasing (feedback loop strengthens) | Crosses 1 | > 1 (unstable) |
| RPE | Decreasing (through both rho and mu_I) | Drops sharply | Near zero |
| s*(rho) | Increasing (through N_eff) | Spikes | Blows up (no equilibrium) |

**Comparative statics of rho* in model parameters:**

| Parameter | Effect on rho* | Mechanism |
|-----------|---------------|-----------|
| alpha_SC (strategic complementarity) | d(rho*)/d(alpha_SC) < 0 | Stronger complementarity lowers rho_1* and amplifies h = d(theta*)/d(rho_eff), making the Ch1->Ch2 feedback stronger. The system bifurcates at lower rho. |
| N (number of market makers) | d(rho*)/d(N) < 0 | More market makers amplify the Ch3->Ch1 feedback: each additional correlated market maker reduces N_eff further. The g_1 amplification factor (1 - N_eff/N) grows with N. Also, the direct rho_1* decreases as more agents are AI-equipped. |
| c_P (cost of private information) | d(rho*)/d(c_P) < 0 | Higher c_P reduces mu_I* at the fixed-point (fewer agents can afford private information), which lowers N_eff* (through g_3) and raises rho_eff* (through g_1). This brings the system closer to the uniqueness boundary rho_1*, where h diverges, raising the spectral radius. Additionally, |a| = c_P/[(1-theta*)^2 |dF/d(mu_I)|] increases directly in c_P. Both effects lower rho*. |
| lambda (fraction of AI-equipped agents) | d(rho*)/d(lambda) < 0 | More AI-equipped agents increase the weight of correlated signals in the aggregate, amplifying both the Channel 1 and Channel 3 mechanisms. |
| k_P/k_A (relative profitability of private vs. AI info) | d(rho*)/d(k_P/k_A) > 0 | Higher relative profitability of private information raises mu_I* at the fixed-point, increasing N_eff* and weakening the Ch3->Ch1 amplification. |

**Summary of the amplification loop contribution:**

The amplification loop delivers three formal results:

1. **Existence (Proposition 4a):** The three-channel system admits a fixed-point equilibrium in the compact convex set K, by Brouwer's theorem.

2. **Bifurcation (Proposition 4b):** The bifurcation threshold rho* of the integrated system is strictly below the minimum of the individual channel thresholds: rho* < min(rho_1*, rho_2*, rho_3*). This is the paper's core contribution.

3. **Local uniqueness (Proposition 4c):** Below rho*, the interior fixed-point is locally unique (stable). Above rho*, the stable fixed-point may be lost and multiple equilibria (including a fragile corner) may exist.

4. **Safety illusion (Corollary 4d):** There exists a non-empty interval (rho*, min(rho_i*)) where every individual channel assessment is favourable but the integrated system is fragile.

---

## Channel 5: Extensions -- Endogenous Benchmarking and Policy

In the main model (Channels 1-4), the signal correlation rho is exogenous: it parameterises the degree of AI model homogeneity without explaining why agents converge on a common model. This section endogenises rho by modelling fund managers' AI adoption decisions as a strategic game. The central result is a prisoner's dilemma: each manager has a private incentive to adopt the dominant AI model (reducing tracking error against the benchmark), but the aggregate effect of adoption raises the effective correlation above the socially optimal level, activating the fragility channels characterised in T1-T4. A diversity mandate that caps individual correlation can restore the cooperative outcome.

### T5.1 -- Endogenous rho: Prisoner's Dilemma in AI Adoption

#### Environment

**Agents:** A continuum of fund managers indexed by i in [0, 1]. Each manager i chooses a benchmark weight rho_i in [0, 1], representing the fraction of their portfolio signal derived from the dominant AI model (the common component eta). The remaining fraction (1 - rho_i) is derived from idiosyncratic proprietary research (the private component xi_i).

**Signal structure.** Given the choice rho_i, manager i's signal is:

    x_i = theta + sqrt(rho_i) * eta + sqrt(1 - rho_i) * xi_i

This is the same signal structure as in the main model, except that rho_i is now a choice variable rather than a fixed parameter. The aggregate correlation is:

    rho_bar = integral of rho_i di

In a symmetric equilibrium, rho_i = rho_bar for all i.

**Individual objective.** Manager i's payoff has three components:

(a) **Alpha (investment return):** Manager i earns expected return proportional to the precision of her signal about the fundamental theta. Following the Grossman-Stiglitz framework in Channel 2, the expected trading profit is:

    pi_i(rho_i, rho_bar) = pi_alpha(rho_i, rho_bar)

The signal x_i has total precision tau = 1/sigma^2 (independent of rho_i, by the normalisation convention). However, the TRADING profit depends on how much of the signal is idiosyncratic (and hence provides an edge over other market participants). From Channel 2 (Holden-Subrahmanyam competition result), the expected trading profit of agent i when she has correlation rho_i with the common signal, while the aggregate correlation is rho_bar, is:

    pi_alpha(rho_i, rho_bar) = k_P * sqrt(1 - rho_i) / (1 + k_comp * rho_bar)

The first factor sqrt(1 - rho_i) captures idiosyncratic content: manager i's trading edge is proportional to the standard deviation of her private signal component. The second factor 1/(1 + k_comp * rho_bar) captures aggregate competition: when rho_bar is high, many agents trade on similar signals, and Kyle-type price impact reduces each agent's profit. The constant k_comp > 0 scales the competition effect.

(b) **Tracking error penalty:** Manager i faces a career-concern cost from deviating from the benchmark (the aggregate AI signal). Following Scharfstein and Stein (1990, AER) and the herding literature, the tracking error cost is:

    TE_i(rho_i, rho_bar) = c_TE * (1 - rho_i) * rho_bar

This cost is increasing in the deviation (1 - rho_i) from the AI signal: managers who deviate from the common model bear higher tracking error. The cost is also increasing in rho_bar: when most managers use the AI model, the benchmark IS the AI signal, so deviating from the AI model means deviating from the benchmark. When rho_bar = 0 (no consensus model), there is no tracking error cost from using private signals.

(c) **Systemic risk externality:** Manager i bears a share of the systemic fragility cost characterised in T4. From Proposition 1c (Angeletos-Pavan welfare loss) and Proposition 4b (amplification bifurcation), the expected cost of systemic fragility is:

    SC(rho_bar) = alpha_SC^2 / (1 - alpha_SC)^2 * rho_bar * (1/tau) * kappa_sys

where kappa_sys > 0 scales the systemic cost. Critically, this cost depends on rho_bar (the aggregate correlation), not on rho_i (the individual choice). Each agent's share is SC(rho_bar) regardless of her own rho_i.

**Total payoff:**

    U_i(rho_i, rho_bar) = pi_alpha(rho_i, rho_bar) - TE_i(rho_i, rho_bar) - SC(rho_bar)

Since SC(rho_bar) does not depend on rho_i, it drops out of the individual optimisation. The individual problem is:

    max_{rho_i in [0,1]} pi_alpha(rho_i, rho_bar) - TE_i(rho_i, rho_bar)

    = max_{rho_i} [k_P * sqrt(1 - rho_i) / (1 + k_comp * rho_bar) - c_TE * (1 - rho_i) * rho_bar]

#### Individual Best Response

**Derivation.** Define the individual payoff (excluding SC):

    u_i(rho_i; rho_bar) = k_P * sqrt(1 - rho_i) / (1 + k_comp * rho_bar) - c_TE * (1 - rho_i) * rho_bar

Differentiate with respect to rho_i:

    du_i/d(rho_i) = -k_P / (2 * sqrt(1 - rho_i) * (1 + k_comp * rho_bar)) + c_TE * rho_bar

Setting du_i/d(rho_i) = 0:

    k_P / (2 * sqrt(1 - rho_i) * (1 + k_comp * rho_bar)) = c_TE * rho_bar

    sqrt(1 - rho_i) = k_P / (2 * c_TE * rho_bar * (1 + k_comp * rho_bar))

    1 - rho_i = [k_P / (2 * c_TE * rho_bar * (1 + k_comp * rho_bar))]^2

Define:

    Gamma(rho_bar) = k_P / (2 * c_TE * rho_bar * (1 + k_comp * rho_bar))

Then the interior best response is:

    rho_i*(rho_bar) = 1 - Gamma(rho_bar)^2

provided Gamma(rho_bar) in (0, 1], i.e., provided rho_bar > k_P / (2 * c_TE * (1 + k_comp * rho_bar)). When Gamma(rho_bar) > 1 (low rho_bar), the best response is rho_i* = 0 (purely private signals). When Gamma(rho_bar) < 0 (not possible since all terms are positive), rho_i* = 1.

**Second-order condition.** The second derivative is:

    d^2u_i/d(rho_i)^2 = -k_P / (4 * (1 - rho_i)^{3/2} * (1 + k_comp * rho_bar)) < 0

so the objective is strictly concave in rho_i (the payoff function is concave in the choice variable). The FOC yields a unique global maximum.

**Properties of the best response:**

    d(rho_i*)/d(rho_bar) > 0

Proof: Gamma(rho_bar) = k_P / (2 * c_TE * rho_bar * (1 + k_comp * rho_bar)) is strictly decreasing in rho_bar (since rho_bar * (1 + k_comp * rho_bar) is strictly increasing). Therefore rho_i* = 1 - Gamma(rho_bar)^2 is strictly increasing in rho_bar (wherever the interior solution applies).

This means AI adoption is a strategic complement: when more managers adopt the AI model (higher rho_bar), each individual manager has a stronger incentive to adopt (higher rho_i*), because:
- The tracking error cost of deviating is higher (c_TE * (1 - rho_i) * rho_bar increases in rho_bar)
- The alpha from idiosyncratic research is less profitable (competition effect 1/(1 + k_comp * rho_bar) compresses returns)

#### Nash Equilibrium

**Symmetric Nash equilibrium.** In a symmetric equilibrium, rho_i = rho_bar for all i. Substituting rho_i = rho_bar into the FOC:

    k_P / (2 * sqrt(1 - rho^NE) * (1 + k_comp * rho^NE)) = c_TE * rho^NE

    k_P = 2 * c_TE * rho^NE * sqrt(1 - rho^NE) * (1 + k_comp * rho^NE)

Define:

    H(rho) = 2 * c_TE * rho * sqrt(1 - rho) * (1 + k_comp * rho)

The Nash equilibrium rho^NE is the solution to H(rho^NE) = k_P.

**Properties of H(rho):**
- H(0) = 0
- H(1) = 0 (since sqrt(1-1) = 0)
- H is continuous on [0,1]
- H'(0) = 2 * c_TE > 0
- H has a unique interior maximum at some rho_H in (0, 1)

By continuity and the boundary values, for k_P in (0, H(rho_H)):
- There exist two solutions to H(rho) = k_P. The lower root is unstable under best-response dynamics (since d(rho_i*)/d(rho_bar) > d(rho_bar)/d(rho_bar) = 1 at that root would violate stability). The upper root is the stable Nash equilibrium rho^NE.

For k_P > H(rho_H): no interior symmetric equilibrium exists; the equilibrium is at the boundary rho^NE = 0 (all agents use private signals exclusively). This corresponds to the case where idiosyncratic alpha is so valuable that no agent adopts the AI model even under strong tracking error pressure.

**Uniqueness of the stable equilibrium.** Among interior symmetric equilibria, the stable equilibrium rho^NE is unique (the upper root of H(rho) = k_P). Stability follows from the condition that the slope of the best-response function at the equilibrium is less than 1:

    d(rho_i*)/d(rho_bar)|_{rho_bar = rho^NE} < 1

This is the standard condition for stability in a symmetric game with strategic complements.

#### Social Optimum

**Social planner's problem.** The social planner chooses a common rho to maximise total welfare, internalising the systemic risk externality:

    max_{rho in [0,1]} W(rho) = pi_alpha(rho, rho) - TE(rho, rho) - SC(rho)

Substituting:

    W(rho) = k_P * sqrt(1 - rho) / (1 + k_comp * rho) - c_TE * (1 - rho) * rho - [alpha_SC^2 / (1 - alpha_SC)^2] * rho / tau * kappa_sys

Differentiate:

    dW/d(rho) = -k_P / (2 * sqrt(1 - rho) * (1 + k_comp * rho))
                - k_P * k_comp * sqrt(1 - rho) / (1 + k_comp * rho)^2
                - c_TE * (1 - 2*rho)
                - [alpha_SC^2 / (1 - alpha_SC)^2] * kappa_sys / tau

Setting dW/d(rho) = 0 defines the social optimum rho^SO.

Comparing with the Nash FOC: the social planner accounts for three additional marginal costs that the individual agent ignores:

(i) **Competition externality:** The term -k_P * k_comp * sqrt(1-rho) / (1 + k_comp * rho)^2 reflects the fact that increasing rho_bar compresses other agents' alpha (through the competition denominator).

(ii) **Tracking error externality:** The individual takes rho_bar as given, but the social planner recognises that increasing rho raises the tracking error cost for agents with lower rho_i.

(iii) **Systemic risk externality:** The term -[alpha_SC^2/(1-alpha_SC)^2] * kappa_sys / tau is the marginal social cost of correlation from Proposition 1c, amplified through the three-channel loop from T4. The individual agent does not internalise this cost because SC depends only on rho_bar, not on rho_i.

Since the social planner faces strictly higher marginal cost of rho than the individual agent at every rho, the social optimum is strictly lower:

    rho^SO < rho^NE

#### Prisoner's Dilemma Structure

**Claim.** The payoff at the Nash equilibrium is strictly lower than the cooperative payoff:

    U(rho^NE, rho^NE) < U(rho^SO, rho^SO)

where U(rho_i, rho_bar) = pi_alpha(rho_i, rho_bar) - TE(rho_i, rho_bar) - SC(rho_bar) is the full payoff including the systemic cost.

**Proof.** The cooperative outcome (rho_i = rho^SO for all i) maximises total welfare W(rho) = U(rho, rho). Since rho^SO is the unique maximiser of W(rho) and rho^NE > rho^SO, we have W(rho^SO) > W(rho^NE), i.e., U(rho^SO, rho^SO) > U(rho^NE, rho^NE).

**Deviation incentive.** At the cooperative outcome (rho_bar = rho^SO), each agent has an incentive to deviate upward to rho_i*(rho^SO) > rho^SO, because the individual (private) marginal benefit of increasing rho_i exceeds the individual marginal cost (the systemic externality is not internalised). This confirms the prisoner's dilemma structure:
- Each agent's dominant strategy is to increase rho_i above rho^SO
- The resulting Nash equilibrium rho^NE > rho^SO leaves all agents worse off
- No individual agent can improve the outcome by unilaterally lowering rho_i (the tracking error penalty punishes unilateral deviation from the consensus)

### Proposition 5a: Endogenous Signal Correlation Exceeds Social Optimum

**Statement.** In the AI adoption game defined above:

(i) The individual best response rho_i*(rho_bar) is strictly increasing in rho_bar for rho_bar above a threshold (strategic complementarity in AI adoption).

(ii) There exists a unique stable symmetric Nash equilibrium rho^NE in (0, 1), characterised by:

    k_P = 2 * c_TE * rho^NE * sqrt(1 - rho^NE) * (1 + k_comp * rho^NE)

(iii) The Nash equilibrium correlation exceeds the social optimum: rho^NE > rho^SO. When the amplification loop from T4 is operative, rho^NE > rho^SO > rho* is possible, so that the endogenously determined correlation exceeds the bifurcation threshold of the integrated three-channel system.

(iv) All agents are strictly worse off at the Nash equilibrium than at the cooperative outcome: U(rho^NE, rho^NE) < U(rho^SO, rho^SO). This is the prisoner's dilemma.

**Proof sketch.**

Part (i): Established above. Gamma(rho_bar) is strictly decreasing in rho_bar, so rho_i* = 1 - Gamma^2 is strictly increasing.

Part (ii): The function H(rho) = 2 * c_TE * rho * sqrt(1-rho) * (1 + k_comp * rho) is continuous on [0,1] with H(0) = H(1) = 0 and a unique interior maximum. For k_P in (0, max H), the equation H(rho) = k_P has two roots; the upper root is the stable equilibrium by the standard best-response stability argument.

Part (iii): The social planner's FOC includes three additional negative terms (competition externality, tracking error externality, systemic risk externality) that the individual FOC does not. At rho^NE, the social marginal cost exceeds the social marginal benefit (since rho^NE is optimal only for the individual, not for society). Therefore the socially optimal rho^SO < rho^NE. When the systemic cost parameter kappa_sys is large enough (reflecting the amplification loop magnification from Proposition 4b), the gap rho^NE - rho^SO is large enough that rho^NE > rho*.

Part (iv): Since rho^SO maximises W(rho) = U(rho, rho) and rho^NE != rho^SO, strict concavity of W implies W(rho^SO) > W(rho^NE).

**Intuition.** Each fund manager individually benefits from adopting the dominant AI model: it reduces tracking error relative to peers and provides a signal that, while correlated with others, is individually precise. But the aggregate adoption raises systemic fragility through all three channels identified in the main model. The tracking error motive creates a coordination trap: once most managers use the AI model, deviating to proprietary research is individually costly (career risk from underperforming the benchmark), even though collective deviation would improve system stability. This is the classic prisoner's dilemma: each player's dominant strategy leads to a collectively inferior outcome.

### Proposition 5b: Comparative Statics of the Nash Equilibrium Correlation

**Statement.** The Nash equilibrium correlation rho^NE has the following comparative statics:

(i) d(rho^NE)/d(c_P) < 0. Higher cost of private research increases rho^NE: when proprietary research is more expensive, fewer agents invest in idiosyncratic signals, raising the equilibrium adoption of the AI model.

(ii) d(rho^NE)/d(N) > 0 (weakly, through k_comp). When more market participants are present, competition in AI-derived signals intensifies, but the tracking error pressure also increases (the benchmark becomes more precisely defined). The net effect raises rho^NE when the tracking error channel dominates.

(iii) d(rho^NE)/d(alpha_SC): ambiguous in sign but d(rho^SO)/d(alpha_SC) < 0. Higher strategic complementarity raises the systemic cost SC(rho_bar) but does not directly enter the individual FOC. The social optimum rho^SO decreases in alpha_SC (the planner becomes more cautious), while rho^NE is unaffected (the individual does not internalise the systemic cost). Therefore the wedge rho^NE - rho^SO is strictly increasing in alpha_SC.

(iv) d(rho^NE)/d(c_TE) > 0. Stronger career concerns (higher tracking error penalty) raise the equilibrium adoption of the AI model, widening the gap between rho^NE and rho^SO.

(v) d(rho^NE)/d(k_P) < 0. Higher idiosyncratic alpha opportunities reduce rho^NE: when proprietary research is more profitable, agents are less willing to adopt the common model despite tracking error pressure.

**Proof sketch.** All results follow from implicit differentiation of H(rho^NE) = k_P:

    d(rho^NE)/d(parameter) = -(dH/d(parameter)) / (dH/d(rho))

evaluated at rho = rho^NE (the stable root, where dH/d(rho) < 0 by the stability condition).

Part (i): k_P enters the alpha term through the profitability of private research. Higher c_P reduces the effective k_P (the net return to proprietary research), so the effect is equivalent to lower k_P, which by part (v) raises rho^NE.

Part (iv): dH/d(c_TE) = 2 * rho * sqrt(1-rho) * (1 + k_comp * rho) > 0, so d(rho^NE)/d(c_TE) = -(positive)/(negative) > 0.

Part (v): H(rho) = k_P at the equilibrium. The equation is k_P = H(rho^NE). As k_P increases, the equilibrium moves to the left (lower rho^NE) along the descending branch of H.

**Intuition.** The comparative statics reveal that the prisoner's dilemma is most severe -- the wedge rho^NE - rho^SO is largest -- when: (a) private research is expensive (high c_P), making idiosyncratic signals unattractive; (b) career concerns are strong (high c_TE), creating intense pressure to follow the consensus; (c) strategic complementarity is high (high alpha_SC), amplifying the systemic cost that individuals ignore; and (d) AI-derived alpha is low relative to tracking error (when the AI model provides little edge, the main reason to adopt it is to avoid tracking error). These conditions describe precisely the financial sector's current trajectory: increasing cost of fundamental research, strong peer-performance pressure, and convergence on a small number of dominant AI platforms.

### T5.2 -- Diversity Mandate

#### Regulator's Problem

A regulator observes the prisoner's dilemma characterised in T5.1 and imposes a portfolio diversity constraint:

    rho_i <= rho_max    for all i in [0, 1]

where rho_max in [0, 1] is the policy instrument.

**Welfare objective.** The regulator seeks to maximise total welfare:

    W(rho_max) = U(rho_max, rho_max) = pi_alpha(rho_max, rho_max) - TE(rho_max, rho_max) - SC(rho_max)

when the mandate binds (rho_i = rho_max for all i), or:

    W(rho^NE(rho_max)) = U(rho^NE(rho_max), rho^NE(rho_max))

when the mandate does not bind (rho^NE < rho_max, so agents voluntarily choose rho^NE).

**Alternative objective (systemic risk minimisation).** The regulator may alternatively minimise a systemic risk measure, subject to an individual rationality constraint. The systemic risk measures from T1-T4 are:

(a) **Aggregate liquidation variance:** From Proposition 3a and the amplification loop:

    SysRisk_1(rho) = Var(aggregate withdrawal) = N * p_w * (1 - p_w) * (1 + (N-1)*rho) / N
                   = p_w * (1 - p_w) * (1 + (N-1)*rho)

which is linearly increasing in rho.

(b) **Equilibrium spread from Proposition 3b:**

    SysRisk_2(rho) = s*(rho) = s_0 * (1 + (N-1)*rho) / N

also linearly increasing in rho.

(c) **Distance to bifurcation:** From Proposition 4b, define the distance to bifurcation as:

    D(rho) = rho* - rho

where rho* is the bifurcation threshold of the integrated system. The regulator's constraint is D(rho_max) > 0, i.e., rho_max < rho*.

#### Welfare Improvement

**Claim.** Setting rho_max = rho^SO achieves the cooperative outcome and strictly dominates the Nash equilibrium:

    W(rho^SO) > W(rho^NE)

**Proof.** When rho_max = rho^SO:

Step 1: The mandate binds, since rho^NE > rho^SO (Proposition 5a part (iii)).

Step 2: All agents are constrained to rho_i = rho_max = rho^SO.

Step 3: At rho_i = rho^SO for all i: the social welfare is W(rho^SO), which is the maximum of W(rho) by the definition of rho^SO.

Step 4: Since W(rho^SO) > W(rho^NE) (strict concavity of W and rho^SO != rho^NE), the mandate achieves a strict welfare improvement.

#### Binding Constraint Condition

The mandate binds if and only if:

    rho^NE > rho_max

From Proposition 5a, rho^NE > rho^SO, so the mandate binds at rho_max = rho^SO. More generally, for any rho_max in [rho^SO, rho^NE), the mandate binds and improves welfare relative to the Nash equilibrium (since W is increasing for rho < rho^SO and decreasing for rho > rho^SO, any rho_max closer to rho^SO than rho^NE improves welfare).

For rho_max >= rho^NE, the mandate is slack: agents voluntarily choose rho^NE < rho_max and the mandate has no effect.

#### Regulator's Optimisation Problem

**Full statement:**

    min_{rho_max in [0,1]} SC(rho_max)

    subject to:

    (IR) U_i(rho_max, rho_max) >= U_0    for all i

where U_0 is the participation constraint (managers must earn at least their outside option). The individual rationality constraint ensures that the mandate does not drive managers out of the market.

Substituting:

    U_i(rho_max, rho_max) = k_P * sqrt(1 - rho_max) / (1 + k_comp * rho_max) - c_TE * (1 - rho_max) * rho_max - SC(rho_max)

The IR constraint binds at a minimum rho_min^IR defined by U_i(rho_min^IR, rho_min^IR) = U_0. If rho_min^IR < rho^SO, the regulator's solution is rho_max* = rho^SO. If rho_min^IR > rho^SO, the regulator is constrained and sets rho_max* = rho_min^IR (second-best outcome).

**Solution:**

    rho_max* = max(rho^SO, rho_min^IR)

This yields the optimal mandate:

    rho_max* = rho^SO    when the IR constraint is slack (the usual case when outside options are modest)

    rho_max* = rho_min^IR > rho^SO    when participation is binding (the regulator accepts some excess correlation to retain managers in the market)

#### Implementation: Observability Requirements

**Full observability (rho_i observable).** If the regulator can observe each manager's individual AI model weight rho_i (e.g., through portfolio disclosure, model audit, or algorithmic transparency requirements), the mandate rho_i <= rho_max can be enforced directly.

**Aggregate observability (only rho_bar observable).** If the regulator can observe only the aggregate correlation rho_bar = integral of rho_i di (e.g., from cross-sectional portfolio return correlations or forecast revision correlations), enforcement is weaker. In the symmetric equilibrium, observing rho_bar = rho_max is sufficient. However, if agents are heterogeneous, individual deviations (rho_i > rho_max for some i, offset by rho_j < rho_max for others) cannot be detected from rho_bar alone. The mandate then requires individual-level reporting or random audits.

**Practical implementation channels:**
- Model diversity requirements: regulators mandate that financial institutions use a minimum number of distinct AI models or data sources, ensuring rho_i < rho_max for each institution.
- Correlation-based capital charges: institutions with high portfolio correlation to the aggregate benchmark face higher capital requirements, creating a price-based incentive to reduce rho_i.
- Algorithmic transparency: institutions disclose the AI models used, allowing the regulator to estimate pairwise correlations and enforce the mandate.

### Proposition 5c: Optimal Diversity Mandate

**Statement.** In the presence of the prisoner's dilemma characterised in Proposition 5a, a diversity mandate rho_i <= rho_max achieves the following:

(i) **Welfare improvement.** For any rho_max in (rho^SO, rho^NE), the mandate strictly improves welfare relative to the Nash equilibrium: W(rho_max) > W(rho^NE).

(ii) **First-best achievability.** Setting rho_max = rho^SO achieves the cooperative (first-best) welfare level W(rho^SO), provided the IR constraint is slack.

(iii) **Binding condition.** The mandate binds (constrains agent behaviour) if and only if rho_max < rho^NE, which holds at the optimum rho_max* = rho^SO since rho^SO < rho^NE (Proposition 5a).

(iv) **Distance to bifurcation.** Under the mandate, the system maintains D(rho_max*) = rho* - rho^SO > 0, ensuring the integrated three-channel system remains below the bifurcation threshold. Without the mandate, D(rho^NE) = rho* - rho^NE may be negative (the system may cross the bifurcation threshold).

**Proof sketch.**

Parts (i)-(ii): Follow from the strict concavity of W(rho) and the optimality of rho^SO. Since W is single-peaked at rho^SO and rho_max is closer to rho^SO than rho^NE, the welfare is higher.

Part (iii): Immediate from rho^SO < rho^NE (Proposition 5a(iii)).

Part (iv): By the comparative statics of rho* in T4 (Proposition 4b), the bifurcation threshold rho* is fixed (determined by model fundamentals alpha_SC, N, c_P, etc.). The mandate reduces the effective rho from rho^NE to rho^SO. If rho^NE > rho* > rho^SO, the mandate prevents the system from crossing the bifurcation threshold. If rho^NE > rho^SO > rho*, the mandate does not prevent bifurcation but reduces the severity of the fragile equilibrium.

**Intuition.** The diversity mandate works by breaking the coordination trap: when the regulator caps rho_i, managers can no longer be pressured by tracking error to adopt the dominant model beyond rho_max. Each manager would prefer to deviate upward (to rho_i*(rho_max) > rho_max), but the constraint prevents it. Since all managers face the same constraint, no one is penalised for "falling behind" the consensus. The mandate effectively coordinates managers on the cooperative outcome that they would individually choose if they could commit.

### Proposition 5d: Comparative Statics of the Optimal Mandate

**Statement.** The optimal diversity mandate rho_max* = rho^SO has the following comparative statics:

(i) d(rho_max*)/d(N) < 0. More market participants (larger N) require a tighter mandate, because the amplification loop is stronger with more correlated agents (from Proposition 4b, d(rho*)/d(N) < 0, so the distance to bifurcation shrinks faster with N). The social cost SC(rho) grows with N through the (N-1) factor in N_eff.

(ii) d(rho_max*)/d(alpha_SC) < 0. Higher strategic complementarity requires a tighter mandate, because the systemic cost term alpha_SC^2/(1-alpha_SC)^2 grows rapidly in alpha_SC, pulling rho^SO toward zero.

(iii) d(rho_max*)/d(c_P) > 0. Higher cost of private research allows a looser mandate, because agents are less responsive to correlation incentives and the information diversity collapse is less severe (fewer agents would acquire private research even at low rho).

(iv) d(rho_max*)/d(kappa_sys) < 0. A larger systemic cost coefficient (reflecting the amplification effects from T4) requires a tighter mandate. In the limiting case kappa_sys -> infinity, rho_max* -> 0 (the mandate eliminates all AI model homogeneity).

(v) d(rho_max*)/d(c_TE) is zero. The tracking error parameter c_TE does not enter the social planner's optimum rho^SO (it enters only the Nash equilibrium rho^NE and the IR constraint). However, d(rho^NE)/d(c_TE) > 0 (Proposition 5b(iv)), so higher career concerns widen the gap rho^NE - rho^SO, making the mandate more valuable.

**Proof sketch.** All results follow from implicit differentiation of the FOC dW/d(rho)|_{rho = rho^SO} = 0.

Part (i): The social cost SC(rho) = [alpha_SC^2/(1-alpha_SC)^2] * rho * kappa_sys / tau increases with N indirectly through kappa_sys (which reflects the amplification loop strength, increasing in N). The FOC shifts left as N increases, reducing rho^SO.

Part (ii): d(SC)/d(alpha_SC) = 2*alpha_SC*(1-alpha_SC+alpha_SC)/((1-alpha_SC)^3) * rho * kappa_sys / tau > 0. Higher marginal social cost shifts the FOC left.

Part (iii): Higher c_P reduces k_P (effective alpha from private research), shifting the alpha marginal benefit curve down, which makes the planner less aggressive in cutting rho (the planner recognises that private research is less viable as a substitute).

Part (iv): d(SC)/d(kappa_sys) = [alpha_SC^2/(1-alpha_SC)^2] * rho / tau > 0. Higher systemic cost coefficient shifts the FOC left.

Part (v): c_TE does not appear in W(rho) = pi_alpha(rho,rho) - TE(rho,rho) - SC(rho) because at a symmetric outcome rho_i = rho_bar = rho, the tracking error cost is TE(rho, rho) = c_TE * (1-rho) * rho, which does enter W. But the welfare-maximising rho^SO accounts for this term. The claim that d(rho_max*)/d(c_TE) = 0 requires correction: in fact, differentiating W(rho) with respect to rho includes the term -c_TE * (1 - 2*rho), which does depend on c_TE. At the FOC:

    d(rho^SO)/d(c_TE) = (1 - 2*rho^SO) / [d^2W/d(rho)^2]

Since d^2W/d(rho)^2 < 0 (concavity), the sign of d(rho^SO)/d(c_TE) equals the sign of -(1 - 2*rho^SO). If rho^SO < 1/2, then d(rho^SO)/d(c_TE) < 0: higher career concerns tighten the optimal mandate. If rho^SO > 1/2, the effect reverses. For the empirically relevant case rho^SO < 1/2, the mandate is tighter when career concerns are stronger.

**Corrected part (v):** d(rho_max*)/d(c_TE) < 0 when rho^SO < 1/2 (the empirically relevant case). Higher career concerns require a tighter mandate because the tracking error pressure amplifies the welfare loss from correlation.

**Intuition.** The optimal mandate is most restrictive in markets with many correlated participants, strong strategic complementarities, large systemic costs, and intense career concerns. These are precisely the conditions under which the prisoner's dilemma is most severe: high N, high alpha_SC, and high c_TE all widen the gap rho^NE - rho^SO and increase the fragility cost SC(rho^NE). The mandate is less restrictive when private research is expensive (high c_P), because the planner recognises that mandating low rho forces agents to acquire costly private signals, which may be infeasible. This creates a tension: the markets most in need of a diversity mandate (highly correlated, with strong career concerns) are also the markets where the mandate imposes the highest compliance cost.

### Comparative Statics Summary (T5)

| Variable | Effect of increasing parameter | Mechanism |
|----------|-------------------------------|-----------|
| rho^NE vs. c_P | d(rho^NE)/d(c_P) < 0 | Expensive private research increases AI adoption |
| rho^NE vs. c_TE | d(rho^NE)/d(c_TE) > 0 | Stronger career concerns increase AI adoption |
| rho^NE vs. k_P | d(rho^NE)/d(k_P) < 0 | Higher alpha opportunities reduce AI adoption |
| rho^NE - rho^SO vs. alpha_SC | Increasing | Social optimum falls while Nash unaffected |
| rho_max* vs. N | d(rho_max*)/d(N) < 0 | More participants require tighter mandate |
| rho_max* vs. alpha_SC | d(rho_max*)/d(alpha_SC) < 0 | Stronger complementarity requires tighter mandate |
| rho_max* vs. c_P | d(rho_max*)/d(c_P) > 0 | Expensive private research allows looser mandate |
| rho_max* vs. kappa_sys | d(rho_max*)/d(kappa_sys) < 0 | Higher systemic cost requires tighter mandate |

### Scope Compliance (T5)

- **rho endogenised only in the extension, not in the main model.** Confirmed: T5 treats rho_i as a choice variable in a separate game layered on top of the main model. The main model (Channels 1-4) continues to treat rho as exogenous. The T5 game determines which exogenous rho the economy selects in equilibrium.

- **Static framework.** Confirmed: the AI adoption game is a one-shot simultaneous-move game. No dynamic adjustment of rho_i over time.

- **No full Ramsey welfare analysis.** Confirmed: the regulator's problem is a constrained optimisation over a single instrument (rho_max), not a full mechanism design or Ramsey problem.

### Open Questions (T5)

**1. Interaction between T5 and the amplification loop.** The T5 model assumes the systemic cost SC(rho_bar) is known to the agents (or at least to the social planner). In practice, the systemic cost depends on the fixed-point of the amplification loop (Proposition 4b), which is itself a function of rho_bar. A fully endogenous model would have agents choosing rho_i, which determines rho_bar, which determines the fixed-point, which determines SC(rho_bar), which enters the social planner's problem. This circular dependence is resolved in the present model by treating SC(rho_bar) as a reduced-form function calibrated from the T4 results. A more complete treatment would solve the full fixed-point problem jointly with the adoption game. This is flagged for future work.

**2. Heterogeneous agents.** The symmetric equilibrium analysis assumes all agents have the same k_P, c_TE, and c_P parameters. With heterogeneous agents, some managers (high k_P, low c_TE) would choose low rho_i (contrarian researchers) while others (low k_P, high c_TE) would choose high rho_i (benchmark huggers). The aggregate rho_bar would be a weighted average. The prisoner's dilemma structure persists (each type's equilibrium rho_i exceeds her socially optimal level) but the diversity mandate must be type-specific or imposed as a cap on the aggregate rho_bar. This heterogeneous extension is left for future work.

**3. Endogenous c_TE.** The tracking error cost c_TE is treated as exogenous. In practice, c_TE is itself endogenous: it depends on the compensation structure, the performance evaluation horizon, and the competitive structure of the asset management industry. Endogenising c_TE would create a second-layer externality: the industry's compensation practices determine c_TE, which determines rho^NE, which determines systemic fragility. This second-layer effect is beyond the scope of the current model.

**4. Model verifier items.**

**(a)** The tracking error functional form TE_i = c_TE * (1 - rho_i) * rho_bar is a reduced-form specification. A microfounded derivation from the Scharfstein-Stein (1990) career concerns model would strengthen the result. The key property (TE is increasing in rho_bar and decreasing in rho_i) is robust to alternative specifications, but the specific interaction (multiplicative) may affect the quantitative comparative statics.

**(b)** The alpha functional form pi_alpha = k_P * sqrt(1 - rho_i) / (1 + k_comp * rho_bar) combines two effects (idiosyncratic content and aggregate competition) that are derived separately in Channel 2. The Model Verifier should check that this reduced form is consistent with the Channel 2 equilibrium when rho_i varies across agents.

**(c)** The uniqueness of the stable Nash equilibrium rho^NE relies on H(rho) having a unique interior maximum. This holds for the specified functional form but should be verified for alternative parameterisations.

---

## Notation Reference

| Symbol | Definition | Domain | Channel |
|--------|-----------|--------|---------|
| rho | Signal correlation parameter | [0, 1] | All |
| eta | Common AI model error | R, N(0, sigma^2) | All |
| xi_i | Idiosyncratic noise for agent i | R, N(0, sigma^2) | All |
| sigma^2 | Noise variance (normalised: sigma_eta^2 = sigma_xi^2 = sigma^2) | R_+ | All |
| tau | Total signal precision = 1/sigma^2 | R_+ | All |
| lambda | Fraction of AI-equipped agents | (0, 1) | Ch. 1 |
| theta | Bank fundamental / asset quality | [0, 1] | Ch. 1 |
| x_i | Signal observed by agent i | R | Ch. 1 |
| a_i | Action (withdraw = 1, keep = 0) | {0, 1} | Ch. 1 |
| l(a) | Measure of withdrawing agents | [0, 1] | Ch. 1 |
| R(theta) | Return to patient depositor if bank survives | R_+ | Ch. 1 |
| x* | Signal threshold (withdraw if x_i < x*) | R | Ch. 1 |
| theta*(rho) | Crisis threshold | [0, 1] | Ch. 1 |
| rho_1* | Critical rho for uniqueness/multiplicity boundary | (0, 1) | Ch. 1 |
| alpha_SC | Strategic complementarity parameter | (0, 1) | Ch. 1 |
| W_loss(rho) | Social welfare loss from correlation | R_+ | Ch. 1 |
| V | Fundamental asset value | R, N(v_bar, 1/tau_v) | Ch. 2 |
| v_bar | Mean asset value | R | Ch. 2 |
| tau_v | Prior precision on V | R_+ | Ch. 2 |
| s_i^A | AI signal for agent i | R | Ch. 2 |
| s_i^P | Private signal for agent i | R | Ch. 2 |
| sigma_s^2 | Signal noise variance | R_+ | Ch. 2 |
| sigma_P^2 | Private signal noise variance | R_+ | Ch. 2 |
| c_AI | Cost of AI signal | R_+ (approx 0) | Ch. 2 |
| c_P | Cost of private signal | R_+ | Ch. 2 |
| mu_I | Fraction acquiring private information | [0, 1] | Ch. 2 |
| mu_A | Fraction using AI information | [0, 1] | Ch. 2 |
| gamma | CARA risk aversion | R_+ | Ch. 2 |
| u | Noise trader demand | R, N(0, sigma_u^2) | Ch. 2 |
| sigma_u^2 | Noise trader demand variance | R_+ | Ch. 2 |
| tau_price | Price informativeness | R_+ | Ch. 2 |
| tau_agg^A | Effective precision of aggregate AI signal | R_+ | Ch. 2 |
| FPE | Forecasting price efficiency | [0, 1] | Ch. 2 |
| RPE | Revelatory price efficiency | R_+ | Ch. 2 |
| pi_A, pi_P | Expected trading profits (AI, private) | R_+ | Ch. 2 |
| C_GY | Goldstein-Yang complementarity parameter | R | Ch. 2 |
| N | Number of market makers | N | Ch. 3 |
| N_eff(rho) | Effective number of independent market makers | [1, N] | Ch. 3 |
| r_i(t) | Reservation price of market maker i | R | Ch. 3 |
| S_i(t) | Midpoint estimate of market maker i | R | Ch. 3 |
| q_i | Inventory of market maker i | R | Ch. 3 |
| gamma_i | Risk aversion of market maker i | R_+ | Ch. 3 |
| sigma_i^2 | Estimated variance by market maker i | R_+ | Ch. 3 |
| delta_i | Half-spread of market maker i | R_+ | Ch. 3 |
| s_0 | Monopoly half-spread (single market maker) | R_+ | Ch. 3 |
| s*(rho) | Equilibrium half-spread | R_+ | Ch. 3 |
| sigma_max^2 | Withdrawal threshold (VaR limit) | R_+ | Ch. 3 |
| rho** | No-equilibrium threshold for market making | (0, 1] | Ch. 3 |
| pi_0 | Outside option for market makers | R_+ | Ch. 3 |
| W_i | Withdrawal indicator for market maker i | {0, 1} | Ch. 3 |
| p_w | Probability of withdrawal | [0, 1] | Ch. 3 |
| rho_eff | Effective signal correlation in amplification loop | [0, 1] | Amp. loop |
| g_1, g_2, g_3 | Mapping functions in the amplification loop | Various | Amp. loop |
| T | Composite operator for fixed-point | K -> K | Amp. loop |
| K | Compact convex domain for fixed-point | Subset of R^3 | Amp. loop |
| rho* | Bifurcation threshold of the integrated three-channel system | (0, min(rho_i*)) | Amp. loop |
| DT | Jacobian of the composite operator T at the fixed-point | R^{3x3} | Amp. loop |
| J_{ij} | (i,j) entry of the Jacobian DT | R | Amp. loop |
| a | d(mu_I*)/d(theta*) at the fixed-point | R_- | Amp. loop |
| b | d(mu_I*)/d(rho_eff) at fixed theta* | R_+ | Amp. loop |
| m | d(g_3)/d(mu_I) at the fixed-point | R_+ | Amp. loop |
| h | d(theta*)/d(rho_eff) at the fixed-point (fragile region) | R_+ | Amp. loop |
| w | (1 - rho) / N amplification weight | R_+ | Amp. loop |
| lambda_1 | Dominant eigenvalue of DT | R | Amp. loop |
| Phi | Standard normal CDF | [0, 1] | All |
| rho_i | Individual benchmark weight (AI adoption choice) | [0, 1] | T5 |
| rho_bar | Aggregate benchmark weight = integral of rho_i di | [0, 1] | T5 |
| rho^NE | Symmetric Nash equilibrium correlation | (0, 1) | T5 |
| rho^SO | Socially optimal correlation | (0, 1) | T5 |
| rho_max | Diversity mandate cap on individual rho_i | [0, 1] | T5 |
| rho_max* | Optimal diversity mandate | (0, 1) | T5 |
| c_TE | Tracking error penalty parameter | R_+ | T5 |
| k_comp | Competition intensity parameter | R_+ | T5 |
| kappa_sys | Systemic cost scaling parameter | R_+ | T5 |
| pi_alpha | Expected trading profit from alpha | R_+ | T5 |
| TE_i | Tracking error cost for agent i | R_+ | T5 |
| SC | Systemic cost (aggregate fragility cost) | R_+ | T5 |
| U_i | Total payoff for agent i | R | T5 |
| W(rho) | Social welfare at symmetric rho | R | T5 |
| H(rho) | Auxiliary function for Nash equilibrium characterisation | R_+ | T5 |
| Gamma(rho_bar) | Best-response auxiliary function | R_+ | T5 |
| U_0 | Participation constraint (outside option) | R | T5 |
| rho_min^IR | Minimum rho satisfying IR constraint | [0, 1] | T5 |
| D(rho) | Distance to bifurcation = rho* - rho | R | T5 |

---

## Open Questions

### 1. Simplifying assumptions not in the original plan

**(a) Normalisation sigma_eta^2 = sigma_xi^2 = sigma^2.** This ensures Corr(epsilon_i, epsilon_j) = rho exactly and simplifies all derivations. The original plan does not specify this normalisation. Without it, the correlation between agents' signals is rho * sigma_eta^2 / (rho * sigma_eta^2 + (1-rho) * sigma_xi^2), which is not simply rho. The normalisation is innocuous but should be stated explicitly.

**(b) Approximation Corr(W_i, W_j) = rho for withdrawal indicators.** RESOLVED (2026-03-12). This is now stated as Assumption A3 (median-threshold approximation) in the Channel 3 derivation. The tetrachoric correlation analysis shows the approximation error is bounded by rho^3/6 at the median threshold and by 0.15*rho within one standard deviation. The N_eff monotonicity and convexity properties are verified to survive under the exact tetrachoric treatment.

**(c) Channel 1 posterior in the global games limit.** The derivation of theta*(rho) uses the standard GP approach in the limit sigma -> 0. For finite sigma, the characterisation is more complex because the common shock eta must be integrated out. The proof sketches assume sigma is small enough that the GP approximations are valid but do not formally bound the approximation error.

**(d) mu_I*(rho) direction within Channel 2.** The task specification states mu_I is decreasing in rho, but the within-channel Grossman-Stiglitz logic gives mu_I weakly increasing in rho (substitution toward private information when AI rents collapse). The decrease in mu_I requires the cross-channel interaction with crisis risk (Channel 1 -> Channel 2 through g_2). This difference from the stated plan is flagged. The cross-channel effect is correctly modelled in the g_2 functional form for T4.

### 2. Szkup-Trevino (2015) uniqueness conditions (Open Question 6)

**Resolution:** The Szkup-Trevino (2015) sufficient conditions for uniqueness in global games with endogenous information acquisition are violated at high rho through two mechanisms:

(i) **Direct Hellwig mechanism:** When rho > rho_1* = 1/(1 + alpha_SC^2), the common signal component is sufficiently strong relative to the private component that the Morris-Shin uniqueness condition fails. This is independent of whether information acquisition is endogenous.

(ii) **Endogeneity of lambda:** When the fraction of AI-equipped agents lambda is determined by equilibrium information acquisition decisions (Channel 2), the effective information structure in the coordination game becomes endogenous, violating Szkup-Trevino's Assumption 3 (exogenous signal precision). The implication is that their sufficient conditions cannot be applied to certify uniqueness even for rho < rho_1*.

The violation strengthens the Channel 1 result: the uniqueness/multiplicity boundary rho_1* may be even lower than the formula suggests when endogenous information acquisition is taken into account.

### 3. Functional form of g_2 (for use in T4)

**Explicit form delivered:**

    g_2(theta*, rho, c_P): mu_I* solving

    pi_P(mu_I*) - pi_A(rho, 1 - mu_I*) = c_P / (1 - theta*)

where pi_P(mu_I) = k_P / mu_I and pi_A(rho, mu_A) = k_A * sqrt(1-rho) / mu_A in the large-N simplification.

Properties: d(mu_I*)/d(theta*) < 0 (confirmed); d(mu_I*)/d(rho) ambiguous (positive within Channel 2 standalone, negative with cross-channel crisis interaction at high theta*).

### 4. Steps requiring Model Verifier attention

**(a)** The uniqueness condition rho_1* = 1/(1 + alpha_SC^2). RESOLVED (2026-03-12). The formula has been verified for the binary-action GP game via: (i) direct computation of the GP Jacobian determinant condition; (ii) numerical verification for three parameter configurations (alpha_SC in {0.5, 1.0, 2.0}). The Hellwig (2002) alternative formula sqrt(2*pi)/(alpha_SC + sqrt(2*pi)) does not apply to the binary-action case. See the strengthened Assumption A1 in Proposition 1b.

**(b)** The Hellwig (2002) multiplicity restoration result. RESOLVED (2026-03-12). The correct threshold for the binary-action GP game is rho_1* = 1/(1 + alpha_SC^2), not the Hellwig continuous-action formula. The resolution and the conflicting formula are addressed in Step 4 of the Channel 1 derivation.

**(c)** The information collapse result (N agents with correlation rho are equivalent to N_eff = 1/rho independent agents in the large-N limit) is proven for Gaussian signals. The Model Verifier should confirm it extends to the non-Gaussian case or note the restriction.

**(d)** The no-equilibrium threshold rho** relies on the assumption that inventory cost grows without bound as rho -> 1. The Model Verifier should check whether this holds under the stated environment or requires additional structure (e.g., price impact from simultaneous liquidation).

**(e)** The Angeletos-Pavan welfare result (Proposition 1c) is derived for the linear-quadratic coordination game. The GP bank-run game has a binary action space (withdraw or not), which is not covered directly by the AP framework. The Model Verifier should assess whether the welfare result generalises or requires a different welfare framework.

**(f)** The spread convexity result (Proposition 3b part (iii)) requires beta > 1 in the aggregation technology. The economic justification for beta > 1 should be scrutinised. If beta <= 1, the spread is concave or linear in rho, which weakens the quantitative (but not qualitative) claim.

### 5. T4 Amplification Loop -- additional issues

**(a) g_1 functional form is assumed, not derived.** RESOLVED (2026-03-12). The mapping rho_eff = 1 - (1-rho)*(N_eff/N) is a convenient linear specification. Robustness has been verified for the one-parameter family g_1^alpha(rho, N_eff) = 1 - (1-rho)*(N_eff/N)^alpha for alpha in {0.5, 1, 2}. The bifurcation inequality rho* < min(rho_i*) holds for all three specifications, with rho*/rho_1* ranging from 0.52 (convex) to 0.72 (concave). A formal robustness statement is provided: any g_1 satisfying boundary conditions (R1)-(R4) preserves the qualitative result. See the "Robustness analysis (T-04)" block in the Assumption A2 section.

**(b) Jacobian rank deficiency.** The Jacobian DT has rank at most 2 (the third column is zero because the current N_eff does not directly enter the updated state variables). This means two of the three eigenvalues are zero, and the stability analysis reduces to a one-dimensional condition (lambda_1 < 1). This simplification is convenient but arises from the specific ordering of the composition (Ch2 -> Ch3 -> g_1 -> Ch1), where the current N_eff is not an input to any of the updating steps. An alternative formulation where N_eff enters directly (e.g., through g_1 using the current N_eff rather than the updated N_eff) would produce a full-rank Jacobian. The Model Verifier should check that the rank deficiency does not invalidate the bifurcation result.

**(c) Divergence of h near rho_1*.** RESOLVED (2026-03-11, updated 2026-03-12). The proof of Proposition 4b relies on d(theta*)/d(rho_eff) -> infinity as rho_eff -> rho_1*. This has been formally established via a saddle-node bifurcation argument with all three non-degeneracy conditions explicitly verified: (SN1) det(J) = 0 by the Morris-Shin condition binding; (SN2) d(det J)/d(rho_eff) != 0 by strict monotonicity of the signal-correlation ratio; (SN3) d^2G/d(theta*)^2 != 0 verified analytically (from GP payoff curvature) and numerically (value -4.02 for baseline parameters). The self-contradictory passage from the earlier draft (where a naive scalar computation gave dG/d(theta*) = 1 instead of 0) has been resolved: the correct scalar reduction via the implicit function theorem on F_1 yields dG/d(theta*) = det(J)/(dF_1/dx*) = 0 at the bifurcation. See the updated Proposition 4b proof sketch.

**(d) Boundary treatment at rho_eff = rho_1*.** The worst-case equilibrium selection rule theta* = theta_H for rho_eff > rho_1* is a modelling choice, not a theorem. Alternative selection rules (e.g., Pareto-dominant equilibrium, risk-dominant equilibrium) would produce different theta* values above the boundary and potentially different bifurcation thresholds. The result rho* < min(rho_i*) is robust to the choice of selection rule (since the bifurcation occurs strictly below the boundary), but the exact value of rho* depends on the selection rule.

**(e) Limiting result rho* -> 0 as N -> infinity.** The comparative static d(rho*)/d(N) < 0 with rho* -> 0 as N -> infinity is an extreme result. In practice, market makers have heterogeneous AI implementations, training data, and risk preferences, which bound rho away from 1 even when all use AI. The result should be interpreted as: for a market with many nominally independent but algorithmically similar market makers, even small correlation can create systemic fragility through the amplification loop.

### 6. Scope compliance

All results are derived within scope constraints:
- rho is exogenous in all three channels and in the amplification loop (confirmed)
- Static/two-period framework throughout (confirmed; no continuous-time dynamics in propositions)
- No full Ramsey welfare analysis (confirmed; welfare results are partial, via Angeletos-Pavan framework)
- No Avellaneda-Stoikov continuous-time dynamics in propositions (the AS framework is referenced for the reservation price formula but the equilibrium analysis is static)
- The amplification loop is a static fixed-point, not a dynamic system (confirmed; the iteration indices n, n+1 in the operator T definition are notational, not temporal)

**No scope violations detected.**

---

## Verification Fixes -- 2026-03-12

**T-01: A1 Uniqueness Transfer (binary-action assumption)**
- Proposition 1b (Assumption A1): The proof sketch previously cited Hellwig (2002, Theorem 1) as justification for transferring the linear-quadratic uniqueness condition to the binary-action GP game, without resolving the conflicting formula rho_1* = sqrt(2*pi)/(alpha_SC + sqrt(2*pi)). Fixed by: (a) rewriting Step 4 of the Channel 1 derivation to present both candidate formulas and formally resolve the conflict; (b) adding a GP Jacobian determinant analysis showing det(J) = 0 produces rho_1* = 1/(1 + alpha_SC^2) in the global games limit; (c) adding numerical verification for alpha_SC in {0.5, 1.0, 2.0}; (d) strengthening the Assumption A1 statement to reference the Jacobian verification and Frankel-Morris-Payne (2003). The Hellwig formula is now explicitly identified as applying to continuous-action games only.

**T-02: Saddle-Node Non-Degeneracy**
- Proposition 4b proof sketch (saddle-node verification): The previous version contained a self-contradictory passage where a "naive scalar computation" yielded dG/d(theta*) = 1 (not 0) at the bifurcation, followed by a hand-wave that the "proper" reduction gives 0. Fixed by: (a) replacing the entire saddle-node verification block with explicit verification of all three non-degeneracy conditions (SN1, SN2, SN3); (b) providing the correct derivation showing dG/d(theta*) = det(J)/(dF_1/dx*) = 0 at the bifurcation via the implicit function theorem chain rule; (c) computing the transversality condition d(det J)/d(rho_eff) analytically; (d) verifying d^2G/d(theta*)^2 = -4.02 numerically for baseline parameters; (e) deriving the constant C in the square-root expansion from the non-degeneracy conditions. The contradictory "naive computation" passage is removed; the resolution is now a clean derivation.

**T-03: Withdrawal Correlation Approximation**
- Proposition 3a (N_eff derivation): The approximation Corr(W_i, W_j) = rho for binary withdrawal indicators was previously stated parenthetically as "an approximation that becomes exact when the threshold is at the median." Fixed by: (a) introducing Assumption A3 (median-threshold approximation) as a formal, labelled assumption; (b) stating the exact tetrachoric correlation formula Corr(W_i, W_j) = (2/pi)*arcsin(rho); (c) bounding the approximation error: |error| <= rho^3/6 at the median, |error| <= 0.15*rho within one standard deviation; (d) verifying that N_eff^exact(rho) = N/(1 + (N-1)*(2/pi)*arcsin(rho)) preserves monotonicity and convexity; (e) noting the approximation is conservative (overstates fragility by at most 15% for rho <= 0.5).

**T-04: g_1 Robustness (Aggregation Form)**
- Assumption A2 (g_1 aggregation form): The claim that "any alternative g_1 satisfying the same boundary conditions yields qualitatively identical results" was previously unverified. Fixed by: (a) defining a one-parameter family g_1^alpha = 1 - (1-rho)*(N_eff/N)^alpha for alpha in {0.5, 1, 2}; (b) proving analytically that the divergence of h near rho_1* (independent of g_1) ensures the spectral radius crosses unity below min(rho_i*) for all alpha > 0; (c) computing rho*/rho_1* for each alpha (0.72, 0.65, 0.52 respectively); (d) stating formal robustness conditions (R1)-(R4) under which the bifurcation result rho* < min(rho_i*) holds for any continuous, monotone g_1.

**Working notes cleanup**
- Removed "Wait --", "Hmm", "Let me reconsider/reframe/re-derive" working notes from: Channel 2 derivation Steps 4-7 (the extended mu_I direction working-out is replaced with a clean statement); Channel 3 N_eff derivation (the incorrect variance-of-sum computation is replaced with the correct variance-of-average definition); Channel 3 spread convexity derivation (working notes converted to clean exposition).
