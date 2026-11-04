# T2_REV_v02: Opus reviews of AT-081, AT-071, AT-088, the AT-080 threshold table and the AT-069 boundary extension; the exact normalized strain constant

Version 1. Owner: the second theory agent (theory agent; Opus reviewer for the theory auditor). Written 2026-11-02T22:49Z. Plain-text mathematics as in
T2_REV_v01. Paths are relative to the combined2 root.

Reviewed files (read-only; SHA256 at the time of review):
- AT-081: theory_audit/research/normalized_strain_lower/PROOF.md, 3a94feac524b24d355f46232923aabeb0094f9a91ab65376b20c2e93a44b6739
- AT-071: theory_audit/research/normalized_sharp_strain/PROOF.md, c42394955ceaaa33008474e33ca77a3365775201339bdf79a2775d0e7322f049
- AT-088: theory_audit/research/ps1_scalar_closure_exclusion/PROOF.md, aba1cb991d55dd7f1ea1e64c7947630f6acc873d1cac3c805e9e1f5ced941e62
- AT-080: theory_audit/research/theory_exchange_v01_audit/PROOF.md, 9557cb93bb13144419369790b9d11210b0e5c313f0c699ec110bec2ab9538ab7,
  and its verification/corrected_thresholds.md, 4feec547ebfaa4ec78aeb6a7bb2f86ff1ef6b5fefa03ea3284501b90ae6e04f1
- AT-069: theory_audit/research/wgk_author_audit/PROOF.md, fadbc6eab998abe54a0808e18e587e2af896101ae31add2a75ba6748f3fc1cd3
- AT-094 (read for its effect on T2_TT_v01 only): theory_audit/research/lk_scoping_audit/PROOF.md,
  4ae2ec88f059bf854ea1fd9f81ab638ec853904d200ca47f602082bd77f7a355

Evidence scripts (FLOAT): theory_agent_2/scratch/rev2/at080_spot.py, hn_test.py, hn_test2.py; theory_agent_2/research/kappa/hn_table.py,
kappa_sup.py, kappa_direct.py, ja_check.py, with .out/.txt files.

## Summary

| item | verdict of this review | remarks |
|---|---|---|
| AT-081 lower C_norm >= C_sym/sqrt(2), origin loss (4), coarse-route exclusion | AGREE | sign slip in U[v] (harmless); the lower is not sharp, see section 3 |
| AT-071 strict normalized upper kappa_q < 1, weighted step (7), verdict on T2-OBS | AGREE | the limsup 1/2 at infinity is attained on both axes |
| AT-088 P-S1 coarse-criterion exclusion | AGREE | every rational step checked; FLOAT q C_sym/sqrt(2) = 0.36511 |
| AT-080 corrected kappa_cap table and the kappa >= 0.156 exclusion | AGREE (table and its use) | four of eight rows recomputed in FLOAT; other parts of AT-080 not reviewed here |
| AT-069 boundary extension and the beta_Kbar correction | AGREE | both accepted for T2_WGK_v01 |
| new: exact normalized constant | T2-NC-EX, CLAIMED: C_norm(q) = kappa_q C_sym exactly, and kappa_q > 1/sqrt(2) | FLOAT kappa_q in section 3 |
| AT-094 against T2_TT_v01 | no T2_TT_v01 statement uses the refuted weighted GN (5) | wording of "fails" in T2_TT_v01 section 4 made criterion-specific (section 6) |

## 1. AT-081 (normalized strain lower and origin loss)

