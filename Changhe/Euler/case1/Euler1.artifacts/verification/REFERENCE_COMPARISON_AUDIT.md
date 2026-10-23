# Matched checkpoint metric audit

Date: 2026-10-23T07:34:31.036489+00:00. The latest comparison uses v2 M1 at prescribed c_l=0.45, step 4500, saved 2026-10-23T07:30:54Z. Checkpoint SHA256: **6946a4395f6b229958e6a82f7cef23f2324c5c40c2c6b05c950de9e7c229f74a**. Holdout SHA256: **c1cbf320174d2d998618930587076f1bafb31414e88f1aee3454d5bc03f6dfc0**. Evidence: `evidence/reference-compare-6946a4395f6b2299-disjoint.json`.

**CONFIRMED: the independent decoder and physical FD6 derivatives reproduce the repaired trainer's saved disjoint core-and-shell residual metrics.** At the finer step, the largest relative discrepancy across all twelve regional momentum/nonlinear ratios is 1.3256012923e-08; the largest origin Jacobian discrepancy is 5.58442181386e-13. Both derivative steps give consistent results, with the largest cancellation error in the farthest shell.

The frozen checkpoint is read as data. No trainer field or residual module is imported. The comparison uses the identical 9728 saved holdout points. This is an implementation check, not independent sampling evidence and not a training/holdout-gap measurement. The independent monitor uses separate volume shells and grids for PDE acceptance.

| Radial region | Disjoint sample count | Momentum ratio | Nonlinear ratio | Verdict |
|---|---:|---:|---:|---|
| D1_R<1 | 61 | 0.24454062604 | 0.48003094957 | CONFIRMED agreement with saved metrics |
| D2_1-3 | 1658 | 0.123488454954 | 0.46093974911 | CONFIRMED agreement with saved metrics |
| D3_3-10 | 2970 | 0.0196180902646 | 1.1221093878 | CONFIRMED agreement with saved metrics |
| D4_10-100 | 1445 | 0.0026641511015 | 2.67749178887 | CONFIRMED agreement with saved metrics |
| D5_100-1e3 | 1407 | 4.45675599604e-05 | 7.32205258435 | CONFIRMED agreement with saved metrics |
| D6_1e3-1e5 | 651 | 9.31114480907e-07 | 14.2473102313 | CONFIRMED agreement with saved metrics |

All six saved sample counts agree. The core R<1 has only 61 points in this saved holdout; its estimated ratio is 0.24454062604. Adding the overlapping origin and axis samples would instead give 0.215492326008. The latter is a different measure and is not used for this repaired checkpoint. Ratios far below 1e-3 in outer shells coexist with nonlinear ratios above one, demonstrating why the full-term denominator alone is insufficient.

Historical pilot500 and v2 step500 comparisons remain in their original immutable JSON files. Those reproduce the older overlapping measure and explicitly report a disjoint alternative. The CLI now requires `--reference-measure legacy` or `--reference-measure disjoint`, records that choice and checks saved regional counts. It never infers an apparent implementation error by silently using the wrong measure. A small synthetic nonzero-C test confirms that the old extra-C denominator differs from the corrected one; current campaign C=0 does not exercise that defect numerically.

The new checkpoint still fails PDE screening. Agreement between implementations does not certify the profile, numerical convergence, an optimized exponent, or the infinite-domain tail. Training/holdout gap remains OPEN because matching saved training points are unavailable for this resample-every-step checkpoint.
