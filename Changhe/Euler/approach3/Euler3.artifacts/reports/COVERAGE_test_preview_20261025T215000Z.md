# Coverage snapshot: test_preview (boundary 2026-10-25T21:50:00Z; generated 2026-10-25T21:57:36Z; ledger status/ledger.jsonl)

Counts of ledger RECORDS and trajectories between T0 2026-10-24T17:09:12Z and 2026-10-25T21:50:00Z (28.68 h of wall clock), not of distinct random starts or accepted states; rows with ts after the boundary are not counted (next stage); ranked rows and bins are counted at the boundary only. Primary route only.

## Jobs (supervisor queue)
- Launched: 211 distinct jobs (297 process launches incl. 44 retries; 59 resumes from checkpoint; 42 worker error records).
- Completed by the boundary: 200; failed: 7 (c2x2_L10_cl0.47_om+1.0_fixed, c2x2_L6_cl0.45_om+1.0_free, c2x2_L6_cl0.47_om+1.0_free, c2x2_L8_cl0.47_om+1.0_fixed, d6odd_L6_cl0.45_om+0.3_fixed_m1e-2, s10smoke_L6_cl0.45_om+1.0_fixed_both1, smoke_kh_L4_cl0.45_om+1.0_fixed_v124); cancelled: 1 (nest10smoke_L10_cl0.45_om+1.0_fixed); running at the boundary (their rows count as the next stage): 6 (c2x2_L10_cl0.47_om+1.0_free, nest10_L10_cl0.45_om+0.3_fixed_p0, nest10_L10_cl0.45_om+1.0_fixed_p0, nest8nk8_L8_cl0.45_om+1.0_fixed, s10_L6_cl0.45_om+1.0_fixed_both1, s1c_vortnlw_L6_cl0.41_om+0.3).
- Disposable jobs (smokes, LM-only validations, resume tests; never ranked): 13; free-parameter jobs: 11.
- Jobs by tag (launched / completed): c2x2 9 / 5, c2x2b 2 / 2, c2x2c 6 / 6, c2x2split 1 / 1, d6odd 2 / 2, d6scan 6 / 6, d6split 1 / 1, d6t 2 / 2, d6tZ 1 / 1, d6u 3 / 3, d6v 2 / 2, d6w 4 / 4, d6w2 2 / 2, d6w3 3 / 3, d6w4 1 / 1, nest10 2 / 0, nest10smoke 3 / 3, nest2 3 / 3, nest4 9 / 9, nest6 5 / 5, nest8 6 / 6, nest8nk8 1 / 0, nest8nk8smoke 1 / 1, s10 1 / 0, s10smoke 2 / 1, s11smoke 1 / 1, s12smoke 1 / 1, s1a 35 / 35, s1b_momnlw 25 / 25, s1c_vortnlw 24 / 23, s1j_R05 9 / 9, s1k_sigmaZ 9 / 9, s1nk 4 / 4, s1r1 1 / 1, s7a 4 / 4, s7b 2 / 2, s7c 3 / 3, s8 3 / 3, s8p 2 / 2, s9 1 / 1, s9b 4 / 4, s9dsmoke 1 / 1, smoke_kh 2 / 1, val8dense 1 / 1, val8split 1 / 1.

## Recorded starts (start_result rows)
- Total 885; by status: {'ftol': 346, 'max_iter': 483, 'stalled': 47, 'time_limit': 9}.
- By degree L: {'2': 187, '4': 37, '6': 642, '8': 15, '10': 4}; by radial Nk: {'4': 7, '8': 181, '10': 13, '12': 23, '16': 638, '20': 15, '24': 6, '32': 2}.
- Symmetry classes (azimuthal parity): {'even': 881, 'all': 4}; by L and parity: {'L10 even': 4, 'L2 even': 187, 'L4 all': 2, 'L4 even': 35, 'L6 all': 2, 'L6 even': 640, 'L8 even': 15}.
- Formulations: {'vort': 357, 'mom': 527, 'both': 1}; nonlinear denominators: {'None': 528, 'all5': 257, 'all5far': 91, 'nl': 6, 'split': 3}; parameter mode: {'fixed (c_l, omega)': 876, 'free (c_l, omega)': 9}; solver versions: {'v1': 328, 'v2-untagged': 67, 'v3-2026-10-24T19:12Z': 95, 'v4-2026-10-24T20:35Z': 12, 'v5-2026-10-24T21:05Z': 383}.
- Seed families: {'random': 237, 'nonaxi': 134, 'tail': 127, 'poloidal': 124, 'toroidal': 114, 'init_from': 99, 'affine_core': 50}.
- Start wall time (ledger 'seconds'): 94.6 process-hours; by lineage: s1 584 starts 30.9 h, nest 203 starts 27.4 h, d6 27 starts 22.2 h, c2x2c 6 starts 5.5 h, s8 5 starts 3.1 h, s9 6 starts 1.8 h, s7 9 starts 1.2 h, c2x2 5 starts 1.0 h, pilot 10 starts 0.8 h, c2x2b 2 starts 0.5 h, resume 4 starts 0.2 h, c2x2split 1 starts 0.1 h, smoke 15 starts 0.0 h, wtest 8 starts 0.0 h.

