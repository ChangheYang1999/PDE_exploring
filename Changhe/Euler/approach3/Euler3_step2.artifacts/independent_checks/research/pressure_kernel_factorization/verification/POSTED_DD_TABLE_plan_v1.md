# First posted pressure-table check

Registered 2026-10-29T11:07Z. The numerics pressure source27d154bbe28cf4cf was posted with its own float64 comparison. No verifier evaluation of that source has run. Local immutable copy: artifacts/dd_posted_snapshot_v1/code, with a before-import manifest.

Run the unmodified build_tables_dd on the actual frozen quadrature geometry, selecting the pressure degrees0,1,36, evaluation indices0,50 and source-interpolation columns0,24,47. All quadrature nodes are kept; all orders0 through36 are computed. This selection changes array dimensions only, not the arithmetic per table entry. It provides the three table entries registered before the implementation was posted, at every registered base and +/-h,+/-2h point for h=1e-3,1e-4 in S01 optimizer z_c and S05 physical c_l.

Compare to the already preserved90-digit finite-sum references. Also compare to separate90-digit sums that take the implementation's parameter-independent binary64 geometry expressions and final reciprocal1/(2l+1) as exact inputs. Keep both results. Their difference measures the changed constant-input convention, rather than a parameter-dependent elementary arithmetic error. This source uses the unfactored kernel, so its elementary exponential arguments extend below the common-factor-only range. Check actual exp pairs, including tiny/subnormal outputs, against90-digit values and record both absolute and relative error. Do not infer an error bound from finite random sensitivity draws.

Store all selected table pairs, exact parameter coordinates, source and reference hashes, extrema and nonfinite counts. Verify the snapshot hashes after execution. No result from this reduced table extraction is itself a full residual, Jacobian or (l)(6) reproduction.
