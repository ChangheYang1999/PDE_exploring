# Independent CPU Jacobian checks

Prepared on 2026-10-29, before any result from this CPU driver. The exact preparation timestamp and source hashes are in `artifacts/complete_jacobian_cpu_v1_preparation.json`.

The first execution waits for the inherited single-core holdout sequence to finish and for the production arithmetic choice and source snapshot. This preparation does not release the optimizer or transfer an earlier result to new code.

Use `scripts/verify_complete_jacobian_cpu_v1.py` through `scripts/python.sh`. The driver requires CPU 35, one thread, explicitly hidden GPUs, an immutable stable production snapshot, the chosen precision mode, and the dated specification. It checks the input exchange, driver, independent helpers, finite-difference helpers, production sources and manifest, and specification identities again at every saved checkpoint. An unchanged invalid geometry or parameter-domain flag cannot count as a valid stencil. It uses the imported state's parameters unless a shifted pair is explicitly supplied. It neither normalizes the input nor patches the production evaluator.

Three outputs have distinct meanings:

- `Jcw` uses the actual production forward-mode columns and compares them to fresh residual values with the closure target and patterns held, with weights and pressure tables recomputed.
- `Jc` uses a reverse-over-reverse graph derivative plus the pattern contribution. This is an additional complete-derivative diagnostic, not the worker's matrix assembly.
- `worker_Jc` calls the actual worker helper with actual selected Jcw columns. Its selected coefficient and parameter columns are compared against the self-consistent residual. It is tested in optimizer coordinates, which are the helper's native coordinates. The other matrix columns are not certified by this test.

The five-step ladder, 1e-6 whole-column threshold, 1e-5 group thresholds, fixed floor, Richardson condition, active-set comparison, and registered coefficient step rescaling are retained. Both unscaled and scaled ladders are saved when they differ. A comparison also runs with zero floor to distinguish a relative pass from an absolute-only pass. A missing consecutive valid pair is OPEN. A finite ladder does not rule out smaller-scale structure or switches between sampled points.

Every stencil residual is retained. To limit disk use, arrays are stored in separate compressed, hashed NumPy archives without also producing a duplicate combined archive. A check stops before exceeding its two-GiB data budget or the side launch margin. Incomplete artifacts are retained.

`scripts/audit_complete_jacobian_cpu_v1.py` reconstructs second- and fourth-order differences from these saved values and recomputes the decisions independently of `fd_validation.py`. Its integrity verdict and the underlying derivative-test verdict are separate: a faithfully recorded failed derivative test may pass the archive audit. The auditor does not reconstruct the physical pressure or validate the accuracy of the production discretization.

Before real execution, qualify archive decoding, a correct smooth polynomial, an intentionally biased derivative, a floor-only case, an active-set switch, unchanged but invalid pressure geometry, a corrupted stored difference, and a corrupted source identity. Save all controls and results. These are software controls, not Euler evidence.

For full-release evidence, use at least the two required lineages and two distinct parameter pairs under the lead's frozen-source decision. Carry earlier independent results forward only after checking the identity of every relevant source. Any untested change remains OPEN. Pressure accuracy and the independent physical residual are handled by the separate holdout sequence.

The CPU driver avoids duplicate complete closure evaluations. A Jcw stencil still calls the actual `residual_vector_rebuild_wd`; its independent switch recorder receives separately evaluated pressure tables and nonlinear weights. The base-point switch metadata and independent weight error must exactly match those obtained from the full objective. For complete derivatives, the actual `objective_at` residual returned with its metadata is reused. This changes neither the tested functions nor the finite-difference points.
