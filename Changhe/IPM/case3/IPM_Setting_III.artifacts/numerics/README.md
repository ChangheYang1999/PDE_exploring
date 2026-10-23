# Numerics of IPM Setting III (y-leading branch): file index

All paths relative to this folder.  Python 3.9, numpy, scipy, torch (CUDA optional: pass device 'cpu' in the scripts
by editing `dev = 'cuda'`).  Every script writes a timestamped log into `runs/` (create it: `mkdir -p runs`).

Note for the published folder: the run logs (`*.log`, `*.out`), the batch launch scripts (`launch/`) and the referee
question and answer files mentioned below are not included; the commands below and the scripts in `src/` are. Where
this index refers to the numerics report of the run, the corresponding statements are in Section 4 of the published
report.

## Code
- `src/ipm3.py`     discretisation (compactified Chebyshev-Radau x quadrant trig grid), canonical modal Green-function
                    inverse, residual E, exact linearisation, dense Jacobian, Newton (plain / defect / forced modes),
                    off-grid evaluator (rho, grad rho, U, psi, R, N_f, N_v), regrid.
- `src/ipm3q.py`    smooth-by-construction representation with mode-dependent collocation (NUM_REPORT 4J); calibrated against sheet 1.
- `src/smooth_constraints.py`   smoothness imposed by Taylor-coefficient constraints, GN/LM (NUM_REPORT 4I).
- `src/ipm3s.py`    alternative smooth-centre representation (r^2-analytic map, sigma^k beta_k modes); inverse validated,
                    centre unknowns ill-conditioned; not used for results.
- `src/scan_forced.py`, `src/scan_beta.py`   forced continuation mu(c_l) at fixed gauge and mu(beta) at fixed c_l (sheet 1).
- `src/multistart_forced.py`, `src/multistart_broad.py`   multistart searches for further forced sheets.
- `src/sheet2.py`, `src/sheet2_root.py`, `src/refine_fixed.py`   sheet-2 continuation, root-finding, refinement tests.
- `src/sheet1_table.py`   converged table of mu(c_l, beta) on sheet 1.
- `src/release_cl.py`, `src/resstudy2.py`, `src/valley_chain.py`, `src/orbit_test.py`   valley (unforced) states and their
                    resolution / scaling tests.
