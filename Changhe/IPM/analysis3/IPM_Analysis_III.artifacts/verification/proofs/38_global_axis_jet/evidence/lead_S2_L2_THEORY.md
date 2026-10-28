# S2_L2_THEORY.md: weighted L^2 theory for the linearized S2 operator (Avenue I)

First version 2026-10-28T01:44Z (theory author); revised 2026-10-28T02:09Z for the verdicts V022 to V025, 02:41Z (single-knot weight in section 5) and 02:45Z (V031, V032). Labels: THEOREM (verifier-confirmed), DERIVED (proof written here, awaiting
independent check), CONDITIONAL (proved under named hypotheses), NUMERICAL (computed, not a bound), OPEN, REFUTED.
Nothing in this file is a THEOREM until the matching verdict exists; the verdict status of each item is listed in
section 9.

## 0. Setting and notation

Equation, parity and background are those of the accompanying CONVENTIONS (items S1 to S4). Summary:

- F(rho) = (c_l X + U[rho]).grad rho - rho, U = (-psi_y, psi_x), -Lap psi = d_x rho on R^2, rho even in x, odd in y
  (class P). c[h] = psi[h]_xy(0); normalization 3 c_l - c[rho] = 1.
- Background rho_bar: the exactly joined and exactly normalized modal trial (c_l = 1/k exactly, k = 0.17936053...).
  A = 2 c_l - 1 = 10.1507..., D = 4 c_l - 1 = 2A + 1 = 21.3014..., b_0 := 1 + c_l = (A + 3)/2 = 6.5753...
- V = c_l X + U[rho_bar]; div V = 2 c_l. Full linearization L h = V.grad h - h + W[h].grad rho_bar with
  W[h] = U[h] + (c[h]/3) X; L = L_fix + (c[h]/3) G_bar, G_bar = X.grad rho_bar, L_fix h = V.grad h - h + T h,
  T h := U[h].grad rho_bar.
- Self-adjoint Riesz convention: Rt_j is the Fourier multiplier with symbol nu_j = xi_j/|xi|. Then
  U[h] = (Rt_1 Rt_2 h, -Rt_1^2 h) and T h = a Rt_1 Rt_2 h - c Rt_1^2 h with a := d_x rho_bar, c := d_y rho_bar.
  The frozen symbol of T is p(X, nu) = a nu_1 nu_2 - c nu_1^2, and
      b_+(X) := max_{|nu| = 1} p(X, nu) = (|grad rho_bar| - d_y rho_bar)/2 >= 0.
- q(X) := V(X).X/|X|^2 (radial rate of the flow), t = log r.

## 1. Theorem O: the frozen saddle on a jet-plus-remainder space (THEOREM: (a), (b), (d) CONFIRMED in V022; (c) CONFIRMED as a bounded integral extension)

Verdict notes (V022). The verifier's independent proof uses a unitary double-logarithmic transform to the multiplier
-kappa_0 + i(-A xi + D eta) and confirms (a), (b), (d) with the global realization stated here. Numerical value: for
a = 7/2, b = 6/5 one has kappa_0 = (8/5) A + 3/10 = 16.54116035405294722844... (the earlier rounded value 16.5 is
corrected), sigma = 7/10, C_ang^2 = 20/3. The strain extension of (c) satisfies
|c[h 1_{r<1}]| <= |J|/8 + 0.069735617396310252 ||beta_t'||_G + 0.045183183318774124 ||h_R||_{R_w} (constants proved by
the verifier). The verifier REFUTED only the reading of (c) under which every member of the abstract graph space has
classical pointwise derivatives at 0: a thin flow-tube sum in Z_0 is not even continuous at 0. (c) is therefore a
statement about the continuous extension from the core, as written below.

T_0 := -A x d_x + D y d_y - 1 is the frozen transport at the origin (D = 2A + 1). Let Y_0 := -A x d_x + D y d_y, with
flow Phi_s(x, y) = (x e^{-A s}, y e^{D s}).

Weights. Fix 5/2 < a < 9/2, 0 <= b < 3/2 with a + b > 4, and put w(X) = |x|^{-2a} |y|^{-2b},
kappa_0 := b_0 + A a - D b. Jet weight e^{-2 sigma t} with sigma := a + b - 4 > 0 (in the CONVENTIONS S9 notation
b2 = a + b - 5/2).

Spaces. R_w := L^2_P(R^2, w dX). G := L^2(R, e^{-2 sigma t} dt). Jet-plus-remainder space
    Z_0 := { h = x^2 y beta(log r) + h_R : beta(t) = J + beta_t(t), beta_t' in G, beta_t(-inf) = 0, h_R in R_w,
             Y_0 h_R in R_w },
||h||_{Z_0}^2 := |J|^2 + ||beta_t'||_G^2 + ||h_R||^2 + ||Y_0 h_R||^2. Target
    Y := { f = x^2 y gamma(log r) + F_R : gamma in G, F_R in R_w },  ||f||^2 = ||gamma||_G^2 + ||F_R||^2.
(The decomposition is unique: x^2 y gamma(log r) is in R_w only if gamma = 0, because a > 5/2 makes
int |cos theta|^{4 - 2a} d theta diverge.)

Theorem O. Assume kappa_0 > 0.
(a) On R_w, T_0 with domain {h in R_w : Y_0 h in R_w} is bijective onto R_w, with
    T_0^{-1} F = - int_0^inf e^{-s} F(Phi_s X) ds,   ||T_0^{-1}|| = 1/kappa_0 (sharp).
    The conormal fields x d_x and y d_y commute with T_0, so the same bound holds on every conormal space
    H^m_b(w) = {h : (x d_x)^i (y d_y)^j h in R_w, i + j <= m}.
