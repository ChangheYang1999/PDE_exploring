# S2_NUMERICAL_CERTIFICATES.md (numerics team; updated 2026-10-28T05:15Z)

Every entry: exact quantity, background, input identity, method, precision, truncation error, rounding error, final outward
enclosure, independent check. "Verified" means also confirmed by the verifier team (VERIFICATION_RECORD.md item); otherwise "certified by
num" (ball arithmetic by this team, not yet independently reproduced).

## C1. Strain of the exact modal trial (certified by num; re-verifies Analysis I modal_repair and the verifier's V017 background)
- Quantity: c[rho~] - (3/k - 1), c[rho~] = psi~_xy(0) = (1/2) int_R f_1(e^s) ds, for the exact modal trial rho~ (modal_v2.json.xz,
  SHA-256 57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6; joins at the knot endpoints; Ei, Eo exact 6-jet
  solutions; A_00 + z with z in [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20]).
- Method: work/exact_trial.py. Exact rational B-spline cell polynomials (Cox-de Boor, fmpq_poly); exact rational joins; sine projection;
  closed-form exponential-polynomial moments; forward/backward Green recurrences; three formulas (head + middle + tail; the B_1 route;
  the cosine-mode identity int r (a_0/4 + a_1/8 - a_2/8 - a_3/8) dr). Ball arithmetic (python-flint/Arb) at 320 bits; every operation
  outward; uniform over the z enclosure (z carried as a ball). No truncation (all sums finite, half-line integrals in closed form).
- Enclosures: c (Green) in 15.726087831924638026669384596423888989546298 +/- 4.36e-43; c (B_1 route) the same ball;
  c (cosine modes) in 15.7260878319246380266693845964238889895462983 +/- 4.07e-44; target 3/k - 1 = ... 2983 +/- 2.60e-44;
  c - target in [-1.62e-43, 1.62e-43].
- Independent check: Analysis I float Green data agree (A_1(t_-) = 5.71238711e-10 float vs 5.71238710784e-10 +/- 2.3e-22 exact).
- Run: logs of 00:52Z (exact_trial.py __main__), reproduce with `python3 work/exact_trial.py` (3 min).

## C2. Identity test of the exact operator machinery (consistency check, fixture trial trial_small_M20.npz)
- Statement checked: sum_m L(x^2 y a_m cos 2m theta) = L rho~ = 2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ in every sine mode at sample points
  of 8 cells (inner half-line, inner sub-cell, first/middle/last spline cells, outer sub-cell, outer half-line), all 42 output modes.
- Result (02:02Z, logs/test_identity3.log, 200 bits): maximum over modes and sample points of |midpoint| + radius of the difference ball:
  1.692e-46 (cells 1, 3, 6: inner sub-cell and the first spline cells), 5.354e-48 (cell 782), 1.848e-54 (cell 1560), 1.260e-55 (outer
  sub-cell 1562); the quantities compared have sizes 1e-8 to 4e-2 (the leading terms cancel in the identity). The first run exposed a
  Green-step error (factor e^{4h} instead of e^{(4+e)h}; work log 01:29Z) with mismatches 2e-12 near t_-; after the fix all mismatches are at
  the ball-radius level. PASSED (consistency of the operator machinery; not itself a bound on anything).

## C3. Finite section S0 (exact trial; Mh = 4, coarse stride 60, Mout = 12, test stride 30): certified by num (finite statement; 04:30Z)
- Objects: A = Q_M L P_N for the exact modal trial rho~ (inputs as in C1), columns = 169 conforming columns of basis.py (q = 3 B-splines on the
  coarse knots of stride 60, C^2 joins by exact rational Vandermonde solves; inner continuation '+in' and outer power columns 'out5..out9';
  the J column; modes m = 0..3 (43, 42, 42, 42 columns)) plus the TAU tail column, each compensated by dk_j KP so that the far
  e^{alpha_0 t} tail of the image cancels exactly (denominator 3 c_l + k c_KP, enclosed, excludes 0); test space: 69 cubic test splines
  per output mode (end splines dropped, V020) x 12 output modes sin((2N+1) theta). Norms: domain H^1-type mixed norm of the factor
  b = h/(x^2 y) with weights eps0X = 1, gammaX = (3k - 1)/2, mode weight (1 + (2m)^2)^1, unit weights for J, TAU, dk (notes team message 2);
  forcing: the same type on f/r^3 with weights (1 + (2N+1)^2)^1. Precision 256 bits; exact integration of all cell integrals (exponential
  polynomials); assembly 02:06Z-03:58Z (6797 s, 2 workers); max radius of a Gram entry 1.24e-62, of a row entry 5.99e-28.
- Method (certify.py): sigma_min^2 = min_x x^T B^T G_Y^{-1} B x / x^T G_X x >= s^2 if K - s^2 G_X is PSD, K := B^T (2 Z_0 - Z_0 G_Y Z_0) B
  (any symmetric Z_0; G_Y^{-1} >= 2 Z_0 - Z_0 G_Y Z_0 exactly); PSD verified by E = L_f^{-1} M L_f^{-T} - I in ball arithmetic, ||E||_inf < 1.
  Whitening (04:10Z, verifier V056 confirmed independently): the raw G_X has condition number 1.74e24 ('+in' columns parallel to 1 - 1.3e-10),
  so a change of basis T = L^{-T} (80-digit mpmath Cholesky of the exact dyadic midpoints) is applied in ball arithmetic: G -> T^T G T,
  K -> T^T K T, B -> B T. The generalized singular values are invariant under any invertible real T.
