# Partial S01 vorticity holdout plan

Registered before implementation and execution of this diagnostic. The timestamp is recorded in the adjacent registration.json.

Prerequisites are the passing Cartesian spatial v2 qualification and the passing potential-identity tensor/scattered evaluator qualification. Use the exact immutable S01 coefficients at their saved parameters, without refitting or regauging.

Use two levels: 4 then 8 radial nodes per domain; 16x32 then 32x64 fresh full-sphere directions. Report standard and half-offset dyadic families, common physical shells with R0=0.3, the registered origin and core balls, and |y|<1. Keep the reference core radius 0.4304351316933 fixed to match the momentum pilot.

For the two axis caps sin(theta)<0.05, use 4 then 8 Gauss nodes per hemisphere and 16 then 32 azimuthal nodes, with the same radial refinement. Evaluate cap portions of every standard shell and report their normalized volume ratios separately.

For centered balls use the sampled maximum and a_eff from the immutable S01 momentum v2 artifact, and radii a_eff/2 and a_eff/4. Use 4 radial nodes with 8x16 directions, then 8 with 16x32 directions. A batched scattered evaluator avoids allocating a full Hessian at each point.

Report the five-term ratio, nonlinear ratio, single-term ratio, raw residual and vorticity RMS, divergence, and direct-versus-stable linear curl differences. At y=0 report Cartesian values and the pressure-independent residual without claiming a full Taylor audit.

For a common finite-ball comparison use a partition of |y|<1024 consisting of the innermost standard core ball, dyadic shells up to radius1024, and a final partial shell if needed. Combine squared shell norms with physical volumes; never sum normalized shell means without volumes. Record the exterior as omitted. Report quadrature changes between matching domains. No new acceptance threshold is selected from these results.

The thin far shells beyond the currently qualified spatial radius65536R0 are omitted from this partial diagnostic. They require separate extended far qualification. This script does not perform pressure or momentum evaluation and does not establish any Tier status.
