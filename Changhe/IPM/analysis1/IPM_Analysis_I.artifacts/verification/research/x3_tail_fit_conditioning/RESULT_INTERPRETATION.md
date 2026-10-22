# Actual source-fit diagnostics and exact synthetic moments

2026-10-21T17:03Z. The first proof review, actual Opus5.5 request aa185ad1-3895-47ea-bcac-9d8ee3dce235, confirmed the analytic coefficient and source-integral identities. It requested explicit spline conventions and warned against interpreting quadrature agreement as a bound. The subsequent exact check verifies spline degree7,376 control coefficients per mode,384 knots, endpoint multiplicity8,603 endpoint identities, and1608 rational last-span polynomial coefficients. The second derivative obtained through floating differentiated controls differs from the rounded exact value by up to about4.29e-14 in the worst scaled case. The initial overly small5e-15 diagnostic tolerance failed and is preserved. The successful diagnostic uses rounded exact endpoint values.

The Gauss512/768 and trapezoid8192 angular coefficient computations differ by at most about1.1e-13 in absolute value. A separate exact-polynomial density implementation preserves delta=q-1 directly, uses an integration-by-parts source formula and trapezoid4096/8192, and compares60 source scalars at12 fixed window radii and5 modes against de Boor/Gauss768. The largest relative difference is about3.36e-13. These are numerical consistency checks, not rigorous integration error bounds.

| Source fit | Floating design condition | Mode1 relative fit residual | Synthetic strain change from the baseline fit at the same R |
|---|---:|---:|---:|
| baseline, one decade, four powers | 1759.36 | 1.80e-13 | 0 |
| half decade, four powers | 2078.66 | 8.27e-15 | -5.16324e-17 |
| two decades, four powers | 62442.16 | 5.48e-11 | 1.22225e-14 |
| one decade at1e11 L, four powers | 1759.36 | 9.96e-15 | different outer radius |
| one decade, leading power only | 1 | 8.20e-5 | 4.51589e-9 |
| zero exterior source | not a fitted design | not applicable | -2.91221e-5 |

The five individual synthetic moments and four same-radius differences have been independently reconstructed as exact rationals from the recorded binary64 A and q, with18 Arb/iv enclosures. This rigor applies only to the separately defined synthetic power functions. It does not enclose the true X3 exterior source.

At the baseline, the four fitted mode1 coefficients differ from the evaluated analytic asymptotic coefficients by approximately4.27e-12,-1.89e-7,0.161,-0.337 in relative terms, respectively. Over two decades the last two differences are approximately0.783 and-0.806. At1e11 L the last two analytic contributions are extremely small, and their fitted relative differences are approximately-393 and33800. A very small sampled least-squares residual can therefore coexist with poor relative recovery of subleading coefficients. This is evidence about these numerical fits, not a certified failure of the full canonical inverse.

The half-decade synthetic strain change is about0.029 of one ulp of the saved full c, whereas the two-decade change is about6.88 ulps. Both saved full c values equal baseline exactly. Thus final rounding alone does not explain every equality, and no claim of such an explanation is made. The independently fitted leading-only change differs from the saved full-grid c change by about1.62e-13; the independently fitted zero-source change differs by about1.75e-14. These discrepancies combine unvalidated differences in angular rules, source representations, reconstructed grids and recurrence arithmetic. They are not error bars.

After adding an independently integrated annulus from the baseline outer radius to1e11 L, the extended fit's mode1 tail moment at the baseline radius differs from the baseline fit by about-5.6e-17. The64/128-point radial Gauss comparison is floating. This provides a plausible scale for one component of the observed numerical stability, while the cause of the full saved field coincidences remains OPEN.

The analytic coefficient formulas and exact moments of recorded synthetic sources can be CONFIRMED independently of fit accuracy. The numerical condition numbers, angular integrals, source comparisons and coefficient drifts remain explicitly floating diagnostics. No quantitative remainder, physical residual enclosure, historical radius-array provenance, global inverse or decisive IPM endpoint follows.
