# Sharp threshold within the nonlinear vorticity weight method

## 1. Statement, scope and dependencies

Let 0 < c < 2/3 and omega be any real number. A profile here means U in C^2(R^3;R^3), P in C^1(R^3), div U = 0, satisfying

    (cy + U - omega J y).grad U = (c - 1)U - omega J U - grad P,
    J y = e_3 cross y.

Assume Hb: U is bounded and U(R .) tends to zero in distributions as R tends to infinity. Uniform decay suffices. Write W = curl U. The independently confirmed Lemma NW (A1584) says that U = 0 if sup |W| <= M and there are a > 0 and g in C^1([0,M^2]) with g(0) = 0, g' >= 0, and

    H[g,a] = 2tg' - 3cg - at/2 - 2t^2(g')^2/(3a) > 0,  0 < t <= M^2.

Its input energy boundary error tends to zero under Hb and c < 2/3; no integrability of W or decay of DU is assumed. Rotation cancels in that argument for every omega. This review uses that established lemma and proves its exact strict threshold and rational brackets. The ODE decimal approximations in the submission are not evidence used here.

Set x_h = t/3 + 2ch and

    F_c(t,h) = (3/(2t))(1 - sqrt(1 - x_h)),   t > 0, x_h < 1.

There is a unique C^1 solution h_c with h_c(0) = 0 of h_c' = F_c(t,h_c), until its first barrier time t_c in (0,3). It extends C^1 to t_c and x_h(t_c) = 1. Define T(c) = sqrt(t_c). Then sup |W| < T(c) implies U = 0. The supremum of the M admitted by strict Lemma NW is exactly T(c), and is not attained by a strict admissible weight. T is nonincreasing in c.

## 2. Singular comparison and existence

Put nu = 3c/2 in (0,1). If h,k are C^1 at zero, both vanish there, both graphs satisfy x < 1 on (0,tau), and

    h' - F_c(t,h) >= k' - F_c(t,k),

then h >= k. Indeed D = h-k is O(t), and the fundamental theorem of calculus in the h variable gives

    F_c(t,h)-F_c(t,k) = m(t)D/t,
    m(t) = nu integral_0^1 (1 - t/3 - 2c(k + theta D))^(-1/2) dtheta.

Here m is continuous away from zero and m(t) = nu + O(t) at zero. If D(t0) < 0, integration of D' - mD/t >= 0 backwards from t0 yields -D(t) >= C t^nu for small positive t, with C > 0. This contradicts D = O(t), since nu < 1. Endpoint comparison follows by continuity. No comparison across an unentered square-root domain is used.

For existence put h = tu, kappa = 1-nu, u0 = 1/(4kappa). Rationalizing the square root gives a smooth function

    F_c(t,tu) = Psi(t,u) = (3/2)(1/3+2cu)/(1+sqrt(1-t(1/3+2cu))).

At t = 0, Psi(0,u) = 1/4 + nu u. Write R(t,u) = Psi(t,u)-Psi(0,u); on a small rectangle about (0,u0), both |R| and its Lipschitz constant in u are bounded by Ct. The integral map

    u(t) = u0 + t^(-kappa) integral_0^t s^(kappa-1) R(s,u(s)) ds

maps the closed unit ball around the constant u0 in C([0,delta]) into itself and contracts when C delta/(1+kappa) < 1. Its fixed point gives h = tu in C^1, h'(0) = u0, and h' = F_c(t,h). Uniqueness follows from comparison in both directions.

The solution is positive and increasing, and x' >= 1/3. For a fixed small delta, h(t) >= h(delta) > 0 thereafter, so t < 3-6c h(delta) while x < 1. This gives the strict bound t_c < 3, filling the abbreviated strictness step in the source. Also 0 <= h' <= 3/(2delta) for t >= delta. Thus no blowup is possible before the barrier. Ordinary local continuation away from t = 0 implies x tends to 1 at the finite maximal endpoint. The formula for h' then gives h'(t_c) = 3/(2t_c), proving the C^1 extension.

## 3. Strict optimum and monotonicity

