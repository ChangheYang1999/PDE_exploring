# CPU closure-table check

Registered 2026-10-29T01:07:36.377329+00:00, before running the new harness.

Capture every actual angular table consumed by first_correction_graph, first_correction and carried_patterns for the immutable S01 and S05 inputs on the CPU candidate snapshot. The model's main grid is reduced only to avoid constructing unused tables; each closure function constructs its unchanged 22 by 42 grid. Preserve the captured coordinates, modes, derivative orders and route names. Repeated inputs must produce bitwise equal tables.

Use the independently qualified 70-digit normalized Cartesian recurrence from normalized_angular_recurrence/PROOF.md. Check every unique captured entry at its exact binary64 coordinates. Retain the registered entrywise tolerance 1e-13 and the denominator max(abs(reference),1e-13 times the maximum reference magnitude for the same degree and derivative order). Check exact-zero groups separately.

Count eval_Y calls on the three executed closure paths and compare the graph target with first_correction to relative tolerance1e-12. These are local consistency checks, not a substitute for a complete-gradient or worker-Jacobian test. The candidate snapshot is immutable but is not yet the released source. Compare hashes again after the production freeze.
