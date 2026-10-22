# Numerical artifacts for "Self-similar profiles of the 2D inviscid Boussinesq equations, Setting A1"

## Outcome

There is no candidate solution. The outcome of the study is UNRESOLVED. The coefficient files in this folder are
least-squares numerical states: iterates obtained by reducing collocation residuals of the profile equations under fourfold
parity, without established stationarity or minimality. The main generating-function states hold the stored temperature
coefficient a0 = 600 fixed (the physical centre slope is a0/h, with h the centre value of the chart) and the exponent beta = 3
fixed (apart from the explicitly labelled exponent-study states genfn_bfl96_298.npz and genfn_bfl96_302.npz); the
earlier polar states and some lineage seeds in the inventory carry other values of a0, stored in each file. Their sampled residuals are small (about
3e-7 to 1e-6 in the normalized ratios on the best generating-function states) but they are not claimed to approximate,
or to be close to, an exact solution. Every residual number quoted below is the authors' own evaluation with the
listed scripts unless it is attributed to the independent verifier; interval enclosures by the verifier are statements
about finite point sets only.

## Folder layout

- `*.npz` (top level): coefficient files of the numerical states (NumPy archives; read with `allow_pickle=False`; the
  solver history is the JSON string in the key `hist`). Each state is identified by the SHA-256 of its original
  coefficient file, the digest cited in the report; STATE_DIGESTS.txt maps it to the published file (see below).
- `states_cited/`: the further coefficient files whose digests the report cites (Section 9 of the report): the
  exponent study at (56, 30) with a core patch (bfc_*.npz), the early (48, 26) and (64, 34) states (snap_J48K26.npz,
  frzA_sc2_J64K34.npz, frzD_n2_J64K34.npz), the amplitude excursions to a0 = 550, 650, 700, 800 and their returns
  (tra*.npz), the (80, 96) parent and exponent pair (p80K96.npz, bfl96k_*.npz), the cutoff members and earlier cutoff
  attempts (dom*_t*.npz), the core-20 control (core20_ctrl.npz), the exponent excursions and continuations at (80, 64)
  and (96, 64) (bfl29*.npz, bfl30*.npz, bfl96_300.npz), the free-exponent pairs and their controls (bfl297.npz,
  bfl303.npz, fbeta_from29*/30*.npz, ctrl29*/30*.npz), the 200-iteration controls (ctrl200_c62.npz, fbeta200_c62.npz,
  fab200_c62.npz) and the resolution-sequence members (res_J64K48.npz, res_J80K64.npz).
- `STATE_DIGESTS.txt`: for every coefficient file, the SHA-256 of the original file (the digest cited in the report),
  the SHA-256 of the published file, whether the `init` field was changed, and whether the report cites the digest.
- `*.where2.txt`, `*.regtab.txt`: authors' dense between-node residual checks (where2_gpu.py) and banded residual
  tables (regtab.py) of the generating-function states, one pair per state. The first line names the evaluated state
  file; the evaluations were made on the original coefficient files (original SHA-256 in STATE_DIGESTS.txt), whose
  numerical content is identical to the files in this folder.
- `*.eval.json`: independent-point residual evaluations of the polar states (scripts_polar_char/eval_candidate.py).
  Their field `file`, and the first line of char_cs4_jacobian_analysis.txt, give the original run file name.
- `*.chareval.json`: off-grid evaluations of the characteristic (slaved-transport) states (char_eval.py).
- `char_cs4_jacobian_analysis.txt`: truncated least-squares analysis of the reduced closure Jacobian of
  char_state_cs4_16x48_it5.npz (jac_analysis.py).
- `diag_lead/`: sampled physical-space diagnostics (axis profiles, half-plane samples, sign and zero tables) of
  genfn_c32_J96K80.npz and genfn_c20sedge_inner128.npz, produced by scripts_genfn_gpu/lead_diag.py.
