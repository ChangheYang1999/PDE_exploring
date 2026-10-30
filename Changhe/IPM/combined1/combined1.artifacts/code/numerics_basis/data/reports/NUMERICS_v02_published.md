# numerics_v02 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v02; UTC time: 2026-10-28T23:36:22Z; author: The N1/N2 numerics worker; supersedes numerics_v01 (sha256 975aa84c943a0ab52dfd2d22baf1eb54f4c384f1f9d57a4ce0738551210cfa52).
- consulted: The N3 numerics worker team notes and status file; the N4 numerical auditor VERDICT_LEDGER.md (to N4-044) and team notes; the coordinator team notes,
  the run contracts v01-v04, closure_matrix v02/v03; theory_v01.md (the T1/T3 theory worker, 2026-10-28T22:14:15Z, read in full, ACK in its status log (not published) 22:16Z).
- theory version followed: theory_v01. Norm IDs: NORM-A2-E2 components, NORM-T-X3-v1 (raw-component proxy), NORM-T-DYADIC-v1,
  NORM-T-PTNEC-v1, NORM-T-PTSYM-v1. Candidate IDs: C1-BASE-S131, C1-A2-d2, C1-N1-001..004, new: C1-N1-005-d2w-j7-x3, C1-N1-006-8branch-e2 (working file INDEX.md (not published)).
- Response to theory_v01: section R. ACK of theory_v01 recorded in its status log (not published) at 22:16Z.

## R. Response to theory_v01
R1 accepted. The worked tail examples of numerics_v01 section 3 mixed quarter-plane and full-circle norms. Corrected table, exact pure-exterior
formula with FULL-CIRCLE sector norms E_n = 2 n (c_l - 1) ||G_n||_quarter (file numerics/far_field/tail_cost_table_fullcircle.md; sector norms
agree with theory_v01 NC-A2-FIXED and NC-T-TAILCOST to the printed digits):

| n | e(n,0) | E_n (full circle) | ||F||_(r>T), T = 10 / 100 / 1000 | ||rF||_(r>T), T = 10 / 100 / 1000 |
|---|---|---|---|---|
| 4 | -1.2381 | 345.672 | 289.6 / 167.4 / 96.75 | not in L^2 with weight r |
| 5 | -1.6857 | 1045.35 | 184.1 / 37.96 / 7.829 | not in L^2 with weight r |
| 6 | -2.1333 | 3081.27 | 150.6 / 11.08 / 0.8151 | 4391 / 3231 / 2377 |
| 7 | -2.5809 | 9679.97 | 142.9 / 3.751 / 0.09846 | 2357 / 618.8 / 162.4 |
| 8 | -3.0285 | 35192.4 | 163.6 / 1.532 / 0.01435 | 2298 / 215.2 / 20.15 |
| 9 | -3.4761 | 628495 | 943.6 / 3.153 / 0.01053 | 12220 / 408.3 / 13.64 |
| 10 | -3.9237 | 910751 | 448.9 / 0.5351 / 6.379e-4 | 5535 / 65.97 / 0.7864 |
| 11 | -4.3713 | 3.58664e6 | 587.4 / 0.2498 / 1.062e-4 | 7004 / 29.79 / 0.1267 |
| 12 | -4.8189 | 1.07395e7 | 589.6 / 0.08946 / 1.357e-5 | 6862 / 10.41 / 0.0158 |

Theory_v01 item 9.4 (certified E_9 to E_12): the recursion in numerics/far_field/state131_stationary_orders_0_12.json
(sha256 6a51a4f837c20c8a2b673cbf7f2cc862ae2f20e61608a1bb68541cc40f43fc72) is EXACT rational arithmetic (gmpy2 mpq) on the exact Theta_0 of
state 131 and the exact c_l; every G_n, Phi_n, C_n is stored as exact 'num/den' strings; the Poisson identity holds exactly in every order.
The squared full-circle norms E_n^2/pi are exact rationals in numerics/far_field/E_n_fixed_sector_norms_exact.json (sha256
a03db2b767b0063a209b5c46399b84aa66c15b98279638a8174ee315587d2aee). Status EXACT, PENDING-N4 (orders 9 to 12 not yet reproduced by another
lane; orders 4 to 8 CONFIRMED by N4-003/N4-032 and T4-027). Orders 13 to 16 are being computed (far_field/recursion_exact_16.log).

