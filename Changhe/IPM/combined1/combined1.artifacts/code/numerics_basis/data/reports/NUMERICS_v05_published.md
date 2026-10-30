# numerics_v05 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v05; UTC time: 2026-10-29T02:32:22Z; supersedes numerics_v04 (sha256 1aab468111951bce33f78f6f83c9ec00c5686cb0682b13b96ba2f93a1974ce9b), numerics_v03 (sha256 4d91a51db33f7f258fca54a48ec718e11a4ed26c78bb5eb3f41d8e2d688290a8); supersedes numerics_v02 (sha256 bc3f7c6e9d507df91084984ac481c3d484935cd0c33ebea1604e996a6fbc4569); author: The N1/N2 numerics worker; supersedes numerics_v01 (sha256 975aa84c943a0ab52dfd2d22baf1eb54f4c384f1f9d57a4ce0738551210cfa52).
- consulted (v05): theory_v02.md (the T1/T3 theory worker, 2026-10-29T01:44Z; sections 0, 2, 5.2, 8, 9 and R read; ACK in its status log (not published) 01:49Z); theory_v01.md;
  the coordinator team notes through 02:23Z (closure matrix v31; requests of 01:47Z, 02:10Z, 02:19Z) and the run contracts; the N4 numerical auditor team notes through 02:27Z
  (N4-131 to N4-142: 007 G0 and theta CONFIRMED, FW-T-DYADIC-Y-v1 excluded at 007 for every 0 < a < 2, 009 kappa 0.71321 CONFIRMED, 010 point exclusions
  CONFIRMED, rounded-coefficient cutoff a > 2/c, multi-scale moment integrator N4-137) and status file; the N3 numerics worker team notes through 02:28Z (007
  VALIDATED G0, rF, G1, P2; exact N_a(d2) validation of wlap_norms.py; exact N_a(007) running) and status file; the second model/farfield-structure/answer.md.
  Batch N consultation for this version: The N3 numerics worker and the N4 numerical auditor results above are cited with their IDs; no number of theirs is restated as mine.
- theory version followed: theory_v02 (norm IDs used in addition: NORM-T-WEAK-v1, NORM-T-WL2-v1, NORM-T-WLAP-v1; necessary conditions NC-T-DIST, NC-T-DYADIC-LAP). Norm IDs: NORM-A2-E2 components, NORM-T-X3-v1 (raw-component proxy), NORM-T-DYADIC-v1,
  NORM-T-PTNEC-v1, NORM-T-PTSYM-v1. Candidate IDs: C1-BASE-S131, C1-A2-d2, C1-N1-001..004, C1-N1-005..010 (working file INDEX.md (not published)); new in v04: C1-N1-008-d2w-j7-x3bal, C1-N1-009-d2w-j7-x3balk, C1-N1-010-d2w-j7-x3bal-legqs.
- Corrections since v02: section 3b restated after the second model referee (the second model/farfield-structure/answer.md); section 6 prose corrected after the N4 numerical auditor N4-078; section 7 table separator fixed (the coordinator 23:38Z); Hdot^-1 outer prefactor (N4-067) fixed at 23:12Z, every H below is from the fixed code or the fixed recombination.
- Response to theory_v01: section R. ACK of theory_v01 recorded in its status log (not published) at 22:16Z.

## R2. Response to theory_v02 (01:44Z)
R2-1. Request order adopted (theory_v02 section 9 item 2): for 007, 009 and 010 the weak distance (NORM-T-WEAK-v1, a = 0, k = 0..8), the weighted
L^2 norms NORM-T-WL2-v1 at a = 1/2, 3/4, 1, 6/5 and the weighted Laplacian N_a on the cover {0, 1/4, ..., 3/2, 1 + 1/c} with the NC-T-DYADIC-LAP
cell test are computed FLOAT by optimization/weak_tests.py (I_k = mesh quadrature plus a finite asymptotic far correction beyond r = 8356.47 from the
exact surviving sectors, not an exact far part; A_k, B_k, C_k on the mesh region; exact H_k);
values in section 5b. Every future manifest carries the weak distance.
R2-2. R5 accepted: the tail cost at onset T = 10 is NOT monotone in the number of branches (order 9: 943.6, order 10: 448.9); the correct statement is
that it stays between about 1.4e2 and 1.0e3 for 4 to 16 branches. The order-onset trade-off numbers (6611 for 12 branches, 881 for 16) stand.
R2-3. R2 noted: an r^-1 low weight is admissible; the relevant framework is FW-T-DYADIC-Y-v1, RULED OUT at 007 for 4/5 <= a < 2 and open for
0 < a < 4/5; FLOAT N_a values on the cover are in section 5b, certified bounds are the N4 numerical auditor's.
R2-4. Design consequence for batch N: the fixed-c weak L^2 distance is the quantity to minimize next (007: certified LB 4.4e-5 against scalar budgets
<= 3.8e-6, graded 4.6e-4); the k = 0..8 pairings are linear functionals of F and will enter the objective as explicit rows.

