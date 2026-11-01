# Finite audit of the period-ten floating runs

Status: finite checks CONFIRMED in V593 on 2026-10-31T21:47:12+00:00.

## Exact statement and hypotheses

Fix delta=1/5, c=5/4 and f_1=sin(theta)+b_i sin(3theta), where b_i is one of the fourteen isolated algebraic roots from281. The producer uses binary64 arithmetic and a stated dyadic amplitude, then prints unit-amplitude density and stream logarithmic norms and the affine tuning responses. We compare only these printed finite quantities, under the exact source hashes archived with this audit.

## Independent norm and response comparison

The rational coefficient polynomials from281 give f_1,...,f_20 and g_1,...,g_19 before the first free harmonic. Evaluate each polynomial over the certified root interval by directed Horner arithmetic. The sum of absolute values encloses its angular Wiener norm. Prove this interval positive before taking its base-ten logarithm. Subtract the printed decimal, regarded as an exact rational, to enclose its discrepancy. This comparison measures finite error and does not declare the decimal an enclosure.

For every printed sigma_k, use the exact small-response polynomials from282 for2<=k<=20, and its reduced rational formula for k>=21. Evaluate separately at the root interval and at the exact rational represented by the producer's binary64 parsing of its decimal root. Exclude zero before division. Record relative discrepancies against both references and the relative change due to root rounding. These identities are valid independently of the accuracy of the later floating continuation.

## Printed-data fits

For each complete block10j<n<=10(j+1), take the largest density and stream logarithms separately and assign them the endpoint10(j+1). The printed decimals are exact rationals for this calculation. For endpoint cutoffs100,150,200, the least-squares line has slope (m sum(xy)-sum(x)sum(y))/(m sum(x^2)-sum(x)^2) and intercept (sum(y)-slope sum(x))/m. Distinct endpoints make the denominator positive. Compute the mean squared residual exactly; directed square root and exponential enclose its RMS, A=10^slope and the diagnostic A^5. Compare A and RMS with the producer's stated decimal rounding bins. Record actual last printed order and last complete block; neither is inferred from the announced final computed order.

The admission replay independently solves the same line problem by centered covariance formulas at higher precision, verifies all stored discrepancy bounds, source hashes and fit rounding bins, and counts every comparison.

## Dependencies and limits

Dependencies:281 for exact roots and early coefficients,282 for the response identity, and263/279 for the finite fit method. This audit does not enclose the high-order floating arrays, infer a growth law, or provide a sharp convergence radius. The separate majorant proof supplies convergence and sufficient exterior radii.

## Completed checks

All fourteen runs pass546 exact-root low-order norm comparisons,392 affine response comparisons at indices2..29,84 complete-block line fits and126 printed rounding bins. Every producer announces density order300 and prints norms through299; the complete-block fits end at290 with20,15,10 blocks. Uniform strict discrepancy bounds are norm-log<1/10000000000, response-relative-to-exact<1/100000000000, response-relative-to-binary<1/100000000000, and root-rounding-effect<1/1000000000000. A separate1536-bit centered covariance replay gives identical rational slopes and intercepts and overlapping directed A, A^5 and RMS enclosures. The original finite audit took1.619278seconds.

CONFIRMED for finite comparisons and printed-data statistics. The high-order binary64 arrays are not enclosed. These fits provide no asymptotic growth law, sharp radius or new convergence theorem.
