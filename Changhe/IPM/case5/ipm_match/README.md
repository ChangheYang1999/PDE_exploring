# Stationary IPM matching solver — fresh start

This project contains the unchanged solver sources and validation dependencies. Historical fields, scans, advanced experiments, reports, and caches have been archived outside the repository. No old solution is needed to initialize a new problem.

## Source layout

| Path under `inputs/base/` | Purpose |
|---|---|
| `newton_run/core/bvp.py` | Exact angular Fourier products, two-domain log-radius equations, Hermite–Simpson discretization, Newton, sparse solves, and jump/response calculations. |
| `newton_run/core/origin_manifold.py` | Finite nonlinear Cartesian Taylor expansion. |
| `newton_run/core/taylor.py` | Joint solution for the field and free Taylor coefficients; quadratic far closure. Main fresh-start API: `solve_taylor`. |
| `newton_run/vendor/` | Required `ipm_bvp.py`, `nonlinear_bvp.py`, and local origin-chart dependency used by the spectral implementation. |
| `newton_run/validation/audit.py` | Independent physical transport/Poisson residual evaluation. |
| `ipm_reconstruction/spectral/spectral.py` | Fourier–Galerkin/Gauss spectral-element solver, matching, Newton, and sensitivities. |
| `ipm_reconstruction/spectral/{polar_origin,stage,endpoint}.py` | Polar Taylor chart, reduced local solves, and Python/SciPy endpoint QR. |
| `ipm_reconstruction/spectral/{collars,compare_fields,qualify}.py` | Origin/far extensions, field comparisons, and acceptance checks. |

There are 14 Python files. Both local copies of `origin_manifold.py` are retained because the two existing import layouts use them; their contents are identical. Other duplicate snapshots are archived.

The equations use `u=(-psi_y,psi_x)` and `-Delta psi=rho_x`. Core variables are `(f,g,p)` with `rho=r*f`, `psi=r^2*g`, `p=g_z`. Spectral variables are `(A,G,U)` with side-dependent scaling and `U=r^(-sigma)*psi_r`. Matching leaves the first even Neumann jump `J2` as an **outer-minus-inner output**; a small discrete residual does not establish `J2=0` or a rigorous global profile.

## Runtime

Tested with Python 3.12.3, NumPy 1.26.4, SciPy 1.14.1, and threadpoolctl 3.6.0. A working environment was created **outside the repository** at `/root/.venvs/ipm_match`. From this project's root:

```bash
source /root/.venvs/ipm_match/bin/activate
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export PYTHONPATH="$PWD/inputs/base/newton_run/core:$PWD/inputs/base/ipm_reconstruction/spectral${PYTHONPATH:+:$PYTHONPATH}"
```

On another machine, create an external virtual environment and install `numpy==1.26.4 scipy==1.14.1 threadpoolctl==3.6.0`. No environment, datasets, or generated numerical output belongs in this source directory.

## Initialize without a checkpoint

This small smoke check constructs a fresh Taylor model and its equations; it performs no Newton step or factorization:

```bash
python -B - <<'PY'
import numpy as np
from taylor import TaylorModel
model = TaylorModel(c=2., a=1., n=4, m=4, li=2., lo=4.)
y = model.seed_T(None)
r, jac, _, _ = model.whole(y, 1., True)
assert np.isfinite(r).all() and jac.shape == (len(y), len(y))
print('Fresh initialization OK:', len(y), 'unknowns')
PY
```

## Start a new solve when ready

Use `guess=None`; the following is a small procedural example, not a validated parameter choice or a computation performed during cleanup:

```python
from taylor import solve_taylor
field = solve_taylor(c=2., a=1., n=4, m=16, li=2., lo=12.,
                     guess=None, maxit=8, tol=1e-10, verbose=True)
print(field['ok'], field['res'], field['J'])
```

The spectral solver can take this newly generated dictionary as a seed:

```python
from spectral import Spectral
solver = Spectral(c=2., a=1., nf=4, ng=4, p=4,
                  mi=4, mo=8, li=2., lo=12.)
refined = solver.solve(field)
```

Check convergence and physical residuals before interpreting any scalar. Keep future saved fields, logs, and factor snapshots outside this source tree. `spectral.audit` accepts a spectral field dictionary; the validation module's `audit` accepts a saved field path.

Two legacy references remain in unchanged source: the spectral CLI's default historical `--seed` path is unavailable, so use the API above or explicitly supply a newly generated seed; its optional `density_green` seed converter requires the archived Green implementation and is outside the retained fresh-start path. Standard initialization, native LU, reduced stages, and the retained endpoint QR do not require that converter or compiled helper libraries.

See [CLEANUP_MANIFEST.md](CLEANUP_MANIFEST.md) for archive location, verification, and scope.
