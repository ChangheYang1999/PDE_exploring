# S2_BASIS_CERTIFICATION.md: Avenue IV, finite-basis inverse certification (theory author document)

First version 2026-10-28T03:02Z (theory author), revised 03:03Z. The construction and the run logs are in the numerics team's detailed
document of the same name (the accompanying numerics S2_BASIS_CERTIFICATION.md). This file states what Avenue IV has
established, with the verifier's verdicts, and adds the theory author's analysis of the realization and of the complement.
Labels as in S2_CLOSURE.md: THEOREM (verifier-confirmed, verdict given), DERIVED, CONDITIONAL, NUMERICAL, OPEN, REFUTED.
Background of every rigorous statement: the exactly joined, exactly normalized modal trial rho~ (c_l = 1/k exactly).

## 1. Answers to the Avenue IV questions

| Question | Answer at this version |
|---|---|
| Is the finite basis conforming? | Yes, since the 02:08Z repair: degree-7 splines in t = log r, C^6, joined to the inner and outer power laws by exact rational jet solves; retained test splines (V027 confirms the H^1 test-space interpretation; V020 had REFUTED the earlier snapshot) |
| Is the finite inverse certified? | Not yet. The first exact section S0 (4 angular modes, 169 columns plus TAU, KP compensation) is assembled; its verified sigma_min is PENDING |
| Off-basis residual bounds? | The method is valid (section 4); no bound has been computed. The code defects of V027 and V033 are repaired in the code, and the verifier is re-auditing it |
| Is the complement controlled? | No. In the S0 realization it cannot be (Prop IV.O, section 5). In the realization of Theorem R it reduces to the finite checks of Lemma IV.1 (section 6), which are not done |
| Genuine inverse theorem? | No |

## 2. The earlier finite sections (PROMPT 6.1)

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

## 3. Exact objects and the conforming basis (PROMPT 6.2)

- The trial in ball arithmetic: exact rational B-spline cell polynomials, exact joins, the normalization repair z of
  V005 carried as a ball. Green boundary data A_n, B_n, n = 1, ..., 261, at all 1559 cell boundaries, 320 bits.
  Check: c[rho~] - (3/k - 1) lies in [-1.62e-43, 1.62e-43] by three formulas (certificate C1 of
  S2_NUMERICAL_CERTIFICATES.md), uniform over the z enclosure.
- Exact operator images of x^2 y b(t) cos(2m theta) for exponential-polynomial b. Two cancellations are built in: at
  the origin the strain term cancels the constant of the velocity (image O(r^2) in every mode), and in the far field
  the compensated column phi + dk KP, with dk = -k c[phi]/(3 c_l + k c[KP]), has no e^{(k-3)t} tail. V020 confirms the
  compensation formula; V034 shows d = 3 c_l + k c[KP] >= 3 c_l > 0 for every admissible cutoff.
- Conformity criterion (V014): at a continuous interface the image jumps by (V.n)[d_n h]. Hence H^1-type conformity
  needs the derivative jumps to cancel exactly, and rounded values do not suffice. The present basis has C^6 joins by
  construction, one-sided jets agreeing to 5e-51 (evaluation rounding of exact data).
- J = x^2 y times an exact C^6 cutoff (factor exactly 1 near 0). KP = x^2 y chi (t - t_+) e^{(k-3)(t-t_+)} Theta_0~,
  the log variation of the far exponent. TAU is honestly defined as the truncated product (V027).
- Identity test: on a 20-mode fixture trial, sum_m L(x^2 y a_m cos 2m theta) reproduces
  2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ in all 42 output modes to 1.7e-46. This checks the machinery; it bounds
  nothing.

## 4. The finite matrices, the finite certificate and the off-basis bound (PROMPT 6.3 to 6.5)

