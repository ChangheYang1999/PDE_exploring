# numerics_v09 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v09; UTC time: 2026-10-29T07:11:15Z; supersedes numerics_v08 (sha256 229ba0c596669dd120f6b2b9bfd171384f2f82a5b462b0cf2f5a7e96eef63d6f) and earlier versions.
- consulted (v09): theory_v03.md (the T1/T3 theory worker, 03:41:45Z; ACK 04:17Z); theory_v04.md (the T1/T3 theory worker; sha256 7638b0dae2e1cd03...; ACK in RUN_Published 2026-10-29T07:11:15Z. Best certified candidate: C1-N1-007 (G0 0.37669, (B-L2), distance 0.004769 in mode 7, forcing gap 3.6e6). Best design candidates (FLOAT, basis not yet
covered by the exact pipeline): C1-N1-016 (R0 = 25: G0 0.3089, kappa 0.7338, held-out (21, 522) 2.3e-4, (23, 2400) 6.5e-4) and C1-N1-017 (R0 = 50: G0 0.3209, kappa
0.7279, held-out (21, 522) 3.4e-4, (23, 2400) 6.4e-4); both leave a best held-out probe of about 1e-3 at (19, 1800) and push some mass into modes 33 to 47
(up to 1.6e-4). The continuation of 016 (C1-N1-018, 12 more steps) is running (core 54; step 6 at 07:10Z, objective 1.4745e7); its snapshot and diagnostics are left to
the next shift of this lane (an earlier work session ends about 08:32Z) and go into NUMERICS_FINAL.md. Requests: The N4 numerical auditor: structure, point gaps and the held-out probes (21, 522),
(23, 2400) and (19, 1800) on 016 and 017; the N3 numerics worker: feasibility of exact norms for the legqs candidates (N4-137 integrator); batch T: The coordinator 05:33Z item 3 (geometry
tolerating L^2 mass 1e-4 to 1e-3 at r 20 to 40) with the new FLOAT numbers above. Continuation plan for batch N: scales 25 and 50 together, blocks m = 16..23
(modes 33 to 47) added, 60+ steps, held-out sets fixed before each run (R-HOLDOUT), MID 16 for runs and MID 32 for every reported number.); the coordinator team notes through 2026-10-29T07:04 (05:26Z: 013 RULED OUT by the held-out
  (21, 522) probe T4-255; 05:33Z: matrix v46, feedback request on the mid-field floor, format notes); the N4 numerical auditor team notes / VERDICT_LEDGER.md through
  2026-10-29T03:00:41. (ledger to N4-251; N4-178, N4-175, N4-200, N4-204, N4-205, N4-207, N4-209 used); the N3 numerics worker team notes through 2026-10-29T07:05; the second model/weakprobe-asympt/answer.md.
  Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by ID; the new numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v03 (R6(b) Newton step, R6(c) held-out probes, R9 quotient basis). Candidate IDs new in v09: C1-N1-017-legqs50-quot013 (and C1-N1-018-legqs25-cont12 if its diagnostics are in before publication); v08 introduced 015 and 016. Normalization status of every the N1/N2 numerics worker snapshot: PRIMARY chart, c_l = 4076476460239181/2^51 and Theta_0 of state 131 EXACT, center
  relation EXACT, a_0 free (FLOAT value in each MANIFEST); coefficient file path: working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).