- `scripts_genfn_gpu/`: mixed-coordinate (generating-function) Levenberg-Marquardt solver on the GPU (gsolve_gpu.py; the
  free-exponent variants gsolve_fbg.py, gsolve_fbc.py, gsolve_fbd.py), the model and jet modules, and the evaluators
  where2_gpu.py, wmax.py, regtab.py, desing.py, jetratio.py, farfield_C.py, gphys_local.py, stag_check.py, common_pts.py
  and further diagnostics (lead_diag.py, gphys_band.py, aspect_lead.py, xaxis_gpu.py, vaxis.py, signrev.py, noise_test.py).
- `scripts_genfn_cpu/`: the authors' first implementation of the generating-function representation (PyTorch in
  float64, CPU): Taylor jets (jets.py, jets3.py), the basis and residual (model.py, model_core.py with the centre
  patches, the free-exponent variants model_fb.py, model_core_fb.py, model_h.py; formula sheet FORMULA_core.md), the
  Levenberg-Marquardt drivers (gsolve.py and the free-exponent drivers gsolve_fb.py, gsolve_fbc.py, gsolve_fbc_curv.py,
  gsolve_fbd.py, gsolve_fbh.py), far rows (farrows.py) and evaluators and diagnostics (where.py, where2.py, where3.py,
  geval.py, gphys.py, desing.py, gmap.py, xaxis.py, yaxis.py, yband.py, rays.py, profile1d.py, farx.py, hfar.py,
  wspec.py, vamp.py, beta_table.py, thy_sign.py, proj.py, reproj.py, hot.py; tests test_jets.py, test_model.py). The
  states snap_J48K26.npz, frzA_sc2_J64K34.npz, frzD_n2_J64K34.npz and bfc_*.npz of `states_cited/` were computed with
  this code; scripts_genfn_gpu/ is its port to the GPU.
- `exploratory/`: exploratory code of the authors. dynres/: dynamic rescaling (dr.py on a Cartesian grid,
  dr_logpolar.py on a grid uniform in log r). charfp/: the characteristic fixed-point and Newton-Krylov iterations
  (picard.py, nk.py to nk4.py, ray.py, ray2.py, refit.py, refit2.py, charlib.py, with the polar basis library
  polarlib.py and evalfields.py at the version used there); their saved iterates are not included. jets/centre_jets.py:
  centre Taylor jets of polar states. formaljets/: check_formal.py (symbolic check of the formal local jets and of the
  operator T_N of Proposition 26 of the report), growth.py and its float64 version growth_fast.py (the centre
  coefficient recursion run forwards).
- `scripts_polar_char/`: the polar spectral least-squares solver (solve_gn.py, solve_lsqr.py, polarlib.py) and its checks
  (eval_candidate.py, direct_bs_check.py: direct Biot-Savart quadrature check, charcheck.py: characteristic
  re-derivation, artifact_tests.py: nontriviality tests, nulldir.py / nulldir2.py: null direction of the Jacobian,
  test_inverse.py: manufactured tests of the modal inverse, identities.py), and the characteristic slaved-transport
  solver (charsolve.py, charlib2.py, charlib_gpu.py, char_eval.py, proj_psi.py, test_charlib.py, jac_analysis.py).
- `verification/`: the independent verifier's code (see the section on independent checks), with
  `verification/research/*/PROOF.md` (mathematical premises of the interval and certificate scripts) and
  `verification/results/*/` (summaries of the finite-point interval enclosure runs).
- `SHA256SUMS.txt`: SHA-256 of every file in this folder.

## Requirements

Python 3.9, NumPy 2.0.2, SciPy 1.13.1, SymPy 1.14.0, mpmath 1.3.0, PyTorch 2.8.0 with CUDA. An NVIDIA A100 80 GB GPU was
used; the (96, 80) solver runs need about 77 GB of GPU memory; where2_gpu.py at 241 x 300 needs about 4 GB per
4096-point chunk. desing.py and jetratio.py run on the CPU (`CUDA_VISIBLE_DEVICES=`). A few verifier scripts for the far
section (far_section_interval.py, far_section_rational.py, far_poly_bounds.py, certify_far_polynomial.py,
certify_far_point_examples.py, check_far_section_rational.py) also import python-flint and/or gmpy2; their versions are
not recorded here. Solver reruns are deterministic up to GPU reduction order (coefficients agree to about 1e-12
relative between runs).