(b) J(h) := lim_{t -> -inf} beta(t) is a coordinate of Z_0, hence continuous. T_0 maps Z_0 boundedly into Y, its kernel
    in Z_0 is spanned by x^2 y, and it is onto Y. The right inverse with J = 0 is
        beta_t(t) = (1/D) int_{-inf}^t gamma,   h_R = T_0^{-1}( F_R + ((A + D)/D) x^2 y cos^2(theta) gamma(log r) ),
    with ||beta_t'||_G = ||gamma||_G / D and ||h_R|| <= kappa_0^{-1} (||F_R|| + ((A + D)/D) C_ang ||gamma||_G),
    C_ang^2 = int_0^{2 pi} |cos theta|^{8 - 2a} |sin theta|^{2 - 2b} d theta < inf.
(c) The strain functional c is continuous on Z_0 restricted to {r < 1}: |c[h 1_{r<1}]| <= C (|J| + ||beta_t'||_G + ||h_R||).
(d) Exclusions. (i) T_0 has no approximate kernel in Z_0 / span{x^2 y}: ||h||_{Z_0} <= C ||T_0 h||_Y when J = 0.
    In particular the degree-two center quasimodes (|x|^{1.3227} sgn(y) |y|^{0.6773} cut off, verified obstruction of
    the earlier diagnostic norm) are not quasimodes here. The uncut angular profile is not in R_w near the y-axis
    (2 p - 2a < -1); angularly cut-off versions can belong to R_w (V022), and the inverse bound excludes them as
    approximate kernels after normalization in the Z_0 norm. (ii) The packets B_delta = (4 H_delta - H_{2 delta})/3, H_delta = x^2 y chi(r/delta), which make J
    nonclosed in weaker norms (verified), have J(B_delta) = 1 and ||T_0 B_delta||_Y ~ delta^{-sigma} -> infinity: they
    do not contradict (b).

Proof. (a) By the change of variables X' = Phi_s X (Jacobian e^{(D - A)s}, w(Phi_s^{-1} X') = w(X') e^{(-2aA + 2bD)s}),
||F o Phi_s||_w = e^{-(kappa_0 - 1)s} ||F||_w, since (D - A)/2 + aA - bD = kappa_0 - 1. Hence the integral converges in
R_w with norm <= ||F||/kappa_0, and differentiating along the flow gives (Y_0 - 1) h = F. For uniqueness, the field
Y_0 is tangent to both axes with |Y_0| <= C dist(X, axes) locally and |Y_0| <= C r, so the cutoffs chi(x/eps),
chi(y/eps), chi(r/R), chi(r eps) have Y_0 chi uniformly bounded; with Friedrichs mollification in the open quadrants
this shows that C_c^infty of the open quadrants is a core for the maximal operator. On the core,
Re <T_0 h, h>_w = -(1 + (1/2) div Y_0 + (1/2) Y_0.grad log w) ||h||^2 = -kappa_0 ||h||^2
(div Y_0 = D - A, (1/2) Y_0.grad log w = aA - bD). So T_0 and its adjoint are injective with closed range: T_0 is
bijective. Sharpness: in the double Mellin variables (log|x|, log|y|) per quadrant, T_0 is multiplication by
-kappa_0 + i(-A xi + D eta). Commutation: [x d_x, Y_0] = [y d_y, Y_0] = 0.
(b) Exact identities: T_0(x^2 y) = (-2A + D - 1) x^2 y = 0 and, for beta = beta(log r),
T_0(x^2 y beta) = x^2 y beta'(t) (D sin^2 theta - A cos^2 theta) = x^2 y (D beta' - (A + D) cos^2(theta) beta').
So T_0 h = x^2 y D beta_t' + [T_0 h_R - (A + D) x^2 y cos^2(theta) beta_t']. The bracket lies in R_w: with
x^2 y cos^2 theta = r^3 cos^4 theta sin theta and dX = r^2 dt d theta,
|| x^2 y cos^2(theta) g(log r) ||_w^2 = C_ang^2 int |g|^2 e^{(8 - 2a - 2b) t} dt = C_ang^2 ||g||_G^2
(C_ang < inf iff a < 9/2 and b < 3/2). Matching the decomposition of Y gives D beta_t' = gamma and the stated remainder
equation; Hardy's inequality (beta_t(-inf) = 0, sigma > 0) gives int |beta_t|^2 e^{-2 sigma t} <= sigma^{-2} ||beta_t'||_G^2.
The kernel: T_0 h = 0 forces gamma = 0, so beta_t = 0, and then T_0 h_R = 0, so h_R = 0 by (a): h = J x^2 y.
(c) Let C_0 be the core of Z_0 consisting of J x^2 y chi_0(r) + x^2 y beta_t(log r) chi_0(r) + h_R with beta_t smooth,
compactly supported in t, and h_R in C_c^infty of the open quadrants. Every element of C_0 vanishes to order 3 at 0, so
h_y(0) = 0 and c[h] = (1/pi) int sin 3theta r^{-3} h (CONVENTIONS S3.2, no local term). The estimate below shows that this
integral is continuous in the Z_0 norm, and c is defined on Z_0 as its continuous extension (this is a definition for
the abstract maximal space, not a pointwise statement about members of Z_0; correction after the verifier's audit
note of 01:46Z). The jet part gives
(1/pi)(pi/4) int_0^1 beta(log r) r dr, bounded by C(|J| + ||beta_t'||_G) (Cauchy-Schwarz, sigma > 0). The remainder:
|int_{r<1} sin 3theta r^{-3} h_R| <= ||h_R||_w (int_{r<1} r^{-6} w^{-1})^{1/2}, finite because 2a + 2b - 4 > 0.
(d) (i) is (b) with J = 0. For (ii): beta = (4 chi(e^t/delta) - chi(e^t/(2 delta)))/3 has beta(-inf) = 1 and
beta' supported where e^t ~ delta, so ||D beta'||_G^2 ~ delta^{-2 sigma}. QED.

Remark O.1 (what Theorem O does and does not give). It is a frozen statement: J is a continuous coordinate, the
x^2 y direction is the only kernel, and the remainder inverse has the explicit constant 1/kappa_0 (kappa_0 = 16.541 at
a = 7/2, b = 6/5). It does not control the nonlocal coupling, which near 0 is formally smaller by r^2
(CONVENTIONS S6.1); a localized version needs the weighted velocity bounds of section 5 (Lemma E), because w is not an A_2
weight.

## 2. Exact criticality of x^2 y: why the origin weight must be anisotropic (N1 to N5 CONFIRMED in the corrected forms of V025)

Proposition N1. Consider product-conic weights w = r^{-2 beta_r} |cos theta|^{-2a} |sin theta|^{-2b} near the origin.
For the frozen operator, (1/2) Y_0.grad log w + 1 + (D - A)/2 = kappa(theta) with
    kappa(theta) = b_0 + aA - bD + e q_0(theta),  e := a + b - beta_r,  q_0(theta) = -A cos^2 theta + D sin^2 theta in [-A, D].
Coercivity on all rays (kappa > 0 for every theta) is equivalent to
    beta_L(b) < beta_r < beta_U(a),  beta_L(b) = (b(3A + 1) - b_0)/A,  beta_U(a) = (a(3A + 1) + b_0)/D.
x^2 y (cut off) belongs to L^2(w) near 0 iff a < 5/2, b < 3/2 and beta_r < 4. Since D = 2A + 1 and b_0 = (A + 3)/2,
beta_L(3/2) = beta_U(5/2) = 4 exactly. Consequently: if T_0 is coercive in L^2(w) and x^2 y is not in L^2(w), then
a >= 5/2.
Proof. kappa is affine in q_0, so positivity on [-A, D] is positivity at the two ends; these are the two inequalities.
beta_L is increasing in b and beta_U increasing in a. If a < 5/2 and b < 3/2, exclusion needs beta_r >= 4 > beta_U(a).
If a < 5/2 and b >= 3/2, then beta_r > beta_L(b) >= 4 > beta_U(a). QED.

So any space in which J is continuous by exclusion of x^2 y from the remainder, and in which the frozen saddle is
coercive, contains the angular factor |cos theta|^{-2a}, a >= 5/2. The endpoint a = 5/2 is admissible with a positive
margin (b < 3/2, beta_L(b) < beta_r < 4); strict a > 5/2 is not forced (V025, which REFUTED the earlier word
"strictly"). This sharpens CONVENTIONS S7.3
(isotropic weights) and explains the borderline: kappa vanishes identically at (a, b, beta_r) = (5/2, 3/2, 4), the
weight for which x^2 y is critical, because T_0(x^2 y) = 0.

Proposition N2 (persistence along the outgoing y-axis; CONFIRMED in V025 conditional on the positive axis rate
q(0, y) > 0 for y != 0, which for the trial is a numerical observation, not yet a certified bound). Let w = |cos theta|^{-2a(t)} e^{phi(X)} near the y-axis with
a(t) smooth and phi smooth. Then near theta = pi/2,
    (1/2) V.grad log w = -a(t) V.grad log|cos theta| - a'(t) q(X) log|cos theta| + (1/2) V.grad phi,
and on the y-axis q(0, y) = V_2(0, y)/y > 0 (numerically 5.58 <= V_2/y <= 21.31 on the trial). If a'(t_1) < 0 at some
t_1, then kappa_w -> -infinity as theta -> pi/2 at r = e^{t_1}. Hence a(t) is nondecreasing along the whole y-axis:
the anisotropic factor cannot be switched off anywhere on the outgoing axis. On the incoming x-axis near 0
(q < 0), the analogous factor |sin theta|^{-2b(t)} can be decreased outward at no cost (the sign is favorable).
Proof. log|cos theta| -> -infinity, a' q < 0 at t_1, so the middle term tends to -infinity; the other terms stay
bounded, because V.grad log|cos theta| = V_1/x - q -> d_x V_1(0, y) - V_2(0, y)/y on the axis. QED.

Corollary N3 (the y-axis jet). In such a space every element vanishes on the y-axis to order a - 1/2 > 2 in the L^2
sense, so the x^2 Taylor coefficient along the entire y-axis must be a separate unknown:
    h = x^2 g(y) chi_ax(X) + h_R,   g(y) = y beta(log|y|),  J = lim_{y -> 0} g(y)/y.
(chi_ax is a conic cutoff to a neighbourhood of the y-axis.) The jet row (x^2 coefficient of L_fix h on the axis) is
    V_2(0, y) g' + (2 u(y) - 1) g + 2 rho_2(y) d_x U_1[h](0, y) + rho_2'(y) U_2[h](0, y) = f_2(y),
with u(y) := d_x V_1(0, y) and rho_bar = x^2 rho_2(y) + O(x^4). This is the row of L_fix. The row of the full
linearization L replaces U by W = U + (c[h]/3) X in the two coupling terms, i.e. adds (c[h]/3)(2 rho_2(y) + y rho_2'(y)):
    V_2(0, y) g' + (2 u(y) - 1) g + 2 rho_2 (d_x U_1[h](0, y) + c[h]/3) + rho_2' (U_2[h](0, y) + c[h] y/3) = f_2(y).
As y -> 0 (rho_2 = y + o(y), d_x U_1[h](0, y) -> -c[h], U_2[h](0, y) = c[h] y + o(y)) the L_fix coupling is
-c[h] y + o(y) and the full coupling is o(y): the strain term cancels the leading coupling exactly, as in CONVENTIONS S4.5.
(Derivation: V_1 = u x + O(x^3), U_1[h] odd in x, U_2[h] even in x, d_x rho_bar = 2 x rho_2 + O(x^3),
d_y rho_bar = x^2 rho_2' + O(x^4), X.grad(x^2 rho_2) = x^2 (2 rho_2 + y rho_2'). Correction of the first version,
which labelled the L_fix row as the row of L; pointed out by the verifier at 01:46Z.) At y -> 0: V_2 = D y,
u = -A, and the row is D y beta'. At infinity V_2 ~ c_l y, u -> c_l, and the homogeneous solution is g ~ y^{k - 2},
the trace of the r^k Theta far tails. Trial values (NUMERICAL): u changes sign near y = 9.5 (u(8) = -1.02,
u(9.9) = +0.53), rho_2/y decreases from 1 at 0 to 0.29 at y = 15 and decays like y^{k - 3}.

Proposition N4 (far window). At infinity V = c_l X + O(r^k) and DV -> c_l I. With a far factor r^{-2 gamma}
(times any bounded angular factor), kappa_infinity = b_0 - gamma c_l. Coercivity needs gamma < b_0/c_l = 1 + k;
exclusion of the homogeneous far tails r^k Theta needs gamma < 1 + k (the same number, since b_0/c_l = 1 + k
exactly); membership of the trial residual r^{2k - 1} Eps(theta) holds for gamma > 2k and needs it when the leading coefficient
Eps is not identically zero (V025). So 2k < gamma < 1 + k. A radial
A_2 far weight needs in addition gamma < 1. With gamma < 1 + k the scaling direction K_bar ~ (1 - k) r^k Theta_0 is
excluded; then J is not a constraint but an output (it is fixed by the equation, and a(0) = 1 is restored by the
exact rescaling rho -> lambda rho(X/lambda) with lambda^2 = 1 + J, valid when 1 + J > 0).

Remark N5 (nonlinear consistency at infinity; corrected statement CONFIRMED in V025). An exact solution has far
exponent k' = 1/c_l[rho], which differs from k when c[h] != 0. The first version said that r^{k'} - r^k is not of the
form r^k (C + kappa log r) + o(r^k); this literal statement is false for k' < k (take C = -1, kappa = 0) and was
REFUTED. The correct fixed-space statement (V025): for gamma < 1 + k and 0 < |delta| < 1 + k - gamma, the function
r^{k + delta} Theta - r^k Theta (cut off near infinity) lies outside span{r^k Theta, r^k log r Theta} + L^2(r^{-2 gamma})
at infinity, for either sign of delta. Moreover any twice differentiable small parameterization of the tail by a fixed
background has a log^2 r second variation. Hence rho_bar + Z with a fixed background cannot contain exact solutions
with c[h] != 0, and the nonlinear term (c[h]/3) X.grad(kappa KP) grows like r^k log r. The consistent nonlinear formulation is the parametric one with a
one-parameter background family rho_bar_ell whose far part is exactly r^{1/ell} Theta_bar (ell X.grad - 1 annihilates
it), unknowns (ell, h) with h in Z (no r^k tails at all), and the scalar equation 3 ell - c[rho_bar_ell + h] = 1. The
derivative d rho_bar_ell/d ell ~ -k^2 r^k log r Theta_bar is the log-tail column; the far angular profile Theta_bar is
then fixed by the space: the linear far problem has the outflow family r^k Theta for every Theta, and the space
selects the member with the tail of the background.