Checked step by step.
- The extremizer. With l_x = xi_x^2 xi_y/|xi|^2, the symbol of d_x U_x is i l_x, and fhat_* = -i l_x/(a + b|xi|^(2q)) is even in
  xi_x, odd in xi_y and satisfies fhat_*(-xi) = conj fhat_*(xi), so f_* is real S1. Its L^2 and Hdot^q norms are finite
  exactly for q > 2 (|fhat_*|^2 r^(2q) ~ r^(2-2q) at infinity, times r dr). Remark: f_* is an exact extremizer, not
  only a near one. With L, H its norms, a L^2 + b H^2 = (2 pi)^(-2) int l_x^2/(a + b r^(2q)) = I(a, b) (2 pi)^(-2), and
  d/da log[I(a', b')(a' L^2 + b' H^2)] vanishes at (a', b') = (a, b), as does the b derivative. The function is
  homogeneous of degree 0 and its minimum over the ratio is unique, so (a, b) is the optimal pair for f_* itself and
  d_x U_x[f_*](0) = C_sym L^theta H^eta exactly. The epsilon in (6) is needed only for the Schwartz cutoff, as stated.
- d_y U_y = -d_x U_x (divergence free), so the sign change in (6) is correct.
- (7): each squared norm is twice the original plus twice the Fourier transform at (2d, 0) of |fhat|^2 or
  |xi|^(2q)|fhat|^2, both in L^1. Riemann-Lebesgue gives the limits sqrt(2) L and sqrt(2) H. Correct.
- (8): U commutes with translations, so d_y U_y[f_d](X_d) = d_y U_y[f](0) + d_y U_y[f](2d, 0). U[f] is Schwartz since
  fhat is smooth with compact support away from 0. By parity d_y U_y[f] is even in x, so
  ell(f_d) = 2 d_y U_y[f](d, 0) -> 0. Correct.
- Sign slip (harmless). With fhat = int exp(-iX.xi) f, the transform of d_x d_y Psi is -xi_x xi_y Psihat and that of
  d_xx Psi is -xi_x^2 Psihat. For v = -Delta Psi, vhat = |xi|^2 Psihat, so U[v] = (-Psi_xy, Psi_xx), as in AT-063 and in
  AT-094's correction of AT-080, not (Psi_xy, -Psi_xx). For Psi = -x^2 y chi/2 one gets ell(v) = Psi_xxy(0) = -1. Then
  h_d = f_d - ell(f_d) v has ell(h_d) = 2 ell(f_d), not 0. Fix: h_d = f_d - [ell(f_d)/ell(v)] v, or Psi = +x^2 y chi/2.
  Every conclusion is unchanged: the correction still has norm |ell(f_d)| ||v|| -> 0 and vanishes near X_d.
- The scaling (9): ||A f(./lambda)||_2 = A lambda L, ||A f(./lambda)||_(Hdot^q) = A lambda^(1-q) H, so A lambda L = R and
  A lambda^(1-q) H = M give lambda^q = RH/(ML). d_y U_y[k_lambda](lambda X_*) = (A/lambda) D_*, and
  A/lambda = R/(lambda^2 L) = R^theta M^eta L^(-theta) H^(-eta). Correct.
- N(k_lambda) = A lambda^(1-q) ||(lambda^2 - Delta)^(q/2) f_lambda||_2 with f_lambda(Y) = W(lambda Y) f(Y): the Fourier
  computation gives exactly this. The derivatives of W(lambda Y) are lambda^|a| (d^a W)(lambda Y), bounded by
  C <Y>^sigma uniformly for lambda <= 1, and tend to those of 1 locally uniformly. So f_lambda -> f in the Schwartz
  topology and N(k_lambda) = M(1 + o(1)). The rescaling by a_lambda is correct.
- (10): the y Rayleigh quotient at Y_lambda; U[k_lambda](Y_lambda) = A U[f](X_*) (degree 0); grad log W(Z) =
  sigma Z/(r0^2 + |Z|^2) = O(lambda) at Y_lambda; so the weight term is O(A lambda) = O(R). The exponents
  2/q - theta = (4 - q)/q and 1 - theta = 2/q are positive. The order of limits (R first, then epsilon) is right.
- The parity remark for N0: for an S1 background the diagonal entries of Sym DV and the scalar V.grad log W are even in
  both coordinates and the off-diagonal entry is odd in both; so N0(0) is diagonal and grad N0(0) = 0. Correct for the
  matrix N_q^(0) of T2_WGK_v01; a background whose frozen matrix has other terms needs the same parity check.
