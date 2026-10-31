# Pair fixture amendment

Registered 2026-10-29T11:17:35.298989+00:00, after the v1 arithmetic fixture failed and before any Euler reproduction. The v1 log and sources are retained. The failure was a five-point numerator with cancellation: at h=1e-4, sample 48, the relative error against the small quotient was 1.0381492224e-28, above the proposed universal 1e-28 threshold. This does not establish a defect or accuracy of the pair routine.

The replacement fixture measures absolute error divided by the sum of the absolute stencil operands divided by the absolute binary64 denominator. Its threshold is 1e-30. This is an empirical test at the double-double arithmetic scale, not a proved error bound; the quotient-relative error is still reported. The relation between the two errors is exactly multiplication by this stencil's condition ratio. Severe cancellation can therefore enlarge relative error without enlarging the scaled error. No Euler pass tolerance, floor or data changes.

Source inspection also fixes the independent Richardson denominator to the registered literal 99.0, rather than recomputing (h/hp)^2-1 from the rounded step labels. The two named columns have step scale one. The v1 independent module is preserved.
