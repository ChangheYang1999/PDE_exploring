# P2 segment-two independent holdout reading guide

Written 2026-10-29T14:41:52.826501+00:00.

The saved FREE endpoint has c_l = 0.45272851087117016 and omega = 0.3040154299573543; the common start and FIXED endpoint have c_l = 0.45 and omega = 0.3. These are endpoint comparisons with unequal optimization budgets: 280 total iterations for FREE and 360 for FIXED. The earlier optimization ledger also records unequal sharing histories, so this table is not a matched-compute comparison.

The independent route evaluates the saved coefficients without refitting. Each holdout uses 2,751,840 points, 42 by 84 angular quadrature, fixed fresh azimuthal phase 0.2975612633975048, and two pressure quadratures. Field and source arithmetic is binary64; stable linear terms and pressure reconstruction use long double. The observed pressure changes do not bound quadrature or floating-point error.

| Family | Quantity | INITIAL | FIXED | FREE |
|---|---|---:|---:|---:|
| dyadic | rho_u_max | 0.0522678986361 | 0.0528135180252 | 0.0524658277059 |
| dyadic | sigma_u_max | 1.90888922465 | 1.92516374218 | 1.93563265032 |
| dyadic | weighted_absolute_residual_max | 1.92101371034 | 1.96680624243 | 1.96416243126 |
| dyadic | physical_residual_over_U_max | 1.04988907356 | 1.0588400582 | 1.05931656295 |
| half_offset | rho_u_max | 0.0717226561181 | 0.0682401781492 | 0.0676348259127 |
| half_offset | sigma_u_max | 1.60955091262 | 1.7107627897 | 1.71453359921 |
| half_offset | weighted_absolute_residual_max | 1.82629000674 | 1.94971420798 | 1.9469077765 |
| half_offset | physical_residual_over_U_max | 0.885253001942 | 0.940919534335 | 0.938315356002 |
| registered_core_ball | rho_u_max | 0.00165175754937 | 0.00161983109074 | 0.00162824647293 |
| registered_core_ball | sigma_u_max | 0.0746109527056 | 0.0736603194745 | 0.0746521859058 |
| registered_core_ball | weighted_absolute_residual_max | 0.103607113798 | 0.102158949071 | 0.103144081707 |
| registered_core_ball | physical_residual_over_U_max | 0.0410360239881 | 0.040513175711 | 0.0408550129474 |

FREE has slightly lower normalized rho_u than FIXED on both shell families, but higher sigma_u on both. On the standard dyadic shells FREE also exceeds the initial rho_u and sigma_u. Therefore this record does not establish a broad advantage for jointly optimizing the parameters. Sigma_u divides the residual RMS by the RMS of (1-c_l)U. It is distinct from the weighted absolute residual.

The registered origin-centered core ball has radius 0.14364049210478602/32. It does not replace the two displaced balls centered at the sampled vorticity maximum. Those checks are queued separately. The direct and composite unit-ball rules give different RMS values; their difference is a spatial-quadrature diagnostic and cannot be replaced by the much smaller pressure-level difference.

Both endpoint compact audits pass all 3100 controls, and the common-grid comparison passes 699 controls across 224 summary rows and 116 shell rows. The original scalars, both pressure levels, input hashes and all pair differences remain in `artifacts/P2_segment2_comparison_v1/`. Comparison JSON SHA256: 95e6c5ccae38cfe48ba08b220d0ab173bdbda912232ef4d66fbf4e3e4036e660. These observations are not stationarity evidence, continuous extrema, an exact Euler solution, or an existence proof.

Dated completion 2026-10-29T15:42:47.184678+00:00: the previously missing displaced-ball momentum measurements are now complete and audited for INITIAL, FIXED and FREE. See the [six-state augmented comparison](../../../artifacts/six_state_augmented_comparison_v1/COMPARISON.md) for the finite augmented maxima and full domain CSV. This resolves the missing sampled sets; cross-degree core resolution and final Phase IV acceptance remain OPEN.