4.1 Realization of S0. Domain X: h = x^2 y sum_m b_m(t) cos(2m theta) with
  ||h||_X^2 = sum_m (1 + 4m^2) int (b_m^2 + b_m'^2) W_X dt + (three scalar coordinates J, KP, TAU),
W_X = e^{2|t - t_-|} for t < t_-, 1 on [t_-, t_+], e^{2(3 - gamma)(t - t_+)} for t > t_+, gamma = (3k - 1)/2. Target Y:
f = e^{3t} sum_N G_N(t) sin((2N + 1) theta) with ||f||_Y^2 = sum_N (1 + (2N+1)^2) int (G_N^2 + G_N'^2) W_Y dt, W_Y of
the same form. The test space Y_M (degree-7 splines times sin((2N + 1) theta), N <= 11) lies in Y (V027).

4.2 Finite certificate. sigma_min(Q_M L P_N) >= s holds if K - s^2 G is positive definite, where
K = B^T (Z + Z^T - Z^T G_Y Z) B <= B^T G_Y^{-1} B for any real Z. Positive definiteness is verified by
||L^{-1} M L^{-T} - I||_inf < 1 in ball arithmetic. V020 confirms the matrix identity. Status: PENDING.

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

## 5. Prop IV.O: the S0 realization cannot carry an inverse (DERIVED, submitted)

Proposition IV.O. Let X and Y be the spaces of 4.1 (any radial weights W_X, W_Y that are bounded above and below on
[t_-, t_+]). Then:
(i) L maps X into Y_0 := {f in Y : f(0, y) = 0 for all y != 0}, which is a closed subspace of infinite codimension.
    Hence L : X -> Y is not onto.
(ii) L : X -> Y_0 is not bounded below: there are h_eps in X with ||L h_eps||_Y <= C eps^2 ||h_eps||_X.
So no estimate ||h||_X <= K ||L h||_Y holds on X, and a certified lower bound for sigma_min of a finite section in
this realization cannot be uniform in the angular dimension.

Proof.
(i) Every column (remainder, J, KP and TAU) has the factor x^2 y, and so does rho~. On the y-axis, h = 0 and
grad h = 0, and likewise grad rho~ = 0. The strain term is a multiple of X.grad rho~ = x d_x rho~ + y d_y rho~, which
vanishes at x = 0. Hence L h(0, y) = (V.grad h - h + U[h].grad rho~ + (c[h]/3) X.grad rho~)(0, y) = 0. The trace at
theta = pi/2 is f(0, e^t) e^{-3t} = sum_N (-1)^N G_N(t), and by Cauchy-Schwarz with weights (1 + (2N+1)^2) its
H^1(W_Y dt) norm is bounded by C ||f||_Y. So Y_0, the kernel of a continuous surjection onto an infinite-dimensional
space of axis traces, is closed and of infinite codimension.
(ii) Let beta be smooth with compact support in (t_-, t_+) and phi smooth, even, with support in (-1, 1), and set
b_eps(t, theta) = beta(t) phi((pi/2 - theta)/eps) near theta = pi/2, extended by the parity symmetries, and
h_eps = x^2 y b_eps.
- Domain norm. ||h_eps||_X^2 >= c int int |d_theta b_eps|^2 dtheta dt >= c' eps^{-1}.
- Transport part. (V.grad - 1) h_eps = x^2 y T'b_eps with T'b = V.grad b + b (2 V_1/x + V_2/y - 1). Near the y-axis
  V_theta/r = O(eps) on the support (V_1 is odd in x), so (V_theta/r) d_theta b_eps = O(1) with the same angular
  profile, and T'b_eps is O(1) with derivatives O(eps^{-1}) in theta. On the support cos^2(theta) = O(eps^2).
  So the Y norm of x^2 y T'b_eps / r^3 is O(eps^2 eps^{-1} eps^{1/2}) = O(eps^{3/2}).
- Normalization. |c[h_eps]| <= C ||h_eps||_{L^1} = O(eps^{5/2}), since h_eps is supported in a fixed annulus and
  |x^2| <= eps^2 r^2 there. Fix h_* in X, supported in the same annulus, with c[h_*] = 1, and replace h_eps by
  h_eps - c[h_eps] h_*. This changes both norms by O(eps^{5/2}) and gives c[h_eps] = 0, so the strain term and the KP
  compensation vanish.
- Coupling. ||h_eps||_{H^1} = O(eps^{3/2}), and U is bounded on H^1. Near 0: by parity and div U = 0,
  DU[h](0) is a multiple of c[h] diag(-1, 1), and U_1 (odd in x, even in y) has no quadratic term, so c[h_eps] = 0
  gives U[h_eps] = O(r^3) and U[h_eps].grad rho~ = O(r^5), which is integrable against W_Y. At infinity U[h] = O(r^{-2})
  for compactly supported h, and grad rho~ = O(r^{k-1}), so the coupling is O(r^{k-3}), integrable against
  e^{2(3 - gamma)t}. With these tails the coupling has Y norm O(eps^{3/2}).
Hence ||L h_eps||_Y = O(eps^{3/2}) while ||h_eps||_X >= c eps^{-1/2}. QED.

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

## 6. The complement (PROMPT 6.6): a quantitative injectivity lemma

Lemma IV.1 (DERIVED, submitted). Let H be a Hilbert space and L : D(L) -> H closed and densely defined. Assume:
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
  with a bound in terms of ||grad m||_infinity, which is the mechanism. No explicit delta is available yet (OPEN).
- (A) is a finite computation of the kind the exact pipeline already does: psi_i is a finite spline combination,
  L^* psi_i is explicit (transport adjoint plus the adjoint coupling, whose velocity is again given by Green data), and
  eps_i is an off-basis norm. Note that (A) needs approximate adjoint solutions. The finite-section value sigma_min is
  not what enters.
- Uniformity over the correction ball (S2_CLOSURE.md 3.5(b)): replacing L by A_h changes only the transport, so (G)
  holds with m reduced by the margin perturbation of 3.5(a), and eps_i grows by at most C ||D W[h]||_infinity times a
  weighted H^1 norm of psi_i. The same psi_i serve for all h in the ball.
- For the scalar c alone, V035 gives the analogous dual criterion: an approximate solution of L^* phi = c with
  certified defect gives |c[h]| <= C ||L h|| under an auxiliary estimate (S2_C_FUNCTIONAL.md 8.1).

## 7. Respecting the known obstructions (PROMPT 6.7)

- The domain carries J, KP and TAU as explicit coordinates and excludes the r^k tail, as V006, V012, V025 (N4, N5)
  require. KP is the log variation of the exponent.
- Prop IV.O is a new obstruction of the same kind as N1 to N3: a norm that is stronger near the outgoing y-axis on
  the domain side than on the target side cannot be bounded below. Increasing the basis dimension cannot repair it.
- Raw X3 has no finite density bandwidth, while the exact modal trial does (V014). Every certificate is therefore
  stated for rho~, never for X3.

## 8. What Avenue IV can still deliver in this run

1. The certified sigma_min of S0 (a finite statement) and the margin certificate for mu~, which makes Theorem R
   unconditional for L_fix in L^2(e^{mu~}).
2. The L_fix section in L^2(e^{mu~}), the first finite section in a realization where Lemma IV.1 applies.
3. A first set of approximate adjoint solutions psi_i with certified defects (item (A)); (S) remains analytic work.
A genuine inverse theorem in this avenue needs, in addition, the quantitative split (S) and, for the normalized
operator, the realization (b) of section 5.
