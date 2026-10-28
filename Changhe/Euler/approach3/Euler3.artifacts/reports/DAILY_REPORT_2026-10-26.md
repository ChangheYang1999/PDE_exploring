# Daily report, numerics lane, 2026-10-26 T0 + 48 h (canonical copy; generated tables below from scripts/daily_report.py at 17:07Z; narrative written 2026-10-26T17:19Z, shift 10)

## Narrative (all values primary-reported and unvalidated unless stated; no state is a candidate; label provisional C, lead)

- Stage II (hours 30 to 72) runs to 2026-10-27T17:09Z; the gate II.4 schedule (lead d128 AV) is in RUN_STATUS.md item 5. Four GPUs (0, 1, 4, 5) run the queue; the lane holds 1.5 GB; <shared volume> had 238 GB free at 17:06Z.
- Degree-10 rungs of both nest ladders are READ and CLOSED under R2 (both floored at degree 10 with 4 channel functions; both stopped at the iteration limit): c_l 0.45, omega 0.3, omega/c_l 2/3: holdout rho_u^max 0.05650 / 0.05645, q_10 0.946 / 0.950, V10 0.0084; c_l 0.45, omega 1, omega/c_l 20/9: 0.04195 / 0.04145, q_10 0.961 / 0.957, V10 0.0052 (19.6 GPU-h). The omega 1 ladder falls by about 0.955 per two degrees (0.04604, 0.04393, 0.04195); the Tier S bound 1e-2 is 4.2x below the best degree-10 state. Both degree-10 states are exported (candidates/nest10_L10_cl0.45_om0.3_p0, nest10_L10_cl0.45_om1.0_p0).
- Degree-8 closure-met rungs (lead BV/CR; closure rows at weight 1 promoted from the S11 L6 states): the omega 1 rung nest8_L8_cl0.45_om+1.0_fixed_cl1 ended 16:42Z (ftol after 91 iterations, 1.86 reserved GPU-h) at holdout 0.02983 / 0.03130, the lowest of the campaign (2.98x / 3.13x the Tier S bound), with the unnormalized training momentum RMS rms_mom down only 7.4 per cent and the core-set a_max 1.206 = 2.02x nest10 (0.45, 1); max|U| +36 and max|Omega| +48 per cent; reached through an unsafeguarded lagged iteration (two excursions of three orders); NOT ORDERED under SPEC 7.3b against any state of the branch (the verifier's audit 62b59a82 confirms both 7.3b guards fail against all five comparators). The lead's decisions (d128 HS 4): a bounded diagnostic continuation with the safeguarded refresh (nest8_L8_cl0.45_om+1.0_fixed_cl1_sgcont150, enqueued 17:09:44Z, cap 1.9 GPU-h) and a SPEC 10 export (running on the CPU). The omega 0.3 rung nest8_L8_cl0.45_om+0.3_fixed_cl1 is running on GPU 5 since 15:59Z (iteration 95 at 17:07Z, in an unsafeguarded excursion: cost 9.9e-6 against 1.27e-8 at iteration 0); it will be read under the same rules (a state ending inside an excursion with a terminal cost above its start's is 'not a state to rank').
- nest8nk8_L8_cl0.45_om+1.0_fixed_cont150 (150-iteration continuation of nest8nk8, 0.04082 / 0.04141, the lowest independently checked state St1) is running on GPU 0 since 16:13Z (20000 s limit); its reading decides whether cont150's companion in the Stage III shortlist is replaced (lead HP 2).
- S9d balance-row chains are COMPLETE on both branches (kappa 0.1, 1, 10, 100 from the S11 weight-1 states Z0): (0.45, 1), Z0 0.04526 / 0.04457, ended at 0.05297 / 0.05455 at kappa 100 (1.170 / 1.224 of Z0; rms_mom +30 per cent; core-set a_max 4.7x); (0.45, 0.3), Z0 0.05227 / 0.05368 (an unsafeguarded end state whose gain depended on the excursion path, per the CV 4 replay read today), ended at 0.07143 / 0.07108 (1.367 / 1.324 of Z0; rms_mom +58 per cent). The balance rows do not bring E_ren to zero without raising the residual (NUM_REPORT Shift 8).
- All-m arms (three, all init_from perturbations of even-class states): the holdout ended between 2.8 per cent below and 4.7 per cent above the even-class degree-6 state of the same branch; no evidence that odd modes lower the residual materially; odd-mode states are not excluded. The S7 (c) m = 1 seeding relaxed back (odd content 10 -> 3.5 per cent of ||U||). S14, a FRESH all-m multi-start (four L4 jobs, 8 random/nonaxi/poloidal/toroidal starts each, c_l in {0.42, 0.45, 0.48}, omega in {0.3, 1}), is queued at priority 5 (cap 4 GPU-h; promotion rule in reports/S14_ENQUEUE_20261026.md).
- S8 pinned viscous ladders COMPLETE on both branches: 'viscosity does not remove the floor' (R^nu floor over the inviscid floor 1.00 to 1.39 at (0.45, 0.3), 1.07 to 1.23 at (0.45, 1)); every rung a 'viscous solve, not converged' (R7 (a) by one to two orders, (b) by sign). S7 (c) m = 2 boost at L6: an amplitude excursion, not a state.
- Robustness re-solves (lead d128 EQ; registration reports/STAGE2_ROBUSTNESS_REGISTRATION_20261026.md and Appendices A to F; eleven jobs at priority 6): the group (i) control s5ctl_L6_cl0.45_om+1.0_fixed_R0p3_ctl is running (iteration 255 at 17:17Z); the R0 0.6 variant FAILED as a re-solve (LM status xtol after one accepted step from a re-expanded warm start whose non-PDE rows cost 0.37 against a PDE cost 4.5e-8; max|U| 1.23 -> 15.25: an amplitude blow-up; not a reading of R0 sensitivity); the R0 0.15 variant released its LM right after iteration 0 (battery running). The four pending re-expanded variants are HELD (list below); the far-anchor variants (group (iii)) and the controls proceed as queued. The lead's rule for any corrected warm start (CPU evidence before GPU use; deadline 2026-10-27T12:00Z) is in the lead's reply of this shift.
- GPU use (whole-job seconds from the ledger): 204.9 GPU-slot hours of completed jobs since T0 (table below); the nest ladder 72.0 h, from-scratch sweeps 49.2 h, D6 lineage 22.2 h, S8 6.2 h, S9/S9b/S9d 4.2 h, S7 4.0 h, other 11.2 h.

## Held jobs (queue/hold, not launched; each file carries its hold_reason)

- s4cl_L6_cl0.42_om+0.3_fixed_from045, s4cl_L6_cl0.44_om+0.3_fixed_from045, s4cl_L6_cl0.46_om+0.3_fixed_from045, s4cl_L6_cl0.48_om+0.3_fixed_from045: not launched under the registered warm-start gauge rule (lead d128 DU / DW): warm-start ||F|| - 1 of -0.19 to +0.2 at the target c_l, above 0.05 (reports/warm_start_gauge_s4cl.json); a pre-registered outcome, not a failure and not a reading.
- s5r0_L6_cl0.45_om+0.3_fixed_R0p6, s5r0_L6_cl0.45_om+0.3_fixed_R0p15, s5r0_L8_cl0.45_om+1.0_fixed_R0p6, s5r0_L8_cl0.45_om+1.0_fixed_R0p15: hold_reason (shared): "held 2026-10-26T17:15:26Z (shift 10): the group (i) re-expanded R0 variants s5r0_L6_cl0.45_om+1.0_fixed_R0p6 (DONE 17:06:57Z, LM status xtol after one accepted step, non-PDE row cost of the re-expanded start 0.3699 against a PDE cost 4.48e-8; the step raised max|U| from 1.23 to 15.25: an amplitude blow-up, a failed re-solve) and R0p15 (LM released after iteration 0) failed as re-solves; this re-expanded warm start is ..." (held this shift; the lead accepted the hold; release with scripts/release_hold.sh after a dated lead note).

## Generated tables (scripts/daily_report.py 'T0 + 48 h', 17:07Z)


Campaign elapsed: 47.98 h of 96 (T0 = 2026-10-24T17:09:14Z, logged). Stage II. Stage I ends 2026-10-25T23:09Z, Stage II 2026-10-27T17:09Z, Stage III 2026-10-28T17:09Z.

## Resource use (measured)

- Starts completed: 933 (by degree L: {10: 6, 2: 187, 4: 45, 6: 678, 8: 17}); jobs completed: 240; GPU-slot minutes of completed jobs: 12296 = 204.9 GPU-slot hours (1-3 processes per GPU on GPUs 0, 1, 4, 5; exclusive L8 jobs hold a whole GPU); largest job RSS 11.2 GB (host).
- Start types (formulation, nl_weighting, optimizer): {('vort', False, 'lm'): 218, ('mom', True, 'lm'): 571, ('vort', True, 'lm'): 139, ('both', True, 'lm'): 5}
- GPU hours per lineage (start wall time, from the ledger):
    - nest ladder (route's own random-start ladder L2 -> L4 -> L6 -> L8): 207 starts, 72.0 h
    - from-scratch L6 sweeps and continuations (s1*, c2x2*): 610 starts, 49.2 h
    - D6 lineage (independent-route transfer d6*, continuations): 27 starts, 22.2 h
    - other (smoke, tests, controls): 55 starts, 11.2 h
    - S8 artificial viscosity (labelled viscous continuation states): 9 starts, 6.2 h
    - S9/S9b balance arm: 14 starts, 4.2 h
    - S7 mean-swirl probes: 11 starts, 4.0 h

## Best states by holdout rho_u^max (SPEC 7.3 key; standing lines; none is a candidate: no state reaches Tier S; all primary-reported, unvalidated unless stated in NUM_REPORT)

- nest8_L8_cl0.45_om+1.0_fixed_cl1/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0298 std / 0.0313 half; rho_nl^max 0.33; sigma_u^max 0.51; sigma_Om 0.40; a_max 1.21; rho_lin 0.11; Q_sw 0.407; tau_F 0.427; tau_0/1/2 1.2e-04/8.5e-03/1.9e-01; E_ren -1.071; H_tot/int|h| -0.599; K_E ratio 1.00; K_H ratio 1.00; V10 4.4e-01; 91 its, 1.01 GPU-h; status ftol
- s11_L6_cl0.45_om+1.0_fixed_cl1ftol/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 16): rho_u^max 0.0311 std / 0.0333 half; rho_nl^max 0.20; sigma_u^max 0.48; sigma_Om 0.39; a_max 0.91; rho_lin 0.17; Q_sw 0.435; tau_F 0.473; tau_0/1/2 8.9e-04/1.3e-02/4.1e-02; E_ren -0.993; H_tot/int|h| -0.700; K_E ratio 1.01; K_H ratio 0.99; V10 5.4e-01; 300 its, 0.74 GPU-h; status max_iter
- nest8nk8_L8_cl0.45_om+1.0_fixed/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0408 std / 0.0414 half; rho_nl^max 0.93; sigma_u^max 0.45; sigma_Om 0.43; a_max 0.84; rho_lin 0.13; Q_sw 0.601; tau_F 0.521; tau_0/1/2 6.0e-03/3.3e-02/2.3e-01; E_ren -1.358; H_tot/int|h| -0.710; K_E ratio 0.24; K_H ratio 1.01; V10 8.9e-03; 150 its, 4.45 GPU-h; status max_iter
- s12_L6_cl0.45_om+1.0_fixed_rl3/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 16): rho_u^max 0.0417 std / 0.0443 half; rho_nl^max 0.65; sigma_u^max 0.59; sigma_Om 0.57; a_max 1.35; rho_lin 0.13; Q_sw 0.197; tau_F 0.459; tau_0/1/2 1.8e-03/4.3e-02/3.3e-01; E_ren -1.129; H_tot/int|h| -0.740; K_E ratio 372.70; K_H ratio 1.50; V10 6.2e-02; 300 its, 0.81 GPU-h; status max_iter
- nest10_L10_cl0.45_om+1.0_fixed_p0/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 10, Nk 24): rho_u^max 0.0420 std / 0.0415 half; rho_nl^max 1.13; sigma_u^max 0.42; sigma_Om 0.42; a_max 0.60; rho_lin 0.15; Q_sw 0.682; tau_F 0.557; tau_0/1/2 3.2e-03/4.0e-02/2.1e-01; E_ren -1.570; H_tot/int|h| -0.699; K_E ratio -4.25; K_H ratio 1.04; V10 5.2e-03; 300 its, 19.63 GPU-h; status max_iter
- nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0437 std / 0.0433 half; rho_nl^max 1.13; sigma_u^max 0.44; sigma_Om 0.42; a_max 0.60; rho_lin 0.16; Q_sw 0.651; tau_F 0.564; tau_0/1/2 4.4e-03/4.0e-02/1.6e-01; E_ren -1.583; H_tot/int|h| -0.700; K_E ratio -4.94; K_H ratio 1.05; V10 2.1e-03; 83 its, 0.95 GPU-h; status ftol
- nest8_L8_cl0.45_om+1.0_fixed_p0/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0439 std / 0.0435 half; rho_nl^max 1.15; sigma_u^max 0.43; sigma_Om 0.42; a_max 0.58; rho_lin 0.16; Q_sw 0.647; tau_F 0.567; tau_0/1/2 3.7e-03/3.9e-02/1.6e-01; E_ren -1.590; H_tot/int|h| -0.700; K_E ratio -5.18; K_H ratio n/a; V10 8.0e-03; 300 its, 3.43 GPU-h; status max_iter
- d6w_L8_cl0.45_om+0.3_fixed/0 (c_l 0.45, omega 0.3, omega/c_l 0.667, L 8, Nk 20): rho_u^max 0.0442 std / 0.0543 half; rho_nl^max 1.46; sigma_u^max 1.82; sigma_Om 1.38; a_max 2.19; rho_lin 0.49; Q_sw 0.150; tau_F 0.898; tau_0/1/2 4.5e-04/1.6e-02/3.3e-02; E_ren -0.982; H_tot/int|h| -0.877; K_E ratio -434.48; K_H ratio 1.60; V10 n/a; 180 its, 2.00 GPU-h; status time_limit
- s9d_L6_cl0.45_om+1.0_fixed_bal0.000131342_corepin_naxpin_k0.1/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 16): rho_u^max 0.0448 std / 0.0443 half; rho_nl^max 0.42; sigma_u^max 0.45; sigma_Om 0.39; a_max 0.67; rho_lin 0.16; Q_sw 0.640; tau_F 0.548; tau_0/1/2 8.3e-04/1.4e-02/1.1e-01; E_ren -1.311; H_tot/int|h| -0.677; K_E ratio 1.00; K_H ratio 1.00; V10 9.5e-01; 100 its, 0.38 GPU-h; status max_iter
- s1nk_L6_cl0.45_om+1.0_fixed_Nk32/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 32): rho_u^max 0.0451 std / 0.0451 half; rho_nl^max 1.06; sigma_u^max 0.46; sigma_Om 0.42; a_max 0.62; rho_lin 0.16; Q_sw 0.628; tau_F 0.570; tau_0/1/2 2.0e-03/4.8e-02/2.2e-01; E_ren -1.560; H_tot/int|h| -0.698; K_E ratio -3.23; K_H ratio 1.04; V10 1.2e-02; 238 its, 2.01 GPU-h; status time_limit