## R. Response to theory_v01 (kept from v02/v03)
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
consequence (exact pure-exterior formula, FULL-CIRCLE norms): with onset T = 10 the tail cost ||F||_(L^2(r>T)) does NOT decrease systematically with
the number of exact branches: it is 143 to 164 for 7 to 8 branches, 944 at 9, 449 at 10, 590 at 12, 1008 at 13, 812 at 16 (not monotone: order 9 exceeds
order 10, N4-103; the growth of the amplitudes balances the decay); with T = 100 it falls by a
factor of about 0.38 (= 3 x 100^(-lambda)) per added branch on average (3.75 at 7 branches, 1.53 at 8, 3.15 at 9, 0.54 at 10, 0.089 at 12, 0.002 at
16); with T = 1000 it is 1.4e-5 at 12 branches and 4.9e-9 at 16. For an isolated sector to fall below 1e-8 the onset must exceed about 6611 (12
branches) or 881 (16 branches): an order-onset trade-off, not a necessity of T >= 1000 (the second model referee 23:44Z, the second model/farfield-structure/answer.md;
the same referee confirmed the formula, the quoted amplitudes and exponents, the absence of exponent collisions and integer resonances for
h <= 20, q <= 8, and flagged the near-resonance (alpha_8+1)^2 - 4 = 0.1148 behind the order-9 jump). The convergence-radius estimate is
HEURISTIC (a root at one order, not a limsup), and the identification of the stationary series with an exact solution is unproved.
Exterior Hdot^-1 of a zero-extended sector 1_(r>T) r^e E, E = sum b_k sin(k theta): ||.||_H^2 = pi T^(2e+4)/(-2e-4) sum_k b_k^2/(k(k-e-2)) for
e < -2 (referee; implemented in ipm_farpart.hminus1_far_sector; reported per surviving sector in the diag2 files from v03 on). Hence the number of exact branches is not the binding constraint for the
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
The weak probe (N4-053, T2-R3 Proposition W) is reported as the pairing <F, y/(1+r^2)^2> (mesh part plus a finite asymptotic far correction from the sin(theta)
coefficients of the sectors) together with A_2, B_2, C_2, N_2 and the implied minimal correction size m_min = |<F,phi_2>|/(A_2 + 5 B_2 + C_2)
(d = 0 version; the d N_2 term is added per framework ball). For the FW-T-T4L2-v1 ball (m = 2^-23, d = 6.2e-3) a candidate needs
|<F, phi_2>| <= about 1.2e-7 (A_2 + 5 B_2 + C_2 + 6.2e-3 N_2), i.e. of order 1e-6; d2 has 0.0288 (N4-053).

## 4. Candidates
GPU REVOCATION. At 2026-10-29T00:57:59Z the lane's GPU was withdrawn (lane file GPU_UPDATE.md); the three optimizations then running were stopped
(two finalized exactly from their last checkpoints on CPU: 009 at step 56/60, 010 at step 39/60; the E_2 + legqs run was lost before its first
step). All further numerics run on CPU (one Gauss-Newton step for 2982 generators takes about 150 s on one core with the reduced radial rule,
against 40 s on the GPU); two CPU runs are in progress (E_2-balanced continuation of 007; E_2-balanced with the legqs functions from 007).
New since v03 (all PRIMARY chart, same 421 exact rows and eleven EXACT-ZERO sectors, first survivor (3,1); FLOAT values in the table of section 5):
- C1-N1-008 (X3 objective without the rF term, from 005): worse than 007 in G0, H, kappa and the weak pairing: the rF (Hardy) term tames the
  surviving far sectors and must be kept even for the no-H route.
