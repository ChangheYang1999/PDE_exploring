# Exact rational implementation of the second cutoff method

Written 2026-10-21T09:38:46.458680+00:00 before the new program. The first6000-row
mpmath.iv run reached its115-second command limit without a result file.
This is an incomplete computation, not a failed enclosure comparison.
The reviewed iv program is preserved unchanged.

The second cutoff method in ADDENDUM.md uses only rational arithmetic
until the Frobenius square root. All distance endpoints are exact dyadics,
the argument endpoints and subdivisions are rational, and all polynomial
coefficients and Bernstein conversion factors are integers or rationals.
Consequently it can be implemented with exact fractions without any
interval rounding. For the Hessian, nonnegativity permits the equivalent
comparison T2^2+(T1/r_min)^2 <= saved_T2F^2. The other five cutoff bounds
are compared directly as rational numbers. This implements the same
proved Bernstein convexity argument, with neither critical roots nor
floating operations. Adaptive subdivision succeeds only after every
required inequality has passed; exhausted refinement is reported OPEN.
It proves the same six field assertions as the Arb extrema engine.

Every row is identified by its full ci,q,bs,bp,ks,kp index, and complete
coverage is accepted only after disjoint chunks span all43949 rows of
the pinned input. A successful sample never counts as the complete audit.
