# T2_REV_v03: Opus reviews of AT-110 (normalized-output extension), AT-114 (WG-K activation), AT-103, AT-106 and
# AT-107; corrections to T2_REV_v02

Version 1. Owner: the second theory agent (theory agent; Opus reviewer for the theory auditor). Written 2026-11-02T22:57Z. Plain-text mathematics as in
T2_REV_v01. Paths are relative to the combined2 root.
Section 0 corrects T2_REV_v02 after audit_v54 and audit_v55. Sections 1 to 5 were requested by the theory auditor in audit_v48
(header: the normalized C1 example, ell closedness and the growth counterexamples) and audit_v49 (header: the
normalized-output lower extension and the full WG-K activation, including the common-cutoff choice, the actual
matrix and the boundary inverse).

Reviewed files (read-only; SHA256 at the time of review):
- AT-110: theory_audit/research/sharp_tame_lower/PROOF.md, 4415cbac0b2498be2bf361c96ffd112674603986934737ec1cadffa9c37ac732
- AT-114: theory_audit/research/sharp_full_garding/PROOF.md, 894359480752ce338413ca853c006acdf98e9f011bdbc932cfe40e969686ba0b
- AT-112 and AT-113 (read as dependencies of AT-114): theory_audit/research/sharp_tame_upper/PROOF.md,
  0e853c183367fa740af089558dc98c2620b3d89375aa5ac90b24bba4d8ab2ec8; theory_audit/research/uniform_compact_tame_transfer/PROOF.md,
  056e723026bb792fca3a9f7d85f2947d8a51fd8bfb7836b82399fa33c7e1632f
- AT-103: theory_audit/research/coefficient_c1_counterexample/PROOF.md,
  6143e65b2accc9cb2e62467ba0afbab6f6ba23e1b9ac97d06e830bfb8667e00f
- AT-106: theory_audit/research/holder_ball_closure/PROOF.md, 650f2e2e213af9671847fa10b0858b7aa8fb72a993b5cfc7f70d0ace2d132cc4
- AT-107: theory_audit/research/upper_tier_remainder_scope/PROOF.md,
  68270cca10e66634d17084ebe683b78bf32ee1dec955096e7a2b389c29361b7e

No script was executed for this review; every step below was checked by hand.

## Summary

| item | verdict of this review | remarks |
|---|---|---|
| AT-110 normalized-output extension | AGREE | the origin disk of e0 must be chosen inside the complement of supp theta; the energy and output corrections are O(e^L) and O(n^(-q-L)) |
| AT-114 common cutoff, actual matrix, boundary inverse, scalar closure | AGREE | the absorbed constant C_Y is of size B^(2q/(q-2)) and is used only qualitatively; (2) and (6) use the unabsorbed form |
| AT-112, AT-113 as used in AT-114 | AGREE (as dependencies) | the tame term uses N(k) of the full coefficient, through CU |
| AT-103 normalized C1 example | AGREE | C1 at the y axis checked by a difference quotient; non-Lipschitz from an unbounded continuous derivative |
| AT-106 ell closedness, H1 implies H-L, contraction | AGREE | the exterior term converges already by L2 convergence; c_grad = max(1, sigma/2) suffices |
| AT-107 growth scope | AGREE | the common reference ball also fixes the margin b |
| corrections to T2_REV_v02 | R2-1 to R2-4 | resolvent sign; AT-081 normalization slip; origin-loss equality needs kappa_E = kappa_q |

## 0. Corrections to T2_REV_v02 (frozen 2026-11-02T22:49Z, SHA256 5df01d21c0fbfd8fd5cce8c6298ee9cec90bfd753279c5fce4512bb0c3310647)

T2_REV_v02 is not edited. The following corrections replace the cited passages; the theory auditor audit_v54 (AT-127) and
audit_v55 (AT-128) raised them.
- R2-1 (section 5, AT-069 boundary extension). The resolvent identity has the opposite sign:
  A_k(z_n - z) = (a_k - a_(k_n)).grad z_n. The norm estimate and the convergence argument are unchanged (AT-127).
- R2-2 (section 1 and summary, AT-081). The U[v] sign slip is not harmless as written: with the old negative
  potential ell(v) = -1, so the displayed subtraction has ell = 2 ell(f_d), which is generally nonzero, and the
  normalization step fails as written. Reversing the potential (Psi = +x^2 y chi/2) repairs it with all limiting norms
  and constants unchanged. This is AT-127's corrected theorem; I agree with it.