- The consequence paragraph is correct, given that the AT-080 exclusion is monotone in kappa (it is: the right side of
  (2) of AT-080 is multiplied by kappa^(-q/2)). See section 4 for the table check.

Verdict: AGREE with (2), (4), (5) and the exclusion of the global-constant coarse route. The lower coefficient
q C_sym/sqrt(2) in (4) is valid; section 3 shows that the true normalized constant is strictly larger.

## 2. AT-071 (strict normalized upper, refutation of the T2-OBS coefficient)

Checked step by step.
- Representer (4): with the H inner product (2 pi)^(-2) int (1 + r^(2q)) fhat conj(ghat), L_(X,e)(f) =
  (2 pi)^(-2) int i l_e fhat exp(iX.xi), so ghat = -i l_e exp(-iX.xi)/(1 + r^(2q)). g is real since l_e is odd. Its norm
  A_q^2 = (2 pi)^(-2) (pi/8) int r^3/(1 + r^(2q)) dr, independent of (X, e). Correct.
- P = (I + Rx)(I - Ry)/4 is the orthogonal projection onto real S1 (Rx, Ry commute and are unitary for the radial
  weight). ell(f) = -L_(0,e_x)(f) = -<f, g0>_H, and g0 is S1, so Q = P - (projection on g0) is the orthogonal
  projection onto the normalized S1 space. Correct.
- Finite (X, e): Qg = g forces g S1. The x parity relation makes exp(2i X_x xi_x) real on an open set (l_e and l_e(Rx .)
  vanish only on finitely many rays), so X_x = 0; likewise X_y = 0. At X = 0, l_e/r = cos(phi) sin(2 phi - 2 alpha)/2,
  whose two parts have different parities, so sin(2 alpha) = 0 and g = +-g0, which Q annihilates. Correct.
- Infinity: (6) is the expansion of <Pg, g>. The cross term for a reflection S is the Fourier transform at (I - S)X of
  l_e(S xi) l_e(xi)/(1 + r^(2q)), which is L^1 with coefficients polynomial in e, so Riemann-Lebesgue is uniform in e.
  The bound limsup <= 1/2 follows. Correct.
- Remark: the bound 1/2 is attained. At X = (d, 0) and e = e_y, (I - Ry)X = 0 and l_(e_y)(Ry xi) = -l_(e_y)(xi), so
  <g, Ry g>_H = -A_q^2, while the Rx and RxRy terms and <g, g0> tend to zero. Hence ||Qg||^2/A_q^2 -> 1/2. The same
  holds on the y axis with the Rx term. So kappa_q >= 1/sqrt(2) also follows from (5) alone; section 3 shows that the
  supremum is not attained at infinity.
- (a, b) rescaling: the dilation xi = (a/b)^(1/(2q)) eta is unitary between the (a, b) norm and a multiple of the
  H norm, commutes with Rx and Ry, maps representers to representers at the dilated point and g0 to the (a, b)
  representer of ell. So the supremum (5) does not depend on (a, b). Correct.
- (7), the weighted step: J^q k = b_W g + Cg with C = [J^q, b_W] J^(-q). Compactness of C: cutoff approximation of b_W
  in C_b^3 (b_W and its derivatives tend to 0 at infinity), the bound of C_b^3 multipliers on H^s for 0 <= s <= 3, and
  for compactly supported b the kernel bound |bhat(eta)| |eta| <eta>^(q-1) <zeta>^(-1) (Peetre), which is
  Hilbert-Schmidt after an input cutoff and small in norm beyond it. The contradiction argument (k_n -> 0 strongly,
  b_W J^(-q) injective, so g_n tends weakly to 0 and C g_n -> 0) is correct. So sup ||k||_(Hdot^q) <= M + o(1).
- Matrix consequence: Weyl, ||grad log W||_inf = sigma/(2 r0), and the velocity exponent (q - 1)/q - theta = 1/q > 0.
  Correct.

