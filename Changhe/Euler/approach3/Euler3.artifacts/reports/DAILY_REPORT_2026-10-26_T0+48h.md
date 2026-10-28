# Daily report, numerics lane, 2026-10-26 17:07Z T0 + 48 h

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