- R2-3 (end of section 3, sharpened origin loss). The asymptotic equality is withdrawn as stated. Let E be the binding
  top eigenspace of N0(0) and kappa_E the normalized supremum with the strain direction e restricted to E. The
  concentration argument gives
  q kappa_E C_sym <= liminf (beta - beta_K)/(R^theta M^eta) <= limsup <= q kappa_q C_sym,
  and equality holds if kappa_E = kappa_q (AT-128). The reason is that the profile must be placed with a direction in
  E: a direction outside E carries a fixed deficit of the background matrix that the concentration does not remove.
  Status: the two-sided bound CLAIMED (AT-128 states it as the content of its complete concentration proof); the
  equality CONDITIONAL on kappa_E = kappa_q. FLOAT evidence: in the kappa table of T2_REV_v02 section 3 the numerical
  maximizer is attained with e = e_x and with e = e_y at the same value, so for E = span(e_y) (origin binding in e_y,
  as in (3) of AT-081) or E = span(e_x) the search gives kappa_E = kappa_q at q = 2.1, 2.4, 2.5, 2.6. This is not a
  proof, because the S1 class is not rotation invariant and the global maximality of the axis point is a FLOAT finding.
- R2-4 (section 7, request to the first theory agent). Use C_norm = kappa_q C_sym and 1/sqrt2 < kappa_q < 1 as CONFIRMED (AT-128);
  the kappa values remain FLOAT; carry the origin-loss statement in the form R2-3.

## 1. AT-110: normalized-output extension

Checked step by step, including the unnormalized part on which it rests.
- Energy identity. a.grad u = W a.grad h + (a.grad log W) u, and Re(a.grad g, g) = -(1/2) int div a |g|^2 = 0, so
  E(k, u) = Re(J^q[W a.grad h], g) on smooth data. Correct.
- Coefficients. U[-Delta psi] = (-psi_xy, psi_xx) gives the displayed a_n; k_n and a_n are supported in supp chi0, away
  from the origin, so ell(k_n) = 0. ||k_n||_2 + ||a_n||_inf = O(n^(-q)), ||Da_n||_inf = O(n^(1-q)). Correct.
- Limits. J^q[W a_n.grad h0] = -V_n + o(1): the leading part is (a_n)_2 h0_y = -n^(-q) chi0 h0_y cos(nx) + O(n^(-q-1)),
  and (2) turns n^(-q) A cos(nx) into A cos(nx) + o(1) after J^q. The term tau W a_n.grad w_n has amplitude O(n^(-2q)) at
  frequencies 0 and 2n (the x derivative of w_n costs n but meets (a_n)_1 = O(n^(-q-1))), so its H^q norm is O(n^(-q)).
  g_n = g0 - tau V_n + o(1), so E -> Re(-V_n, g0 - tau V_n) -> tau D0^2/2 and ||g_n||^2 -> N(h0)^2 + tau^2 D0^2/2.
  In (1) the quadratic coefficient tends to 0 (q > 1), so tau D0^2/2 <= c4 (C0/sqrt2) A(h0) (N(h0)^2 + tau^2 D0^2/2)^(1/2);
  dividing by tau and letting tau -> infinity gives (5). Correct.
- Saturation. On the packets centred at (+-x*, +-2 pi e) with radius e^2, theta = 1 and h0_e,y = cos(y/e) >= cos(e);
  |grad h0_e| <= 1 + C e. Correct.
- e0. psi = (3x^2 y - y^3) eta(|X|^2)/6 is even in x and odd in y, so e0 = -Delta psi is S1, and
  ell(e0) = partial_y psi_xx(0) = 1. For the extension the support of eta must lie in a disk that avoids supp theta (and
  hence every packet); this is possible since x* > 0 is fixed. With that choice the statement is correct.
- ell(h0_e) = O(e^L). ell(f) = -partial_y Q_11 f(0); for f supported away from 0 this is the pairing of f with a kernel
  that is smooth on supp theta. Each integration by parts in y against sin(y/e) gains a factor e. Correct. The same
  argument in x against cos(nx) gives ell(w_n) = O(n^(-q-L)) for fixed e. Correct.
