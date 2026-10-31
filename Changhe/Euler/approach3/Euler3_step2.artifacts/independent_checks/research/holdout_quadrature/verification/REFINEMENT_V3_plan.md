# S01 holdout refinement and common-domain plan

Registered 2026-10-29T00:46:32.831859+00:00, before execution.

Use the unchanged saved S01 full coefficients and parameters. Keep the sampled reference core radius from v2,0.4304351316933, so the dyadic and thin-shell domains are the same. Increase the holdout radial order from3 to6 and angular counts from24 by48 to42 by84; draw a fresh azimuthal phase with seed10290046. Refine pressure from radial16/angular48 by96 to radial24/angular64 by128. Keep the raw source moments, analytic leading-tail integration and qualified extended reconstruction. Source and field evaluation remain binary64, explicitly recorded.

Add the specification6.5 common physical shells [2^j R0,2^(j+1)R0], j=-4,...,8, with R0=0.3. Report RMS(R_u), RMS(U) and their ratio on every shell, without parameter-dependent row weights. An external reference-R0 argument fixes these domains when comparing inputs whose own R0 differs. These quantities use the already-qualified normalized-volume RMS formulas; the ratio is an additional report, not a new acceptance rule.

Compare v3 and v2 on their identical domains, and record changes rather than treating agreement as an error enclosure. If the change is material, refine the holdout radial rule again on the same domains. Pressure-refinement differences use identical points within each run. There is no new passing threshold or Tier claim. Centered balls, spatial vorticity and the remaining full validation remain separate.
