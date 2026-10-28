# S2_CLOSURE.md: status of the nonlinear existence theorem

First version 2026-10-28T02:47Z (theory author), updated 02:55Z after V034 to V036 and 03:06Z after V037 and V038. Labels follow the accompanying CONVENTIONS (item S8):
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
profile.

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
  remainder and its parameter derivatives lie in the far radial target whenever max(q, k) < 5/16 (k = 0.17936). This
  does not settle membership for the angular factor |cos theta|^{-2a} (3.5(d)).
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
  system of Prop B (V034). Membership of the remaining axis jets in the chosen target is OPEN.

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
- X_lo: the jet-plus-remainder domain Z of the accompanying S2_L2_THEORY.md section 5, with the weight
  w_a = |cos theta|^{-2a} e^{mu_a(log r)}, a = 17/4, the jet coordinate J, the y-axis jet g_t and the remainder h_R.
  In the parametric formulation the KP coordinate is replaced by the unknown ell.
- Y_lo: the matching target, x^2 f_2(y) chi_ax + F_R with F_R in L^2(w_a).
- X_hi: the same structure with m conormal derivatives (x d_x, y d_y), which commute with T_0, and m ordinary
  derivatives away from the axes. The frozen windows are s < 2373/680 at the source (V011) and arbitrary conormal
  order at 0 (Theorem O(a), V022). m must be large enough that grad h is bounded with the decay needed in 3.5(c).
- Y_sigma: a forcing space of order sigma above Y_lo. A loss of order is allowed here because the forcing is fixed.

3.2 Iteration. h_0 = 0 and A_{h_j} h_{j+1} = -F_N(rho_bar), so that
     A_{h_j}(h_{j+1} - h_j) = -W[h_j - h_{j-1}].grad h_j.

3.3 Constants (each must be a proved bound; none is available yet).
- eta := ||F_N(rho_bar)||_{Y_sigma}, the residual of the background in the forcing norm.
- K_H := sup over ||h||_{X_hi} <= r of ||A_h^{-1}||_{Y_sigma -> X_hi}.
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
    |c[h]|/3 + (1/2)(sup|mu_a'| + 4a) ||D W[h]||_infinity. This defines an admissible r_V explicitly once the
    unperturbed margin is certified (DERIVED).
(b) Uniformity of the inverse over the ball. In the Garding estimate the compact remainder K comes only from the
    coupling with coefficient grad rho_bar, which by 2.1 does not depend on h. The transport part enters through the
    margin, which is controlled by (a). So
       (m_* - eps - |c[h]|/3 - C ||D W[h]||_infinity) ||g|| <= ||A_h g|| + ||K g||,
    with K independent of h (DERIVED, given (E) of S2_L2_THEORY.md section 5). This holds for the fixed background. In
    the parametric form the coupling gradient grad rho_bar_ell varies with ell, so K depends on ell; uniform
    compactness or a quantitative perturbation bound in ell must be proved (V038). A quantitative K_L then needs two
    certified steps at h = 0 (DERIVED sketch):
    - a decomposition K = K_fin + K_small, with K_fin of finite rank on smooth functions phi_i and ||K_small|| below
      half the margin;
    - smooth approximate solutions psi_i of the adjoint problems A_0^* psi_i = phi_i with certified defects.
    Then <g, phi_i> = <A_h g, psi_i> + (small) ||g||. The h-dependence enters only through ||D W[h]||_infinity times the
    weighted H^1 norms of the psi_i, so the bound is uniform on the correction ball. This is the complement estimate
    of Avenue IV in a form that is checkable on a finite basis.
(c) The bilinear bound C_B and the axis jets. U[d] does not vanish on the y-axis (U_2 is even in x), and
    d_y h = x^2 g_h'(y) + O(x^4) there. So W[d].grad h has a nonzero x^2 jet along the y-axis and is not in L^2(w_a)
    by itself (|x|^{4 - 2a} is not integrable for a > 5/2). Its x^2 coefficient on the axis is
       U_2[d](0, y) g_h'(y) + 2 d_x U_1[d](0, y) g_h(y) + (c[d]/3)(2 g_h + y g_h'),
    which belongs to the jet row of Y_lo. The rest is O(x^4) by parity, and |x|^{8 - 2a} is integrable for a < 9/2.
    So for a > 5/2 a finite C_B needs the jet decomposition of the product, and the O(x^4) remainder is admissible
    for a < 9/2 (DERIVED). The trace
    bounds of V026 (U_2 on the axis in H^2_y, d_x U_1 in H^1_y, on strips) are the local ingredients.