## Main states

SHA-256 prefixes below are the first 16 hex digits of the SHA-256 of the original coefficient file, as cited in the
report; STATE_DIGESTS.txt gives the full original digest and the SHA-256 of the published file. (J, K) are the
radial and angular degrees of the generating-function representation; "core" is the degree of the centre patch. The
residual values are the authors' dense maxima of the prompt ratio R/N and the grouped ratio R/N2 over the chart grid
for r < 1e8 (where2_gpu.py + wmax.py), two significant digits.

| file | SHA-256 (first 16) | (J, K) | core degree | note |
|---|---|---|---|---|
| genfn_c32_J96K80.npz | 6cccc71450bbfe06 | (96, 80) | 32 | best (96, 80) state; authors' dense maxima R/N 3.0e-7, R/N2 2.7e-7 (r < 1e8) |
| genfn_c32_J96K64.npz | 2ffdd4aedaa1b40a | (96, 64) | 32 | best (96, 64) state; authors' dense maxima 5.6e-7, 4.7e-7 |
| genfn_res_J96K80.npz | 134d909825dab1e1 | (96, 80) | 20 | core-20 parent of the (96, 80) ladder; authors' dense maxima 9.8e-7, 7.8e-7 |
| genfn_c20sedge_inner128.npz | 62df5606c929d8ae | (80, 64) | 20 | rows next to the axes, inner 128 x 80 collocation; parent of every later state; authors' dense maxima 1.3e-6, 1.2e-6 |
| genfn_res_J96K64.npz | fb05ac9a8c903f2c | (96, 64) | 20 | core-20 parent of the (96, 64) ladder; 1.01e-6, 8.0e-7 |
| genfn_core24.npz | 7b9c2e1c1323d60e | (80, 64) | 24 | core degree 24 at (80, 64); 1.3e-6, 1.1e-6 |
| genfn_c24_J96K64.npz | e5617175b37d883f | (96, 64) | 24 | core ladder member; 6.7e-7, 6.0e-7 |
| genfn_c24_J96K80.npz | b4ab67f1dbda9f61 | (96, 80) | 24 | core ladder member; 3.8e-7, 3.5e-7 (near-centre zoom 6.2e-7, 4.9e-7) |
| genfn_c28_J96K64.npz | 397be00ecb74777a | (96, 64) | 28 | core ladder member; 5.8e-7, 5.2e-7 |
| genfn_c28_J96K80.npz | d6f1d97d6dbc3407 | (96, 80) | 28 | core ladder member; 3.2e-7, 2.8e-7 (near-centre zoom 4.2e-7, 3.4e-7) |
| genfn_c28_J112K64.npz | cd816d1510dc75e8 | (112, 64) | 28 | radial degree 112; 5.3e-7, 3.6e-7 |
| genfn_d28_J96K64.npz | 51d5562a2150fd6a | (96, 64) | 28 | 4x denser far rows (32 x 160 gap rows, 81 infinity rows); 5.8e-7, 5.1e-7 |
| genfn_d32_J96K64.npz | be6980ac5329d2d7 | (96, 64) | 32 | 4x denser far rows; 5.7e-7, 4.7e-7 |
| genfn_d32_J112K64.npz | d476151c0235ce40 | (112, 64) | 32 | dense far rows; one accepted step saved before the run ran out of GPU memory; 5.3e-7, 3.5e-7 |
| genfn_bfl302_rt.npz | aa3b7ed9d26bda02 | (80, 64) | 20 | beta excursion to 3.02 and return to beta = 3; 1.2e-6, 9.6e-7 |
| genfn_bfl96_298.npz | bb21b77b10579347 | (96, 64) | 20 | free-exponent basis (fb = 1) held at beta = 2.98; see the evaluator caveat |
| genfn_bfl96_302.npz | d700d05bbeea57eb | (96, 64) | 20 | free-exponent basis (fb = 1) held at beta = 3.02; see the evaluator caveat |
| genfn_bfl96_298_rt.npz | b4342e47ec80005f | (96, 64) | 20 | return to beta = 3 from genfn_bfl96_298 (fb = 1 file, beta = 3) |
| genfn_bfl96_302_rt.npz | d886192c5ecff046 | (96, 64) | 20 | return to beta = 3 from genfn_bfl96_302 (fb = 1 file, beta = 3) |
| state_b3.0_chain240.npz | a5d59a286e6670b1 | NT = NO = 16, K = 48 (polar) | n/a | polar least-squares state, about 240 iterations; solver-grid normalized residuals about 1.3e-3 (Theta), 7e-4 (Omega) |
| state_b3.0_res2.npz | 8d29592591b4aad3 | NT = NO = 24, K = 64 (polar) | n/a | polar least-squares state, domain r <= 1e6; solver-grid residuals 2.8e-4 (Theta), 1.4e-4 (Omega) |
| state_b3.0_res2_dom0999.npz | 2d3f9649ecc46471 | NT = NO = 24, K = 64 (polar) | n/a | polar least-squares state, domain r <= 1e9 |
| state_b3.0_res3_32x32.npz | ca25d78b1bf73101 | NT = NO = 32, K = 96 (polar) | n/a | polar least-squares state, 32 + 32 angular modes |

