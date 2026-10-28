# S2_C_FUNCTIONAL.md: Avenue III, the singular functional c[h] = psi_xy[h](0)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T02:27Z (theory author), corrected 02:33Z, 02:45Z (V032 in 5.2 and 8.4) and 02:54Z (V034, V035), and 03:07Z (V038 on the reduced inverse), and 12:05Z (section 10: status at 12:05Z), and 13:51Z (section 10: the finite split of V190), and 14:34Z (6.4 (E2): the Hoelder form of the corner rate, V219), and 15:54Z (review corrections V251: the eta = -4 endpoint construction in 5.2, the general-p dual conditions in 2.5, pointwise scopes in 1.1 and 6.1, the target of the V190 obstruction in 10, historical status markers in 0, 2.4, 6.4, 8.3, 8.4 and 10), and 15:59Z (10: Z_2 mapping confirmed, V254) and 16:56Z (V274: the averaging bound of the zero-strain packets). Labels:
- DERIVED: derived by the theory author, not yet checked.
- CONFIRMED (Vnnn): checked by the verifier at the scope of verification record Vnnn; such a statement carries the
  label THEOREM (CONDITIONAL THEOREM when it has explicit hypotheses).
- REFUTED (Vnnn): shown false by the verifier.
- NUMERICAL: grid evidence, not a bound.
- OPEN.
Background: every quantitative statement refers to the exactly normalized modal trial rho~ (CONVENTIONS S0.3(i)), for which
c_l = 1/k exactly. Notation follows CONVENTIONS.md:
- A = 2c_l - 1 = 10.15073, D = 4c_l - 1 = 2A + 1 = 21.30145, b_0 = (A + 3)/2 = c_l + 1 = 6.57536.
- t = log r. The frozen saddle field is V_0 = (-Ax, Dy) and T_0 = V_0.grad - 1.

## 0. Summary of the answers

Sections 0 to 9 record the status of 03:07Z, apart from the later corrections listed in the header. Where they call an
item OPEN or requested, section 10 (status at 12:05Z) records what was completed later.

Q1 (saddle-adapted local estimate).
- The frozen saddle admits coercive local and global estimates, but only in anisotropic weights.
- The product weight w = |x|^{-ap}|y|^{-bp} has the exact multiplier kappa_0(p) = 2c_l/p + 1 + Aa - Db (Prop M). This
  multiplier is the adjoint weight.
- The inflow sides of a box (the stable x-direction) give a flux of the good sign. The outflow sides (the unstable
  y-direction) give a flux that is not small. After y-averaging, that flux is a shell norm along the outgoing axis.
- For p = 2 the global version is Theorem O (CONFIRMED, V022), with sharp inverse norm 1/kappa_0 and a continuous jet
  coordinate J.
- With the verified constants this gives the explicit frozen bound (Corollary C1):
  |c_<[h]| <= 0.0027316 ||f||_R + 0.0136875 ||gamma||_G <= 0.013958 ||T_0 h||_F, for h with J = 0 and
  T_0 h = x^2 y gamma(log r) + f.
- Radial and isotropic moments cannot be coercive (CONVENTIONS S7.3, V010).

Q2 (absorbing the nonlocal remainders).
- After the exact strain cancellation and the parity-dictated subtraction of the two y-axis jets U_2(0, y) and
  x d_x U_1(0, y), the remaining coupling has an explicit O(R) bound on x-strips of width R:
  eta(R) = 2 C_a R ||rho_2|| + C_a R^2 ||rho_2'|| + D_a R^3 ||r_1|| + D_a R^4 ||r_2|| -> 0.
  This is CONFIRMED (V026) at local-strip scope, for 5/2 < a < 9/2 and no weight in y.
- The origin corner, the weight in y, and the interaction with input outside the strip were OPEN at 03:07Z. Together
  they form the edge lemma (E) of S2_L2_THEORY.md section 5. (Superseded: section 10 treats the nonlocal remainders as
  compact perturbations of a Fredholm low realization.)

Q3 (reducing the rank-one term).
- c is bounded on the domain Z_cap (Theorem O control on r < 2, plus L^2(e^{mu~}) globally), with
  |c[h]| <= 0.31210 ||h||_{Z_cap} (Prop C2, THEOREM, V034, with C_cap < 0.312093; from V022(c) and an elementary far bound).
- Near the origin, the rank-one term (c[h]/3) G_bar cancels the linear part of U[h].grad rho_bar exactly.
- At infinity it is bordered by the log direction KP = chi_inf r^k log r Theta_0. The scalar denominator
  d = 3c_l + k c[KP] satisfies d >= 3 c_l > 0 for every smooth cutoff 0 <= chi_inf <= 1 supported in r >= 1
  (THEOREM, V034; the first version needed a cutoff radius beyond an explicit R_*).
- After bordering, the rank-one term is a bounded rank-one perturbation inside the target space. It does not change the
  Fredholm index. d != 0 (a theorem, V034) permits the exact elimination of the tail coordinate. It does not invert the
  reduced operator: when L_ren is invertible, L_red is invertible if and only if 1 + c[L_ren^{-1} zeta] != 0, and
  L_ren needs its own inverse (V038).

Obstruction (task item 5.5).
- The explicit bound |c[h]| <= C_c ||L h||_Y for the full operator is not obtained.
- The obstruction lies in the velocity remainders and weighted elliptic bounds at the origin corner and along the
  outgoing axis, which is (E) (status of 03:07Z; superseded by section 10).
- A second obstruction is the absence of a quantitative inverse: Theorem R and its corner analogue are Fredholm
  statements without a norm bound for the inverse.
- The obstruction is not in the adjoint weight, which exists explicitly with kappa_0 > 0.
- It is not in the inflow fluxes, which have the good sign.
- It is not in the rank-one reduction. The elimination of the tail coordinate is exact, given d != 0 (V034). The
  inverse of the reduced operator is a separate question (V038).