R2 (sectors for FW-T-T4L2-v1), R3 (no r^-2 low weight), R4 (Route T-E no gain; recommendation 10-12 exact branches with descendants q <= 3 zero
and inner accuracy to r ~ 1e4): understood and adopted as the working target; see sections 4 and 8 for what was achieved and what the inner
representation can do.

## 1-3. Source, identification, state 131 facts: unchanged from numerics_v01.

## 3b. Structural result of the far-field work (N1): where the residual of any admissible candidate must live
The exact recursion to order 16 (file above) gives ||G_n||^(1/n) about 3.0 at n = 16, so the stationary tail series rho ~ sum_n r^(alpha_n) G_n converges
only for r > r_c about 3^(1/delta) = 12 (HEURISTIC root test; the ratios fluctuate between 1.3 and 15.9). The corrected table of R1 shows the
consequence (exact pure-exterior formula, FULL-CIRCLE norms): with onset T = 10 the tail cost ||F||_(L^2(r>T)) never drops below about 150 for any
number of branches (4 to 16); with T = 100 it falls by a factor about 0.33 per added branch (3.75 at 7 branches, 1.5 at 8, 0.54 at 10, 0.089 at 12,
0.002 at 16); with T = 1000 it is 1.4e-5 at 12 branches and 4.9e-9 at 16. Hence the number of exact branches is not the binding constraint for the
L^2 route: the binding constraint is the radius T out to which the inner representation (the part of the candidate that is not the stationary
tail) reproduces the solution. The case4/analysis2 inner basis (Legendre polynomials of degree <= 25 in t = r^2/(1+r^2)) resolves the mid field only
to r of order 20 (the extreme zero of P_25 is at 1 - t about 2.3e-3). Two consequences for the numerics (both implemented, section 4):
(i) warm starts from C1-A2-d2 (whose inner part is already good: G0 = 4.99, sup|F| = 0.105) plus new exact branches are far better than cold starts
or min-norm projections of state 131 (which give G0 of order 100 to 1e5 and never recover within the step budgets we can afford);
(ii) multi-scale inner functions with vanishing far-field moments: H_m (1+r^2)^(p_j-m) t_R0^w u_R0^Q P_n(2 t_R0 - 1), t_R0 = r^2/(R0^2 + r^2),
u_R0 = 1 - t_R0, R0 in {10, 100}, Q = 4 (exact far-field moments q < 4 vanish, so they never touch the constrained sectors; their expansion in
r^-2 is rational, so the exact sector table stays exact; radial derivatives by automatic differentiation, verified against finite differences and
against the exact expansion, numerics/lib/ipm_eval.py and ipm_exact.legqs_moments). These give resolution at the scales R0 (1 to 20) x R0.
A third design, a FIXED exact tail with all descendants q <= 3 zeroed in every block (4 Legendre functions per block solved exactly for moments
(C_j, 0, 0, 0); numerics/lib/ipm_tail.py), was built and abandoned for j >= 8: the exact potential coefficients of branch 8 are of size 4.4e5
(2p_8 = -0.0285 makes the m = 0 potential inversion -s^2(s-2) C_0 near-resonant, and alpha_8 + 1 = -2.03 makes the mode-2 angular Poisson inversion
near-resonant), the moment-constrained block functions reach 1.2e7, and the inner functions would have to cancel fields of that size in the
mid field (cold-start objective 1e32). For j <= 7 the fixed tail is usable but offered no advantage over free descendants with the E_2 objective.

## 3c. (B-L2) and the weak probe for every candidate (requests the coordinator 22:21Z (b),(e) and 22:43Z)
theta = sup (|grad rho| - rho_y)/2 and kappa^2 = [(ln 2 - 1/2)||D rho_x||_2^2 + (3 ln 2 - 2)||D rho_y||_2^2]/(16 pi) are computed FLOAT on the
polar mesh (0.02 <= r <= 8356) for each candidate (diag2.py); the condition theta + kappa <= c_l - 1 = 0.810319 is reported as a margin.
The weak probe (N4-053, T2-R3 Proposition W) is reported as the pairing <F, y/(1+r^2)^2> (mesh part plus the exact far part from the sin(theta)
coefficients of the sectors) together with A_2, B_2, C_2, N_2 and the implied minimal correction size m_min = |<F,phi_2>|/(A_2 + 5 B_2 + C_2)
(d = 0 version; the d N_2 term is added per framework ball). For the FW-T-T4L2-v1 ball (m = 2^-23, d = 6.2e-3) a candidate needs
|<F, phi_2>| <= about 1.2e-7 (A_2 + 5 B_2 + C_2 + 6.2e-3 N_2), i.e. of order 1e-6; d2 has 0.0288 (N4-053).

