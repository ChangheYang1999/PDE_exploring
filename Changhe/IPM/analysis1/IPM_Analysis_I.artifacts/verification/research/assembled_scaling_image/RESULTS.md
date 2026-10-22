# Complete saved-array results

UTC 2026-10-21T21:08:48.507563+00:00. These are rigorous finite-array enclosures from the complete computation. Acceptance still requires the actual model review and later verifier adjudication.

The 42 labelled pieces partition [0,260); all have 467 rows and 40 columns. All 881864 imported scalars agree between NumPy/Fraction and manual NPY/IEEE/fmpq decoding. The two exact summations agree on all 18680 entries. The supplement confirms 87 raw payload identities and 1866 exact positive row coefficients. The complete outward norm computations use Arb320 by nodal weights and iv100 by reversed edge sums, with 64 interval agreement checks. Four manufactured quadratic forms, eight IEEE boundary values, ten malformed parser cases and eight invalid range mutations also pass their intended tests.

S denotes the exact sum, Z the separately saved assembled array and D the saved direct array. The following are R_b(S-D)/R_b(D), not relative changes between two norm values:

| row | exact finite ratio enclosure |
|---|---|
| L2 | (0.0000536483196810, 0.0000536483196811) |
| L2q | (0.0000418540060235, 0.0000418540060236) |
| H1 | (0.0000578785928536, 0.0000578785928537) |
| H1q | (0.0000495301619260, 0.0000495301619261) |

The relative differences of the Z and D norm values are:

| row | enclosure |
|---|---|
| L2 | (0.0000008975601819, 0.0000008975601820) |
| L2q | (0.0000005683888104, 0.0000005683888105) |
| H1 | (0.0000022131398683, 0.0000022131398684) |
| H1q | (0.0000013612583832, 0.0000013612583833) |

Every R_b(Z-S)/R_b(D) is below 0.00000000001032, and max|Z-S| is below 0.000000000000007106. Both are explicit finite-data discrepancies, with no inferred production error model. The exact saved image difference satisfies max|Z-D| in (0.00000012705413363426, 0.00000012705413363427). The direct max is in (0.00196042261623195074, 0.00196042261623195075).

Nine original diagnostic tolerances fail and remain marked false: the four difference norms, the four normalized difference norms, and max_abs_img_diff. This refutes agreement at those proposed tolerances for the particular frozen Z/JSON pairing. It does not refute the reported approximate comparison at its published precision. The relative discrepancy between the JSON difference norms or ratios and the exact Z-based values is below 0.00000001518; the other norm values agree within 0.000000000000278 relative. The original attempt is preserved. No output tolerance was widened to conceal failure; the corrected checker returns each discrepancy and each original boolean.

The first proof reviewer requested exact summation of every entire rational Q. That extra requirement is unnecessary: the two implementations independently enclose the proved finite rational expression with outward arithmetic. All inputs, exact coefficient conversions and signs are checked. Overlap is a consistency test, not the proof of either enclosure.

The direct image bytes agree with the specified B2 archive. The historical origin of Z and the accumulation order used for its JSON are not authenticated. No constituent physical mode is independently reassembled here. Thus the numerics lane's physical assembler comparison remains floating and unreproduced, while its saved complete arrays now have an independent finite arithmetic check. There is no continuous norm, quadrature/tail estimate, exact scaling-image verification, inverse or IPM endpoint.