## 3. The weighted Garding-Lyapunov estimate for L_fix (DERIVED, with standard harmonic-analysis inputs)

Lemma G1 (transport identity). For any smooth positive weight w and h in C_c^infty(R^2 \ {0}),
    Re <(V.grad - 1) h, h>_w = - int kappa_w |h|^2 w,   kappa_w := b_0 + (1/2) V.grad log w.
(Integration by parts with div V = 2 c_l.)

Lemma G2 (coupling bound). Let a, c be continuous on R^2, tending to 0 at 0 and at infinity. For every eps > 0 there
is a compact operator K_eps on L^2 with
    Re <T g, g> <= int (b_+ + eps) |g|^2 + Re <K_eps g, g>   for all g in L^2.
Proof. Approximate a, c uniformly within eps/4 by a_eps, c_eps in C_c^infty(R^2 \ {0}); the error in T has norm
<= eps/2 (|Rt_1 Rt_2|, |Rt_1^2| <= 1). For the smooth coefficients, M(X) := [[-c_eps, a_eps/2], [a_eps/2, 0]] has
p_eps = nu^T M nu and lambda_max(M) = b_+^eps. The matrix lambda_max(M) + eps/4 - M is positive definite and smooth;
its square root Q(X) equals (eps/4)^{1/2} I outside a compact set. Then, with R = (Rt_1, Rt_2)^T and
R_1^2 + R_2^2 = I,
    (b_+^eps + eps/4) - Op(p_eps) = (Q R)^*(Q R) + K,