## 0. Summary of what is new
1. Scale comparison: G0 0.3209, kappa 0.7279; (21, 522) probe m 3.36e-04 (007/013/014: 1.12e-3); best N4-160 probe 19:1800 1.03e-03. Against 016 (R0 = 25): scale 50 is slightly better at r 28 to 40 ((23, 1200) 2.7e-4 vs 3.0e-4; (23, 2400) 6.4e-4 vs 6.5e-4) and slightly worse at r 19 ((21, 522) 3.4e-4 vs 2.3e-4); mode 19 at K = 1800 rises for both (1.03e-3 / 9.0e-4). G0 0.3206 vs 0.3084 (MID 16 run reports), objective 1.440e7 vs 1.487e7.
2. Continuation of 016 by 12 more steps (C1-N1-018): PENDING (run in progress at publication).
3. Held-out sweep extended to odd modes 33 to 47 (weak_tests3, IPM_NMAX = 47; never objective rows): for 013 the best m per mode is 7.4e-5 (n = 33) down to
   7.6e-6 (n = 47), so the r 20 to 40 mass of the d2-descended candidates sits in modes 19 to 31 and the sweep to n = 31 of v08 was sufficient; for 016 the best m per mode for n = 33 to 47 is 1.0e-04 (n = 33), 2.1e-05 (n = 35), 3.3e-05 (n = 37), 8.6e-05 (n = 39), 7.5e-05 (n = 41), 7.9e-05 (n = 43), 1.6e-04 (n = 45), 6.0e-05 (n = 47); best overall held-out probe of 016 over n <= 47: 19:1800 (9.02e-04).
4. End-state damped Galerkin steps (R-TANGENT, FLOAT, MID 24, lam 1e-6): 016 ||F||_2 0.309 -> 0.200 (||h0||_2 1.46e-2), 017 0.321 -> 0.217 (1.32e-2), against 007
   0.377 -> 0.338 (1.85e-2): the resolved bases have far more leverage on the L^2 residual (no span-floor claim, N4-211).
5. The v08 sections on 016, 015, the explicit SVD and the far-field validation are unchanged and not repeated; this version adds sections 1b (017) and 1c (018).

## 1. C1-N1-016-legqs25-quot013 (controlled test of mid-field resolution at modes 19 to 31; held-out probes)
Run (the coordinator 05:33Z item 3): the exact quotient basis of 013 (1922 generators) plus 252 multi-scale legqs functions at scale R0 = 25 (Q = 4 vanishing far-field moments,
12 radial functions per block) in the blocks j = 1, 2, 3, m = 9..15 (density sine modes 19 to 31), zero start; balanced objective of 007 plus 67 pairing rows
(27 first-mode probes and the N4-160 angular probes with n <= 17 only), weight 1e12, MID 16, 12 CPU steps (about 175 s each). The probes n = 19..31 at
K = (n-1)/2 + 512 (r 23 to 32) are HELD OUT (not rows of the objective): they decide whether the mid-field floor of 013/014 was a span limit.
Snapshot C1-N1-016-legqs25-quot013 (exact JSON sha256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42; 2174 generators; 421 exact rows; eleven EXACT-ZERO sectors). Last accepted step: it  12 obj 1.486502e+07 -> 1.482665e+07 ACC pred 1.652e+05 lam 1.4e-03 parts F 1.294e+07 G 2.265e+05 P 4.769e+04 K 1.616e+06 PAIR 6.891e+02 max|I_k| 1.
FLOAT (diag2, MID 32): G0 0.3089 (007 0.3767, 013 0.3722, 014 0.3726), G1 3.727, P2 218.1, rF 7.146, H 0.6178, sup|F| 0.1495,
theta 0.0114, kappa 0.7338 (margin +0.065), R_nec(2^-18) 1.264e-03; first-mode weak probes max over
k <= 4096: 1.500e-04 at k = 2048.
HELD-OUT probes at r 23 to 32 (FLOAT, weak_tests3 rule; 007, 013, 014 values for comparison):
| probe (n, K) | r_peak | m 007 | m 013 | m 014 | m C1-N1-016-legqs25-quot013 |
|---|---|---|---|---|---|
| (19, 521) | 19 | 1.50e-04 | 1.90e-04 | 1.60e-04 | 1.69e-04 |
| (21, 522) | 19 | 1.12e-03 | 1.12e-03 | 1.12e-03 | 2.33e-04 |
| (23, 523) | 19 | 7.62e-04 | 7.58e-04 | 7.58e-04 | 2.32e-04 |
| (25, 524) | 19 | 5.49e-04 | 5.28e-04 | 5.51e-04 | 1.70e-04 |
| (27, 525) | 19 | 3.23e-04 | 3.10e-04 | 3.17e-04 | 1.04e-04 |
| (29, 526) | 19 | 2.02e-04 | 2.00e-04 | 1.96e-04 | 3.77e-05 |
| (31, 527) | 19 | 1.22e-04 | 1.19e-04 | 1.23e-04 | 3.26e-05 |
| (23, 600) | 20 | 6.84e-04 | 6.81e-04 | 6.80e-04 | 2.17e-04 |
| (25, 600) | 20 | 5.20e-04 | 4.99e-04 | 5.22e-04 | 1.94e-04 |
| (23, 1200) | 28 | 7.74e-04 | 7.74e-04 | 7.78e-04 | 2.97e-04 |
| (25, 1200) | 28 | 4.47e-04 | 4.65e-04 | 4.44e-04 | 1.16e-04 |
| (23, 1800) | 35 | 1.59e-03 | 1.59e-03 | 1.60e-03 | 5.94e-04 |
| (25, 1800) | 35 | 1.07e-03 | 1.09e-03 | 1.07e-03 | 4.19e-04 |
| (23, 2400) | 40 | 1.80e-03 | 1.80e-03 | 1.81e-03 | 6.50e-04 |
| (25, 2400) | 40 | 1.27e-03 | 1.28e-03 | 1.27e-03 | 5.37e-04 |
| (29, 2400) | 40 | 4.97e-04 | 4.98e-04 | 5.01e-04 | 2.72e-04 |
Best m by mode (N4-160 family, FLOAT): n = 1: 1.7e-04; n = 3: 8.3e-05; n = 5: 5.1e-05; n = 7: 1.1e-04; n = 9: 7.6e-05; n = 11: 4.6e-05; n = 13: 1.2e-04; n = 15: 2.0e-04; n = 17: 5.1e-05; n = 19: 9.0e-04; n = 21: 2.3e-04; n = 23: 6.5e-04; n = 25: 5.4e-04; n = 27: 1.0e-04; n = 29: 2.7e-04; n = 31: 2.0e-04. Best probe 19:1800 (9.02e-04).

