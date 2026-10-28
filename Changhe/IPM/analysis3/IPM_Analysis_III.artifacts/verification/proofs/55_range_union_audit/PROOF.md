# Interval union after rounding: an enclosure counterexample

## Claim and exact test

The inspected range_finite function in the numerics team encloses an exponential polynomial separately on finitely many subintervals. It converts each enclosure endpoint to an ordinary nearest binary64 float, takes their minimum and maximum, and reconstructs a ball from their floating midpoint and width. This operation is not a valid interval union in general, even with a small multiplicative radius inflation and an absolute radius floor.

Let

 f(x)=1+2^(-80)+2^(-200) exp(10x), 0<=x<=1.

This is an exact exponential polynomial. Its constant offset is much larger than the code's radius floor1e-300, and much smaller than a binary64 unit in the last place near1. Its varying term is smaller still. With split=6 and maximal exponent10, the range routine makes two subintervals. At256-bit precision, the Taylor enclosures remain narrow enough that all four endpoints round to the binary64 number1. The reconstructed final interval is centered at1 and has radius about1e-300. It excludes f(0), which is at least1+2^(-80).

The accompanying check runs this exact input against an archived copy of the inspected implementation and records containment, endpoint values and hashes. This is a counterexample to the general enclosure operation, not a claim that a particular final S2 number has been incorrectly enclosed.

## Why the local Taylor argument is valid

For a smooth exponential polynomial f on [0,h], Taylor's theorem at m=h/2 gives

 f(m+x)=sum_(j=0)^K f^(j)(m)x^j/j!+R,
 |R|<=sup_[0,h]|f^(K+1)| (h/2)^(K+1)/(K+1)!.

For e real and an ordinary polynomial p, the coefficient bound

 sup_[0,h]|exp(ex)p(x)|
 <=max(1,exp(eh)) sum_j |p_j|h^j

is valid for h>=0. Thus the algebraic Taylor scheme in the snapshot is sound. The counterexample arises when its subinterval balls are assembled through nearest-rounded endpoints, after this valid step.

## Correct union and proof

Keep the lower and upper endpoints as exact dyadic endpoints or use explicitly directed conversions. Let l be a lower bound on every subinterval lower endpoint and u an upper bound on every upper endpoint. Form the ball (l+u)/2 plus a symmetric radius (u-l)/2 using interval arithmetic, so all rounding is enclosed. Then every subinterval, and hence the whole range, is included.

Using nearest floats for l and u would require adding the endpoint rounding errors and the midpoint rounding error to the radius. Multiplying only the interval width cannot repair a shared offset lost from both endpoints. The exact constant1+2^(-80) illustrates this distinction.

For the finite-subdivision count, the quantity |e|max h/split is only an efficiency choice. If its floating evaluation rounds down and produces fewer subintervals, the Taylor remainder still covers each chosen subinterval. It cannot repair or cause the interval-union defect just described.

## Other changes in the same snapshot

The new hypA snapshot uses geometric left/right cell selection and puts a cell crossing t=0 in both parts of M_P. These changes repair the coverage defects of proof 51, provided every required quantity is either finite or explicitly records failure. Its all-Arb Chebyshev tail sums remove the earlier need to justify floating products there. The new range_finite dependency must itself be repaired before its results can support certified bounds.

No certified transport margin or singular value is inferred from this audit.
