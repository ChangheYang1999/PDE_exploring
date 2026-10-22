# Verified finite-data witness and exact scope

The polynomial implication in PROOF.md has now been checked on frozen data.
Every binary64 number means its exact dyadic value, not an interval hiding
an unspecified continuous spline.

M16/s16 at ppc2,4,6 has three byte-identical saved piece records, hash
311fa80a7ff1aafa054222aadac374843deaf0c5d6e7351d391f25c505ac281c.
Each has1953 function columns. All90 eligible mode-zero spline columns with
strict interior support have a nonzero value jump:720 of810 tested endpoints.
These are three copies of one dataset, not three independent experiments.

M24/s8/ppc4 has5257 function columns. All187 eligible mode-zero interior
spline columns have a nonzero value jump:1496 of1683 tested endpoints.
Its saved piece hash is
9c5976081bc9d01f86137ee41747b57892b33b28c0975b29ea95822e35664208.
The two tiny raw NPZ members tmin.npy and t0.npy were independently extracted
and equal the corresponding metadata cells endpoints exactly. Their full
raw matrix was not copied, hashed, loaded or recomputed. The absent M16
raw matrices prevent the same historical scalar linkage for those runs;
their exact encoded-piece result relative to their metadata endpoints holds.

For both unique piece datasets the selected witness is zero-based column16,
mode0, label sp8. Its complete eight-piece coefficient record is in both
compute.json and independent.json. For the M24 witness:

    tmin = -0x1.37dcfe8f38528p+2
    t0 = 0x1.0454aec299e0ap+3
    tstar = -0x1.2c57dfd6e6674p+2

The adjacent left interval is [-0x1.3695507abd714p+2,-0x1.2c57dfd6e6674p+2),
and its ascending coefficients are

    0x0.0p+0, 0x0.0p+0, 0x0.0p+0, 0x0.0p+0, 0x0.0p+0, 0x0.0p+0, 0x0.0p+0, 0x1.27a8701451759p+6

The right trace is its adjacent right polynomial constant

    0x1.a01a01a01a01ap-13

Exact right-minus-left trace difference:

    Delta = 65844087666320684129053345726054163814357358560164208857406676666267195997018441942473691/4697085165547666455778961193578674054751365097816639741414581943064418050229216886927397996769537406063869952

Both methods prove 10^-22 < Delta < 10^-14. The rounded value
1.4018074049258473e-20 is for orientation only. The sign and nonzero result
use exact rational arithmetic. No smallness tolerance makes this jump an
L2 weak gradient.

The frozen source imposes join constraints only at tmin and t0. Therefore,
for the M24 saved columns with those raw endpoints, its exact pre-eigencut
constraint kernel contains this non-X direction for every finite derivative
matching order NJ. It is present in each source-defined Fminus, Fminus_noJ,
free and free_noJ column set. Nonzero diagonal equilibration and an exact
full-kernel parametrization do not remove it. This is a statement about
the mathematical kernel, not a claim that a floating SVD produces an exact
nullspace. Eigenvalue truncation can remove directions: no claim about the
actual retained Gram subspace or smallest singular vectors follows here.

The unrestricted assertion that matching only the two external joins
makes these encoded polynomial columns conforming is REFUTED. The reported
finite matrix singular values are not recomputed or numerically refuted.
An exactly continuous B-spline representation or a certified reconstruction
could repair the interpretation. No bound on that repair is established.
No PDE solution, inverse, residual bound, or NO endpoint follows.

Method1 used NumPy only through an explicit restricted pickle loader and
Fraction Horner evaluation. Method2 imported no NumPy, reconstructed arrays
with data-only proxy classes, decoded IEEE754 sign/mantissa/exponent bits,
and evaluated direct exact power sums for every eligible column before
reading method1. Both counts and every coefficient of the selected witness
agree. The source was inspected, never executed. First method2 attempt
found a missing M16 raw matrix; its code and failure are preserved, and the
final result records that linkage as OPEN rather than inventing metadata.
