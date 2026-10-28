# S2_BASIS_CERTIFICATION.md: Avenue IV, finite-basis inverse certification (theory author's document)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T03:02Z (theory author), revised 03:03Z and 03:08Z (two proof repairs in 5(ii) from the verifier's audit note of 03:04Z), 03:11Z (V039 and V040) 04:11Z (S0 certification failure, V054; Theorem C') , 04:47Z (V056: the failure is a precision artifact) 05:00Z (S0 certified as a finite statement by the numerics team) 05:16Z (V066), 05:26Z (margin certificate for mu~ computed once) and 05:35Z (V072) and 05:46Z (feasibility of the split (S): explicit commutator bounds and rank estimates) and 06:00Z (V077, V081 to V083; improved single-team margins), 06:16Z (V086: margins at least 5/2; Lemma INJ-S, DERIVED), 06:40Z (V092 to V096: Lemma INJ-S THEOREM; second-order principal energy; explicit strip constant; revised rank scale) 06:45Z (V097 to V100) and 07:04Z (V101, V102, V105: INJ-Q). Updated 08:05Z (V111: the raw-sine finite-section projection; the angular resolution needed for the strong residual) and 12:05Z (section 9: status at 12:05Z, with V178 and V180) and 12:46Z (section 9: the recomputed c[h] = 0 values and the two-mode sections of S_1) and 13:09Z (section 9: the error model and assembly, V187 to V189, V193; the high-norm enclosure) and 13:52Z (V200: the no-TAU S0 value verified; V202: the exact pure-spline input Gram), and 14:12Z (V210: the high-conforming subspaces of the pure section, section 9; qualification of the C^6 wording in section 3), and 14:20Z (cross-audit of V210: the jet order q = 3 at t_- and t_+ in section 1 and section 3), and 14:34Z (V220: the scope of V210 is exactly the 78 pure columns; the 169-column jet-joined section is separate), and 15:54Z (review corrections V250; V252 integrated: the completed three-mode pure section, section 9) and 16:27Z (V260, V263: the shifted outer columns of a far-junction section) and 16:36Z (V267: the complete input Gram of that section) and 16:48Z (V269: its high intersections, dimensions 32 and 29) and 16:52Z (V275: V269 is a THEOREM) and 16:56Z (V274: task item references) and 16:58Z (V277: S1J1 output, floating) and 17:04Z (V279, V280: S1J1 output scope) and 17:22Z (team message 131 wording; V282, V291: exact strain-zero subspaces of S1J1, input only) and 17:43Z (V300: the strict input-form bounds are stated for nonzero vectors).
The construction and the run logs are in the companion numerical document of the same name among the accompanying
artifacts. This file states what Avenue IV has
established, with the verifier's verdicts, and adds the theory author's analysis of the realization and of the complement.
Labels as in S2_CLOSURE.md: THEOREM (verifier-confirmed, verdict given), DERIVED, CONDITIONAL, NUMERICAL, OPEN, REFUTED.
Background of every rigorous statement: the exactly joined, exactly normalized modal trial rho~ (c_l = 1/k exactly).

## 1. Answers to the Avenue IV questions

The answers below are those of 08:05Z; the answers at 12:05Z, with later updates, are in section 9.

| Question | Answer at this version |
|---|---|
| Is the finite basis conforming? | Yes, since the 02:08Z repair: degree-7 splines in t = log r, C^6 at the interior knots, joined to the inner and outer power laws by exact rational solves of the 3-jet (C^3 at t_- and t_+); retained test splines (V027 confirms the H^1 test-space interpretation; V020 had REFUTED the earlier snapshot) |
| Is the finite inverse certified? | For finite sections only. The L_fix section in the realization of Theorem R has sigma_min >= 0.510914 (one team, 05:42Z; reproduced independently from the exported entries at 384 bits, V081, conditional on the exported balls enclosing the exact pairings). For S0: the exact section S0 (4 angular modes, 169 conforming columns plus TAU, KP compensation, 12 output modes) has the certified lower bound sigma_min >= 4.3337e-07, and sigma_min >= 2.0685e-02 without the TAU column (one team, 04:30Z and 04:33Z; conditional on the exported entry balls enclosing the exact pairings). The verifier has confirmed the whitened Gram (V056) and, independently, the bound with TAU as a conditional matrix certificate (V066, exact dyadic s = 4093149700530291/2^73, conditional on the exported entry enclosures); the bound without TAU is not yet reproduced at this version (it was reproduced later, V200, with the same condition). The first attempt failed at 03:59Z because the Gram midpoints were rounded to binary64 (V054, V056). By Prop IV.O (THEOREM, V039) these numbers do not bound any continuum inverse |
| Off-basis residual bounds? | The method is valid (section 4); no bound has been computed. The code defects of V027 and V033 are repaired in the code, and the verifier is re-auditing it |
| Is the complement controlled? | No. In the S0 realization it cannot be (Prop IV.O, THEOREM, V039). In the realization of Theorem R, and in the jet realization of Theorem C' (Fredholm of index 0 for the modal background under (A) and (M); V047 with V049 to V053), it reduces to the checks of Lemma IV.1 (THEOREM as a conditional statement, V040): a quantitative finite-rank split of the compact part and certified approximate adjoint solutions. Neither is done; the compact parts of V049 to V052 are qualitative |
| Genuine inverse theorem? | No |

## 2. The earlier finite sections (task item 6.1)

- The construction of the earlier study was recovered from the case 1 code, and the production section
  (M = 16, stride 16, Mout = 40, four collocation points per cell) was regenerated in floating point. Smallest singular
  values: 0.41312, 0.52004, 0.54650, 0.65491, 0.68781 (H^1q rows, C^1 joins) and 0.16978, 0.20276, 0.21306 (L^2 rows,
  C^0 joins). These match the archived values to the printed digits. So the saved computation is reproducible
  (NUMERICAL).
- These numbers are not continuum bounds (V014, V015):
  - the spline columns jump at internal piece endpoints (1e-22 to 1e-14), so they are not in H^1;
  - the archived TAU column omits the nonzero mode-260 coefficient, so it is not the full Theta_0 cos(2 theta) tail
    direction (V015, REFUTED as a definition);
  - the matrix does include the strain term c[h] X.grad rho/3, despite the "unnormalized" label (V015);
  - the Gram uses finite radial endpoints without a half-line remainder, and the collocation rows carry no measure.
  A finite-rank approximate inverse alone has defect at least one on an infinite-dimensional space (V014).

## 3. Exact objects and the conforming basis (task item 6.2)

- The trial in ball arithmetic: exact rational B-spline cell polynomials, exact joins, the normalization repair z of
  V005 carried as a ball. Green boundary data A_n, B_n, n = 1, ..., 261, at all 1559 cell boundaries, 320 bits.
  Check: c[rho~] - (3/k - 1) lies in [-1.62e-43, 1.62e-43] by three formulas (certificate C1 of
  S2_NUMERICAL_CERTIFICATES.md), uniform over the z enclosure.
