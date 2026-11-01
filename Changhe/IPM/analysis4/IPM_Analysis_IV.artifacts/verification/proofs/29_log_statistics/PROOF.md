# Underflow in logarithmic coefficient statistics

Status: the retained statistics routine is refuted on exact synthetic test states. No failure of a particular computed IPM coefficient is asserted.

## Claim and counterexample

The numerical logarithmic routine is intended to report the logarithm of each coefficient-column norm and to stop when a column's radius-to-maximum-coefficient ratio exceeds `1e-6`. Its stored coefficients use arbitrary-precision Arb arithmetic.

The retained `_stats` implementation first converts every raw coefficient magnitude and radius to a binary64 number. Values smaller than the binary64 range underflow to zero before the code chooses its scaling coefficient. This is inconsistent with the intended scale-independent statistics.

Consider a state with the two density columns `[[1],[x]]`, where the Arb interval `x` has midpoint `10^(-400)` and radius slightly larger than `10^(-405)` due to outward rounding. The second column has finite logarithmic norm within `4.35e-6` of `-400`, and its certified radius ratio is larger than `1e-5`. The routine instead reports its log norm as negative infinity and its radius ratio as zero. Thus the column is lost and the precision test fails to trigger. With the sole column `[[x]]`, it raises a `ValueError` from taking the logarithm of zero.

A control state with `x` at scale `10^(-40)` reports the expected finite norm and radius ratio. This isolates the failure to the conversion of tiny magnitudes, rather than the algebraic recurrence or polynomial convention.

## Verification and repair

`code/log_statistics_audit.py` executes the three states against a hashed source snapshot, with bytecode writing disabled. All exact input balls, observed results, and independently computed Arb norm/radius ratios are retained in `verification/counterexamples.json`. The source itself is retained in `sources`. The experiment is a unit counterexample and is not a stationary solution.

A scale-independent implementation should choose a nonzero pivot without converting its raw magnitude to binary64, compute its logarithm in Arb, and convert only dimensionless normalized coefficients and radius ratios. If a column is exactly zero, it can be recorded as such. An interval containing zero is not an exactly zero column.

## Scope

This failure affects reported statistics and stopping decisions once the coefficients leave the binary64 magnitude range. It does not invalidate the exact containment comparison through order 73, and does not prove any existing checkpoint has exhausted its precision. The independent verified coefficient enclosures remain valid on their stated finite prefix.

## Repair audit, 2026-10-31T03:26:52Z

The revised routine chooses a pivot from arbitrary-precision midpoint exponents before converting normalized quantities to binary64. The three original examples now pass: the tiny column has log norm approximately -400, the radius ratio is approximately 2e-5, and a sole tiny column no longer raises an exception. Division by an interval pivot inflates this ratio relative to division by its exact midpoint, which explains the factor of approximately two.

A narrower failure remains. With columns `[[1],[arb(0, "1e-20")]]`, the second column has a nonzero certified radius but every midpoint is zero. The code skips it, reports a negative-infinite column log norm and an overall radius ratio zero, and consequently does not trigger its precision stop. The exact-zero control `[[1],[arb(0)]]` returns the same statistics. The two states should be distinguished: for the uncertain column, a relative error with respect to its zero midpoint is unbounded or undefined, while the absolute upper bound is positive.

The revised five-case executable check and retained source are under `repair/`. Undefined interval logarithms and zero-denominator quotients are explicitly stored as `nan`, not interpreted as finite certified numbers. This remains a synthetic stopping-rule counterexample, not evidence that a retained stationary-series checkpoint has failed.
