# Daily report, numerics lane, 2026-10-25 17:08Z T0 + 24 h

Campaign elapsed: 23.99 h of 96 (T0 = 2026-10-24T17:09:14Z, logged). Stage I. Stage I ends 2026-10-25T23:09Z, Stage II 2026-10-27T17:09Z, Stage III 2026-10-28T17:09Z.

## Resource use (measured)

- Starts completed: 880 (by degree L: {10: 2, 2: 187, 4: 36, 6: 641, 8: 14}); jobs completed: 195; GPU-slot minutes of completed jobs: 6434 = 107.2 GPU-slot hours (1-3 processes per GPU on GPUs 0, 1, 4, 5; exclusive L8 jobs hold a whole GPU); largest job RSS 6.5 GB (host).
- Start types (formulation, nl_weighting, optimizer): {('vort', False, 'lm'): 218, ('mom', True, 'lm'): 522, ('vort', True, 'lm'): 139, ('both', True, 'lm'): 1}
- GPU hours per lineage (start wall time, from the ledger):
    - from-scratch L6 sweeps and continuations (s1*, c2x2*): 597 starts, 35.9 h
    - nest ladder (route's own random-start ladder L2 -> L4 -> L6 -> L8): 200 starts, 25.2 h
    - D6 lineage (independent-route transfer d6*, continuations): 27 starts, 22.2 h
    - S8 artificial viscosity (labelled viscous continuation states): 5 starts, 3.1 h
    - S9/S9b balance arm: 5 starts, 1.8 h
    - S7 mean-swirl probes: 9 starts, 1.2 h
    - other (smoke, tests, controls): 37 starts, 1.1 h

## Best states by holdout rho_u^max (SPEC 7.3 key; standing lines; none is a candidate: no state reaches Tier S; all primary-reported, unvalidated unless stated in NUM_REPORT)

- nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0437 std / 0.0433 half; rho_nl^max 1.13; sigma_u^max 0.44; sigma_Om 0.42; a_max 0.60; rho_lin 0.16; Q_sw 0.651; tau_F 0.564; tau_0/1/2 4.4e-03/4.0e-02/1.6e-01; E_ren -1.583; H_tot/int|h| -0.700; K_E ratio -4.94; K_H ratio 1.05; V10 2.1e-03; 83 its, 0.95 GPU-h; status ftol
- nest8nk8smoke_L8_cl0.45_om+1.0_fixed/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0439 std / 0.0443 half; rho_nl^max 1.04; sigma_u^max 0.42; sigma_Om 0.42; a_max 0.59; rho_lin 0.16; Q_sw 0.694; tau_F 0.560; tau_0/1/2 2.9e-03/4.1e-02/1.7e-01; E_ren -1.493; H_tot/int|h| -0.703; K_E ratio 0.29; K_H ratio 1.01; V10 1.1e-02; 3 its, 0.08 GPU-h; status max_iter
- nest8_L8_cl0.45_om+1.0_fixed_p0/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 8, Nk 20): rho_u^max 0.0439 std / 0.0435 half; rho_nl^max 1.15; sigma_u^max 0.43; sigma_Om 0.42; a_max 0.58; rho_lin 0.16; Q_sw 0.647; tau_F 0.567; tau_0/1/2 3.7e-03/3.9e-02/1.6e-01; E_ren -1.590; H_tot/int|h| -0.700; K_E ratio -5.18; K_H ratio n/a; V10 8.0e-03; 300 its, 3.43 GPU-h; status max_iter
- d6w_L8_cl0.45_om+0.3_fixed/0 (c_l 0.45, omega 0.3, omega/c_l 0.667, L 8, Nk 20): rho_u^max 0.0442 std / 0.0543 half; rho_nl^max 1.46; sigma_u^max 1.82; sigma_Om 1.38; a_max 2.19; rho_lin 0.49; Q_sw 0.150; tau_F 0.898; tau_0/1/2 4.5e-04/1.6e-02/3.3e-02; E_ren -0.982; H_tot/int|h| -0.877; K_E ratio -434.48; K_H ratio 1.60; V10 n/a; 180 its, 2.00 GPU-h; status time_limit
- s1nk_L6_cl0.45_om+1.0_fixed_Nk24/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 24): rho_u^max 0.0451 std / 0.0445 half; rho_nl^max 1.04; sigma_u^max 0.47; sigma_Om 0.41; a_max 0.63; rho_lin 0.17; Q_sw 0.637; tau_F 0.573; tau_0/1/2 2.9e-03/4.8e-02/1.4e-01; E_ren -1.560; H_tot/int|h| -0.697; K_E ratio -2.19; K_H ratio 1.03; V10 1.5e-02; 300 its, 1.40 GPU-h; status max_iter
- d6t_L8_cl0.45_om+0.3_fixed/0 (c_l 0.45, omega 0.3, omega/c_l 0.667, L 8, Nk 20): rho_u^max 0.0456 std / 0.0554 half; rho_nl^max 3.03; sigma_u^max 1.86; sigma_Om 1.39; a_max 2.23; rho_lin 0.50; Q_sw n/a; tau_F n/a; tau_0/1/2 n/a/n/a/n/a; E_ren n/a; H_tot/int|h| n/a; K_E ratio n/a; K_H ratio n/a; V10 n/a; 300 its, 0.37 GPU-h; status max_iter
- nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 16): rho_u^max 0.0460 std / 0.0463 half; rho_nl^max 1.04; sigma_u^max 0.45; sigma_Om 0.41; a_max 0.56; rho_lin 0.18; Q_sw 0.673; tau_F 0.583; tau_0/1/2 2.9e-03/3.6e-02/1.5e-01; E_ren -1.543; H_tot/int|h| -0.711; K_E ratio n/a; K_H ratio n/a; V10 6.1e-02; 600 its, 1.92 GPU-h; status max_iter
- s12smoke_L6_cl0.45_om+1.0_fixed_rl3/0 (c_l 0.45, omega 1.0, omega/c_l 2.222, L 6, Nk 16): rho_u^max 0.0481 std / 0.0510 half; rho_nl^max 0.95; sigma_u^max 0.47; sigma_Om 0.55; a_max 0.57; rho_lin 0.14; Q_sw 0.526; tau_F 0.543; tau_0/1/2 7.4e-04/3.7e-02/1.3e-01; E_ren -1.376; H_tot/int|h| -0.718; K_E ratio -62.05; K_H ratio 1.71; V10 4.3e-02; 3 its, 0.01 GPU-h; status max_iter
- s1nk_L6_cl0.45_om+0.3_fixed_Nk32/0 (c_l 0.45, omega 0.3, omega/c_l 0.667, L 6, Nk 32): rho_u^max 0.0508 std / 0.0701 half; rho_nl^max 0.23; sigma_u^max 1.80; sigma_Om 1.30; a_max 1.81; rho_lin 0.49; Q_sw 0.188; tau_F 0.885; tau_0/1/2 3.5e-04/1.1e-02/4.0e-02; E_ren -1.059; H_tot/int|h| -0.824; K_E ratio -0.53; K_H ratio 1.03; V10 9.7e-03; 239 its, 2.00 GPU-h; status time_limit
- d6u_L8_cl0.45_om+0.3_fixed/0 (c_l 0.45, omega 0.3, omega/c_l 0.667, L 8, Nk 20): rho_u^max 0.0509 std / 0.0720 half; rho_nl^max 3.82; sigma_u^max n/a; sigma_Om n/a; a_max n/a; rho_lin 0.50; Q_sw n/a; tau_F n/a; tau_0/1/2 n/a/n/a/n/a; E_ren n/a; H_tot/int|h| n/a; K_E ratio n/a; K_H ratio n/a; V10 n/a; 222 its, 0.05 GPU-h; status ftol

