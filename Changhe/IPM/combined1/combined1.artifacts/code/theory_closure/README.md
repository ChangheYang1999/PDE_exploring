# the T1/T3 theory worker artifacts: reproduction of every number reported by the T1/T3 theory worker

UTC 2026-10-28T22:38Z (an earlier work session). All paths below are relative to this directory (working file artifacts (not published)).

## Environment

- Python: python3 (system site packages: numpy 2.5.0, scipy 1.18.0,
  mpmath, sympy, python-flint 0.9.0). No lane venv is needed.
- Run with OMP_NUM_THREADS=1, python -B, and PYTHONDONTWRITEBYTECODE=1 (no caches are written).
- Scripts read inputs only from data/ subdirectories here. They write only to stdout, except check_T4182.py,
  c_shift_diag.py and check_T4185.py, which also write a small JSON summary next to themselves (check_T4182.json,
  c_shift_diag.json, check_T4185.json); check_T4185.py reads check_T4182.json, so run_all.sh runs it after check_T4182.

## One command

    bash run_all.sh            # overwrites the stored *.out files next to each script
    bash run_all.sh OUTDIR     # writes the outputs to OUTDIR instead (for comparison)

run_all.sh runs each script from its own directory under taskset -c 50,51 and nice -n 19. The 22:33Z rerun of the
scripts present then took about 5 minutes, most of it six_branch_K.py (about 230 s). Scripts added later are not in
that figure; check_T4397.py alone takes about 2 minutes. The 22:33Z rerun reproduced every stored output byte for byte,
except for one detail: check_T4013_T4017.out, six_branch_K.out and graded_l2.out each carry an appended final line
"rc=0" written when they were first produced.

## Individual commands and contents

Each command is run from the script's directory, for example
`cd closure_calc && OMP_NUM_THREADS=1 python3 -B closure_calc.py > closure_calc.out`.