- Exact operator images of x^2 y b(t) cos(2m theta) for exponential-polynomial b. Two cancellations are built in: at
  the origin the strain term cancels the constant of the velocity (image O(r^2) in every mode), and in the far field
  the compensated column phi + dk KP, with dk = -k c[phi]/(3 c_l + k c[KP]), has no e^{(k-3)t} tail. V020 confirms the
  compensation formula; V034 shows d = 3 c_l + k c[KP] >= 3 c_l > 0 for every admissible cutoff.
- Conformity criterion (V014): at a continuous interface the image jumps by (V.n)[d_n h]. Hence H^1-type conformity
  needs the derivative jumps to cancel exactly, and rounded values do not suffice. The present basis is C^6 at the interior
  coarse knots by construction. At t_- and t_+ the spline columns are joined to the power-law columns by exact solves
  of the q-jet with q = 3, so they are C^3 there (J is the exception: C^6 at t_-); the one-sided jets agree to 5e-51
  (evaluation rounding of exact data). This suffices for the H^1-type conformity of V014, which needs C^1. The
  zero-extended coarse splines of the later pure spline section (section 9) are C^(min(i, 33 - i) - 1) at the ends:
  C^3, C^4, C^5 for i = 4, 5, 6 and for i = 29, 28, 27 (V210 and its cross-audit).
- J = x^2 y times an exact C^6 cutoff (factor exactly 1 near 0). KP = x^2 y chi (t - t_+) e^{(k-3)(t-t_+)} Theta_0~,
  the log variation of the far exponent. TAU is honestly defined as the truncated product (V027).
- Identity test: on a 20-mode fixture trial, sum_m L(x^2 y a_m cos 2m theta) reproduces
  2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ in all 42 output modes to 1.7e-46. This checks the machinery; it bounds
  nothing.

## 4. The finite matrices, the finite certificate and the off-basis bound (task item 6.3 to 6.5)

