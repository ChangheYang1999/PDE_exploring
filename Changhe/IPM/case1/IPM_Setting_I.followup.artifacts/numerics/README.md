# Artifacts: numerics for the strong setting P_inf of IPM Setting I (follow-up run, numerical researcher)

Status: final. Three full-solve resolutions at L = 8 ((72,30), (96,40), (120,48)) and three compactification scales at (96,40) (L = 4, 8, 16) under the smooth system, each with its dense Jacobian, stagnation state, SVD, S4 (e) row and exact-action Ritz values (data/svd_*, s4e_*, ritz_*, dnB_*/dnSB_* states); soft-direction diagnostics (smooth_*, reweight_*, actloc_*, valley_s4e_*, opchannel_*, chk_modes_*). Verdict (section 6.4 of the report): no endpoint; Q1 undecided by the resolution-sequence reading (S3 (e)) on three grids; B_3 unreadable at residuals 1e-4. The command sequences of the full solves are in COMMANDS.md (chains E2b for the grids and domains, K for the third resolution, A and B for the earlier systems).
Everything runs with python3 + torch (CUDA) + numpy + scipy; single-threaded CPU (OMP_NUM_THREADS=1); one GPU. The programs locate their working folder through the constant LANE
(in src/jtools.py and at the top of the standalone programs), set to "." for publication: run every command from this folder (numerics/), after creating runs/ and copying or linking the files of data/ into it (the programs read states and write outputs under runs/).
The B_3 estimator (src/b3_axis.py) imports the lead researcher's B_3 evaluator from ../lead/b3_functional/b3infl, the lead researcher's part of these artifacts.
Labels such as S3 (e) or S4 (e) in comments and file names refer to items of the run's specification, defined in section 6.4 of the report (the
resolution-sequence reading and the axis-coefficient row).
Publication changes: absolute local paths were replaced by paths relative to this folder (LANE = "."; other parts as ../lead, ../verifier); the job-driver shell chains (scripts/) are replaced by COMMANDS.md; two backup copies of earlier program versions (ipm_newton_v1_backup.py, charmap_pre_tauswitch_backup.py, needed only for numbers of the first sessions that the report does not use) and run logs are not included. The numerical researcher's internal report and work log, cited below as "the numerical findings" and "the research record", are not published; the results the report uses are stated in its section 6.4.

## Top-level parts
- src/: the solver, the Jacobian / SVD / Ritz tools and the diagnostics (Python, torch CUDA).
- data/: the stagnation states (npz) of the five discrete systems and every json / log quoted in the numerical findings (SVD reports, S4 (e) rows, Ritz values, valley, reweighting, smoothness, operator-channel, direct checks).
- COMMANDS.md: the exact command sequences of the chains that produced the states.
- tests/: the model tests (section 2 of the numerical findings).

## Data used by the report (section 6.4 Q1 of the lead's report) and their files in data/
Each discrete system has a stagnation state (npz: b on the grid, c_l, C and the grid parameters), an SVD report (svd_*.json: residual norms, c_l, C, stationarity,
matrix singular values in two norms, soft vectors with their fresh responses), an axis-coefficient row (s4e_*.json: x*, g(P), h(P) - 1, identity defect, Taylor
coefficients d1, d3, d5, d7 of the axis function at the origin, B_3 estimators) and the exact-action Ritz values on 24 directions (ritz_*.json).
- (72,30), L = 8:  dnB_n72m30S.npz (md5 c81d083063696cae2087d72351ea2526), svd_n72m30S_final.json, s4e_dnB_n72m30S.json, ritz_n72m30S.json, reweight_n72m30S.json,
  smooth_n72m30S.json; second pass (not used by the report): dnC_n72m30S.npz, svd_n72m30S_final2.json, s4e_dnC_n72m30S.json, ritz_n72m30S_C.json.
