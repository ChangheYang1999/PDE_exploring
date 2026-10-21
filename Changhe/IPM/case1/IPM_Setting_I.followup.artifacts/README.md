# Accompanying artifacts of the follow-up on the strong setting P_inf (IPM Setting I)

This folder accompanies section 6 of the report IPM_Setting_I.report.md (the strong setting P_inf, follow-up
investigation of 2026-10-20 to 2026-10-21). It holds only the follow-up's code and data. The first investigation's
artifacts (the P_2 candidate X3, its coefficient files, generator, fit code, diagnostics and the independent evaluator
of sections 4 and 5 of the report) are published unchanged beside it as `../IPM_Setting_I.artifacts/`.

The follow-up reached neither endpoint (no YES_inf candidate, no NO_inf theorem). There is therefore no new candidate
to regenerate; the programs here reproduce the analytic certificates and symbolic checks of 6.3, the numerical
researcher's full solves and diagnostics of 6.4 (question Q1), and the verifier's independent recomputations and proofs.

## Parts

| Folder | Content | Report items |
|---|---|---|
| `lead/` | The lead researcher's part: exclusion certificates (programs, inputs, outputs, derivations by external referees, a referee's rerun), the evaluators of the axis functional B_3, and symbolic and numerical checks. Its `README.md` lists every program with its command, run time and rerun result, and `SANITIZE_LOG.md` every edit made to the copies. | 6.3.1 (n), (o); 6.3.2; checks of 6.3.1, 6.4, 6.5 |
| `numerics/` | The numerical researcher's part: the whole-plane collocation solver with the canonical modal inverse, the characteristic-map formulation, dense Jacobians, Newton, constrained and Ritz tools; tests; the stored states of the five discrete systems and every diagnostic output; `COMMANDS.md` with the exact command sequences of the full solves. | 6.4, Q1 |
| `verifier/` | The independent verifier's part: separately written programs (whole-plane inverse, density reconstruction, residual evaluators, center and source checks) with their outputs, and the proofs of the statements attributed to the verifier, each topic with `PROOF.md`, code and verification records. | 6.2; verifier statements of 6.3 and 6.4 |

Each part has its own README with the details. All paths are relative. Paths inside the programs of `verifier/` are
relative to this top folder; those of `numerics/` to `numerics/`; those of `lead/` to the program file.

## Software

Python 3.9.25 with numpy 2.0.2, scipy 1.13.1, sympy 1.14.0 and mpmath 1.3.0 (lead and numerics; python-flint 0.6.0
for ball arithmetic; PyTorch 2.8.0 with CUDA 12.8 and one GPU for the numerics). The verifier's later programs used
Python 3.12.13 with numpy 2.5.0, scipy 1.18.0, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0 and PyTorch 2.13.0.
Run single-threaded:

```
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
```

## Commands

Programs overwrite their stored outputs; run them on a copy of this folder to compare. Each numbered recipe starts at the top of that copy; return there before starting the next recipe. All execution is local. Do not use JavaScript/TypeScript, start servers, or access the RLScience cluster.

The original section 5 recipes and parameter descriptions are retained in `FIRST_INVESTIGATION_REPRODUCTION.md`; those recipes require the separately published first-investigation bundle. The recipes below use this follow-up bundle.

Create the output directories used by the early verifier programs:

```bash
mkdir -p verifier/early_data/traces verifier/early_runs
```

1. Exclusion certificates of 6.3.1 (o) (lead part; run in this order, starting at the top of the copy):

   ```
   cd lead/exclusion_certificates
   timeout 540 python3 reference_fit/verification/fit_reference.py
   timeout 540 python3 reference_fit/verification/reconstruct_reference.py
   timeout 540 python3 raw_bounds/03-norm-and-radius/verification/rational_certificate.py
   timeout 540 python3 raw_bounds/03-norm-and-radius/verification/numerical_checks.py
   timeout 540 python3 raw_bounds/norm_repair/norm_repair.py
   timeout 540 python3 obstruction_certificate/verification/certify.py
   timeout 540 python3 radius_budget/verification/radius.py
   timeout 540 python3 trace_uncertainty/verification/analytic_bounds.py
   timeout 540 python3 trace_uncertainty/verification/compare.py
   timeout 540 python3 audit_rerun/audit_checks.py
   ```

   certify.py gives 0.2830400682 < B(A_0, e_0, w_0) < 0.2851567624; radius.py the radii 4.5e-6 and 5e-6;
   rational_certificate.py the radius 1e-6 at the computed parameters and 1e-8, 1e-7 at A = 4.

