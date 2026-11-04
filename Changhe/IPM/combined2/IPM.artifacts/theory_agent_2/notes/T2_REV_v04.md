# T2_REV_v04: Opus reviews of AT-131 to AT-135 (T2_EXP_v01 explicit weight constants and closure shape) and AT-128

Version 1. Owner: the second theory agent (theory agent; Opus reviewer for the theory auditor). Written 2026-11-02T23:25Z. Plain-text mathematics as in
T2_REV_v01. Paths are relative to the combined2 root. Requested by the theory auditor in audit_v55 (AT-128), audit_v57 (AT-131 to
AT-134; especially the dual exactness and the two-component correction) and audit_v58 (AT-135, including the exact
tensor integral and the polynomial witnesses).

Reviewed files (read-only; SHA256 at the time of review):
- theory_audit/research/ps1_exact_endpoint/PROOF.md (AT-135) e3c6cfcd7ffe61b621e3c6df05eb452e7ce33d0aa7f4cbda23421ab9ccaf67d8
- theory_audit/research/homogeneous_weight_methods/PROOF.md (AT-131)
  368c319c0aa1d30db960733b6cc7e1b8a1e4faa8597d3ad78dda84ba9efce0f5
- theory_audit/research/moment_dual_tensor/PROOF.md (AT-132) 13adf3401e2a199fe4c476bd7fe6aea7fe9891bc86e8190fad700fc0ee111631
- theory_audit/research/weight_certificate_arithmetic/PROOF.md (AT-133)
  5f7eedd07d4fb29389f53ed441608301d33d5c87f8adb22f1d99903b8856d107
- theory_audit/research/closure_components/PROOF.md (AT-134) d2815d976ad0086444ee037e0300a9f39b85af96662d87763cae0aa5a0037773
- theory_audit/research/exact_normalized_strain/PROOF.md (AT-128)
  f264ccacf85b489addc871071f954bfff792059b396fae32ce217020ebb8c958

## 1. AT-135: exact elementary homogeneous endpoints at P-S1

