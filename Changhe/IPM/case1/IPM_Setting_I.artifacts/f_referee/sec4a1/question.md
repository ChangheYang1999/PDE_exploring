You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

# Audit of six analytic statements in a numerical report on a self-similar IPM profile

Setting. On R^2, with rho even in x and odd in y, solve W.grad rho = rho with W = c_l X + U, U = grad^perp psi =
(-psi_y, psi_x), -Delta psi = d_x rho (psi the canonical full-plane inverse, psi(0) = 0, grad psi(0) = 0, no added
harmonic polynomial), rho = x^2 y a, a(0) = 1, c_l = (1 + psi_xy(0))/3. So div W = 2 c_l. The source point is
P = (x*, 0), x* about 8.6, with W(P) = 0; there DW(P) = diag(A, h(P)), A = 2 c_l - 1 about 10.15, and an exact profile
has h(P) = d_y W_2(P) = 1. The class P_2: rho in C^(2,alpha)_loc for some alpha in (0, 1), rho = x^2 y a near 0 with a
continuous and a(0) = 1. R = W.grad rho - rho is the transport residual of a trial density (velocity computed from the
trial density itself by the canonical inverse).

Trial family. With u = r/L, q = 1 - (1 + u^2)^(-(1-k)/2), chi = u^2/(u^2 + r_0^2), r_0 = 0.02, k = 1/c_l = 0.17936,
p_3 = 6 + 2/(2 c_l - 1) = 6.19698, L = 7.6514,
   rho_h = x^2 y exp(H),
   H = ((k - 3)/2) log(1 + u^2) + sum_{m=0}^{150} chi^max(m-1,0) b_m(q) cos(2 m theta)
       + (u^2/(1 + u^2))^(p_3/2) cos(theta)^(p_3 - 2) sin(theta)^2 T(2q - 1),
where each b_m is a clamped spline of polynomial degree 7 in q on [0, 1] with simple interior knots (so C^6 in q, with
piecewise constant seventh derivative) and b_m(0) = 0, and T is a polynomial (Chebyshev, degree 5). Polar angle theta in
(-pi/2, pi/2] on x > 0 extended by evenness in x. The coefficients of the reported candidate are in
fixc_c6f_m1.0e-03_shape.npz (read-only; numpy npz; z[0] = k and
z[1:] are the coefficients in the order of names, pairs (m, j) with m = -1 for the fractional-power Chebyshev terms;
spline_knots, spline_order (the degree, passed to scipy BSpline), degree (number of radial functions), angular (150),
singular (6 Chebyshev terms), origin_radius (r_0), L, c_l; the key tail_terms concerns the velocity closure, not rho).
The code that builds the basis is stationary.py (class Shape,
build_basis and _build_spline_tensor; there s = u^2/(1 + u^2) and the fractional exponent is written 6 + 2k/(2 - k), equal
to p_3). Read-only. Use them for spot checks if useful; no refit is asked.

Statements to audit (each is quoted as it would appear in the report; for each, say whether it is correct as stated,
correct with a stated qualification (give the qualification), or wrong (give the correct statement)):

S1 (trial regularity and class). "The fractional-power term is |x|^(p_3 - 2) y^2 (L^2 + r^2)^(-p_3/2) T(2q - 1) in
Cartesian form, in C^(4,beta)_loc with beta = p_3 - 6; the radial splines are of polynomial degree 7 with simple interior
knots, so C^(6,1). The trial is in C^(4,beta)_loc. H(0) = 0, so a(0) = 1 exactly; rho_h is even in x and odd in y by
construction; each angular term is analytic at 0 because b_m(q(u^2))/u^2 is." Please check in particular: the Cartesian
form; whether the spline terms composed with q(u^2) and multiplied by chi^max(m-1,0) cos(2 m theta) are C^(6,1)_loc on
R^2 including the origin (the factor cos(2 m theta) is singular at 0 on its own); the exact Hoelder class of the whole
trial (is it C^(4,beta) and not better, and is beta = p_3 - 6 or p_3 - 6 rounded differently); whether "analytic at 0"
needs "on the first knot interval" or a similar qualification; and that rho_h meets the regularity part of P_2.

S2 (far field). "Since b_m is a polynomial near q = 1 and 1 - q = (1 + u^2)^(-(1-k)/2),
   rho_h = r^k Theta_0(theta) (1 + r^(k-1) Theta_1(theta) + O(r^(2k-2))),
 Theta_0(theta) = L^(3-k) cos(theta)^2 sin(theta) exp(sum_m b_m(1) cos(2 m theta) + T(1) sin(theta)^2 cos(theta)^(p_3-2)),
 and Theta_1 is given by b_m'(1) and T'(1). The leading term is homogeneous of degree 1/c_l, and the first correction is
 relative r^(k-1)." Please check the expansion (including whether the O(r^-2) terms from chi, from (1 + u^2)^((k-3)/2) and
 from (u^2/(1+u^2))^(p_3/2) are dominated by r^(2k-2) for k = 0.179), give Theta_1 explicitly, and say whether the O-term
 is uniform in theta (note cos(theta)^(p_3 - 2) and the factor cos^2 sin vanishing on the axes).