where K is a finite sum of commutators [m, Rt_j] Rt_l with m in C_c^infty + constants, compact on L^2 (commutators
of Riesz transforms with continuous functions vanishing at infinity are compact; Uchiyama's theorem, or directly for
C_c^infty symbols). Hence Re <Op(p_eps) g, g> <= int (b_+^eps + eps/4)|g|^2 + Re <K g, g>, and
|b_+^eps - b_+| <= eps/4. QED. (This is the square identity of the earlier analysis of this case, extended from
Wiener-algebra coefficients to C_0 coefficients by approximation.)

Lemma G3 (radial A_2 weights and conjugation). Let w = e^{mu(log r)} with mu smooth, mu' and mu'' bounded and
M := sup|mu'| < 2. Then (i) w is an A_2 weight on R^2; (ii) Rt_j Rt_l are bounded on L^2(w); (iii) for every
coefficient m continuous on R^2 \ {0} with m -> 0 at 0 and at infinity, m [w^{1/2}, Rt_j Rt_l] w^{-1/2} is compact
on L^2.
Proof. (i) For balls B(0, R): since mu' + 2 >= 2 - M > 0, int_{B(0,R)} w <= 2 pi R^2 w(R)/(2 - M), and likewise for
w^{-1}; the product of averages is <= 4/(2 - M)^2. For balls B(x_0, rho) with rho < |x_0|/2, w varies by at most
the factor 3^M; larger balls are comparable to balls centred at 0. (ii) is the A_2 theorem. (iii) The kernel of
[w^{1/2}, S] w^{-1/2} is K(X - Y)(w(X)^{1/2} w(Y)^{-1/2} - 1) with |K(Z)| <= C |Z|^{-2}. Let m_eps = m 1_{eps < r < 1/eps};
||(m - m_eps)[...]|| -> 0 because the commutator is bounded by (ii). For X in the annulus, the part of the kernel with
|Y| < eps/2 or |Y| > 2/eps is Hilbert-Schmidt: (w(X)/w(Y))^{1/2} <= C_eps |Y|^{-M/2} near 0 and <= C_eps |Y|^{M/2} at
infinity, and |Y|^{-M} is integrable at 0, |Y|^{M - 4} at infinity, exactly when M < 2. On the remaining bounded
region |w(X)^{1/2} w(Y)^{-1/2} - 1| <= C_eps |X - Y|, so the kernel is O(|X - Y|^{-1}) there: a weakly singular kernel
on a bounded set, hence compact (truncate at |X - Y| > eta: Hilbert-Schmidt; the rest has Schur norm O(eta)). QED.

