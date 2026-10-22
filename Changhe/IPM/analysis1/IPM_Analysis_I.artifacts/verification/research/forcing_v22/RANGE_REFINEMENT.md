# Preserve factor correlations in the exact Bernstein check

Written 2026-10-21T09:41:56.055796+00:00 before the revised range implementation.
The initial10-row exact check failed to bound the saved TL,TL1,TL2,T2F
using128 subdivisions. Its source and OPEN output are retained. The
failure concerns that sufficient overestimate, not the saved physical
cutoff bounds, which have already passed the complete Arb extrema test.
The earlier3000-row exact command timed out after90seconds without output.

The initial method bounded v^(5-j)(1-v)^(5-j) and Q_j separately. To
remove this avoidable overestimate, form the Bernstein coefficients of
the full derivative polynomial S_j on each rational subinterval.
For degree n=9-j and v=a+hu, the exact power coefficients are
c_l=h^l sum_{k=l}^n p_k binom(k,l) a^(k-l).
The exact Bernstein coefficients are
b_i=sum_{l=0}^i c_l binom(i,l)/binom(n,l).
These are precisely the affine substitution and basis identity proved
in ADDENDUM.md. Thus max_i|b_i| bounds |S_j| without multiplying separate
ranges. The arithmetic is rational throughout. The same radial scaling
and squared Frobenius comparison apply. This method has no critical-point
inputs and is independent of the Arb extrema computation.

Subdivision remains adaptive with explicit OPEN status on any failed
inequality. Completeness is checked from the exact contiguous row ranges
and the pinned merged input, never from a successful sample alone.