## 1b. C1-N1-017-legqs50-quot013 (scale comparison, R0 = 50)
Run: identical to 016 except the scale R0 = 50 of the 252 added legqs functions (blocks j = 1, 2, 3, m = 9..15), same start, same 67 rows, MID 16, 12 CPU steps:
a controlled comparison of the resolution scale.
Snapshot C1-N1-017-legqs50-quot013 (exact JSON sha256 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114; 2174 generators; 421 exact rows; eleven EXACT-ZERO sectors). Last accepted step: it  12 obj 1.442423e+07 -> 1.440123e+07 ACC pred 2.376e+04 lam 1.4e-03 parts F 1.257e+07 G 2.040e+05 P 4.033e+04 K 1.590e+06 PAIR 1.933e+02 max|I_k| 5.
FLOAT (diag2, MID 32): G0 0.3209 (007 0.3767, 013 0.3722, 014 0.3726), G1 3.538, P2 200.5, rF 7.049, H 0.6153, sup|F| 0.1565,
theta 0.0114, kappa 0.7279 (margin +0.071), R_nec(2^-18) 1.012e-03; first-mode weak probes max over
k <= 4096: 1.247e-04 at k = 2048.
HELD-OUT probes at r 23 to 40 (FLOAT; 007, 013, 014 baselines; 016 values in section 1):
| probe (n, K) | r_peak | m 007 | m 013 | m 014 | m C1-N1-017-legqs50-quot013 |
|---|---|---|---|---|---|
| (19, 521) | 19 | 1.50e-04 | 1.90e-04 | 1.60e-04 | 1.31e-04 |
| (21, 522) | 19 | 1.12e-03 | 1.12e-03 | 1.12e-03 | 3.36e-04 |
| (23, 523) | 19 | 7.62e-04 | 7.58e-04 | 7.58e-04 | 3.22e-04 |
| (25, 524) | 19 | 5.49e-04 | 5.28e-04 | 5.51e-04 | 2.43e-04 |
| (27, 525) | 19 | 3.23e-04 | 3.10e-04 | 3.17e-04 | 1.60e-04 |
| (29, 526) | 19 | 2.02e-04 | 2.00e-04 | 1.96e-04 | 8.95e-05 |
| (31, 527) | 19 | 1.22e-04 | 1.19e-04 | 1.23e-04 | 5.82e-05 |
| (23, 600) | 20 | 6.84e-04 | 6.81e-04 | 6.80e-04 | 3.01e-04 |
| (25, 600) | 20 | 5.20e-04 | 4.99e-04 | 5.22e-04 | 2.63e-04 |
| (23, 1200) | 28 | 7.74e-04 | 7.74e-04 | 7.78e-04 | 2.72e-04 |
| (25, 1200) | 28 | 4.47e-04 | 4.65e-04 | 4.44e-04 | 8.77e-05 |
| (23, 1800) | 35 | 1.59e-03 | 1.59e-03 | 1.60e-03 | 5.76e-04 |
| (25, 1800) | 35 | 1.07e-03 | 1.09e-03 | 1.07e-03 | 4.04e-04 |
| (23, 2400) | 40 | 1.80e-03 | 1.80e-03 | 1.81e-03 | 6.35e-04 |
| (25, 2400) | 40 | 1.27e-03 | 1.28e-03 | 1.27e-03 | 5.30e-04 |
| (29, 2400) | 40 | 4.97e-04 | 4.98e-04 | 5.01e-04 | 3.05e-04 |
Best m by mode (N4-160 family, FLOAT): n = 1: 1.4e-04; n = 3: 1.9e-04; n = 5: 7.9e-05; n = 7: 8.3e-05; n = 9: 6.4e-05; n = 11: 9.7e-05; n = 13: 5.6e-05; n = 15: 1.6e-04; n = 17: 7.3e-05; n = 19: 1.0e-03; n = 21: 3.4e-04; n = 23: 6.4e-04; n = 25: 5.3e-04; n = 27: 1.6e-04; n = 29: 3.1e-04; n = 31: 2.5e-04. Best probe 19:1800 (1.03e-03).