Theorem R (Fredholm index zero in radial A_2 weights; CONDITIONAL THEOREM, CONFIRMED in V023 under the exact
hypotheses: V globally Lipschitz and C^1 with V(0) = 0 and div V = 2 c_l; coupling coefficients a, c continuous and
tending to 0 at 0 and at infinity; w = e^{mu(log r)} with sup|mu'| < 2; the exact global margin (H_m). The verifier's
proof gives the estimate with m_* itself, with no eps loss. It also replaces the step of Lemma G2 below in which the
square root of lambda_max(M) + eps/4 - M is called smooth, which fails at zeros of the coefficients, by an exact matrix
quadratic inequality and compact coefficient commutators. The weighted Riesz-product bound is proved directly by a
Schur test with auxiliary function 1/r. V031 extends the theorem, with the same margin constant and no smoothing, to
globally Lipschitz mu with Lip(mu) < 2, in particular to piecewise affine mu; the core, adjoint and compactness steps
hold with weak derivatives.) Let w be as in Lemma G3 (or mu Lipschitz as in V031) and let D_w be the
maximal domain {h in L^2_P(w) : V.grad h in L^2_P(w)}. Assume the margin hypothesis
    (H_m)   m_* := inf_{X != 0} [ b_0 + (1/2) mu'(log|X|) q(X) - b_+(X) ] > 0.
Then L_fix : D_w -> L^2_P(w) is Fredholm of index 0, and for every eps in (0, m_*) there is a compact K on L^2_P(w)
with
    (m_* - eps) ||h||_w <= ||L_fix h||_w + ||K h||_w   for all h in D_w.
L_fix is invertible on L^2_P(w) if and only if it is injective on D_w.
Proof. Core: C_c^infty(R^2 \ {0}) (parity-projected) is a core for the maximal operator V.grad on L^2(w): V is
globally Lipschitz with V(0) = 0, so cutoffs chi(r/R), chi(r/eps) have |V.grad chi| <= C, and Friedrichs mollification
applies locally (w is smooth away from 0). On the core, with g = w^{1/2} h, Lemma G1, Lemma G2 (applied to g with
eps/2) and Lemma G3(iii) give
    Re <L_fix h, h>_w <= - int (kappa_w - b_+ - eps)|h|^2 w + Re <K h, h>_w <= -(m_* - eps) ||h||^2 + ||K h|| ||h||,
K compact; by density this holds on D_w. Cauchy-Schwarz gives the displayed estimate, so L_fix has finite-dimensional
kernel and closed range (Peetre). The adjoint in L^2(w) has the same maximal domain (the Friedrichs argument is
symmetric), and Re <L_fix^* h, h>_w = Re <L_fix h, h>_w, so the same estimate holds for L_fix^*: the cokernel is finite
dimensional. Index: L_s := V.grad - 1 + s T, s in [0, 1], satisfies the same estimate with b_+ replaced by s b_+ <= b_+
(T is bounded on L^2(w) by Lemma G3(ii), so s -> L_s is norm-continuous from D_w with the graph norm). L_0 satisfies
Re <L_0 h, h> <= -m_* ||h||^2 and the same for L_0^*, so L_0 is invertible and has index 0; the index is constant along
the path. QED.

Numerical status of (H_m) (NUMERICAL, not a bound; code and data in the accompanying artifacts, code/lyapunov,
data/lyapunov). Trial field on the polar grid t in [log 1e-3, log 1e5] (700 points), theta in [0, pi/2]
(181 points), velocity from the Green representation of the trial (c reproduced to 7e-14):
- max b_+ = 10.14 > b_0 = 6.575, attained at r = 12.5, theta = 1.239; b_+ > b_0 exactly on a region inside
  r in [5.5, 50.6], theta in [0.78, 1.48], where |V| >= 42 and q >= 0.88. So no constant weight satisfies (H_m)
  (consistent with the negative-energy obstruction), but the flow is strongly outward there.
- With mu' free at each t, the largest attainable margin on the grid is 2.98.
- An explicit smooth choice (window midline, Gaussian smoothing in t of width 0.3, mu' = -1.8 at large r,
  mu' in [-1.80, 1.09]) gives min margin 0.81 on the grid, attained at r = 8.43, theta = 0.96. M = 1.80 < 2.
Certification of (H_m) needs interval enclosures of b_+ and q on all of R^2, including the asymptotic regions
(b_+ -> 0 and q -> -A cos^2 + D sin^2 at 0; q -> c_l at infinity).
- The weight used for certification is piecewise affine. mu~(0) = 0, and mu~' is piecewise constant with knots
  t = 3/2, 7/4, 3, 4, 5, 6, 7, 8, 9, 10 and values 4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20 (multiples of 1/16) on
  (-oo, 3/2), [3/2, 7/4), ..., [10, oo). Then sup|mu~'| = 7/4 < 2, e^{mu~} ~ r^{1/4} at 0 and ~ r^{-5/4} at infinity
  (-5/4 lies in (-2, -4k)).
- On the same grid, evaluating both neighbouring slopes at each knot, the minimum margin is 2.590, at r = 4.48,
  theta = 0.90 (NUMERICAL; code/lyapunov/mu_pwc.py, data/lyapunov/mu_pwc.json). By V031, Theorem R applies to this
  weight directly.
- A box certificate of (H_m) for mu~ is being computed with the exact modal trial in ball arithmetic. Its status is
  recorded in the accompanying S2_NUMERICAL_CERTIFICATES.md.

Remark R.1 (what Theorem R gives). It is the strongest inverse-type statement for the full coupled nonlocal L_fix
that the present analysis can reach in an A_2 class: closed range, finite kernel, index 0, and an explicit coercive
constant modulo a compact operator. It is not usable for the existence problem: in L^2(w) with |mu'| < 2 near 0, J is
not continuous (x^2 y is deep inside the space), c[h] is unbounded, G_bar is not in L^2(w), and no nonlinear estimate
holds. Proposition N1 shows that no A_2 weight can repair the origin. Injectivity is OPEN (no kernel element is known:
the scaling mode, the only obvious candidate, is excluded by the far weight; translations are outside class P).

Remark R.2 (the strain is not closable on the Theorem R graph; THEOREM, V032). Let w be comparable to r^eta near 0
with eta >= -4, satisfying the coefficient and tail hypotheses of V032; this covers mu~, whose eta is 1/4. Take H smooth,
annular and in class P, with c[H] = 1, and set h_n = eps_n H(X/eps_n), eps_n -> 0 (for eta = -4, average over disjoint
scales). Then J(h_n) = 0 and c[h_n] = 1, while h_n -> 0 and L_fix h_n -> 0 in L^2(w).
- Hence c has no closed extension to D_w with its graph norm.
- The full normalized operator L = L_fix + (c/3) G_bar, as a map into L^2(w) plus span{G_bar}, is not closable on D_w.
- Adding only the far compensation coordinate (KP) leaves the constrained graph nonclosed.
- So Theorem R is a statement about L_fix. The normalization must be carried by a stronger origin space: Z_cap of
  the accompanying S2_C_FUNCTIONAL.md, or Z_0 and Z of sections 2 and 5 here, where c is bounded.

## 4. Lyapunov weights reduce to conditions at the fixed points (DERIVED, sketch)

The trial flow has three invariant ends: the source P = (x_P, 0) (repelling node, eigenvalues A_P ~ A, mu_P ~ 1), the
saddle 0, and infinity (attracting, V ~ c_l X). Every orbit in the open quadrant leaves every neighbourhood of P in
finite time and reaches infinity, except the x-axis segment (0, x_P) and the stable and unstable separatrices of 0 (the
axes). Let E(X) be continuous with E < 0 on neighbourhoods N_P, N_0, N_inf of the three ends (in the conormal sense at
0, i.e. for the frozen rate there). Then there is a smooth phi with V.grad phi >= 2 E + 2 delta outside
N_P cup N_0 cup N_inf, obtained by integrating E along orbits from a transversal; the transit time through the
complement of the three neighbourhoods is uniformly bounded. Taking E = b_+ - b_0 + delta (L^2) or the H^s analogue
of section 6 shows that (H_m)-type margins are decided by local conditions at P, 0 and infinity, plus the A_2
constraint at 0 and infinity; on compact sets away from 0 any smooth bounded weight is admissible (equivalent norm,
compact conjugation commutators). The numerical windows above are an explicit radial instance.

## 5. A jet-compatible global weight and the consistent domain (CONDITIONAL / OPEN)

Weight. w = |cos theta|^{-2a} |sin theta|^{-2 b(t)} e^{mu(t)}, a constant (Proposition N2), b(t) decreasing from b_max to
0 (free on the incoming x-axis), mu' -> -2(a + b_max) + (window) at 0, mu' -> -2 gamma at infinity. At the origin this
is the product weight of Theorem O times r^{-2 e}, and kappa(theta) = kappa_0 + (a + b + mu'/2) q_0(theta); coercivity
needs a + b + mu'/2 in (-kappa_0/D, kappa_0/A).

NUMERICAL (grid as above; code/lyapunov/aniso*.py): with a = 7/2, b_max = 6/5, b(t) = (6/5)(1 - tanh(t/2))/2 and an
explicit smooth mu' rising from -8.5 (r -> 0) to -1.64 (r -> infinity, gamma = 0.82 in (2k, 1 + k)), the margin
kappa_w - b_+ is >= 1.36 on the grid (minimum at r = 19.6 next to the x-axis beyond P; >= 12.0 for r < 0.1, >= 17.2
for 0.1 < r < 5, >= 1.58 for r > 60, >= 1.63 next to the y-axis). The window is feasible at every grid radius for
a in {2.6, 3.0, 3.5, 4.0, 4.45} and b_max in {0, 1.2, 1.45}. Along the y-axis the angular factor contributes
a (V_2/y - u) (110 at y -> 0, 1.3 at y = 1e3, -> 0 at infinity), which is why it is harmless there.

Simpler weight with b = 0 (NUMERICAL, added 02:41Z; work/lyap/aniso_knot0.py, artifacts/data/lyapunov/aniso_knot0.json).
- Take w_a = |cos theta|^{-2a} e^{mu_a(log r)}, a = 17/4, with mu_a' = -2a for t < 0 and mu_a' = -5/4 for t >= 0
  (mu_a(0) = 0). In r < 1 this is exactly |x|^{-2a}, the Theorem O weight with b = 0. So Theorem O and the strip
  estimate V026 (unweighted in y) apply in the unit disk without a change of weight.
- The margin for this weight is m_a = b_0 + (mu_a'/2) q + a T_ang - b_+, with
  T_ang = tan(theta) V.grad(theta) = sin(theta) V_2/r - sin(theta)^2 V_1/x.
- On the grid, min m_a = 3.09, in the far field (the limit b_0 - (5/8) c_l). The minimum is 12.78 at the knot with both
  values, 49.7 for r < 0.1 and 9.97 for 0.1 < r < 5. The values are the same for a = 4.1 and a = 4.4 except near 0.
- The factor |sin theta|^{-2b(t)} of the weight above is not needed. Its own contribution to the multiplier is
  -b cot(theta) V.grad(theta), which equals -b(A + D) cos^2(theta) for the frozen field and is never positive.
- The far exponent -5/4 meets the membership conditions: r^k Theta is out of the space, and r^{2k-1} Eps is in it.
- The certification of m_a on boxes was requested from the numerics team (theory author message 7).
- This weight is the candidate for (H_m') below. Its Garding bound (E4) is not covered by V023.

Candidate consistent domain (definition). Z := { h = J x^2 y chi_0 + x^2 g_t(y) chi_ax + h_R + kappa KP } where:
J in R; g_t is the jet correction along the y-axis in a weighted 1D space adapted to the jet row (Corollary N3), with
g_t = o(y) at 0 and g_t = o(y^{k-2}) at infinity; h_R in L^2_P(w) with the conormal regularity needed below; KP is the
log tail r^k log r Theta_0 cut off near infinity, with kappa tied to c[h] so that the r^k Theta_0 tails of
(c[h]/3) G_bar and of kappa L KP cancel (kappa = -c[h_0] k/(3 c_l + k c[KP]), where h_0 is the uncompensated part, so that c[h] = c[h_0] + kappa c[KP];
the compensated column; V025). Target
Y := { x^2 f_2(y) chi_ax + F_R : f_2 in the jet target, F_R in L^2_P(w) }.

On Z: J is continuous (Theorem O(b) along the axis); c is bounded (Theorem O(c) near 0, the far weight with
gamma < 1 + k at infinity); L maps the jet row to a 1D transport problem whose homogeneous solution behaves like J y at 0
and like y^{k - 2} at infinity, so with the far condition the jet row is uniquely solvable, J is determined, and the
pure-transport operator (coupling switched off) is invertible on Z by Theorem O, Lemma G1 and the margin.

Conditional Theorem C (statement of the missing link). Suppose
 (E) (edge Garding lemma) the Taylor-subtracted coupling T_R h := [U[h].grad rho_bar]_remainder is bounded on L^2(w),
     and Re <T_R h, h>_w <= int (b_+ + eps)|h|^2 w + Re <K h, h>_w with K compact; and the y-axis traces
     U_2[h](0, .), d_x U_1[h](0, .) are bounded (and compact into the jet target after multiplication by rho_2, rho_2');
 (H_m') the margin inf (kappa_w - b_+) > 0 holds for the weight of this section.
Then L : Z -> Y is Fredholm of index 0, by the proof of Theorem R with the block-triangular homotopy
s -> (jet row with coupling s, remainder with coupling s), plus a finite-rank change for the strain/KP bordering.
Why (E) is plausible (not a proof): near the y-axis the coupling coefficients vanish, d_x rho_bar = 2 x rho_2 + O(x^3),
d_y rho_bar = x^2 rho_2' + O(x^4), and b_+ = O(|x|); in the edge regime |x||xi| <~ 1, where the conjugated velocity
operator is not pseudodifferential, the factor x makes the coupling of relative size 1/|xi|, hence compact after
frequency and spatial localization; in the regime |x||xi| >> 1 the conjugated operator has the Riesz principal symbol
and Lemma G2 applies. At the origin the coefficients are O(r^2) and the strain term (c/3) X exactly cancels the
non-Taylor-subtracted part of the velocity (CONVENTIONS S4.5). The Taylor-subtracted velocity bounds in the weights
|cos theta|^{-2a}, a not in 1/2 + Z, follow from the Mellin criterion: the subtracted 1D kernel
|x|^{-a}|s|^{a}(x/s)^m/(x - s) is bounded on L^2 iff m - 1/2 < a < m + 1/2 (m = number of subtracted jets). With parity
each nonzero subtracted jet shifts the window by 2, because the next jet vanishes. For the odd output U_1 the windows
are (-1/2, 3/2), then (3/2, 7/2) after subtracting x d_x U_1(0, y). For the even output U_2 they are (-3/2, 1/2), then
(1/2, 5/2) after subtracting U_2(0, y). The coupling needs U_1 in L^2(|x|^{-2(a-1)}) and U_2 in L^2(|x|^{-2(a-2)}), so
these two subtractions cover exactly 5/2 < a < 9/2 (1D model; added 02:13Z).

## 6. Regularity bookkeeping for a nonlinear closure (DERIVED, frozen necessary conditions)

For an H^s-type energy (principal symbol |xi|^{2s}), the transport commutator contributes s nu^T DV nu, so the
pointwise symbol margin is
    m_s(X, nu) = kappa_w(X) - [ s nu^T S(DV(X)) nu + p(X, nu) ],  S = symmetric part,
and the condition is sup_nu < kappa_w - delta. At P this is exactly the frozen source condition (verified):
max(sA - g, s mu) < b_0, i.e. s < 2373/680 ~ 3.49 on the certified coefficient box. At 0 the isotropic version fails
for every s > 0.31 (sup_nu nu^T DV nu = D); conormal derivatives (x d_x, y d_y) commute with T_0 and cost nothing.
Ordinary y-derivatives at the corner cost s D: on the x-axis near 0 the margin is b_0 + aA - (b + s) D, so H^s in y with
the weight |y|^{-2b} needs s + b < (b_0 + aA)/D (< 2.453 for a < 9/2). At infinity, scaled derivatives r grad cost
nothing. A sufficient condition for the nonlinear term: W[h] Lipschitz (necessity not claimed, V038), i.e. Riesz^2(d_x h) in L^infinity because DU[h] = Riesz^2(d_x h)
(S2_CALPHA_THEORY.md). d_x h in C^alpha (with decay) is sufficient; it is not necessary (the first version claimed
equivalence; V025 REFUTED it with a compact parity-compatible C^1 counterexample with zero center jets); and only conormal derivatives across the axes, because W_1 = 0 on
{x = 0} and W_2 = 0 on {y = 0}, so W.grad h = (W_1/x)(x h_x) + (W_2/y)(y h_y). In the weight of section 5 the x-axis
factor b(t) is switched off away from 0, so across the x-axis away from 0 ordinary H^s regularity in y is needed;
an H^{2 + eps} theory therefore requires s in (2, 2.45) near the corner (with a in ((2D - b_0)/A, 9/2) = (3.55, 4.5))
and s < 3.49 at P. These windows are nonempty; whether they are sufficient is OPEN.

## 7. Audit of the earlier obstructions (status for the present spaces)

| Obstruction (earlier record) | Applies to | Status here |
|---|---|---|
| Degree-2 center quasimodes X/X_m (verified) | diagnostic norm with r^{-6} weight | evaded by a > 5/2 (not in R_w); no approximate kernel (Theorem O(d)) |
| Negative potential energy at the saddle (verified) | energy pairing with Phi | applies to the energy method; not to the transport-weighted estimate |
| B_F and Y_(a,s) quasimodes with a >= 5/2 need jets | conic weights without jets | consistent with N1 to N3: the y-axis jet is a required coordinate |
| J nonclosed in weak norms (verified, also at fixed c) | norms without a jet coordinate | evaded: J is a coordinate of Z_0 and Z |
| Radial local moment gap (verified) | radial gap estimates | applies: no radial argument; the domain is anisotropic (N1) |
| No constant weight: b_+ > b_0 somewhere (new, numerical) | constant or slowly varying weights | applies; avoided by the radial Lyapunov factor (section 3, 5) |
| Transport inverses below about a = 3.55 for conic weights | conic weights with this far exponent | consistent with section 6 (two y-derivatives at the corner need a > 3.55) |
| Straight homotopy cannot transport the index for b_0/A < s < s_fast | that weighted family | not used: homotopy here is in the coupling strength at fixed weight |
| Source jet transport not onto (mu_P = 1) | axis-jet transport alone | applies to transport alone; the coupling g is what restores the source inverse (verified frozen source theorem) |
| Small finite-section residuals are not inverse bounds | all finite sections | applies; the complement must be controlled by an estimate such as Theorem R |

## 8. Open items (precise)

1. Lemma (E) of section 5 with proof: Taylor-subtracted weighted velocity bounds beyond A_2 along the y-axis and at 0,
   the edge Garding inequality with the b_+ bound, and compactness of the y-axis trace couplings.
2. Certification of the margins (H_m) / (H_m') with interval arithmetic on all of R^2.
3. Injectivity of L (or L_fix) on the chosen space; with Theorem R or C it is equivalent to invertibility. A
   computer-assisted route: the estimate (m_* - eps)||h|| <= ||L h|| + ||K h|| with K approximated by finite rank
   reduces injectivity to a finite-dimensional check, which is exactly the complement control a finite section lacks.
4. The H^s or C^{1,alpha} version (section 6) and the nonlinear estimate in the same space.

## 9. Verification status

- Theorem O: CONFIRMED (V022) for (a), (b), (d); (c) CONFIRMED as the bounded integral extension; the pointwise reading
  of (c) REFUTED.
- Proposition N1: CONFIRMED with a >= 5/2 (endpoint allowed); "strictly" REFUTED (V025). Proposition N2: CONFIRMED
  conditional on the positive axis rate (V025). Corollary N3: CONFIRMED in the corrected full-L form (V025).
  Proposition N4: CONFIRMED, with the residual threshold needing a nonzero leading coefficient (V025). Remark N5:
  corrected statement CONFIRMED, literal o(r^k) version REFUTED (V025).
- Lemmas G1 to G3, Theorem R: CONFIRMED under the exact hypotheses listed in section 3 (V023), with the Lemma G2
  square-root step replaced. V031 extends Theorem R to Lipschitz mu with Lip(mu) < 2, including mu~. V032 confirms
  Remark R.2 (c not closable on D_w). The global margin (H_m), injectivity, the strain column and the transfer to the
  jet space remain OPEN.
- Section 5 compensation formula: CONFIRMED with c[h_0] (V025). Section 6 Lipschitz equivalence: REFUTED (V025),
  corrected to a sufficient condition.
- Sections 4 to 6 otherwise: DERIVED sketches; not submitted as theorems. Lemma (E): the verifier is proving a local
  vertical-axis piece (note of 02:04Z); the global product-weight and corner versions are OPEN.
