# Initial-state displaced-ball application, version 2

Registered 2026-10-29T15:10:18.442331+00:00, after admission preflight failed and before any new field evaluation. The v1 preflight correctly rejected the legacy two-file P1 exchange. Its log remains at logs/initial_centered_application_preflight_v1.log.

P1 INITIAL is the frozen Euler3 coefficient exchange, whose exact coeffs.npz and meta.json SHA256 values are already bound by the accepted initial holdout. It has no saved_full_vector.npz. The new verify_centered_holdout_v3.py admits this one exact legacy path and two-file digest map in addition to the unchanged four-file exchange contract. No arbitrary incomplete exchange is admitted. Its field, pressure, quadrature and metric code are identical to v2; source binding adds this plan. P2 uses the modern four-file exchange. Qualification checks the actual inputs, mutation rejection and unchanged evaluator AST.

Freeze each center and a_eff from the accepted P1/P2 initial holdout. Evaluate both a_eff/2 and a_eff/4 balls, both pressure levels and both geometric rules. Keep every result; apply the same separate 10 percent node-doubling checks on residual and linear-term RMS. Run serially after the segment-two centered queue exits, CPU35, one busy worker and thread, GPUs hidden,60-minute per-state watchdog. No JavaScript/TypeScript, servers, remote or paid compute, RLScience cluster, or Lean/Lake. Write only this side.

Extend only the source-admission branch of the existing centered auditor and finite aggregator to accept v3 after qualification. Preserve all earlier results. These development measurements are not Phase IV validation, continuum enclosures, or evidence of cross-degree resolution.