## 2. C1-N1-015-pairQ-quot013 (angular rows on the exact quotient basis)
Run: the exact quotient basis of 013 (1922 generators, no zero-potential directions) with the SAME 102 pairing rows as 014 (angular n >= 19 included), weight 1e12,
MID 16, 12 CPU steps (about 167 s each): the redundancy of the basis is removed and nothing else changes, so a difference from 014 would attribute the
immobility of the r 23 to 32 probes to conditioning.
Snapshot C1-N1-015-pairQ-quot013 (exact JSON sha256 d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae; 1922 generators; 421 exact rows; eleven EXACT-ZERO sectors). Last accepted step: it  12 obj 1.720964e+07 -> 1.720957e+07 ACC pred 1.849e+04 lam 4.6e-05 parts F 1.539e+07 G 1.922e+05 P 3.660e+04 K 1.586e+06 PAIR 7.640e+02 max|I_k| 1.
FLOAT (diag2, MID 32): G0 0.3723 (007 0.3767, 013 0.3722, 014 0.3726), G1 3.434, P2 191.0, rF 7.811, H 0.6312, sup|F| 0.1436,
theta 0.0114, kappa 0.7271 (margin +0.072), R_nec(2^-18) 1.015e-03; first-mode weak probes max over
k <= 4096: 1.270e-04 at k = 2048.
Probes at r 23 to 32 (IN the objective for 014 and 015; FLOAT):
| probe (n, K) | r_peak | m 007 | m 013 | m 014 | m C1-N1-015-pairQ-quot013 |
|---|---|---|---|---|---|
| (19, 521) | 19 | 1.50e-04 | 1.90e-04 | 1.60e-04 | 1.65e-04 |
| (21, 522) | 19 | 1.12e-03 | 1.12e-03 | 1.12e-03 | 1.14e-03 |
| (23, 523) | 19 | 7.62e-04 | 7.58e-04 | 7.58e-04 | 7.62e-04 |
| (25, 524) | 19 | 5.49e-04 | 5.28e-04 | 5.51e-04 | 5.43e-04 |
| (27, 525) | 19 | 3.23e-04 | 3.10e-04 | 3.17e-04 | 3.13e-04 |
| (29, 526) | 19 | 2.02e-04 | 2.00e-04 | 1.96e-04 | 2.02e-04 |
| (31, 527) | 19 | 1.22e-04 | 1.19e-04 | 1.23e-04 | 1.15e-04 |
| (23, 600) | 20 | 6.84e-04 | 6.81e-04 | 6.80e-04 | - |
| (25, 600) | 20 | 5.20e-04 | 4.99e-04 | 5.22e-04 | - |
| (23, 1200) | 28 | 7.74e-04 | 7.74e-04 | 7.78e-04 | - |
| (25, 1200) | 28 | 4.47e-04 | 4.65e-04 | 4.44e-04 | - |
| (23, 1800) | 35 | 1.59e-03 | 1.59e-03 | 1.60e-03 | - |
| (25, 1800) | 35 | 1.07e-03 | 1.09e-03 | 1.07e-03 | - |
| (23, 2400) | 40 | 1.80e-03 | 1.80e-03 | 1.81e-03 | - |
| (25, 2400) | 40 | 1.27e-03 | 1.28e-03 | 1.27e-03 | - |
| (29, 2400) | 40 | 4.97e-04 | 4.98e-04 | 5.01e-04 | - |
Best m by mode (N4-160 family, FLOAT): n = 1: 1.4e-04; n = 3: 9.8e-05; n = 5: 1.7e-05; n = 7: 7.8e-06; n = 9: 9.2e-06; n = 11: 1.2e-05; n = 13: 5.6e-06; n = 15: 9.6e-06; n = 17: 3.8e-05; n = 19: 1.7e-04; n = 21: 1.1e-03; n = 23: 7.6e-04; n = 25: 5.4e-04; n = 27: 3.1e-04; n = 29: 2.0e-04; n = 31: 1.1e-04. Best probe 21:522 (1.14e-03).