- Result (logs/certify_S0_v4.log, runs/S0_M4_s60_o12/certificate.json): whitened G_X positive definite, ||E||_inf = 1.753e-27 (the verifier's
  independent value, V056); G_test positive definite (||E|| = 1.08e-13; cond 1.1e23). Float generalized singular values: 4.4222e-07,
  2.1107e-02, 3.6791e-02, 5.1198e-02, 6.5271e-02, ..., 76.33. VERIFIED LOWER BOUND sigma_min >= 4.3337e-07 (exact s = 4093149700530291/9444732965739290427392 = 4.33379081799e-07, rounded down; verifier V066 reproduced the matrix step with positivity residual < 4.4e-12; K - s^2 G PSD with
  ||E|| = 2.9e-12 at s = 0.98 x 4.4222e-07). The weakest direction is the TAU column (coordinate mass 0.9964): the finite section barely
  sees the compensated TAU + dk_TAU KP image (its image lives beyond the test knots t <= 16.14). A variant without TAU is in C3b.
- Meaning: a statement about the 170-column section only. By Prop IV.O (V039) the S0 realization cannot carry a continuum inverse (its
  domain norm is stronger than its target norm near the y-axis), so this number is a pipeline test, not an ingredient of a theorem.
- Independent checks: verifier V043 (cTAU, cKP enclosures from the original NPZ), V056 (whitened Gram PD, same ||E||), identity test C2.

## C3b. S0 without the TAU column (169 compensated basis columns; same rows, norms and method): certified by num (04:33Z)
- Result (logs/certify_S0_noTAU.log, runs/S0_M4_s60_o12/certificate_noTAU.json): float generalized singular values 2.1107e-02, 3.6791e-02,
  5.1198e-02, 6.5271e-02, 8.8180e-02, ..., 76.33; VERIFIED LOWER BOUND sigma_min >= 2.0685e-02 (K - s^2 G PSD, ||E||_inf = 5.25e-11).
  Weakest direction: the far power columns out9, out8, out5 (modes m = 1 and 0), i.e. the outer region beyond t_+ where the test
  splines end (t <= 16.14): the far columns are weakly observed by this test space. Same finite-statement scope as C3.

