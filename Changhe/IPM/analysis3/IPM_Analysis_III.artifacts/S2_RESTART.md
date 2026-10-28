# S2_RESTART.md: reproducibility and continuation (theory author)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T02:51Z (theory author), updated 04:47Z, 05:00Z, 05:16Z, 05:26Z, 05:35Z, 05:47Z, 05:58Z, 06:16Z, 06:40Z, 06:45Z, 07:01Z, 07:04Z, 07:16Z, 08:06Z and 08:25Z and 08:31Z and 08:54Z and 09:43Z and 09:59Z and 10:10Z and 10:24Z and 10:33Z and 11:20Z and 11:50Z and 11:54Z and 12:19Z (V179 to V182; items 7 and 8: the necessary test of (S) and the assembly rules) and 12:46Z (V183, V184; the S_1 floating sections) and 13:09Z (V185 to V194: items 6 to 8) and 13:27Z (V198, V199: item 7) and 13:49Z (item 7: the knot-scale scan and guidance for a new trial) and 14:34Z (the label of V184 is CONDITIONAL THEOREM) and 15:15Z (section 5 item 9: the global Hoelder theory on the scaled far target) and 15:30Z (section 5 item 9: the scaled far target is not a global target, V243; the candidate with scaled quadratic axis control) and 15:36Z (item 9: V244, V245) and 16:06Z (review corrections V248, V250, V251, V253, V255; V246, V247, V249, V252, V254 integrated; V256 turning-height caveat in item 9, DERIVED; THEOREM since V262) and 16:14Z (V257 in item 9, DERIVED; V259: m_a >= 3) and 16:21Z (V262; V261 joint-cofactor target, DERIVED, in item 9) and 16:25Z (V265: V257 is a THEOREM; V264 in item 9) and 16:36Z (V268: V261 is a THEOREM; V266 DERIVED, in item 9) and 16:41Z (V271: V264 is a THEOREM) and 16:43Z (V272: V266 is a THEOREM, transport only) and 16:56Z (V274: the necessary tests concern (I) and (S) jointly) and 16:58Z (V277) and 17:04Z (V279; the Gaussian test direction, 5 item 7) and 17:10Z (V283: the Gaussian direction is a THEOREM) and 17:14Z (sharp coupling tails V276, V278 in the Hoelder continuation item) and 17:17Z (V286, V287: both THEOREMS) and 17:22Z (V290: the sharp tails are stated on E_2 and Y_gamma, not on Z_cof) and 17:28Z (V291: strain-zero subspaces of S1J1 in section 5 item 4) and 17:34Z (V292, V294, V296: exact axis identity for R_d in section 5 item 7) and 17:43Z (V299: axis and zeta notation defined there; V300: nonzero vectors in the input-form bound) and 17:45Z (V298, V301: global axis identity in section 5 item 7) and 17:53Z (V304: c[d] != 0 in the strict tests, signed axis cutoff chi in item 7) and 17:58Z (V302, V307, V308: exact knot-jump ratio in section 5 item 7). The numerics team keeps a detailed restart file for the exact finite-basis
pipeline (the accompanying numerics S2_RESTART.md); this file covers the theory documents and the theory author's grid
computations, and states how to continue the whole S2 project.

## 1. Workspace map

The work was split into three parts: theory (this file, CONVENTIONS.md, the theory documents S2_L2_THEORY.md,
S2_CALPHA_THEORY.md, S2_C_FUNCTIONAL.md, S2_CLOSURE.md and the final report), the exact numerical pipeline (its
certificates and reports S2_BASIS_CERTIFICATION.md, S2_NUMERICAL_CERTIFICATES.md, the numerics report and its own
restart file), and independent verification (the verification report with records V001 onwards, each with claim,
method, result, verdict, evidence and date, and one proof directory per topic with PROOF.md and evidence; proof
SHA-256 values are listed in the records). In the accompanying artifacts these are, in order, the top level with
code/, data/ and theory_notes/; numerics/; and verification/ (see the README there). The original data of case 1 and of
the earlier analysis were only read, never written; every part worked on its own copy.

## 2. Inputs and their identity

- Accepted numerical state X3 (reference only): IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz of case 1,
  md5 15f8095f7e79dbfa0c50d75e5fe8997a.
- Rigorous background: the exact modal trial of Analysis I, verification/data_exact/modal_v2.json.xz, SHA-256
  57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6, with the scalar repair z of V005.
- Float version of the trial for grid evidence (V255: the raw NPZ data, like X3, are not literally the normalized
  background, which is defined only after the exact joining and the scalar repair): numerics/data/trial_v2_h0.008.npz of Analysis I,
  md5 95d4b484f7c924d6e09fd347d0c0fab5.
- Held constants: k = 1615536043799051/2^53, c_l = 1/k, A = 2c_l - 1, D = 4c_l - 1 (CONVENTIONS S0.1).

## 3. Reproducing the theory author's grid evidence (NUMERICAL, float64; none of it is a bound)

Environment: Python 3.12.13 (the pyenv build used throughout the run), invoked by its explicit interpreter path
(python3 below stands for it), with numpy, single-threaded (export OMP_NUM_THREADS=1, run under nice). Cluster, remote
or paid compute, JavaScript/TypeScript tooling and servers are not allowed; write only into one's own working copy
(V255).

Step 1, the field on the polar grid (about 40 s):
```
export ANALYSIS1_SRC=<copy of Analysis I>/IPM_Analysis_I.artifacts/numerics/src
cd artifacts/code/lyapunov
python3 field.py 700 181        # writes field.npz: t in [log 1e-3, log 1e5] (700), theta in [0, pi/2] (181)
```
The log line must report c = 15.726087831924705 and 3/k - 1 = 15.726087831924637. The stored grid is
artifacts/data/lyapunov/field.npz, SHA-256 206e5bbb43eb84522f75d5ce5d582ca38954a3b89dffbbb86778faca833462c8.

Step 2, the margins (each a few seconds; run in the directory that holds field.npz):