(d) Residual membership.
    - Radial exponent at infinity: the trial residual is r^{2k-1} Eps(theta) + o(r^{2k-1}), and the far radial weight
      is r^{-5/4}. Since -5/4 < -4k = -0.717, the radial integral converges, for L^2(e^{mu~}) and for w_a alike
      (DERIVED from V025, N4).
    - Angular factor: w_a carries |cos theta|^{-2a} at every radius. So membership in Y_lo needs the residual's x^2 jet
      along the whole y-axis to lie in the jet target, and the rest to lie in L^2(w_a). This holds near 0 and along the
      axis only if the residual has this structure; it is OPEN, and checkable from the trial's exact modal form.

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
  Injectivity is equivalent to invertibility. This is CONDITIONAL on (H_m), which is not yet certified.
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
V032, V039, and the refuted parts of V025, V028 and V038.

## 5. The missing estimates, in order

The first missing inequality is the same for the closest route (section 7): the edge Garding lemma (E) for the
anisotropic weight w_a. In the form of S2_L2_THEORY.md section 5:
     Re <T_R h, h>_{w_a} <= int (b_+ + eps) |h|^2 w_a + Re <K h, h>_{w_a},  K compact,
for the Taylor-subtracted coupling T_R. The y-axis traces U_2[h](0, .) and d_x U_1[h](0, .) must be bounded, and
compact into the jet target after multiplication by rho_2 and rho_2'. Its parts are (E1) the weight in y, (E2) the
origin corner, (E3) input outside a strip with output inside it, and (E4) the Garding part for |cos theta|^{-2a} e^{mu_a}.
After (E) the remaining items are:
1. (H_m') certified: inf (kappa_{w_a} - b_+) > 0 on all of R^2 \ {0}. The grid value is 3.09 (NUMERICAL).
2. Injectivity of L_red on Z with a quantitative inverse bound (K_L at h = 0). This is the complement estimate.
3. The high-norm inverse K_H in X_hi, with the regularity bookkeeping of S2_L2_THEORY.md section 6.
4. The bilinear bound C_B with the jet decomposition (3.5(c)).
5. The residual eta in Y_sigma, including its axis jet (3.5(d)), with a certified enclosure.
6. The application of the abstract two-norm theorem (3.4, V038) to the moving-tail equation: its hypotheses for the
   augmented map of 2.2 (or for the version with ell = ell(h) eliminated), with the ell-dependence of the compact part
   of the Garding estimate bounded.

## 6. Constants that need certification

| Quantity | Needed for | Status |
|---|---|---|
| c[rho~] = 3/k - 1 (exact normalization) | every rigorous statement | CERTIFIED (V005; numerics team C1) |
| source x_P, mu_P, g_P | source inverse | THEOREM (V017) |
| source neighbourhood margin kappa - E | source inverse | THEOREM (V024) |
| m_* for mu~ (H_m) | Theorem R for L_fix | grid 2.590 (NUMERICAL); box certificate in progress in the numerics team; V033 defect to be fixed first |
| m_a for w_a (H_m') | Theorem C, scheme | grid 3.09 (NUMERICAL); box certificate requested |
| positive axis rate q(0, y) > 0, y != 0 | N2, S1.4 | NUMERICAL (5.58 <= V_2/y <= 21.31 on the grid) |
| d = 3 c_l + k c[KP] != 0 | rank-one bordering | THEOREM (V034): d >= 3 c_l > 0 for every admissible cutoff; the numerics team's ball value c[KP] = 0.0703723 gives d about 16.74 |
| s_3 = int sin(3 theta) Theta_0 | the sign of c[KP] | THEOREM (V034): 37.63077494715565 < s_3/pi < 37.63077494715567 |
| C_a, trace constants | (E) | THEOREM at strip scope (V026) |
| Prop C2 constant C_cap | c bounded on Z_cap | THEOREM (V034): C_cap < 0.312093 (a = 7/2, b = 6/5), C_cap < 0.359253 (a = 17/4, b = 0) |
| K_A <= 0.032163 | frozen c adjoint | THEOREM (V016) |
| finite-section sigma_min and off-basis residual | Avenue IV | PENDING (section S0); interval defects V027, V033 |
| eta, K_H, K_L, C_B, C_V, r_V | closure inequalities 3.4 | not available |

## 7. The closest avenue and why

The closest route combines Avenues I and III and uses Avenue IV for the complement:
- the anisotropic L^2 space Z with weight w_a;
- the jet coordinate J and the y-axis jet;
- the rank-one bordering by KP, or by ell in the parametric form;
- a certified finite-dimensional injectivity check for the compact part of the Garding estimate.

Reasons:
1. Every frozen piece is proved with explicit constants: Theorem O at the origin (V022), the source inverse (V011,
   V021, V024) and the far window (V025, N4).
2. The global Fredholm mechanism is proved for radial weights (V023, V031). It transfers to w_a once (E) is proved.
   (E4) has the same structure as V023, and (E1) to (E3) are local estimates near the y-axis and the corner. V026
   already proves the strip piece.
3. The normalization is handled exactly. c is bounded on Z_cap (Prop C2, V034), and the need for the origin part of
   Z_cap is a theorem (V032). d >= 3 c_l > 0 is a theorem (V034), so the tail coordinate (KP or ell) can be eliminated
   exactly. This does not invert the reduced operator L_red: when L_ren is invertible, L_red is invertible if and only
   if the scalar 1 + c[L_ren^{-1} zeta] is nonzero (V038), and L_ren still needs its own inverse. The scalar
   normalization ell(h) is unique with |ell(h) - c_l| <= |c[h]|/3 (V038).
4. The grid margins have room: 3.09 for w_a and 2.59 for mu~, against a perturbation cost that 3.5(a) bounds linearly
   in ||D W[h]||_infinity.
5. By 3.5(b), for a fixed background, uniformity over the correction ball reduces to the single h = 0 complement estimate (in the parametric form the ell-dependence of K must also be bounded), because the compact
   part does not depend on h.

Avenue II is farther. There is no Hoelder analogue of the sharp Garding inequality. The Hoelder theory of the actual
transport near 0 is OPEN (the conjugacy transfer was REFUTED, V028). Lemmas N and N' show that C^alpha alone cannot
close the nonlinear problem.

Avenue IV alone is farther. A finite section is not an inverse bound without a complement inverse (V014). The first
exact section (S0: 4 angular modes, 169 columns) is still being assembled, and its interval pipeline has open defects
(V033).

## 8. Checklist against the strict standards (PROMPT 11)

| Standard | Status in this run |
|---|---|
| Inverse statements give domain and range | Theorem O (Z_0 -> Y), Theorem R (maximal domain D_w -> L^2(w)), source inverses (maximal H^s realizations), Theorem C (Z -> Y, CONDITIONAL) |
| Membership of perturbation and image | checked: x^2 y in Z_0 (J = 1); r^k Theta not in Z; r^{2k-1} Eps in the far target; the coupling image of Z_0 under (E) only; the residual near 0 OPEN (3.5(d)) |
| Normalization meaningful and closed | J is continuous on Z_0 (V022). c is bounded on Z_cap (DERIVED, Prop C2). c is not closable on the radial graph (V032), and J is not closed in the weak norms (V012), so neither of these weaker spaces is used for the normalization |
| Log variation of exponent perturbations | KP = chi_inf r^k log r Theta_0 carried explicitly; parametric family rho_bar_ell (2.2); log^2 second variation noted (V025) |
| Full infinite-dimensional operator, not its matrix | finite sections are used only with a complement estimate (V014); the complement is OPEN |
| No unproved finite rank, compactness or small residual used as invertibility | complied with; the Fredholm statements are labelled as such, and injectivity is OPEN |
| Absence of proof is not nonexistence | complied with (section 1) |
| Counterexamples where a bound fails | given: V006, V007, V009, V010, V012, V019, V025, V028, V030, V032; code defects V020, V027, V033 |
| Bounds valid but too large | the V026 constant C_a (about 593 at a = 17/4) forces strip width R < 0.02/sup abs(rho_2). Whether this loss is intrinsic is OPEN |
