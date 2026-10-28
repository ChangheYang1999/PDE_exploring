# S2_CLOSURE.md: status of the nonlinear existence theorem

First version 2026-10-28T02:47Z (theory author), updated 02:55Z after V034 to V036, 03:06Z after V037 and V038, 03:24Z after V041 and V042, 03:34Z after V043 to V046, 04:11Z after V047 to V054, 04:47Z after V055 to V061 and Prop F4, 04:58Z after V062 to V064, 05:16Z after V065 to V068 and Lemma Z, and 05:26Z after the box certificates of the margins and of (A) (computed once) and 05:35Z after V069 to V072, and 05:45Z after V073 to V076 and a rank estimate for the injectivity certificate, and 05:54Z after V077 to V080 (Theorems R and C' unconditional for the actual background, global (Z), the cylinder corner threshold), and 06:01Z after V081 to V083 (C6 reproduced; the injectivity lemmas; the Mellin bound). Labels follow the accompanying CONVENTIONS (item S8):
- THEOREM: a complete proof exists and the independent verifier has CONFIRMED it (verdict number given).
- DERIVED: a proof or computation written by the theory author, not yet independently checked.
- CONDITIONAL: proved under hypotheses that are named.
- NUMERICAL: computed, not a bound.
- OPEN: not established.
- REFUTED: shown false.

Background of every rigorous statement: the exactly joined and exactly normalized modal trial rho~ (c_l = 1/k exactly,
CONVENTIONS S0.3(i)). The accepted numerical state X3 is the reference only. Its normalization defect
3/k - 1 - c[X3] lies in (1.0301137738456e-8, 1.0301137743913e-8) (THEOREM, V018), so F(X3) with the normalized
exponent contains a term that grows like r^k, and X3 cannot itself serve as the rigorous background.

## 1. Answer

No complete nonlinear existence theorem is established. Nothing in this run proves or suggests that no exact solution
exists near X3: the obstructions found are obstructions to particular norms and methods (section 4, last paragraph), not to the
profile. What is proved at the linear level: for the actual normalized modal background, the reduced normalized operator
L_red : Z -> Y_lo is Fredholm of index 0 (Theorem C', V047, V049 to V053, V055, V077), so it is invertible if and only
if it is injective; the global flow of the background has exactly the expected zeros (V080). Injectivity, an inverse
bound, the high-order inverse and the certified residual size are the missing pieces (section 5).

## 2. The exact nonlinear structure (PROMPT 7)

2.1 Remainder, including the variation of c_l (CONVENTIONS S4.1 to S4.3; DERIVED and used by every avenue).
- Formulation N: c_l[rho] := (1 + c[rho])/3 and F_N(rho) := (c_l[rho] X + U[rho]).grad rho - rho.
- Because c_l[.] is affine and U is linear, for every background with 3 c_l_bar - c[rho_bar] = 1,
     F_N(rho_bar + h) = F_N(rho_bar) + L h + N(h),
     L h = V.grad h - h + W[h].grad rho_bar,   N(h) = W[h].grad h,   W[h] := U[h] + (c[h]/3) X,
  with V = c_l_bar X + U[rho_bar]. There are no cubic terms.
- Quasilinear form (exact): with A_h g := (V + W[h]).grad g - g + W[g].grad rho_bar (linear in g, affine in h),
     F_N(rho_bar + h) = F_N(rho_bar) + A_h h.
- The coupling coefficient of A_h is grad rho_bar for every h. Only the transport field V + W[h] depends on h.
  Its divergence is the constant 2 c_l_bar + 2 c[h]/3, and at 0 its linear part is diag(-A', D') with
  A' = A + 2c[h]/3 and D' = D + 4c[h]/3 = 2A' + 1. So the normalization structure is preserved along the iteration.

2.2 Exponent variation and the log column (THEOREM for the obstruction, V025; DERIVED for the formulation).
- An exact solution with c[h] != 0 has far exponent k' = 1/c_l[rho] != k.
- For a fixed background, rho_bar + Z cannot contain such a solution in any of the weighted spaces used here
  (V025, corrected N5). Any smooth parameterization of the tail has a log^2 r second variation.
- The consistent formulation is parametric. Use the background family
     rho_bar_ell := rho~ + chi_inf(r) (r^{1/ell} - r^k) Theta_0(theta),
  with unknowns (ell, h), the equation F(rho_bar_ell + h; ell) = 0 with exponent ell, and the scalar equation
  3 ell - c[rho_bar_ell + h] = 1.
- THEOREM (V038, corrected form): in F(rho_bar_ell; ell) - F(rho~; c_l) the two r^k Theta_0 terms cancel exactly.
  With Phi_q := r^q Theta_0 and q = 1/ell: (ell X.grad - 1) Phi_k = (ell - c_l) k Phi_k (positive sign; the first
  version had the sign wrong), and (ell X.grad - 1) Phi_q = 0. So the subtracted Phi_k in rho_bar_ell cancels the
  parameter variation acting on the old tail.
- What remains is O(r^{2 max(q,k) - 1}), plus cutoff terms with compact support. The first version claimed
  O(r^{q + k - 1}). V038 REFUTED this for every q != k close to k: the highest density mode sin(521 theta) of the tail
  produces a nonzero sin(1043 theta) self-interaction with coefficient -(521 - q) a_521^2/(4 (523 + q)).
- For the far weight r^{-5/4} a power r^beta is square integrable at infinity if and only if beta < -3/8. So the
  remainder and its parameter derivatives lie in the far radial target whenever max(q, k) < 5/16 (k = 0.17936).
  Membership in the full anisotropic target, angular factor included, is THEOREM (V042; 3.5(d)).
- d rho_bar_ell/d ell at ell = c_l equals -k^2 KP, where KP := chi_inf r^k log r Theta_0. This is the log-tail column
  of Prop B of the accompanying S2_C_FUNCTIONAL.md.
- Scalar normalization (THEOREM, V038). Let chi_inf >= 0 be supported in r >= 1 and equal to 1 for large r, and put
  nu(ell, h) := 3 ell - 1 - c[rho_bar_ell] - c[h]. Then d nu/d ell = 3 + q^2 (s_3/pi) int chi_inf r^{q-2} log r dr >= 3
  for ell > 1. For every finite c[h] there is exactly one ell(h) > 1 with nu = 0, it depends smoothly on c[h], and
  |ell(h) - c_l| <= |c[h]|/3. At h = 0, d nu/d ell = k d with d = 3 c_l + k c[KP]. This uses no PDE inverse. It makes
  the normalization closed on any space where c is continuous, such as Z_cap (V034), and not on the radial graph (V032).
- Augmented map (THEOREM, V038). For independent (ell, h) the residual F(rho_bar_ell + h; ell) contains the forcing
  jet nu(ell, h) x^2 y at the origin, which the weighted origin targets exclude. The consistent map is
     (ell, h) -> ( F(rho_bar_ell + h; ell) - nu(ell, h) H_0 , nu(ell, h) ),   H_0 := chi_0 X.grad rho~ / 3,
  whose first component is the PDE residual when nu = 0. Its derivative at (c_l, 0) is
  (g, delta ell) -> (L_ren g + (g_far - k^2 y_KP) delta ell, -c[g] + k d delta ell), which is exactly the bordered
  system of Prop B (V034). V038 assumed J(h) = 0.
- Free-J correction (THEOREM, V042). On a domain that keeps J(h) as a free coordinate (as 3.1 does), the cubic
  coefficient of F(rho_bar_ell + h; ell) at 0 is (1 + J(h)) nu(ell, h), and the augmented map must be
     (ell, h) -> ( F(rho_bar_ell + h; ell) - (1 + J(h)) nu(ell, h) H_0 , nu(ell, h) ).
  Subtracting only nu H_0 leaves the jet J nu x^2 y, which is not in Y_lo whenever J nu != 0, however small (REFUTED
  for free J, V042). The derivative at (c_l, 0) is unchanged, because J = nu = 0 there, so Prop B is unaffected.
- Membership (THEOREM, V042). For max(q, k) < 5/16 on a compact ell-interval, F(rho_bar_ell; ell) - nu(ell, 0) H_0
  lies in Y_lo of 3.1, smoothly in ell, with up to five conormal derivatives. Membership for a general correction h
  in a specified correction space is OPEN.

2.3 Derivative loss (THEOREM, V019 and V030).
- N(h) = W[h].grad h loses one derivative. In the weak graph norm of the earlier diagnostic space it is not even
  continuous at the certified modal source (V019).
- For every 0 < alpha < 1, h -> L^{-1} N(h) is unbounded on C^alpha-bounded sets near a regular axis point (Lemma N),
  and inputs with bounded C^alpha graph norm can have ||N||_{C^alpha} >= c n (Lemma N'), V030.
- So no scheme that measures h only in a transport graph norm or in C^alpha can close.
- A sufficient high-norm requirement is a Lipschitz velocity, D U[h] in L^infinity (the entries of D U[h] are Riesz
  products applied to d_x h, S2_CALPHA_THEORY.md). Necessity is not claimed. The first version called a Lipschitz
  velocity necessary and equivalent to a Riesz bound, and V025 and V038 REFUTED these unrestricted forms.

## 3. A valid two-norm scheme and its closure inequalities (DERIVED schema; every hypothesis OPEN)

3.1 Spaces.
- Weight: w_a = |cos theta|^{-2a} e^{mu_a(log r)}, a = 17/4, mu_a' = -2a for t = log r < 0 and -5/4 for t > 0,
  mu_a(0) = 0. So w_a = |x|^{-17/2} in r < 1 and |cos theta|^{-17/2} r^{-5/4} in r >= 1.
- Jet lift: E gamma := x^2 y gamma(log r). Scalar target G: ||gamma||_G^2 = int_{t<0} |gamma|^2 e^{-t/2} dt
  + int_{t>0} |gamma|^2 e^{27t/4} dt. E G and L^2(w_a) intersect only in 0 (|cos theta|^{4-2a} is not integrable).
- Y_lo := E G (+) L^2(w_a), with the sum of the squared norms (V042).
- X_lo: the jet-plus-remainder domain Z := E B (+) D_R of the accompanying S2_L2_THEORY.md section 5, with B the scalar
  axis space of V041 (it contains the cubic coefficient J = lim_{t -> -inf} beta(t) as a bounded functional) and D_R a
  remainder domain in L^2(w_a). In the parametric formulation the KP coordinate is replaced by the unknown ell.
  The precise Fredholm statement on these spaces is Theorem C' of S2_L2_THEORY.md section 5 (THEOREM as a conditional
  statement, V047). For the modal background its coupling hypotheses are THEOREMS (V049 to V053), so L_red : Z -> Y_lo
  is Fredholm of index 0 under the axis rate (A) and the margin (H_m') alone. Both are CONFIRMED for the actual
  background by the verifier's own original-data computation (V077: d >= 5.5752, m_a >= 0.53072), so L_red : Z -> Y_lo
  is Fredholm of index 0 (THEOREM). Its uncoupled part, the pure transport T : Z -> Y_lo, is an isomorphism (THEOREM as
  a conditional statement, V046, on (A), (CB) and kappa_* > 0; (A) is V077, (CB) is finite by V047 and V055, and
  kappa_* >= 1.6377 from the verifier's own finite cells, V077 note).
- The renormalized coupling must be part of the realization: L_fix does not map Z into Y_lo, and c[.] H_0 is not a
  bounded perturbation into Y_lo (THEOREM, V044, counterexample h = x^4 y eta_0(r)).
- X_hi: a space of variable order (S2_L2_THEORY.md 6.6): order 2 + eps on a neighbourhood (in the polar blow-up) of the
  closed segment [0, x_P] x {0} of the x-axis (ordinary derivatives; in the corner, cylinder derivatives of
  h/r^(3+delta)), with eps < 2A/(A+D) - 1/2 = 0.14547 and origin exponent delta in ((A+D)(1/2 + eps)/A, 2), forced by
  the cylinder corner threshold s < 3/2 + delta A/(A+D) (THEOREM for the frozen operator with an explicit low-domain
  counterexample at delta = 3/2, s = 21/10, V079); delta = 9/5, s = 41/20 is admissible,
  conormal order N near the y-axis and scaled order N at infinity, nondecreasing along the flow. A uniform order is
  impossible for the frozen corner operator: by Prop F4 (S2_L2_THEORY.md 6.2, THEOREM, V067) the frozen saddle maps a
  smooth compactly supported source to -C x^4 sgn(y)|y|^{2 - 1/D}, so no frozen inverse reaches H^s across the x-axis
  segment for s >= 5/2 - 1/D = 2.4531 (and for general L^2(w_a) data even in x the limit is the energy value 2.334,
  V067). For the true operator the transfer is OPEN. The
  frozen source threshold at P, s_fast = 3.5785 (sharp, V064; the box-uniform value 2373/680 of V011), is therefore
  not the binding one. Order 2 + eps suffices for grad h in
  C^eps, which is what C_V and C_B use. The mapping bounds C_B and C_V are THEOREMS for the cylinder-H^7 spaces of V057
  and V060 (finite constants, not computed); by Prop F4 those spaces cannot be the range of the frozen corner inverse.
  V065 proves C_B and C_V (finite, not computed) for the cone-local space: V060's factored H^7 control near the vertical
  axis plus a cylinder H^s bulk, s > 2 (s = 21/10 admissible), on |cos theta| >= eps, which covers the closed x-axis
  segment and the origin with order below the corner thresholds. This is the mapping side of X_hi. Because the
  background is only C^6 across a knot circle that every orbit crosses (V069), the factored order near the vertical
  axis is lowered to sigma = 25/4; V073 proves the mapping bounds for every sigma > 6 and 1/4 < delta < 2 (so for
  delta = 9/5, s = 41/20, gamma = -1/2), and V076 proves that the actual residual lies in the corresponding target
  (0 < delta < 2).
- Y_sigma: a forcing space of order sigma above Y_lo. A loss of order is allowed here because the forcing is fixed.

3.2 Iteration. h_0 = 0 and A_{h_j} h_{j+1} = -F_N(rho_bar), so that
     A_{h_j}(h_{j+1} - h_j) = -W[h_j - h_{j-1}].grad h_j.

3.3 Constants (each must be a proved bound; none is available yet).
- eta := ||F_N(rho_bar)||_{Y_sigma}, the residual of the background in the forcing norm.
- K_H := sup over ||h||_{X_hi} <= r of ||A_h^{-1}||_{Y_sigma -> X_hi}, for the solution operator of the low realization
  restricted to Y_sigma (an inverse-regularity bound; A_h is not a bounded map X_hi -> Y_sigma of the same order, and its
  graph domains may depend on h, V074).
- K_L := sup over ||h||_{X_hi} <= r of ||A_h^{-1}||_{Y_lo -> X_lo}.
- C_B: ||W[d].grad h||_{Y_lo} <= C_B ||d||_{X_lo} ||h||_{X_hi}.
- C_V: ||D W[h]||_{L^infinity} + |c[h]| <= C_V ||h||_{X_hi}.
- r_V: the size of velocity perturbation for which the weighted margin stays at least half its value (3.5(a)). The
  Garding argument needs only the margin. A pointwise bound on D W[h] does not by itself give the global flow
  portrait (number and connections of equilibria); the first version listed it, and V038 noted that it is a separate
  hypothesis.

3.4 Closure inequalities.
     K_H eta <= r,     K_L C_B K_H eta < 1,     C_V r <= r_V.
Abstract two-norm theorem (THEOREM, V038). Let X_H be reflexive and continuously and injectively embedded in X_L, and
Y_H continuously embedded in Y_L. Let A_0 : X_H -> Y_L be bounded and B : X_L x X_H -> Y_L bounded bilinear with
||B(d, h)||_{Y_L} <= C_B ||d||_{X_L} ||h||_{X_H}. For every v in the closed r-ball of X_H let R_v be a linear solution
operator on Y_L with values in X_L, mapping Y_H into X_H, with A_v R_v f = f for f in Y_H (A_v := A_0 + B(v, .)),
||R_v||_{Y_L -> X_L} <= K_L, ||R_v||_{Y_H -> X_H} <= K_H, and ||g||_{X_L} <= K_L ||A_v g||_{Y_L} for g in X_H. Let
f in Y_H, eta = ||f||_{Y_H}, h_0 = 0, h_{j+1} = R_{h_j}(-f). If K_H eta <= r and K_L C_B K_H eta < 1, then h_j converges in
X_L to a solution of A_0 h + B(h, h) = -f with ||h||_{X_H} <= K_H eta; it is unique in the high ball if K_L C_B r < 1.
- The two solution operators must be compatible (one realization in both norms).
- Reflexivity replaces the weak-star compactness of the first version, which an unspecified Banach high space does not
  supply (V038).
Application to IPM (OPEN). In the fixed-background form, B(d, h) = W[d].grad h. But the actual far exponent moves, and a
fixed correction space with one log column does not contain chi_inf (Phi_q - Phi_k) for q != k (V025). The hypotheses
must be proved for the augmented map of 2.2, or for its version with ell = ell(h) eliminated, with the parameter
columns and the nonlinear tail cancellations treated jointly. Updating ell after a fixed-space step is not a proof
(V038). Its scalar derivative at h = 0 is k d, with d = 3 c_l + k c[KP] the denominator of Prop B
(S2_C_FUNCTIONAL.md 7.4).

3.5 What each constant needs.
(a) The margin under perturbation. Lemma G1 of S2_L2_THEORY.md gives, for the field V + W[h], the multiplier
    kappa_w + c[h]/3 + (1/2) W[h].grad log w. For w_a, grad log w = mu_a' X/r^2 + 2a tan(theta) grad(theta), and
    tan(theta) W.grad(theta) = sin(theta) W_2/r - sin(theta)^2 W_1/x. Since W[h](0) = 0 and W_1[h] is odd in x,
    |W|/r and |W_1/x| are bounded by ||D W[h]||_infinity. Hence the change of the margin is at most
    |c[h]|/3 + (1/2)(sup|mu_a'| + 4a) ||D W[h]||_infinity. For a = 17/4 the coefficient is (1/2)(17/2 + 17) = 51/4.
    For the fixed-background family A_h the coupling coefficient is grad rho_bar, so b_+ does not change, and the full
    margin kappa_w - b_+ decreases by at most |c[h]|/3 + (51/4) ||D W[h]||_infinity (THEOREM, V075 with the verifier's
    clarification of 05:42Z; the identity tan(theta) W_theta/r = (y^2/r^2)(-W_1/x + W_2/y) and parity give the bound by
    2 ||D W||). When the coupling background moves, as in the moving-tail family, b_+ is a Lipschitz function of the
    density gradient and the term ||grad h||_infinity is added; the full change of the background enters every term. This defines an explicit half-margin radius r_V once C_c, C_W
    and C_g (the bounds of |c[h]|, ||D W[h]|| and ||grad h|| by the high norm) are certified. The positive axis rate
    persists if ||D W[h]|| < min d; the endpoint asymptotics and the stability of the inverse are separate.
(b) Uniformity of the inverse over the ball. In the Garding estimate the compact remainder K comes only from the
    coupling with coefficient grad rho_bar, which by 2.1 does not depend on h. The transport part enters through the
    margin, which is controlled by (a). So
       (m_* - eps - |c[h]|/3 - C ||D W[h]||_infinity) ||g|| <= ||A_h g|| + ||K g||,
    with K independent of h (DERIVED; (E) of S2_L2_THEORY.md section 5 is now proved, V049 to V053, with
    qualitative K). This holds for the fixed background. In
    the parametric form the coupling gradient grad rho_bar_ell varies with ell, so K depends on ell; uniform
    compactness or a quantitative perturbation bound in ell must be proved (V038). A quantitative K_L then needs two
    certified steps at h = 0 (DERIVED sketch):
    - a decomposition K = K_fin + K_small, with K_fin of finite rank on smooth functions phi_i and ||K_small|| below
      half the margin;
    - smooth approximate solutions psi_i of the adjoint problems A_0^* psi_i = phi_i with certified defects.
    Then <g, phi_i> = <A_h g, psi_i> + (small) ||g||. The h-dependence enters only through ||D W[h]||_infinity times the
    weighted H^1 norms of the psi_i, so the bound is uniform on the correction ball. This is the complement estimate
    of Avenue IV in a form that is checkable on a finite basis.
    Cost of the split (NUMERICAL estimates, grid data, none a bound; S2_BASIS_CERTIFICATION.md 6). With the explicit
    commutator bound for the principal Garding step (error (4/Lambda)(sum_ij S_1(B_ij) + 2 S_1(b_eta)) above frequency
    Lambda, S_1 the first Fourier moment of the coefficient on a periodic cylinder window), the grid gives
    sum_ij S_1(B_ij) + 2 S_1(b_eta) about 1.65e3, hence Lambda about 2.7e4 and a rank of order 1e9 for the margin 0.966:
    not feasible. A global cutoff from the pointwise derivative scale (sup |grad_(t,theta) B| about 140) gives a rank of
    about 4.8e5 (5.0e4 at margin 3). A cutoff adapted locally to the coefficient derivatives gives about 1.2e4 with the
    certified margin 0.966 and 1.2e3 with margin 3, and about 150 with the local grid margin of w_a. So the injectivity
    certificate is plausible only with phase-space localized cutoffs, local margins and certified local error terms;
    the global commutator bound is too lossy by a factor of order 1e5 to 1e7 in rank.
(c) The bilinear bound C_B and the axis jets. U[d] does not vanish on the y-axis (U_2 is even in x), and
    d_y h = x^2 g_h'(y) + O(x^4) there. So W[d].grad h has a nonzero x^2 jet along the y-axis and is not in L^2(w_a)
    by itself (|x|^{4 - 2a} is not integrable for a > 5/2). Its x^2 coefficient on the axis is
       U_2[d](0, y) g_h'(y) + 2 d_x U_1[d](0, y) g_h(y) + (c[d]/3)(2 g_h + y g_h'),
    which belongs to the jet row of Y_lo. The rest is O(x^4) by parity, and |x|^{8 - 2a} is integrable for a < 9/2.
    So for a > 5/2 a finite C_B needs the jet decomposition of the product, and the O(x^4) remainder is admissible
    for a < 9/2 (DERIVED). The trace
    bounds of V026 (U_2 on the axis in H^2_y, d_x U_1 in H^1_y, on strips) are the local ingredients.
(d) Residual membership (THEOREM, V042). Write F(rho~) = x^2 y B(r, theta) (exact factorization of the modal residual),
    gamma(t) := B(e^t, pi/2) and F_R := x^2 y [B(r, theta) - B(r, pi/2)]. Then F(rho~) = E gamma + F_R with gamma in G
    and F_R in L^2(w_a), and the same holds with up to five conormal derivatives x d_x, y d_y.
    - Angular factor: B is even in x, so B - B(r, pi/2) = O(cos^2 theta) and F_R carries cos^4(theta) sin(theta);
      int |cos theta|^{8 - 2a} sin^2 theta dtheta < infinity because a < 9/2.
    - Near 0: B = O(r^2) by the exact normalization (the constant term -2A + D - 1 vanishes); the squared radial
      exponent is 12 - 2a = 7/2 > 0.
    - At infinity: B = O(r^{2k-4}); the squared exponent 4k - 5/4 is negative.
    This is membership only. A certified value of eta = ||F(rho~)||_{Y_lo} (or in Y_sigma) needs quantitative bounds on
    the radial coefficient integrals and is OPEN.

## 4. What is proved (THEOREMS, with verdicts)

Background and normalization:
- V005: the exact-join modal trial has c0 in [15.7260878319246786225638146971829, 15.7260878319246786225638146971831]
  and exact normalization correction z in [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20].
- The numerics team recomputed c[rho~] - (3/k - 1) in [-1.62e-43, 1.62e-43] with independent code (certificate C1 of
  the accompanying S2_NUMERICAL_CERTIFICATES.md).
- V018: the raw X3 strain and normalization defect (section 0).
- V017: the exact modal source exists uniquely at x_P in (4841405518533377, 4841405518533711)/2^49, with mu in
  (0.99999997745, 0.99999997750) and g in (29, 30). So the trial is not stationary at the source, and mu = 1 must not be
  substituted.

Origin (Avenue I and III):
- V022, Theorem O: on the jet-plus-remainder space Z_0 the frozen saddle is bijective modulo span{x^2 y}.
  - The remainder inverse is sharp, with ||T_0^{-1}|| = 1/kappa_0 (kappa_0 = 16.54116 at a = 7/2, b = 6/5).
  - J is a continuous coordinate.
  - The strain extends continuously to r < 1, with explicit constants.
- V025: N1 (a >= 5/2 is necessary for coercivity with x^2 y excluded) and N2 (the anisotropic factor cannot be switched
  off along the outgoing y-axis, conditional on a positive axis rate). Also N3 (the y-axis jet row with the full strain
  term), N4 (far window 2k < gamma < 1 + k with a nonzero leading residual) and N5 (fixed-background obstruction).
- V016: the frozen local strain adjoint, with K_A <= 0.032163.
- V036: the trial is C^{4,1} but not C^5 at 0. The local coupling estimates that use the trial near 0 need only C^4.
- V026: the local vertical-axis piece of (E). On strips of width R, the Taylor-subtracted coupling has an explicit O(R)
  bound, the axis traces are bounded, and the localized jet coupling is compact (C_a = 1759/6 at a = 7/2).

Global Fredholm theory (Avenue I):
- V023 and V031, Theorem R: for radial weights e^{mu(log r)} with mu Lipschitz, Lip(mu) < 2, and a positive global
  margin (H_m), L_fix is Fredholm of index 0 on its maximal domain. A compact K exists with m_* ||h|| <= ||L_fix h|| + ||K h||.
  Injectivity is equivalent to invertibility. (H_m) holds for mu~ and the actual background: m_R >= 1.78605 (V077,
  the verifier's own original-data computation; the numerics team's certificate gives m_* >= 1.029821, aggregation
  verified, V072). So Theorem R is a THEOREM for L_fix and the actual normalized modal background.
- V032: c is not closable on that radial graph, so Theorem R does not carry the normalization.

Normalization functional (Avenue III):
- V034: Prop M (local anisotropic moment), the frozen representer, Corollary C1 (C_c0 < 0.013958 at a = 7/2, b = 6/5;
  C_c0 < 0.017231 at a = 17/4, b = 0) and Prop C2: |c[h]| <= C_cap ||h||_{Z_cap} with C_cap < 0.312093
  (a = 7/2, b = 6/5) and C_cap < 0.359253 (a = 17/4, b = 0).
- V034: Prop B, the rank-one bordering by KP, conditional on an operator domain X embedded in Z_cap with L_ren : X -> Y.
  The far angular moment satisfies 37.63077494715565 < s_3/pi < 37.63077494715567, so c[KP] >= 0 and
  d = 3 c_l + k c[KP] >= 3 c_l > 0 for every smooth cutoff 0 <= chi_inf <= 1 supported in r >= 1.
- V038: the scalar normalization nu(ell, h) = 0 has a unique solution ell(h) > 1 for every finite c[h], with
  d nu/d ell >= 3 and |ell(h) - c_l| <= |c[h]|/3; the augmented map of 2.2 has the Prop B bordered system as its
  derivative; d != 0 permits eliminating the tail coordinate but does not invert L_red (REFUTED as a sufficiency claim).
- V035: a bound |c[h]| <= C ||L h|| holds if and only if c = L^* phi with ||phi|| <= C. It does not need an inverse,
  and an approximate dual phi with certified defect gives it under an auxiliary estimate. Actual adjoint solvability
  is OPEN.

Source (Avenues I and II):
- V011: the full nonlocal frozen source inverse is bijective on H^s for s < 2373/680 on the certified box. Its inverse
  norm is 500/1687 at s = 31/10, and mu = 1 is not a pole.
- V021: an auxiliary variable-coefficient source inverse with explicit bound and sharp strain norm. The rank-one
  extension is invertible exactly when 1 + c[A^{-1} ell_delta] != 0.
- V024: the source neighbourhood, with the perturbation margin kappa - E >= 44699521/14000000.
- V013 (mu = 1) and V029 (the actual modal rate): the frozen source inverse maps compact C^alpha input to C^alpha for
  every 0 < alpha < 1.

Hoelder theory (Avenue II):
- V028: H0, S(a) to S(c). Anisotropic C^alpha_p is bounded under T_0^{-1} if and only if 1 + pA > D alpha, sharp.
  The smooth-cutoff coupling estimate S(d) gives a whole-plane inverse of T_0 plus the localized coupling on C^alpha_1
  for alpha < (1 + A)/D = 0.5227.
- V030: Lemmas N and N' (section 2.3).

Nonlinear structure (Closure):
- V041: the scalar axis row. With d(t) = V_2(0, e^t)/e^t > 0 and the endpoint bounds |d - D| + |d'| <= C e^{nu_- t}
  (t < 0), |d - ell| + |d'| <= C e^{-nu_+ t} (t > 0), the axis row A beta = d beta' + (D - d - 2d') beta is an
  isomorphism from the explicit space B onto the target Gamma (norm ||gamma/(dH)||_{L^2(omega)}), with explicit
  constants; J is a bounded functional and an output of the far condition, and on {J = 0} the range is a closed
  hyperplane. For a = 17/4, Gamma is equivalent to G of 3.1. Positivity of d and the endpoint constants are numerical
  obligations. The global Theorem C of the first draft was not a fully specified conditional theorem (V041).
- V042: membership of the modal residual and of the parameter-family residual in Y_lo (3.5(d)); the free-J augmented
  map (2.2).
- V046: pure transport on the strong spaces. Under (A), the angular coefficient bounds |q - d| <= M_Q cos^2(theta),
  |p - p_axis| <= M_P min(r^2, 1) cos^2(theta) and a positive transport margin kappa_* > 0, T = V.grad - 1 is an
  isomorphism from E B (+) D(T_R) onto E Gamma (+) L^2(w_a), with the exact lower-triangular form [A, 0; B_V, T_R],
  ||T_R^{-1}|| <= 1/kappa_* and the explicit triangular inverse. J is continuous; J = 0 gives a closed range of
  codimension one. This is Lemmas C'1 to C'3 of S2_L2_THEORY.md 5.2.
- V047: Theorem C' with Lemmas C'1 to C'4, CONFIRMED as a conditional theorem on (A), (L) (= the angular coefficient
  bounds), (M) (= (H_m')), (E0), (E-J), (E-G). No adjoint estimate is needed; the lower off-diagonal block need only be
  bounded. (L) holds for the modal field with finite constants. c_R = 0.2075698661066814348... (sharp); zeta in Y_lo.
- V049: the jet row Gamma : E B (+) R -> G is Hilbert-Schmidt under (A), so (E-J) holds. V050: the jet-input coupling
  C E : B -> Y_lo is Hilbert-Schmidt. V051: the remainder-input coupling is bounded on R (near-diagonal dyadic part with
  output-annulus bound C min(r_0^2, r_0^{k-1}), plus a Hilbert-Schmidt part), so (E0) holds. V052: the Garding
  inequality (E-G). These four are CONFIRMED under the explicit annular C^5 and cofactor endpoint bounds (B1), (B2),
  and V053 CONFIRMS that the exact normalized modal density satisfies them. All constants are qualitative.
- V048: scope audit of the report, with corrections (applied). V054: the first certificate script for (A): identities
  CONFIRMED; coverage and underflow steps REFUTED (silently dropped endpoint cells, a 2^{-1200} tail lost in a float
  radius); near-resonant inner Green correction lambda = 75/2^46 in mode 27; S0 domain Gram certification failed.
- V055: transport regularity of the modal field (V globally Lipschitz C^1, V_1/x and V_2/y bounded, endpoint bounds of
  d, finite M_Q, M_P) and the exact energy limits kappa_0 = (19/2) c_l - 13/4 = 49.7159... and kappa_inf =
  1 + 3 c_l/8 = 3.0908.... With V047 and V049 to V053, Theorem C' holds for the modal background under (A) and (M)
  (= (H_m')) alone; injectivity is separate.
- V057: an explicit Hilbert high space H_gamma (cofactor in cylinder H^7) that embeds in Z with classical J, and the
  low/high bilinear bound ||W[d].grad h||_Y <= C ||d||_{X_lo} ||h||_{H_gamma} with the full W and exact axis
  subtraction, and ||D W[h]||_infinity + |c[h]| <= C_V ||h||_{H_gamma}. V060: the same for H_(delta, gamma)
  (origin exponent delta in (1/4, 2), which admits smooth quintic corrections) plus a compact H^s component, s > 2,
  away from x = 0. Constants finite, not computed. Not a range of the frozen corner inverse (see 3.1 and Prop F4, V067).
- V056, V058, V059, V061: numerics audits. The S0 Gram is positive after exact-midpoint whitening (conditional on the
  entry enclosures; no singular value); the float union of the first Taylor range code is REFUTED (V058) and the
  repaired union with resonance merging CONFIRMED (V061); stable Green moment formulas (V059).
- V062: the moving-tail quasilinear formulation. With ell = ell(h) fixed by n(ell) = c[h] and
  M(ell) = H_0 + (B(ell) - B(ell_0))/n(ell), B(ell) = F_ell(rho_ell) - n(ell) H_0, the operator A_h of S2_L2_THEORY.md
  6.7 maps the high space into Y, F_ell(h)(rho_ell(h) + h) = f_0 + A_h h exactly, and
  ||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_{X_lo} ||g||_high (all powers of log r included). The general free-J augmented
  residual is smooth into Y and its derivative is the verified Schur complement. Uniform right inverses into the high
  space, a low inverse estimate and the two smallness conditions imply existence (CONFIRMED as a conditional theorem,
  assuming the positive axis rate). This is the precise form of 3.4 for the moving-tail problem; its inverse hypotheses
  are OPEN.
- V063: Lemma H1 (orbit classification) CONFIRMED under (Z), and a compact escape lemma (V.grad phi >= 1 on any compact
  set without zeros, phi in C_c^infinity, even) CONFIRMED without (Z). Positive divergence and the endpoint data do not
  imply (Z).
- V064: the frozen source threshold with the Riesz coupling retained is sharp: s_fast = (b_0 + g)/A_P, with
  3.57854758171660 < s_fast < 3.57854758172942, and a fixed smooth forcing has no H^s solution for s >= s_fast.
- V065: the cone-local high space (factored H^7 near the vertical axis, cylinder H^s bulk with s > 2 on |cos theta| >= eps,
  origin exponent 1/4 < delta < 2, far exponent gamma < -3/8): classical J, continuous embedding into Z, the low/high
  product bound and the bounded-DW bound, CONFIRMED under the positive axis rate. Inverse preservation OPEN.
- V066: the S0 matrix lower bound sigma_min >= 4.3337e-07 (exact dyadic s = 4093149700530291/2^73), CONFIRMED
  independently as a conditional matrix certificate (conditional on the exported entry enclosures). A finite statement.
- V067: Prop F4 CONFIRMED for the frozen corner operator (formula, maximal weighted inverse, both Sobolev endpoints,
  exclusion of the old high spaces); the parity-only threshold REFUTED (for general data even in x the limit is the
  energy value 2.33392298496953..., attained as m decreases to a - 1/2); the transfer to the true operator OPEN.
- V068: the revised range method and the adaptive angular refinement CONFIRMED as finite-cell methods; the archived
  merge of the production parts REFUTED (it drops the refined arrays and the zero-set data). No global certificate yet.
- V069: the exact modal spline has nonzero seventh-derivative jumps (modes 0 and 1) at the knot
  t = 4958764014967233/2^51; the residual and its axis-jet remainder are locally H^s there exactly for s < 13/2,
  CONFIRMED; smoothness of the residual away from the origin REFUTED. Every high order on that circle and upstream of
  it must be below 13/2; the mapping bounds of V060 and V065 are unaffected.
- V070: on Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2], ||D^2 V||_F < 1.159484 and S(DV) > 0.1801 I, so
  |V(X)| >= 0.1801 |X - P| on Q and P is the only zero there, CONFIRMED.
- V071: Lemma Z (S2_L2_THEORY.md 6.3) CONFIRMED, with the exact source constant 19847539549/20000000000 > 0.992 and the
  polar containment tests for the disc and for Q; the star-shaped Jacobian variant needs alpha_1, alpha_2 > 0 (a
  two-zero counterexample REFUTES the product condition alone).
- V072: the merged production arrays of the margin and axis-rate runs cover all 100416 boxes with finite entries and
  retained refined and zero-set arrays; the summary extrema (m_* >= 1.0298211720474706, m_a >= 0.9659182260060386,
  d >= 5.575203976688894) are reproduced as exact dyadic endpoints. CONFIRMED conditional on the exported cell
  enclosures. Global (Z) OPEN: 86 boxes have a zero lower bound of |V|/r, 77 of them outside Q.
- V073: the mapping side of the high space (product bound, Lipschitz-velocity bound, embedding into Z, classical J) for
  every factored order sigma > 6, CONFIRMED; sigma = 25/4, delta = 3/2, gamma = -1/2, s = 21/10 admissible.
- V074: a bounded same-order forward isomorphism L : H -> Y_H REFUTED (oscillatory packet), and a common graph domain
  for small Lipschitz perturbations REFUTED (d_x - 1 versus d_x + eps d_y - 1); the high theorem must be an
  inverse-regularity estimate (OPEN).
- V075: the margin perturbation of 3.5(a) with coefficient 51/4, CONFIRMED (plus ||grad h||_infinity only when the
  coupling background moves).
- V076: the normalized modal residual lies in Y intersected with the fractional target of order 25/4 (delta = 3/2,
  gamma = -1/2; the proof covers 0 < delta < 2), CONFIRMED (membership only).
- V077: independent original-data certificates (all 1558 spline spans and 261 stream modes rebuilt, 512-bit Green
  moments, 3276 x 128 cells plus the outer continuation and analytic ends, separate 640-bit audit): d >= 5.5752 on the
  whole axis, m_a >= 0.53072 for w_a, m_R >= 1.78605 for mu~. So (A), (H_m') and (H_m) hold, and Theorems R and C' are
  THEOREMS for the actual normalized modal background: L_fix : D_w -> L^2_P(e^{mu~}), L_ren : Z -> Y_lo and
  L_red : Z -> Y_lo are Fredholm of index 0 (complete statement with spaces in the verifier's proof 76). Injectivity,
  inverse norms and existence are not addressed.
- V078: the 34 source exclusions of the numerics team's refinement lie in the exact Q, CONFIRMED; its leaf counts
  REFUTED (359 terminal leaves, not 463).
- V079: the cylinder corner threshold s_x = 3/2 + delta A/(A+D) for v = r^{-(3+delta)} h, with an explicit frozen
  low-domain counterexample at delta = 3/2, s = 21/10 (cone-supported forcing in the target with every cylinder order;
  solution a nonzero multiple of x^{B - nu} sgn(y)|y|^nu, nu = 1 + (delta + tau) A/(A+D), Sobolev threshold 2.0164 at
  tau = 1/10), CONFIRMED; the implication from the Cartesian threshold REFUTED.
- V080: global (Z) for the actual field: the only zeros of V are 0 and (+-p, 0), and |V|/r >= 3/12500 outside Q in the
  closed first quadrant away from 0 (independent original-data cover with exact refinement and a 640-bit audit),
  CONFIRMED. So Lemma H1 (i), (ii) of V063 hold for the actual field.
- V081: the C6 finite matrix (L_fix section in L^2(e^{mu~}), sigma_min >= 0.510914) reproduced at 384 bits from the
  exported entries, CONFIRMED conditional on those entries enclosing the exact pairings. A finite statement.
- V082: the sufficient injectivity lemmas, CONFIRMED as conditional lemmas: the finite adjoint-witness criterion
  (d = m - delta - eps > 0, inverse bound (1 + Psi)/d), the Schur criterion (s = a - b c/d > 0,
  p_0 = (1 + (b/d)^2)^{1/2}/s, inverse bound (p_0^2 + ((1 + c p_0)/d)^2)^{1/2}), and the commutator and principal
  Garding estimates on a regular periodic cylinder. OPEN: their quantitative inputs for the actual operator (singular
  angular conjugation, cutoffs, jet rows, compact-defect approximation, complement bijectivity).
- V083: the homogeneous velocity formulas and the Mellin bound max(|sigma + 1|, 1)/(Lambda - |sigma + 2|) on a regular
  cylinder (sigma = 13/4 near 0, -3/8 at infinity for the radial isometry of w_a), CONFIRMED with that scope.
- V044: the counterexample of 3.1 (L_fix h has a constant axis factor not in G); with the strain term in the coupling
  the image is in Y_lo.
- V045: the cross-region piece (E3) for separated input: input in |x| > 2R, output in |x| < R, |y| < Y, after the
  x^2 axis subtraction, is compact in the weight w_a (0 < a < 9/2, eta < 2), with smooth traces. Adjacent input, uniform
  limits at 0 and infinity and jet inputs are OPEN.
- V043: the S0 tail-column strain values c[KP_shifted] = 0.0703723369886642336..., c[TAU] = 0.0685475542628381482...
  and the denominator 3/k + k c[KP_shifted] = 16.73870985167530795... (independent 512-bit enclosures).
- V038: the exact quadratic fixed-background expansion; the far cancellation with the corrected sign; the parametric
  remainder O(r^{2 max(q,k) - 1}), in the far radial target for max(q, k) < 5/16 (the smaller exponent q + k - 1 was
  REFUTED); the abstract two-norm theorem of 3.4 under reflexivity and compatible solution operators. Its application to
  the moving-tail IPM equation is OPEN.

Finite-basis method (Avenue IV):
- V014: exact conformity criterion, continuum Gram formulas, and the requirement of a complement inverse.
- V039: Prop IV.O of the accompanying S2_BASIS_CERTIFICATION.md. The S0 realization (factor domain, density target) maps
  into a closed subspace of infinite codimension and is not bounded below (zero-strain angular packets with ratio
  O(eps^2)), so no finite S0 singular value extends to a continuum inverse in those norms.
- V040: Lemma IV.1 as a conditional theorem, with the transport extension: ||g|| <= (1 + Psi)/(m_W - delta - eps - p)
  ||A g||, with p built from dW ||r grad psi_i|| and (2|c|/3 + (M + 4a) dW) ||psi_i||. The split, the adjoint defects
  and the numerical inverse are OPEN.
- V020, V027, V033, V037: audits of the numerics team's code; the listed repairs are confirmed, and the defects are
  recorded. V037 (02:58Z) confirms the directed endpoints, exact row maxima, gradient and anisotropic quotient formulas
  and the plain-B decomposition, and leaves two arithmetic obligations (a positive-subnormal discard and the float
  inflation of the tail bound), which the numerics team reports fixed at 03:00Z (not yet re-audited). An anisotropic
  margin is global only if no box returned a nonfinite value.

Obstructions (THEOREMS, each with an explicit counterexample): V006 (centre quasimodes in X_m), V007 (pointwise cubic
coefficient), V009 (first fractional mode), V010 (radial moment gap), V012 (J nonclosed at fixed strain), V019, V030,
V032, V039, V074, V079, and the refuted parts of V025, V028 and V038.

## 5. The missing estimates, in order

The edge Garding lemma (E), the first missing inequality at earlier versions, is proved for the modal background in the
form (E0), (E-J), (E-G) of S2_L2_THEORY.md section 5 (V049 to V053). With Theorem C' (V047), L_red : Z -> Y_lo is
Fredholm of index 0 under (A) and (H_m'), and both hold for the actual background (V077). The remaining items are:
1. (A) and (H_m'): DONE (V077; d >= 5.5752, m_a >= 0.53072, m_R >= 1.78605 for Theorem R, independent original-data
   computation). The numerics team's sharper one-team values (m_a >= 0.965918, kappa_* >= 3.037693, d in
   [5.575203, 21.301451], the endpoint constants 0.100883, 0.202073, 89.3342, 73.3113) keep their one-team status and
   matter only for quantitative bounds.
2. Injectivity of L_red on Z with a quantitative inverse bound (K_L at h = 0). This is the complement estimate. It needs
   explicit constants for the qualitative compact operators of V049 to V052 and a finite-rank split of K_eps. The
   abstract criteria that turn such a split into an inverse bound are proved (V082); the regular-cylinder commutator,
   Garding and Mellin estimates are proved (V082, V083); the actual-operator errors are not.
3. The high-norm inverse K_H in the variable-order X_hi (Theorem H of S2_L2_THEORY.md 6.6, DERIVED outline).
   Hypothesis (Z) of Lemma H1 holds for the actual field (V080), so the orbit classification and qualitative escape
   functions are THEOREMS; quantitative escape constants are not. The high orders must be below 13/2 on a knot circle of
   the background and upstream of it (V069); the order 25/4 is admissible for the mapping side (V073), and the residual
   lies in the target (V076). Near the corner the cylinder threshold forces delta > (A+D)(1/2 + eps)/A and
   eps < 0.14547 (V079); delta = 9/5, s = 41/20 is admissible. The estimate must be proved in inverse-regularity form
   (graph domain), since a bounded same-order forward isomorphism is false (V074). An external consultation identified
   further needed hypotheses (S2_L2_THEORY.md 6.6 (a) to (g); claims, not verification records): global weighted
   high-order control of the combined coupling and normalization terms (a rank-one construction shows that smoothness
   of the normalization profile is not enough; for L_red this asks for zeta in Y_H and an order gain of C), the
   regularization step from the low domain, and tame (not only C^1) dependence on g for uniformity; the uniform estimate
   then follows from the low bound by absorption but surjectivity needs the graph-domain construction.
4. The bilinear bound C_B and the Lipschitz bound C_V in that X_hi. They are THEOREMS with finite, uncomputed
   constants for the cone-local space of V065 and V073, with order s > 2 near the closed x-axis segment and the origin
   (41/20 with delta = 9/5 is inside their ranges and below the cylinder corner threshold 2.0809 of V079). Explicit
   values are not available.
5. A certified enclosure of the residual eta in Y_sigma. Membership, axis jet included, is THEOREM in Y_lo (V042) and in
   the fractional high target of order 25/4 (V076).
6. The moving-tail formulation and its conditional iteration are THEOREMS (V062). What remains are its hypotheses:
   uniform right inverses into the high space for the family A_v (item 3, with the ell-dependence of the compact part of
   the Garding estimate bounded), the low estimate K_L (item 2) and the smallness conditions with the certified eta.

## 6. Constants that need certification

| Quantity | Needed for | Status |
|---|---|---|
| c[rho~] = 3/k - 1 (exact normalization) | every rigorous statement | CERTIFIED (V005; numerics team C1) |
| source x_P, mu_P, g_P | source inverse | THEOREM (V017) |
| source neighbourhood margin kappa - E | source inverse | THEOREM (V024) |
| m_* for mu~ (H_m) | Theorem R for L_fix | THEOREM (V077): m_R >= 1.78605 (independent original-data computation); the numerics team's certificate gives m_* >= 1.029821 (aggregation verified, V072), refined to m_* >= 2.471224 (one team, 05:58Z); grid 2.590 |
| m_a for w_a (H_m') | Theorem C', scheme | THEOREM (V077): m_a >= 0.53072; one-team certificate m_a >= 0.965918 (aggregation verified, V072), refined to m_a >= 2.500023 (one team, 05:58Z); grid 3.09 |
| positive axis rate q(0, y) > 0, y != 0, with endpoint bounds (A) | N2, V041 axis row, V046, Theorem C' | THEOREM (V077): d >= 5.5752 on the whole axis, with the qualitative endpoint estimates of V055; one-team quantitative values d in [5.575203, 21.301451], sup abs(d') <= 5.6012, endpoint constants 0.100883, 0.202073 (t <= 0) and 89.3342, 73.3113 (t >= 0) |
| angular coefficient constants M_Q, M_P and transport margin kappa_* for w_a | V046 (Lemmas C'1 to C'3) | finite for the modal field (V047); box bounds M_Q <= 337.66, M_P <= 1075.52, kappa_* >= 3.037693 (same production run, aggregation verified, V072) |
| constants of (E0), (E-J), (E-G) and a finite-rank split of K_eps | K_L | finite (V049 to V053); not computed |
| hypothesis (Z): V has no zero on the closed quadrant other than 0 and P, and DV(P) is a hyperbolic repeller | Lemma H1 (THEOREM under (Z), V063), Theorem H (S2_L2_THEORY.md 6.3, 6.6) | THEOREM (V080): the zeros are 0 and (+-p, 0); abs(V)/r >= 3/12500 outside the source rectangle Q (closed first quadrant, away from 0); abs(V(X)) >= 0.1801 abs(X - P) on Q (V070) |
| d = 3 c_l + k c[KP] != 0 | rank-one bordering | THEOREM (V034): d >= 3 c_l > 0 for every admissible cutoff; for the numerics team's shifted column, d lies in [16.73870985167530795255805332462072, 16.73870985167530795255805332462074] (THEOREM, V043) |
| s_3 = int sin(3 theta) Theta_0 | the sign of c[KP] | THEOREM (V034): 37.63077494715565 < s_3/pi < 37.63077494715567 |
| C_a, trace constants | (E) | THEOREM at strip scope (V026); (E) itself THEOREM with qualitative constants (V049 to V053) |
| Prop C2 constant C_cap | c bounded on Z_cap | THEOREM (V034): C_cap < 0.312093 (a = 7/2, b = 6/5), C_cap < 0.359253 (a = 17/4, b = 0) |
| K_A <= 0.032163 | frozen c adjoint | THEOREM (V016) |
| finite-section sigma_min and off-basis residual | Avenue IV | S0: sigma_min >= 4.3337e-07 with TAU (V066, conditional matrix certificate), >= 2.0685e-02 without TAU (once); a finite statement (V039); off-basis residual not computed |
| r_V (half-margin radius) | closure inequalities 3.4 | the perturbation coefficient is THEOREM (V075): for the fixed background the margin drops by at most abs(c[h])/3 + (51/4) norm(D W[h]) (plus norm(grad h) when the coupling background moves); the constants C_c, C_W (and C_g) of the high space are not computed |
| eta, K_H, K_L, C_B, C_V | closure inequalities 3.4 | not available (C_B, C_V finite by V057, V060, V065, V073) |

## 7. The closest avenue and why

The closest route combines Avenues I and III and uses Avenue IV for the complement:
- the anisotropic L^2 space Z with weight w_a;
- the jet coordinate J and the y-axis jet;
- the rank-one bordering by KP, or by ell in the parametric form;
- a certified finite-dimensional injectivity check for the compact part of the Garding estimate.

Reasons:
1. Every frozen piece is proved with explicit constants: Theorem O at the origin (V022), the source inverse (V011,
   V021, V024) and the far window (V025, N4).
2. The global Fredholm mechanism is proved for radial weights (V023, V031) and, for the full normalized operator on the
   jet spaces with w_a (V047 with V049 to V053), and both hold for the actual background with the margins and the axis
   rate certified independently (V077). So the whole problem at h = 0 is reduced to injectivity.
3. The normalization is handled exactly. c is bounded on Z_cap (Prop C2, V034), and the need for the origin part of
   Z_cap is a theorem (V032). d >= 3 c_l > 0 is a theorem (V034), so the tail coordinate (KP or ell) can be eliminated
   exactly. This does not invert the reduced operator L_red: when L_ren is invertible, L_red is invertible if and only
   if the scalar 1 + c[L_ren^{-1} zeta] is nonzero (V038), and L_ren still needs its own inverse. The scalar
   normalization ell(h) is unique with |ell(h) - c_l| <= |c[h]|/3 (V038).
4. The certified margins are m_a >= 0.53072 for w_a and m_R >= 1.78605 for mu~ (THEOREM, V077; one-team values 0.9659
   and 1.0298; grid values 3.09 and 2.59), against a perturbation cost that 3.5(a) bounds linearly in
   ||D W[h]||_infinity.
5. By 3.5(b), for a fixed background, uniformity over the correction ball reduces to the single h = 0 complement estimate (in the parametric form the ell-dependence of K must also be bounded), because the compact
   part does not depend on h.

Avenue II is farther. There is no Hoelder analogue of the sharp Garding inequality. The Hoelder theory of the actual
transport near 0 is OPEN (the conjugacy transfer was REFUTED, V028). Lemmas N and N' show that C^alpha alone cannot
close the nonlinear problem.

Avenue IV alone is farther. A finite section is not an inverse bound without a complement inverse (V014). The first
exact section (S0: 4 angular modes, 169 columns) is certified as a finite statement (V066), but in its realization no
continuum bound is possible (V039).

## 8. Checklist against the strict standards (PROMPT 11)

| Standard | Status in this run |
|---|---|
| Inverse statements give domain and range | Theorem O (Z_0 -> Y), Theorem R (maximal domain D_w -> L^2(w)), source inverses (maximal H^s realizations), V041 axis row (B -> Gamma, conditional on d > 0), V046 pure transport (Z -> Y_lo, conditional on (A), the angular coefficient bounds and kappa_* > 0), Theorem C' (Z -> Y_lo, THEOREM as a conditional statement, V047, and THEOREM for the actual background, V049 to V053 and V077) |
| Membership of perturbation and image | checked: x^2 y in Z_0 (J = 1); r^k Theta not in Z; r^{2k-1} Eps in the far target; the coupling image of Z in Y_lo (V049 to V053); the residual and the parameter-family residual in Y_lo (V042, membership, no norm) |
| Normalization meaningful and closed | J is continuous on Z_0 (V022). c is bounded on Z_cap (THEOREM, Prop C2, V034) and on Z (Lemma C'4, V047). c is not closable on the radial graph (V032), and J is not closed in the weak norms (V012), so neither of these weaker spaces is used for the normalization |
| Log variation of exponent perturbations | KP = chi_inf r^k log r Theta_0 carried explicitly; parametric family rho_bar_ell (2.2); log^2 second variation noted (V025) |
| Full infinite-dimensional operator, not its matrix | finite sections are used only with a complement estimate (V014); the complement is OPEN |
| No unproved finite rank, compactness or small residual used as invertibility | complied with; the Fredholm statements are labelled as such, the qualitative compact operators are never used as bounds, and injectivity is OPEN |
| Absence of proof is not nonexistence | complied with (section 1) |
| Counterexamples where a bound fails | given: V006, V007, V009, V010, V012, V019, V025, V028, V030, V032, V039, V044; Prop F4 (THEOREM for the frozen corner operator, V067: the corner singularity limiting the high order); V067 (parity-only threshold); V069 (knot jump limiting the high order below 13/2); V074 (no same-order forward isomorphism); V079 (frozen low-domain corner solution excluding delta = 3/2, s = 21/10 in the cylinder norm); code defects V020, V027, V033, V037, V054, V058, V068 (merge) |
| Bounds valid but too large | the V026 constant C_a (about 593 at a = 17/4) forces strip width R < 0.02/sup abs(rho_2). Whether this loss is intrinsic is OPEN |