## C4. Margin certificates for the theory author's weights (margin.py; CERTIFIED by num, 05:10Z; verifier V086 confirmed; addendum V197; addendum 2 of 15:54Z not yet verified)
- Objects (exact modal trial rho~, inputs as C1): on every box [t_a, t_b] x [theta_i, theta_(i+1)] of the cover of the closed first quadrant
  (1558 spline cells, inner sub-cells t_- - (4, 2, 1, 1/2), outer sub-cells t_+ + (1/2, 1, 2, 4, 8), the two half-lines (-oo, t_- - 4], [t_+ + 8, oo);
  64 angular boxes of pi/128; parity gives the plane), rigorous lower bounds of
    m = b_0 + (1/2) mu~'(t) q - b_+            (Theorem R margin, weight e^(mu~(log r)), theory author message 5: mu~' piecewise constant with knots 3/2, 7/4, 3, ..., 10
                                                 and values (4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20)/16; both values on a box touching a knot),
    m_a = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta) - b_+   (weight w_a = |cos theta|^(-2a) e^(mu_a), a = 17/4, mu_a' = -17/2 (t < 0), -5/4 (t > 0), theory author message 7),
  with b_0 = 1 + c_l, q = V.X/r^2, b_+ = (|grad rho~| - d_y rho~)/2 (upper bound (sup|grad rho~| - inf d_y rho~)/2, V033 form), the angular identity
  sin(2n theta)/cos(theta) = 2 sum_(k<=n) (-1)^(n-k) sin((2k-1) theta) exact for n <= 8 and |.| <= 2n beyond; radial enclosures encl.py (section 6.2 of
  S2_BASIS_CERTIFICATION.md), 160 bits on the spline cells, 512 bits on the other 11 cells; directed final floats. Adaptive angular refinement
  (bisection where a lower bound is below 0.5, depth <= 4) was available but NOT needed: refined_boxes = 0.
- Results (work/runs/MARGIN/margin.json, merged from MARGIN_A (cells 0:785) and MARGIN_B (785:1569); cells_computed = 1569 of 1569; 1835 s):
    inf m   >= 1.029821   (argmin: cell 668, t_a = 2.1449, theta box 32 of 64), negative boxes: 0;
    inf m_a >= 0.965918   (argmin: cell 1022, theta box 5), negative boxes: 0, NaN boxes: 0;
    on the inner half-line m >= 5.3065, on the outer half-line m >= 3.0888;
    sup b_+ <= 11.2281;  sup |grad rho~| <= 30.4196 (finite cells; -> 0 at both ends);  sup |DU[rho~]| <= 125.7436 (component-sum bound du = |psi_rr| + 2|psi_rth|/r + |psi_thth|/r^2 + |psi_r|/r + |psi_th|/r^2 >= operator norm of DU; its limit at 0 is 2c while the operator norm of DU(0) is c (V069 remark); c_l + sup du is a global Lipschitz constant of V);
    q in [-10.150726, 21.301451] (the exact limits are -A = -10.150725... and D = 21.301450...);  tan(theta) V.grad(theta) in [-0.1387, 31.4522].
  Hence hypothesis (H_m) of Theorem R holds for mu~ with m_* >= 1.0298, and (H_m') of Theorem C' holds for w_a with m_a >= 0.9659 (both for the
  exact modal trial, on the whole plane).
- Hypothesis (Z) outputs (theory author message 12): per-box lower bounds of |V|/r (sqrt(min|q|^2 + min|V_theta/r|^2) on the box) and enclosures of the
  four entries of DV = c_l I + DU (exact polar second derivatives of psi). P = (8.600064, 0) lies in cell 671 (t_a = 2.1507), theta box 0.
  On that box: DV_xx in [9.9588, 10.3327], DV_xy in [-1.7668, 1.8053], DV_yx in [-0.5901, 0.5699], DV_yy in [0.8180, 1.1919]
  (the frozen rates at an exact source are A_P = 2 c_l - 1 = 10.1507 and 1; the box is 0.2 wide in arc length, so the entries vary across it).
  Boxes with |V|/r lower bound < 0.1: 255 boxes, t_a in [2.1315, 2.2116], theta boxes <= 10
  (a neighbourhood of P only); outside them |V|/r >= 0.100068. The per-box arrays VLO, DV are in margin.npz for the
  theory author's choice of neighbourhoods of 0 and P.
- IMPROVED (theory author message 16 item 3; 05:56Z; work/runs/MARGIN_REF/margin.json = production arrays with the 855 cells whose minimum of m or m_a was
  below 2.5 recomputed with adaptive angular bisection to depth 5 (threshold 2.5) and the sharper tail bound |sin(2n theta)/cos theta| <=
  min(2n, 1/min cos theta) in the anisotropic term (the old bound 2n was the source of the 0.97 at r ~ 52 near the x-axis); merge_override.py):
    inf m   >= 2.471224   (argmin cell 525, t_a = 1.4962, theta box 36; the refinement stopped at depth 5 there),
    inf m_a >= 2.500023   (every refined box reached the target 2.5; argmin cell 1351, box 16);
  refined boxes 17242, leaves 133255, negative boxes 0, all leaves finite, 1569/1569 cells, 100416/100416 boxes.
  Second round (06:14Z; targets m >= 2.55, m_a >= 3.0, angular depth 6 on the 1027 cells still below; work/runs/MARGIN_REF2/margin.json):
    inf m   >= 2.482724   (argmin cell 525, t_a = 1.4962, theta box 36: r = 4.46, theta ~ 51 deg; depth 6 reached: a box-width floor),
    inf m_a >= 2.871539   (argmin cell 1563 = the first outer sub-cell [t_+, t_+ + 1/2], theta box 0: limited by the radial width of
                            that sub-cell (h = 1/2), which angular bisection cannot reduce; a radial subdivision of the outer sub-cells would
                            bring it to the far limit 3.0908);
  31127 boxes refined into 263417 leaves, negative boxes 0, all finite, full coverage. These supersede the 1.029821 / 0.965918 of the
  first production run as the certified margins (same inputs and method; the refinement only subdivides boxes).
- Lemma Z inputs (theory author message 14; work/runs/MARGIN/Z0.json, post-processing of the DV boxes): (Z0) delta_0(r_0) = sup over boxes with t_b <= log r_0
  of the Frobenius norm of the entrywise deviation of DV from diag(-A, D) (upper bound from the interval entries): r_0 = 0.05: 4.5895; 0.1: 4.5964;
  0.2: 4.6247; 0.3: 4.6708; 0.5: 4.8166; the largest cell boundary with delta_0 < A = 10.1507 is t_b = 0.9209 (r_0 = 2.5116, delta_0 = 10.1314).
  The 4.59 at small r is the angular box width (pi/128) acting on the O(c) mode sums, not the field (DV -> diag(-A, D) exactly). Alternatively
  |V|/r >= 10.0988 on the inner half-line boxes and >= 10.0947 on all cells with t_b <= -2. (Zb) (work/zrefine.py, V073/V074 repairs of 05:47Z: terminal-leaf bookkeeping, exact rational endpoints, directed q and u bounds exported for every
  positive leaf, containment margin 1e-3 in x and y for the center uncertainty of P; results work/runs/ZREF2/zrefine.json (rect) and
  work/runs/ZREFD2/zrefine.json (disc), copies in artifacts/data/ZREF/). The 255 production boxes with |V|/r lower bound < 0.1 (they contain the
  verifier's 77 zero boxes outside Q, V072) were bisected (theta or t, whichever is longer in arc length, depth <= 9).
  Rectangle Q = [8.100064, 9.100064] x [-1/2, 1/2] (V070: unique zero of V in Q; V071 containment test r- cos th+ >= x-, r+ cos th- <= x+, r+ sin th+ <= 1/2):
  463 nodes, 359 terminal leaves = 34 inside Q + 325 positive + 0 unresolved; smallest positive leaf bound |V|/r >= 2.8297e-04
  (cell 670, t in [2.14874, 2.15065], theta in [0.14726, 0.17181]).
  Disc B_P = B_{99/2000}(P) (theory author's Lemma Z): 595 nodes, 425 terminal leaves = 3 inside B_P + 422 positive + 0 unresolved; smallest positive
  leaf bound |V|/r >= 8.4400e-06 (cell 672, t in [2.15256, 2.15448], theta in [0.021475, 0.024544]).
  With |V|/r >= 0.100068 on all other boxes and >= 10.0946 on the cells with t_b <= -2, |V|/r is certified positive box by box on the closed
  quadrant minus Q (resp. minus B_P): (Zb) holds for both excluded sets.
- Independent checks: the far limits agree with the verifier's exact values (V055): kappa_0 = 49.716 at the origin (our inf over the inner
  half-line boxes of kappa_w is 46.42 with 64 boxes), kappa_inf = 1 + 3 c_l/8 = 3.0908 (our outer half-line value 3.0889 for m, 3.0899 for kappa_w);
  the theory author's grid values (NUMERICAL, team message 7) m_a: 3.09 far, 12.78 at the knot, 49.7 for r < 0.1 are consistent with our box lower bounds.
- Files: work/margin.py, work/encl.py, work/merge_margin.py; logs/margin_A.log, margin_B.log, margin_merge.log; outputs work/runs/MARGIN/.

## C4 addendum (12:45Z): finer radial cover of the first outer sub-cell (margin.py MARGIN_OUTER_EXTRA; work/runs/OUTER_F403; outer_merge.py)
- The production cell [t_+, t_+ + 1/2] (where inf m_a = 2.871539 of C4 was attained, theta box 0) was recomputed as 8 cells of width 1/16 with
  the same enclosures and depth-6 angular refinement (run OUTER_F403, family mode, which refines every box with m_fam < 1.5, i.e. all boxes
  here): m_a >= 3.058366 on [t_+, t_+ + 1/2] (float 3.0583669728; corrected 16:10Z from the rounded 3.058367, which exceeded the float). Combined with the unchanged production arrays elsewhere: inf over the plane m_a >= 2.927096
  (truncated: 2.9270), attained at the production cell [t_+ + 1, t_+ + 2], theta box 0. (Superseded 15:54Z by C4 addendum 2: inf m_a >= 3.000000.) Likewise C7: m_fam(4, 0.3) >= 1.327659 on
  [t_+, t_+ + 1/2], inf over the plane >= 1.250110 (1.2501), same cell and box. Both are limited by the next production sub-cell; a finer
  cover of [t_+ + 1/2, t_+ + 8] would raise them toward 3.06 / 1.33. Data: artifacts/data/MARGIN/family_refined/outer_merge_F403.json.
- Disclosure: the companion run OUTER_MA (non-family mode) had its refinement silently disabled by a placeholder bug introduced at 08:35Z
  (fixed 12:43Z); its bounds (unrefined, 2.871026) are superseded. No certified production value (C4 05:00Z-06:14Z, (Z), C5, C7) was computed
  with the affected code path.

## C4 addendum 2 (15:54Z): finer radial cover of the whole outer region [t_+, t_+ + 8] (work/runs/OUTER_F8 with OUTER_F403; outer_merge2.py)
- Quantity: the same directed per-box lower bounds of m_a (and m) as C4, on the 24-offset outer cover (MARGIN_OUTER_EXTRA = 1/16, ..., 7/16, 1/2,
  5/8, 3/4, 7/8, 1, 5/4, 3/2, 7/4, 2, 5/2, 3, 7/2, 4, 5, 6, 7, 8: 8 cells of width 1/16 on [t_+, t_+ + 1/2] from OUTER_F403 and 16 cells of widths
  1/8, 1/4, 1/2, 1 on [t_+ + 1/2, t_+ + 8] from OUTER_F8, cells 1571..1586 of that cover, work/runs/outer_cells_f8.json), all 64 angular boxes
  refined to depth 6 (MARGIN_REF_THR=99; 4096 leaves per box in OUTER_F8), 160 bits (512 on the non-mid cells), the same exact trial, weights and
  enclosures as C4. Wall time 620 s (OUTER_F8, one process).
- Result: on [t_+ + 1/2, t_+ + 8] the refined bound is m_a >= 3.0368 (OUTER_F8; per cell 3.0368 to 3.0896; old production bound on those four cells
  2.9271) and m >= 2.994240 (float 2.9942407627); combined with OUTER_F403 (m_a >= 3.0584 on [t_+, t_+ + 1/2]) and the production arrays elsewhere (which stand
  unchanged), the plane infimum is inf m_a >= 3.000000 (exact float 3.000000251655344; before 2.9270), now attained as a bound at the production
  cell 1188 (t_a = 5.1695, r about 176), angular box 3, after 31 refinement leaves; 4455 production boxes have refined bounds within 0.01 of 3.
  inf m >= 2.482724 is unchanged (cell 525). The far region is no longer the limiting region for m_a.
- Method and status: directed lower bounds (flo) of the same box enclosures as C4 (logs/outer_f8.log, outer_merge2_f403_f8.log;
  work/runs/OUTER_F8/margin.json, margin.npz, outer_merge2.json; outer_merge2.py replaces exactly the production cells tiled by the new cells,
  asserted; hardened 16:08Z after the second-model referee merge_gram_ref: contiguity and exact tiling of the computed cells, every retained or replacing box
  finite, Delta >= 0 and a_ang <= 17/4, refinement arrays on the base geometry, directed float recomputation of m_fam on unrefined boxes, printed
  bounds truncated toward -infinity; the values were unchanged by the hardening: logs/outer_merge2_f403_f8_v2.log). CERTIFIED by this team as a finite computation with the C4 hypotheses (the dropped-constant conditionality of C4 applies);
  NOT independently verified at the time of writing (the verifier confirmed the earlier addendum as V197).

## C5. Hypothesis (A) axis data, (CB) constants and kappa_* (hypA.py; CERTIFIED by num, 05:10Z, conditional as stated)
- Definitions (S2_L2_THEORY.md 5.2; identities checked by second-model referee (second-model referee/hypA_ids/answer.md) and the verifier (V054)): d(t) = V_2(0, e^t)/e^t =
  c_l - sum_n (-1)^n Pe_n(t); p = 2 V_1/x + V_2/y - 1; a_1 = (q - d)/cos^2 theta = 2 sum (-1)^n Pe_n U_(n-1)(sin theta)^2; a_0 = (p - p_axis)/cos^2 theta
  (hypA.py docstring); M_Q = sup |a_1|, M_P = sup max(e^(-2t), 1) |a_0|; kappa_w = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta) (a.e.; = m_a + b_+).
  Same cover, enclosures and precision as C4; exact angular identities for modes n <= 12, tails by |U_(n-1)| <= min(n, 1/min cos theta),
  |g_n| <= (4n^3 + 2n)/3, |U_(n-1)(cos 2 theta)| <= min(n, 1/min|sin 2 theta|), all in Arb.
- Results (work/runs/HYPA/hypA.json, merged from HYPA_A, HYPA_B; cells_computed = 1569 of 1569; 2262 s):
    d in [5.575203, 21.301451] on the whole axis (inf on the outer half-line: d -> c_l = 5.5754; sup at the origin: d -> D = 21.3015);  sup |d'| <= 5.6012;
    (A) at 0:  sup_(t<=0) |d - D| e^(-2t) <= 0.100883,  sup_(t<=0) |d'| e^(-2t) <= 0.202073  (both attained on the inner half-line; C_left = 0.302956);
    (A) at oo: sup_(t>=0) |d - c_l| e^((1-k)t) <= 89.3351,  sup_(t>=0) |d'| e^((1-k)t) <= 73.3123  (both attained on the outer half-line; C_right = 162.6454);
    (CB): M_Q <= 337.6560 (argmax cell 1091, theta box 49: r ~ 60 near the y-axis),  M_P <= 1075.5156 (the e^(-2t)-weighted part on t <= 0 is 1.0899; the unweighted sup on t >= 0 is 1075.5156);
    kappa_* >= 3.037693 (argmin cell 1135, theta box 4),  sup kappa_w <= 125.4206;  q in [-10.150726, 21.301451].
    Consistency: max over cells and modes of sup |n Qe_n - Pe_n - Pe_n'/2| = 4.09e-35 (the Green data satisfy the defining identity).
- Conditional step: on the inner half-line the exponent-0 constant of d - D is dropped; it is the ball -4.338e-37 +/- 2.045e-35
  and equals c[rho~] - (3 c_l - 1), exactly zero for the repaired trial by the definition of z (V005). The second dropped constant (6(Qe_1 - Pe_1), ball
  0 +/- 2.453e-34) is structural (-6 e^(-2t) A_1 has no constant term; second-model referee and V054).
- Interpretation: positivity of d on the whole axis and the finiteness of the (A) and (CB) constants are the two coefficient obligations of Lemma
  C'1-C'3 (V046, V055); with C4 (m_a > 0) both remaining hypotheses of the theory author's Theorem C' hold for the exact modal trial. The large far
  constants (M_Q, M_P, C_right) reflect the slow decay in n of the far angular modes (a_1 near the y-axis equals 2 sum (-1)^n n^2 Pe_n in size).
- Files: work/hypA.py, work/encl.py, work/merge_hypA.py; logs/hypA_A.log, hypA_B.log, hypA_merge.log; outputs work/runs/HYPA/.

## C6. L_fix section in the theory author's L^2(e^(mu~)) norm (section_l2.py / certify_l2.py; CERTIFIED by num as a finite statement, 05:41Z)
- Objects: operator L_fix h = (V.grad - 1) h + U[h].grad rho~ (no strain term; S2_BASIS_CERTIFICATION.md section 5), exact modal trial; columns:
  the 169 conforming columns of basis.py (q = 3, coarse stride 60, modes m = 0..3, J included; NO tail columns: r^k Theta and KP are outside the
  space); domain and target norm: the spatial L^2 with weight e^(mu~(log r)) (theory author message 5 weight; in the factor modes e^(8t + mu~) dt with the exact
  angular Gram of x^2 y cos 2m theta for h and pi sum_N for the image modes); rows: pi int G_N psi_i e^(8t + mu~) dt for 69 active cubic test
  splines (end splines removed) x 12 output modes; cells split at the mu~ knots so every weight is a single exponential per cell; exact integration,
  256 bits (max Gram radius 2.1e-37); assembly 05:10Z-05:35Z (1490 s, 4 workers; logs/phase2e.log; work/runs/L2fix_M4_s60_o12/).
- Method: as C3 with two-sided exact whitening (05:45Z): the raw Grams span 68 orders of magnitude (inner power columns ~1e-23, far columns
  ~1e28, test splines 1e-20 .. 1e48; raw cond(G) = 3.53e+68), so T_X = L_X^(-T), T_Y = L_Y^(-T) from 140-digit mpmath Choleskys of the exact
  dyadic midpoints are applied in ball arithmetic (G -> T_X^T G T_X, G_test -> T_Y^T G_test T_Y, B_N -> T_Y^T B_N T_X); the generalized singular
  values are invariant. Whitened Grams verified PD: ||E|| = 1.01e-38 (G), 8.56e-45 (G_test).
- Result (logs/certify_l2_v2.log, work/runs/L2fix_M4_s60_o12/certificate.json): float generalized singular values 0.52134, 0.52147, 0.52163, 0.52178, 1.01050, ...,
  largest 146.2153; VERIFIED LOWER BOUND sigma_min(Q_M L_fix P_N) >= 0.510914 (K - s^2 G PSD with ||E|| = 4.41e-12). The weakest direction
  is in the inner power columns in5/in6/in7 (m = 0, 1), i.e. functions concentrated at r < e^(t_-) = 0.0077 where the weight e^(8t + t/4) is tiny; the
  four nearly equal smallest values 0.5213-0.5218 are the four angular modes of that direction, the next value is 1.0105.
- Meaning: the finite section of Theorem R's realization (the first section in a realization where Lemma IV.1 applies) has a verified lower bound
  0.51; by itself this is not a continuum bound (the complement needs the split (S)). Theorem R's coercive margin m_* >= 1.0298 (C4) exceeds the
  section value, consistent with a compact coupling K that lowers the bound. The matrices (exact dyadic balls) are in work/runs/L2fix_M4_s60_o12/
  matrices_dyadic.json.gz for an independent check.

## C7. Near-axis refinement of the decoupled weight-family margin (margin.py MARGIN_FAMILY + family_combine.py; directed lower bounds, 10:09Z)
- Quantity: boxwise lower bounds of m_fam(X) = m_a(X) + (a_ang - 17/4) tan(theta) V.grad(theta) - Delta q(X) 1_{r>=1}, q = V.X/r^2, the exact
  variation of the C4 anisotropic margin m_a for the decoupled weight family (inner radial exponent fixed at 17/4, angular exponent a_ang, far
  shift Delta; theory author team message 26-28, verifier V121 formula), for (a_ang, Delta) = (4, 0.3) and (3.6, 0.3), on the same cover as C4 (1569 radial cells x
  64 angular boxes of [0, pi/2]; exact modal trial, inputs as C1/C4).
- Method: margin.py (ball arithmetic as in C4: Taylor enclosures encl.py on the finite cells, 512 bits on the non-mid cells) forms on every box the
  ball ma + (a_ang - 17/4) tang_hi - Delta q_fam with tang_hi, q_hi the upper ends of the certified enclosures of tan(theta) V.grad(theta) and q;
  q_fam = q_hi on cells inside t >= 0, max(q_hi, 0) on cells meeting both sides of t = 0 (the indicator vanishes on the t < 0 part), 0 on cells inside
  t < 0; the lower end (directed, work/outward.py flo) is the box bound. On the 469 cells with t_a >= 4.5 the theta boxes 56-63 (84.4 to 90 deg)
  were refined adaptively to depth 6 (<= 64 leaves per box) wherever the bound was below 1.5 (runs FAM_4_03_A-D, FAM_36_03_A-D; the
  remaining boxes of those runs are coarse and unused). family_combine.py takes per box max(refined leaf bound, MA_ref + (a_ang - 17/4) TANG_hi
  - Delta q_fam - 1e-12) with MA_ref, TANG, Q the certified per-box arrays of the C4 production (work/runs/MARGIN_REF2/margin.npz); the second
  term is a float combination of directed doubles, the slack 1e-12 covers its rounding (the quantities are O(1..10)).
- Result (artifacts/data/MARGIN/family_refined/family_4_03.json, family_36_03.json; logs/FAM_*.log):
    (4, 0.3):   inf over the plane >= 1.1296 (before refinement 0.7268), attained at the outer sub-cell [t_+, t_+ + 1/2] (r in [3413, 5627]),
                theta box 63 (88.6 to 90 deg); on the refined cells the minimum away from the near-axis boxes is 1.3196 (t_a = 4.50, 5.6 deg);
                negative boxes 0.
    (3.6, 0.3): inf over the plane >= 0.9596 (before 0.2154; 774 refined cells, t_a >= 2.5: runs FAM_36_03_A-F), attained inside the refined
                range at t_a = 5.70 (r = 299), theta box 61 (85.8 to 87.2 deg); unrefined cells elsewhere >= 2.2822; negative boxes 0.
                All values truncated (lower bounds); raw values in the json files.
- Meaning and limits: rigorous lower bounds of the boxwise minima of the exact margin formula applied to the certified box data (conditional on
  the exact normalization as C4). They say nothing about the mapping properties of the new weights (verifier V121/proof 118: the tied family
  with a <= 4 loses the finite-J scalar inverse; the decoupled family needs its own jet-row proofs, theory author message 28). The (4, 0.3) bound is limited
  by the radial width of the first outer sub-cell, like m_a itself (2.8715 there).

## C7 addendum (15:54Z): the finer outer cover and the family (4, 0.3)
- Directed recheck (16:56Z, work/family_recheck.py; second-model referee merge_gram_ref): the whole-plane combination of family_combine.py (float
  arithmetic with a 1e-12 slack on directed box data) was recomputed with every operation rounded toward the valid side (nextafter; Delta
  rounded up where q >= 0 and down where q < 0; c = a_ang - 17/4 exact; no slack; every box finite; refinement arrays on the base geometry):
  m_fam(4, 0.3) >= 1.129601 (float 1.1296010639673741, identical to the family_combine.py value, before the outer-cover addenda) and
  m_fam(3.6, 0.3) >= 0.959670 (float 0.9596701830971922, identical). The C7 statements (truncated 1.1296 and 0.9596) stand.
  logs/family_recheck_4_03.log, family_recheck_36_03.log.
- OUTER_F8 tracked m_fam(4, 0.3) on its 16 cells: refined bound >= 1.340733 (float 1.3407339514; per cell about 1.3407 to 1.4169; old production bound there 1.2501);
  OUTER_F403 gives >= 1.3277 on [t_+, t_+ + 1/2]. Combined with the refined production arrays (family_4_03.json refinement directories A-D),
  inf over the plane of m_fam(4, 0.3) >= 1.250190 (float 1.2501909638; truncated, not rounded; 1.2501 before), now attained at the production cell 1338
  (t_a = 6.3452, r about 570), box 61, inside the near-axis refined range. The outer region no longer limits the family value; a further
  improvement would need deeper near-axis refinement at t_a about 6.3 (not run). Same status as C4 addendum 2 (team-certified, not independently verified).

## N1. NUMERICAL (not a certificate): floating core section of S_1 = T_R + C_R on L^2(w_a), Mh = 2 (fsec.py FSEC_MODE=S1; 09:50Z)
- See S2_BASIS_CERTIFICATION.md 7.3-7.5 and NUMERICS_REPORT 10(b): 42 remainder columns (angular mode m = 1 only), complete 531-mode images,
  Gauss quadrature, double accumulation; generalized singular values 4.1552 (Rayleigh quotient of the computed far-junction direction in [4.137, 4.174] under an
  accumulation-rounding model), 6.08 and 23.3 (undetermined: near-dependent outer power columns), bulk >= 50; artifacts/data/S1/ (Grams, meta, result). Upper bound of the infimum over the subspace only. Assembler repaired 12:35Z (v2, theory author message 38:
  parts/bases/latest checkpoint with a coverage check; the v1 sum double-counted checkpointed cells; s1_robust.py values unaffected); c[h_0] = 0
  values 4.4563, 6.0844, 23.314 (NUMERICAL). Assembler v3 (13:00Z) checks union(done sets) == recorded expected cell set (V188); S1 passes (1569/1569). (CAVEAT 13:00Z, verifier V187/V189: the rounding model covers the accumulation only; the cos^4 divisions (input quotients through a padding-dependent pseudoinverse, about 1e-7 relative in G_Z; image quotients with a worst-case amplification 5.4e10) are not covered, so 'resolved' means resolved with respect to the accumulation rounding only.)

## N2. NUMERICAL: the same section with Mh = 3 (84 columns, m = 1 and 2; 12:35Z)
- 50-digit values 2.3443, 2.9209, 3.5011, 3.8285, 3.9096, ... (the five smallest except 3.5011 undetermined: near-null outer-column directions);
  the 52 pure spline columns give 3.4557, 4.2477, 5.4604 (resolved, well conditioned) against 50.32 (m = 1 splines alone) and 25.47 (m = 2 alone):
  the coupling of the angular modes m = 1, 2 in the bulk r = 18..360 lowers the section value by a factor 15. NUMERICS_REPORT 10(e),
  S2_BASIS_CERTIFICATION.md 7.6; data artifacts/data/S1/S1M3_*.

## N3. NUMERICAL: the same section on the 78 pure spline columns with m = 1, 2, 3 (run S1M4P; 15:43Z)
- Inputs: exact modal trial as in C1; basis = pure spline columns sp4..sp29 (stride 60) in the angular remainder modes m = 1, 2, 3 (FSEC_DROP of
  the '+in', '+out', in5-7, out columns); complete mode set (NMAX 534), Gauss nodes 3/8/16, 256 bits for the node values, double accumulation;
  1569 cells, 4 workers, 10758 s; producer = the 12:41Z fsec.py with pinv input quotients (V187; not frozen: work/runs/S1M4P/PRODUCER_PROVENANCE.md);
  coverage 1569/1569 (fsec_assemble.py v3), never resumed; meta.json unchanged since launch (SHA recorded by the verifier in proofs/198).
- Input Gram against the verifier's exact V202 Gram (640-bit balls): largest entrywise relative discrepancy 7.41e-7 (diagonal of (sp9, m = 3)),
  congruent quadratic-form relative error 2.69e-6 (work/gram_compare.py; floating comparison; logs/s1m4p_gram_compare.log).
- 50-digit generalized singular values: 2.7655, 3.2685, 4.3913, 5.3953, 5.6169, 6.8798, ...; on c[h_0] = 0: 2.7662, 3.2695, 4.3933. Sub-blocks:
  m <= 2 (52 columns) 3.4557, 4.2477, 5.4604 (= N2 pure-spline values); m = 1 alone 50.3201, m = 2 alone 25.4729, m = 3 alone 12.1142; the 60
  columns sp7..sp26 (V210) in the low norms: 2.8648 (m <= 3), 3.7223 (m <= 2), 53.6343 (m <= 1). Weakest vector in the bulk splines sp21..sp27
  with a fixed angular profile (mode coefficients about 1 : 1 : 0.47). The value against the cutoff, 50.32 / 3.456 / 2.766, is not converged.
- Verifier V252 (15:45Z, proof 231): independent parts-only fsum assembly, exact disjoint-union coverage, source and metadata SHA checks,
  640-bit congruence bound: relative quadratic-form input error < 2.688e-6 for all vectors (CONFIRMED); independent floating values 2.765547309,
  3.268491498, 4.391313969, two-mode block 3.455656563, 60-column block 2.864768631 (low norms). OPEN: output pairings, certified singular values.
- Status: NUMERICAL evidence (upper bounds of the infimum over each subspace; accumulation-only rounding model; the division errors of the
  image quotients are not covered, V187/V189). Not a certificate; nothing follows for injectivity or the complement. Data: artifacts/data/S1/S1M4P_*;
  S2_BASIS_CERTIFICATION.md 7.7; NUMERICS_REPORT 10(f).

## N4. NUMERICAL: junction test S1J1 (theory author message 32; Mh = 2, outer power columns attached at t_+ + 1, sp+out dropped; 16:52Z)
- Convention for N1 to N4: "on c[h_0] = 0" means the hyperplane of the stored binary strain row cvec of meta.json, not exactly ker c; the verifier's
  V282 (proof 246) shows that for S1J1 the low-metric projection of that hyperplane onto the exact strain nullspace moves every vector by less
  than 6.244e-16 of its norm (input side only; adopted as a theorem by the verifier's V291 after an independent audit, theory author message 72).
- 38 columns, complete modes (NMAX 530), exact VM templates, 4165 s on 4 workers, coverage 1569/1569, producer frozen (runs/S1J1/PRODUCER_SHA256.txt).
- 50-digit values 4.7481 (weakest direction -0.79 out9 + 0.56 out5 + 0.25 out8, Rayleigh quotient only weakly resolved: [3.7414, 5.5835] under the
  accumulation model), 15.14 and 34.29 (undetermined, same near-null outer-column space), 44.21 (four values below 50, all concentrated in the outer-column coordinates), 51.58; c[h_0] = 0: 4.7482. Without the outer
  power columns 50.32, 51.58, 53.16; pure splines 50.3201 (= S1, S1M4P m = 1). Compared with S1 (junction at t_+): 4.1552 in [4.137, 4.174].
- Input Gram against the verifier's exact V267 export (proofs/239, 640 bits; same meta.json and producer hashes): largest entrywise relative
  discrepancy 6.01e-7 (diagonal of (sp9, m = 1); outer block 1.2e-9; cross block exactly 0), whitened quadratic-form relative error 4.31e-4
  (amplified along the near-null extended columns sp0+in/sp1+in/sp2+in); work/gram_compare_s1j1.py, logs/s1j1_gram_compare.log.
- Reading (corrected after V279): every value below 50 on the m = 1 subspace is concentrated in the outer-column coordinates (not exact membership in their span, verifier
  team message 131), and the smallest moves
  only from 4.2 to 4.7 under the junction shift; the coordinate near-dependence makes the quotients weakly resolved but does NOT show the value
  spurious (V279: the same phenomena occur for a genuine operator minimum). Whether the exact operator is correspondingly small there is OPEN. NUMERICAL evidence only (accumulation model; division errors not covered, V187/V189). S2_BASIS_CERTIFICATION.md
  7.8; NUMERICS_REPORT 10(g); data artifacts/data/S1/S1J1_*.