## 4. Candidates
C1-N1-001 to 004: as in numerics_v01 and the INDEX (001 not admissible; 002, 003 admissible with poor inner region; 004 four-branch L^2 candidate at
the (4,0) floor). Correction to their manifests (the coordinator 22:21Z (c), N4-044/N4-048): radial_max_k = 72 (002), 82 (003), 42 (004), not 25; later
manifests carry the computed value (ipm_snapshot.basis_summary).
C1-N1-005-d2w-j7-x3 (parent C1-A2-d2): d2's 2382 generators plus exact branches 6 and 7 (600 new generators, blocks m <= 69, 79); 421 exact
rows; eleven EXACT-ZERO sectors (h,0) h <= 7, (0,1), (1,1), (2,1); first survivor (3,1) at -2.7904, quarter 34095 (full 68190), then the
invariant (8,0) 17596; 60 GN steps on the X3 proxy from d2 with min-norm start of the new blocks; a0 = 10.2934.
C1-N1-006-8branch-e2 (parent C1-BASE-S131 family, start C1-N1-003): the state-131 eight-branch basis (2140 generators) on the E_2 proxy, 60 steps;
eleven EXACT-ZERO sectors; first survivor (3,1) quarter 4563 then (8,0) 17596; a0 = 4.664.
Both are admissible for every registered framework (R-Ns and R-X3) but far from every threshold (table below) and both violate (B-L2).
Controlled comparison: the d2 warm start (005) beats the state-131-descended family (006) in G0 (1.56 vs 17.8), G1 (7.7 vs 164), P2 (379 vs 7461),
sup|F| (1.5 vs 20) and kappa (1.36 vs 14.1); 006 has the smaller H (10.1 vs 42.3) because its (3,1) sector is 7.5 times smaller.
Lesson for the objective: the raw X3/E_2 proxies (2^18 on ||F||_2^2) push the residual into the near field, where the area is small but the
pointwise values, the point tests and kappa are large; the balanced objective (section 8) adds int F^2 ds dtheta (equal weight per dyadic annulus)
and a kappa^2 penalty. The first balanced run is in progress (numerics_v03).

## 5. Residual table (theory_v01 item 9.1; all FLOAT, float64 GPU, radial Gauss 32/panel x angular midpoint on 0.02 <= r <= 8356.47 plus exact sector far parts; H by the validated evaluator)
| candidate | G0 | G1 | P2 | rF | H | X3 raw | E2 raw (with H) | sup|F| | theta / kappa / (B-L2) | <F,phi_2> | R_nec(2^-18) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1-A2-d2, team values (N3 VALIDATED G0 4.98881700, G1 1.02914187, P2 20.5367651; N4 H 390.2168349 (N4-020), theta <= 2/25 (N4-051), kappa 0.710411 (N4-030), pairing -0.0288020811 (N4-053)) | 4.98882 | 1.02914 | 20.5368 | 2331.57 | 390.217 | 2557.7 | 1.95e5 | 0.105 | <=0.08 / 0.7104 / holds | -0.02880208 | n/a |
| C1-A2-d2 by my diag2 (validation row) | 4.98882 | 1.02914 | 20.5368 | 2331.6 | 390.217 | 2557.8 | 1.95e+05 | 0.1052 | 0.0114 / 0.7092 / holds | -0.0288020811 | 0.000116 |
| C1-N1-005-d2w-j7-x3 | 1.563 | 7.731 | 378.7 | 266.7 | 42.28 | 1328 | 2.117e+04 | 1.54 | 0.0471 / 1.36 / FAIL | -0.156 | 0.0656 |
| C1-N1-006-8branch-e2 | 17.85 | 164 | 7461 | 47.07 | 10.11 | 2.408e+04 | 2.46e+04 | 20.2 | 9.25 / 14.1 / FAIL | 5.676 | 0.144 |
| (balanced 007: next version) | | | | | | | | | | | |
## 6. NORM-T-DYADIC-v1 profiles (item 9.3)