Other states (lineage seeds, earlier resolution studies and controls; all at beta = 3):

| file | SHA-256 (first 16) | (J, K) | core degree |
|---|---|---|---|
| char_state_cs4_16x48_it5.npz | c750f0ff46931eac | NO = 16, K = 48 (Psi basis) | n/a |
| genfn_c20sedge_100.npz | f3b56f62d8e4bbc8 | (80, 64) | 20 |
| genfn_fa64_500.npz | 157f5b1d3c7e8186 | (64, 34) | none |
| genfn_g1_sc2_J80K40.npz | 006d600c89a4f005 | (80, 40) | none |
| genfn_nE80.npz | 7d990964bc47eef5 | (80, 40) | 16 |
| genfn_nE80K64_c20_fa600_infdes.npz | ca1f18529b54cbae | (80, 64) | 20 |
| genfn_nE80K64_fa600.npz | f426a3c9aeb92b50 | (80, 64) | 16 |
| genfn_nE80K64_fa600_inf.npz | 2f1a793c5f2bc1e3 | (80, 64) | 16 |
| genfn_nE80K64_fa600_infdes.npz | d6efe3207d1964c8 | (80, 64) | 16 |
| genfn_nE80K64_fa600_infdes2.npz | a7e057ae57c1a686 | (80, 64) | 16 |
| genfn_nE80K64_fa600_t3e-3.npz | 0b090513ecc07dd7 | (80, 64) | 16 |
| genfn_nE80K80_fa600.npz | 57caba170111d3c6 | (80, 80) | 16 |
| genfn_nE80K96_fa600.npz | f9d7f2b4d5326db8 | (80, 96) | 16 |
| genfn_nE80K96_fa600_infdes.npz | 2fe327c06a4eba36 | (80, 96) | 16 |
| genfn_nE80_fa600.npz | 2759b4a959a05c40 | (80, 40) | 16 |
| genfn_nE80_fa600_t1e-2.npz | 78edbe8eb31fe2c0 | (80, 40) | 16 |
| genfn_nE96K64_fa600_infdes.npz | 147551db9f9a5948 | (96, 64) | 16 |
| genfn_nmt80_a600.npz | 428ec7531da6b10c | (80, 40) | none |
| genfn_nmt80_core16in_a600.npz | 2ea272bee7545267 | (80, 40) | 16 |
| lead_J48K26_fitted_psi31x64.npz | d57295478c66728c | NO = 31, K = 64 (Psi basis) | n/a |
| prelim_b3.0_q99.npz | 4eb3d37c9971f436 | NT = NO = 16, K = 48 (polar) | n/a |
| state_b3.0_res2_dom0999_PSI.npz | 2b7ccd7ec5bf6806 | NO = 24, K = 64 (Psi basis) | n/a |