## 3. Explicit SVD on the exact quotient basis (optimization/gn_svd.py; candD2/007_quot_gn_svd.json)
Explicit weighted design matrix J Z on the admissible tangent of the exact quotient basis of 007 (343440 rows x 1496 columns; constraint rank 426;
balanced objective weights; MID 16 x 180), column-scaled, singular values by torch.linalg.svdvals (relative resolution about 1e-16): largest 10.666,
smallest 7.81e-13; counts below 1e-4 / 1e-6 / 1e-8 / 1e-10 / 1e-12 of the largest: 987 / 788 / 653 / 556 / 48 (of 1496).
Quantiles (scaled): 1 percent 5.56e-12, 10 percent 3.41e-11, median 2.52e-06, 90 percent 6.88e-01.
Gram metric (T4-229, theory_v03 R9(c)): the mesh L^2 Gram of the densities on the tangent has eigenvalues from -3.35e-04 to 1.30e+12, i.e. it is numerically
singular in binary64, so the generalized singular values could not be formed; this means that the densities of the 1922 exactly independent potentials are
nearly dependent as functions on the mesh (the smallest directions of the normal-equation spectrum are combinations of the radial Legendre functions within the
high-m blocks, m = 17 to 19 of branch 1; the cause is OPEN, N4-211 (c)). Reading: the exact quotient removes the 1060 exact zero potentials but the physical problem remains strongly
ill-conditioned (about 40 percent of the tangent has no effect at the 1e-8 level); the Levenberg-Marquardt damping governs a large part of each step, and the
plateaus of the balanced objective cannot be called stationary points from this evidence (supersedes numerics_v06 section 5 and v07 section 4 wording). No
inverse bound of L follows (R9(d)). For the continuation: per-block orthogonalized densities and fewer radial functions at high m.

