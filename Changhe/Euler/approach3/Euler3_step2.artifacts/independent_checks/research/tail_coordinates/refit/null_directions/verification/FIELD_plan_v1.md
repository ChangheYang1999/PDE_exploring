# Fresh field comparison for the three frozen raw refits

This is a development diagnostic. The failed pilot and V491 coefficient findings are already known. Use only V491's immutable source and raw-refit coefficient exchanges. Independent velocity evaluation imports no producer field evaluator.

Use physical-volume normalized quadrature on the thirteen shells [0.3*2^j,0.3*2^(j+1)], j=-4,...,8. The two quadrature levels are (radial,polar,azimuthal,phase)=(4,18,40,0.361927) and (8,32,64,0.827351). Keep every source and target at its saved binary64 physical parameters. Compare raw refits with their source and with the source coefficients retained at target parameters. Report separate synthetic unit-F scalings explicitly, without calling them actual optimizer starts.

The self-refit is tested against a maximum physical-volume shell relative velocity discrepancy of 1e-10. Passing means only velocity agreement on these fresh finite grids. For nonself refits record every shell discrepancy, with no success threshold. Report the independently evaluated F norm and its discrepancy from the producer's raw F-norm record, without assuming that cancellation-prone coefficient sums meet a fixed relative precision. Remove masked l=1 E entries in a temporary evaluator copy and verify that the velocity values are unchanged. Qualify the velocity-only contraction against the full independent evaluator at two radii and allow 1e-13 relative discrepancy. Store exact input and source hashes and actual times.

Uniform azimuthal counts exceed twice the largest carried azimuthal degree; physical radial weights include r^2. These finite comparisons do not control spatial derivatives, pressure, Euler residuals or coefficient conditioning. No field sample from this test belongs to the final Phase IV cohort.

Registered 2026-10-29T22:33:58.165758+00:00