NORM-T-DYADIC-v1 profile of C1-N1-005-d2w-j7-x3 (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| 0.0029, ||rF|| 37.4):
| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |
|---|---|---|---|---|---|
| [0, 0.0625) | 2.09e-05 | 1.23e-06 | 0.00218 | 0.184 | 0.000573 |
| [0.0625, 0.125) | 0.00074 | 8.52e-05 | 0.0905 | 7.69 | 0.0149 |
| [0.125, 0.25) | 0.23 | 0.0527 | 3.54 | 75.8 | 1.38 |
| [0.25, 0.5) | 0.464 | 0.161 | 3.52 | 131 | 1.54 |
| [0.5, 1) | 0.257 | 0.175 | 4.1 | 231 | 0.503 |
| [1, 2) | 0.143 | 0.208 | 3.23 | 202 | 0.215 |
| [2, 4) | 0.221 | 0.697 | 2.07 | 113 | 0.124 |
| [4, 8) | 0.391 | 2.42 | 1.52 | 99.4 | 0.0937 |
| [8, 16) | 0.463 | 5.48 | 0.859 | 58.7 | 0.0663 |
| [16, 32) | 0.61 | 14.5 | 0.458 | 16.2 | 0.0361 |
| [32, 64) | 0.641 | 30.2 | 0.285 | 5.91 | 0.0326 |
| [64, 128) | 0.595 | 57.2 | 0.0795 | 1.27 | 0.00868 |
| [128, 256) | 0.583 | 108 | 0.0485 | 0.55 | 0.00485 |
| [256, 512) | 0.389 | 136 | 0.0192 | 0.196 | 0.00182 |
| [512, 1024) | 0.191 | 130 | 0.0051 | 0.046 | 0.00047 |
| [1024, 2048) | 0.0774 | 104 | 0.00106 | 0.00842 | 9.85e-05 |
| [2048, 4096) | 0.0267 | 71.4 | 0.000184 | 0.00127 | 1.71e-05 |
| [4096, 8192) | 0.00928 | 48.6 | 3.29e-05 | 0.0002 | 3.1e-06 |
| [8192, 1.638e+04) | 0.000846 | 6.99 | 1.79e-06 | 9.76e-06 | 5.02e-07 |

NORM-T-DYADIC-v1 profile of C1-N1-006-8branch-e2 (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| 0.000305, ||rF|| 4.02):
| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |
|---|---|---|---|---|---|
| [0, 0.0625) | 5.58e-05 | 3.29e-06 | 0.00629 | 0.605 | 0.00151 |
| [0.0625, 0.125) | 0.00561 | 0.00065 | 0.219 | 6.65 | 0.0698 |
| [0.125, 0.25) | 0.174 | 0.0392 | 6.14 | 348 | 1.4 |
| [0.25, 0.5) | 3.91 | 1.73 | 71.6 | 2.91e+03 | 16.3 |
| [0.5, 1) | 13.5 | 10.2 | 110 | 4.38e+03 | 20.2 |
| [1, 2) | 8.42 | 11.6 | 77.5 | 3.34e+03 | 13.3 |
| [2, 4) | 5.64 | 15.5 | 51.9 | 3.21e+03 | 4.95 |
| [4, 8) | 3.88 | 21.2 | 28.3 | 2.37e+03 | 1.78 |
| [8, 16) | 1.62 | 17.4 | 8.97 | 881 | 0.668 |
| [16, 32) | 0.706 | 15.2 | 1.92 | 209 | 0.0965 |
| [32, 64) | 0.277 | 12.8 | 0.388 | 38.3 | 0.0226 |
| [64, 128) | 0.148 | 12.2 | 0.0633 | 4.5 | 0.00424 |
| [128, 256) | 0.0391 | 6.93 | 0.0102 | 0.619 | 0.00056 |
| [256, 512) | 0.0278 | 9.97 | 0.00242 | 0.102 | 0.000188 |
| [512, 1024) | 0.0159 | 10.9 | 0.000632 | 0.0174 | 5.15e-05 |
| [1024, 2048) | 0.00695 | 9.4 | 0.000139 | 0.00283 | 1.08e-05 |
| [2048, 4096) | 0.00254 | 6.84 | 2.57e-05 | 0.000421 | 2.02e-06 |
| [4096, 8192) | 0.000928 | 4.89 | 4.87e-06 | 6.77e-05 | 3.96e-07 |
| [8192, 1.638e+04) | 8.7e-05 | 0.718 | 2.75e-07 | 3.41e-06 | 6.7e-08 |