## Exports (candidates/, SPEC 10 format; immutable, SHA256 manifests; v1.24 far-coefficient supplements beside meta.json)

- d6t_L6_cl0.45_om0.3 (32 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- d6t_L8_cl0.45_om0.3 (32 MB): K_E ratio -2835.41, K_H ratio 1.391, carried mismatch 4.425
- d6w3_L6_cl0.45_om0.3 (32 MB): K_E ratio -3.25, K_H ratio 1.074, carried mismatch 0.216
- d6w_L6_cl0.45_om0.3 (32 MB): K_E ratio -15.22, K_H ratio 0.182, carried mismatch 1.419
- d6w_L8_cl0.45_om0.3 (32 MB): K_E ratio -434.48, K_H ratio 1.599, carried mismatch 4.297
- nest10_L10_cl0.45_om0.3_p0 (39 MB): K_E ratio -0.01, K_H ratio 1.224, carried mismatch 0.041
- nest10_L10_cl0.45_om1.0_p0 (39 MB): K_E ratio -4.25, K_H ratio 1.043, carried mismatch 0.056
- nest4_L4_cl0.42_om0.3_p0 (56 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest4_L4_cl0.45_om1.0_p0 (32 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest4_L4_cl0.45_om1.0_p0_d2u (56 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest6_L6_cl0.42_om0.3_p0 (57 MB): K_E ratio 5.38, K_H ratio 1.317, carried mismatch 0.349
- nest6_L6_cl0.45_om0.3_p0 (57 MB): K_E ratio -8.98, K_H ratio 4.242, carried mismatch 0.399
- nest6_L6_cl0.45_om0.3_p1 (57 MB): K_E ratio 19.08, K_H ratio 2.186, carried mismatch 0.980
- nest6_L6_cl0.45_om1.0_p0 (57 MB): K_E ratio -32.63, K_H ratio 1.262, carried mismatch 0.346
- nest6_L6_cl0.45_om1.0_p1 (57 MB): K_E ratio 29.74, K_H ratio 1.212, carried mismatch 0.466
- nest8_L8_cl0.42_om0.3_p0 (32 MB): K_E ratio 3.88, K_H ratio 1.214, carried mismatch 0.210
- nest8_L8_cl0.42_om0.3_p0_cont150 (32 MB): K_E ratio 3.86, K_H ratio 1.207, carried mismatch 0.200
- nest8_L8_cl0.45_om0.3_p0 (32 MB): K_E ratio -0.28, K_H ratio 1.276, carried mismatch 0.049
- nest8_L8_cl0.45_om0.3_p0_cont150 (32 MB): K_E ratio -0.22, K_H ratio 1.259, carried mismatch 0.047
- nest8_L8_cl0.45_om1.0_p0 (32 MB): K_E ratio -5.18, K_H ratio 1.054, carried mismatch 0.069
- nest8_L8_cl0.45_om1.0_p0_cont150 (32 MB): K_E ratio -4.94, K_H ratio 1.051, carried mismatch 0.067
- nest8nk8_L8_cl0.45_om1.0_p0 (39 MB)
- s11_L6_cl0.45_om0.3_cl1 (64 MB): K_E ratio 1.00, K_H ratio 1.000, carried mismatch 0.000
- s11_L6_cl0.45_om1.0_cl1 (39 MB): K_E ratio 1.00, K_H ratio 1.000, carried mismatch 0.000
- s11_L6_cl0.45_om1.0_cl1_d2u (57 MB)
- s9b_L4_cl0.45_om1.0_bal10 (57 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000
- stage1_best_affine_cl0.45_om1 (33 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000
- stage1_best_sigmaZ_cl0.43_om1 (33 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000

## Optimizer exit statuses and failure modes

- Exit statuses of all starts: {'max_iter': 521, 'ftol': 352, 'stalled': 47, 'time_limit': 12, 'xtol': 1}
- Job errors, retries and failures: 98 records; last: job_error runs/t11lit/job_P.json RuntimeError('shape mismatch: value tensor of shape [12, 12]; job_error runs/t11lit/job_P.json RuntimeError('shape mismatch: value tensor of shape [12, 12]; job_error runs/sgsmoke/job_B.json RuntimeError('shape mismatch: value tensor of shape [12, 12]; job_error runs/sgsmoke/job_C.json RuntimeError('shape mismatch: value tensor of shape [12, 12]; job_error runs/sgsmoke/job_A.json RuntimeError('shape mismatch: value tensor of shape [12, 12]
- Failure map: FAILURE_ANALYSIS.md (numbered items with mechanisms and remedies); current label provisional C (lead): no accepted candidate, no obstruction.

## Supervisor and queue (machine-readable: status/STATUS.json, updated every poll)

- 2026-10-26T17:07:40Z: running 4 (nest8_L8_cl0.45_om+0.3_fixed_cl1, nest8nk8_L8_cl0.45_om+1.0_fixed_cont150, s5ctl_L6_cl0.45_om+1.0_fixed_R0p3_ctl, s5r0_L6_cl0.45_om+1.0_fixed_R0p15), pending 12, done 239, failed 30, disk free 238.5 GB, lane 1.43 GB, GPUs {'0': {'mem_MiB': 43905, 'util': 14}, '1': {'mem_MiB': 3157, 'util': 0}, '4': {'mem_MiB': 49843, 'util': 20}, '5': {'mem_MiB': 44785, 'util': 36}}

## Pointers

- NUM_REPORT.md (current summary), reports/STAGE1_SHORTLIST.md (G4 shortlist with the 7.3b pairwise table), reports/G1_TESTS.md, reports/G3_LEDGER.md, reports/FAR_COEFFICIENTS.md (SPEC v1.24 7.8), reports/GATE_I4_RESPONSE_DRAFT.md, reports/STAGE2_FEASIBILITY_DRAFT.md, reports/RESOLUTION_LADDER.md, reports/figures/.