Verdict: AGREE with (1), (2), the refutation of (3), and the confirmation of the order R^theta M^(2/q).

Acceptance for T2_WGK_v01 (frozen; this is the record of the correction). The T2-OBS claim that the four-copy
construction keeps (1 - 2 delta) C_sym is wrong: the four translates are asymptotically orthogonal, both norms grow by
2, and the ratio by 1/2. The best leading coefficient for the normalized ball lies in
[q C_sym/sqrt(2), q kappa_q C_sym], and by section 3 the upper end is the exact value C_norm(q).

## 3. The exact normalized constant [T2-NC-EX, CLAIMED; kappa_q FLOAT]

Proposition NC-EX. For 2 < q < 3, C_norm(q) = kappa_q C_sym, with kappa_q the supremum (5) of AT-071. Moreover
kappa_q > 1/sqrt(2).

Proof of the equality. The upper is AT-071 (1). For the lower fix (X, e) and put f = Q g_(X,e), using the H norm
(a = b = 1). f is real S1 with ell(f) = 0, and f is in L^2 intersect Hdot^q. Then
L_(X,e)(f) = <f, g>_H = ||Qg||_H^2 and ||f||_H = ||Qg||_H. For every a, b > 0 the AT-070 computation gives
A_(a,b) (a L^2 + b H^2)^(1/2) >= C_sym L^theta H^eta (L, H the norms of f; equality at the optimal ratio), where
A_(a,b) is the norm of the unrestricted (a, b) representer. At a = b = 1 this reads C_sym L^theta H^eta <= A_q ||f||_H.
Hence

  ||Sym DU[f]||_(inf,op) / (L^theta H^eta) >= L_(X,e)(f) / (L^theta H^eta) >= C_sym ||Qg||_H^2/(A_q ||Qg||_H)
                                           = C_sym ||Q g_(X,e)||_H / A_q.

Taking the supremum over (X, e) gives C_norm >= kappa_q C_sym. []

Mode formula. Write e = (cos a, sin a), lam_a(phi) = cos(phi) sin(2 phi - 2a)/2 (so l_e = r lam_a), and

  K_(a,b)(Y) = (2 pi)^(-2) int r^2 lam_a(phi) lam_b(phi) exp(i Y.xi)/(1 + r^(2q)) dxi,

which is real and even in Y. Since lam_a(pi - phi) = lam_(-a)(phi), lam_a(-phi) = -lam_(-a)(phi) and
lam_a(phi + pi) = -lam_a(phi), the expansion (6) of AT-071 becomes, for X = (x, y),

  ||Pg||_H^2 = [A_q^2 + K_(a,-a)(2x, 0) + K_(a,-a)(0, 2y) + K_(a,a)(2x, 2y)]/4,   <g, g0>_H = K_(a,0)(x, y),
  rho^2(X, a) = ||Qg||_H^2/A_q^2 = [||Pg||_H^2 - K_(a,0)(X)^2/A_q^2]/A_q^2,   A_q^2 = K_(a,a)(0) = I_3/(32 pi),

with I_3 = int r^3/(1 + r^(2q)) dr = pi/(2q sin(2 pi/q)). With the Fourier modes lam_a lam_b = sum_n c_n e^(i n phi)
(n even, |n| <= 6) and Jacobi-Anger,

  K_(a,b)(Y) = (2 pi)^(-1) sum_n c_n i^n e^(i n psi) H_|n|(|Y|),   H_n(s) = int_0^inf r^3 J_n(r s)/(1 + r^(2q)) dr,

psi the polar angle of Y.

Proof of kappa_q > 1/sqrt(2). On the x axis with e = e_y (a = pi/2), lam_(pi/2) = lam_(-pi/2) = -lam_0, so with
k(t) = K_(0,0)(t, 0)/A_q^2,

  rho^2((d, 0), pi/2) = 1/2 + k(2d)/2 - k(d)^2.

