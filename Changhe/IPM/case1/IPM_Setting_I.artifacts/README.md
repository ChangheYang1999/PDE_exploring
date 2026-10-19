# Accompanying artifacts of the report "IPM Setting I"

This folder accompanies the final report on full-plane IPM self-similar profiles with even-x / odd-y symmetry
(Setting I). Its parts (a) to (f) are those of section 5 of the report. All paths below are relative to this folder.
Software: Python 3.9 with numpy 2.0, scipy 1.13 and sympy 1.14 (CPU, single-threaded, OMP_NUM_THREADS=1); the GPU
driver of step 5 also needs PyTorch 2.8 with CUDA.

## Contents
(a) `a_coefficients/`: the trial coefficient files `<name>_shape.npz` (spline knots and order, the coefficient of every
    radial x angular function, the fractional-power coefficients, k = 1/c_l, L, c_l and the origin radius).
    `MD5SUMS.txt` lists the md5 of every file as published and as verified. Eight files are byte-identical to the
    verified files (the candidate, its control, X2, F2, F0, F1, X1 and the start of X1). In the other files the field
    `recycle_step`, a solver restart vector that no evaluator reads, was removed to keep the folder small; every other
    field is unchanged. Start files of continued fits are not included: the m <= 200 starts are the m <= 150 ends with
    the new angular coefficients set to zero (`b_fit/make_angular.py`), and the shifted starts of the fixed-c_l rows
    are made by `b_fit/transplant.py` and `b_fit/make_fixc_start.py`.
    `a_generator/`: the generator that evaluates rho, psi, U and the residuals from a coefficient file.
(b) `b_fit/`: the Gauss-Newton / LSQR solvers (free and fixed-c_l: `long_solve.py`, `long_solve_fixcl.py`), the
    lead's between-node scan program `quick_scan.py`, the export program `export_fit.py` and auxiliary tools.
    `b_fit_domain/`: the same solver with bounded fit domains and the two-term closure (domain columns of 4.4); the GPU
    driver imports it. `b_fit_gpu/`: the GPU driver `gpu_long_solve.py`, the GPU port of the LSQR matrix-vector
    products `gpu_op.py` and its test against the CPU operator `test_gpu_op.py`.
(c) `c_diagnostics_code/`: the characteristic-defect code (`char_defect.py`), the original-form B_3 evaluator
    (`b3_ibp.py`) and auxiliary scan scripts. `c_diagnostics/`: their outputs for the trials of (a) (`*_scan.json`,
    `*_scan960.json` and related scans, `*_cd.txt`, `*_jsplit.txt`, `*_map.txt`, `*_b3.txt`); the larger JSON files are
    xz-compressed (`xz -dk c_diagnostics/*.json.xz` restores them). `c_farfield/`: the far-field diagnostic of 4.5 with
    its outputs.
(d) `d_evaluator/`: the separately written generator and residual evaluator (`code/`, with the wrappers
    `gen_audit.sh` and `extra_checks.sh`), auxiliary scripts of the verifier (`scratch/`), empty output directories
    (`runs/audit`, `runs/gen4`), the reference outputs of steps 1 and 2 on the candidate (`runs/reference`, with
    `README.txt` and `MD5SUMS`) and the verifier's record (`verification_record.md`).
(e) `e_independent/`: the independent discretization of 4.6 (`src/`, report `numerics_report.md`) and the real-space
    quadrature check of the velocity of 4.5 (`ray/`).
(f) `f_spec/`: the specification of the problem classes and diagnostics (`SPEC.md`) and the analysis notes behind
    section 3 (`analysis.md`). `f_referee/`: the questions put to the external referee and its answers, one directory
    each.
The records of the research run (work logs, job drivers, queues, per-run solver logs) are not included. The
verifier's record and the referee files were written during the run; directory prefixes of the machine used were
removed from them and from the scripts, so some auxiliary scripts name files by their bare names, and the
names of working files of the run that they mention (logs, notes, other reports) refer to files that are not part of
this folder.

