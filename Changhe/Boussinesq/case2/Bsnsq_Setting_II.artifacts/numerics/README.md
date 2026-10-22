# Numerics: Boussinesq Setting A2 numerical search for self-similar profiles

Status: no candidate profile was found. Every stored state in states/ is a rejected numerical state, not a solution and not an
approximation of a known solution. The states are kept so that the quoted misfits and diagnostics can be reproduced.

Three methods were used: over-collocated least squares (fixed beta, both signs of a0, N up to 240, exact first-tail matching rows;
free-beta refits at N208/N240 in states FB_*), forward characteristics / Picard iteration, and dynamic rescaling in pseudo-time (four
gauges). This folder contains the code, the validation tests and the stored least-squares states, together with the commands that
regenerate a state, run the validation tests and evaluate the residuals and diagnostics of the stored states.

Layout and working directory: run every command from inside this folder (numerics/), after creating the output folder with
`mkdir -p runs`. The scripts import the library from code/ (relative path), read stored states from states/ and write their logs and
output states to runs/. The run logs of the original study and the run launch scripts are not included; every solver option of a stored
state is saved inside its archive (key `extra`, JSON), and the iteration history in key `hist`.

Software: Python 3.9, numpy 2.0, scipy 1.13, sympy 1.14, torch 2.8 (float64). The states were fitted on one NVIDIA A100 GPU in float64
with torch 2.8; CPU works (torch selects it automatically when no GPU is available) but is slower.

States in states/ are numpy .npz archives (np.savez_compressed, lossless; load with numpy.load(path, allow_pickle=True)). They are
lossless re-archives of the solver's own output files runs/<name>.npz (np.savez, uncompressed): the bytes differ, every array is
identical key by key (checked with numpy.array_equal, NaN-aware). No evaluated quantity depends on which copy is loaded, so all commands
below work with either copy.

## Full list of state files (states/, 72 files; the families below use abbreviated names)
    AM2_B2m_N176M66, AM_B2m_N144M72, ANN96_B2m_N144_w0.1, ANN96_B2m_N144_w0.3, ANN96_B2m_N144_w1.0, ANN96_B2m_N176_w1.0, ANN_B2m_N144_w0.3, ANN_B2m_N144_w1.0, B2_m_gauss_N112, B2_m_gauss_N144, B2_m_gauss_N80, B2_p_gauss_N112, B2_p_gauss_N144, B2_p_gauss_N176, B2_p_gauss_N80, CF_B2m_N144, CF_B2m_N176, CF_B2p_N144, CF_B2p_N176, CTRL_B2m_N144M36, FBR_B2m_N144, FBR_B2m_N176, FBR_B2p_N144, FBR_B2p_N176, FB_B2m_N144, FB_B2m_N176, FB_B2m_N208, FB_B2p_N144, FB_B2p_N176, FB_B2p_N208, FB_R7_N208, I5_fix3_gauss, K3_fix1.94_N112M28, KC_B2m_N176_fix1.9538, KC_B2m_N208_fix1.96, KC_B2p_N176_fix1.9809, KC_B2p_N208_fix1.99, Nn4_fix3_a0m1_N80, Nn5_fix3_a0m1_N112, PATCH_B2m_N144_w0.1, PATCH_B2m_N144_w1.0, PR3_fix3_N112_pres, R4_fix3_N112M28, R5_fix3_N144M36, R6_fix3_N176M44, T5_fix3_N80M20L1, TL_B2m_N112, TL_B2m_N176, TL_B2m_N208, TL_B2m_N240, TL_B2p_N112, TL_B2p_N176, TL_B2p_N208, TL_B2p_N240, TL_K5_fix1.94_N176, TL_K6_fix1.94_N208, TL_Nn6_a0m1_N144, TL_R4_N112, TL_R7_N208, W4_fix3_N112_wmax1, YF_fix3_N176_free_fromYP6, YP3_fix3_N112_ypen, YP4_fix3_N144_ypen, YP6_fix3_N176_ypen, plus eight original uncompressed solver outputs (np.savez, byte-identical to the files evaluated during the study): A1_N48M12L6_b1 (excluded control, beta = 0.9331), B1_fix3_N40M10L15, T4_fix3_N48M12L1, DM_B2m_N112_L0.5, DM_B2m_N112_L2.0, DM_B2m_N112_Rw20, DM_B2m_N112_Rw45 (fit-domain variants at N = 112), Nn3_fix3_a0m1_N64