4.1 Realization of S0. Domain X: h = x^2 y sum_m b_m(t) cos(2m theta) with
  ||h||_X^2 = sum_m (1 + 4m^2) int (b_m^2 + b_m'^2) W_X dt + (three scalar coordinates J, KP, TAU),
W_X = e^{2|t - t_-|} for t < t_-, 1 on [t_-, t_+], e^{2(3 - gamma)(t - t_+)} for t > t_+, gamma = (3k - 1)/2. Target Y:
f = e^{3t} sum_N G_N(t) sin((2N + 1) theta) with ||f||_Y^2 = sum_N (1 + (2N+1)^2) int (G_N^2 + G_N'^2) W_Y dt, W_Y of
the same form. The test space Y_M (degree-7 splines times sin((2N + 1) theta), N <= 11) lies in Y (V027).

4.2 Finite certificate. sigma_min(Q_M L P_N) >= s holds if K - s^2 G is positive definite, where
K = B^T (Z + Z^T - Z^T G_Y Z) B <= B^T G_Y^{-1} B for any real Z. Positive definiteness is verified by
||L^{-1} M L^{-T} - I||_inf < 1 in ball arithmetic. V020 confirms the matrix identity. Status for S0: the first attempt FAILED at 03:59Z (domain Gram not certified positive definite;
V054); after whitening, sigma_min >= 4.3337e-07 with TAU and sigma_min >= 2.0685e-02 without TAU (CERTIFIED by one team; both bounds VERIFIED as conditional matrix certificates, with TAU V066, without TAU V200, each
conditional on the exported entries enclosing the exact pairings; the
weakest direction with TAU is the TAU column, whose compensated image lies beyond the last test knot t = 16.14; without TAU it
is the far power columns of modes 0 and 1).
V056 (independent reconstruction of the exported 170 x 170 Gram, scalar and dk terms included): float Cholesky fails,
but a 100-digit Cholesky fed the exact Arb midpoint mantissas and exponents succeeds, and the 384-bit interval
congruence gives ||T^T G T - I||_inf < 1.754e-27 with every triangular diagonal interval excluding 0. So the Gram is
positive definite, conditional on the exported entry enclosures; this certifies neither the entries nor a singular value.

4.3 Off-basis bound. With R a fixed matrix such that E = R^{-T} G R^{-1} - I has ||E||_inf < 1,
  ||(I - Q_M) L P_N||_{X_N -> Y} <= |t^|_2/(1 - ||E||_inf)^{1/2},   t^_i = sum_j |(R^{-1})_{ji}| t_j,
where t_j bounds ||(I - Q_M) L u_j||_Y. A naive bound with absolute coordinates is invalid (2 x 2 counterexample).
Per column, t_j^2 = S_j - r_j^T G_Y^{-1} r_j + E_j^>, with S_j the exact norm of the retained modes, the subtraction
bounded from below by the same Z device, and E_j^> the dropped modes N > 11. The trial has exactly 260 angular modes,
so every image has finite angular bandwidth and nothing is truncated.
Defects found and repaired in the code (verdicts CONFIRMED for the repairs, REFUTED for the earlier versions):
- V027: KP and TAU used the wrong density lookup (259 modes lost); nearest-float conversion of upper bounds.
- V033: a zero-straddling interval product before a square root (NaN); row maxima chosen by nearest-float ties; tiny
  positive endpoints discarded; Bt used where the plain B formula was required, which dropped a C(-x, y).grad rho term;
  an obsolete input file.
- Still open at 02:49Z (verifier): one remaining discard of small positive endpoints in offbasis.py, and an
  operation-count proof for the float inflation in the tail bound.
Status: no off-basis bound has been computed.

## 5. Prop IV.O: the S0 realization cannot carry an inverse (THEOREM, V039, for the corrected proof below and the maximal S0 domain)

Proposition IV.O. Let X and Y be the spaces of 4.1 (any radial weights W_X, W_Y that are bounded above and below on
[t_-, t_+]), and let L : D_max subset X -> Y with the maximal domain D_max = {h in X : L h in Y distributionally}.
Then:
(i) L maps D_max into Y_0 := {f in Y : f(0, y) = 0 for all y != 0}, which is a closed subspace of infinite codimension.
    Hence L : D_max -> Y is not onto.
(ii) L : D_max -> Y_0 is not bounded below: there are h_eps in D_max with ||L h_eps||_Y <= C eps^2 ||h_eps||_X.
So no estimate ||h||_X <= K ||L h||_Y holds on D_max, and a certified lower bound for sigma_min of a finite section in
this realization cannot be uniform in the angular dimension. (L is a first-order transport operator; the statement
does not assert that it maps all of X into Y. The axis value in (i) is the weak axis trace of L h for h in D_max,
V039.)

Proof.
(i) Every column (remainder, J, KP and TAU) has the factor x^2 y, and so does rho~. On the y-axis, h = 0 and
grad h = 0, and likewise grad rho~ = 0. The strain term is a multiple of X.grad rho~ = x d_x rho~ + y d_y rho~, which
vanishes at x = 0. Hence L h(0, y) = (V.grad h - h + U[h].grad rho~ + (c[h]/3) X.grad rho~)(0, y) = 0. The trace at
theta = pi/2 is f(0, e^t) e^{-3t} = sum_N (-1)^N G_N(t), and by Cauchy-Schwarz with weights (1 + (2N+1)^2) its
H^1(W_Y dt) norm is bounded by C ||f||_Y. So Y_0, the kernel of a continuous surjection onto an infinite-dimensional
space of axis traces, is closed and of infinite codimension.
(ii) Let eta_0 be smooth with compact support in (t_-, t_+), put beta(t) := e^{-2t} eta_0'(t), so that beta has compact
support and int e^{2t} beta dt = 0, and let phi be smooth, even, with support in (-1, 1). Set
b_eps(t, theta) = beta(t) phi((pi/2 - theta)/eps) near theta = pi/2, extended by the parity symmetries, and
h_eps = x^2 y b_eps.
- Domain norm. ||h_eps||_X^2 >= c int int |d_theta b_eps|^2 dtheta dt >= c' eps^{-1}.
- Transport part. (V.grad - 1) h_eps = x^2 y T'b_eps with T'b = V.grad b + b (2 V_1/x + V_2/y - 1). Near the y-axis
  V_theta/r = O(eps) on the support (V_1 is odd in x), so (V_theta/r) d_theta b_eps = O(1) with the same angular
  profile, and T'b_eps is O(1) with derivatives O(eps^{-1}) in theta. On the support cos^2(theta) = O(eps^2).
  So the Y norm of x^2 y T'b_eps / r^3 is O(eps^2 eps^{-1} eps^{1/2}) = O(eps^{3/2}).
- Normalization. h_eps vanishes near 0, so c[h_eps] = (1/pi) int sin(3 theta) r^{-3} h_eps dX. In polar coordinates
  (h_eps = r^3 cos^2(theta) sin(theta) b_eps, dX = r^2 dt dtheta) this factors as
  (1/pi) (int e^{2t} beta dt) (int sin(3 theta) cos^2(theta) sin(theta) phi((pi/2 - theta)/eps) dtheta) = 0. So c[h_eps] = 0 exactly, and the strain term and the KP compensation vanish. (The first version subtracted
  c[h_eps] h_* for a fixed h_* with c[h_*] = 1. That does not control the Y norm, since L h_* has a forbidden far tail;
  verifier's audit note of 03:04Z.)
- Coupling. ||h_eps||_{H^1} = O(eps^{3/2}), and U is bounded on H^1. The target norm of S0 contains the mixed derivative
  d_t d_theta. Use the generators Dil = X.grad and Omega = d_theta: Dil commutes with the homogeneous Riesz multipliers
  of U, and [Omega, U] is again a bounded multiplier of order zero, so the mixed norms of U[h_eps] are bounded by those of
  h_eps, which are O(eps^{3/2}) (one theta derivative costs eps^{-1}, the factor x^2 gives eps^2 and the support eps^{1/2}).
  Near 0: by parity and div U = 0,
  DU[h](0) is a multiple of c[h] diag(-1, 1), and U_1 (odd in x, even in y) has no quadratic term, so c[h_eps] = 0
  gives U[h_eps] = O(r^3) and U[h_eps].grad rho~ = O(r^5), which is integrable against W_Y. At infinity U[h] = O(r^{-2})
  for compactly supported h, and grad rho~ = O(r^{k-1}), so the coupling is O(r^{k-3}), integrable against
  e^{2(3 - gamma)t}. With these tails the coupling has Y norm O(eps^{3/2}).
Hence ||L h_eps||_Y = O(eps^{3/2}) while ||h_eps||_X >= c eps^{-1/2}. QED.
Verification (V039, 03:07Z): CONFIRMED for the corrected proof (exact zero-strain radial moment, weak axis trace,
dilation and rotation multiplier identities, both tails) and the exact domain: ||L h_eps||_Y/||h_eps||_X <= C eps^2.
A finite S0 singular value cannot extend to a uniform continuum inverse in these norms.

Remarks.
- The mismatch is the factor cos^2(theta) sin(theta) between the domain variable h/(x^2 y) and the target variable
  f/r^3. The residual F(rho~) and the nonlinear term W[h].grad h also vanish on the y-axis, so Y_0 is the natural
  target. But (ii) shows that Y_0 with the induced norm is still too weak.
- A consistent realization uses the same weight on both sides. Two are available:
  (a) L^2(e^{mu~(log r)}) on both sides, the realization of Theorem R (V023, V031). The numerics team has this section
      written (its section 5). It covers L_fix only, because c is not closable on that graph (V032).
  (b) the theory author's realization: L^2(w_a) on both sides with the y-axis jet and the coordinate J (S2_CLOSURE.md 3.1).
      This carries the normalization (Prop C2, V034), but the columns must be split into their x^2 jet along the
      y-axis and an O(x^4) remainder.
  A factor-to-factor variant (divide every image by x^2 y and use the domain norm for the target) is exact to compute.
  Whether it is bounded below is OPEN. N1 (V025) suggests an angular weight |cos theta|^{-2a'} with a' >= 1/2 on the
  factor for any coercive method.
- This does not affect the validity of the finite certificate of 4.2 as a statement about the matrix. It limits what
  the matrix can mean for the continuum operator.

## 6. The complement (task item 6.6): a quantitative injectivity lemma

Lemma IV.1 (THEOREM as a conditional statement, V040). Let H be a Hilbert space and L : D(L) -> H closed and densely defined. Assume:
(G) m ||g|| <= ||L g|| + ||K g|| for all g in D(L), with K bounded on H and m > 0;
(S) K = K_S + sum_{i=1}^n <., phi_i> e_i with ||K_S|| <= delta, e_1, ..., e_n orthonormal and phi_i in H;
(A) psi_i in D(L^*) with ||L^* psi_i - phi_i|| <= eps_i.
Put Psi = (sum ||psi_i||^2)^{1/2} and eps = (sum eps_i^2)^{1/2}. If delta + eps < m, then
     ||g|| <= (1 + Psi)/(m - delta - eps) ||L g||   for all g in D(L).
If moreover L is Fredholm of index 0, then L : D(L) -> H is bijective and ||L^{-1}|| <= (1 + Psi)/(m - delta - eps).
Proof. ||K g|| <= delta ||g|| + (sum |<g, phi_i>|^2)^{1/2}. For g in D(L) and psi_i in D(L^*),
<g, phi_i> = <L g, psi_i> - <g, L^* psi_i - phi_i>, so |<g, phi_i>| <= ||psi_i|| ||L g|| + eps_i ||g||, and by
Minkowski's inequality in l^2 the vector of these numbers has norm at most Psi ||L g|| + eps ||g||. Insert this into
(G) and absorb (delta + eps) ||g||. Bijectivity follows from injectivity and index 0. QED.

How it applies.
- In L^2(e^{mu~}), Theorem R (V023, V031) gives (G) for L_fix with m = m_*, once the margin (H_m) is certified, and
  L_fix is Fredholm of index 0. The compact K of the verifier's proof is explicit: weighted conjugation of the Riesz
  products and commutators [m, R_j] of the coupling coefficients with the Riesz transforms.
- (S) needs an analytic high-frequency theorem: a quantitative split of these commutators into a part of small norm
  (frequencies above Lambda/|X| relative to the local scale, and the regions near 0 and infinity where grad rho~ is
  small) and a finite-rank part on a bounded log-annulus at low frequency. The commutator [m, R_j] gains one derivative
  with a bound in terms of ||grad m||_infinity, which is the mechanism. That alone does not give delta: the low
  frequencies, both spatial ends, the weight conjugation and every cutoff term must be included (V040). No explicit
  delta is available yet (OPEN).
- (A) is a finite computation of the kind the exact pipeline already does: psi_i is a finite spline combination,
  L^* psi_i is explicit (transport adjoint plus the adjoint coupling, whose velocity is again given by Green data), and
  eps_i is an off-basis norm. Note that (A) needs approximate adjoint solutions. The finite-section value sigma_min is
  not what enters.
- Uniformity over the correction ball (S2_CLOSURE.md 3.5(b); THEOREM as a conditional statement, V040). Let
  H = L^2(w dX) with log w = mu(log r) - 2a log|cos theta|, M = ess sup|mu'|, and A = L + W.grad with W globally
  Lipschitz, W(0) = 0, W_1 odd in x and div W = 2c/3 constant. Suppose m_W ||g|| <= ||A g|| + ||K g|| with the same K.
  For psi_i smooth and supported away from the axes, (A^* - L^*) psi = -W.grad psi - (div W + W.grad log w) psi, and
  with dW = ||D W||_infinity,
     ||(A^* - L^*) psi_i|| <= dW ||r grad psi_i|| + (2|c|/3 + (M + 4a) dW) ||psi_i|| =: p_i.
  Hence ||g|| <= (1 + Psi)/(m_W - delta - eps - p) ||A g||, p = (sum p_i^2)^{1/2}, whenever the denominator is positive.
  The same psi_i serve for every h in the ball. The factor r in ||r grad psi_i|| is needed on the unbounded domain.
  In a jet-plus-remainder space the adjoint formula must also include the jet rows and their couplings (V040).
- For the scalar c alone, V035 gives the analogous dual criterion: an approximate solution of L^* phi = c with
  certified defect gives |c[h]| <= C ||L h|| under an auxiliary estimate (S2_C_FUNCTIONAL.md 8.1).

6.1 Feasibility of the split (S) (DERIVED inequalities; NUMERICAL rank estimates; none is a certificate).
- Realization. The Garding estimate holds for the remainder row in L^2(w_a). For the jet realization Z -> Y it is
  convenient to work with the bounded operator F = L_red T^{-1} : Y -> Y, where T : Z -> Y is the transport
  isomorphism (V046); c T^{-1} is then a bounded functional on Y. The constant m_T of an estimate
  m_T ||g||_Y <= ||F g||_Y + ||K g|| is not m_a: with a coupling bound ||C|| <= b in the remainder norm and m_0 = m_a - eps,
  one admissible choice is m_T = m_0/(m_0 + b) with K = (b/(m_0 + b)) K_G T^{-1}. Then Lemma IV.1 gives
  ||L_red^{-1}||_{Y -> Z} <= ||T^{-1}||_{Y -> Z} (1 + Psi)/(m_T - delta - eps).
- Coordinates. The axis subtraction must be built into the basis before any frequency truncation. A smooth even
  remainder x^p lies locally in L^2(w_a), a = 17/4, iff 2p - 17/2 > -1, that is p > 15/4, so the first admissible power
  is x^4; the individual angular harmonics of cos^4(theta) sin(theta) do not vanish to that order, so an ordinary angular
  truncation of the remainder leaves L^2(w_a). Two options: the cylinder isometry
  (J_w h)(t, theta) = e^{-13t/4 + (29/8) t_+} |cos theta|^{-17/4} h(e^t, theta), t_+ = max(t, 0), with projections
  J_w^{-1} P J_w, or a basis with explicit x^4 factor, whose axis weight becomes |x|^{-1/2}. The kink of mu_a at t = 0
  must be handled as an interface or smoothed with a recertified margin.
- Explicit commutator bound. On a periodic cylinder window of length ell with frequency lattice (2 pi j/ell, n), let Q_Lambda
  keep frequencies |p| >= Lambda and let the multiplier M satisfy |M| <= M_0 and |grad M(p)| <= M_1/|p| for |p| >= Lambda/2.
  With S_1(a) = sum_q |q| |a^(q)|, ||[a, M] Q_Lambda|| <= max(2 M_1, 4 M_0) S_1(a)/Lambda (split |q| <= Lambda/2, mean value
  theorem, and |q| > Lambda/2, then Young's inequality on l^2). For the principal coupling C_pr = sum_ij B_ij S_i S_j with
  B the polar-frame form of [[-g_2, g_1/2], [g_1/2, 0]], g = grad rho~, S_j = p_j/|p|, and b_eta = (sqrt(|g|^2 + eta^2) - g_2)/2
  (so 0 <= b_eta - b_+ <= eta/2), for v = Q_Lambda v:
     Re <C_pr v, v> <= int b_+ |v|^2 + [eta/2 + (4/Lambda)(sum_ij S_1(B_ij) + 2 S_1(b_eta))] ||v||^2.
  The difference between the exact Mellin multipliers of U and their principal part is explicit: with the stream
  function convention, U maps r^lambda e^{i n theta} to combinations of e^{i(n +- 2) theta} with coefficients
  (lambda - n)/(lambda + n + 2) and (lambda + n)/(lambda - n + 2), and on the Mellin line sigma, for Lambda > |sigma + 2|,
  ||(U_sigma - U_pr) Q_Lambda|| <= max(|sigma + 1|, 1)/(Lambda - |sigma + 2|) for the vector error (the parallelogram
  identity for the two components removes the factor sqrt(2) of the consultation's version). The radial isometry of
  w_a gives sigma = 13/4 near 0 and sigma = -3/8 at infinity. These bounds were proposed in an external consultation.
  The commutator bound and the principal Garding inequality on a regular periodic cylinder are THEOREMS (V082; the
  consultation's sharper commutator display needs a plus sign between its low- and high-frequency terms; the display
  above has it). The velocity formulas and the Mellin bound are THEOREMS for the homogeneous Mellin family on a regular
  cylinder (V083). Weight conjugation (singular in theta), localization, periodization, the Taylor-subtracted axis terms,
  output tails and the jet row are not covered by them (OPEN, V082, V083), and a raw periodic rank count is not a
  conforming IPM section (V082).
- Rank. On a window of length ell, the parity class (sine modes n = 1, 3, 5, ...) has about ell Lambda^2/8 real modes with
  |p| <= Lambda; for a local cutoff Lambda(t, theta) the count is about (1/(16 pi)) int Lambda^2 dt dtheta over the full
  circle. Grid evaluation from the theory author's field (artifacts code injrank/s1_estimate.py and injrank/local_rank.py,
  NUMERICAL): sum_ij S_1(B_ij) + 2 S_1(b_eta) = 1.65e3 (eta = 0.1, window t in [-3, 11] or [-2, 9.5]); the coupling
  coefficients are significant (|g| > 0.3) only for t in [-0.66, 9.06]; sup |grad_(t,theta) B| = 139.7 at t = 4.0.
  Allotting a quarter of the margin m to the frequency error:
  | cutoff | m = 0.966 (certified) | m = 3 |
  |---|---|---|
  | global, from the l^1 commutator bound above | Lambda about 2.7e4, rank about 1e9 | rank about 1e8 |
  | global, from the pointwise derivative scale 4 sup abs(grad B)/m | Lambda 578, rank 4.8e5 | rank 5.0e4 |
  | local, 4 abs(grad B)(t, theta)/m | rank 1.2e4 | rank 1.2e3 |
  | local, with the local grid margin of w_a | rank about 150 (local margin >= 3.09 on the grid) | |
  These are scale estimates, not bounds: the local counts ignore localization and uncertainty-principle constants.
  The margin has since been raised: both global margins are at least 5/2 (THEOREM, V086, the verifier's independent
  refinement; the numerics team's own values are inf m_a >= 2.500023 for w_a and inf m >= 2.471224 for mu~, one team).
  With the inverse-square scaling of the count, the local column at m = 5/2 is about 1.7e3.
  Second-order revision (V094 to V096). The principal real energy error on |p| >= Lambda is
  eta/2 + [S2mat(B) + S2(b_eta)]/(2 Lambda^2), with S2 the second Fourier moments (THEOREM on a regular periodic
  cylinder, V096: sym C_pr = sum S_i B_ij S_j + (1/2) sum [S_i, [S_j, B_ij]], and the comparison with b_eta is a double
  commutator up to the zero mode; S2(a) <= C_L D4(a) with C_L^2 <= 1 + pi/2 + 3L/4). The near-strip error is A_ax s with
  A_ax = sqrt(W_max)[39 M_20 + (25 s_0/2) M_21 + (39 s_0^2/6) M_40 + (25 s_0^3/24) M_41] (THEOREM with stated
  coefficient bounds, V095 with the sharpened universal constants of V099). For the full regular Mellin velocity the
  error gains G_0 E_0 + 6 K G_1/(Lambda - 2 - |sigma + 2|)^2 and stays of second order (V098), and the paired weight
  conjugation is Hilbert-Schmidt with an explicit bound on a compact regular patch (V097). The certificate itself is
  INJ-Q (CONDITIONAL THEOREM, V102): the projection blocks S_F = P S + S P - P S P are kept in full, the columns need
  not be orthonormal (Gram bounds e, p, d by certified positive-definiteness tests), and ||S_1^{-1}||_R <=
  (1 + e p)/(5/2 - eps - delta_F - e d); localization is exact for the transport energy and costs a paired double
  commutator in the coupling (V101); the trace functionals and the radial lift have closed majorants (V105). The projection, Hilbert-Schmidt, triangular conversion and bordering algebra of the
  finite-rank construction is CONFIRMED (V094). Grid values (NUMERICAL; accompanying code injrank/rank2.py,
  s2_estimate.py, s2_eta_scan.py, s2_local.py, s2_noaxis.py), window t in [-3, 11], eta = 0.1:
  | quantity or cutoff rule | principal budget E = 1 | E = 3/2 |
  |---|---|---|
  | sum_ij S2(B_ij); S2(b_eta) | 2.15e4; 3.46e4 (2.1e4 at eta = 1) | same |
  | global second-order rule Lambda^2 = [S2mat + S2(b_eta)]/[2(E - eta/2)] | Lambda 172, 5.2e4 modes per parity class | Lambda 139, 3.4e4 |
  | the same with unit radial cells (localization errors not included) | 2.8e4 | 1.8e4 |
  | the same with the vertical-axis strip removed by a smooth cutoff of half-width 0.3 | 1.9e4 | 1.3e4 |
  | first-order global rule with the same budget (for comparison) | about 4.7e6 | |
  | local proxy, Lambda^2 = 2(abs(D^2 B) + abs(D^2 b_eta))/m, m = 5/2 | about 130 | |
  The moments are dominated by an angular layer at the vertical axis for t in [3, 8] (d_theta^2 B about 250 to 350 near
  theta = pi/2), inside the singular strip of w_a, where the strip estimate replaces Fourier counting. Conclusion
  (estimates for the chosen proposed method, from the uncertified moment values and the incomplete localization of the
  table; not a proved necessary dimension): with the rigorous tools now available, a certified split by this method is
  estimated to need of order 1e4 low modes, beyond the computing limits of this work; the local proxy (about 1e2)
  indicates what phase-space localized error bounds could achieve. The estimates suggest that the global commutator
  route is out of reach for this method, and that for this method a certificate appears plausible only with
  phase-space localized cutoffs, local margins, and a certified box margin close to its grid value. Compressing only the
  significant positive part of the compact energy defect, S <= (P S P)_+ + eta' I when ||S - P S P|| <= eta', can reduce
  the number of adjoint witnesses below the representation dimension.
- Homotopy and Schur tests (THEOREM as conditional lemmas, V082). Let A : H -> H be a bounded Fredholm operator
  of index zero on a Hilbert space H, P an orthogonal projection of finite rank, Q = I - P, and
  A = [[P A P, P A Q], [Q A P, Q A Q]]. Assume that the complement D = Q A Q : QH -> QH is bijective with
  ||D^{-1}|| <= 1/d (d > 0), ||P A Q|| <= b, ||Q A P|| <= c and ||P A P p|| >= a ||p|| for every p in PH. If
  s = a - b c/d > 0, then A is invertible and, with p_0 = (1 + (b/d)^2)^{1/2}/s,
  ||A^{-1}|| <= (p_0^2 + ((1 + c p_0)/d)^2)^{1/2}. The block bounds alone give injectivity and a lower bound; existence
  uses index zero (alternatively, the finite rank of P together with the bijective D reduces it to the injective
  finite Schur complement on PH).
  Without these hypotheses the conclusion fails: S (+) I on ell^2 (+) R, with S the unilateral shift and P the
  infinite-rank projection onto ell^2, satisfies all the block bounds with a = d = 1, b = c = 0 and is not onto
  (V250). A lower bound on P A P alone is not enough ([[1, 1], [1, 1]]). Index 0 along a homotopy gives no protection against a
  kernel at the endpoint (diag(1 - 2s, 1, 1, ...) is singular at s = 1/2), so a continuation proof needs an inverse
  certificate on every subinterval: ||A_s^{-1}|| <= K_j/(1 - K_j M |s - s_j|) if ||A_s - A_(s_j)|| <= M |s - s_j|.
- Reduction to the remainder block (Lemma INJ-S, THEOREM, V092, with the Hilbert-norm form of its first bound; full
  statement and proof in the accompanying S2_CLOSURE.md 3.5(b)). In Z = E B (+) D_R, Y = E Gamma (+) R write
  L_red(E beta + h_R) = E[(A + Gamma_B) beta + Gamma_R h_R + c[h] zeta_J] + [X beta + S_1 h_R + c[h] zeta_R] with
  S_1 = T_R + C_R : D_R -> R (Theorem C' step 2) and c[h] = c_B beta + c_R h_R. If S_1 is injective, then with
  s = c[h] and h_R = S_1^{-1}(phi_R - X beta - s zeta_R) the equation L_red h = E phi_J + phi_R is equivalent to a
  system M_J for (beta, s) in B x R, with M_J = (A (+) (-1)) + compact, Fredholm of index 0, and ker L_red is in
  bijection with ker M_J. Lemma IV.1 is then needed only for S_1 on the plain space R = L^2(w_a), with (G) given by
  Theorem C' (iii) at margin 5/2 - eps and no jet rows in the adjoint; this removes the gap noted after Lemma IV.1
  (the jet-row adjoint). The remaining one-variable system needs explicit tail bounds of Gamma_R S_1^{-1} X,
  Gamma_R S_1^{-1} zeta_R and c_R S_1^{-1} (OPEN). A certified L^2 bound k_1 for S_1^{-1} converts to the graph norm by
  s_1 <= (k_1^2 + (1 + ||C_R|| k_1)^2)^{1/2}, and ||c_R|| < 0.20757 (V092, V093).

## 7. Respecting the known obstructions (task item 6.7)

- The domain carries J, KP and TAU as explicit coordinates and excludes the r^k tail, as V006, V012, V025 (N4, N5)
  require. KP is the log variation of the exponent.
- Prop IV.O is a new obstruction of the same kind as N1 to N3: a norm that is stronger near the outgoing y-axis on
  the domain side than on the target side cannot be bounded below. Increasing the basis dimension cannot repair it.
- Raw X3 has no finite density bandwidth, while the exact modal trial does (V014). Every certificate is therefore
  stated for rho~, never for X3.
- Strong-space sections need a conforming angular projection (V111). The projection used by the floating strong-space
  sections (raw sine truncation, extraction of the axis jet, Euclidean least-squares division by cos^4) is not
  contractive in Y: its amplification exceeds 5037.58 at cutoff 19 (5037.63 with the false jet), attained near the
  input cos^4(theta) sin(37 theta) (REFUTED as a contraction, V111). The repair of the cos^4 division by the exact
  quotient (the DKB form) is CONFIRMED. A certified strong-space section therefore needs either a proved factor for its
  projection or a projection that is conforming for the angular norm of V100.
- Angular resolution (NUMERICAL, theory author, once). The strong residual of rho~ lies in a layer at the vertical axis
  (94 to 99.7 percent of the remainder energy within 0.01 rad for 4 <= log r <= 10), its angular spectrum is nearly flat up
  to mode about 160, and truncation at 60 or 120 modes changes the energy by orders of magnitude. A section with 19
  angular modes cannot represent this layer, so its residual columns do not approximate the strong residual.

## 8. What Avenue IV can still deliver in this run

1. The certified sigma_min of S0 (done by one team and, with TAU, reproduced by the verifier, V066: >= 4.3337e-07; without TAU >= 2.0685e-02, reproduced in V200; both conditional matrix certificates, valid if the exported entry balls enclose the exact pairings; a finite statement; by V039
   it is not a continuum bound) and the margin certificate for mu~, which makes Theorem R unconditional for L_fix in
   L^2(e^{mu~}) (the independent original-data computation gives m_R >= 1.78605, V077, and m_R >= 5/2 after its
   refinement, V086; the numerics team's own values are m_* >= 1.029821, aggregation verified, V072, and 2.471224
   after refinement, one team).
2. The L_fix section in L^2(e^{mu~}), the first finite section in a realization where Lemma IV.1 applies: computed and
   certified by one team at 05:42Z, sigma_min >= 0.510914 (169 conforming columns, modes 0 to 3, 12 output modes; weakest
   direction the inner power columns at r < 0.0077). A finite statement. V081 reproduces the matrix implication at
   384 bits (exact s = 255457/500000, positivity residual < 4.532e-12), conditional on the exported entries; the entries
   are not regenerated from the profile, and no complement bound is implied.
3. A first set of approximate adjoint solutions psi_i with certified defects (item (A)); (S) remains analytic work.
A genuine inverse theorem in this avenue needs, in addition, the quantitative split (S) and, for the normalized
operator, the realization (b) of section 5.

## 9. Status at 12:05Z (2026-10-28T12:05Z, with later updates as listed in the header)

Answers to the Avenue IV questions at 12:05Z, with the later updates. They replace the table of section 1 where the two differ.

| Question | Answer |
|---|---|
| Is the finite basis conforming? | Yes (section 3, unchanged) |
| Is the finite inverse certified? | Only for finite sections in auxiliary realizations: S0 (V066, V200) and L_fix in L^2(e^{mu~}) (V081). Both are conditional matrix certificates, valid if the exported entry balls enclose the exact pairings, and finite statements. For the remainder block S_1 = T_R + C_R of the low realization used by Theorem E only floating sections exist (NUMERICAL, below). No finite section of the base operator A_0 of Theorem E is certified |
| Off-basis residual bounds? | None computed |
| Is the complement controlled? | Reduced, not controlled. Lemma INJ-S (THEOREM, V092) reduces injectivity of the low operator to injectivity of S_1 and a one-variable system with a compact perturbation, with the moving-tail vector in the bordering. Lemma INJ-Q (CONDITIONAL THEOREM, V102) turns a certified finite-rank split of S_1 with explicit localization errors into ||S_1^{-1}||_R <= (1 + e p)/(5/2 - eps - delta_F - e d). The split is not computed. With the rigorous error tools of this run it is estimated at order 1e4 low modes; this is a planning estimate for the present method, not a proved necessary dimension |
| Does it yield an inverse theorem? | No. Avenue IV does not supply hypothesis (I) of Theorem E (CONDITIONAL THEOREM, V178) in this run |

Floating sections of S_1 (NUMERICAL; R = L^2(w_a) norm on both sides; all 531 output sine modes, exact jet split and
exact cos^4 quotient, so the non-contraction of V111 does not arise).
- First angular remainder mode, 42 columns x^2 y b_i(t)(cos 2 theta + 1): smallest generalized singular values
  4.155, 6.08, 23.3, 51.6, 53.1, ... For the value 4.155 the computed direction has the approximate floating Rayleigh
  value 4.155, and the quoted interval [4.137, 4.174] covers accumulation rounding only (V187; the image division and
  quadrature errors are uncertified), so it is not a rigorous upper bound of the section's smallest value (an exact
  full-image Rayleigh quotient would be one) and it does not bound that value from below; its direction is concentrated in the coordinates of the outer power columns, which live just beyond the outer junction (r about 3400). 6.08 and 23.3 are not resolved (Gram
  condition number 1.5e13). Without the seven nearly dependent directions the values are 10.1, 13.6, 51.0, ...; the
  33 pure spline columns give 50.3, 51.6, ... An exact complete-image section value bounds the infimum over its
  subspace from above (a projected-output singular value would not); these floating values do so only within the
  accumulation-only error model, with the image division error uncertified (V187), and they prove nothing about
  injectivity. It is consistent with the margin 5/2 used by INJ-Q and shows no small value in
  the bulk.
- Accounting. The default assembler summed the final per-worker blocks together with the retained cumulative
  checkpoints, so most cells were counted twice. It is REFUTED as a once-per-cell sum (V180), with exact two-cell
  counterexamples: (G_1, B_1) = (1, 1), (G_2, B_2) = (1, 9) give squared value 5, the duplicated first cell gives
  11/3, and omitting it gives 9. The parts-only assembly of the completed, never resumed run covers every cell
  exactly once (CONFIRMED, V180); the values above come from it. The values 4.44, ... on the subspace c[h] = 0 came
  from the double-counted assembly and are withdrawn; recomputed from the parts-only sum they are 4.456, 6.084, 23.31,
  51.70 (NUMERICAL). A resumed run must combine all disjoint base
  blocks with the final blocks and omit the latest checkpoints (V180).
- First two angular remainder modes (84 columns: the 42 radial functions times p (cos 2 theta + 1) and
  p (cos 4 theta - 1), p = cos^2(theta) sin(theta); complete images; never resumed; each cell counted once)
  (NUMERICAL): smallest values 2.344, 2.921, 3.501, 3.829, 3.910, 4.700, ...; all except 3.501 are below the rounding
  estimate of their computed directions, which are near-null combinations of the outer power columns at the far
  junction. The first-mode sub-block reproduces the values above; the second mode alone gives 3.668, 4.341, 12.44. The
  well-conditioned subspace of the 52 pure spline columns (no inner or outer power law; rounding estimates about 1e-9
  relative) gives 3.456, 4.248, 5.460, 6.942, against 50.3 for the first mode alone and 25.5 for the second mode alone.
  Its weakest vector mixes the two angular modes with comparable weights on the coarse splines centred at r = 18 to 360,
  where the transport margins have their minima. So the coupling of angular modes in the bulk lowers the section value
  from 50 to 3.46; whether it keeps falling as modes are added decides the size of the finite-rank part that a
  certificate of Lemma INJ-S needs. These values are floating observations: within the accumulation-only rounding
  model (V187; image division and quadrature errors uncertified) they approximate upper bounds of infima over
  subspaces, they are not rigorous upper bounds, and they prove nothing about injectivity.
- First three angular remainder modes on the pure spline columns (NUMERICAL, V252; 78 columns, the coarse splines
  i = 4..29 times m = 1, 2, 3, complete images, completed run). Every one of the 1569 cells is counted exactly once,
  and the 1531 retained checkpoint cells are excluded as duplicate prefixes (accounting CONFIRMED, V252). Smallest
  floating generalized singular values 2.7655, 3.2685, 4.3913 (independent assembly by the verifier: 2.765547309,
  3.268491498, 4.391313969); 2.7662 on the floating strain-zero hyperplane c[h] = 0 (defined by the stored binary
  strain row). The sub-block m <= 2 gives 3.4557, 4.2477, 5.4604 and reproduces the two-mode values above; the single
  modes alone give 50.32 (m = 1), 25.47 (m = 2) and 12.11 (m = 3). Against the angular cutoff the section value is
  50.32 (m <= 1), 3.456 (m <= 2) and 2.766 (m <= 3): it decreases with the cutoff and is not converged in m. The 60
  high-graph-conforming columns i = 7..26 (V210) give 2.8648, measured in the LOW norms of this computation; it is
  not a high-norm value. Input side: |v^T (G_float - G_exact) v| < 2.688e-6 v^T G_exact v for every nonzero v, against the
  exact V202 input Gram (directed 640-bit interval comparison, CONFIRMED, V252); this is rigorous on the input side
  only. The output division and quadrature remain uncertified (accumulation-only rounding model, V187), so these
  values are floating observations: no lower bound, no exact operator bound and no certificate follows.
- Error model and assembly (V187 to V189, V193). The input quotients by cos^4(theta) of these runs were formed with a
  padded pseudoinverse instead of the exact integer templates Q_j = 2 (-1)^(m-1-j) (2m - 2j - 1) for the input modes
  (V189: m = 1 gives [2], m = 2 gives [-6, 2], m = 3 gives [10, -6, 2]); this changes the domain Gram by about 1e-7
  relative (9.31e-8 for m = 1, V187). The image quotients go through the same pseudoinverse and their division error
  is not covered by any error model in this run, so "resolved" and "rounding estimate" above refer to accumulation
  rounding only; the rounding-model intervals are REFUTED as total error bounds and CONFIRMED as floating observations
  (V187). The exact image bandwidth is J + M odd sines, 264 to 266 raw slots (V193). The assembler of these runs
  checked the number of cells, not equality of the covered and expected cell sets; that is REFUTED as a generic
  guarantee and CONFIRMED for the actual runs (V188). Runs from now on record the expected cell set at creation and
  assert set equality. The input side is now controlled independently (V202, CONFIRMED): an exact reconstruction of
  the pure-spline input Gram from the original knots (exact rational B-spline polynomials, 512-bit integration with a
  640-bit replay) shows |v^T (G_float - G_exact) v| < 2.37e-6 v^T G_exact v for every nonzero v in the 52-column pure section of
  two modes, covering padding, quadrature, division and accumulation on the input side, and every stored pure-column
  strain coefficient has relative error below 2.71e-16. For the completed 78-column three-mode section the same
  comparison gives the input-form bound 2.688e-6 (V252, item above). Output pairings and division errors on the image side remain uncertified, so the section values
  are still floating.
- High conformity of the pure section (THEOREM, V210). The 78 columns h_(i,m) = r^3 p(theta) b_i(log r) F_m(theta),
  4 <= i <= 29, 1 <= m <= 3, F_m = cos(2 m theta) - (-1)^m, use the 34 clamped degree-7 coarse B-splines extended by
  zero outside [t_-, t_+]. For i = 4..7, b_i vanishes to exact order i at t_-, so its zero extension is C^(i-1) there
  with a nonzero jump of order i; for i = 26..29, b_i vanishes to exact order 33 - i at t_+, so its zero extension is
  C^(32-i) there with a nonzero jump of order 33 - i. Every other b_i vanishes in a neighbourhood of the respective
  endpoint, so its zero extension is smooth there. Every zero extension is C^6 at every interior simple knot (exact check of all
  endpoint jets and 884 interior joins from the original knots, 216 exact polynomial replays). All 78 columns are
  low-conforming, so the low finite-section calculation is unaffected. In the high realization of Theorem E the
  section meets the input space H_full exactly in the span of i = 6..27 (66 columns), because a jump of the q-th
  derivative keeps a function in H^s only for s < q + 1/2 and the zero vertical cofactor trace makes the relevant
  order 25/4 (not the scalar 29/4). It meets the maximal high graph domain of the normalized operator exactly in
  i = 7..26 (60 columns): for i = 6 and 27 the transport image has the fifth-derivative jump q(t_-, theta) G(theta)
  (resp. at t_+), q the radial transport speed, nonzero near the vertical axis since d >= 5.5752, and the bounded
  coupling cannot cancel it. A certificate that involves the high image (output norms, graph-norm singular values)
  must use the 60-column subspace; a pure input Gram in the high input space may use all 66. Independent cross-audit
  (14:18Z, recorded by the verifier as V220): PASS WITH REMARKS, no gap (the jump lemma should be stated for
  piecewise smooth multipliers, and where the proof says C^5 it needs H^6 locally; an explicit Hadamard split of the
  coefficient closes both points). V210 classifies exactly these 78 pure columns and no others. The separate
  169-column jet-joined section has q = 3 endpoint joins, so it is C^3 at t_- and t_+; its high-space status is not
  addressed by V210.
- Shifted outer columns for a far-junction section (THEOREM, V260; independent review recorded as V263). Let
  alpha_i = k - 3 - j_i(1 - k) - 2 l_i be the outer exponents of the trial, (j_i, l_i) = (0,0), (1,0), ..., (5,0),
  (0,1), (1,1), (2,1), (0,2) for i = 0, ..., 9, and t_J = t_+ + 1. For q = 5, ..., 9 let b_q(t) be zero for t < t_J and
  exp(alpha_q(t - t_J)) minus its Lagrange interpolant on the four exponents alpha_1, ..., alpha_4 for t >= t_J, and
  h_q = r^3 p(theta)(cos 2 theta + 1) b_q(log r). The five h_q are linearly independent and exactly C^3 across
  r = exp(t_J), with a nonzero fourth radial derivative jump; they belong to the low input space and to the maximal
  low graph realization of S_1, and their cubic jet at the origin is zero. Writing J_n(d) for the n-th derivative jump
  at t_J of sum d_q b_q, their span O satisfies
    O cap H_full = {J_4 = J_5 = 0} (dimension 3),   O cap D_H(A_0) = {J_4 = J_5 = J_6 = 0} (dimension 2),
  by the same jump criterion as V210 (cofactor order 25/4 on vertical sectors) and the nonzero radial transport speed
  near the vertical axis. So no single column is high-admissible, but the span is not high-inadmissible. The exact
  low input Gram is G_qr = 8 Beta(3/2, 1/4) exp(27 t_J/4) sum_(i,j = 1..9) B_qi B_rj/(-27/4 - alpha_i - alpha_j)
  (B_qq = 1, B_qi = minus the Lagrange weight for i <= 4, zero otherwise; every denominator is positive), with an
  exact rational check and 512/640-bit interval enclosures. This certifies the inputs only: no output Gram, singular
  value or complement inverse follows.
- Complete input Gram of the far-junction section S1J1 (VERIFIED, V267, verifier computation from the original data).
  For all 38 input columns of that section (four inner-extended splines, three extra inner powers, 26 pure splines and
  the five shifted outer columns above) the exact scaled low input Gram is enclosed in 640-bit balls with exact
  dyadic endpoints. It has exact disjoint-support blocks of sizes 33 and 5, agrees after exact scaling with V202 on the
  676 pure entries and with V260 on the outer block, and every stored strain coefficient has relative error below
  2.701e-16 and absolute error below 2.053e-17. Low conformity and positive definiteness are proved analytically. No
  additional high dimension is claimed, and the output values of the section remain floating until their division
  and integration errors are enclosed.
- High intersections of the whole far-junction section S1J1 (THEOREM, V269, verifier proof with exact ranks,
  independent audit recorded as V275). Write the 38 columns as h_i = 2 r^3 cos(theta)^4 sin(theta)
  B_i(log r)/s_i with the radial functions B_i and exact binary scales s_i of V267, and for a coefficient vector d let
  J_(v,n)(d) be the jump of the n-th t-derivative of sum_i d_i B_i/s_i at the join v = t_-, t_+ or t_J = t_+ + 1. Then
    S cap H_full = {J_(v,4) = J_(v,5) = 0 for all three joins} (dimension 32),
    S cap D_H(A_0) = {J_(v,4) = J_(v,5) = J_(v,6) = 0 for all three joins} (dimension 29),
  by the jump criterion of V210 and V260 applied at the three separated joins, with the nonzero radial transport speed
  d(t) >= 5.5752 near the vertical axis at each of them. The jump rows have disjoint column supports and exact rational
  coefficients after scaling, so the ranks 6 and 9 are exact; an independent rational replay rebuilt every row from the
  knots, k and the scales of V267 and reproduced both nullspaces. The whole section has J = 0 and zero vertical cofactor
  trace. These are statements about subspaces, not high-norm estimates: a singular value of a low-norm matrix restricted
  to the 29-dimensional subspace would still use the low norm and an uncertified output matrix.
- Output of the far-junction section S1J1 (NUMERICAL, computed by the numerics team; input comparison V277). The
  completed far-junction section itself (NUMERICAL, floating outputs; complete projected core images of S_1 after the
  exact jet split, not full A_0 images, in the low input and output norms; all 1569 cells counted once; the input form
  is certified against the exact Gram with relative error below 0.000431058, V277, which does not control the output
  uncertainty) has the smallest generalized singular values 4.7481, 15.142, 34.29, 44.21, ..., and about 4.7481 on the
  hyperplane defined by the stored binary strain row (V267 bounds the error of that row; the exact strain-zero
  subspaces of the 38-column span and of its 32- and 29-dimensional high subspaces have dimensions 37, 31 and 28, and
  in the low input metric, within each of these spaces, the exact kernel of the stored binary row lies within relative
  distance 6.244e-16 of the exact kernel of the strain functional: THEOREM, V282, verifier proof, independent audit
  recorded as V291; this is an input statement only, it does not cover the floating basis used for the value, and no
  exact constrained output value follows). The weakest direction is concentrated in the shifted outer power columns
  (-0.79 out9 + 0.56 out5 + 0.25 out8, normalized Gram eigenvalue 9.0e-12); its Rayleigh quotient lies in [3.74, 5.59]
  under the accumulation-only rounding model, which is not a certified enclosure, and 15.1 and 34.3 are not resolved.
  Without the five outer columns the 33 remaining columns give 50.32, 51.58, 53.16 (the 26 pure splines 50.3201).
  Restricted to the exact 32-dimensional high input subspace the value is 5.8703, and to the exact 29-dimensional high
  graph subspace 7.4692 (both floating, from the same S_1 core images in the low norms, not high-norm values). Moving
  the outer attachment from t_+ to t_+ + 1 changes the far value from about 4.16 to about 4.75. These observations
  show only that the small floating values are concentrated in the outer-column coordinates, persist after its
  attachment is moved, and give way to larger values once that subspace is removed; they do not show that the small
  value is spurious (an
  exact two-column example with arbitrarily bad Gram conditioning has a genuine small minimum that disappears after
  deleting a column, V279). Its accuracy and exact operator meaning are unresolved. No output value is certified,
  none is a high-norm value, and no inverse or complement bound follows.

What an inverse theorem along this avenue would still need: (i) rigorous R-norm Grams of the full-mode images
(estimated at about 18 hours on four cores for the 42-column basis, beyond this run); (ii) the split of INJ-Q with
phase-space localized error bounds (the local proxy suggests about 1e2 modes, against about 1e4 with global
commutator bounds); (iii) the explicit tail bounds of the one-variable system of INJ-S; (iv) the conversion to the
graph norm; (v) the actual full normalized bordering (the strain row and the moving-tail vector of INJ-S, not only the
remainder block S_1) and the adjoint hypotheses with their tails (certified approximate adjoint solutions psi_i with
off-basis defects eps_i, Lemma IV.1 (A), and the adjoint-witness Gram bounds of INJ-Q). Only with all of these does (I)
follow and K_L become computable. A high graph norm computed on the 60 pure columns would still be a finite statement,
and neither the certified input Grams (V202, V252) nor the 60-column conformity (V210) proves an image pairing or a
complement bound. Beyond (I), hypothesis (S) of Theorem E also needs K_H, C and a
realistic high residual norm eta_H (in a fixed equivalent norm only the enclosure 3.866e10 < eta_* < 6.321e129 is
certified, V192, V182, and two constant-free necessary tests of (S), V185 and V194, are probably failed by the archived
trial on a knot-scale heuristic; S2_THEORY_18H_REPORT.md 6.5 item 10).
