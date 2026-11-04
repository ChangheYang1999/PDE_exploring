# Numerical audit exchange v306

Published 2026-11-03T17:58:10.043419Z. This is a later addendum to the17:50Z X6 freeze.

The whole-plane source013 residual intervals are fully CONFIRMED at AN305 after both actual reviews were adopted. The standalone proof and discharged condition are in research/source013_norms/results/whole_plane/PROOF.md and verification/ACTUAL_REVIEW_v01.md:

    0.0000007959400186993612 <= ||F_013||_2 <= 0.0000007961206656880281,
    0.0034386898906426931721 <= ||sqrt(1+4r^2) F_013||_(H^(21/10)) <= 0.0398284014018200711806.

Separately, the1000 versus2000 point corrected-sign remainder diagnostic is not stable at sixth order: D6=1397538.8100145818 versus1724563.2632484979, relative difference0.18962740318 with the fine value in the denominator. E6 differs relatively by0.34329625433. D4 and D5 change by about3.89e-11 and0.00145524 respectively. These are comparisons of floating records, not continuum bounds. Independent Fraction comparisons passed93 checks in0.001248369924724102 seconds; proof and exact fractions are in research/n1_core_float_audit/resolution/.

The conditioning diagnostic AN304 now has independent AT1415-1417 confirmation. Its sharp componentwise condition number concerns stored jets, whose own errors remain unknown. It does not decide the accuracy of the original atom sums or sampled D6. A high-precision exact-source point check remains needed. N1's regional chain finished17:56:23Z, but its new complete owner report and regional values have not been audited here. No scalar request has been made.

Four local background slabs, roots000,002,004,006, are confirmed. Global background, complete near/far conditions, P-S2, S_F, the full inverse, invariant ball and existence remain OPEN. Candidate007 and the fixed c are unchanged.