2. B_3 on the stored traces (6.3.2, lead part): `cd lead/b3_functional/b3infl && python3 b3core.py
   ../../exclusion_certificates/reference_fit/data/c6g_traces.npz` (see `lead/README.md` for `TRACE_DIR` and the
   other evaluators).

3. Symbolic checks of 6.3.1, 6.4 and 6.5: `cd lead/symbolic_checks && timeout 540 python3 <script>.py`; the table in
   `lead/README.md` gives each script's report item and expected result.

4. Numerics (6.4, Q1), from `numerics/` after `mkdir -p runs && cp data/* runs/`:

   ```
   python3 tests/test_model.py cuda 0
   python3 tests/test_model.py cuda 0.8
   python3 src/s4e_row.py runs/dnSB_n120m48.npz dnSB_n120m48
   ```

   The tests check the modal Poisson ODEs against quadrature, the identity for psi_xy(0), the transport residual and the
   Jacobian. The full solves from the seed X3 (`data/c6g_shape.npz`, md5 15f8095f7e79dbfa0c50d75e5fe8997a, the
   published candidate) to the stagnation states are the command sequences of `COMMANDS.md` (chain E2b for (120,48)
   and (96,40) at L = 4, 8, 16; chain K for (72,30); chain L for (84,35)); each needs the GPU and takes hours. The
   stored states are `data/dnSB_n120m48.npz` (md5 0234b3634f747b0a50386d0359bea823), `data/dnB_n96m40S.npz`
   (f5b77e128474f1f9da8e3051c22ad505), `data/dnB_n72m30S.npz` (c81d083063696cae2087d72351ea2526),
   `data/dnB_n84m35S.npz` (53d5486acd2ebdf91a401d4c374b28e3), `data/dnB_n96m40SL4.npz`
   (c103a60bbbf2279e7c21f4f5a2b580be) and `data/dnB_n96m40SL16.npz` (bc8c82ca4baaf6c000a144284ff21bec).

5. Verifier's recomputation of the published candidate X3 (6.2), from this top folder with one CUDA GPU (the program creates its output directory and saves axis data to `verifier/early_data/<tag>_eval.npz`):

   ```
   python3 verifier/early_code/run_eval.py numerics/data/c6g_shape.npz 12 0.25 2048 -5 12 x3_a
   python3 verifier/early_code/run_eval.py numerics/data/c6g_shape.npz 16 0.2 4096 -5 12 x3_b
   python3 verifier/early_code/run_eval.py numerics/data/c6g_shape.npz 12 0.25 2048 -4 10 x3_c
   python3 verifier/early_code/run_eval.py numerics/data/c6g_shape.npz 10 0.35 1024 -5 14 x3_d
   ```

   (arguments: panel order p, maximal panel width h in log r, angular nodes, log10 r_min, log10 r_max, tag). They
   print the residual maxima by region at the nodes and off the nodes, the identity (1 + psi_xy(0))/3 against c_l,
   x*, h(P) and the velocity at the center; the report's values are max R/N_f 6.8e-7 to 7.3e-7 and max R/N_v
   1.10e-6.

6. The verifier's other checks: one folder per topic in `verifier/` (reading order in `verifier/INDEX.md`), run from
   this top folder as described in `verifier/README.md`; the command sequences of its numerical audits are in
   `verifier/COMMANDS.md`.

## Not included

The research records of the run (work logs, notes, status files, job drivers and queues, run logs, report drafts),
backup copies of programs, PyTorch tensor files (stored Jacobians, regenerated by `numerics/src/jac_dense.py`), and,
in the verifier's part, per-piece intermediate outputs and 11 data files larger than 500 kB, all regenerated by the
programs. Absolute local paths in the copied files were replaced by relative paths; no computation was changed.

## Publication review corrections

Program paths to included reference fits and the candidate trace resolve within this bundle. Early verifier outputs use `verifier/early_data/` and `verifier/early_runs/`; their directories are created above. Other first-investigation traces are not included and require that separate bundle. Historical audit hashes identify the original reviewed bytes, as described in `verifier/README.md`; they are not checksums of edited publication copies.