Reading: for C1-N1-005 the L^2 mass sits in [0.25, 2) (the near field) while d2's sits in [8, 64); the far field beyond 8356 is negligible for both new candidates (the (6,0) sector is gone), which is why H dropped from 390 to 42 (005) and 10 (006).
## 7. Point tests NORM-T-PTNEC-v1 / PTSYM-v1 (item 9.5), FLOAT maxima over the mesh points (not certified point values)
| candidate | R_nec(2^-18) | at (r, theta) | R_nec(2^-17) | R_nec(2^-16) | R_nec(5 2^-18) | R_sym axis (2^-18) |
|---|---|---|---|---|---|---|| C1-A2-d2 | 0.000116 | (0.529, 1.57) | 0.000161 | 0.000222 | 0.000247 | 0.000161 |
| C1-N1-005-d2w-j7-x3 | 0.0656 | (0.259, 1.57) | 0.0863 | 0.112 | 0.121 | 0.0106 |
| C1-N1-006-8branch-e2 | 0.144 | (0.487, 0.569) | 0.194 | 0.256 | 0.28 | 0.104 |
The framework balls have radius 2^-14 (FW-T-T4L2-v1) to 2^-16 (FW-A2-Db): every candidate, d2 included, is excluded by these maxima by 2 to 4 orders of magnitude (consistent with T4-007/T4-055).
## 7b. Hdot^-1 FLOAT evaluator: version statement (the coordinator 23:19Z item 2, N4-067)
numerics/lib/ipm_hminus1.py (sha256 cb01d01d95286b2d3a241a6045b7e8df8590ecfd0ea79e4d3a78a5fabbc4b98b): modes sin(n theta) (odd n) by the midpoint rule; radial double integral in the cumulative form
I_n = 2 int F_n r^4 J~_n ds with J~_n(r) = int_0^s F_n e^((n+2)(s'-s)) ds' computed from the exact exponential moments of the Lagrange basis on
each Gauss panel in s = log r (64-node quadrature of the moments for (n+2) h < 64, forward recursion above); exterior r > 8356.47 by the exact
sectors (outer-outer with the factor 2 for the two orderings, i.e. prefactor pi/n, and the inner-outer cross terms). The prefactor error
reported in N4-067 was found and fixed at 23:12Z (power-tail test: 9.758244 vs exact 9.758237). Values: d2 390.2169 (N4-020 390.2168, 2.2e-7),
C1-N1-005 42.28 (parts of a pre-fix run recombined), C1-N1-006 10.105 (fixed code). All FLOAT.

## 8. Next steps (batch N) and what the theory should take from v02
1. Balanced objective runs from C1-N1-005: X3 proxy + 2^18 R_ref^2 int F^2 ds dtheta (R_ref = 10) + 1e6 kappa^2; then with the multi-scale
   inner functions (legqs, R0 = 10, 100). Targets: (B-L2) restored (kappa < 0.7), sup|F| below d2's 0.105, G0 below 1, H below 40. Snapshot 007.
2. For every candidate the full table of section 5 plus the dyadic profile; exact JSON and sha256 to the N3 numerics worker for VALIDATED components.
3. Message to batch T (unchanged from v01 but now quantified): the number of exact branches is cheap (we have eight exactly); the mid-field
   accuracy out to r of order 100-1000 is the lever for every framework; the (B-L2) condition is a real design constraint that the raw
   L^2-weighted objectives violate; a framework whose low component is measured with a weight decaying like r^-1 (i.e. ||F||_(ds dtheta)-type)
   would match what the optimizer can control, but R3 of theory_v01 says such weights are outside the admissible range.