## Exports (candidates/, SPEC 10 format; immutable, SHA256 manifests; v1.24 far-coefficient supplements beside meta.json)

- d6t_L6_cl0.45_om0.3 (32 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- d6t_L8_cl0.45_om0.3 (32 MB): K_E ratio -2835.41, K_H ratio 1.391, carried mismatch 4.425
- d6w3_L6_cl0.45_om0.3 (32 MB): K_E ratio -3.25, K_H ratio 1.074, carried mismatch 0.216
- d6w_L6_cl0.45_om0.3 (32 MB): K_E ratio -15.22, K_H ratio 0.182, carried mismatch 1.419
- d6w_L8_cl0.45_om0.3 (32 MB): K_E ratio -434.48, K_H ratio 1.599, carried mismatch 4.297
- nest4_L4_cl0.42_om0.3_p0 (56 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest4_L4_cl0.45_om1.0_p0 (32 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest4_L4_cl0.45_om1.0_p0_d2u (56 MB): K_E ratio 0.00, K_H ratio -0.000, carried mismatch 1.000
- nest6_L6_cl0.42_om0.3_p0 (57 MB): K_E ratio 5.38, K_H ratio 1.317, carried mismatch 0.349
- nest6_L6_cl0.45_om0.3_p0 (57 MB): K_E ratio -8.98, K_H ratio 4.242, carried mismatch 0.399
- nest6_L6_cl0.45_om0.3_p1 (57 MB): K_E ratio 19.08, K_H ratio 2.186, carried mismatch 0.980
- nest6_L6_cl0.45_om1.0_p0 (57 MB): K_E ratio -32.63, K_H ratio 1.262, carried mismatch 0.346
- nest6_L6_cl0.45_om1.0_p1 (57 MB): K_E ratio 29.74, K_H ratio 1.212, carried mismatch 0.466
- nest8_L8_cl0.42_om0.3_p0 (32 MB): K_E ratio 3.88, K_H ratio 1.214, carried mismatch 0.210
- nest8_L8_cl0.45_om0.3_p0 (32 MB): K_E ratio -0.28, K_H ratio 1.276, carried mismatch 0.049
- nest8_L8_cl0.45_om0.3_p0_cont150 (32 MB): K_E ratio -0.22, K_H ratio 1.259, carried mismatch 0.047
- nest8_L8_cl0.45_om1.0_p0 (32 MB): K_E ratio -5.18, K_H ratio 1.054, carried mismatch 0.069
- nest8_L8_cl0.45_om1.0_p0_cont150 (32 MB): K_E ratio -4.94, K_H ratio 1.051, carried mismatch 0.067
- s9b_L4_cl0.45_om1.0_bal10 (57 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000
- stage1_best_affine_cl0.45_om1 (33 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000
- stage1_best_sigmaZ_cl0.43_om1 (33 MB): K_E ratio 0.00, K_H ratio 0.000, carried mismatch 1.000

## Optimizer exit statuses and failure modes

- Exit statuses of all starts: {'max_iter': 479, 'ftol': 346, 'stalled': 47, 'time_limit': 8}
- Job errors, retries and failures: 93 records; last: job_error queue/running/nest10smoke_L10_cl0.45_om+1.0_fixed.json OutOfMemoryError('CUDA out of memory. Tried to allocate 43.5; job_retry nest10smoke_L10_cl0.45_om+1.0_fixed exit 1; job_error queue/running/nest10smoke_L10_cl0.45_om+1.0_fixed.json OutOfMemoryError('CUDA out of memory. Tried to allocate 43.5; job_retry nest10smoke_L10_cl0.45_om+1.0_fixed exit 1; job_retry nest10smoke_L10_cl0.45_om+1.0_fixed_ch19 exit -9
- Failure map: FAILURE_ANALYSIS.md (numbered items with mechanisms and remedies); current label provisional C (lead): no accepted candidate, no obstruction.

## Supervisor and queue (machine-readable: status/STATUS.json, updated every poll)

- 2026-10-25T17:08:22Z: running 4 (s1nk_L6_cl0.45_om+1.0_fixed_Nk32, nest10smoke_L10_cl0.45_om+1.0_fixed_ch19, nest10smoke_L10_cl0.45_om+1.0_fixed_jtj2, nest10_L10_cl0.45_om+1.0_fixed_p0), pending 12, done 194, failed 30, disk free 203.0 GB, lane 1.08 GB, GPUs {'0': {'mem_MiB': 76761, 'util': 100}, '1': {'mem_MiB': 79355, 'util': 0}, '4': {'mem_MiB': 72061, 'util': 9}, '5': {'mem_MiB': 17313, 'util': 26}}

## Pointers

- NUM_REPORT.md (current summary), reports/STAGE1_SHORTLIST.md (G4 shortlist with the 7.3b pairwise table), reports/G1_TESTS.md, reports/G3_LEDGER.md, reports/FAR_COEFFICIENTS.md (SPEC v1.24 7.8), reports/GATE_I4_RESPONSE_DRAFT.md, reports/STAGE2_FEASIBILITY_DRAFT.md, reports/RESOLUTION_LADDER.md, reports/figures/.
