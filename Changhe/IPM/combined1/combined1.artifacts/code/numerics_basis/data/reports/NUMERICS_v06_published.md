# numerics_v06 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v06; UTC time: 2026-10-29T04:42:22Z; supersedes numerics_v05 (sha256 9e569e6419671b1e9665e7aad3f4f40526db18372f4af4863dee766d9bb9bf2d) and earlier versions (hashes in v05).
- consulted (v06): theory_v02.md (the T1/T3 theory worker, 2026-10-29T01:44Z); the coordinator team notes and closure_matrix through 2026-10-29T03:45Z; the N4 numerical auditor team notes and VERDICT_LEDGER.md through latest
  (N4-053, N4-091 weak probes at k = 0, 128, 512, 1024; N4-132; N4-139 to N4-142); the N3 numerics worker team notes through 2026-10-29T03:36Z (exact N_a(d2) and N_a(007));
  the second model referee the second model/weakprobe-asympt/answer.md (large-k asymptotics of the weak probe; its PROOF.md in the same directory). Batch N consultation: The N3 numerics worker and the N4 numerical auditor
  results are cited by ID; the new numbers below are the N1/N2 numerics worker's (FLOAT unless stated) and are offered to the N4 numerical auditor for certification.
- theory version followed: theory_v02. Norm IDs used: NORM-T-WEAK-v1 (k extended to 65536), NORM-T-WL2-v1, NORM-T-WLAP-v1, NORM-A2-E2 components, NORM-T-X3-v1,
  NORM-T-DYADIC-v1, NORM-T-PTNEC-v1. Candidate IDs: C1-N1-007..013 (new in v06: C1-N1-011-e2bal-legqs-from007, C1-N1-012-e2balk1e7-from009, C1-N1-013-pairU-from007).

## 0. Summary of what is new
1. Calibration of my FLOAT evaluators against exact values (section 1): weak pairing of d2 to 10 digits (N4-053), weak-probe bound of 007 at k = 128 to all
   printed digits (N4-091), N_a(d2) to 4-6 digits (the N3 numerics worker exact values). The FLOAT disagreement on N_a(007) (coordinator request 3 of 02:19Z) is resolved:
   my 343.49 at a = 0 is the all-mode value, the T1/T3 theory worker's 25.25 is the partial sum over modes 1 to 15 (the N4 numerical auditor's reading).
2. The weak distance (NORM-T-WEAK-v1) must be maximized over a much larger k range than k <= 8 (v05 section 5b underestimated it): the probe at k is
   localized near r = sqrt((2k+e+2)/(2-e)) (the second model, for F ~ r^e), and for 007 the maximum over k <= 4096 is 1.31e-4 at k = 2048 (r about 30), three times
   the certified value at k = 128. Extended tables for 007 to 012 in section 2; high-k probes (k to 65536) in section 2b.
3. Far-field floor of the weak distance from the EXACT sector table (section 3): for k large enough that the probe sits where the exact far-field expansion
   of F holds, I_k is an exact finite sum of Beta functions sigma_e T_e(k) over the surviving sectors, and m_k ~ K k^((e+1)/2) with K = |sigma| Gamma((1-e)/2)
   sqrt(2/(pi(1+2c+3c^2))) (the second model, confirmed formula; sigma = pi s_1 with s_1 the sin(theta) coefficient of the first surviving sector; 007: s_1 = 724.4,
   K = 458.6). Far-field weak probe of 007 from the exact sector table (31 sectors with a sin theta component, exponents -2.79 to -6.82; I_far = |sum_e pi s_1(e) T_e(k)| exact-formula; A_k exact; B_k, C_k scaled estimates; near-field bound G0 t_R^k sqrt(pi/12)):
