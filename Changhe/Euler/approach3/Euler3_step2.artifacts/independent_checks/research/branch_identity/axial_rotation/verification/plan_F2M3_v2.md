# P1 s4 versus F2 m3 independent rotation diagnostic

This prospective extension uses the unchanged Fourier and geometric-rotation controls of plan_v1.md on the V647 inputs in artifacts/high_pair_field_v2. The exact proofs in ../PROOF.md and ../../logarithmic_twist/PROOF.md apply unchanged. No fitted rotation changes the registered saved-phase branch rule.

Disclosed producer observation: the lead reports a best rigid-rotation distance about 0.1406 for this pair and a coefficient-rotation angle about -0.204 radians modulo pi; shell angles have increments about -0.0448 radians per doubling. These observations are comparison targets, not tolerances or tuning inputs.

Use V647's exact saved endpoints and its three spatial grids 6/24/48, 12/42/84, 24/64/128, with phases 0.617293, 0.284719 and 0.936157. The original field imports and source hashes must remain unchanged. Retain the original 8192-angle complete finite search, 60 golden-section steps, all original control tolerances and the empirical Lipschitz lower estimate. Do not import producer field or rotation code. The calculation is a fresh independent field evaluation, not a replay of producer shell values. Bound it to 240 seconds, with one CPU35 computation and the pressure controller safely paused and resumed; the prior instance used 137 seconds. Any timeout is retained and does not justify an unchecked result.

Report global and shell minima as supplementary numerical observations. Spatial and finite-search error checks are empirical, not interval enclosures for the continuum field. No Euler solution, common family or mathematical branch-count conclusion follows. CPU only, one thread, low priority; no JavaScript/TypeScript, servers, cluster, remote compute, Lean/Lake, or writes outside this side.