- `src/offgrid_check.py`, `src/origin_fit.py`, `src/inspect_state.py`, `src/identity_checks.py`   diagnostics of saved
                    states (between-node residuals, near-origin slopes, strain formula (I1), weighted identity (I5'), T1).
- `src/charac.py`   second method: backward characteristics to the source, eta = lim e^tau y(tau), D = rho - a0 eta.
- `src/multistart_save.py`, `src/multistart_rich.py`, `src/sheet_from_guess.py`, `src/sheet_cont.py`,
  `src/rescale_state.py`   sheet searches (with refinement-invariance filter), continuation, canonical rescaling.
- `src/manufactured_test.py`, `src/manufactured_sheet.py`, `src/manufactured_refine.py`   methodology validation on a
                    planted smooth solution (NUM_REPORT 4C).
- `src/valley_converge.py`   converge valley states and measure their centre exponent.
- `src/y3branch.py`   exploratory Gauss-Newton solver for the secondary (pure y^3) branch (NUM_REPORT 4E).
- `src/t2_check.py`   quartic harmonic datum H = int s^-3 f_2 and the cubic relations (T1), (T2).
- `src/residual_table.py`   residual tables (PROMPT section 6 format) for saved forced states (NUM_REPORT 4F).
- `src/weighted_smin.py`, `src/gram_smin.py`   weighted-norm conditioning attempts (unreliable, NUM_REPORT 4.5).
- `src/manufactured_fixed.py`, `src/manufactured_scaled.py`   planted test with a fixed continuum source / scaled family.
- `src/arclength_beta.py`   pseudo-arclength continuation of a forced sheet in beta.
- `src/eps_continuation.py`   large-beta limit of sheet 1 in the fixed-amplitude picture (forcing width eps -> 0; NUM_REPORT 4G).
- `src/nonsmooth_term.py`   unforced solve with an explicit C s^(d-1) origin term (weaker-class exploration, 4G.1).
- `src/q_free.py`   free-c_l least-squares releases in the smooth Q basis with the radial map REBUILT from c_l at every step (NUM_REPORT 4K(c));
                    options `clmin=`, `L=` (outer map scale), `fixcl=` (fixed-c_l least-squares refinement, 4L(c)), secondary branch via q_y3.py.
- `src/q_survey.py` free-c_l survey from a grid of starts (c_l, a0) (NUM_REPORT 4M).   `src/q_y3.py` secondary y^3-leading branch (exploratory, 4N).
- `src/qdiag.py`    diagnostics of a saved state (between-node residual tables with maximizing coordinates, G6 energy margins, Theta0 data,
                    strain moment from the evaluated rho, x-axis functions, zeros of W) (NUM_REPORT 4L(b)).
- `src/drift_table.py`   drift tables (step, c_l, a0, a0/D, |F|) from the per-step logs of q_free runs (4L(a)).
- `src/farfield_check.py`   numerical check of the far-field two-term expansion with Theta1 from the analytic formula (4L(b4)).
- `src/manifest.py`   writes MANIFEST_STATES.md (one line per saved state: sha256 id, file, representation, N x M, c_l, a0, mu, map power, L, Lf, gauge, report row).
- `src/jets.py`       origin jets b, e, q1, q2 (validated by the Poisson relation), sup|grad rho|/|a0| and max_th |S|_op(r) on a dense set (4L(c9)-(c11)).
- `src/eta3.py`       windowed third-derivative residual ratio eta_3 = ||D^3 R||_2/||D^3 rho||_2 (FD stencils on the evaluated fields) (NUM_REPORT 4L(h)).
- `src/q_free.py` regrids free-state starts with `regrid_fit` (minimum-norm fit in the mode-value space; the plain coefficient regrid of ipm3s.regrid_s injects unconstrained coefficients, NUM_REPORT 4L(c8) caveat).
- `src/q_free.py` options: `fine=1 M2=<3M>` collocates the residual at M2 fine angles (angular oversampling, 4L(c6), (c8)); `snap=K` saves a snapshot every K steps.
- `MANIFEST_STATES.md`  the state manifest (regenerate with `python3 src/manifest.py > artifacts/MANIFEST_STATES.md` from the lane root).
- `launch/`         the shell batch scripts that produced runs/qfree1.out, qfree2.out, qfix1.out, survey1.out, y3.out, qdiag*.out.
- `results/`        text outputs: drift tables, far-field check, qdiag outputs for the Q and ipm3 states.
- `tests/`          manufactured tests (run each with `python3 tests/<name>.py`).

## Commands used for the numbers in NUM_REPORT.md (from the lane root, with `src/` and `runs/` present)
    python3 tests/test_basic.py; python3 tests/test_poisson.py; python3 tests/test_fields.py; python3 tests/test_forced_jac.py
    python3 src/scan_forced.py 48 12 1.0 forced48_inf 1.1,1.2,1.35,1.5,1.75,2.0,2.5,3.0,4.0,5.0 inf
    python3 src/scan_beta.py 48 12 1.0 beta48_cl2.0 2.0 0.25,0.5,1,1.5,2,3,4,6,8,12,16,24,32
    python3 src/release_cl.py runs/beta48_cl1.5_beta16.0000.pt rel_beta48_cl1.5_beta16.0000
    python3 src/offgrid_check.py runs/rel_beta48_cl1.5_beta16.0000.pt
    python3 src/origin_fit.py runs/rel_beta48_cl1.5_beta16.0000.pt
    python3 src/multistart_forced.py 48 12 ms48 1.5,2.5 4.0
    python3 src/sheet2.py 48 12 sheet2_48 4.0 2.5 16.0 0.1 2.4,2.3,2.2,2.1,2.0
    python3 src/sheet2_root.py runs/sheet2_48fine_cl2.9500.pt root_b4 48x12,48x24,72x32,96x48,144x64 4.0
    python3 src/refine_fixed.py runs/sheet2_48fine_cl2.8000.pt rf_s2_cl2.8 48x24,64x32,96x48,128x64 4.0
    python3 src/refine_fixed.py runs/forced48_inf_cl3.0000.pt rf_s1_cl3.0 48x24,64x32,96x48 1.0
    python3 src/sheet1_table.py 64 32 s1tab64 1.1,1.2,1.35,1.5,1.75,2.0,2.5,3.0,4.0,5.0,6.5,8.0 0.25,1.0,4.0,16.0,64.0
    python3 src/multistart_broad.py 48 16 msb48 1.5,2.0,2.5,3.0,4.0,5.0,6.5 1.0,4.0,16.0
    python3 src/identity_checks.py runs/res_cl1.5_N96M24.pt
    python3 src/charac.py runs/res_cl1.5_N96M24.pt runs/forced48_inf_cl3.0000.pt
    python3 src/manufactured_test.py 48 16 3.0 -0.5 manuf2; python3 src/manufactured_sheet.py 48 16 3.0 -0.5 manuf2_sheet
    python3 src/manufactured_refine.py
    python3 src/multistart_rich.py 48 16 rich_cl2_b1 2.0 1.0
    python3 src/eps_continuation.py runs/bb64_cl2_beta4.0000.pt eps_cl2 96 32 4.0 1.0,0.7,0.5,0.35,0.25,0.18,0.125,0.09,0.0625,0.045,0.03125,0.022,0.0156
    python3 src/scan_forced.py 48 16 1.0 neg48_bm1 1.2,1.35,1.5,1.75,2.0,2.5,3.0,4.0,5.0,6.5,8.0 inf -1.0 nocont -1.0
    python3 src/q_ls.py forced 3.0 96 24 2.0 1,0.5,0.25,0.125 qls_cl3.0_N96          # least-squares Q basis (NUM_REPORT 4K(a))
    python3 src/q_ls.py release runs/qls_cl3.0_N96_Lf0.25.pt qlsrel_cl3.0_N96_Lf0.25   # unforced release, c_l free (4K(b); fixed map, superseded by q_free.py)
    python3 src/q_free.py runs/qls_cl1.5_N64_Lf0.25.pt qfree_cl1.5_N64_Lf0.25 64 16 150     # rebuilt-map free-c_l release (4K(c)); data/qfree_cl1.5_N64_Lf0.25.pt is its result (QFREE64)
    python3 src/q_free.py runs/qls_cl1.5_N64_Lf0.25.pt qfix_cl1.5_N96 96 24 120 fixcl=1.5      # fixed-c_l least-squares refinement (4L(c))
    python3 src/drift_table.py runs/qfree_cl1.5_N64_Lf0.25.log                                 # drift table (4L(a))
    python3 src/qdiag.py runs/qfree_cl1.5_N64_Lf0.25.pt QFREE64                               # diagnostics (4L(b)); works on ipm3 states too
    python3 src/farfield_check.py runs/rf_s1_cl3.0_N96M48.pt                                   # far-field second term (4L(b4))
    python3 src/q_survey.py 64 16 100 survey64 1.25,1.5,2,3,4,6 1,-1,3,-3,10,-10,4A            # start-grid survey (4M)
    python3 src/q_y3.py 64 16 100 y3_64 1.5,2,3,5 1,4,-1                                       # secondary y^3 branch (4N)
    python3 src/q_free.py runs/qls_cl1.5_N64_Lf0.25.pt qfreeF_cl1.5_N64 64 16 150 fine=1 M2=48      # oversampled free release (4L(c8), QFREEF64)
    python3 src/eta3.py runs/qfree_cl1.5_N64_Lf0.25.pt 0.1 10                                      # eta_3 on the window 0.1 < r < 10 (4L(h))
    python3 src/manifest.py > artifacts/MANIFEST_STATES.md

    python3 src/scan_beta.py 96 32 1.0 betascan_cl1.25 1.25 1,2,4,8,16,32,64,128      # low-c_l sheet 1 for 4G.2
    python3 src/eps_continuation.py runs/fine48_b1_cl1.2500.pt eps_cl1.25 96 32 1.0 1.0,0.7,0.5,0.35,0.25,0.18,0.125,0.09,0.0625,0.045,0.03125,0.022,0.0156,0.011,0.0078,0.0055,0.0039
    python3 src/scan_beta.py 128 48 1.0 betascan_cl1.25c 1.25 1,2,4,8,12,16,18,20,22,24,26,28,30   # resolution check for 4G.2
    python3 src/arclength_beta.py runs/betascan_cl1.25c_beta22.0000.pt arc_cl1.25c 1.0 40 1.0        # pseudo-arclength in beta (4G.2)
    python3 src/q_calib2.py runs/bb64_cl3_beta4.0000.pt 64 16 96 24                                  # Q basis vs sheet-1 state (4K(a))
    python3 src/q_free.py runs/qls_cl1.5_N64_Lf0.25.pt qfree_cl1.5_N64_Lf0.25 64 16 150                 # free-c_l release, map rebuilt from c_l (4K(c))

## Data (`data/`)
- `forced48_inf_cl3.0000.pt`: sheet-1 forced state, c_l = 3, beta = 1, N = 48, M = 12 (mu = 1.98066).
- `rel_beta48_cl1.5_beta16.0000.pt`: valley (unforced, non-smooth) discrete solution at c_l = 1.49992, N = 48, M = 12.
- `root_b4_N48M24.pt`: the withdrawn sheet-2 root state (c_l = 3.075975, beta = 4), kept for the record.
- `qls_cl3.0_N96_Lf0.125.pt`, `qls_cl1.5_N96_Lf0.125.pt`: forced states in the least-squares Q basis (rep = 'QL'; keys beta (N+1 x M
  mode functions beta_k(t_i), b = sum_k sigma^k beta_k cos 2k theta), u (Chebyshev coefficients), cl, mu, Lf, gK); rebuild with
  `ipm3ql.IPM3QL(N, M, 1.0, gamma, Lf=Lf)` and evaluate with `IPM3QL.evaluate(beta, cl, flds, r, theta)`.
State files are torch dicts: b (N+1 x M Radau x quadrant values of b, rho = y w b), cl, gamma, N, M, L, p, [mu, beta].
Load with `torch.load`; rebuild the model with `ipm3.IPM3(N, M, L, gamma, p=p)` and evaluate with `IPM3.evaluate`.

No candidate profile is published here; see NUM_REPORT.md for the verdict (UNRESOLVED).
- Shift 3 (2026-10-21) additions, c_l = 3 fixed-c_l chain diagnostics (NUM_REPORT 4L(c13)-(c15)):
  `src/local_exponent.py` cubic jets, (T1)/(T2) checks, core scale ell_c, local exponent s(r) = dlog|1-q|/dlog r on both axes, fits
  (`python3 src/local_exponent.py runs/r1C_cl3.0_N128.pt rfit=1e-4,0.03`); `src/departure_radius.py` first radius where |s - 2| > tol
  (grid smoothing scale 3.9 L/N); `src/compare_scaled.py` comparison of states modulo the exact scaling symmetry (invariants a0, b K^3, e K^3 at
  c_l = 3; q(r) against q_ref(r/lam)); `src/compare_axis.py` pointwise axis values (rho, q, strains) of several states; `src/q_free.py` new option
  `gK=` (override of the far-field coefficient gauge; the physical amplitude is K = (1/2) L^(1-1/c_l) gK, so a true map-scale test at fixed physical K
  uses gK' = gK (L/L')^(1-1/c_l)); `launch/launch_r1b.sh` (160x40, 192x48 of the chain), `launch/launch_mapscale.sh` (restarts at L = 0.5, 2 with
  gK fixed = exact rescalings), `launch/launch_mapscale2.sh` (fixed physical K), `launch/launch_restart1.sh` (lineage test).  Results:
  `results/r1b.out`, `r1b_diag.out`, `mapscale*.out`, `locexp_cl3*.txt`, `departure_radius_cl3.txt`, `compare_scaled_cl3*.txt`, `compare_axis_cl3.txt`,
  `qdiag_N128_Lh.txt`, referee round `referee_locexp1_{question,answer}.md`.
  Also (shift 3): `src/covariance_check.py` (bit-exact scale covariance of the mapped discrete problem; residual along coefficient-space segments between
  stall points), `src/stationarity_check.py` (projection fraction ||PF||^2/||F||^2 of the truncated Gauss-Newton direction, GN step test, smallest kept
  singular values), `launch/launch_spread64.sh`, `launch_spread64b.sh`, `launch_spread_a22.sh` (restart spread at 64x16 and refinement of the a0 ~ 6A
  state, NUM_REPORT 4L(c16)), `launch/launch_y3id.sh` (secondary branch with the y^3 identity centre row, 4N); results `results/covariance_check_cl3.txt`,
  `stationarity_cl3*.txt`, `spread64*.out`, `spread64_diag.out`, `compare_scaled_spread64.txt`, `y3id.out`, referee round `referee_restart1ref_*.md`.
  Further shift-3 results: `results/taylor_resid_cl3.txt`, `resid_core_check.txt` (origin Taylor coefficients of R and the direct check), `axis_neighbourhood_cl3.txt`,
  `stream_modes_cl3.txt` (stream-mode endpoint derivatives: converged forced states 1e-15, chain 1e-5 .. 1e-4), `disagreement_radius_cl3.txt`,
  `angular_spectrum_cl3.txt`, `eta_k_cl3.txt` (when finished), `restart1*.out`, `spread_a22*.out`, `lowslope.out` (when finished), referee round
  `referee_shift3ref_*.md`.  Scripts: `src/taylor_resid.py`, `resid_core_check.py`, `axis_neighbourhood.py`, `stream_modes.py`, `disagreement_radius.py`,
  `angular_spectrum.py`, `eta_k.py`, `parse_lowslope.py`.
  `data/psic_export/<state>.json`: exact (repr float64) discrete stream modes PsiC on the Lobatto nodes, nodes tL/tR, density modes beta, map parameters and
  the SHA-256 of the source state, for independent audits of the interpolated inverse (script `src/export_psic.py`; 12 states: chain 64..192, the a0 ~ 30
  lineage at 64 and 128, forced controls at c_l = 3 and 1.5, one at c_l = 1.2).
  `results/region_maxima.txt` (script `src/region_maxima.py`): per radial bin, sampled maxima of |R|, |R|/N_f, |R|/N_v with locations for 21 states (chain,
  spread, angular/radial test), with the sample-set description and the excluded set (x-axis only); `results/lowslope_table.txt`, `supq_lowslope.txt`,
  `lowslope.out` (low-slope batch, NUM_REPORT 4L(c22)); `results/anisorefine*.out` (4L(c24)); `results/radial_projections_cl3.txt` (4L(c23)).

## Shift 4 (2026-10-21, 05:58Z-): dynamic rescaling in pseudo-time (NUM_REPORT 4O)
Code: src/dr.py (class DR: equation (DR) in the smooth Q basis, variant A with the slope normalisation and c_x = C c_w; least-squares coefficient projection
in the mode-value space; RK4 with the step from the Jacobian restricted to the visible directions; logs c, c_w, c_x, a0*, |rho_tau| on r <= 1/10/100/all
(projected derivative), centre jets, trace coefficients, b3 against the law of result 154, T_phys, a_tau/b_tau/e_tau, exterior strain moments I_1, I_10,
I_100 with the strain identity check, projection defects, sampled |R*|/N_f*, |R*|, N_f*, probes at five fixed points).  Exact test: tests/test_dr_manufactured.py
(verifier result 151 field).  Diagnostics: src/dr_table.py (matched-time tables), dr_cscan.py (C-scan drift rates), dr_vis_modes.py (visible-subspace spectra
with/without velocity feedback and eigenvector localisation), dr_modes.py, dr_compare_states.py, dr_perturb2.py, dr_transient.py, dr_linear_vs_nonlinear.py.
Commands (from the lane root):  python3 tests/test_dr_manufactured.py cuda
  python3 src/dr.py N=64 M=16 C=3.0 a0=1.0 tau_end=20 log_every=1.0 save_every=5 jac_every=1000 basis=local rcond=1e-8 tag=drY_C3.0_N64
  python3 src/dr.py N=64 M=16 C=3.0 start=runs/r1C_cl3.0_N64.pt tau_end=1.5 log_every=0.05 save_every=0.5 jac_every=100000 basis=local rcond=1e-8 tag=drW_C3.0_chain64
  python3 src/dr_vis_modes.py runs/r1C_cl3.0_N64.pt 64 16 3.0 thr=1e-6 top=5
  batches: launch/launch_dr1.sh .. launch_dr4.sh (results/ holds the logs and tables named in NUM_REPORT 4O; data/dr/ the tau = 20 constant-start states).
Note: logs drA_*/drA2_* are the first scheme (product-rule differentiation of beta_k); drV_*/drW_*/drY_* the fixed scheme (NUM_REPORT 4O(d2)); the I_R
columns of drW_* are invalid (4O(d3)).
Shift 4 additions (07:50Z): dr.py options freeze=both|U|c (frozen-velocity / frozen-rate flows, mechanism tests 4O(j4), (j4b)); src/dr_vis_lift.py (full-lift
residuals of compressed eigenpairs, 4O(h2)); src/dr_vis_refine.py (fixed-background N, M, M2 refinement, 4O(h3)); src/regauge_table.py (lead 07:10Z re-gauge
diagnostic, 4O(l)); src/dr_probes_table.py, dr_cscan.py (batch-4 tables, 4O(j)).  Referee rounds: results/referee_dr1_*.md, referee_dr2_*.md (both applied,
4O(k), (k2)).  Result files: results/drY_*, drZ_*, drF_*, dr_vis_*, dr_linear_*, regauge_*.
Reconstruction package (lead 07:40Z): artifacts/reconstruction/ (20 cited states with SHA-256, standalone loader load_state.py, run_all.sh,
RECONSTRUCTION_OUTPUT.txt with the reproduced a0, c, K, b, e and sampled residual maxima; see its README.md).
Task HS (lead 08:04Z, hydrostatic eps = 0 problem; NUM_REPORT 4P): src/hs.py (vertical-line inverse evaluator + manufactured test: python3 src/hs.py), src/hs_solve.py
(least-squares solve: python3 src/hs_solve.py N=64 M=16 c=3.0 [cfree=1] [fine=1] [start=runs/hsS_*.pt] tag=...), src/hs_start_from_chain.py (re-gauged chain
starts), src/hs_dilation_overlap.py (singular values of the residual rows in the full and visible coefficient space; dilation overlap); results
results/hs_manufactured.txt, hs_manufactured_hstep.txt (both FD step rules), hsA_summary.txt (fixed c and free c, simple start), hsBC_summary.txt (re-gauged
chain starts; oversampled rows), hsD_summary.txt (centre condition kept), hs_centre_defects.txt (single defect c + c_H - 1), hs_sampled_axis.txt (sampled
residuals with the exact y-axis included: the summaries' tables use angular midpoints only and understate the annulus by factors 3 .. 5), hs_fdstep_check.txt
(FD-step dependence: the fixed step of the hsA..hsD runs is round-off dominated where g is large, i.e. the c = 1.5 far field; option hstep=r fixes it),
hs_dilation_overlap.txt (the full-space near-null counts 0/27/247/679 are basis artefacts; visible subspace: none below 1e-13 smax, 30 .. 212 below 1e-8).
Later additions (09:00Z-09:30Z): src/hs_dilation_overlap.py, src/hs_stationarity.py (first-order stationarity of the least-squares functional at the stalls,
results/hs_stationarity.txt), src/hs_axis_exact.py (exact centre integral by the verifier's axis primitive, results/hs_axis_exact.txt: agrees with the
verifier's exact values to 1e-12), src/hs_summary.py (one-line summaries from the '# RESULT' json lines); batch 5 (results/launch_hs5.sh, hsE_*: r-scaled FD
step, results/hsE_summary.txt) and batch 6 (results/launch_hs6.sh, hsF_*: exact centre row, results/hsF_summary.txt); results/hs_centre_fd_check.txt (FD-step
dependence of the centre row).  States data/hs/*.pt (12 states; keys u, tk, basis_nodes, inverse_options incl. fd_step, map_exponent_P, tail_exponent,
map_formula, cH, centre_defect_single, cH_exact, centre_defect_exact; for free-c states rebuild the model from map_exponent_P, not from the final c).
data/hs/spectra/<tag>.npz + META.json (src/hs_export_spectra.py): residual vectors, collocation points, singular spectra (full and visible subspace), dilation
vectors and residual fractions of the 14 analysed stalls, for independent recomputation of NUM_REPORT 4P(b)(ii) and (viii).

## Shift 5 (2026-10-21, 11:48Z-): axis core constant, near-axis layer diagnostic, inner-quadrature caveat, resolved-map solves (NUM_REPORT 4P(b)(x)-(xv))
Scripts (src/): hs_m0.py (axis core constant m_0 of a saved state by the exact axis primitive K(t) = -H - J(1) + J(t), the F(y) = V_2(0, y) - Q y^p/(p(1-p))
fit, the exponent decomposition of the axis residual, the exact second axis coefficient c_2, and the independent regularised core integral
m_0 = int_0^inf [s g_xixi(0, s) - Q s^(p-1)] ds from the finite-difference g_xixi; python3 src/hs_m0.py runs/<state>.pt ... [--ymax 1e12] -> results/hs_m0.txt,
hs_m0_hsGH.txt); hs_layer.py (near-axis R_h/N_f against z = xi/y^((p+1)/2) and against the angle; contains the core-resolving inverse hydro_V_log used as the
reference inverse; python3 src/hs_layer.py runs/<state>.pt ... -> results/hs_layer.txt); hs_quadcheck.py and hs_quadtable.py (between-node far-field residual
with the default inner rule of hs.hydro_V against the resolved rule, by region; python3 src/hs_quadcheck.py [rmin=0.1] runs/<state>.pt ... then python3
src/hs_quadtable.py results/hs_quadcheck*.txt -> results/hs_quadcheck.txt, hs_quadcheck_all_part1.txt, hs_quadcheck_all_part2.txt); hs_rows.py (C_p, K, Q and
m_0 as linear row functionals of the coefficient vector; python3 src/hs_rows.py runs/<state>.pt tests them against the state values; the m_0 row is exact per
unit vector but row . u loses 7 digits by cancellation in the local coefficient basis, 4P(b)(xv)); hs_solve.py gained the options inner=log (core-resolving
inner rule in the solver maps: Gauss with 24 points on [0, min(1, y)] plus composite log-Gauss on [1, y] with n = ceil(4 log10(max_rows y)) uniform log panels per row (at least 4 per decade), 8 points each; the default
inner=gauss of all hsA..hsF states is unchanged) and extra=cp[,m0] wextra=<w>[,<w>|auto] (extra least-squares rows C_p = 0, m_0 = 0).
Runs: launch/launch_m0.sh, launch_layer.sh, launch_quadall.sh (killed after 2 states, output kept), launch_quadall2.sh, launch_hsG.sh (c = 3, inner=log,
collocated 64/96/128 and oversampled 64/96: data/hs/hsG_*.pt/.log), launch_post_hsG.sh (64 collocated rerun + quadall2), launch_hsH.sh (c = 3, inner=log,
extra row C_p = 0: data/hs/hsH_*.pt/.log).  Referee: referee/m0ref (hostile referee of the m_0 argument; its corrections are applied in 4P(b)(x)-(xi)).
Further results files of shift 5: results/hs_cp_form3.txt (C_p of all 29 saved states with the cancellation-free polar form 3 at S = 1e3 .. 1e6; the form-1
values of results/hs_cp.txt carry a cancellation error of up to 3e-4 K at S = 1e5, NUM_REPORT 4P(b)(ix)), results/hs_quadtable.txt (resolved-rule versus
default-rule regional maxima for 19 states, 4P(b)(xiii)), results/hs_m0_hsGH.txt (m_0 table of the hsG/hsH states), data/hs/hsG_* and hsH_* states (listed
with SHA-256 in MANIFEST_STATES.md).
Caveat recorded in 4P(b)(xii)-(xiii): the default inner Gauss rule of hs.hydro_V (n_in points on [0, y]) does not resolve the core t ~ 1 when y >> 1; the
far-field rows of the hsA..hsF tables are confirmed within 5 percent for the collocated c = 3 states but are evaluator-dominated for the oversampled states
(hsC 128: 2.0e-4 tabulated, 3.9e-5 resolved); use hs_layer.hydro_V_log (or n_in >= 1024) for any far-field residual below 1e-3.

## Shift 6 (2026-10-21, 17:47Z-): 192x48 and 224x56 c = 2 resolved-map states; function-space convergence test (NUM_REPORT 4P(b)(xiv), (xvi))
src/hs_cauchy.py <state.pt> <state.pt> ...: consecutive saved states evaluated at 19649 common points (401 log radii 1e-3 .. 1e7 x 49 quadrant angles incl.
both axes); max |g_a - g_b|/(1+r)^p, max |g_a - g_b|/|g_b|, max |grad(g_a - g_b)|/(1+r)^(p-1) by radial region; axis traces.  src/hs_centre_reg.py
<state.pt> ...: local cubic coefficients (G/y - 1)/y^2, (g_y(xi,0) - 1)/xi^2 at y, xi = 1e-4 .. 1 and the local log-log slope of |G/y - 1| (shows that the
exact jets E, B are attained only below the first collocation node).  Outputs: results/hs_cauchy_c2.txt, hs_cauchy_c3_hsG.txt, hs_cauchy_c3_hsE.txt,
hs_cauchy_c3_hsA.txt, hs_centre_reg_c2.txt, hs_centre_reg_c3_hsG.txt, hs_vel_cauchy_c2.txt, hs_vel_cauchy_c3_hsG.txt (src/hs_vel_cauchy.py: velocities of consecutive states from the resolved inverse), hs_common_res_c2.txt, hs_common_res_c3_hsG.txt (src/hs_common_res.py: residuals of all states on one common point set with one resolved evaluator), results/referee_cauchy1/ (referee Q/A), chain_cauchy_cl3.txt (src/chain_cauchy.py: the same function-space test on the full-problem c_l = 3 chain states r1C_cl3.0_N64..192), hs_layer_scan.txt (src/hs_layer_scan.py: centre-layer position against the first node), data/hs_points_export/ (g, grad g at the 19649 common points for the verifier; src/hs_export_points.py).  Runs: launch/launch_hsG4.sh (192x48 c = 2 -> data/hs/hsG_c2.0_N192_log.pt/.log),
launch/launch_hsG5.sh (224x56 c = 2, batch 2, maxit 55), launch/launch_post224.sh (waits for it: harvest, five-state diagnostics, then c = 2.5 96/128/160 and c = 1.5 96/128 sequences).

## Shift 7 (2026-10-21T23:45Z to 2026-10-22T05:41Z): 224x56 c = 2 state harvested; the fifth state withdraws the 'stabilisation' reading; start-dependence test (NUM_REPORT 4P(b)(xiv), (xvi) REVISION, item 13)
State data/hs/hsG_c2.0_N224_log.pt (sha256 fd0bc052...; the identical coefficient vector saved before the diagnostics is data/hs/hsG_c2.0_N224_log.raw.pt, sha256 7c5ec5f1...),
log data/hs/hsG_c2.0_N224_log.log; point export data/hs_points_export/hsG_c2.0_N224_log_points.npz (same 19649 points as the other exports).  Commands (lane root):
  python3 -u src/hs_solve.py N=224 M=56 c=2.0 hstep=r inner=log maxit=30 batch=2 tag=hsG_c2.0_N224_log          # launch/launch_hsG5.sh; 10481 s on the shared GPU
  bash runs/harvest_hs.sh hsG_c2.0_N224_log; python3 src/hs_m0.py runs/hsG_c2.0_N224_log.pt                     # results/harvest_hsG_c2_N224.txt
  F5="runs/hsG_c2.0_N96_log.pt runs/hsG_c2.0_N128_log_cont.pt runs/hsG_c2.0_N160_log.pt runs/hsG_c2.0_N192_log.pt runs/hsG_c2.0_N224_log.pt"
  python3 src/hs_cauchy.py $F5; python3 src/hs_centre_reg.py $F5; python3 src/hs_vel_cauchy.py $F5; python3 src/hs_common_res.py $F5; python3 src/hs_layer_scan.py $F5
                                                                                                                 # results/hs_{cauchy,centre_reg,vel_cauchy,common_res,layer_scan}_c2_5states.txt
Start-dependence test (src/hs_project.py, launch/launch_sd.sh): python3 src/hs_project.py <coarse.pt> N_f M_f <out.pt> projects a saved state exactly onto the
finer basis of the same c (mode values interpolated to the finer Radau nodes, then the least-squares coefficient projection; test 96 -> 128: 1.9e-8 weighted);
then hs_solve.py ... start=<out.pt> at the finer size; hs_cauchy.py compares the stall with the simple-start stall of the same size (results/hs_cauchy_sd_*.txt
when available).  launch/harvest_cdep.sh harvests the c = 2.5 / 1.5 sequences and the c = 2 C_p-row states that launch_sd.sh runs afterwards.
Shift 7 continued (02:00Z-): diagnostics prompted by referee rounds referee cauchy2 / mapq1 (results/referee_cauchy2, results/referee_mapq1):
  src/hs_node_check.py <state.pt>        : residual of a saved state AT ITS OWN COLLOCATION NODES under the independent resolved evaluator (HS_RULE=std uses the
                                            solver's standard quadrature rule instead; HS_CH = GPU chunk).  Outputs results/hs_node_check_c2_N*.txt.  Finding: the
                                            solver's standard maps (80-point tail rule) misrepresent V at far nodes near the x-axis (NUM_REPORT 4P(b)(xvi) item 14).
  src/hs_stationarity.py <state.pt>      : rebuilds the maps, computes the retained residual fraction rho_K, the exact line profile along the truncated Gauss-Newton
                                            step (acceptance-rule test), the map-error forcing b = R_ref - R_map and the first-order response d = -V_K S_K^-1 U_K^T b;
                                            exports data/hs_points_export/<tag>_nodes_maps.npz (node-level map and evaluator velocities).  results/hs_stationarity_c2_N96.txt.
  hs_solve.py options n0= per_decade= ngl= n_tail= q= : quadrature of the maps (accurate-map solves: n0=32 per_decade=10 ngl=16 n_tail=400 q=2); fine=1 oversamples
                                            the angular rows (3M angles).  States data/hs/hsQ_c2.0_N{96,128}_acc*.pt (accurate maps; the 128 simple-start and the 96
                                            from-standard-stall states are node-exact ALIASED solutions, item 14 continued).
  launch/launch_acc.sh, launch_acc2.sh, launch_acc3.sh : the chains that produced them (exact commands inside).
  src/hs_angular_scan.py <state.pt> r1 r2 ... : signed residual along the angle at fixed radii on 8M + 1 angles (sign changes, dominant cos 2k theta mode, value at the
                                            collocation angles): the aliasing signature (results/hs_angular_scan_acc128.txt: exactly M = 32 sign changes, dominant k = M).
  Referee rounds results/referee_cauchy2, referee_mapq1, referee_alias1 (questions and answers; corrections applied in NUM_REPORT (xvi-r2)-(xvi-r4)).
  launch/launch_acc4.sh (oversampled 128 with the reduced accurate rule 6x12/240 q=2 after the full rule ran out of GPU memory), launch_acc5.sh (homogeneous
  oversampled sequence 80/96/112 with the reduced rule + diagnostics), launch_acc6.sh (node check of the oversampled 128 state).  States data/hs/hsQ_c2.0_N*_acc6_fine.pt.
  Results: results/hs_cauchy_acc_fine_vs_std.txt (oversampled 96 -> oversampled 128: 4.3e-3 weighted in 1 <= r < 100; oversampled 128 vs standard 128c: 0.22),
  results/hs_cauchy_acc6_fine_seq.txt (homogeneous sequence), results/hs_node_check_c2_N*_acc6_fine.txt.
Shift 7 summary of what the hydrostatic-problem artifacts show (details NUM_REPORT 4P(b)(xiv)-(xvi)): three families of discrete trial states for the c = 2
hydrostatic problem: (1) standard-quadrature square collocation (hsG_*: 96 .. 224): node residuals 1e-7 with their own maps, but the maps are inconsistent with
the accurate inverse at the nodes (up to 5e-3 at 96, of the size of the 4e-5 .. 5e-5 plateau at 160 .. 224); consecutive function differences 0.129, 0.066, 0.0079,
0.031; (2) accurate-quadrature square collocation (hsQ_*_acc*): approximately node-exact endpoints that are angularly aliased (between-node residual 0.05 .. 0.6);
(3) accurate quadrature with 3M oversampled rows (hsQ_*_acc6_fine, 80 .. 128): members from 96 on agree to 0.2 .. 0.4 percent as functions with sampled annulus
maxima 3.2e-5, 2.4e-5, 8.0e-6 (1.0e-4 at 80), far-field maxima 7.9e-7 .. 6.7e-8 and far-field compatibility quantities at 1e-4 .. 1e-6, with a centre defect that shrinks with the size (-4.8e-3 .. -9.4e-6).  None is a
validated approximation of a continuum solution; nothing concerns the profiles of Setting III.  results/ACC_FINAL.md is the frozen record sent to the lead.

## Shift 8 (2026-10-22T05:41Z to the end of the run; scheduled cap 12:44Z): end of run; node-array exports for the checker; no new solver runs
End-of-run state: verdict UNRESOLVED, no candidate profile of Setting III, nothing excluded by numerics (NUM_REPORT section 6 (xx), the closing item).  The lead's
rule 'no new solver runs after 06:30Z' was respected; the only computation of this shift is an evaluation-only re-run of the node checks with a node-level export.
  src/hs_node_check.py: new optional environment variable HS_SAVE=<file.npz> saves all arrays at the evaluated nodes (x, y, V1, V2, g, g_xi, g_y, R_h, N_f, plus c, N, M,
  the fine flag, the rule string, the state file and its sha256, the solver's own node residual).  Commands (lane root; launch/launch_export_nodes.sh):
  HS_SAVE=artifacts/data/hs_points_export/hsG_c2.0_N160_log_nodes_resolved.npz        python3 src/hs_node_check.py runs/hsG_c2.0_N160_log.pt        # 6400 collocation nodes
  HS_SAVE=artifacts/data/hs_points_export/hsQ_c2.0_N128_acc6_fine_rows_resolved.npz   python3 src/hs_node_check.py runs/hsQ_c2.0_N128_acc6_fine.pt  # 12288 oversampled solve rows
  Both use the resolved evaluator (32 inner Gauss points, >= 10 log panels per decade x 16 points, 400-point tail, exponent q = 2).  These are the two node sets whose
  maxima the checker could compare only against this lane's printed records (note 172 (i)); the printed maxima of the re-run must agree with results/hs_node_check_c2_N160.txt
  and results/hs_node_check_c2_N128_acc6_fine.txt (see results/hs_node_check_c2_N160_export.txt, hs_node_check_c2_N128_acc6_fine_export.txt and the sha256 lines below).
  Load: d = numpy.load(f); d['x'], d['y'], d['V1'], d['V2'], d['g'], d['g_xi'], d['g_y'], d['R_h'], d['N_f']; str(d['rule']), str(d['state_sha256']).
  Results (DONE 06:16:13Z; evaluation time 12.2 min for 6400 nodes, 19.0 min for 12288 rows): the 160x40 re-run gives maxima of |R_h|/N_f 1.334e-5 / 4.382e-5 / 3.616e-5 /
  8.613e-5 by region against the recorded 1.334e-5 / 4.381e-5 / 3.616e-5 / 8.613e-5 (the record of 01:52Z used the evaluator's then-default tail exponent 3 and chunks of
  100 nodes, the re-run exponent 2 and chunks of 1500: NUM_REPORT item 14, note 175; the chunk-size attribution first given was withdrawn); the 128x32 oversampled re-run reproduces the recorded 1.513e-5 / 2.436e-5 / 1.034e-5 / 2.932e-8 to every printed digit.  sha256 (results/export_nodes_sha256.txt):
  ecfadc376fb7fc6ebedffb4e69c0cac658eaebaf945c5b0ca53c33f16545c16d  data/hs_points_export/hsG_c2.0_N160_log_nodes_resolved.npz  (465567 bytes)
  288e95d19baa407201dd034078ca80b085b4321256d8d67bdf6348d6085b7163  data/hs_points_export/hsQ_c2.0_N128_acc6_fine_rows_resolved.npz  (889559 bytes)
  In both files R_h and N_f recomputed from the saved x, y, V1, V2, g, g_xi, g_y agree exactly with the saved R_h, N_f; no zero denominators (minimum N_f 5.0e-5 at the
  innermost rows).  artifacts total 28 MB after the exports.
  Provenance test (launch/launch_q_test.sh, 06:22Z .. 06:40Z; results/hs_node_check_c2_N160_q3_ch100.txt, _q2_ch100.txt, q_test.out): HS_Q=3 HS_CH=100 reproduces the
  01:52Z record results/hs_node_check_c2_N160.txt digit for digit (that record used the script's pre-02:55Z default tail exponent 3; NUM_REPORT item 14, notes 175-176),
  and HS_Q=2 HS_CH=100 reproduces the export run digit for digit: the chunk size has no effect at the printed digits.
  Tail-exponent check of the 192 / 224 node checks (launch/launch_q3_192_224.sh, 06:45Z .. 07:22Z; results/hs_node_check_c2_N192_q3.txt, _N224_q3.txt, q3_192_224.out):
  with exponent 3 the regional maxima agree with the q = 2 records (results/hs_node_check_c2_N192.txt, _N224.txt) to three printed digits (one printed-unit differences:
  2.448 vs 2.449e-5 at 192, 2.247 vs 2.248e-5 at 224); NUM_REPORT item 14.
  Angular-scan sampling test (07:50Z; src/hs_angular_scan.py now takes HS_NTH = number of angles over the quadrant, default 8M + 1): results/hs_angular_scan_acc128_r3_sampling.txt,
  the r = 3 scan of data/hs/hsQ_c2.0_N128_acc.pt on 127 / 255 / 511 / 1023 interior angles (sign changes 31 / 31 / 33 / 37; dominant mode 31 / 33 / 33 / 33; amplitude 3e-6 .. 4.4e-6).
  Evaluator-sensitivity test of the r = 3 scan (08:02Z; src/hs_angular_scan.py options HS_HREL (finite-difference step factor), HS_QS (tail exponent), HS_NTAIL, HS_SAVE (pointwise
  npz export)): results/hs_angular_scan_acc128_r3_sensitivity.txt; pointwise exports data/hs_points_export/hsQ_c2.0_N128_acc_scan_r3.npz, _r30.npz.  At r = 3 the sign-change
  count is 31 / 6 / 15 / 37 / 0 under the default / step 1e-6 / exponent 3 / 800 tail points / step 1e-4, dominant mode 33 stable; at r = 30 all variants agree (32, k = 32).

## Shift 9 (2026-10-22T11:41Z to the cap 12:44Z): no computation; integrity checks only
Nothing was run.  Checks at 2026-10-22T11:45:56Z: all 46 archived `.pt`/`.npz` states named in `MANIFEST_STATES.md` reproduce their sha256; `reconstruction/SHA256SUMS.txt`
20 of 20 OK; all 129 files in `src/` and `tests/` compile; total size 26.9 MB.  The lane's time line (T0, T_end of the team's report, elapsed time, last edit)
is in the TIMELINE header of `../NUM_REPORT.md` and in `../RUN_STATUS.md`.