Direct completion of the square gives

    H[h,1] = -(2/3)t^2(h'-3/(2t))^2 + (3/2)(1-x_h),
    H[g,a] = a H[g/a,1].

In particular H > 0 forces x_h < 1 and h' > F_c(t,h). A strict admissible h = g/a therefore satisfies h >= h_c until the earlier endpoint. If M^2 >= t_c this gives x_h(t_c) >= 1, contradicting strict positivity there. Hence M < T(c).

Conversely, given 0 < M < T(c), set lambda = t_c/M^2 and g(t) = h_c(lambda t). This function is C^1 through the right endpoint, is increasing, and vanishes at zero. Direct substitution gives

    H[g,1](t) = H[h_c,1](lambda t) + (lambda-1)t/2 = (lambda-1)t/2 > 0.

It is therefore admissible. If sup |W| < T(c), choose such an M at least that supremum and apply Lemma NW.

For c < d < 2/3, F_d(t,h) >= F_c(t,h) when h >= 0 and both are defined. Before the first barrier of h_c considered in the d-domain, comparison at d gives h_d >= h_c. Thus the d-solution reaches its barrier no later. This proves t_d <= t_c and the asserted monotonicity. The first d-barrier of h_c occurs by t_c because its x-value increases when c is replaced by d.

## 4. Exact brackets and verification

The exact coefficients and interval endpoints are in the team records. They were extracted as literals from the submitted source, without executing that source. The independent program in the team records constructs the density polynomial and its Sturm chain over the rationals. For each lower row, H[g,1]/t and g' have zero Sturm root count on the open interval and strictly positive values at both endpoints. They are therefore positive on the entire closed interval. For each upper row, H[k,1]/t and tk'-3/2 are negative, and k/t is positive, by the same exact argument. The barrier excess x_k(tau)-1 is strictly positive, and U^2-tau is nonnegative, in every row.

For the upper argument let tau0 be the first zero of x_k-1. Before tau0, H[k,1] < 0 and tk' < 3/2 place k' below the lower quadratic root F_c(t,k). Comparison gives h_c >= k until the earlier endpoint, so t_c <= tau0 < tau. This proves strict T(c) < U. The verified brackets are:

| c | Lower M < T(c) | T(c) < upper U |
|---|---:|---:|
| 0.41 | 0.982 | 0.99127 |
| 0.42 | 0.960 | 0.96952 |
| 0.43 | 0.938 | 0.94744 |
| 0.44 | 0.916 | 0.92503 |
| 0.45 | 0.893 | 0.90226 |
| 0.46 | 0.870 | 0.87909 |
| 0.47 | 0.846 | 0.85550 |
| 0.48 | 0.822 | 0.83146 |
| 0.49 | 0.797 | 0.80693 |
| 0.50 | 0.772 | 0.78185 |

Each lower weight also works for every smaller positive c, since its g is nonnegative and partial_c H = -3g. Therefore sup |curl U| <= 0.772 suffices for every 0 < c <= 1/2 and every omega, under the exact profile and Hb hypotheses of Section 1. Equality at the displayed rational lower thresholds is included because their certificate is strictly positive throughout the positive interval. This is different from equality at the unknown exact optimum T(c).

The independent exact run passed all twenty rows and three negative controls. Its actual times were 2026-11-03T16:48:04.895156+00:00 to 2026-11-03T16:48:09.308554+00:00, elapsed 4.413396113086492 seconds, CPU affinity [55], nice 19 and one thread. Full endpoint fractions and sign variations are retained in the team records. No ODE numerical integration was run by this audit.

## 5. Repair of the nonnegative-density claim

Remark R2 as submitted infers that a nonnegative-density method fails from the existence of a point where H <= 0. That inference alone is invalid: equality is compatible with nonnegativity. Its conclusion is correct with the following stronger argument, and with the essential g(0) = 0 and C^1 hypotheses retained.

Suppose a > 0, g in C^1([0,L]), g(0) = 0 and H[g,a] >= 0 on (0,L]. No separate monotonicity assumption is needed for this obstruction. Let h = g/a. Completion of the square gives x_h <= 1 everywhere and h' >= F_c(t,h) wherever x_h < 1. If L > t_c and x_h remains below 1 through t_c, comparison gives x_h(t_c) >= 1, a contradiction. Consequently there is a first contact tau <= t_c. At any such contact, nonnegative H forces

    h'(tau) = 3/(2tau),
    x_h'(tau) = 1/3 + 3c/tau > 0.

Since tau < L, differentiability forces x_h > 1 immediately afterwards, also a contradiction. Thus L <= t_c. In particular when M > T(c), H must be strictly negative somewhere, not merely nonpositive. At that t the exact minimized density

    D = a |S - (g'/a)(W tensor W - t I/3)|^2 + H[g,a](t)

is strictly negative for a suitable trace-free symmetric S. No pointwise nonnegative density of this particular form can cover all |W| <= M. Without g(0) = 0, the assertion for an arbitrary g is false, for example a sufficiently negative constant g makes H positive on any fixed finite interval. Such a weight does not meet the transport argument's nonnegative-weight requirement.

## 6. Verdicts and remaining questions

The singular comparison, existence, exact strict optimum, monotonicity, twenty certified brackets and all-omega profile corollaries are CONFIRMED. The literal inferential step in Remark R2 needs the repair in Section 5. The repaired nonnegative obstruction is CONFIRMED within its specified scalar-weight and constant-a family.

No claim here rules out weights involving other variables, other identities, nonlocal combinations, the endpoint sup |W| = T(c), or profiles with larger vorticity. In particular bare decay alone has not been shown to imply the small-vorticity premise. The full nonexistence question remains OPEN.
