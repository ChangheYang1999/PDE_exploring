# S01 axis-cap momentum plan

Registered before execution on 2026-10-29. This is a fixed-state diagnostic, not a Tier decision.

Use the two caps sin(theta)<0.05 on every standard and half-offset shell of the completed 12-node radial S01 holdout. Use 8 and 16 Gauss nodes per cap and 80 azimuthal nodes, at fresh fixed phases 0.287 and 0.731. Keep the radial quadrature fixed, so the reported refinement is angular only. Evaluate U, DU, Omega, DOmega and stable linear terms with the qualified long-double tensor route.

Reuse the completed fine pressure source from holdout_S01_v5_cpu.json, with its exact saved nodes, weights, projected source remainders and leading-tail coefficients. Reconstruct the same full-space Green pressure at the exact panel-edge radii. No interpolation, source-moment constraint, pressure boundary, or new harmonic correction is introduced. Source projection remains binary64; arithmetic reuse is not another pressure-accuracy test.

Before the axis evaluation, compare reconstructed P and grad P against the saved fine pressure arrays at five radii and three directions. Require relative vector differences at each point at most 2e-12, with the scale of each nonzero reference value; report zero-reference differences absolutely. This checks reconstruction and provenance, not continuum accuracy.

Report all five-term momentum ratios, absolute residuals, divergence, vorticity ratios and observed angular-grid changes. Reference V118 for the existing pressure refinement, whose original directions differ from these caps. Preserve all input hashes. Do not call the caps a full spherical shell.
