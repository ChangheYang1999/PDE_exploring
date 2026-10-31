# S01 radial refinement and composite unit-ball rule

Registered before implementation and execution of v4. See registration_v4.json for the real timestamp and file hash.

The v3 evaluation used six Gauss nodes in normalized volume on each domain, with42x84 angular points. Compared with v2, its unit-ball residual RMS changed by12.4percent and its single-term ratio changed by18.1percent relative to v3. Some nonmaximal dyadic-shell residual norms changed by15 to19percent. Pressure-refinement changes were much smaller. These facts motivate a radial check, without changing any acceptance threshold.

Keep the same42x84 directions, azimuthal phase, seed10290046, reference core radius0.4304351316933 and common physical reference R0=0.3. Double the radial node count from6 to12 on the existing domains. Retain the two pressure levels16/48x96 and24/64x128 so their computed difference is available at the new points.

In addition to the existing single-rule unit ball, add a composite rule for exactly the same physical ball |y|<1. Partition it at the reference radius r_core/32 and its successive doubles up to1. Apply the same12-node normalized-volume rule on each subdomain. Multiply each panel's weights by its volume fraction and concatenate the points. The total weights are positive and sum to one. This is an integration refinement on the existing field, not a change in the basis, domain, norm, gauge, or objective.

Compare the simple12-node ball with the composite ball, and compare v3 with v4 on every matching domain. If the simple rule remains unstable, preserve it and identify it as unresolved. The composite rule is not an error enclosure. Further refinement or a separate integration method is required before using a value near a decision threshold.

Do not modify any accepted evaluator dependency during the job. Preserve every output and source manifest. This remains a partial momentum diagnostic.
