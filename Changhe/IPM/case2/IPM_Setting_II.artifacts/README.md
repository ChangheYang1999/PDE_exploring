# IPM Setting II: accompanying artifacts

These files accompany the report `../IPM_Setting_II.report.md`. The report's outcome is that neither admissible
endpoint was reached: there is no nonexistence theorem for the natural full-plane class and no YES candidate.
Consequently there is no candidate profile to regenerate and no candidate residuals to recompute. What is here is the
code behind the numerical studies of the report (Sections 5 and 8), the independent verifier's solvers and check
scripts, the lead analyst's exploratory forward-evolution code, and a small set of computed records. Everything here is
numerical evidence about specific discretisations or symbolic checks of individual identities; nothing here is a
proof, and the proofs printed in Section 9 of the report do not depend on these files.

All paths below are relative. Python 3.9 with numpy 2.0, scipy 1.13, sympy 1.14 and PyTorch 2.8 (float64) were used.
The GPU scripts use CUDA when available; most of them hard-code `device='cuda'` or `dev = 'cuda'`, which can be
changed to `'cpu'` (much slower).

## Layout

- `numerics/`: the numerical researcher's code (the code called LP1 in Section 8 of the report, and the spectral
  polar solver of Section 5.1(i)).
  - `code/ipm2polar.py`, `code/green_inverse.py`, `code/zetasolve.py`, `code/solve.py`, `code/landscape.py`: spectral
    polar discretisation (Fourier in th, Chebyshev in log(1 + r^2/L^2)), the per-mode full-plane inverse of the
    once-subtracted velocity law, a Green-function inverse used as a cross-check, and the Levenberg-Marquardt, Picard,
    homotopy and c_l-continuation drivers of Sections 5.4-5.7 (zetasolve works with rho = zeta^2).
  - `code/dynrescale.py`: the log-polar dynamic-rescaling probe of Section 5.1(iii).
  - `code/pfwd.py`, `code/pfwd_batch.py`: the forward reformulation of Section 5.8 (rho = r^p g on a log-polar grid,
    semi-Lagrangian transport, product-integration velocity; the batched class uses a prefiltered cubic B-spline
    interpolant).
  - `code/pfwd_exitmap.py`, `code/pfwd_exitmapb.py`: the exit-map fixed-point solver (exact characteristic map with
    the velocity of the current state, Anderson acceleration) used for the stationary states of 5.8(vi).
  - `code/pfwd_fp.py`, `code/pfwd_bnewton.py`, `code/pfwd_gnewton.py`, `code/pfwd_tangent.py`: Newton searches on the
    far-field datum and p (Sections 5.8(iv)-(vi), 8.5).
  - `code/pfwd_parity.py`: the parity-free tests of Section 5.8(vii) (datum with both parities, x-odd rows, linear
    response by GMRES).
  - `code/pfwd_diag.py`, `code/pfwd_diag2.py`, `code/pfwd_shoulder.py`: diagnostics (node strain m1, up-down
    asymmetry D, moment and continuation diagnostics of Section 8.4) and one datum family.
  - `tests/`: validation tests (manufactured solutions, inverse cross-checks, analytic benchmarks of Section 5.2 in
    `tests/bench_analytic.py`, moment identity of Theorem C) and the analysis and table scripts of the forward
    computations.
  - `runs/pfwd/par/`: the five records read by the quick check below (exit-sensitivity outputs ES256b, ES512, ES1024
    and the 1024-angle column pair PLM1024Ak6/Ak7 of Section 5.8(vii)).
  - `records/`: result records (JSON lines `*.out`) of the exit-sensitivity, closure and velocity-refinement tests
    at the parity-free base state, and in `records/r22/` the consistent-linearisation tests (LCK, LC, M1, M2); their
    response fields (`*_resp_b1.npz`, about 11 MB) are omitted for size.
- `verifier/`: the independent verifier's own code, written separately from the other two codes.
  - `code/derive_reduction.py`: symbolic check of the moving-centre reduction (Section 1).
  - `code/charsolve.py`: characteristic-marching transport solver with Gauss-Legendre radial panels, Newton-GMRES and
    pseudo-arclength continuation (Section 5.1(ii)); `code/run_char.py`, `code/newton_char.py`,
    `code/homotopy_char.py`, `code/forced_char.py`, `code/scan_cl.py` drive it.
  - `code/bs_cartesian.py`, `code/polar_inverse.py`: the Cartesian Ewald-split and polar full-plane inverses used to
    cross-check the velocity law.
  - `code/fwdstat.py` with `tests/fs_run.py`: the panel-grid stationary solver of the forward problem (the code called
    PG in Section 8).
  - `code/check_*.py`, `tests/v*.py`: the verifier's symbolic (sympy) and numerical checks of individual statements
    and proof steps, named by the number of the verifier's check and, where applicable, by the section of the draft
    they checked. Examples: `tests/v138_app90.py` (Section 9.0, Steps 1-7), `tests/v158_step7.py` (Section 9.2,
    Step 7), `tests/v122_app92.py`, `tests/v123_app93.py`, `tests/v127_app94.py`, `tests/v129_app95.py`,
    `tests/v135_app97.py`, `tests/v151_app98.py`, `tests/v154_app99.py`, `tests/v157_app910.py`,
    `tests/v161_app911.py` (drafts of Sections 9.2-9.11), `tests/v190_sec914_sym.py`, `tests/v191_sec915_sym.py`,
    `tests/v192_sec916_sym.py`, `tests/v197_sec917_sym.py` (drafts of Sections 9.14-9.17),
    `tests/fr47_sym.py` (the far-field correction for A = cos^2 th of Section 4.7). Several of these scripts were
    written against intermediate wordings of the report, and some read saved states or draft texts that are not
    included; the checks of the later proof sections were made mainly by hand derivation and are not all represented
    by scripts here.
