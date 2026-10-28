# S2_CLOSURE.md: status of the nonlinear existence theorem

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T02:47Z (theory author), updated 02:55Z after V034 to V036, 03:06Z after V037 and V038, 03:24Z after V041 and V042, 03:34Z after V043 to V046, 04:11Z after V047 to V054, 04:47Z after V055 to V061 and Prop F4, 04:58Z after V062 to V064, 05:16Z after V065 to V068 and Lemma Z, and 05:26Z after the box certificates of the margins and of (A) (computed once) and 05:35Z after V069 to V072, and 05:45Z after V073 to V076 and a rank estimate for the injectivity certificate, and 05:54Z after V077 to V080 (Theorems R and C' unconditional for the actual background, global (Z), the cylinder corner threshold), and 06:01Z after V081 to V083 (C6 reproduced; the injectivity lemmas; the Mellin bound), and 06:13Z after V084 to V087 (with Lemma INJ-S, DERIVED), 06:39Z after V088 to V096 (Lemma INJ-S THEOREM; the second-order principal energy; a revised rank scale), 06:45Z after V097 to V100 (full regular Mellin energy; regular-patch conjugation; strip constants 39 and 25; exact angular target norm), and 07:01Z (Lemma H-spec for the remainder block, Corollary H-spec for the jet row) and 07:04Z after V101 to V105 and 07:16Z after V106 (H-spec: abstract theorem confirmed, direct free-J form refuted) (INJ-Q; exact localization; frozen regularization in both corner charts; trace and lift majorants). Labels follow the accompanying CONVENTIONS (item S8): Updated 08:03Z after V107 and V110 to V118 (the size of the strong residual, the jet-row conditions of the high inverse) and 08:14Z after V120 to V122 (exact far rate, weight family, quadrature audit) and 08:31Z after V123 to V125 (certified far tail) and 08:55Z after V126 to V129 ((H1) and (H2) on the variable-order space) and 09:43Z after V130 to V137 (the order function, the origin normal family, stable end inverses, source margin 4.52536; Proposition H3-red) and 09:59Z after V138 to V140 (Lemma Hs-sym, Proposition Hs) and 10:10Z after V141 to V144 and 10:24Z after V146 to V150 (all calculus inputs of Proposition Hs) and 10:33Z after V151 to V155 (Proposition Hs and (H3) on X_s, the high Fredholm theorem, the perturbation status) and 11:20Z after V156 to V163 (the uniform high theory for small frozen-coupling transport perturbations) and 11:50Z after V164 to V174 (the full residual enclosure, the bordered, low and moving-tail uniform theory, the decoupled weight family) with Theorem E (conditional existence, DERIVED) and 11:54Z after V175 to V178 (the decoupled-family inverse and difference theory; Lemma Emb THEOREM; Theorem E CONDITIONAL THEOREM), and 12:03Z after V179 and V180 (low residual lower bound 3.270; finite-section accounting), and 12:16Z (section 7, items 6 to 8: the assembly, a constant-free necessary test of (S), what the trial must improve), 12:17Z after V181 and V182 (outer-merge coverage checks insufficient; a loose certified majorant of the high residual norm), and 12:44Z after V183 and V184 (a certified high-norm lower bound; the necessary test of (S) confirmed), and 13:09Z after V185 to V194 (the stronger lower bound 3.866e10; two constant-free tests of (S) and a heuristic violation, section 7 item 9), and 13:18Z (a floating axis check of the heuristic; V195 to V197), and 13:27Z (V198, V199), and 13:49Z (item 9: the span-by-span knot-scale scan), and 14:09Z (V203 to V208, the localized origin inverses in Hoelder spaces), and 14:12Z (V210, V211), and 14:20Z (V213 to V217), and 14:34Z (the V213 cross-audit; V219), and 14:59Z (V222, V224, V226 to V228: the common Hoelder target; the far obstruction to a bounded inverse on it, DERIVED) and 15:12Z (V232, V234: the far obstructions are THEOREMS; V235, V236: the scaled far target, DERIVED) and 15:30Z (V242: the exterior inverse is a THEOREM; V243: infinite cokernel on the scaled target, DERIVED) and
15:36Z (V244: the scaled-target mapping theory is a THEOREM; V245: the scaled quadratic-axis target, DERIVED) and 16:06Z (review corrections V248, V250, V251, V253, V255; V246, V247, V249, V252, V254 integrated; V256 turning-height obstruction on Z_2, DERIVED; THEOREM since V262, 16:19Z) and 16:14Z (V257: the
refinement to alpha > 1/2 for A_0 and L_ren, DERIVED; THEOREM since V265, 16:23Z; V259: m_a >= 3 VERIFIED) and
16:25Z (V264: nonlinear derivative loss on Z_cof, DERIVED) and 16:36Z (V268: the joint-cofactor target V261 is a THEOREM; V266: transport alone not onto Z_2 or Z_cof near the source, DERIVED; consistency corrections) and 16:41Z (V271: V264 is a THEOREM) and 16:43Z (V272: V266 is a THEOREM, transport only) and 16:56Z (V274: review corrections; summary, 3, 5) and 16:58Z (V276: the coupling tail is sharp) and 17:04Z (an exact Gaussian test direction, 7 item 9) and 17:10Z (V283: the Gaussian direction is a THEOREM; V278, V281: sharp renormalized tail, section 3; independent audits of V276 and V278 passed) and 17:17Z (V286, V287: the sharp tails V276 and V278 are THEOREMS) and 17:53Z (V304: c[d] != 0 in the strict residual-subtracted test, item 9).
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
if it is injective; the global flow of the background has exactly the expected zeros (V080). The high-order
inverse theory (conditional on base low injectivity) and certified enclosures of the residual size are in place; the
missing pieces are base low injectivity (I), quantitative inverse and closure constants, and the smallness condition (S)
(section 5). The archived trial has a large certified residual in the strong norm: 6049.11 < ||F||_Y < 8601.42 (THEOREM,
V164; about 7.2e3 by a single-team all-mode computation, NUMERICAL, 3.5(d)), and in the high norm
3.866e10 < eta_* < 6.321e129 in an explicitly fixed equivalent norm (THEOREMS, V192, V182; the upper end is a
loose majorant); a failure of (I) or (S) has not been established. If K_H and C_V were of order one, the
closure inequalities would fail by orders of magnitude, whatever the high inverse turns out to be, unless the weight
or the trial is changed.
This is a heuristic concern only: no lower bound for the actual constants is proved, the failure of (S) is OPEN, and no
certified direction violates the constant-free necessary tests V185, V194, V199 (V248, V255). In
the decoupled weight family (far weight lowered by 0.6, angular exponent a in [18/5, 4]) the certified low norm is
between 3.270 and 485.632, with margin at least 1.10534 and the full low Fredholm theory (THEOREM, V171, V172, V174, V179). The uniform
inverse theory of the exact moving-tail family is complete up to injectivity of the base low operator (THEOREM, V166,
V168 to V170), and existence reduces exactly to that injectivity and one smallness condition with qualitative
constants and the high residual norm, which is enclosed in an explicitly fixed equivalent norm as
3.866e10 < eta_* < 6.321e129 (THEOREMS, V192, V182; the upper end is a deliberately loose majorant): Theorem E (section 5 item 6) is a CONDITIONAL THEOREM (V178), with its
embeddings Lemma Emb a THEOREM (V177), in both the original and the decoupled low spaces (V175, V176). It is a
conditional existence theorem, not an unconditional existence proof for the actual trial.

## 2. The exact nonlinear structure (task item 7)

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
  remainder and its parameter derivatives lie in the far radial target whenever max(q, k) < 5/16 (k is about 0.17936).
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
- J free, final normalization (V087). The restriction of L_red to ker J is Fredholm of index -1, so an onto theorem on
  Z does not carry over to J = 0 (REFUTED); if L_red is invertible, its range on ker J is the hyperplane
  J[L_red^{-1} f] = 0. The existence problem is therefore solved with J free. A classical solution rho_* with cubic
  coefficient 1 + j > 0 is normalized afterwards by rho_norm(X) = lambda rho_*(X/lambda), lambda = (1 + j)^{1/2},
  which preserves the speed c_l and the far exponent and multiplies the far angular profile by (1 + j)^{(1 - q)/2}
  (THEOREM, V087, with explicit small-j bounds; this final scaling is distinct from the fixed-tail correction chart).
- Membership (THEOREM, V042). For max(q, k) < 5/16 on a compact ell-interval, F(rho_bar_ell; ell) - nu(ell, 0) H_0
  lies in Y_lo of 3.1, smoothly in ell, with up to five conormal derivatives. Membership for a general correction h
  in a specified correction space is OPEN.

2.3 Derivative loss (THEOREM, V019 and V030).
- N(h) = W[h].grad h loses one derivative. In the weak graph norm of the earlier diagnostic space it is not even
  continuous at the certified modal source (V019).
- For every 0 < alpha < 1, h -> L^{-1} N(h) is unbounded on C^alpha-bounded sets near a regular axis point (Lemma N),
  and inputs with bounded C^alpha graph norm can have ||N||_{C^alpha} >= c n (Lemma N'), V030.
- So the explicit semilinear fixed-point map built on h -> L^{-1} N(h) does not close when h is measured only in a
  transport graph norm or in C^alpha, within the hypotheses of Lemmas N and N' (V253); quasilinear schemes, stronger
  spaces and the existence of a profile are not addressed by this.
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
  background by the verifier's own original-data computation (V077: d >= 5.5752, m_a >= 0.53072; both margins are
  at least 5/2 by V086, m_a >= 2.9270 by V197 and m_a >= 3 by V259), so L_red : Z -> Y_lo
  is Fredholm of index 0 (THEOREM). Its uncoupled part, the pure transport T : Z -> Y_lo, is an isomorphism (THEOREM as
  a conditional statement, V046, on (A), (CB) and kappa_* > 0; (A) is V077, (CB) is finite by V047 and V055, and
  kappa_* >= 1.6377 from the verifier's own finite cells, V077 note).
- The renormalized coupling must be part of the realization: L_fix does not map Z into Y_lo, and c[.] H_0 is not a
  bounded perturbation into Y_lo (THEOREM, V044, counterexample h = x^4 y eta_0(r)).
- X_hi: a space of variable order (S2_L2_THEORY.md 6.6): order 2 + eps on a neighbourhood (in the polar blow-up) of the
  closed segment [0, x_P] x {0} of the x-axis (ordinary derivatives; in the corner, cylinder derivatives of
  h/r^(3+delta)), with eps < 2A/(A+D) - 1/2 (about 0.14547) and origin exponent delta in ((A+D)(1/2 + eps)/A, 2), forced by
  the cylinder corner threshold s < 3/2 + delta A/(A+D) (THEOREM for the frozen operator with an explicit low-domain
  counterexample at delta = 3/2, s = 21/10, V079); delta = 9/5, s = 41/20 is admissible,
  conormal order N near the y-axis and scaled order N at infinity, nondecreasing along the flow. A uniform order is
  impossible for the frozen corner operator: by Prop F4 (S2_L2_THEORY.md 6.2, THEOREM, V067) the frozen saddle maps a
  smooth compactly supported source to -C x^4 sgn(y)|y|^{2 - 1/D}, so no frozen inverse reaches H^s across the x-axis
  segment for s >= 5/2 - 1/D, about 2.4531 (and for general L^2(w_a) data even in x the limit is the energy value 2.334,
  V067). For the true operator the transfer is OPEN. The
  frozen source threshold at P, s_fast (about 3.5785; sharp, V064; the box-uniform value 2373/680 of V011), is therefore
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

3.3 Constants (each must be a proved bound). At this version eta is enclosed in the low norms and in a fixed high norm
(3.5(d); V164, V174, V179, V182, V192), C_B and C_V are finite but not computed, and K_H, K_L and r_V are not available
(V255).
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
    certified margin 0.966 and 1.2e3 with margin 3, and about 150 with the local grid margin of w_a. So, by these estimates for the chosen
    method (not a proved necessary dimension, V250), the injectivity certificate appears feasible only with phase-space
    localized cutoffs, local margins and certified local error terms, and the global commutator bound is estimated to be
    too lossy by a factor of order 1e5 to 1e7 in rank.
    Second-order revision. The principal real energy error above Lambda is of second order,
    eta/2 + (S2mat(B) + S2(b_eta))/(2 Lambda^2) with the second Fourier moments (THEOREM on a regular cylinder, V096);
    for the full regular Mellin velocity with coefficients g_1, g_2 the error gains G_0 E_0 + 6 K G_1/(Lambda - 2 -
    |sigma + 2|)^2 and stays of second order (V098); the paired weight conjugation is Hilbert-Schmidt with an explicit
    bound on a compact regular patch (V097); the axis-strip constant is explicit in four background derivatives,
    A_ax = sqrt(W_max)[39 M_20 + (25 s_0/2) M_21 + (39 s_0^2/6) M_40 + (25 s_0^3/24) M_41] (V095, V099); and the
    conditional algebra of the split is CONFIRMED (V094). The certificate is one conditional statement, INJ-Q
    (CONDITIONAL THEOREM, V102): with m = 5/2, eps the high-frequency bound of S = sym(C_R) - M_(b_+) on ran Q,
    delta_F the finite-rank error of S_F = P S + S P - P S P and columns with Gram bounds e, p, d (actual Hilbert
    pairings), a = 5/2 - eps - delta_F > e d gives S_1 bijective with ||S_1^{-1}||_R <= (1 + e p)/(a - e d) and the graph
    bound (k_1^2 + (1 + M_C k_1)^2)^{1/2}; eps = c_loc^2 max E_j + eps_small + sum delta_l, with every localization,
    tail, lift and comparison error listed. Localization is exact for the transport energy, with the paired double
    commutator as the coupling defect (V101); the trace functionals and the radial lift have explicit majorants
    (V105). The jet system and the scalar border keep their own certificate (Lemma INJ-S). Grid values (NUMERICAL; accompanying code injrank/rank2.py, s2_estimate.py, s2_local.py,
    s2_noaxis.py): sum_ij S2(B_ij) about 2.15e4 and S2(b_eta) about 3.46e4 at eta = 0.1, so a principal budget E = 1
    (3/2) needs Lambda about 172 (139), about 5.2e4 (3.4e4) low modes per parity class against about 4.7e6 at first
    order; radial localization gives 2.8e4 (1.8e4) before localization errors; removing the vertical-axis strip gives
    1.3e4 to 1.9e4; a local proxy with |D^2 B| in place of the moments gives about 130. A certified split of the
    estimated order 1e4 modes (an estimate for this method, not a proved necessary dimension) is beyond the computing
    means allowed in this work.
    Lemma INJ-S (reduction of the injectivity certificate to the remainder block and a one-variable system; THEOREM,
    V092, with the norm form of (iv) below). Notation of Theorem C' step 1 (S2_L2_THEORY.md 5.2): for h = E beta + h_R in
    Z = E B (+) D_R write gamma_C[h] = Gamma_B beta + Gamma_R h_R (Gamma_B : B -> Gamma and Gamma_R : D_R -> Gamma
    compact by (E-J)), c[h] = c_B beta + c_R h_R with c_B beta = (1/4) int e^{2t} beta dt (Lemma C'4), and
    zeta = E zeta_J + zeta_R in Y. Then
       L_red(E beta + h_R) = E[(A + Gamma_B) beta + Gamma_R h_R + c[h] zeta_J] + [X beta + S_1 h_R + c[h] zeta_R],
    with S_1 = T_R + C_R : D_R -> R Fredholm of index 0 (Theorem C' step 2). Assume S_1 is injective, hence bijective,
    with s_1 := ||S_1^{-1}||_{R -> D_R} (graph norm). For f = E phi_J + phi_R in Y put s := c[h]. Then L_red h = f holds
    if and only if h_R = S_1^{-1}(phi_R - X beta - s zeta_R) and (beta, s) in B x R solves M_J(beta, s) = g_f with
       M_J(beta, s) := ( A' beta + s z_J ,  l beta - s (1 + c_R S_1^{-1} zeta_R) ),
       A' := A + Gamma_B - Gamma_R S_1^{-1} X : B -> Gamma,   z_J := zeta_J - Gamma_R S_1^{-1} zeta_R in Gamma,
       l := c_B - c_R S_1^{-1} X (a bounded functional on B),
       g_f := ( phi_J - Gamma_R S_1^{-1} phi_R ,  -c_R S_1^{-1} phi_R ) in Gamma x R.
    Consequences. (i) h -> (beta, c[h]) is a bijection of ker L_red onto ker M_J (the second row returns s = c[h]), so
    L_red is injective if and only if M_J is. (ii) M_J = (A (+) (-1)) + compact (Gamma_B and Gamma_R S_1^{-1} X are
    compact, Gamma_B not of rank one in general; the other corrections have rank at most one), so M_J : B x R -> Gamma x R is Fredholm of index 0. (iii) L_ren is invertible if
    and only if A' is, and then M_J is invertible if and only if the scalar
    1 + c_R S_1^{-1} zeta_R + l A'^{-1} z_J = 1 + c[L_ren^{-1} zeta] is nonzero (the criterion of V038 in reduced form).
    (iv) Bounds, with Hilbert product norms (V092): (||beta||_B^2 + |s|^2)^{1/2} <= ||M_J^{-1}|| (1 + (||Gamma_R|| +
    c_R) s_1) ||f||_Y (for the sum ||beta||_B + |s| insert a factor sqrt(2); a two-by-two example shows that it is
    needed) and ||h_R||_{D_R} <= s_1 (||phi_R|| + ||X|| ||beta||_B + |s| ||zeta_R||). A certified L^2 inverse bound k_1
    of S_1 gives the graph-norm bound s_1 <= (k_1^2 + (1 + ||C_R|| k_1)^2)^{1/2}, and c_R has norm
    ((58/99)(6618/725) B(3/2, 19/4)/pi^2)^{1/2} < 0.20757 on R and on D_R (THEOREM, V093). Proof: block elimination; for (i), if
    M_J(beta, s) = 0 and h_R = -S_1^{-1}(X beta + s zeta_R), then c[h] = l beta - s c_R S_1^{-1} zeta_R = s by the second
    row, and the first row and the definition of h_R give L_red h = 0.
    Use. The two-dimensional certificate is needed only for S_1 on the plain space R = L^2(w_a): Lemma IV.1 with the
    Garding inequality of Theorem C' (iii) at margin m_a - eps >= 5/2 - eps (V086), without jet rows and without the
    rank-one normalization term. The jet coupling, the cubic coordinate and the normalization then form the system M_J
    for functions of one variable plus one scalar; its compact part involves S_1^{-1} only through Gamma_R S_1^{-1} X,
    Gamma_R S_1^{-1} zeta_R and c_R S_1^{-1}, and a certificate needs explicit tail bounds for these (OPEN). If
    ||(A + Gamma_B)^{-1}|| ||Gamma_R|| s_1 ||X|| < 1, A' is invertible by a Neumann series, and (iii) leaves one scalar.
(c) The bilinear bound C_B and the axis jets. U[d] does not vanish on the y-axis (U_2 is even in x), and
    d_y h = x^2 g_h'(y) + O(x^4) there. So W[d].grad h has a nonzero x^2 jet along the y-axis and is not in L^2(w_a)
    by itself (|x|^{4 - 2a} is not locally integrable for a >= 5/2, V255). Its x^2 coefficient on the axis is
       U_2[d](0, y) g_h'(y) + 2 d_x U_1[d](0, y) g_h(y) + (c[d]/3)(2 g_h + y g_h'),
    which belongs to the jet row of Y_lo. The rest is O(x^4) by parity, and |x|^{8 - 2a} is integrable for a < 9/2.
    So for a >= 5/2 a finite C_B needs the jet decomposition of the product, and the O(x^4) remainder is admissible
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
    This is membership only. The size (08:03Z):
    - Enclosure (THEOREM, V164): 6049.11 < ||F(rho~)||_Y < 8601.42, by interval integration of the original data over
      all angular modes, 1860 radial cells on -40 <= log r <= 20 and both analytic tails (thirteen 640-bit replays). It
      supersedes the lower bound ||F(rho~)||_Y > 933.47 (THEOREM, V110) from the remainder energy on
      9.9 <= log r <= 10.1 alone, with the exact angular reduction of V100 and six directed point densities (V107).
    - Value (NUMERICAL, one team, original data, all angular modes, 81 radii at spacing 1/4 in t on [0, 20], further
      points to t = 60): eta about 7.24e3 (squared norm 5.24e7). Halving the step changes the squared norm by about
      1 percent. Shares of the energy: t in [0, 4] 0.07 percent, [4, 8.135] 4.72 percent, [8.135, 12] 69.84 percent,
      [12, 20] 25.0 percent, beyond 20 0.39 percent (shares with exact exponential partial-segment integration; the
      quadrature value is reproduced independently, and coarser nodes or trapezoids give 7202 and 7253; CONFIRMED as
      arithmetic only, V122). The axis energy on [0, 20] is about 123.4, so the axis norm is about 11.1. The far energy
      density decays at the rate 4k - 5/4 exactly: the residual has a nonzero term of degree 2k - 1 with remainder
      energy coefficient in (4577286933.12061, 4577286933.12062) in the t variable (THEOREM, V120; an asymptotic
      formula, not a finite-radius tail bound). The far tail is certified (THEOREM, V125, all angular modes, axis and
      remainder): the energy beyond t = 20 lies in (203443.34, 203445.56), beyond 25 in (14192.84666678,
      14192.84666680), beyond 30 in (990.0012675088110412, 990.0012675088110415); V123 gives < 3175 beyond 40 and
      < 0.666 beyond 45. The quadrature value beyond 20, about 2.04e5, agrees to 0.5 percent. The enclosure of V164 covers the rest.
    - Structure. The residual is pointwise small: sup |F|/sup |rho~| on circles is between 1e-8 and 3e-7 for
      0 <= t <= 20. Its strong energy lies in a thin angular layer at the vertical axis: the fraction of the remainder
      energy within 0.01 rad of the axis is 0.88, 0.98, 0.996, 0.997, 0.94, 0.55, 0.54 at t = 2, 4, 6, 8, 10, 15, 20.
      The angular spectrum of the residual quotient is nearly flat up to mode about 160 and falls after it. The weight
      |cos theta|^(-17/2) amplifies this layer. Angular truncation at 60 or 120 modes changes the value by orders of
      magnitude (non-monotone), so truncated projections are not usable for eta (compare V111).
    - Weight dependence (NUMERICAL). With angular exponent a and far weight r^(-5/4 - 2 Delta): eta about 7241, 1006, 212
      at a = 17/4 and Delta = 0, 0.2, 0.4; about 1833, 220, 43 at a = 4; about 791, 83, 14 at a = 3.8; about 396, 38,
      5.3 at a = 3.6. The weighted margin changes exactly by (a - 17/4)[tan(theta) V.grad(theta) - q 1_{r<1}] -
      Delta q 1_{r>=1} (DERIVED), its far limit is 1 + 3c_l/8 - Delta c_l, which vanishes at Delta = k + 3/8, and the
      x-axis order bound (1 + c_l + aA)/D drops from 2.334 at a = 17/4 to 2.12 at a = 3.8 and 2.02 at a = 3.6. The margin
      map of the tied family is not computed. The variation formula and the far limit are CONFIRMED (V121). In this tied
      family the inner scalar weight is e^((8 - 2a)t), and for a <= 4 the finite-J scalar inverse is lost (constant or
      1/(1 + |t|) inner forcings with infinite cubic trace, V121); the finite-J realization needs a > 4 and
      Delta < k + 3/8. The useful variant keeps the inner radial exponent at 17/4 and lowers only the angular and far
      exponents; the far eta values are the same there (r < 1 carries 0.07 percent of the energy), but the jet-row
      results (angular trace gain a - 1/2, V116) and the margin must be redone; this is now done at Delta = 0.3 (below). Its margin changes by
      (a - 17/4) tan(theta) V.grad(theta) - Delta q 1_{r>=1}; floating box lower bounds from the refined margin map are
      1.38, 0.73, 0.07 (a = 4), 1.13, 0.48, -0.18 (a = 3.8), 0.88, 0.22, -0.45 (a = 3.6) for Delta = 0.2, 0.3, 0.4,
      attained at r about 180 to 210 next to the vertical axis, where the angular bound is still unrefined (FLOATING).
    - Decoupled family (THEOREMS). At Delta = 0.3 (far weight r^(-37/20)), inner radial exponent unchanged and a in
      [18/5, 4]: margin at least 1.10534 (at least 1.2501 at a = 4 by an independent refinement, V191; V171, 512-bit original-data enclosure on 423719
      cells); low mapping, closed scalar normalization, Hilbert-Schmidt axis row, Garding estimate and index 0, with
      remainder strain norms < 0.239392 (a = 18/5) and < 0.230190 (a = 4) (V172); no uniform third axis derivative
      bound for a <= 4 (REFUTED, V173; the proof of V172 uses a source-scale split instead); and
      ||F(rho~)||_(Y_a) < 485.632 for every a in the interval (V174, by exact radial reweighting of the V164 envelopes),
      and ||F(rho~)||_(Y_a) > 3.270 for every a in the interval (V179, eight disjoint windows, a partial lower bound).
    - Consequence (DERIVED). With global constants the closure needs C_V K_H < 10/(51 eta) at a = 17/4 (margin
      perturbation coefficient 3a), so below 10/(51 x 6049.11) < 3.25e-5 by V164. If K_H were of the order of the
      inverse transport energy rates and C_V an embedding constant of order one, this would fail; that is a heuristic
      concern, not a proof, since no lower bounds for the actual constants are known, and (S) remains OPEN (V255). In the decoupled
      family the analogue with margin 1.10534 would be about 2.1e-4 at a = 3.6 with 485.632 in place of eta (indicative
      only: the margin perturbation bound is not proved for the new weight, and the closure needs the high norm of the
      residual, which is not computed).

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
  - The remainder inverse is sharp, with ||T_0^{-1}|| = 1/kappa_0 (kappa_0 about 16.54116 at a = 7/2, b = 6/5).
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
  Injectivity is equivalent to invertibility. (H_m) holds for mu~ and the actual background: m_R >= 5/2 (V086; first m_R >= 1.78605, V077,
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
- V213 to V215: on C^alpha_b intersected with L^2 the frozen source inverse needs no support restriction, the actual
  source flow is smoothly conjugate to its linearization, and the whole-plane extension of the actual variable
  unnormalized source operator is invertible for every alpha < 1; the full strain functional is unbounded in that
  norm (relative to the graph norm this is not decided).
- V216, V217: the smooth J = c = 0 core has the same graph closure as the smooth c = 0 core in the C^alpha_2 graph of
  S(e); smooth inputs are not dense in the whole maximal graph (REFUTED as an unqualified claim).
- V219: on C^alpha_2 the exact normalization makes the localized coupling of size comparable to delta^2 (sharp),
  against order delta^(1-alpha) without it; the frozen Neumann error is O(delta^2), and by V226 (supported-endpoint
  multiplier estimate) so is the actual-variable one.

Hoelder theory (Avenue II):
- V028: H0, S(a) to S(c). Anisotropic C^alpha_p is bounded under T_0^{-1} if and only if 1 + pA > D alpha, sharp.
  The smooth-cutoff coupling estimate S(d) gives a whole-plane inverse of T_0 plus the localized coupling on C^alpha_1
  for alpha < (1 + A)/D (about 0.5227).
- V203 to V207: S(e). U_1[h]/x is uniformly C^alpha in y on C^alpha_p (1 <= p <= 2) without derivatives of h; the
  complete normalized localized coupling has norm O(delta^(3-p-alpha)); the frozen saddle, and the actual transport
  on B_(delta/2) blended to the frozen saddle outside B_delta, plus this coupling are invertible on C^alpha_2 for every
  alpha < 1 and delta small. The 0.5227 barrier and the necessity of an x-derivative are REFUTED (V203).
- V208: the cubic coordinate J is not closable in the C^alpha_2 graph norm of these localized operators (smooth
  compact packets with J = 1, c = 0 and graph norm O(eps^(1-alpha))), so the local Hoelder inverse does not give a
  closed normalization.
- V211: Lemma N''. In the same C^alpha_2 graphs, smooth compact inputs away from the axes with J = c = 0 and bounded
  graph norm have ||N(h_n)||_{C^alpha_2} >= c n and ||L_delta^{-1} N(h_n)||_{C^alpha_2} >= c n; the quadratic term
  is discontinuous at 0 from the graph norm, so the local Hoelder inverse does not close the perturbative
  (semilinear) fixed-point map; a quasilinear scheme is not addressed.
- V210: of the 78 pure spline columns of the finite section (all low-conforming), exactly the 66 with 6 <= i <= 27
  lie in the high input space and exactly the 60 with 7 <= i <= 26 in the maximal high graph domain (the zero
  extension is exactly C^(i-1) at the left end only for i = 4..7 and exactly C^(32-i) at the right end only for
  i = 26..29; the other columns vanish near the respective endpoint).
- V030: Lemmas N and N' (section 2.3).
- V222, V224, V228: the common target Y = C^alpha_2 intersected with L^2((1 + |X|^2)^(-gamma/2)), gamma > 4k, contains
  the residual F0 and carries the cut-off origin and source inverses (after the cutoffs); the renormalized coupling
  C_ren = U[.].grad rho0 + c[.] H0 is bounded on Y, with tail O(R^(k-1)(1 + log R)) for 4k < gamma < 2 and on E_2
  (this tail rate holds for every gamma > 4k and is sharp, R^(k-1) log R from below as well, on E_2 and on every
  Y_gamma, also on the strain-zero inputs ker c, where C0 = C_ren: THEOREM, V278 with sign clarification V281,
  verifier proof, independent audit recorded as V287); the complete coupling C0 = C_ren + c[.](M0 - H0) is bounded,
  with tail ||beta_R C0|| <= C (R^(k-1) + R^(k-gamma/2) + R^(2k-1) + R^(2k-gamma/2))(1 + log R) on E_2 intersected
  with L^2(w_gamma) for every gamma > 4k (V241, V247; all exponents negative; O(R^(2k-gamma/2)(1 + log R)) for the
  earlier full operator with 4k < gamma < 2; the rate R^max(2k-1, 2k-gamma/2) log R is sharp, by the exact nonzero r^p
  log r coefficient of the moving-tail column, so the faster rate of C_ren is false for C0: THEOREM, V276, verifier
  proof, independent audit recorded as V286), the moving-tail column m0 lies in Y, and L_ren and the full chart
  operator A_0 are closed on the maximal domain D_Y, first for 4k < gamma < 2 and, by V241 (THEOREM, recorded as
  V247), on E_2 itself and for every gamma > 4k; J is not closable there. V227: the error of the specified single
  cut-off parametrix (one patch, cutoffs with the flow-box hypothesis) is bounded but not compact on that graph; this
  does not exclude cancellation in a sum of patches or another parametrix. Independent cross-audits V231, V233: no
  gap.
- V232, V234 (cross-audit V237): T, L_ren and A_0 are not onto Y, so Y is not a valid global target (two
  independent far-field mechanisms: vertical oscillation near the x-axis at large radius, V234, for every bounded
  linear coupling with vanishing tails; a strip along the vertical axis at large height, V232, giving an algebraic
  cokernel of continuum dimension). THEOREM (verifier proof V241, recorded as V247): on E_2 and on every
  Y_gamma, gamma > 4k, T, L_ren and A_0 have infinite algebraic cokernel; the range of the actual residual and the
  closedness of the range remain OPEN.
- THEOREM (verifier proof V235, independent audit recorded as V244): on the candidate
  target Z (E_2 near the origin, scaled far annular C^alpha norms with growth r^beta, L^2(w_gamma)) the residual lies
  in Z, the complete coupling is bounded with small tails and A_0 is closed for 2k - 1 < beta < k (at the endpoint
  beta = 2k - 1 the column m0 is outside Z by a logarithmic far term, so the operator does not map the entire transport
  domain into Z; within the transport domain the exact condition for the image to lie in Z is c[h] = 0, and a
  restricted closed realization is not excluded). THEOREM (V236, V242): the exterior operator on {|X| > R} is invertible for large R.
  THEOREM (verifier proofs V239, V240, recorded as V246): the error of the explicit full-column origin cut-off patch
  (a single patch, cutoffs with the flow-box hypothesis) is noncompact on Z, which does not cover sums of patches or
  every parametrix (a norm-small complete right error would give onto only); completing smooth zero-strain inputs in
  the graph norm plus |J| gives G_sm (+) R, whose function projection has a nonzero pure scalar kernel invisible to
  A_0, where G_sm is the smooth graph closure only, not the entire maximal domain.
  THEOREM (verifier proof V243, recorded as V249): T, L_ren and A_0 have infinite algebraic cokernel on Z
  (0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k), because ordinary far C^alpha
  allows transverse powers |x|^sigma along the outgoing vertical axis, which the characteristics carry to the origin
  region, where the local E_2 factor requires O(x^2); this says nothing about the range of the actual residual or
  about Z_2, and it does not rest on the cut-off proofs. THEOREM (verifier proof V245, independent audit recorded as
  V254, at this scope): on the target Z_2 with scaled
  quadratic axis control on every annulus the residual lies in Z_2, the complete coupling is bounded with small
  tails, A_0 is closed on the full maximal domain, and the actual auxiliary exterior operator is invertible for large
  R; the cubic normalization is not closable there. THEOREM (verifier proof V256 with an original-data interval
  certificate of a simple zero of a(0, y) = d_x V_1(0, y) on the vertical axis, y_* in (9.1465, 9.1468), a_t in
  (7.1952, 7.1954); independent audit recorded as V262): T is not onto Z_2 for alpha > 1/2, and A_0 and L_ren are not onto Z_2
  for alpha > 2/3, for all 2k - 1 < beta < k and gamma > 4k (turning-height obstruction); degenerate zeros are not
  covered; a stronger divided velocity bound (V257: U_1[x^2 g]/x is jointly C^alpha on bounded x-strips for g compactly supported,
  even in x, bounded and uniformly C^alpha in y; THEOREM, verifier proof, independent audit recorded as V265) extends the statement for A_0 and L_ren
  to every alpha > 1/2; alpha <= 1/2 is OPEN for A_0 and L_ren (for T alone see V266 below),
  the remedy alpha <= 1/2 is heuristic, and the other remedy, a divided horizontal seminorm near the vertical axis, is
  the joint-cofactor target Z_cof (THEOREM, V261, verifier proof, independent audit recorded as V268): h = x^2 g with g in the
  full joint C^alpha locally and sup_R R^(2-beta)(||g||_inf + R^alpha [g]_(C^alpha)) on the dyadic annuli, plus
  L^2(w_gamma). For every 0 < alpha < 1 and 2k - 1 < beta < k the complete coupling is bounded with a small tail,
  the residual lies in Z_cof, T, L_ren and A_0 are closed on their maximal domains, and the actual auxiliary exterior
  operator is invertible; J is not closable. The turning-height forcings are unbounded in this norm, so V256 and V257
  do not apply to it; its global inverse is OPEN. Transport alone is not onto Z_2 or Z_cof near the source (THEOREM, V266, verifier proof, independent audit recorded as V272): with DV(P) = diag(A_s, mu_s) at the source P, 10 < A_s < 51/5, the cusp profiles s_+^a phi(y/s_+^b), a = 1/A_s, b = mu_s/A_s, of the conjugated transport give smooth compact forcings with c = J = 0 that span an infinite-dimensional subspace of the cokernel of T on either target for alpha > 1/A_s, so for every alpha >= 1/10. This excludes a Neumann series around T; it says nothing about A_0 or L_ren, since the full source coupling changes the equation. The nonlinear derivative loss persists on Z_cof (THEOREM, V264, verifier proof, independent audit recorded as V271): there are smooth
  inputs h_n with c = J = 0, supported in a fixed compact set away from both axes and bounded in the graph norms of T,
  L_ren and A_0, with ||N(h_n)|| >= b n for N(h) = (U[h] + (c[h]/3) X).grad h; so N has no continuous extension at 0
  in these graph topologies. This does not exclude a quasilinear scheme, stronger derivative norms or a profile.
  A global inverse on Z_2, the matching across the middle annuli, and hence a global Hoelder inverse, are OPEN. None of this affects Theorem E, which is proved in Hilbert spaces.

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
  L_red : Z -> Y_lo are Fredholm of index 0 (V077; the complete statement with spaces is in the verifier's record). Injectivity,
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
  (d = m - delta - eps > 0, inverse bound (1 + Psi)/d), the Schur criterion (for F bounded and Fredholm of
  index zero on a Hilbert space, P an orthogonal finite-rank projection, Q = I - P, D = QFQ bijective on ran Q with
  ||D^{-1}|| <= 1/d, ||PFQ|| <= b, ||QFP|| <= c and ||PFP p|| >= a ||p||: s = a - b c/d > 0,
  p_0 = (1 + (b/d)^2)^{1/2}/s, inverse bound (p_0^2 + ((1 + c p_0)/d)^2)^{1/2}; without the index-zero and finite-rank
  hypotheses the operator is only bounded below and need not be onto, V250), and the commutator and principal
  Garding estimates on a regular periodic cylinder. OPEN: their quantitative inputs for the actual operator (singular
  angular conjugation, cutoffs, jet rows, compact-defect approximation, complement bijectivity).
- V083: the homogeneous velocity formulas and the Mellin bound max(|sigma + 1|, 1)/(Lambda - |sigma + 2|) on a regular
  cylinder (sigma = 13/4 near 0, -3/8 at infinity for the radial isometry of w_a), CONFIRMED with that scope.
- V084: the bordering profile zeta lies in Y intersect H_base^sigma: g_far, y_KP and zeta divided by the origin and far
  factor are in cylinder H^sigma for 0 < delta < 2, gamma > 2k - 1, 0 <= sigma < 13/2 (including delta = 9/5,
  gamma = -1/2, sigma = 25/4), so c[.] zeta maps Z boundedly into the high base target, CONFIRMED (finiteness only).
- V085: a one-order gain of the full coupling C is REFUTED. Parity-symmetric packets N^{-s} phi cos(N x) on a regular
  patch with rho_y > 0 are bounded in H^s, have zero cubic and tail coordinates and lie in the graph domains, while
  the localized H^{s+1} norms of C h_N grow at least linearly in N (order-zero multiplier
  p(X, xi) = (rho_x xi_1 xi_2 - rho_y xi_1^2)/|xi|^2). The high estimate must keep the full order-zero principal
  coupling in the energy (the joint symbol); smoothing is available only for commutators and separated-support pieces.
- V086: both global energy margins are at least 5/2 for the actual normalized background (independent 512-bit
  refinement with 194816 roots and 213985 terminal leaves, separate audit with a 640-bit replay of 136 boxes; saved
  lower endpoints about 2.500165 for m_a and 2.500014 for m_R), CONFIRMED. The axis bound d >= 5.5752 is that of V077.
- V087: L_red restricted to ker J has index -1 (the unchanged onto theorem on ker J is REFUTED); the final physical
  normalization by scaling (section 2), CONFIRMED.
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
- V039: Prop IV.O of the accompanying S2_BASIS_CERTIFICATION.md. The S0 realization (factor domain, density target), on
  its maximal domain D_max = {h in the factor space : L h in the density target}, maps D_max
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
   computation; both margins are at least 5/2 by V086, m_a >= 2.9270 by V197 and m_a >= 3 by V259). The numerics team's sharper single-team values (m_a >= 0.965918, kappa_* >= 3.037693, d in
   [5.575203, 21.301451], the endpoint constants 0.100883, 0.202073, 89.3342, 73.3113) keep their single-team status and
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
   of the normalization profile is not enough; for L_red the normalization part holds, zeta in Y intersect H_base^sigma
   (V084), and a one-order gain of the full C is false (V085), so the high energy must keep the full order-zero
   principal coupling), the
   regularization step from the low domain, and tame (not only C^1) dependence on g for uniformity; the uniform estimate
   then follows from the low bound by absorption but surjectivity needs the graph-domain construction. Lemma H-spec
   (S2_L2_THEORY.md 6.6) is CONFIRMED as an abstract theorem and REFUTED for a direct identity shift on the free-J
   spaces (V106: the cubic direction is in the intended high domain and not in the target, and a subtraction of the
   cubic coordinate has no O(1/lambda) inverse). Its restated form (DERIVED, submitted) reduces the regularization
   and the surjectivity to hypotheses that are OPEN for the actual spaces, by continuation in a spectral parameter
   applied to the remainder block S_1 = T_R + C_R: with (H1) C_R bounded from X_H to Y_H, (H2)
   ||(T_R - lambda)^{-1}||_{Y_H -> X_H} <= M/(lambda - omega) for lambda > omega (transport only; characteristic formula
   with the order nondecreasing along the flow), and (H3) the high a priori estimate with a compact error for
   S_1 - lambda on 0 <= lambda <= omega + 1 + 2M||C_R||, S_1 is Fredholm of index 0 on D_H = {h in X_H : T_R h in Y_H}.
   Corollary H-spec adds the jet row through the triangular form of Theorem C' ((J1) the off-diagonal block bounded
   from B_H := {beta in B : A beta in Gamma_H} into Y_H, (J2) the jet coupling compact into Gamma_H, (J3) zeta in the
   high target): L_red is Fredholm of index 0 on the high domain; with injectivity on Z it is an isomorphism and its
   inverse is the low inverse; the bound is C_1' + C_2' K_L iota_Y when the high estimate has its compact errors
   through Z. The jet row cannot be continued together with the remainder (the cubic constant is not in Gamma, and on
   {J = 0} the shifted scalar row changes index at lambda = D/4). The same holds for each A_g on its own domain.
   (J1) and (J2) reduce to N + 1 radial conormal derivatives of h in a sector around the y-axis, by the dilation
   commutation (y d_y)^j T_h = T_{(X.grad)^j h} and the trace majorants of V105, with only the base norm outside the
   sector (S2_L2_THEORY.md 6.6 remark (6), DERIVED). This is now proved, and (J1) to (J3) hold on one explicit
   candidate (THEOREM, V112 to V118): Gamma_H = a H^(25/4) with a = e^(9t/5) at the origin end and e^(-7t/2) at infinity,
   B_H = {J chi + a v : v in H^(29/4)} (V117), and R_H = R_base + Q (factored axis-zero order 25/4 plus cone-bulk order
   41/20 in |cos theta| >= epsilon; V118). The fractional trace gain (V116) and the critical angular Hardy inequality
   (V114) give J2; the integer target H^6 is not compatible (V115). For this sharp cone sum (H1) is expected to fail at
   the cone boundary (REFUTED as a choice, V119); a smooth variable order avoids that. On the smooth variable-order
   space X_s (order between 41/20 and 25/4, uniformly smooth, reflection invariant, 25/4 on a fixed vertical sector),
   (H1) and J1 to J3 are THEOREMS (V126), and (H2) is a THEOREM in a dyadic norm under W.grad s >= 0 (V129; five
   coefficient derivatives do not suffice, V127). An order function with W.grad s >= 0, equal to 41/20 near the closed
   x-axis segments and the sources and to 25/4 elsewhere outside a thin shell, exists for the actual field (THEOREM:
   V132 for the exit-time construction of a repeller block, Lemma H2-ord; V130 for an independent blow-up construction
   with a smooth escape function). (H3) was the remaining hypothesis and is now a THEOREM (V151, below); a pure energy
   estimate is impossible at the vertical-axis end (V128).
   Verified toward it: the exact origin normal family is bijective for every real frequency and Re lambda > -0.9726
   (V131), uniformly in the frequency for the exact normal operator (V133); the selected principal end inverses at the
   vertical, horizontal and far ends are stable under the actual small coefficient errors (V135, V137); the joint
   source margin at order 41/20 is 4.52536 (V134, which REFUTED the earlier value about 14.8). Proposition H3-red
   (CONFIRMED, V141) reduces (H3) on X_s to the high-frequency estimate (Hs_eps)
   ||h||_s <= C (||(S - lambda) h||_s + ||h||_(s-eps)), by the exact energy identity of the actual field in the norm
   N_0(h) = ||h/(b cos^4 theta)||_(L^2(dt dtheta)), whose energy tends to 65.45 cos^2 theta + 8.84 sin^2 theta at the
   origin and 3.79 at infinity. A small actual first-order coefficient error is unbounded on the normal graph (V138),
   so the end inverses are proved by energy; the actual inner end estimate holds with a finite annular error (V139),
   and the coupling tails vanish in the X_s operator norm, which reduces the full equation to a compact core with a
   high-norm error (V140). Proposition H3-red is CONFIRMED conditional on (Hs_eps) (V141). Lemma Hs-sym (THEOREM, V144,
   after one decimal correction): the global symbol inequality
   m + N W.grad Lambda + L_0 (W.nu)^2 >= mu holds for every mu < 0.9726 on the compactified cosphere bundle, by
   compactness from the confirmed margins and the escape function of V130; Proposition Hs derives (Hs_eps) from it and
   the calculus inputs (Q0), (Q1), (Q2), (Q5') (finite-regularity quantization; positivity is pointwise in matrix
   form). All four inputs are THEOREMS for the actual coefficients: (Q0) the order reduction with a lower-norm error and
   the sector support correction (V146); (Q2) the coupling modulo compact and arbitrarily small errors (V147, with V140,
   V142, V143); (Q5') the penalty through the equation with an arbitrarily small high error and C_R bounded on
   X_(s-eps) (V148); (Q1) the transport commutator for W^(7,inf) coefficients with the exact logarithmic coefficient
   (V149, a kernel Taylor expansion to degree 6), on the maximal domain (V150). The positivity and logarithmic steps
   hold at the actual finite regularity with an H^(-1/32) remainder (V145). The assembly of (Hs_eps) from these inputs
   (Steps 1 to 4 of Proposition Hs) is CONFIRMED, so (H3) holds on X_s (THEOREM, V151), and the remainder block
   S - lambda (lambda >= 0), L_ren and L_red are Fredholm of index 0 on their high graph domains, B_H (+) D_s ->
   Gamma_H (+) X_s with B_H = {J chi_0 + a v : v in H^(29/4)} (THEOREM, V152). A high null vector is a low null vector,
   so low injectivity would give the high inverse; low injectivity is OPEN, and no constant (K_H in particular) is
   computed. Uniformity over a ball of backgrounds (needed for the closure in item 6 of 2.1): the fixed order is robustly
   monotone, (W + B).grad s >= 0 for ||B||_inf <= kappa_s/2, with an explicit matrix-margin loss (THEOREM, V154); the
   logarithmic positivity holds at C^(1,alpha) (THEOREM, V155); the full variable-order Kato-Ponce commutator bound is
   false (REFUTED, V153). The tame step is proved in square-summed form: the perturbation velocity B[g] = c[g] E_0 +
   Z[g] is bounded in H^(s(.)) and C^(1,alpha) by C ||g||_G (THEOREM, V156), the dyadic coefficient commutators obey
   the tame bound (THEOREM, V157) and the dyadic energy reproduces the background estimate (THEOREM, V158). For the
   frozen-coupling family S_g = (V + U[g] + c[g] X/3).grad - 1 + C_R, ||g||_G <= r_*: the compact-error estimate holds
   uniformly on the exact maximal domains D_g (THEOREM, V159); T_g generates a C_0 semigroup with generator domain D_g,
   S_g - lambda is Fredholm of index 0, and if S_0 is injective then ||h|| + ||T_g h|| <= C ||S_g h|| uniformly on a
   smaller ball (THEOREM, V160). A second proof with a single-operator tame commutator is CONFIRMED (V161, V163) after a
   sign correction in the auxiliary N_0 energy (V162). The bordered block, the low estimate and the moving background
   are THEOREMS as well: the perturbed scalar axis row is an isomorphism on a small ball, with the axis trace
   tau_g = c[g] chi_0 + e_g and e_g in H^(31/4) (V166; the axis multiplier sign is +2/eta^2, V167); the full fixed-coupling
   block is Fredholm of index 0 with a fixed compact error map and a uniform high inverse under base injectivity (V168)
   and a uniform low inverse (V169); and the exact moving-tail family has both uniform inverses under base low
   injectivity (V170). OPEN: base low injectivity and all constants.
   For the frozen operators the low-to-high step is proved in both corner charts (THEOREM, V103: x-axis cylinder chart,
   ||u||_{H^s} <= ||F||_{H^s}/kappa_s, kappa_s = 1 + A(3 + delta) + (A + D)/2 - s(A + D), about 0.97261 at delta = 9/5,
   s = 41/20; V104: vertical remainder cofactor, local H^s for every finite s >= 2, two-normal-derivative bound
   1/8.83565); transitions, the free jet and the variable nonlocal operator remain. Verified: the
   principal joint high-energy symbol, with margins 142.5074 (y-axis, 25/4), 0.97261 (x-axis cylinder, 41/20; threshold
   2.08092342) and 3.78768 (infinity, gamma = -1/2) at delta = 9/5 (V088); the rank-one non-implication (V089); the
   geometric clause of uniformity for sup ||DW|| <= 1e-5 (THEOREM, V090: same three zeros, types and flow, speed/r >=
   0.00023 outside the source rectangles, source shift <= 1/1801), so C_V r <= 1e-5 suffices for it; and the exact
   torus family of V091, which shows that C^1 convergence with uniform low inverses does not give uniform high inverses,
   so the high estimate must be tame in the high norm of the perturbation.
4. The bilinear bound C_B and the Lipschitz bound C_V in that X_hi. They are THEOREMS with finite, uncomputed
   constants for the cone-local space of V065 and V073, with order s > 2 near the closed x-axis segment and the origin
   (41/20 with delta = 9/5 is inside their ranges and below the cylinder corner threshold 2.0809 of V079). Explicit
   values are not available.
5. A residual that is small in the closure norm. Membership, axis jet included, is THEOREM in Y_lo (V042) and in
   the fractional high target of order 25/4 (V076). The size is not small: 6049.11 < eta < 8601.42 (THEOREM, V164) and about
   7.2e3 (NUMERICAL), in a thin layer at the vertical axis that the weight |cos theta|^(-17/2) amplifies (3.5(d)). So this
   item needs a better trial near the vertical axis for 4 <= log r <= 20, or a weight with smaller angular exponent and
   far exponent (about 13 at a = 3.6 with the far exponent lowered by 0.6, NUMERICAL). In that decoupled family the
   margin is re-certified (>= 1.10534, V171), the low theory holds (V172) and the low norm is certified below 485.632
   (V174). The closure needs the high norm of the residual. In an explicitly fixed equivalent high norm it is enclosed
   as 3.866e10 < eta_* < 6.321e129 (THEOREMS, V192, V182). The upper end comes from global coefficient and derivative
   majorants and is not an estimate of the size. The lower end is the fractional difference bound
   |g_axis^(5)(t) - g_axis^(5)(u)|^2 <= [8/(3 sqrt(2 pi))] |t - u|^(3/2) eta_*^2 at t = 8, u = 1001/125 for the
   weighted axis trace (V192, strengthening the point bound 1906360017 of V183 and 36400585492 of V186); it uses only the axis summand of the norm, so it holds for every angular cutoff and
   Littlewood-Paley partition with this weight and order, and it is driven by the knot-scale structure of the spline
   residual (7 item 8). In this norm (S) needs K_L C K_H < 2.6e-11; this refutes nothing, since the constants are not
   computed and change with the equivalent norm. A realistic value is OPEN.
6. The moving-tail formulation and its conditional iteration are THEOREMS (V062). What remains are its hypotheses:
   uniform right inverses into the high space for the family A_v (item 3, with the ell-dependence of the compact part of
   the Garding estimate bounded), the low estimate K_L (item 2) and the smallness conditions with the certified eta.
   The uniform inverses are now THEOREMS under base low injectivity (V170, item 3), and the assembly is Theorem E
   (CONDITIONAL THEOREM, V178; full text in S2_L2_THEORY.md 6.8): with Lemma Emb (THEOREM, V177) (Gamma_H in G, B_H in B, X_s in R
   and in every perturbed maximal low domain, H_full in the high space of the bilinear bound), if (I) the base low
   operator is injective and (S) K_H eta_0 <= r <= r_*, K_L C K_H eta_0 < 1 with eta_0 = ||f_0||_(Y_full), then there are
   ell and h in H_full with ||h|| <= K_H eta_0 and F_ell(rho_ell + h) = 0, the profile is C^(1,alpha) off the origin for
   every alpha < 1/20 with cubic jet (1 + J) x^2 y and far field r^(1/ell) Theta(theta) + O(r^(-1/2)), h is unique in
   the fixed correction ball if K_L C r < 1 (before rescaling), and for |J| < 1 (sufficient: ||J||_(H*) K_H eta_0 < 1)
   the rescaled profile has leading term exactly x^2 y and tail amplitude lambda^(1 - 1/ell). The same holds with the
   decoupled low spaces for each fixed a in [18/5, 4] (V175, V176). (I) is OPEN and (S) cannot be checked with
   qualitative constants and with eta_0 known only within 3.866e10 < eta_* < 6.321e129 in a fixed equivalent norm (V192,
   V182); two constant-free necessary consequences of (I) and (S) are THEOREMS (V185, V194; 7 item 9); this is not an unconditional existence proof for the actual trial.

## 6. Constants that need certification

| Quantity | Needed for | Status |
|---|---|---|
| c[rho~] = 3/k - 1 (exact normalization) | every rigorous statement | CERTIFIED (V005; numerics team C1) |
| source x_P, mu_P, g_P | source inverse | THEOREM (V017) |
| source neighbourhood margin kappa - E | source inverse | THEOREM (V024) |
| m_* for mu~ (H_m) | Theorem R for L_fix | THEOREM (V086): m_R >= 5/2 (independent refinement; first m_R >= 1.78605, V077); the numerics team's certificate gives m_* >= 1.029821 (aggregation verified, V072), refined to m_* >= 2.471224 (one team, 05:58Z); grid 2.590 |
| m_a for w_a (H_m') | Theorem C', scheme | THEOREM (V259): m_a >= 3 on the whole plane, coefficient-margin scope (earlier m_a >= 2.9270, V197, and m_a >= 5/2, V086, still valid but superseded; first m_a >= 0.53072, V077; the numerics team's finer outer cover gives 3.000000); single-team certificate m_a >= 0.965918 (aggregation verified, V072), refined to m_a >= 2.500023 (one team, 05:58Z); grid 3.09 |
| positive axis rate q(0, y) > 0, y != 0, with endpoint bounds (A) | N2, V041 axis row, V046, Theorem C' | THEOREM (V077): d >= 5.5752 on the whole axis, with the qualitative endpoint estimates of V055; single-team quantitative values d in [5.575203, 21.301451], sup abs(d') <= 5.6012, endpoint constants 0.100883, 0.202073 (t <= 0) and 89.3342, 73.3113 (t >= 0) |
| angular coefficient constants M_Q, M_P and transport margin kappa_* for w_a | V046 (Lemmas C'1 to C'3) | finite for the modal field (V047); box bounds M_Q <= 337.66, M_P <= 1075.52, kappa_* >= 3.037693 (same production run, aggregation verified, V072) |
| constants of (E0), (E-J), (E-G) and a finite-rank split of K_eps | K_L | finite (V049 to V053); not computed |
| hypothesis (Z): V has no zero on the closed quadrant other than 0 and P, and DV(P) is a hyperbolic repeller | Lemma H1 (THEOREM under (Z), V063), Theorem H (S2_L2_THEORY.md 6.3, 6.6) | THEOREM (V080): the zeros are 0 and (+-p, 0); abs(V)/r >= 3/12500 outside the source rectangle Q (closed first quadrant, away from 0); abs(V(X)) >= 0.1801 abs(X - P) on Q (V070) |
| d = 3 c_l + k c[KP] != 0 | rank-one bordering | THEOREM (V034): d >= 3 c_l > 0 for every admissible cutoff; for the numerics team's shifted column, d lies in [16.73870985167530795255805332462072, 16.73870985167530795255805332462074] (THEOREM, V043) |
| s_3 = int sin(3 theta) Theta_0 | the sign of c[KP] | THEOREM (V034): 37.63077494715565 < s_3/pi < 37.63077494715567 |
| C_a, trace constants | (E) | THEOREM at strip scope (V026); (E) itself THEOREM with qualitative constants (V049 to V053) |
| Prop C2 constant C_cap | c bounded on Z_cap | THEOREM (V034): C_cap < 0.312093 (a = 7/2, b = 6/5), C_cap < 0.359253 (a = 17/4, b = 0) |
| K_A <= 0.032163 | frozen c adjoint | THEOREM (V016) |
| finite-section sigma_min and off-basis residual | Avenue IV | S0: sigma_min >= 4.3337e-07 with TAU (V066, conditional matrix certificate), >= 2.0685e-02 without TAU (V200, conditional matrix certificate); a finite statement (V039); off-basis residual not computed |
| r_V (half-margin radius) | closure inequalities 3.4 | the perturbation coefficient is THEOREM (V075): for the fixed background the margin drops by at most abs(c[h])/3 + (51/4) norm(D W[h]) (plus norm(grad h) when the coupling background moves); the constants C_c, C_W (and C_g) of the high space are not computed |
| eta | closure inequalities 3.4 | low norm: 6049.11 < eta < 8601.42 (THEOREM, V164; earlier lower bound 933.47, V110); between 3.270 and 485.632 in the decoupled family, a in [18/5, 4] (THEOREM, V174, V179); NUMERICAL value about 7.2e3 at a = 17/4 (3.5(d)); the high norm of Theorem E, in an explicitly fixed equivalent norm: 38666592266 < eta_* < 6.321e129 (THEOREMS, V192 difference bound from the fifth axis derivatives at t = 8 and 1001/125, earlier 1906360017 from one point, V183, V182 a deliberately loose majorant; ||F/(r^3 p a_*)||_(H^(25/4)) < 1.195e93); a realistic value is OPEN |
| K_H, K_L, C_B, C_V | closure inequalities 3.4 | not available (C_B, C_V finite by V057, V060, V065, V073) |

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
4. The certified margins are m_a >= 3 for w_a (THEOREM, V259; earlier 2.9270, V197, and 5/2, V086) and m_R >= 5/2 for mu~ (THEOREM, V086; first 1.78605, V077 (m_a: 0.53072),
   V077; values 2.500023 and 2.471224 from a single computation; grid values 3.09 and 2.59), against a perturbation cost that 3.5(a) bounds linearly in
   ||D W[h]||_infinity.
5. By 3.5(b), for a fixed background, uniformity over the correction ball reduces to the single h = 0 complement estimate (in the parametric form the ell-dependence of K must also be bounded; done for the exact moving-tail family, V170), because the compact
   part does not depend on h.
6. The assembly is explicit. Theorem E (CONDITIONAL THEOREM, V178) reduces existence exactly to (I) injectivity of
   the base low operator and (S) one smallness condition, so a certified injectivity with a quantitative inverse,
   explicit radii and constants, and a high residual norm are precisely what remains.
7. The route can be tested before any constant is certified (CONDITIONAL THEOREM, a necessary test under (I) and (S), V184). For j >= 1 the residual of the j-th iterate is
   (A_(h_j) - A_(h_(j-1))) h_j, by the exact identity F_ell(h)(rho_ell(h) + h) = f_0 + A_h h, so under (S)
   ||F_(ell(h_j))(rho_(ell(h_j)) + h_j)||_Y <= q_0^j ||f_0||_Y with q_0 = K_L C K_H eta_0. Every admissible choice of
   constants therefore has q_0 >= nu_1, the ratio of the low residual norms after and before the first step
   h_1 = -A_0^(-1) f_0. If one exact step does not reduce the low residual norm, (S) fails for every admissible r_*, K_H,
   K_L and C (the step presupposes (I), so this tests (S) under (I)). The test needs no inverse constant. The positivity of the low residual norm that the ratio needs is
   certified (V164, V179); a step computed from a finite section is NUMERICAL and cannot refute (S) without a certified
   error bound. It has not been computed in this run.
8. What the trial must improve (NUMERICAL heuristic, not a proof). For t between 2 and 10, 88 to 99.7 percent of the
   strong angular energy of the residual lies within 0.01 rad of the vertical axis (13 to 40 percent for the profile),
   exactly where the high norm has order 25/4, and the order-25/4 proxy of the residual exceeds that of the profile by
   factors of about 165 at t = 2 and 14 at t = 4. K_H eta_0 <= r_* is therefore unlikely for this trial. At infinity
   the residual divided by the high weight decays only like r^(2k - 1/2), about r^(-0.14); the far operator
   ell X.grad - 1 multiplies r^m Theta_m(theta) by ell m - 1 (1 - ell for m = 2k - 1, 2 - 2 ell for m = 3k - 2), so the
   far corrections are algebraic and the first one improves this to r^(3k - 3/2), about r^(-0.96). They are finite
   trigonometric sums with the parity of the problem that vanish to second order at the vertical axis, since the
   velocity is tangent to it (DERIVED, not verified). A trial refined in the axis layer and carrying these
   corrections, with its residual measured in the high norm, is the next step before (S) can be tested. The certified
   high lower bound adds a second requirement: at t = 8, just inside the outer join, the weighted axis trace has the
   value 0.158 and the fifth derivative 4.48e8 (V183), and central differences with steps from 1/256 down to 2^-20 give
   1.5e8 to 4.48e8 (NUMERICAL), so the fifth derivative varies on the knot scale (spacing 0.008 there). In the
   order-25/4 norm the residual in that region appears (a numerical diagnostic, not a decomposition theorem) to be
   dominated by the spline approximation error of the C^6 background, whose residual can jump in the sixth derivative
   at the joins; a nonzero jump is certified at the knot t = 4958764014967233/2^51 (V069), not at every join. A trial for
   the high closure probably needs joins of higher continuity, or an analytic representation, where the high norm
   weights most; an improved trial is not by itself an existence result (V255).
9. Two sharper tests without constants (CONDITIONAL THEOREMS, V185, V194) and a heuristic violation (DERIVED heuristic with
   NUMERICAL input, not a bound). Since n is increasing with n' >= 3 and every admissible ell exceeds 4, (I) and (S)
   imply eta_0 |c[d]| <= N4 ||A_0 d||_(Y_H) for every nonzero high-domain d, N4 = -n(4) in (0, 9.06) (V185). The parts
   M_0 and L_fix d of the rank-one split are not separately in the strong zero-jet Sobolev targets of Theorem E when
   c[d] != 0 (cubic coefficients 1 and -c[d], V190; in the Hoelder targets Y, Z, Z_2 of S2_CALPHA_THEORY.md 3.4 both
   columns are target-valued, V255), so the residual is subtracted: with alpha_0 = 1/(ell_0 n'_0), R_d = A_0 d - alpha_0 c[d] f_0 = L_ren d + alpha_0 c[d]
   Q_ren with Q_ren = ell_0 n'_0 m_0 - f_0 in Y_H, and (I) and (S) imply ||R_d|| >= (1/N4 - alpha_0) eta_0 |c[d]|
   > 1956082280 |c[d]| whenever c[d] != 0 (V194). One certified upper bound below this threshold, or ||R_d|| <= theta eta_0 |c[d]| with
   theta <= 0.0507 (V199, from the sharper bound N4 <= 9.0450253607...; 9.06 alone gives 50/453 - k/3 = 0.050588...),
   for a single direction with c[d] != 0 would refute the conjunction of (I) and (S), hence (S) under (I); none is certified. The scaling tangent rho_0 - X.grad rho_0 is not a
   usable test direction: even after a smooth cutoff it is outside the chosen high correction space, because its axis
   cofactor has a sixth-derivative jump at an interior knot (V198). An exact admissible direction is the Gaussian
   density d = -Delta v of report 6.5 item 10, with c[d] = 1, J[d] = 0, d in D_H(A_0), A_0 d = L_ren d + m_0 and
   R_d = L_ren d + m_0 - f_0/(ell_0 n'_0) (THEOREM, V273, verifier proof, independent audit recorded as V283); no
   upper bound of these norms is certified. Floating fifth
   differences of the weighted axis trace at every fourth span midpoint put its knot-scale structure in two zones:
   t in [1.92, 2.62], where the knot gaps go down to 0.0019 and |g_axis^(5)| reaches 6.06e9, and t in [7.9, 8.135]
   next to the outer junction, up to 1.93e9; elsewhere it is at most 2.1e6 (NUMERICAL). The knot-scale part is a
   component that alternates in sign from span to span (seventh t-derivatives of the modes, constant on each span):
   relative to the profile its amplitude is at the rounding level 1e-16 for t in [-4.5, 1] and [3.5, 7], 3e-12
   (median) to 4.7e-10 for t in [2, 2.4], and it grows towards t_+, not uniformly (median factor 2.5 per three spans),
   to 4.9e-13 of the axis cofactor on the last span (NUMERICAL, interval evaluation span by span; reproduced from exact
   rational coefficients, V209). The certified lower bounds of eta_* (all at t = 8 and 8.008) sit where it is large;
   that they are produced by it is a heuristic reading (V209 confirms the numbers, not the reading, and the diagnostic
   says nothing about an exact profile near the trial). A coefficient filter by index differences is not a valid cure (it raised |g_axis^(5)|
   by five to eight orders of magnitude), since the coefficients of a smooth function are not smooth in the index on
   these knots. At the knot scale f_0 is
   (ell_0 + u) d_t rho_knot, u the radial transport coefficient of U[rho_0], while M_0 is about d_t rho_knot / n'_0 and
   L_fix d is negligible for a smooth inner d; so A_0 d is about c[d] f_0 / (n'_0 (ell_0 + u)) at that scale, and if
   the knot scale dominates the high norm, eta_0 |c[d]| / ||A_0 d|| is about n'_0 (ell_0 + u) >= 16.7 against
   N4 < 9.06 (the axis value ell_0 + u is 14.2 to 18.1 and 5.69 to 5.71 in the two zones). On the axis the first step is
   checked in floating point: g_axis^(5) = (ell_0 + u) q^(5), q the weighted axis trace of X.grad rho_0, up to a
   relative l2 deviation of 1.6 and 0.8 percent over the sampled span midpoints of the two zones, and the l2 ratio
   ||g_axis^(5)|| / ||q^(5)|| over the samples is 14.4, so the proxy of the ratio is about 14.4 n'_0 >= 43 (NUMERICAL;
   the angular structure of the near-axis layer is not tested). A failed test would rule out (S) under (I), not existence, and it
   does not determine the scalar component of the actual Newton step (V195: an exact two-dimensional example with a
   failed test and a Newton step of zero scalar component). A rigorous version needs an upper bound of the high norm of R_d without its knot-scale part, beyond the
   present tools. The requirement on the next trial is that of item 8.

Avenue II is farther. No Hoelder analogue of the sharp Garding inequality is available here. The generic conjugacy
transfer was REFUTED (V028), but the localized actual inverse near the origin on C^alpha_2 is proved (V203 to V207);
what is OPEN is the global Hoelder inverse (the matching across the middle annuli; on Z_2 see section 4, V245, V254,
V256). Lemmas N, N' and N'' (V030, V211) show that the explicit semilinear fixed-point map does not close in C^alpha
alone; quasilinear schemes are not addressed.

Avenue IV alone is farther. A finite section is not an inverse bound without a complement inverse (V014). The first
exact section (S0: 4 angular modes, 169 columns) is certified as a finite statement (V066, a conditional matrix
certificate: conditional on the exported entries enclosing the exact pairings), but in the S0 realization no
continuum bound is possible (V039; this concerns the S0 norms, not the L_fix and S_1 sections).

## 8. Checklist against the strict standards (task item 11)

| Standard | Status in this run |
|---|---|
| Inverse statements give domain and range | Theorem O (Z_0 -> Y), Theorem R (maximal domain D_w -> L^2(w)), source inverses (maximal H^s realizations), V041 axis row (B -> Gamma, conditional on d > 0), V046 pure transport (Z -> Y_lo, conditional on (A), the angular coefficient bounds and kappa_* > 0), Theorem C' (Z -> Y_lo, THEOREM as a conditional statement, V047, and THEOREM for the actual background, V049 to V053 and V077) |
| Membership of perturbation and image | checked: x^2 y in Z_0 (J = 1); r^k Theta not in Z; r^{2k-1} Eps in the far target; the coupling image of Z in Y_lo (V049 to V053); the residual and the parameter-family residual in Y_lo (V042, membership; the norm is enclosed in the low norms by V164, V174, V179 and in a fixed high norm by V182, V192, 3.5(d)) |
| Normalization meaningful and closed | J is continuous on Z_0 (V022). c is bounded on Z_cap (THEOREM, Prop C2, V034) and on Z (Lemma C'4, V047). c is not closable on the radial graph (V032), and J is not closed in the weak norms (V012), so neither of these weaker spaces is used for the normalization |
| Log variation of exponent perturbations | KP = chi_inf r^k log r Theta_0 carried explicitly; parametric family rho_bar_ell (2.2); log^2 second variation noted (V025) |
| Full infinite-dimensional operator, not its matrix | finite sections are used only with a complement estimate (V014); the complement is OPEN |
| No unproved finite rank, compactness or small residual used as invertibility | complied with; the Fredholm statements are labelled as such, the qualitative compact operators are never used as bounds, and injectivity is OPEN |
| Absence of proof is not nonexistence | complied with (section 1) |
| Counterexamples where a bound fails | given: V006, V007, V009, V010, V012, V019, V025, V028, V030, V032, V039, V044; Prop F4 (THEOREM for the frozen corner operator, V067: the corner singularity limiting the high order); V067 (parity-only threshold); V069 (knot jump limiting the high order below 13/2); V074 (no same-order forward isomorphism); V079 (frozen low-domain corner solution excluding delta = 3/2, s = 21/10 in the cylinder norm); code defects V020, V027, V033, V037, V054, V058, V068 (merge) |
| Bounds valid but too large | the V026 constant C_a (about 593 at a = 17/4) forces strip width R < 0.02/sup abs(rho_2). Whether this loss is intrinsic is OPEN |
