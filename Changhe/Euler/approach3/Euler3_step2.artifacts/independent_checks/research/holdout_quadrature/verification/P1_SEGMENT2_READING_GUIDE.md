# P1 second-segment independent comparison

Recorded 2026-10-29T14:07:50.490873+00:00. Numerical verdict V326. The exact finite quadrature statement and proof are in [PROOF.md](../PROOF.md).

FREE lowers the sampled maximum momentum ratio rho_u on the standard and half-offset shells relative to FIXED. Their FREE/FIXED ratios are 0.974620796158 and 0.931810126604. The absolute residuals give a mixed result. For example, the dyadic weighted absolute maximum is slightly larger for FREE, and both optimized states have a larger physical residual RMS in the small core ball than INITIAL. A smaller denominator-normalized ratio alone does not establish a smaller physical residual.

The states are retained INITIAL, the FIXED current endpoint after360 accepted iterations, and the FREE current endpoint after228. Parameters are FIXED(0.45,1) and FREE(0.4489870053700033,1.2625881450841698). The optimization histories have unequal accepted counts and elapsed times, with the reported P1 sharing change after the control finished. This is an endpoint comparison on common quadrature, not an equal-time causal performance estimate.

| Domain family | INITIAL rho_u max | FIXED rho_u max | FREE rho_u max | FREE/FIXED |
|---|---:|---:|---:|---:|
| physical_common | 0.0470178597628 | 0.0440291210032 | 0.0417173963666 | 0.947495553307 |
| dyadic | 0.0460426501257 | 0.042696190719 | 0.0416125953915 | 0.974620796158 |
| half_offset | 0.0463007181803 | 0.0430585809331 | 0.0401224217507 | 0.931810126604 |
| registered_core_ball | 0.00560326159341 | 0.0176531160595 | 0.0194080308111 | 1.09941104708 |
| unit_ball | 0.0388905394817 | 0.0351811213962 | 0.0338164631744 | 0.961210496776 |
| unit_ball_composite | 0.0389278342023 | 0.0356396794596 | 0.0339682091942 | 0.953100861434 |
| origin_ball | 0.00297141978907 | 0.0160996582376 | 0.0188579207561 | 1.17132429011 |
| far_thin | 1.84394960434e-10 | 2.03976738883e-10 | 1.64083529283e-10 | 0.804422750269 |

| Domain family | INITIAL weighted absolute max | FIXED weighted absolute max | FREE weighted absolute max |
|---|---:|---:|---:|
| physical_common | 0.424247794635 | 0.500188915096 | 0.497086464869 |
| dyadic | 0.433042335041 | 0.514013519646 | 0.514729199951 |
| half_offset | 0.418734049712 | 0.450318160447 | 0.449252101527 |
| registered_core_ball | 0.0177021378357 | 0.0706087595381 | 0.0670098421331 |
| unit_ball | 0.0668282612187 | 0.0749870064198 | 0.0760901640256 |
| unit_ball_composite | 0.0662646673679 | 0.0754098532117 | 0.0758060209456 |
| origin_ball | 0.00926284647918 | 0.063732963025 | 0.0642274822734 |
| far_thin | 0.0406196267773 | 0.0460248193695 | 0.0456614378612 |

The shell weight is(1+r_k)^(2 alpha+1), alpha=(1-c_l)/c_l, and changes with c_l. For the origin-centered balls r_k=0, so their weighted absolute entry equals physical residual RMS. The small registered core ball is B(0,0.4304351316933/32), radius0.013451097865415625; the origin ball has radius0.4304351316933/256. Neither is a ball centered at the vorticity maximum. Domain counts, bounds and exact field quadrature are unchanged from the [segment-one guide](P1_SEGMENT1_READING_GUIDE.md). Both endpoints have the same complete radial and angular point/weight hashes as INITIAL.

Pressure is recomputed independently from saved coefficients with20/32 radial nodes and48x96/64x128 angular source points, phase0.417. This table uses the higher pressure level. All174 pairwise residual-RMS changes exceed the sum of their two measured pressure-gradient changes. The largest change/difference ratio is0.05123748334118139, in the outer far-thin FREE versus INITIAL comparison where the physical difference is only1.348003634413132e-24. For FREE versus FIXED alone the largest ratio is0.00044908310878925383. These are measured refinement changes, not continuum error bounds.

The complete [comparison](../../../artifacts/P1_segment2_comparison_v1/comparison.json) has SHA256 72a8a3e5194d8f946f8d9fe7447187acd15161bf8dac3d50ca313b67231f0ace,697 provenance/geometry controls,224 summary rows and116 domain rows across two pressure levels. Each endpoint's compact audit passes3100 controls. It checks saved grids, selected witnesses and scalar identities; the independent scientific driver performed the field and pressure evaluations. Full field arrays are not retained. FIXED completed2026-10-29T13:44:26.926028Z in1091.000535s; FREE completed2026-10-29T14:02:57.371143Z in1100.435599s. Those measured elapsed times include recorded audit pauses.

This is a development holdout and partial momentum/pressure check. The full registered a_max still requires translated balls and resolution conditions. Vorticity residuals, stationarity, final unseen Phase IV points and Tier requirements are separate. No exact Euler solution or basis-resolution floor is inferred.

The single-term ratio sigma_u = RMS(R_u)/RMS((1-c_l)U) is distinct from the weighted absolute residual. At higher pressure quadrature its dyadic maxima are INITIAL 0.4319991253341032, FIXED 0.45401117004250496, FREE 0.4603225809331302; half-offset maxima are 0.3997296062068746, 0.3909661646546755, 0.3916432565856983. Both full sigma_u^max and full a_max require the missing registered core-resolved momentum sets. V330 verifies this mapping and these finite family values.

Dated completion 2026-10-29T15:42:47.184678+00:00: the previously missing displaced-ball momentum measurements are now complete and audited for INITIAL, FIXED and FREE. See the [six-state augmented comparison](../../../artifacts/six_state_augmented_comparison_v1/COMPARISON.md) for the finite augmented maxima and full domain CSV. This resolves the missing sampled sets; cross-degree core resolution and final Phase IV acceptance remain OPEN.