| Script | Computes | Expected output | Document |
|---|---|---|---|
| margin.py | radial windows for (H_m); first smoothed mu | best margin with free radial mu' 2.977; smoothed mu': min margin 0.8105 at r = 8.426, theta = 0.960 | S2_L2_THEORY 3 |
| mu_explicit.py | closed-form tanh-type mu, sup abs(mu') = 1.90 | min margin 2.932 (far field), 5.21 for r < 0.1 (mu_explicit.json) | theory author's team message 4 |
| mu_pwc.py | the piecewise affine mu~ (knots 3/2, 7/4, 3, ..., 10) | min margin 2.590 at r = 4.48, theta = 0.90 (mu_pwc.json) | S2_L2_THEORY 3, S2_C_FUNCTIONAL 5 |
| aniso.py, aniso_mu.py, aniso_margin.py | anisotropic windows with abs(sin theta)^{-2b(t)} | margin >= 1.36 (a = 7/2, b_max = 6/5) | S2_L2_THEORY 5 |
| aniso_pwc.py <a> | per-row slope windows for w_a | aniso_pwc_a4.10/4.25/4.40.json | S2_L2_THEORY 5 |
| aniso_knot0.py | w_a with one knot at r = 1, for a = 4.10, 4.25, 4.40 | min margin 3.0908 (far field), 12.78 at the knot, 49.70 for r < 0.1 at a = 4.25 (aniso_knot0.json) | S2_L2_THEORY 5, S2_CLOSURE 6 |
| box_moment.py | anisotropic L^p box moments, inflow/outflow signs | table 2.4 | S2_C_FUNCTIONAL 2 |
| artifacts/code/hinorm/joint_margin.py, joint_regions.py (FIELD_NPZ=<path of field.npz>) | joint symbol margin kappa_w - sup_nu (s nu^T DV nu + p(X, nu)) for ordinary, conormal and scaled derivatives; regional minima | at P it reproduces V011's delta_s; the x-axis ratio kappa/d_yV_2 tends to 2.334 at r -> 0; conormal margin on theta > pi/4 is 5.4, 4.3, 1.8 at s = 1, 2, 3 | S2_L2_THEORY 6.1, 6.5 |
| artifacts/code/injrank/s1_estimate.py, local_rank.py (run in the directory of field.npz) | first Fourier moments S_1 of the polar coupling matrix B and of b_eta on periodic windows; local phase-space rank counts | sum S_1(B_ij) + 2 S_1(b_eta) = 1648.4 (window [-3, 11]); sup abs(grad B) = 139.67 at t = 4.0; local counts 11979 (m = 0.966), 1242 (m = 3), 148 (local grid margin) (s1_estimate.json, local_rank.out) | S2_BASIS_CERTIFICATION 6.1 |
| artifacts/code/injrank/rank2.py, s2_estimate.py, s2_eta_scan.py, s2_local.py, s2_noaxis.py (run in that directory with the path of field.npz as argument; the last three reuse the first lines of s2_estimate.py) | second Fourier moments S2 of B_ij and b_eta (V096 rule), eta scan, unit radial cells, vertical-axis strip removed; local second-order proxy | window [-3, 11], eta = 0.1: sum S2(B_ij) = 21483, S2(b_eta) = 34621; Lambda 172 (E = 1), 139 (E = 3/2); per-parity counts 5.2e4, 3.4e4 (global), 2.8e4, 1.8e4 (unit cells), 1.9e4, 1.3e4 (strip half-width 0.3 removed); local proxy 130 at m = 5/2 (rank2_eta0.1.json, s2_*.json) | S2_BASIS_CERTIFICATION 6.1 |
| artifacts/code/hinorm/corner_counterexample.py (needs scipy) | quadrature of the frozen corner solution of Prop F4 | agreement with -C x^4 sgn(y)|y|^{2-1/D} to 1e-15 relative; C = 4.2088e-3 for the bump used | S2_L2_THEORY 6.2 |

Step 3, the strong residual of rho~ (NUMERICAL; python-flint; single thread; each point about 0.5 to 50 s). Code in
artifacts/code/farres, outputs and logs in artifacts/data/farres (SHA256SUMS in both). The scripts import the
verifier's independent original-data modules global_check.py (of V077) and angular.py (the exact angular
norm of V100) by absolute path (variable LANE at the top of each script); run them from artifacts/code/farres.

| Script | Computes | Expected output |
|---|---|---|
| far_points.py --points <t list> | axis and remainder energy densities of F(rho~) at the given t = log r, all angular modes, exact quotient moments | far_points_192.json (t = 2..60), far_points_160.json (t = 0..20, step 1/4; remainder 1.1780e7 at t = 10) |
| eta_estimate.py | log-linear quadrature of the densities, regional shares, tail at the fitted rate | eta_estimate.json: eta about 7240.66, squared norm 5.2427e7, shares 0.07/4.85/69.7/25.0/0.39 percent by proportional splitting of the segment at 8.135 (exact exponential splitting gives 4.72/69.84, V122) |
| profile_points.py | the same densities for rho~ itself | profile_points_160.json |
| sup_points.py, trunc_points.py | pointwise sup of F and rho~ on circles; the residual energy after angular truncation at 60 and 120 modes | sup_grid.log (ratios 1e-8 to 3e-7), trunc_grid.log |
| ang_layer.py | cumulative fraction of the remainder density within phi = pi/2 - theta < delta (Clenshaw in Arb on phi = u^2) | ang_layer.log (0.88 to 0.997 within 0.01 rad for 2 <= t <= 8) |
| sob_proxy.py, mode_decay.py | unweighted angular H^s proxies and octave-band rms of the quotient modes | sob_proxy.log, mode_decay.log |
| eta_family.py, eta_family_sum.py | the remainder density for a in {3.6, 3.8, 4.0, 4.25} and the integral with far shift Delta in {0, ..., 0.5} | eta_family.json (7241 at a = 17/4, Delta = 0; 13 at a = 3.6, Delta = 0.3) |

SHA-256 of the JSON outputs: mu_pwc.json 2b9ea7e6e202f824002ce551f5ec61bbccf068254d4f0ecd5c9c08151198e8e2,
mu_explicit.json 44fb204103d89f2ee20565738c3e25698d55db37d109d130233d5a964882943b,
aniso_knot0.json db750b3bd483f72638993eb7bf17dbe674b32a2abdf77d3181a2fa7e67f2d1d9.

## 4. Status at this version

- This section is the historical status of the verdicts V001 to V106 (as of 07:16Z); the later records are summarized
  in section 5 and in S2_CLOSURE.md section 4 (V255). The THEOREM list and the open items are in S2_CLOSURE.md
  sections 4 and 5.
- V034 (02:48Z) confirmed Prop M, the representer formula, Corollary C1, Prop C2 and Prop B (the last conditional on
  the operator domain); V035 replaced one sentence on c-bounds; V036 corrected the origin regularity to C^{4,1}.
