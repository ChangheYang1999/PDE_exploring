# numerics artifacts (Setting B2 numerics) -- final state of the last shift (shift 8, 2026-10-22; T_end and elapsed time are recorded in
# NUM_REPORT.md sec. 9 at the end of the run). No unforced B2-P candidate was obtained. The consolidated table contains 121 forced-problem audit entries and two manufactured-control entries; repeated archive hashes occur across comparisons.

Run every command from the lane directory, which contains code/, runs/ and artifacts/ (the scripts read states from runs/ and write there);
bare filenames in the artifact inventory below refer to files in artifacts/. Conventions: a command containing <state.npz>, runs/<state>.npz,
<tag> or a square-bracketed option is a TEMPLATE (replace the placeholder by a concrete file, drop the brackets); every other command line is
executable as written from the lane directory. Software: Python 3.9, numpy 2.0, scipy 1.13, torch 2.8 (CUDA), sympy (tests only).
Final scripts are copied here from ../code at the end of each shift; the authoritative versions during the run are in
../code. Hardware requirements and runtimes depend on the script. Consolidation reads saved JSON and NPZ data using Python and NumPy.

## Scripts
- bq3core.py      basis (spline x cosine modes, two radial maps), canonical full-plane inverse (modal Green formula,
                  k = 1 once-subtracted), design operators, residuals R_F, R_G, N_F, N_G, Jacobian.
- charnewton.py   characteristic residual map (backward RK4 along W from every residual point, centre jet to second
                  order, Omega integral accumulated over the F basis), LM solver (FD Jacobian, Broyden updates,
                  CUDA-graph replay), fixed/free beta, forcing homotopy parameter eps.
- homotopy.py     driver: eps = 0 linear solve from an external Gaussian dipole, then LM at increasing eps.
- scan_eps0.py    eps = 0 scan (strain of the transported vorticity versus the external dipole).
- evalstate.py    independent-node evaluation of a state: normalized residuals |R_F|/N_F, |R_G|/N_G and absolute
                  residuals by region (points differ from the fit nodes: 9 Gauss points per interval, 2x angles).
- diagnostics.py  SPEC sec. 7 diagnostics: centre identities, far-field exponents, W.X on circles, stagnation points,
                  v0(R), odd-power content near the centre.
