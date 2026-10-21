# Verifier's part: independent checks of the follow-up on the strong setting P_inf

This folder holds the independent verifier's separately written programs, their outputs, and the proofs of the
statements attributed to the verifier in sections 6.3 and 6.4 of the report, with their symbolic or numerical checks.
None of these programs imports the numerical researcher's solver; the numerical researcher's stored states are read as
data from `../numerics/data/`.

## Reading order

1. `FINAL_VERIFIER_FINDINGS.md`: the verifier's final synthesis (completed numerical checks, analytic findings, exact
   scope and the remaining gaps; neither YES_inf nor NO_inf established).
2. `EVIDENCE_MAP.md`: maps the requested verifier checks to their proofs and their scope.
3. `INDEX.md`: the topic list in reading order.
4. One folder per topic (for example `inverse/`, `fifth-order/`, `weighted-source/`, `finite-angular/`,
   `far-field-trace/`, `r12-global-sign/`, `five-grid-comparison/`): each has a standalone `PROOF.md` (statement,
   hypotheses, argument, scope), its programs in `code/`, and its outputs and acceptance records in `verification/`
   (and frozen inputs in `data/` where used). Several topics also hold `RESULTS.md` or `ACCEPTANCE.md`.
5. `early_code/`: the verifier's programs from the first sessions of the follow-up (before 2026-10-20T13:06Z), among
   them the separately written generator, inverse and residual evaluator used for the recomputation of the published
   candidate in section 6.2 (`vgen.py`, `vinv.py`, `vres.py`, `run_eval.py`), the B_3 estimators (`b3_*.py`) and
   the symbolic checks (`symb/`, `d44/` to `d52/`, `o8/` to `o18/`, `f28/`, `frozen/`).

Historical verification entries (AV1, AV2, ...) refer to the verifier's dated research record; it is not published here, and the verdicts the report relies on are
stated in the report itself (sections 6.2 to 6.5 and the verification timeline). Some files also contain checks made
after the report's content was frozen (for example the (108,44) state in `fifth-grid/` and `five-grid-comparison/`);
the report does not use them.

## Running the programs

- Software: Python 3.12.13 with numpy 2.5.0, scipy 1.18.0, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0 and, for the
  physical inverse, PyTorch 2.13.0 with one CUDA GPU. `early_code/` was run with Python 3.9.25, numpy 2.0.2,
  scipy 1.13.1, sympy 1.14.0 and mpmath 1.3.0.
- Single-threaded: `export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1`.
- Run every program from the top of the accompanying artifacts folder (the folder that contains `lead/`, `numerics/`
  and `verifier/`), for example

  ```
  python3 verifier/inverse/code/realspace.py
  python3 verifier/inverse/code/strain.py numerics/data/dnB_n96m40S.npz verifier/grid-states/verification/dnB_n96m40S_strain.json --nang 2048 --order 24 --panel .12 --rmax 1e30
  ```

  File paths inside the programs and records are written relative to that top folder (`verifier/<topic>/...`,
  `numerics/data/...`, `lead/...`). Inputs that a program reads from `numerics/runs/` are the files of
  `numerics/data/` (copy or link them, as the numerics README describes). The included candidate trace is read directly from
  `lead/exclusion_certificates/reference_fit/data/c6g_traces.npz`. Other first-investigation traces are not included.
  Before using the early programs, run `mkdir -p verifier/early_data/traces verifier/early_runs`; their output paths are relative to the top folder.
  The historical ten-trace studies still require the other traces from the first-investigation bundle.
- The programs write their outputs into the `verification/` folder of their topic and overwrite the stored files;
  run them on a copy to compare.
- `COMMANDS.md` lists the exact command sequences of the numerical audits that were run through shell sequences (the
  grid, domain, fixed-c_l, far-row, far-field-trace, physical-correction and inner-cutoff topics). The launcher
  `fifth-grid/code/launch.py` calls such an excluded shell script and does not run as published; use the commands of
  `COMMANDS.md` instead. For the other programs, the usage line, `PROOF.md` or the `protocol.json` and
  `acceptance.json` records of the topic name the inputs.

## What was changed or left out for publication

- Absolute local paths were replaced by paths relative to the top folder, and the verifier's internal folder prefix of
  the topics and the run's internal labels of the three researchers were replaced by `verifier/`, `numerics/` or
  `lead-run-records/` (and by the word "verifier" in comments). Paths of material outside these artifacts are written as
  `verifier-run-records/`, `lead-run-records/`, `first-run-records/` or `other-investigation-records/`; those records
  are not published (the first run's published artifacts are `../IPM_Setting_I.artifacts/`). Because of these edits,
  the SHA-256 pins recorded inside some JSON files no longer match the edited files; they identify the original bytes.
- Not included: copies of report drafts audited by the verifier, model-review exchanges, run control (process records,
  job launchers, shell scripts, and a one-off script that edited the team's notes), run logs and standard-output captures, PyTorch tensor files (`.pt`), diff files,
  per-piece intermediate outputs of batched computations (their combined outputs are included), and 11 data files
  larger than 500 kB (sampled action matrices, direction arrays and fit arrays; regenerated by the programs of their
  topics).
- No computation or mathematical content was changed.
