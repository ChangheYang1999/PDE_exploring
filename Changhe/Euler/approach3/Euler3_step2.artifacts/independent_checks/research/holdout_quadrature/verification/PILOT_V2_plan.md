# Pilot v2 plan

Registered 2026-10-29T00:37:35.962546+00:00, before the pilot.

The original pilot failed its prerequisite and produced no holdout result. Keep it and the old grid-helper failures unchanged. Version2 uses the qualified long-double stable linear evaluator and the long-double full-space Green reconstruction of the same binary64 source data, with no imposed zero moments. It requires the original stable-linear, tensor-grid and metric qualifications, precise_grid_helpers_v1, and the analytic leading-tail branches of extended_tail_pressure_v1. The latter file also contains a failed raw-logarithmic control, which is disclosed and not used.

Run S01 with three radial nodes per domain and a fresh 24 by48 angular grid. Refine pressure from radial order12/angular40 by80 to radial16/angular48 by96, retaining identical holdout points. Use the saved coefficients unchanged. The angular truncation is2*lmax+6. Report source precision separately from reconstruction precision.

There is no new pass threshold: this pilot reports computed diagnostics, their pressure-refinement differences, and denominator warnings. It does not certify a Tier or continuous errors. If pressure refinement is material, investigate it before drawing a state-quality conclusion. Full validation remains pending as listed in the result schema.