| script | reproduces | cited in | inputs | time |
|---|---|---|---|---|
| closure_calc/closure_calc.py | A2 framework thresholds (FW-A2-Db 1/1572864 = 6.3578e-7, component bounds, D(a), Dw1, Dw2), optimal-s formula, what-if table | theory_v01 sections 2-4; BASELINE_CLOSURE_AUDIT.md | none | < 1 s |
| closure_calc/tail_budget.py | HEURISTIC tail budget for n-branch far fields (D(b) and graded model) | theory_v01 tail tables | none | < 1 s |
| closure_calc/six_branch_K.py | A2 P33 six-branch bound (K <= 3675) and cutoffs 1315 (rebal), 1021 (the T1/T3 theory worker graded box), 1063 (T4 box), 511 (FW-T-TB-sharp-v1) | theory_v01 necessary conditions; confirmed by T4-040 | data/nb_stableA2_exact.annular.json (copy of A2 certificates/P25_admissible_tail_gap) | about 230 s |
| closure_calc/l2_sector_cost.py | L2 versus Hdot^-1 sector costs, onset radii for 4 to 12 branches, C1-N1-003 (3,1) and (8,0) onsets, Gram check of T4-019 | theory_v01 section R and tail tables | none (E_n copied in the script from the N4 numerical auditor floors.json) | < 1 s |
| closure_calc/bl2_trade.py | (B-L2) trade corollary FW-T-T4L2-bL-v1 (TP-5): EXACT Gram bisection of the largest PD rate mu_lo as a function of beta_L at the sharp and sharpw weights, smallest beta_L with a positive rate (exact 3829321675/5037023232 and 15208393675/44307283968; the printed 8-digit values 0.76023506 and 0.34324816 are truncations below them, so use 0.76024 and 0.34325 as safe sufficient values; T4-113), FLOAT eta table, two exact sharpw instances (beta_L = 7/5, 1), matrix-floor sensitivity (A2 floors, P96 bounds, TP-4 caps) | review set 09 TP-5; theory_v02 | none | < 1 s |
| graded_calc/graded_calc.py | FW-T-TB-graded-v1 comparison-system sensitivities, interval re-check | theory_v01 FW-T-TB-graded-v1 | none | about 40 s |
| graded_calc/graded_instance.py | certified graded instance (s = 5 * 2^-18, mpmath iv), q0 < mH sqrt(m0) | theory_v01; review set 02 R1-005 | imports graded_calc.py | about 2 s |
| graded_calc/graded_l2.py | FW-T-TB-gradedL2-v1 instance (28 x D(b) components), point gaps for the T4-019 ball and gradedL2 box, HEURISTIC L2 tail table | theory_v01 FW-T-TB-gradedL2-v1 (confirmed by T4-039) | ../checks/data/N4_cartesian_witnesses.json | about 5 s |
| checks/check_T2R1_T4007.py | T2-R1 Gram positivity (rate 297/1000), T4-007 rational relaxations | review set 01 R1-001..003 | none | < 1 s |
| checks/check_T4013_T4017.py | T4-017 symmetric point bound checks and gaps, T4-013 rational box reproduction | review set 02 R1-004, R1-005 | data/N4_cartesian_witnesses.json, data/rational_box.json; imports ../graded_calc/graded_calc.py | about 12 s |
| checks/check_T2R3.py | exact certificate of T2-R3 (Gram minors, row sums 400.99788 < 401 and 396.66411 < 397, beta, eta, c_s r/2), requirement roundings, point gaps, FLOAT weight optimum and joint-Gram variant | review set 03 R1-006 | data/N4_cartesian_witnesses.json | about 2 s |
| checks/check_T4041.py | T4-041 review: U kernel and contact term, kernel (2) coefficient 1/4, (5), integrals of (3), block formulas (exact and FFT), Sym Q = P + K and K_b = S_b - b with exact rational matrices, I0, FLOAT weighted block norms and sampled pointwise bounds, size of (3) | review set 04 R1-008 | none | about 18 s |
| checks/check_T4051.py | T4-051 review: arb reproduction of all scalar constants (alpha, m2, K_X < 11.490384, 2 c_s R < 0.012467), certified operator-norm form ||N|| <= 7.6682217 (eta = R/7.6682), K_L table with re-optimized rational (s, R), exact checks of (6), c_s, Young (9), root bound, origin identity and M1(0); FLOAT (6) multiplier and comparison-system decay | review set 05 R1-009 and TP-1 | none | about 2 s |
| checks/check_T4054.py | T4-054 review: exact polar blocks and d-bar examples, weighted ODEs (5)-(6), identities (7)-(10) with Re<H',pH> cancelling, K_n monotonicity, symbol identity; FLOAT weighted block identity residuals, sharpness packets, S1 far-field and discretized velocity constants; TP-2 exact rational Schur certificates of the S1 velocity constant C_S1(a) (1.616466 at a = 6/5) | review set 06 R1-010 and TP-2 | none | about 25 s |
| checks/check_T4047.py | T4-047 review: principal symbol, lambda formula, S1 reflection covariance, contact kernel, drift b (sympy); FFT contact term and S1 packet quotients on state131 (FLOAT); own arb evaluator of the exact state131 fields validated against the A2 point enclosures and the seven T4-047 points; TP-3 obstruction map in (a, R) with 58 arb-certified entries and the far-field data | review set 07 R1-011 and TP-3 | data/state131_exact.json, data/state131_field_points.json, data/T4047_points.json | about 35 s (two timing lines in the output vary between runs) |
| checks/check_T4060.py | T4-060 review: expansion (4), leading transport coefficient (6) and the cross-term cancellation, weighted identity and Poisson bracket for general direction and weight, U cone bound, c[g] = 1 (sympy); arb origin data of state131 (normalization residual, M_q(0)); FLOAT FFT packet quotients in H^q; TP-4 map of inf lambda_min(M_(q,w)) with arb values at the minimizing grid points; exact identification of the A2 matrices (B1), (B4), (B5), (B6), (W2) and the P95 closed forms | review set 08 R1-012 and TP-4 | data/state131_exact.json | about 10 s (the total-time line varies) |
| checks/check_T4097.py | T4-097 review: Wirtinger mode formulas of the Beurling transform and the two convolution solutions, symbol identity -(1+B)/2 = U2 + i U1, (L_inf + beta_inf) h_N, low density limit, plateau scaling and the (5)-(6)-(7) algebra (sympy); FFT check of U[h] vanishing inside the support and of the mode formulas (FLOAT); ceilings (8), lower bound (5) and the FLOAT minimum of the (7) squared ratio; finite angular content and r^-delta decay of u/r and D rho for state131 (FLOAT, own evaluator) | review set 09 R1-013 and the T4-099 chain | data/state131_exact.json | about 18 s, about 2 GB (the total-time line varies) |
| checks/check_T4107.py | T4-107 and T4-112 review: polar Laplacian formula T_(d,1)^2 P - n^2 P (sympy), change of variables of the z-integral (mpmath quadrature), plateau exponents and core/shell weight comparisons, the seven-cell d2 cover from the seven T4-107 norms (values lowered by 1e-20), log-convexity exponents, A = 1 + 1/c < 7/4 | review set 10 R1-014 | none (the seven norms are copied in the script from the T4 theory auditor verification/d2_2048.json) | about 10 s (the total-time line varies) |
| checks/check_T4127.py | T4-127 review: recomputes the four selected-mode cell ratios (S = {1, 3}) for C1-N1-007 from the stored T4 mode norms and prints the FLOAT pointwise ratios for S = {1, 3} and S = {1, ..., 15} | review set 11 R1-015; theory_v02 sections 5 and 9 | checks/data/T4127_combined_cover.json | under 1 s |
| checks/check_T4128.py | T4-128, T4-130/132, T4-133 (BALL_LDL) and T4-138 review: exact sympy checks of the Poisson family identities, H_0, G_00, C_00, the pairing kernels, the divergence identity, the Beta moments, the angular integral formula, the angular-family parities and the LDL congruence; FLOAT random-matrix tests of the three abstract inequalities | review set 12 R1-016 | none | about 7 s |
| checks/check_T4146.py | T4-145, T4-146 and APPLICATION_007 (T4-147) review: exact sympy checks of the log-chart conjugation, the interior profile phi_sigma, |symbol U|^2 = p, the origin trace (L h)_y(0) = a0 c[h], the critical-point polynomial of H and the ceiling slope; 300-digit interval enclosures of s*, H(c - 1) < 57/50 and the seven 007 cell ratios | review set 13 R1-017 | checks/data/T4127_combined_cover.json | about 3 s |
| checks/check_T4153.py | T4-153 review: exact sympy checks of the q = 3 boundary values and strip, the zero profile, the scaling exponents of E_eps (with an exact S1 example for k = 0 to 3), the localization identity (7) and the sign of c[g] | review set 14 R1-018 | none | about 9 s |
| checks/origin_inv_table.py | theory_v03 section 5 NC-T-ORIGIN-INV: directed values (mpmath iv, 60 digits) of the T4-146 ceiling H(c - 1) beta_inf(a)/(1 + a), the T4-097 ceiling B(a) and the combined N_a ceiling at eleven values of a (the cell thresholds); s*, H(c - 1), the M floor at s* and the FLOAT crossover a | theory_v03 section 5 | none | under 1 s |
| checks/check_joint_ceiling.py | R1-019 (review set 15): The T2 theory worker joint ceiling (the review of T4-146 remark R1) from both actual-inverse floors M >= 1/(c - 1 - s) and M >= 1/beta_inf(a); exact case analysis (sympy), switch a = 1.27577707759, directed joint Y and N_a ceilings at twelve values of a, FLOAT ratios to the T4-097 ceiling; 6 checks | `OMP_NUM_THREADS=1 python3 -B check_joint_ceiling.py > check_joint_ceiling.out` (from artifacts/checks; under 2 s) |
| checks/check_T4170.py | R1-020 (review set 16): FLOAT sanity check of T4-170 Theorem C (compact Lipschitz Lindley weight) on a toy field: bounds 0 <= psi <= C, support in r1 <= |X| <= R, Lipschitz bound (C3), g >= theta_1 - lambda, (C4); 5 checks, FLOAT only | `OMP_NUM_THREADS=1 python3 -B check_T4170.py > check_T4170.out` (from artifacts/checks; about 20 s) |
| checks/check_T4182.py | R1-021 (review set 17): independent numerical review of T4-182, the 15-term rational span weak probe for candidate 007 (a = 0, C_U = 1): fields from the N1/N2 numerics worker snapshot with the T2 theory worker weighted_weak_sharp.py code, pairing, ||M_phi||_2, ||phi |D rho| ||_2 compared with T4, own bisection certificate of H, radius > 7868527/25000000000; arb (certified). Inputs data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json, data/T4182_a0.json (sha256 checked); writes check_T4182.json | `OMP_NUM_THREADS=1 python3 -B check_T4182.py > check_T4182.out` (from artifacts/checks; about 18 s) |
| checks/c_shift_diag.py | theory_v03 section R (Lemma S remark): c-direction diagnostic for candidate 007. At fixed rho the pairing with phi_P = y W^2 P(t) is I_P + (c' - c) J_P; prints I_P, J_P and dc_P = -I_P/J_P for P = t^k (k = 0 to 8, 128) and the T4-182 vector. arb values; the interpretation is a diagnostic, not a bound. Reuses the field code of check_T4182.py (same data/ inputs); writes c_shift_diag.json | `OMP_NUM_THREADS=1 python3 -B c_shift_diag.py > c_shift_diag.out` (from artifacts/checks; about 15 s) |
| checks/check_T4185.py | R1-022 (review set 18): independent numerical review of T4-185, the angular mode-7 weak probe phi_7 = r W^2 P(t) sin(7 theta) for candidate 007 (a = 0, C_U = 1): own sine/cosine series and Parseval for ||M||_2 and ||phi D rho||_2, pairing both directly from the sin(7 theta) part of F and as -int rho M, pointwise check against Cartesian central differences, n = 1 reproduction of check_T4182.json and N4-091, own bisection certificate of H, radius > 4769166867/10^12; arb (certified). Inputs as check_T4182.py plus data/T4185_n7_a0.json (sha256 checked); reads check_T4182.json; writes check_T4185.json | `OMP_NUM_THREADS=1 python3 -B check_T4185.py > check_T4185.out` (from artifacts/checks, after check_T4182.py; about 35 s) |
| checks/theta0_007.py | R1-023 (review set 19) remark R2: prints the leading far-field profile Theta_0 = sum_l R_(0,l)(1) sin(l theta) of candidate 007 (FLOAT evaluation of the exact snapshot polynomials; R_(0,1)(1) = 18.5678222975, so Theta_0 is not identically zero). Uses the head of check_T4182.py. Writes no file. | `OMP_NUM_THREADS=1 python3 -B theta0_007.py > theta0_007.out` (from artifacts/checks; about 2 s) |
| checks/check_T4199.py | R1-024 (review set 20): exact side conditions of T4-199 (potential-to-density injectivity) for candidate 007: every one of the 2982 snapshot generators is H_m (1+r^2)^(p_j-m) T(t) with j in 0..7, integer m >= 0 and polynomial T (mono or leg, no explicit p, no legqs); c, gamma, delta, p_j recomputed as fractions and equal to the T4 theory auditor parameters.json; d = 3 + gamma < 4; all p_j and all 28 differences p_j - p_k nonintegral (exact). Inputs data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json and data/T4199_parameters.json (sha256 checked). Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4199.py > check_T4199.out` (from artifacts/checks; under 1 s) |
| checks/check_T4205.py | R1-025 (review set 21): FLOAT illustration (mpmath, 30 digits) of T4-205 bound (1), ||d_gamma^N T_gamma||_(E_b)^2 <= pi (2N)!/(2 eps)^(2N+1) for Theta = sin(theta), gamma = 1/c, eps = 0.05 and 0.25, N = 0..4, and of the growth of the partial E_a norms of T_gamma - chi r^gamma0 P(log r) Theta at a = 0 and a = 1 + gamma. Not part of the proof. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4205.py > check_T4205.out` (from artifacts/checks; about 3 s) |
| checks/tail_profiles_007.py | R1-025 (review set 21) remark R3: exact test that the far-field branch profiles Theta_j = sum_l R_(j,l)(1) sin(l theta), j = 0..7, of candidate 007 are nonzero (fmpq), with exponents 1 - (j+1) delta. Uses the head of check_T4182.py. Writes no file. | `OMP_NUM_THREADS=1 python3 -B tail_profiles_007.py > tail_profiles_007.out` (from artifacts/checks; about 2 s) |
| checks/check_T4206.py | R1-026 (review set 22): FLOAT physical-space check of T4-206, ||w D^k U[h]||_2 <= sqrt(1 + 2/(k+1)) ||w D^k h||_2 (centrally odd h; 1 + 2/k for a centrally even h), k = 0, 1, 2, six Gaussian test functions; U and D^k by FFT on [-L, L)^2, (N, L) = (1024, 48) and (2048, 96), weighted norms as Riemann sums (the moment identity (4) is not used). Not part of the proof. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4206.py > check_T4206.out` (from artifacts/checks; about 50 s) |
| checks/t4206_angular_sup.py | R1-026 (review set 22) remark R2: FLOAT angular constant Lambda_k (largest generalized eigenvalue on odd modes n <= 21, 41, 81, 161) that gives the sharp constant sqrt(max(1, Lambda_k)) in T4-206 (1); not certified. Writes no file. | `OMP_NUM_THREADS=1 python3 -B t4206_angular_sup.py > t4206_angular_sup.out` (from artifacts/checks; under 1 s) |
| checks/check_T4222.py | R1-027 (review set 24): exact checks for T4-222. First sine harmonics R_(j,1)(1), j = 0..7, of the 007 branch profiles from the raw density generators (fmpq), compared for exact equality with the T4 theory auditor canonical-potential values in audit/theory_audit/research_code/dilation_chart_audit/verification/result.json (read only); exact dimension thresholds 4g-2 < 3g-1 < 2g < 1+g; e_4 < -1; det(z_i^k - 1) = 288 for z = 2..5. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4222.py > check_T4222.out` (from artifacts/checks; about 2 s) |
| checks/check_T4211.py | R1-028 (review set 24): T4-211 checks. Symbolic leading linear matrices of the five Taylor directions (c, a free); exact squared density L2 norms / pi of eta_(i,j) by three polynomial derivative steps and beta moments, compared exactly with audit/theory_audit/research_code/taylor_projection/verification/result.json; the triangle bound sum |t_i| B_i with the T4 theory auditor parameters (read only) at 60 digits. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4211.py > check_T4211.out` (from artifacts/checks; about 1 s) |
| checks/check_T4229.py | R1-029 (review set 25): exact sympy checks of T4-229 section 3 on random rational data: ker of the pullback normal matrix equals ker K, consistency, K z = w* for two onto parameterizations, the Euclidean damping counterexample (1/2, 2/3), and the lambda -> 0 limit (G-minimum-norm least squares). Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4229.py > check_T4229.out` (from artifacts/checks; about 2 s) |
| checks/check_T4234.py | R1-030 (review set 26): checks of T4-234 with exact rational Fourier arithmetic and 40-digit mpmath Cartesian differentiation: exponent identities, dilation weights z^(j+1), the angular Poisson equation (1), velocity (5), residual expansion (8), an incompatible Theta_1, potential endpoint formulas. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4234.py > check_T4234.out` (from artifacts/checks; about 2 s) |
| checks/check_T4235x.py | R1-030 B: raw-generator cross-check of T4-235 for 007 (data/c1n1_007_...json via the head of check_T4182.py): Psi_j solves (1), j = 0..3, and recurrence (4) from Theta_0 alone reproduces Theta_1..Theta_3 exactly. Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4235x.py > check_T4235x.out` (from artifacts/checks; about 2 s) |
| checks/check_T4251.py | R1-031 (review set 28): T4-251 affine lift. Part A, symbolic in c and a with a general even-even degree-8 potential jet: strain row, exact quadratic expansion of C, block lower triangular Jacobian with diagonal 24(a-4c+2), -240, K, -480c, -1344, the lift (u0, v0, w0), unique nonlinear repair eta, affine equation (1) and nonlinear defect (2), tail identity. Part B, exact at c_007: tau and z parameters, 15 canonical tau coordinates and tail rows, B_ij^2/pi by Beta integrals, arb bounds 1.3465e-26 and 3.4237e-12. Writes no file. | review set 28 R1-031; theory_v04 section 2.1 | data/T4251_inputs.json (copy of fields of the T4 theory auditor taylor_projection and affine_taylor_lift files; source sha256 inside) | about 6 s |
| checks/annulus_admissible.py | theory_v04 R2 item 6 and THEORY_FINAL 2.7 (repaired per T4-278): Lemma A bound (n0/R_out)^2 for corrections supported in 20 <= r <= 32 with odd modes n >= 19, the sharpw fixed-ball L^2 radius at most 1.312585972e-6, the conservative family ceiling below 2.839272409e-6 (uniform comparison constant 1 - (48/25)/1024), the graded bound 50/(651 sqrt(28248)) < 25/54684, and the HEURISTIC decaying-weight extrapolations (1.638e-4, 4.335e-4, 2.169e-3; upper values rounded up). Exact fractions and floats as labelled. Writes no file. | `OMP_NUM_THREADS=1 python3 -B annulus_admissible.py > annulus_admissible.out` (from artifacts/checks; under 1 s) |
| checks/check_T4281.py | R1-033 (review set 30): review of T4-281 (no compactly supported L^2 correction): part A sympy check of the kernel step (K, polar form, DK^T DK = I/(pi^2 r^6), disk moment, constant 4 sqrt(2/pi)); part B exact (fmpq) first descendants of 007, 013 and 014 from the raw the N1/N2 numerics worker generators via the head of check_T4182.py: l* = 4, lower descendants zero, e = 1 - 4 delta - 2 > gamma - 4, exponent noncoincidence; part C comparison of (c e - 1) D_(4,n) with the N1/N2 numerics worker sector tables. Inputs the three generator files and three sector tables in data/ (sha256 checked). Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4281.py > check_T4281.out` (from artifacts/checks; about 11 s) |
| checks/check_T4295.py | R1-034 (review set 31): review of T4-295 (branch-3 potential correction (6) of the T4 theory auditor research/forced_integrable_tail) and check of the T2 theory worker the review of T4-281 R2, for 007, 013 and 014 from the raw the N1/N2 numerics worker generators via the head of check_T4182.py: part A own exact far-field residual sectors (exponent >= -7/2) against the N1/N2 numerics worker sector tables; part B the correction, A1_m and correction terms against the T4 theory auditor data files, branch and origin checks, residual sectors after the correction (first nonzero (9,0), epsilon_1); part C R2 endpoint fit before and after; part D Arb ||eta||_2. Inputs the three generator files, three sector tables and data/T4295_*_tail_repair.json (sha256 checked). Writes no file. | `OMP_NUM_THREADS=1 python3 -B check_T4295.py > check_T4295.out` (from artifacts/checks; about 2.5 min) |
| checks/check_T4314.py | R1-035 (review set 32): review of T4-314 (far-out potential tail repair, the T4 theory auditor research/far_out_tail_repair): exact exponents q = 4 gamma - 5, 5 gamma - 6, 2q - 1, 1 - 9 delta and the norm-scaling exponents; sympy Fourier check that v = (-d_y psi, d_x psi), psi = d_x d_y chi, is the IPM multiplier velocity of h = -d_y Lap chi; mpmath (40 digits, FLOAT, not interval) C_(0,0) = 215936.9 for the 007 profile, direct quadrature of ||h_L||_2 at L = 2, 4 against L^(q+1) C_(0,0), angular norm 810.545 of the r^q profile, the L for ||h_L||_2 below 1e-3 and 1e-6 | review set 32 | checks/data/T4295_007_tail_repair.json | about 35 s |
| checks/check_T4322.py | R1-036 (review set 33): review of T4-322 (no density gauge in the radius-scaled spaces, the T4 theory auditor research/scaled_rank_audit): census of the 016 and 017 generator shapes against old_basis.json; exact nonintegrality of the 8 p_j and 28 differences; sympy pole order N + 4 and coefficient (1) at v0 = -1/(R0^2 - 1) for all 84 (m, N) at R0 = 25 and 50, built from the N1/N2 numerics worker legqs definition; the r^17 sin(17 theta) density coefficient of G_190 | review set 33 | checks/data/T4322_shapes.json (written once by checks/extract_T4322_shapes.py from audit/theory_audit/research_code/scaled_rank_audit/data; not part of run_all.sh) | about 20 s |
| checks/check_T4359.py | R1-037 (review set 34): review of T4-359 (annular moment adjustment, the T4 theory auditor research/annular_moment_adjustment): exact sympy checks of the mode-1 radial solution (5), the derivatives of y/r^2, the polar components, the endpoint expansion (4), the scaling exponents and C_w = 819257/25; FLOAT log-kernel quadrature of U[f] off the support (interior zero, exterior dipole), of the potential against (5), and of U[h_R].grad rho for an exact power-law rho | review set 34 | none | about 7 s |
| checks/check_TP6.py | R1-038 (review set 35, TP-6, CLAIMED): exact screening radii d_j - b for the registered snapshots and the three ceilings; exact identities D_delta = 5c - 1 and 1 - c q* = 4c; mpmath interval bounds for Rmax(b), Emax(b) and 33919 Emax(b) (velocity-constant threshold of the T4-351 test) and a recheck of the T4-351 cap 9.28e-11; the Kantorovich thresholds 33917/2 and 1/33917 | review set 35 | none | about 0.1 s |
| checks/check_T4372.py | R1-039 (review set 36): independent review of T4-372 (sharp first-moment inequality with a homogeneous amplitude bound, the T4 theory auditor research/sharp_amplitude_moment), written from the PROOF text only. Part A, exact sympy in d > 0: exponent identities, radial integrals of the extremizer at d = 1/2, 2 and the campaign d, the elimination to Csharp beta^theta H^(1-theta), D0 = (d+2) C0/d, the split bound minimum Csplit, and the pointwise maximizer on rational grids. Part B, mpmath interval arithmetic at 60 digits: exact theta and nu at the campaign d, J_nu, C0, Csharp, Csplit and Csharp/Csplit with directed decimal rounding, and mu < 5.04423. Part C (FLOAT diagnostics): 2D quadrature of the extremizer at three d, Gaussian test ratios. 26 checks, ALL PASS (output check_T4372.out) | review set 36 | none | about 15 s |
| checks/check_T4381.py | R1-040 (review set 38): independent review of T4-381 (lower bound for every universal velocity constant in T4-335 (1), the T4 theory auditor research/universal_velocity_lower), written from the PROOF text and T4-335 section 1 only. Part A, exact sympy: H_q = 1 for the test h = y(1+r)^(q-1)/a (chain-rule gradient, cross-checked), the moment 6 pi/(a^2(a-1)(a-2)(a-3)), the mode-1 Green formula, the two tails, the Hessian velocity of y r^(q+1), the dipole -DK(X)M, K = (G_xy, -G_xx), |(6)| = Etest at pi/4, the shape integral, Etest exact at the campaign q. Part B, mpmath interval arithmetic at 60 digits: Etest enclosure, the 24 T4-380 thresholds (agree with its result to 1e-40), the crude and shape caps at E = Etest, the consistency with R1-038 Emax(b), and the cap with the T4-351 H0 only. Part C (FLOAT): the exact remainder ratio along theta = pi/4 at r = 10^3 to 10^6. 25 checks, ALL PASS (output check_T4381.out) | review set 38 | data/T4380_inputs.json (fields copied from the T4-380 result; source sha256 inside) | about 5 s |
| checks/check_N4refdiff.py | R1-041 (review set 39): independent review of the N4 numerical auditor reference-difference lemma (audit record reference_difference, proof, sufficient condition (P) for hypothesis (S) of R-SCREEN), written from the PROOF text only. Part A, exact: 2/5 < delta < 1/2 and the omitted density exponents below -1; u = (psi_xy, -psi_xx) with Lap psi = rho, Lap V = (g_xy, -g_xx), div V = 0; the Fourier symbols (-R1R2, R1^2) and their bound 1; the divergence form of the equation; the leading coefficient 1 (q = 0) or 0 (q > 0) of five sample generators; tau_R = t/(1+(R^2-1)v) and the radial measure; the derivative identity behind the J_k recursion. Part B (FLOAT): J_1 = 2F1/(b+1) and the recursion against quadrature; decay rates and V = U[g] (mode-1 Green potential) for a synthetic pair satisfying (P). 11 checks, ALL PASS (output check_N4refdiff.out) | review set 39 | none | about 20 s |
| checks/check_T4397.py | R1-042 (review set 40): independent review of T4-397 (the universal velocity lower bound persists in every fixed fractional ball X_(s,w), the T4 theory auditor research/fractional_ball_velocity_lower), written from the PROOF text, the T4-381 PROOF and source/sharp_space_PROOF.md only. Part A, exact sympy: the weight inequality, heat-kernel moment, Bessel multiplier, t-integral, (1+x)^(2/5) <= 1+x^(2/5), the sqrt(2) trace contraction, J^s = J^(-alpha)(1-Delta), scaling exponents, polar gradient and H_q bounds, the y-axis limit, c[F sin(theta)] = -F'(0)/4, the slopes giving c[k_R] = 0, the large-r expansion, the leading nondipole potential, |W(pi/4)| = Etest exact. Part B, python-flint arb at 200 bits: C_s(1/5184) = 4.468299565794177..., the bump-gradient constant. Part C (FLOAT): int omega G_alpha against its bound; A_k, B_k, D for the sharpw parameters, X(b), and the first R = 2^j (R = 512) putting k_R in the sharpw X and L2 balls. 24 checks, ALL PASS (output check_T4397.out) | review set 40 | none | about 2 min |
| checks/check_T4410.py | R1-043 (review set 41): independent review of T4-410 (velocity remainder with unequal decay weights, the T4 theory auditor research/two_weight_velocity_remainder), written from the PROOF text, the T4-335 PROOF and the review of T4-402 section 4 only. Part A, exact sympy: K = 1/(2 pi z^2) and its derivative norms, the local integral and L r/(4B) = k r^eps, the annulus, far, moment and Taylor constants, J' and the (4) identity, sup |r chi'| = 4/sqrt(3), the mode Green formula (generic f, symbolic n) and its exterior forms, the Hessian magnitude n(n+1) r^(-n-2), the per-mode error, the polar gradient of h_b, the lower bound lam1 = 1/2 + 5 2^(1-q). Part B, python-flint arb at 200 bits: C_a and L_a at a = q - delta, r_beta and Kcrit for 007 / 013 / 014 and the four targets (sharpw values agree with the review of T4-402 to 0.1), the T4-410 bound >= 3.1635 H on [L0, 13761.58] and >= 2.7473 H on [L0, 18860], the radii where the A_in part reaches each room, J(R) >= 51.67 Kcrit (4.73 with the factor 2^(-a) removed), the (F3) factor < 23.14, and the radius-dependent Eeff >= 2.496 and >= 1.7277. Part C (FLOAT): the cutoff model error against (5) at r = 4 to 400; the A_in part for a tail list with exponents near q + 5. 22 checks, ALL PASS (output check_T4410.out) | review set 41 | data/T4380_inputs.json | about 20 s |
| checks/check_R1044.py | R1-044 (review set 42): the T4-410 remainder with the T4-335 (7) tail list at every starting radius R in [L0, r_beta], without A_in and with any outer factor >= 1, written from the T4-410, T4-335, T4-380 and T4-421 PROOF texts only. python-flint arb at 200 bits, no FLOAT step: the identities q = 1/c - 4, delta = 1 - 1/c, D = 5c - 1; lam1 > 109.6 and kap/(kap + delta) > 0.908; for 007 / 013 / 014 and the four targets, the lower bound lam1 E g0/(D r_beta^delta) (E >= 0.793, V >= 0) against Kcrit/H in constant use (> 3.756) and radius-dependent use (ratio > 4.34), and with the universal fallback min(0.793, ...) (Eeff > 0.7929 > 0.7851); the largest necessary kernel constants Lam_max for Eprof = 0, 93/250 and 583/1000, with and without the fallback (all below lam1/3.75, at most 28.92); a conditional V-term-alone line (V >= v0). 7 checks, ALL PASS (output check_R1044.out) | review set 42 | data/T4380_inputs.json | under 1 s |
| checks/check_T4425.py | R1-045 (review set 43): independent review of T4-425 (radial averaging does not rescue the current two-weight remainder, the T4 theory auditor research/radial_averaged_remainder_obstruction), written from the PROOF text only. Part A, exact sympy: kappa = 1 - q = 4 + delta and D = c kappa; Emin = (-q-1)/(2(-q)(-q-3)) equals Etest of T4-381 exactly; 2^(3-q) + 2^(1-q) = 5 2^(1-q); the ray integration of c r h_r - h = f; the two forms of the averaging formula; the operator fixes constants; both branches of T[e_min], continuity at r_u and monotonicity. Part B, python-flint arb at 200 bits: lambda > Emin > 0.79303, r_u = 302748.40..., T[e_min](18860) = 0.79303619..., for 007 / 013 / 014 and the four targets 5 < r_beta < 18860 and Kcrit/Phi < 0.785064 < T[e_min](18860), the 1.747261 averages 1.745480614 and 1.727790118, and the A_out-only extension (R1-045 R1) with averaged floor > 0.79303648. 16 checks, ALL PASS (output check_T4425.out) | review set 43 | data/T4380_inputs.json | about 1.3 s |
| checks/v08_factors_007.py | theory_v08 section 1: the failure factor at candidate 007 of each failed test for a specified certificate (24 rows: distance, smallness, origin inverse, universal and profile velocity constants, remainder rooms, radial average, kernel constant), as p/t rounded down at the displayed precision, 10^(-k) floor(10^k p/t), with p a cited lower bound of the quantity proved for 007 and t a cited upper bound of the threshold; exact fractions, no FLOAT; revision 2 corrects S2 to the sharp norm lower comparison 516.9717852723 (the T4 theory auditor T4-437; revision 1 had sha256 prefix c458e24e) | theory_v08 section 1, THEORY_FINAL section 9.2 | cited bounds only (in the script) | < 1 s |
| checks/h18_table_ratios.py | H18 falsification check (the coordinator 13:41Z item 11): every ratio of the THEORY_FINAL section 7 distance table (displayed distance floor over the family ceilings 3.7930e-6, 2.8496e-6 and 25/54684) is recomputed with exact fractions; each displayed ratio must equal the exact ratio rounded down at the displayed precision | THEORY_FINAL section 7, team note v48 item 3 | ../THEORY_FINAL.md (the table itself) | < 1 s |
| checks/row_refs.py | Pre-freeze consistency check (THEORY_FINAL against the closure matrix): every reference "C1-N1-0XX ... row N" or "rows N and M" in THEORY_FINAL must point to a matrix row whose FW or candidate cell names that snapshot; reading only, no number is computed. Default matrix since the final THEORY_FINAL (18:25Z): the frozen v170 copy, against which the final gives an output byte-identical to the stored one. The stored output was made with THEORY_FINAL draft 58 and the frozen matrix v157 copy (83 references, 0 mismatches; draft 59 with the same copy gives a byte-identical output; draft 57 with the v157 copy gave 83 and 0; draft 56 with the v155 copy gave 83 and 0, draft 55 with the v153 copy 83 and 0, draft 54 with the v151 copy 83 and 0, draft 53 with the v146 copy 82 and 0, draft 52 with the live matrix v140 83 and 0); it changes when either input changes. Since draft 53 the default matrix is a frozen copy, not the live file | THEORY_FINAL sections 0, 1, 7 and 11 (row references) | ../THEORY_FINAL.md, checks/data/closure_matrix_v157.md | < 1 s |
| checks/h18_verdicts.py | H18 check (the coordinator 14:29Z, the T1/T3 theory worker line): every candidate verdict of THEORY_FINAL sections 0 and 7 against the closure matrix row by row. Part A classifies each matrix row whose candidate column starts with a candidate ID (RULED OUT, OPEN, other); Part B checks the hand-coded claims of drafts 48 to 50: those of draft 46 with 017 and row 106 added to the dyadic list, and since draft 53 028 (rows 107 and 108) in the OPEN list (161 claims; stored output: draft 58 against the v157 copy); Part C prints sentences that put a candidate next to OPEN while all its rows are RULED OUT, or the reverse; Part D checks the scope of the 001 to 004 statements (001 in no sweeping list; since draft 53 the separate 001 statement must name both reasons of row 35, framework inapplicability and the affine L^2 exclusion at every real c, T4-471; 002 to 004 carried beyond their specified balls only by the T4-068 distance rows of section 7). Reading only, no number is computed. Default matrix since the final THEORY_FINAL (18:25Z): the frozen v170 copy, against which the final gives an output byte-identical to the stored one. Stored output: draft 58 against the frozen v157 copy, RESULT PASS, identical to the draft 59 output against the same copy, the draft 57 output against the same copy, the draft 56 output against the v155 copy, the draft 55 output against the v153 copy, the draft 54 output against the v151 copy and the draft 53 output against the v146 copy (draft 52 against the v140 copy and the draft 46 to 51 runs against the v135, v137, v138 and v139 copies, with the claims of those drafts, also passed) | THEORY_FINAL sections 0, 7 and 11 (errata 77, 80, 81) | ../THEORY_FINAL.md, checks/data/closure_matrix_v157.md | < 1 s |
| checks/check_T4458.py | Review R1-046 of the T4 theory auditor T4-458 (C1-N1-001 has no stationary correction in its affine L^2 class): Part A checks the polar formulas (3), (4) and (6) of the PROOF exactly against Cartesian differentiation (sympy, symbolic radial exponent, sample frequencies); Part B recomputes from the raw generator file, by direct differentiation of homogeneous functions r^p F(theta) with exact Gaussian-rational Laurent coefficients, the leading densities G_0 and G_1 and the leading residual coefficient E = (c_0 q - 1) G_1 + u_0 . grad rho_0 at q = 2 gamma - 1, and compares them exactly with the T4 theory auditor table (E has sine modes 21 to 39 only, E nonzero, q = 427123167131315/4076476460239181 with 0 < q < gamma < 1, every other exponent label below q); 912 checks | review set 44 (R1-046), THEORY_FINAL sections 0 and 7 | checks/data/C1-N1-001_raw.json, checks/data/T4458_leading_coefficients.json | < 5 s |
| checks/check_T4462.py | Review R1-047 of the T4 theory auditor T4-462 (weight-uniform necessary budgets of the T2-R3 and TB-sharp Gram schemes): (A) the determinant (4), the numerator identity (5), the AM-GM elimination of w1 and w2 to (6) and its equality point, exact in sympy with independent p, a, c; (B) the s-elimination 4 mu^3/(27 C), the maximum over the positive-margin range 0 < s < mu/C (the script's comment and print line omit that range; THEORY_FINAL section 11 item 79, T4-468); (C) the constants K and v of (10), (11) by mpmath interval arithmetic at 200 bits; (D) for each of the seven rows, no root of the degree 7 polynomial Q_b of (9) on [0, m2] (exact Sturm count), the printed gains as upper factors over the exact registered sharpw and TB-sharp ceilings and the 007 and H18 factors as lower factors (exact), and the sampled supremum of (8) (FLOAT, printed only); (E) beta monotonicity of the bL extension; 48 checks | review set 45 (R1-047), THEORY_FINAL sections 2.8 and 9.4 | none | a few s |
| checks/check_N4396.py | Review R1-048 of the N4 numerical auditor N4-396 (two-mode dual lower bound for candidate 016 and E2(007) < E2(016)): (A) admissibility of all 663 test coefficients (beta > 3/2, k >= -1, 3 + 2k >= n, 3 + 2k - n even); (B) the exact gradient energies d_1/pi and d_3/pi by a third method (rational Beta integrals in r), equal digit for digit to the N3 numerics worker and the N4 numerical auditor rationals; (C) Arb at 1200 bits: |p_n|/sqrt(d_n) from the N4-396 pairing balls, the strict mode floors below it and below both partner quotient balls, the N4 numerical auditor pairing ball overlapping the N3 numerics worker display (containment also holds, checked separately at 16:05Z), p_n/d_n - 1; (D) exact: H^2 floor, H > 0.529469576110512066428681, the E2 floor 608.392385921614 against the accepted 007 upper 606.820219 (N4-392 component floors, N4-252), separation 786083460807/(5 10^11), the floor without H (547.86) and the H threshold 0.522193054; (E) FLOAT display arithmetic of numerics_v15 section 5 (six snapshots below 007); 1368 checks; the pairings themselves are read, not recomputed | review set 46 (R1-048), THEORY_FINAL section 7 | checks/data/N3_016_hdual_m13deep.json, N4396_mode_001.json, N4396_mode_003.json, N4396_result.json, N4392_comparison.json, N4252_result.json | 140 s |
| checks/check_T4469.py | Review R1-049 of the T4 theory auditor T4-469, ERRATA_v01 and team note 247 (divergence-free improvement of the angular Hardy upper bound): (A) sympy: div A_F = F, <A_F, grad psi> = -p with no radial term, the M2 density, orthogonality of Z across modes; (B) sympy: formulas (7), (8), the operator (9) for symbolic b including the t^0 term, the (10) and (11) measures, R0^2 + r^2 = (1 + 624 w)/w, the r^2 Delta_n label shift; (C) exact fixtures (d/pi = 3/8, 6/35; M2/pi = 3/4, 64/315; a/pi = 3/8, 2/63 three ways; b = -a; 153/280; 1457/2520; the residual identity equals the t = 1 case of (3)); (D) FLOAT mpmath quadrature at 40 digits: (10) = (7) and (11) = (8) for a two-group trial and a source with the pole (1 + 624 w)^(-3); (E) candidate 016: a_1/pi and a_3/pi of N4-398 recomputed exactly by a separate method, a_n + b_n about 1e-38, the improvement floors, and (CONDITIONAL on the N3 numerics worker mode Hardy displays) M2_n - b_n^2/a_n - LB_n^2 containing 0 with radius below 1e-29; 65 checks | review set 46 (R1-049), THEORY_FINAL section 7 | checks/data/N3_016_hdual_m13deep.json, N4398_mode_001.json, N4398_mode_003.json, N4398_result.json | 330 s |
| checks/check_T4474.py | Review R1-050 of the T4 theory auditor T4-474 (complete angular Hardy upper bound from a mode prefix) and of the tail step of the N4 numerical auditor N4-403 (candidate 016): (A) sympy: parity (odd sine modes only), div A_F = f sin(n theta), radial cutoff gradients orthogonal to A_F, angular Parseval, fixture S_1/pi = 3/4 and S_3/pi = 64/35, the theta-integrated identity int A_F . grad phi = -int F phi for two rational phi; (B) symbolic modes 1 to 23: B_N - M2 identity, bound (3) coefficientwise, B_(N+2) - B_N, N4-403 (1) = T4-474 B_(N+2); 204 exact lists (4 T4-474 fixtures, 200 random, seed 474): (2), (3), monotonicity, outward form (4) <= split formula with difference sum (U_n - L_n)/N^2; omission counterexamples; known solution B_3 = 1201/1260, B_3 - a_1 - a_3 = 153/280; (C) candidate 016, exact from the saved N4-403 endpoints: R2 endpoints = squares of the accepted rF endpoints, M2 <= 1.129995950 < 1.129996, plain H <= 1.063012677 < 1.063013, improved H^2 <= 0.891336793, H <= 0.944106347 < 0.944107, E2 < 722.968760 (E2 <= 763.064677 without the improvement), loss bounds U^2/N^2 for N = 1 to 65; (D) CONDITIONAL on the N3 numerics worker's 30-digit mode Hardy displays: their balls contain the N4-403 q_1 and q_3 endpoints; FLOAT tail about 0.097613 against the bound 0.605053; displayed uppers are rounded up and lowers rounded down (display lines changed 16:43Z, review set 48 errata E4 to E7; checks unchanged); 4783 checks | review set 47 (R1-050), review set 48 section E, THEORY_FINAL section 7 | checks/data/N4403_result_v01.json, T4474_parameters.json, N4392_comparison.json, N4396_result.json, N4398_result.json, N3_016_hdual_m13deep.json | 7 s |
| checks/check_N4409.py | Review R1-051, exact recomposition of the N4 numerical auditor N4-409 (candidate 016, prefix of the odd modes 1 to 31, first omitted 33) and N4-410 (accepted complete H and E2 bounds of 016) from their saved endpoints: (A) hashes, bindings of N4-410's parameters, coverage (16 of 160 modes, tail retained), modes 1 to 7 equal to N4-403, prefix balls contain the exact prefix sums; (B) R2 endpoints = squares of the accepted rF endpoints, tail endpoints, positive-coefficient M2 <= 0.622626936301 at m = 33 and the split formula, plain H <= 0.789067131 < 0.789068, N4-398 floor for modes 1 and 3, H^2 <= 0.383967779848, H <= 0.619651338 < 0.619652, E2 <= 629.296112163 < 629.296113 (674.979607 without the improvement); (C) N4-410: H < 619651337324093367770781451079/10^30, E2 < 629.296112162914, H lower square = N4-396's, H > 0.529469576110, E2 > 608.392385921614, E2(016) - E2(007) > 1.572166921614 exactly; (D) N4-409 below N4-403, M2 width <= 0.000525, H(016) upper below the N4-252 H(007) lower ball (Arb); CONDITIONAL: The N3 numerics worker's q_1, q_3 balls contain the endpoints; FLOAT: The N3 numerics worker's complete Hardy display and CLAIMED H(016) bracket inside the enclosure; 54 checks | review set 48 (R1-051), THEORY_FINAL section 7 | checks/data/N4409_result_v02.json, N4410_result.json, N4410_parameters.json, N4403_result_v01.json, N4392_comparison.json, N4396_result.json, N4398_result.json, N4252_result.json, N3_016_hdual_m13deep.json | < 1 s |
| checks/check_v50.py | Erratum E11 of review set 50 and the sharpw values of THEORY_FINAL section 2.1 (N4-415), exact Fractions: (A) from the N4-409 saved endpoints and the N4-392 accepted rF endpoints, every ratio of a prefix endpoint (modes 1 to 31) to an R2 endpoint lies strictly between 0.988805 and 0.988806, so R1-051 V7 "at most 0.9888" is false; (B) mu = 201799/648000, A = 576/5, at r = 1351/10^6 beta(r) = 63092119/405000000 >= 1557/10000, 4207/(2 10^7) <= (1557/10000) r, beta(r) r = 85237452769/405000000000000 > 2.1046e-4, and eta* - beta(r) r = A (r - r*)^2 > 0; 20 checks (13 after Part A, 20 cumulative after Part B; review set 50 and draft 55 said 33, corrected in review set 51 E12 after T4-487) | review set 50 (E11), review set 51 (E12), THEORY_FINAL sections 2.1 and 12 | checks/data/N4409_result_v02.json, N4392_comparison.json | < 1 s |
| checks/check_N4418.py | Review R1-052, exact recomposition of the N4 numerical auditor N4-417 (prefix-31 tail with all 16 corrected modes) and N4-418 (complete 016 H and E2 bounds) from their saved endpoints: (A) hashes, bindings (one 016 raw file; the 4430 and 2065 recorded checks true), coverage (160 modes, prefix 31, 16 trial modes, 2130 pairing groups), the 16 prefix intervals and R2 endpoints of N4-417 equal to N4-409's, so M2 <= 0.622626936301 is unchanged; (B) L2 = sum L_n^2 >= 0.380360210930, J = sum J_n > 0.240761083124 from the 16 selected floors, U2 = M2 upper - J <= 0.381865853176, L_n^2 < U_n/n^2 - J_n in every mode, and the exact width identity U2 - L2 = sum_n (U_n/n^2 - J_n - L_n^2) + (R_U - Q_U)/33^2; (C) strict endpoints 0.616733500735 < H(016) < 0.617952953855 and 628.580088525 < E2(016) < 628.879024750 by exact squaring, E2 squares from the N4-392 component bounds, E2(016) - E2(007) > 21.759869525 and H(007) - H(016) > 0.017571422145091 (N4-252), the T4-486 and N4-418 displays; (D) nested strictly inside N4-410, J above the N4-398 floor with J_1 + J_3 equal to it, FLOAT positions of the N3 numerics worker's CLAIMED values and, since review set 52 (erratum E13), the exact distance 18225240013184170643/(5 10^29), in (3.64e-11, 3.65e-11), of the N3 numerics worker's H lower below the strict H lower; 89 checks; the group intervals are read, not recomputed | review set 51 (R1-052), review set 52 (E13), THEORY_FINAL section 7 | checks/data/N4418_result_v01.json, N4417_result_v03.json, N4409_result_v02.json, N4410_result.json, N4392_comparison.json, N4398_result.json, N4252_result.json | < 1 s |
| checks/check_N4425.py | Review R1-053 of the N4 numerical auditor's 017 replay proof (audit record candidate017_dual_residual_replay, proof, 0ce420a0...) and N4-425: (A) sympy, generic radial profiles u(r), f(r), n = 1, 3, 5: div A_Fn = F_n, r^2 Delta psi = (u_yy - n^2 u) sin(n theta), the theta integrals of d, p, a, b, Qn and ||A||^2; (B) three manufactured fixtures (rational beta > 3/2, k >= -1 with 3 + 2k - n even and >= 0, rational delta), every quantity by 50-digit mpmath quadrature in r (FLOAT): the residual identity Rn^2 = Qn + 2n^2(b - p) + n^2(a + d), ||r Delta psi||^2 = n^2(a + d), int r^2 F_n Delta psi = n^2(b - p), ||A||^2 = Qn/n^2; (C) the PROOF's t-formulas for d, a, p, b, Qn evaluated exactly and matched with (B); (D) exact: the 16 dual floors, their squared sum, H(017) > 307209799380023711068567013529/(5 10^29) > 0.614419598760, the mode 1 and 3 residual enclosures, consistency with the dual floors and with T4-484; 79 checks (75 if the read-only the N4 numerical auditor source files are absent: the four source comparisons are then skipped) | review set 53 (R1-053), THEORY_FINAL section 7 | checks/data/N4425_extract.json | about 31 s |
| checks/check_N4427.py | Review R1-054: exact recomposition of the N4 numerical auditor's N4-427 and N4-428 (candidate 016, Hardy prefix 1, 3, ..., 47) and N4-430 and N4-431 (prefix 1, 3, ..., 63) from the saved endpoints: (A) hashes and bindings; (B) coverage of the 160 odd modes, mode intervals (1..31 equal to N4-417's), R2 and tail endpoints, M2 lower and the positive-coefficient M2 upper at N = 49 and N = 65; (C) U2 = M2 upper - J with the 16 N4-418 floors, per-mode consistency, strict H and E2 endpoints by exact squaring, the gaps over 007 (N4-252), the N4 numerical auditor's displays; (D) nesting P = 63 inside P = 47 inside N4-418 and the width split; (E) the extract against the four source files when readable; 272 checks (138 if the read-only the N4 numerical auditor source files are absent: Part E is then skipped) | review set 54 (R1-054), THEORY_FINAL section 7 | checks/data/N4427_extract.json, N4418_result_v01.json, N4417_result_v03.json, N4392_comparison.json, N4252_result.json | about 0.1 s |
| transfer_checks/transfer_numbers.py | S1 facts of the Hou transfer matrix: origin linear data, D^2 transport rates, (B5) M_2(0), Taylor-mode counts, vanishing orders, T4L2 radius with and without the sqrt(s) loss, HNW margin, weight windows | hou_literature/TRANSFER_MATRIX.md | none | < 1 s |

## Data provenance

- The matrix copies v135 to v153 are stored gzip-compressed (since 18:22Z) to keep this directory under 20 MB;
  the sha256 values given below for them are those of the uncompressed copies, and the SHA256 section lists
  the .gz files. checks/h18_verdicts.py and checks/row_refs.py read uncompressed files only.
- checks/data/closure_matrix_v137.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v137.md.gz): copy of exchange/closure_matrix.md, version v137 (2026-10-29T14:52Z), read at 14:59Z,
  sha256 f1022eff44d39f8318647ad165d80fea641bec3b6c45ac4287e068029b6f63ca; the default matrix of checks/h18_verdicts.py for draft 47.
- checks/data/closure_matrix_v138.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v138.md.gz): copy of exchange/closure_matrix.md, version v138 (2026-10-29T15:00Z), read at 15:08Z,
  sha256 7e6423c626d350b861e0cab2535be846d86efe16e9a5979d4485cd844e581089; the default matrix of checks/h18_verdicts.py for draft 48.
- checks/data/closure_matrix_v139.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v139.md.gz): copy of exchange/closure_matrix.md, version v139 (2026-10-29T15:13Z), read at 15:15Z,
  sha256 7da41503bc629bff3a7b1f91de20a9bba8e00c234052b17d84c14b372f18bf49; the default matrix of checks/h18_verdicts.py for draft 49.
- checks/data/closure_matrix_v155.md: copy of exchange/closure_matrix.md, version v155 (2026-10-29T17:15Z), read at 17:18Z,
  sha256 1751c1c9286d6857de72ce20fc345b18996b885a3f091b8dbe0b8ee10e13acbf; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py for draft 56.
- checks/data/closure_matrix_v157.md: copy of exchange/closure_matrix.md, version v157 (2026-10-29T17:24Z), read at 17:27Z,
  sha256 c94780adb23e986e6ff1a885e6c889291456523b07d3855367adea6bcc4ed7c4; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py for drafts 57 to 64.
- checks/data/closure_matrix_v170.md: copy of exchange/closure_matrix.md, version v170 (2026-10-29T18:22Z), read at 18:25Z,
  sha256 8bf325ea63f55e53495421349f6cfe098d1d1c9d38f8b045a3a8531c553787ac; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py since the final THEORY_FINAL.
- checks/data/closure_matrix_v153.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v153.md.gz): copy of exchange/closure_matrix.md, version v153 (2026-10-29T16:58Z), read at 16:59Z,
  sha256 99f99c850705547e2a83389e6bde4c75e6b3cebfb2d6dc02c1cc71d4c93b6d61; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py for draft 55.
- checks/data/closure_matrix_v151.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v151.md.gz): copy of exchange/closure_matrix.md, version v151 (2026-10-29T16:40Z), read at 16:46Z,
  sha256 23534a462f910c0cb79bcd61ae4d46056dd33013c3024fbf0ffd78c9c48e0a6d; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py for draft 54.
- checks/data/closure_matrix_v146.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v146.md.gz): copy of exchange/closure_matrix.md, version v146 (2026-10-29T16:15Z), read at 16:16Z,
  sha256 2361ea1f8eba2d7462823a0f5eb5e270e6fe1294a30e3f68e4800cd22e77ec6a; the default matrix of checks/h18_verdicts.py and
  checks/row_refs.py for draft 53.
- checks/data/closure_matrix_v140.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v140.md.gz): copy of exchange/closure_matrix.md, version v140 (2026-10-29T15:22Z), read at 15:24Z,
  sha256 927f13f5303198d430b46f39b8fc4d679c3556764ca1ce954ec6888975536e94; the default matrix of checks/h18_verdicts.py for drafts 50 to 52.
- checks/data/closure_matrix_v135.md.gz (gzip -9 -n of the copy since 18:22Z; restore with gunzip -k checks/data/closure_matrix_v135.md.gz): copy of exchange/closure_matrix.md, version v135 (2026-10-29T14:25Z), read at 14:29Z,
  sha256 e4b8370989232d05de0a739852b84dda49e359d35831d8800286cddd4eb07918 (the same hash the T4 theory auditor froze for its H18 audit, team note 233).
- checks/data/C1-N1-001_raw.json: copy of audit/theory_audit/research_code/candidate001_affine_exclusion/source/raw.json (the generator
  file of the immutable snapshot C1-N1-001), sha256 8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7.
- checks/data/T4458_leading_coefficients.json: copy of audit/theory_audit/research_code/candidate001_affine_exclusion/data/leading_coefficients.json,
  sha256 9829a3563bea97194c50ac752643a658a59112c6bbf5a050e7c4e774c9db371a; read only for the exact comparison in Part B of check_T4458.py.
- checks/data/N3_016_hdual_m13deep.json: copy of audit/numerical_audit/research_code/candidate016_dual_lower/source/N3_exact_vectors.json (the N3 numerics worker's
  exact mode 1 and mode 3 test vectors for candidate 016), sha256 a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5.
- checks/data/N4396_mode_001.json, N4396_mode_003.json, N4396_result.json: copies of audit/numerical_audit/research_code/candidate016_dual_lower/
  verification/mode_001.json, mode_003.json and result.json (N4-396), sha256 4291bb11104879c7821a888c52ad666d1700065d6cf365540250dd0080b34cda,
  e57ce8e56dcd9e613afdb17b7f2d6f8c74252480be65502efe9065938036aab9, e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa.
- checks/data/N4392_comparison.json: copy of audit/numerical_audit/research_code/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json
  (N4-392 accepted component lower bounds of 016), sha256 a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc.
- checks/data/N4252_result.json: copy of audit/numerical_audit/research_code/negative_norm_forcing_assembly/verification/result.json (N4-252, the 007
  E2 upper bound), sha256 d94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c.
- checks/data/N4398_mode_001.json, N4398_mode_003.json, N4398_result.json: copies of audit/numerical_audit/research_code/candidate016_solenoidal_upper/
  verification/mode_001.json, mode_003.json and result.json (N4-398), sha256 53e2f9a049a97a7f85a6fcb692b272c16e048d0723a2518ee7e671065975634e,
  2dff6601c75bdf39c6fd038ba57020ef1fd257ed5bcf9ce04a39066406eab40e, e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603.
- checks/data/N4403_result_v01.json: copy of audit/numerical_audit/research_code/candidate016_angular_tail_bound/verification/result_v01.json
  (N4-403, prefix 1, 3, 5, 7 of candidate 016), sha256 8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1.
- checks/data/T4474_parameters.json: copy of audit/theory_audit/research_code/partial_mode_hardy_certificate/data/parameters.json (T4-474
  fixture lists, rF upper, cross improvement floor, loss cuts), sha256 659210cd3824e5367dd5eea0d8b8a649c8242a78cebc415f6d8301dc8040ed05.
- checks/data/N4409_result_v02.json: copy of audit/numerical_audit/research_code/candidate016_angular_tail_bound/verification/result_v02.json
  (N4-409, prefix 1, 3, ..., 31 of candidate 016), sha256 01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41.
- checks/data/N4410_result.json and N4410_parameters.json: copies of
  audit/numerical_audit/research_code/candidate016_reviewed_upper/verification/result.json and source/parameters.json (N4-410, complete 016
  H and E2 bounds; PROOF.md sha256 bf8cb48f0f49dd226a009f92923ba74a3dea366ee63d95641861db2850f37ed2), sha256
  d50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0 and a65ce341175cfaf85d5959a398d38ddd908f66bb233b43f1cb8a654840e3053d.
- checks/data/N4418_result_v01.json: copy of audit/numerical_audit/research_code/candidate016_multimode_complete_bounds/verification/result_v01.json
  (N4-418, complete 016 H and E2 bounds from 16 corrected modes; PROOF.md sha256
  967c25cdeb2192c56ba8212ae7d356c1dac206fc7f1f7fe794d527fcd0dac568), sha256
  8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728.
- checks/data/N4425_extract.json: fields copied verbatim from audit/numerical_audit/research_code/candidate017_dual_residual_replay/verification/result.json
  (N4-425, sha256 7e093982e733237262819ca3ad0486f85bdc4d31c69d73a99e382dbad5c3ab06), mode_001.json (28d03477...) and
  mode_003.json (b768eea2...), written by `python3 -B checks/make_N4425_extract.py` (a full copy of the three files,
  about 0.9 MB, would not fit the 20 MB artifact limit); sha256
  35c0b8fe19a528699abcdbc46089d047f917dc9b878721228e9bbff120a7b5fa.
- checks/data/N4427_extract.json: fields of audit/numerical_audit/research_code/candidate016_angular_tail_bound/verification/result_v04.json
  (N4-427, sha256 d1d90c2295662dd1288a3a77d100b0b9cc3cdfbfb8a8345399145c7cba3f0bff) and result_v05.json (N4-430,
  dc1dfe24d70ba74c405e317864391dcb01e0a8188bbf8eb97edaefbe11ef9066), and of
  audit/numerical_audit/research_code/candidate016_multimode_complete_bounds/verification/result_v02.json (N4-428,
  42e43b1b5240309fad4ab3d7579dfe557ae15a89ead61b9a4991da18a4950513) and result_v03.json (N4-431,
  6c5f02dc951d92cff7df788228594d2137e5f41b5bdea58b17b8505cb40cd3ee), written by
  `python3 -B checks/make_N4427_extract.py`: exact strings under 400 characters verbatim, longer ones as their sha256,
  mode intervals as q_lower and q_upper - q_lower (a full copy of the four files, about 1.1 MB, would not fit the 20 MB
  artifact limit); sha256 611a8febe1f823f04fd32047bba49f647452f713349f3aa0cb34898465427cac.
- checks/data/N4417_result_v03.json: copy of audit/numerical_audit/research_code/candidate016_angular_tail_bound/verification/result_v03.json
  (N4-417, prefix 1, 3, ..., 31 with all 16 corrected modes), sha256
  285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840.
- checks/data/N4_cartesian_witnesses.json: copy of
  audit/theory_audit/research_code/symmetry_point_witness/source/N4_cartesian_witnesses.json, where
  the run directory = working file r6 (not published) These are the N4 Cartesian point intervals for C1-A2-d2, C1-A2-Mpen2 and
  C1-A2-b6.
- checks/data/rational_box.json: copy of audit/theory_audit/research_code/graded_closure_audit/verification/rational_box.json.
- closure_calc/data/nb_stableA2_exact.annular.json: copy of the A2 certificate file (leading sine coefficients of the
  fixed sector) source data (read-only, not included): analysis2/IPM_Analysis_II.artifacts/certificates/P25_admissible_tail_gap/nb_stableA2_exact.annular.json
  (identical sha256).

- checks/data/state131_exact.json and checks/data/state131_field_points.json: copies of
  source data (read-only, not included): analysis2/IPM_Analysis_II.artifacts/certificates/P1_source/state131_exact.json and
  .../P1_source/state131_field_points.json (A2 stored point enclosures), identical sha256.
- checks/data/T4047_points.json: copy of audit/theory_audit/research_code/principal_energy_obstruction/verification/points.json
  (comparison only).
- checks/data/T4127_combined_cover.json: copy of audit/theory_audit/research_code/projected_laplacian/verification/combined_cover.json
  (T4-127 combined result), identical sha256.

- checks/data/T4251_inputs.json: fields copied from audit/theory_audit/research_code/taylor_projection/verification/{parameters,result}.json,
  .../taylor_projection/source/canonical007.json (a0 and the block-0 order) and audit/theory_audit/research_code/affine_taylor_lift/verification/
  {parameters,result}.json (comparison values); the source sha256 values are stored in the file.

- checks/data/T4380_inputs.json: the fields q, delta, D and, per reference, theta_exact, H_point, G_lower_exact,
  V_lower_exact, B and the stored thresholds, copied verbatim from
  audit/theory_audit/research_code/endpoint_pointwise_budget/verification/result.json (T4-380, sha256
  b081ef430ad054bb3255d191ec23b0bdad713b98f0d30f3407fe1540c456f4d5, stored in the file).

- checks/data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json, c1n1_013_pairU_m16_exact.json and
  c1n1_014_pairB_m16_exact.json: copies of the generator files d2w_j7_n4_E2bal_mid180_exact.json,
  d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json and d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json in
  candidates/C1-N1-007-d2w-j7-e2bal, .../C1-N1-013-pairU-from007 and .../C1-N1-014-pairB-from007;
  checks/data/c1n1_0NN_sector_table.json: copies of sector_table.json of the same snapshots. All sha256 values equal
  the snapshot SHA256SUMS.

## SHA256 of the stored files (2026-10-28T22:38Z; check_T4041 added 22:56Z; check_T4051 added 23:13Z; check_T4054 added 23:26Z; check_T4047 added 23:45Z; check_T4060 added 2026-10-29T00:08Z; bl2_trade and check_T4097 added 00:41Z; check_T4107 added 00:53Z; check_T4127 added 01:27Z; check_T4128 added 01:55Z; check_T4146 added 02:06Z; check_T4153 added 02:10Z; origin_inv_table added 02:15Z; check_joint_ceiling added 02:26Z; check_T4170 added 02:39Z; check_T4182 added 02:55Z; c_shift_diag added 03:02Z; check_T4185 added 03:09Z; theta0_007 added 03:19Z; check_T4199 added 03:46Z; check_T4205 and tail_profiles_007 added 03:52Z; check_T4206 and t4206_angular_sup added 03:58Z; check_T4222 added 04:09Z; check_T4211 added 04:12Z; check_T4229 added 04:22Z; check_T4234 and check_T4235x added 04:35Z; check_T4251 added 05:20Z; annulus_admissible added 06:05Z, directed rounding 06:14Z; check_T4281 added 06:24Z; check_T4295 added 07:00Z; check_T4314 added 07:26Z; check_T4322 added 07:49Z; check_T4359 added 09:08Z; check_TP6 added 09:43Z; check_T4372 added 10:00Z; check_T4381 added 10:16Z; run_all.sh rehashed 10:16Z; check_N4refdiff added 10:26Z; run_all.sh rehashed 10:26Z; check_T4397 added 11:14Z; run_all.sh rehashed 11:14Z; check_T4410 added 11:55Z; run_all.sh rehashed 11:55Z; check_R1044 added 12:20Z; run_all.sh rehashed 12:20Z; check_T4425 added 12:27Z; run_all.sh rehashed 12:27Z; check_T4474 added 16:33Z; run_all.sh rehashed 16:33Z; check_T4474 rehashed 16:43Z; check_N4409 added 16:43Z; run_all.sh rehashed 16:43Z; row_refs and h18_verdicts rehashed, closure_matrix_v151 added 16:57Z; row_refs and h18_verdicts rehashed, closure_matrix_v153, check_v50 added, run_all.sh rehashed 17:02Z; row_refs and h18_verdicts rehashed, closure_matrix_v155, check_N4418 added, run_all.sh rehashed 17:23Z; row_refs and h18_verdicts rehashed, closure_matrix_v157 added 17:29Z; check_N4418 rehashed 17:46Z; check_N4425 and make_N4425_extract added, run_all.sh rehashed 18:04Z; check_N4427 and make_N4427_extract added, run_all.sh rehashed 18:15Z; matrix copies v135 to v153 gzipped 18:22Z; final matrix copy v170 and H18 default switch 18:25Z)

    25999c14b978fc2cc9297b16eafbc34a8405f6cadd2e583bdf20ac5d57e3a7b8  checks/check_T2R1_T4007.py
    c86218da474493af58886743741b6fadf23eae272d0be153ee56c4cc966f1214  checks/check_T2R1_T4007.out
    1d6ce37ff48ce7a252ea918cc091959887058b568993104b5a4b95390ababef4  checks/check_T2R3.py
    947aaeb5c1918c046bd1fc7fb65cecc1c46481d36f46fdd8b63256cc09ac7df2  checks/check_T2R3.out
    6cc2e9d8f7f01372cd9c65efe99ce285a8cae0d2f86a01a0a43a85da523ca786  checks/check_T4041.py
    8393bb13135bf9ebee6e2e636987f6bf31f89f9eda423e3b165798fc68611445  checks/check_T4041.out
    256175f0b57999800e9afaacdb439e8918e4aea561d43bed1907e11ee922c0d6  checks/check_T4051.py
    24f9c7fde5fcda178cf8d5b2cbd6d1c4fd4d5c89a3cf8d948c5e801f5a680335  checks/check_T4051.out
    b2c6bfd098c3422c23f9378c7a7f1c2522eaae03e29d020cffc7a8c8aa97a4d3  checks/check_T4054.py
    7589d58572e30adccf6cdc1b5ad4e4ece70ee1585248d470868771bca0a4bdf6  checks/check_T4054.out
    ae5d0e6df805aa643e8119ab6ca3ec50a4c7d52d71b22cccb82bc1d479972228  checks/check_T4047.py
    9215750d4c2f9243db4b25435c3abb5f19e44d9851907655bbe9ba4840984294  checks/check_T4047.out
    b02fdd8fbdf69aa764fbc6a32de7a1d21d7da6bb099948a36a1f831e51190403  checks/check_T4060.py
    e93e59903fdb260b91962a667c7bdcbca6be907d1b123cac647ea47f42c84010  checks/check_T4060.out
    e525e9d55f74e227b1ad9d2138032eb67f43261c05848e53844f33f8c55162b5  checks/data/state131_exact.json
    f384928cf76efc23517a5751ed104bc3d966e5437d51a28f6b9cb271167e02d8  checks/data/state131_field_points.json
    a7e63cc67d1f1b1903e23e21afa79ed5e9d46400abd0e893597ca10792e4fc70  checks/data/T4047_points.json
    73d4350cdcb176b2ef172808d9e811b293b1e1f05bbac8439dfb9c77267034ef  checks/check_T4013_T4017.py
    3a30cf7921dc21eec7a7bb926d524f49d0e9eb2f04dedd08fe2c39ed9af53c1d  checks/check_T4013_T4017.out
    96fbe6c036b0b9f5ac8db245d9013d156070d76d4d643fc6ab49c71335e22fe3  closure_calc/closure_calc.py
    260766a1d1f0863c894103995d9f2756b381dfeb6d1b8957a26c57f2c1b5c812  closure_calc/closure_calc.out
    17d8a36474112595bd90b03efb98e9622052754d8dd5a53b9105434bed3772a6  closure_calc/l2_sector_cost.py
    489c3e27b18a18827b02660b67d780844df231fc9f0a5f855cf7130463201d2b  closure_calc/l2_sector_cost.out
    56f6a80401d28fc4e84b3375316dcbe2f7e4518d5ad7941da0fe1669d90b31a7  closure_calc/six_branch_K.py
    a1cb14ab9680525d440cf12783c9a9964d528dec17ee8f41acc81d80f4789b11  closure_calc/six_branch_K.out
    58c33c51e082b86c2756ce3f8b584f56746b723548809ab212a645bd103ff7ce  closure_calc/tail_budget.py
    fd688ff7df6f46edec41c8c81b441571490454f81a4c5c7ae096061dbf5b8c75  closure_calc/tail_budget.out
    d1b79c0fe7042420dae5ac69d60feeb051fae3fdf869ef77883422251d55d073  graded_calc/graded_calc.py
    c111a33099b67b60a211c18fb4b17c4f73a018095122964ec53371dc90e05e26  graded_calc/graded_calc.out
    0f7ca86ee7be8ae37d489964176f3270e623afac5cd2f47539c2b6bbaa7fd952  graded_calc/graded_instance.py
    3506446d8a3ac481ebb73c6b84273665cfce9ea17edf1844364540b0feff7267  graded_calc/graded_instance.out
    44cbad9d3da2086c639c646a3300f4a1139589470aad796d23681b737d5723a8  graded_calc/graded_l2.py
    37ea1faf0c52f2b93b51cea3eab672ce7360a99718aeb732b5391fcb39e5b889  graded_calc/graded_l2.out
    a3c49cbd7c6a295cc4d2cd87d366a742b991f5ccbcfc8cd186a469cbcdf7f549  transfer_checks/transfer_numbers.py
    7f8e6f2e3a9105bb4afcc420fad197b131f22c5cf22e845a69146f8c4dbe4c5a  transfer_checks/transfer_numbers.out
    4596e2d6a18041d2bad3a01f14cca26611ba508070be63ec77786b2984407a7e  checks/data/N4_cartesian_witnesses.json
    6724a0dbea2eda2c72afbc194e917806f498fc233f46bffbc1af4a8f501aea80  checks/data/rational_box.json
    6aebb0482b6af0285bc43e6b7d3fa9dd4a616d080be9d562e410957bc2d0de49  closure_calc/data/nb_stableA2_exact.annular.json
    96c09fbef4a781a66100bb268881bc89e1e56ff53cbcf139d6365ded4d068ac5  closure_calc/bl2_trade.py
    57503e9f71c728c19508ebbb36c365778339e4eda7b71e9b4bfb3cddd0debe97  closure_calc/bl2_trade.out
    3cb784332d8757d65414e657c604009f8fcc10c67fd24392dd7ae44b3a2a81a9  checks/check_T4097.py
    53f5ad8dacdd4b02367b06d508299d446f5e7d27c9378992f29e181d5cd459d7  checks/check_T4097.out
    5722485a34cd67d5ecc8dbddfc67de347df34270c542988462ae3c29b1e8c4b7  checks/check_T4107.py
    3208fb4cddfeb8f51a268ec775beb77af5252410bc591c5dd88ea5a4da86256a  checks/check_T4107.out
    58db02c43f9dbe05d62fbf76d67dd1458dda1928a0cddf2efff132a23733ad71  checks/check_T4127.py
    b7ce547a6b97f2e575670f848a5c613d6d46093473cd31eb23baf48d8b4d09c6  checks/check_T4127.out
    bd5a33163064e077c0b145f27837c853762651dfe0f3ab85dedf35dfa6a6e0f1  checks/data/T4127_combined_cover.json
    57baff05c8b9d2a2c4c7ea1765fd9ce864e2bc105914ed2c7bdd80d6338b3d5a  checks/check_T4128.py
    5300ecf2d211d71588abb1b4a1b6a9ed310842709e94891efe6423c9ee8908d7  checks/check_T4128.out
    b9fa36b3096ac6b78acaaf09c9427ea4713ddfeb45a4e9703a45b2aae2c6e3c5  checks/check_T4146.py
    24c3709a7a39142bcf9db58e7685b9b225dec3c5a1d5fb43a28c0797a88d5115  checks/check_T4146.out
    24b5ee9adaff15b14030361e6d521e1ac6f02fd88ef7459f93616f82e57ec78e  checks/check_T4153.py
    ac73d557433fa69e9c136931129f1ee2622de487cb2554bc5bfbef0853a35865  checks/check_T4153.out
    0008aea26c5021eea2a3857f21683a8df3cd0fb941386541827d6205df42ccb0  checks/origin_inv_table.py
    e2a2c632a302888269fc31f1a3db400125909458d7f52283573f99698da887f6  checks/origin_inv_table.out
    8b25c051994938e02620751a53a621b5471be08c4e02719946ea30d907fc01ad  checks/check_joint_ceiling.py
    68ba4371ba170ef61a242e9ec273d90e66a6281293006a243b3694ada684d2c0  checks/check_joint_ceiling.out
    e7d584ee7ecd59bc003f73b9c14e97185bcd18db6c694550df418f0cb9e85ac3  checks/check_T4170.py
    a59d2c46d7c60fe29372c8c531e10e986112837c5c1ea1eebb9961fb18d74d72  checks/check_T4170.out
    9b453898881d594d747a805341a5a05800de41e270cad58f2ef1518038c1ccef  checks/check_T4182.py
    febe723b8d540da8757c3c8bd9023e430640935ebd76272abe9f869308b35daa  checks/check_T4182.out
    fcda1d95042350c0dbf684a076c2024729574be9353014f1e3b20b03a71a97f7  checks/c_shift_diag.py
    748039f59875f6fcf497191f09057c84c456241a0f3915a0ceca13cbb348ddfa  checks/c_shift_diag.out
    dfc82b709cd87673d82d2ca13446e5fd063757793fb7847bd3d6108f61a090b3  checks/check_T4185.py
    8f6a6578b4d2a523f4c37f0e0c451eb9cb784716ccb404c5e1d3d64547feafba  checks/check_T4185.out
    35551dd444c2e78ae16a4ca449edc663fcc421c890ba443db3ece7ba4e56366d  checks/theta0_007.py
    c6d60fb598167f028de4c067a06b581100061617ff3ba8bf3d623df9f5fe150b  checks/theta0_007.out
    2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f  checks/data/T4185_n7_a0.json
    ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21  checks/data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json
    b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e  checks/data/T4182_a0.json
    d1b4367127fbdd902440124e53b15b904268608d06eab9ad5ccb0cf56e69bca7  checks/check_T4199.py
    0e7c718f9c2afffba132f9e72f911d0efbff9d24b8922fb07aa6e12c4578addc  checks/check_T4199.out
    eb73db2c8ba7849fd0738f9ce9e6510c548bbd3443952b2748c88e9e5f74d85f  checks/data/T4199_parameters.json
    2ef699138a9787e1567be06931c282826eaab0a75b88c5b7d92a3e0f62e73c35  checks/check_T4205.py
    37bd997abc59d8f04aeb1694eec3d58cbdb184b5f306bb9d6ad9a160d6fe3242  checks/check_T4205.out
    c1aa7f1968eb19bfd1d305d5af0e538f6be992450aa99ad0c47a5287229aa689  checks/tail_profiles_007.py
    529d653e5a6869249b0198175dcad0992ab584e1e8e997d069705deb451cd9ca  checks/tail_profiles_007.out
    d772b7608e50b7c0c2d50cb2f70c3be51b9c75e74f96bc343bcea047cd169de8  checks/check_T4206.py
    b61fbf17227dd448383631fe7a60a246b47463cd923ab189ca815b6fed3e0803  checks/check_T4206.out
    c46b9886f5ae0abafe87f323bbd0f2aff293f2b32f03a9315fd6af38d72cb53a  checks/t4206_angular_sup.py
    a2071d8558362192569fb917a026285b925d5a5be4a59d6cd4ece0ed6c6815ce  checks/t4206_angular_sup.out
    57b9d3ba7ca07ccc2b72116ec3d549625772f84165bac1007a3119ca48afa001  checks/check_T4222.py
    02bc57cf45dda2e7b7a1a7f74b464a2fd9ec756155a93749bb7ccc97893c6f2d  checks/check_T4222.out
    0f649cd8f51dc891bf3b797ccb020a292425bc1dcd54acbe217f3bcfbbda4318  checks/check_T4211.py
    d6445be095f9a232c447874b7b2d06e782d54215ccc9f6f8b7d302f3397089df  checks/check_T4211.out
    5c27352b112e899b2e039b1801837ee4f6141f4c0dc5295fb8a53906469e9a1b  checks/check_T4229.py
    5bbc70d2f29b57f80ac765f06c4c954d07e3c9aebe843bdc6da8e1e07998e47e  checks/check_T4229.out
    c88696e7faa0b6a66d53a26b5e61225affe821d10c756a20c6ea41358fb70172  checks/check_T4234.py
    3e6c2bcd978a9a13f58155cf49e69746239532a9c3603818301703ea72ee72d7  checks/check_T4234.out
    aeb38ab3ba5ab990875f643351b483f2b176d8fcec7035cb2e72df7a03f2dca8  checks/check_T4235x.py
    af29ef87a463e3515dd5fbd801d5919dce1387c274dde8f1396da1ce7ae415b3  checks/check_T4235x.out
    9799804ccf2ef343ad6a6dc076106ec958ce24009496776b6e8001496c23778f  checks/check_T4251.py
    901e2fa9484f736fa562c630a2dca6c1cb628db9ed98e8a0a77389382755d906  checks/check_T4251.out
    0282a067664e36f0c4faa6e5360c29e97a6610bb2959c0aa3d558d1d4ff1a5bb  checks/data/T4251_inputs.json
    1abcded46240ec8b1e581b074361437012017d1218d5cdb9a48fa07808fe7da8  checks/annulus_admissible.py
    d2650e979e620e9bca5a1ed9ba16de7e2e46de574f0147ce7ec407c802e500ef  checks/annulus_admissible.out
    9d54471429323126d6270de5779ef6566f6753a1ce943bee65073be75b68f42a  checks/data/c1n1_007_sector_table.json
    c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940  checks/data/c1n1_013_pairU_m16_exact.json
    bac5f78f424fa812c82f17e385a22ed0a6313039311c4b5b19a4f756e3e7d0a5  checks/data/c1n1_013_sector_table.json
    8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746  checks/data/c1n1_014_pairB_m16_exact.json
    b1f237688d61cf98fb4f07ea9bddaf9beaa7c18fa8a443a86192a3a9ec74d0b7  checks/data/c1n1_014_sector_table.json
    c05bf08f1b78b0b5eef598577929d867ded763ead2c8fde0c2b4f16d0f8a70dc  checks/check_T4281.py
    c59bbff085bf75d87566e74a4b17fdd9149d6a67eed0f26e95b1d59feefccfc3  checks/check_T4281.out
    079b12db094591240c74edd5182d4ee1bed5ec5fe82e8cb046b067ec6c52ef7c  checks/check_T4295.py
    30547728570f0a4a69ec5bfa2343c7c5f28b2c8e6a816afea3fb490e3897cd7f  checks/check_T4295.out
    0425c8deee99466a7b934ac50e3602e42d6c70fe09a49b75638b59cc8ace9c25  checks/check_T4314.py
    9ea89e6b3bd91517198223197d54af19c4679e275c2980bb1475442d5bafd9cf  checks/check_T4314.out
    bad9b06a64a3f045e3de487d63793f8ec0c6b021a692c5e11cea91279ed5fcd6  checks/data/T4295_007_tail_repair.json
    5485a201200fe4cdd57560775c32c0e09938a06f352127a605a780dceaa1c0e4  checks/data/T4295_013_tail_repair.json
    b69aa6a844b89409b92c6e3c94de220289a6f6c486b7d5e3e6a8c91b1327999d  checks/data/T4295_014_tail_repair.json
    d3e7e6cf6ca0ec2956b4a3f7caa1894abf3ac579ce7a410ed0f3013c4099a9d9  checks/check_T4322.py
    f3cd671f36eb06a3b3c5a3f7b0cad1c0566ffa329577d415592c6f85f1780ea8  checks/check_T4322.out
    f648e5c2fc4d63994e0ca1569eb9718b94883ba861907b5b57dd388a1f5581e2  checks/extract_T4322_shapes.py
    4145865f84a4da40d9b8f8fc3eba839e50439cb3c5480b3a126e20339b63ab55  checks/data/T4322_shapes.json
    af27eb15cace8b1e1e453522f62cf14a12e1f6781850a041b30151fdd4c4a5c8  checks/check_T4359.py
    e03f47e84f9cad8b66e8e5529c779ff5fc4c742aaf02761c21791c996227bee0  checks/check_T4359.out
    5486c845723c53ef0519a3dfe312d47b24998a613c789ccfca92dc92a033c40e  checks/check_TP6.py
    17446d9486f2766fa8daec3236e19cc54612d31997b9c0d422e33da30086f515  checks/check_TP6.out
    e76fe11252a738fabae1047b029207eb157b385d55888b5cc8db847d967a274e  checks/check_T4372.py
    3ab5792cff152c278895f2fb0c7881f3cac54bf685ba48d1f0395e01b9ed6e60  checks/check_T4372.out
    87a887bef625b00c0e0daca15b8217d629a7adca1cc7fd5b2091a328dfc502c3  checks/check_T4381.py
    75a29d0f603b54b7018d382b10f773b5a093dbc2a3a7942f4a76b0285a432776  checks/check_T4381.out
    d790aa42bae7e94394717ea56473410a9f42e5c6c6faf3c5e8e5205d03b1bd09  checks/check_N4refdiff.py
    1de3740f40bb6c7fa2bb9bde2a3566d344196c1f8177fb1638ff89f34b117008  checks/check_N4refdiff.out
    c5f4045fb09f474ffe2b3dc98cb8196535b06de78cc585446c7845a198f4dd80  checks/data/T4380_inputs.json
    c39a631acb8cf1b81a3b850a73284a1502567d7faa2e5a038b337ee4fac0423c  checks/check_T4397.py
    3b2c129ee539501b0ecb23b392d3e78cebe22e2137c665c3faba1415435a786a  checks/check_T4397.out
    a359eff8289636aaf060181881ec0e1764f0dd6e16393791402361f60988c7a6  checks/check_T4410.py
    725863d244601a66f902d4bbf78c673838da9454c892e1c51b0fc43ee0bafb1e  checks/check_T4410.out
    e50772029d985101498310c0cf352af31b532d6f3fb6b756013e6b556e27394f  checks/check_R1044.py
    c24d2c51b0739a652fd60c43f58b2ca0217955fb9e9f48a1c479078430ab728d  checks/check_R1044.out
    a70a1512db660f802c41f981974f7873763e3229eb50fef00ba620097927f8dc  checks/check_T4425.py
    8d83f7e8f1a509cc79c52806629a89d77ff0239f9b4b594ba6d5efbcf43ec40d  checks/check_T4425.out
    2615c95aeb72c0cc5967d7a0a8d2d9e7de0a2700192fa1bb9fdd878d95727fcf  checks/v08_factors_007.py
    4ad9ac5a12f18621dbed9c620f07217dfbdfde24d3f4f9534dc0d250503585a6  checks/v08_factors_007.out
    610fc962ece767e9df5238b17353a0bdfa466a0c4a6a9676e80c4e0b200eebc3  checks/h18_table_ratios.py
    b2abba574ee437906b9b4b9d52bdb5bd2707f4832bbbf79be6f3a464d5440d02  checks/h18_table_ratios.out
    7c2d4da3ed1695fdf78132b701261d676e3d9b9c0250266466d5a4974af8c51d  checks/row_refs.py
    9216c6b8b6a0ce1c0428ea779203fb74aa94e28b6b4ef4bdffd6005dda743edc  checks/row_refs.out
    bd9403264660a50953052030074f1af291bebcc1db043ea7f3501ca8fe28f87d  checks/h18_verdicts.py
    d31eff37a6499409c1a02737e4891f87a366f6e48dccac599daeb243a71c577e  checks/h18_verdicts.out
    3815cfce34d3f08240d46828eddee0ddc34e64b12505932af707613594438600  checks/data/closure_matrix_v135.md.gz
    1dd1bcbc88b04eb1f4fd7cf0cf03ad8ffd233521202479a1c639d7234452388f  checks/data/closure_matrix_v137.md.gz
    80dc671a1e689ff1737d29499c90f577235bc20f55a0194e14a09b7ea356bcac  checks/data/closure_matrix_v138.md.gz
    ff700f8256de2b0fddacbbde0e13a39da3e9462688144abae2f1c63fb03a9b75  checks/data/closure_matrix_v139.md.gz
    54ac0e26e9bbf829f0972b297a82e111fdbde56a07d8e454f5c16aeaa87eda97  checks/data/closure_matrix_v140.md.gz
    c1431b770553f5cc90540596fcc19f1ba7d1197ffa66537be2fe14f3488d2906  checks/data/closure_matrix_v146.md.gz
    82400cb35d385da109dc5e6f6c09fd13910c228ee34d77f01285a5a7cd7aca10  checks/data/closure_matrix_v151.md.gz
    b02f50b6ed5e954b01c451535b9d2d274fe9f7c97b9de84a25439f227c792c92  checks/data/closure_matrix_v153.md.gz
    1751c1c9286d6857de72ce20fc345b18996b885a3f091b8dbe0b8ee10e13acbf  checks/data/closure_matrix_v155.md
    c94780adb23e986e6ff1a885e6c889291456523b07d3855367adea6bcc4ed7c4  checks/data/closure_matrix_v157.md
    8bf325ea63f55e53495421349f6cfe098d1d1c9d38f8b045a3a8531c553787ac  checks/data/closure_matrix_v170.md
    cb7eec586031b571ab022aef7337b2729fa3684b40188b7bf15b30b70483b1bc  checks/check_T4458.py
    8748b2950df75bd88aa4175dd2a3a6c1ab5e42a708012817a88caf95feacc664  checks/check_T4458.out
    8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7  checks/data/C1-N1-001_raw.json
    9829a3563bea97194c50ac752643a658a59112c6bbf5a050e7c4e774c9db371a  checks/data/T4458_leading_coefficients.json
    6d8b95ec45526c1a97f914ae1257b05473d9a055b1e84a1e10dfd225c2ed7435  checks/check_T4462.py
    c7cb5657de235ba3cc78a33bbd1b56a6b1c204064b01f352760ba2af68a71b5c  checks/check_T4462.out
    580e957bebd2d51adcef2c3a0ce39d15433858e5dbdf3d5f8e881dbba2d09452  checks/check_N4396.py
    7c9fd9a8c9b49c60138e515e017bbb957bfde0fda80e1621fae94aecaeae4234  checks/check_N4396.out
    049776c91f253702d118b53307e21c258cd4ad03445fa08fb308396d9db78ed6  checks/check_T4469.py
    4b8a684424901def9b5db2457869edf3c0bca60ecac09a67935f39702bc27f10  checks/check_T4469.out
    a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5  checks/data/N3_016_hdual_m13deep.json
    4291bb11104879c7821a888c52ad666d1700065d6cf365540250dd0080b34cda  checks/data/N4396_mode_001.json
    e57ce8e56dcd9e613afdb17b7f2d6f8c74252480be65502efe9065938036aab9  checks/data/N4396_mode_003.json
    e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa  checks/data/N4396_result.json
    a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc  checks/data/N4392_comparison.json
    d94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c  checks/data/N4252_result.json
    53e2f9a049a97a7f85a6fcb692b272c16e048d0723a2518ee7e671065975634e  checks/data/N4398_mode_001.json
    2dff6601c75bdf39c6fd038ba57020ef1fd257ed5bcf9ce04a39066406eab40e  checks/data/N4398_mode_003.json
    e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603  checks/data/N4398_result.json
    b22bf2be6608c210ff26497b0e183486a3e65f2ff16dec7e9875d89ef1d58cc9  checks/check_T4474.py
    9aac773a3231d0abba29272e9e67c42a77e04cb9fca3dfd02d3bcc6ea9fd5d01  checks/check_T4474.out
    8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1  checks/data/N4403_result_v01.json
    659210cd3824e5367dd5eea0d8b8a649c8242a78cebc415f6d8301dc8040ed05  checks/data/T4474_parameters.json
    79f98f5f2446ec705844e35186f2caa08c3d9af6cb4eddd17687ccd3821a4415  checks/check_N4409.py
    dcc6a9bdaea5629c7ddf52c06feafaa8708a091f69d4e1f0c3c4bcef914f9163  checks/check_N4409.out
    3f53ab49d70e0f49615dbe7278b4c92c808579c666560bd7f59095c0223ebe59  checks/check_v50.py
    fb4fa87fa21ddba29b20a4b33f158dc5751f1737067168cd78187e75ad65e840  checks/check_v50.out
    01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41  checks/data/N4409_result_v02.json
    d50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0  checks/data/N4410_result.json
    a65ce341175cfaf85d5959a398d38ddd908f66bb233b43f1cb8a654840e3053d  checks/data/N4410_parameters.json
    04dad65377c0fa6db08bcc48f27f439b28ed323664b01f5eb041b2f0bbc9a440  checks/check_N4418.py
    24c61edaf70f5b7d81724bdc29ace821dcec2f36a9388f3cd8e0945308bdf412  checks/check_N4418.out
    8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728  checks/data/N4418_result_v01.json
    285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840  checks/data/N4417_result_v03.json
    7249be609524b953c413d72ed90998923c66b72f1aaee69e843c7563573566e1  checks/check_N4425.py
    85d63f2da6a40677a23e9e98a31e8d88e7ad0d52122fd5c49fd80cda9ae6e892  checks/check_N4425.out
    8ef5cbb01e87f7327cda5b00efcdb2b13f8ce40b8210eb3ca94afd7a04afb5a4  checks/make_N4425_extract.py
    35c0b8fe19a528699abcdbc46089d047f917dc9b878721228e9bbff120a7b5fa  checks/data/N4425_extract.json
    fb1f7ec32dc1950e009f85a8db22d31178df14422c3b9a04ed10fed2c7a67995  checks/check_N4427.py
    fc37d48d3b619967c3ed9708199c6bf5937fbab401935f69028b79567a5716ca  checks/check_N4427.out
    6677d230843bcf16a09a27706b166569c0b386637ab08c4e15de58942f085094  checks/make_N4427_extract.py
    611a8febe1f823f04fd32047bba49f647452f713349f3aa0cb34898465427cac  checks/data/N4427_extract.json
    8cc556b17e8bf4874782f4478faeb061e93dad4393df9c28ca9544b70ff0c546  run_all.sh

## Labels

- Exact or interval outputs (fractions, mpmath iv, arb) are the certified parts, as stated in each script header.
- Nelder-Mead optima, weight scans and tail tables are FLOAT or HEURISTIC and are labelled as such in the outputs and
  in the documents that cite them.