The generating-function files contain a string field `init` naming the initial state of the run. In the original
files it held an absolute path on the machine where they were produced; for publication it was shortened to the file
name, by rewriting only the archive member init.npy. Every other member of each archive has the same uncompressed
bytes (the same CRC-32) as in the original file, so all coefficients, parameters and solver histories are unchanged,
but the SHA-256 of a changed file differs from the digest cited in the report. STATE_DIGESTS.txt lists both digests
for every file; a file with `init_changed = no` is byte-identical to the original. The names in `init` are the run
names of the original files, which differ in part from the published file names.

## Commands

### Regenerating a generating-function state (run from scripts_genfn_gpu/, GPU required)

The positional arguments are: initial state, output file, J, Kw, Nt, Ns (collocation counts), iteration budget, tmin,
gauge, alpha; the settings are also stored in each state.

    python3 gsolve_gpu.py ../genfn_c28_J96K80.npz out.npz 96 80 200 168 200 3e-3 1 3 --core 32 32 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600 --print-every 25 --save-every 25   # genfn_c32_J96K80
    python3 gsolve_gpu.py ../genfn_c28_J96K64.npz out.npz 96 64 200 136 200 3e-3 1 3 --core 32 32 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600 --print-every 25 --save-every 25   # genfn_c32_J96K64
    python3 gsolve_gpu.py ../genfn_c20sedge_inner128.npz out.npz 96 80 200 168 200 3e-3 1 3 --core 20 20 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600 --print-every 25 --save-every 25   # genfn_res_J96K80
    python3 gsolve_gpu.py ../genfn_c20sedge_inner128.npz out.npz 96 64 200 136 200 3e-3 1 3 --core 20 20 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600   # genfn_res_J96K64
    python3 gsolve_gpu.py ../genfn_c20sedge_inner128.npz out.npz 80 64 168 136 200 3e-3 1 3 --core 24 24 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600   # genfn_core24
    python3 gsolve_gpu.py ../genfn_nE80K64_c20_fa600_infdes.npz out.npz 80 64 168 136 100 3e-3 1 3 --core 20 20 0.1 0.4 --inner 128 80 1e-3 4.0 --sedge --nmin --step qr --lam0 1e-11 --infrow 41 --desrows 16 80 1.0 --fixa0 600   # genfn_c20sedge_inner128 from its seed

The core-24 and core-28 ladder members were produced with the same options and the core degree changed, from their
parents (core 24 from genfn_res_J96K64 / genfn_res_J96K80, core 28 from the core-24 states, core 32 from the core-28
states); the d28 / d32 states use `--desrows 32 160 1.0 --infrow 81`. The beta
excursions use gsolve_fbg.py with `--btarget`; their run drivers are not included.

### Recomputing residuals (run from scripts_genfn_gpu/; replace the state file as needed)

    python3 where2_gpu.py ../genfn_c32_J96K80.npz 241 300 1e-4 --edges > w.txt; python3 wmax.py w.txt   # dense check, 77064 points; wmax.py gives the band maxima for r < 1e8
    python3 regtab.py ../genfn_c32_J96K80.npz 241 300 1e-4 --edges                                 # absolute and divided residuals by band of r
    CUDA_VISIBLE_DEVICES= python3 desing.py ../genfn_c32_J96K80.npz 3e-3,1e-3,1e-4,1e-6,0 --NS 300   # desingularized far rows
    CUDA_VISIBLE_DEVICES= python3 desing.py ../genfn_c32_J96K80.npz rand:2000:1e-8:3e-3 --seed 1
    python3 farfield_C.py ../genfn_c32_J96K80.npz --nv 41                                          # far-field limit max |C/N20|
    CUDA_VISIBLE_DEVICES= python3 jetratio.py ../genfn_c32_J96K80.npz --r1 1e-3 --r2 1e-2           # centre jets and the exact jet relation
    python3 gphys_local.py ../genfn_c32_J96K80.npz phys.npz 1e-3 1e8 241 73                         # physical-space polar sampling (17593 points)
    python3 stag_check.py ../genfn_c32_J96K80.npz                                                  # stagnation and homogeneity diagnostics
    CUDA_VISIBLE_DEVICES= python3 common_pts.py ../genfn_c32_J96K64.npz ../genfn_c32_J96K80.npz      # fields at common physical points

