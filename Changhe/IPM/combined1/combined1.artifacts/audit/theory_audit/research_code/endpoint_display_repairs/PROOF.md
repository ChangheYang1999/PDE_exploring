# Acceptance of the second endpoint display revision

## Statement, hypotheses and dependency

This documentary result accepts revision 2 of T2 the review of T4-375, frozen in
source/REVIEW.md. The underlying theorem is T4-375, independently accepted
in T4-385 and with its first presentation repair accepted in T4-398.
For the real C1 S1 corrections, canonical IPM velocity, endpoint asymptotic
hypotheses and finite weighted amplitude and gradient norm H_q stated in
that theorem, its endpoint-gradient lower bound and conditional CI
inequality remain unchanged. All mathematical constants retain their
exact definitions in the accepted proof. This result asserts correct
rounding and provenance of the revised displayed consequences, not a
new analytic estimate.

## Argument

The complete source diff changes decimal conversion, labels and provenance.
The analytic formulas and stored Arb calculation path are unchanged.
Both revised display scripts use the same directed conversion already
checked in T4-401. A finite positive Arb endpoint is extracted as the exact
dyadic rational m times 2^e. An initial decimal exponent from a floating
logarithm is corrected by exact rational comparisons. Exact floor or
ceiling at the selected decimal place gives a lower or upper rational.
The formatted decimal is parsed back to a rational and its direction is
asserted. The float guess cannot affect the enclosure direction.
The AST comparison recorded here checks that both conversion functions
are identical to the accepted T4-401 function, ignoring source locations.

Consequently the downward pointwise values are 999775.737764,
999745.395628 and 999748.875812 for 007, 013 and 014. The common critical
E display is at most 0.6819391, rather than the earlier too-small 0.681939.
The corrected onset and cap tables retain the accepted interval comparisons.
The nine code, result and log hashes in the review equal the files frozen
here. The sharpE checker itself is unchanged from the prior accepted
revision; its separate folded-kernel integral has not been independently
audited here and remains CLAIMED.

The lower-bound script now checks the exact theta-star entries consumed
from the 375 result, and prints rather than asserts the whole-file hash.
It also consumes Phi(theta-star). Acceptance of this particular frozen
run uses the matching hashed 375 result; checking theta alone would not
validate arbitrary replacement Phi data. No stronger generic provenance
claim is made. This distinction does not alter any accepted interval or
analytic statement.

## Verdict and scope

CONFIRMED: the second revision repairs the displayed bound directions
without changing the accepted theorem. The full revision is now the
accepted display text. The FLOAT minimax calculation remains diagnostic,
and E_new remains a separate OPEN audit. No foreign code was executed,
no numerical integral repeated, and no new stationary solution, inverse,
finite-radius velocity theorem or existence closure follows.