- The function space matters: every isotropic or radial space at the x^2 y scale fails (V010, S7.3). Within the
  coercive product-weight mechanism of N1 (V025), a space in which x^2 y is excluded and the frozen operator is
  coercive needs a >= 5/2 near the y-axis. V035 corrects a broader reading: continuity of J alone does not force
  anisotropic weights. The anisotropy is a requirement of the coercive method, not of every space.

## 1. The functional: normalization, convergence, symmetry

1.1 (CONVENTIONS S3.1 and S3.2; CONFIRMED V002)
- c[h] := psi[h]_xy(0) = d_y U_2[h](0) = -d_x U_1[h](0), not divided by 3.
- For h in the parity class P (even in x, odd in y) with |h| <= C r^{1 + eps} near 0, |h| <= C <r>^beta at infinity
  (beta < 1), and h locally Hoelder:
     c[h] = (1/pi) int_{R^2} sin(3 theta) r^{-3} h(X) dX      (absolutely convergent).
- Near 0 the integrand is O(r^{eps - 2}) times the area element r dr. At infinity it is O(r^{beta - 3}) times r dr.
- sin 3theta is odd in y and even in x, so the formula only sees the P-part of h.
- Scaling: c[lambda h(./lambda)] = c[h] (CONVENTIONS S5.1).
- If d_y h(0) != 0 the canonical functional carries the extra local term -(1/4) d_y h(0) (CONVENTIONS S3.2 warning). In the
  smooth and high-regularity S2 classes of sections 2 to 9 every correction is O(r^3) at 0 (by their pointwise
  regularity hypotheses), so the term is absent. This blanket statement does not cover the later Hoelder realization on
  E_2 = C^alpha_2 (accompanying S2_CALPHA_THEORY.md), which has only the weaker pointwise bounds h = O(r^(2 + alpha))
  and U[h](X) = c[h](-x, y) + O(r^2 (1 + |log r|)) at 0 (V205). The local derivative term still vanishes on E_2,
  because h = O(r^(2 + alpha)) gives d_y h(0) = 0.

1.2 Normalization: c[x^2 y chi] > 0 for a radial cutoff chi >= 0. Also c_<[x^2 y] = 1/8, where
c_<[h] := (1/pi) int_{r<1} sin(3 theta) r^{-3} h dX. Here the angular integral of cos^2 sin sin3 is pi/4 and the radial
integral is int_0^1 r dr = 1/2, so c_<[x^2 y] = (1/pi)(pi/4)(1/2). The value 1/8 is part of V022(c).

1.3 Known continuity statements:
- (V004) c is continuous on the diagnostic space X of Analysis I, with constant 1/(L^2 sqrt(11 pi (1 - 2k))). There J is
  unbounded, and {J = 0} is dense even at fixed c (V012). No estimate of c by L h follows.
- (V016) A frozen sup-norm adjoint bound: |c_R[h]| <= K_A R^2 ||T_0 h/(x^2 y)||_inf, with zero outer flux and
  K_A <= 0.032163 (the certified value is about 0.032162163; use the upward-rounded bound, V028). The angular adjoint ODE at degree -3 has no solution bounded at both axes. The singular solution
  omega_0 pairs absolutely with x^2 y C^1 factors.
- (V021) At the source, the auxiliary inverse on H^s has raw-strain norm exactly 1/[8 sqrt(pi (s-1)(s-2))]
  (0.046401 at s = 3.1).
- (V022(c)) On the jet-plus-remainder space Z_O of Theorem O:
     |c_<[h]| <= |J|/8 + C_v ||v||_G + C_R ||u||_R,
  with C_v = 1/[8 sqrt(sigma(sigma+1)(sigma+2))] and C_R as in V022. For a = 7/2, b = 6/5 (sigma = 7/10):
  C_v = 0.0697356174, C_R = 0.0451831833.
- (V018) X3 itself is not exactly normalized. Every certified statement uses rho~.

## 2. Characteristic geometry of the saddle and the local moment (Prop M, DERIVED)

2.1 Geometry.
- The flow of V_0 is Phi_s(x, y) = (x e^{-As}, y e^{Ds}). The invariant is |x|^D |y|^A, so characteristics are the
  curves |x|^D |y|^A = const.
- The x-axis is the stable (incoming) manifold and the y-axis the unstable (outgoing) one.
- On a box Q = {|x| < R_x, |y| < R_y} the sides x = +-R_x are inflow (V_0.n = -A R_x < 0) and the sides y = +-R_y are
  outflow (V_0.n = D R_y > 0). For the actual field V the same signs hold on the boxes of 2.4.
- This is the opposite of the expanding model B_beta = (x/2, beta y) of task item 5.1, where every side is outflow.

2.2 Identity. Let p in [1, inf), w = |x|^{-ap}|y|^{-bp}, and phi = phi(y) even, equal to 1 for |y| <= R, linear in |y|
on [R, 2R], and 0 beyond.
- The identity is for the remainder class:
  - h is in P;
  - h and (V.grad - 1) h are in L^p(w) on Q = {|x| < R_x} x {|y| < 2R};
  - V is the C^1 background field.
- In the log coordinates (log|x|, log|y|) of each quadrant the axes and the origin are at infinity, so no flux arises
  there. This is the closed-realization argument of V022, applied with |h|^p in place of |h|^2.
- Define
     kappa_w(X) := 2 c_l/p + 1 - a V_1(X)/x - b V_2(X)/y        (div V = 2 c_l),
  so that kappa_w(0) = kappa_0(p) = 2c_l/p + 1 + Aa - Db (CONVENTIONS S7.3; 2c_l = D - A).