## Names of the fits of the report
| report | file |
|---|---|
| candidate X3 (m <= 200, c_l fixed at 5.5753626) | `c6g_shape.npz` (md5 15f8095f7e79dbfa0c50d75e5fe8997a) |
| its equal-budget free control F3 | `c6gF_shape.npz` (md5 0398af3f08a2a4f75e42c846edbaa375) |
| X2 (m <= 150, fixed c_l) and its free control F2 | `s2g_shape.npz`, `seg3g_shape.npz` |
| X1 (CPU, fixed c_l) and its start (F0 moved by -1e-3 along the soft direction) | `fixc_c6f_m1.0e-03_shape.npz`, `fxs1_-1.0e-03_shape.npz` |
| F0 (free fit, 375 radial functions, m <= 150) and F1 (its segment 2) | `c6f_seg1_shape.npz`, `c6f_seg2_shape.npz` |
| fixed-c_l rows of 4.3 at c_l = 5.6004662, 5.5793640, 5.5783631, 5.5743631, 5.5723653, 5.5683739, 5.5604082, 5.5524653 | `fxv24g`, `fxu3g`, `fxu2g`, `fxm2g`, `fxn4g`, `fxn8g`, `fxn16g`, `fxn24g` (`_shape.npz`) |
| the two continued fits at 5.5604082 and 5.5524653 | `fxn16gb_shape.npz`, `fxn24gb_shape.npz` |
| the nested pair (m <= 200) at 5.6004662 and 5.5683739 | `nst24g_shape.npz`, `nsn8g_shape.npz` |
| resolution rows at the candidate's c_l | `fxd1g_shape.npz`, `fxb1g_shape.npz` |
| budget row (X3 continued 20750 iterations) | `c6g2_shape.npz` |
| m <= 250 row, its free control, its continuation with rows to 9000 L | `c6h_shape.npz`, `c6hF_shape.npz`, `c6h9000_shape.npz` |
| X3 continued with the inverse domain at 1e4 L | `c6gR4_shape.npz` |
| domain columns (rows to 90 L, 300 L, 9000 L), the free control and the continuation of the 9000 L row | `dom90g`, `dom300g`, `dom9000g`, `dom9000gF`, `dom9000g2` (`_shape.npz`) |
| free resolution study with m <= 100 (215, 244, 302, 375 radial functions) | `c6a`, `c6b_seg1`, `c6c`, `c6d_seg1` (`_shape.npz`); later segments `c6b`, `c6d`, `c6f`; `c6d_e1`, `c6d_e2` auxiliary states of the 375 basis |
| soft-direction study (244 basis, offsets along the tangent) | `tan_c6b_tan<offset>_shape.npz` |
| fixed-c_l studies on the earlier bases and continuations of X1 | `fixc_c6b_560*`, `fixc_c6d_m1.0e-03`, `fixc_c6f_m1.0e-03_s2`, `fixc_c6f_m1.0e-03_s2w`, `fxfr_c6f_m1.0e-03`, `fxt_s3cl_*` |
| solver-setting arms of 4.2 | `reo_plain8`, `reo_plain12`, `reo_reorth8` (`_shape.npz`) |
c_l of any file: `python3 -c "import numpy as np; print(float(np.load('a_coefficients/c6g_shape.npz')['c_l']))"`.

## Commands
Run every command single-threaded (`export OMP_NUM_THREADS=1`). `<coef>` is a coefficient file, `<tag>` any label;
the times are on one core of the machine of the run. Peak memory is up to 13.8 GiB (step 1 at 16875 x 768).

1. Residual tables of 4.4 by the separate evaluator (maxima of R/N_f and R/N_v by region, J, h(P) - 1):
   ```
   cd d_evaluator/code
   bash gen_audit.sh ../../a_coefficients/c6g_shape.npz c6g "7.652e-4 7.652e6 11250 384 479;7.652e-4 7.652e6 16875 384 479;7.652e-4 7.652e6 16875 512 639;7.652e-4 7.652e6 16875 768 959;7.652e-4 7.652e6 22500 384 479;7.652e-4 7.652e6 22500 512 639"
   ```
   2 to 8 minutes per configuration; output `d_evaluator/runs/audit/<tag>_N<N>_q<nq>_R<R>.json` and `.log`, to be
   compared with `d_evaluator/runs/reference`.