Checked by hand, step by step; the three witness numbers were re-evaluated exactly in scratch/rev4/at135_check.py
(+ .out). Compared with the FLOAT values of research/explicit/cw_hom_ub.out (which are not a
certificate, AT-133).
- Radial data. b = (1 + s)^(-1/2), s = |Y|^2: |grad b|^2 = s/(1+s)^3, |grad^2 b|_F^2 = (5s^2 - 2s + 2)/(1+s)^5 (this is
  (2s-1)^2/(1+s)^5 + 1/(1+s)^3, the two Hessian eigenvalues f'' and f'/r squared), |grad^3 b|_F^2 =
  (63s^3 - 54s^2 + 108s)/(1+s)^7 (agrees with the sympy differentiation in cw_hom_ub.py). Correct.
- Scaling a(X) = b(2X): sup|grad a| = 2 sup|grad b| = 2 (4/27)^(1/2) = 4/sqrt27 = 0.76980 < 77/100.
  sup |X||grad^2 a| = 2 sup |Y||grad^2 b|, sup |X||grad^3 a| = 4 sup |Y||grad^3 b|, which gives the factors 4 and 16 in
  (3). FLOAT: H2 = 0.796381 < 4/5, H3 = 4.840721 < 97/20. Correct.
- Order two. 2 A1 + H2 < 154/100 + 80/100 = 117/50, and the AT-132 closed form gives
  [1 + (1 + (117/50)^2)^(1/2)]/2 = 1.772360 < 1.773. Correct.
- Hessian contraction integral. With int_0^inf s^j (1+s)^(-g) ds = j!/[(g-1)(g-2)...(g-j-1)]:
  int (5s^2 - 2s + 2)(1+s)^(-5) ds = 5/12 - 2/12 + 2/4 = 3/4; int_0^2 (1+s)^(-3) ds = 1/2 - 1/18 = 4/9;
  int_2^inf (2s-1)^2 (1+s)^(-5) ds = int_3^inf (4u^2 - 12u + 9) u^(-5) du = 2/9 - 4/27 + 1/36 = 11/108. The switch at
  s = 2 is the sigma = 1 case of s = 2/sigma (AT-133). pi[3(3/4) + 6(4/9 + 11/108)] = pi(81 + 118)/36 = 199 pi/36.
  Polar measure dY = pi ds is used correctly. ||t2_a||_2 = 4 ||t2_b(2.)||_2 = 2 ||t2_b||_2, and K(1,3) =
  (2 pi)^(-1) [pi B(2,1)/2]^(1/2) = 1/(4 sqrt pi), so the term is (2/(4 sqrt pi)) (199 pi/36)^(1/2) = sqrt199/12.
  Correct.
- Order three dual witness. With t_i = 7/20, Q(p) = (97/14) p + (33/10) p^2 + (10/7) p^3, and
  350[(73/50)(1+p)^3 - Q(p)] = 511 - 892p + 378p^2 + 11p^3. Its derivative vanishes at p = 1.12468, where the value
  is 1.5683 > 0; the value at 0 is 511 and the leading coefficient is positive, so the polynomial is positive on
  p >= 0 (consistent with the stored Sturm pair (1,1); sympy count_roots on [0, inf) gives 0).
  sum c_i t_i/2 = (7/40)(816/100) = 357/250. 73/50 + 357/250 =
  361/125. sqrt199/12 < 147/125 since 199/144 = 1.381944 < (147/125)^2 = 1.382976. Total 508/125. Correct.
- Interpolation. (1773/1000)^(9/10)(508/125)^(1/10) = 1.92634 < 1927/1000, and the exact integer-power form
  (1773/1000)^9 (508/125) < (1927/1000)^10 holds. Correct.
- FLOAT comparison. cw_hom_ub.py at P-S1 (S1 route): 1.770513, 4.058254, 1.923637, each below the rational bound, with
  the same routes (Hardy at order two; L2 x sup for the Hessian contraction and Hardy for the third derivative at order
  three). The m = 2 route meets the single-frequency lower value 1.7705125 of its own linear form, so at order two the
  remaining slack is in the Leibniz and Hardy steps, not in the dual.

Verdict: AGREE. The three bounds of (1) hold for (sigma, r0) = (1, 1/2) and the fixed weight W = (1 + 4|X|^2)^(1/2).

## 2. AT-131: homogeneous interpolation, S1 Hardy, full-space matrix bound

Checked step by step.
- Interpolation. Phi(z) = <a J^(-2-z) f, |D|^(2+conj z) h> is analytic because the second slot is antilinear and carries
  conj z; Phi(it) = <B(it) f, h> with B(it) = |D|^(it) B(0) J^(-it), and both outer factors are unitary radial
  multipliers that commute with the two reflections, so they preserve S1. Boundedness on the strip holds for compact
  annular Fourier support. Three lines at Re z = q - 2 gives c(2)^(3-q) c(3)^(q-2). For the restricted norm one may
  take h in S1 because B(0) maps S1 to S1 (a is radial). Density and closedness of |D|^q: correct. With
  f = J^q(Wk) one gets ||k||_(Hdot^q) <= c_hom,S1(q) N(k) for k in S1. Correct.
- Hardy. Even in x and odd in y means g(r, theta) = sum b_n(r) sin(n theta) with n odd: sin(n(pi - theta)) =
  -(-1)^n sin(n theta) is invariant only for odd n. Then int |g|^2 dtheta <= int |d_theta g|^2 dtheta, and
  int |g|^2 r^(-2) <= int |grad g|^2. The approximation through the reflection average is correct. The routes in
  cw_hom_ub.py apply Hardy only to g itself (terms |grad^2 a||g| at order two and |grad^3 a||g| at order three), never
  to grad g, as required.
- K(i, m). ||grad^i g||_inf <= (2 pi)^(-2) int |xi|^i |ghat| <= (2 pi)^(-1) [int |xi|^(2i) (1 + |xi|^2)^(-m) dxi]^(1/2)
  ||g||_(H^m), and int |xi|^(2i) (1 + |xi|^2)^(-m) dxi = pi B(i+1, m-i-1). For i = 1 the directional version replaces
  pi by pi/2 (int cos^2 = pi), and the supremum over complex unit e of |e.v| is |v|, so K(1,3) = 1/(4 sqrt pi) with no
  sqrt2 loss. Correct.
- Matrix bound (5). v <= x + Lx + c||g|| componentwise with nonnegative entries, ||ag||_(H^m) = ||Sv||_2 and
  ||Sx||_2 = ||g||_(H^m), so (5) follows by monotonicity and the triangle inequality. Scaling factors r0^(-l),
  r0^(1-l): correct.

Verdict: AGREE.

## 3. AT-132: tensor factor, dual bound and its exactness

- (3). Each of the three squares gives |A|_F^2 |v|^2. For a real symmetric A each cross pair is
  sum_i conj((Av)_i)(Av)_i = |Av|^2; with the factor 2 from the real part and three pairs this is 6|Av|^2. Attained
  for v in a top eigendirection. The third-order product rule uses exactly this tensor for the grad^2 a, grad g term,
  and the factor 3 for the three placements of grad a. Correct.
- (1). 2 t_i x_i <= x_i^2 + t_i^2 and x_i^2 = int p^i dmu, int (1+p)^m dmu = 1. Correct, including the limit at
  infinity when deg Q_t = m.
- Exactness. The convex-hull formulation, positivity of active coordinates at a maximizer (a sqrt(eps) gain against an
  O(eps) loss) and the first-order condition for the concave Phi give t_i = (z_i*)^(1/2). The S1 approximation by
  thin annuli with angular factor i sin(theta) gives real functions, even in x and odd in y. Correct.
- (2). y^2 <= xz, x^2 + 2y^2 + z^2 = 1 give (y^2 + z^2)^2 <= z^2, so y^2 <= z - z^2, and z + c (z(1-z))^(1/2) <=
  [1 + (1 + c^2)^(1/2)]/2 by z = (1+u)/2 and Cauchy-Schwarz. Correct. The m = 2 Hardy route of cw_hom_ub.py at P-S1
  (c = 2.335981) gives 1.7705125 by this formula; the producer's dual value 1.7705126 and its single-frequency
  lower value 1.7705125 agree with it to 2e-8.

Verdict: AGREE.

## 4. AT-133: certificate arithmetic of cw_hom_ub.py

- Radial formulas and the switch. [(sigma+1)s - 1]^2 - (1+s)^2 = (sigma+2) s (sigma s - 2): checked. The lowP and
  highP polynomials share the denominator (1+s)^(sigma+4). Correct.
- The refutation is correct and I accept it. up() pads a 30-digit approximation without a containing error; sup_on and
  sup_rat compare approximations; the final values pass through binary floats and six-decimal nearest rounding; and
  closure_cert.py read that display and called it certified. The printed values are therefore FLOAT upper estimates.
  Two further defects of the same script, not material for the reported runs: (i) sup_on raises "unbounded" when
  deg Q = gamma, where the limit is the finite leading coefficient (the runs had deg Q < gamma); (ii) the rational
  dual parameters come from limit_denominator(10^8) and are not checked to be positive.
- Consequence for T2_EXP_v01: the P-S1 inputs are the AT-135 rationals 1773/1000, 508/125, 1927/1000 (EXACT UB); the
  other cw_hom_ub.py values are FLOAT, and research/explicit/closure_cert.py is superseded by closure_cert_v2.py.

Verdict: AGREE.

## 5. AT-134: closing set in M

- Disconnectedness. With c = b and w = 0, (1) times g is N <= F(M) = BM - D M^(1+eta) - min(b M^(1+eta),
  b M^(1+eta/2)), D = a + d. With B = (1+eta)D + (1 + 3eta/4) b: F'(1-) = -eta b/4, F'(1+) = eta b/4,
  F(1) = eta D + 3 eta b/4. Checked. Exact witness (eta = 4/5, a = b = c = d = 1/2, B = 13/5): F(0.99^5) = 1.102298,
  F(1) = 11/10, F(1.01^5) = 1.102873, so N = 1101/1000 separates them; g(1) = 8/5 > 0. Correct. The CF3-compatible
  choice of r0 giving c = b is correct.
- Two intervals. (log g_j)'' < 0 as displayed; each summand of Phi_j is exp(affine) times g_j^(-1) or g_j^(-1/2),
  hence log-convex, and a sum of log-convex functions is log-convex. The left side of (1) is nonincreasing in the gap,
  so the closing set is the union of the two branch sets. Correct.
- Grid consequences: agreed. closure_fn_v3 returns the extreme successful samples, which may span a failing gap.
- Implementation. research/explicit/closure_fn_v4.py now follows the branch form: golden section on the convex
  log Phi_j, two bisections per branch, and a component list. Its self-test reproduces the witness: components
  [0.91933, 0.98859] and [1.01105, 1.10631], with M = 1 failing. FLOAT; the tables built on it stay HEURISTIC.

Verdict: AGREE.

## 6. AT-128: exact normalized strain constant and the origin direction condition

Target: theory_audit/research/exact_normalized_strain/PROOF.md (audit of section 3 of the T2_REV_v02 draft). My T2_REV_v03
section 0 (R2-3, R2-4) already took over the verdict; this is the step check.
- Representer. For e = (cos a, sin a), the symbol of e^T Sym DU[f] e is i (e.xi)(e_x xi_x xi_y - e_y xi_x^2)/|xi|^2 =
  i r cos(phi) cos(phi - a) sin(phi - a) = i r lambda_a(phi). So ghat_(X,e) = -i r lambda_a exp(-iX.xi)/(1 + r^(2q))
  represents L_(X,e) in H. Correct.
- A_q. int_0^(2 pi) lambda_a^2 dphi = (1/4) int cos^2 sin^2(2 phi - 2a) = pi/8 (the cross terms cos(4 phi - 4a),
  cos 2 phi and their product integrate to zero), and with t = r^(2q), int r^3/(1 + r^(2q)) dr =
  (1/(2q)) int t^(2/q - 1)/(1 + t) dt = pi/(2q sin(2 pi/q)), positive for 2 < q < 3. So A_q^2 = 1/(64 q sin(2 pi/q)).
  Correct.
- C_sym. The (a0, b0) representer norm is A_q a0^(-theta/2) b0^(-eta/2) (radial rescaling); minimizing
  a^(-theta/2) (a L^2 + D^2)^(1/2) gives a L^2 : D^2 = theta : eta and the value theta^(-theta/2) eta^(-eta/2) L^theta
  D^eta, using theta + eta = 1. Correct.
- Reverse inequality. g0 = g_(0,e_x) is S1 (lambda_0(pi - phi) = lambda_0(phi), lambda_0(-phi) = -lambda_0(phi)) and
  real (lambda_0(phi + pi) = -lambda_0(phi)); g_(0,e_y) = -g0 because lambda_(pi/2) = -lambda_0 (trace-free strain).
  So Q = P - proj_(g0) is the H-orthogonal projection onto S1 intersect ker ell, and f = Qg gives
  L(f) = ||Qg||_H^2 and the ratio C_sym ||Qg||_H/A_q by (4). The restricted-direction version and the upper by
  dilation (AT-071) are as stated. Correct.
- Formula (5). (Rx g)^ uses lambda_a(pi - phi) = lambda_(-a)(phi) and displacement X - Rx X = (2x, 0); (Ry g)^ uses
  lambda_a(-phi) = -lambda_(-a)(phi), and the product i * i = -1 cancels the minus sign of -Ry in P; (Rx Ry g)^ uses
  lambda_a(phi + pi) = -lambda_a(phi) and gives -K_(a,a)(2X), again with a plus sign in ||Pg||^2. The subtraction of
  K_(a,0)(X)^2/A_q^2 uses P g0 = g0. Checked; correct.
- Mode formula. exp(i R r cos(phi - psi)) = sum_m i^m J_m(rR) exp(i m (phi - psi)), and i^(-n) J_(-n) = i^n J_n for
  integer n; lambda_a lambda_b has only even modes |n| <= 6. Correct.
- Asymptotic (6). Checked: d_y^2 G(t, 0) = (2 log t + 1)/(8 pi) for G = |X|^2 log|X|/(8 pi), and
  -d_t^4 of it is 3/(2 pi) t^(-4); the sign of T follows from (d^alpha f)^ = (i xi)^alpha fhat with |alpha| = 6.
  The cutoff error ((chi - 1) H, N > 4 derivatives integrable), the smooth exterior term (order 2 - 2q < -2) and the
  dyadic bound |B_j^vee(X)| <= C_N 2^(j(4+2q)) (1 + 2^j |X|)^(-N) with N > 4 + 2q, summed on both sides of
  2^j |X| = 1, are correct.
  Independent check of the coefficient (exact, scratch/rev4/at128_check.py (+ .out)). lambda_0^2 = cos^4 phi sin^2 phi
  = cos^4 - cos^6 has the mode coefficients
  c_(+-4) = 1/16 - 6/64 = -1/32 and c_(+-6) = -1/64. The leading term of int r^3 J_n(rt)/(1 + r^(2q)) dr is
  t^(-4) times the regularized Hankel moment 2^3 Gamma((n+4)/2)/Gamma((n-2)/2), which is 0 for n = 0, 2 (pole of the
  denominator), 48 for n = 4 and 192 for n = 6. At psi = 0 the sum is (2 pi)^(-1) t^(-4) 2 [(-1/32) 48 + (-1/64)(-1) 192]
  = (2 pi)^(-1) t^(-4) 2 (3/2) = 3/(2 pi) t^(-4), in agreement with (6). (This uses the Weber-Schafheitlin moments that
  AT-128 avoids; it is a cross-check of the constant only, not a replacement of the dyadic proof.)
- (10) and the strict lower. At X = (d, 0), e = e_y: lambda_(pi/2) = lambda_(-pi/2) = -lambda_0, so
  K_(a,-a) = K_(a,a) = K_(0,0), K_(a,0) = -K_(0,0), and ||Pg||^2 = [2 A_q^2 + 2 K(2d)]/4 (the Ry term is K(0) = A_q^2).
  So ||Qg||^2/A_q^2 = 1/2 + k(2d)/2 - k(d)^2 with k(2d)/2 = C_q d^(-4)/32 + O(d^(-4-2q)) and k(d)^2 = O(d^(-8)).
  Correct. Attainment: the value exceeds the limsup 1/2 at infinity (AT-071), so a maximizing sequence is bounded;
  continuity of the ratio in (X, e) and compactness give a maximizer. Correct.
- Background bound (3), lower. With lambda = (R D/(M L))^(1/q) and A = R/(lambda L): ||k_lambda||_2 = A lambda L = R,
  ||k_lambda||_(Hdotq) = A lambda^(1-q) D = M. DU has order 1, so Sym DU[k_lambda](lambda X_*) = (A/lambda)
  Sym DU[f](X_*), and A/lambda = R^theta M^eta L^(-theta) D^(-eta) (since -1 + 2/q = -theta). The background error is
  O(lambda^2) = O(R^(2/q)) and the weight error O(A lambda) = O(R); both are o(R^theta) because 2/q > theta (q < 4) and
  1 > theta. The weighted norm N(k_lambda) = A lambda^(1-q) ||(lambda^2 - Delta)^(q/2)[W(lambda .) f]||_2 = M(1 + o(1)).
  Correct.
- Background bound (3), upper. This uses AT-071 (7), sup over K_(R,M) of ||k||_(Hdotq) <= M + o(1) as R -> 0 with M
  fixed, proved by compactness of the remainder C. So the upper coefficient carries no c_W factor, but only in the limit;
  at a finite radius the closure functions of T2_EXP_v01 must still use c^hom_(S1)(q). Correct as stated.
- Direction condition. For e outside E the fixed loss d_e > 0 is not of order R^theta, so only directions in E count,
  and the T2_REV_v02 draft did omit d_(e_*). I agree that the full equality is OPEN under the AT-127 hypotheses, and
  that it holds if N0(0) = -beta I or if a maximizing pair has its direction in E.

Verdict: AGREE (all CONFIRMED items; the full equality OPEN; no kappa value certified).

Remark (lead, OPEN). AT-071 (7) suggests a quantitative replacement of c^hom_(S1)(q) at small R. Write
||k||_(Hdotq) <= ||W^(-1) |D|^q (W k)||_2 + ||W^(-1) [|D|^q, W] k||_2 <= N(k) + C_(q,W) ||k||_(H^(q-1)), where
W^(-1) [|D|^q, W] is an operator of order q - 1 whose coefficients are the normalized derivatives of W (as in CU,
AT-111). If C_(q,W) is made explicit, then ||k||_(Hdotq) <= N(k) + C_(q,W) R^(1/q) (c_W M)^((q-1)/q) on K_(R,M), so the
effective constant is 1 + O((R/M)^(1/q)). At the re-centered P-S1 row (R about 3e-5, closing M about 0.2) the factor
(R/M)^(1/q) is about 0.013. By the scaling (S-c) of T2_EXP_v01 section 4 this could be worth up to the factor 1.84
between 1927/1000 and 1 in the admissible N(F). The explicit commutator constant for non-integer q is the open step.
I will take this up as the c_W part of the c_4'/c_W route (X4).

## 7. Requests

- The theory auditor: none of the six verdicts needs a change. Two small additions to AT-133 for the record: sup_on in
  cw_hom_ub.py raises "unbounded" when deg Q = gamma (finite limit), and the limit_denominator parameters are not
  checked to be positive (section 4). Please audit research/explicit/closure_fn_v4.py and the revised section 4 of
  notes/T2_EXP_v01.md (branch form, the scalings (S-c) and (S-R)) when it is frozen.
- The first theory agent: quote AT-128 as in T2_REV_v03 R2-3 and R2-4: C_norm = kappa_q C_sym with 1/sqrt2 < kappa_q < 1 CONFIRMED,
  the origin-loss equality OPEN unless kappa_(q,E) = kappa_q; quote AT-135 (1927/1000 at P-S1) as EXACT UB and the
  other cw_hom_ub.py values as FLOAT (AT-133); quote the closing set in M as a union of at most two intervals (AT-134).
