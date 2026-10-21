# Fixed-c_l corrections on withheld points

Date: 2026-10-20T19:51:23.734012+00:00. Verdict: CONFIRMED numerical finite-sample measurements; no endpoint.

The frozen independent corrections were fitted on 58 prescribed physical points. The independent paired whole-plane inverse was then evaluated on 84 different prescribed points, with 4096 angular nodes, radial order 28 and log-panel width .08, exterior cutoff 1e30. The normalization below is recomputed for each field. No numerical researcher's inverse or solver was imported.

| Grid | Base max abs(R)/N_f | Corrected max | Base RMS | Corrected RMS | Improved/worse |
|---|---:|---:|---:|---:|---:|
| n96m40S | 0.00274939062504 | 0.0016835821716 | 0.000749991665335 | 0.000290133344118 | 50/34 |
| n120m48_S | 0.00229954757285 | 0.00114210545176 | 0.000468830772675 | 0.000201155682993 | 57/27 |

The corrected maxima occur at (10.8053652282,5.21958640933) for 96x40 and (7.44606476890,.897841554667) for 120x48. They exceed 1e-3. Some samples worsen. The 58 fitting-point maxima, .0009829284 and .0001790104, therefore understate the largest measured residual over the additional sample set.

The paired quadratic expansion agrees with direct residuals to 1.6e-16 in fixed base units. Cartesian step refinement changes normalized residuals by at most 4.54e-10, and independent analytic gradients change them by at most 3.68e-10. Exact exterior velocity bounds propagated using numerical gradients contribute below 4.70e-15 at these points. These are separate sensitivity channels, not a rigorous bound on interior inverse quadrature or a uniform residual certificate.

The frozen corrected center has nonzero forbidden fifth-degree angular coefficients and a nonzero exact transport determinant, so neither fixed field has a smooth center or satisfies the exact transport equation with a C3 velocity. The new exact whole-plane center-moment calculation also excludes literal equality in the stored c_l identity, with defects about -1.3614e-14 and -1.1185e-14; this supersedes earlier floating differences near machine precision and is not a significant residual obstruction. The moment certificate's independent code review remains pending. No statement excludes a smooth limiting solution.

Inputs, hashes, individual points, residuals, derivative differences and quadratic terms are in withheld.json and withheld_summary.json. The proof and optimization protocol are ../PROOF.md.
