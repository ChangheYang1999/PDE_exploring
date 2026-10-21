# Verification record and reproduction

The mathematical certificate inputs are exact decimal strings, interpreted as rational numbers. All proved bounds on transcendental expressions use `mpmath.iv` with outward interval arithmetic. Every integrated Taylor remainder is bounded on its entire interval, not estimated from samples. Saved interval endpoints are exact rational numbers reconstructed from the interval library's binary endpoints.

The new proof code is under `01-obstruction/verification`, `02-radius/verification`, and `03-trace-uncertainty/verification`. Input tables stay in JSON. The previous reference-relative estimate is copied, with its digest, to `02-radius/verification/reference_estimate.md`.

Reproduce the certificates from the `fred23` directory, in this order:

```sh
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python answer/01-obstruction/verification/certify.py
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python answer/02-radius/verification/radius.py
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python answer/03-trace-uncertainty/verification/analytic_bounds.py
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python answer/verify_artifacts.py
```

The separate numerical comparison was also executed:

```sh
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python answer/03-trace-uncertainty/verification/compare.py
```

The programs set a 1.9 GB address-space limit, disable parallel numerical threads, and use CPU computation only. They do not create servers, use JavaScript/TypeScript, or access the RLScience cluster. Outputs are written only below `answer/`. No packages were installed.

The final certificate run and artifact audit are recorded in `verification.log`.

What is proved:

- \(0.2830400682<B(A_0,e_0,w_0)<0.2851567624\), \(0.40222790015<g_0(1)<0.40222790016\), and the four displayed parameter derivative bounds.
- The entire inventory used in the reference-relative estimate, including origin remainders, whole tail intervals, endpoint data, and parameter margins.
- The exact quadratic budgets for both closed balls, including the norm-conversion alternative.
- The exact differences of the first three free Taylor coefficients, the norm conversion, the conditional analytic continuation bound, and the interval arithmetic evaluations of that bound.

What is numerical only:

- The suprema in the pairwise norm-distance table.
- The K12/K18 obstruction values and all their differences, and the extra printed digits in the fitted obstruction value.
- No certified pointwise sign condition \((H_-)\) is asserted.

The nonlinear source endpoint theorem in the supplied report is an analytic dependency, stated explicitly in the exclusion proof. Open-axis smoothness is retained as a hypothesis to avoid silently relying on the report's unchecked propagation citation. The numerical certificates neither prove an exact profile exists nor prove that an exact trace lies in any exclusion ball.

Opus 5.5 collaboration could not take place: the existing Python Bedrock profile failed to obtain credentials before model discovery. There was no second-model review or silent model substitution.
