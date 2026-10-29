# Accompanying artifacts

This is the published subset supporting the accompanying report. The main search has
outcome C: no accepted Euler profile was found. The separate obstruction D concerns
uniformly decaying Cartesian C^2 axisymmetric profiles on R^3 with 0 < c_l < 1/2.
The smooth case c_l = 1/2 remains open. Floating-point checks of rejected states do
not constitute an existence proof.

## Exact commands for this subset

Run these commands from this directory. They require `sha256sum` and an existing
Python environment with NumPy, SymPy and PyTorch. The recorded environment is in
`numerical_code/env/pip_freeze_shared_interpreter.txt`; its relevant versions are
NumPy 2.5.0, SymPy 1.14.0 and PyTorch 2.13.0. The commands use CPU only, start no
server and do not launch optimization jobs.

```sh
export PYTHONDONTWRITEBYTECODE=1
export CUDA_VISIBLE_DEVICES=
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
sha256sum -c SHA256SUMS
python3 numerical_code/candidates/T1_ladder/L4rm5/field_eval.py
python3 numerical_code/tests/test_ops.py
```

The first command checks every listed file. The field evaluator compares the R5
export with its stored samples and prints maximum absolute differences; the final
review obtained 2.220446049250313e-16 for phi and 1.3322676295501878e-15 for q.
The operator suite completed with 68 passing checks and zero failures. These are
field-evaluation and operator checks, not a new reproduction of the full registered
Euler residual evaluation.

`START_HERE.md` indexes the mathematical arguments, numerical tables, exported
states, figures and validation records. `RUNBOOK.md` records the original campaign
commands and identifies procedures requiring the omitted run archive.

## Reproduction limits

`independent_validator_source/reproduce_r5.py` and the validator source are retained
for inspection. That historical wrapper expects the complete validation bundle,
its original directory layout, evidence records and checksum manifest. Those inputs
are not all included here, so the wrapper cannot run unchanged from this subset.
The report's full R5 rejection and resume-test results are historical validation
results, not results newly reproduced by the commands above. The complete run
archive, complete independent proof archive and external referee reports are also
omitted; the mathematical documents and validation record state their proof and
audit coverage.

## Larger retained files

The files exceeding 1 MB are data or a report figure, not scratch files or log dumps:

- `figures/independent_validation/ladder_l1_20261029T004517.856506Z/field_distribution.svg`
  is the vector version of figure F4, the swirl and poloidal field distributions.
- `numerical_code/configs/t1budget_seeds/c0.60.npz`,
  `numerical_code/configs/t1budget_seeds/c0.68.npz` and
  `numerical_code/configs/t1budget_seeds/c0.74.npz` contain the seed field grids used
  by the supplied configurations and source code.

`SHA256SUMS` covers every other file, including this README. Paths in the commands
are relative to this directory; scripts resolve their project data relative to the
script location or the documented working directory.
