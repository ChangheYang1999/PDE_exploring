# Six 48-point-quadrature re-solves: independent verification

Written 2026-10-22T06:15:35.170767+00:00. Verdict: CONFIRMED as the finite observations and exact literal-field obstructions below; REFUTED as six literal unforced B2 profiles. The general B2 question remains OPEN.

The complete informal proof is PROOF.md. The six inputs and 24 supporting files were frozen at 2026-10-22T05:53:45.205281+00:00, before computation. The sequential independent pipeline completed at 2026-10-22T06:07:51Z. Its full-plane PDE evaluation took 814.424588 seconds. The separate metadata and exact witness consumer passed 284/284 controls in 0.747811 seconds (2026-10-22T06:15:34.163382+00:00 to 2026-10-22T06:15:34.911171+00:00). The first run passed 265/266: its sole mistaken expectation was that the one-inner-iteration lineage-2 rerun changed its vorticity array. That array is bitwise unchanged. Both original control and correction are retained.

## Independent PDE and center checks

Each state uses 15,456 points on 161 radii, 1e-5 through 1e8, both x signs and both axis directions. The verifier uses its own adaptive physical-log-radius Green inverse over the whole plane and seven-point Cartesian differences of the raw represented fields. The fixed source is evaluated in its native source basis. No NUM code was imported or executed. The two steps h=2e-5 max(1,r) and h=1e-5 max(1,r) give at most 6.12182749e-10 difference in the reported maxima of normalized residuals. This is sensitivity, not an error enclosure or a supremum certificate. No denominator floor is used. The precise Cartesian and divided fields, absolute maxima and maximizing points are in verification/GLOBAL_RESIDUALS.csv; all radial bands are in REGIONAL_RESIDUALS.json and .md.

The defining B2 velocity is beta X+B[Omega]. The separately labeled forced velocity adds lambda B[f]. Their normalized divided residuals must not be conflated. The exact center consumer independently reloads the binary coefficients and computes rational B-spline moments.

| State | Forced F | Forced G | B2 F | B2 G | Exact saved forced m, rounded | Exact self center F ratio, rounded |
|---|---:|---:|---:|---:|---:|---:|
| quadB32_beta3p062 | 0.0676676502 | 0.108550912 | 0.729557961 | 0.743668413 | -9.40197975e-08 | 8.85308738e-08 |
| quadB40_3076_beta3p076 | 0.0560409696 | 0.120490051 | 0.726935258 | 0.954271394 | -3.56807952e-07 | 3.31605792e-07 |
| quadB40_3092_beta3p092 | 0.0868834804 | 0.151217688 | 0.724154747 | 0.965594334 | -1.57451374e-06 | 1.44186032e-06 |
| quadB48_3062_beta3p062 | 0.00452306826 | 0.0115948049 | 0.729557839 | 0.452346595 | -5.98127012e-07 | 5.63207791e-07 |
| quadB48_3092_beta3p092 | 0.0189634276 | 0.04225604 | 0.72415463 | 0.702572155 | -8.74850626e-07 | 8.01144619e-07 |
| quadL2B40_3085_beta3p085 | 0.000247828174 | 0.000253199795 | 0.744872156 | 0.419876053 | -7.79963638e-07 | 0.636970206 |

Every exact self thermal center ratio is strictly positive. Every state therefore fails the defining PDE, independently of finite-grid sampling. The first five retain a0=1.011258, so they also retain that normalization defect; the final state has a0=1. No convergence to a zero-forcing state is inferred from a small forced residual.

## Exact tails and inverse

For every field, separate rational Laurent evaluations confirm nonzero H0, ET, DT, EO and DO, together with simple zeros of the source stream at both axis angles. Since 3<beta<4, the leading self thermal residual power 1-3/beta and next forced power 2/3-2/beta are positive and distinct, above the decaying remainder 1-4/beta. Hence the absolute thermal residual is infinite on the whole plane, for both defining and forced equations. The result concerns each literal spline field, and does not preclude a nearby corrected smooth field. There is no physical truncation wall at the map scale L.