## Distinct (c_l, omega) points: 49
| c_l | omega | omega/c_l | recorded starts | ranked |
|---|---|---|---|---|
| 0.41 | -3.0 | -7.3171 | 6 | 0 |
| 0.41 | -0.3 | -0.7317 | 6 | 0 |
| 0.41 | 0.1 | 0.2439 | 18 | 12 |
| 0.41 | 0.3 | 0.7317 | 13 | 7 |
| 0.41 | 1.0 | 2.439 | 18 | 12 |
| 0.41 | 3.0 | 7.3171 | 18 | 12 |
| 0.41 | 10.0 | 24.3902 | 18 | 12 |
| 0.42 | 0.3 | 0.7143 | 65 | 57 |
| 0.43 | -3.0 | -6.9767 | 6 | 0 |
| 0.43 | -0.3 | -0.6977 | 6 | 0 |
| 0.43 | 0.1 | 0.2326 | 18 | 12 |
| 0.43 | 0.3 | 0.6977 | 26 | 20 |
| 0.43 | 1.0 | 2.3256 | 26 | 19 |
| 0.43 | 3.0 | 6.9767 | 26 | 19 |
| 0.43 | 10.0 | 23.2558 | 18 | 12 |
| 0.4498 | 0.9015 | 2.0042 | 1 | 0 |
| 0.45 | -3.0 | -6.6667 | 6 | 0 |
| 0.45 | -0.3 | -0.6667 | 6 | 0 |
| 0.45 | 0.1 | 0.2222 | 12 | 6 |
| 0.45 | 0.2065 | 0.4589 | 1 | 0 |
| 0.45 | 0.3 | 0.6667 | 131 | 115 |
| 0.45 | 0.3014 | 0.6698 | 1 | 0 |
| 0.45 | 0.3232 | 0.7182 | 1 | 0 |
| 0.45 | 0.533 | 1.1844 | 1 | 0 |
| 0.45 | 0.9205 | 2.0456 | 1 | 0 |
| 0.45 | 1.0 | 2.2222 | 147 | 95 |
| 0.45 | 3.0 | 6.6667 | 27 | 21 |
| 0.45 | 10.0 | 22.2222 | 18 | 6 |
| 0.4509 | 1.0001 | 2.218 | 1 | 0 |
| 0.4518 | 0.368 | 0.8145 | 1 | 0 |
| 0.46 | 0.3 | 0.6522 | 1 | 1 |
| 0.47 | -3.0 | -6.383 | 6 | 0 |
| 0.47 | -0.3 | -0.6383 | 6 | 0 |
| 0.47 | 0.1 | 0.2128 | 18 | 12 |
| 0.47 | 0.3 | 0.6383 | 27 | 20 |
| 0.47 | 1.0 | 2.1277 | 32 | 23 |
| 0.47 | 3.0 | 6.383 | 26 | 16 |
| 0.47 | 10.0 | 21.2766 | 18 | 12 |
| 0.4707 | 0.9965 | 2.1171 | 1 | 0 |
| 0.475 | 0.3 | 0.6316 | 1 | 1 |
| 0.48 | 0.3 | 0.625 | 2 | 2 |
| 0.49 | -3.0 | -6.1224 | 6 | 0 |
| 0.49 | -0.3 | -0.6122 | 6 | 0 |
| 0.49 | 0.1 | 0.2041 | 18 | 12 |
| 0.49 | 0.3 | 0.6122 | 19 | 11 |
| 0.49 | 1.0 | 2.0408 | 18 | 9 |
| 0.49 | 3.0 | 6.1224 | 18 | 10 |
| 0.49 | 10.0 | 20.4082 | 18 | 6 |
| 0.499 | 0.2702 | 0.5415 | 1 | 0 |

