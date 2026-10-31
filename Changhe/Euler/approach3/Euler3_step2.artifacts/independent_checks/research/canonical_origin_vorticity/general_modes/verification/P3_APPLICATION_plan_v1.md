# P3 exact-origin application

Use the already qualified general-mode origin reader on the immutable raw INITIAL, FREE and FIXED inputs of the matched P3 freeze. This extends the application explicitly registered in plan_v1.md; neither the formula, decoder nor tolerance changes. Register this file and the wrapper before opening the resulting origin values.

Require the completed matched-freeze receipt and its original input hashes. Run exact_origin_general_v2.py as a separate bounded process: maximum 512 MiB address space, 60 CPU seconds and 90 wall seconds. Record all rational interval endpoints for U, DU, Omega, DOmega and the origin vorticity residual. Retain signs and intervals that contain zero without changing precision or thresholds to obtain an exclusion.

Compare each exact interval midpoint against the independently differentiated Cartesian field at the origin, with the qualification threshold norm(error)/max(norm(reference),1e-30) <= 2e-12 for each of U, DU, Omega, DOmega and the vorticity residual. This empirical check is separate from the exact arithmetic. Recheck every input and source hash after both routes.

A nonzero residual component excludes only that exact canonical represented field as a smooth rotating Euler solution near the origin. It gives no global residual lower bound, no exclusion of nearby fields, and no profile nonexistence theorem. The raw and F-projected states are distinct; this application concerns the raw states named in the freeze. It is development work, not a replacement for the final frozen Phase IV cohort.

Use one CPU35 process at a time, nice10, OMP/BLAS one and CUDA_VISIBLE_DEVICES empty. Pause and resume the active owned controller with the qualified audit helper. No JavaScript/TypeScript, servers, RLScience cluster, remote or paid compute, GPUs, Lean/Lake, or writes outside the verifier side.