- After both corrections: ell(h_n) = ell(h0tilde_e) - tau(ell(w_n) - ell(w_n) ell(e0)) = 0. The energy changes by the
  terms with tau ell(w_n) e0: W a_n.grad e0 = 0 since supp a_n is disjoint from supp e0, and the change of g_n is
  tau ell(w_n) J^q(W e0) = O(n^(-q-L)) in L^2. So (4) and (5) are unchanged. A(h0tilde_e) = A(h0_e) + O(e^L), and
  (h0tilde_e)_y = (h0_e)_y on the packets, so the saturation still gives c4 >= cos(e)/(1 + C'e + O(e^L)) -> 1.

Verdict: AGREE. The normalized-output version holds for both tame norms.

## 2. AT-114: activation of the low-frequency premise in the WG-K setting

Checked step by step.
- Far-field bound. Since 0 is in Kbar, betaK <= -lim lambda_max B_q(0)(X) as |X| -> infinity. There Sym DV -> cI,
  Kmat -> 0 and V.grad log W -> c sigma, so B_q(0) -> (qc - c - 1 - c sigma) I and
  sigma >= q - 1 - 1/c + betaK/c. This exceeds q - 2 because c > 1 and betaK > 0. Correct. (Compactness of the weighted
  H^q ball in L^2 needs only sigma > 0 and q > 0.)
- Compact family. On the fixed ball the map k -> a_low = U[chi(D/Lambda)k] is continuous from L^2 into every C_b^m
  (Bernstein on the fixed Fourier support), and Kbar is compact in L^2 (compact embedding plus weak closedness of Kbar).
  So {a_low} is compact in C_b^m, each a_low tends to 0 at infinity with its derivatives (it lies in every H^s), and
  the AT-065/069 operators C_(a_low) form an operator-norm compact family. AT-113 (3) then gives the uniform weak bound
  for each fixed Lambda. The contradiction proof in AT-113 needs only that W^(-1) J^(-q) is bounded and injective;
  checked.
- Actual matrix (the point raised by the theory auditor). B_q(k_low) - B_q(k) = -q Sym DU[e] + (U[e].grad log W) I, with operator
  norm at most q ||DU[e]||_inf + ||grad log W||_inf ||U[e]||_inf, and B_q(k) <= -betaK I because k is in Kbar. So
  B_q(k_low) <= -(betaK - epsilon/4) I without asking whether k_low is in Kbar (by CU, N(k_low) <= (1 + C/Lambda) Mbar,
  so in general it is not). Correct.
- Fourier estimates. ||U[e]||_inf <= (2 pi)^(-2) int_(|xi| > Lambda) |ehat| <= C Lambda^(1-q) ||k||_(Hdot^q) and
  ||DU[e]||_inf <= C Lambda^(2-q) ||k||_(Hdot^q) (the second needs q > 2), with ||k||_(Hdot^q) <= c_W Mbar. Correct.
- Common cutoff. (4) holds for every sufficiently large Lambda with a Lambda-dependent constant. Lambda is then raised
  once more so that AT-112 (2) holds with d = min(delta0, epsilon/2) on N(k) <= Mbar, and the low constant is evaluated
  at this final Lambda. The order of choices is consistent: no constant is evaluated before its cutoff is fixed. The
  decomposition Q_k = Q_low + E(e, u) is exact because A_k is affine in k and div U[e] = 0. Adding gives (1) with rate
  betaK - epsilon/2 - d >= betaK - epsilon. Correct.
- Tame term. AT-112 bounds the tame part by (1 + C/Lambda) N(k) ||grad h||_inf G with N(k) of the full coefficient
  (through CU, N(Q_Lambda k) <= (1 + C/Lambda) N(k)), so (1) carries N(k), as stated. Correct.
- Absorption (5). With B = (1 + delta0) Mbar C_grad c_W^(1-theta), GN gives the tame product <= B L^theta E^(1-theta/2).
  The scalar maximum of B Y^p E^(1-p) - d1 E over E is p B^(1/p) [(1-p)/d1]^((1-p)/p) Y; checked. With p = theta/2 =
  (q-2)/(2q) the constant contains B^(2q/(q-2)) (exponent 42 at q = 21/10), so the absorbed inequality is numerically
  useless; it is used only to start the regularity argument, and (2) and (6) are derived from the unabsorbed (1).
  This is the correct order and should be kept in any quantitative version.
- Boundary inverse. Approximation by smooth S1 coefficients rescaled by min(1, Rbar/||k_n||_2, Mbar/N(k_n)) stays in
  Kbar and converges in N; the constants of (1) are uniform on Kbar; the limit argument is the AT-069 one (reviewed in
  T2_REV_v02 section 5). Correct.
- Quadratic step. b x^2 <= D x + Cbar L^2 gives x <= (D + (D^2 + 4 b Cbar L^2)^(1/2))/(2b) <= (D + (b Cbar)^(1/2) L)/b.
  Correct.
- Scalar closure (6). From (2), N(k) <= M, GN and ||z||_2 <= R: x <= a + d2 M x^(1-theta). If x > M then
  1 <= a/x + d2 M x^(-theta) < a/M + d2 M^(1-theta) <= 1 (strict since a > 0 for F nonzero). So x <= M and then
  x <= a + zeta_grad M. Correct. The trial ball K (with ell(k) = 0) lies in Kbar when R <= Rbar and M <= Mbar, and b is
  the margin of Kbar.

Remarks.
- For tables: taking the reference ball equal to the trial ball without the ell constraint (Rbar = R, Mbar = M) is
  allowed. A lower estimate of betaK is then beta - tau(R, M) with the unnormalized GN constants (Kbar has no ell
  constraint), which is what closure_fn_v3 uses.
- The weak constant comes from a compactness contradiction (AT-113 (3)) and is not constructive. An explicit Cbar needs
  a quantitative replacement of (3) for the family C_(a_low), for example a frequency and space splitting of g with
  Bernstein on the low part. This is the route of the k-dependent C_eps_bar note (T2_EXP_v01 section 5).

Verdict: AGREE with (1), (2) and (6) as conditional implications under the retained hypotheses. Common cutoff,
actual-matrix comparison and boundary inverse are correct as written.

## 3. AT-103: small normalized C1 coefficients with non-Lipschitz velocity

Checked step by step.
- Kernel and identity. P = Q_11 - Q_22 has symbol cos(2 phi_xi), homogeneous of degree 0 with zero circular mean; its
  kernel is -cos(2 theta)/(pi |Y|^2) (real part of the Beurling kernel; the sign convention of the Fourier transform
  does not matter since cos is even). Q_11 = (I + P)/2, so partial_y U_2[k] = -Q_11 partial_y k =
  -(partial_y k + P partial_y k)/2. Correct.
- Logarithmic growth. In the middle annulus g(X - Y) = cos(2 theta_Y) + O(r/|Y|) (theta_(-Y) = theta_Y + pi), and
  int K cos(2 theta_Y) over 2r < |Y| < r1/2 equals -(1/pi) pi log(r1/(4r)). The error is O(r int s^(-2) ds) = O(1); the
  inner core is bounded by circular cancellation and |grad g| <= C/r near X; the two transition annuli have finite
  logarithmic width. Correct.
- C1 example. omega' = omega^2/r <= omega/r. On r < r1, |partial_y k0| <= omega(R), and the two terms of partial_x k0
  are bounded by omega(R) |x| int_0^|y| dt/(x^2 + t^2) <= (pi/2) omega(R) and 4 omega(R) int_0^|y| |x| t^2/(x^2 + t^2)^2
  dt <= pi omega(R). So |grad k0| <= C omega(R) -> 0 at the origin, where k0 is differentiable with gradient 0
  (|k0| <= |y| omega(R)). On the y axis away from 0: the difference quotient (1/h) int_0^y [g(h, t) - g(0, t)] dt splits
  into t < h, bounded by 2 omega(2h), and t > h, where g(h, t) - g(0, t) = (h^2/2) partial_xx g(xi, t) by evenness and
  |partial_xx g| <= C omega(t) t^(-2) (omega'' = (2 omega^3 - omega^2)/r^2); splitting int_h^y omega(t) t^(-2) dt at
  t = h^(1/2) bounds this part by C(omega(h^(1/2)) + h^(1/2)). Both tend to 0, so partial_x k0(0, y) = 0 (k0 is even
  in x), and continuity follows from the uniform bound. Correct.
- Divergence. int_(2r)^(r1/2) omega(s) ds/s = log log(e/(2r)) + O(1), and the translated-profile error is
  C r int omega(s) s^(-2) ds = O(1). partial_y k0 - g vanishes on a neighbourhood of supp chi, so its P image is smooth
  near 0. Hence partial_y U_2[k0] = (1/2) log log(e/r) + O(1) is unbounded. Correct.
- Non-Lipschitz. partial_y U_2[k1] is continuous on R^2 minus the translated centres and unbounded near one of them; if
  U[k1] were Lipschitz its distributional derivative would be an L^inf function equal a.e. to this continuous function.
  So U[k1] is not Lipschitz. (The proof says this implicitly.)
- Normalization. ell(e0) = 1 as in section 1; f vanishes near 0, so ell(f) is finite; k1 = f - ell(f) e0 and scaling
  keep C1, compact support, S1 and ell = 0. Correct.

Verdict: AGREE. The stronger obstruction (compact C1, normalized, arbitrarily small A(k)) holds. The Dini remark is
correct: a modulus with finite int_0 omega(s) ds/s keeps DU bounded.

## 4. AT-106: ell closedness, H1 implies H-L, contraction

- ell closedness. ell(k_n) = -(partial_y k_n(0) + P partial_y k_n(0))/2. The inner cancelled integral is at most
  2 [grad k_n]_alpha r^alpha/alpha times the weight conversion, uniformly in n. The outer part, after integration by
  parts, is a boundary integral on |Y| = r plus int_(|Y| > r) (grad K)(Y) k_n(-Y) dY; the boundary term at infinity
  vanishes since |k_n| <= eps and |K| = O(|Y|^(-2)). Remark: the exterior integral converges already because
  1_(|Y| > r) grad K is in L^2 and k_n -> k in L^2; dominated convergence is not needed. Along the Arzela-Ascoli
  subsequence ell(k_n) -> ell(k), and since every ell(k_n) = 0 this is enough. Correct.
- Closedness of H(k) <= eps. Finite tests approaching the three suprema for the limit, then passage to the limit for
  each n; correct.
- H1 implies H-L with (1). With H(k) <= epsL: ||DU[k]||_inf <= eps0 and c_T Lambda(k) ||grad z||_inf <=
  c_T C_CZ C_sigma c_grad H(k) H(z) <= H(z)/(2 C0), so H(z) <= 2 C0 (N_Y(G) + ||z||_2). Correct. Remark: with w =
  <X>^sigma one has |grad w|/w <= sigma/2, so ||grad z||_inf <= max(1, sigma/2) H(z); the value c_grad = max(1, sigma)
  used in the proof is therefore safe, and max(1, sigma/2) already suffices.
- Contraction. A_k(z - z') = -U[k - k'].grad z', ||U[k - k']||_2 <= ||k - k'||_2, so
  ||z - z'||_2 <= c_grad eps ||k - k'||_2/beta0 < ||k - k'||_2. Correct.
