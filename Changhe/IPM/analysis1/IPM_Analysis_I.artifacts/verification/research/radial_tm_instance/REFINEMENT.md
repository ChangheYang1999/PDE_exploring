# Preserving input dependencies in the second coefficient computation

The initial sufficient test smoke_checks.json failed one containment:
cell0, n261, R coefficient j0 in mpmath.iv. Its direct interval recursion
computes (B/Z-A/Z)/2. This loses the common E dependency before subtracting
A and B, and its interval radius exceeded the producer radius. The Arb
closed-weight calculation passed this coefficient. All 12 tested remainder
comparisons and the other 155 coefficient comparisons passed. This is an
inconclusive upper-bound failure, not a refutation.

The second implementation instead carries affine weights under its ODE
recursion. Write each Taylor coefficient of q_plus or q_minus as

 (a A+b B)/Z + Z sum_k d_k F_k.

At j0 the weights are (a,b)=(0,1) for plus and (1,0) for minus, d_k=0.
For the step j to j+1 multiply all current weights by lambda/(j+1)
and add sign*2^(j-k)/((j+1)(j-k)!) to d_k for k<=j. The sign is minus
for q_plus and plus for q_minus. These recurrences follow directly from
the scalar ODE coefficient recursion. They are independent of the closed
beta-integral weights used by the first calculation.

After forming half-sums or half-differences of weights, evaluate each
input A, B and F_k once, and divide their combined homogeneous numerator
by Z once. Interval arithmetic on the weights and on inputs gives a
rigorous enclosure of the same full input family. This algebraic
reorganization discards no uncertainty. It avoids the dependency loss
which caused the first failure. All weights and their averaging use
mpmath.iv; the first checker's rational T weights are never imported.
The independently constructed derivative-polynomial remainder calculation
is unchanged. The original code and failed output are preserved.
