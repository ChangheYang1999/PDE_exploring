# Source-specific CPU stable momentum check

Registered before execution on 2026-10-29, using the actual UTC creation record in artifacts/stable_momentum_cpu_v1_preparation.json.

The existing G6 CPU adapter compares a direct Cartesian momentum identity formed from production field values. It does not differentiate the stable linear implementation used by Problem.evaluate. This separate check closes that coverage gap without changing either adapter or any threshold.

Use the immutable cpu_v1 production snapshot, fixed reduced coefficients, both manufactured fields (all modes at c_l=0.45, omega=1; even modes at c_l=0.42, omega=0.3), and three points per radial group. Radii over R0 are 1e-7, 1e-4, 0.02, 0.15, 2.3, 127, 4096, 16384, 65536. Angular nodes are selected with seed 2910202641 before results. The production grid field, stable linear term, and nonlinear contraction are evaluated and differentiated with torch.func.jvp. The nonlinear contraction is exactly the expression in Problem.evaluate. Pressure is excluded.

Evaluate the independent Cartesian basis freshly at 70 digits. Compare U, DU, their two parameter derivatives, the stable linear term and its two parameter derivatives, and the two pressure-free momentum derivatives. Apply the existing G6 rule: relative L2 error at most 1e-10 when the absolute-term-sum condition estimate is at most 1e4; otherwise absolute L2 error at most 1e-14 times the term-sum scale. Linear-only comparisons are an additional diagnostic using the same rule, not a replacement for the full pressure-free momentum derivatives. Save all numerical values and scales. Audit the record separately using Decimal arithmetic and source hashes. No pressure or weighted objective claim follows.

Run only while the current numerical process and its sleeping handoff are paused with identity checks; resume both in a finally block. No GPU, JavaScript/TypeScript, servers, remote compute, cluster access or Lean builds.