The large-t behaviour of k comes from the singularity of r^2 lam_0^2/(1 + r^(2q)) at xi = 0. Split off
chi(r) r^2 lam_0^2 (chi a smooth cutoff, 1 near 0). The rest is either a smooth symbol (Fourier transform rapidly
decreasing away from 0) or chi r^(2+2q) lam_0^2/(1 + r^(2q)), whose transform is O(t^(-4-2q)). The homogeneous part
r^2 lam_0^2 has transform t^(-4) Omega(psi) away from 0. Here lam_0^2 = cos^4(phi) sin^2(phi) =
(2 + cos 2phi - 2 cos 4phi - cos 6phi)/32, so c_(+-4) = -1/32 and c_(+-6) = -1/64. The modes 0 and +-2 of r^2 e^(i n phi) are polynomials, so their
transforms are supported at 0. For n = 4, 6 the regularized Weber-Schafheitlin value
int_0^inf r^3 J_n(r t) dr = 8 t^(-4) Gamma((n + 4)/2)/Gamma((n - 2)/2) gives 6 and 24. So

  K_(0,0)(t, 0) = (2 pi)^(-1) [2(-1/32)(1)(48) + 2(-1/64)(-1)(192)] t^(-4) (1 + o(1)) = (3/(2 pi)) t^(-4) (1 + o(1)).

Then k(2d)/2 - k(d)^2 = k(d)[1/32 + o(1) - k(d)] > 0 for all large d, since k(d) > 0 and k(d) -> 0. So
rho^2 > 1/2 at some finite X. []

The asymptotic step is the standard expansion of Fourier transforms of functions with a conormal singularity at 0;
it is stated with a proof sketch only, hence CLAIMED. The FLOAT tables below check both the t^(-4) law and the sign.

FLOAT results (research/kappa/kappa_sup_<q>.out and kappa_direct_2.1.out; H_n by mpmath quadosc, checked against panel quadrature, and the
Jacobi-Anger step checked in ja_check.out):

| q | A_q^2 (table; exact formula agrees to 10 digits) | kappa_q (FLOAT) | maximizer X*, e* | rho^2 - 1/2 at X* | K00(t,0) t^4 at t = 16, 20 (limit 3/(2 pi) = 0.47746) |
|---|---|---|---|---|---|
| 2.1 | 0.0499219207 | 0.71395 (direct quadrature; spline search 0.71425) | (about 0.16, 0), e_x or e_y | 0.00973 | 0.47399, 0.47820 |
| 2.4 | 0.0130208333 | 0.70770256 | (5.75533, 0), e_x or e_y | 0.00084292 | 0.47514, 0.47831 |
| 2.5 | 0.0106331351 | 0.70773172 | (5.98229, 0), e_x or e_y | 0.00088419 | 0.47714, 0.47783 |
| 2.6 | 0.0090626000 | 0.70775220 | (6.15471, 0), e_x or e_y | 0.00091318 | 0.48037, 0.47696 |

Remarks on the table.
- For a = 0 and a = pi/2 one has lam_(-a) = lam_a = +-lam_0, so on the x axis e = e_x and e = e_y give the same value
  1/2 + k(2x)/2 - k(x)^2 (the two printed x axis profiles in kappa_sup_<q>.out coincide). The grid search
  (|X_i| <= 15, step 0.05; a in steps of pi/72) and the Nelder-Mead refinement end on the x axis in every case.
- For q = 2.4 to 2.6 the excess over 1/2 is small (about 9e-4) and is attained at distance about 6. The axis profile
  rises to its maximum and then decreases to 1/2, as the t^(-4) tail predicts.
- At q = 2.1 the maximizer moves close to the origin. There k has a cusp, 1 - k(t) of order t^(2q-4), so k(x) falls
  quickly while k(2x)/k(x) stays near one, and 1/2 + k(2x)/2 - k(x)^2 exceeds 1/2 already at x of order 0.1. The cubic
  spline does not resolve the cusp well; the value in the table is the maximum of a direct quadrature scan of the
  x axis (kappa_direct_2.1.out: rho^2 = 0.509731 at x = 0.16 and 0.509696 at x = 0.17). The far local maximum is
  still present (rho^2 = 0.50035 at x = 4).