- Then
     int kappa_w |h|^p w phi = - int ((V.grad - 1) h) |h|^{p-2} h w phi
                               + (1/p) Flux_in + (1/p) int |h|^p w (-V_2 phi'(y)),
  where Flux_in = int_{x = +-R_x} |h|^p w phi V.n <= 0.
- Proof: from div(V w phi) = p (kappa_w - 1) w phi + w V_2 phi'. Integrate (1/p) V.grad|h|^p against w phi by parts.

2.3 Estimate. Assume, on Q, that:
- V_1/x < 0 (inflow at x = +-R_x);
- V_2/y > 0 (so -V_2 phi' >= 0);
- Delta := inf_Q kappa_w > 0.
Let N := (int |h|^p w phi)^{1/p}, which is at least M_R := ||h||_{L^p(Q_R, w)}, where Q_R = {|x| < R_x, |y| < R}. Then
   N <= Delta^{-1} ||(V.grad - 1) h||_{L^p(Q, w phi)} + (2 Vhat/(p Delta))^{1/p} ||h||_{L^p(S_R, w)},
with S_R = {|x| < R_x, R < |y| < 2R} and Vhat = sup_{S_R} V_2/y. For the frozen field Vhat = D.
- Proof. Drop Flux_in. Use |V_2 phi'| <= 2 Vhat on S_R and Hoelder, which gives Delta N^p <= F N^{p-1} + B with
  B = (2 Vhat/p)||h||_{S_R}^p.
- If N > F/Delta + (B/Delta)^{1/p}, then N^{p-1}(Delta N - F) > B, a contradiction.

2.4 Size of Delta for the modal trial (NUMERICAL; artifacts/code/lyapunov/box_moment.py; grid of field.npz with the axis
rows excluded; R_x = 2R, Q = Q_{2R}). The sign conditions V_1/x < 0 and V_2/y > 0 hold on all of these boxes.

| p | a | b | kappa_0(p) | Delta on Q_2R, R = 0.1 | R = 0.25 | R = 0.5 | R = 1 |
|---|---|---|---|---|---|---|---|
| 2 | 7/2 | 6/5 | 16.5412 | 16.504 | 16.308 | 15.621 | 13.030 |
| 2 | 17/4 | 0 | 49.7159 | 49.626 | 49.174 | 47.513 | 41.480 |
| 4 | 7/2 | 6/5 | 13.7535 | 13.716 | 13.520 | 12.834 | 10.242 |
| 1 | 7/2 | 6/5 | 22.1165 | 22.079 | 21.883 | 21.197 | 18.606 |

The variable transport costs little: Delta stays within 26 percent of kappa_0 up to |x|, |y| < 2. This is the explicit
positive Delta_R of task item 5.4 for the transport part. It is not yet a certified bound. A certificate needs box enclosures
of V_1/x and V_2/y of the same kind as the margin certificate then requested from the numerics team (status of 03:07Z;
the margins were verified later, section 10).

2.5 What Prop M does and does not give.
- Jets are excluded from the class. If a > 2 + 1/p, then x^2 y beta(y) with beta != 0 is not in L^p(w) near the
  y-axis (angular integral of |cos theta|^{(2-a)p}). The jet is carried separately as in Theorem O, and Prop M is the
  remainder row.
- The shell term is not lower order. S_R touches the outgoing y-axis, where the weight is singular. A solution there has
  the structure x^2 g(y) + remainder, and ||h||_{L^p(S_R, w)} is the remainder norm on the next dyadic block of the
  outgoing axis.
  - Iterating Prop M in y does not close: the flux is transported out to the next block.
  - It closes only with a global treatment of the whole outgoing axis. Theorem O does this for the frozen field: the
    double-logarithmic transform is global and the outflow goes to t = +inf.
  - The answer to "the influence of the boundary fluxes along the stable and unstable directions":
    - stable (inflow) fluxes are harmless;
    - unstable (outflow) fluxes are the reason that no purely local moment closes;
    - they are controlled by the global realization, not by a local smallness.
- Isotropic weights fail. For r^{-beta p} the multiplier is 2c_l/p + 1 - beta(-A cos^2 theta + D sin^2 theta), negative
  on the y-axis once beta > (D - A + p)/(pD) (CONVENTIONS S7.3). Every weight that sees the x^2 y scale (beta near 3 + 2/p) is
  indefinite. V010 shows that the radial moment gap fails even with an H^s remainder (2 < s < 4 - 2/p): there are
  smooth compact J = c = 0 perturbations with ||h/r^3||_{L^p(B_R)} = 1, image moment -> 0 and ||h||_{H^s} -> 0.
- Exponents p: any p in [1, inf) with kappa_0(p) > 0. The p = inf limit is Prop H0 of S2_CALPHA_THEORY.md (weighted
  sup inverse 1/(1 + aA - bD)). For 1 < p < inf and real a, b the near strain c_< of 1.2 (integral over the unit disk
  B_1) is bounded on the parity subspace of L^p(B_1, w) exactly when a + b > 1 + 2/p, a > -1/p' and b > -1 - 1/p'
  (duality, V251). The last two conditions are automatic for a, b >= 0, which covers every weight used here. Without
  them the radial test alone is not sufficient: p = 2, a = 5, b = -2 passes it, but the dual kernel is not square
  integrable near the x-axis (V251). On B_1 the exact dual constant is C_p = (1/pi)(Ang_p/((a + b - 3)p' + 2))^{1/p'},
  with Ang_p = int |sin 3theta|^{p'} |cos theta|^{a p'} |sin theta|^{b p'} dtheta. For p = 2 this is C_R of V022. On a
  rectangle {|x| < R_x, |y| < R_y} the same three conditions decide boundedness, but the angular integrand carries the
  extra factor R(theta)^s, with s = (a + b - 3)p' + 2 and R(theta) = min(R_x/|cos theta|, R_y/|sin theta|); the
  constant is then (1/pi)(s^{-1} int |sin 3theta|^{p'} |cos theta|^{a p'} |sin theta|^{b p'} R(theta)^s dtheta)^{1/p'}.
  p = 2 is the only exponent with a Hilbert structure, and the Hilbert structure is what the Fredholm theory and
  Avenue IV use.

## 3. The adjoint weight and the representer of c (DERIVED)

3.1
- On the remainder space R, Theorem O (V022) gives the outflow resolvent
  T_{0,R}^{-1} f(X) = -int_0^inf e^{-s} f(Phi_s X) ds. So u(X) is determined by f along the forward orbit of X.
- For f in R, substituting Y = Phi_s X (dX = e^{-(A+1)s} dY) gives
     c_<[T_{0,R}^{-1} f] = int f phi_R dY,
     phi_R(Y) = - int_0^inf e^{-(A+2) s} omega(Y_1 e^{As}, Y_2 e^{-Ds}) ds,   omega = (1/pi) sin(3theta) r^{-3} 1_{r<1}.
- phi_R solves the adjoint equation T_0^* phi_R = omega with T_0^* = -V_0.grad - (A + 2), in the distributional
  sense on the quadrants, and phi_R is in the dual space R' = L^2(w^{-1}).
- The jet row is not an outflow problem. The J = 0 inverse integrates beta' = gamma/D from the origin
  (t = -inf), not along forward orbits. Hence for T_0 h = x^2 y gamma(log r) + f with J = 0 the full representer is
  the pair
     c_<[h] = int (f + ((A + D)/D) x^2 y cos^2(theta) gamma(log r)) phi_R dX
              + (1/(8D)) int_{-inf}^0 (1 - e^{2s}) gamma(s) ds,
  where the second term is the jet formula of V022.
- This pair is the adjoint weight of the two-step idea of task item 5.1, in the saddle geometry.

3.2 Properties.
- Sign: phi_R is not positive. It inherits the sign changes of sin 3theta along the backward orbits.
- Support: supp phi_R is contained in the forward hull {Phi_s X : |X| < 1, s >= 0}, which lies in
  {|x| < 1, |x|^D |y|^A < 1}. This is a cusp around the outgoing y-axis, unbounded in y.
- Integrability: the part of the integral with s near 0 gives phi_R(Y) of size |Y|^{-3} near 0, so phi_R is not
  bounded at 0 and is not integrable against |h| for general h. The pair of 3.1 is a
  bounded functional on F, with norm <= 0.013958 (Corollary C1).
- The adjoint weight of the expanding-flow construction cannot be copied (task item 5.1). For the saddle, V016 shows
  that the homogeneous angular adjoint at degree -3 has no solution bounded at both axes.
- So the adjoint weight exists only as a dual element of the anisotropic space, not as a positive pointwise weight.

## 4. Corollary C1: the explicit frozen strain bound (DERIVED arithmetic from CONFIRMED V022 constants)

Let a = 7/2, b = 6/5, sigma = 7/10, kappa_0 = 16.54116035, C_ang = (20/3)^{1/2} = 2.5819889. Let h be in Z_O with J = 0
and T_0 h = x^2 y gamma(log r) + f (gamma in G, f in R).
- By V022, v = gamma/D and ||u||_R <= kappa_0^{-1}(||f||_R + (A + D) C_ang ||gamma||_G / D).
- Hence
     |c_<[h]| <= C_F ||f||_R + C_gamma ||gamma||_G <= C_c0 ||T_0 h||_F,
     C_F = C_R/kappa_0 = 0.0027315607,
     C_gamma = C_v/D + C_R (A + D) C_ang/(D kappa_0) = 0.0136874900,
     C_c0 = (C_F^2 + C_gamma^2)^{1/2} = 0.0139573925 (rounded; the verified upper bound is C_c0 < 0.013958, V034).
- For J != 0, add |J|/8. c_< is then not controlled by T_0 h, since x^2 y spans the kernel. This is the scaling freedom.
- Alternative weight a = 17/4, b = 0 (sigma = 1/4, allowed by Theorem O since a + b > 4). It matches the y-unweighted
  strip estimate V026:
  - C_R = 0.1278385, C_v = 0.1490712, C_ang = 2.6442680, kappa_0 = 49.7159448;
  - C_F = 0.0025714, C_gamma = 0.0170377, C_c0 = 0.0172306 (rounded down; the verified upper bound is C_c0 < 0.017231,
    V034).

## 5. Prop C2: boundedness of c on the intersection domain (CONFIRMED, V034, with the upper bounds below)

5.1 Far part.
- Let mu~ be the piecewise-linear weight exponent of the theory author's note of 02:18Z, with mu~(0) = 0, mu~' in [-5/4, 7/4],
  mu~'(+inf) = -5/4.
- For c_>[h] := (1/pi) int_{r>1} sin(3theta) r^{-3} h dX, Cauchy-Schwarz in L^2(e^{mu~(log r)} dX) gives
     |c_>[h]| <= (I/pi)^{1/2} ||h 1_{r>1}||_{L^2(e^{mu~})},   I = int_0^inf e^{-4t - mu~(t)} dt = 0.2352184,
  so C_> = 0.2736281, with the verified upper bound C_> < 0.273629 (V034). I is evaluated in closed form on each
  interval of mu~ (30 digits).
- In general C_> <= (pi (4 - M_-))^{-1/2} with M_- = sup_{t>0} max(-mu', 0) < 4. Hence any Theorem R weight with
  sup|mu'| < 2 controls c_>.
- The homogeneous product weight of Theorem O does not control c_> at infinity: the dual integral grows like
  r^{2(a+b) - 4}.

5.2 The domain Z_cap.
- Let chi_1 be a smooth radial cutoff, equal to 1 for r <= 1 and 0 for r >= 2. Define
  Z_cap := {h : chi_1 h in Z_O, h in L^2(e^{mu~})}, with ||h||_{Z_cap}^2 = ||chi_1 h||_{Z_O}^2 + ||h||_{L^2(e^{mu~})}^2.
- Since c_<[h] = c_<[chi_1 h],
     |c[h]| <= |J|/8 + C_v ||v||_G + C_R ||u||_R + C_> ||h||_{mu~} <= C_cap ||h||_{Z_cap},
  where (J, v, u) are the coordinates of chi_1 h and C_cap = (1/64 + C_v^2 + C_R^2 + C_>^2)^{1/2}.
  - At a = 7/2, b = 6/5: C_cap = 0.3120928222..., so C_cap < 0.312093 (V034). The decimal 0.3120928 printed in the
    first version is an approximation from below, not an upper bound.
  - At a = 17/4, b = 0 (the weight matched to V026 and to w_a): C_cap < 0.359253 (V034).
- The localization is deliberate. The product weight of Z_O is not usable at infinity: its radial exponent
  -2(a + b) < -8 lies far outside the range sup|mu'| < 2 of Theorem R.
- Z_cap is a domain for the c-bound only. The operator-level domain is the weight of S2_L2_THEORY.md section 5,
  whose angular factor carries the near-axis control at every height. Commutators with chi_1 near the y-axis in
  1 < r < 2 are controlled only in that weight. Whether L maps that domain into its target is (E).
- The origin part of Z_cap cannot be dropped. By V032 (THEOREM), on L^2(w) with w ~ r^eta near 0 and eta >= -4
  (this includes e^{mu~}, eta = 1/4), there are smooth compact inputs h_n with J = 0 and c = 1, while h_n -> 0 and
  L_fix h_n -> 0. The construction differs at the endpoint:
  - for eta > -4 (in particular for e^{mu~}) the single rescaled annular packets h_n = eps_n H(X/eps_n) with c[H] = 1
    suffice, since their graph norm tends to zero (the input and frozen transport parts are
    O(eps_n^(2 + eta/2)));
  - at eta = -4 the L^2(w) norm of a single packet is bounded below by a positive constant, so the single family does
    not tend to zero. V032 then uses the averages h_n = (1/n) sum_{j=1}^n eps_j H(X/eps_j) of n packets on disjoint
    geometric scales eps_j = eps_* 4^(-j). Disjointness of the supports gives the bound O(n^(-1/2)) for the packet
    inputs and their frozen transport images; the nonlocal coupling and error terms of the individual packets have
    norms O(eps_j^2), a summable sequence, so their average contributes O(1/n). Hence the graph norm of h_n is
    O(n^(-1/2)) while c[h_n] = 1.
  So c is not closable on the L_fix graph in L^2(e^{mu~}). In Z_cap the single packets have
  ||chi_1 eps H(./eps)||_{Z_O} -> infinity (of order eps^{2-a-b}), consistent with Prop C2.
- J is a coordinate of norm 1 on Z_cap.
- So the two prerequisites of task item 5.4 hold on Z_cap: c is bounded and J is continuous, before any rank-one
  treatment.

5.3 Membership.
- x^2 y chi_0 is in Z_cap (J = 1).
- r^k Theta chi_inf is not in L^2(e^{mu~}): mu~'(inf) = -5/4 > -2 - 2k.
- The trial residual r^{2k-1} Eps is in L^2(e^{mu~}): -5/4 < -4k = -0.7174.
- The log direction KP = chi_inf r^k log r Theta_0 is not in Z_cap. It is added as a separate coordinate (section 7).

## 6. Renormalized coupling and the remainder smallness (task item 5.3)

6.1 Exact cancellation (CONVENTIONS S4.5; with C2 of CONVENTIONS v1.1 for the pointwise reading).
- U[h] = DU[h](0) X + U^(2)[h], with DU[h](0) X = c[h](-x, y). Hence
     (U[h] + (c[h]/3) X).grad(x^2 y) = c[h](-2x/3, 4y/3).(2xy, x^2) = 0   exactly.
- For rho_bar = x^2 y a_bar: W[h].grad rho_bar = U^(2)[h].grad rho_bar + c[h] x^2 y (-(2/3) x a_x + (4/3) y a_y).
- The last factor is o(1) at 0 when |x a_x| + |y a_y| -> 0.
- On the y-axis the x^2 coefficient of the c-terms also cancels to leading order as y -> 0. By parity
  T h := U_2[h](0, y) = c y + O(y^3) and T1 h := d_x U_1[h](0, y) = -c + O(y^2). If a_bar(0, .) is C^2, then
  rho_2(y) = y a_bar(0, y) = y + O(y^3). Hence
     2 rho_2 (T1 h + c/3) + rho_2' (T h + c y/3) = 2y(-2c/3) + (4/3) c y + O(y^3) = O(y^3).
  The O(y^3) coefficient depends on h through the next Taylor terms of the traces, not only through c. The c-part of
  the last bracket is the term (c/3)(2 rho_2 + y rho_2') of V025 (N3).
- Scope of the pointwise reading. The trace expansions and the O(y^3) remainder assume that U_2[h](0, .) and
  d_x U_1[h](0, .) have the corresponding Taylor expansions at 0, as in the smooth and high-regularity classes of this
  file. On the Hoelder space E_2 of the accompanying S2_CALPHA_THEORY.md only U[h](X) = c[h](-x, y) + O(r^2 (1 + |log r|))
  at 0 is proved (V205), and the O(y^3) remainder is not claimed there. The exact cancellation of the first display
  needs only DU[h](0) = c[h] diag(-1, 1), which V205 proves on E_2.

6.2 Parity Mellin subtraction (S2_L2_THEORY.md section 5).
- U_1 is odd in x and U_2 is even. The coupling needs U_1 in L^2(|x|^{-2(a-1)}) and U_2 in L^2(|x|^{-2(a-2)}).
- Subtracting x d_x U_1(0, y) and U_2(0, y) moves the admissible windows to (3/2, 7/2) and (1/2, 5/2), which is
  exactly 5/2 < a < 9/2 (1D model).

6.3 Strip estimate (CONFIRMED, V026, local-strip scope). For inputs h even in x, supported in |x| < R, in
L^2(x^{-2a} dx dy), and a background with rho_x = 2x rho_2(y) + x^3 r_1, rho_y = x^2 rho_2'(y) + x^4 r_2 on the strip,
   E_R h := U[h].grad rho - x^2 [2 rho_2 T1 h + rho_2' T h]
satisfies
   ||E_R h||_{(a,R)} <= eta(R) ||h||_{(a,R)},
   eta(R) = 2 C_a R ||rho_2||_inf + C_a R^2 ||rho_2'||_inf + D_a R^3 ||r_1||_inf + D_a R^4 ||r_2||_inf.
- Here
     C_a = 1 + 10 * 2^{a+1/2} + 64[1 + 1/(9/2 - a)] + 2[1/(a+1/2) + 1/(a-1/2) + 1/(a-3/2) + 1/(a-5/2)],
     D_a = C_a + B_a/sqrt(9 - 2a).
- The traces satisfy ||d_y^j T h||_{L^2(dy)} <= B_a R^{a-j-1/2} ||h||_{(a,R)} for j = 0, 1, 2. For rho_2 in C_c^2 the
  jet coupling is compact into L^2(dy).
- This answers task item 5.3 at strip scope: eta(R) -> 0 is proved, with an explicit rate O(R).
- The constants are far from sharp. At a = 17/4, C_a is about 593, so eta(R) < kappa_0/2 = 24.9 needs about
  R < 0.02/||rho_2||_inf.

6.4 What remained of (E) at 03:07Z (OPEN then; superseded by section 10, where the nonlocal remainders are compact
perturbations of a Fredholm low realization; the Hoelder statement in (E2) is from 14:34Z).
- (E1) The weight in y. V026 is unweighted in y. With b = 0 and 4 < a < 9/2, the Theorem O weight near the origin is
  exactly the V026 weight in x. Along the axis at every height, the section 5 weight multiplies |x|^{-2a} by a
  function of y that is bounded above and below on compact y-intervals. The dyadic y-blocks and the origin must still
  be coupled.
- (E2) The origin corner.
  - The y-traces T h, T1 h near y = 0 must lie in the jet target G after the c-subtraction of 6.1.
  - rho_2(y) = O(|y|) there, so a box version of 6.3 would have eta = O(R^2). This is DERIVED heuristically, not
    proved in L^2. Its Hoelder analogue is proved: on C^alpha_2 (accompanying S2_CALPHA_THEORY.md, 2(e)) the complete
    normalized coupling localized to B_delta has operator norm comparable to delta^2, and the rate is sharp (THEOREM,
    V219); without the term c[h] X/3 the rate is of exact order delta^(1-alpha) (DERIVED: the difference is the
    rank-one term c[h] chi_delta X.grad rho~/3).
- (E3) Input outside the strip, with output inside it. The kernel is smooth in x at positive distance. The expected
  bound is C(R)||h||_reg, with the anisotropic shell norm of 2.5 as ||.||_reg.
- (E4) The Garding part away from the axis is the radial-weight argument of V023. It must be redone for the product of
  the angular factor and e^{mu}.
- (E2) and (E3) are the precise remaining estimates of Avenue III.

## 7. Prop B: rank-one bordering (CONFIRMED, V034, conditional on the domain hypothesis in 7.3)

7.1 Setting.
- Target space: Y := {f : chi_1 f in F, f in L^2(e^{mu~})}, with the sum norm. This is the target analogue of Z_cap.
- Let Phi_hat := chi_inf r^k Theta_0. It is not in Y, since it is not in L^2(e^{mu~}).
- Let chi_0 be a cutoff equal to 1 near 0 with compact support. Write (1 - chi_0) G_bar = k Phi_hat + g_far, where
  G_bar = X.grad rho~. Then g_far is in Y, because the trial's next far term is (2k - 1) r^{2k-1}(...), which is in
  L^2(e^{mu~}).
- Let KP := chi_inf r^k log r Theta_0, the log variation of the far tail: (c_l r d_r - 1)(r^k log r) = c_l r^k
  (CONVENTIONS S6.4).
- Define y_KP by L_fix KP + (c[KP]/3) chi_0 G_bar = c_l Phi_hat + y_KP.
- Then y_KP is in Y:
  - (V - c_l X).grad KP and U[KP].grad rho~ are O(r^{2k-1} log r) at infinity, and the cutoff terms have compact
    support;
  - near 0, U[KP] is smooth with linear part c[KP](-x, y). Its contribution to U[KP].grad rho~ is cancelled by
    (c[KP]/3) chi_0 G_bar, as in 6.1.

7.2 Bordered operator.
- Split the strain term as (c[h]/3) G_bar = (c[h]/3) chi_0 G_bar + (c[h]/3)(1 - chi_0) G_bar.
- The near piece is combined with U[h].grad rho~ into the renormalized coupling of 6.1, which maps into Y given (E).
- For h = h_0 + kappa KP with h_0 in Z_cap, set L_ren h_0 := V.grad h_0 - h_0 + [U[h_0] + chi_0 (c[h_0]/3) X].grad rho~.
  Since c[h] = c[h_0] + kappa c[KP] and L = L_fix + (c[.]/3) G_bar,
     L h = L_ren h_0 + kappa (c_l Phi_hat + y_KP) + ((c[h_0] + kappa c[KP])/3)(k Phi_hat + g_far).
- Since Phi_hat is not in Y, L h is in Y if and only if
     kappa (3 c_l + k c[KP]) = -k c[h_0],
  that is, kappa = -k c[h_0]/d with d := 3 c_l + k c[KP] (V025 form).
- Then c[h_0] + kappa c[KP] = 3 c_l c[h_0]/d and
     L h = L_red h_0 := L_ren h_0 + c[h_0] zeta,   zeta := (c_l g_far - k y_KP)/d, which is in Y.

7.3 Consequences.
- Scope of V034: the algebra of 7.2 and the membership of g_far and y_KP in Y are CONFIRMED, conditional on an actual
  operator domain X that embeds continuously in Z_cap and on which L_ren maps X into Y. Z_cap alone controls only c;
  that L_ren maps the domain of S2_L2_THEORY.md section 5 into Y is (E).
- c is bounded on Z_cap (Prop C2), so c[.] zeta is a bounded rank-one operator from Z_cap to Y.
- If L_ren is Fredholm of index 0 from its domain in Z_cap to Y, so is L_red. It is invertible if and only if it is
  injective.
- If L_ren is invertible, L_red is invertible if and only if 1 + c[L_ren^{-1} zeta] != 0. This is the V021 form of the
  rank-one condition.

7.4 Denominator.
- c[KP] = (s_3/pi) int chi_inf(r) r^{k-2} log r dr, with s_3 := int_0^{2pi} sin(3theta) Theta_0 dtheta.
- For chi_inf = 1_{r > R}: int_R^inf r^{k-2} log r dr = R^{k-1}[log R/(1 - k) + 1/(1 - k)^2], which tends to 0.
- Hence |k c[KP]| < 3 c_l, and so d != 0, as soon as
     (k |s_3|/pi) R^{k-1}[log R/(1 - k) + 1/(1 - k)^2] < 3 c_l = 16.726.
- |s_3| <= ||Theta_0||_{L^1} is available from the exact trial. With a smooth cutoff the same bound holds up to the
  transition width.
- d != 0 is therefore an elementary certificate. The compensated column of the numerics team uses the same formula
  for d, with its own cutoff.
- Sharper (THEOREM, V034). From the original modal coefficients, 37.63077494715565 < s_3/pi < 37.63077494715567, so
  s_3 > 0. Since r^{k-2} log r >= 0 for r >= 1, every smooth cutoff 0 <= chi_inf <= 1 supported in r >= 1 gives
  c[KP] >= 0, hence d >= 3 c_l > 0 and the total-strain factor 3 c_l/d lies in (0, 1]. No cutoff-dependent estimate
  is needed. (Even the absolute-value test of the first bullet holds: k|c[KP]| <= 10.02225 < 3 c_l.)

7.5 Log variations. The log variation r^k log r of the exponent change is an explicit coordinate (KP). Without it the
range of L misses Phi_hat whenever c[h_0] != 0, and the problem is not Fredholm in Y. This is the far form of the
normalization obstruction.

## 8. Toward |c[h]| <= C_c ||L h||_Y, and the exact obstruction

8.1 Given a bounded inverse of L_red on Z_cap, |c[h]| <= 0.31210 ||L_red^{-1}|| ||L h||_Y follows at once, with
kappa = -k c[h_0]/d recovered from c[h_0].
- Conversely, with c bounded on Z_cap, the c-estimate follows from the inverse estimate.
- A c-bound does not by itself require an inverse bound. By V035 (Hahn-Banach), |c[h]| <= C ||L h|| on the domain
  holds if and only if c = L^* phi for some phi in the dual of Y with ||phi|| <= C (dual solvability), and this can
  hold when L has a kernel, or when L is injective with dense nonclosed range. The first version said that no route
  avoids an inverse bound; V035 REFUTES that sentence. Direct adjoint solvability for the realization of section 7 is
  OPEN. V035 also gives a conditional approximate-dual absorption criterion. If phi is in Y^* with the defect
  bound ||c - L^* phi||_{X^*} <= delta, and an independent estimate ||h||_X <= A ||L h||_Y + B |c[h]| holds with
  delta B < 1, then |c[h]| <= (||phi|| + delta A)/(1 - delta B) ||L h||_Y. A small adjoint residual alone is not
  enough without such an estimate.
- The frozen route of Corollary C1 uses Theorem O's exact inverse.

8.2 Closed (DERIVED or CONFIRMED):
- the frozen adjoint weight and the local and global frozen moments;
- the explicit frozen constants;
- boundedness of c and continuity of J on Z_cap;
- the near cancellation;
- the strip smallness of the Taylor-subtracted coupling;
- the exact rank-one bordering, with d >= 3 c_l > 0 for every admissible cutoff (V034).

8.3 Missing (status of 03:07Z; items (a) and (c) are superseded by section 10):
- (a) (E2) and (E3) of 6.4: the corner and the strip-exterior interaction, together with (E1) and (E4).
  - With these, L_ren is Fredholm of index 0 on the domain of S2_L2_THEORY.md section 5, by the Theorem R argument
    and given the margin (H_m') of that section.
  - That domain embeds continuously in Z_cap if its radial factor agrees with mu~ for r > 2 and its weight dominates
    the product weight of Z_O for r < 2. The angular factor is at least 1. This embedding is DERIVED.
- (b) Injectivity of L_red and a quantitative inverse bound. Theorem R gives no norm bound, so this needs the
  complement estimate of Avenue IV, or a perturbative argument from a certified finite section.
- (c) The certification of the margins (H_m) and (H_m'), requested from the numerics team for mu~ at 03:07Z (done
  later: V077, raised to at least 5/2 by V086; section 10).

8.4 Obstruction categories (task item 5.5; status of 03:07Z, see section 10 for the later treatment of the velocity
remainders):

| Category | Verdict |
|---|---|
| adjoint weight | not the obstruction: explicit, kappa_0(p) > 0 |
| boundary fluxes | inflow: not the obstruction; outflow: forces a global axis realization, which is available in the frozen case |
| velocity remainders | obstruction (E2), (E3) |
| weighted elliptic bounds | obstruction (E2), (E3) (same estimates) |
| chosen function space | isotropic or radial spaces are obstructed (V010, S7.3), and c is not closable on the radial graph (V032); the anisotropic domain (section 5 weight, Z_cap for c) passes every check made: c bounded, J continuous, x^2 y in, r^k Theta out, residual r^{2k-1} in |
| finite-rank reduction | not the obstruction for the rank-one term (exact elimination, d != 0); the inverse of the reduced operator, with the scalar condition 1 + c[L_ren^{-1} zeta] != 0, is the remaining quantitative question (Avenue IV) |

## 9. Status and submissions

Verifier decisions (V034 and V035, 02:48Z):
- Prop M (2.2, 2.3), the representer formula 3.1 and the frozen constants: CONFIRMED at the detailed domain scope of
  the verifier's proof.
- Corollary C1 arithmetic: CONFIRMED with the upper bounds C_c0 < 0.013958 (a = 7/2, b = 6/5) and C_c0 < 0.017231
  (a = 17/4, b = 0).
- Prop C2: CONFIRMED with C_cap < 0.312093 and C_> < 0.273629; C_cap < 0.359253 at a = 17/4, b = 0.
- Prop B (7.2 to 7.4): CONFIRMED conditional on a domain X embedded in Z_cap with L_ren : X -> Y (7.3), with the
  sharper denominator bound d >= 3 c_l > 0. General invertibility after bordering is OPEN.
- The sentence of 8.1 on c-bounds and inverse bounds: REFUTED and replaced (V035).
- V038 (03:02Z): the scalar normalization has a unique solution ell(h) > 1 with |ell(h) - c_l| <= |c[h]|/3; the
  augmented parametric map has the Prop B system as its derivative; d != 0 alone does not invert L_red (REFUTED as a
  sufficiency claim; the extra condition is 1 + c[L_ren^{-1} zeta] != 0 when L_ren is invertible).
The numerical table 2.4 is evidence only.
Code: artifacts/code/lyapunov/box_moment.py and mu_pwc.py. Data: artifacts/data/lyapunov/mu_pwc.json.

## 10. Status at 12:05Z (2026-10-28T12:05Z, with the V190 amendment of 13:51Z; not the end of the run)

The answers of section 0 stand at their stated scope. Later in the run the rank-one term and the normalization were
resolved structurally, in a form that removes the need for the explicit bound |c[h]| <= C_c ||L h||_Y on the
established route.

- Exact moving-tail elimination of c (THEOREM: the iteration theorem, V062; the uniform inverse theory of the exact
  moving-tail family, V170). The far exponent is a free parameter: rho_ell = rho_0 + chi_inf (r^(1/ell) - r^k) Theta,
  and n(ell) = 3 ell - 1 - c[rho_ell] satisfies n(ell_0) = 0 and n' >= 3 on the parameter interval. For a correction h
  the parameter ell(h) is defined by n(ell(h)) = c[h], so |ell(h) - ell(v)| <= ||c||_(X*) ||h - v||_X / 3. In the
  linearization the strain then enters only as c[f] M(ell). M(ell) itself is not in the Sobolev/jet targets of
  Theorem E (the high and low weighted targets of V190): its cubic coefficient at the origin is 1 (V190), so there it
  must be paired with the cubic column. The finite form is L_ren f + c[f] m(ell),
  with L_ren = L_fix + c[.] H_0 and m(ell) = M(ell) - H_0 a smooth target-valued family: a bounded rank-one
  term inside an operator that is Fredholm of index 0. In those targets norms of the two pieces M and L_fix f cannot
  be taken separately (V190, REFUTED for that separate diagnostic). No inverse estimate for c is needed; invertibility
  of the whole operator reduces to its injectivity. The V190 obstruction is specific to these Sobolev/jet targets: in
  the later Hoelder targets Y, Z and Z_2 of the accompanying S2_CALPHA_THEORY.md, 3.4 (not the Y of 7.1), the full
  moving-tail column M0 is target-valued (Y: V228; Z: V235, for beta > 2k - 1; Z_2: by the mapping theorem of
  V245, confirmed in V254).
- Closed scalar normalization. In the decoupled low family (radial exponents 17/2 inside and 37/20 outside, angular
  exponent a in [18/5, 4]) the jet coordinate J is a closed continuous coordinate of the domain, the axis row is
  Hilbert-Schmidt and the full low block is Fredholm of index 0 (THEOREM, V172). The perturbed and moving-tail
  operators keep these properties with fixed compact estimates (THEOREM, V175).
- Normalization of the profile (Theorem E, CONDITIONAL THEOREM, V178). The iteration works in a fixed chart and gives
  the jet (1 + J(h)) x^2 y. If |J(h)| < 1, then lambda = (1 + J(h))^(1/2) and rho_norm(X) = lambda rho(X/lambda) has
  unit cubic coefficient, the same ell and c, and tail amplitude lambda^(1 - 1/ell). A sufficient test is
  ||J||_(H*) K_H eta_H < 1.
- Q1 at the scope of 12:05Z. The saddle-adapted estimate became a global low realization: transport margin at least 5/2
  for the fixed weight (V086) and at least 1.10534 in the decoupled family (V171), and the maximal-domain transport
  inverse ||T_v^(-1)|| <= 2/m_* = 100000/55267 on the small perturbation ball (V175). Lemma INJ-S (THEOREM, V092)
  reduces injectivity of the low operator to the remainder block S_1 = T_R + C_R and a one-variable system.
- Q2 at the scope of 12:05Z. The nonlocal remainders are not absorbed by smallness. They are handled as compact
  perturbations: Hilbert-Schmidt axis row and a Garding estimate with a fixed compact map (THEOREM, V168, V172, V175).
  Absorption with explicit constants needs the quantitative split of Lemma INJ-Q (CONDITIONAL THEOREM, V102). With the
  present tools that split is estimated at order 1e4 low modes, a planning estimate and not a proved necessary
  dimension.
- The explicit bound |c[h]| <= C_c ||L h||_Y for the full operator is still not obtained (OPEN). Once (I) of Theorem E
  is proved and K_L computed, it follows as |c[h]| <= ||c||_(X*) K_L ||A h||_Y. On the established route it is not
  needed separately.
- Labels. In this file CONFIRMED (Vnnn) is the verifier's verdict, and the statement then carries the label THEOREM.