The header line of where2_gpu.py output reports the maximum of R/N2 over all rows, including rows beyond r ~ 1e8 that
are binary64 rounding noise; use wmax.py for the band maxima. A rerun of regtab.py on an A100 reproduced
genfn_c32_J96K80.regtab.txt in the "all" row and in all bands from r = 4e-3 to 6.3e4; the near-centre and outermost
bands differed in the third digit (GPU reduction order on cancellation-limited values is a possible explanation; not
established).

### Polar least-squares solver and its checks (run from scripts_polar_char/)

    python3 test_inverse.py                                   # manufactured tests of the modal inverse and basis derivatives
    python3 solve_gn.py --beta 3.0 --NT 16 --NO 16 --K 48 --Nr 300 --Nth 48 --qmax 0.99 --iters 60 --init ../prelim_b3.0_q99.npz --out replay_b3
    python3 eval_candidate.py ../prelim_b3.0_q99.npz --Nr 800 --Nth 65 --umax 1e7   # residual tables at independent points
    python3 direct_bs_check.py ../state_b3.0_res3_32x32.npz    # velocity by direct 2D Biot-Savart quadrature vs the modal inverse
    python3 charcheck.py ../state_b3.0_res3_32x32.npz          # Theta and Omega re-derived along backward characteristics of the state's own velocity
    python3 artifact_tests.py ../state_b3.0_res3_32x32.npz     # nontriviality, nonlinearity, sign structure, far-field amplitudes
    python3 nulldir.py ../state_b3.0_res3_32x32.npz            # smallest singular direction of the Jacobian vs the scaling generator

The same checks apply to the other polar states (state_b3.0_*.npz). The discretization settings are stored in each
state (keys beta, L, NT, NO, K, Nr, Nth, gamma_T, gamma_O, mu).

### Characteristic slaved-transport solver (run from scripts_polar_char/)

    python3 proj_psi.py ../state_b3.0_res2_dom0999.npz psi.npz            # project a polar state onto the Psi basis
    python3 charsolve.py --init ../state_b3.0_res2_dom0999_PSI.npz --out tag --Nr 120 --Nth 32 --dt 0.01 --iters 12 --jac-every 3 --batch 32
    python3 charsolve.py --init ../state_b3.0_res2_dom0999_PSI.npz --out tag --diag --dt 0.005   # consistency diagnostic only
    python3 char_eval.py ../char_state_cs4_16x48_it5.npz --per-decade 6 --Nth 18 --dt 0.01 --json out.json
    python3 test_charlib.py                                               # manufactured-velocity test of the reconstruction

## Evaluator caveat

where2_gpu.py, regtab.py, gphys_local.py, farfield_C.py and stag_check.py build the fixed-m (beta = 3) basis. They are
invalid for the free-exponent states at beta != 3, genfn_bfl96_298.npz and genfn_bfl96_302.npz. desing.py, jetratio.py,
aspect_lead.py and common_pts.py dispatch on the stored flag fb and are valid for them.

## Independent checks of the verifier (verification/)

These scripts were written and run by an independent verifier and do not import the solvers above. They were run from
a working directory in which the scripts lived under `code/` and wrote their records under `runs/`, `research/` and
audit directories. To use them from this folder:

    cd verification && ln -s . code && mkdir -p runs

Main modules:

- Cartesian finite-difference residual evaluator without floors: independent_residuals.py (data accessors for Theta,
  Omega, Psi and their parity quotients; parity-axis limits), physical_cartesian_fd.py, physical_vorticity_fd.py,
  core_cartesian_residual.py (own chart inversion and eighth-order differences), center_jet_crosscheck.py.
- Full-plane inverse (Biot-Savart) evaluators: bs_modal.py (modal radial Green function), direct_bs.py (target-centred
  polar quadrature, no parity), fullplane_duffy.py and fullplane_duffy_regularized.py (parity-folded quadrature),
  gaussian_plane_inverse.py, plane_quadrature.py, core_physical_inverse_recovery.py, core_physical_mp.py, core_physical_mp_v2.py.
