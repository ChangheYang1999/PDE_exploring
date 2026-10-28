# S2_L2_THEORY.md: weighted L^2 theory for the linearized S2 operator (Avenue I)

First version 2026-10-28T01:44Z (theory author); revised 2026-10-28T02:09Z for the verdicts V022 to V025, 02:41Z (single-knot weight in section 5), 02:45Z (V031, V032) 03:24Z (V041, V042; section 5.2 rewritten as Theorem C' on fully specified spaces) 03:33Z (V043 to V046) 04:10Z (V047 to V054: Theorem C' a conditional theorem, its coupling hypotheses proved for the modal background) and 04:46Z (V055 to V061; section 6 rewritten: Prop F4, the corner singularity, and the variable-order high space) and 04:55Z (V062 to V064: Lemma H1 conditional theorem, sharp source threshold, moving-tail iteration) and 05:17Z (V065, V067: cone-local
high space, Prop F4 confirmed for the frozen operator with the parity correction; Lemma Z added) 05:26Z (box certificates of the margins and of (A), computed once; high order below 13/2) and 05:33Z (V069 to V072: knot threshold, source rectangle, Lemma Z confirmed, production aggregation verified; outward-rounded decimals). Labels: THEOREM (verifier-confirmed), DERIVED (proof written here, awaiting
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
  the cell enclosures from the original data is running. With it, Theorem R is unconditional for L_fix and rho~.

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

## 5. A jet-compatible global weight and the consistent domain (5.2: Lemmas C'1 to C'4 and Theorem C' THEOREM as conditional statements, V046, V047; the coupling hypotheses (E0), (E-J), (E-G) THEOREM for the modal background, V049 to V053; so Theorem C' holds for the modal background under (A) and (H_m') alone)

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
the triangular inversion uses only its boundedness.

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

Theorem C' (THEOREM as a conditional statement, V047, on (A), (CB), (E0), (E-J), (E-G) and (H_m'); for the modal background (CB), (E0), (E-J) and (E-G) are THEOREMS, V047, V049 to V053, so only (A) and (H_m') remain). Let (H_m') be m_a := ess inf (kappa_w - b_+) > 0
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
  for m_a and 5.575203976688894 for d are reproduced), conditional on the exported cell enclosures; the original-data
  recomputation is running.
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

## 6. The high-order space: thresholds, the corner singularity and the variable-order structure (6.1 DERIVED frozen conditions; 6.2 Proposition F4 THEOREM for the frozen operator, V067; 6.3 Lemma H1 THEOREM under (Z), V063, and Lemma Z THEOREM, V071; 6.4 to 6.7 DERIVED, not theorems)

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
  77 of them are not contained in Q. Those 77 boxes are being refined; (Z) is OPEN until each refined leaf either lies
  in Q or carries a positive bound.
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
| infinity | scaled r grad | cost O(r^{k-1}) | none | DERIVED |

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