## 4. Far-field model validation (bridge probes; candD2/d2w_j7_n4_E2bal_mid180_weaktests2_bridge.json, 007_far_weak.json)
Mesh pairings of 007 on 0.02 <= r <= 8356 (radial Gauss 32 x midpoint 180, far correction beyond 8356 omitted: relative size below 1e-4 for k <= 3.2e6) against the
exact-sector sums sum_e pi s_1(e) T_e(k) of far_weak.py (31 sectors to exponent -7):
| k | r_peak | mesh I_k (no far correction) | exact-sector sum | ratio | m_k (mesh) | 008 mesh I_k / m_k |
|---|---|---|---|---|---|---|
| 100000 | 204 | -6.004e-09 | 5.839e-09 | 1.028 | 1.63e-04 | -4.50e-07 / 1.22e-02 |
| 200000 | 289 | -2.638e-09 | - | - | 1.51e-04 | -1.25e-07 / 7.15e-03 |
| 500000 | 457 | -5.679e-10 | - | - | 8.63e-05 | -2.18e-08 / 3.31e-03 |
| 1000000 | 646 | -1.282e-10 | 1.279e-10 | 1.002 | 4.06e-05 | -5.63e-09 / 1.78e-03 |
| 2000000 | 914 | -1.569e-11 | - | - | 1.03e-05 | -1.43e-09 / 9.39e-04 |
| 3162278 | 1149 | +1.333e-12 | 1.531e-12 | 0.871 | 1.41e-06 | -5.73e-10 / 6.08e-04 |
Reading: at k = 1e6 (r about 650) the exact far-field expansion reproduces the full pairing to 0.2 percent, at k = 1e5 (r about 200) to 3 percent, at k = 3.2e6 the
mesh value is at its cancellation level (1e-12). The model was offered (numerics_v06 section 3) only where the sector series converges (r above about 300 to 600);
N4-209's comparison at K <= 1e4 (r <= 65) lies where the series diverges and the table entries were not estimates, so N4-209 and this validation are
consistent. Conclusions unchanged: the surviving sectors of 007 cancel to 97 to 99.7 percent in the sin theta pairing, 007 has no far-field floor of its first-mode
weak distance, and its maximum over all k is 1.73e-4 at k = 12288 (FLOAT). The 008 column shows the contrast for a candidate optimized without the rF term.

## 1c. C1-N1-018-legqs25-cont12 (continuation of 016)
PENDING (diagnostics not finished at publication; the run log candD2/quot013_legqs25_cont12_cpu_m16.log carries the step record).

## 5. Status and next steps
Published 2026-10-29T07:11:15Z. Best certified candidate: C1-N1-007 (G0 0.37669, (B-L2), distance 0.004769 in mode 7, forcing gap 3.6e6). Best design candidates (FLOAT, basis not yet
covered by the exact pipeline): C1-N1-016 (R0 = 25: G0 0.3089, kappa 0.7338, held-out (21, 522) 2.3e-4, (23, 2400) 6.5e-4) and C1-N1-017 (R0 = 50: G0 0.3209, kappa
0.7279, held-out (21, 522) 3.4e-4, (23, 2400) 6.4e-4); both leave a best held-out probe of about 1e-3 at (19, 1800) and push some mass into modes 33 to 47
(up to 1.6e-4). The continuation of 016 (C1-N1-018, 12 more steps) is running (core 54; step 6 at 07:10Z, objective 1.4745e7); its snapshot and diagnostics are left to
the next shift of this lane (an earlier work session ends about 08:32Z) and go into NUMERICS_FINAL.md. Requests: The N4 numerical auditor: structure, point gaps and the held-out probes (21, 522),
(23, 2400) and (19, 1800) on 016 and 017; the N3 numerics worker: feasibility of exact norms for the legqs candidates (N4-137 integrator); batch T: The coordinator 05:33Z item 3 (geometry
tolerating L^2 mass 1e-4 to 1e-3 at r 20 to 40) with the new FLOAT numbers above. Continuation plan for batch N: scales 25 and 50 together, blocks m = 16..23
(modes 33 to 47) added, 60+ steps, held-out sets fixed before each run (R-HOLDOUT), MID 16 for runs and MID 32 for every reported number.