A separate inverse-constant certificate and its consumer give the following rational negative intervals. These are properties of the stored field, not estimates of a limiting continuum branch.

| State | Certified C2 interval |
|---|---|
| quadB32_beta3p062 | [-5149.015, -5149.014] |
| quadB40_3076_beta3p076 | [-5514.655, -5514.654] |
| quadB40_3092_beta3p092 | [-6004.355, -6004.354] |
| quadB48_3062_beta3p062 | [-5140.086, -5140.085] |
| quadB48_3092_beta3p092 | [-5983.681, -5983.680] |
| quadL2B40_3085_beta3p085 | [-417.562, -417.561] |

## Saved-stage comparisons

All six new logs specify ng_quad=48, while none of their archives records ng_quad. They accept the inherited lambda at secant zero, with a finite permissive objective acceptance factor 1e9, inner tolerance 3e-5 and outer tolerance 1e-5. The source coefficients and source geometry are bitwise unchanged in every pair. All temperature vectors change. The five lineage-1 vorticity vectors change; the lineage-2 vector is unchanged after one inner iteration. These facts establish neither a new root nor a bound on its displacement.

| State | Inner iterations | Objective increase, percent | Logged m | Exact saved m minus logged m, rounded |
|---|---:|---:|---:|---:|
| quadB32_beta3p062 | 8 | 0.47473531 | 9.25289907e-08 | -1.86548788e-07 |
| quadB40_3076_beta3p076 | 8 | 1.5435037 | -1.34376644e-07 | -2.22431308e-07 |
| quadB40_3092_beta3p092 | 9 | 1.65488333 | -1.4313999e-06 | -1.43113839e-07 |
| quadB48_3062_beta3p062 | 4 | 3.44115434 | -5.75942452e-07 | -2.21845604e-08 |
| quadB48_3092_beta3p092 | 8 | 3.50014097 | -4.21214425e-07 | -4.53636201e-07 |
| quadL2B40_3085_beta3p085 | 1 | 0.0266241276 | -7.51333943e-07 | -2.86296954e-08 |

The logged mismatch is the last pre-update stopping value. The saved-field mismatch is separately recomputed and differs by up to 4.54e-7. Thus the statement that the logged values have absolute value below 1.5e-6 is true, but it must not be applied to every saved-field value: the 40-mode beta3.092 field has saved absolute mismatch 1.5745137e-6. The last, lineage-2 objective increase is 0.0266 percent, outside the 0.475 to 3.50 percent range for the five lineage-1 fields.

This packet does not certify the numerical lane's runtime interpolant or its 12-versus-48-point runtime velocity comparison. A difference between two quadrature orders is not an error bound relative to the exact inverse. The new numerical lane wording of 06:03 makes this distinction; its runtime numbers require a separate independent reproduction. Root-shift, discretization-convergence and unforced-profile claims remain OPEN.

## Verification record and dependencies

- CONFIRMED: six archive identities, source and geometry preservation, inherited lambda and logged acceptance, distinct saved and logged strain.
- CONFIRMED: exact nonzero self-center defects; exact leading thermal residual witnesses and infinite absolute whole-plane thermal residuals; certified negative inverse constants.
- CONFIRMED as floating-point observations: independent finite-grid residuals and step sensitivity, with the stated limits.
- REFUTED: each literal frozen archive as an unforced B2 profile.
- OPEN: solver runtime-interpolation error, exact scalar root shifts, continuum convergence and general smooth B2 existence/nonexistence.

Earlier independent manufactured tests and analytic dependencies are identified in PROOF.md; no new tests are claimed for unchanged code. The complete input hashes, code hashes, rational certificates and raw-array reductions remain alongside this summary. The broader run has no decisive endpoint and no T_end here.

Actual Opus5.5 reviews499/500/502 were fully adjudicated in verification/OPUS_ADJUDICATION.md. The models assessed mathematical arguments and context, not the unseen artifacts; all numerical and exact-data verdicts remain the verifier's independently established results.