6.6 Theorem H (variable-order high inverse; DERIVED outline, OPEN as a theorem). Assume (A), (M), (Z) and injectivity
of L_red : Z -> Y (so L_red is invertible by Theorem C'). Fix eps in (0, 1/3) and N with 3 <= N < 13/2 (see the
constraint below). Let the order be
2 + eps on {Lambda <= 1 + tau} (a neighbourhood of the closed segment [0, x_P] x {0} and of S_x) and N on
{Lambda >= 2 - tau}, nondecreasing in Lambda, realized by nested cutoffs psi_0 > psi_1 > ... > psi_n = F_n(Lambda):
ordinary derivatives near the low set (in the corner, cylinder derivatives of h/r^3), conormal derivatives near the
y-axis, scaled derivatives at infinity, and weights e^{N phi} on the transition sets. Let H and Y_H be the resulting
domain and target spaces (same orders on both sides). Claim: L_red : H -> Y_H is an isomorphism with
||L_red^{-1}||_{Y_H -> H} <= K_H, and the same holds with a uniform constant for A_g = L_red + W[g].grad (and for the
moving-tail family) when ||g||_H <= r_V.
Outline. The base estimate is Theorem C' with injectivity. Each step localizes with psi_j: at a critical element inside
the region of order s_j the frozen margin of 6.5 holds (with the joint symbol at P); on the transition sets the escape
weight absorbs the commutator loss; V.grad psi_j >= 0 (6.4); and the nonlocal coupling is triangular, because
psi_{j+1} U (1 - psi_j) is smoothing and [psi_j, U] has order -1, so the step to order s_j uses only order s_j - 1 on
the larger region. Uniformity: P moves to a nearby hyperbolic repeller P_g, and (V + W).grad psi_j >= c/2 where
grad psi_j != 0 once ||D W||_infinity is small, because V.grad Lambda > c there. The order 2 + eps gives grad h in C^eps
(with decay), which is what the Lipschitz-velocity bound needs.
Not done: the energy estimates themselves (each step is a standard positive-commutator argument, but the coupling at P
and the corner arc with the jet coordinate need the joint symbol and the jet rows), explicit constants, and the
compatibility of Y_H with the residual: away from 0 and from the knot circles below, F(rho~) is smooth, and it lies in
Y_H if its corner expansion has the form of the jet plus terms of order at least 2 + eps across the axis.
Constraint from the regularity of the background (THEOREM, V069). rho~ is a degree-7 spline in t = log r with C^6
joins at its radial knots r = r_j. At the interior knot t_j = 4958764014967233/2^51 (r_j about 9.04, outside the source
x_P = 8.60) the seventh t-derivative of the exact spline coefficients jumps in the angular modes 0 and 1 (exact rational
check). Hence the sixth derivatives of F(rho~), and of its canonical axis-jet remainder, jump on a nonempty part of
every open arc of that circle away from the axes. Both functions are locally H^s there for s < 13/2 and not locally
H^(13/2). So an ordinary or equivalent conormal target of order N >= 7 across an open sector of this circle excludes the
actual residual (V069: REFUTED for smoothness away from the origin, CONFIRMED for the jump and the local threshold).
Every orbit from P to infinity crosses this circle, and the order is nondecreasing along the flow (6.4), so every order
used on the circle and upstream of it must be below 13/2. The factored H^7 control near the vertical axis used by V060 and V065 must
be replaced by a fractional order in (6, 13/2), which still embeds the cofactor in C^5; its mapping bounds and the
membership of the residual need a new proof (V069 states that the correction mapping bounds of V060 and V065 remain
valid and that forcing membership is a separate condition). The limit is a property of the trial, not of the problem: a background
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
  low/high product bound and the bounded-DW bound, embeds into Z and has a classical J.
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

1. Hypothesis (A) (positive axis rate with endpoint bounds), independently confirmed. The box certificate (section
   5.2) has verified coverage and aggregation (V072); the independent recomputation of its cell enclosures is running. (E0), (E-J), (E-G) are proved (V049 to V053); explicit values of their constants, of the constants
   of Lemma C'1 and a finite-rank split of K_eps are OPEN and are needed for item 3.
2. Independent recomputation of the cell enclosures of the margin certificates (H_m) and (H_m') (m_* >= 1.029821,
   m_a >= 0.965918; coverage and aggregation verified, V072).
3. Injectivity of L (or L_fix) on the chosen space; with Theorem R or C it is equivalent to invertibility. A
   computer-assisted route: the estimate (m_* - eps)||h|| <= ||L h|| + ||K h|| with K approximated by finite rank
   reduces injectivity to a finite-dimensional check, which is exactly the complement control a finite section lacks.
4. The high-order inverse (Theorem H of 6.6, variable order: 2 + eps near the closed segment [0, x_P] x {0}, N
   elsewhere) and the bilinear and Lipschitz bounds in the same space. Prop F4 shows that a uniform order above
   5/2 - 1/D across the x-axis segment is impossible for the frozen corner inverse (V067), so the V057 and V060 spaces
   cannot be its ranges; for the true operator this is OPEN. The mapping side of the variable-order space is proved
   (V065) with factored H^7 control near the vertical axis; because rho~ is only C^6 across a knot circle that every orbit
   crosses (V069), the orders there and upstream must be below 13/2 (6.6), so that control must be lowered to a fractional
   order in (6, 13/2).
5. Hypothesis (Z) of Lemma H1 (no zeros of V other than 0 and P; P a hyperbolic repeller), certified. Lemma Z (6.3)
   (THEOREM, V071) reduces it to source data, a bound near 0 and positive box lower bounds of |V|/r elsewhere. The source
   rectangle Q of V070 is certified (|V| >= 0.1801 |X - P| on Q, P the only zero there). The production boxes give
   |V|/r >= 10.0988 on the inner half-line and |V|/r >= 0.100068 outside 255 boxes near P; 86 boxes have a zero lower
   bound, and 77 of them are not contained in Q (V072). What remains is the refinement of these 77 boxes.

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
  conditional on the exported cell enclosures; global (Z) OPEN (77 boxes to refine).
- Lemma H2, Theorem H: DERIVED outlines.
- Sections 4 to 6 otherwise: DERIVED sketches; not submitted as theorems. Lemma (E) is proved in the form (E0), (E-J), (E-G) (V049 to V053).