2. Identity c_l = (1 + psi_xy(0))/3, the identity-free root of h(P) = 1, the centre relations, the zeros of W on the
   axes, the verifier's B_3 estimator, the axis integral and the characteristic defect on 857 labels (same directory):
   ```
   bash extra_checks.sh ../../a_coefficients/c6g_shape.npz c6g "7.652e-4 7.652e6 11250 384 479"
   python3 vb3ibp.py ../runs/gen4/c6g_traces.npz
   python3 gen_shape.py ../../a_coefficients/c6g_shape.npz 7.652e-4 7.652e6 16875 384 ../runs/gen4/c6g.npz
   python3 vaxis.py ../runs/gen4/c6g.npz 479 ../runs/audit/c6g_ax.json
   python3 vchar_dense.py ../runs/gen4/c6g.npz 479 20 737 60 1e-4 ../runs/audit/c6g_jd2.json
   rm ../runs/gen4/c6g.npz
   ```
3. The lead's scans (whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P on the candidate):
   ```
   cd b_fit
   python3 quick_scan.py ../a_coefficients/c6g_shape.npz 32768 640 out.json
   python3 quick_scan.py ../a_coefficients/c6g_shape.npz 24576 960 out960.json
   ```
   Reference: `c_diagnostics/c6g_scan.json.xz`, `c_diagnostics/c6g_scan960.json.xz`.
4. The lead's characteristic defect (185 labels) and the original-form B_3 from an export (about 1.4 GB, regenerated):
   ```
   cd b_fit
   cp ../a_coefficients/c6g_shape.npz .
   python3 export_fit.py c6g 24576 576
   python3 ../c_diagnostics_code/char_defect.py c6g_fields.npz 20 185
   python3 ../c_diagnostics_code/b3_ibp.py c6g_fields.npz mu1only
   ```
   The "orig" lines of b3_ibp.py are the values quoted in the report; the "ibp" lines are not quoted.
5. Regenerating the candidate. X1 from its start on the CPU (1.8 h cap, 750 iterations), then X2 and X3 on the GPU:
   ```
   cd b_fit
   python3 long_solve_fixcl.py ../a_coefficients/fxs1_-1.0e-03_shape.npz X1_shape.npz --fix-cl --nr 20480 --nt 720 --hours 1.8 --inner 500 --check 250
   cd ../b_fit_gpu
   python3 gpu_long_solve.py ../b_fit/X1_shape.npz X2_shape.npz --nr 20480 --nt 720 --hours 4.9 --inner 2500 --check 250 --fix-cl --max-its 20750 --damping 1e-8
   python3 ../b_fit/make_angular.py X2_shape.npz X2m200_shape.npz 200
   python3 gpu_long_solve.py X2m200_shape.npz X3_shape.npz --nr 20480 --nt 960 --hours 4.9 --inner 2500 --check 250 --fix-cl --max-its 20750 --damping 1e-8
   ```
   F1, F2 and F3 follow the same chain from F0 (`c6f_seg1_shape.npz`) without `--fix-cl`; F1 is
   `python3 long_solve.py ../a_coefficients/c6f_seg1_shape.npz F1_shape.npz --nr 20480 --nt 720 --hours 1.8 --inner 2500 --check 250`.
   The domain columns continue X3 with the same GPU settings at `--nt 960` and `--fit-radius 90`, `--fit-radius 300`,
   or `--fit-radius 9000` with `--nr 24576`. LSQR paths differ at the 1e-4 level after hundreds of iterations, so a
   regenerated fit is not expected to equal the stored one digit by digit; every residual of the report is evaluated
   from the stored files by steps 1 to 4 and 6, 7.
6. The velocity check of 4.5 by real-space quadrature (about 32 minutes on the candidate), in `e_independent/src`
   (outputs of the run in `e_independent/ray`), with the coefficient file and the export of step 4 copied there:
   ```
   python3 raycheck.py cand c6g_shape.npz c6g_fields.npz out.json "Smax:1e18,smode:adapt,phimax:0.02,pcluster:1" full
   ```
7. The far-field diagnostic of 4.5, in `c_farfield` (it finds the generator in `b_fit_domain`):
   ```
   python3 far1_axis.py ../a_coefficients/c6g_shape.npz
   python3 far1.py ../a_coefficients/c6g_shape.npz
   python3 far2.py ../a_coefficients/c6g_shape.npz
   cd ../b_fit_domain
   python3 ../c_farfield/ptest.py ../a_coefficients/c6g_shape.npz 24576 576 1e7 out.json
   python3 ../c_farfield/band_nv.py ../a_coefficients/c6g_shape.npz 24576 576 <Rinv> out.json
   ```
