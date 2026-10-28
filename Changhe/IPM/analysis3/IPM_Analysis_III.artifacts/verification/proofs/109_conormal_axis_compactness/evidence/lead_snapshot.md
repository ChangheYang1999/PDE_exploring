# S2_L2_THEORY.md: weighted L^2 theory for the linearized S2 operator (Avenue I)

First version 2026-10-28T01:44Z (theory author); revised 2026-10-28T02:09Z for the verdicts V022 to V025, 02:41Z (single-knot weight in section 5), 02:45Z (V031, V032) 03:24Z (V041, V042; section 5.2 rewritten as Theorem C' on fully specified spaces) 03:33Z (V043 to V046) 04:10Z (V047 to V054: Theorem C' a conditional theorem, its coupling hypotheses proved for the modal background) and 04:46Z (V055 to V061; section 6 rewritten: Prop F4, the corner singularity, and the variable-order high space) and 04:55Z (V062 to V064: Lemma H1 conditional theorem, sharp source threshold, moving-tail iteration) and 05:17Z (V065, V067: cone-local 06:40Z (V088 to V091: principal joint symbol margins, the geometric radius 1e-5, the non-implications) and 06:54Z (Lemma H-spec in 6.6, DERIVED) and 07:01Z (Lemma H-spec restated for the remainder block, Corollary H-spec for L_red with the jet row split off; the jet row cannot be shifted) and 07:16Z (V106: Lemma H-spec CONFIRMED as an abstract theorem, REFUTED in the direct free-J form; remark (6) on (J1), (J2)) and 07:04Z (V088 to V105 in the verdict list; V103, V104 in 6.6 (e)).
high space, Prop F4 confirmed for the frozen operator with the parity correction; Lemma Z added) 05:26Z (box certificates of the margins and of (A), computed once; high order below 13/2) and 05:33Z (V069 to V072: knot threshold, source rectangle, Lemma Z confirmed, production aggregation verified; outward-rounded decimals) and 05:44Z (V073 to V076: fractional order 25/4 for the mapping side, Theorem H restated in inverse-regularity form, residual membership in the fractional target) and 05:52Z (V077 to V080: Theorems R and C' unconditional for the actual
background, global (Z) confirmed, cylinder corner threshold and revised high-space parameters delta = 9/5, s = 41/20) and 06:15Z (V081 to V087: margins at least 5/2, zeta in the high target, no derivative gain of the full coupling, J kept free). Labels: THEOREM (verifier-confirmed), DERIVED (proof written here, awaiting
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
- A box certificate of (H_m) for mu~ with the exact modal trial in ball arithmetic (1569 radial cells times 64
  angular boxes, every cell computed, no negative box) gives m_* >= 1.029821 (numerics team; the accompanying S2_NUMERICAL_CERTIFICATES.md).
  V072 verified complete coverage, retention of every refined array and the directed aggregation, reproducing the
  exact dyadic minimum 1.0298211720474706, conditional on the exported cell enclosures; the verifier's recomputation of
  the cell enclosures from the original data was done separately (next item).
- Independent certificate (THEOREM, V077). The verifier rebuilt all 1558 spline spans and 261 stream modes from the
  original data (512-bit Green moments, 3276 radial cells times 128 angular cells, the exact outer continuation, both
  infinite ends bounded analytically; a separate 640-bit audit) without using the numerics team's code, and obtained
  m_R >= 1.78605 for this weight mu~ (raised to m_R >= 5/2 by its refinement, V086). So (H_m) holds and Theorem R is a THEOREM for L_fix and the actual normalized
  modal background: L_fix : D_w -> L^2_P(e^{mu~}) is Fredholm of index 0 (complete statement with spaces in the
  verifier's proof 76). Injectivity is not addressed.

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

## 5. A jet-compatible global weight and the consistent domain (5.2: Lemmas C'1 to C'4 and Theorem C' THEOREM as conditional statements, V046, V047; the coupling hypotheses (E0), (E-J), (E-G) THEOREM for the modal background, V049 to V053; so Theorem C' holds for the modal background under (A) and (H_m') alone; both are CONFIRMED by V077, so Theorem C' is a THEOREM for the actual normalized modal background)

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

5.2 The fully specified spaces (definitions; V041 and V042 for the scalar and target parts). All functions have the IPM
parity (even in x, odd in y); t = log r; a = 17/4; w := w_a as above.
- R := L^2_P(w dX).
- G: the scalar space with ||gamma||_G^2 = int_{t<0} |gamma|^2 e^{-t/2} dt + int_{t>0} |gamma|^2 e^{27t/4} dt. These are
  the exponents 8 - 2a and 8 - 5/4: e^{8t + mu_a(t)} is exactly the radial factor of |x^2 y|^2 w r^2.
- Jet lift: E gamma := x^2 y gamma(log r).
- Target: Y := E G (+) R with the sum of the squared norms. The sum is direct because |cos theta|^{4 - 2a} is not
  integrable (V042).
- Axis data: d(t) := V_2(0, e^t)/e^t, D = 4 c_l - 1, H and the scalar space B (beta = H z, z' in L^2(omega),
  z(+inf) = 0, sigma = 1/4, kappa = 3/8 + k) and the scalar target Gamma as in V041. J(beta) := lim_{t -> -inf} beta(t)
  is the cubic coefficient. Hypothesis (A): d satisfies d_min <= d <= d_max, |d - D| + |d'| <= C e^{2t} for t <= 0 and
  |d - c_l| + |d'| <= C e^{-(1-k)t} for t >= 0. The endpoint orders are those of the modal field (V041); positivity of
  d on the whole axis and the constants are numerical obligations. The box certificate (aggregation verified,
  V072, conditional on the exported cell enclosures) gives d in [5.575203, 21.301451], sup_{t<=0} |d - D| e^{-2t} <= 0.100883, sup_{t<=0} |d'| e^{-2t} <= 0.202073,
  sup_{t>=0} |d - c_l| e^{(1-k)t} <= 89.3342 and sup_{t>=0} |d'| e^{(1-k)t} <= 73.3113. Under (A), Gamma = G with
  equivalent norms (V041).
- T := V.grad - 1 in distributions on R^2 \ {0}; D_R := {h in R : T h in R} with the graph norm.
- Domain: Z := E B (+) D_R with ||E beta + h_R||_Z^2 := ||beta||_B^2 + ||h_R||_R^2 + ||T h_R||_R^2. The sum is direct for
  the same reason as for Y.
This replaces the phrase "a weighted 1D space adapted to the jet row" of the first version, which did not define a
Banach space (V041).

Lemma C'1 (the transport of the lift; the identity and the bound THEOREM under the coefficient bounds (CB) below, V046;
(CB), called (L) in V047, holds for the modal background with finite constants, V047). Put q := V.X/r^2 and p := 2 V_1/x + V_2/y - 1. Both are even in x and
in y, so a_1 := (q - q(r, pi/2))/cos^2(theta) and a_0 := (p - p(r, pi/2))/cos^2(theta) are bounded on every annulus.
For the modal background, a_1 is bounded on R^2 \ {0} and a~_0(t) := sup_theta |a_0(e^t, theta)| <= C min(e^{2t}, 1).
For beta in B,
     T(E beta) = E(A beta) + Err beta,    Err beta := x^2 y cos^2(theta) [a_1 beta'(t) + a_0 beta(t)],
where A beta = d beta' + (D - d - 2 d') beta is the axis row of V041, and
     ||Err beta||_R <= I_a^{1/2} ( ||a_1||_inf ||beta'||_G + ||a~_0 beta||_G ) <= C_E ||beta||_B,
     I_a := int_0^{2 pi} |cos theta|^{8 - 2a} sin^2(theta) dtheta = 2 Gamma(1/4) Gamma(3/2)/Gamma(7/4) = 6.99215... (a = 17/4).
Proof.
- V.grad(x^2 y) = x^2 y (2 V_1/x + V_2/y) and V.grad beta(log r) = q beta'. So T(E beta) = x^2 y [q beta' + p beta].
- On the y-axis q = d and p = 2 d_x V_1(0, y) + d - 1 = D - d - 2d', because d_x V_1 + d_y V_2 = 2 c_l and
  d_y V_2(0, y) = d + d' (V041). This gives the identity.
- Bounds on a_1, a_0. V_1/x, V_2/y and q are smooth and even in x on each annulus (finite angular Fourier sums), so
  their difference from the axis value is O(cos^2 theta) with the second angular derivative as constant (the argument of
  V042 (7)). Near 0, V = (-A x, D y) + V^(3) + O(r^5 |log r|) with V^(3) = (x (al x^2 + be y^2), y (ga x^2 + de y^2))
  (V042), so q - q_axis = -(A + D) cos^2(theta) + O(r^2 cos^2 theta) and p - p_axis = (2 al + ga - 2 be - de) x^2 +
  O(r^4) = O(r^2 cos^2 theta), since the constant term -2A + D - 1 of p vanishes. At infinity V - c_l X = O(r^k) with its
  angular derivatives, so a_1, a_0 = O(r^{k-1}).
- Norm. |x^2 y cos^2 theta|^2 w r^2 = e^{8t + mu_a(t)} |cos theta|^{8 - 2a} sin^2 theta, and e^{8t + mu_a(t)} is the
  G weight. For beta = H z: beta' = H (z' - p_1 z), p_1 = (D - d - 2d')/d = O(e^{2t}) at -inf and bounded at +inf.
  For t < 0 the G weight is omega (sigma = 1/4), H is bounded and z is bounded by |J| + (2 sigma)^{-1/2} ||z'||_omega,
  and a~_0 = O(e^{2t}); for t > 0, H^2 e^{27t/4} <= C e^{2 kappa t} = C omega because kappa = 27/8 - (3 - k), and
  ||z||_{omega, t>0} <= kappa^{-1} ||z'||_omega (V041 Hardy bound). So both terms are bounded by C ||beta||_B. QED.
The constant C_E is explicit in sup |a_1|, the e^{-2t} sup of a~_0 and the constants of (A). It is a box enclosure of
the same kind as the margin certificate. V046 states the hypothesis on the whole field as
 (CB) |q - d(log r)| <= M_Q cos^2(theta) and |p - p_axis(log r)| <= M_P min(r^2, 1) cos^2(theta) at every off-axis point,
that is, M_Q = sup |a_1| and M_P = sup min(r^2, 1)^{-1} |a_0|, and confirms ||Err beta||_R <= I_a^{1/2} (M_P ||min(e^{2t}, 1) beta||_G
+ M_Q ||beta'||_G). V047 confirms that the modal field satisfies (CB) (its (L)) with finite constants, by the argument above; the sizes of
M_Q and M_P are not computed. They are not needed for the Fredholm statement, only for an inverse bound.

Lemma C'2 (the remainder transport; THEOREM, V046, for kappa_* > 0 and kappa_w bounded). Let kappa_w := 1 + c_l + (1/2) V.grad log w, defined a.e.
(at the knot r = 1 both slopes of mu_a are admissible), and kappa_* := ess inf kappa_w. If kappa_* > 0, then
T_R := T restricted to D_R is a bijection D_R -> R, with
     ||T_R^{-1}||_{R -> R} <= 1/kappa_*,   T_R^{-1} f = - int_0^inf e^{-s} f(Phi_s(X)) ds,
where Phi_s is the flow of V. Smooth functions with compact support in R^2 \ ({0} cup {x = 0}) are dense in D_R, and
Re <T h, h>_w = - int kappa_w |h|^2 w for h in D_R.
Proof.
- V is C^1 on R^2 \ {0}, tangent to both axes, and |V| <= C r at 0 and at infinity, so Phi_s is global on R^2 \ {0}
  and preserves the parity class and the axes.
- Change of variables: ||f o Phi_s||_w^2 = int |f|^2 exp(- int_0^s (div V + V.grad log w)(Phi_{-tau} Y) dtau) w dY
  <= e^{-2 s (kappa_* - 1)} ||f||_w^2, since div V = 2 c_l. Hence the integral formula converges in R with norm at most
  ||f||/kappa_*, and differentiating along the flow gives T(T_R^{-1} f) = f in distributions.
- Density. With an angular cutoff psi(cos theta/eps), V.grad psi = psi'(.) (-sin theta)(V.grad theta)/eps and
  V.grad theta = cos(theta) V_2/r - sin(theta) cos(theta) V_1/x = O(cos theta), so (V.grad psi) h -> 0 in R by dominated
  convergence. Radial cutoffs at 0 and infinity are handled the same way, since V.X/r^2 is bounded. Friedrichs
  mollification on compact sets away from the axis and 0 completes the density. w is Lipschitz there.
- For smooth compactly supported h, Re int (V.grad h) h w = -(1/2) int |h|^2 (div V + V.grad log w) w, which gives the
  energy identity, and it extends to D_R by density. It gives ||T h|| >= kappa_* ||h||, hence injectivity. QED.
The angular part of V.grad log w is 2a tan(theta) V.grad(theta) = 2a (sin(theta) V_2/r - sin^2(theta) V_1/x), which is
bounded. So kappa_w is the multiplier m_a + b_+ of the margin certificate.

Lemma C'3 (transport on Z; THEOREM as a conditional statement, V046). Assume (A), (CB) and kappa_* > 0. Then T maps Z into Y,
     T(E beta + h_R) = E(A beta) + (Err beta + T h_R),
and T : Z -> Y is bijective with inverse E gamma + F -> E A^{-1} gamma + T_R^{-1}(F - Err A^{-1} gamma). The inverse norm is
bounded by ||A^{-1}||_{Gamma -> B} (V041 (7)), C_E and 1/kappa_*. The cubic coefficient of the solution is the output
J = - int gamma/(d H) dt (V041 (6)).
Proof. Lemma C'1 and Lemma C'2; the operator is block lower-triangular with invertible diagonal blocks. QED.
V046 adds: J is continuous on Z, and restricting to J = 0 leaves a closed range of codimension one whose condition is
the scalar compatibility integral of V041. The off-diagonal block Err need not be compact (it is not compact at 0);
the triangular inversion uses only its boundedness. For the full normalized operator L_red of Theorem C' the
restriction to ker J is Fredholm of index -1 (THEOREM, V087), so the inverse is sought with J free and the solution
is normalized at the end by rho_norm(X) = lambda rho_*(X/lambda), lambda = (1 + j)^{1/2} for cubic coefficient 1 + j > 0
(same speed and far exponent; far angular profile multiplied by (1 + j)^{(1 - q)/2}; V087).

Lemma C'4 (the strain functional on Z; THEOREM, V047). For h = E beta + h_R in Z,
     c[h] = (1/4) int e^{2t} beta(t) dt + (1/pi) int sin(3 theta) r^{-3} h_R dX,
both absolutely convergent (S3.2 of CONVENTIONS; int_0^{2pi} sin(3 theta) cos^2(theta) sin(theta) dtheta = pi/4), and
|c[h]| <= C_c ||h||_Z. The second term is bounded by c_R ||h_R||_R with
     c_R = (1/pi) (int_0^{2pi} |cos theta|^{2a} sin^2(3 theta) dtheta)^{1/2} (2/9 + 4/11)^{1/2}
         = 0.2075698661066814348070539594... < 0.207570 (a = 17/4; sharp for this Cauchy-Schwarz step, V047 at 384/768 bits),
by Cauchy-Schwarz (the radial integrals int e^{(2a-4)t} over t < 0 and int e^{-11t/4} over t > 0). The first is bounded
by C ||beta||_B because beta is bounded at -inf and beta = o(e^{-(3 + 3/8)t}) at +inf. QED.

Coupling and the precise hypothesis (E). On Z put
     C h := [U[h] + chi_0 (c[h]/3) X].grad rho~,   so that   L_ren = T + C
(the renormalized coupling of Prop B, accompanying S2_C_FUNCTIONAL.md 7.2). Near 0 the strain part cancels the linear
part c[h](-x, y) of U[h] against x^2 y, so C h has no constant cubic jet. When C h is in Y, write C h = E gamma_C[h] + C_R h.
 (E0) C maps Z boundedly into Y.
 (E-J) The jet part h -> gamma_C[h] is compact from Z to G. On the axis gamma_C[h] = [2 d_x U_1[h](0, y) rho_2(y)
       + U_2[h](0, y) rho_2'(y)]/y + (strain terms), so this is the trace statement of the first version.
 (E-G) C_R restricted to D_R extends to a bounded operator on R, and for every eps > 0 there is a compact operator
       K_eps on R with Re <C_R h, h>_w <= int (b_+ + eps) |h|^2 w + Re <K_eps h, h>_w for h in D_R,
       where b_+ = (|grad rho~| - d_y rho~)/2 >= 0.
(E0) contains the jet-input coupling beta -> C_R(E beta), B -> R, and the cross-region coupling (input outside a strip,
output inside it; (E3) of S2_C_FUNCTIONAL.md 6). The local strip piece of (E-G) and (E-J) is V026.
Status of (E0), (E-J), (E-G) (THEOREMS for the modal background; V049 to V053). The background hypotheses are explicit:
(B1) the angular and radial cofactor bounds (b - 1 and b_t, with three angular derivatives, O(r^2) at 0, and b, b_t
O(r^{k-3}) at infinity, for rho~ = x^2 y b), and (B2) a uniform C^5 bound for rho~(r_0 X)/d(r_0) on 1/32 <= |X| <= 32
for every r_0 > 0, with d(r_0) = r_0^3 (r_0 <= 1) and r_0^k (r_0 >= 1). V053 verifies (B1), (B2) and the axis-density
assumptions for the exact normalized modal density from the original data (exact recomputation of all 3640 C^6 join
equations of the 260 modes, the scalar repair identities, the outer exponents and the logarithmic gaps).
- (E-J), V049 (under (A)). With alpha(t) := rho_2(e^t) e^{-t} and T_h(y) := U_2[h](0, y), the axis row is
  Gamma h = (alpha + alpha') T_h/y - 2 alpha T_h' + c[h] chi_0 (alpha + alpha'/3), and Gamma : E B (+) R -> G is
  Hilbert-Schmidt. Near 0, T_h - c[h] y = O(y^3) because for a > 4 the third derivative of the trace is a bounded
  functional on R; at infinity the functional norms satisfy ||T_h^{(j)}(y)||_{R*} <= F_j y^{eta/2 - 1 - j}.
  The Hilbert-Schmidt criterion used is sum_n ||Gamma e_n||^2 = int ||Gamma_t||^2_{R*} g dt.
- (E0), jet inputs, V050: beta -> C(E beta) is Hilbert-Schmidt from B to Y.
- (E0), remainder inputs, V051: D h := U[h].grad rho~ - x^2 y gamma_U[h](log r), with the radial lift
  gamma_U[h] = (alpha + alpha') T_h(r)/r - 2 alpha T_h'(r), is bounded on R; D = D_near + D_far with D_far
  Hilbert-Schmidt (separated scales) and ||1_{2^j <= r < 2^{j+1}} D_near h|| <= C min(2^{2j}, 2^{(k-1)j})
  ||1_{2^{j-3} < r < 2^{j+3}} h||. Outer sources at 0 need the exact linear-strain cancellation and a > 4. C_R - D is
  bounded of rank one.
- (E-G), V052: for every eps > 0 there is a compact self-adjoint K_eps with
  Re <C_R h, h> <= int (b_+ + eps)|h|^2 w + <K_eps h, h> on R. Steps: operator-norm smallness of the output tails at 0
  and infinity (from (2) of V051, and for the compact part by strong convergence of the output indicators); smallness
  of the output on |x| < delta on a fixed annulus (strip input |x| < eps_0 by V026, O(eps_0); the radial-versus-vertical
  lift O(delta^{1/4}); separated input O(x^4), hence O(delta^{1/4}) with a constant depending on eps_0; delta -> 0
  before eps_0 -> 0); on the remaining compact set, compact weight conjugation (Lipschitz extension of w^{1/2}) and
  the exact quadratic form g_1 Re(R_2 h conj(R_1 h)) - g_2 |R_1 h|^2 of g_1 U_1 + g_2 U_2 modulo compact commutators,
  bounded by ((g_1^2 + g_2^2)^{1/2} - g_2)/2 times |R_1 h|^2 + |R_2 h|^2; commuting the coefficient back gives
  b_+ |h|^2 modulo compact. No weighted singular-integral theorem for the non-A_2 angular weight is used.
All constants are finite and not computed. An independent consultation (not a verification record) also derived
Schur-test bounds for the Taylor-subtracted kernels in |x|^{-2a'} with the windows (3/2, 7/2) and (1/2, 5/2), and
dyadic bounds in |cos theta|^{-2a'} r^{2b} for -2 < b < 2, and noted that the individual global traces fail to be
bounded for a >= 2, so only the combined remainders extend (accompanying file of the consultation B2_weights).
Proved piece of (E0) (THEOREM, V045). For input supported in |x| > 2R and output restricted to |x| < R, |y| < Y, the
Taylor-subtracted coupling (the full x^2 axis coupling removed) is compact in the weight w_a, 0 < a < 9/2, far exponent
eta < 2 (so a = 17/4, eta = 5/4 is covered): its kernel is at most x^4 times a combination of delta^{-2}, ..., delta^{-5}
in the separation delta, it is weighted Hilbert-Schmidt, and its trace has every fixed number of local y derivatives.
Adjacent input, limits uniform as R -> 0 or Y -> infinity, and jet inputs are not covered.
Why the strain term must sit inside C (THEOREM, V044). L_fix := T + U[.].grad rho~ does not map Z into Y. For
h = x^4 y eta_0(r) with eta_0 >= 0 supported in 2 < r < 3, h is in R with J = 0 and c[h] = (3/16) int r^3 eta_0 dr > 0,
but L_fix h = -c[h] x^2 y + O(r^5) near 0, and a constant axis factor is not in G. H_0 is not in Y either. So
c[.] H_0 is not a bounded rank-one perturbation into Y, and Theorem C' cannot be obtained from the L_fix theory of
section 3 by adding it. With the strain term in C, the image of this h is in Y (V044).

Theorem C' (THEOREM as a conditional statement, V047, on (A), (CB), (E0), (E-J), (E-G) and (H_m'); for the modal background (CB), (E0), (E-J) and (E-G) are THEOREMS, V047, V049 to V053, and (A) and (H_m') are CONFIRMED by an independent original-data computation, V077: d >= 5.5752 on the whole axis, m_a >= 0.53072. So Theorem C' is a THEOREM for the actual normalized modal background). Let (H_m') be m_a := ess inf (kappa_w - b_+) > 0
for w = w_a. Then:
(i) L_ren = T + C : Z -> Y is Fredholm of index 0.
(ii) The bordered operator of Prop B, L_red := L_ren + c[.] zeta, is Fredholm of index 0 from Z to Y, provided
     zeta := (c_l g_far - k y_KP)/d lies in Y. So L_red is invertible if and only if it is injective.
(iii) For each eps in (0, m_a), (m_a - eps) ||h_R||_R <= ||P_R L_ren h_R|| + ||K_eps h_R|| on D_R, where P_R is the
     projection of Y onto R.
Proof.
1. Block form. For h = E beta + h_R, L_ren h = E(A beta + gamma_C[h]) + (Err beta + C_R E beta + (T + C_R) h_R). So
   L_ren = M + K_1 with K_1 h := E gamma_C[h], compact by (E-J), and M the block lower-triangular operator with
   diagonal blocks A : B -> Gamma and S_1 := T_R + C_R : D_R -> R, and off-diagonal block X := Err + C_R E : B -> R,
   bounded by Lemma C'1 and (E0).
2. The remainder block. Put S_s := T_R + s C_R, 0 <= s <= 1. By Lemma C'2 and (E-G), using b_+ >= 0,
   Re <-S_s h, h>_w >= int (kappa_w - s b_+ - s eps) |h|^2 w - s Re <K_eps h, h>_w >= (m_a - eps) ||h||^2 - ||K_eps h|| ||h||.
   So (m_a - eps) ||h|| <= ||S_s h|| + ||K_eps h||. The graph norm of D_R is controlled by ||h|| + ||S_s h|| + ||C_R|| ||h||,
   and K_eps composed with the bounded inclusion D_R -> R is compact. Hence every S_s is upper semi-Fredholm. The path
   s -> S_s is norm continuous from D_R to R, so its index is constant (stability of the semi-Fredholm index), and S_0 =
   T_R is bijective by Lemma C'2. Hence S_1 is Fredholm of index 0. This is (iii) at s = 1.
3. Triangular factorization. M = [[1, 0], [X A^{-1}, 1]] [[A, 0], [0, S_1]] with respect to Y = E Gamma (+) R and
   Z = E B (+) D_R. The first factor is an isomorphism of Y and A is an isomorphism (V041). So M is Fredholm of index 0.
4. L_ren = M + K_1 with K_1 compact, so (i) holds. c is bounded on Z (Lemma C'4), so c[.] zeta is a bounded rank-one
   operator when zeta is in Y, and (ii) follows. QED.
Membership of zeta in Y (DERIVED, by the argument of V042). g_far = (1 - chi_0) G_bar - k Phi_hat vanishes near 0; near 0
y_KP is [U[KP] + c[KP] X/3].grad rho~ = x^2 y O(r^2), because the linear part of U[KP] is c[KP](-x, y); at infinity
both are O(r^{2k-1} log r) with the factor x^2 y and an even-in-x cofactor, so the axis subtraction of V042 applies and
4k - 5/4 < 0 gives the radial integrability, the logarithms being harmless.

What Theorem C' settles and what it does not.
- Lemmas C'1 to C'4 and Theorem C' are THEOREM as conditional statements (V046, V047). V047 checked step 2 directly:
  the whole fixed-domain path is upper semi-Fredholm and starts at an isomorphism, so no adjoint estimate is needed, and
  the lower off-diagonal block need only be bounded. zeta is in Y by the verified residual endpoint orders (V047).
- It answers V041's list as follows. The lifting is E with its transport error (Lemma C'1). The jet-input coupling and the
  cross-region coupling are in (E0). The remainder domain is the maximal domain D_R, with density and the energy
  identity (Lemma C'2); no adjoint is needed, because the index is computed by the homotopy of step 2 and the triangular
  factorization of step 3. The normalization enters through Lemma C'4 and the rank-one term of Prop B.
- (E0), (E-J) and (E-G) are THEOREMS for the modal background (V049 to V053, qualitative constants). They are the
  analytic content of (E1) to (E4).
- (A) and (H_m') are certification obligations: (A) is a box enclosure of V_2(0, y)/y and its derivative along the axis
  with the endpoint expansions; (H_m') is the anisotropic margin of the numerics team, which is global only if no box
  returns a nonfinite value (V037). The first script for (A) was audited in V054 (coverage and underflow steps REFUTED;
  near-resonant inner Green correction in mode 27). The repaired computation (range method CONFIRMED, V061, V068)
  gives, once, m_a >= 0.965918, kappa_* >= 3.037693, the (A) constants above and the (CB) constants M_Q <= 337.66,
  M_P <= 1075.52. V072 verified the coverage and the directed aggregation of this run (the exact minima 0.9659182260060386
  for m_a and 5.575203976688894 for d are reproduced), conditional on the exported cell enclosures. The verifier's own
  original-data computation (V077, independent code, 640-bit audit) gives d >= 5.5752 and m_a >= 0.53072 (raised to
  m_a >= 5/2 by its refinement, V086), which closes
  (A) (with the qualitative endpoint estimates of V055) and (H_m'). The sharper one-team values m_a >= 0.965918,
  kappa_* >= 3.037693 and the quantitative d', M_Q, M_P constants keep their one-team status; the verifier's own finite
  cells give kappa >= 1.6377 if a verified kappa_* is needed.
- Injectivity of L_red is not addressed. With injectivity, a quantitative inverse bound needs Lemma IV.1 of the
  accompanying S2_BASIS_CERTIFICATION.md on the Hilbert space Y with the jet rows included (V040).

5.3 Heuristics for (E) and the Mellin windows (motivation only; the proofs are V049 to V052).
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

## 6. The high-order space: thresholds, the corner singularity and the variable-order structure (6.1 DERIVED frozen conditions; 6.2 Proposition F4 THEOREM for the frozen operator, V067; 6.3 Lemma H1 THEOREM under (Z), V063, Lemma Z THEOREM, V071, and (Z) CONFIRMED for the actual field, V080; 6.5 cylinder corner threshold THEOREM for the frozen operator, V079; 6.4 to 6.7 otherwise DERIVED, not theorems)

6.1 Frozen necessary conditions. For an H^s-type energy (principal symbol |xi|^{2s}), the transport commutator
contributes s nu^T DV nu, so the pointwise symbol margin is
    m_s(X, nu) = kappa_w(X) - [ s nu^T S(DV(X)) nu + p(X, nu) ],  S = symmetric part,
and the condition is sup_nu < kappa_w - delta. The commutator symbol and the coupling symbol p must be maximized
jointly over nu; the decoupled bound b_+ + s lambda_max(S(DV)) fails at P. At P the joint condition is exactly the
frozen source condition (verified): max(sA - g, s mu) < b_0, i.e. s < 2373/680 ~ 3.49 uniformly on the certified
coefficient box (V011); at the actual source the threshold is s_fast = (b_0 + g)/A_P = 3.5785..., and it is sharp
(V064: a fixed smooth forcing has no H^s solution for s >= s_fast).
At 0 the isotropic version fails for every s > 0.31 (sup_nu nu^T DV nu = D); conormal derivatives (x d_x, y d_y)
commute with T_0 and cost nothing. Ordinary y-derivatives at the corner cost s D: on the x-axis near 0 the margin is
b_0 + aA - (b + s) D, so H^s in y with the weight |y|^{-2b} needs s + b < (b_0 + aA)/D (2.334 for a = 17/4, 2.453 for
a = 9/2). At infinity, scaled derivatives r grad cost nothing. A sufficient condition for the nonlinear term: W[h]
Lipschitz (necessity not claimed, V038), i.e. Riesz^2(d_x h) in L^infinity because DU[h] = Riesz^2(d_x h)
(S2_CALPHA_THEORY.md). d_x h in C^alpha (with decay) is sufficient; it is not necessary (the first version claimed
equivalence; V025 REFUTED it with a compact parity-compatible C^1 counterexample with zero center jets). Across the axes
only conormal derivatives enter the product, because W_1 = 0 on {x = 0} and W_2 = 0 on {y = 0}, so
W.grad h = (W_1/x)(x h_x) + (W_2/y)(y h_y). In the weight of section 5 the x-axis factor is switched off away from 0,
so across the x-axis away from 0 ordinary regularity in y is needed.

6.2 Proposition F4 (the frozen corner singularity; called H0 in V067 and in earlier versions of this file, and
unrelated to Proposition H0 of S2_CALPHA_THEORY.md; THEOREM, V067, for the frozen formula, the endpoint obstruction and the
exclusion of the old high spaces as ranges of the frozen inverse; the parity statement of the first version of (b), (c) was REFUTED
and is corrected below; the transfer to the true operator is OPEN). Let
L_00 h = -A x h_x + D y h_y - h on R^2. Let psi in C_c^infinity(R) be odd, supported in 1/2 <= |y| <= 2, with psi >= 0
and psi not identically 0 on (0, infinity); let chi in C_c^infinity(R) be even with chi = 1 on [-1, 1]; put
f(x, y) = x^4 chi(x) psi(y). Then f is smooth with compact support, even in x, odd in y and in L^2(w_a), and the
solution
    h(x, y) = - int_0^infinity e^{-s} f(x e^{-A s}, y e^{D s}) ds
of L_00 h = f (the unique solution in L^2(w_a): for the frozen field kappa_{w_a} >= 1 + c_l + 5A/8 > 0) satisfies,
wherever 0 < |y| < 1/2 and |x| (2|y|)^{A/D} <= 1,
    h(x, y) = - C x^4 sgn(y) |y|^beta,   beta = (1 + 4A)/D = 2 - 1/D = 1.95305...,   C = D^{-1} int_0^infinity u^{-beta-1} psi(u) du > 0.
Proof. For |y| < 1/2 only s >= log(1/(2|y|))/D contributes, and there |x e^{-A s}| <= |x| (2|y|)^{A/D} <= 1, so
chi = 1. Substitute u = |y| e^{D s}: e^{-(1 + 4A) s} = (|y|/u)^beta, ds = du/(D u), and psi(sgn(y) u) = sgn(y) psi(u).
The identity 1 + 4A = 2D - 1 gives beta = 2 - 1/D. QED. (Quadrature check, NUMERICAL: the accompanying
corner_counterexample.py reproduces the formula to 1e-15 relative at four points.)
Consequences.
(a) h is C^{1, 1-1/D} across the x-axis, but h is not in H^s on any neighbourhood of a point (x_0, 0), 0 < |x_0| <= 1,
    for s >= 5/2 - 1/D = 2.4531, and the cofactor h/(x^2 y) = -C x^2 |y|^{beta - 1} is not in H^sigma in theta for
    sigma >= 3/2 - 1/D = 1.4531. So no bounded inverse of L_00 from a target containing such f maps into a space that
    requires more regularity across the x-axis.
(b) The general exponent is beta_m = (1 + m A)/D for a source term |x|^m psi(y), and the ordinary threshold across the
    x-axis is beta_m + 1/2 = (1 + mA)/D + 1/2. For data that are smooth across the y-axis (so that, in L^2(w_a), the
    expansion in x starts with the jet x^2 and continues with x^4) m = 2 gives beta_2 = 1, the smooth jet x^2 y (since
    1 + 2A = D), and m = 4 is the next term, admitted by L^2(w_a) when a < 9/2 (x^m is in L^2(|x|^{-2a}) near x = 0
    iff m > a - 1/2). Parity alone does not give this: |x|^m chi(x) psi(y) with a - 1/2 < m < 4 is even in x, lies in
    L^2(w_a), and gives the threshold (1 + mA)/D + 1/2 < 5/2 - 1/D (V067, REFUTED the parity-only reading of the first
    version).
(c) The L^2-energy threshold of 6.1 is exactly (b_0 + aA)/D = (1 + (a - 1/2) A)/D + 1/2, the limit of the thresholds of
    (b) as m decreases to a - 1/2 (2.33392298496953... at a = 17/4, V067). So the energy method is sharp for general
    L^2(w_a) data even in x, and 5/2 - 1/D = (b_0 + (9/2) A)/D is the threshold for the m = 4 term of smooth data. The
    order 2 + eps, 0 < eps < 1/3, of 6.6 lies below both.
(d) Scope (V067). The local rescaling X -> X/lambda makes the variable transport, U[H_lambda].grad rho~ and the
    normalized rank-one term O(lambda^{-2}) on fixed rescaled compact sets (c[H_lambda] = lambda c[H]). This does not
    control the globally selected inverse, the exterior nonlocal input or the nonzero corner coefficient. So F4 excludes
    the old high spaces as ranges of the frozen inverse only; for the true operator the exclusion is OPEN and needs a
    local asymptotic or resolvent-stability argument (6.5).

6.3 Lemma H1 (dynamics of the transport field; (i), (ii) THEOREM as a conditional statement under (Z), V063; (iii) THEOREM on every compact K
containing no zero, without (Z), V063). Hypotheses: V in C^1 is globally Lipschitz with
V_1 odd in x, V_2 odd in y and div V = 2 c_l (V055 and the exact identity); V = (-A x, D y) + O(r^3) at 0 and
V = c_l X + O(r^k) at infinity (V055); (A) d = V_2(0, y)/y > 0 on the y-axis; and
(Z) V has no zero on the closed quadrant {x >= 0, y >= 0} other than 0 and P = (x_P, 0), and P is a hyperbolic
    repeller (V017 gives the rate mu ~ 1 in y; the x-rate is about 10.15).
Claims. (i) There is no periodic orbit and no cycle of separatrices in the open quadrant. (ii) Every orbit in the open
quadrant tends to P as t -> -infinity and to infinity as t -> +infinity; the segment (0, x_P) of the x-axis flows to 0,
the ray (x_P, infinity) and the y-axis flow to infinity. (iii) For every compact K of the closed quadrant with
0, P not in K there is a bounded smooth phi, even in x and y after reflection, with V.grad phi >= 1 on K.
Proof sketch. (i) Bendixson-Dulac: a closed orbit or a cycle of separatrices bounding a region Omega would give
0 = (flux of V through the boundary) = 2 c_l |Omega| > 0. (ii) For large r, d r/dt >= (c_l/2) r, so backward orbits are
bounded and forward orbits that reach large r go to infinity. By Poincare-Bendixson on the closed quadrant the alpha-
limit set is a zero, a periodic orbit or a graphic; periodic orbits and graphics are excluded by (i) (a graphic through
0 would need an orbit returning from infinity), and the alpha-limit cannot be {0} because the unstable manifold of 0 is
the y-axis. So the alpha-limit is P. A bounded forward orbit would have omega-limit P (impossible, a repeller) or 0
(only on the stable manifold, the x-axis segment). (iii) By (ii) no orbit stays in K for all forward or all backward
time; by compactness the transit times through a neighbourhood of K are bounded, and phi is built from a flow-box
cover in the standard way.
Verification (V063). (i) and (ii) are CONFIRMED under (Z), parity and the endpoint data, through the C^1 planar
limit-set theorem, a backward trapping ellipsoid at the repeller P and the identification of the local stable and
unstable manifolds of 0 with the axes. For (iii) the verifier gave an independent proof that needs neither (Z) nor the
endpoint data: if no f in C_c^infinity had V.grad f > 0 on K, Hahn-Banach separation would give an invariant probability
measure supported in K, hence a periodic orbit in K, which div V > 0 excludes. phi can be taken compactly supported and
even. The lemma gives no constant and no sign of V.grad phi outside K, so e^{N phi} alone does not give a global
energy estimate; the global sign is the role of Lambda in 6.4. Positive divergence and the endpoint expansions do not
imply (Z) (equivariant compactly supported Hamiltonian bumps can add zeros), so (Z) needs its own certificate.

Lemma Z (reduction of (Z) to finite checks; THEOREM, V071). Let V = c_l X + U[rho~] with the parities
V_1 odd in x and even in y, V_2 even in x and odd in y. Assume:
(Z0) there are r_0 > 0 and delta_0 < A with ||DV(X) - diag(-A, D)|| <= delta_0 (operator norm) for |X| <= r_0;
(ZP) the data of V017 and V024: P = (x_P, 0) with x_P in the certified interval, V(P) = 0, w' = d_x V_1(P) in (10, 10.2),
     mu = d_y V_2(P) in (0.99999997745, 0.99999997750), and ||D^2 V||_F < 0.308 on the disc B_P := B_{rho_P}(P),
     rho_P = 3 delta = 99/2000;
(Zb) a finite family of closed polar boxes Q_i = {r in [r_i^-, r_i^+], theta in [theta_i^-, theta_i^+]} in the closed
     quadrant (r_i^+ = infinity allowed) whose union contains {0 <= theta <= pi/2, r >= r_0} minus the interior of B_P,
     with certified numbers m_i > 0 such that |V(X)| >= m_i |X| on Q_i.
Then (Z) holds. More precisely, on the closed quadrant V vanishes only at 0 and P;
|V(X)| >= (A - delta_0)|X| for |X| <= r_0; |V(X)| >= 0.992 |X - P| on B_P; and P is a hyperbolic repeller with
DV(P) = diag(w', mu).
Proof. (i) Origin. V(0) = 0, so V(X) = M_0(X) X with M_0(X) = int_0^1 DV(sX) ds, and
||M_0(X) - diag(-A, D)|| <= delta_0 because the segment [0, X] lies in the disc. Since |diag(-A, D) X| >= A|X|
(A < D), |V(X)| >= (A - delta_0)|X|. (ii) Source. By the parities V_2(x, 0) = 0 and d_y V_1(x, 0) = 0, so DV(P) is
diagonal, with entries w' and mu (V017). For X in B_P, V(X) = M_P(X)(X - P) with M_P(X) = int_0^1 DV(P + s(X - P)) ds,
and ||DV(Y) - DV(P)|| <= ||D^2 V||_F |Y - P| on the convex disc, so ||M_P(X) - DV(P)|| <= 0.154 |X - P| <= 0.00763.
Hence sigma_min(M_P(X)) >= mu - 0.00763 > 0.992. Both eigenvalues of DV(P) are positive, so P is a hyperbolic
repeller. (iii) Elsewhere, (Zb) gives |V| > 0. (iv) On the closed quadrant every point lies in the disc
{|X| <= r_0}, in B_P or in some Q_i. QED.
Remarks.
- Acceptance check for a box near P: for 0 <= theta^- <= theta^+ <= pi/2,
  |X - P|^2 = r^2 - 2 r x_P cos(theta) + x_P^2 is increasing in theta and convex in r, so a polar box lies in B_P iff
  its two corners (r^-, theta^+) and (r^+, theta^+) do. The box family must be refined near P until every leaf
  either lies in B_P or carries m_i > 0; near the boundary of B_P, |V|/r is about 0.992 rho_P / x_P = 5.7e-3.
- (Z0) can be replaced by positive lower bounds of |V|/r on the inner boxes down to r = 0 (|V|/r tends to
  |diag(-A, D) e_theta| >= A as r -> 0), and (ZP) by a Jacobian condition on a coarser region: if Q is star-shaped with
  respect to P and every entry enclosure of DV on Q satisfies d_x V_1 >= alpha_1, d_y V_2 >= alpha_2,
  |d_y V_1| <= beta_1, |d_x V_2| <= beta_2 with alpha_1 alpha_2 > beta_1 beta_2, then P is the only zero of V in Q,
  because M_P(X) lies in this convex matrix box and every member has determinant at least alpha_1 alpha_2 - beta_1 beta_2.
  The positivity alpha_1 > 0 and alpha_2 > 0 is needed and must be stated: V(s, y) = (s(1 - s), y) on
  [-1/2, 3/2] x [-1, 1] has alpha_1 = -2, alpha_2 = -1, beta_1 = beta_2 = 0, so alpha_1 alpha_2 > beta_1 beta_2, and two
  zeros (V071).
- Verification (V071). The main lemma is CONFIRMED, including the factor 1/2 of the averaged Jacobian (the exact source
  constant is 19847539549/20000000000 > 0.992), the parity argument at P and the two-corner containment test (both ends
  of the bracket of x_P are used). The star-shaped variant is CONFIRMED with alpha_1, alpha_2 > 0 and REFUTED as first
  written (product condition only).
- A larger source region replaces B_P (V070, CONFIRMED). On the rectangle
  Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2], with p_-, p_+ = 4841405518533377/2^49, 4841405518533711/2^49 the V017 bracket
  of x_P, a ball-arithmetic bound ||D^2 V||_F < 1.159484 (6048 covering polar cells, 640-bit audit) and the distance
  bound max |X - P| < 0.7071068 give a symmetric part S(DV) > 0.1801 I on Q (enclosed margin about 0.18012). Hence
  |V(X)| >= 0.1801 |X - P| on Q and P is the only zero of V in Q. A polar box with 0 <= theta^- <= theta^+ <= pi/2 lies in
  Q iff r^- cos(theta^+) >= p_- - 1/2, r^+ cos(theta^-) <= p_+ + 1/2 and r^+ sin(theta^+) <= 1/2 (V071). So (ZP) may be
  replaced by Q, and (Zb) is needed only on boxes not contained in Q.
- Status of the box data (V072). The production arrays cover all 1569 x 64 boxes with finite entries. The inner
  half-line boxes carry |V|/r >= 10.0988 (and every cell with t_b <= -2 carries >= 10.0946), so the origin needs no
  separate Jacobian estimate once the cell enclosures are accepted. There are 86 boxes with a zero lower bound of |V|/r;
  77 of them are not contained in Q. (This was the state at V072; the next item settles (Z).)
- (Z) holds for the actual field (THEOREM, V080). The verifier's own original-data cover (512-bit Green and Taylor
  enclosures on 3276 radial times 128 angular boxes and both analytic half-lines, exact refinement of the 108 unresolved
  boxes, a separate 640-bit audit of coverage, partitions, exclusions and every exceptional box) leaves no unresolved
  box: 47 terminal boxes lie in the exact rectangle Q, and outside Q, in the closed first quadrant away from 0,
  |V|/r >= 3/12500. With V070, the only zeros of V in the plane are 0 and (+-p, 0), p in the V017 bracket. So Lemma H1
  (i), (ii) of V063 (the orbit classification and the qualitative compact escape functions) are THEOREMS for the actual
  normalized modal field. No quantitative escape constant follows. The numerics team's own refinement (34 exclusions,
  all inside Q by the exact check of V078) had a node count reported as a leaf count (359 terminal leaves, not 463,
  V078) and stores only the minimum of the positive leaves; V080 does not depend on it.
- With Lemma Z, hypothesis (Z) of Lemma H1 becomes a finite certificate on the box data that the numerics production run
  computes (lower bounds of |V|/r and the entries of DV per box), with the acceptance checks of V068: complete coverage
  of all angular entries, finite refined leaves, and no silent replacement of refined values.

6.4 Lemma H2 (order function; DERIVED). Blow up the origin (polar coordinates, r >= 0) and compactify at infinity. On
the arc r = 0 the induced flow is d theta/dt = (A + D) sin(theta) cos(theta), with saddles S_x (theta = 0) and S_y
(theta = pi/2); infinity is attracting. Under the hypotheses of Lemma H1 the sets P, S_x, S_y, infinity form a Morse
decomposition ordered by P < S_x < S_y < infinity (the connecting orbits are the x-axis segment P -> S_x, the arc
S_x -> S_y, the y-axis S_y -> infinity and the interior orbits P -> infinity, and none runs downward). Conley's theorem
gives a continuous Lambda, smooth off these sets, with V.grad Lambda > 0 off them and Lambda(P) = 0, Lambda(S_x) = 1,
Lambda(S_y) = 2, Lambda(infinity) = 3. For psi = F(Lambda) with F nondecreasing, the energy identity for the weight
psi^2 w gains int (V.grad psi) psi |g|^2 w >= 0. So a regularity order that is nondecreasing along the flow costs
nothing at the transitions.

6.5 Frozen thresholds at the critical elements (the only places where a loss cannot be absorbed by e^{N phi}).

| Critical element | Derivatives | Condition | Value | Status |
|---|---|---|---|---|
| P | ordinary, joint symbol | s < s_fast = (b_0 + g)/A_P (frozen source, Riesz coupling retained; sharp: a fixed smooth forcing has no H^s solution for s >= s_fast) | 3.57854758171660 < s_fast < 3.57854758172942; 2373/680 = 3.49 is the box-uniform guaranteed value | THEOREM (V064, frozen maximal realization; V011) |
| S_x and the segment [0, x_P) | ordinary across the x-axis | s < (b_0 + aA)/D for general L^2(w_a) data even in x (sharp in the limit m -> a - 1/2); s < 5/2 - 1/D for the m = 4 term of data smooth across the y-axis (sharp) | 2.334 at a = 17/4; 2.4531 | THEOREM for the frozen corner operator (V067); grid ratio kappa/d_yV_2 on the x-axis at r -> 0 is 2.334 (NUMERICAL) |
| S_x, cofactor variables | theta-derivatives of h/(x^2 y) | sigma < 3/2 - 1/D (smooth data); one less than the ordinary threshold in general | 1.4531; 1.334 | THEOREM, frozen (V067) |
| S_y and the y-axis | conormal x d_x, y d_y | none at S_y (commuting); finite loss along the axis absorbed by e^{N phi} | grid joint margin on theta > pi/4: 5.4, 4.3, 1.8 at s = 1, 2, 3 | NUMERICAL |
| S_x, cylinder norm of v = r^{-(3+delta)} h in H^s(dt dtheta) (the norm of the high space) | theta-derivatives of v | s < s_x(delta) = 3/2 + delta A/(A+D) | 1.9841 at delta = 3/2; 2.1132 at delta = 19/10; 2.080923418 at delta = 9/5 (margin 0.97261 at s = 41/20); below 2.1455 for every delta < 2 | THEOREM for the frozen operator (V079), with an explicit counterexample; the principal joint symbol value at delta = 9/5 CONFIRMED (V088) |
| S_y, factored v_a = r^{-delta} h/(x^2 y) | theta-derivatives of v_a | sigma > 1/2 + delta D/(A+D) (energy margin (A+D)(sigma - 1/2 - delta D/(A+D))) | 1.719076582 at delta = 9/5; margin 142.5074 at sigma = 25/4 | principal symbol CONFIRMED (V088, with the metric caveat of the record) |
| infinity | scaled r grad | cost O(r^{k-1}); the leading dilation c_l d_t + c_l gamma - 1 has margin 1 - c_l gamma | none; 3.787681305 at gamma = -1/2 | CONFIRMED (V088) |

Corner threshold in the cylinder norm (THEOREM for the frozen operator, V079). With Sigma = A + D, a(theta) =
-A cos^2 theta + D sin^2 theta and b(theta) = Sigma sin theta cos theta, the frozen operator L_00 = -A x d_x + D y d_y - 1
satisfies r^{-(3+delta)} L_00 r^{3+delta} = a d_t + b d_theta + (3 + delta) a - 1. At theta = 0, theta-derivatives of
order s add s Sigma, and the divergence of (a, b) is Sigma, so the energy constant is -(3 + delta) A - 1 - Sigma/2 + s Sigma
= Sigma (s - 3/2 - delta A/Sigma), using 3A + 1 = Sigma (the theory author rechecked this). It is negative, as the future inverse
needs, iff s < s_x(delta) := 3/2 + delta A/Sigma. The homogeneous solutions x^{2 + delta D/Sigma} y^{1 + delta A/Sigma}
of degree 3 + delta (D - 2A - 1 = 0) attain it. V079 proves sharpness for the low-domain inverse: for the cone-supported
forcing x^{3+delta+tau} chi(x) phi(y/x), which lies in the target with every finite cylinder order and in the low
remainder space, the unique maximal low-domain solution is a nonzero multiple of x^{B - nu} sgn(y) |y|^nu near a
nonzero x-axis segment, nu = 1 + (delta + tau) A/Sigma. For delta = 3/2, tau = 1/10 its Sobolev threshold is
2.0163... < 21/10. So the choice delta = 3/2, s = 21/10 of the first version of 6.6 is excluded for the frozen
operator; the earlier Cartesian threshold 2.334 (Prop F4) belongs to a different norm and does not imply the
cylinder statement (V079: REFUTED as an implication). Since delta < 2 is needed (V065, V073), the bulk order is
2 + eps with eps < 2A/Sigma - 1/2 = 0.14547..., and delta > Sigma (1/2 + eps)/A. The choice delta = 9/5, s = 41/20 passes
the strict scalar threshold (margin Sigma (s_x - s) = 0.9726). No transfer to the actual nonlocal operator is claimed.

Since the order may only increase along the flow (6.4) and P lies upstream of S_x, the binding order near the closed
segment [0, x_P] x {0}, P included, is the corner value: s < 2.334 for general data in L^2(w_a), a = 17/4 (2.4531 for
the x^4 term of smooth data). The frozen
source threshold s_fast = 3.5785 at P (V064) is not binding. In the full problem the singularity of Prop F4 sits on the stable manifold of
the origin, which is the whole segment [0, x_P), and reaches P from the left: a point (x_P - xi, y) leaves the
neighbourhood of P after a time about log(1/xi)/10.15 and then passes the corner. The y-axis, the ray (x_P, infinity)
and infinity carry no such singularity. The proposed transfer of Prop F4 to the true operator: at scale lambda^{-1}
near 0 the coupling U[h].grad rho~ is O(lambda^{-2}) relative to the transport (grad rho~ = O(r^2), U homogeneous of
degree 0), the strain term has rank one, and V = (-A x, D y) + O(r^3); the exponents are fixed by DV(0) = diag(-A, D),
with logarithms possible at resonances. V067: the rescaling estimate is correct but does not by itself transfer the
singular coefficient of the globally selected inverse; the transfer is OPEN. It is not on the critical path, because
the design order 2 + eps of 6.6 is below the frozen thresholds and so is not affected by the outcome.

6.6 Theorem H (variable-order high regularity; DERIVED outline, OPEN as a theorem). Assume (A), (M), (Z) and injectivity
of L_red : Z -> Y (so L_red is invertible by Theorem C'). Fix eps in (0, 2A/(A+D) - 1/2) = (0, 0.14547...), an origin
exponent delta in ((A+D)(1/2 + eps)/A, 2) (the cylinder corner threshold of 6.5, V079), and N in (6, 13/2), for example
eps = 1/20, delta = 9/5, N = 25/4 (see the constraint below; V073 needs N > 6 for the factored control near the
vertical axis). Let the order be
2 + eps on {Lambda <= 1 + tau} (a neighbourhood of the closed segment [0, x_P] x {0} and of S_x) and N on
{Lambda >= 2 - tau}, nondecreasing in Lambda, realized by nested cutoffs psi_0 > psi_1 > ... > psi_n = F_n(Lambda):
ordinary derivatives near the low set (in the corner, cylinder derivatives of h/r^3), conormal derivatives near the
y-axis, scaled derivatives at infinity, and weights e^{N phi} on the transition sets. Let H_reg and Y_H be the resulting
regularity space and target (same orders on both sides, origin exponent delta = 9/5 and far exponent gamma = -1/2; V065,
V073 and V076 cover every delta in (1/4, 2); the value delta = 3/2 of the first version is excluded by V079). Claim (inverse-regularity form): for every f in Y_H the solution h = L_red^{-1} f of the low
problem lies in H_reg, and ||h||_{H_reg} <= K_H ||f||_{Y_H}. Equivalently, L_red maps the graph domain
D = {h in Z : h in H_reg, L_red h in Y_H}, normed by ||h||_{H_reg} + ||L_red h||_{Y_H}, isomorphically onto Y_H. The
same is claimed with one constant K_H for A_g = L_red + W[g].grad (and for the moving-tail family) when ||g||_{H_reg} <= r_V;
the graph domains D_g may depend on g, and only the solution operators R_g := A_g^{-1} : Y_H -> H_reg enter the two-norm
theorem of S2_CLOSURE.md 3.4.
Correction (V074). The first version claimed that L_red : H -> Y_H is a bounded isomorphism of same-order spaces. That
is REFUTED: a compact packet N^{-s} eta(X) e^{i N xi.X} at a regular point has bounded H^s norm, while its image has H^s
norm of order N, because the transport differentiates and the order-zero and strain terms do not cancel it. Also, the
maximal H^s graph domains of d_x - 1 and d_x + eps d_y - 1 differ for every eps != 0 (h = chi(x) g(y) with g in H^s and
not in H^(s+1)), so a small ||DW|| does not give a common domain. The two-norm theorem uses only bounds for R_v and the
low comparison ||g||_{X_L} <= K_L ||A_v g||_{Y_L}, which is what the inverse-regularity form provides (V062 was stated in
this way).
Further hypotheses needed (claims of an external consultation; the theory author checked items (b) and (c) by hand; status of
the verified parts: (a) settled for L_red by V084 and V085, its rank-one example CONFIRMED as a non-implication, V089;
the principal symbol of (c) CONFIRMED with its margins, V088; the example of (f) CONFIRMED in a torus version, V091, and
the geometric part of uniformity proved, V090).
(a) Smoothness of the normalization profile is not enough. Rank-one construction: take u = -Delta v with v supported on
    annuli r ~ 4^j away from the axes, angular frequencies n_j ~ e^{j^2} and amplitude 4^{2j} n_j^{-4}, so that u is in Z
    and not in H_reg, c[u] = 0 (v vanishes near 0) and U[u] = (-d_xy v, d_xx v). Put N := L_0 u and L_eps := L_0 +
    eps c[.] N. Then L_eps^{-1} f = L_0^{-1} f - eps c[L_0^{-1} f] u for every eps, so the low inverse and all frozen data
    are unchanged, while L_eps^{-1} f is not in H_reg whenever c[L_0^{-1} f] != 0. The hypothesis this identifies is
    global weighted high-order control of the combined coupling and normalization terms. For L_red = T + C + c[.] zeta
    the normalization part is settled: zeta = (c_l g_far - k y_KP)/d lies in Y intersect H_base^sigma for 0 < delta < 2,
    gamma > 2k - 1, 0 <= sigma < 13/2 (THEOREM, V084, finiteness only), so c[.] zeta maps Z boundedly into the high
    base target. A one-order gain of the full coupling is false (REFUTED, V085): with the order-zero multiplier
    p(X, xi) = (rho_x xi_1 xi_2 - rho_y xi_1^2)/|xi|^2, parity-symmetric packets h_N = N^{-s} phi cos(N x) on a regular
    patch with rho_y > 0 are bounded in H^s, have zero cubic and tail coordinates and lie in the graph domains, while
    the localized H^{s+1} norms of C h_N grow at least linearly in N. So the high energy must keep the full order-zero
    principal coupling (the joint symbol of (c) and 6.1); one-order smoothing is available only for commutators and
    separated-support pieces.
(b) The cubic term at the origin. For symmetric h supported away from 0, DU[h](0) = diag(-c[h], c[h]), so
    U[h].grad(x^2 y) = -c[h] x^2 y + O(r^5); after division by r^3 this is a leading term that the local symbol
    p = O(r^2) does not see. In the present operator it is cancelled by the strain term c[h] X/3 inside C (V044; CONVENTIONS
    S4.5), so it enters only through the jet row.
(c) The high-frequency symbol of the energy at order s is kappa_w - p(X, nu) - s nu^T DV nu, maximized jointly in nu
    (this is 6.1); bounding the coupling by its absolute value loses s_fast at P.
(d) The neighbourhood {Lambda <= 1 + tau} must be a neighbourhood in the polar blow-up (it contains a piece of the arc
    r = 0 near S_x), and the order function should be smooth on the blown-up compactification with V.grad m >= 0;
    a direction-dependent order is not needed.
(e) Each nested commutator step needs the transition term Theta_j H^{s_j} on the support of grad psi_j, and the
    regularization step (a low solution with L h in Y_H is in H_reg) must be proved separately: an a priori estimate
    for h already in H_reg does not give it, and radial-point regularization has a direction and a threshold. Lemma
    H-spec below replaces this step by a large-parameter bound for the transport alone. For the frozen corner operators
    the step itself is proved (THEOREM, V103 in the x-axis cylinder chart, ||u||_{H^s} <= ||F||_{H^s}/kappa_s with
    kappa_s = 0.97261 at delta = 9/5, s = 41/20; V104 in the vertical remainder cofactor chart, every finite s >= 2),
    given the complete localized right side, including (V.grad chi) h, in the stated space.
(f) Uniformity. If ||h||_H <= C_1 ||A_g h||_{Y_H} + C_2 ||h||_Z holds with constants uniform in g, then with the low
    bound and the product bound ||h||_H <= (C_1 + C_2 K_L)/(1 - C_2 K_L C_prod C_E r_V) ||A_g h||_{Y_H}. This is an
    estimate; it does not give surjectivity of A_g (the perturbation has one derivative), which needs the graph-domain or
    a regularized construction. C^1 control of the coefficients alone does not bound high-order constants:
    T_n = (1 + n^{-1-alpha} chi(y) sin(ny)) d_x - 1 converges in C^1 to d_x - 1 while the H^s norms of the solutions for
    a fixed forcing grow like n^{s-1-alpha}. This illustrates the need for tame estimates in g in H_reg; it is not a
    counterexample to the family used here. Verified version (THEOREM, V091): on the torus,
    T_n = (1 + n^{-beta} sin(ny)) d_x - 1 with 1 < beta < s has L^2 inverse norm at most 1 and coefficients converging
    in C^1, while ||T_n^{-1} e^{ix}||_{H^s} grows like n^{s - beta}. The geometric part of uniformity is settled
    separately (THEOREM, V090): for every parity-preserving C^1 field W with sup ||DW|| <= 1e-5, V + W has exactly the
    three zeros of V with the same types, the same quadrant flow and the qualitative escape, speed/r >= 0.00023 outside
    the source rectangles and a source shift of at most 1/1801. The rank-one construction of (a) is CONFIRMED as a
    non-implication (V089).
(g) W^{2,p} control with p > 2 gives a Hoelder gradient but not H^{2+eps}; an L^p route would be a separate program.
Lemma H-spec (spectral-parameter continuation; DERIVED, submitted for verification; revised at 07:01Z: stated for the
remainder block, with the jet row split off by the triangular form of Theorem C', because the inclusion X_H in Y_H
fails on the jet coordinate; see the paragraph after the corollary). It replaces the regularization step of (e) and
the surjectivity construction of (f) by a large-parameter bound for the transport alone.
Setting. S = T + C with T := T_R and C := C_R, the remainder block S_1 of Theorem C' (step 2), so S : D_R -> R is
Fredholm of index 0. Let X_H and Y_H be Banach spaces with continuous inclusions X_H in Y_H (norm iota') and Y_H in R
(norm iota), and let D_H = {h in X_H : T h in Y_H}, T taken in distributions, with the norm ||h||_{X_H} + ||T h||_{Y_H}.
Assume
(H1) C maps X_H boundedly into Y_H;
(H2) there are omega >= 0 and M >= 1 such that for every lambda > omega the map T - lambda : D_H -> Y_H is bijective
     and ||(T - lambda)^{-1} f||_{X_H} <= M (lambda - omega)^{-1} ||f||_{Y_H};
(H3) there are C_1, a Banach space W and a compact K : X_H -> W with
     ||h||_{X_H} <= C_1 ||(S - lambda) h||_{Y_H} + ||K h||_W for all h in D_H and 0 <= lambda <= lambda_*,
     where lambda_* := omega + 1 + 2 M ||C||_{X_H -> Y_H} (strictly above omega, so that C = 0 is covered; the verifier's scope check of 06:59Z).
Then S : D_H -> Y_H is Fredholm of index 0, D_H is continuously included in D_R, and the kernel of S on D_H lies in
its kernel on D_R.
Proof. D_H is complete: if (h_n) is Cauchy in D_H, then h_n -> h in X_H and T h_n -> f in Y_H; both limits also hold
in R, so T h = f in distributions, f is in Y_H and h_n -> h in D_H. The inclusion D_H -> D_R is continuous, since
||h||_R + ||T h||_R <= iota iota' ||h||_{X_H} + iota ||T h||_{Y_H}. The map lambda -> S - lambda from [0, lambda_*] to
B(D_H, Y_H) is norm-continuous, with ||(S - lambda) - (S - lambda')|| <= iota' |lambda - lambda'|. At lambda_*,
S - lambda_* = (I + C (T - lambda_*)^{-1})(T - lambda_*) on D_H and ||C (T - lambda_*)^{-1}||_{Y_H -> Y_H} <=
||C|| M/(1 + 2M ||C||) < 1/2, so S - lambda_* is an isomorphism, of index 0. For lambda in [0, lambda_*], (H3) and
||T h||_{Y_H} <= ||(S - lambda) h||_{Y_H} + (||C|| + lambda iota') ||h||_{X_H} give ||h||_{D_H} <= c (||(S - lambda) h||_{Y_H}
+ ||K h||_W) with K compact on D_H, so S - lambda has finite-dimensional kernel and closed range (upper semi-Fredholm).
The index is locally constant on the open set of semi-Fredholm operators (Kato, Perturbation Theory, IV.5.17 and
IV.5.22), and [0, lambda_*] is connected, so ind (S : D_H -> Y_H) = ind (S - lambda_*) = 0. The kernel statement
follows from D_H in D_R. QED.
Corollary H-spec (the full operator L_red). Let Gamma_H be a Banach space continuously included in Gamma, let
B_H := {beta in B : A beta in Gamma_H} with the norm ||beta||_B + ||A beta||_{Gamma_H}, and put X_H^full := E B_H (+) D_H
and Y_H^full := E Gamma_H (+) Y_H. Assume (H1) to (H3) for S_1 and
(J1) the lower off-diagonal block X = Err + C_R E maps B_H boundedly into Y_H;
(J2) the jet coupling h -> gamma_C[h] maps X_H^full compactly into Gamma_H (the high-order form of (E-J));
(J3) zeta lies in Y_H^full (V084 gives membership in the base target of every order sigma < 13/2).
Then L_red : X_H^full -> Y_H^full is Fredholm of index 0 and its kernel lies in the kernel of L_red on Z. If L_red is
injective on Z, it is an isomorphism of X_H^full onto Y_H^full, and for f in Y_H^full the element L_red^{-1} f is the
low solution.
Proof. A : B_H -> Gamma_H is an isomorphism by the definition of B_H and V041. As in steps 1 and 3 of Theorem C',
L_red = M_H + K_1 + c[.] zeta on X_H^full, where M_H is block lower triangular with diagonal blocks A : B_H -> Gamma_H
and S_1 : D_H -> Y_H and off-diagonal block X, bounded by (J1); so M_H = [[1, 0], [X A^{-1}, 1]] diag(A, S_1) is
Fredholm of index 0 by the lemma. K_1 = E gamma_C is compact by (J2). X_H^full is continuously included in Z (B_H in B,
D_H in D_R), and c is bounded on Z (Lemma C'4), so with (J3) c[.] zeta is a bounded rank-one map into Y_H^full. Hence
L_red is Fredholm of index 0 on X_H^full, and X_H^full in Z gives the kernel statement. With injectivity on Z, L_red is
injective of index 0 on X_H^full, hence bijective, and its inverse is the restriction of the low inverse. QED.
Bound. If the high estimate takes the form ||h||_{X_H^full} <= C_1' ||L_red h||_{Y_H^full} + C_2' ||h||_Z (the compact
errors factoring through Z, with C_1' and C_2' explicit in C_1, ||A^{-1}||, ||X|| and the (J2), (J3) data), then
||L_red^{-1}||_{Y_H^full -> X_H^full} <= C_1' + C_2' K_L iota_Y, with K_L = ||L_red^{-1}||_{Y -> Z} and iota_Y the norm of
the inclusion Y_H^full in Y.
Why the jet row is split off and not shifted (DERIVED). The inclusion fails on the jet coordinate: beta = J H with
J != 0 is in B but not in Gamma, because ||beta||_Gamma = ||z/d||_{L^2(omega)} with z -> J and omega = e^{-2 sigma t} as
t -> -infinity (the same fact as H_0 not in Y, V044), so T - lambda does not map E B into Y for lambda != 0. Restricting
to B_0 = {J = 0} does not help. Write beta = H z and Phi' = 1/d; then (A - lambda) beta = H (d z' - lambda z), and with
g = gamma/(dH) the solution that vanishes at +infinity is z(t) = -int_t^infinity e^{-lambda (Phi(s) - Phi(t))} g(s) ds.
The homogeneous solution e^{lambda Phi} grows at +infinity and behaves like e^{lambda t/D} as t -> -infinity. Hence
A - lambda : B_0 -> Gamma is injective with the closed range {gamma : int_R e^{-lambda Phi} gamma/(dH) = 0} of
codimension one for 0 <= lambda < sigma D (lambda = 0 is V041 (8)), an isomorphism for lambda > sigma D, and not
Fredholm at lambda = sigma D (= D/4, about 5.33, at the low weight sigma = 1/4), where the exponent lambda/D meets the
weight exponent sigma. Every weight has such a point, because the index on B_0 is -1 at lambda = 0 and 0 for large
lambda. A continuation that shifts the jet row therefore crosses a non-Fredholm point before lambda_*, which is far
larger (remark (5)). In the corollary the jet block A is inverted exactly and only the remainder block is continued.
Remarks. (1) In energy form (H3) at lambda = 0 gives (H3) for every lambda >= 0 with the same C_1 and K, because the
shift adds lambda ||h||^2 to the coercive side of Re <-(S - lambda) h, h>_H. (2) (H2) concerns T_R only. By the
characteristic formula (T - lambda)^{-1} f = -int_0^infinity e^{-(1+lambda)s} f o Phi_s ds (Phi_s the flow of V),
(H2) holds with omega = omega' - 1 if ||f o Phi_s||_{X_H} <= M e^{omega' s} ||f||_{Y_H} for s >= 0, together with the
corresponding statement for the graph norm. Such a composition bound needs the order to be nondecreasing along the
flow (f o Phi_s at X samples f at Phi_s(X), where the order is at least the order at X), which is the design
condition of 6.4; omega' is controlled by the growth of D Phi_s up to the order of the space and by the weights; the
flow preserves both axes, so the factored structure near the y-axis is kept. (3) For the perturbed operators
A_g = L_red + W[g].grad of (f), the corollary applies on the g-dependent domain, with the scalar row of V + W[g] (again
tangent to both axes, W[g] being parity preserving) in place of A, so surjectivity follows for each g from (H1) to
(H3), (J1) to (J3) for A_g and injectivity of A_g on Z; the transport bound (H2) for V + W[g], with W[g] only Lipschitz
and of the same order as g, is the standard transport estimate with a Kato-Ponce commutator bound (order above 2 in
two dimensions) instead of a composition bound. A uniform K_H needs C_1', C_2', omega and the low bound uniform in g
(tame estimates; V091 shows that C^1 control is not enough). (4) The lemma and the corollary give no constant by
themselves; they show that the high inverse needs (H1) to (H3) for the remainder block, (J1) to (J3) for the jet row,
and low injectivity, and nothing else. (5) The homotopy T + sC in the coupling strength, used for Theorem C', does not
work in the high space: at the source the frozen energy margin at order sigma is min(b - sigma mu, b + g - sigma A),
b = 1 + (A + mu)/2 (V011), so without the coupling (g = 0) it is negative for sigma > b/A, about 0.65, and the coercive estimate for T alone
fails at the order 2 + eps used near P (with the coupling the margin at 41/20 is about 14.8); a negative frozen energy
by itself does not prove that T is not semi-Fredholm (V106), but it removes the energy proof along that path. The shift
by lambda keeps the full coupling along the path, and at the large end the transport is inverted with the help of
the shift (near P, lambda above about sigma A - b, about 14.2 at sigma = 41/20). (6) Reduction of (J2) and (J1) to
conormal regularity near the y-axis (DERIVED, not a proof). By V049 the jet row is
Gamma h = y^{-1} [(alpha + alpha') T_h - 2 alpha (y d_y) T_h] + c[h] chi_0 (alpha + alpha'/3), with T_h(y) = U_2[h](0, y)
(d_x U_1[h](0, y) = -T_h'(y) by incompressibility). The map h -> U[h] is homogeneous of degree 0 and commutes with
dilations, so (X.grad) U[h] = U[(X.grad) h] and, on the axis, (y d_y)^j T_h = T_{(X.grad)^j h}. Split
h = chi_s h + (1 - chi_s) h with chi_s homogeneous of degree 0, equal to 1 on a sector around the y-axis and 0 outside
a larger sector of half-angle theta_s; chi_s commutes with X.grad. (a) Sector part: by V105 (j = 0),
|(y d_y)^j T_{chi_s h}(y)| <= N_0(y) ||chi_s (X.grad)^j h||_R, so an order-N norm of Gamma h in t = log y is bounded by
N + 1 radial conormal derivatives of h in the sector, provided alpha and alpha' are multipliers of order N in t (true
below the knot ceiling of V069) and N_0(y)/y is bounded against the weight of Gamma_H at both ends, as in the
Hilbert-Schmidt proof of V049. (b) Outside the sector: for X on the axis and Y outside the larger sector,
|X - Y| >= sin(theta_s) max(|X|, |Y|), so all y-derivatives fall on the kernel, |d_y^j K(X - Y)| <= c_j
(sin theta_s)^{-j-2} max(|X|, |Y|)^{-j-2}, and (y d_y)^j T_{(1 - chi_s) h} has a majorant of the form (1) of V105 that
uses only ||h||_R. So (J2) holds as a bounded statement if X_H controls N + 1 radial conormal derivatives in the
sector, which is the factored conormal order that the design of 6.4 places near the y-axis, and compactness follows
from one further conormal derivative (Rellich on bounded t-intervals) together with the end decay of the majorants.
(J1): Err beta = x^2 y cos^2(theta) [a_1 beta' + a_0 beta] (Lemma C'1) is smooth in the angle with the lift
coefficients a_1, a_0 of the modal field, so it maps B_H into Y_H if the high norm counts no more derivatives than a_1,
a_0 carry (finite below the knot ceiling); C_R E beta is the coupling applied to an angularly smooth profile, and the
same sector split applies. The constants are not computed, and the statements depend on the final choice of X_H and
Gamma_H. For (H2) see remark (2): it is a composition bound for the flow of V in X_H.
Outline. The base estimate is Theorem C' with injectivity. Each step localizes with psi_j: at a critical element inside
the region of order s_j the frozen margin of 6.5 holds (with the joint symbol at P); on the transition sets the escape
weight absorbs the commutator loss; V.grad psi_j >= 0 (6.4); and the nonlocal coupling is triangular, because
psi_{j+1} U (1 - psi_j) is smoothing and [psi_j, U] has order -1, so the step to order s_j uses only order s_j - 1 on
the larger region. Uniformity: P moves to a nearby hyperbolic repeller P_g, and (V + W).grad psi_j >= c/2 where
grad psi_j != 0 once ||D W||_infinity is small, because V.grad Lambda > c there. The order 2 + eps gives grad h in C^eps
(with decay), which is what the Lipschitz-velocity bound needs.
Not done: the energy estimates themselves (each step is a standard positive-commutator argument, but the coupling at P
and the corner arc with the jet coordinate need the joint symbol and the jet rows) and explicit constants. Residual
membership is settled (THEOREM, V076): F(rho~)/[p A_(delta,gamma)] lies in cylinder H^sigma for 0 < delta < 2,
gamma > 2k - 1 and sigma < 13/2, by the exact cofactor identity F/p = (2V_1/x + V_2/y - 1) a + q a_t + v a_theta, which
extends across both axes; F/p = O(r^2) at 0 (the constant -2A + D - 1 vanishes) and O(r^(2k-4)) at infinity (ell k = 1).
So F(rho~) belongs to Y intersected with the base target of order 25/4, delta = 3/2, gamma = -1/2, scalar coordinate 0
(the proof covers 0 < delta < 2, so also delta = 9/5),
and to the larger cone-bulk sum target of V073. Y_H of this section has order 2 + eps near the segment and 25/4
elsewhere, the same delta and gamma, and bounded escape weights, so it contains F(rho~) (verifier's note of 05:39Z).
This is membership; no norm bound is certified.
Constraint from the regularity of the background (THEOREM, V069). rho~ is a degree-7 spline in t = log r with C^6
joins at its radial knots r = r_j. At the interior knot t_j = 4958764014967233/2^51 (r_j about 9.04, outside the source
x_P = 8.60) the seventh t-derivative of the exact spline coefficients jumps in the angular modes 0 and 1 (exact rational
check). Hence the sixth derivatives of F(rho~), and of its canonical axis-jet remainder, jump on a nonempty part of
every open arc of that circle away from the axes. Both functions are locally H^s there for s < 13/2 and not locally
H^(13/2). So an ordinary or equivalent conormal target of order N >= 7 across an open sector of this circle excludes the
actual residual (V069: REFUTED for smoothness away from the origin, CONFIRMED for the jump and the local threshold).
Every orbit from P to infinity crosses this circle, and the order is nondecreasing along the flow (6.4), so every order
used on the circle and upstream of it must be below 13/2. The factored H^7 control near the vertical axis used by V060 and V065 is
therefore replaced by a fractional order sigma in (6, 13/2), which still embeds the cofactor in C^5. V073 (THEOREM)
proves that the low/high product bound ||W[d].grad h||_Y <= C_B ||d||_{X0} ||h||_H and the bound
||DW[h]||_infinity + |c[h]| <= C_V ||h||_H, the embedding into Z and the classical J all hold for every sigma > 6 (with
(A), 1/4 < delta < 2, gamma < -3/8 and a cone-local bulk order s > 2); sigma = 25/4, delta = 3/2, gamma = -1/2,
s = 21/10 is admissible for the mapping side, and so is the revised choice delta = 9/5, s = 41/20 (inside the same ranges). V076 proves the residual membership stated above. The limit is a property of the trial, not of the problem: a background
spline of degree n with C^(n-1) joins would allow orders below n - 1/2.

6.7 Relation to the verified high spaces and to the nonlinear scheme.
- V057 and V060 prove the low/high bilinear bound ||W[d].grad h||_Y <= C ||d||_{X0} ||h||_high and the
  Lipschitz-velocity bound for H_(delta, gamma) (cofactor in cylinder H^7, origin exponent delta in (1/4, 2)) plus a
  compact H^s component, s > 2, away from x = 0. By Prop F4 these are valid mapping spaces but not ranges of a high
  inverse: near the corner on theta = 0, which no compact set away from x = 0 covers, they require cofactor
  theta-regularity 7 > 1.4531, and on a compact K meeting the segment, s = 31/10 > 2.4531. This exclusion is a
  THEOREM for the frozen inverse (V067) and OPEN for the true operator. The compatible space is the one of 6.6. Its
  mapping side is now proved (V065): V060's factored H^7 space near the vertical axis plus a cylinder H^s bulk with
  s > 2 (s = 21/10 admissible) on |cos theta| >= eps, including the closed x-axis segment and the origin, satisfies the
  low/high product bound and the bounded-DW bound, embeds into Z and has a classical J. V073 extends this to every
  factored order sigma > 6, so the order 25/4 below the knot ceiling 13/2 of V069 is admissible; V076 places the actual
  residual in the corresponding target.
- The moving-tail formulation (V062, CONFIRMED for the mapping, the exact identities and the conditional iteration,
  assuming the positive axis rate): with ell = ell(h) fixed by n(ell) = c[h], B(ell) = F_ell(rho_ell) - n(ell) H_0 and
  M(ell) = H_0 + (B(ell) - B(ell_0))/n(ell) (cubic coefficient 1), the operator
  A_h g = (ell(h) X + U[rho_ell(h)] + U[h]).grad g - g + U[g].grad rho_ell(h) + c[g] M(ell(h)) maps the high space into
  Y and F_ell(h)(rho_ell(h) + h) = f_0 + A_h h exactly. Because c[d] + c[z] = 3 delta ell, the difference is
  (A_h1 - A_h0) g = W[d].grad g + W[z].grad g + U[g].grad z + c[g](m_1 - m_0), so
  ||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_{X0} ||g||_high; every power of log r is included. Existence follows from
  uniform right inverses R_v : Y_H -> H_high with K_H ||f_0||_{Y_H} <= r, a low estimate ||g||_{X0} <= K_L ||A_v g||_Y and
  K_L C K_H ||f_0||_{Y_H} < 1; final rescaling restores J = 1 if |J(h)| < 1. None of these inverse hypotheses is proved.
- Quasilinear two-norm scheme (fixed tails, for orientation): h_{n+1} = -A_{h_n}^{-1} F(rho~), so differences satisfy
  A_{h_n}(h_{n+1} - h_n) = -W[h_n - h_{n-1}].grad h_n, a low-times-high product (V057 structure). The iteration
  contracts in the low norm if K_L C_B K_H ||F||_{Y_H} < 1 and stays in the high ball if K_H ||F||_{Y_H} <= r_V, with
  K_L the low inverse bound, C_B the bilinear constant and K_H the uniform high bound. The moving tails and the scalar
  normalization enter through the parameter family (S2_CLOSURE.md 3.4).

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

1. Hypothesis (A): DONE (V077, d >= 5.5752 on the whole axis, independent original-data computation). (E0), (E-J),
   (E-G) are proved (V049 to V053); explicit values of their constants, of the constants of Lemma C'1 and a finite-rank
   split of K_eps are OPEN and are needed for item 3.
2. The margins (H_m) and (H_m'): DONE (V077, m_R >= 1.78605 for mu~, m_a >= 0.53072 for w_a; both at least 5/2 by
   V086). Theorems R and C' are
   THEOREMS for the actual background. Larger certified margins would shorten item 3 (S2_BASIS_CERTIFICATION.md 6.1).
3. Injectivity of L (or L_fix) on the chosen space; with Theorem R or C it is equivalent to invertibility. A
   computer-assisted route: the estimate (m_* - eps)||h|| <= ||L h|| + ||K h|| with K approximated by finite rank
   reduces injectivity to a finite-dimensional check, which is exactly the complement control a finite section lacks.
4. The high-order inverse (Theorem H of 6.6, variable order: 2 + eps near the closed segment [0, x_P] x {0}, N
   elsewhere) and the bilinear and Lipschitz bounds in the same space. Prop F4 shows that a uniform order above
   5/2 - 1/D across the x-axis segment is impossible for the frozen corner inverse (V067), so the V057 and V060 spaces
   cannot be its ranges; for the true operator this is OPEN. The mapping side of the variable-order space is proved
   (V065) with factored H^7 control near the vertical axis; because rho~ is only C^6 across a knot circle that every orbit
   crosses (V069), the orders there and upstream must be below 13/2 (6.6); the mapping side with the fractional order
   25/4 is proved (V073) and the residual lies in the target (V076). The theorem must be stated in inverse-regularity
   (graph-domain) form, not as a bounded same-order isomorphism (V074). The cylinder corner threshold (V079) forces
   delta > (A+D)(1/2 + eps)/A and eps < 0.14547; delta = 9/5, s = 41/20 is admissible. What remains is the inverse
   estimate itself, with the hypotheses (a) to (f) of 6.6.
5. Hypothesis (Z) of Lemma H1: DONE (V080; the verifier's own original-data cover, |V|/r >= 3/12500 outside the source
   rectangle Q, P the only zero in Q by V070). Quantitative escape constants are OPEN.

## 9. Verification status

- Theorem O: CONFIRMED (V022) for (a), (b), (d); (c) CONFIRMED as the bounded integral extension; the pointwise reading
  of (c) REFUTED.
- Proposition N1: CONFIRMED with a >= 5/2 (endpoint allowed); "strictly" REFUTED (V025). Proposition N2: CONFIRMED
  conditional on the positive axis rate (V025). Corollary N3: CONFIRMED in the corrected full-L form (V025).
  Proposition N4: CONFIRMED, with the residual threshold needing a nonzero leading coefficient (V025). Remark N5:
  corrected statement CONFIRMED, literal o(r^k) version REFUTED (V025).
- Lemmas G1 to G3, Theorem R: CONFIRMED under the exact hypotheses listed in section 3 (V023), with the Lemma G2
  square-root step replaced. V031 extends Theorem R to Lipschitz mu with Lip(mu) < 2, including mu~. V032 confirms
  Remark R.2 (c not closable on D_w). The global margin (H_m) is CONFIRMED for mu~ (V077, m_R >= 1.78605; m_R >= 5/2 by V086), so Theorem R
  holds for the actual background; injectivity remains OPEN, and the strain column and the jet space are handled by
  Theorem C' instead.
- V041: the scalar axis row on the explicit spaces B -> Gamma (CONFIRMED, conditional on the positive axis rate and
  the endpoint bounds). V041 also found that the first-version Theorem C was not a fully specified conditional theorem
  (lifting, cross couplings, remainder domain and homotopy were not stated). Section 5.2 now states them: Lemmas C'1
  to C'4 and Theorem C' were DERIVED and submitted to the verifier.
- V046: Lemmas C'1 to C'3, the pure-transport isomorphism T : Z -> Y = E Gamma (+) R with the exact triangular form,
  CONFIRMED as a conditional theorem (hypotheses (A), (CB), kappa_* > 0). The coupled homotopy remains OPEN.
- V044: L_fix does not map Z into Y and c[.] H_0 is not a bounded perturbation into Y (CONFIRMED counterexample); the
  renormalized coupling of Theorem C' maps the counterexample into Y.
- V045: the separated outside-to-inside strip coupling is compact (CONFIRMED at fixed bounded strip scope).
- V042: the target Y = E G (+) L^2(w_a) and membership of the modal residual and the parameter-family residual in it
  (CONFIRMED, membership only).
- Section 5 compensation formula: CONFIRMED with c[h_0] (V025). Section 6 Lipschitz equivalence: REFUTED (V025),
  corrected to a sufficient condition.
- V047: Theorem C' and Lemmas C'1 to C'4 CONFIRMED as a conditional theorem; (L) = (CB) holds for the modal field with
  finite constants; c_R = 0.2075698661066814348...; zeta in Y.
- V049, V050, V051, V052: (E-J) under (A), the jet-input part of (E0), the remainder-input part of (E0), and (E-G),
  CONFIRMED under the background hypotheses (B1), (B2). V053: the exact modal density satisfies them (CONFIRMED).
- V048: scope audit of the report (corrections applied). V054: the first (A) certificate script, REFUTED in coverage and
  underflow steps; identities CONFIRMED.
- V055: transport regularity of the modal field (V globally Lipschitz C^1, V_1/x and V_2/y bounded, the endpoint
  bounds of d, finite M_Q and M_P) and the exact energy limits kappa_0 = (19/2) c_l - 13/4 = 49.7159..., kappa_inf =
  1 + 3 c_l/8 = 3.0908..., CONFIRMED. So Theorem C' holds for the modal background under (A) and (M) alone.
- V057: the low/high bilinear bound and the Lipschitz-velocity bound in the cylinder-H^7 space H_gamma, CONFIRMED (finite
  constants, not computed). V060: the same for H_(delta, gamma) plus a compact H^s component (s > 2) away from x = 0,
  CONFIRMED. By Prop F4 (6.2, V067) neither is a possible range of the frozen corner inverse; for the true operator
  this exclusion is OPEN.
- V056, V058, V059, V061: numerics audits (the S0 Gram is positive after exact-midpoint whitening, conditional on the
  entries; a float union REFUTED and repaired; stable Green moments; resonance merging), recorded in
  S2_NUMERICAL_CERTIFICATES.md.
- V062: the moving-tail quasilinear formulation, the low/high difference bound and the conditional iteration (6.7),
  CONFIRMED; the inverse hypotheses are OPEN. V063: Lemma H1 (i), (ii) under (Z) and the compact escape lemma (iii)
  without (Z), CONFIRMED; (Z) itself OPEN. V064: the frozen source threshold s_fast = (b_0 + g)/A_P is sharp with the
  Riesz coupling retained, 3.57854758171660 < s_fast < 3.57854758172942, CONFIRMED (frozen maximal realization).
- V065: the cone-local high space (V060's factored H^7 space plus a cylinder H^s bulk, s > 2, on |cos theta| >= eps, origin
  exponent 1/4 < delta < 2, far exponent gamma < -3/8) has classical J, embeds into Z and carries the low/high product and
  bounded-DW estimates, CONFIRMED under the positive axis rate; s = 21/10, delta = 3/2, gamma = -1/2 is admissible. This is
  the mapping side of the space of 6.6; inverse preservation is OPEN.
- V067: Prop F4 CONFIRMED (frozen formula, maximal weighted inverse, both Sobolev endpoints, exclusion of the old high
  spaces for the frozen inverse); the parity-only threshold REFUTED (corrected in 6.2(b), (c)); transfer to the true
  operator OPEN.
- V069: the exact seventh-derivative jump of the spline at the knot t = 4958764014967233/2^51 and the local threshold
  13/2 for the residual and its jet remainder, CONFIRMED; smoothness of the residual away from the origin REFUTED.
- V070: the source rectangle Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2] with |V| >= 0.1801 |X - P|, CONFIRMED.
- V071: Lemma Z (6.3), CONFIRMED; the star-shaped variant needs alpha_1, alpha_2 > 0 (REFUTED without).
- V072: coverage, retention and directed aggregation of the production margin and axis-rate runs, CONFIRMED
  conditional on the exported cell enclosures; global (Z) was then OPEN (now V080).
- V073: the mapping side (product, Lipschitz-velocity, embedding into Z, classical J) for every factored order sigma > 6,
  CONFIRMED; sigma = 25/4, delta = 3/2, gamma = -1/2, s = 21/10 admissible.
- V074: a bounded same-order forward isomorphism L : H -> Y_H, and a common graph domain for small Lipschitz perturbations,
  REFUTED (oscillatory packet; d_x versus d_x + eps d_y); the inverse-regularity form of 6.6 is the correct statement (OPEN).
- V075: the margin perturbation of S2_CLOSURE.md 3.5(a), CONFIRMED with the coefficient 51/4 for a = 17/4 and the
  additional term ||grad h||_infinity for the change of b_+.
- V076: global membership of the normalized residual in the fractional target of order 25/4 (delta = 3/2, gamma = -1/2),
  CONFIRMED; no norm bound.
- V077: independent original-data certificates d >= 5.5752, m_a >= 0.53072, m_R >= 1.78605, CONFIRMED; hence (A),
  (H_m') and (H_m) hold, and Theorems R and C' are THEOREMS for the actual normalized modal background (Fredholm of
  index 0; injectivity OPEN). Clarification (verifier's note of 05:42Z): for the fixed-background family A_h the term
  ||grad h||_infinity of V075 is not needed (b_+ is built from grad rho~); it is needed when the coupling background
  moves, as in the moving-tail family.
- V078: the 34 source exclusions of the numerics refinement lie in the exact Q, CONFIRMED; its leaf counts REFUTED
  (359 terminal leaves).
- V079: the cylinder corner threshold s_x = 3/2 + delta A/(A+D) and an explicit frozen low-domain counterexample at
  delta = 3/2, s = 21/10, CONFIRMED; the implication from the Cartesian threshold REFUTED. The actual high inverse with
  the revised parameters is OPEN.
- V080: global (Z) for the actual field, CONFIRMED; the zeros are 0 and (+-p, 0); Lemma H1 (i), (ii) hold.
- V081: the L_fix finite section in L^2(e^{mu~}) (sigma_min >= 0.510914), reproduced as a conditional matrix
  certificate. V082: the adjoint-witness and Schur injectivity criteria and the regular-cylinder commutator and
  Garding estimates, CONFIRMED as conditional lemmas. V083: the regular-cylinder Mellin bound, CONFIRMED.
- V084: zeta in Y intersect H_base^sigma (6.6 (a)), CONFIRMED. V085: no one-order gain of the full coupling, REFUTED
  as a claim, with the packet counterexample CONFIRMED. V086: both global margins at least 5/2, CONFIRMED.
  V087: index -1 on ker J and the final scaling normalization (5.2), CONFIRMED; the unchanged onto theorem on ker J
  REFUTED.
- V088: the principal joint high-energy symbol and its margins (6.5), CONFIRMED. V089: the rank-one non-implication of
  6.6 (a), CONFIRMED. V090: the geometric radius 1e-5, CONFIRMED. V091: the torus example of 6.6 (f), CONFIRMED.
- V092: Lemma INJ-S, CONFIRMED (Hilbert-norm correction, graph conversion). V093: ||c_R|| < 0.20757, CONFIRMED.
  V094 to V100: the conditional split algebra, the axis-strip constant (39 and 25), the second-order principal and
  Mellin energies, the regular-patch conjugation and the exact angular target norm, CONFIRMED. V101: exact energy
  localization, CONFIRMED. V102: INJ-Q for S_1, CONFIRMED as a conditional theorem. V105: trace majorants and the
  radial-lift bound, CONFIRMED (values OPEN).
- V103, V104: low-to-high regularization of the selected frozen inverses in the x-axis cylinder chart and in the
  vertical remainder cofactor chart, CONFIRMED; they settle item (e) of 6.6 for the frozen corner operators only.
- Lemma H2, Theorem H: DERIVED outlines. V106: Lemma H-spec CONFIRMED as an abstract conditional theorem (with
  lambda_* = omega + 1 + 2M||C||, so that C = 0 is covered); REFUTED for a direct application with the physical
  identity shift on the free-J spaces (the cubic direction e_0 = x^2 y chi_0 is in the intended high domain and not in
  the target, and subtracting J(h) e_0 kills e_0, so no O(1/lambda) inverse bound holds); OPEN for a compatible shift
  and the actual high inverse. The restated form for the remainder block with Corollary H-spec for the jet row
  (07:01Z) is the compatible form; it is DERIVED, submitted. Remark (6): DERIVED.
- Sections 4 to 6 otherwise: DERIVED sketches; not submitted as theorems. Lemma (E) is proved in the form (E0), (E-J), (E-G) (V049 to V053).