| k | r_peak | I_far | leading-sector term | A_k | m_far (estimate) | near-field bound R=100 / 300 / 1000 |
|---|---|---|---|---|---|---|
| 3162 | 36 | 6.574e-04 | +2.541e-04 | 7.530e-04 | 4.009e-01 | 1.4e-01 / 1.9e-01 / 1.9e-01 |
| 10000 | 65 | 3.436e-06 | +2.867e-05 | 2.382e-04 | 7.554e-03 | 7.1e-02 / 1.7e-01 / 1.9e-01 |
| 31623 | 115 | 8.441e-09 | +3.235e-06 | 7.533e-05 | 6.580e-05 | 8.2e-03 / 1.4e-01 / 1.9e-01 |
| 100000 | 204 | 5.839e-09 | +3.650e-07 | 2.382e-05 | 1.588e-04 | 8.8e-06 / 6.3e-02 / 1.7e-01 |
| 316228 | 363 | 1.290e-09 | +4.118e-08 | 7.534e-06 | 1.206e-04 | 3.6e-15 / 5.7e-03 / 1.4e-01 |
| 1000000 | 646 | 1.279e-10 | +4.646e-09 | 2.382e-06 | 4.055e-05 | 7.2e-45 / 2.9e-06 / 7.1e-02 |
| 3162278 | 1149 | 1.531e-12 | +5.242e-10 | 7.534e-07 | 1.625e-06 | 9.0e-139 / 1.1e-16 / 8.2e-03 |
| 10000000 | 2043 | 3.402e-12 | +5.914e-11 | 2.382e-07 | 1.196e-05 | 0.0e+00 / 1.1e-49 / 8.8e-06 |
| 31622777 | 3634 | 8.598e-13 | +6.672e-12 | 7.534e-08 | 9.926e-06 | 0.0e+00 / 4.9e-154 / 3.6e-15 |
| 100000000 | 6461 | 1.572e-13 | +7.528e-13 | 2.382e-08 | 5.915e-06 | 0.0e+00 / 0.0e+00 / 7.2e-45 |
| 316227766 | 11490 | 2.472e-14 | +8.493e-14 | 7.534e-09 | 3.012e-06 | 0.0e+00 / 0.0e+00 / 8.9e-139 |
| 1000000000 | 20433 | 3.553e-15 | +9.581e-15 | 2.382e-09 | 1.395e-06 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
| 3162277660 | 36335 | 4.817e-16 | +1.081e-15 | 7.534e-10 | 6.070e-07 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
| 10000000000 | 64614 | 6.268e-17 | +1.220e-16 | 2.382e-10 | 2.527e-07 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
Reading. (i) The sector amplitudes grow by about a factor 10 per unit of exponent, so the exact far-field expansion of the 007 residual converges only
beyond r of order 300 to 600 (terms at r = 100 increase; at r = 650 they decrease by 0.2 to 0.5 per step). (ii) For k >= 1e6 (r_peak >= 650) the near-field
bound with R = 300 is below 3e-6 and the exact-sector pairing is 1.3e-10 (k = 1e6) to 1.5e-12 (k = 3.2e6): the 31 sectors cancel to 97 to 99.7 percent in
the sin theta pairing (the leading (3,1) term alone is 4.6e-9 at k = 1e6), a consequence of minimizing ||rF||_2 on the mesh out to r = 1e4. (iii) The
resulting far-field m is 4e-5 to 2e-6 (ESTIMATE: B_k and C_k scaled from the mesh values at k = 4096 by (k/4096)^(gamma/2 - 3/2), the second model's O-bound), so 007
has no far-field floor of its fixed-c weak distance; the asymptotic law m_k ~ K k^((e+1)/2), K = 458.6 (from the exact (3,1) sine coefficient
s_1 = 724.4 and e = -2.7904), applies only where the leading sector dominates, far beyond k = 1e7. (iv) Candidates without the rF term (008) do not cancel:
their first-mode distance keeps rising to k of order 6000 (0.047) and decays only slowly beyond (0.0165 at k = 65536)._SUMMARY
4. The fixed-c weak distance at the tested k is a soft constraint of the objective in the near and mid field: one Gauss-Newton step with 27 penalty rows
   (k <= 4096) drives max_k |I_k| from 1.55e-4 to 4.5e-7 at no visible cost; but the rows with k >= about 1000 (r >= 25) have a tiny Jacobian in the 007
   basis (per-k weights and hard constraints both explode), so m_k at those k does not improve: the maximum of m_k over k <= 4096 went from 1.31e-04 (007) to 1.33e-04 (013), with G0 0.3722 and kappa 0.7270 (section 4, snapshot C1-N1-013).
5. Conditioning of the constrained Gauss-Newton problem at 007 (section 5): 1022 of 2556 reduced directions are exactly redundant (d2's blocks contain
   both t^h and P_n(2t-1) functions), 200 more are below 1e-4 of the largest singular value; the reduced gradient is 8e-4 relative: 007 is a plateau of
   its objective, and the redundancy is a basis artifact, not a near-kernel of the linearization (prompt section 12 item 5).
6. Controlled comparisons 011 (legqs functions added to 007: no gain in 20 CPU steps) and 012 (kappa 1e7 on top of the balanced objective from 009: worse
   than 009): section 6.

## 1. Calibrations (FLOAT evaluators against exact values)
| quantity | my FLOAT | exact / certified | source |
|---|---|---|---|
| weak pairing k = 0 of d2 | -0.02880208111 | -0.0288020811 | N4-053 |
| weak-probe bound m_128 of 007 | 4.3987e-5 | 4.3987003470e-5 | N4-091 |
| N_a(d2), a = 0 / 1 / 5/4 / 3/2 | 1161.625 / 22.6837 / 10.2218 / 5.25474 | 1161.6596 / 22.68370 / 10.22182 / 5.25474 | The N3 numerics worker wlap_norms.py (02:28Z) |
| A_0 (weak probe denominator) | 1.6595 | 1.65953 (exact formula pi/12 (1+2c+3c^2-6c^2/5)) | the second model |
Radial-rule accuracy: the reduced optimization rule (8 Gauss points per unit log-panel) gives the k = 0 pairing of 007 as -2.28e-4 against +1.551e-4
(32 points); 16 points give +1.5566e-4 and 24 points +1.55098e-4 (numerics/optimization/logs/test_ik_mid.out). All reported FLOAT values use 32 points.

## 2. Extended weak distances (NORM-T-WEAK-v1, a = 0; FLOAT; k in {0..8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096})
| candidate | m_k k=0 | m_k k=8 | m_k k=64 | m_k k=128 | m_k k=512 | m_k k=1024 | m_k k=2048 | m_k k=4096 | m_k k=8192 | m_k k=16384 | m_k k=32768 | m_k k=65536 | max over all computed k (at k) | pairing k=0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1-N1-007-d2w-j7-e2bal | 1.62e-05 | 3.79e-05 | 9.74e-05 | 4.40e-05 | 2.91e-05 | 2.39e-05 | 1.31e-04 | 8.67e-06 | 1.71e-04 | 1.35e-04 | 1.68e-05 | 1.35e-04 | 1.733e-04 (k = 12288; k range to 65536) | +1.551e-04 |
| C1-N1-008-d2w-j7-x3bal | 5.12e-05 | 4.70e-05 | 2.65e-04 | 5.52e-04 | 4.03e-03 | 1.75e-02 | 3.63e-02 | 4.70e-02 | 4.54e-02 | 3.64e-02 | 2.56e-02 | 1.65e-02 | 4.735e-02 (k = 6144; k range to 65536) | +4.906e-04 |
| C1-N1-009-d2w-j7-x3balk | 4.93e-03 | 5.26e-03 | 1.80e-04 | 2.03e-03 | 1.02e-03 | 2.19e-03 | 4.01e-03 | 4.15e-03 | 3.34e-03 | 2.24e-03 | 1.26e-03 | 6.00e-04 | 6.032e-03 (k = 3; k range to 65536) | +4.721e-02 |
| C1-N1-010-d2w-j7-x3bal-legqs | 1.83e-03 | 1.93e-03 | 6.20e-04 | 1.08e-03 | 1.49e-03 | 1.77e-03 | 2.23e-03 | 2.91e-03 | - | - | - | - | 2.908e-03 (k = 4096; k range to 4096) | +1.754e-02 |
| C1-N1-011-e2bal-legqs-from007 | 2.36e-05 | 4.76e-04 | 2.57e-04 | 1.09e-04 | 7.28e-05 | 1.33e-04 | 1.77e-04 | 1.86e-04 | - | - | - | - | 5.120e-04 (k = 12; k range to 4096) | +2.259e-04 |
| C1-N1-012-e2balk1e7-from009 | 8.01e-03 | 1.50e-02 | 5.07e-03 | 3.60e-04 | 4.81e-03 | 1.87e-03 | 1.02e-03 | 2.28e-03 | - | - | - | - | 1.501e-02 (k = 8; k range to 4096) | +7.670e-02 |

Reading: the maximum over k is attained at k of order 1e4 (r of order 50 to 100) for 007 and 008 and at small k for 009, 010, 011, 012 (large
near-field pairings); 007's maximum 1.733e-4 is 3.9 times its certified k = 128 value (N4-091) and 46 times the largest scalar budget (3.793e-6), but below the
certified first-mode optimized probe 3.1474e-4 (T4-182) and far below the mode-7 probe 0.004769 (T4-185), which remains the binding necessary distance.

Full k profile of C1-N1-007 (FLOAT; I_k signed mesh value plus far correction, D_k, m_k):
| k | r_peak (dr density, e = -2.79) | I_k | D_k | m_k |
|---|---|---|---|---|
| 0 | 0.0 | +1.551e-04 | 9.582e+00 | 1.619e-05 |
| 1 | 0.5 | +9.638e-05 | 5.300e+00 | 1.818e-05 |
| 2 | 0.8 | +7.412e-05 | 3.636e+00 | 2.038e-05 |
| 3 | 1.0 | +6.358e-05 | 2.748e+00 | 2.313e-05 |
| 4 | 1.2 | +5.749e-05 | 2.198e+00 | 2.616e-05 |
| 5 | 1.4 | +5.333e-05 | 1.824e+00 | 2.924e-05 |
| 6 | 1.5 | +5.014e-05 | 1.554e+00 | 3.226e-05 |
| 7 | 1.7 | +4.751e-05 | 1.351e+00 | 3.516e-05 |
| 8 | 1.8 | +4.524e-05 | 1.193e+00 | 3.793e-05 |
| 12 | 2.2 | +3.829e-05 | 8.029e-01 | 4.769e-05 |
| 16 | 2.6 | +3.347e-05 | 5.988e-01 | 5.590e-05 |
| 24 | 3.1 | +2.732e-05 | 3.906e-01 | 6.993e-05 |
| 32 | 3.6 | +2.344e-05 | 2.864e-01 | 8.183e-05 |
| 48 | 4.5 | +1.775e-05 | 1.835e-01 | 9.674e-05 |
| 64 | 5.2 | +1.298e-05 | 1.333e-01 | 9.741e-05 |
| 96 | 6.3 | +6.220e-06 | 8.462e-02 | 7.350e-05 |
| 128 | 7.3 | +2.691e-06 | 6.119e-02 | 4.399e-05 |
| 192 | 8.9 | +6.351e-08 | 3.869e-02 | 1.642e-06 |
| 256 | 10.3 | -4.389e-07 | 2.793e-02 | 1.571e-05 |
| 384 | 12.7 | +1.654e-08 | 1.764e-02 | 9.374e-07 |
| 512 | 14.6 | +3.709e-07 | 1.273e-02 | 2.913e-05 |
| 768 | 17.9 | +2.114e-07 | 8.050e-03 | 2.626e-05 |
| 1024 | 20.7 | -1.392e-07 | 5.817e-03 | 2.392e-05 |
| 1536 | 25.3 | -4.035e-07 | 3.684e-03 | 1.095e-04 |
| 2048 | 29.2 | -3.483e-07 | 2.666e-03 | 1.306e-04 |
| 3072 | 35.8 | -1.243e-07 | 1.693e-03 | 7.345e-05 |
| 4096 | 41.4 | +1.064e-08 | 1.227e-03 | 8.671e-06 |
| 6144 | 50.6 | +9.588e-08 | 7.814e-04 | 1.227e-04 |
| 8192 | 58.5 | +9.699e-08 | 5.679e-04 | 1.708e-04 |
| 12288 | 71.6 | +6.284e-08 | 3.627e-04 | 1.733e-04 |
| 16384 | 82.7 | +3.561e-08 | 2.642e-04 | 1.348e-04 |
| 24576 | 101.3 | +8.300e-09 | 1.693e-04 | 4.903e-05 |
| 32768 | 117.0 | -2.078e-09 | 1.236e-04 | 1.681e-05 |
| 49152 | 143.3 | -7.605e-09 | 7.946e-05 | 9.570e-05 |
| 65536 | 165.4 | -7.826e-09 | 5.815e-05 | 1.346e-04 |

## 2b. High-k probes (k = 6144 .. 65536)
Included in the table above (columns k = 8192 to 65536; files candD2/<tag>_weaktests2_highk.json). The mesh (0.02 <= r <= 8356) resolves these probes
(r_peak <= 185); a bridge list k = 1e5 to 1e7 (r_peak 200 to 2600) for 007 is running (chainM2) at publication; values in v07.

## 3. Far-field weak probe from the exact sector table (007)
Far-field weak probe of 007 from the exact sector table (31 sectors with a sin theta component, exponents -2.79 to -6.82; I_far = |sum_e pi s_1(e) T_e(k)| exact-formula; A_k exact; B_k, C_k scaled estimates; near-field bound G0 t_R^k sqrt(pi/12)):
| k | r_peak | I_far | leading-sector term | A_k | m_far (estimate) | near-field bound R=100 / 300 / 1000 |
|---|---|---|---|---|---|---|
| 3162 | 36 | 6.574e-04 | +2.541e-04 | 7.530e-04 | 4.009e-01 | 1.4e-01 / 1.9e-01 / 1.9e-01 |
| 10000 | 65 | 3.436e-06 | +2.867e-05 | 2.382e-04 | 7.554e-03 | 7.1e-02 / 1.7e-01 / 1.9e-01 |
| 31623 | 115 | 8.441e-09 | +3.235e-06 | 7.533e-05 | 6.580e-05 | 8.2e-03 / 1.4e-01 / 1.9e-01 |
| 100000 | 204 | 5.839e-09 | +3.650e-07 | 2.382e-05 | 1.588e-04 | 8.8e-06 / 6.3e-02 / 1.7e-01 |
| 316228 | 363 | 1.290e-09 | +4.118e-08 | 7.534e-06 | 1.206e-04 | 3.6e-15 / 5.7e-03 / 1.4e-01 |
| 1000000 | 646 | 1.279e-10 | +4.646e-09 | 2.382e-06 | 4.055e-05 | 7.2e-45 / 2.9e-06 / 7.1e-02 |
| 3162278 | 1149 | 1.531e-12 | +5.242e-10 | 7.534e-07 | 1.625e-06 | 9.0e-139 / 1.1e-16 / 8.2e-03 |
| 10000000 | 2043 | 3.402e-12 | +5.914e-11 | 2.382e-07 | 1.196e-05 | 0.0e+00 / 1.1e-49 / 8.8e-06 |
| 31622777 | 3634 | 8.598e-13 | +6.672e-12 | 7.534e-08 | 9.926e-06 | 0.0e+00 / 4.9e-154 / 3.6e-15 |
| 100000000 | 6461 | 1.572e-13 | +7.528e-13 | 2.382e-08 | 5.915e-06 | 0.0e+00 / 0.0e+00 / 7.2e-45 |
| 316227766 | 11490 | 2.472e-14 | +8.493e-14 | 7.534e-09 | 3.012e-06 | 0.0e+00 / 0.0e+00 / 8.9e-139 |
| 1000000000 | 20433 | 3.553e-15 | +9.581e-15 | 2.382e-09 | 1.395e-06 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
| 3162277660 | 36335 | 4.817e-16 | +1.081e-15 | 7.534e-10 | 6.070e-07 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
| 10000000000 | 64614 | 6.268e-17 | +1.220e-16 | 2.382e-10 | 2.527e-07 | 0.0e+00 / 0.0e+00 / 0.0e+00 |
Reading. (i) The sector amplitudes grow by about a factor 10 per unit of exponent, so the exact far-field expansion of the 007 residual converges only
beyond r of order 300 to 600 (terms at r = 100 increase; at r = 650 they decrease by 0.2 to 0.5 per step). (ii) For k >= 1e6 (r_peak >= 650) the near-field
bound with R = 300 is below 3e-6 and the exact-sector pairing is 1.3e-10 (k = 1e6) to 1.5e-12 (k = 3.2e6): the 31 sectors cancel to 97 to 99.7 percent in
the sin theta pairing (the leading (3,1) term alone is 4.6e-9 at k = 1e6), a consequence of minimizing ||rF||_2 on the mesh out to r = 1e4. (iii) The
resulting far-field m is 4e-5 to 2e-6 (ESTIMATE: B_k and C_k scaled from the mesh values at k = 4096 by (k/4096)^(gamma/2 - 3/2), the second model's O-bound), so 007
has no far-field floor of its fixed-c weak distance; the asymptotic law m_k ~ K k^((e+1)/2), K = 458.6 (from the exact (3,1) sine coefficient
s_1 = 724.4 and e = -2.7904), applies only where the leading sector dominates, far beyond k = 1e7. (iv) Candidates without the rF term (008) do not cancel:
their first-mode distance keeps rising to k of order 6000 (0.047) and decays only slowly beyond (0.0165 at k = 65536).

## 4. Pairing penalty rows (ipm_opt3.Problem3) and snapshot C1-N1-013
Run: run_pair.py from the 007 coefficients, balanced E_2 objective of 007 (wlog 2^18*100, wkap 3e6) plus 27 rows sqrt(1e15) I_k, k in {0..8, 12, ..., 4096}
(first-mode probes phi_k = y t^k u0^2; uniform weight; MID 16 radial rule, midpoint 180), 12 Gauss-Newton steps on one CPU core (about 285 s per step).
Last step line: it  12 obj 1.720945e+07 -> 1.720925e+07 ACC pred 2.717e+03 lam 1.4e-03 parts F 1.539e+07 G 1.930e+05 P 3.667e+04 K 1.586e+06 PAIR 7.094e+02 max|I_k| 4.580e-07 I.
Snapshot C1-N1-013-pairU-from007 (exact JSON sha256 c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940; same basis and 421 exact rows as 007; eleven EXACT-ZERO sectors).
FLOAT (diag2, MID 32): G0 0.3722 (007 0.3767), G1 3.441 (3.439), P2 191.2 (190.8), rF 7.810 (7.83), H 0.6313 (0.636), sup|F| 0.1437 (0.138),
theta 0.0114, kappa 0.7270 (margin +0.072), X3 516.6, E2 605.3, R_nec(2^-18) 1.022e-03.
First-mode weak probes at MID 32 (the optimization rule MID 16 is not used for any reported value; N4-150):
| k | I_k (007) | I_k (013) | m_k (007) | m_k (013) |
|---|---|---|---|---|
| 0 | +1.551e-04 | -5.688e-07 | 1.619e-05 | 5.936e-08 |
| 1 | +9.638e-05 | -4.049e-07 | 1.818e-05 | 7.639e-08 |
| 2 | +7.412e-05 | -3.119e-07 | 2.038e-05 | 8.577e-08 |
| 3 | +6.358e-05 | -2.175e-07 | 2.313e-05 | 7.913e-08 |
| 4 | +5.749e-05 | -1.443e-07 | 2.616e-05 | 6.567e-08 |
| 5 | +5.333e-05 | -9.478e-08 | 2.924e-05 | 5.196e-08 |
| 6 | +5.014e-05 | -6.318e-08 | 3.226e-05 | 4.064e-08 |
| 7 | +4.751e-05 | -4.265e-08 | 3.516e-05 | 3.156e-08 |
| 8 | +4.524e-05 | -2.853e-08 | 3.793e-05 | 2.392e-08 |
| 12 | +3.829e-05 | -4.091e-09 | 4.769e-05 | 5.096e-09 |
| 16 | +3.347e-05 | -4.491e-09 | 5.590e-05 | 7.500e-09 |
| 24 | +2.732e-05 | +3.772e-09 | 6.993e-05 | 9.657e-09 |
| 32 | +2.344e-05 | +1.961e-08 | 8.183e-05 | 6.848e-08 |
| 48 | +1.775e-05 | -1.261e-08 | 9.674e-05 | 6.872e-08 |
| 64 | +1.298e-05 | -4.137e-08 | 9.741e-05 | 3.104e-07 |
| 96 | +6.220e-06 | +4.932e-08 | 7.350e-05 | 5.829e-07 |
| 128 | +2.691e-06 | +1.003e-07 | 4.399e-05 | 1.639e-06 |
| 192 | +6.351e-08 | -1.328e-07 | 1.642e-06 | 3.434e-06 |
| 256 | -4.389e-07 | -2.169e-07 | 1.571e-05 | 7.765e-06 |
| 384 | +1.654e-08 | +1.980e-07 | 9.374e-07 | 1.122e-05 |
| 512 | +3.709e-07 | +4.580e-07 | 2.913e-05 | 3.596e-05 |
| 768 | +2.114e-07 | +2.253e-07 | 2.626e-05 | 2.799e-05 |
| 1024 | -1.392e-07 | -1.422e-07 | 2.392e-05 | 2.445e-05 |
| 1536 | -4.035e-07 | -4.103e-07 | 1.095e-04 | 1.114e-04 |
| 2048 | -3.483e-07 | -3.535e-07 | 1.306e-04 | 1.326e-04 |
| 3072 | -1.243e-07 | -1.271e-07 | 7.345e-05 | 7.511e-05 |
| 4096 | +1.064e-08 | +8.991e-09 | 8.671e-06 | 7.325e-06 |
Maximum over the 27 k values: 007 1.306e-04 (k = 2048) -> 013 1.326e-04 (k = 2048).
Reading: the penalty rows reduce the first-mode pairings at the k where the basis has leverage (k <= about 1000, r <= 25) by two to three orders of magnitude at
essentially no cost in the other components (the objective parts F, G, P, K changed by less than 1 percent), while the rows with k >= 1536 (r >= 28) barely move:
their Jacobian in this basis is tiny (the same unreachability that made the per-k-weighted and hard-constraint variants explode). So NC-T-DIST with first-mode
probes at small k is a soft constraint of the objective; the mid-field probes (k of order 1e4, r of order 50 to 100) and the angular mode-7 probe (T4-185) are not.

Held-out angular probes (weak_tests3.py, N4-160 family, FLOAT): best m by mode for 007 -> 013: n = 1: 1.47e-04 -> 1.49e-04; n = 3: 7.19e-04 -> 1.61e-04; n = 5: 8.67e-04 -> 4.86e-05; n = 7: 2.87e-03 -> 7.22e-05; n = 9: 1.91e-03 -> 2.68e-05; n = 11: 2.01e-04 -> 1.22e-05; n = 15: 3.04e-05 -> 1.91e-05; n = 21: 1.12e-03 -> 1.12e-03; n = 31: 1.22e-04 -> 1.19e-04.
Mode-7 pairings (n = 7, K = 3 + K0): K = 3: I -1.766e-03 -> -1.499e-04, m 6.02e-04 -> 5.11e-05; K = 11: I -1.301e-03 -> -6.416e-05, m 1.46e-03 -> 7.22e-05; K = 35: I -6.558e-04 -> -1.423e-05, m 2.54e-03 -> 5.50e-05; K = 131: I -1.690e-04 -> -3.846e-07, m 2.87e-03 -> 6.52e-06; K = 515: I -1.630e-05 -> -2.720e-07, m 1.30e-03 -> 2.17e-05. Best probe 013: 21:522 (m = 1.124e-03); 007: 7:131 (2.866e-03). (Calibration: my FLOAT value for 007 at the N4-160 best probe (7, 131) is 2.866e-3 against N4-160's certified 2.8652581e-3; the stronger certified value 0.004769 (T4-185) uses an optimized radial polynomial, not a single t^K probe, so the 013 numbers above are FLOAT held-out comparisons under one rule, to be certified by the N4 numerical auditor with the frozen T4-182/T4-185 vectors.)
Reading: the first-mode penalty rows also reduced the HELD-OUT angular pairings of modes 3 to 11 at the reachable radii (K <= 131, r <= 10) by one to two orders of magnitude (mode 7 at K = 131: m 2.87e-3 -> 6.5e-6), while the probes at K about 520 (r 23 to 32) of modes 19 to 31 are unchanged (best remaining 1.12e-3 at n = 21): the remaining FLOAT distance of 013 is a mid-field quantity at r about 25 to 30, consistent with the first-mode profile (k = 2048, r about 30) and with the reachability radius of the basis.
The run with 75 additional angular probes (N4-160 family, n = 3..31) is C1-N1-014 (in progress at publication; see section 7).

## 5. Conditioning / near-kernel diagnostic at 007 (optimization/gn_spectrum.py, MID 16, balanced objective)
Reduced dimension 2556 (2982 generators, 426 independent constraint rows: 421 exact rows plus 5 linearized Taylor rows). Singular values of the
column-scaled reduced Jacobian: 1022 are zero to rounding (exact redundancy: the d2 generator list has both 'mono' t^h and 'leg' P_n(2t-1) radial
functions in the same (j, m) blocks; the null directions are combinations of these), 200 more below 1e-4 of the largest (15.4); quantiles of the
scaled spectrum: median 2.7e-3, 75 percent 5.9e-2, 90 percent 0.29, 99 percent 4.2. Reduced gradient norm relative to sqrt(phi) times the largest
singular value: 8.0e-4 (near-stationary). Reading: Gauss-Newton with Levenberg-Marquardt damping handles the redundancy (min-norm steps), the
plateaus of the balanced objective are genuine (near-stationary points, not conditioning stalls), and the prompt's question (section 12) whether an
apparent near-kernel is an obstruction, a normalization mode or a basis artifact is answered for this basis: artifact (file candD2/007_gn_spectrum.json).

## 6. Controlled comparisons 011 and 012 (FLOAT, MID 32)
| candidate | start / objective | G0 | G1 | P2 | rF | H | sup|F| | theta / kappa / (B-L2) | pairing k=0 | extended weak distance |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-N1-007 (reference) | 005 / balanced E_2, 60 GPU steps | 0.3767 | 3.439 | 190.8 | 7.83 | 0.636 | 0.138 | 0.0114 / 0.7269 / holds | 1.55e-4 | 1.31e-4 (k = 2048) |
| C1-N1-011-e2bal-legqs-from007 | 007 + 960 legqs (R0 10, 100) / same objective, 20 CPU steps | 0.3745 | 3.528 | 196.0 | 7.78 | 0.612 | 0.153 | 0.0114 / 0.7277 / holds | 2.26e-4 | 5.1e-4 (k = 12) |
| C1-N1-012-e2balk1e7-from009 | 009 / balanced E_2 + kappa 1e7, 30 CPU steps | 1.556 | 12.94 | 908 | 24.7 | 2.84 | 0.773 | 0.0116 / 0.878 / fails | 0.0767 | 1.5e-2 (k = 8) |
Reading: 011 shows that 960 multi-scale functions do not help at 20 CPU steps from a converged 007 (the reduced-rule report of G0 0.3635 was a quadrature
artifact: 0.3745 at MID 32); 012 shows that a strong kappa penalty added to the balanced objective from a different objective's optimum does not
converge in 30 CPU steps (objective 1.83e8 -> 1.69e8, rejections dominate). Neither is a certification target.

## 7. Status and next steps
Published 2026-10-29T04:42:22Z. Best candidate unchanged: C1-N1-007 (certified G0 0.3767, (B-L2), distance 0.004769 in mode 7). Running: C1-N1-014 run (102 pairing
rows including the 75 angular probes of N4-160, uniform weight 1e12, MID 16, 12 steps, core 52; the 1e15 version was killed after one step because the
angular pairings of 007, of order 1e-4 to 1e-3 each, dominated the objective by 1000x and the Gauss-Newton step raised the F part 20x); high-k and bridge
probes for the remaining candidates (core 53). Next: snapshot 014 with weak_tests2/3 and diag2 (about 05:40Z) and numerics_v07; then NUMERICS_FINAL.md and
artifacts by 08:30Z (H12). Corrections carried from the coordinator 02:48Z: the graded-box exclusion of 007 comes from the N4-102 point gap (N4-145), the 14 percent
difference in v05 section 5b compared k = 8 with k = 128 (N4-146), and every FLOAT value of this lane is CPU float64 (the 'float64 GPU' header of v05 section
5 applies to runs before 00:58Z only). The conditioning statement of section 5 is to be read on the 1922 independent generators (N4-158): the 1022 zero
singular values are exactly the redundant directions and the remaining spectrum is that of the independent problem.