- Exact rational centre Taylor coefficients: core_center_certificate.py, certify_generating_center.py,
  certify_scaled_generating_center.py, center_moment_crosscheck.py, center_resonance_polynomials.py, high_order_jets.py,
  jet_recurrence_check.py, check_formal_local_jets.py, check_generating_low_jets.py, check_pde_jets216.py, check_stagnation_jets.py.
- Backward-characteristic checker: characteristic_check.py, with test_characteristic_check.py and verify_characteristic_polar.py.
- Interval enclosures of residuals at finite point sets: interval_residual221.py, dyadic_root220.py,
  root220_replay_arithmetic.py, prepare_/run_/replay_residual221.py, prepare_/run_/replay_fullgrid225.py and the
  test_interval_residual221*.py tests; results in results/interval_residual221/ and results/fullgrid_interval225/.
- Certificates of the global chart and the far section: logarithmic_chart_certificate.py,
  replay_logarithmic_chart_certificate.py, generating_chart_certificate.py, replay_chart_certificate.py,
  certify_generating_far_chart.py, certify_generating_far_axis.py, certify_logarithmic_far_axis.py,
  certify_outer_chart_margin.py, certify_candidate_far_axes.py, check_global_chart_flow.py, far_section_rational.py,
  far_section_interval.py, far_poly_bounds.py, check_far_section_rational.py, certify_far_polynomial.py,
  certify_far_point_examples.py, certify_polar_tail_fourier.py, certify_core_patch_bound.py, certify_core_patch_sharp.py,
  certify_core_source.py.
- Symbolic and other checks: check_generating_toy_symbolic.py, check_logarithmic_far_axis_symbolic.py,
  compactification_direct_residual.py, check_finite_family_interval_exclusion.py, rational_solver.py (independent
  rational-basis search, not an existence proof).

Commands that run from verification/ after the setup line above (CPU only):

    python3 test_bs_modal.py                 # manufactured tests of the modal inverse
    python3 test_direct_bs.py                # direct quadrature vs exact and vs modal velocities
    python3 test_independent_residuals.py    # manufactured test of the finite-difference residual evaluator (writes runs/)
    python3 test_characteristic_check.py     # manufactured transport test of the characteristic checker (writes runs/)
    python3 test_rational_solver.py
    python3 logarithmic_chart_certificate.py ../genfn_nmt80_a600.npz --out cert_chart   # exact rational global-chart certificate (beta = 3, m = 3, alpha > 0)
    python3 certify_outer_chart_margin.py ../genfn_nmt80_a600.npz --out cert_margin      # chart margin; refuses files with a centre patch

Both certificate scripts read only the coefficient array c. certify_outer_chart_margin.py rejects files with a centre
patch (keys core, cc); for patched states the verifier supplied separately exported outer components from its own audit
directories, which are not part of this folder.

The interval tests (test_interval_residual221*.py) additionally need `mkdir -p research/interval_residual221/verification`
and run once (they refuse to overwrite their output). The following cannot run standalone from this folder because they
read input records, plans or exported coefficient files from the verifier's audit directories, which are not included:
run_/replay_/prepare_residual221.py, run_/replay_/prepare_fullgrid225.py (they also require an external plan SHA-256
and `nice 19`), certify_generating_center.py, certify_scaled_generating_center.py, certify_generating_far_chart.py,
certify_generating_far_axis.py, certify_far_*.py, certify_core_*.py, certify_candidate_far_axes.py,
generating_chart_certificate.py (expects an exported source with the key `coeff`), check_far_section_rational.py,
check_global_chart_flow.py, check_core_dense_extrema.py, verify_characteristic_polar.py and verify_gaussian_residuals.py.
They are included as the exact code behind the verifier's records; the library modules listed above can be imported
directly.

## Checksums

SHA256SUMS.txt lists the SHA-256 of every file in this folder as published, except itself (regenerate with
`find . -type f ! -name SHA256SUMS.txt | sort | xargs sha256sum`). Verify with `sha256sum -c SHA256SUMS.txt`.