S3 (residual at P). "For the trial, R/rho extends continuously to P with value h(P) - 1 (it is undefined on the x-axis
itself)." Here h(P) is d_y W_2 at P for the trial's own W and P is the zero of W_1 on the positive x-axis. State the
hypotheses needed (regularity of rho_h and W near P, rho_y(P) > 0) and whether "extends continuously" is right, or only
along some approach directions. Also: is it right that an "identity-free" determination of c_l from h(P) = 1 at fixed rho
is therefore not independent of a small residual next to P?

S4 (characteristic defect). Define J_eps(X0) = int_{t_eps}^0 (R/rho)(Phi_t X0) dt along the backward characteristic of the
trial's own W from X0 to the first time t_eps < 0 at which |Phi_t X0 - P| = eps (P is a source node of W: both
eigenvalues A and h(P) positive, A about 10 times h(P)). Statement: "It is the logarithmic density ratio log rho(X0) -
log rho_tr,eps(X0) for transport from that cutoff section (e^J - 1 is the relative difference). A nonzero h(P) - 1 adds
(h(P) - 1) log(1/eps)/h(P) + O(1) to each label off the x-axis as eps -> 0, so the spread over labels is the reported
quantity." Please check: the identification with the log density ratio (define rho_tr,eps precisely); the asymptotic
term, including which eigendirection a generic backward characteristic approaches P along, what happens for labels whose
backward orbit approaches P along the fast direction, and whether the O(1) is uniform; and whether "spread over labels"
removes the eps-divergent part.

S5 (polynomial states). "Polynomial states: x^2 y and every polynomial density grow at least like r^3; the trial grows
like r^k with k = 1/c_l = 0.179, the degree required by R2." (R2 is a proved statement in the report: every nonzero
profile of the relevant class has a homogeneous far field of degree 1/c_l with c_l > 1.) Correct the wording if
"grow at least like r^3" is not literally true for polynomials (zero sets, directions), and say what the sentence can
correctly claim (a polynomial density of the class has degree at least 3, so it is not O(r^k) with k < 3; is that the
right exclusion?). Is every polynomial rho = x^2 y a with a(0) = 1 excluded as an exact profile for another reason too?

S6 (layer sign). Context: if a solution has a conormal layer rho_sing = b_+(s) n_+^lam + b_-(s) (-n)_+^lam along the
invariant curve Gamma = {x = gamma(y)} through P (n = x - gamma(y), s = y), then under the expansion hypotheses each
amplitude obeys the same linear ODE V b' + (lam kappa - 1 - R'/D) b = 0 with V(s) = W_2(gamma(s), s), R(s) =
rho(gamma(s), s), D = 1 + gamma'^2, kappa = 2 c_l - V', and lam = rho_y(P)/(2 c_l - 1) about 2.93 (a previous referee
derived this). Measurement: on every fit, the jump of the third x-derivative of H = log a across Gamma, estimated by
separate polynomial fits on each side at fixed y, is about +0.12 at y = 0, changes sign near y = 0.5 and is about -0.4 at
y = 1. The fits are C^6 (degree-7 splines), so their literal third-derivative jump is zero; the estimate is a feature of
one-sided extrapolation. Statement: "If a solution has a layer of the form |x - gamma(y)|^lambda along that
characteristic, the exponent is lambda = rho_y(P)/(2 c_l - 1), about 2.93, and such a layer is C^(2, lambda - 2) but not
C^3; whether a solution has one is open. A single layer of this form keeps the sign of the step along the curve; the
measured step changes sign near y = 0.5, so the fits' feature is not of this form at leading order." Please check:
(a) whether "keeps the sign" holds for b_+ and b_- separately and for the combination that a one-sided third-derivative
step estimator would see (note a pure power with lam in (2, 3) has no finite third-derivative jump; the estimator with
windows of fixed width sees a window-dependent combination; also H = log a and rho differ by the smooth factor x^2 y
exp, and a = rho/(x^2 y) adds 1/y near the axis); (b) whether V can vanish on Gamma for 0 < y <= 1 (it would allow a sign
change), given W_2 = y h near the axis with h(P) = 1; (c) whether the conclusion "not of this form at leading order" is
justified, should be weakened, or should be dropped. Propose a correct sentence.

For each statement give a short verdict line first (CORRECT / CORRECT WITH QUALIFICATION / WRONG), then the reasoning,
then the replacement wording if any. Numerical spot checks on the npz file are welcome where they decide something
(for example, the far-field coefficients, or V on Gamma for y in (0, 1]); say what you computed.
