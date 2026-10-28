# Verification result

Recorded 2026-10-28T16:29:27.180738+00:00. The original-data run finished at 2026-10-28T16:28:35.545137+00:00 after 5.503 seconds, single-threaded. All 1,444 entries of the complete 38-column input Gram and all 38 strain coefficients agree between the 512-bit Taylor enclosure and the 640-bit antiderivative replay. Every active spline polynomial agrees with the independent de Boor recurrence: 216 polynomial checks, 884 interior column-join checks, and 28 inner matching equations. The infinite inner and outer integrals are exact finite exponential sums, with no omitted tail.

The separate 768-bit saved-evidence audit checks all dependency hashes, exact positive LDL factors of the seven inner exponential functions, and all 676 entries of the pure 26-column subblock against the earlier original-data certificate, after exact changes of binary scales. The five outer entries and strains agree with proof 235. The complete matrix has exact disjoint-support blocks of sizes 33 and 5.

For the specified stored strain row, the maximum absolute error is less than 2053/10^20 = 2.053e-17, and the maximum relative error is less than 2701/10^19 = 2.701e-16. These are outward comparisons with the exact declared columns. They make no claim about the output matrix.

Certificate SHA256: c6d2e2c862f5023e90f24bb8ec550e655ea75e153ba9ccf22abb9f2599079858.
Exact rational input SHA256: 3b962aa65f6d6127863a6a69f813ce152cfb1cbed4d9f7143d438191408f2f35.
Saved-evidence audit SHA256: 3dc72191898ca58a1183372dcab1e13c8a8dacc19d1c9bf6549ef623c5c83799.
Proof SHA256, unchanged since before the run: fc97b44e300cf9456285e95c1aeca25580977be8ed5e71dd5268f9b52cdb9eb0.
Executed code SHA256: f918a24bf7683c880a5b4a9901a8186d12c96e5b560260562b83c15f150a6e38.
Frozen metadata SHA256: bd16b7d2bd321e4e931016354ab3e08b5235a9f06e186587b6ed108bc86913f7.

The first attempt incorrectly used the Arb equality predicate to test equality of nonzero-radius balls. That predicate does not assert equality of their centers and radii. It failed before writing a certificate. The revised check verifies interval overlap; symmetry is an exact consequence of the integral formulas. Both the failed script and log are preserved. No claimed mathematical formula or accepted number changed.

Verdict: CONFIRMED for the complete input Gram and strain row only. The output Gram, a finite operator lower bound, high-norm singular values, off-basis residuals and the continuum complement remain separate open verification tasks.