- `analysis/explore/`: the lead analyst's exploratory code (the code called LP2 in Section 8): forward self-similar
  evolution (`pforward.py`, `pforward2.py`, `p0_forward.py`, `p0_forward2.py`), the fixed-point evaluator and Newton
  variants (`fpeval.py`, `fpnewton.py` and related), the exact characteristic test (`exactT.py`), the axis summary of
  the up-down asymmetry (`dsum.py`, `axcheck.py`) and the B-spline interpolant (`bspline_torch.py`).

Not included: the computed states and logs of the individual runs (several gigabytes in total), and the run
configurations that were not recorded in the scripts. Scripts that read a saved state (`runs/...npz`, `runs/...pt`)
therefore need a state produced first by the corresponding solver command; where an input state is not in this folder
the script cannot be run as it stands. Section 8.8 of the report lists the settings of the principal quoted states.

## Commands

Quick check of the numerical code (run from `numerics/`; about 3 minutes on one GPU). These are the four commands
whose outputs the numerical researcher recorded and, on a rerun near the end of the run, reproduced identically apart
from timing lines:

    cd numerics
    python3 tests/test_poisson.py     # manufactured decaying solutions: inverse and residuals (psi about 1.7e-10 at Nr 64)
    python3 tests/test_green.py       # collocation inverse vs Green-function inverse (8.4e-12 / 9.9e-12 / 2.2e-11 at Nr 48 / 64 / 96)
    python3 tests/pfwd_es_table.py runs/pfwd/par/ES256b.out runs/pfwd/par/ES512.out runs/pfwd/par/ES1024.out
                                      # exit-sensitivity table of the parity-free base state (Section 5.8(vii))
    python3 tests/pfwd_par_colcmp.py runs/pfwd/par/PLM1024Ak6_J.npz runs/pfwd/par/PLM1024Ak7_J.npz
                                      # 1024-angle column pair: true residuals 0.0361 / 0.16, x-odd relative difference 0.235

Analytic benchmarks of Section 5.2 and the moment law (from `numerics/`):

    python3 tests/bench_analytic.py                  # strain moments, cubic Taylor data, one frozen transport step
    python3 tests/kappa_scan.py 40 24 100 400 11     # moment-law pair over random nonnegative inputs (Theorem C)
    python3 tests/picard_map2.py 64 32 300 1         # one-step characteristic map of Section 5.3

Forced continuation in c_l of Section 5.7 (from `numerics/`; GPU, tens of minutes), then its per-stage table:

    python3 code/zetasolve.py --Nr 48 --Nth 32 --R 300 --cl0 2.0 --ay 1.5 --eps 0 --method lm --smooth --compat 10 \
        --maxit 40 --svd_cut 1e-11 --prefactor s --cl_path "2.0,1.9,1.8,1.75,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.05" \
        --name clpathS
    python3 tests/clpath_table.py runs/clpathS.log
    python3 tests/offnode_residual.py runs/clpathS_cl1.800.pt   # off-collocation residual of one stage

Forward evolution of Section 5.8 to a steady state (from `numerics/`; GPU, about 12 s per state at 661 x 256):

    mkdir -p runs/pfwd
    python3 code/pfwd.py p=0.5 Nr=661 Nth=256 lo=-12 hi=10 kind=cos2 ds=0.02 nsteps=1500 every=100 out=runs/pfwd/cos2.npz
    python3 tests/pfwd_node_diag.py runs/pfwd/cos2.npz   # near-node structure of the state

Independent symbolic checks (from `verifier/`; CPU, seconds to minutes each):

    cd verifier
    python3 code/derive_reduction.py      # the moving-centre reduction and the profile system of Section 1
    python3 code/check_struct_sym.py      # symbolic identities of the structure results
    python3 tests/v138_app90.py           # Section 9.0, Steps 1-7
    python3 tests/v158_step7.py           # Section 9.2, Step 7
    python3 tests/fr47_sym.py             # the far-field correction for A = cos^2 th

The numerical diagnostics printed by these commands are observations about the discretisations used. As stated in the
report, no state computed in this work passed the complete candidate verification package, so none of these outputs
is YES evidence in the sense of the task.