- V037 confirmed the pipeline repairs and left two arithmetic obligations; V038 confirmed the corrected far cancellation,
  the scalar normalization ell(h), the augmented map and the abstract two-norm theorem, and refuted the smaller far
  exponent and the sufficiency of d != 0; V039 confirmed Prop IV.O; V040 confirmed Lemma IV.1 with its transport
  extension as a conditional theorem; V041 confirmed the scalar y-axis row on explicit spaces (conditional on a positive
  axis rate) and found the first-version Theorem C underspecified; V042 confirmed membership of the residual in the
  jet target Y = E G (+) L^2(w_a) and corrected the augmented map for a free cubic coordinate. Theorem C' of
  S2_L2_THEORY.md 5.2 (DERIVED) states the global Fredholm claim on fully specified spaces. V046 confirmed its
  pure-transport part (Lemmas C'1 to C'3) as a conditional theorem; V044 showed that the strain term must be part of the
  coupling (L_fix does not map Z into Y); V045 proved the separated part of the cross-strip coupling (E3); V043
  independently enclosed the S0 tail-column strains and the bordering denominator.
- V047 confirmed Theorem C' as a conditional theorem; V049 to V052 proved its coupling hypotheses (E-J), (E0), (E-G)
  under explicit annular C^5 and endpoint bounds of the background; V053 verified those bounds for the modal density.
  So L_red : Z -> Y is Fredholm of index 0 for the modal background under (A) and (M). V048 audited the report.
  V054 audited the first (A) certificate script (coverage and underflow REFUTED) and recorded the failed S0 Gram test.
- V055 proved the transport regularity of the modal field and the exact energy limits at 0 and infinity, so Theorem C'
  needs only (A) and (M). V056 showed the S0 Gram failure was a precision artifact. V057 and V060 proved the low/high
  bilinear and Lipschitz-velocity bounds in cylinder-H^7 high spaces. V058 refuted a float union in the range code;
  V059 and V061 confirmed stable moment formulas and the repaired union with resonance merging.
- V062 confirmed the moving-tail quasilinear formulation (A_h with the exact scalar elimination, the low/high difference
  bound, the conditional iteration). V063 confirmed Lemma H1 under (Z) and a compact escape lemma without (Z), and showed
  that (Z) does not follow from the divergence and endpoint data. V064 proved that the frozen source threshold
  s_fast (about 3.5785) is sharp with the Riesz coupling retained.
- V065 confirmed the mapping side of the variable-order high space (cone-local cylinder H^s bulk, s > 2, near the
  x-axis segment and the origin; factored H^7 near the vertical axis). V066 reproduced the S0 bound with TAU
  independently (conditional on the exported entries). V067 confirmed Prop F4 for the frozen operator, refuted the
  parity-only threshold, and left the transfer to the true operator OPEN. V068 confirmed the revised range and refinement
  method and refuted the archived merge of the production parts.
- Lemma Z (S2_L2_THEORY.md 6.3) reduces hypothesis (Z) to finite checks (CONFIRMED, V071). V070 certified the source
  rectangle Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2] (|V| >= 0.1801 |X - P|, P the only zero in Q).
- The numerics team certified the finite section S0: sigma_min >= 4.3337e-07 (2.0685e-02 without TAU), a finite
  statement only (Prop IV.O). Both values are verified conditional matrix certificates (V066, V200): conditional on the
  exported entries enclosing the exact pairings.
- Prop F4 (S2_L2_THEORY.md 6.2, THEOREM for the frozen operator, V067): the frozen corner solution -C x^4 sgn(y)|y|^{2 - 1/D} shows that no frozen
  inverse reaches order 5/2 - 1/D across the x-axis (2.334 for general weighted data even in x); for the true operator
  the transfer is OPEN; the proposed high space has variable order (6.6), with order 2 + eps below both values.