- transplant.py   change of basis (K, Nt, L, beta_basis, rmap) by weighted least squares on point values.
- evalpoints.py   B2-P residuals at arbitrary Cartesian points (exact modal inverse; default: the verifier's seven points).
- dump_state.py   transported vs represented fields of a characteristic state (where the mismatch sits).
- identity_check.py  checks c = Lambda + NL (NOTES_FOR_LEAD sec. 7) on eps = 0 fields.
- angspec.py      angular cosine spectrum of the transported G at eps = 0 (resolution check).
- shells.py       radial-shell decomposition of the centre strain of eps = 0 fields.
- solve.py        method 1 (collocation LM on cF, cG, beta); converges only to the polynomial gauge artifact (report sec. 3).
- test_inverse.py, test_inverse2.py  earlier manufactured inverse tests (Gaussian and algebraic tails, r map).
- test_velinterp.py  off-node velocity interpolation and divergence test of the characteristic solver.
- test_inverse3.py   manufactured-solution test of the inverse (both maps).

## Commands (examples)
    python3 code/test_inverse3.py                              # inverse tests, both maps
    python3 code/scan_eps0.py --cases "2.5,2.85,1.0" --rmap r2 --grade 1.0 --out runs/scan_eps0_r2b.json  # eps = 0 strain of the transported vorticity
    python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 40 --K 12 --beta_basis 3.0 --beta_fixed 3.0 \
        --ext_gauss "2.5,2.85,1.0" --eps_schedule "0.34,0.67,1.0" --iters 8 --broyden_every 3 --tag fb30
    python3 code/evalstate.py runs/fb30_eps0.npz               # residual table on independent nodes (the fb30 run archived its eps = 0 seed only;
    python3 code/diagnostics.py runs/fb30_eps0.npz             #  no eps = 1 state exists)

## Shift 2 additions (2026-10-20, 18:41Z onward): solver validation, Anderson continuation, fold search, gauge-fixed path
All commands run from the lane directory with CUDA available; states are .npz files in runs/ (regenerable).
- Jacobian consistency test:            python3 code/test_jac.py runs/fb30i_eps0.1.npz
- Manufactured problem, LM:             python3 code/manufactured.py --s0 runs/fb30g_eps0.npz --perturb scale,0.7 --tag man1 --iters 14
- Manufactured problem, Anderson:       python3 code/picard.py --state runs/fb30g_eps0.npz --s0 runs/fb30g_eps0.npz --perturb scale,0.7 --m 10 --mix 0.5 --iters 150 --tag man_pic1
- Compare two states (bands, axis):     python3 code/compare_states.py runs/fb30g_eps0.npz runs/man_pic1.npz
- Small-eps Anderson (eps = 0.02):      python3 code/picard.py --state runs/fb30g_eps0.npz --eps 0.02 --m 10 --mix 0.5 --iters 100 --tag pic_e002
- eps-continuation (safeguarded):       python3 code/picard_cont.py --state runs/pic_e002.npz --eps_schedule 0.04,0.06,0.08,0.1,0.13,0.16,0.2,0.25,0.3,0.35,0.4,0.5,0.6,0.7,0.8,0.9,1.0 --tag cont1 --iters 40 --mix 0.3 --m 15 --blow 5 --restart_every 12
- lambda defect-forcing path:           python3 code/picard_cont.py --state runs/fb30g_eps0.npz --s0 runs/fb30g_eps0.npz --lam_schedule 0.95,0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag lamc1 --iters 40 --mix 0.3 --m 15 --blow 5 --restart_every 12
- a0-parameterized continuation (fold): python3 code/picard_a0.py --state runs/cont1b_eps0.05.npz --a0_schedule 1.9,2.1,2.4,2.7,3,3.5,4,5,6,8,10,13,16,20,30,50 --tag a0c1 --iters 40
- gauge-fixed path (a0 fixed, beta free): python3 code/picard_beta.py --state runs/fb30g_eps0.npz --ext_gauss 2.87,1.0 --eps_schedule 0.02,0.04,0.06,0.08,0.1,0.13,0.16,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0 --tag bfree1
- eps = 0 state for a new beta:         python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 40 --K 12 --Nphi 24 --Nphi_res 12 --beta_basis 2.25 --beta_fixed 2.25 --ext_gauss 2.125,2.85,1.0 --eps_schedule 0.0 --iters 0 --tag fb225
- Diagnostics / independent-node residuals of a state: python3 code/diagnostics.py <state.npz>; python3 code/evalstate.py <state.npz>
Logs of every run quoted in NUM_REPORT.md are in runs/<tag>.log.
- Fixed-basis beta-free lambda path:         python3 code/picard_beta.py --state runs/fb30g_eps0.npz --ext_gauss 2.87,1.0 --a0 1.011631 --lam_schedule 0.99,0.98,0.97,0.96,0.95,0.94,0.93,0.92,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.5,0.4,0.3,0.2,0.1,0.05,0.0 --tag blam12g --Nphi_res 24 --fixed_basis 1
- Predictor residual of a lambda state:        python3 code/predictor_check.py runs/blam1_lambda0.97.npz 0.97 0.96 0.94
- Off-node self-check (48 angles):             python3 code/offnode_check.py runs/a0c1os_a02.1.npz --Nphi_res 48
- Stage tables from logs:                      python3 code/summarize_runs.py runs/a0c1os.log runs/bfree1os3.log

## Shift 3 additions (2026-10-21, 00:24Z onward): fixed source-velocity block (retied basis), constant-velocity diagnostic
- Fixed-source tests (cross inverse, manufactured, block interpolation):  python3 code/fixedsrc.py
- Retied-basis lambda path with the fixed source-velocity block (lead 22:53Z design; the only mode whose lambda = 0 endpoint could be a candidate):
      python3 code/picard_beta.py --state runs/fb30g_eps0.npz --ext_gauss 2.87,1.0 --a0 1.011631 --lam_schedule 0.99,0.98,0.97,0.965,0.96,0.955,0.95,0.945,0.94,0.93,0.92,0.91,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag blam12v --Nphi_res 24 --fixed_source 1
      python3 code/picard_beta.py --state runs/fb30g16_eps0.npz --ext_gauss 2.87,1.0 --a0 1.011258 --lam_schedule 0.99,0.98,0.97,0.965,0.96,0.955,0.95,0.945,0.94,0.93,0.92,0.91,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag blam16v --Nphi_res 32 --fixed_source 1
  (--fixed_basis 1 is the superseded DIAGNOSTIC mode: representation exponent frozen at the seed's; its states cannot be candidates.)
  Restart from a saved stage: --state runs/blam16v_lambda0.965.npz (the stored seed source cG_f and beta_seed are reused).
- Equivalence test at beta = beta_seed (3 inner iterations, both modes must agree): add --max_secant 1 --iters 3 to the two commands above with --fixed_basis 1 / --fixed_source 1.
- Constant far-field velocity C2 (FINAL_REPORT 4.26(b); 2 < beta_basis < 3; a retied candidate needs C2 = 0):  python3 code/constvel.py <state.npz> (template; optional arguments are listed in the script header)
  (also reported by diagnostics.py as const_velocity_C2). Cross-checked with the verifier's packet-93 formula on runs/bfree1os3_eps0.025/0.03/0.035.npz.
Seeds for regeneration: runs/fb30g_eps0.npz (K 12) and runs/fb30g16_eps0.npz (K 16) are produced by
      python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 40 --K 12 --Nphi 24 --Nphi_res 24 --beta_basis 3.0 --beta_fixed 3.0 --ext_gauss 2.5,2.87,1.0 --eps_schedule 0.0 --iters 0 --tag fb30g
  (K 16: --Nt 56 --K 16 --Nphi 32 --Nphi_res 32 --tag fb30g16); copies are kept in artifacts/ when under the size budget.
- Angular refinement along the lambda path (K 16 -> 24 -> 32; the seed source K16/Nt56 stays in its own basis via seed_* metadata):
      python3 code/transplant.py runs/blam16v_lambda0.965.npz runs/blam24v_start.npz --K 24 --Nphi 48
      python3 code/picard_beta.py --state runs/blam24v_start.npz --ext_gauss 2.87,1.0 --a0 1.011258 --lam_schedule 0.96,0.955,0.95,0.945,0.94,0.935,0.93,0.92,0.91,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag blam24v --Nphi_res 48 --fixed_source 1
      python3 code/transplant.py runs/blam24v_lambda0.955.npz runs/blam32v_start.npz --K 32 --Nphi 64
      python3 code/picard_beta.py --state runs/blam32v_start.npz --ext_gauss 2.87,1.0 --a0 1.011258 --lam_schedule 0.95,0.945,0.94,0.935,0.93,0.925,0.92,0.91,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag blam32v --Nphi_res 64 --fixed_source 1
- Per-stage diagnostics of a lambda state: exact axis transport check and asymptotic axis slopes Q_+-:  python3 code/axis_ode.py <state.npz> --rmax 1e8 --n 60
  far-field transported-vs-represented mismatch by band and angular profiles:                         python3 code/transported_tail.py <state.npz> --Nphi_res 96
  constant far-field velocity C2 (noninteger beta in (2,4)):                                           python3 code/constvel.py <state.npz>
  forced transport field W_lambda (axis zeros, inward flow, near-stagnation points):                   python3 code/wfield_check.py <state.npz> --lams 0.9,0.5,0
- Controlled resolution comparison at one lambda (K 24 / 32 / 40 at lambda 0.95):  python3 code/compare_K.py runs/blam24v_lambda0.95.npz runs/blam32v_lambda0.95.npz runs/blam40v95_lambda0.95.npz
  (K 40 stage at fixed lambda: python3 code/transplant.py runs/blam32v_lambda0.95.npz runs/blam40v95_start.npz --K 40 --Nphi 80; python3 code/picard_beta.py --state runs/blam40v95_start.npz --ext_gauss 2.87,1.0 --a0 1.011258 --lam_schedule 0.95 --tag blam40v95 --Nphi_res 80 --tol_m 1e-5 --fixed_source 1)

Shift 4 additions (2026-10-21, from 06:18Z):
- Upper-axis transition diagnostic (lead 03:25Z item 2): python3 code/axis_drop.py runs/blam40v_lambda0.94.npz --Nphi_res 360 --radii 1e2,1e4,2.3e5 > runs/drop_blam40v_lambda0.94.json
  (a_pl, 90/10 percent angles, width w, axis slope proxy q(r), S = w q / a_pl; transported and represented fields; table of lineage 1 in
  drop_table_lineage1.txt, raw JSON runs/drop_<state>.json).
- Beta-parameterized continuation (beta fixed per stage, lambda the secant unknown; passes a fold in lambda; acceptance test disabled for exploration):
      python3 code/picard_lam.py --state runs/blam32v_lambda0.945.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.023855,3.0315,3.040,3.050,3.062,3.076,3.092,3.11,3.13,3.16 --tag blamB32 --Nphi_res 64 --fixed_source 1 --tol_m 5e-5 --accept_factor 1e9 --dlam 0.003 > runs/blamB32.out 2>&1
      (the archived run is the restart of 06:50:11Z; an earlier attempt with a longer schedule was stopped)
  States runs/blamB32_beta<b>.npz (param = 'beta', lam = the solved lambda).
- Second lineage (lead 03:25Z item 3): seed python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 56 --K 24 --Nphi 48 --Nphi_res 48 --beta_basis 3.0 --beta_fixed 3.0 --ext_gauss 2.5,2.5,1.0 --eps_schedule 0.0 --iters 0 --tag fb30y25g24
  then python3 code/picard_beta.py --state runs/fb30y25g24_eps0_a01.npz --ext_gauss 2.5,1.0 --a0 1.0 --lam_schedule 0.99,0.98,0.97,0.965,0.96,0.955,0.95,0.945,0.94,0.935,0.93,0.92,0.91,0.9 --tag blamL2k24 --Nphi_res 48 --fixed_source 1 --tol_m 5e-5 > runs/blamL2k24.out 2>&1
  (the archived run of 06:50:31Z, seed rescaled to a0 = 1; the a0 4.332010 attempt of 06:41Z was abandoned)
- Per-stage one-line summary (runs axis_ode / axis_drop / constvel if their outputs are missing): python3 code/stage_diag.py runs/<state>.npz
- Comparison of (lambda, Q_R) along the beta-parameterized path with the lead's pre-registered fits at lambda 0.935/0.93/0.925: python3 code/predict_compare.py
- Consolidated independent residual tables from the verifier's audits (read-only on verification): python3 code/consolidate_audits.py
  (it writes artifacts/consolidated_residuals.md and artifacts/consolidated_residuals.csv)
- Tables of this shift: drop_table_lineage1.txt (a_pl, w, q, S per stage), outer_trace_table.txt (a at fixed angles from the upper axis), collapse_table.txt
  (rescaled profiles), m_beta_table.txt (reduced strain-mismatch sensitivity per stage).
- Lineage comparison (lineage 1 vs blamL2k24 at equal lambda, normalized by a0^(1/beta)): python3 code/compare_lineages.py blamL2k24
- K 40 checkpoint of the beta-parameterized path: python3 code/picard_lam.py --state runs/blam40v_lambda0.94.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.0315,3.04 --tag blamB40chk --Nphi_res 80 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.002

Shift 5 additions (2026-10-21, from 12:11Z):
- Lineage 2 in the beta parameterization (K 24; every converged secant evaluation saved as ..._sec<k>.npz):
      python3 code/picard_lam.py --state runs/blamL2k24_lambda0.99.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.088,3.09 --tag blamL2B24 --Nphi_res 48 --fixed_source 1 --tol_m 2e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1
      python3 code/picard_lam.py --state runs/blamL2B24_beta3.09.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.0925,3.095,3.10,3.105,3.11,3.12,3.14,3.17,3.2,3.25,3.3 --tag blamL2B24b --Nphi_res 48 --fixed_source 1 --tol_m 2e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1
- Field continuity between consecutive saved stages on a common physical grid (fold2 protocol; stored F, G via bq3core.fields_at):
      python3 code/field_continuity.py runs/blamL2B24_beta3.088.npz runs/blamL2B24_beta3.09.npz runs/blamL2B24b_beta3.0925.npz runs/blamL2B24b_beta3.095.npz runs/blamL2B24b_beta3.1.npz runs/blamL2B24b_beta3.105.npz runs/blamL2B24b_beta3.11.npz runs/blamL2B24b_beta3.12.npz --json runs/fieldcont_L2B24.json
- K 32 refinement around the lineage-2 turn: python3 code/transplant.py runs/blamL2B24b_beta3.0925.npz runs/blamL2B32_start.npz --K 32 --Nphi 64
      python3 code/picard_lam.py --state runs/blamL2B32_start.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.0925,3.085,3.10,3.11 --tag blamL2B32f --Nphi_res 64 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1
- Left side of the lineage-2 lambda(beta) map at tighter tolerance:
      python3 code/picard_lam.py --state runs/blamL2B24_beta3.088.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.0865,3.085,3.083,3.08,3.076,3.072,3.066,3.06,3.05,3.04,3.02,3.0,2.95,2.9 --tag blamL2B24L --Nphi_res 48 --fixed_source 1 --tol_m 5e-6 --accept_factor 1e9 --dlam 0.0005 --save_secants 1
- Separate elliptic-inversion error E = -Lap Psi - Omega of the modal inverse (Psi_k'' by Richardson finite differences of the cross-inverse Psi_k',
  not by the modal ODE; mode-wise ratio |E_k| / N_k and absolute maxima by radial band): python3 code/elliptic_error.py runs/<state>.npz [--json runs/ellip_<state>.json]

Software and code versions (recorded 2026-10-21T13:47Z): python 3.9.25, torch 2.8.0+cu128 (CUDA 12.8), numpy 2.0.2, scipy 1.13.1, one NVIDIA A100-SXM4-80GB
shared with the verifier lane; OMP_NUM_THREADS=1. code_sha256.txt covers all current code/*.py files, including backups and tests. Later continuation archives (runs/*.npz) contain the hashes of
the code files that produced them (key code_sha256) and of their start state (start_sha256); the early seeds fb30g_eps0.npz and fb30g16_eps0.npz do not.
- Direct measurement of the reduced mismatch at the lineage-2 vertex lambda (nondegeneracy; one inner solve per beta, no outer secant):
      python3 code/picard_beta.py --state runs/blamL2B24b_beta3.0925.npz --ext_gauss 2.5,1.0 --a0 1.0 --lam_schedule 0.989973 --max_secant 1 --Nphi_res 48 --fixed_source 1 --tol_m 5e-5 --tol_f 1e-5 --iters 60 --beta0 3.0852 --tag mbb_b3.0852 > runs/mbb_b3.0852.out 2>&1
      python3 code/picard_beta.py --state runs/blamL2B24b_beta3.0925.npz --ext_gauss 2.5,1.0 --a0 1.0 --lam_schedule 0.989973 --max_secant 1 --Nphi_res 48 --fixed_source 1 --tol_m 5e-5 --tol_f 1e-5 --iters 60 --beta0 3.0952 --tag mbb_b3.0952 > runs/mbb_b3.0952.out 2>&1
      python3 code/picard_beta.py --state runs/blamL2B24b_beta3.0925.npz --ext_gauss 2.5,1.0 --a0 1.0 --lam_schedule 0.989973 --max_secant 1 --Nphi_res 48 --fixed_source 1 --tol_m 5e-5 --tol_f 1e-5 --iters 60 --beta0 3.1052 --tag mbb_b3.1052 > runs/mbb_b3.1052.out 2>&1
  (scripts runs/mbb_scan.sh, runs/mbb_scan2.sh; results runs/mbb_b<beta>.out: m = -1.592e-4, +5.2e-6, -1.516e-4 -> m_beta_beta = -3.21 +- 0.08, m_beta = 3.8e-4).
- K 40 fate stages of lineage 1 (shift 5): python3 code/picard_lam.py --state runs/blamB40chk_beta3.04.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.05,3.062,3.076,3.092 --tag blamB40ext --Nphi_res 80 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.002 --save_secants 1
- Queue helper used in shift 5 (bash, launches the next detached run when the previous exits; not needed for reproduction): code/queue_watcher.sh

## Shift 6 additions (2026-10-21, 18:00Z onward): the prompt's remaining verification items on the forced states (NUM_REPORT 7m)
- Off-axis stagnation search (grid of |W|/(beta r), Newton refinement of qualifying minima, axis sign changes, W.X by band):
      python3 code/stagnation_search.py runs/mbb_b3.0952_lambda0.989973.npz --out runs/stag_L2v.json
      (the variant --unforced 1 searches the unforced field W = beta X + U_rel[Omega])
- Symbolic reconstruction audit (sympy only; moving centre, material-centre condition, translation equivalence, scaling family, centre identities):
      python3 code/reconstruction_audit.py > runs/reconstruction_audit.txt
- Far-field next-order asymptotics (exact endpoint coefficients vs the PDE relations; window fits; lambda-path mixed terms subtracted):
      python3 code/farfield_nextorder.py runs/a0c1hr2os_a02.4.npz --out runs/ffno_F_hr2os_2.4.json
- FD Jacobian / conditioning of the inner fixed-point map and the continuation Jacobian at a lambda-path state (3 h on the GPU for K 24):
      python3 code/jacobian_fp.py --state runs/mbb_b3.0952_lambda0.989973.npz --ext_gauss 2.5,1.0 --tag L2v --batch 16 --h 1e-6
      (--timing_only 1 runs a timing test instead)
- Equal-budget comparison K 24/32/40 (same seed, same (beta, lambda), 20 inner iterations each, exits disabled): bash code/eqb.sh (also in runs/ and artifacts/; the script lists the three commands)
- Map-scale test (re-projection to another L, then one inner solve at fixed beta and lambda):
      python3 code/transplant.py runs/mbb_b3.0952_lambda0.989973.npz runs/L2v_L1.0.npz --L 1.0
      python3 code/picard_lam.py --state runs/L2v_L1.0.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.0952 --lam0 0.989973 --max_secant 1 --tag mapL2v_L1.0 --Nphi_res 48 --fixed_source 1 --tol_m 1e-9 --iters 25 --tol_f 1e-5 --tol_obj 1e-5 > runs/mapL2v_L1.0.out 2>&1
Outputs quoted in NUM_REPORT 7m: runs/stag_*.json, runs/reconstruction_audit.txt, runs/ffno_*.json, runs/jac_L2v.{log,json}, runs/eqb*.log, runs/mapL2v_*.out
(copied here at the end of the run as far as the 30 MB limit allows; the Jacobian matrix itself (13 MB) stays in runs/).
- Post-processing of a saved Jacobian (corrected scaling direction, field-metric singular values): python3 code/jac_post.py --state runs/mbb_b3.0952_lambda0.989973.npz --ext_gauss 2.5,1.0 --jac runs/jac_L2v.npz --tag L2v
- Augmented continuation matrices from a saved Jacobian (CPU): OMP_NUM_THREADS=1 python3 code/jac_augmented.py runs/jac_L2v.npz --c_f 1.9229006858248248 --out runs/jacaug_L2v.json
- Equal-budget per-iteration table: python3 code/eqb_table.py runs/eqb24.log runs/eqb32.log runs/eqb40.log > artifacts/eqb_table.txt
  (eqb_table.txt is the script's output as of 08:08Z; the earlier copy carried a hand-written clarification of the K 32 line, 'within 5 percent
  first at iteration 13 and continuously over 16-19 (iteration 15 is 7.8 percent above)', which now lives in NUM_REPORT 7m (iii) only)
Shift-6 outputs copied here: stag_*.json, ffno_*.json, jac_L2v.json, jacpost_L2v.json, jacaug_L2v.json, eqb*.log, eqb_table.txt, reconstruction_audit.txt.

## Shift 7 additions (2026-10-22, 00:00Z onward): sign-changing eps = 0 scan, J2 (NUM_REPORT 7n, 7m (ii)(g))
- scan_eps0_signed.py: eps = 0 scan (sec. 5 of NUM_REPORT) with a SIGNED sum of Gaussian lobes, case syntax 'cin|a1,y1,s1|a2,y2,s2|...'
  (a1 = +1 by convention, A fixed by c_in). Outputs c_out, the sign structure of the transported G, unfinished trajectories.
  Exact commands (one case per command, K 16, Nt 40; about 35 s each on the shared GPU):
    python3 code/scan_eps0_signed.py --K 16 --Nt 40 --cases "2.5|1,2.85,1.0;2.5|1,1.5,1.0" --out runs/scan_signed_control.json
    python3 code/scan_eps0_signed.py --K 16 --Nt 40 --cases "2.5|1,2.87,1.0|-0.5,-2.0,1.0" --out runs/scan_signed_01.json
    (and likewise for the cases listed in scan_signed_table.md; scan_signed_09 used --max_steps 1500)
- scan_signed_table.py: collects runs/scan_signed_*.json into scan_signed_table.md (the table of NUM_REPORT 7n): python3 code/scan_signed_table.py > artifacts/scan_signed_table.md
- scan_signed_*.json, scan_signed_table.md: the 21 cases (two single-lobe controls, 18 sign-changing sources incl. two at c_in 2.2 and 3.0 and the a_2 = -0.03 bracket y0 2.87-3.5, one sign-definite two-lobe control).
- blamL2B40.out: K 40 check of the lineage-2 vertex (NUM_REPORT 7l 'THIRD ANGULAR RESOLUTION K 40'). Commands:
    python3 code/transplant.py runs/blamL2B32f_beta3.0925.npz runs/blamL2B40_start.npz --K 40 --Nphi 80
    python3 code/picard_lam.py --state runs/blamL2B40_start.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.0925,3.085,3.10 --tag blamL2B40 --Nphi_res 80 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1 > runs/blamL2B40.out 2>&1
    python3 code/picard_lam.py --state runs/blamL2B40_beta3.1.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.11,3.076 --tag blamL2B40b --Nphi_res 80 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1 > runs/blamL2B40b.out 2>&1
  (blamL2B40b.out: the K 40 stages at 3.11 and 3.076.)
- blamL2B48.out: K 48 (fourth angular resolution) check of the lineage-2 vertex segment (7l 'FOURTH ANGULAR RESOLUTION K 48'):
    python3 code/transplant.py runs/blamL2B40_beta3.085.npz runs/blamL2B48_start.npz --K 48 --Nphi 96
    python3 code/picard_lam.py --state runs/blamL2B48_start.npz --ext_gauss 2.5,1.0 --a0 1.0 --beta_schedule 3.085,3.10 --tag blamL2B48 --Nphi_res 96 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.001 --save_secants 1 > runs/blamL2B48.out 2>&1
- ell_/stag_/ffno_L2K40_b3085.json: elliptic error, stagnation search and far-field next-order check of runs/blamL2B40_beta3.085.npz (same tools as the shift-6 diagnostics).
- blamB48ext.out (and blamB48ext2.out if present): K 48 stages of the lineage-1 fate run (7l, lineage-1 fate table; shift 7):
    python3 code/transplant.py runs/blamB40ext_beta3.076.npz runs/blamB48ext_start.npz --K 48 --Nphi 96
    python3 code/picard_lam.py --state runs/blamB48ext_start.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.076,3.092 --tag blamB48ext --Nphi_res 96 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.002 --save_secants 1 > runs/blamB48ext.out 2>&1
    python3 code/picard_lam.py --state runs/blamB48ext_beta3.092.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.076,3.062 --tag blamB48ext2 --Nphi_res 96 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.002 --save_secants 1 > runs/blamB48ext2.out 2>&1
- Per-stage diagnostics of the K 48 lineage-1 states (Q_R, a_pl, w, q, S, C2 for the 7l fate table): python3 code/stage_diag.py runs/blamB48ext_beta3.092.npz (and _beta3.076.npz); outputs runs/axis_*.json, runs/drop_*.json, runs/constvel_*.txt.
- ell_L1K48_b3092.json, ell_blamB40ext_beta3.092.json, ell_blamB40ext_beta3.076.json, ell_blamB48ext2_beta3.062.json, ell_blamB32_beta3.062.json, stag_L1K48_b3092.json: elliptic inversion diagnostic and stagnation search on the lineage-1 fate states (7l 'ELLIPTIC-ERROR CAVEAT'; sec. 8 item 2): python3 code/elliptic_error.py runs/<state>.npz --json runs/ell_<tag>.json; python3 code/stagnation_search.py runs/<state>.npz --out runs/stag_<tag>.json.
- quad_order_check.py, quad_*.json: far-field velocity sensitivity of the modal Green inverse to its Gaussian quadrature order (12 vs 48 points) for the fate states and the lineage-2 K 40 state (7l 'ELLIPTIC-ERROR CAVEAT', sec. 8 item 2): python3 code/quad_order_check.py runs/<state>.npz --ng 48 --out runs/quad_<tag>.json

## Shift 8 additions (2026-10-22, 05:19Z onward): quadrature-order check of the modal Green inverse, FINAL_REPORT 6.1 consistency check (NUM_REPORT 7l 'QUANTIFICATION', sec. 8 item 2, sec. 6)
- picard_lam.py: new flag --ng_quad N (Gauss points per radial quadrature cell of the modal Green inverse; default 12 = every earlier run; applied
  to the unknown's Basis and to the seed Basis of the fixed source block). The quadrature order is recorded in the run log, not in the npz.
- quad_chain.sh (SUPERSEDED: its lineage-2 line carries the lineage-1 forcing and amplitude; it was stopped after its first job), quad_chain2.sh
  (the corrected chain actually used), quad_chain2.log, quadB32.out, quadB40_3092.out, quadB48_3092.out, quadB48_3062.out, quadB40_3076.out,
  quadL2B40_3085.out: re-solves of stored stages with --ng_quad 48 and otherwise the original flags (inherited lambda accepted at secant 0 in
  every case). Exact command (K 32 example; the others differ in the state file, beta, --Nphi_res 80 / 96 and, for lineage 2, --ext_gauss 2.5,1.0 --a0 1.0):
    python3 code/picard_lam.py --state runs/blamB32_beta3.062.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.062 --tag quadB32 --Nphi_res 64 --fixed_source 1 --tol_m 1e-5 --accept_factor 1e9 --dlam 0.002 --save_secants 1 --ng_quad 48 > runs/quadB32.out 2>&1
- runtime_vel_quad.py, rtvel_*.json, rtvel_table.txt: sensitivity of the solver's RUNTIME velocity (CharResidual.prepare + velocity on the frozen
  archived coefficients, fixed source block rebuilt at the same order) to the quadrature order, on half circles r 1e2-1e9 (181 angles):
    python3 code/runtime_vel_quad.py runs/blamB48ext_beta3.092.npz --ng 48 --out runs/rtvel_K48_b3092.json
  (quad_order_check.py, shift 7, evaluates the DIRECT Green formula instead; the runtime interpolant amplifies the perturbation at large radii.)
- fr61e_check_0550.txt, state_inventory_0545.txt: consistency check of the lead's FINAL_REPORT Table 6.1e (87 rows) against the archived npz
  metadata (beta, lambda / eps, K, a0, acceptance flag); no discrepancy. The command python3 code/state_inventory.py > runs/state_inventory.txt regenerates the current 96-state inventory
  (state_inventory.txt); state_inventory_0545.txt is a historical 88-state inventory written 05:30Z whose exact regeneration recipe is not
  supplied, and fr61e_check_0550.txt is the historical per-row log (check_fr61e.py reproduces its verdict, not its format).
- code_sha256.txt refreshed 05:46Z (picard_lam.py changed by the flag; default behaviour unchanged).
- quad_root_chain.sh, quad_root_chain.log, quadroot12_B32.out, quadroot48_B32.out: roots lambda(beta = 3.062) at K 32 DETERMINED independently
  with 12 and 48 Gauss points (start 0.93171, tol_m 1e-7, tol_f 3e-6; 7l 'DETERMINED ROOTS'): lambda_12 = 0.931683766, lambda_48 = 0.931683784.
    python3 code/picard_lam.py --state runs/blamB32_beta3.062.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.062 --tag quadroot48_B32 --Nphi_res 64 --fixed_source 1 --tol_m 1e-7 --tol_f 3e-6 --iters 60 --max_secant 6 --accept_factor 1e9 --lam0 0.93171 --dlam 0.0001 --save_secants 1 --ng_quad 48 > runs/quadroot48_B32.out 2>&1
- runtime_vel_quad.py now takes --ng_ref (reference order, default 12); rtvel_K48_b3092_ng12_24.json and _ng24_48.json: 12-vs-24 and 24-vs-48
  comparisons for the K 48 3.092 state (7l 'QUADRATURE CONVERGENCE OF THE RUNTIME VELOCITY'):
    python3 code/runtime_vel_quad.py runs/blamB48ext_beta3.092.npz --ng_ref 24 --ng 48 --out runs/rtvel_K48_b3092_ng24_48.json
- code_sha256.txt refreshed 06:28Z.
- apply_referee_edits.py: applies 'Quoted / Replacement' pairs of an astra referee answer to NUM_REPORT.md with whitespace-insensitive
  matching (used 06:45-06:57Z for the stale-assertion scans astra/shift8e and shift8f; dry run by default, --apply to write).
- consolidate_audits.py (updated 07:20Z): now also reads the verifier's later audits under verification/research/<packet>/verification/
  REGIONAL_RESIDUALS.json (K 48 lineage-1 states, K 40 / K 48 lineage-2 states, equal-budget and map-scale re-solves, six 48-point quadrature restarts and the two tighter secant states computed at 12 and 48 points), maps the diagnostic labels to runs/ archives, and labels the new families EQ, MS, Q. consolidated_residuals.md /
  .csv regenerated: 123 audit entries (121 forced-problem states + 2 manufactured controls), 5904 rows; the earlier 95 states' rows are unchanged.
    python3 code/consolidate_audits.py
- check_fr61e.py: consistency check of the lead's FINAL_REPORT Table 6.1e (beta, lambda / eps, K, a0, acceptance flag of every row) against the
  archived states in runs/ (name map for the lead's labels; homotopy rows matched by beta / eps / a0 / K): python3 code/check_fr61e.py runs/FR_snapshot_0530.md (the 05:30Z snapshot of the lead's
  report, 87 rows; without the argument the script reads the lead's current FINAL_REPORT.md)
- verifier/: the verifier lane's audit inputs needed by consolidate_audits.py (regional_inventory_20261021T035630Z.json and every
  REGIONAL_RESIDUALS.json under verification/<audit>/ and research/<packet>/verification/, plus the 61 frozen state archives the inventory
  points to; same relative layout as the verifier lane; 5.3 MB).
  consolidate_audits.py now reads them from artifacts/verifier/ by default (environment variable BQ3_VER overrides); the state archives it joins
  are stored under artifacts/verifier/ and runs/. Both directories are inputs to the reconstruction. Regenerating from the lane directory: python3 code/consolidate_audits.py  (123 audit entries, 5904 rows; checked 07:58Z).
- state_inventory.py, state_inventory.txt: inventory of the archived continuation states (beta, lambda, K, Nt, Nphi, a0, acceptance flag,
  beta_basis): python3 code/state_inventory.py > runs/state_inventory.txt
- README repairs of 07:55-08:00Z after the astra reproducibility audit (astra/shift8k/answer.md): every quoted executable command now has its complete
  schedule (from the run logs) and output capture (template lines with placeholders are marked by the Conventions paragraph); working-directory instruction; missing inputs replaced (fb30_eps0, blam16v_lambda0.965);
  lineage-2 command corrected to the archived run (a0 = 1 seed); quad_chain.sh marked superseded; provenance wording corrected.
- code_sha256.txt refreshed 07:58Z; its paths are relative to code/. At the verifier's 08:20Z read, all 66 records matched that directory, 55 also had matching copies in artifacts/, and 11 did not have artifact copies. This is a code-directory inventory, not a complete artifact-file manifest.
