# Finite pressure cutoff scan

Registered 2026-10-29T12:12:53.777374+00:00, before the scan.

Use the captured qualifier-v4 dd_pressure argument statements verbatim through AST extraction. Evaluate their high and low words on the frozen full quadrature geometry prepared in V263 for S01_shift_a z_c and S05_shift_c physical c_l and z_c. Include all21 points per stencil set, all37 pressure degrees,51 evaluation radii, and every quadrature point selected by the original interior/exterior masks. Include wr, moment and sfac exponents separately. These are argument scans, with no exp, trigonometric evaluation, Green contraction, residual or derivative ladder.

For each family and point, check finiteness, count arguments selected by the high-word cutoff, retain the nearest high words on both sides, the corresponding paired argument and original indices, and the maximum absolute low word. Use Fraction to enclose log(10^(-250)) with N=256 in the standalone proof, and compare d>B+E exactly. No tolerance is tuned after viewing the result. If a strict inequality fails, report OPEN and retain its witness. Require zero auxiliary-factor cutoff counts to justify the current kernel-only replacement.

Bind the source snapshot, source AST, exact input geometry and all physical parameters in hex. The future qualifier's actual60 point records must agree with these parameter bits and geometry. The saved geometry was extracted from byte-identical production pressure/radial helpers, with named configuration and fixed quadrature; a final qualifier record has not yet been produced. The result is conditional on this source/configuration tie.

GPU7 is authorized and has75.55GB free at12:11:50Z. Use at most4GB of live tensors, chunk2048 quadrature nodes, CPU35 and one thread. Pause the current P2 controller and child during this bounded scan; automatically resume them on completion/failure. Timeout540s. Only this side is written. No JavaScript/TypeScript, servers, remote or paid compute, RLScience cluster, or Lean/Lake.