## Code
- code/a2core.py      basis (xi-map), modal full-plane Green inverse, residual assembly, per-mode orthonormalization
- code/a2core_t.py    beta-adapted t-map basis (t = (1+r^2/L^2)^(-1/(2 beta))) with its Green inverse
- code/lm_solve.py    over-collocated Levenberg-Marquardt driver (fixed or free beta), state I/O, re-fitting
- code/diag_state.py, code/diag_rows.py, code/table_states.py   diagnostics and tables of saved states
- code/charcheck.py   independent characteristics-based transport consistency check of a state
- code/forward.py     transport from the x-axis source with local Taylor data (forward formulation)
- code/picard.py      forward fixed-point (Picard) solver attempt (no converged iterate was obtained)
- code/zeroset.py     stagnation set of W, nodal sets of Theta/Omega, origin exponent (K'_0) fits of a state
- code/beta2_zset.py, code/beta2_arc.py   beta = 2 stagnation-locus diagnostics
- code/enriched.py    labelled finite-regularity test (extra basis chi(r) x^p y with canonical stream response)
- code/lead_tables.py x*, resonance defect, Theta_y(x*,0), residual maxima, residual-direction correlations (reads the fixed runs/ file
                      names listed at the top of the script)
- code/make_hybrid.py helper (least-squares interior + power-law tail start state)
- code/axq.py         axis quantization diagnostics (d_y W2 at y-axis zeros, Theta_xx slopes; beta = 2 sup|U| vs r)
- code/yaxis_ratio.py Omega_x/Theta_xx along the y-axis;  code/natural_tail.py  r^{1/beta} Omega(r, phi) table
- code/annular_energy.py  e(R) = annular kinetic energy / R^{4-4/beta};  code/annular_grad.py  annular ratios of |grad Theta|^2 and kinetic energy for beta > 2 states
- code/beta2_locus.py  beta = 2 locus P -> Q+ with det/tr DW, far-field slopes, kinetic energy
- code/bs_direct.py   direct 2D Biot-Savart quadrature (fourfold images, far grid to 1e13) and finite-difference Poisson residual
- code/jdiag.py, code/jdiag_origin.py   beta = 2 outgoing-amplitude invariant J and its near-origin check
- code/branch_b2.py   beta = 2 tail-branch test (natural r^{1/2} Omega vs bounded-velocity r Omega)
- code/signs_beta3.py  sampled sign descriptions of the stored beta > 2 states: fraction of points with sgn(a0) Omega < 0 by radial band,
                      angular profiles of r^(1/beta) Omega at selected radii (reads runs/zjac_<state>.log if present)
- code/dynres2.py   dynamic rescaling in pseudo-time (third method): local-grid semi-Lagrangian transport of the desingularized fields
                    with the exact modal inverse each step; c_l(s) = (c-2)/2 keeps a(0) = 1 (beta is an output)
- code/dynres.py    first (spectral-projection) version of the same, unstable as a time-stepper; kept for the record
- code/dyn2_newton.py  Newton-Krylov (GMRES) search for fixed points of the flow map of dynres2 (did not converge)
- code/dyn2_diag.py   one-step consistency of dynres2 against the LM residual and grid convergence
- code/dyn2_arnoldi.py Arnoldi eigenvalues of the linearized flow map
- code/svd_states.py, code/svd_states2.py  SVD / near-kernel / beta-sensitivity of the LM Jacobian at saved states
- code/tail_compare.py misfit without the tail rows, next-order far-field defect
- code/robust_zero.py sampled constants (K, k(R), gamma(R)) and admissible C^1 perturbation sizes for a conditional criterion on
                      persistence of the interior zero Q+ on balls around Q+.
                      Usage: python3 code/robust_zero.py states/TL_B2m_N208.npz 13.67859 5.66655
- code/zjac_table.py  summarize runs/zjac_*.log (saved outputs of code/zero_jac.py) into one table
- code/local_res_Q.py  Cartesian residuals R_Theta, R_Omega and their normalizations on sampled circles around the interior zero Q+.
                      Usage: python3 code/local_res_Q.py states/TL_B2m_N208.npz [x y]  (Q+ is read from runs/zjac_<state>.log if x y are omitted)
- code/cauchy_diff.py  relative sup differences of Theta, grad Theta, Omega, W between successive states on fixed polar grids.
                      Usage: python3 code/cauchy_diff.py states/TL_B2m_N112.npz states/B2_m_gauss_N144.npz states/TL_B2m_N176.npz states/TL_B2m_N208.npz
- code/loss_bands.py   weighted squared loss of a saved state grouped by radial band of the collocation nodes
- code/misfit_fit.py   power-law and power-plus-floor fits of the misfit sequences; python3 code/misfit_fit.py [RMS_N240 x]
- code/ext_moments.py  exterior Biot-Savart moments and the velocity induced on r < R by the vorticity difference beyond R (repaired after
                      an external referee's audit; the referee's direct polynomial-moment values supersede the first outputs of the unrepaired version)
- lm_solve.py --patch XC YC RAD W   localized Cartesian temperature-residual rows (RAD > 0: polar tensor rectangle around (XC, YC); RAD <= 0:
                      annulus XC <= r <= YC) for the localized-refit experiment (states PATCH_*, ANN_*)
- lm_solve.py --patch_n K  K x K penalty nodes instead of 12 x 12 (disc) / 24 x 24 (annulus); used by the ANN96_* states (K = 96)
- code/state_summary.py  per-round first/last printed labels (beta, |F|), rebuild betas, final-dict fields, origin identities, q_0(-1) = sum_n c[0, n] (-1)^n
                      of the stored a and G arrays and the mismatch constants 2 (beta_map - beta)/beta_map, (beta_map - beta)/beta_map of a finished run.
                      Usage: python3 code/state_summary.py FBR_B2p_N176  (reads runs/<name>.log, runs/<name>.out, runs/<name>.npz of a run made here)
- code/elliptic_defect.py  sampled elliptic defect E = -Lap Psi - Omega = -curl U - Omega on the common 10000-point grid of common_grid_resid.py,
                      polar curl by fourth-order central differences at three paired fractional/angular steps. Usage: python3 code/elliptic_defect.py states/TL_B2m_N240.npz
- code/elliptic_summary.py  compact table from runs/elliptic_defect.log (per state and step: regional maxima of |E|, grid max of |E|/N_E, ratios to max|Omega| and max|R_Theta|)
- code/common_grid_maxloc.py  sub-band (10-20, 20-30, 30-100, >= 100) maximizers of |R_Theta| and |R_Omega| on the common grid with their locations
- code/ray_signs.py    sampled ray sign patterns (+,-,+) / (-,+,-) of sgn(a0) Omega and sgn(a0) Theta along 90 rays, 400 log radii in [0.5, 1e6].
                      Usage: python3 -u code/ray_signs.py states/R6_fix3_N176M44.npz
- code/annulus_between.py  between-node residuals on the penalty regions of the localized refits (penalty nodes and midpoint grids 33x49,
                      65x97, 129x193). Usage: python3 code/annulus_between.py ann states/B2_m_gauss_N144.npz states/ANN_B2m_N144_w0.3.npz
                      (region 'patch' for the PATCH_* states)
- code/common_grid_resid.py  region-wise residual maxima of several states on ONE common independent grid (200 radii x 50 interior angles).
                      Usage: python3 -u code/common_grid_resid.py states/TL_B2m_N112.npz ... states/TL_B2m_N240.npz
- code/stationarity.py  gradient J^T F of the state's own objective (reverse-mode AD) and sigma_max(J) by power iteration; relative stationarity
                      defect. Usage: python3 -u code/stationarity.py states/TL_B2m_N208.npz
- code/norm_floor_check.py  minima and near-zero counts of the normalizations N_Theta, N_Omega on the between-node grids
- code/kernel_dir.py   coefficient step between two states of a branch against the fine problem's Jacobian: sigma_eff, singular-direction
                      energies, nonlinear remainder, misfit along the segment. Usage: python3 code/kernel_dir.py A.npz B.npz (GPU, about 9 min at N208)
- code/omega_sign.py  sign pattern of the fitted Omega on Q1 (axis traces, {Omega > 0} extent; a0 < 0 states)
- code/cross_rw.py    cross-evaluation of states fitted with different row-weight radii Rw under each weighting
- code/farfield_amp.py  far-field amplitudes a r^(2+2/beta_map), G r^(2+1/beta_map), relative residuals R_a/a, R_G/G at r = 1e2 .. 1e30 and 8 angles,
                      with the derived limits 2 (beta_map - beta)/beta_map and (beta_map - beta)/beta_map for states whose beta differs from the basis
                      exponent beta_map. Usage: python3 code/farfield_amp.py states/TL_B2m_N208.npz states/FB_B2m_N208.npz  (CPU, seconds)
- code/beta_scan.py   fixed-coefficient beta scan of a state's objective by row group (standard, origin, tail rows).
                      Usage: python3 -u code/beta_scan.py states/TL_B2m_N112.npz
- code/beta_scan_summary.py  compact table from a saved beta_scan.py output. Usage: python3 code/beta_scan_summary.py runs/beta_scan.log
- code/zero_jac.py    exact pointwise diagnostics at every zero of W (Omega - Theta_x, |grad Theta|, DW eigenvalues and type, circle
                      projections around Q+, transversal test near P; formulas checked by an external referee).
                      Usage: python3 code/zero_jac.py states/TL_B2m_N208.npz > runs/zjac_TL_B2m_N208.log
- code/bernoulli.py   Bernoulli / Lyapunov identity residual of a saved state
- lm_solve.py --rounds K  (free beta) rebuilds the map, prefactors and sigmas at the current beta after each round and refits the state, keeping
                      --tail/--t1/--wmax on the rebuilt rounds (used by FBR_* with K = 4; every other stored state was fitted with K = 1).
- Further solver options: --tail W --t1 T1 (exact first-tail matching rows); --wmax (cap far-field weights); --ypen C0 W (y-axis positivity
  penalty); --pres XLO XHI W (exact resonance at P with x* unknown); --r_fit R (robust refit when changing beta or map).

## Validation tests (seconds to a minute each)
    python3 tests/check_reduction_sympy.py     # (A2-red), Taylor identities, desingularized forms, Green mode formula
    python3 tests/test_inverse.py              # xi-map inverse: exact to 1e-16 on manufactured solutions
    python3 tests/test_residual_sympy.py       # fields, velocity, R_a, R_G vs sympy: 1e-14
    python3 tests/test_inverse_t.py            # t-map inverse vs direct quadrature (1e-13) and sympy (1e-15)

## Regenerating stored least-squares states with the Levenberg-Marquardt driver (GPU, minutes each)
    mkdir -p runs
    python3 code/lm_solve.py --map t --N 48 --M 12 --L 1 --fixed_beta 3.0 --kind gauss --RG 15 --Rw 30 --maxit 200 --name I5_fix3_gauss
    python3 code/lm_solve.py --map t --N 64 --M 16 --L 1 --fixed_beta 3.0 --Rw 30 --maxit 250 --init runs/I5_fix3_gauss.npz --name R1
    python3 code/lm_solve.py --map t --N 80 --M 20 --L 1 --fixed_beta 3.0 --Rw 30 --maxit 250 --init runs/R1.npz --name R2
    python3 code/lm_solve.py --map t --N 112 --M 28 --L 1 --fixed_beta 3.0 --Rw 30 --maxit 400 --init runs/R2.npz --name R4
    python3 code/table_states.py runs/*.npz          # RMS, max residuals, resolution indicators
    python3 code/diag_state.py runs/R4.npz           # axes, stagnation point, between-node residuals, far field
    python3 code/charcheck.py runs/I5_fix3_gauss.npz # independent characteristics transport check + y-axis exponent test
A tail-row refinement, a consistent-basis free-beta run and a fixed-beta control from stored starts, e.g.
    python3 code/lm_solve.py --map t --N 176 --M 44 --L 1 --fixed_beta 2.0 --Rw 30 --maxit 300 --tail 1.0 --t1 1e-5 --init states/B2_p_gauss_N176.npz --name TL_B2p_N176
    python3 code/lm_solve.py --map t --N 144 --M 36 --L 1 --a0 -1 --Rw 30 --rounds 4 --maxit 50 --tail 1.0 --t1 1e-5 --init states/B2_m_gauss_N144.npz --name FBR_B2m_N144
    python3 code/lm_solve.py --map t --N 208 --M 52 --L 1 --a0 -1 --Rw 30 --fixed_beta 1.960048 --maxit 200 --tail 1.0 --t1 1e-5 --init states/FB_B2m_N208.npz --name KC_B2m_N208_fix1.96
The options of any other stored state can be read from its archive, e.g.
    python3 -c "import numpy as np, json; print(json.loads(str(np.load('states/TL_B2m_N208.npz', allow_pickle=True)['extra'])))"

Stored families: I5, R4, R5, R6 (beta = 3, N48/112/144/176), YP3, YP4, YP6 (y-axis-penalized, N112/144/176), YF (free beta from YP6, N176),
PR3 (exact P resonance, N112), W4 (interior-only weights, N112), K3 (control at the excluded beta = 1.943, N112), T5 (default family N80),
B2_p_gauss_N80/N112/N144/N176 (beta = 2, a0 = +1; N80-N144 fitted with Rw = 20, N176 with Rw = 30), B2_m_gauss_N80/N112/N144 (beta = 2,
a0 = -1; N80 at Rw = 20), Nn4/Nn5 (beta = 3, a0 = -1, N80/N112). TL_* states were fitted with the finite-t1 first-tail matching rows
(--tail 1.0 --t1 1e-5): TL_B2p_N112/N176/N208/N240 (beta = 2, a0 = +1), TL_B2m_N112/N176/N208/N240 (beta = 2, a0 = -1), TL_R4_N112 and TL_R7_N208 (beta = 3, a0 = +1), TL_Nn6_a0m1_N144 (beta = 3, a0 = -1), TL_K5_fix1.94_N176 and
TL_K6_fix1.94_N208 (like-for-like controls at the excluded beta = 1.9431). AM_B2m_N144M72 and AM2_B2m_N176M66 (angular refinement),
CTRL_B2m_N144M36 (matched-budget control at M36), PATCH_B2m_N144_w0.1/w1.0 (localized temperature rows on a polar patch),
ANN_B2m_N144_w0.3/w1.0 (24 x 24 annulus rows), ANN96_B2m_N144_w0.1/w0.3/w1.0 and ANN96_B2m_N176_w1.0 (96 x 96 annulus rows via
--patch 9 20 0 W --patch_n 96). Free-beta refits FB_B2m_N144/N176/N208, FB_B2p_N144/N176/N208, FB_R7_N208 (beta_map fixed at the initial
beta, 200 LM iterations with tail rows); matched-budget fixed-beta controls CF_B2m_N144/N176, CF_B2p_N144/N176 (200 LM iterations with beta
fixed at 2 from the same starts and rows); consistent-basis free-beta runs FBR_B2m_N144/N176, FBR_B2p_N144/N176 (--rounds 4 --maxit 50);
fixed-beta refits at the free-beta endpoints with beta_map = beta: KC_B2m_N208_fix1.96 (beta = 1.960048, from FB_B2m_N208),
KC_B2p_N208_fix1.99 (beta = 1.990445, from FB_B2p_N208), KC_B2m_N176_fix1.9538 (beta = 1.953773, from FBR_B2m_N176), KC_B2p_N176_fix1.9809
(beta = 1.980937, from FBR_B2p_N176), each 200 iterations with tail rows.

## Residuals and diagnostics of stored states
    python3 code/tail_compare.py states/B2_p_gauss_N176.npz states/TL_B2p_N176.npz
    python3 code/svd_states2.py states/R4_fix3_N112M28.npz        # s_beta, near-kernel
    python3 code/bernoulli.py --nr 2400 --nth 128 states/B2_p_gauss_N176.npz   # Lyapunov identity residual
    python3 code/zeroset.py states/R4_fix3_N112M28.npz
    python3 code/beta2_arc.py states/B2_p_gauss_N80.npz
    python3 code/zero_jac.py states/TL_B2m_N208.npz > runs/zjac_TL_B2m_N208.log
    python3 code/local_res_Q.py states/TL_B2m_N208.npz
    python3 -u code/common_grid_resid.py states/TL_B2m_N112.npz states/TL_B2m_N176.npz states/TL_B2m_N208.npz states/TL_B2m_N240.npz
    python3 -u code/stationarity.py states/TL_B2m_N208.npz
    python3 code/farfield_amp.py states/TL_B2m_N208.npz states/FB_B2m_N208.npz
(further usage lines are given with each script in the Code section above and in the docstring at the top of each script)

## Dynamic rescaling runs (GPU, 1-3 minutes each; logs written to runs/)
    python3 code/dynres2.py --init states/B2_p_gauss_N112.npz --N 112 --M 28 --Ni 512 --Nj 96 --beta 2.0 --ds 0.01 --nsteps 600 --diag_every 50 --name D2_lm112
    python3 code/dynres2.py --init states/B2_p_gauss_N112.npz --N 112 --M 28 --Ni 512 --Nj 96 --beta 2.0 --ds 0.01 --nsteps 600 --mode fixed --name D2_lm112_fix
    python3 code/dynres2.py --N 112 --M 28 --Ni 512 --Nj 96 --beta 2.0 --kind gauss --ds 0.01 --nsteps 300 --name D2_gauss
    python3 code/dynres2.py --init states/B2_p_gauss_N112.npz --N 112 --M 28 --Ni 1024 --Nj 192 --beta 2.0 --ds 0.01 --nsteps 150 --diag_every 25 --name D2_lm112_hi
    python3 code/dynres2.py --init states/B2_p_gauss_N112.npz --N 112 --M 28 --test --name dyn2_test      # one-step consistency vs LM residual
    python3 code/dyn2_newton.py --init states/B2_p_gauss_N112.npz --N 112 --M 28 --T 0.5 --newton 12 --name NK_lm112
