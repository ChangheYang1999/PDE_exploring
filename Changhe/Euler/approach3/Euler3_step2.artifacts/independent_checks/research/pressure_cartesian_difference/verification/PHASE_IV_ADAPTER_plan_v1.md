# Frozen-cohort Cartesian pressure adapter

Registered 2026-10-29T22:48:17.735618+00:00, before any final cohort or final sampling draw. Read ../PROOF.md, S01_plan.md and ../../holdout_quadrature/verification/PHASE_IV_plan_v2.md first. This is an implementation extension of the proved finite-difference identities, with no new threshold or error enclosure.

Use the exact, unchanged frozen coefficient exchange selected for the strongest supported state or states. Its primary momentum record must pass the real frozen-cohort auditor. Use the separately frozen unsigned64 Cartesian seed. From numpy default_rng(seed), draw three normal coordinates a,b,c, form the three directions proportional to (a,b,c), (-b,c,a), (c,a,-b), then draw one uniform pressure azimuthal phase. These three directions are correlated signed permutations, not independent draws. Their construction retains shared stencil radii while giving fresh points. No field value enters the sampling. Reject a zero/nonfinite vector rather than changing the rule.

Use twelve base points, at radii R0 times .03,.3,3,30 along those directions. The three h levels are R0 max(1,r/R0) times .04,.02,.01. Evaluate all444 Cartesian stencil points and retain full arrays. Coalesce only roundoff-equivalent radii under the already qualified32eps rule. Include every grouped radius as a Green-integral breakpoint and report the reconstruction discrepancy.

Pressure grids remain16/48/96 and24/64/128. Reconstruct the full-space raw source tr(DU DU), with no imposed zero moments and with the complete remainder after leading-tail subtraction. The pressure source tensor is binary64; Cartesian DU, angular synthesis, stencils and Green reconstruction use the qualified long-double route. Disable the optional on-disk angular cache.

Report absolute Poisson defects, their ratios to squared DU Frobenius norm, absolute/relative gradient differences, all h levels and both pressure levels. A zero denominator gives an undefined ratio plus its absolute error, never an invented zero or infinity. Preserve all refinements; do not select the most favorable h after evaluation. These are finite consistency checks and supply no derivative supremum or rigorous quadrature error bound.

The scalar/array auditor independently reconstructs seeded geometry and stencil formulas, checks91 exact monomial controls, input and source identities, pressure settings, every stored ratio and refinement. Qualify both a legacy-geometry full replay and fresh-geometry controls before final use. A legacy replay is development only and is rejected by the final wrapper. The wrapper requires all sources and qualification evidence in the pre-entropy binding and an audited primary record, shares the side execution lock, uses CPU35 with one thread and a finite deadline, and preserves partial failures.

No JavaScript/TypeScript, servers/listeners, remote or paid compute, RLScience cluster, GPU, Lean/Lake build or write outside this side.
