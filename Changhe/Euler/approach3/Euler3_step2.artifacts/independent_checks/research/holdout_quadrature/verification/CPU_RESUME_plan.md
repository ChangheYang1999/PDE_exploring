# CPU continuation after GPU revocation

The GPU update of 2026-10-29T00:57:59Z revokes every GPU from this side. The running v4 process disappeared after its field checkpoint and before its first pressure result. Preserve its incomplete JSON and field arrays. No pressure or complete holdout verdict can be drawn from v4.

Continue the registered v4 quadrature on CPU only, with one thread and CPU 35. Reuse its saved U, DU and stable linear arrays after checking their hashes and the exact directions and radii. The CPU pressure calculation recomputes the source on the unchanged quadrature. No GPU may be opened. Record the mixed device provenance explicitly.

Before continuation, compare CPU U and DU with saved GPU field values at a deterministic sample of 12 radii and all 3528 directions. Use the original tensor-grid tolerance 1e-10. Compare CPU projected source coefficients at eight deterministic nontail nodes from the v3 finest source checkpoint with the saved GPU projections, at the original projection tolerance 1e-13 relative to the full coefficient vector. This is a sampled device regression, not a new quadrature claim.

Cache each CPU projected source batch by the exact input state, source code, directions, projection matrix and radial nodes. Reuse a batch only when its stored inputs and hash key match. The cache changes neither the mathematical rule nor the summation inside a batch. Write cache files atomically. Preserve the prescribed two pressure levels and composite unit-ball rule. Further resumptions must use the same cache and source manifest.

The elapsed time for the continuation is reported separately from the interrupted run. No stopped or waiting interval is counted as active computation. No acceptance threshold changes.