- C1-N1-009 (X3 objective with kappa penalty 3e8, from 007): lowest sup|F| (0.0935 < d2's 0.105) and largest (B-L2) margin (+0.087, kappa 0.712),
  best P2 (110) and G1 (2.09); but G0 1.10, H 7.0 and weak pairing 0.047 are worse than 007. Second reference for batch T.
- C1-N1-010 (005 + 960 multi-scale legqs inner functions, X3 objective, 39 steps): against 008 (same objective, no legqs, 60 steps) G0 0.82 vs
  1.42, H 27.6 vs 43, X3 837 vs 941 in fewer steps; sup|F|, P2 and kappa worse. Evidence that mid-field resolution helps the low components.
C1-N1-007-d2w-j7-e2bal (NEW; parent C1-A2-d2; exact JSON sha256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21): the C1-N1-005 basis and constraints (2982 generators, 421 exact rows),
re-optimized for 60 GN steps with the BALANCED E_2 objective 2^18(||F||^2 + (20/21)||rF||^2) + 2^14||grad F||^2 + ||omega D^2F||^2
+ 2^18*100 int F^2 ds dtheta + 1e6 kappa^2. EXACT: eleven zero sectors (through (7,0), (0,1), (1,1), (2,1)); first survivor (3,1) at -2.7904 with
quarter norm 2452.5 (full 4905.1; d2 71294), then the invariant (8,0) 17596. FLOAT: G0 0.3767 (d2 4.989; 13x), G1 3.439 (d2 1.029), P2 190.8
(d2 20.54), H 0.6355 (d2 390.2; 614x), rF 7.78 (d2 2331.6), X3 proxy 517 (d2 2558), E_2 proxy with H 606.8 (d2 1.95e5; 320x), sup|F| 0.138
(d2 0.105); (B-L2) HOLDS in FLOAT (theta 0.0114, kappa 0.7269, margin +0.072); weak pairing +1.55e-4 (d2 -0.0288; 186x smaller), m_min(d=0) 1.5e-5;
R_nec(2^-18) 1.02e-3 (d2 1.2e-4); a0 = 10.3120. Still about 1e8 (G0 against FW-T-T4L2-v1's 1.19e-8) to 1e9 (E_2 against FW-A2-Db) above the
thresholds, but it is the first admissible candidate with all components finite and moderate, the signed condition satisfied, and the far field
(H, rF, weak pairing) under control. Next: stronger kappa margin, the legqs multi-scale inner functions, and longer runs (section 8).
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
| C1-N1-007-d2w-j7-e2bal (best in G0, H, E_2, pairing) | 0.3767 | 3.439 | 190.8 | 7.828 | 0.6355 | 517.1 | 606.8 | 0.138 | 0.0114 / 0.7269 / holds (margin +0.072) | 0.0001551 | 0.00102 |
| C1-N1-009-d2w-j7-x3balk (kappa penalty 3e8, X3 objective, from 007) | 1.096 | 2.086 | 109.8 | 43.78 | 7.001 | 631 | 3555 | 0.0935 | 0.0113 / 0.712 / holds (+0.087) | 0.04721 | 0.000767 |
| C1-N1-008-d2w-j7-x3bal (X3 objective, no rF; comparison) | 1.423 | 4.18 | 262.9 | 284.7 | 43.03 | 941.4 | 21523 | 0.155 | 0.0114 / 0.845 / fails (-0.046) | 4.906e-4 | 3.88e-3 |
| C1-N1-010-d2w-j7-x3bal-legqs (005 + 960 multi-scale legqs functions, X3 objective, 39 steps) | 0.8163 | 5.091 | 318.8 | 186.9 | 27.65 | 837.2 | 1.384e+04 | 0.206 | 0.0116 / 0.9219 / fails (-0.123) | 0.01754 | 0.00612 |
## 5b. theory_v02 cheap tests (FLOAT; optimization/weak_tests.py; rule radial Gauss 32/panel x midpoint 180 on 0.02 <= r <= 8356.47; I_k with a finite asymptotic far correction from the exact surviving sectors beyond 8356.47)
C1-N1-007-d2w-j7-e2bal: weak-distance lower bound (NORM-T-WEAK-v1, a = 0, max over k = 0..8) 3.7931e-05 (N4-091 certified 4.3987e-5);
NORM-T-WL2-v1 at a = 1/2, 3/4, 1, 6/5: 0.1756, 0.1275, 0.0958, 0.0779; per-annulus k = 0 pairing: [0.125,0.25): +4.51e-06; [0.25,0.5): +2.53e-05; [0.5,1): +1.18e-04; [1,2): +1.45e-04; [2,4): -1.42e-04; [4,8): -3.86e-05; [8,16): +3.19e-05; [16,32): +1.38e-05; [32,64): -2.75e-06.
| k | I_k | D_k = A_k+B_k+C_k | H_k | m >= |
|---|---|---|---|---|
| 0 | 1.5510e-04 | 9.5820 | 1.0000 | 1.6186e-05 |
| 1 | 9.6383e-05 | 5.3003 | 0.6091 | 1.8184e-05 |
| 2 | 7.4115e-05 | 3.6362 | 0.3390 | 2.0382e-05 |
| 3 | 6.3583e-05 | 2.7485 | 0.2161 | 2.3134e-05 |
| 4 | 5.7487e-05 | 2.1979 | 0.1498 | 2.6155e-05 |
| 5 | 5.3330e-05 | 1.8241 | 0.1100 | 2.9235e-05 |
| 6 | 5.0142e-05 | 1.5545 | 0.0842 | 3.2257e-05 |
| 7 | 4.7509e-05 | 1.3511 | 0.0665 | 3.5162e-05 |
| 8 | 4.5236e-05 | 1.1926 | 0.0538 | 3.7931e-05 |
NORM-T-WLAP-v1 and the NC-T-DYADIC-LAP cell test (fails everywhere; the open pair FW-T-DYADIC-Y-v1 x 007 on 0 < a < 4/5 closes if an LB is certified):
| a | N_a(007) FLOAT | 5^((a-2)/2) N_a | ceiling B(a) | passes |
|---|---|---|---|---|
| 0.0000 | 343.491 | 68.698 | 39.5942 | False |
| 0.2500 | 260.659 | 63.749 | 22.2947 | False |
| 0.5000 | 206.476 | 61.751 | 12.1309 | False |
| 0.7500 | 168.983 | 61.800 | 6.0445 | False |
| 1.0000 | 141.892 | 63.456 | 2.5066 | False |
| 1.2500 | 121.600 | 66.500 | 0.6677 | False |
| 1.5000 | 105.931 | 70.840 | 0.0180 | False |
| 1.5524 | 103.094 | 71.912 | nan | None |
C1-N1-009-d2w-j7-x3balk: weak-distance lower bound 6.0319e-03 (k = 0: 4.932e-03; 160x that of 007: its pairing 0.047 is what
theory_v02 R10 anticipated), WL2 a = 1: 0.1564, N_a fails the LAP test at every a (a = 1/2: 40.79 vs 12.13).
C1-N1-010-d2w-j7-x3bal-legqs: weak-distance lower bound 2.3087e-03 (61x 007), WL2 a = 1: 0.1396, N_(1/2) = 401.1 (fails the LAP test at every a).
Ordering by the decisive quantity (fixed-c weak distance, FLOAT): 007 3.8e-5 < 008 8.1e-5 < 010 2.3e-3 < 009 6.0e-3 < 005 (N4: 1.6e-2) < d2 (0.30 certified).
C1-N1-008-d2w-j7-x3bal: weak-distance lower bound (NORM-T-WEAK-v1, a = 0, max over k = 0..8) 8.1181e-05 (at k = 2; k = 0: 5.120e-05; I_0 = +4.9061e-04); NORM-T-WL2-v1 at a = 1/2, 3/4, 1, 6/5: 0.2694, 0.1614, 0.1152, 0.0958; N_a FLOAT at a = 0, 1/2, 1: 971.47, 359.28, 206.12 (NC-T-DYADIC-LAP cell test passes at: no a); per-annulus k = 0 pairing (|.| > 1e-6): [0.0625,0.125): +2.16e-05; [0.125,0.25): -0.000274; [0.25,0.5): +5.69e-05; [0.5,1): +0.000109; [1,2): +4.25e-05; [2,4): -1.46e-05; [4,8): +0.00082; [8,16): -0.000522; [16,32): +0.000469; [32,64): -0.00016; [64,128): -5.12e-05; [128,256): -6.09e-06.
Reading of 008: its weak distance 8.1e-5 is only 2.1x that of 007 (4.9e-4 pairing against 1.6e-4), although its G0, H and kappa are far worse; its
k = 0 pairing is a sum of alternating annulus contributions of size up to 8e-4 in 4 <= r < 64 (large cancellation between annuli), whereas 009 and 010
(kappa penalty, legqs functions) have one-signed pairings of 1e-2 created in 0.5 <= r < 8. So the objectives that improve the pointwise and
(B-L2) numbers (009) or the mid-field L^2 numbers (010) both raise the weak distance by two orders of magnitude; the weak distance is small only where
the objective keeps the near-field annuli in balance, and in every case it is produced by cancellation between annuli, not by a small residual.
The d2 calibration row of weak_tests.py (expected pairing -0.0288 and distance 0.2955 against N4-053 / T4-064) is running (core 54) and will be in
v06; until then the FLOAT distances above are calibrated only through 007 (3.79e-5 FLOAT against N4-091's certified 4.3987e-5, a 14 percent
difference that is consistent with the mesh quadrature of the A_k, B_k, C_k denominators and the finite far correction; the FLOAT value is NOT a bound).

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

Reading (corrected after the N4 numerical auditor N4-078; v02 misread the table): for C1-N1-005 the L^2 mass is in the mid field, 69.2 percent of ||F||_2^2 in 8 <= r < 256 (largest annulus [32, 64)), only 12.4 percent in [0.25, 2); the NEAR field carries the point peaks (sup|F| = 1.54 at r = 0.26) and the derivative energy (87.2 percent of ||grad F||_2^2 and 81.6 percent of ||omega D^2 F||_2^2 in r < 2). The far field beyond 8356 is negligible for both new candidates (the (6,0) sector is gone), which is why H dropped from 390 (d2) to 42 (005) and 10 (006).
NORM-T-DYADIC-v1 profile of C1-N1-007-d2w-j7-e2bal (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| 6.14e-05, ||rF|| 0.92):
| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |
|---|---|---|---|---|---|
| [0, 0.0625) | 3.41e-06 | 2e-07 | 0.000392 | 0.0366 | 0.000124 |
| [0.0625, 0.125) | 0.000182 | 2.06e-05 | 0.00696 | 0.309 | 0.00197 |
| [0.125, 0.25) | 0.000964 | 0.0002 | 0.0465 | 2.11 | 0.00785 |
| [0.25, 0.5) | 0.00533 | 0.00226 | 0.253 | 15.5 | 0.0237 |
| [0.5, 1) | 0.031 | 0.0254 | 1.32 | 92.8 | 0.0897 |
| [1, 2) | 0.0891 | 0.148 | 2.06 | 131 | 0.101 |
| [2, 4) | 0.196 | 0.605 | 2.06 | 93.8 | 0.138 |
| [4, 8) | 0.248 | 1.43 | 1.18 | 40.1 | 0.122 |
| [8, 16) | 0.145 | 1.59 | 0.324 | 9.18 | 0.0314 |
| [16, 32) | 0.091 | 1.8 | 0.108 | 2.51 | 0.0113 |
| [32, 64) | 0.0566 | 2.53 | 0.0306 | 0.603 | 0.00262 |
| [64, 128) | 0.0146 | 1.39 | 0.00412 | 0.0792 | 0.000582 |
| [128, 256) | 0.0194 | 3.58 | 0.00259 | 0.039 | 0.000211 |
| [256, 512) | 0.0117 | 3.99 | 0.000841 | 0.0113 | 9.95e-05 |
| [512, 1024) | 0.00463 | 3.06 | 0.000172 | 0.00202 | 2.38e-05 |
| [1024, 2048) | 0.00148 | 1.94 | 2.79e-05 | 0.000287 | 3.9e-06 |
| [2048, 4096) | 0.000432 | 1.15 | 3.83e-06 | 3.42e-05 | 4.81e-07 |
| [4096, 8192) | 0.000155 | 0.828 | 5.62e-07 | 4.35e-06 | 9.23e-08 |
| [8192, 1.638e+04) | 1.61e-05 | 0.133 | 2.68e-08 | 1.81e-07 | 1.67e-08 |

Reading for 007: largest L^2 annulus [4, 8) with 43 percent of ||F||_2^2; the balanced objective removed the near-field peak of 005 (sup|F| 0.138 at r = 2-4).
NORM-T-DYADIC-v1 profile of C1-N1-009-d2w-j7-x3balk (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| 0.000313, ||rF|| 4.02):
| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |
|---|---|---|---|---|---|
| [0, 0.0625) | 1.75e-06 | 1.03e-07 | 0.00021 | 0.0208 | 6.48e-05 |
| [0.0625, 0.125) | 0.000115 | 1.32e-05 | 0.00508 | 0.195 | 0.00186 |
| [0.125, 0.25) | 0.00131 | 0.000293 | 0.0245 | 0.911 | 0.0086 |
| [0.25, 0.5) | 0.00924 | 0.00397 | 0.264 | 16 | 0.029 |
| [0.5, 1) | 0.0383 | 0.0313 | 0.837 | 57.8 | 0.065 |
| [1, 2) | 0.11 | 0.183 | 1.05 | 68.8 | 0.0815 |
| [2, 4) | 0.275 | 0.887 | 1.06 | 49.9 | 0.0922 |
| [4, 8) | 0.531 | 3.26 | 0.902 | 30 | 0.0935 |
| [8, 16) | 0.683 | 8.2 | 0.62 | 15.8 | 0.0675 |
| [16, 32) | 0.501 | 10.9 | 0.365 | 8.51 | 0.0384 |
| [32, 64) | 0.262 | 11.6 | 0.0877 | 2.02 | 0.00913 |
| [64, 128) | 0.165 | 15.1 | 0.0195 | 0.281 | 0.00287 |
| [128, 256) | 0.11 | 19.7 | 0.0077 | 0.0763 | 0.00128 |
| [256, 512) | 0.0587 | 20.2 | 0.00229 | 0.0203 | 0.000383 |
| [512, 1024) | 0.0254 | 17 | 0.000518 | 0.00396 | 9e-05 |
| [1024, 2048) | 0.00943 | 12.6 | 9.77e-05 | 0.00064 | 1.76e-05 |
| [2048, 4096) | 0.00308 | 8.19 | 1.58e-05 | 8.84e-05 | 2.87e-06 |
| [4096, 8192) | 0.00103 | 5.39 | 2.7e-06 | 1.3e-05 | 5e-07 |
| [8192, 1.638e+04) | 9.22e-05 | 0.761 | 1.43e-07 | 6.11e-07 | 7.85e-08 |
Reading for C1-N1-009-d2w-j7-x3balk: largest L^2 annulus [8, 16) with 39 percent of the mesh ||F||_2^2; sup|F| 0.0935.
NORM-T-DYADIC-v1 profile of C1-N1-010-d2w-j7-x3bal-legqs (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| 0.00195, ||rF|| 24.6):
| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |
|---|---|---|---|---|---|
| [0, 0.0625) | 2.54e-05 | 1.49e-06 | 0.00271 | 0.238 | 0.000688 |
| [0.0625, 0.125) | 0.00147 | 0.000167 | 0.0461 | 2.27 | 0.0196 |
| [0.125, 0.25) | 0.0191 | 0.0043 | 0.623 | 25.6 | 0.165 |
| [0.25, 0.5) | 0.0417 | 0.016 | 1.63 | 84.9 | 0.156 |
| [0.5, 1) | 0.0879 | 0.0689 | 3.14 | 192 | 0.206 |
| [1, 2) | 0.134 | 0.216 | 2.85 | 186 | 0.162 |
| [2, 4) | 0.201 | 0.623 | 1.61 | 92.6 | 0.123 |
| [4, 8) | 0.26 | 1.6 | 1.19 | 97.4 | 0.0712 |
| [8, 16) | 0.272 | 3.14 | 0.766 | 63.1 | 0.0429 |
| [16, 32) | 0.392 | 9.79 | 0.495 | 17.8 | 0.0307 |
| [32, 64) | 0.431 | 19.4 | 0.255 | 5.96 | 0.0279 |
| [64, 128) | 0.231 | 20 | 0.0665 | 1.21 | 0.0096 |
| [128, 256) | 0.115 | 20.6 | 0.014 | 0.213 | 0.00207 |
| [256, 512) | 0.119 | 46.5 | 0.00418 | 0.0433 | 0.000426 |
| [512, 1024) | 0.173 | 124 | 0.00406 | 0.0357 | 0.000396 |
| [1024, 2048) | 0.0785 | 103 | 0.00103 | 0.00823 | 0.000122 |
| [2048, 4096) | 0.0224 | 59.1 | 0.000141 | 0.000964 | 1.7e-05 |
| [4096, 8192) | 0.00683 | 35.5 | 2.09e-05 | 0.000123 | 2.88e-06 |
| [8192, 1.638e+04) | 0.000584 | 4.82 | 1.03e-06 | 5.32e-06 | 4.54e-07 |
Reading for C1-N1-010-d2w-j7-x3bal-legqs: largest L^2 annulus [32, 64) with 28 percent of the mesh ||F||_2^2; sup|F| 0.206.
Reading across 007, 009, 010 (theory_v02 R10d): the L^2 mass of every balanced candidate sits in 2 <= r < 64 (mid field), the derivative energy in
0.5 <= r < 8, and the weak pairing is created in 0.5 <= r < 8 (section 5b). The far field beyond r = 64 contributes less than 1e-6 to the pairing and
less than 2 percent to G0^2 for 007 and 009; for 010 the legqs functions at scale R0 = 100 leave a visible bump in ||rF|| at 256 <= r < 2048
(46 to 124 against 3 to 4 for 007), which is why its rF is 187 against 7.8.

## 7. Point tests NORM-T-PTNEC-v1 / PTSYM-v1 (item 9.5), FLOAT maxima over the mesh points (not certified point values)
| candidate | R_nec(2^-18) | at (r, theta) | R_nec(2^-17) | R_nec(2^-16) | R_nec(5 2^-18) | R_sym axis (2^-18) |
|---|---|---|---|---|---|---|
| C1-A2-d2 | 0.000116 | (0.529, 1.57) | 0.000161 | 0.000222 | 0.000247 | 0.000161 |
| C1-N1-005-d2w-j7-x3 | 0.0656 | (0.259, 1.57) | 0.0863 | 0.112 | 0.121 | 0.0106 |
| C1-N1-006-8branch-e2 | 0.144 | (0.487, 0.569) | 0.194 | 0.256 | 0.28 | 0.104 |
| C1-N1-007-d2w-j7-e2bal | 0.00102 | (0.735, 1.44) | 0.00143 | 0.00198 | 0.0022 | 0.00136 |
| C1-N1-008-d2w-j7-x3bal | 0.00388 | (0.235, 1.57) | 0.00523 | 0.00694 | 0.00758 | 0.00256 |
| C1-N1-009-d2w-j7-x3balk | 0.000767 | (0.579, 1.42) | 0.00107 | 0.00147 | 0.00163 | 0.000933 |
| C1-N1-010-d2w-j7-x3bal-legqs | 0.00612 | (0.235, 1.57) | 0.00825 | 0.0109 | 0.0119 | 0.00339 |
The framework balls have radius 2^-14 (FW-T-T4L2-v1) to 2^-16 (FW-A2-Db): every candidate, d2 included, is excluded by these maxima by 2 to 4 orders
of magnitude (consistent with T4-007/T4-055; the CONFIRMED exact point exclusions are N4-106 (008), N4-115 (009), N4-123 (010)). 009 has the smallest
FLOAT R_nec (7.7e-4) but the largest weak distance of the three balanced candidates (section 5b): the point tests and the weak distance pull in
different directions under our objectives, and the weak distance is the one that excludes 007 (coordinator matrix v31: every snapshot 001 to 010 is
RULED OUT in every specified ball by its fixed-c L^2 distance).
## 7b. Hdot^-1 FLOAT evaluator: version statement (the coordinator 23:19Z item 2, N4-067)
numerics/lib/ipm_hminus1.py (sha256 cb01d01d95286b2d3a241a6045b7e8df8590ecfd0ea79e4d3a78a5fabbc4b98b): modes sin(n theta) (odd n) by the midpoint rule; radial double integral in the cumulative form
I_n = 2 int F_n r^4 J~_n ds with J~_n(r) = int_0^s F_n e^((n+2)(s'-s)) ds' computed from the exact exponential moments of the Lagrange basis on
each Gauss panel in s = log r (64-node quadrature of the moments for (n+2) h < 64, forward recursion above); exterior r > 8356.47 by the exact
sectors (outer-outer with the factor 2 for the two orderings, i.e. prefactor pi/n, and the inner-outer cross terms). The prefactor error
reported in N4-067 was found and fixed at 23:12Z (power-tail test: 9.758244 vs exact 9.758237). Values: d2 390.2169 (N4-020 390.2168, 2.2e-7),
C1-N1-005 42.28 (parts of a pre-fix run recombined), C1-N1-006 10.105 (fixed code). All FLOAT.

## 8. Status at publication, next steps (batch N) and what the theory should take from v05
Status (FLOAT unless stated). Best candidate: C1-N1-007 (certified: G0 0.37668932 (N3 VALIDATED, N4-139 CONFIRMED), theta <= 2/25 and (B-L2) with
kappa_HS 0.72816 (N4-111/T4-162 CONFIRMED), fixed-c L^2 distance LB 4.3987e-5 (N4-091 CONFIRMED)). It misses FW-T-T4L2-sharpw-v1 by a certified
factor above 1.83e6 in X_(s,w) (the coordinator v31) and is excluded from every registered ball by the weak distance (budget <= 3.8e-6 scalar, 4.6e-4 graded).
Every other snapshot is worse in the weak distance by a factor 2.1 (008), 61 (010) and 160 (009). FW-T-DYADIC-Y-v1 is RULED OUT at 007 for every 0 < a < 2
(N4-132, AUDITED conditional), so my FLOAT N_a values in section 5b are now calibration data only; the N3 numerics worker's exact N_a(007) (running, about 03:15Z)
decides the FLOAT disagreement with the T1/T3 theory worker's partial sums (N4's reading: the partial sum over modes 1 to 15 and my all-mode value need not agree).
Running (CPU, cores 52 and 53; each about 150 s per Gauss-Newton step on the reduced radial rule): (a) E_2-balanced + legqs multi-scale functions from
007, 20 steps (step 17 at 02:30Z, objective 1.707e7 against 1.711e7 at the start: a plateau); (b) E_2-balanced with kappa penalty 1e7 from 009, 30 steps
(step 22 at 02:30Z, objective 1.82e8, rejections dominate: plateau). Both will be snapshotted (011, 012) with weak tests first (theory_v02 order), then
point tests and the section 5 table; expected before 03:30Z. Neither is expected to beat 007 in the weak distance.
Next (in order):
1. Weak-pairing rows. The nine pairings I_k = <F, phi_k>, k = 0..8, of NORM-T-WEAK-v1 are linear in F (quadratic in the coefficients) and will enter the
   balanced objective as nine explicit residual rows with weight w_k such that w_k |I_k| of order 1e-5 competes with the other terms (w_k about
   2^18 x 1e2 / 1e-5); implementation as extra rows in ipm_opt2 (like the kappa row), run from 007 on CPU (reduced mesh, 20 steps). Target: weak
   distance below 3.8e-6 (factor 11.6) while (B-L2) (kappa margin), G0 and sup|F| stay within 20 percent of 007. This is a test of whether the
   exclusion by NC-T-DIST is a soft constraint of the objective or a structural obstruction of the basis. Note for the theory: driving I_k to zero
   removes the exclusion by these nine test functions, it does not make the candidate pass a sufficient condition; the smallness gap of 1.8e6 in
   X_(s,w) is untouched by it.
2. If 1 succeeds in FLOAT: exact snapshot 013 and the weak distance certified by the N4 numerical auditor (N4-091 method); if it fails (G0 or kappa blow up), report the
   trade-off curve (weak distance against G0 and kappa) as the quantitative answer to "can the fixed-c L^2 distance be optimized away".
3. Message to batch T (unchanged from v01, now quantified): the number of exact branches is cheap (eight exact branches, eleven EXACT-ZERO sectors in
   every balanced candidate); the mid-field accuracy out to r of order 100 to 1000 is the lever for every framework; (B-L2) is a real design
   constraint that the raw L^2-weighted objectives violate (008, 010) and the balanced objective satisfies with margins +0.072 (007) to +0.087 (009);
   the fixed-c L^2 distance is created in 0.5 <= r < 8 by all our objectives; a theory whose ball is not centered at the fixed c (or whose distance
   test allows the scaling direction) would remove the exclusion that now rules out every snapshot, and the quantitative evidence for that request
   is section 5b.
4. CPU-only consequences (honest statement): one Gauss-Newton step for 2982 generators takes 150 s on one core; 20-step runs take about one hour.
   No run with the full radial rule (416 panels) or with more than about 4000 generators is feasible before the freeze; the multi-scale (legqs)
   designs with R0 = 1000, which section 3b identifies as the lever for the mid field beyond r = 100, cannot be optimized within the budget on CPU.
   They are documented as the first item of the continuation plan (NUMERICS_FINAL.md section 7).
