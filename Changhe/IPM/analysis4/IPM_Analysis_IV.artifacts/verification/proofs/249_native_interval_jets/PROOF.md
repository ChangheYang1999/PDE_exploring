# Native truncated-series evaluation of interval jets

Status: conditional interval-arithmetic justification and finite implementation checks completed. This refines the admitted Taylor enclosure theorem234; a final certificate still requires its separate manual-jet replay.

## Statement

Fix a nonnegative integer d and real intervals for the coefficients of truncated series in x. Represent a jet by its first d+1 coefficients, with the coefficient of x^j representing the j-th derivative divided by j!. Perform addition, subtraction and multiplication modulo x^(d+1). Division is allowed only when the constant interval of the divisor excludes zero. A native real-ball series implementation with outward rounding and precision at least d+1 gives the same inclusion guarantee as the explicit coefficient operations in234. The Taylor enclosure used there remains valid.

## Proof

Addition and subtraction are componentwise. Multiplication uses the finite convolution c_n=sum_(j=0)^n a_j b_(n-j). Each exact coefficient lies in its outward-rounded result by interval inclusion. For division, the coefficients are uniquely determined in increasing order by b_0 c_n=a_n-sum_(j=1)^n b_j c_(n-j). Since b_0 excludes zero, every exact quotient coefficient lies in the corresponding ball; this is the same recursion as the manual jet implementation. Native truncated-series arithmetic performs these ring operations, with each operation retaining at least d+1 coefficients. The implementation checks that precision condition after every operation and refuses a possibly zero constant divisor.

Consequently the whole-interval highest coefficient and pointwise lower coefficients enclose the same derivatives as in234. Taylor's theorem and the final interval Horner evaluation therefore give a valid function enclosure. This refinement changes execution cost and possibly interval widths; it changes no mathematical hypothesis or coverage rule.

## Verification plan and scope

Compare deterministic rational and interval operations against the explicit manual implementation; test zero-denominator rejection and precision-cap rejection; compare the complete degree-five compact response for sin17 at delta6/13 with the retained manual result and with direct evaluations inside its interval. A final response certificate can use this constructor while retaining the original manual implementation in its independent replay. No performance measurement constitutes proof of a response bound.

## Completed finite checks

At 2026-10-31T18:06:42+00:00, the retained test receipt records 504 native/manual coefficient-operation comparisons across degrees1 through7. All enclosures overlap; zero constant divisors and insufficient series precision are rejected. The full degree-five response enclosure on [0,1/3808] overlaps the independently computed manual enclosure and contains the endpoint and midpoint evaluations. The native and manual elapsed times were10.4857 and30.1207 seconds for this one enclosure, under the conditions recorded in the receipt. These finite comparisons do not prove a general software implementation correct. The inclusion statement above is conditional on the documented outward-rounded ring operations, and the final sin17 response certificate is replayed using the manual implementation.
