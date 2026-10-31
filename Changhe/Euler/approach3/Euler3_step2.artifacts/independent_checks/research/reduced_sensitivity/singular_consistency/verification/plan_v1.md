# P3 singular-value discrepancy diagnostic

Registered 2026-10-29T21:45:52.155678+00:00, after the P3 FREE endpoint auditor failed its unchanged relative 1e-12 largest-singular-value comparison, but before reading its actual discrepancy. Preserve artifacts/jc_endpoint_P3_v1/audit.json and its failed check. Do not reinterpret that failed tolerance as a pass.

Bind both published and frozen EVAL JSON and complete R archives. Compute singular values with LAPACK gesdd including vectors, and a second values-only gesvd computation. Require relative largest-value agreement <=1e-12 between the two CPU methods; empirical Frobenius relative reconstruction and orthogonality defects <=1e-11. Record the actual producer discrepancies regardless of whether they pass. Check unit column norms and the producer's scaling code. No full Jacobian rebuild, GPU, or inferred rank. Review the proof in ../PROOF.md before coding; its operator-norm enclosure is a mathematical identity, not a rigorous bound from this binary64 diagnostic.

CPU35, one thread and one busy process, 240 seconds maximum under the owned-controller pause wrapper. Keep all outputs in this side. No JavaScript/TypeScript, servers, RLScience, remote compute or Lean/Lake.