- (84,35), L = 8:  dnB_n84m35S.npz (md5 53d5486acd2ebdf91a401d4c374b28e3), svd_n84m35S_final.json, s4e_dnB_n84m35S.json, ritz_n84m35S.json, reweight_n84m35S.json.
- (96,40), L = 8:  dnB_n96m40S.npz (md5 f5b77e128474f1f9da8e3051c22ad505), svd_n96m40S_final.json, s4e_dnB_n96m40S.json, ritz_n96m40S.json, reweight_n96m40S.json, smooth_n96m40S.json.
- (120,48), L = 8: dnSB_n120m48.npz (md5 0234b3634f747b0a50386d0359bea823), svd_n120m48_S.json, s4e_dnSB_n120m48.json, ritz_n120m48_S.json, reweight_n120m48_S.json,
  smooth_n120m48_S.json, actloc_n120m48_S.json, opchannel_n120m48_S.json, valley_s4e_n120m48_S.json, chk_modes_n120m48_S.out.
- (96,40), L = 4:  dnB_n96m40SL4.npz (md5 c103a60bbbf2279e7c21f4f5a2b580be), svd_n96m40SL4_final.json, s4e_dnB_n96m40SL4.json, ritz_n96m40SL4.json, reweight_n96m40SL4.json, smooth_n96m40SL4.json.
- (96,40), L = 16: dnB_n96m40SL16.npz (md5 bc8c82ca4baaf6c000a144284ff21bec), svd_n96m40SL16_final.json, s4e_dnB_n96m40SL16.json, ritz_n96m40SL16.json, reweight_n96m40SL16.json, smooth_n96m40SL16.json.
- Earlier states and diagnostics (session 1 to 3; the session-3 record sections of the numerical findings): dnC_n120m48.npz, dn2_n120m48.npz, dnA_n120m48.npz, dnR8_n120m48.npz,
  dnS_dt0005_n120m48.npz, the fixed-c_l histories fixcl*_hist.json, crossgrid_*.json, anatomy_*.json, colcheck_*.json, dirtest_*.json, s3*.json, valley_*.json.
- (108,44), L = 8 (NOT used by the lead's report, computed after its content was frozen; the verifier's independent whole-plane audit of this state completed 2026-10-21T00:12:28Z, recorded in the numerical findings section 5): dnB_n108m44S.npz (md5 306dbedbf3d5f31045a4de1e4c28e028),
  svd_n108m44S_final.json, s4e_dnB_n108m44S.json, ritz_n108m44S.json.

## Code (src/)
- ipm_newton.py   collocation model on the whole plane: rho = r^3 w cos^2 sin b(q, theta), Chebyshev in the compactified q,
                  mapped Fourier in the angle (beta clusters angles at the y-axis), canonical modal inverse (the canonical modal inverse), exact
                  dense Jacobian (b-columns exact for the quadratic residual, c_l column by forward-mode AD), Newton, LM.
- charmap.py      Psi-map (characteristics) formulation: backward RK4 orbits from every node to P, eta_P with the b - h_P
                  integrand and the analytic tail, hybrid residual F (collocation rows at the innermost nodes, Psi rows elsewhere,
                  h(P) - 1, identity), vmap-friendly F_fixed.
- run_newton.py   collocation Newton driver from the X3 seed (data/c6g_shape.npz via rayshape_firstrun.py) or a saved state;
                  stagnation data; smallest singular values.
