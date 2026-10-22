# Source parsing, endpoint separation and region labels

2026-10-21. Written after the proof review and the two complete exact geometry runs, before final acceptance.

Every distinct endpoint belongs to an interval of positive length. That interval covers a one-sided neighborhood of the endpoint. Therefore two zero-count open segments cannot lie on both sides of a distinct endpoint; each zero-count segment in the event sweep is already a complete open component. This supplies the explicit separation step in the proof.

The first rational method and the manual-bit method initially use the same Python decimal-to-binary64 JSON parser. Independence of the union algorithms and binary import paths does not mean an independent decimal parser. The additional check reads each original decimal token with Decimal, constructs its exact rational value, and checks it against the two exact midpoint boundaries of the claimed binary64 rounding cell. At a tie it requires an even last significand bit. It separately compares the manual-bit decoded rational to the topic152 exact row export. This certifies the rounding of all source geometry tokens without trusting a second floating conversion.

The integer grid exponent is the largest observed denominator depth in the manual IEEE decomposition. The importer explicitly covers both normal and subnormal finite numbers; zero has zero numerator regardless of sign. The checked data need exponent67. This exponent is sufficient for these data and makes no universal claim about arbitrary binary64 arrays.

A region here means the collection of rows bearing one saved region label, with every interval kept in full. There is no clipping to a new physical radius threshold. Inner, middle and outer hulls overlap at their two joins. The all-region calculation operates on all19389 intervals at once and independently tests the actual complement of their combined hull. Thus cross-label coverage cannot be silently discarded or double-counted.

The new computation finds strictly increasing starts and ends throughout the complete row sequence. The previously qualified1968 positive adjacent differences are consequently1968 actual components of the literal union complement:405 inner, none middle,1563 outer. Their exact total log-length is5294293/4611686018427387904. The maximum is4151/2305843009213693952. These are finite source-data facts only. There is no bound here for the residual on the gaps, for omitted tails, or for a global inverse.
