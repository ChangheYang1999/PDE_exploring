# S2_BASIS_CERTIFICATION.md (Avenue IV, numerics team; updated 2026-10-28T16:05Z, a session; sections 7.7, 7.8 and 8 added in a session)

Status words: CERTIFIED (interval arithmetic with every error enclosed, inputs identified), FLOATING (evidence only), OPEN.
All times are real UTC times from the run log. Background of every rigorous statement: the exactly joined and exactly
normalized modal trial rho~ of Analysis I (exact export verification/data_exact/modal_v2.json.xz, SHA-256 57f67a53...a6, with
the scalar repair z of its modal_repair proof), not X3 itself.

## 1. Recovery of the earlier finite sections (prompt 6.1)

The construction is recorded in team message board (team message 1). The shipped fixture chain and the production section
M16/s16/Mout40 (four collocation points per cell) were regenerated in research_copy/ with the original code:
H1q rows, C^1 joins: smallest singular values 0.41312, 0.52004, 0.54650, 0.65491, 0.68781 (archived 0.4131, 0.5200, 0.5465,
0.6549, 0.6878); L2 rows, C^0 joins: 0.16978, 0.20276, 0.21306 (archived 0.1698, 0.2028, 0.2131). The saved computation is
reproducible (floating point; logs/repro_M16.log, runs in research_copy/analysis1/.../numerics/runs/c2/*repro*).
Known defects of that construction (verified in Analysis I, topics 130-132): the saved spline columns have value jumps of
1e-22 to 1e-14 at internal piece endpoints; the J column x^2 y 1_{r<R0} jumps at R0; the collocation rows carry no measure;
the smallest singular values are not continuum inverse bounds.

## 2. Exact objects (this run)

2.1 The trial in ball arithmetic (work/exact_trial.py). All stored doubles are exact rationals; the B-spline cell polynomials
are computed in exact rational arithmetic (Cox-de Boor with fmpq_poly); the join coefficients Ei, Eo are the exact 6-jet
solutions; A_00 carries the scalar repair z (enclosure from the verified modal_repair proof). Green boundary values A_n(t_i),
B_n(t_i), n = 1..261, at the 1559 cell boundaries by the stable forward and backward recurrences with closed-form moments at
320 bits. CERTIFIED check: c[rho~] - (3/k - 1) lies in [-1.62e-43, 1.62e-43] (three formulas: Green head+middle+tail, the
B_1 route, the cosine-mode identity int r (a_0/4 + a_1/8 - a_2/8 - a_3/8) dr), uniform over the z enclosure; this re-verifies the
exact normalization with code independent of Analysis I.

2.2 Exact operator images (work/opimage.py). For h = x^2 y b(t) cos 2m theta with b an exponential polynomial on each cell,
the image L h = sum_N (Lh)_N sin((2N+1) theta) is computed exactly (ball arithmetic) as exponential polynomials of the
factor modes G_N = e^{-3t} (Lh)_N on every cell: transport part, background velocity acting on h, velocity of h acting on the
background (closed-form Green data of the column), and the strain term (c[h]/3) X.grad rho~. Two exact cancellations are built
in: (i) at the origin the n = 1 velocity constant of h together with the strain term equals c[h] times the image of the local
field (-2x/3, 4y/3), whose constant term vanishes identically in every mode ((-2x/3, 4y/3).grad(x^2 y) = 0, checked in exact
rationals), so G_N = O(r^2) at the origin for every column; (ii) in the far field the compensated column phi + dk KP with
dk = -c[phi] k / (3 c_l + k c[KP]) has no e^{(k-3)t} tail term in its image (c_l k = 1 exactly).
Consistency test (CERTIFIED as an identity check): on the 20-mode fixture trial, sum_m L(a_m) equals
2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ in all 42 output modes at sample points of eight cells, with differences of at most 1.7e-46
(ball radius level at 200 bits; S2_NUMERICAL_CERTIFICATES.md C2, 02:02Z). The first run had found a Green-step error, fixed at 01:31Z.

2.3 Exactly conforming basis (work/basis.py). Per angular mode m: coarse degree-7 B-splines in t on every stride-th trial
boundary (C^6 by construction, exact dyadic knots); the first and last q+1 splines are extended across t_- and t_+ by the
unique combination of q+1 inner powers e^{2jt} (resp. outer power laws e^{alpha_q t}, q = 1..q+1) with the same q-jet (exact
rational Vandermonde solves), the remaining inner powers (j = q+2..7) and outer power laws (q = q+2..9) enter with their q-jets
removed; q = 3. J = x^2 y (1 on t < t_- plus the sum of the first 8 coarse splines) is C^6 at t_- with factor exactly 1 near 0.
TAU = x^2 y chi e^{(k-3)(t-t_+)} Theta_1 and KP = x^2 y chi (t-t_+) e^{(k-3)(t-t_+)} Theta_0~ with the exact C^6 cutoff chi (sum of
the last 10 trial splines, exactly 1 on the last cells). Checked: one-sided jets agree to 5e-51 (evaluation rounding only).

## 3. Norms and the finite matrices (prompt 6.3)

3.1 Spaces. Perturbations h = x^2 y sum_m b_m(t) cos 2m theta (t = log r). Domain X = X_rem (+) R J_ref (+) R KP (+) R TAU (direct sum):
  ||h||_X^2 = sum_m wX_m^2 int_R (b_m^2 + b_m'^2) W_X(t) dt  on the remainder, plus w_J J^2 + w_k dk^2 + w_tau dtau^2 on the three scalar
  coordinates (J_ref = x^2 y times the exact C^6 cutoff of basis.py; KP, TAU as in section 2.3; none of the three has finite remainder
  norm, so the direct sum is a norm). W_X(t) = e^{-2 eps0 (t - t_-)} for t < t_-, 1 on [t_-, t_+], e^{2(3 - gamma)(t - t_+)} for t > t_+,
  with eps0 = 1 (the remainder factor vanishes at least like r in the L^2 sense) and gamma = (3k - 1)/2 (the remainder decays faster than
  r^gamma; the tail r^k is excluded, the outer power laws r^{2k-1} are included); wX_m^2 = (1 + (2m)^2)^{sX}, sX = 1.
  Forcing Y: for g = e^{3t} sum_N G_N(t) sin((2N+1) theta), ||g||_Y^2 = sum_N wY_N^2 int (G_N^2 + G_N'^2) W_Y dt, W_Y of the same form with the
  same parameters, wY_N^2 = (1 + (2N+1)^2)^{sY}, sY = 1. (All parameters are inputs of work/section.py Weights; the theory author may change them.)
  Membership: every compensated column u_j = phi_j + dk_j KP (and TAU + dk KP, J + dk KP) has L u_j in Y: at the origin G_N = O(r^2)
  (exact cancellation (i) of 2.2, second-model referee Claim 2 with the background hypothesis |d^nu(rho~ - x^2 y)| = O(r^{5-|nu|}), satisfied by the trial's
  inner expansion), in the far field by the compensation (ii) (second-model referee Claim 3; logarithmic factors allowed since gamma > 2k - 1), and in between
  by the C^q joins and the C^{2,alpha} regularity of the trial (image in C^{1,alpha}_loc subset H^1_loc).
3.2 Finite spaces. X_N = span of the compensated columns (section S0: 4 angular modes, coarse stride 60: 169 columns incl. J, plus TAU).
  Y_M = span{psi_i(t) sin((2N+1) theta) e^{3t}: N <= Nmax = 11, i = 1..nb-2} with psi_i degree-7 B-splines on the test knots (every 30th
  trial boundary plus the inner/outer sub-cell boundaries t_- - {1/2, 1, 2, 4}, t_+ + {1/2, 1, 2, 4, 8}), clamped at t_- - 4 and t_+ + 8,
  the two end splines removed (so Y_M subset Y; verifier V020). Q_M = Y-orthogonal projection onto Y_M.
3.3 Matrices (exact ball-arithmetic integrals, 256 bits; work/run_section.py): G_rem (remainder Gram, block diagonal over m, with wX_m^2),
  G_test (H^1_W Gram of the test splines; G_Y = blockdiag_N wY_N^2 G_test), B_{(N,i),j} = wY_N^2 <L phi_j, psi_i>_{H1_W} (rows), the same rows
  for KP and TAU, the strains c_j, c_KP, c_TAU. Compensated rows B_c = B + b_KP dk^T, domain Gram G = blockdiag(G_rem, w_J, w_tau) + w_k dk dk^T.
  All entries are stored as exact dyadic balls (matrices_dyadic.json.gz) and as float mid/rad (matrices.npz).
3.4 Certificate (work/certify.py): sigma_min(Q_M L P_N) = lambda_min(B_c^T G_Y^{-1} B_c, G)^{1/2} >= s if K - s^2 G is positive definite, where
  K = B_c^T (Z + Z^T - Z^T G_Y Z) B_c <= B_c^T G_Y^{-1} B_c for any real Z (verified identity, second-model referee Claim A and the verifier); positive
  definiteness of an interval symmetric matrix M is verified by ||L^{-1} M L^{-T} - I||_inf < 1 in ball arithmetic for a floating Cholesky
  factor L (row sums and the square s^2 in ball arithmetic; the certificate is void unless G_test and G are also verified positive definite).
3.5 Results for S0 (CERTIFIED as finite statements; S2_NUMERICAL_CERTIFICATES.md C3, C3b; assembly 02:06Z-03:58Z, 6797 s, 256 bits).
  The raw domain Gram has condition number 1.74e24: the two '+in' columns (coarse splines extended across t_- by the inner powers) are
  parallel to 1 - 1.3e-10 because the common inner continuation dominates their norm (diagonal 8e10 against 4e-3 for the far power
  columns), and the far power columns out5..out9 are nearly dependent. The certificate therefore works in a whitened basis T = L^{-T}
  (80-digit Cholesky of the exact dyadic midpoints), which leaves the generalized singular values unchanged; the whitened Gram is verified
  positive definite with ||E||_inf = 1.753e-27 (the verifier's independent value, V056). Float generalized singular values: 4.4222e-07,
  2.1107e-02, 3.6791e-02, 5.1198e-02, 6.5271e-02, ..., 76.33. VERIFIED: sigma_min >= 4.3337e-07. The weakest direction is the TAU column
  (coordinate mass 0.9964): the compensated TAU + dk KP image lives beyond the last test knot t = 16.14, so the test space hardly sees it (a
  defect of the test space, not of the operator). Without the TAU column: VERIFIED sigma_min >= 2.0685e-02 (float 0.02111), weakest direction
  in the far power columns out5/out8/out9 (m = 1, 0), again the weakly observed outer region. Interpretation: Prop IV.O (theory author, V039) shows
  that this realization cannot carry a continuum inverse, so these numbers are a test of the exact pipeline (conforming basis, exact images,
  exact Gram and rows, verified PSD certificate), not an ingredient of a theorem.

## 4. Off-basis blocks (prompt 6.4, 6.5)

4.1 The block (I - Q_M) L P_N. The columns of the section are the compensated functions u_j = phi_j + dk_j KP (the direct-sum norm
||u_j||^2 = ||phi_j||_X^2 + w_k dk_j^2 is the DEFINITION of the norm on X_N; KP itself has infinite X-norm). Let t_j >= ||(I - Q_M) L u_j||_Y.
A naive Cauchy-Schwarz with absolute values of the coordinates is NOT valid (second-model referee round offbasis, with a 2 x 2 counterexample);
the valid bound used here: with R a fixed real matrix such that G ~ R^T R (floating Cholesky factor, exact dyadic) and E := R^{-T} G R^{-1} - I
enclosed in ball arithmetic with ||E||_inf < 1, the functions uhat_i = sum_j (R^{-1})_{ji} u_j satisfy ||sum_i y_i uhat_i||_X^2 = y^T (I+E) y
>= (1 - ||E||_inf) |y|^2 and ||(I - Q_M) L uhat_i||_Y <= that_i := sum_j |(R^{-1})_{ji}| t_j, hence
    ||(I - Q_M) L P_N||_{X_N -> Y} <= |that|_2 / (1 - ||E||_inf)^{1/2}.
Per column, by the orthogonality of the angular modes and of Y_M within the retained modes (verified by second-model referee, Claim C):
    ||(I - Q_M) L u_j||_Y^2 = [S_j - r_j^T G_Y^{-1} r_j] + E_j^>,
S_j the exact squared norm of the modes N <= Nmax of L u_j over the whole plane (Phase 2a, work/run_norms.py: the images are compensated
BEFORE integration and the identically cancelling far tail term e^{(k-3)(t-t_+)} is stripped after a containment check; without the
compensation the separate images have infinite Y-norm, second-model referee Claim E), r_j^T G_Y^{-1} r_j >= r_j^T (Z + Z^T - Z^T G_Y Z) r_j (lower bound,
any real Z), and E_j^> the energy of the dropped modes N > Nmax, bounded above in Phase 2b (work/run_tailbound.py) by the l^1 majorant
(sum_N sqrt(wY2(N)) ||G_N||)^2 with term bounds ||f g||_{H1_W} <= sup|f| ||g||_{H1_W} + sup|f'| ||g||_{L2_W} (second-model referee Claim D: valid, l^2 over
cells would be sharper). The trial has exactly 260 angular modes, so all sums over N are finite and complete: nothing is truncated.
Status: Phase 2a/2b/offbasis code written and audited (V027, V033, V037, 03:13Z repair) but NOT RUN on the production S0 section: the
chain steps were dropped at 05:40Z to free the cores, because by Prop IV.O (V039) the S0 realization cannot give a continuum bound (the
quasimodes of V006 live in it), so the off-basis numbers of S0 would have been a pipeline test only. No certified off-basis bound exists in
this team; the code is in artifacts/code (run_norms.py, run_tailbound2.py, offbasis.py) with the commands in S2_RESTART.md.
4.2 The blocks Q_M L (I - P_N) and D_{M,N} = (I - Q_M) L (I - P_N) are infinite-dimensional and need the analytic high-frequency
theorem of prompt 6.6; nothing here bounds them. How the pieces would combine (Method A of prompt 6.6, not achieved): the theory author's
Theorem R (S2_L2_THEORY.md, conditional on the margin (H_m)) gives for the fixed-exponent operator L_fix in a weighted L^2(w) space
Re <L_fix h, h>_w <= -(m_* - eps)||h||_w^2 + ||K h||_w ||h||_w with K compact and explicit; this is an analytic reference inverse modulo a
compact K. Injectivity then reduces to a finite-dimensional check on an approximation of K, which is what a certified finite section can
supply, PROVIDED the section is computed in the same realization (the theory author's norm is an L^2(w) norm with anisotropic weights
|x|^{-2a}|y|^{-2b} and a radial Lyapunov factor; the present section uses factor H^1-type norms with pure radial powers). The two
realizations are not the same; a combined theorem needs either the section recomputed in the theory author's norm (the assembly code accepts any
piecewise-exponential radial weight but not anisotropic angular weights: those would require new angular Gram matrices, feasible since
|cos theta|^{-2a}|sin theta|^{-2b} integrals against trigonometric polynomials are explicit Beta functions) or the theory author's estimate
transferred to the present norm. Neither is done as a certificate. The later S_1 core section (section 7) IS computed in the theory author's
realization (R = L^2(w_a) on both sides, with the exact angular Gram against |cos theta|^{-1/2} after the cos^4 division), but only in
floating point; the certified version is out of reach in the window (7.5). The margin inputs b_+ and q themselves can be enclosed box by box from the exact data
(work/enclose.py). The numbers a Method-B argument needs from this team are the same coefficient tables
as Phase 2b (sup bounds of the background velocity modes Pe_n, Qe_n on every cell and the weighted norms of the background density
modes), which run_tailbound.py saves (tablesA.npz) for every cell and every n, j <= 261.

## 5. Second section in the theory author's realization (L_fix on L^2(e^{mu~(log r)}); theory author team message 4 and 5)

Operator L_fix h = (V.grad - 1) h + U[h].grad rho~ (no strain term; the strain term's image X.grad rho~ is not in this space). Space: the
plain spatial L^2 with weight e^{mu~(log r)}, mu~ piecewise linear in t with mu~(0) = 0 and mu~' piecewise constant (knots 3/2, 7/4, 3, 4,
5, 6, 7, 8, 9, 10; values 4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20 sixteenths); sup |mu~'| = 7/4 < 2, mu~'(-oo) = 1/4, mu~'(+oo) = -5/4.
In the factor modes, ||h||^2 = sum_{m,m'} Aang_mm' int b_m b_m' e^{8t + mu~} dt with the exact angular matrix of the x^2 y factor
(section_l2.angular_matrix), and ||g||^2 = pi sum_N int G_N^2 e^{8t + mu~} dt for the image. The trial's radial cells are split at the knots
(partial Green recurrences on the sub-cells), so every weight is a single exponential on every cell and all integrals are closed forms.
Columns: the conforming basis of section 2.3 (inner powers, coarse splines, outer power laws, J), 4 modes, stride 60; no tail columns
(r^k Theta and KP are outside the space: the integral int r^{2k} r^{-5/4} r dr diverges). Rows: pi int G_N psi_i e^{8t+mu~} dt for the test
splines of S0 with the end splines removed. Certificate: as 3.4 without compensation (certify_l2.py).
What it is for: the theory author's Theorem R (conditional on the margin (H_m), verified V023) gives in this space
m_* ||h|| <= ||L_fix h|| + ||K h|| with K compact and explicit; the section is the finite part of the complement question (Method A of
prompt 6.6). The margin itself is certified separately (work/margin.py). Result (C6, 05:41Z, work/runs/L2fix_M4_s60_o12/): sigma_min >= 0.510914 (float 0.52134; weakest direction the inner power
columns in5/in6/in7 at r < 0.0077) after two-sided exact whitening (raw condition number 3.5e68); a finite statement only.

## 6. Box certificates for the theory author's hypotheses (margin.py, hypA.py; the coefficient inequalities of Theorem R and Theorem C')

6.1 What is certified. On a cover of the closed first quadrant (parity gives the rest) by boxes [t_a, t_b] x [theta_i, theta_{i+1}] (the
trial's 1558 radial cells, the inner sub-cells t_- - {4, 2, 1, 1/2}, the outer sub-cells t_+ + {1/2, 1, 2, 4, 8}, the two half-lines; 64
angular boxes, refined adaptively where needed), rigorous lower/upper bounds of: the Theorem R margin m = b_0 + (1/2) mu~'(t) q - b_+
(weight e^{mu~(log r)}, theory author message 5), the anisotropic margin m_a = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta) - b_+ (w_a, a = 17/4,
theory author message 7), kappa_w = m_a + b_+ (Lemma C'2), q = V.X/r^2, b_+ = (|grad rho~| - d_y rho~)/2, |grad rho~|, |DU|, |V|/r (lower), the entries
of DV (hypothesis (Z), theory author message 12); the axis data d(t) = V_2(0, e^t)/e^t, d'(t), the endpoint constants of hypothesis (A), the (CB) constants
M_Q = sup |q - d|/cos^2 theta and M_P = sup max(e^{-2t}, 1) |p - p_axis|/cos^2 theta (exact Chebyshev identities, hypA.py docstring, second-model referee and
V054 confirmed). Numbers: S2_NUMERICAL_CERTIFICATES.md C4, C5.
6.2 Radial enclosures (work/encl.py; V058 repaired, V061 accepted). The background modes on a cell are exponential polynomials
f(sigma) = sum_e e^{e sigma} p_e(sigma) whose representation carries large cancelling coefficients (the Green particular solutions), and on
the inner sub-cells a near-resonance (inner mode 27, exponent gap lambda = 1.07e-12, coefficients of size lambda^-7; verifier V054). Any bound
treating the terms separately is useless there (radii 1e78). Method: (1) exact merging of exponent clusters with |e - e_0| h <= 1 by the
truncated expansion of e^{(e - e_0) sigma} to order 20 with the remainder e^{max(e_0,0) h} (sum |c_a| h^a) (|lambda| h)^21/21! e^{|lambda| h}
added to the radius, in >= 512-bit arithmetic so that the cancellations leave radii ~ 2^-512 lambda^-7; (2) Taylor enclosure of order 8 about
the midpoint of each sub-interval (width <= 6/|e|_max) with the rigorous remainder sup|f^(9)| (delta/2)^9/9! by coefficient sums on the
sub-interval; (3) exact hull of the sub-interval balls in Arb; (4) negligible modes (merged coefficient-sum bound < 1e-14) enclosed by that
bound. Half-lines: exact constant plus the coefficient-sum bound of the decaying rest (tailbound.sup_bound). All non-mid cells are processed
at 512 bits. Validation (logs/dbg_encl3.log, dbg_encl4.log, 512 bits): on cells 4, 1 (inner), 1563, 1566 (outer), 800, 1300 (mid) every
one of 9 x 260 sampled values of every mode lies in its enclosure; sums of mode radii 4.3e-6, 1.2e-7, 1.9e-2, 8.8e-3, 1.8e-2, 1.4e-1 against
3.4e78, 9.2e33, 1.3e5, 1.8e-2, 1.9e3, 1.4e-1 for the former mean-value bound.
6.3 Angular enclosures: arb balls of the theta boxes; the angular identities used for a_1, a_0 and tan(theta) V.grad(theta) are exact
trigonometric identities (Chebyshev polynomials of the second kind), with the modes n > 12 bounded by |U_{n-1}| <= min(n, 1/min cos theta),
|g_n| <= (4n^3 + 2n)/3, |U_{n-1}(cos 2 theta)| <= min(n, 1/min |sin 2 theta|). Adaptive refinement (margin.py): a standard box whose lower
bound of m or m_a is below 0.5 is bisected recursively (depth <= 4); the certified infimum is the minimum over the leaves. Test evidence
(ntheta 16): the P cell (t_a = 2.1507) had -3.65 unrefined and 0.76 refined; cell 800 (t = 2.52) -1.24 and 1.13; m_a on cell 850 -3.51 and 0.52.
6.4 Directed arithmetic: every final float is an outward conversion of a ball endpoint (outward.py); tail coefficients are formed in Arb;
sums of final floats are rounded upward; failed cells are +inf and are counted (failure counts in the JSON summaries). Exact-zero constants
dropped on the inner half-line are listed with their ball radii; the one for d - D rests on the exact normalization of the repaired trial
(V005), the others are structural (no e^{0 t} term exists in -6 e^{-2t} A_1 and in Pe_n, Qe_n for n >= 2).
6.5 Results (05:10Z; S2_NUMERICAL_CERTIFICATES.md C4, C5). All 1569 cells x 64 boxes, no refinement needed, zero negative boxes:
inf m >= 1.029821 (Theorem R margin for mu~; argmin t = 2.145, theta = 45.7 deg), inf m_a >= 0.965918 (w_a; argmin t = 3.95 near the x-axis),
kappa_* >= 3.037693; d in [5.575203, 21.301451] on the y-axis, |d'| <= 5.6012, (A) constants 0.100883/0.202073 at 0 and 89.334/73.311 at infinity,
M_Q <= 337.66, M_P <= 1075.516; sup b_+ <= 11.229, sup |grad rho~| <= 30.42, sup |DU| <= 125.744. (Z) data: |V|/r >= 0.10006 outside 255 boxes around
P (t in [2.131, 2.212], theta <= 15.5 deg); DV on the P box: xx [9.9588, 10.3327], xy [-1.7668, 1.8053], yx [-0.5901, 0.5699], yy [0.8180, 1.1919];
(Z0) Frobenius deviation of DV from diag(-A, D): 4.59 for r <= 0.05 (angular box width), 10.13 < A up to r_0 = 2.51. The refinement of the
P neighbourhood down to the disc B_{99/2000}(P) (theory author's Lemma Z, (Zb)) runs in work/zrefine.py.
With these, the two coefficient hypotheses (A) and (H_m') of the theory author's Theorem C' hold for the exact modal trial; Theorem R is unconditional
for L_fix on L^2(e^{mu~}). What remains for an inverse in this avenue is analytic: injectivity of L_red (section 7 below reports a floating
estimate when available) and the quantitative split (S) of Lemma IV.1.

## 7. Floating sections in the theory author's jet realization (NUMERICAL evidence only; fsec.py, fsec_ang.py, fsec_assemble.py; 05:00Z-08:30Z)

7.1 Object. The theory author's L_red (Prop B) acts on Z = E B (+) D_R into Y = E G (+) R, R = L^2(w_a), w_a = |cos theta|^{-17/2} e^{mu_a}, and
L_red h_0 = L(h_0 + kappa KP) with kappa = -k c[h_0]/(3 c_l + k c_KP) (S2_C_FUNCTIONAL.md 7.2): exactly the compensated columns of the S0 machinery.
Domain basis with the same span as the S0 columns: jet columns x^2 y b_i(t) (the m = 0 columns, J included) and remainder columns
x^2 y b_i(t) (cos 2m theta - (-1)^m) = cos^4 theta r^3 (...) for m >= 1 (they vanish like x^4 y at the y-axis, as D_R requires). Images: exact
ExpPolys per cell (opimage), combined with the KP compensation in ball arithmetic at Gauss nodes (3 per spline cell, 8 per sub-cell, 16 per
half-line stretch of length 40), then floats. Norms (fsec_ang.py): the image modes G_N are split into the axis jet gamma = -(1/2) sum (-1)^N
(2N+1)^2 G_N (= the cofactor B(t, pi/2)) and the remainder G - gamma x^2y-modes, which is divided by cos^4 theta (least squares) and measured
with the exact angular Gram A_{jl} = int sin((2j+1) theta) sin((2j'+1) theta)|cos theta|^{-1/2} dtheta (Gamma-function formula and the
recurrence I(k+2) = -I(k)(k+1/2)/(k+3/2), checked against quadrature to 1e-15, positive definite); radial weights e^{8t + mu_a}, G weights
e^{-t/2} / e^{27t/4}, B norm ||z'||_{L^2(omega)} with z = beta/H and H from the exact axis data d(t) (the Hardy/J terms of V041 omitted).
Core section S_1 = T_R + C_R on R (FSEC_MODE=S1): remainder columns only, images T u + C u with the strain term cut off by chi_0 := the exact C^6
J cutoff (1 near 0), no KP, remainder part only on both sides.
7.2 What was learned (logs/dbg_far.log, dbg_div.log, fsec_diag*.log). (i) The weight e^{8t + mu_a} spans e^{-25}..e^{+108} over the supports, and
the '+out' columns (splines extended across t_+ by alpha_2..alpha_5; the tail alpha_1 = k - 3 is excluded) carry Vandermonde coefficients of
size 1e4..1e8: unscaled float Grams span 1e34 and are numerically indefinite; every column is now divided by its weighted radial norm. (ii) The
KP compensation must be combined with the images in ball arithmetic at the node values (float combination leaves the cancelling e^{(k-3)t}
tails as noise 1e4 times the remainder at far nodes). (iii) The division by cos^4 (equivalently (B - gamma)/cos^2 of the cofactor) in a
TRUNCATED angular basis is ill-conditioned by ~N^3 (the division recurrence has the fourfold root -1) and the far weight multiplies the
error: at t = 6 a 20-mode truncation gives 5% of the exact weighted density, 80 modes 92%; the verifier's exact counterexample
cos^4 theta sin(37 theta) (V111) shows the truncated map is not a contraction. With the complete mode set (535 sine modes) the jet split and the
division are exact (residual energy fractions 5e-32 and 4e-15 in the 5-cell S1 test). The far region genuinely dominates the Y norm of a
column image in this normalization (weighted remainder density 1e11 at t = 6 for a mid spline of mode 1; the theory author's team message 25 found the same for
the residual: eta about 7.24e3 with 70% of the energy from log r in [8.135, 12]).
7.3 Result of the S_1 core section, Mh = 2 (FLOATING; 09:50Z; work/runs/S1/fsec_result.json, logs/s1_prod.log, logs/s1_assemble.log,
work/s1_robust.py). Basis: Mh = 2 produces the 42 remainder columns x^2 y b_i(t)(cos 2 theta + 1), b_i the stride-60 radial functions of the
S0 basis (sp0+in..sp3+in: splines extended inward by the inner power laws; in5, in6, in7: inner power columns; sp4..sp29: interior splines;
sp30+out..sp33+out: splines extended across t_+ by alpha_2..alpha_5; out5..out9: outer power laws minus their matching combination), so only
the angular remainder mode m = 1 is present. Images with the complete mode set (531 sine modes): the axis residual of the jet split is
<= 1.2e-15 relative and the cos^4 division residual <= 9e-8 relative (energy-weighted 2.5e-12 of the total image energy 2130), so the
angular map is exact up to double rounding and the verifier's V111 caveat does not apply; the floating parts are the Gauss quadrature
(3/8/16 nodes per cell type) and the double-precision accumulation of the two 42 x 42 Grams G_Z (columns in R) and B_Y (images in R).
Wall time 4817 s on 4 workers (1569 cells). Generalized singular values of the pair (B_Y, G_Z), i.e. the stationary values of
||S_1 u||_R / ||u||_R on the 42-dimensional subspace, solved at 50 digits from the stored double matrices (the double Cholesky whitening gives
4.136 for the first because cond G_Z = 1.5e13):
   4.1552, 6.0843, 23.314, 51.576, 53.109, 53.158, ...; largest 1038.2;  restricted to c[h_0] = 0: 4.44, 6.09, 23.3, 51.7.
7.4 Reliability of these numbers. The columns are nearly dependent in the R norm: the normalized Gram has eigenvalues 8.9e-13 (direction
0.78 out9 - 0.59 out5 - 0.20 out8: the outer power columns share the matching tail e^{alpha_1 tau}), 2.1e-11 (sp0+in against sp1+in), 4.4e-9,
1.3e-8, 2.6e-8, ... (seven below 1e-6). For each singular vector x (unit coefficient vector, columns pre-scaled) the Rayleigh quotients
x^T G_Z x and x^T B_Y x were compared with the accumulation-rounding estimate e = 1.3e-12 (sum_i |x_i| sqrt(diag_i))^2 (gamma_N for about
6000 additions times the Cauchy-Schwarz bound sqrt(M_ii M_jj) of the summands of a positive semidefinite sum; it covers the accumulation only,
not the formation of the node terms, the quadrature or the double images). For sigma = 4.1552: x^T G_Z x = 8.8e-6 and x^T B_Y x = 1.5e-4
against e_G = 1.5e-10 and e_B = 1.3e-6, so the Rayleigh quotient of this FIXED computed direction lies in [(b - e_B)/(g + e_G), (b + e_B)/(g - e_G)],
i.e. in [4.137, 4.174] under that model; since a Rayleigh quotient is an upper bound of the infimum, the section's smallest value is <= 4.18
up to the unmodelled errors. (CAVEAT 13:00Z, verifier V187/V189: the rounding model covers the accumulation only; the cos^4 divisions (input quotients through a padding-dependent pseudoinverse, about 1e-7 relative in G_Z; image quotients with a worst-case amplification 5.4e10) are not covered, so 'resolved' means resolved with respect to the accumulation rounding only.) This check does not bound the ORDERED smallest value from below (second-model referee junction_ref, item 3): the two next
computed directions (6.08, 23.3), near-null combinations of out5/out8/out9 with x^T G_Z x = 2.1e-9 and 1.8e-10, have image quotients 7.7e-8 and
9.6e-8 below their estimate 7e-7, so values in those directions are undetermined by this computation (anything from 0 to about 50). The
direction of 4.1552, 0.75 out9 - 0.55 out5 - 0.23 sp32+out - 0.22 out8, is a function concentrated just beyond t_+ = 8.135 (r about 3400),
where the matching combinations cancel the common tail. A sharper check would reassemble the Grams from the nodal factors in compensated
arithmetic (not stored) or certify B_Y - l^2 G_Z >= 0 from rigorous matrix enclosures (not available, 7.5). Removing the seven near-dependent directions leaves 10.13, 13.63, 50.96, 52.33, ...; the 33 pure spline columns (no outer
power law) give 50.32, 51.58, 53.16, 55.82. Reading: on this m = 1 subspace S_1 has no singular value below 50 away from the far junction;
the resolved value 4.16 sits at the junction t_+ in the outer power columns (comparable with the certified margin m_a >= 2.87, below the far
transport scale |c_l alpha_j - 1| of 20 to 40 there). A section value is an upper bound of the infimum over its subspace and proves nothing
about injectivity or about the complement; it is evidence for Lemma INJ-S only in that no small value appears in the bulk. The Mh = 3 run
(adds the m = 2 columns) is the convergence check; its result is 7.6, and the m = 3 run on the pure splines is 7.7.
7.5 Why this section is not certified. A certificate of sigma_min for this section needs the two Grams with rigorous error: the integrands
are e^{8t + mu_a(t)} Q_i(t)^T A Q_j(t) with Q_i = D^{-1} J G_i the exact cos^4 quotient of the 531-mode image vector G_i of exponential
polynomials. Exact term-by-term integration is out of reach (the quotient mixes all modes: 531^2 products of exponential polynomials per
entry per cell). A rigorous Taylor-model quadrature (Taylor coefficients of every image mode at the cell midpoint with the remainder of
encl.py, then exact integration of polynomial times exponential) costs about three times the floating evaluation per Taylor order and
needs the sub-interval splitting that the spline cells and the near-resonant inner modes require (encl.py: width <= 6/|e|_max), roughly six
sub-intervals per cell: about 18 h on the 4 cores of this team for the 42-column basis, outside the remaining window. A cheaper certificate
would need a better-conditioned far basis (the near-dependence of the outer power columns also makes any certified Gram ill-conditioned) and a
truncation theorem for the mode set, which the verifier's V111/V113 rule out for raw truncation. The method and the cost are recorded here
as the first missing step of the Avenue IV certification of S_1; the matrices of the floating section are exported (artifacts/data/S1).
7.6 Result with Mh = 3 (FLOATING; 12:35Z; work/runs/S1M3, logs/s1m3_assemble_v2.log, s1m3_robust.log, s1m3_bulk.log; 8709 s on 4 workers;
assembled with the repaired fsec_assemble.py (v2 of 12:35Z; v3 of 13:00Z checks the union of the block cell sets against the recorded
expected cell set, V188): the v1 sum had added the retained checkpoints to the parts and double-counted
1502 cells in S1, theory author message 38; s1_robust.py, which reads the parts alone, was never affected, and S1 re-assembled gives 4.15523, 6.08407,
23.31349 and, on c[h_0] = 0, 4.4563, 6.0844, 23.314). The 84 columns are the m = 1 and m = 2 remainder columns of the 42 radial functions.
50-digit generalized singular values: 2.3443, 2.9209, 3.5011, 3.8285, 3.9096, 4.6996, 5.6894, 6.3370, ..., largest 2389.5; on c[h_0] = 0: 2.3457,
2.9281, 3.5083. Flags: all of 2.3443, 2.9209, 3.8285, 3.9096, 4.6996 are UNDETERMINED (near-null combinations of out5/out8/out9 in both modes,
x^T G_Z x between 4.5e-10 and 2.5e-8, image quotients below the rounding estimate), 3.5011 weakly resolved ([2.55, 4.25]). Sub-blocks: the
m = 1 block reproduces S1 to the printed digits (same columns and nodes; the Grams differ by 9.3e-8 relative because the input quotients
went through a padding-dependent pseudoinverse, verifier V187; exact integer templates are used from 13:00Z on); the m = 2 block alone gives 3.6676 ([3.655, 3.680], far junction
direction), 4.34 (undetermined), 12.44, 28.49; without the seven most dependent directions 3.024, 3.345, 4.048.
The resolved, well-conditioned statement is about the 52 PURE SPLINE columns (sp4..sp29 in m = 1 and 2; normalized Gram eigenvalue
min 1.3e-4, rounding estimates 1e-9 relative): smallest values 3.4557, 4.2477, 5.4604, 6.9419, against 50.32 for the m = 1 splines alone
and 25.47 for the m = 2 splines alone. The weakest vector mixes the two angular modes with comparable weights on the coarse splines sp19
to sp25 (centred at t = 2.9 to 5.9, r = 18 to 360): sp25 (m=1) -0.39, sp23 (m=1) -0.36, sp24 (m=1) -0.31, sp22 (m=1) -0.28, sp21 (m=1) -0.25,
sp25 (m=2) -0.24, sp23 (m=2) -0.23, sp19 (m=1) -0.22. The weakest vector has a nearly constant mode ratio a_b/c_b = 1.45..1.8 (m = 1 over m = 2 coefficient) across the splines sp18..sp27, i.e. a FIXED angular profile h ~ r^3 cos^4 theta sin theta (a - 4 c sin^2 theta) (zero near theta = 39 deg) times a broad radial profile over t = 2..7 (artifacts/data/S1/S1M3_pure_spline_block.json, work/s1_vectors.py). So the smallest value of S_1 on the spline subspace falls by a factor 15 when the second
angular remainder mode is admitted, through the coupling of the two modes in the bulk region where the certified margins m_a and m_fam
also have their minima; this is a different phenomenon from the ill-conditioned far-junction values. Whether the bulk value keeps falling with m = 3 was tested by the run S1M4P (pure splines, m = 1, 2, 3): see 7.7; the junction test of theory author message 32 (S1J1) is 7.8. All of this is numerical evidence: a section value is an upper bound of the
infimum of ||S_1 u||_R / ||u||_R over its subspace, nothing more.

7.7 Result with m = 1, 2, 3 on the pure splines (run S1M4P; FLOATING; 15:43Z; work/runs/S1M4P, logs/s1m4p_prod.log, s1m4p_chain.log,
s1m4p_gram_compare.log; 10758 s on 4 workers; 1569 cells in four disjoint parts, coverage 1569/1569 against the recorded expected cell set,
never resumed). The 78 columns are the pure spline columns sp4..sp29 in the angular remainder modes m = 1, 2, 3, i.e. x^2 y b_i(t)(cos 2m theta
- (-1)^m); the near-dependent '+in', '+out' and power-law columns are left out (FSEC_DROP), so the normalized input Gram has smallest eigenvalue
1.36e-5 and dropping directions below 1e-6 removes nothing (below 1e-4 removes four and moves the first value to 2.766). Producer: the 12:41Z
fsec.py with the pinv input quotients (V187); that file was not frozen before it was edited, and work/runs/S1M4P/PRODUCER_PROVENANCE.md records
what is known about it (the later edits touched only the quotient templates, the settings record and the resume refusal; sampling, images and
accumulation unchanged). Input side checked against the verifier's exact scaled input Gram (V202; 640-bit balls, radii at most 1.3e-149
relative): largest entrywise relative discrepancy |G_ij - mid_ij|/sqrt(mid_ii mid_jj) = 7.41e-7 (the diagonal entry of (sp9, m = 3)), median 0,
congruent quadratic-form relative error 2.69e-6 with a 50-digit whitener of the exact midpoints (work/gram_compare.py, runs/S1M4P/gram_compare.json);
consistent with the pinv input error being largest for m = 3. Nothing follows from this for the image Gram B_Y (V187/V189 division errors). The verifier's V252 (proof 231) confirms the accounting (1569 cells once; 1531 retained checkpoint cells are duplicate prefixes and
excluded) and proves the input-form inequality (relative quadratic-form error < 2.688e-6 for every coefficient vector, 640 bits) and reproduces the
floating values independently (2.765547309, 3.268491498, 4.391313969; two-mode block 3.455656563).
50-digit generalized singular values of (B_Y, G_Z): 2.7655, 3.2685, 4.3913, 5.3953, 5.6169, 6.8798, 8.2071, 8.5554, ..., largest 2561.7; on
c[h_0] = 0: 2.7662, 3.2695, 4.3933. The Rayleigh quotient of the weakest computed vector lies in [2.7655, 2.7656] under the accumulation model
(x^T G_Z x = 34.3, x^T B_Y x = 262.7 against the estimates 1.0e-8 and 9.1e-4). Sub-blocks: m <= 2 (52 columns) 3.4557, 4.2477, 5.4604 (the
S1M3 pure-spline values of 7.6 reproduce to the digits shown; mode padding 534 against 533); m = 1 alone 50.3201; m = 2 alone 25.4729; m = 3
alone 12.1142; the 60 columns sp7..sp26 (the pure columns of the theory author's high graph, V210), measured in the LOW norms of this computation:
2.8648, 3.4089, 4.6170 (m <= 3), 3.7223 (m <= 2), 53.6343 (m <= 1); these are not high-norm values. Weakest vector: the bulk splines
sp21..sp27 (centres t = 3.9 to 6.9, r about 48 to 1000) with nearly proportional mode coefficients per spline (sp23: -0.289, -0.298, -0.140 for
m = 1, 2, 3; sp25: -0.292, -0.285, -0.130; sp24: -0.271, -0.280, -0.132): again one fixed angular profile, r^3 cos^4 theta sin theta times
a (cos 2 theta + 1) + c (cos 4 theta - 1) + d (cos 6 theta + 1) with a : c : d about 1 : 1 : 0.47 (in the scaled coordinates of meta
column_scales), times a broad radial profile (work/runs/S1M4P/vectors.json, artifacts/data/S1/S1M4P_vectors.json). Producer diagnostics: axis
residual of the jet split at most 1.2e-15, division residual at most 9.9e-8 (the pinv quotient mismatch), trace-jet at most 5e-14.
Reading: the pure-spline section value against the angular cutoff is 50.32 (m <= 1), 3.456 (m <= 2), 2.766 (m <= 3). The fall continues but
slows (factor 0.80 after 0.069); the sequence is not converged in m, and the window did not allow the m <= 4 run (about 3.5 h on 4 cores). The
S1 core section is therefore NOT bounded below by these runs; the floating values decrease with the angular cutoff, and the weakest direction
stays in the bulk region where the certified margins m_a and m_fam have their minima, not at the far junction. Everything in 7.7 is numerical
evidence: each value is an upper bound of the infimum of ||S_1 u||_R / ||u||_R over its subspace, up to the unmodelled division and quadrature
errors; nothing here is certified, and nothing follows for injectivity or for the complement.
7.8 Junction test (run S1J1; theory author message 32; FLOATING; 16:52Z; work/runs/S1J1, logs/s1j1_prod.log, s1j1_chain.log; 4165 s on 4 workers; 1569/1569
cells, never resumed; producer frozen with SHA256 in runs/S1J1/PRODUCER_SHA256.txt). The Mh = 2 section (m = 1 only) with the four sp+out columns
dropped and the five outer power columns out5..out9 attached at t_+ + 1 instead of t_+ (basis.py BASIS_OUT_SHIFT=1, 38 columns; conformity of
the shifted basis in logs/basis_shift_test.log: one-sided jets to order 3 and J to order 6 agree to 5.1e-51 and 1.4e-46, radii of exact zeros).
50-digit generalized singular values 4.7481, 15.1419, 34.287, 44.210, 51.576, 53.158, ...; on c[h_0] = 0: 4.7482, 15.142, 34.289. The weakest
direction is again the near-null matching combination of the outer power columns (-0.79 out9 + 0.56 out5 + 0.25 out8; normalized Gram
eigenvalue 9.0e-12) with x^T G_Z x = 1.98e-8 against the rounding estimate 9.8e-11 and x^T B_Y x = 4.47e-7 against 1.7e-7, so its Rayleigh
quotient is only weakly resolved, in [3.74, 5.58] under the accumulation model (S1 at t_+: 4.1552 in [4.137, 4.174]); the next two values live
in the same near-null space with image quotients at the rounding level (undetermined). Dropping normalized-Gram directions below 1e-10 leaves
5.84, 22.0, 44.2; below 1e-6: 8.31, 35.6, 45.7. Without the outer power columns (33 columns): 50.32, 51.58, 53.16; the 26 pure splines: 50.3201,
identical to S1 and to the m = 1 block of S1M4P (same columns). Reading: the small far value is not tied to the junction location (it moves
from about 4.2 to about 4.7 when the power laws are attached one unit further out) but to the outer power-law columns themselves: it lives in
their near-dependent matching combination, where the image quotient is at the rounding level of the computation, and it disappears when
those columns are removed. On the m = 1 subspace the only value below 50 is therefore an ill-conditioned artifact of the far basis; the
genuinely small section values are the pure-spline mode-coupling values of 7.6 and 7.7. Input side against the verifier's exact V267 Gram
(same meta.json and producer hashes): entrywise 6.01e-7 at the diagonal of (sp9, m = 1), outer block 1.2e-9, whitened quadratic form 4.31e-4
(near-null extended columns); with exact VM templates in use, the 6e-7 is the floating input quadrature and accumulation, not the V187
quotient error (work/gram_compare_s1j1.py, logs/s1j1_gram_compare.log). Numerical evidence only.

## 8. Answers to the prompt 6.8 questions from the numerics side (status 2026-10-28T16:05Z)

8.1 Is the finite basis conforming? Yes, exactly. The S0 basis (section 2: inner power laws, coarse C^6 splines with analytically imposed
joins, outer power laws minus their matching combinations, J, the TAU and KP tail columns, 169 compensated columns + TAU) is built from exact
rational and dyadic data; the identity test of the exact operator machinery passes to 1.7e-46 (C2), and every join and jet condition is an
exact identity in ball arithmetic, not a floating-point residual (the shifted outer basis of the junction test was re-checked the same way:
logs/basis_shift_test.log, one-sided jets to order 3 and J to order 6 agree to 5.1e-51 and 1.4e-46, radii of exact zeros). Membership of
the columns and of their images in the claimed spaces is stated in section 2 and was audited by the verifier (V020, V027, V033, V037, V043,
V054, V056). The pure-spline columns of the S_1 sections belong to the theory author's low remainder space (verifier V202) but, except for the 60
columns sp7..sp26, not to the high graph domain (V210).
8.2 Is the finite inverse rigorously certified? Only as finite statements, and only in realizations that cannot carry a continuum inverse.
Certified: S0 (169 columns + TAU, 12 x 69 rows, exact integration, 256 bits, two-sided exact whitening): sigma_min >= 4.3337e-7 with TAU and
>= 2.0685e-2 without (C3, C3b); the L_fix section in L^2(e^{mu~}): sigma_min >= 0.510914 (C6). By Prop IV.O (theory author, V039) the S0 realization
admits the quasimodes of V006, so these are pipeline tests, not theorem inputs. The sections in the theory author's realization (S_1 = T_R + C_R on
L^2(w_a), sections 7.3 to 7.7) are FLOATING only; their certification would need the rigorous quadrature of the cos^4-divided complete-mode
images (7.5: about 18 h on the team's 4 cores for 42 columns) and a mode-truncation theorem that V111/V113 rule out for raw truncation.
8.3 What are the off-basis residual bounds? None certified. The bound for (I - Q_M) L P_N (4.1: exact squared norms of the complete finite
angular expansion, 260 modes, minus the retained projection, with the l^1 tail majorant) is derived, coded (run_norms.py, run_tailbound2.py,
offbasis.py) and audited (V027, V033, V037), but it was not run on the production S0 section because of Prop IV.O. The blocks Q_M L (I - P_N)
and D_{M,N} were not bounded by this team (4.2).
8.4 Is the infinite-dimensional complement controlled? Not by this team. What this team contributes to the theory author's Method A (analytic reference
inverse modulo a compact K, Avenue IV sections 6 to 8 of the theory author's report) are the certified coefficient inequalities of the reference
operators: inf m >= 2.482724 and inf m_a >= 3.000000 over the plane (C4 with addenda; the earlier 2.9270 is verifier V197), the axis data,
(CB) constants and kappa_* (C5), the (Z) data (C4), the decoupled-family margins m_fam(4, 0.3) >= 1.250190 and m_fam(3.6, 0.3) >= 0.9596 (C7
with addendum). The remaining finite part, injectivity of S_1 on the low-frequency subspace (the theory author's Lemma INJ-S), is where the sections
of section 7 enter, and they are evidence only: the pure-spline section value decreases with the angular cutoff (50.32, 3.456, 2.766 for
m <= 1, 2, 3) without converging, with the weakest direction in the bulk r about 48 to 1000 and a fixed angular profile. No certified
injectivity statement exists.
8.5 Does the combination yield a genuine inverse theorem? No. The first missing inequality on the numerics side is a certified lower bound
of the S_1 section in the theory author's realization (8.2), preceded by convergence of the floating value in the angular cutoff (an m <= 4 run of
about 3.5 h is the next test); on the analytic side, the complement theorem (prompt 6.6) is the theory author's open item. Everything certified by
this team is listed in S2_NUMERICAL_CERTIFICATES.md (C1 to C7 with addenda); everything floating is N1 to N3 and section 7.
8.6 Real work time of this team: a session 00:21Z to 03:31Z, a session 03:32Z to 09:32Z, a session 09:32Z to 15:32Z, a session 15:33Z to the end of the
window (18:20Z); the long computations ran detached between shifts (shifts/shifts.log, work log).