- The numerics team's box certificates (production 04:50Z to 05:10Z; coverage, retention and directed aggregation
  CONFIRMED by V072 conditional on the exported cell enclosures; the verifier's independent original-data values are in
  the V077 bullet below):
  m_* >= 1.029821 for mu~, m_a >= 0.965918 and kappa_* >= 3.037693 for w_a, d in [5.575203, 21.301451] with the endpoint
  constants of (A), M_Q <= 337.66, M_P <= 1075.52, and the (Z) box data (abs(V)/r >= 0.100068 outside 255 boxes near P;
  86 boxes with a zero lower bound, 77 of them outside Q; global (Z) was settled independently by V080). All short decimals are rounded outward from the
  stored endpoints (the verifier's note of 05:24Z found several rounded inward in the first summary). Next in that team: an L_fix section in the L^2(e^{mu~}) norm and a floating section of L_red in the
  jet realization. Their status is in the accompanying S2_NUMERICAL_CERTIFICATES.md.
- Constraint for the high space (CONFIRMED, V069): rho~ has a nonzero seventh-derivative jump at the knot
  t = 4958764014967233/2^51, so the residual is not locally H^(13/2) there and every order of the high target on that
  circle and upstream of it must be below 13/2 (S2_L2_THEORY.md 6.6). V073: the mapping side holds for every factored
  order sigma > 6 (25/4 admissible with delta = 3/2, gamma = -1/2, s = 21/10; V079 later excluded s = 21/10 at
  delta = 3/2 by the cylinder corner threshold, and the parameters are now delta = 9/5, s = 41/20). V076: the residual lies in that target.
  V074: Theorem H must be an inverse-regularity (graph-domain) estimate; a bounded same-order isomorphism is false.
  V075: the margin perturbation coefficient is 51/4 (plus ||grad h||_infinity for b_+).
- Injectivity: grid estimates of the rank of the finite-rank split (S2_BASIS_CERTIFICATION.md 6.1) give about 1e9 for
  the global commutator bound and about 1e2 to 1e4 for locally adapted cutoffs; by these estimates a certificate
  with this method would have to be localized (estimates for the chosen method, not a proved necessary dimension).
- V077 (the verifier's own original-data computation, independent code): d >= 5.5752, m_a >= 0.53072, m_R >= 1.78605.
  So (A), (H_m') and (H_m) hold and Theorems R and C' are THEOREMS for the actual background (Fredholm of index 0;
  the complete statement with spaces is in the verifier's accompanying proof of the Fredholm statement). V080: global (Z), the zeros of V are 0 and
  (+-p, 0), |V|/r >= 3/12500 outside Q. V078: the numerics refinement's exclusions are in Q, its leaf count was a node
  count. V079: the cylinder corner threshold 3/2 + delta A/(A+D); delta = 3/2, s = 21/10 is excluded; use delta = 9/5,
  s = 41/20 (S2_L2_THEORY.md 6.5, 6.6). The external consultation TH_varorder lists further hypotheses of Theorem H
  (S2_L2_THEORY.md 6.6 (a) to (g); claims).
- V081: the C6 finite matrix (L_fix section in L^2(e^{mu~}), sigma_min >= 0.510914) reproduced as a conditional matrix
  certificate. V082: the adjoint-witness and Schur injectivity criteria and the regular-cylinder commutator and Garding
  estimates (conditional lemmas). V083: the regular-cylinder Mellin bound. V084: zeta lies in Y intersect H_base^sigma
  for 0 < delta < 2, gamma > 2k - 1, sigma < 13/2. V085: a one-order gain of the full coupling C is REFUTED (packet
  counterexample), so the high energy keeps the full order-zero principal coupling. V086: both global margins are at
  least 5/2 (independent refinement and audit). V087: L_red restricted to ker J has index -1; the problem is solved
  with J free and normalized afterwards by rho_norm(X) = lambda rho_*(X/lambda), lambda = (1 + j)^{1/2}.
- V088: the principal joint high-energy symbol, margins 142.5074 (y-axis, 25/4), 0.97261 (x-axis cylinder, 41/20;
  threshold 2.08092) and 3.78768 (infinity) at delta = 9/5. V089: the rank-one non-implication. V090: sup ||DW|| <= 1e-5
  keeps the zero set and the flow. V091: C^1 convergence does not give uniform high inverses (torus family).
- Lemma INJ-S (S2_CLOSURE.md 3.5(b); THEOREM, V092, with Hilbert product norms in its first bound and the graph-norm
  conversion s_1 <= (k_1^2 + (1 + ||C_R|| k_1)^2)^{1/2}): if S_1 = T_R + C_R is injective on D_R, the injectivity of
  L_red is equivalent to that of a Fredholm index-0 system M_J on B x R (one variable plus one scalar), so the
  two-dimensional certificate is needed only for S_1 on the plain space L^2(w_a). V093: ||c_R|| < 0.20757 exactly.
- V094: the conditional algebra of the finite-rank split. V095: the explicit axis-strip constant
  A_ax = sqrt(W_max)[593 M_20 + (593 s_0/2) M_21 + (612 s_0^2/6) M_40 + (612 s_0^3/24) M_41] (four background suprema
  to be enclosed). V096: the principal real energy error above Lambda is second order,
  eta/2 + (S2mat(B) + S2(b_eta))/(2 Lambda^2). Grid moments (NUMERICAL, code injrank/rank2.py, s2_*.py): the split is
  estimated to need of order 1e4 to 5e4 low modes with these tools, about 1e2 for local proxies (estimates for the
  chosen method, not a proved necessary dimension).
- V097: the paired weight-conjugation difference is Hilbert-Schmidt on a compact regular patch. V098: the full regular
  Mellin velocity keeps the second-order real-energy error, with the extra terms G_0 E_0 + 6 K G_1/(Lambda - 2 -
  |sigma + 2|)^2. V099: strip constants 39 and 25 instead of 593 and 612. V100: exact angular reduction of the target
  norm, with directed code in the verification evidence (to be used for the residual enclosure).
- V101: exact energy localization (no transport error for sum chi_j^2 = 1; coupling defect a paired double commutator,
  Hilbert-Schmidt on regular patches). V102: INJ-Q, the conditional quantitative injectivity certificate for S_1 with
  every input listed (bound (1 + e p)/(5/2 - eps - delta_F - e d)). V103, V104: low-to-high regularization of the
  frozen inverses in the x-axis cylinder chart (1/kappa_s = 1.02816 at delta = 9/5, order 41/20) and the vertical
  remainder chart (every finite order). V105: closed trace majorants N_j and the radial-lift bound. V106: Lemma H-spec
  CONFIRMED as an abstract theorem (lambda_* = omega + 1 + 2M||C||), REFUTED for the direct identity shift on the free-J
  spaces, OPEN for a compatible shift and the actual high inverse.

## 5. How to continue (priority order)

1. (Done: the margins (H_m), (H_m') and (A) are VERIFIED by independent original-data code, V077; the numerics team's
   sharper single-team values are in S2_NUMERICAL_CERTIFICATES.md section 4; both margins are at least 5/2 by V086, and
   m_a >= 2.9270 by V197 and m_a >= 3 by V259, an independent original-data whole-plane certificate.) The
   first open item is now injectivity of L_red (item 4).
2. (E) is proved (V049 to V053), with qualitative constants. For an inverse bound, make its compact parts explicit:
   operator-norm bounds for the output tails, the strip and separated pieces near the axis, and a finite-rank
   approximation with explicit error of the remainder on a bounded region away from the axis.
3. (Done: (A) and the margins, V077; (Z), V080.) Quantitative versions: the coefficient constants M_Q, M_P of (CB)
   and kappa_* are certified once (numerics team); an independent check would make V046's constants explicit.
   Membership of the residual in Y_lo is proved (V042); its norm is now enclosed (item 6: V164, V174, V179 in the
   low norms, V182, V192 in a fixed high norm; V255).
4. Injectivity and a quantitative inverse at h = 0, through the finite certificate of S2_CLOSURE.md 3.5(b): by Lemma
   INJ-S, first S_1 on L^2(w_a) (a finite-rank part of the compact remainder of Theorem C' (iii) at margin 5/2 - eps
   and certified approximate adjoint solutions on a conforming basis), then the one-variable system M_J with explicit
   tail bounds and its scalar 1 + c[L_ren^{-1} zeta]. The principal error is second order (V096) and the strip constant
   explicit (V095, V099); the symmetric weight conjugation on a regular patch (V097) and the full Mellin remainder
   (V098) are bounded in the same second-order form; the next steps are enclosures of the second moments and of
   M_20, M_21, M_40, M_41 and of alpha, alpha', alpha'' (lift, V105), the singular-strip split of the conjugation,
   and then a certified low block in the INJ-Q form (V102; localization V101) of the resulting size (estimated of order 1e4 modes with
   global moments for this method, not a proved necessary dimension; a ball-arithmetic computation of that size is
   outside the allowed means of this work). Floating sections of S_1 (NUMERICAL, S2_BASIS_CERTIFICATION.md section 9;
   floating output observations: only the input quadratic-form errors are certified, the image division and the
   quadrature are not (accumulation-only rounding model, V187), so none of these values is an operator bound or an exact
   finite singular value): 4.155 with the first angular remainder mode (outer power columns; about 4.75 when they are attached at t_+ + 1, S1J1, V277;
   its exact strain-zero subspaces, of dimensions 37, 31 and 28, are certified on the input side only, V282, V291;
   the small floating value stays concentrated in the outer-column coordinates, its accuracy and meaning unresolved, V279), 2.344 with
   the first two modes (84 columns; unresolved because of near dependence), and 3.456 on the 52 pure spline columns of
   the first two modes against 50.3 for the first mode alone; the coupling of angular modes in the bulk (r about 18 to
   360) lowers the section value. The completed pure spline section with three angular modes (V252; NUMERICAL at every
   scope; 78 columns sp4 to sp29, m = 1, 2, 3, S_1 on L^2(w_a)) has the floating smallest generalized singular values
   2.7655, 3.2685, 4.3913 (independent assembly by the verifier 2.765547309, 3.268491498, 4.391313969) and 2.7662 on
   c[h_0] = 0; its sub-block m <= 2 gives 3.4557, 4.2477, 5.4604 (reproducing 3.456), the single modes give 50.32
   (m = 1), 25.47 (m = 2), 12.11 (m = 3), and the 60 columns sp7 to sp26 give 2.8648 in the low norms of this
   computation (not a high-norm value). Against the angular cutoff the value is 50.32, 3.456, 2.766 for m <= 1, 2, 3:
   decreasing, not converged in m. The input-form error is below 2.688e-6 for all nonzero vectors against the exact V202 input
   Gram (rigorous); output division and quadrature are uncertified, so there is no exact operator lower bound and no
   certificate. Finite floating observations do not decide the rank needed for a complement certificate (V255).
5. The high norm of variable order (S2_L2_THEORY.md 6.6: order 2 + eps near the closed x-axis segment [0, x_P] with
   eps < 0.14547 and origin exponent delta = 9/5, conormal order N near the y-axis, scaled order N at infinity;
   hypothesis (Z) of Lemma H1 is VERIFIED, V080), the bilinear and
   Lipschitz bounds in that space (proved for cylinder-H^7 spaces, V057, V060), then the closure inequalities of
   S2_CLOSURE.md 3.4. The high energy must keep the full order-zero coupling (V085); zeta is in the high target (V084).
   Lemma H-spec (6.6) is CONFIRMED as an abstract theorem and REFUTED in the direct free-J form (V106). The restated
   form (07:01Z, DERIVED, submitted) reduces the high inverse to (H1) the mapping bound of C_R, (H2) a large-parameter
   bound for T_R and (H3) the high a priori estimate for S_1 - lambda, plus (J1) to (J3) for the jet row (Corollary
   H-spec) and low injectivity; no separate regularization step. Remark (6) of 6.6 reduces (J1), (J2) to sector
   conormal regularity near the y-axis (DERIVED). Next theory targets (historical: the 'Next' steps of this item up to
   the 10:24Z note were carried out, as the 10:33Z and 11:50Z notes record; V255): (H2) as a composition bound for the
   flow of V in X_H (remark (2)), and (H3) at lambda = 0 in energy form (remark (1)).
   Do not shift the jet row: on {J = 0} the shifted scalar row changes index at lambda = D/4.
   Status 08:06Z: (J1) to (J3) are THEOREMS on the explicit candidate of V118 (Gamma_H = a H^(25/4), a = e^(9t/5) at
   the origin end and e^(-7t/2) at infinity, B_H = {J chi + a v : v in H^(29/4)}, R_H = factored axis-zero order 25/4
   plus cone-bulk order 41/20; V112 to V118). Do not use the integer target H^6 (V115). For the sharp cone sum (H1) is
   expected to fail at the cone boundary (S2_L2_THEORY.md 6.6 remark (7)); the next target is a smooth variable order
   s = F(Lambda) with V.grad s >= 0, on which J1 to J3 carry over, and then (H1), (H2), (H3) on it.
   Status 08:25Z: the sharp cone sum fails (H1) (REFUTED as a choice, V119). Lemma H2-var (S2_L2_THEORY.md 6.6, after
   remark (7)) defines the variable-order space H_var (factored order 25/4 on a sector around the y-axis, order s(x)
   with V.grad s >= 0 elsewhere) and proves (H2) for it by a regularized energy estimate (DERIVED, sent to the verifier).
   Next: (H1) on H_var (order-zero operators of the dilation-invariant calculus on variable-order spaces; the
   factored structure of C_R h at the y-axis) and (H3) in energy form with an escape weight e^(N G(Lambda)).
   Status 08:54Z: (H1) and (J1) to (J3) on the equivalent space X_s are THEOREMS (V126); (H2) on X_s is a THEOREM in
   the dyadic norm under W.grad s >= 0 (V129; the five-derivative version is REFUTED, V127). Lemma H2-ord
   (S2_L2_THEORY.md 6.6, after Lemma H2-var) constructs the order function from the exit time of a repeller block
   around the closed x-axis segments and the sources (DERIVED, sent to the verifier). Do not try an energy proof of (H3)
   with only a compact error on the isotropic cofactor space: t-frequency packets at the vertical-axis end have
   negative energy (V128). Lemma H3-var (after Lemma H2-ord) reduces (H3) to the characteristic-set margins, the
   origin-end normal family (bijective for lambda > -0.9726, frozen ODE computation, submitted) and the far end
   (lambda > -3.7877). Next: the uniformity in xi of the normal-family inverse, the propagation estimates with
   W^(7,infinity) coefficients in the dyadic form of V129, and the radial-source estimate at P below threshold.
   Status 09:43Z: the order function exists (V130, V132), so (H1) and (H2) hold on an actual X_s. The origin normal family
   is bijective for fixed frequency (V131) and uniformly in it for the exact normal operator (V133); the selected
   principal end inverses (vertical, horizontal, far) are stable under the actual coefficient errors (V135, V137). The
   joint source margin is 4.52536, not 14.8 (V134). Proposition H3-red (S2_L2_THEORY.md 6.6, after item 6 of Lemma
   H3-var; DERIVED, sent to the verifier) reduces (H3) to (Hs_eps) ||h||_s <= C (||(S - lambda) h||_s + ||h||_(s-eps))
   through the exact identity -Re <T_R g, g>_(N_0) = int kappa |g/(b cos^4)|^2, N_0 the bulk weight divided by
   cos^8 theta. Do not absorb first-order coefficient errors by a Neumann series in the graph norm (counterexample
   R_eps = eps d_theta). Next: (Hs_eps), i.e. the global symbol inequality m + N W.grad Lambda + L_0 (W.nu)^2 >= mu and
   its finite-regularity quantization (variable order, W^(7,infinity) coefficients, coupling principal symbol).
   Status 09:59Z: V138 (first-order error unbounded on the normal graph, actual coefficients), V139 (actual inner end
   with an annular error) and V140 (coupling tails -> 0 in X_s; reduction to a compact core with a high-norm error)
   CONFIRMED. H3-red CONFIRMED conditional on (Hs_eps) (V141). Lemma Hs-sym (S2_L2_THEORY.md 6.6, after Proposition
   H3-red; THEOREM, V144, after one decimal correction at S_y): the symbol inequality holds
   for every mu < m_x by compactness from the confirmed margins and the escape function of V130. Proposition Hs:
   (Q0), (Q1), (Q2), (Q5) => (Hs_eps) (10:06Z: matrix form, positivity (F1) and the log term (F2) proved
   elementarily; 10:10Z: (Q2) restated modulo compact and small errors and covered by V140, V142, V143 except for the
   local commutator with Op(<xi>^(s(X))); V145 confirms the scalar positivity and log steps). Status 10:24Z: all four
   inputs CONFIRMED (V146 (Q0) with the sector support correction, V147 (Q2), V148 (Q5') with a small high error, V149
   and V150 (Q1) on the maximal domain); Proposition Hs reassembled on these forms (theory_notes/Hs.md = S2_L2_THEORY 6.6;
   L_0 is fixed before the small parameters a, eta, theta). Status 10:33Z: the assembly is CONFIRMED (V151) and the high
   Fredholm theorem holds: S - lambda, L_ren and L_red are Fredholm of index 0 on the high graph domains (V152).
   Perturbation: do not use a variable-order Kato-Ponce bound for the full commutator [A, B.grad] (REFUTED, V153, it
   misses -(B.grad s) log<D>); keep (W + B).grad s as one coefficient, nonnegative for ||B||_inf <= kappa_s/2 by the
   robust order of V154, and discard it by V155 (C^(1,alpha) suffices). Status 11:20Z: the uniform high theory for small
   frozen-coupling transport perturbations is CONFIRMED (V156 velocity bounds; V157 square-summed commutator; V158
   dyadic energy; V159 uniform compact-error estimate on D_g; V160 generation, index 0, uniform inverse if S_0 is
   injective); the single-operator route (theory_notes/Hs_pert.md, Lemma K) is a second confirmed proof (V161, V163) with the
   N_0 sign corrected (V162; the Corollary (i) formula there is wrong as written, use (1/2) div B - beta B_r +
   4 tan(theta) B_theta). Status 11:50Z: the bordered block, the low estimate and the moving background are CONFIRMED
   by the verifier's own proofs (V166 perturbed scalar axis row with the weighted trace; V168 full fixed-coupling high
   block; V169 its low version; V170 exact moving-tail family, uniform low and high inverses under base low
   injectivity); a planned separate perturbation note was withdrawn as superseded. Assembly: theory_notes/Exist_cond.md (Lemma Emb and
   Theorem E, conditional existence; S2_L2_THEORY 6.8): Lemma Emb THEOREM (V177), Theorem E CONDITIONAL THEOREM (V178),
   both for the original and the decoupled low spaces (V175, V176 give the decoupled inverse and difference theory).
   Next: base low injectivity (OPEN, the only structural hypothesis left), then a realistic value of the high residual
   norm eta_H (enclosed only as 3.866e10 < eta_* < 6.321e129 in a fixed equivalent norm, item 6) and the constants r_*,
   K_H, K_L, C of the smallness condition (all qualitative now).
6. The residual. 6049.11 < ||F||_Y < 8601.42 (V164, complete interval certificate; earlier eta > 933.47, V110) and
   about 7.2e3 (NUMERICAL, Step 3), in a layer at the vertical axis. Decoupled family (inner radial exponent kept,
   far weight r^(-37/20), a in [18/5, 4]): margin >= 1.10534 (V171), low mapping and Fredholm theory (V172; the old
   uniform third axis derivative bound fails, V173), 3.270 < ||F||_(Y_a) < 485.632 (V174, V179). These are low norms;
   the high norm of Theorem E is enclosed as 3.866e10 < eta_* < 6.321e129 in an explicitly fixed equivalent norm (V192
   lower bound from the fifth derivatives of the weighted axis trace at t = 8 and 1001/125 by a fractional difference
   inequality, after the point bound 1906360017 of V183 and 36400585492 of V186; independent of the cutoff and the
   Littlewood-Paley partition; V182 deliberately loose majorant). Floating fifth differences at every fourth span
   midpoint (artifacts code/farres/axis_profile.py) put the knot-scale structure in t in [1.92, 2.62] (up to 6.06e9)
   and t in [7.9, 8.135] (up to 1.93e9); certifying a point there (about 2.6e10 at t = 2.2335, 3.3e11 for the pair
   2.2259, 2.2335, NUMERICAL) would raise the lower bound but decides nothing. The lower bound sits where the knot-scale structure of
   the C^5 spline residual under the weight 1/a_* is large (a numerical diagnostic, not a decomposition theorem), so a
   trial for the high closure probably needs joins of higher continuity or an analytic representation (report 6.5
   item 9; a heuristic suggestion, and an improved trial is not an existence result, V255); a realistic value is still
   needed. The rest of this item is the earlier plan, now carried out at Delta = 0.3. Before any
   closure attempt: either a trial that resolves the axis layer for 4 <= log r <= 20, or a weight with smaller angular
   and far exponents (about 13 at a = 3.6, Delta = 0.3) with the margin map m(a, Delta) certified. In the tied family
   a <= 4 loses the finite-J scalar inverse (V121); keep the inner radial exponent at 17/4 and lower only the angular
   and far exponents (r < 1 carries 0.07 percent of the residual energy), and redo the jet-row proofs for the new angular
   exponent (V116 uses the trace gain a - 1/2). A certified upper
   bound needs the directed window method of V110 over all windows on 0 <= t <= 20; the tail beyond t = 20 is
   certified (V125: energy in (203443.34, 203445.56)). Floating margins of the decoupled variant: numerics
   margin_family.json (min 0.73 at a = 4, Delta = 0.3; 0.22 at a = 3.6, Delta = 0.3; negative boxes for Delta = 0.4 at
   a <= 3.8).
7. Before any further closure attempt, run the constant-free necessary test of (S) (S2_THEORY_18H_REPORT.md 6.5 item 8,
   CONDITIONAL THEOREM, V184: under (I) and (S) the exact residual of the j-th Newton-type iterate satisfies
   ||F(iterate j)||_Y <= q_0^j ||f_0||_Y with q_0 = K_L C K_H eta_0 < 1): compute the first step h_1 = -A_0^(-1) f_0 and compare the low residual norm after it with the low
   residual norm of the trial; if it does not decrease, (S) fails for every admissible constant (under (I), which the
   step presupposes). Improve the trial
   where the residual sits (the vertical-axis layer for t between about 2 and 10, and the far corrections of degrees
   2k - 1 and 3k - 2, which the far operator determines algebraically; report 6.5 item 9), and measure the residual
   in the high norm of V182 rather than only in the low norms. Two further constant-free tests (report 6.5 item 10):
   eta_0 |c[d]| <= N4 ||A_0 d||_(Y_H) with 0 < N4 < 9.06 (V185), and ||R_d||_(Y_H) > 1956082280 |c[d]| if c[d] != 0, for
   R_d = A_0 d - c[d] f_0/(ell_0 n'_0) = L_ren d + c[d] Q_ren/(ell_0 n'_0) (V194); in relative form a certified
   ||R_d|| <= 0.0507 eta_0 |c[d]| for one d with c[d] != 0 suffices (V199). Never norm M_0 or L_fix d separately in the strong zero-jet Sobolev targets of
   Theorem E: for c[d] != 0 neither is in them (V190; in the Hoelder targets Y, Z, Z_2 of S2_CALPHA_THEORY.md 3.4 both
   columns are legitimate, V255). Do not use the scaling tangent rho_0 - X.grad rho_0 as d: it is outside the chosen
   high correction space (V198). Use the exact Gaussian density d = -Delta v of report 6.5 item 10 instead (c[d] = 1,
   J[d] = 0, d in D_H(A_0); THEOREM, V273, verifier proof, independent audit recorded as V283): only certified upper
   bounds of ||L_ren d + m_0||_(Y_H) and
   ||L_ren d + m_0 - f_0/(ell_0 n'_0)||_(Y_H) are needed, in the fixed norm of the eta_* enclosure; the rational polynomial
   of d is in the accompanying verification artifacts. Write axis(q)(y) = lim_(x->0) q(x,y)/x^2, zeta for
   the density derivative partial_ell rho_ell at ell_0 and chi_infinity for the chart cutoff. On the axis segment
   |y| < 1, where chi_infinity vanishes and hence zeta = 0, one has exactly
   axis(R_d) = w f' - 2 w' f + lambda f, with f = axis(rho_0), lambda = 1/(ell_0 n'_0),
   w = -g'' + (U_2[zeta](0, y) - U_2[rho_0](0, y)/ell_0)/n'_0 and g(y) = -(y^3/6) exp(-y^2); w'(0) = lambda, so the
   cubic coefficient cancels, and the separately large axis terms of f_0 and m_0 need not be subtracted (THEOREM,
   V292 with its binding correction V294 of the Gaussian trace, verifier proof, independent audit recorded as V296;
   a pointwise identity for |y| < 1, not a bound of the high norm). For every y, with a = 1/n'_0, z = axis(zeta),
   u = U_2[rho_0](0, y), K_q F = q F' - 2q' F and D F = (ell_0 y + u) F' + (2 ell_0 - 1 - 2u') F, the same quantity
   is axis(R_d) = K_w f + lambda f + a D z; where chi_infinity = 1 it equals
   K_w f + a k (f - f_inf) - a k^2 [(u/y) f_inf + log|y| K_u f_inf], f_inf = axis(r^k Theta), r^k Theta(theta) the
   leading far density of rho_0, so the leading dilation term cancels exactly, and in the cutoff transition the term
   -a k^2 (ell_0 y + u) chi' log|y| f_inf, with chi(y) = chi_infinity(|y|) and chi'(y) = sign(y) chi_infinity'(|y|),
   is kept explicitly (THEOREM, V298, verifier proof, independent audit
   recorded as V301; an identity, not a bound). At an interior spline knot r_* where the axis cofactor
   A(t) = f(e^t)/e^t of rho_0 has a nonzero seventh-derivative jump (verified at the knot of original index 700, V198),
   the sixth t-derivative jumps of axis(R_d)/y and axis(f_0)/y, t = log y, have the exact ratio
   w(r_*)/(ell_0 r_* + u(r_*)), with a positive denominator (THEOREM, V302, verifier proof, independent audit
   recorded as V307; a ratio of derivative jumps at one knot, not of high norms). Formally dropping U_2[d] and
   U_2[zeta] from w turns this ratio into a/(ell_0 + u_r) - lambda, the heuristic below for A_0 d minus lambda, as
   R_d = A_0 d - lambda f_0 (DERIVED algebra; the dropped terms have no estimated error, so this remains a
   heuristic). A heuristic at the knot scale (A_0 d is about c[d] f_0/(n'_0 (ell_0 + u_r)), u_r = U[rho_0].e_r/r
   the radial transport coefficient, u_r = u/y on the axis) indicates that the archived trial fails both tests; a certified upper bound of
   ||R_d|| for one d with c[d] != 0, with the knot-scale part separated, would refute the conjunction of (I) and (S), hence (S) under (I), not
   (S) alone. For a new trial, check first that
   its high norm is not dominated by knot-scale structure (joins of higher continuity or an analytic representation in
   t in [1.9, 2.7] and near the outer junction). In the archived trial that structure is (as a numerical diagnostic,
   not a decomposition theorem) a component alternating in sign from span to span, of relative size 3e-12 to 5e-10 in the fine-knot zone and growing towards the outer
   junction (report 6.5 item 10; numbers reproduced independently, V209). Measure it span by span with the seventh-derivative scan of the accompanying
   artifacts (code/farres/knot_scan.py); it should be at the rounding level everywhere before the high norm is used.
   Likely causes are the conditioning of the final solve on the knot gaps 0.0019 and the C^6 match with the far
   expansion at t_+; a final solve in extended precision there and a smoother junction (higher-order matching, or a
   blend over many spans) are the first remedies to try; a smoother trial only makes the tests checkable and is not an
   existence result. Do not filter the coefficients by index differences: on
   nonuniform knots this destroys the smooth part (it raised the axis values by five to eight orders).
8. Numerical assembly rules. Assemble a finite section so that every cell is counted exactly once: for a completed,
   never-resumed run use the final parts only; for a resumed run use the final parts and every disjoint base block,
   never the retained checkpoints; record the done-cell set of every block and assert disjointness and full coverage
   before summing (V180); the check must compare the union of the done sets with the expected cell set recorded at run
   creation, not only the number of cells (V188). Form the input quotients by cos^4(theta) with the exact integer
   templates Q_m(theta) = 2 sum_(j=0)^(m-1) (-1)^(m-1-j) (2m - 2j - 1) sin((2j + 1) theta) (V189, V255), not with a padded pseudoinverse (input error about 1e-7 relative,
   V187), and bound the image division error before calling a section value resolved; the exact raw image bandwidth of the S_1 remainder
   column product is J + M odd sines, 264 to 266 raw slots (V193; not the bandwidth of a full free-jet or tail section,
   V255). A margin replacement needs a complete exact radial cover of each replaced cell and a finite
   new bound for every angular box and every reported quantity, or the retained old bound where none exists (V181).
9. Avenue II, global Hoelder theory (S2_CALPHA_THEORY.md 3.4). Do not use the common target C^alpha_2 intersected
   with L^2(w_gamma) as a global target: the full operator is not onto it (V232, V234), and on E_2 and on every Y_gamma, gamma > 4k, the
   complete coupling is bounded and the maximal realization closed, but T, L_ren and A_0 have infinite algebraic cokernel
   (V241, THEOREM, recorded as V247; the range of the actual residual and closedness of the range remain OPEN). Do not use the scaled far
   target Z of 3.4(g) as a global target either: ordinary far C^alpha lets transverse powers |x|^sigma,
   alpha < sigma < 1 + alpha, along the outgoing vertical axis escape every range (V243, THEOREM, recorded as V249: infinite
   algebraic cokernel of T, L_ren and A_0 on Z for 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k; no conclusion about the
   actual residual or about Z_2). Z remains useful: with
   2k - 1 < beta < k (at the endpoint 2k - 1 the moving-tail column has a logarithmic far term outside Z, so the operator does
   not map the entire transport domain into Z; a restricted closed realization is not excluded, V235) the
   coupling is bounded with small tails (V235, V244), and the exterior operator is invertible (V236, V242). The next
   target must keep scaled quadratic control along the whole outgoing vertical axis. Use Z_2 of 3.4(g), the rescaled
   C^alpha_2 annular norms (V245, THEOREM, independent audit recorded as V254, at this scope): it has the bounded
   complete coupling, the residual, the closed full operator on its maximal domain and an actual auxiliary exterior
   inverse, obtained with the time change a = V_1/x
   (x_t = e^t x exactly along V/a). What remains on Z_2 is a global inverse. Caveat, check its record first: by the
   turning-height obstruction (THEOREM: verifier proof V256 with an original-data interval certificate of a simple zero
   of a(0, y) = d_x V_1(0, y) on the vertical axis, y_* in (9.1465, 9.1468), a_t in (7.1952, 7.1954); independent audit
   recorded as V262), T is not onto Z_2 for alpha > 1/2, and A_0 and L_ren are not onto Z_2 for alpha > 2/3 (all 2k - 1 < beta < k,
   gamma > 4k); degenerate zeros are not covered. A stronger divided velocity bound (V257: U_1[x^2 g]/x jointly C^alpha on bounded x-strips for g compactly supported, even in x,
   bounded and uniformly C^alpha in y;
   THEOREM, verifier proof, independent audit recorded as V265) extends the A_0 and L_ren statement to every
   alpha > 1/2. Open: alpha <= 1/2 for A_0 and L_ren (for T alone see V266 below). The heuristic
   remedy alpha <= 1/2 is open whether sufficient. The other remedy is now the next candidate: the joint-cofactor target Z_cof (THEOREM, V261, verifier proof, independent audit recorded as V268): h = x^2 g with g in the
   full joint C^alpha locally and sup_R R^(2-beta)(||g||_inf + R^alpha [g]_(C^alpha)) on the dyadic annuli, plus
   L^2(w_gamma). For every 0 < alpha < 1 and 2k - 1 < beta < k the complete coupling is bounded with a small tail,
   the residual lies in Z_cof, T, L_ren and A_0 are closed on their maximal domains, and the actual auxiliary exterior
   operator is invertible; J is not closable. The turning-height forcings are unbounded in this norm, so V256 and V257
   do not apply to it; its global inverse is OPEN. For an exterior smallness argument on E_2 or on Y_gamma = E_2
   intersected with L^2(w_gamma), gamma > 4k, use the sharp coupling tails proved there: the complete coupling tail is
   of exact order R^(2k-1) log R on E_2 and R^max(2k-1, 2k-gamma/2) log R on Y_gamma (THEOREM, V276, verifier proof,
   independent audit recorded as V286), and the renormalized coupling tail, which equals the complete one on the
   strain-zero inputs, is of exact order R^(k-1) log R on those same spaces (THEOREM, V278 with sign clarification
   V281, verifier proof, independent audit recorded as V287); no faster rate can be assumed there. These rates are not
   proved sharp on Z_cof (V290); there its separately proved tail estimates apply. Transport alone is not onto Z_2 or
   Z_cof near the source (THEOREM, V266, verifier proof, independent audit recorded as V272): with DV(P) = diag(A_s,
   mu_s) at the source P, 10 < A_s < 51/5, the cusp profiles s_+^a phi(y/s_+^b), a = 1/A_s, b = mu_s/A_s, of the
   conjugated transport give smooth compact forcings with c = J = 0 that span an infinite-dimensional subspace of the
   cokernel of T on either target for alpha > 1/A_s, so for every alpha >= 1/10. This excludes a Neumann series around
   T; it says nothing about A_0 or L_ren, since the full source coupling changes the equation. The nonlinear
   derivative loss persists on Z_cof (THEOREM, V264, verifier proof, independent audit recorded as V271): there are
   smooth inputs h_n with c = J = 0, supported in a fixed compact set away from both axes and bounded in the graph
   norms of T, L_ren and A_0, with ||N(h_n)|| >= b n for N(h) = (U[h] + (c[h]/3) X).grad h; so N has no continuous
   extension at 0 in these graph topologies. This does not exclude a quasilinear scheme, stronger derivative norms or
   a profile.
   Restart program on Z_cof: a global inverse of A_0 on Z_cof (not a Neumann series around T, by V266), with a quasilinear scheme for the
   nonlinear step. The next open step is the matching of the exterior inverse with the cut-off local inverses at the origin and the sources
   across the middle annuli. The complete error of a single cut-off patch is not compact (V227 on the common target,
   V239 on Z, THEOREM, recorded as V246; both for the specified single patch with cutoffs satisfying the flow-box
   hypothesis), so compactness of each patch error is not available (cancellation in a sum of patches is not excluded,
   and an error of norm below 1 gives surjectivity only); what is needed is a Hoelder substitute for the Garding
   inequality of the L^2 theory, for example a propagation estimate along the flow that keeps the zero-order
   coupling, or an exact construction that is triangular along the flow. For existence this is not on the critical
   path: Theorem E is proved in Hilbert norms, and Hoelder regularity of a solution follows from the Sobolev windows
   by embedding (S2_CALPHA_THEORY.md 3.3, route (ii)).
Do not use Hoelder norms alone for the explicit semilinear nonlinear step (V030, V211), the radial graph for the normalization (V032), or a
finite section without a complement bound (V014).
