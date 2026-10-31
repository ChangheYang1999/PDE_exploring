# Independent segment-three sensitivity replay

Registered 2026-10-29T17:48:05.422459+00:00. The lead outputs at 17:42:37Z have been read; this is an independent reproduction of known claims, not a blind experiment.

Use the qualified independent_sensitivity_v1 implementation, with the same rectangular Householder phase complement and gesvd computation used in V379. Read the producer complete-Jacobian factors at P1 cumulative iteration 409 and P2 iteration 466 in place, and bind their full hashes to the lead input manifest. No large factor is copied. Verify the coordinate order, chain factors, positive scales, triangular factor, endpoint objective and complete-Jacobian labels before using the record.

Compare singular values, eta, gradients, all four coefficient truncation thresholds, reduced matrices, eigenvectors up to sign, predicted steps and decreases, and band shares with the unchanged lead tools. Keep the V379 tolerances: most reduced quantities relative 1e-4, eta absolute 2e-7, factor reconstruction 1e-11. Exact-rank and nonlinear stationarity claims remain outside this computation. A separate exact stored-value progress check decides the last-50 accepted transition conjunct. The 1e-3 absorption-warning predicate is checked directly for both columns.

One busy CPU35 task, one thread, no GPU. If inserted during the independent holdout queue, suspend its identified controller and child, record the real pause interval, run the bounded replay serially, and resume both in finally. No JavaScript/TypeScript, servers, remote compute, RLScience, Lean/Lake, or writes outside this side.
