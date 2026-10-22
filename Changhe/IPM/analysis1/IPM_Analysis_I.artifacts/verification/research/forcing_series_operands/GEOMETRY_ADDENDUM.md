# Independent squared geometry and exact binomial tests

Written2026-10-21 before the second geometry program, in the same shell call.

The second geometry engine uses mpmath.iv with160 decimal digits. Its
radial lower and upper endpoints enclose exp(t_lower) and exp(t_upper),
respectively. At the lower angle it uses the Cartesian projection gap
from PROOF.md, without taking square roots. For the upper angle it uses
instead the exact half-angle identity
 q=(r-p)^2+4rp sin^2(theta/2).
Both terms are nonnegative since r,p>0. Evaluate at both radial endpoints
and bound p throughout its source interval. Convexity of q in r and
monotonicity in theta justify these endpoint bounds. This formula is
independent of the first engine's evaluation of the two Cartesian squares.

For binomial coefficient k, put a_k=binom(2k,k)c0^(-k)/4^k>0. The exact
coefficient has sign(-1)^k and magnitude a_k/sqrt(c0). If a saved signed
midpoint-radius interval has positive magnitude endpoints L,V, then it
contains this coefficient exactly when
 L^2 c0 <= a_k^2 <= V^2 c0.
Squaring is order preserving on these nonnegative operands. This is the
rational check used alongside independent directed square-root evaluation
and the recurrence b_k=-(2k-1)b_(k-1)/(2kc0).

The explicit saved block coordinates, uniform positive source interval,
and restricted parent intersections remain as in PROOF.md and topic119.
No part of this addendum asserts that the physical residual Taylor model
or historical computation is sound.
