# Result and proposed correction

The independent diagnostic completed2026-10-21T16:34:53.575856Z in35.47seconds, using one thread and no producer imports. It reconstructed four smallest Fminus vectors with both20- and32-point radial Gauss rules and the exact sparse trigonometric transform. Both rules agree at the printed digits. This is floating evidence, not rigorous integration or an infinite-tail bound.

| Family and row mode | Saved m=0 squared projection | Saved frequency1,3 fraction | Independently evaluated full Gram-source fraction |
| --- | ---: | ---: | ---: |
| M24/s8 H1 | 0.8627268516330306 | 0.8686696517296857 | 0.8686696517295548 |
| M24/s8 H1q | 0.8055331599669888 | 0.8095467940043288 | 0.8095467940043325 |
| M16/s16 H1 | 0.8916910947291276 | 0.8980797438644411 | 0.8980797438644150 |
| M16/s16 H1q | 0.8303342850023315 | 0.8343874245209748 | 0.8343874245209721 |

Each saved projection is below its corresponding saved harmonic fraction. The same-norm nesting theorem therefore encounters no inconsistency in these saved numbers. The report's approximately81percent value for the M24 H1-row direction is contradicted by its saved profile. The correct artifact value rounds to87percent. Approximately81percent belongs to H1q, a different vector. The copy-error interpretation is inferred from the matching values, not proved as an account of the author's editing process.

The source profile evaluator truncates the KP/TAU angular coefficients to26modes at M24 and18modes at M16. The source Gram uses260modes. Including all source modes changes the first harmonic fraction by at most about1.31e-13 in these four floating diagnostics, and restores the energy to the saved hGh at about machine precision. This is an implementation distinction but does not explain the six percentage point report mismatch. No rigorous bound on that small truncation difference is claimed.

The m=0 projection itself has not been independently recomputed here, only checked as an exact saved binary64 scalar and placed under a proved nesting theorem. This audit does not accept its pseudoinverse numerical stability, the admissibility of encoded discontinuous columns, the finite-section spectrum, a refined-section limiting value, or an infinite-dimensional inverse.