## Ranking (shortlist filters, applied in order)
- excluded: 0 rows: no ranking key (rho_u_max_holdout, rho_u_max and rms_final all missing)
- excluded: 34 rows: disposable id (smoke, lm-only, val8/wtest, resume test)
- excluded: 8 rows: free-parameter job (ranked only after a fixed-parameter evaluation, SPEC 7.3)
- excluded: 271 rows: trivial or failed state (max|Omega| <= 1e-6, rotation content <= 1e-3, failure flag, max|U| <= 1e-6 or gauge defect > 1e-3)
- Ranked nontrivial states: 572 (all solver versions, as in STAGE1_SHORTLIST.md); 319 under the latest solver version only (v5-2026-10-24T21:05Z); 157 of the ranked rows predate 2026-10-24T19:39Z and are not used for ranked claims (G3); 0 ranked rows are flagged by a ledger correction record.
- Descriptor bins: not computed (--no_bins).
- Ranked rows that entered after the cited shortlist generation (2026-10-25T20:17Z): 1: nest8_L8_cl0.42_om+0.3_fixed_p0_cont150/0 (2026-10-25T20:57:07Z, 0.06154, c_l 0.42, omega 0.3, L 8).
- Lowest ranked rows at the boundary: nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/0 0.04367 (c_l 0.45, omega 1.0, L 8); nest8_L8_cl0.45_om+1.0_fixed_p0/0 0.04393 (c_l 0.45, omega 1.0, L 8); d6w_L8_cl0.45_om+0.3_fixed/0 0.04423 (c_l 0.45, omega 0.3, L 8); s1nk_L6_cl0.45_om+1.0_fixed_Nk32/0 0.0451 (c_l 0.45, omega 1.0, L 6); s1nk_L6_cl0.45_om+1.0_fixed_Nk24/0 0.04514 (c_l 0.45, omega 1.0, L 6).

## GPU use from the ledger wall times (launch -> first exit record of the same job, clipped at the boundary)
| GPU | process-hours | of which still running at the boundary | launches | distinct jobs | busy wall-hours | mean concurrency when busy | max concurrency | hours at concurrency 1 / 2 / 3+ | idle hours |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 31.41 | 0.88 | 65 | 54 | 27.18 | 1.16 | 2 | 22.95 / 4.23 / 0 | 1.5 |
| 1 | 35.63 | 4.33 | 83 | 63 | 27.4 | 1.3 | 2 | 19.16 / 8.24 / 0 | 1.28 |
| 4 | 39.68 | 4.28 | 87 | 74 | 27.33 | 1.45 | 2 | 14.99 / 12.35 / 0 | 1.35 |
| 5 | 33.43 | 4.76 | 62 | 46 | 27.71 | 1.21 | 3 | 22.45 / 4.81 / 0.45 | 0.97 |
- Three hour figures, side by side, with distinct definitions; they are never added together:
    - ALLOCATED GPU-hours (primary resource figure): 114.72 = 4 GPUs x 28.68 h from T0 2026-10-24T17:09:12Z to 2026-10-25T21:50:00Z.
    - LEDGER BUSY GPU WALL-HOURS (activity proxy): 109.6 = sum over GPUs of the wall time with at least one launch -> first-exit interval open.
    - LEDGER PROCESS-HOURS (activity proxy): 140.2 = sum over launches of (first exit record - launch); 1 to 3 processes shared a GPU.
- For reference only, the supervisor's 'minutes' of completed jobs (daily-report convention): 6941 GPU-slot minutes = 115.7 h.
- Jobs without an exit record: the ledger figures miss nothing else; the jobs running at the boundary (nest10_L10_cl0.45_om+0.3_fixed_p0, nest10_L10_cl0.45_om+1.0_fixed_p0, nest8nk8_L8_cl0.45_om+1.0_fixed, s10_L6_cl0.45_om+1.0_fixed_both1) are clipped at the boundary and their rows count as the next stage.
- 4 launches have no exit record before a relaunch of the same job (supervisor restarts on 2026-10-24); their wall time ends at the relaunch: [('c2x2_L10_cl0.47_om+1.0_fixed', '2026-10-24T20:49:50Z', 5), ('c2x2_L10_cl0.47_om+1.0_free', '2026-10-24T21:12:38Z', 4), ('c2x2_L10_cl0.47_om+1.0_free', '2026-10-24T21:17:07Z', 5), ('c2x2c_L6_cl0.45_om+1.0_free', '2026-10-24T22:33:00Z', 5)].
- 1 to 3 processes shared a GPU (slots_per_gpu 2 for non-exclusive jobs; exclusive L >= 8 and SPEC-channel jobs hold a whole GPU); ad hoc CPU/GPU evaluations outside the queue (exports, re-evaluations, pressure studies) are not in these wall times. Foreign processes (0.5 to 1.6 GB) are not ours and are not counted.
