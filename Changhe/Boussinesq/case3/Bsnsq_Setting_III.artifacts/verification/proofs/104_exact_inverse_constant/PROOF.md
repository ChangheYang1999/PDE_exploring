# Exact certificate for the constant of a finite full-plane inverse

Written UTC: 2026-10-21T01:48:18.838547+00:00
Status: CONFIRMED for the four specified exact source fields. Full archive-linked rational rechecks and actual Opus5.5 exchange129-131 completed. Updated 2026-10-21T01:56:08.703079+00:00.

## Statement, data and scope

Let 2<b<3 and L>0 be exact rational numbers. Let S be a rational-coefficient spline of degree d>=2 with rational knots on [0,1], with S and S' continuous. Suppose S is the first-cosine scalar coefficient C0-C2/2 of the source representation in packet93. All source coefficients, including the subtraction C0-C2/2, are interpreted exactly as the rational values of the stored binary numbers after the explicit origin mask. Define a=3-b in(0,1). Packet93, whose full-plane inverse argument is independent of the following integration method, proves

    C2=-b L^2/[2(b-1)(b-2)] * B,
    B=S'(0)-(b-2)S(0)+int_0^1 (1-t)^(a-1) S''(t)dt.       (1)

Here C=(0,C2) is the constant after the first two homogeneous velocity terms in the centered inverse of that source. This packet gives a finite rational certificate enclosing B and C2. If its enclosure for C2 excludes zero, the specified source has C!=0. This statement alone is not a profile test. For the actual retied fields with b=beta, the separate hypotheses and implication of packet90 must also hold before the nonzero constant can exclude the exact represented field from B2. It never excludes nearby fields or an approximating sequence.

The certificate checks exact archive correspondence and does not replace floating numerical data by large literal tables in a proof source. The exact JSON data and their hashes are build inputs to the reusable checker.

## Exact reduction of each spline cell

On a positive knot interval [A,B], exact Cox recursion gives S(A+(B-A)u) as a polynomial in u. Twice differentiating and substituting u=(1-z-A)/(B-A) gives

    S''(1-z)=sum_(j=0)^(d-2) d_j z^j,   1-B<=z<=1-A,

with rational d_j. For a>0 every a+j is positive. Thus the cell integral is exactly

    sum_j d_j/(a+j) * [(1-A)^(a+j)-(1-B)^(a+j)].           (2)

For any rational v in[0,1], v^(a+j)=v^j v^a; at v=0 it is zero. Hence finitely many enclosures of v^a suffice for every cell. Adding the cell intervals covers the entire integral, including the integrable endpoint at t=1. There are no missing knot terms: S' is continuous. The endpoint values S(0), S'(0) come from the first positive cell by exact evaluation. The origin mask and archive knots are checked independently of the scalar coefficient generation.

## Rational bounds for the powers

At v=0 or1 use the exact power 0 or1. Otherwise choose an integer k>=1 and rational w in[1,2) with v=2^(-k)w. For h=(w-1)/(w+1) in[0,1/3), the identity

    log w=2 sum_(n=0)^infinity h^(2n+1)/(2n+1)

follows by integrating the geometric series for 2/(1-h^2). If N terms are retained, its nonnegative remainder is at most

    2 h^(2N+1)/[(2N+1)(1-h^2)].                           (3)

The same formula with h=1/3 encloses log2. Consequently subtraction of k log2 gives a rational interval for log v. Multiplication by -a gives one for x=-a log v>=0.

To bound exp(x) at any nonnegative rational endpoint, choose m>=0 with y=x/2^m<=1/2. Truncate the positive exponential series through degree M. The first omitted term is y^(M+1)/(M+1)!; the ratio of successive later terms is at most y/(M+2). Therefore

    sum_(j=0)^M y^j/j! <= exp(y)
       <= sum_(j=0)^M y^j/j! + [y^(M+1)/(M+1)!]/[1-y/(M+2)]. (4)

Squaring m times and taking the reciprocal gives bounds for exp(-x). Monotonicity supplies bounds at both ends of the interval for x. At every arithmetic stage a rational interval may be rounded outward to dyadic endpoints: floor(D l)/D<=l and u<=ceil(D u)/D for any positive integer D. Such rounding changes precision but cannot invalidate containment. The implemented accuracy choices N,M,D are recorded with the certificate; the checker recomputes inequalities (3)-(4) using exact rationals. No floating transcendental value is trusted.

## Enclosure theorem and checking procedure

For each endpoint v, compute the interval for v^a by the preceding construction. Multiply it by the exact nonnegative v^j, subtract the two endpoint intervals in(2), multiply by the signed rational d_j/(a+j), and sum. Signed interval multiplication swaps endpoints when needed. This encloses the exact improper integral because (2) holds on each cell, including the endpoint cell by a>0. Add the two exact boundary terms in(1), then multiply by the exact negative prefactor. This proves containment of B and C2 in the generated rational intervals.

A checker reloads the exact input JSON and checks its hash and its correspondence to the raw archive: exponent, scale, degree, reconstructed knots, masked C0 and C2. It reconstructs every cell polynomial and every rational power bound and compares the final certificate intervals exactly. A nonzero verdict is accepted only if the entire final C2 interval lies on one side of0. A changed interval, archive, knot, coefficient, mask or hash is rejected. A wide enclosure containing0 is OPEN, never a nonzero certificate.

## Dependencies and limitations

Packet93 proves(1) for the stated source and canonical relative full-plane inverse. The computations here independently establish its exact value enclosure, rather than certifying any transport equation. Packet90 gives the additional conditional inverse-constant necessity for a B2 solution in the retied finite representation. All interval identities and their hypotheses have been stated above. Numerical cross-checks and model reviews are supplementary. No Lean/Lake build is used or claimed.

## Actual source provenance and application

The four eps025/030/035/040 inputs in verification are registered exact JSON. All archives declare core SHA79128784b725d66fc429759272ead3c616bf93846952daf187fc7bed96eaa89f, identical to the retained source audit snapshot. Static inspection verifies the knot formula, unnormalized cosine basis, r2 mask and k,j layout. The checker compares this declaration and snapshot hash, validates float64/C-order data and reads the archive bytes only once. Only the defined serialized fields are certified; unrecorded historical runtime contents are not. The source may be C1 piecewise polynomial: the packet93 integrations by parts still hold because S and Sprime have no jumps. Actual degree5 simple-knot fields are C4.

All four C2 intervals lie strictly belowzero, with outward decimal enclosures recorded in verification/SUMMARY.md. By packet90 and exact b=beta these individual represented fields cannot satisfy B2 identically. No broad exclusion or endpoint follows.
