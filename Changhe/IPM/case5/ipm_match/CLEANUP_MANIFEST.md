# Cleanup record — 2026-11-05

## Scope

Cleaned the actual project at `/mnt/d/Changhe_D/PDE_exploring/Changhe/IPM/case5/ipm_match`. The requested `/mnt/d/Changhe_D/case5/ipm_match` does not exist. Git root is `/mnt/d/Changhe_D/PDE_exploring`; the project was untracked and there were no tracked working-tree changes before cleanup.

## Retained

Fourteen unchanged Python sources, totaling **78,485 bytes**, retain the original core and spectral solvers, Fourier products, Taylor/origin charts, far conditions, interface/jump calculation, Newton, sparse/local/endpoint solvers, and essential physical validation. Existing module paths were preserved. [README.md](README.md) lists their roles and fresh-start commands.

The only newly created active files are `README.md` and this record. There are no historical NPZ/NPY fields, factorization caches, environments, generated figures, logs, or Python caches in the active project.

## Archived

External archive, confirmed outside both the project and its Git repository:

```text
/mnt/d/Changhe_D/ipm_match_archive_20261105/
```

Moved **314 original files, 81,524,363 bytes**, preserving relative paths beneath `files/`. These include all seven numerical/operator NPZs, the old 448-mode state, scalar receipts/tables, reports and the four previous audit documents, duplicate snapshots, continuation/phase/precision/FFT experiments, and historical diagnostic/packaging/launcher sources. Unique algorithms remain recoverable externally; none was rewritten.

The detailed external `MANIFEST.json` records every archived original path, destination, size, reason, and SHA-256, plus fingerprints of the 14 retained sources. `VERIFICATION.json` records solver smoke results; `ARCHIVE_VERIFICATION.json` records checkpoint integrity checks. The archive did not exist before cleanup, and no existing archive was overwritten.

## Permanently deleted

**No files.** Only empty directories left by the moves were removed; their paths are recorded externally. No disposable cache files were present to delete. Uncertain historical/performance code was archived conservatively rather than discarded.

## Verification

- Every retained source has its original SHA-256. All 314 moved files were checked against their pre-move sizes and SHA-256 values.
- All seven archived NPZs passed ZIP CRC checks and NumPy loading; all 217 arrays were checked for valid non-object data and finite floating entries.
- An external environment at `/root/.venvs/ipm_match` supplies Python 3.12.3, NumPy 1.26.4, SciPy 1.14.1, and threadpoolctl 3.6.0. Imports and initialization now work.
- Fresh Taylor initialization (123 unknowns) and fresh spectral initialization (219 unknowns) passed with checkpoint loading explicitly disabled. `maxit=0` checks performed no Newton updates and did not produce a converged solution claim.
- Cartesian/polar origin discrepancy was `1.28e-16`; a Taylor Jacobian directional check differed from complex step by `7.98e-17`.
- The first Neumann jump remains unconstrained and a higher jump remains constrained. Small full-local, reduced-local, and endpoint-QR linear solves had residuals at most `2.22e-13`; a small physical residual-evaluator smoke check passed.
- No expensive solves, continuation, parameter scans, high-resolution validation, commits, or Git history changes were performed.

The retained solver is functional for fresh initialization and the tested small linear/validation paths. Convergence of a new nonlinear investigation remains to be established when that work is authorized. The base system Python still lacks numerical packages; use the external environment.

Known legacy references are documented in the README: the historical CLI default seed and the optional archived Green-format seed converter. No missing dependency remains on the tested fresh-start path. The need for advanced archived precision/performance methods at future resolutions is intentionally undecided.

## Size accounting

| Measure | Files | File-content bytes |
|---|---:|---:|
| Before cleanup | 328 | 81,602,848 |
| Active project after cleanup | 16 | 87,693 |
| Original files moved to external archive | 314 | 81,524,363 |
| Net bytes removed from active project | — | 81,515,155 |

The active project contains 14 original sources and two new documents. Detailed final statistics are also recorded externally. These totals exclude directory allocation and the external Python environment; filesystem disk usage can differ. The archive retains the moved data, so this is an active-project reduction, not a claim of freed total disk space.
