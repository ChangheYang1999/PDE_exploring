# Resolution comparison: conditional aggregation and the limits of upper bounds

This proof precedes the new computations. It specifies a conditional audit of the saved numerical tables for the base trial and variants v3, v4 and v5. It does not certify the cellwise physical residual majorants, the reconstruction of these variants, their Poisson law or their relation to an exact solution. Those premises remain OPEN for this audit.

## Data semantics and statement

A JSON number in a producer output represents the binary64 number recovered by a correctly rounded decimal-to-binary64 conversion. Its exact value is a dyadic rational, not the exact decimal rational in the printed token. Scalar x_star is stored as midpoint and radius; all other scalar pairs are endpoints. Work with exact dyadic endpoints. The four trial files and each report/source excerpt must be pinned before accepting a comparison. The base parameters k and L are the exact dyadics represented by0.17936053129375418 and7.651424601381517. Verify that the stored binary64 computation0.5-k equals the exact rational difference before using that exponent.

Each row supplies a positive log-radius left endpoint t_i, or a negative endpoint, and h_i>0; q_i=W_over_m>=0 and ell_i=L2piece>=0. Its nominal radial interval is [exp(t_i),exp(t_i+h_i)]. This statement concerns those literal nominal intervals. The producer's physical interval coverage may instead use its larger Green boundary balls and has to be verified separately. Do not deduce global coverage from these literal endpoints.

For gamma>=0, let w_gamma(r)=(1+r/L)^gamma. If q_i bounds the nonnegative physical quantity q(r,theta) on the corresponding cell, then

 sup_cell w_gamma(r)q(r,theta) <= q_i w_gamma(exp(t_i+h_i)).       (1)

This follows because the derivative of w_gamma is gamma(1+r/L)^(gamma-1)/L>=0. Thus the maximum of the right sides is a conditional bound over the union of the cells. Gamma=1/2 and gamma=1/2-k are the cases used here. Independent interval exponentials and powers must enclose each right side; aggregate lower and upper endpoints using maxima. This encloses the exact maximum of the row-bound expressions, not the actual supremum of the PDE residual. If the stored summary upper bound exceeds the independently computed upper endpoint, its rounding is outward for this nominal aggregation.

Similarly the exact sum of the stored nonnegative ell_i is an aggregate bound if the corresponding rowwise integral bounds are valid and the cells cover the region, with nonnegative overlaps allowed for an upper bound. Verify the stored summary and each printed ceiling against this exact sum, rather than reproducing the producer's floating summation. Count rows and verify index uniqueness and the sign constraints; these checks do not replace the separate coverage premise.

For a positive base aggregate b and variant aggregate v, the exact comparison is (v-b)/b. These are comparisons of the published aggregate bounds. They provide no estimate on the relative difference of the actual physical quantities bounded by b and v. In particular, two upper bounds do not show that the true integral mass changes by their percentage difference. A constructive counterexample is to assign both actual values to min(b,v)/2, satisfying both bounds with identical integrals. Assigning the first actual value to b/2 and the second to0 instead gives a100 percent decrease while keeping the same upper bounds. No value lower bound or difference enclosure is supplied by those two upper bounds alone. These counterexamples also apply when the regions differ.

## Scalar intervals and decimal digits

For an interval I=[l,u] and candidate rounded decimal r at step d, if r-d/2<l<=u<r+d/2, every value in I rounds to r to that precision, independently of tie conventions. Test this on the actual stored intervals. For x_star near8 the13-significant-digit step is1e-12; for w_prime near10 the13-significant-digit step is1e-11. Small midpoint changes alone would not prove this property, but strict containment of the complete intervals does. Overlap of two scalar intervals does not prove equality of exact scalar values. Disjoint intervals, if their individual physical enclosures are justified, prove inequality. Rounded printed intervals may touch even when the raw exact intervals are disjoint.

A displayed interval [a,b] is outward for a nominal coverage interval [r_min,r_max] only if a<=r_min and r_max<=b. A rounded approximate region label need not satisfy this and should be marked approximate. An exact equality R=1468 is distinct from a stored R approximately1468; never insert the rounded radius into an exponential and call the result an exact endpoint.

## Independent implementations and scope

The primary implementation decodes with JSON/binary64/Fraction and evaluates monotone weights with Arb256. It computes exact sums, rational relative differences, scalar rounding bins and nominal domain endpoints. The second uses JSON decimal tokens, an integer-only nearest-even binary64 conversion, fmpq accumulation and mpmath.iv80 exponentials/powers, with no import of the primary evaluator or producer source. It compares all aggregate enclosures and exact arithmetic results. The elementary monotonicity and logical nonimplication are common mathematical dependencies and require independent human/model reconstruction. A complete actual Opus5.5 text review, response to objections, later own adjudication and an external rehash are required before a FINAL audit verdict.

The results concern the displayed tables and literal nominal cell aggregations only. They do not constitute a new residual certificate, fit error enclosure, inverse estimate, closing inequality or a decisive PDE endpoint.