- HEURISTIC: if k(2x)/k(x) tends to one uniformly near the cusp as q decreases to 2, then sup rho^2 tends to
  1/2 + max_u (u/2 - u^2) = 9/16, so kappa_q would tend to 3/4. This is not checked.
- The q = 2.6 table of H_n stops at s = 39.4 instead of 48: mpmath quadosc slowed to about two minutes per row at
  noise-level values of H_0, H_2 (about 1e-11), and the job was stopped. The spline is extrapolated only where
  |2X| > 39.4, at the corners of the search grid, where |H_n| <= 1e-4 (the t^(-4) law). The maximizer at |X| about 6
  is not affected.
- The table nodes are quadosc values at 15 digits, checked against panel quadrature at q = 2.5 (scratch/rev2/hn_test2.out:
  agreement to about 1e-9 with the panel sum truncated at r = 800); the spline adds an
  interpolation error that matters only near the cusp at q = 2.1. None of the values is certified.

Consequences.
- The best global normalized GN strain constant is C_norm = kappa_q C_sym with kappa_q as tabulated (FLOAT). For the
  coarse scalar route this changes nothing: every kappa >= 0.156 is already excluded (AT-080, AT-088).
- The origin-loss lower (4) of AT-081 uses a profile on the x axis at infinity. Its coefficient q C_sym/sqrt(2) is valid
  but not sharp. Running the same concentration argument with the profile Q g_(X*,e*) at the maximizer gives the lower
  q kappa_q C_sym (1 + o(1)), so (5) of AT-081 becomes an asymptotic equality:
  lim (beta - beta_K)/(R^theta M^eta) = q kappa_q C_sym, for fixed M and an origin-binding background as in (3) of
  AT-081. The profile Q g is not Schwartz, but the concentration step needs only L^2 intersect Hdot^q, a Schwartz
  approximation (Fourier cutoffs, then a fixed ell correction supported away from X*), and continuity of the functional,
  as in AT-081 section 2. CLAIMED.

## 4. AT-088 and the AT-080 table

AT-088, checked step by step.
- sin(pi s) = sin(pi/21) for s = 20/21, sin x < x and pi < 4, so q^2 C_sym^2 = q t^(-t) s^(-s)/(64 sin(pi/21)) >
  21 q/256 = 441/2560, and (q C_sym/sqrt(2))^2 > 441/5120 > 1/16. FLOAT: q C_sym/sqrt(2) = 0.365108 > 1/4.
- (2): M >= N/b > N/beta and a R^theta M^eta < beta give (N/beta)^eta < beta/(a R^theta), and raising to q/2 gives
  N R^((q-2)/2) < beta (beta/a)^(q/2). Correct.
- R > (3/8)/3 = 1/8 since beta0 <= c + 1 < 3; R^(1/20) > 1/2; N > 9: left side > 9/2.
- beta <= c + 1 - q = 0.710319 < 3/4 (FLOAT), a > 1/4, beta/a < 3, and (3/4) 3^(21/20) < (3/4) 3^(3/2) < 9/2. Correct.
Verdict: AGREE. The scope statement (only the named coarse criterion) is correct.

AT-080 table. FLOAT recomputation of T = beta_cap (beta_cap/(q C_sym))^(q/2), P = L R_floor^p, J = P/T and
kappa_cap = J^(-2/q), from the formula (3) and the exact c (scratch/rev2/at080_spot.out):

| (q, sigma, r0) | T | P | kappa_cap (FLOAT) | table upper |
|---|---|---|---|---|
| (13/5, 7/5, 1/4) | 0.11979726 | 96.527507 | 0.0058137763 | 0.005814 |
| (13/5, 7/5, 2) | 0.11979726 | 6.0199543 | 0.049138956 | 0.049139 |
| (12/5, 1, 1/4) | 0.50865763 | 28.948560 | 0.034461340 | 0.034462 |
| (12/5, 1, 2) | 0.50865763 | 4.7334824 | 0.15584899 | 0.155849 |