- The source-norm counterexample and the 0.999 endpoint example: rechecked (201 against 102; a = 0.9995 lies in
  [0.9995, 1)). Correct.

Verdict: AGREE with both conditional implications and both refutations.

## 5. AT-107: scope of the growth statements

- (1) is equivalent to (2) for R > 0 by direct rearrangement. A strict limsup below a/(b^(1/2) R) gives eventual
  validity because N/(b^(1/2) R M) -> 0; a liminf above it gives eventual failure. The example C(M) = M^2/16 gives
  1 + M/4 <= M/2 iff M >= 4. Correct.
- Cut examples: C_cut = log(e + Lambda) with Lambda = M^p gives (C_cut)^(1/2) = o(M); with Lambda = exp(A/(q-2)) it is
  of order A/(q-2); log log gives logarithmic growth in 1/(q-2). Correct.
- Fixed reference ball. Agree. Remark: the common ball fixes both Cbar and the margin b = betaKbar - epsilon, and
  betaKbar <= betaK for each smaller trial ball, so using one common ball is conservative in both constants.

Verdict: AGREE.

## 6. Requests

- The theory auditor and the first theory agent: apply the corrections R2-1 to R2-4 (section 0) when auditing or citing T2_REV_v02.
- The theory auditor: record sections 1 to 5 as the independent Opus reviews of the AT-110 normalized-output extension, the AT-114
  activation (common cutoff, actual matrix, boundary inverse), AT-103, AT-106 (ell closedness) and AT-107. The two
  small precisions (the e0 support condition in AT-110; c_grad = max(1, sigma/2) in AT-106) do not change any verdict.