- run_psi_newton.py  Newton-Krylov (GMRES with FD matvecs) on the Psi formulation (options --far_psi --n_coll --coll_scale --scl).
- jac_dense.py    dense Jacobian of the hybrid Psi residual by batched (vmap) finite differences, resumable.
- dense_newton.py Newton + Broyden with the dense Jacobian, SVD, soft vectors, stagnation, B_3.
- twogrid.py      two-grid preconditioned Newton-Krylov for finer grids (coarse dense Jacobian as preconditioner).
- nullspace.py, orbit_diag.py   smallest singular triplets of the collocation Jacobian; delta rho / rho along orbits to P.
- s3_svd.py, s3f_alpha.py       the singular-value diagnostics (S3 (a) to (c)) singular values in the lead's norms; S3 (f) first-order costs alpha_cl, alpha_B3.
- b3_axis.py, s4e_row.py        axis w, w', w'' and B_3 by the lead researcher's B_3 tool b3core.py (part of the lead's artifacts, not included here; b3_axis.py imports it by path); the axis-coefficient row (S4 (e)).
- rayshape_firstrun.py          the first run's GPU evaluator of the published trial formula (copied, unchanged).
- s3f_psi.py                    S3 (f) first-order costs in the Psi formulation from a stored dense Jacobian.
- jtools.py                     shared helpers: load a stored Jacobian, S3 (a) norm scalings, LM step with projector, soft vectors,
                                S3 (c) structure diagnostics (Diag); RES_KW = the discrete system (Npsi 480, dt 0.01, dt_near 0.04).
- svd_report.py                 SVD of a stored Jacobian in two norms, smallest 20, counts, soft vectors with S3 (c) diagnostics and
                                the accurate-residual response along each.
- constrained_newton.py         LM-Newton with c_l frozen (--cl) or a prescribed amplitude along a stored direction (--vec), or free
                                (--free, optional --dt): minimal residual, its row distribution, constrained stationarity, B_3.
- s3g_section.py, s3g_compare.py   the prescribed-data test (S3 (g)) prescribed-data test (Legendre coefficients of the trace on x = x* - 1, y in [0.5, 3];
                                cheapest data direction from G = (T J^-1)(T J^-1)^T); cross-grid overlaps / principal angles.
- project_seed.py               project a state to another grid or domain (C kept).
- col_check.py, col_dt.py, dirtest.py   Jacobian-consistency diagnostics (columns against the residual's derivative for other
                                Npsi / dt; dt isolation; directional remainder and dt-convergence tests along smooth, cardinal,
                                Newton and soft directions).
- s4e_table.py, s3e_reading.py  the S4 (e) table over states and the S3 (e) reading over three grids.
- crossgrid_action.py           interpolate soft directions to another grid, exact actions, Ritz values (upper bounds for sigma_i).
- soft_smoothness.py            spectral resolvedness, near-P energy and axis second differences of the softest Ritz directions (4v).
- valley_s4e.py                 S4 (e) quantities at z +- s v along the softest directions (what the valley moves).
- rows_reweight.py              near-P row fractions of the stored Ritz actions and Ritz values after reweighting the rows near P (4x).
- action_location.py, chk_modes_direct.py   fresh central actions of the Ritz vectors and of generic directions with their near-P fractions (4x).
- statediff_project.py          projection of a two-state difference (grids or domains) onto the soft subspace of a Ritz file (4w (ii)).
- opchannel.py                  actions of frozen directions under dt/2, Npsi 720, tau_max 18 at a frozen state (4y).
- noise_probe.py, tauswitch_check.py   smoothness probe of the residual (old position switch vs switch-free) and validation of the schedule.
- ritz_subspace.py              exact-action Ritz values on a candidate soft subspace (matrix-softest + stored soft vectors).
- fixcl_table.py, floors_table.py   tables of fixed-c_l minima and of floors across grids / domains / systems.
Mixed-resolution inverse: Model(..., Npsi) solves the Poisson modes on Npsi + 1 radial nodes (Npsi >= 360 required for
quantitative rows; see the numerical findings section 1).

## Tests
    python3 tests/test_model.py cuda 0 ; python3 tests/test_model.py cuda 0.8
(modal Poisson ODEs vs quadrature 1e-14; identity c = int rho_1 r^-2 dr vs psi_xy(0) 1.5e-13; transport residual vs FD 4e-8;
Jacobian vs FD 1.4e-7).

## Commands used (outputs in data/)
    python3 src/run_newton.py --N 160 --M 64 --beta 0.9 --L 8 --seed x3 --tag t_n160m64b09
    python3 src/nullspace.py runs/seed_n160m64b09.npz 6 40 ; python3 src/orbit_diag.py runs/seed_n160m64b09.npz 3
    chain s3_seeds (COMMANDS.md) ; python3 src/s3f_alpha.py runs/seed_n160m64b09.npz seed_n160m64b09 10 1e-6
    python3 src/run_psi_newton.py --N 120 --M 48 --beta 0.9 --L 8 --seed x3 --tag psi5_n120m48 --far_psi --n_coll 3 --scl 400 --dt_jac 0.01 --maxit 10 --gmres 60 --gtol 1e-3
    python3 src/jac_dense.py runs/psi5_n120m48_it2.npz n120m48 32 1e-5 0.01 ; python3 src/dense_newton.py runs/J_n120m48.pt dn_n120m48 12 20
    python3 src/s4e_row.py runs/dn_n120m48.npz dn_n120m48
  session 2 (discrete system: Npsi 480, dt 0.01; Jacobians with the same dt, eps 1e-6, step cut 7.5):
    chain dense_chain2 (COMMANDS.md)            (accurate-inverse J at dn_n120m48 -> runs/J_n120m48_acc.pt; dense_newton -> runs/dn2_n120m48.npz; s4e_row)
    python3 src/svd_report.py runs/J_n120m48_acc.pt n120m48_acc 8 480
    chain chainA_n144m56 (COMMANDS.md) runs/dn2_n120m48.npz ; chain chainB_rebuild_coarse_domains (COMMANDS.md) runs/dn2_n120m48.npz
    python3 src/dirtest.py runs/J_n120m48_conv.pt n120m48_conv runs/n120m48_conv_softvecs_node_cl400.pt
    python3 src/s4e_table.py dn2_n120m48 dn_n96m40 dn_n144m56 dn_n96m40L4 dn_n96m40L16 ; python3 src/s3e_reading.py node_cl400 n96m40_conv n120m48_conv n144m56

  session 3 (smooth system, charmap.TAU_SWITCH = 7.5; see the numerical findings 6b):
    python3 src/crossgrid_action.py runs/dnSB_n120m48.npz runs/n120m48_S_softvecs_node_cl400.pt 144 56 0.9 8 n144m56_from_dnSB 10 1e-4 480
    python3 src/noise_probe.py runs/dnC_n120m48.npz runs/n120m48_final_softvecs_node_cl400.pt dnC 480 2 ; python3 src/tauswitch_check.py runs/dnC_n120m48.npz runs/n120m48_final_softvecs_node_cl400.pt dnC
    chain chainE2b_smooth (COMMANDS.md) ; chain chainF2_fixcl_smooth (COMMANDS.md) ; chain chainG_fixcl_n96 (COMMANDS.md)
    chain chainH_anatomy (COMMANDS.md) ; chain chainH2_rfar (COMMANDS.md) (IPM_RFAR=1e8) ; chain chainH3_mech (COMMANDS.md) (IPM_COLLSCALE=0.2; Npsi 720)
    python3 src/s3f_psi.py runs/J_n120m48_S_refreshed.pt runs/dnSB_n120m48.npz dnSB 480 12 ; same with runs/J_n96m40S_final_refreshed.pt runs/dnB_n96m40S.npz dnB_n96m40S
    python3 src/ritz_subspace.py runs/J_n120m48_S_refreshed.pt n120m48_S 24 runs/n120m48_S_softvecs_node_cl400.pt 1e-4 480
    python3 src/mode_anatomy.py runs/ritz_n120m48_S.pt runs/J_n120m48_S_refreshed.pt n120m48_S 3 480
    python3 src/fixcl_table.py runs/dnSB_n120m48.npz fixclS_n120m48_d0.001 ... ; python3 src/floors_table.py dnSB_n120m48:n120m48_S dnB_n96m40S:n96m40S_final

## Data (data/)
c6g_shape.npz: the published candidate X3 (md5 15f8095f7e79dbfa0c50d75e5fe8997a, copied from the first investigation's published artifacts, IPM_Setting_I.artifacts, coefficient files).
Converged states (b on the grid, c_l, C) and S4 (e) rows are added when available (runs/dn_*.npz, runs/s4e_*.json).