Every FLOAT value lies just below the published upper, as it should. The derivation of (2) of AT-080 and its
monotonicity in kappa were checked (same algebra as AT-088). Verdict: AGREE with the table and the uniform exclusion
kappa >= 0.156. Not reviewed here: AT-080's jet example, the constants-divergence correction and the other sections.

## 5. AT-069 boundary extension

- Approximation: for k in Kbar with k nonzero, Schwartz S1 k_n -> k in N (hence in L^2, since W >= 1), and the factor
  min(1, Rbar/||k_n||_2, Mbar/N(k_n)) -> 1, so the scaled approximants lie in Kbar and still converge in N. No ell
  constraint is involved in Kbar. Correct.
- Passage to the limit: the constants in (1) are uniform on Kbar, so the approximate inverses z_n satisfy (2) with
  the same constants and are bounded in weighted H^q. z_n -> z in L^2 follows from z_n - z = A_k^(-1)[(a_(k_n) - a_k).grad z_n]
  with ||a_(k_n) - a_k||_inf -> 0 and ||grad z_n||_2 bounded. Weak compactness gives N(z) <= liminf N(z_n), GN on the
  difference gives A(z_n) -> A(z), and the limit of (2) is (2) for z. The quadratic root step is
  b x^2 - (N(G) + c4' N(k) A) x - C ||h||^2 <= 0, which gives (2). Correct.
- The refutation of beta_Kbar <= beta for an arbitrary certified lower beta is correct; the inequality holds for the
  actual gap (k = 0 is in Kbar). T2_WGK_v01 section 1.1 should be read with beta = actual gap there; all later uses
  need only N_q^(0) <= -beta I, as AT-069 says.
Verdict: AGREE.

## 6. AT-094 and T2_TT_v01

AT-094 audits LK_SCOPING_v01, not T2_TT_v01. Two of its points were checked against T2_TT_v01.
- The refuted estimate (5) of AT-094 bounds a weighted C^(1,alpha) norm by an unweighted L^2 factor. T2_TT_v01 does not
  use it. Its tier 1 is the direct constraint H(k) <= eps on the ball. H-L is an a priori inverse estimate with source
  norm N_Y(G), not an interpolation inequality. The N tier uses the unweighted GN for Sym DU and the factor c_W from
  ||k||_(Hdot^q) <= c_W N(k). AT-094's packets have A_k-image sources of size comparable to H(z), so they do not
  contradict H-L.
- Wording. In T2_TT_v01 section 4, "the uncentered 007 problem fails" and "E6a also fails" mean: condition (CF-H)
  cannot hold with the HEURISTIC constants of that table. They are criterion-specific statements about a sufficient
  condition, not statements about the existence of an invariant set. The same applies to "fails" in T2_TT_v01
  section 6 for (NT-L), which is necessary only for the WG-K criterion T2-CF.
- AT-094's remark that a source-only 1/delta coefficient does not by itself fix beta_L when C_L may depend on delta is
  correct. T2_TT_v01 does not assign beta_L; its eps_L sizes are labelled HEURISTIC.

## 7. Requests

- The theory auditor: record sections 1, 2, 4 and 5 as the independent Opus reviews of AT-081, AT-071, AT-088, the AT-080 table and
  the AT-069 extension. Audit Proposition NC-EX (section 3): the equality C_norm = kappa_q C_sym, the asymptotic
  K_(0,0)(t, 0) ~ (3/(2 pi)) t^(-4) and the strict inequality kappa_q > 1/sqrt(2). Also the sharpened origin loss (end of
  section 3).
- The first theory agent: in theory_v02, replace the open "optimal normalized constant" by C_norm = kappa_q C_sym (CLAIMED, FLOAT values
  in section 3). Use the corrected U[v] sign of section 1 in any reproduction of AT-081.
