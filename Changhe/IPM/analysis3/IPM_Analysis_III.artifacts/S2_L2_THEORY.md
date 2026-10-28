# S2_L2_THEORY.md: weighted L^2 theory for the linearized S2 operator (Avenue I)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T01:44Z (theory author); revised 2026-10-28T02:09Z for the verdicts V022 to V025, 02:41Z (single-knot weight in section 5), 02:45Z (V031, V032) 03:24Z (V041, V042; section 5.2 rewritten as Theorem C' on fully specified spaces) 03:33Z (V043 to V046) 04:10Z (V047 to V054: Theorem C' a conditional theorem, its coupling hypotheses proved for the modal background) and 04:46Z (V055 to V061; section 6 rewritten: Prop F4, the corner singularity, and the variable-order high space) and 04:55Z (V062 to V064: Lemma H1 conditional theorem, sharp source threshold, moving-tail iteration) and 05:17Z (V065, V067: cone-local 06:40Z (V088 to V091: principal joint symbol margins, the geometric radius 1e-5, the non-implications) and 06:54Z (Lemma H-spec in 6.6, DERIVED) and 07:01Z (Lemma H-spec restated for the remainder block, Corollary H-spec for L_red with the jet row split off; the jet row cannot be shifted) and 07:16Z (V106: Lemma H-spec CONFIRMED as an abstract theorem, REFUTED in the direct free-J form; remark (6) on (J1), (J2)) and 07:32Z (V108: restated Lemma H-spec and Corollary H-spec CONFIRMED as conditional theorems; V109: the scalar index change, with the cutoff free-jet example) and 07:04Z (V088 to V105 in the verdict list; V103, V104 in 6.6 (e)) and 08:01Z (V110 to V118; remark (6) now proved
in the form of V112 to V118; the sharp cone sum and (H1)) and 08:14Z (V119 to V122) and 08:24Z (Lemma H2-var: the variable-order remainder space and (H2), DERIVED) and 08:31Z (V123 to V125) and 08:42Z (Lemma H3-var: the structure of (H3) on H_var, the origin-end normal family, DERIVED) and 08:53Z (V126 to V129: (H1) on X_s CONFIRMED, (H2) CONFIRMED under the order hypothesis, the five-derivative hypothesis REFUTED, the all-covector energy REFUTED; Lemma H2-ord, existence of the order function, DERIVED) and 09:40Z (V130 to V137 in 6.6 and section 9; Proposition H3-red, the reduction of (H3) on X_s to the symbolic estimate (Hs_eps), DERIVED; source margin 4.52536 by V134; H3-var items 1, 4, 5, 6 corrected) and 09:58Z (V138 to V140 in section 9; Lemma Hs-sym, the global symbol inequality, DERIVED; Proposition Hs, (Hs_eps) from Lemma Hs-sym and the calculus inputs (Q0) to (Q5), CONDITIONAL) and 10:06Z (Proposition Hs in matrix form: positivity and the log term proved, inputs reduced to (Q0), (Q1), (Q2), (Q5); sector Q = supp chi) and 10:09Z (V141 to V144: H3-red CONFIRMED conditional on (Hs_eps), Lemma Hs-sym CONFIRMED; (Q2) restated modulo compact and small errors; V145, the scalar positivity and logarithmic steps) and 10:22Z (V146 to V150: all calculus inputs of Proposition Hs CONFIRMED, including (Q1) on the maximal domain; Proposition Hs rewritten with the weakened (Q5') and the sector support correction; assembly under check) and 10:33Z (V151 to V155: Proposition Hs and (H3) CONFIRMED, the high Fredholm theorem V152, the full Kato-Ponce route REFUTED, the robust order and the C^(1,alpha) logarithm) and 11:20Z (V156 to V163: the perturbation velocity bounds, the uniform perturbed high estimate in dyadic form, generation, index 0 and the conditional uniform inverse for small transport perturbations, Theorem Hs-pert in 6.6; Lemma K CONFIRMED as a second route, with the sign correction V162) and 11:55Z (V164 to V174: the perturbed axis row, the full bordered high and low blocks and the exact moving-tail family with uniform inverses under base low injectivity, 6.7; the decoupled weight family; new 6.8 Lemma Emb and Theorem E, conditional existence) and 11:52Z (V175 to V178: Lemma Emb THEOREM, V177; Theorem E CONDITIONAL THEOREM, V178; the decoupled-family versions, V175, V176) and 12:18Z (V179 to V182 and the necessary test of (S) in the verdict list) and 13:09Z (V183 to V194 in the status of Theorem E and in the verdict list) and 13:18Z (V195 to V197 in the verdict list) and 13:27Z (V198, V199 in the verdict list) and 14:09Z (V200 to V209 in the verdict list) and 14:12Z (V210, V211) and 14:20Z (V213 to V217) and 14:34Z (V219 in the verdict list; the record range of the uniform high theory, V156 to V161 and V163 with the correction of V162) and 14:59Z (V222 to V228 in the verdict list) and 15:12Z (V232, V234 to V236 in the verdict list) and 16:06Z (review corrections V248, V250, V251, V255; V244, V242, V247, V249 labels in the verdict list) and 16:23Z (review corrections V258; V259, V261, V262) and 16:25Z (V265: V257 is a THEOREM; V264) and 16:36Z (V268: V261 is a THEOREM; V266) and 16:41Z (V270: the L2 corrections accepted; V271: V264 is a THEOREM) and 16:43Z (V272: V266 is a THEOREM, transport only) and 17:04Z (the exact Gaussian test direction, section 6) and 17:10Z (V283: the Gaussian direction is a THEOREM) and 17:53Z (V304: c[d] != 0 in the strict residual-subtracted test).
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
x^2 y direction is the only kernel, and the remainder inverse has the explicit constant 1/kappa_0 (kappa_0 about 16.541 at
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
q(0, y) > 0 for y != 0, which for the trial was first a numerical observation; the rate is now certified for the
actual field, d = V_2(0, y)/y >= 5.5752 on the whole axis, V077, so N2 holds there). Let w = |cos theta|^{-2a(t)} e^{phi(X)} near the y-axis with
a(t) smooth and phi smooth. Then near theta = pi/2,
    (1/2) V.grad log w = -a(t) V.grad log|cos theta| - a'(t) q(X) log|cos theta| + (1/2) V.grad phi,
and on the y-axis q(0, y) = V_2(0, y)/y > 0 (numerically 5.58 <= V_2/y <= 21.31 on the trial). If a'(t_1) < 0 at some
t_1, then kappa_w -> -infinity as theta -> pi/2 at r = e^{t_1}. Hence a(t) is nondecreasing along the whole y-axis:
the anisotropic factor cannot be switched off anywhere on the outgoing axis. On the incoming x-axis near 0
(q < 0), the analogous factor |sin theta|^{-2b(t)} can be decreased outward at no cost (the sign is favorable).
Proof. log|cos theta| -> -infinity, a' q < 0 at t_1, so the middle term tends to -infinity; the other terms stay
bounded, because V.grad log|cos theta| = V_1/x - q -> d_x V_1(0, y) - V_2(0, y)/y on the axis. QED.

Corollary N3 (the y-axis jet). In such a space (a >= 5/2, the endpoint allowed by N1) every element h satisfies the
weighted integrability condition int |h|^2 |cos theta|^{-2a} dX < infinity on conic neighbourhoods of the y-axis away
from 0 and infinity; in this L^2 sense h vanishes on the y-axis to order a - 1/2 >= 2. An arbitrary element need not
have a classical pointwise order of vanishing. If h has a smooth Taylor expansion in x at the axis, its x^2 term is
excluded even at a = 5/2, since int |cos theta|^{4 - 2a} dtheta diverges near theta = pi/2 (logarithmically at
a = 5/2). So the x^2 Taylor coefficient along the entire y-axis must be a separate unknown:
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

## 3. The weighted Garding-Lyapunov estimate for L_fix (DERIVED, with standard harmonic-analysis inputs; Lemmas G1 to G3 and Theorem R CONFIRMED, V023, V031)

Lemma G1 (transport identity). For any smooth positive weight w and h in C_c^infty(R^2 \ {0}),
    Re <(V.grad - 1) h, h>_w = - int kappa_w |h|^2 w,   kappa_w := b_0 + (1/2) V.grad log w.
(Integration by parts with div V = 2 c_l.)

Lemma G2 (coupling bound; CONFIRMED in V023 with the exact-matrix proof below, which also gives the bound with
eps = 0). Let a, c be continuous on R^2, tending to 0 at 0 and at infinity. For every eps > 0 there
is a compact operator K_eps on L^2 with
    Re <T g, g> <= int (b_+ + eps) |g|^2 + Re <K_eps g, g>   for all g in L^2.
Proof (the exact-matrix positivity argument of V023). Put R g := (Rt_1 g, Rt_2 g) and
H(X) := [[-c(X), a(X)/2], [a(X)/2, 0]]. H is real symmetric and its largest eigenvalue is exactly b_+(X), so
(R g)^* H (R g) <= b_+ |R g|^2 pointwise; b_+ is continuous and tends to 0 at infinity. For every continuous m
vanishing at infinity, [m, Rt_j] is compact on L^2 (approximate m uniformly by C_c^infty functions; for those the
kernel carries the factor m(X) - m(Y), so its near-diagonal part is weakly singular and the truncated rest is
Hilbert-Schmidt). Moving the coefficients a and c past one Riesz factor in T = a Rt_1 Rt_2 - c Rt_1^2 therefore changes
the form only by a compact operator:
    Re <T g, g> = int (R g)^* H (R g) dX + Re <K_1 g, g> <= int b_+ (|Rt_1 g|^2 + |Rt_2 g|^2) dX + Re <K_1 g, g>.
Moving b_+ back past Rt_j and using Rt_1^2 + Rt_2^2 = I gives Re <T g, g> <= int b_+ |g|^2 dX + Re <K_2 g, g> with
K_2 compact, which is the claim with K_eps = K_2 for every eps >= 0. No smoothness of b_+ or of a matrix square root
is used. QED.
Withdrawn first proof (historical; WITHDRAWN, V023: its claim that lambda_max(M) + eps/4 - M is smooth is false,
since lambda_max(M) is not smooth where the two eigenvalues of M meet, at the common zeros of a_eps and c_eps, and
adding the positive constant eps/4 does not change this). Approximate a, c uniformly within eps/4 by a_eps, c_eps in C_c^infty(R^2 \ {0}); the error in T has norm
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
proof gives the estimate with m_* itself, with no eps loss. It also replaces the step of the first proof of Lemma G2 above in which the
square root of lambda_max(M) + eps/4 - M is called smooth, which fails at zeros of the coefficients, by an exact matrix
quadratic inequality and compact coefficient commutators; that argument is now the proof of Lemma G2, and the first
proof is withdrawn. The weighted Riesz-product bound is proved directly by a
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
  modal background: L_fix : D_w -> L^2_P(e^{mu~}) is Fredholm of index 0 (V077; the complete
  statement with spaces is in the verifier's record). Injectivity is not addressed.

Remark R.1 (what Theorem R gives). It is the strongest inverse-type statement for the full coupled nonlocal L_fix
that the present analysis can reach in an A_2 class: closed range, finite kernel, index 0, and an explicit coercive
constant modulo a compact operator. It is not usable for the existence problem: in L^2(w) with |mu'| < 2 near 0, J is
not continuous (x^2 y is deep inside the space), c[h] is unbounded, G_bar is not in L^2(w), and no nonlinear estimate
holds. Proposition N1 shows that no A_2 weight can repair the origin. Injectivity is OPEN (no kernel element is known:
the scaling mode, the only obvious candidate, is excluded by the far weight; translations are outside class P).

Remark R.2 (the strain is not closable on the Theorem R graph; THEOREM, V032). Let w be comparable to r^eta near 0
with eta >= -4, satisfying the coefficient and tail hypotheses of V032; this covers mu~, whose eta is 1/4. Take H smooth,
annular and in class P, with c[H] = 1, and set h_n = eps_n H(X/eps_n), eps_n -> 0, for eta > -4 (at eta = -4 the input norm
of this single family stays bounded below, and h_n is instead an average of such packets over disjoint geometric
scales, V032, V251). Then J(h_n) = 0 and c[h_n] = 1, while h_n -> 0 and L_fix h_n -> 0 in L^2(w).
- Hence c has no closed extension to D_w with its graph norm.
- The full normalized operator L = L_fix + (c/3) G_bar, as a map into L^2(w) plus span{G_bar}, is not closable on D_w.
- Adding only the far compensation coordinate (KP) leaves the constrained graph nonclosed.
- So Theorem R is a statement about L_fix. The normalization must be carried by a stronger origin space: Z_cap of
  the accompanying S2_C_FUNCTIONAL.md, or Z_0 and Z of sections 2 and 5 here, where c is bounded.

## 4. Lyapunov weights reduce to conditions at the fixed points (DERIVED, sketch; historical heuristic. For the actual field the zero geometry is a THEOREM, V080, the smooth monotone order and the escape function are CONFIRMED, V130, V132, and the low Fredholm theory of Theorems R and C' is a THEOREM, V077)

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

Simpler weight with b = 0 (NUMERICAL, added 02:41Z; code/lyapunov/aniso_knot0.py and data/lyapunov/aniso_knot0.json of the accompanying artifacts).
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
- The certification of m_a on boxes was requested from the numerics team (theory author's team message 7).
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
  m_a >= 5/2 by its refinement, V086, to m_a >= 2.9270 by V197, and to m_a >= 3 by V259, which supersedes 2.9270 and
  is CONFIRMED for the exact normalized joined trial at the coefficient-margin scope), which closes
  (A) (with the qualitative endpoint estimates of V055) and (H_m'). The sharper single-team values m_a >= 0.965918,
  kappa_* >= 3.037693 and the quantitative d', M_Q, M_P constants keep their single-team status; the verifier's own finite
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

## 6. The high-order space: thresholds, the corner singularity and the variable-order structure (6.1 DERIVED frozen conditions; 6.2 Proposition F4 THEOREM for the frozen operator, V067; 6.3 Lemma H1 THEOREM under (Z), V063, Lemma Z THEOREM, V071, and (Z) CONFIRMED for the actual field, V080; 6.5 cylinder corner threshold THEOREM for the frozen operator, V079; in 6.6, Lemma H-spec and Corollary H-spec CONDITIONAL THEOREMS, V108, (H1) and (J1) to (J3) on X_s THEOREM, V126, (H2) on X_s THEOREM under the order hypothesis, V129, and the order hypothesis CONFIRMED for the actual field, V130, V132; the exact origin normal family bijective for fixed frequency, V131, and uniformly in the frequency, V133; stable principal end inverses at the vertical, horizontal and far ends, V135, V137; source margin corrected to 4.52536, V134; Proposition H3-red CONFIRMED, V141, reducing (H3) on X_s to the symbolic estimate (Hs_eps); Lemma Hs-sym THEOREM, V144; Proposition Hs and (H3) on X_s THEOREM, V151; S_1, L_ren and L_red Fredholm of index 0 on X_s THEOREM, V152; Theorem Hs-pert, the uniform high theory for small frozen-coupling transport perturbations, THEOREM, V156 to V163; in 6.7, the perturbed axis row, the full bordered high and low blocks and the exact moving-tail family, THEOREM, V166, V168 to V170; 6.8 Lemma Emb THEOREM, V177, and Theorem E CONDITIONAL THEOREM, V178; 6.4 to 6.7 otherwise DERIVED, not theorems)

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
    for s >= 5/2 - 1/D (about 2.4531), and the cofactor h/(x^2 y) = -C x^2 |y|^{beta - 1} is not in H^sigma in theta for
    sigma >= 3/2 - 1/D (about 1.4531). So no bounded inverse of L_00 from a target containing such f maps into a space that
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

6.4 Lemma H2 (order function; DERIVED outline, historical; for the actual field the order is supplied by V130 and by
Lemma H2-ord, V132). Blow up the origin (polar coordinates, r >= 0) and compactify at infinity. On
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
| P | ordinary, joint symbol | s < s_fast = (b_0 + g)/A_P (frozen source, Riesz coupling retained; sharp: a fixed smooth forcing has no H^s solution for s >= s_fast) | 3.57854758171660 < s_fast < 3.57854758172942; 2373/680 (about 3.49) is the box-uniform guaranteed value | THEOREM (V064, frozen maximal realization; V011) |
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
source threshold s_fast (about 3.5785) at P (V064) is not binding. The frozen model suggests the following geometry for the full problem,
conditional on a transfer argument that is OPEN (below); the frozen source and corner thresholds do not by themselves
prove a singularity of the full operator. The singularity of Prop F4 would sit on the stable manifold of
the origin, which is the whole segment [0, x_P), and would reach P from the left: a point (x_P - xi, y) leaves the
neighbourhood of P after a time about log(1/xi)/10.15 and then passes the corner. The y-axis, the ray (x_P, infinity)
and infinity would carry no such singularity. The proposed transfer of Prop F4 to the true operator: at scale lambda^{-1}
near 0 the coupling U[h].grad rho~ is O(lambda^{-2}) relative to the transport (grad rho~ = O(r^2), U homogeneous of
degree 0), the strain term has rank one, and V = (-A x, D y) + O(r^3); the exponents are fixed by DV(0) = diag(-A, D),
with logarithms possible at resonances. V067: the rescaling estimate is correct but does not by itself transfer the
singular coefficient of the globally selected inverse; the transfer is OPEN. It is not on the critical path, because
the design order 2 + eps of 6.6 is below the frozen thresholds and so is not affected by the outcome.

6.6 Theorem H (variable-order high regularity; DERIVED outline, historical: OPEN as a theorem when written. Its current
form is proved on X_s: the high Fredholm theorem of index 0, whose high inverse is the low inverse under low
injectivity, V152, and the bordered and moving-tail uniform inverses under base low injectivity, V166, V168 to V170,
used in Lemma Emb and Theorem E, V177, V178 (6.8). Base low injectivity (I) and all constants remain OPEN, so this is
not an unconditional inverse theorem). Assume (A), (M), (Z) and injectivity
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
Lemma H-spec (spectral-parameter continuation; CONDITIONAL THEOREM in this form, V108, the abstract version V106;
revised at 07:01Z: stated for the remainder block, with the jet row split off by the triangular form of Theorem C', because the inclusion X_H in Y_H
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
Corollary H-spec (the full operator L_red; CONDITIONAL THEOREM, V108). Let Gamma_H be a Banach space continuously included in Gamma, let
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
Why the jet row is split off and not shifted (THEOREM for the scalar row, V109). The inclusion fails on the jet
coordinate: beta = H chi(t), with chi smooth, equal to 1 near t = -infinity and 0 near +infinity, is in B but not in
Gamma, because ||beta||_Gamma = ||z/d||_{L^2(omega)} with z = chi -> 1 and omega = e^{-2 sigma t} as t -> -infinity
(a constant multiple J H is not in B at all, since B imposes z(+infinity) = 0; V109) (the same fact as H_0 not in Y, V044), so T - lambda does not map E B into Y for lambda != 0. Restricting
to B_0 = {J = 0} does not help. Write beta = H z and Phi' = 1/d; then (A - lambda) beta = H (d z' - lambda z), and with
g = gamma/(dH) the solution that vanishes at +infinity is z(t) = -int_t^infinity e^{-lambda (Phi(s) - Phi(t))} g(s) ds.
For lambda > 0 the homogeneous solution e^{lambda Phi} grows at +infinity and behaves like e^{lambda t/D} as
t -> -infinity; at lambda = 0 it is constant and is excluded by z(+infinity) = 0. Hence
A - lambda : B_0 -> Gamma is injective with the closed range {gamma : int_R e^{-lambda Phi} gamma/(dH) = 0} of
codimension one for 0 <= lambda < sigma D (lambda = 0 is V041 (8)), an isomorphism for lambda > sigma D, and not
Fredholm at lambda = sigma D (= D/4 in [5.325362610641, 5.325362610642] at the low weight sigma = 1/4; dense,
nonclosed range there, by an escaping singular sequence; V109), where the exponent lambda/D meets the weight
exponent sigma. Every weight has such a point, because the index on B_0 is -1 at lambda = 0 and 0 for large
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
two dimensions) instead of a composition bound. Correction (V153): for the full commutator [A, B.grad] with a
variable-order A this Kato-Ponce bound is false (REFUTED), because [A, B.grad] contains -(B.grad s) log<D>. The
current proof (Theorem Hs-pert) keeps that term with the transport coefficient, (W + B).grad s >= 0 (V154, V155),
and estimates only the coefficient commutator, by the square-function bound V157 or by Lemma K (V161). A uniform K_H needs C_1', C_2', omega and the low bound uniform in g
(tame estimates; V091 shows that C^1 control is not enough). (4) The lemma and the corollary give no constant by
themselves; they show that the high inverse needs (H1) to (H3) for the remainder block, (J1) to (J3) for the jet row,
and low injectivity, and nothing else. (5) The homotopy T + sC in the coupling strength, used for Theorem C', does not
work in the high space: at the source the frozen energy margin at order sigma is min(b - sigma mu, b + g - sigma A),
b = 1 + (A + mu)/2 (V011), so without the coupling (g = 0) it is negative for sigma > b/A, about 0.65, and the coercive estimate for T alone
fails at the order 2 + eps used near P (with the coupling the margin at 41/20 is min(b - sigma mu, b + g - sigma A) = 4.52536, the slow branch;
V134, which REFUTED the value about 14.8 given here earlier); a negative frozen energy
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
Status (08:01Z). This reduction is now proved on explicit spaces (V112 to V118, verdict list). (a) and (b) hold with
the exact dilation identity, four sector derivatives for H_g^6 and a Hilbert-Schmidt factorization (V112, V113); the
four derivatives follow from the base order 25/4 by the critical angular Hardy inequality (V114). The integer target is
too weak for (J1) (V115). The compatible choice is Gamma_H = a H^(25/4) with a = e^(9t/5) at the origin end and
e^(-7t/2) at infinity, B_H = {J chi + a v : v in H^(29/4)} (V117), together with the remainder target R_H = R_base + Q,
R_base = {x^2 y a u : u in H^(25/4), u even in both reflections, u(t, pi/2) = 0},
Q = {r^3 a v : v in H^(41/20), parity P, supp v in {|cos theta| >= epsilon}}, and a sector cutoff inside
{|cos theta| < epsilon}. For it (J1) holds into R_base, (J2) holds by the fractional trace gain a - 1/2 = 15/4 (V116), and
(J3) holds (V118).
Remark (7) (the sharp cone sum and (H1); the conormal mechanism below is REFUTED (V124); the failure itself is
CONFIRMED by a different mechanism (V119); the proposed replacement, a smooth order function, was then OPEN; it is
realized by X_s, V126, V130, V132). Lemma H-spec needs (H1), C_R : X_H -> Y_H, with X_H of
the same order as Y_H in the bulk (the transport does not gain). For Y_H = R_H as above this is expected to fail at the
cone boundary. Take h = r^3 a(t) chi(t) phi(theta) (|cos theta| - epsilon)_+^m with 31/20 < m < 19/4 non-integer, so
h is in Q. The boundary {|cos theta| = epsilon} consists of straight lines. For a Fourier multiplier sigma(xi) that is
homogeneous of degree 0 and even, a function f(n.X) of the normal variable alone is multiplied by sigma(n), so
U[f(n.X) g] = sigma(n) f(n.X) g + [U, g] f(n.X). The commutator has order -1 and principal part
sum_j (d_{xi_j} sigma)(D)(d_j g) f(n.X), an odd multiplier of degree -1 in the normal direction. It maps x_+^m to a
combination of x_+^(m+1) and x_-^(m+1) (with logarithms at integer exponents) whose x_- coefficient is nonzero for
generic g. Inside the sector, C_R h therefore has a singularity of type |cos theta - epsilon|^(m+1) at the boundary.
That singularity is in H^(m+3/2-) and not in H^(25/4), while every element of R_base + Q restricted to the open sector is in
the factored H^(25/4). So C_R does not map Q into R_H. Correction (V124): this mechanism is false. For h = u_+^m a(u, z), with u the normal
and z the tangential variable, m > -1 and a smooth with compact support, U[h] restricted to u < 0 extends smoothly to
u = 0. The principal normal multiplier is 1/xi, not 1/|xi|, and its antiderivative keeps the support in u > 0, so the
exterior coefficient c_- is zero. The conclusion survives through V119 below, whose packets also concentrate in the
tangential direction: the exterior smoothness holds for each fixed amplitude but without a uniform high-norm bound.
A finite chain of sharp sectors with order steps of at most one is expected to fail the packet test of V119 at each
boundary (not checked). A smooth order function avoids this. Take s = F(Lambda), with Lambda the
Conley-Lyapunov function of 6.4 and F smooth and nondecreasing, such that:
- s = 25/4 on a fixed sector {|cos theta| < epsilon_1} for all t (possible because Lambda is continuous with
  Lambda >= 2 on the y-axis, at S_y and at infinity);
- s <= 41/20 near the closed x-axis segment, S_x and the source P (below the thresholds 2.08092 at S_x and
  s_fast, about 3.5785, at P);
- V.grad s >= 0.
Order-zero pseudodifferential operators of the dilation-invariant (cylinder) calculus are bounded on the
corresponding variable-order space (Unterberger's calculus; the log terms from x-derivatives of <xi>^(s(x)) lose an
arbitrarily small power). Since s <= 25/4, it contains R_base, so (J1) and (J3) carry over. (J2) carries over if the
sector cutoff lies inside {|cos theta| < epsilon_1}, because there the space is the factored H^(25/4) and V114 gives
the embedding into R_(4,s). (H2) becomes the composition bound of remark (2) with order nondecreasing along the flow,
and the variable-order logarithmic term (V.grad s) log|xi| has the favourable sign (V088). (H1) to (H3) on this space
were OPEN at 08:14Z (on the smooth variable-order space X_s they are now THEOREMS, V126, V129, V151). Independent check (V119): at an inner cone-boundary point away from the axes, packets of scale tau and
amplitude tau^(41/20) just inside the low-order cone have bounded R_H plus T_R graph norm, while the sixth derivative
of the coupling on the high-order side grows like tau^(-59/20); the strain and axis terms are smooth errors of
amplitude O(tau^(41/20 + 2)). So (H1) fails for the sharp sum even with one transport graph derivative. The
counterexample does not apply to a smooth order function.
Lemma H2-var (the variable-order remainder space and (H2); DERIVED. Verification: the space, in the equivalent form X_s
of V126 (global variable-order bulk norm, fixed H^(25/4) cofactor norm on a vertical sector, closed zero-axis traces), and
(J1) to (J3) on it CONFIRMED (V126); (H1), C_R : X_s -> X_s bounded, CONFIRMED (V126, qualitative); the hypothesis (A_V)
with five bounded derivatives REFUTED as sufficient (V127: a C^5 lacunary coefficient for which the low solution of a
fixed smooth forcing is not in H^(25/4) for any large lambda); Claim 2 CONFIRMED in a repaired dyadic Littlewood-Paley
form, with W^(7,infinity) cylinder coefficients (which the actual field has) and W.grad s >= 0 (V129), M = 1 in the
dyadic norm and finite M in equivalent norms. The order hypothesis is supplied by Lemma H2-ord below.) It gives a
concrete space on which (J1) to (J3) carry over and proves (H2) for it; (H3) on it was then OPEN (on X_s it is a THEOREM, V151).
Coordinates. t = log r, theta, measure dt dtheta on the cylinder R x S^1, parity class P. In these coordinates
V.grad = q d_t + vartheta d_theta with q = V.X/r^2 and vartheta = V.grad(theta). The weight a(t) is that of V117
(e^(9t/5) for t <= 0, e^(-7t/2) for t >= 1, smooth and positive). Factored variable u = h/(x^2 y a), bulk variable
v = h/(r^3 a); u = v/(cos^2(theta) sin(theta)).
Assumptions.
(A_V) (WITHDRAWN as a sufficient hypothesis, V127; kept as history. The corrected hypothesis, V129: q, vartheta, q_1
     and q_2 are W^(7,infinity) cylinder coefficients, which the actual field has, vartheta = 0 on the axes, and the
     order s is smooth and monotone, W.grad s >= 0. Original form:) q, vartheta and the multipliers
     q_1 = 2 V_1/x + V_2/y + q a'/a, q_2 = q (3 + a'/a) have bounded derivatives of
     order <= 5 on R x S^1, and vartheta = 0 on the axes. (Expected from rho~ in H^(15/2-) locally, the degree-seven
     knot regularity of V069, so V in C^(6.5-), together with the expansions of V at 0 and at infinity; to be checked.)
(A_s) s is smooth on R x S^1 with bounded derivatives, 41/20 <= s <= 25/4, s = 25/4 on {|cos theta| < eps_1}, and
     V.grad s >= 0. (s = F(Lambda) of remark (7) has these properties if Lambda is chosen smooth off the critical sets
     of 6.4, smooth up to the arc r = 0 of the blow-up, and F is constant near 0, 1, 2 and 3.)
Space. Choose smooth functions psi_1, psi_2 of cos^2(theta) with psi_1 = 1 on {|cos theta| <= eps_1/2}, supp psi_1 in
{|cos theta| < eps_1}, psi_2 = 1 on {|cos theta| >= eps_1}, supp psi_2 in {|cos theta| > eps_1/2}, and
psi_1^2 + psi_2^2 >= c_0 > 0. Let O = {eps_1/2 <= |cos theta| <= eps_1} be the overlap; s = 25/4 on a neighbourhood of
O, and cos^2(theta) sin(theta) is smooth and nonvanishing there. With the left quantization
Op(m) w(x) = int e^{i x.xi} m(x, xi) w^(xi) dxi of the uniform calculus on R x S^1, put
Lambda_1 = Op(<xi>^(25/4)), Lambda_2 = Op(<xi>^(s(x))) and
     ||h||_var^2 := sum_j (||Lambda_j w_j||^2 + ||w_j||^2),   w_1 = psi_1 u, w_2 = psi_2 v
(L^2 norms in dt dtheta over one period; the periodic (toroidal) form of the uniform calculus on R^2). H_var is the
space of h in R in the parity class with finite norm; it is a Hilbert space. The axis zero of R_base is automatic: if
u is in H^(25/4) and u(t, pi/2) != 0, then int |u|^2 |cos theta|^(-9/2) dtheta = infinity near that point, so u is not
the factored variable of an element of R; with the parity, u = O(cos^2 theta) at the y-axis.
Claim 1 (the jet row). R_base is continuously included in H_var (on supp psi_2, v = cos^2(theta) sin(theta) u and
s <= 25/4), and H_var is continuously included in R (write h = sum_i psi_i g_i h with g_i = psi_i/(psi_1^2 + psi_2^2); the psi_1
piece lies in R_base, which is included in R by V118, and the psi_2 piece is of the type of Q in V118, the angular
weight being bounded on supp psi_2). (J1) and (J3) of V118 land in R_base, so they hold with
target H_var. (J2) of V116 and V118 needs the input remainder only in R_(4,s); on the sector {|cos theta| < eps_1/2}
H_var is the factored order 25/4 space with the axis zero, which embeds in R_(4,s) by V114, so (J2) holds for every
D_H in H_var if the sector cutoff of the jet row is placed inside {psi_1 = 1}. (DERIVED.)
Claim 2 ((H2); original form, historical: under the withdrawn (A_V) the proof below is not valid, V127, and the
CONFIRMED form is the dyadic one of V129 described in the Correction after the remarks). Under (A_V) and (A_s) there is omega_H < infinity such that for every lambda > omega_H the operator
T - lambda, T = T_R, maps D_H := {h in H_var : T h in H_var} bijectively onto H_var and
     ||(T - lambda)^{-1} f||_var <= (lambda - omega_H)^{-1} ||f||_var.
So (H2) of Lemma H-spec holds with M = 1 in the norm ||.||_var. (Corrected, V129: M = 1 holds for the dyadic energy
norm of V129; for an equivalent single-operator norm such as ||.||_var, (H2) holds with a finite equivalence constant
M, not automatically M = 1.)
Proof.
Step 0 (charts). For h in D_R and f = (T - lambda) h, T h = x^2 y a (T_1 u) = r^3 a (T_2 v) with
T_j = V.grad + q_j - 1 in cylinder coordinates (V is tangent to both axes, so V_1/x and V_2/y are bounded). Hence
w_j := psi_j (chart variable j) solves (T_j - lambda) w_j = psi_j f_j + vartheta psi_j'(theta) (chart variable j),
with f_1 = f/(x^2 y a), f_2 = f/(r^3 a). The last term is supported in O.
Step 1 (regularization). The chart equations hold in distributions on the whole cylinder: the axes carry no singular
part, because vartheta vanishes there (the argument of the density step of Lemma C'2). The R norm controls the w_j
only up to a power of r, so choose rho_delta(t) = (1 + delta cosh(beta t))^(-1) with beta so large that rho_delta w_j
is in L^2 for every h in R; then |d_t log rho_delta| <= beta uniformly in delta, and rho_delta w_j solves the chart
equation with the extra bounded multiplier q d_t log rho_delta (of size <= beta sup |q|). Below w_j stands for
rho_delta w_j. For 0 < delta <= 1 let J_delta = Op(<delta xi>^(-8)) and Lambda_{j,delta} = Lambda_j J_delta;
the left quantization gives Op(m(x, xi)) Op(b(xi)) = Op(m b) exactly, so Lambda_{2,delta} has the symbol
m_delta = <xi>^(s(x)) <delta xi>^(-8). For each delta it has order <= 25/4 - 8 = -7/4, and the family is bounded,
uniformly in delta, in the order-m_delta symbol class (with the log losses of the variable order:
d_x m_delta = (grad s) log<xi> m_delta). For h in D_R the w_j are in L^2 (on supp psi_1 the angular weight |cos theta|^(-9/2) of the factored variable
is >= 1), so z_j := Lambda_{j,delta} w_j lies in H^(7/4) and the L^2 energy identity
     Re <Lambda_{j,delta} (T_j - lambda) w_j, z_j> = - int (div V~/2 - Re q_j + 1 + lambda) |z_j|^2
         + Re <[Lambda_{j,delta}, V.grad] w_j, z_j> + Re <[Lambda_{j,delta}, q_j] w_j, z_j>
is valid (V~ = (q, vartheta), the divergence taken in dt dtheta).
Step 2 (the commutator symbol). By the composition formula, [Lambda_{2,delta}, V.grad] = Op(e_delta) Lambda_{2,delta}
+ R_delta with
     e_delta = s xi^T DV~ xi/<xi>^2 - 8 delta^2 xi^T DV~ xi/<delta xi>^2 - (V.grad s) log<xi>,
and R_delta of order m_delta <xi>^(-1+eps) uniformly in delta. The first two terms are bounded by (25/4 + 8) sup|DV~|.
For j = 1 the same holds without the log term. [Lambda_{j,delta}, q_j] is of order m_delta <xi>^(-1+eps).
Step 3 (sign of the log term; the only place where V.grad s >= 0 is used). The symbol (V.grad s) log<xi> is
nonnegative and in S^eps_{1,0} with bounded x-derivatives, so the sharp Garding inequality gives
Re <Op((V.grad s) log<xi>) z, z> >= - C_G ||z||^2.
Step 4 (estimate). Interpolation, ||Op(m_delta <xi>^(-1+eps)) w|| <= eta ||Lambda_{j,delta} w|| + C_eta ||w||
uniformly in delta, and steps 1 to 3 give
     Re <Lambda_{j,delta} (T_j - lambda) w_j, z_j> <= (omega_0 - lambda) ||z_j||^2 + C ||w_j||^2,
     omega_0 = sup (|div V~|/2 + |q_j|) + (25/4 + 8) sup |DV~| + C_G + eta - 1.
The overlap terms: s = 25/4 near O, so on functions supported in O, Lambda_{2,delta} and Lambda_{1,delta} differ by an
operator of order -infinity (uniformly in delta), and since psi_1^2 + psi_2^2 >= c_0 on O and cos^2(theta) sin(theta)
is smooth and nonvanishing there, ||Lambda_{j,delta}(vartheta psi_j' (chart variable j))|| <= C_O (||z_1|| + ||z_2||)
+ C (||w_1|| + ||w_2||). The order-zero parts obey the plain L^2 identity
Re <(T_j - lambda) w_j, w_j> = - int (div V~/2 - Re q_j + 1 + lambda) |w_j|^2, with the same overlap terms. With the
inner product <h, g>_delta := sum_j (<Lambda_{j,delta} w_j(h), Lambda_{j,delta} w_j(g)> + K <w_j(h), w_j(g)>) and any
fixed K > 0, Re <(T - lambda) h, h>_delta <= (omega_H - lambda) ||h||_delta^2 for every h in D_R, with omega_H
independent of delta (it contains omega_0, beta sup|q|, C_O and C/K). By Cauchy-Schwarz, (lambda - omega_H) ||h||_delta <= ||(T - lambda) h||_delta for lambda > omega_H.
Step 5 (delta -> 0). For f in H_var, ||f||_delta -> ||f||_var (norm with the same K; rho_delta -> 1 boundedly): Lambda_{j,delta} w = J_delta Lambda_j w +
[Lambda_j, J_delta] w, J_delta -> 1 strongly on L^2, and [Lambda_j, J_delta] is bounded from the order-s space to L^2
uniformly in delta, tends to 0 on smooth w, hence strongly. For h with ||h||_delta bounded, a subsequence of
Lambda_{j,delta} w_j converges weakly in L^2, and the limit is Lambda_j w_j in distributions, so
||h||_var <= liminf ||h||_delta. Hence for f in H_var and h := (T_R - lambda)^{-1} f in D_R (Lemma C'2 with the shift:
T_R - lambda is a bijection of D_R onto R for lambda > -kappa_*, h = -int_0^infinity e^{-(1 + lambda) s} f o Phi_s ds):
     ||h||_var <= liminf ||h||_delta <= (lambda - omega_H)^{-1} lim ||f||_delta = (lambda - omega_H)^{-1} ||f||_var.
Step 6 (bijectivity). h is in H_var by step 5, and T h = f + lambda h is in H_var, so h is in D_H. Injectivity on
D_H follows from D_H in D_R and Lemma C'2. QED.
Remarks. (a) Necessity of the sign. If V.grad s < 0 on an open set, -(V.grad s) log<xi> is positive and unbounded
there and no finite omega_H exists: h(X) = -int e^{-(1+lambda)s} f(Phi_s X) ds samples f downstream, so h has at X only
the regularity of f downstream. This is the transport analogue of V119, where the defect came from the coupling.
(b) The proof uses only (A_V), (A_s), the tangency of V to the axes, the parity and Lemma C'2. It does not use the
coupling, the margin certificates or the Morse structure beyond V.grad s >= 0; constant orders are a special case.
(c) omega_H is not computed; its main term is (25/4 + 8) sup |DV~| plus the overlap constant C_O. For Lemma H-spec only
finiteness matters: omega_H enters through lambda_* = omega_H + 1 + 2 ||C_R||, and (H3) in energy form at lambda = 0
gives (H3) for every lambda >= 0 at once (remark (1)).
(d) For the perturbed operators A_g of remark (3) the sign condition is stable: with s = F(Lambda) and F' = 0 near
0, 1, 2, 3, the set {F'(Lambda) > 0} is compact in the compactified blow-up and disjoint from the critical sets, so
V~.grad Lambda >= c > 0 there, and (V + W)~.grad s >= 0 whenever sup |W|/r <= c/sup |grad Lambda| (implied by a small
sup ||DW||, as in V090). The commutator step for W[g], which has only the regularity of g, needs the tame Kato-Ponce
form ||[Lambda_s, W.grad] h|| <= C (||DW||_infinity ||h||_s + ||W||_s ||grad h||_infinity) in place of the symbol
calculus (remark (3)); grad h is bounded because s >= 41/20 > 2. For a variable order this tame form is false for the
full commutator (REFUTED, V153: the term -(W.grad s) log<D>); the current proof keeps that term with the transport
coefficient, (V + W).grad s >= 0 (V154, V155), and applies a tame bound only to the coefficient commutator (V157, or
Lemma K, V161).
Correction (V127, V129). Step 3 as written needs more than (A_V): with five coefficient derivatives the order-25/4
calculus and the uniform regularizer estimate fail (V127). The verified repair (V129) replaces steps 1 to 5 by the
dyadic norm sum_j ||2^(j s(x)) Delta_j v||^2 + sum_j 2^(2 j sigma) ||Delta_j w||^2, in which differentiating 2^(j s(x))
along the flow gives the exact term -j log 2 (W.grad s) <= 0, so no sharp Garding step is needed; the coefficient
commutators use ||Delta_k W||_infinity <= C 2^(-7k) and the gap 7 - 25/4 = 3/4; the dense core keeps the zero traces.
What remains for the high inverse on H_var: (H1), boundedness of C_R on H_var (now CONFIRMED on X_s, V126, through the
identity U_1[x^2 w]/x = x U_1[w] + 2 [U_1, x] w + x^(-1) [[U_1, x], x] w, six radial Schur estimates, and the pairing of
the normalized strain with U before the inner annuli are summed), and (H3), the a priori estimate with compact error,
which needs the joint high-energy symbol margin where s is locally constant (6.5, V088) and an escape weight
e^(N G(Lambda)) (equivalent norm) on the transition sets; and low injectivity. Lemma H3-var below corrects the second
part: the margin is needed only on the characteristic set, and the ends need the normal families.
Lemma H2-ord (existence of the order function; DERIVED; the direct construction is CONFIRMED, V132). There is a real function s on the
cylinder C = R_t x S^1 with every derivative bounded, invariant under both coordinate reflections, with
41/20 = s_0 <= s <= sigma = 25/4, such that
  (a) s = sigma on {|cos theta| < eps_2} for some eps_2 > 0, and on {t >= T_inf} for some finite T_inf;
  (b) s = s_0 on a set N_0 that contains a uniform neighbourhood of the closed x-axis segments and of the sources:
      N_0 contains {|sin theta| <= beta_0, t <= t_c} and the discs {|X -+ P| <= rho_1/2}, where t_c < log x_P and
      e^(t_c) > x_P - rho_1, for some beta_0 > 0, rho_1 = 1/4;
  (c) W.grad s >= 0 everywhere, W = (q, vartheta) the cylindrical transport field.
So the order hypothesis of V126 and V129 holds, and s is at most 41/20 at S_x, along the x-axis segment and at +-P, as
the frozen thresholds of 6.5 require (2.0809 at S_x in the cylinder norm, 2.334 along the segment, 3.5785 at P).
Inputs (all verified for the actual field). (I1) W is in W^(2,infinity) and C^1 on C, tangent to the axes and
compatible with the reflections (V129, hypothesis 1). (I2) Origin end: q -> q_0 = -A cos^2 theta + D sin^2 theta, vartheta -> vartheta_0 = Sigma sin theta cos theta and
d_theta vartheta -> Sigma cos 2theta uniformly in theta as t -> -infinity. (d_theta vartheta = e_theta.DV e_theta - V.e_r/r, so
this follows from V = diag(-A, D) X + O(r^3) and DV = diag(-A, D) + O(r^2), V055.) (I3) V_1(x, 0) < 0 for
0 < x < x_P (Lemma H1 (ii) and (Z), V063, V080: no zero on the open segment, and V_1 ~ -A x near 0). (I4) On the
rectangle Q of V070 the symmetric part of DV exceeds 0.1801 I, so V.(X - P) >= 0.1801 |X - P|^2 there (V070).
No global property of the flow beyond (I3) is used.
Proof. All distances, normals and derivatives are taken in the coordinates (t, theta). Work in the first quadrant
near theta = 0 and extend everything by the two reflections.
Step 1 (a repeller block B). Since vartheta is odd in theta, vartheta(t, theta) = theta int_0^1 d_theta vartheta(t, u theta) du.
By (I2) choose t_1 with |d_theta vartheta - Sigma cos 2theta| <= Sigma/4 and q(t, theta) < 0 for t <= t_1, |theta| <= pi/8
(q_0 < 0 for tan^2 theta < A/D). Then vartheta(t, theta) >= 0.4 Sigma theta there. On [t_1, t_c], with
x_c := e^(t_c) = x_P - rho_1/2, (I3) and compactness give q(t, 0) <= -2 q_m < 0, and W in C^1 gives
|vartheta(t, theta) - theta a(t)| <= C_2 theta^2 and |q(t, theta) - q(t, 0)| <= C_1 theta, a(t) := d_theta vartheta(t, 0). Put
M := 2(||a||_inf + 1)/q_m, take psi smooth, nondecreasing, psi = 0 on (-infinity, t_1 - 1], psi' = 1 on [t_1, infinity),
0 <= psi' <= 1, and beta(t) := beta_* exp(M psi(t)), where beta_* > 0 is so small that beta <= min(pi/8, q_m/C_1, 1/(2 C_2))
on (-infinity, t_c], x_c beta(t_c) <= rho_1/4 and x_P (1 + 2M) beta(t_c)^2 < rho_1. Here C_1 = ||d_theta q||_inf and
C_2 = ||d_theta^2 vartheta||_inf/2. Let B_T := {t <= t_c, |theta| <= beta(t)} and B_P := {|X - P| <= rho_1}
(B_P lies in Q since x_P lies in the V017 bracket [p_-, p_+]). The outward normal of B_T on theta = beta(t)
is proportional to (-beta', 1), and W.(-beta', 1) = vartheta - beta' q.
- For t <= t_1: q < 0 and beta' >= 0, so W.(-beta', 1) >= vartheta(t, beta) >= 0.4 Sigma beta_*.
- For t_1 <= t <= t_c: beta' = M beta and q(t, beta) <= -q_m, so
  W.(-beta', 1) >= beta (a(t) - C_2 beta + M q_m) >= beta (a(t) + 2||a||_inf + 3/2) >= beta_*.
On the circle |X - P| = rho_1, W.(X - P)/rho_1 >= 0.1801 rho_1 by (I4) (in the plane; the cylinder normal has the same
sign). The end cap {t = t_c, |theta| <= beta(t_c)} lies in the interior of B_P (|X - P|^2 <= (rho_1/2)^2 + x_c x_P beta^2 <
rho_1^2), and along the lateral boundary |X - P|^2 is strictly decreasing in x on [x_P - rho_1, x_c] (its x-derivative
is at most -rho_1 + x_P (1 + 2M) beta^2 < 0), so each lateral boundary curve crosses the circle exactly once, near its
leftmost point, where the circle is nearly vertical and the curve nearly horizontal: the crossing is transversal. Round the two reentrant corners of B_T union B_P by fillets whose normals are
convex combinations of the two adjacent normals; W.n > 0 is convex in n, so it persists. Reflect. The result B is a
closed reflection-invariant set with C^2 boundary, n.W >= kappa_B > 0 on its boundary (uniformly, the t -> -infinity
part included), contained in {|theta| <= pi/8 or |theta - pi| <= pi/8} intersected with {t <= log(x_P + rho_1)}.
Step 2 (B is backward invariant; the exit time). Because W points strictly outward on the C^1 boundary, no backward
orbit leaves B, and a forward orbit starting outside B never enters B. For X not in B let
tau_B(X) := inf{tau >= 0 : Phi_(-tau)(X) in B} in [0, infinity]. Then tau_B(Phi_u X) = tau_B(X) + u for u >= 0, so
W.grad tau_B = 1 where tau_B is finite; {tau_B > c} is open for every c (B closed, [0, c] compact); on {tau_B < infinity}
tau_B is C^1 by the implicit function theorem at the transversal exit point, with
|grad tau_B(X)| <= exp(tau_B(X) ||DW||_inf)/kappa_B. Also tau_B(X) >= dist(X, B)/||W||_inf.
Step 3 (a C^1 Lyapunov function). Fix 0 < tau_1 < tau_2 < tau_3 < tau_4 and G smooth, nondecreasing, G = 0 on
(-infinity, tau_1], G = 1 on [tau_4, infinity], G(tau_2) <= 1/4, G(tau_3) >= 3/4, G' >= kappa_1 > 0 on [tau_2, tau_3].
Put g := G(tau_B) off B, g := 0 on B, g := 1 where tau_B = infinity. Then g is C^1 on C (it is constant near B and
on the open set {tau_B > tau_4}), reflection invariant, 0 <= g <= 1, ||grad g||_inf <= ||G'||_inf exp(tau_4 ||DW||_inf)/kappa_B,
W.grad g = G'(tau_B) >= 0, and W.grad g >= kappa_1 on the open set {1/4 < g < 3/4}, which lies in {tau_2 < tau_B < tau_3}.
g = 1 at distance >= d_4 := tau_4 ||W||_inf from B.
Step 4 (smoothing). Let g_e := g * rho_e with a reflection-invariant mollifier of radius e on C. Then g_e has all
derivatives bounded and is reflection invariant. Take e with e ||grad g||_inf < 1/24. If 1/3 <= g_e(X) <= 2/3, then
|g(Y) - g_e(X)| <= |g(Y) - g(X)| + |g(X) - g_e(X)| <= 2 e ||grad g||_inf < 1/12 on the e-ball around X, so 1/4 < g < 3/4
there, and
  W.grad g_e(X) = int [W(Y).grad g(Y) + (W(X) - W(Y)).grad g(Y)] rho_e(X - Y) dY >= kappa_1 - e ||DW||_inf ||grad g||_inf > 0
for e small. Let F be smooth and nondecreasing, F = 0 on (-infinity, 1/3], F = 1 on [2/3, infinity), and
  s := s_0 + (sigma - s_0) F(g_e).
Then W.grad s = (sigma - s_0) F'(g_e) W.grad g_e >= 0, since F' vanishes off {1/3 < g_e < 2/3}. s = sigma wherever g = 1
on the e-ball, in particular at distance >= d_4 + e from B; take tau_4 and e so small that d_4 + e < pi/24. This contains
{t >= log(x_P + rho_1) + pi/24} and the sector {|cos theta| < 1/2}, whose distance from B is at least pi/3 - pi/8 = 5pi/24
(so eps_2 = 1/2). s = s_0
on the points of B at distance >= e from its boundary, which contain the sets of (b) with beta_0 = beta_*/2 once e < beta_*/2
and e < rho_1/(2(x_P + rho_1)) (the cylinder distance from {|X - P| <= rho_1/2} to the circle is at least this). QED.
Remarks. (1) The order function is sigma on all of C except a thin neighbourhood of the closed x-axis segments and the
sources; the transition lies in the thin shell {tau_1 <= tau_B <= tau_4} just outside B, where every orbit exits once.
The only dynamical input is the block B, that is, the facts that the segment flows to 0, that the origin rates are
those of diag(-A, D) and that P is a source. (2) For t <= t_1 - 2, s(t, theta) = s_0 for |theta| <= beta_*/2 and
s = sigma for |theta| >= beta_* + pi/24 (B is the strip |theta| <= beta_* there, up to reflection, and the shell has width
below pi/24); this is the angular profile used in the normal family of Lemma H3-var, item 2. If s(t, .) converges in C^1
as t -> -infinity (expected from (I2) and Step 2, not needed here), the limit is nondecreasing in |theta| on [0, pi/2],
because vartheta_0 > 0 there.
(3) With V126 and V129 the lemma gives (H1) and (H2) of Lemma H-spec on X_s for this s; (H3) on X_s was then OPEN and is now a THEOREM (V151); low
injectivity on X_s remains OPEN.
Lemma H3-var (the structure of (H3) on H_var; DERIVED outline, not a proof; item 2 is a complete frozen computation
submitted for checking). Notation of Lemma H2-var. Sigma = A + D = 31.452175663849..., delta = 9/5,
c_x := -Sigma - delta A = -49.72348106... (zeroth-order coefficient of the bulk chart at S_x),
c_y := delta D = 38.34261079... (zeroth-order coefficient of the factored chart at S_y),
m_x = Sigma (3/2 - 41/20) + delta A = 0.97260878319, m_y = Sigma (25/4 - 1/2) - delta D = 142.50739927 (V088, V079),
m_inf = 1 + c_l/2 = 3.78768130532 (V088).
1. The plain energy form fails at S_y (CONFIRMED independently, V128, as a directional counterexample; V128 also
   notes that the packets are noncharacteristic, so (H3) as a norm estimate is not refuted). The frozen factored operator at the origin end is q d_t + vartheta d_theta + delta q
   (V088), and at theta = pi/2 one has q = D, d_theta vartheta = -Sigma, d_t q = 0. For a unit covector
   nu = (nu_t, nu_theta) the energy coefficient of the order-sigma conjugated equation is
        m_y(nu) = -Sigma/2 - delta D + sigma Sigma nu_theta^2,
   so V088 is the case nu_theta = 1, while for nu = (1, 0) the coefficient is -Sigma/2 - delta D = -54.0686986 for every
   sigma. No equivalent norm sum_j ||e^(N G) Lambda_j w_j||^2 with bounded scalar weights G therefore makes -S coercive modulo a
   compact term at S_y (as t -> -infinity, V~.grad G -> 0 there, and a sequence escaping along S_y with radial
   frequencies contradicts such an estimate), and remark (1) of Lemma H-spec cannot be used with the plain variable-order energy. The negative
   directions are elliptic for the transport: its symbol is i(D nu_t - Sigma phi nu_theta), phi = pi/2 - theta, and
   m_y(nu) > 0 iff nu_theta^2 > (Sigma/2 + delta D)/(sigma Sigma) = 0.27505 at sigma = 25/4 (|nu_theta| > 0.52445). On
   the complement |nu_t| >= 0.8514, so |D nu_t - Sigma phi nu_theta| >= 0.8514 D - 0.5245 Sigma |phi| > 0 for |phi| < 1.09.
   The coercive and elliptic regions must overlap (corrected at 09:40Z after V131's remark; m_y(1/2) = -4.9247 < 0, so
   a partition at |nu_theta| = 1/2 leaves no coercive region): for example |nu_theta| > 0.53, where m_y >= 1.1495, and
   |nu_theta| < 0.54, where |D nu_t - Sigma phi nu_theta| > 17.91 on |phi| <= 10^(-3) for the exact origin field; on the
   elliptic region the graph norm gives one derivative more. The correct high-frequency condition is a positive margin on the characteristic set
   {nu : V~(X).nu = 0} where V~(X) != 0, and in every direction at the zeros of V~ (only +-P in the open cylinder).
2. The normal family at the origin end (frozen computation; corrected after the verifier's 08:54Z remarks). As
   t -> -infinity, V~ = V~_0 + O(e^(2t)) with V~_0 = (q_0, vartheta_0), q_0 = -A cos^2 theta + D sin^2 theta,
   vartheta_0 = Sigma sin theta cos theta, and the coupling is O(e^(2t)) relative to the transport (grad rho~ = O(r^2), U
   homogeneous of degree 0; 6.5). By the parity reduce to theta in [0, pi/2]. After Fourier transform in t (dual
   variable xi real) the normal family is
        N(xi, lambda) = vartheta_0 d_theta + c(theta) + i xi q_0(theta) - lambda
   on the angular space of X_s: order s_0 = 41/20 in the bulk variable near theta = 0 (odd in theta there), the
   factored variable of order 25/4 near pi/2 (even in phi = pi/2 - theta, with the axis zero), nondecreasing order in
   between. Put nu = Re lambda,
        beta = (lambda - c_x + i xi A)/Sigma,   alpha = (c_y + i xi D - lambda)/Sigma.
   Near 0, vartheta_0 d_theta = Sigma theta (1 + O(theta^2)) d_theta and c + i xi q_0 = c_x - i xi A + O(theta^2), so the
   homogeneous solutions are theta^beta (1 + O(theta^2)); near pi/2, vartheta_0 d_theta = -Sigma phi (1 + O(phi^2)) d_phi
   and c + i xi q_0 = c_y + i xi D + O(phi^2), so they are phi^alpha (1 + O(phi^2)). A Taylor term f_j phi^j of the data at
   pi/2 has the particular solution f_j phi^j / (Sigma (alpha - j)), and a term f_j theta^j at 0 has
   f_j theta^j / (Sigma (j - beta)), modulo terms two orders higher; the indices are j in {2, 4} at pi/2 (even, axis
   zero, j < 25/4 - 1/2) and j = 1 at 0 (odd, j < 41/20 - 1/2).
   Claim: for every real xi, N(xi, lambda) is bijective whenever nu > -m_x = -0.97260878; in particular for every
   lambda >= 0.
   Proof. On (0, pi/2), vartheta_0 > 0, so N g = f is a regular first-order ODE and every solution gains one derivative
   over f in the interior; only the ends matter. Let nu > -m_x. Then Re beta = (nu - c_x)/Sigma > 41/20 - 1/2, so every
   homogeneous solution lies in the space near 0, and nu > -m_y gives Re alpha < 25/4 - 1/2, so no nonzero homogeneous
   solution lies in the space near pi/2 unless alpha is a Taylor index. The resonances alpha = 2, 4 and beta = 1 occur at
   lambda = c_y - 2 Sigma + i xi D, c_y - 4 Sigma + i xi D and c_x + Sigma - i xi A, with real parts -24.5617, -87.4661 and
   -delta A = -18.2713, all below -m_x. Injectivity: a kernel element is a multiple of the global homogeneous solution,
   which is not in the space near pi/2. Surjectivity: near pi/2 put g = sum_{j=2,4} f_j phi^j/(Sigma (alpha - j)) + g_r,
   where the remainder data r vanish to order above 25/4 - 1/2 in the H^(25/4) sense and
   g_r = -(1/Sigma) phi^alpha int_0^phi r(p) p^(-alpha-1) dp (with the O(phi^2) coefficient corrections absorbed by
   iteration); the integral converges and g_r is in the space by the Hardy (Mellin) inequality on the line
   Re = 25/4 - 1/2, since Re alpha < 25/4 - 1/2. Continue g across (0, pi/2) by the ODE. Near 0 the solution is
   C theta^beta (1 + O(theta^2)) + f_1 theta/(Sigma (1 - beta)) + (remainder solved by the Mellin inverse off the line
   Re = 41/20 - 1/2), all in the space since Re beta > 41/20 - 1/2 and beta != 1. QED for fixed xi.
   Role of the axis zero and the parity. Without the axis zero the index j = 0 enters at pi/2: at alpha = 0, i.e.
   lambda = c_y + i xi D, the constant phi^0 is in the space, so N(xi, lambda) has a one-dimensional kernel, and the
   f_0 term is resonant, so it has a one-dimensional cokernel. For fixed xi this is a discrete eigenvalue, not a failure
   of Fredholmness of N(xi, .). For the cylinder operator the union over real xi is the vertical line
   Re lambda = c_y = 38.3426, and S - lambda is not semi-Fredholm there: e^(i xi_0 t) g_0(theta) chi_n(t), g_0 in the
   kernel and chi_n unit-norm cutoffs spreading and moving to t -> -infinity, is a Weyl sequence (the O(e^(2t))
   corrections vanish in the limit), so no estimate ||h|| <= C ||(S - lambda) h|| + ||K h|| with K compact holds at
   lambda = c_y. Without the even parity the index j = 1 enters at pi/2, with the line Re lambda = c_y - Sigma = 6.8904.
   Both lines meet the path 0 <= lambda <= lambda_* of Lemma H-spec once lambda_* exceeds them. The j = 0 obstruction
   is the jet: it is the reason why the jet row is split off and inverted exactly (V109). (The earlier version of this
   item had the sign of the Taylor coefficient reversed and stated the conditions Re alpha < 2 and nu > c_y, nu > c_y -
   Sigma as thresholds; Re alpha < 2 is only the convergence condition of the integral formula from 0 for the whole
   datum, and the other two are isolated resonance lines, not half-planes.)
3. The far end. As t -> +infinity the normal operator in the bulk chart (gamma = -1/2) is c_l d_t - m_inf, and in the
   factored chart near the vertical axis the same, since vartheta d_theta log(cos^2 theta sin theta) = O(e^((k-1)t)). The
   family i xi c_l - m_inf - lambda is invertible for Re lambda > -m_inf = -3.7877. Angular derivatives commute with it;
   the angular transport is O(e^((k-1)t)) and its stretching cost tends to 0.
4. The characteristic-set margins. Away from the ends and from +-P, the escape weight e^(N G(Lambda)) adds
   N V~.grad G(Lambda) > 0 and absorbs any finite margin, including along the x-axis segment from P to S_x, which is a
   connecting orbit and not a critical element. The remaining frozen conditions are the ones already recorded:
   at +-P every direction is characteristic and the joint margin at order 41/20, coupling included, is
   min(b_P - s mu_P, b_P + g_P - s A_P) = 4.52536 (the slow branch; V134, which REFUTED the value about 14.8 stated here
   earlier; the fast branch is 15.51587; below s_fast (about 3.5785), V064); at the ends the characteristic direction is nu_theta, with margins m_x,
   m_y, m_inf, and near the ends the characteristic direction tilts continuously (nu ~ (Sigma phi, D) near S_y).
5. Assembly (the standard variable-order b-type argument, not written out). Elliptic estimate off the characteristic
   set, propagation along the lifted flow with the order nondecreasing (the log term has the favourable sign, V088),
   radial-source estimate at +-P below threshold, and inversion of the normal families at both ends, which uses the
   high-frequency estimate to absorb the O(e^(2t)) and O(e^((k-1)t)) coefficient errors, give
        ||h||_var <= C (||(S - lambda) h||_var + ||h||_E),
   E a weighted H^(s - 1) space with an extra decay e^(eps t) at -infinity and e^(-eps t) at +infinity, for every
   lambda > Lambda_0, with C locally uniform in lambda. The inclusion H_var -> E is compact (Rellich on bounded t-sets
   and the decay factors), so (H3) of Lemma H-spec holds on 0 <= lambda <= lambda_*.
   Correction (historical outline; V151, V152): this lower-order-only form is not established and is not used. The
   established estimate (Proposition Hs, V151) carries an additional compact term,
   ||h||_{X_s} <= C_s (||(S - lambda) h||_{X_s} + ||h||_{X_{s-eps}} + ||K h||_{X_s}) for 0 <= lambda <= lambda_*, which
   still gives (H3) by the absorption and compactness argument of Proposition H3-red. Also, a bound for
   lambda > Lambda_0 does not imply one on 0 <= lambda <= lambda_*; the valid route is the large-shift step of Lemma
   H-spec (S - lambda_* is an isomorphism) together with (H3) on the bounded interval [0, lambda_*].
   Correction (09:40Z): the absorption of the O(e^(2t)) first-order coefficient errors by a normal inverse is not valid as
   stated, since a small first-order coefficient is not small in the graph norm (R_eps = eps d_theta, u_n = n^(-s) chi(t)
   e^(i n theta) against Q_0 = d_t - 1). Proposition H3-red below avoids this step for the low-order end bound, and V135,
   V137 give stable principal end inverses by energy arguments.
6. What this outline does not cover (OPEN; status at 09:40Z: (i) is settled on X_s by V126, (iii) is settled for the
   exact origin normal operator by V133 and is not needed in Proposition H3-red; (ii) is the open input (Hs_eps) of
   Proposition H3-red; (iv) is open. Current status: (ii) is settled by V151, with an additional compact term; (iv),
   low injectivity, remains OPEN). (i) (H1), which is needed before S acts on H_var at all; the factored
   structure at the vertical axis: with dx rho~ = x y (2 B + x B_x) and dy rho~ = x^2 (B + y B_y) (rho~ = x^2 y B near
   the axis), the factored coupling is (2 B + x B_x) U_1[h]/x + (B + y B_y) U_2[h]/y. For h = x^2 y a u, write
   dx h = x g with g even in x; then [(-Lap)^(-1), x] = 2 dx (-Lap)^(-2) gives
   U_1[h]/x = -dy (-Lap)^(-1) g - 2 dx dy (-Lap)^(-2) g / x, where the second term is odd in x and of order -3 in g, so
   the division by x costs nothing; this suggests that U_1[h]/x has the order of u, locally and without weights. The
   power weights of the cylinder norms are far outside A_2, so the Riesz transforms must be handled modulo their
   polynomial (moment) parts, as in Theorem C', and the strain term c[h] gives the jet direction x^2 y at the origin
   and belongs to the jet row. (ii) The propagation and radial estimates with coefficients of finite regularity
   (rho~ in H^(15/2-) locally, V069); tame commutator estimates instead of the full symbol calculus. (iii) Uniformity
   of the inverse in item 2 as |xi| -> infinity (the semiclassical form of item 4 at the end). (iv) Low injectivity.
   The constants C and the norm of the compact part are not computed.
Proposition H3-red (reduction of (H3) on X_s to one symbolic estimate; CONDITIONAL THEOREM, CONFIRMED conditional on
(Hs_eps) by V141). Notation
of V126 (X_s, b, p, chi, the cofactor u = chi h/(b p), the sector |cos theta| < eps_0 where chi = 1), of V129 (the
domain D_H = {h in X_s : T_R h in X_s} and its graph-dense core) and of Lemma H-spec (S = T_R + C_R, lambda_*). The
cylinder field is W~ = (q, vartheta), so V.grad = q d_t + vartheta d_theta and T_R = V.grad - 1; beta(t) := (log b)'(t),
so beta = 3 + delta = 24/5 for t <= -1 and beta = gamma = -1/2 for t >= 1. For 0 < eps <= 1, X_{s-eps} is defined as
X_s with the orders s(.) - eps and sigma - eps, the same weights and the same parity and trace conditions (closed,
since sigma - eps > 1/2). The low norm is the doubly factored weighted L^2 norm
     N_0(h) := || h / (b(t) cos^4 theta) ||_{L^2(C, dt dtheta)},
that is, near the origin N_0(h)^2 = int |h|^2 |x|^(-8) r^(-18/5) dX; it is the plain L^2 norm of v = h/b away from
the vertical axis and the L^2 norm of sin(theta) u / cos^2(theta), the cofactor divided once more by cos^2 theta, in
the sector.
Hypothesis (Hs_eps) (the symbolic estimate; THEOREM, V151, by Proposition Hs below from the inputs V144, V146 to V150; so the claim below is a THEOREM and S_1, L_ren, L_red are Fredholm of index 0 on X_s, V152). For some eps in (0, 1] there is C_s with
     ||h||_{X_s} <= C_s ( ||(S - lambda) h||_{X_s} + ||h||_{X_{s-eps}} )   for all h in D_H, 0 <= lambda <= lambda_*.
Scope of the label (V151): the estimate established by Proposition Hs has an additional term ||K h||_{X_s} with K
compact (the Claim of Proposition Hs); the form without it is not claimed. In the proof of the claim below the extra
term is carried into the compact operator K, so the conclusion is unchanged.
Claim. (Hs_eps) implies (H3) of Lemma H-spec on X_s, with the Banach space W = X_{s-eps} (+) N_0-completion and an
explicit compact K. With (H1) and (J1) to (J3) (V126) and (H2) (V129, with the order of V130 or V132), Lemma H-spec
and Corollary H-spec then give: S_1 : D_H -> X_s and L_red : X_H^full -> Y_H^full are Fredholm of index 0.
No normal-family inversion at either end and no uniformity in the radial frequency is used.

Lemma A (Hardy, interpolation, compactness; elementary). (i) N_0(h) <= C_H ||h||_{X_s} on X_s. (ii) For every
eta > 0 there is C_eta with ||g||_{X_{s-eps}} <= eta ||g||_{X_s} + C_eta N_0(g) on X_s. (iii) For psi smooth in t
with compact support, h -> psi h is compact from X_s to X_{s-eps} and from X_s to the N_0-completion.
Proof. (i) Where |cos theta| >= eps_0, cos^(-4) theta is bounded and ||v||_{L^2} <= ||v||_{H^(s(.))}. On
|cos theta| < eps_0, v/cos^4 theta = sin(theta) u/cos^2 theta, and u(t, pi/2) = 0 (trace condition) and
d_theta u(t, pi/2) = 0 (evenness, sigma > 3/2). The one-dimensional Hardy inequality int_0^a |f/phi|^2 <= 4 int_0^a |f'|^2
for f(0) = 0, applied to d_phi u and then to u, gives ||u/phi^2||_{L^2} <= 16^(1/2) ||d_phi^2 u||_{L^2} for a.e. t,
phi = pi/2 - theta, and cos theta is comparable to phi there; integrate in t. (ii) In the dyadic realization,
||2^(j(s(.) - eps)) Delta_j v|| <= 2^(-j eps) ||2^(j s(.)) Delta_j v|| <= eta ||2^(j s(.)) Delta_j v|| when
2^(j eps) >= 1/eta, and each of the finitely many remaining blocks is bounded by 2^(j sigma) ||v||_{L^2}; the same
for u in H^(sigma - eps). Finally ||v||_{L^2} <= N_0(h), since cos^(-4) >= 1, and ||u||_{L^2} <= C N_0(h), since
|chi/p| <= C cos^(-4) theta (|sin theta| is bounded below on supp chi). (iii) Rellich on a bounded cylinder strip for
the variable order (the order gap is eps > 0); for the N_0 part, Taylor's formula with integral remainder,
u/phi^2 = int_0^1 (1 - tau) (d_phi^2 u)(t, tau phi) dtau, bounds psi u/phi^2 in H^1 of the strip by ||u||_{H^3}, and
H^1 of a bounded strip embeds compactly in L^2. QED.

Lemma B (exact energy identity in N_0; DERIVED, elementary). Put
     kappa(t, theta) := 1 + c_l - (1 + beta(t)) q(t, theta) + 4 vartheta(t, theta) tan theta.
For every g in D_H,
     - Re <T_R g, g>_{N_0} = int_C kappa |g/(b cos^4 theta)|^2 dt dtheta.
Proof. With omega := b^(-2) cos^(-8) theta, integration by parts on C gives - Re <(q d_t + vartheta d_theta - 1) g, g>_omega
= int [1 + (1/2) div_C W~ + (1/2) W~.grad log omega] |g|^2 omega. Since div V = 2 c_l and dX = e^(2t) dt dtheta,
div_C W~ = d_t q + d_theta vartheta = 2 c_l - 2 q exactly; and (1/2) W~.grad log omega = - beta q + 4 vartheta tan theta.
For g in the core of V129 there is no boundary term at the axis: near theta = pi/2, |g|^2 omega = sin^2(theta) |u|^2
/ cos^4 theta is bounded (u vanishes to second order) and vartheta = O(cos theta), because the vertical axis is
invariant (V_1 is odd in x). kappa is bounded (vartheta tan theta = sin theta (vartheta / cos theta) and
|vartheta / cos theta| <= sup |d_theta vartheta|), so both sides are continuous in the graph norm of D_H by Lemma A(i),
and the identity extends from the core to D_H. QED.

Lemma C (positive energy at both ends; DERIVED). As t -> -infinity, kappa -> kappa_-(theta) uniformly, where
     kappa_-(theta) = 1 + c_l - (4 + delta) q_0 + 4 Sigma sin^2 theta
                    = (3 Sigma/2 + delta A) cos^2 theta + (3 Sigma/2 - delta D) sin^2 theta
                    = 65.44956889 cos^2 theta + 8.83565270 sin^2 theta,
and as t -> +infinity, kappa -> 1 + c_l/2 = m_inf = 3.78768131 uniformly. Hence for every c_0 < m_inf there is T_0
with kappa >= c_0 on |t| >= T_0 - 1, and for g in D_H supported in |t| >= T_0 - 1 and Re lambda >= 0,
     (c_0 + Re lambda) N_0(g) <= N_0((T_R - lambda) g).
Proof. At the origin q -> q_0 = -A cos^2 theta + D sin^2 theta and vartheta -> vartheta_0 = Sigma sin theta cos theta
uniformly (continuity of the lifted field on the compactified cylinder, V130); at infinity q -> c_l and
vartheta -> 0 uniformly (V130: rdot/r = ell + O(r^(k-1)), thetadot = O(r^(k-1))). The second cylinder derivatives of
q and vartheta are bounded (V129), so by the interpolation inequality ||f'||_inf <= C ||f||_inf^(1/2) (||f||_inf +
||f''||_inf)^(1/2) on the circle, d_theta vartheta also converges uniformly, to d_theta vartheta_0 and to 0; hence
vartheta tan theta -> Sigma sin^2 theta and -> 0 uniformly. The closed forms follow from 1 + c_l = 1 + (D - A)/2,
D = 2A + 1 and Sigma = 3A + 1 (both coefficients are 1.5 + 6.3 A and 0.9 A - 0.3). The estimate follows from Lemma B:
(c_0 + Re lambda) N_0(g)^2 <= Re <(lambda - T_R) g, g>_{N_0} <= N_0((T_R - lambda) g) N_0(g). QED.
Why the double factor. With the weight b^(-2) |cos theta|^(-2a) on v the vertical value of the limit energy is
1 + c_l - (4 + delta) D + a Sigma = -116.973 + a Sigma, positive iff a > 3.71908 (= 2 + the vertical threshold
1.71908 of V086), while N_0 <= C ||.||_{X_s} needs a < 9/2 (v vanishes like cos^4 theta at the axis). a = 0 (the bulk
weight) gives -116.97 and a = 2 (the single cofactor) gives -54.07, the value of item 1 of H3-var; a = 4 gives 8.8357. The
horizontal value 65.45 does not depend on a. The radial exponents must be those of X_s, because Lemma A(ii) needs
N_0 to dominate the low-frequency part of X_s at both ends.

Lemma D (coupling tails; DERIVED from (8) of V126). Let psi_E^T(t) be smooth, 0 for |t| <= T - 1 and 1 for |t| >= T,
with derivatives bounded independently of T. Then N_0(psi_E^T C_R h) <= eps(T) ||h||_{X_s} with
eps(T) <= C (e^(-(2 - delta) T/2) + e^(-(1 - k) T/2)) -> 0.
Proof. In the annular matrix bounds (8) of V126 for C_ren/b and, near the axis, C_ren/(b p), restrict the output to
radii r <= e^(-T). The row sums are O(e^(-2T)) for s <= r, O(r^(2 - delta)) for r <= s <= 1 and O(r^(2 - delta)) for
s >= 1, so O(e^(-(2 - delta) T)); the column sums stay bounded. For outputs r >= e^T the rows are O(r^(k-1)) and
O(r^(k - 4 - gamma)), so O(e^(-(1 - k) T)); the strain cutoff is supported in a fixed annulus. Schur's test gives
||psi_E^T C_ren h/b||_{H^(s(.))} + ||psi_E^T chi C_ren h/(b p)||_{H^sigma} <= C eps(T) ||h||_{X_s}. Now
C_R h/(b p) = C_ren h/(b p) - Gamma_C[h]/a, and Gamma_C[h]/a is the axis trace of C_ren h/(b p) (the exact axis
identity used in V126), so ||psi_E^T Gamma_C[h]/a||_{H^2(R)} <= C ||psi~ chi C_ren h/(b p)||_{H^(5/2)}, psi~ a slightly
larger cutoff of the same type. C_R h/(b p) is even with zero trace, so the Hardy step of Lemma A(i) bounds the sector
part of N_0(psi_E^T C_R h) by its H^2 norm; away from the axis N_0 is the L^2 norm of v. QED. (The X_s-norm version of
this tail bound would need the H^sigma norm of the jet coefficient on the ends, which the trace does not give; it is
not needed here.)

Proof of the claim. Put psi_m := 1 - psi_E^T. By (Hs_eps), the triangle inequality, Lemma A(ii) with eta and the
uniform multiplier bound ||psi_E^T||_{X_s -> X_s} <= C_2,
     ||h||_{X_s} <= C_s ||(S - lambda) h|| + C_s ||psi_m h||_{X_{s-eps}} + C_s eta C_2 ||h||_{X_s} + C_s C_eta N_0(psi_E^T h).
Since (T_R - lambda) psi_E^T h = psi_E^T (S - lambda) h - psi_E^T C_R h + q (psi_E^T)' h, Lemma C (T >= T_0), Lemma A(i)
and Lemma D give
     N_0(psi_E^T h) <= c_0^(-1) [ C_H ||(S - lambda) h||_{X_s} + eps(T) ||h||_{X_s} + N_0(q (psi_E^T)' h) ].
Choose eta with C_s eta C_2 <= 1/4, then T >= T_0 with C_s C_eta c_0^(-1) eps(T) <= 1/4. Then
     ||h||_{X_s} <= C_1 ||(S - lambda) h||_{X_s} + ||K h||_W,   C_1 = 2 C_s (1 + C_eta C_H / c_0),
     K h := (2 C_s psi_m h, 2 C_s C_eta c_0^(-1) q (psi_E^T)' h) in X_{s-eps} (+) N_0,
and K is compact by Lemma A(iii) (both cutoffs have compact t-support; q is a bounded smooth multiplier). The
constants do not depend on lambda in [0, lambda_*]. QED.

Remarks. (1) The ends need neither the normal family nor its uniformity in xi (item 2 of H3-var, V131 and the
uniform statement under check): the identity of Lemma B is exact for the actual field, so the first-order
coefficient error (V - V_0).grad, which is not small in the graph norm (a standard counterexample: Q_0 = d_t - 1,
R_eps = eps d_theta, u_n = n^(-s) chi(t) e^(i n theta)), never appears; only the zeroth-order quantities q and
vartheta tan theta enter, through their uniform limits. The alternative route through the uniform exact origin normal inverse (V133)
and the stable principal end inverses at the vertical, horizontal and far ends (V135, V137) gives full-order end
estimates for the principal transport; it needs in addition the angular transitions at the origin end and the
coupling in the X_s norm. Lemmas B to D need neither, but they give only the low-order (N_0) end bound and leave the
whole high-frequency estimate to (Hs_eps). (2) The essential growth bound of
the semigroup is at least delta D + Sigma/2 = 54.07 (a computation with explicit escaping packets, not yet
checked, consistent with V128). This does not contradict (H3): the packets are elliptic, and (H3) is a real-parameter
Fredholm estimate, not a semigroup bound. (3) (Hs_eps) is the whole remaining analytic content of (H3). A formulation
without a microlocal partition: with the escape function Lambda of V130 and the order of V130 or V132
there are N, L_0 and mu > 0 with m + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu on the compactified cosphere bundle,
where m is the energy symbol (V086 (1), including the log term (W~.grad s) log|xi| >= 0 and the coupling symbol);
quantizing this inequality and bounding L_0 ||W~.grad h||^2_{X_{s-1}} through the equation gives (Hs_eps). What must
be proved is the finite-regularity quantization: for the W^(7,inf) transport coefficients, the coupling with its
H^(51/8) coefficients (surplus 1/8 over sigma, so eps <= 1/32 is a plausible target), the variable order and the
two-component norm with the cofactor division, the conjugation, positive-quantization and elliptic remainders are
bounded by a strictly lower X norm, uniformly under t-translations and for lambda in [0, lambda_*]. The bounded
commutator estimate of V129 does not give this (its constant is not compared with the margin m_x = 0.9726).
(4) Margins entering (Hs_eps) on the characteristic set {W~.nu = 0} near the critical elements: at +-P (all
covectors) min(b_P - s mu_P, b_P + g_P - s A_P) at s = 41/20, which is 4.52536 (slow branch; the fast branch is
15.51587), from the formula of V011 with the exact source parameters (A_P = 10.150725..., mu_P = 0.99999998,
g_P = 29.749491; CONFIRMED with the sharp interval (4.52536265678952, 4.52536265685856) and a sharpness packet, V134); the earlier value "about
14.8" in remark (5) of Lemma H-spec and item 4 of H3-var was wrong; at S_x m_x = 0.97261 (bulk, angular covector); at
S_y 142.507 (cofactor) and -116.973 + 25/4 Sigma = 79.603 (bulk component at order 25/4); at infinity 3.78768. Near
S_y the negative-energy covectors are elliptic, but the partition must overlap: m_y = 0 at |nu_theta| = 0.524454 and
m_y(1/2) = -4.9247, so cones |nu_theta| > 0.53 (coercive, m_y >= 1.1495) and |nu_theta| < 0.54 (elliptic,
|W~.nu| > 17.91 on |pi/2 - theta| <= 10^(-3) for the exact origin field) are used, not a partition at 1/2.

Lemma Hs-sym (global symbol inequality on the compactified cosphere bundle; THEOREM, CONFIRMED by V144 after the
correction of one decimal at S_y; elementary given V086, V088, V130, V132 and V134). Notation of Proposition H3-red. C-bar is the compactified cylinder of
V130: the radial blow-up of the origin adds the inner circle {t = -infinity} and the far circle F = {t = +infinity} is
added at infinity; W~ = q d_t + vartheta d_theta extends continuously to C-bar as a b-vector field (q rho d_rho near the
inner circle, rho = e^t). Covectors are unit b-covectors nu = (nu_t, nu_theta) in S^1, paired by
W~.nu = q nu_t + vartheta nu_theta. The critical set is Crit = {+-P} u {S_x^+-} u {S_y^+-} u F, with S_x^+- the inner
points theta = 0, pi and S_y^+- the inner points theta = +-pi/2. Lambda is the escape function of V130 (smooth on
C-bar, values 0, 1, 2, 3 on +-P, S_x, S_y, F, W~.grad Lambda > 0 on C-bar \ Crit, hence W~.grad Lambda >= 0 everywhere).
s is the order of V130 or V132 (41/20 near the closed horizontal segments from +-P to S_x^+- and on the source discs,
25/4 on |cos theta| <= 1/2 and on a far collar, W~.grad s >= 0, continuous on C-bar by the origin angular limit of
V132). The sector is Q = {|cos theta| <= eps_1}, where eps_1 <= 1/2 is fixed with supp chi in Q (chi = 1 on
|cos theta| < eps_0 < eps_1, as in Proposition H3-red), so s = 25/4 on Q and the cofactor u = chi h/(b p) lives on Q. The energy symbols are
     m_v(X, nu) = 1 + c_l - (1 + beta) q - s(X) nu^T DW~ nu - p_0(X, nu)                      (bulk v = h/b, order s),
     m_u(X, nu) = 1 + c_l - (1 + beta) q + 2 vartheta tan theta - vartheta cot theta - sigma nu^T DW~ nu - p_0(X, nu)
                                                                            (cofactor u = chi h/(b p), order sigma, on Q),
where p = cos^2 theta sin theta is the cofactor weight, DW~ is the Jacobian of (q, vartheta) in (t, theta) and p_0 is the principal symbol of the coupling (V086 (1),
transported to unit cylinder covectors; the change of variables is conformal). The zeroth-order parts are the exact
energy densities of the operators b^(-1) T_R b and (b p)^(-1) T_R (b p) in L^2(dt dtheta), by div_C W~ = 2 c_l - 2 q
(Lemma B). The logarithmic term (W~.grad s) log<xi> of a variable order (V086) is >= 0 and is not included.
Claim. Put mu_0 := m_x = Sigma (3/2 - 41/20) + delta A = 0.97260878. For every mu < mu_0 there are N >= 0 and L_0 >= 0 with
     G_v := m_v + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu   on C-bar x S^1,
     G_u := m_u + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu   on Q-bar x S^1.
Proof. (a) Continuity. q, vartheta and DW~ converge uniformly as t -> -infinity to q_0 = -A cos^2 theta + D sin^2 theta,
vartheta_0 = Sigma sin theta cos theta and their Jacobian, and as t -> +infinity to (c_l, 0) and 0 (proof of Lemma C;
the t-derivatives tend to 0 by the same interpolation argument). p_0 = O(e^(2t)) at the origin end and O(e^((k-1)t)) at
infinity (6.5), so p_0 -> 0 uniformly at both ends. vartheta tan theta = sin theta (vartheta / cos theta) is continuous
up to the vertical axis, and |vartheta / cos theta| <= sup |d_theta vartheta|. beta is constant near both ends, s
and Lambda are continuous on C-bar. Hence m_v, m_u, W~.grad Lambda and W~.nu are continuous on the compact sets
C-bar x S^1 and Q-bar x S^1.
(b) Characteristic margins over Crit. Let Sigma_0 = {(X, nu) : W~(X).nu = 0}. At +-P, W~ = 0, every nu is
characteristic, q = 0, s = 41/20, and min over nu of m_v(P, nu) = min(b_P - s mu_P, b_P + g_P - s A_P) = 4.52536 (V134;
b_P = 1 + c_l, the Jacobian is diagonal on the x-axis and p_0(P, nu) = -g_P nu_1^2). At S_x^+-, W~ = (-A, 0), the
characteristic covectors are nu = (0, +-1), DW~ = diag(0, Sigma), s = 41/20, so m_v = 1 + c_l + (4 + delta) A - (41/20)
Sigma = 3 Sigma/2 + delta A - (41/20) Sigma = m_x = 0.97261 (V086, V131). At S_y^+-, W~ = (D, 0), nu = (0, +-1),
DW~ = diag(0, -Sigma), s = sigma = 25/4: m_v = 1 + c_l - (4 + delta) D + (25/4) Sigma = -116.97305 + 196.57610 = 79.60305,
and m_u = m_v + 2 Sigma = Sigma (sigma - 1/2) - delta D = 142.50740 (V088). On F, W~ = (c_l, 0), nu = (0, +-1),
DW~ = 0, p_0 = 0, vartheta tan theta = vartheta cot theta = 0: m_v = m_u = 1 + c_l - (1 + gamma) c_l = 1 + c_l/2 =
3.78768 (V088). The minimum of these values is m_x = mu_0. The points of Crit in Q-bar are S_y^+- and F n Q-bar.
(c) Choice of N. Fix mu' in (mu, mu_0). The set E = {(X, nu) in Sigma_0 : m_v(X, nu) <= mu'} is compact and, by (b),
contains no point over Crit. Its projection B is compact in C-bar \ Crit, so c_B := min_B W~.grad Lambda > 0. With
N c_B >= mu' + max |m_v|, the function G_0 := m_v + N W~.grad Lambda satisfies G_0 >= mu' on Sigma_0: on E by the choice
of N, off E because m_v > mu' and W~.grad Lambda >= 0.
(d) Choice of L_0. The set {G_0 <= mu} is compact and disjoint from Sigma_0, so |W~.nu| >= c_U > 0 on it; take
L_0 c_U^2 >= mu + max |G_0|. Then G_v >= mu everywhere. The same steps on Q-bar x S^1 with m_u (and the larger of the
two N and L_0) give G_u >= mu. QED.
Explicit values at S_y (illustration of (d) and of remark (4) of H3-red): at S_y, W~.nu = D nu_t and
m_v(S_y, nu) = -116.97305 + 196.57610 nu_theta^2, m_u(S_y, nu) = -54.06870 + 196.57610 nu_theta^2, so
m + L_0 D^2 nu_t^2 >= mu for all nu iff L_0 D^2 >= 116.97305 + mu (bulk) and 54.06870 + mu (cofactor); with
D^2 = 453.7518 this is L_0 >= 0.2578 + mu/D^2 and L_0 >= 0.1192 + mu/D^2. The negative-energy covectors near the
radial direction at S_y are thus absorbed by the elliptic term, whose cost is of lower order by the equation (Step 3
below). This replaces the overlapping cones of remark (4) of H3-red by one inequality.

Proposition Hs (the high a priori estimate on X_s; THEOREM, V151: every input is CONFIRMED, by V146 to V150 and V144,
and the assembly below is CONFIRMED with its order of choices; with it, the high Fredholm theorem V152). Matrix form of Lemma Hs-sym: every term of G_v and G_u is a quadratic form in nu
(kappa = kappa |nu|^2, (W~.nu)^2 = nu^T W~ W~^T nu, and p_0(X, nu) = nu^T P(X) nu with the symmetric coupling matrix
P(X) = R_theta^T [[-rho_y, rho_x/2], [rho_x/2, 0]] R_theta in the cylinder covector frame, rho_x, rho_y the Cartesian
derivatives of the renormalized density at X and R_theta the rotation by theta, since the change of variables is
conformal), so G_v(X, nu) = nu^T M_v(X) nu for unit nu with
     M_v(X) := (kappa_v + N W~.grad Lambda) I - s(X) sym DW~ - P + L_0 W~ W~^T,   kappa_v = 1 + c_l - (1 + beta) q,
and Lemma Hs-sym is the pointwise matrix inequality M_v(X) >= mu I on C-bar; likewise M_u (kappa_u, sigma) >= mu I on
Q-bar. Fix mu in (0, m_x) and N, L_0 accordingly. Since supp chi is a closed subset of {|cos theta| < eps_1} (V126),
there are open sectors Q_1, Q_2 with supp chi inside Q_1, closure(Q_1) inside Q_2 := {|cos theta| < eps_1}, and s = 25/4
on Q_2. On the cylinder R x S^1 (flat metric, coordinates (t, theta)) let <D> = (1 - d_t^2 - d_theta^2)^(1/2),
R = (R_t, R_theta) = (d_t, d_theta) <D>^(-1), so that R^* R = I - <D>^(-2) and ||R w||^2 = ||w||^2 - ||w||^2_{H^(-1)}.
Let A_v = Op(e^(N Lambda) <xi>^(s(X))) and A_u = Op(e^(N Lambda) <xi>^sigma) = e^(N Lambda) <D>^sigma (uniform left
quantization; the cofactor u is extended by zero outside supp chi), w = A_v v, z = A_u u, and fix eps in (0, 1/32].
||h||^2_{X_s} is equivalent to ||v||^2_{H^(s(.))} + ||u||^2_{H^sigma} (V126), and X_{s-eps} is the space of
Proposition H3-red. The inputs, all CONFIRMED:
 (Q0) (V146) ||w|| <= C ||v||_{H^(s(.))}, ||v||_{H^(s(.))} <= C (||w|| + ||v||_{H^(s(.)-eps)}), and
      ||w||_{H^(-r)} <= C ||v||_{H^(s(.)-r)} for 0 <= r <= 1; the same for z, u and sigma. No invertibility of the bare
      left quantization is used (it may have a low-frequency kernel). Sector support: z and R z are not supported in
      supp chi, but if psi = 1 on Q_1 and supp psi is in Q_2, then ||(1 - psi) R z||_{H^K} <= C_K ||u||_{H^(sigma-eps)}
      for every K; hence for a bounded matrix field M with M >= mu I on Q_2,
           <M R z, R z> >= mu ||R z||^2 - C ||h||_{X_{s-eps}} ||h||_{X_s}.
 (Q1) (V149 on test functions, V150 on the maximal domain) Let P = B.grad + c with B, c in W^(7,inf) uniformly on the
      cylinder, a = B.grad s >= 0, and M_B = ((1/2) div B - c + N B.grad Lambda) I - s sym DB. If v and P v are in
      H^(s(.)), then for every eta > 0
           - Re <A_v P v, A_v v> >= <M_B R A_v v, R A_v v> - eta ||v||^2_{H^(s(.))} - C_eta ||v||_{H^(s(.)-eps)} ||v||_{H^(s(.))},
      and the same for A_u at the constant order sigma (a = 0). On test functions the identity holds with the term
      Re <a log<D> w, w> on the right (V149: a Taylor expansion of the coefficients to degree 6 in the kernel, the
      C^(6,1/2) remainder times the order-25/4 kernel being O(|z|^(-7/4)), integrable in two dimensions; [d_j, A] is
      separated exactly so that the actual coefficient W~.grad s of the logarithm is kept); V150 regularizes w in its
      conjugated equation (two Friedrichs commutators) and discards the logarithmic form by its lower bound
      Re <a log<D> w_n, w_n> >= - C ||w_n||^2_{H^(-1/32)} (V145) before the limit, so no graph-dense core is used. Applied
      to the bulk, B = W~, c = beta q - 1, so M_B = (kappa_v + N W~.grad Lambda) I - s sym DW~ (div_C W~ = 2 c_l - 2 q,
      Lemma B); to the cofactor, c = beta q + vartheta p'/p - 1, so (1/2) div W~ - c = kappa_u. For h in D_H both
      hypotheses hold: P_v v = (T_R h)/b, and P_u u = chi (T_R h)/(b p) + (W~.grad chi) v/p, where the last term is
      supported where p is bounded below and s = sigma.
 (Q2) (V147) For every eta > 0 there is a compact operator K_eta on X_s with
           |- Re <A_v (C_R h/b), w> + <P R w, R w>| + |- Re <A_u (chi C_R h/(b p)), z> + <P R z, R z>|
                <= (eta ||h||_{X_s} + ||K_eta h||_{X_s}) ||h||_{X_s}
      (smooth approximation of the localized H^(51/8) coefficients in multiplier norm, so that each local commutator is a
      limit of compact ones; the exact cofactor identity of V143, the compact axis row of V142 and the tail bounds of
      V140).
 (Q5') (V148) C_R is bounded on X_{s-eps}, and for every a > 0 there is C_a with, f = (S - lambda) h,
           ||W~.R w|| + ||W~.R z|| <= C_5 ||f||_{X_s} + a ||h||_{X_s} + C_a ||h||_{X_{s-eps}},
      C_5 independent of a, uniformly for lambda in [0, lambda_*] (smooth approximation of W~ in C^6 and the equation
      W~.grad v = f/b + (1 + lambda - beta q) v - C_R h/b and its cofactor analogue).
(F1) If M(X) >= mu I pointwise, then <M R w, R w> >= mu ||R w||^2 = mu ||w||^2 - mu ||w||^2_{H^(-1)}: no symbol calculus
is needed, because the symbol is a quadratic form in the covector, and ||w||_{H^(-1)} <= C ||h||_{X_{s-1}} by (Q0).
Claim. (Hs_eps) of Proposition H3-red holds with an additional term ||K h||_{X_s} on the right, K compact on X_s and
independent of lambda in [0, lambda_*] (the proof of H3-red absorbs it into its compact operator): there is C_s with
     ||h||_{X_s} <= C_s (||(S - lambda) h||_{X_s} + ||h||_{X_{s-eps}} + ||K h||_{X_s}),   h in D_H, 0 <= lambda <= lambda_*.
With Proposition H3-red, (H3) follows, and S_1 and L_red are Fredholm of index 0 (Corollary H-spec).
Proof. Let h in D_H, f = (S - lambda) h, f_v = f/b, f_u = chi f/(b p); then ||A_v f_v|| + ||A_u f_u|| <= C ||f||_{X_s}.
Write ||.|| for ||.||_{X_s}, l(h) := ||h||_{X_{s-eps}}, and C for constants that depend only on mu, N, L_0, chi, eps and
the inputs (not on eta, a, theta below).
Step 1 (bulk). f_v = (P_v - lambda) v + C_R h/b. By (Q1) with B = W~, (Q2) and lambda >= 0,
     - Re <A_v f_v, w> >= <(M_v - L_0 W~ W~^T) R w, R w> - (2 eta ||h|| + ||K_eta h||) ||h|| - C_eta l(h) ||h||,
and <L_0 W~ W~^T R w, R w> = L_0 ||W~.R w||^2 exactly, so by (F1)
     mu ||w||^2 <= ||A_v f_v|| ||w|| + L_0 ||W~.R w||^2 + (2 eta ||h|| + ||K_eta h||) ||h|| + C_eta l(h) ||h||.
Step 2 (cofactor). Since b p u = chi h, f_u = (P_u - lambda) u - (W~.grad chi) v/p + chi C_R h/(b p), and the cutoff term is
supported in Q_1 minus {|cos theta| < eps_0}, where p is bounded below and s = 25/4, so
||A_u ((W~.grad chi) v/p)|| <= C_chi ||v||_{H^(s(.))}. As in Step 1, with (Q1) for the cofactor, (Q2), and the sector
form of (Q0) for M_u (which is >= mu I on Q-bar, a superset of Q_2),
     mu ||z||^2 <= (||A_u f_u|| + C_chi ||v||_{H^(s(.))}) ||z|| + L_0 ||W~.R z||^2 + (2 eta ||h|| + ||K_eta h||) ||h||
                   + C_eta l(h) ||h||.
Step 3 (penalty). By (Q5'), L_0 (||W~.R w||^2 + ||W~.R z||^2) <= 3 L_0 (C_5^2 ||f||^2 + a^2 ||h||^2 + C_a^2 l(h)^2).
Step 4 (assembly). Put e := 3 L_0 a^2 + 2 eta + 2 theta for theta > 0. Young's inequality on ||A_v f_v|| ||w||,
(||A_u f_u|| + C_chi ||v||) ||z||, ||K_eta h|| ||h|| and l(h) ||h|| in Steps 1 to 3 gives
     (mu/2) ||w||^2 <= C ||f||^2 + e ||h||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2),
     (mu/4) ||z||^2 <= C ||f||^2 + (2 C_chi^2/mu) ||v||^2_{H^(s(.))} + e ||h||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2).
By (Q0), ||v||^2_{H^(s(.))} <= C_0 (||w||^2 + l(h)^2) and ||u||^2_{H^sigma} <= C_0 (||z||^2 + l(h)^2). Insert the first
bound for ||v||^2 into the second line (the system is triangular: the bulk inequality contains no cutoff term in u, and
the coupling enters both lines only through (Q2)) and add:
     ||h||^2 <= C' (||f||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2)) + C_4 e ||h||^2,
     C_4 = C_eq ((2 C_0/mu) (1 + 8 C_0 C_chi^2/mu^2) + 4 C_0/mu),
C_eq the constant of the norm equivalence, and C_4 does not depend on eta, a, theta. L_0 is fixed by Lemma Hs-sym before a is chosen, so a, eta and theta can be
taken with C_4 e <= 1/2. This gives the claim with K a fixed multiple of K_eta (for the chosen eta). The inequality is proved for every h in D_H
directly, since (Q1) is stated on the maximal domain (V150) and (Q0), (Q2), (Q5') hold on X_s and D_H. QED.
Remarks. (1) Nothing in Lemma Hs-sym is numerical beyond the five confirmed margins m_x, m_y (bulk 79.603, cofactor
142.507), m_inf and the source margin 4.52536; N, L_0, C_s and K are qualitative (the escape function of V130 carries no
derivative constants). mu can be any number below m_x = 0.9726. (2) The bulk margin at S_y at order 25/4 is positive
(79.60), so the bulk component is coercive on its own characteristic set there; the cofactor is needed for the space
(J1 to J3, V126), not for coercivity. (3) The three arbitrarily small high-norm errors (the matrix conversion in (Q1),
the coupling in (Q2) and the penalty in (Q5')) are what the finite coefficient regularity costs: the W^(7,inf)
transport and the H^(51/8) coupling coefficients are approximated uniformly by smooth ones, and only the smooth
approximants enter the symbolic composition, whose constants then multiply only the lower norm or the compact term.
The exact logarithmic coefficient W~.grad s >= 0 is never approximated. (4) The earlier versions of this proposition
used a lower-norm-only (Q5) and a scalar positivity step (F2) for the logarithmic term; (F2) is superseded by V150, which
discards the logarithmic form by V145 inside the proof of (Q1). (5) With V140 (||chi_+- C_R||_{X_s -> X_s} -> 0),
Lemma D of H3-red also follows from Lemma A(i). V140 reduces the full equation to a compact core with a high-norm error;
this is consistent with, but does not replace, (Hs_eps): a core estimate with a compact error requires the same global
propagation structure that Lambda encodes (the flow passes from the core through the horizontal entry of the inner
end, around the inner circle and out through the vertical exit back into the core), so a purely local core estimate
would be circular. (6) Consequence (THEOREM, V152). On the exact maximal domain D_s = D_H, S - lambda : D_s -> X_s is
Fredholm of index 0 for every lambda >= 0 (the path from lambda_* of Lemma H-spec, enlarged to contain any given
lambda); with B_H = {J chi_0 + a v : J in R, v in H^(29/4)(R)}, a = e^(-3t) b, Gamma_H = a H^(25/4)(R), the operators
L_ren and L_red = L_ren + c[.] zeta (zeta the actual moving-tail vector) are Fredholm of index 0 from B_H (+) D_s to
Gamma_H (+) X_s. A high null vector is a low null vector; under low injectivity the high operator is bijective and
its inverse is the restriction of the low inverse. No constant is computed. (7) Perturbation (status 10:30Z). The full
variable-order Kato-Ponce bound ||[A, B.grad] v|| <= C (||grad B||_inf ||v||_{H^s} + ||B||_{H^s} ||grad v||_inf) is
false (REFUTED, V153): [A, B.grad] contains -(B.grad s) log<D>, and localized packets with bounded H^s norm give a
commutator of size log n. The repair keeps (W + B).grad s as the single logarithmic coefficient: the order of V132
satisfies W.grad s >= kappa_s |grad s| (V154), so (W + B).grad s >= 0 for ||B||_inf <= kappa_s/2, and this
coefficient is discarded by V155 when it is C^(1,alpha). The global weighted bounds for the perturbation velocity
are a THEOREM (V156: B_norm[g] = c[g] (chi_0 B_0 + (1, 0)/3) + Z[g], Z[g] in H^(s(.)), B_norm[g] in C_b^(1,alpha) for
alpha < 1/20). The uniform estimate for small perturbations is a THEOREM in the square-summed (dyadic)
form (V157 to V160, Theorem Hs-pert below), with generation, index 0 and, under injectivity of S, a uniform inverse; the
single-operator variant through the tame commutator bound of Lemma K is a second confirmed route (V161, V163, with the
sign correction V162).

Theorem Hs-pert (uniform high estimate, generation, index 0 and a conditional uniform inverse for small rough transport
perturbations with frozen coupling; THEOREM, V157 to V160, constants qualitative). Notation of Proposition Hs; the order s
is the explicit repeller-block order of V130 (s = 25/4 on a neighbourhood of the vertical sector), and W~.grad s >=
kappa_s |grad s| with kappa_s > 0 (V154). G_s is the coefficient space of V156: g = J x^2 y chi_0 + b v_g, v_g in H^(s(.)),
chi_1 v_g/p in H^sigma, same parity, no trace condition, ||g||_G = |J| + ||v_g||_{H^(s(.))} + ||chi_1 v_g/p||_{H^sigma}. For g in G_s
     B_g := (U[g].e_r/r, U[g].e_theta/r) + (c[g]/3, 0),   T_g h := (V + U[g] + c[g] X/3).grad h - h,   S_g := T_g + C_R,
     D_g := {h in X_s : T_g h in X_s in distributions},
with the fixed remainder coupling C_R of the background (the coupling is frozen; T_0, S_0, D_0 are T_R, S, D_s). By V156,
B_g = c[g] E_0 + Z_g with E_0 = chi_0 (-cos 2theta, sin 2theta) + (1, 0)/3 smooth and |c[g]| + ||Z_g||_{H^(s(.))} + ||B_g||_{C_b^(1,alpha)}
+ ||chi_2 Z_g||_{H^sigma} + ||chi_2 Z_(g,theta)/cos(theta)||_{H^sigma} <= C_alpha ||g||_G for alpha < 1/20.
(i) (V157) Square-function commutator. With A_j = Op(e^(N Lambda) <xi>^(s(X)) psi_j(xi)), sum_j psi_j^2 = 1,
     (sum_j ||sum_l [A_j, B_l] d_l v||_2^2)^(1/2) <= C [||DB||_inf ||v||_{H^(s(.))} + ||B||_{H^(s(.))} ||Dv||_inf]
for B in H^(s(.)) with bounded first derivatives, and with C_E |c| ||v||_{H^(s(.))} in place of the B-terms for the smooth part
c E; for B = B_g the right side is at most C ||g||_G ||v||_{H^(s(.))}. This is not the bound for [A, B.grad] refuted in V153.
(ii) (V158) Dyadic energy. sum_j ||A_j v||^2 is equivalent to ||v||^2_{H^(s(.))} modulo the H^(s(.) - eps) norm, and for the
background transport P_0 = W~.grad + c_0
     - Re sum_j <A_j P_0 v, A_j v> = sum_j <M_0 R A_j v, R A_j v> + Re sum_j <(W~.grad s) log<D> A_j v, A_j v> + E(v),
|E(v)| <= eta ||v||^2_{H^(s(.))} + C_eta ||v||_{H^(s(.) - eps)} ||v||_{H^(s(.))}, with the matrix M_0 of (Q1). The extra term from
differentiating the cutoffs psi_j cancels pointwise because sum_j psi_j d_xi psi_j = 0. The coupling form (Q2), the penalty
(Q5') and the sector bounds of (Q0) hold in the square-summed form. On a maximal domain the sums are taken through a
finite index, the logarithmic forms are bounded below before the limit, and no graph-dense core is used.
(iii) (V159) Uniform compact-error estimate. Let eps = 1/5120 and L >= 0. There are r_* > 0, C, a Hilbert space W_* and a
compact K : X_s -> W_*, independent of g and lambda, with
     ||h||_{X_s} <= C ||(S_g - lambda) h||_{X_s} + ||K h||_{W_*},   h in D_g, ||g||_G <= r_*, 0 <= lambda <= L.
Proof outline: A_j (B_g.grad v) = B_g.grad w_j - N (B_g.grad Lambda) w_j - (B_g.grad s) A_j log<D> v + sum_l [A_j, B_(g,l)] d_l v
exactly; the logarithmic coefficient of the sum is (W~ + B_g).grad s >= 0 for small g (V154) and its form is bounded below
by V155 (alpha = 1/40); the commutators are (i); the zeroth-order and divergence terms are O(||g||_G); the penalty gets the
extra source B_g.grad v, bounded in H^(s(.) - 1) by C ||g||_G ||v||_{H^(s(.))}; the cofactor cutoff forcing stays triangular; the
absorption of Proposition Hs is repeated with a replaced by a + C_2 ||g||_G, and r_* is chosen last. The N_0 end energy of
Proposition H3-red changes by (1/2) div B_g - beta B_(g,r) + 4 tan(theta) B_(g,theta), which is O(||g||_G) (divided angular bound),
and the radial cutoff commutator has the bounded coefficient q + B_(g,r), so K is independent of g.
(iv) (V160) Generation, index 0, conditional uniform inverse. For ||g||_G <= r_* (after decreasing r_*): T_g with domain D_g
generates a strongly continuous semigroup on X_s with a growth bound uniform on the ball (positive dyadic Hilbert energy,
smooth approximation of g, flow representation, weak limits plus norm convergence); its generator domain is exactly D_g;
S_g - lambda : D_g -> X_s is Fredholm of index 0 for every lambda >= 0; and if S : D_s -> X_s is injective, then after
decreasing r_* every S_g is bijective and
     ||h||_{X_s} + ||T_g h||_{X_s} <= C ||S_g h||_{X_s},   h in D_g,
with C independent of g. By V152 the injectivity of S on D_s is the low injectivity question.
Scope. The theorem concerns the remainder block with the coupling of the fixed background. It does not include the
bordered block (jet column and axis row of L_ren and L_red under the perturbation), the moving background rho_ell of the
moving-tail formulation (V062), the low inverse for the perturbed operators, or any constant; these are the remaining
analytic inputs of the conditional existence theorem V062 besides low injectivity and the smallness conditions.
Regularity remark: the divided cofactor coefficient (p'/p) vartheta contains vartheta/cos(theta), which is W^(6,inf) and in
H^(6 + delta)_loc for delta < 1/2, not W^(7,inf); this covers the order 25/4 used in the flow argument.

Lemma K (tame coefficient commutator for the single variable-order operator; THEOREM, V161, an alternative to the square-function route of V157, not used by Theorem Hs-pert).
Notation of Proposition Hs. C = R x S^1, s smooth with bounded derivatives and 2 < s_0 <= s(X) <= s_+, Lambda smooth
and bounded with bounded derivatives, N >= 0, A = Op(a), a(X, xi) = e^(N Lambda(X)) <xi>^(s(X)) (uniform left
quantization). Delta_m (m >= 0) is a smooth inhomogeneous Littlewood-Paley partition with sum_m Delta_m = I,
S_k = sum_(m <= k) Delta_m (S_k = 0 for k < 0), Delta~_m a fattened block (Delta~_m Delta_m = Delta_m), and
w_m(X) = e^(N Lambda(X)) 2^(m s(X)). ||v||^2_{H^(s(.))} is equivalent to sum_m ||w_m Delta_m v||^2 (dyadic norm of
V126; e^(N Lambda) is bounded above and below). Let B = c E + Z, where c is a real number, E is a fixed
smooth bounded vector field with all derivatives bounded, and Z is in H^(s(.)) and in C_b^(1,alpha), 0 < alpha < 1. Put
     K_B v := sum_l [A, B_l] d_l v.
Claim. For 0 < eps <= eps_K := min(alpha/2, (s_0 - 2)/2) and v in H^(s(.)),
     ||K_B v||_2 <= C (|c| + ||DZ||_inf) ||v||_{H^(s(.))} + C (|c| + ||Z||_{H^(s(.))} + ||Z||_{C^(1,alpha)}) ||v||_{H^(s(.) - eps)},
C depending only on s, Lambda, N, E, alpha and eps. The same holds at the constant order sigma for
A_u = e^(N Lambda) <D>^sigma.
K_B does not contain the logarithmic term: A(B.grad v) = B.grad(A v) - N (B.grad Lambda) A v - (B.grad s) Op(a log<xi>) v
+ K_B v exactly (left quantization, since d_(X_l) a = a (N d_l Lambda + (d_l s) log<xi>) and d_l Lambda, d_l s depend on X
only), so the claim is consistent with V153, which REFUTES the corresponding bound for [A, B.grad].
Facts used (the kernel facts are those of the proof of V157: moderate weights, annular kernel bounds and the two
high-coefficient paraproduct types).
 (F1) Moderate weights: w_m(X)/w_m(Y) <= C (1 + 2^m d(X, Y))^M, and for k >= m - C_0,
      w_m(X)/w_k(Y) <= C 2^(-(k - m) s_0) (1 + 2^m d(X, Y))^M.
 (F2) Kernel and Bernstein bounds: the kernel of A Delta~_m is bounded by C_L w_m(X) 2^(2m) (1 + 2^m d(X, Y))^(-L) (the
      xi-derivatives of a carry no logarithm), so ||A f||_2 <= C ||w_m f||_2 for f with Fourier support in the annulus of
      Delta~_m, and ||w_m d Delta_m v||_2 <= C 2^m ||w_m Delta~_m v||_2.
 (F3) Frequency localization: a is in S^(s_+)_(1,delta) for every delta > 0 (X-derivatives cost powers of log<xi>), so
      ||Delta_j A Delta_m||_(L^2 -> L^2) <= C_R 2^(-R max(j, m)) for |j - m| > C_1 and every R.
 (F4) Hoelder blocks: ||Delta_k F||_inf <= C 2^(-k(1 + alpha)) ||F||_{C^(1,alpha)} for k >= 1, ||Delta_0 F||_inf <= C ||F||_inf.
 (F5) High-coefficient paraproduct (the two high-coefficient types of V157, with Q_j = Delta_j): for F in H^(s(.)) and
      G in L^inf, ||sum_k Delta_k F . S_(k + C_0) G||_{H^(s(.))} <= C ||F||_{H^(s(.))} ||G||_inf (by (F1), Schur and Young's
      inequality for the sequence 2^(-n s_0), n >= -C_0; s_0 > 0 is used).
Proof. For v smooth with compact support (then by density), B_l d_l v = sum_(k,m) Delta_k B_l Delta_m d_l v and
A d_l v = sum_m A Delta_m d_l v, so K_B v = sum_l sum_(k,m) [A, Delta_k B_l] Delta_m d_l v = I + II + III with
     I   = sum_l sum_m [A, S_(m - C_0 - 1) B_l] Delta_m d_l v                     (k < m - C_0, low coefficient),
     II  = sum_l A( sum_k Delta_k B_l . S_(k + C_0) d_l v )                         (k >= m - C_0, coefficient high, A outside),
     III = - sum_l sum_k Delta_k B_l . A S_(k + C_0) d_l v                          (k >= m - C_0, coefficient high, A inside).
I. Put b_m = S_(m - C_0 - 1) B_l and F_m = [A, b_m] Delta_m d_l v. The kernel of F_m is the kernel of A Delta~_m times
(b_m(Y) - b_m(X)), and |b_m(Y) - b_m(X)| <= ||D B||_inf d(X, Y), which gains 2^(-m); with (F1), (F2) and Schur,
||F_m||_2 <= C ||DB||_inf ||w_m Delta~_m v||_2 (the low-coefficient kernel bound of V157). Both A(b_m Delta_m d_l v) and b_m A Delta_m d_l v have their
Fourier mass in the m-th annulus up to the tails of (F3) (C_0 large), so ||Delta_j F_m||_2 <= C_R 2^(-R max(j, m)) 2^m
||B||_inf ||Delta~_m v||_2 for |j - m| > C_1 + 2, and almost orthogonality gives
     ||I||_2 <= C ||DB||_inf ||v||_{H^(s(.))} + C ||B||_inf ||v||_2,   ||DB||_inf <= |c| ||DE||_inf + ||DZ||_inf.
II. For the part with Z, ||A F||_2 <= C ||F||_{H^(s(.))} ((Q0), V146) and (F5) with G = d_l v give ||II_Z||_2 <= C ||Z||_{H^(s(.))} ||Dv||_inf. For the part with c E,
the blocks Delta_k E, k >= 1, are bounded in W^(R, inf) by C_R 2^(-kR), and the block k = 0 gives a product with Fourier
support in a fixed ball; hence ||II_E||_2 <= C |c| ||v||_2. Finally ||Dv||_inf <= C ||v||_{H^(s_0 - eps)} <= C ||v||_{H^(s(.) - eps)},
since s_0 - eps > 2 (two dimensions) and s(.) >= s_0.
III. By (F2), ||A S_(k + C_0) d_l v||_2 <= sum_(m <= k + C_0) ||A Delta_m d_l v||_2 <= C sum_(m <= k + C_0) 2^m a_m with
a_m = ||w_m Delta~_m v||_2 (a_0 <= C ||v||_2). By (F4), with ||B||_{C^(1,alpha)} <= |c| ||E||_{C^(1,alpha)} + ||Z||_{C^(1,alpha)},
     ||III||_2 <= C ||B||_{C^(1,alpha)} sum_k 2^(-k(1 + alpha)) sum_(m <= k + C_0) 2^m a_m <= C' ||B||_{C^(1,alpha)} sum_m 2^(-m alpha) a_m
              <= C'' ||B||_{C^(1,alpha)} ||v||_{H^(s(.) - alpha/2)},
by the Cauchy-Schwarz inequality, sum_m 2^(-m alpha) a_m <= (sum_m 2^(-m alpha))^(1/2) (sum_m 2^(-m alpha) a_m^2)^(1/2). Adding
I, II and III proves the claim. The constant-order case is the same computation with s = sigma. QED.
Remarks. (1) III is the only place where the single operator differs from the square function of Theorem Hs-pert (i): the sum
over k has no output orthogonality, and it is controlled by the Hoelder decay of the coefficient blocks (alpha > 0), not by
the H^(s(.)) norm of B. With alpha = 0 the bound of III would fail logarithmically; this is a different logarithm from the one
of V153, which is outside K_B. (2) The Hoelder norm is available for the IPM perturbation: by V156, B_norm[g] = c[g] E_0 + Z[g]
with E_0 = chi_0(t) B_0(theta) + (1, 0)/3, B_0 = (-cos 2theta, sin 2theta), and |c[g]| + ||Z[g]||_{H^(s(.))} +
||B_norm[g]||_{C_b^(1,alpha)} <= C_alpha ||g||_G for every alpha < 1/20. Hence ||K_B v||_2 <= C ||g||_G ||v||_{H^(s(.))}, and the
coefficient of the top norm is C (|c| + ||DZ||_inf) <= C ||g||_G. (3) With Lemma K the uniform estimate can be run with the
single operators A_v, A_u of Proposition Hs instead of the dyadic energy of Theorem Hs-pert (ii). This second route (a
work file of the accompanying artifacts) is CONFIRMED (V163) after one correction (V162): the change of the N_0 energy
coefficient under the perturbation is (1/2) div B - beta B_r + 4 tan(theta) B_theta (the formula of Theorem Hs-pert
(iii)); the literal formula -(1/2) div B - (1/2) B.grad log omega + d first written for it has the opposite sign and is
REFUTED (V162; a constant radial field B = (b_0, 0) on the outer end, beta = -1/2, gives b_0/2, not -b_0/2). The error
does not affect the estimate, which uses only the bound |change| <= C ||g||_G. (4) Lemma P (variable-order products,
||A_r (d f)||_2 <= C ||d||_inf ||f||_{H^(r(.))} + C (|c| + ||d_Z||_{H^(r(.))}) ||f||_inf + C |c| ||f||_2 for r(.) = s(.) and
s(.) - 1) is also a THEOREM (V161).

Outline. The base estimate is Theorem C' with injectivity. Each step localizes with psi_j: at a critical element inside
the region of order s_j the frozen margin of 6.5 holds (with the joint symbol at P); on the transition sets the escape
weight absorbs the commutator loss; V.grad psi_j >= 0 (6.4); and the nonlocal coupling is triangular, because
psi_{j+1} U (1 - psi_j) is smoothing and [psi_j, U] has order -1, so the step to order s_j uses only order s_j - 1 on
the larger region. Uniformity: P moves to a nearby hyperbolic repeller P_g, and (V + W).grad psi_j >= c/2 where
grad psi_j != 0 once ||D W||_infinity is small, because V.grad Lambda > c there. The order 2 + eps gives grad h in C^eps
(with decay), which is what the Lipschitz-velocity bound needs.
Not done in this outline (historical; the energy estimates are now proved on X_s, Proposition Hs and (H3), V151, the
high Fredholm theorem, V152, and the uniform perturbed versions, V156 to V163; explicit constants remain OPEN): the
energy estimates themselves (each step is a standard positive-commutator argument, but the coupling at P
and the corner arc with the jet coordinate need the joint symbol and the jet rows) and explicit constants. Residual
membership is settled (THEOREM, V076, 05:44Z): F(rho~)/[p A_(delta,gamma)] lies in cylinder H^sigma for 0 < delta < 2,
gamma > 2k - 1 and sigma < 13/2, by the exact cofactor identity F/p = (2V_1/x + V_2/y - 1) a + q a_t + v a_theta, which
extends across both axes; F/p = O(r^2) at 0 (the constant -2A + D - 1 vanishes) and O(r^(2k-4)) at infinity (ell k = 1).
So F(rho~) belongs to Y intersected with the base target of order 25/4, delta = 3/2, gamma = -1/2, scalar coordinate 0
(the proof covers 0 < delta < 2, so also delta = 9/5),
and to the larger cone-bulk sum target of V073. Y_H of this section has order 2 + eps near the segment and 25/4
elsewhere, the same delta and gamma, and bounded escape weights, so it contains F(rho~) (verifier's note of 05:39Z).
This is membership; at V076 (05:44Z) no norm bound was certified. Current state: in an explicitly fixed equivalent
norm on the high target Y_full of Theorem E (weight a_* = e^(9t/5) (1 + e^t)^(-53/10), a fixed angular cutoff and a
fixed Littlewood-Paley normalization, V182) the actual residual satisfies 38666592266 < eta_* < 6.321e129 (lower
bound V192, from the scalar axis summand; upper bound V182, a deliberately loose majorant with
||F/(r^3 p a_*)||_(H^(25/4)) < 1.195e93). These loose bounds do not check (S) (Theorem E, status of the hypotheses).
Constraint from the regularity of the background (THEOREM, V069). rho~ is a degree-7 spline in t = log r with C^6
joins at its radial knots r = r_j. At one specified interior knot, t_j = 4958764014967233/2^51 (r_j about 9.04, outside the source
x_P = 8.60), the seventh t-derivative of the exact spline coefficients jumps in the angular modes 0 and 1 (exact rational
check); V069 concerns this knot only and proves nothing about the other radial knots. Hence the sixth derivatives of
F(rho~), and of its canonical axis-jet remainder, jump across that circle by the nonzero finite angular jump function
of V069 (built from the mode-0 and mode-1 jumps). That function is analytic in theta, so its zeros are isolated and
the jump is nonzero on a nonempty part of every open arc of that circle away from the axes; the statement concerns
this one circle, not every circle. Both functions are locally H^s there for s < 13/2 and not locally
H^(13/2). So an ordinary or equivalent conormal target of order N >= 7 across an open sector of this circle excludes the
actual residual (V069: REFUTED for smoothness away from the origin, CONFIRMED for the jump and the local threshold).
Every orbit from P to infinity crosses this circle, and the order is nondecreasing along the flow (6.4), so every order
used on the circle and upstream of it must be below 13/2. (In the final spaces the high correction cofactor has
order 25/4 in X_s; only the one-dimensional lifted axis coordinate, v in H^(29/4)(R) in B_H, a function of t alone on
the domain side, has order 29/4.) The factored H^7 control near the vertical axis used by V060 and V065 is
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
  assuming the positive axis rate, certified by V077): with ell = ell(h) fixed by n(ell) = c[h], B(ell) = F_ell(rho_ell) - n(ell) H_0 and
  M(ell) = H_0 + (B(ell) - B(ell_0))/n(ell) (cubic coefficient 1), the operator
  A_h g = (ell(h) X + U[rho_ell(h)] + U[h]).grad g - g + U[g].grad rho_ell(h) + c[g] M(ell(h)) maps the high space into
  Y and F_ell(h)(rho_ell(h) + h) = f_0 + A_h h exactly. Because c[d] + c[z] = 3 delta ell, the difference is
  (A_h1 - A_h0) g = W[d].grad g + W[z].grad g + U[g].grad z + c[g](m_1 - m_0), so
  ||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_{X0} ||g||_high; every power of log r is included. Existence follows from
  uniform right inverses R_v : Y_H -> H_high with K_H ||f_0||_{Y_H} <= r, a low estimate ||g||_{X0} <= K_L ||A_v g||_Y and
  K_L C K_H ||f_0||_{Y_H} < 1; final rescaling restores J = 1 if |J(h)| < 1. None of these inverse hypotheses was proved at V062; the uniform inverses are now proved
  under base low injectivity (V166, V168 to V170; Theorem E, V178), and base low injectivity and the constants remain
  OPEN.
- Quasilinear two-norm scheme (fixed tails, for orientation): h_{n+1} = -A_{h_n}^{-1} F(rho~), so differences satisfy
  A_{h_n}(h_{n+1} - h_n) = -W[h_n - h_{n-1}].grad h_n, a low-times-high product (V057 structure). The iteration
  contracts in the low norm if K_L C_B K_H ||F||_{Y_H} < 1 and stays in the high ball if K_H ||F||_{Y_H} <= r_V, with
  K_L the low inverse bound, C_B the bilinear constant and K_H the uniform high bound. The moving tails and the scalar
  normalization enter through the parameter family (S2_CLOSURE.md 3.4).
- Uniform high theory (THEOREM, V156 to V161 and V163 with the sign correction of V162, Theorem Hs-pert in 6.6). For the frozen-coupling remainder operators
  S_g = (V + U[g] + c[g] X/3).grad - 1 + C_R with ||g||_G <= r_* the high estimate, generation, Fredholm index 0 and,
  under injectivity of S_0, a uniform inverse ||h|| + ||T_g h|| <= C ||S_g h|| hold on the maximal domains D_g. In the
  moving-tail operator A_h of V062 this is the transport part with the background fixed at rho_ell0.
- Bordered and moving-tail perturbation (THEOREM, V166, V168 to V170). (P1) The axis trace of the perturbation velocity,
  tau_g(t) = U_2[g](0, e^t) e^(-t), is c[g] chi_0 + e_g with ||e_g||_{H^(31/4)} + ||chi_- e_g/a||_{H^(31/4)} + |c[g]| <= C ||g||
  (the trace gains 3/2 derivative: the axis kernel has squared L^2 norm 3/(8|eta|^3)); the perturbed axis row is
  A_g = A + (tau_g + c/3) d_t + (c - tau_g - 2 tau_g'), with ||A_g - A||_{B_H -> Gamma_H} <= C ||g||, and A_g is an
  isomorphism on a small ball (V166). The lift error difference G_g - G_0 : B_H -> X_s is O(||g||) with zero cofactor
  trace; the full high block on B_H (+) D_g with fixed coupling and a fixed rank-one vector is Fredholm of index 0, has a
  fixed compact error map (Gamma_C h, c[h], K_R u), and has a uniform inverse if the base full operator is injective
  (V168). (P4) The same on the low spaces: B = J chi_0 + H^1(G); Err difference x^2 y cos^2(theta) [K_1 beta' + K_0 beta]
  with |K_0| <= C ||g|| min(e^(delta t), 1); the weight change kappa_g - kappa_w = c/3 + (mu'/2) B_r + (17/4) tan(theta) B_theta
  is O(||g||), so the margin stays >= 5/4; Fredholm index 0, fixed compact error and a uniform low inverse under base
  injectivity (V169). (P2) For the exact moving-tail family A_h of V062 with max(k, 1/ell) < q_* < 1/4: the tail velocity
  has all-order coefficient bounds O(|ell - ell_0|) (O(r^2) after the strain at 0, O(r^(q_* - 1)) at infinity) although
  z_ell is not in G_s; 3(ell(h) - ell_0) = c[h] + c[z] makes the transport V + W[h] + W[z]; A_h = T_total + C_ren,0 +
  c[.] zeta_0 + D_h with ||D_h|| <= C ||h|| on both realizations; the residual family B(ell) and m(ell) are smooth into the
  high target Y_full (two end cancellations, knot ceiling 13/2); and both realizations are Fredholm of index 0 with
  uniform inverses under base low injectivity, the inverses agreeing on Y_full (V170). Not covered: base injectivity,
  any numerical radius or constant.
- Decoupled weight family (THEOREM, V171 to V174). With inner radial exponent 17/2, outer exponent 37/20 and angular
  exponent a in [18/5, 4], the low margin is at least 1.10534 (V171, original-data enclosure), the low realization has a
  closed cubic coefficient, compact axis row and Fredholm index 0, the high spaces embed into it (V172), a uniform third
  axis derivative fails for a <= 4 (V173, replaced by a source-scale split), and ||F||_(Y_a) < 485.632 (V174, a low
  norm). Low injectivity in these spaces would serve equally well.

6.8 Conditional existence (Lemma Emb THEOREM, V177; Theorem E CONDITIONAL THEOREM, V178). The text is the audited
statement; the scope clarifications of the verification and the extension to the decoupled low spaces follow it.
Lemma Emb (embeddings of the high full spaces; THEOREM, V177). Notation: sigma = 25/4, delta = 9/5,
gamma = -1/2, b = e^((3+delta)t) far left and e^(gamma t) far right, a = e^(-3t) b, p(theta) = cos^2(theta) sin(theta),
E beta = x^2 y beta(log r) = r^3 p(theta) beta(t). B_H = {J chi_0 + a v : v in H^(29/4)(R)}, Gamma_H = a H^sigma(R),
X_s = {h : v = h/b in H^(s(.)), u_X = chi h/(b p) in H^sigma, zero vertical trace}, s_min = 41/20, H_full = B_H (+) X_s,
Y_full = Gamma_H (+) X_s. Low spaces as in the moving-tail iteration: w = |x|^(-17/2) max(1, r)^(29/4), R = L^2_P(w dX),
G = L^2(e^(-t/2) dt on t < 0, e^(27t/4) dt on t > 0), B = {J chi_0 + w_0 : w_0, w_0' in G}, X0 = E B (+) R, Y = E G (+) R.
H_high^sigma = H_base^sigma + Q is the high space of the low/high product theorem (exponents 1/4 < delta < 2, gamma < -3/8,
sigma > 6, s > 2).
Claims. The following inclusions are continuous:
 (a) Gamma_H in G and B_H in B, hence Y_full in Y;
 (b) X_s in R, and for every coefficient perturbation B of the uniform high theory, X_s in the maximal low domain
     D_L = {u in R : (T + B.grad) u in R}; hence H_full in X0 and in the low graph domain of each perturbed operator;
 (c) H_full in H_high^(25/4), with the bulk order s = 41/20 in Q.
Proof. (a) For f = a phi: integral over t < 0 of |a phi|^2 e^(-t/2) = integral e^((2 delta - 1/2) t) |phi|^2, with
2 delta - 1/2 = 31/10 > 0; over t > 0 the weight is e^(-7t) e^(27t/4) = e^(-t/4). For beta = J chi_0 + a v, w_0 = a v and
w_0' = a (v' + (a'/a) v) with a'/a bounded, so ||w_0||_G + ||w_0'||_G <= C ||v||_(H^1).
(b) dX = r^2 dt dtheta. For h = b v: |h|^2 w dX = |v|^2 b^2 r^(-13/2) max(1, r)^(29/4) |cos(theta)|^(-17/2) dt dtheta. The radial
factor is e^((6 + 2 delta - 13/2) t) = e^(31t/10) on the left and e^(-t - 13t/2 + 29t/4) = e^(-t/4) on the right. The angular
factor is bounded off the vertical sector. On the sector h = b p u_X, and u_X is even about the vertical axis with zero
trace there, so u_X = cos^2(theta) u~ with sup_theta |u~(t, .)| <= C ||u_X(t, .)||_(H^3_theta); then |h|^2 |cos|^(-17/2) =
b^2 |cos|^(-1/2) sin^2 |u~|^2, integrable in theta, and integral dt ||u_X(t, .)||^2_(H^3_theta) <= ||u_X||^2_(H^sigma).
For the domain: T_0 h = b P_v v on the bulk and b p P_u u_X on the sector (the conjugated operators of the high theory),
with P_v v in H^(s(.) - 1) in L^2 and P_u u_X in H^(sigma - 1) = H^(21/4) in C^2 uniformly in t. The background field is
tangent to the vertical axis, so P_u u_X has zero trace there (u_X = 0 and d_t u_X = 0 on the axis, vartheta = 0 there), and
it is even; the same computation gives T_0 h in R. For a perturbation B the extra term is b p (B.grad u_X + d_u u_X),
d_u = beta B_t + (p'/p) B_theta, which is again even, has zero vertical trace (B_theta = O(cos theta), u_X = d_t u_X = 0),
and lies in H^(sigma - 1) by the sector bounds of the velocity theorem (chi Z and chi Z_theta/cos(theta) in H^sigma); the
bulk part is bounded in L^2 by ||B||_(C^1) ||v||_(H^1). Hence X_s in D_L, with norm bounds uniform on the ball.
(c) Choose a fixed angular cutoff chi' with chi' chi = chi' (supported where the cofactor is defined) and 1 - chi' supported
in |cos(theta)| >= epsilon. Then
     h = p_phys [a (chi' u_X)] + b [(1 - chi') v],   p_phys = x^2 y = r^3 p(theta), so p_phys a = p(theta) b.
The first term is in H_base^sigma with u = chi' u_X in H^sigma(R x S^1), even under both reflections (h and p have the same
parity); the second is in Q with s = 41/20 > 2 (Q carries no radial restriction and its b is our b; 1/4 < 9/5 < 2,
-1/2 < -3/8). For the scalar part, E(J chi_0 + a v) = p_phys [J chi + a (v + J (chi_0 - chi)/a)]; (chi_0 - chi)/a is smooth
with compact support in t, and v in H^(29/4)(R), viewed as a function on R x S^1, is in H^sigma. QED.
Consequences. With H = H_full, the low/high product theorem gives ||W[d].grad g||_Y <= C_B ||d||_X0 ||g||_H and
||DW[g]||_inf + |c[g]| <= C_V ||g||_H, and therefore the difference bound (4) of the moving-tail iteration,
||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_X0 ||g||_H for h0, h1 in the H ball, holds for H = H_full: (A_h1 - A_h0) g =
W[d].grad g + W[z].grad g + U[g].grad z + c[g] (m(ell_1) - m(ell_0)) with d = h1 - h0, z = z_ell1 - z_ell0, and
|ell_1 - ell_0| <= ||c||_(X0*) ||d||_X0 / 3 by n' >= 3; the z terms are bounded by C |ell_1 - ell_0| ||g||_H by the tail
velocity bounds and the coupling-change bound C_z : X0 -> Y of the moving-tail uniform theorem, and the last term by the
smoothness of m into Y.

Theorem E (conditional existence of the self-similar profile; CONDITIONAL THEOREM, V178).
Setting: the exact moving-tail family rho_ell = rho_0 + chi_inf(r) (r^(1/ell) - r^k) Theta(theta), ell in a fixed interval I
with max(k, 1/ell) < q_* < 1/4, the scalar map n(ell) = 3 ell - 1 - c[rho_ell] (n(ell_0) = 0, n' >= 3), ell(h) defined by
n(ell(h)) = c[h], the operators A_h of the moving-tail family, and f0 = F_ell0(rho_0) (the residual of the normalized
modal density, in Y_full by the moving-tail residual analysis). Hypotheses:
 (I) (base low injectivity) the base operator A_0 : B (+) D_R -> Y is injective;
 (S) (smallness) with r_* the radius, K_H the uniform high inverse bound (B_H (+) D_H(v) -> Y_full) and K_L the uniform
     low inverse bound (into X0) that the moving-tail uniform theorem provides under (I), C the constant of the
     difference bound above, and eta0 = ||f0||_(Y_full), there is r <= r_* with
          K_H eta0 <= r,   K_L C K_H eta0 < 1.
Conclusion. There are ell in I and h in H_full with ||h||_(H_full) <= K_H eta0 and F_ell(rho_ell + h) = 0 in Y; h is the
X0-limit of h_(j+1) = -A_(h_j)^(-1) f0, h_0 = 0. The density rho = rho_ell + h has the parity of the problem, is C^1 off the
origin (s_min > 2), has cubic jet (1 + J(h)) x^2 y at the origin and far field r^(1/ell) Theta(theta) + o(r^(1/ell)) with
q = 1/ell in (0, 1/4), and solves the profile equation pointwise off the origin. If moreover |J(h)| < 1,
rho_norm(X) = lambda rho(X/lambda), lambda = (1 + J(h))^(1/2), is a solution with unit cubic coefficient (leading term
exactly x^2 y), the same ell and c, and tail amplitude lambda^(1 - q). It is unique in the closed r ball if K_L C r < 1.
Proof. Under (I) the moving-tail uniform theorem gives, for ||v||_(H_full) <= r_*, an isomorphism A_v : B_H (+) D_H(v) ->
Y_full with ||A_v^(-1) f||_(H_full) <= K_H ||f||_(Y_full), and the low isomorphism A_v : B (+) D_L(v) -> Y with
||g||_X0 <= K_L ||A_v g||_Y; by Lemma Emb (b), H_full lies in B (+) D_L(v), so the low bound holds on H_full. This is
hypothesis (16) of the conditional iteration theorem with H = H_full (a Hilbert space, hence reflexive), Y_H = Y_full
(continuously embedded in Y by Lemma Emb (a)) and R_v = A_v^(-1). Its hypothesis (4) is the difference bound above, and
(17) is (S). The iteration theorem gives h and the equation f0 + A_h h = 0 in Y, which is F_ell(h)(rho_ell(h) + h) = 0 by the
exact identity F_ell(h)(rho_ell(h) + h) = f0 + A_h h. The regularity and the jet follow from h in H_full: the scalar
component has beta(-inf) = J(h) and rho_ell = rho_0 = x^2 y + O(r^5) near the origin; the far-field statement uses
h = b v with v in H^(s(.)) in C^1 of the cylinder, so h = O(r^(-1/2)) pointwise at infinity, and rho_ell - r^q Theta =
O(r^(2k - 1)) there, both below r^q. The normalization is the scaling identity
F_ell(rho_norm)(X) = lambda F_ell(rho)(X/lambda) of the iteration theorem. QED.
Status of the hypotheses. (I) is OPEN (the present computer-assisted route is estimated to need of order 1e4 low modes
with the present rigorous tools; this is a planning estimate, not a proved lower bound for every method; finite
sections are NUMERICAL evidence only). (S) cannot be checked: r_*, K_H, K_L and C are qualitative constants
(compactness arguments), and the certified residual sizes are low norms (6049.11 < ||F||_Y < 8601.42 in the original
low space, 3.270 < ||F||_(Y_a) < 485.632 in the decoupled family), which are not the high norm eta0, plus the
enclosure 3.866e10 < eta_* < 6.321e129 in an explicitly fixed equivalent high norm (V192, V182; the upper end is a
deliberately loose majorant); none of them is comparable with unknown constants. Two necessary consequences of (I)
and (S) need no constant: eta0 |c[d]| <= N4 ||A_0 d||_(Y_H) with N4 = -n(4) in (0, 9.06) for every nonzero
high-domain d (V185), and ||R_d||_(Y_H) > 1956082280 |c[d]| whenever c[d] != 0, for R_d = A_0 d - c[d] f_0/(ell_0 n'_0) = L_ren d +
c[d] Q_ren/(ell_0 n'_0), Q_ren = ell_0 n'_0 m_0 - f_0 (V194). Both are necessary inequalities only. No actual admissible
high-domain vector d is known to violate either with certified bounds; the scaling tangent, the natural candidate, is
not admissible (V198), while an exact Gaussian density d = -Delta v with c[d] = 1 and J[d] = 0 is admissible
(THEOREM, V273, verifier proof, independent audit recorded as V283;
report 6.5 item 10), and no upper bound of its two high norms is certified. A knot-scale heuristic (S2_THEORY_18H_REPORT.md 6.5 item 10; the diagnostic of V209 is a
numerical record) suggests that the archived trial may fail them; it is NUMERICAL and does not prove failure of (S),
which remains OPEN. The exact size of the high residual alone cannot decide (S), because (S) also involves the unknown
inverse and bilinear constants. Hence Theorem E is a conditional existence theorem, not an unconditional existence
proof for the actual trial; it states exactly what remains.
Scope (V178). (i) The uniqueness concerns the correction h before the rescaling, in the closed r ball of the fixed
moving-tail chart; it is not uniqueness among all unit-normalized profiles. (ii) The unit normalization keeps the
explicit condition |J(h)| < 1; a sufficient test is ||J||_(H*) K_H eta0 < 1. The leading tail of rho_norm is
lambda^(1 - 1/ell) r^(1/ell) Theta. (iii) The far field sharpens to rho_ell + h = r^(1/ell) Theta + O(r^(-1/2)), since
every high correction is O(r^(-1/2)) and 2k - 1 < -1/2. (iv) The profile is C^(1,alpha) on compact subsets of the
punctured plane for every 0 < alpha < 1/20, and the equation holds pointwise there. (v) The same implication holds
with the low spaces of the decoupled family (inner radial weight unchanged, far weight r^(-37/20), one fixed angular
exponent a in [18/5, 4]): the fixed-coupling and moving-tail operators are Fredholm of index 0 there with a fixed
compact error and consistent uniform low and high inverses under base low injectivity in those spaces (THEOREM, V175),
and the low/high product bound and the difference bound (4) hold in the new low norm (THEOREM, V176). The certified low
residual bounds (V164, V174) do not replace eta0.

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
   V086, m_a >= 2.9270 by V197, and m_a >= 3 by V259, which supersedes 2.9270; coefficient-margin scope, exact
   normalized joined trial). Theorems R and C' are
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
   delta > (A+D)(1/2 + eps)/A and eps < 0.14547; delta = 9/5, s = 41/20 is admissible. The inverse-regularity theory
   on X_s is now proved: (H3) and index 0 (V151, V152), and the uniform version for small transport perturbations with
   frozen coupling (V156 to V161 and V163, with the sign correction of V162), and the bordered and moving-tail versions with uniform inverses under base low
   injectivity (V166, V168 to V170). What remains: low injectivity and every constant (6.8, Theorem E, CONDITIONAL THEOREM, V178).
5. Hypothesis (Z) of Lemma H1: DONE (V080; the verifier's own original-data cover, |V|/r >= 3/12500 outside the source
   rectangle Q, P the only zero in Q by V070). Quantitative escape constants are OPEN.

## 9. Verification status

- Theorem O: CONFIRMED (V022) for (a), (b), (d); (c) CONFIRMED as the bounded integral extension; the pointwise reading
  of (c) REFUTED.
- Proposition N1: CONFIRMED with a >= 5/2 (endpoint allowed); "strictly" REFUTED (V025). Proposition N2: CONFIRMED
  conditional on the positive axis rate (V025); the rate is certified, d >= 5.5752 (V077). Corollary N3: CONFIRMED in the corrected full-L form (V025).
  Proposition N4: CONFIRMED, with the residual threshold needing a nonzero leading coefficient (V025). Remark N5:
  corrected statement CONFIRMED, literal o(r^k) version REFUTED (V025).
- Lemmas G1 to G3, Theorem R: CONFIRMED under the exact hypotheses listed in section 3 (V023), with the Lemma G2
  square-root step replaced by the exact-matrix argument of V023 (now the proof of Lemma G2; the first proof is
  withdrawn). V031 extends Theorem R to Lipschitz mu with Lip(mu) < 2, including mu~. V032 confirms
  Remark R.2 (c not closable on D_w). The global margin (H_m) is CONFIRMED for mu~ (V077, m_R >= 1.78605; m_R >= 5/2 by V086), so Theorem R
  holds for the actual background; injectivity remains OPEN, and the strain column and the jet space are handled by
  Theorem C' instead.
- V041: the scalar axis row on the explicit spaces B -> Gamma (CONFIRMED, conditional on the positive axis rate and
  the endpoint bounds; both are now established, V077 and V055). V041 also found that the first-version Theorem C was not a fully specified conditional theorem
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
  CONFIRMED; the inverse hypotheses were then OPEN (now proved under base low injectivity, V166, V168 to V170; base
  low injectivity OPEN). V063: Lemma H1 (i), (ii) under (Z) and the compact escape lemma (iii)
  without (Z), CONFIRMED; (Z) itself then OPEN (now V080). V064: the frozen source threshold s_fast = (b_0 + g)/A_P is sharp with the
  Riesz coupling retained, 3.57854758171660 < s_fast < 3.57854758172942, CONFIRMED (frozen maximal realization).
- V065: the cone-local high space (V060's factored H^7 space plus a cylinder H^s bulk, s > 2, on |cos theta| >= eps, origin
  exponent 1/4 < delta < 2, far exponent gamma < -3/8) has classical J, embeds into Z and carries the low/high product and
  bounded-DW estimates, CONFIRMED under the positive axis rate (certified, V077); s = 21/10, delta = 3/2, gamma = -1/2 is admissible. This is
  the mapping side of the space of 6.6; inverse preservation is OPEN for that space (the current inverse-regularity
  theory is on X_s: V152, and V166, V168 to V170 under base low injectivity).
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
  REFUTED (oscillatory packet; d_x versus d_x + eps d_y); the inverse-regularity form of 6.6 is the correct statement (OPEN at 05:44Z; now
  proved on X_s, V152, with uniform inverses under base low injectivity, V166, V168 to V170).
- V075: the margin perturbation of S2_CLOSURE.md 3.5(a), CONFIRMED with the coefficient 51/4 for a = 17/4 and the
  additional term ||grad h||_infinity for the change of b_+.
- V076: global membership of the normalized residual in the fractional target of order 25/4 (delta = 3/2, gamma = -1/2),
  CONFIRMED; no norm bound at that time (the high-norm enclosure 38666592266 < eta_* < 6.321e129 is V182, V192).
- V077: independent original-data certificates d >= 5.5752, m_a >= 0.53072, m_R >= 1.78605, CONFIRMED; hence (A),
  (H_m') and (H_m) hold, and Theorems R and C' are THEOREMS for the actual normalized modal background (Fredholm of
  index 0; injectivity OPEN). Clarification (verifier's note of 05:42Z): for the fixed-background family A_h the term
  ||grad h||_infinity of V075 is not needed (b_+ is built from grad rho~); it is needed when the coupling background
  moves, as in the moving-tail family.
- V078: the 34 source exclusions of the numerics refinement lie in the exact Q, CONFIRMED; its leaf counts REFUTED
  (359 terminal leaves).
- V079: the cylinder corner threshold s_x = 3/2 + delta A/(A+D) and an explicit frozen low-domain counterexample at
  delta = 3/2, s = 21/10, CONFIRMED; the implication from the Cartesian threshold REFUTED. The actual high inverse with
  the revised parameters was then OPEN (now V152 on X_s; uniform inverses under base low injectivity, V166, V168 to
  V170).
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
- Lemma H2, Theorem H: DERIVED outlines (historical; the order is supplied by V130, V132 and the inverse-regularity
  statement by V152, V166, V168 to V170, under base low injectivity). V106: Lemma H-spec CONFIRMED as an abstract conditional theorem (with
  lambda_* = omega + 1 + 2M||C||, so that C = 0 is covered); REFUTED for a direct application with the physical
  identity shift on the free-J spaces (the cubic direction e_0 = x^2 y chi_0 is in the intended high domain and not in
  the target, and subtracting J(h) e_0 kills e_0, so no O(1/lambda) inverse bound holds); OPEN for a compatible shift
  and the actual high inverse. V108: the restated form for the remainder block and Corollary H-spec for the jet row
  (07:01Z) CONFIRMED as conditional theorems (no identity shift of the free jet; B_H need not embed into Gamma_H);
  every high-space hypothesis (H1) to (H3), (J1) to (J3) was then OPEN (07:32Z; on X_s they are now THEOREMS: (H1) and
  (J1) to (J3) V126, (H2) V129 with the order of V130, V132, (H3) V151). V109: the scalar row A - lambda on B_0 has index -1
  for 0 <= lambda < sigma D, is an isomorphism above and is not Fredholm at sigma D, CONFIRMED; the literal assertion
  that J H with J != 0 lies in B is REFUTED (use H chi). Remark (6): DERIVED.
- V107: six original-data point densities of the strong residual, CONFIRMED; V110: ||F(rho~)||_Y > 933.47, CONFIRMED
  (remainder energy on 9.9 <= log r <= 10.1 alone). V111: the finite-section angular projection (raw sine truncation,
  jet extraction, Euclidean cos^4 division) is not contractive in Y (amplification > 5037 at cutoff 19), REFUTED as a
  contraction; a certified section needs a proved factor or a conforming projection.
- V112 to V118 (the jet-row conditions of Corollary H-spec): V112, dilation commutation (y d_y)^j T_h = T_{(X.grad)^j h}
  on the exact graph domain and compactness of the remainder axis row R_(max(N-2,0),s) -> H_g^N for N <= 6, CONFIRMED;
  V113, the free-jet row is Hilbert-Schmidt on B_N = {beta in B : A beta in H_g^N}, CONFIRMED; V114, the critical
  angular Hardy inequality (C_H^2 about 4.14643) and the embedding of the base order 25/4 remainder into R_(4,s),
  CONFIRMED; V115, the integer target Gamma_H = H_g^6 with remainder order 25/4 fails (J1) (beta_n = n^(-7) chi cos(nt)),
  REFUTED as a choice; V116, the full axis row is compact from E B_6 (+) R_(4,s) into the localized space of order
  25/4, CONFIRMED; V117, the weighted scalar graph Gamma_H = a H^(25/4) (a = e^(9t/5) at the origin end, e^(-7t/2) at
  infinity) with B_H = {J chi + a v : v in H^(29/4)}, CONFIRMED, and the unweighted localized target fails at the origin
  end (beta = r^(1/2) chi_-); V118, (J1) to (J3) for R_H = R_base + Q (factored axis-zero order 25/4 plus cone-bulk order
  41/20 in |cos theta| >= epsilon), CONFIRMED. (H1) to (H3) and injectivity remain OPEN.
- V119 to V122: V119, (H1) fails for the sharp cone sum R_H of V118, even with one transport graph derivative
  (exact-kernel packet counterexample), REFUTED as a choice; V120, the residual of the trial has a nonzero term of
  degree 2k - 1 and its strong remainder energy decays at the exact rate 4k - 5/4, CONFIRMED (not a finite-radius tail
  bound); V121, the margin variation in the weight family (a, Delta), CONFIRMED, and the finite-J scalar inverse fails
  for the tied exponent a <= 4, REFUTED for unchanged reuse; V122, the residual quadrature, CONFIRMED as arithmetic only.
- V123 to V125: V123 and V125, directed far-tail enclosures of the full Y energy of the residual (all angular modes,
  axis and remainder parts): beyond t = 20 in (203443.34, 203445.56), beyond 25 in (14192.84666678, 14192.84666680),
  beyond 30 in (990.0012675088110412, 990.0012675088110415) (V125), and < 3175, < 0.666 beyond t = 40, 45 (V123),
  CONFIRMED; the inner and intermediate energy is not certified. V124, for a one-sided conormal power the coupling is
  smooth on the other side (the principal normal multiplier is 1/xi), CONFIRMED; the conormal mechanism of remark (7)
  is REFUTED, V119 is unaffected.
- V126 to V129: V126, on the smooth variable-order space X_s (order between 41/20 and 25/4, uniformly smooth,
  reflection invariant, 25/4 on a fixed vertical sector; no monotonicity) C_R : X_s -> X_s is bounded and (J1) to (J3)
  hold with Gamma_H = a H^(25/4), CONFIRMED ((H1), qualitative). V127, the five-derivative hypothesis (A_V) of Lemma
  H2-var does not imply the high transport inverse (C^5 lacunary counterexample), REFUTED as a sufficient hypothesis.
  V128, the vertical angular margin 142.5 does not give an all-covector energy estimate on the isotropic cofactor space
  (t-frequency packets have negative energy -> -(delta D + Sigma/2) = -54.0687 with vanishing low graph norm), REFUTED as
  an implication, CONFIRMED as a directional counterexample; (H3) as a norm estimate is not affected. V129, (H2) on X_s
  with M = 1 in the dyadic norm, under W^(7,infinity) coefficients (verified for the actual field) and W.grad s >= 0,
  CONFIRMED; existence of the order function is the remaining hypothesis (Lemma H2-ord, DERIVED, submitted).
- V130 to V137: V130, a smooth monotone order (41/20 near the horizontal source-to-origin segments, 25/4 on
  |cos theta| <= 1/2 and a far collar) and a smooth escape function for the actual field, CONFIRMED; V132, the direct
  construction of Lemma H2-ord, CONFIRMED. So (H1) and (H2) hold on an actual X_s. V131, the exact origin normal family
  bijective for each fixed real frequency and Re lambda > -m_x, CONFIRMED; V133, the same uniformly in the frequency on
  the selected end space, CONFIRMED for the exact normal operator. V134, the joint source margin at order 41/20 is
  4.52536 (sharp), not about 14.8 (REFUTED). V135 and V137, the selected principal end inverses at the vertical,
  horizontal and far ends survive the actual small coefficient errors, CONFIRMED (constants and cutoffs qualitative).
  V136 concerns the residual integrator (numerical certificates). Proposition H3-red (6.6, after Lemma H3-var), the
  reduction of (H3) on X_s to the symbolic estimate (Hs_eps), is DERIVED and submitted.
- V138 to V140: V138, a small first-order coefficient error is not a bounded perturbation of the normal inverse on the
  graph norm (actual-coefficient counterexample; REFUTED for that justification, which H3-var item 5 had used); V139,
  the actual inner end estimate ||chi_inner h|| <= C(||chi (T - lambda) h|| + ||eta_ann h||) with a finite annular
  X_s error, CONFIRMED; V140, ||chi_+- C_R||_{X_s -> X_s} -> 0 at both ends and the reduction
  ||h||_{X_s} <= C_K(||(S - lambda) h||_{X_s} + ||zeta h||_{X_s}) to a compact core with a high-norm error, CONFIRMED.
  Lemma Hs-sym (the global symbol inequality m + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu for every mu < m_x, from the
  confirmed margins and the escape function of V130) is CONFIRMED (V144, below); Proposition Hs derives (Hs_eps) from it
  and the explicitly listed finite-regularity calculus inputs (Q0), (Q1), (Q2), (Q5), which are OPEN (the positivity and
  logarithmic steps (F1), (F2) are elementary, since the energy symbol is a quadratic form in the covector).
- V141 to V144: V141, Proposition H3-red ((Hs_eps) implies (H3) on X_s with an explicit compact K; the N_0 origin
  coefficients are (63 ell - 24)/5 and (9 ell - 6)/5, both above 1 + ell/2; the trace argument needs only H^2 of the
  axis coefficient), CONFIRMED conditional on (Hs_eps); V142, the axis row Gamma_C/a is bounded X_(s-eps) -> H^(51/8)
  and compact X_(s-eps) -> H^(25/4), uniformly for 0 <= eps <= 1/4, CONFIRMED; V143, [C_R, M_phi] is compact on X_s
  for smooth bounded reflection-invariant phi (so escape conjugation by e^(N Lambda) changes C_R by a compact operator
  for each fixed N), and the local order-zero principal symbol of C_ren is grad rho . (xi_x xi_y, -xi_x^2)/|xi|^2 in
  both the bulk and the cofactor variable, CONFIRMED; V144, Lemma Hs-sym, CONFIRMED after one decimal correction (the
  cofactor constant at S_y is -54.06870, not -54.06934; the characteristic cofactor margin 142.50740 is unchanged; no
  values of N, L_0 are certified). With V140 and V142, V143 covers the multiplier, tail, axis and cofactor-symbol parts
  of input (Q2) of Proposition Hs; the local variable-order commutator remains.
- V145: for real a >= 0 of order m <= 1/8 with three bounded spatial derivatives, Re <Op(a) w, w> >= - C ||w||^2 in
  H^(-1/32), and Re <Op(a) w, w> >= mu ||w||^2 - C ||w||^2_{H^(-1/32)} if a >= mu has order 0; this applies to the
  actual G_v, G_u and to (W.grad s) log<xi>, CONFIRMED (the positivity and logarithmic steps of Proposition Hs in
  scalar form; the conversion of the remainder to X_(s-eps), the transport conjugation and (H3) are separate).
- V146 to V150 (the five calculus inputs of Proposition Hs, all CONFIRMED): V146, order reduction: ||A v|| <= C ||v||_{H^s},
  ||v||_{H^s} <= C (||A v|| + ||v||_{H^(s-eps)}), ||A v||_{H^(-r)} <= C ||v||_{H^(s-r)} for 0 <= r <= 1, and the sector support
  correction (R A_u u is not supported where u is; its part outside a larger sector is smoothing), input (Q0) and the
  sector positivity step; V147, input (Q2) for the actual C_R with a compact operator and an arbitrarily small high
  error (smooth approximation of the H^(51/8) coefficients in multiplier norm); V148, C_R bounded on X_(s-eps) and the
  penalty bound ||W.R w|| + ||W.R z|| <= C ||f|| + a ||h||_{X_s} + C_a ||h||_{X_(s-eps)} for every a > 0, input (Q5'); V149,
  input (Q1) for W^(7,inf) coefficients on test functions (kernel Taylor expansion to degree 6, the logarithm with the
  exact coefficient W.grad s); V150, the (Q1) inequality on the maximal domain {v, P v in H^s}, without a graph-dense
  core. The assembly of Proposition Hs from these inputs is CONFIRMED (V151).
- V151: Proposition Hs and (H3) for the actual operator on X_s: for eps = 1/32 and each finite L,
  ||h||_{X_s} <= C (||(S - lambda) h|| + ||h||_{X_(s-eps)} + ||J h||) with J compact, and ||h|| <= C_1 ||(S - lambda) h||
  + ||K h||_{W_0} with K compact, 0 <= lambda <= L, CONFIRMED (qualitative constants).
- V152: the high Fredholm theorem: S - lambda : D_s -> X_s (lambda >= 0), L_ren and L_red : B_H (+) D_s -> Gamma_H (+) X_s
  are Fredholm of index 0; low injectivity implies a high inverse equal to the low inverse on the high target,
  CONFIRMED (no constants, no injectivity).
- V153: the variable-order Kato-Ponce bound for the full commutator [A, B.grad] is false, REFUTED (the term
  -(B.grad s) log<D>; localized packets; smooth parity-P IPM velocities realize a nonzero B.grad s).
- V154: the order of V132 satisfies W.grad s >= kappa_s |grad s|, kappa_s = m/(L + 1) > 0, so (W + B).grad s >= 0 for
  ||B||_inf <= kappa_s/2; explicit matrix-margin loss (1 + sigma) ||DB|| + ||d|| + N ||grad Lambda|| ||B|| +
  L_0 (2 ||W|| ||B|| + ||B||^2) with N, L_0 fixed; CONFIRMED.
- V155: Re <ell log<D> w, w> >= -C ||w||^2_{H^(-alpha/64)} for ell >= 0 in C_b^(1,alpha), and the maximal-domain
  Friedrichs passage with Lipschitz coefficients, CONFIRMED.
- V156: the perturbation velocity on the high coefficient space G_s: B_norm[g] = c[g] E_0 + Z[g] with E_0 fixed and
  smooth, |c[g]| + ||Z[g]||_{H^(s(.))} + ||B_norm[g]||_{C_b^(1,alpha)} + (divided cofactor norms) <= C_alpha ||g||_G,
  alpha < 1/20, CONFIRMED.
- V157: the square-function coefficient commutator (sum_j ||sum_l [A_j, B_l] d_l v||^2)^(1/2) <= C (||DB||_inf ||v||_{H^s}
  + ||B||_{H^s} ||Dv||_inf), CONFIRMED.
- V158: the dyadic energy (A_j = Op(e^(N Lambda) <xi>^s psi_j), sum psi_j^2 = 1; the cutoff term cancels by
  sum psi_j d_xi psi_j = 0) with the coupling, penalty and sector bounds square-summed, CONFIRMED.
- V159: the uniform compact-error estimate ||h|| <= C ||(S_g - lambda) h|| + ||K h|| on the maximal domains D_g for
  ||g||_G <= r_*, 0 <= lambda <= L, with frozen coupling C_R, CONFIRMED (qualitative r_*, C, K).
- V160: T_g generates a C_0 semigroup with generator domain D_g, uniformly on the ball; S_g - lambda is Fredholm of index 0;
  if S_0 is injective, ||h|| + ||T_g h|| <= C ||S_g h|| uniformly on a smaller ball, CONFIRMED. Not included: the
  bordered axis block, the moving background, the low inverse, constants.
- V161: Lemma K (single-operator tame coefficient commutator) and Lemma P (variable-order products), CONFIRMED.
- V162: the literal N_0 energy density written for the single-operator variant has the wrong sign, REFUTED; the corrected
  change (1/2) div B - beta B_r + 4 tan(theta) B_theta is CONFIRMED.
- V163: the single-operator route to the uniform perturbed estimate, with the V162 correction, CONFIRMED (eps = 1/2560).
- V164: certified low residual 6049.11 < ||F||_Y < 8601.42 (low strong target), CONFIRMED.
- V165: finite-band angular division preserves W^(7,inf) (sin(2n theta)/sin(theta) = U_(2n-1)(cos theta),
  sin(2n theta)/cos(theta) = 2 sin(theta) U_(n-1)(cos 2 theta)), CONFIRMED; the generic Hardy-average regularity remark of
  the theory author is REFUTED (lacunary counterexample).
- V166: tau_g = c[g] chi_0 + e_g with H^(31/4) bounds and the inner weighted bound; A_g - A : B_H -> Gamma_H is O(||g||);
  A_g an isomorphism on a small ball, CONFIRMED.
- V167: the local axis multiplier sign is +2/eta^2; the theory author's -2/k^2 is REFUTED.
- V168: the full fixed-coupling high block on B_H (+) D_g: G_g - G_0 = O(||g||), Fredholm index 0, fixed compact error,
  uniform inverse under base full injectivity, CONFIRMED.
- V169: the full fixed-coupling low block: Fredholm index 0, fixed compact error, uniform low inverse under base
  injectivity, CONFIRMED.
- V170: the exact moving-tail family A_h of V062: uniform low and high compact estimates and Fredholm index 0; under
  base low injectivity both uniform inverses, agreeing on Y_full, CONFIRMED (base injectivity and constants OPEN).
- V171: decoupled family margins m >= 1.13 (a = 4) and >= 1.10534 (a = 18/5), inner 17/2, outer 37/20, CONFIRMED.
- V172: low mapping and Fredholm theorem for the decoupled family, a in [18/5, 4], CONFIRMED.
- V173: no uniform third axis derivative bound in the decoupled spaces with a <= 4 (counterexample), CONFIRMED.
- V174: ||F||_(Y_a) < 485.632 for every a in [18/5, 4] (low norm), CONFIRMED.
- 6.8 Lemma Emb: THEOREM (V177). Theorem E: CONDITIONAL THEOREM (V178), with the scope clarifications listed there.
- V175, V176: the uniform perturbed inverse framework and the low/high nonlinear difference in the decoupled family.
- V179: ||F||_(Y_a) > 3.270 for every a in [18/5, 4] (partial lower bound from eight windows, low norm), CONFIRMED.
- V180: finite-section assembly from final blocks plus retained checkpoints double-counts cells (REFUTED as a
  once-per-cell sum); the parts-only assembly of the completed, never-resumed S_1 run covers each cell once, CONFIRMED.
- V181: the coverage checks of the optional outer margin merge are insufficient (REFUTED); no accepted certificate
  depends on them.
- V182: high residual norm, deliberately loose majorant eta_* < 6.321e129 in an explicitly fixed equivalent norm on
  the high target of Theorem E (||F/(r^3 p a_*)||_(H^(25/4)) < 1.195e93), CONFIRMED as an upper bound; it does not test
  (S).
- V183: high residual norm, point lower bound eta_* > 1906360017 from the fifth derivative of the weighted axis trace at
  t = 8, CONFIRMED. V186 and V192: the fractional difference bound at t = 8 and 1001/125 gives eta_* > 36400585492 and,
  with the exact constant 8/(3 sqrt(2 pi)), eta_* > 38666592266, CONFIRMED.
- V184: necessary test of (S): the residual of the j-th iterate of Theorem E is (A_(h_j) - A_(h_(j-1))) h_j, so under
  (S) its low norm is at most q_0^j ||f_0||_Y; one exact step that does not reduce the low residual norm rules out (S)
  for every admissible choice of constants. CONFIRMED as a conditional necessary test.
- V185: scalar-radius test eta0 |c[d]| <= N4 ||A_0 d||_(Y_H), 0 < N4 < 9.06, CONFIRMED as a necessary consequence of
  (I) and (S). V190: for c[d] != 0, M_0 and L_fix d are separately outside the strong zero-jet Sobolev targets of
  Theorem E (cubic coefficients 1 and -c[d]; in the Hoelder targets Y, Z, Z_2 of S2_CALPHA_THEORY.md 3.4 both columns are target-valued, V255); a separate
  norm diagnostic is REFUTED, and A_0 d = L_ren d + c[d] m_0 is the valid finite split. V194: the residual-subtracted
  test ||R_d|| > 1956082280 |c[d]| for c[d] != 0, CONFIRMED as a conditional necessary test.
- V187 to V189, V193: finite-section error model (input division error about 1e-7 relative; rounding-model intervals
  REFUTED as total error bounds), the coverage check by cardinality only (REFUTED as a generic guarantee), the exact
  cos^4 quotient templates, and the exact raw image bandwidth J + M of the S_1 remainder column product; V196: the repaired assembler, CONFIRMED. V191: the
  decoupled margin at a = 4 is at least 1.2501, CONFIRMED. V197: the original-weight margin is at least 2.9270 on the
  whole plane, CONFIRMED (superseded by V259). V259: the old-weight margin m_a >= 3 at every nonzero point, for the
  exact normalized joined trial and the old anisotropic weight (inner slope -17/2, outer slope -5/4, angular exponent
  17/2), CONFIRMED by an independent original-data certificate; a coefficient-margin statement only, with no
  finite-section or inverse conclusion (m_R uses a different weight and is unchanged). V195: a failed scalar-radius test does not determine the scalar component of the actual
  Newton step (exact two-dimensional example; REFUTED as a general inference). V198: the scaling tangent
  rho_0 - X.grad rho_0 of the spline trial, even after a smooth annular cutoff, is outside the chosen high correction space
  (sixth-derivative jump of its axis cofactor at an interior knot; REFUTED for admissibility, CONFIRMED for the local
  nonmembership). V199: the relative threshold ||R_d|| <= 0.0507 eta0 |c[d]| (c[d] != 0) from the sharper bound N4 <= 9.04502536,
  CONFIRMED as a conditional necessary test. V200 (the no-TAU S0 value 0.020685, a conditional matrix certificate) and
  V202 (the exact input Gram of the pure-spline sections; input side only) concern the finite sections. V201 and
  V203 to V208 concern the Hoelder theory (the accompanying S2_CALPHA_THEORY.md, S(e) and section 6). V209: the
  knot-scale diagnostic of the trial reproduced from exact rational coefficients (a numerical record). V210: of the
  78 pure spline columns (all low-conforming), exactly i = 6..27 (66 columns) lie in H_full and exactly i = 7..26
  (60 columns) in the maximal high graph domain D_H(A0); the zero extension is exactly C^(i-1) at the left end only for
  i = 4..7 and exactly C^(32-i) at the right end only for i = 26..29 (the other columns vanish near the respective
  endpoint; at the interior knots every spline has C^6 joins), and for i = 6, 27 a fifth-derivative jump of the transport image, times the vertical radial speed
  d >= 5.5752, cannot be cancelled. V211: the nonlinear failure (Lemma N'') in the localized C^alpha_2 graph. V219: the sharp delta^2 rate of the normalized origin coupling on C^alpha_2. V226: the actual-variable origin factorization error is also O(delta^2). V222, V224, V227, V228: the common Hoelder target Y = C^alpha_2 intersected with L^2(w_gamma), 4k < gamma < 2 (extended to E_2 and every gamma > 4k by V241, recorded as V247), with the residual in it, the bounded complete coupling, the closed full operator A_0 and the noncompact error of the specified single cutoff parametrix (not a statement about sums of patches; S2_CALPHA_THEORY.md 3.4). V232, V234: T, L_ren and A_0 are not onto Y, so Y is not a valid global target; the mapping theory and the actual auxiliary exterior inverse on the scaled far target of S2_CALPHA_THEORY.md 3.4(g) (V235, V236) are THEOREMS (independent audits recorded as V244, V242), and T, L_ren and A_0 have infinite algebraic cokernel on this isotropically scaled Z (Z_sc; V243, recorded as V249), so it is not a global target either. On the scaled quadratic-axis target Z_2 of S2_CALPHA_THEORY.md 3.4(g) the mapping theory (bounded complete coupling with small tails, residual membership, closed full operator) and the actual exterior auxiliary inverse are THEOREMS (V245, audit recorded as V254). At a simple zero y_* in (9.1465, 9.1468) of the axis rate d_x V_1(0, y), certified by an original-data interval enclosure, T is not onto Z_2 for alpha > 1/2, and L_ren and A_0 are not onto Z_2 for alpha > 2/3, for 2k - 1 < beta < k and gamma > 4k (THEOREM, V256, independent audit recorded as V262). The divided-velocity refinement V257 (THEOREM, verifier proof, independent audit recorded as V265) extends the non-surjectivity of L_ren and A_0 on Z_2 to every alpha > 1/2; surjectivity for alpha <= 1/2 is OPEN. A stronger candidate target Z_cof (h = x^2 g with g in the full scaled joint C^alpha) with mapping, residual membership, closed domains and actual exterior inverse is THEOREM (V261, V268); its global inverse is OPEN, and the nonlinear derivative loss persists in its graph topologies (THEOREM, V264, V271). None of these Hoelder results says anything about the Sobolev condition (I) of Theorem E or about whether the actual residual lies in the range of these operators. V213 to V217: the actual unnormalized source
  operator on C^alpha intersected with L^2, and the relative-domain density statement in the C^alpha_2 graph (the
  accompanying S2_CALPHA_THEORY.md, 3.1(iii) and 2(e)).
- Sections 4 to 6 otherwise: the remaining outlines (section 4, Lemma H2 of 6.4, Theorem H and Lemmas H2-var, H3-var
  of 6.6) are DERIVED or historical sketches and are not submitted as theorems; their verified replacements are the
  results labelled THEOREM or CONFIRMED above (V077, V080, V126, V129, V130, V132, V151, V152, V156 to V163, V166,
  V168 to V170, V177, V178). Low injectivity (I) and the quantitative condition (S) remain OPEN. Lemma (E) is proved in the form (E0), (E-J), (E-G) (V049 to V053).
