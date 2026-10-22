# Strict decimal corollary and audit details

This supplements the unchanged proof-first argument. The computations target
these common strict ceilings at R=9,T=3000, applicable to every admissible T:

| derivative order j | individual component or partial derivative ceiling |
|---|---|
| 0 | 1.006144e-11 |
| 1 | 3.394241e-12 |
| 2 | 7.827257e-13 |
| 3 | 1.056035e-13 |

Each ceiling must independently exceed the upper endpoint from both methods.
The actual majorants are different: the complete finite sum is smaller than
the fifth-mode plus quotient-sum majorant. Their nonoverlap is expected and
is not disagreement about the actual velocity, which they only bound above.

The stronger numerical consequence of the same source identity is

 |F_y(rho_T,c0)(P)|>6.6989e-7

for every admissible T. Indeed both relevant jets are below1.006144e-11,
and exact rational subtraction gives
6.70197e-7 -30.0230*(1.006144e-11)>6.6989e-7.
This remains only nonstationarity of the exact specified106 family.

The iv implementation bounds each Zj by64 positive rational terms plus a
geometric tail. For m>=64 the ratio of successive (2m+5)_j is at most
(1+2/(134-j))^j. After multiplication by1/4, the ratio is strictly below1.
The first omitted term is (133)_j/4^64. Its quotient by one minus the
ratio bounds the whole omitted tail. The finite partial sum and that
positive tail enclose the exact generating-function value Zj. This is an
independent series enclosure, not a truncation without a remainder.

The original binary input, full frozen topic113 map, source76 endpoint
bounds, N1 upper bound from105, and all numerator/denominator identities
are dependencies checked by the new auditor. In particular reuse of783
certified H2 coefficient intervals is explicit. This is a new estimate from
already certified finite coefficients; no claim of a new third independent
H2 convolution is made. There is no assertion about the fully composed
flow certificate or the requested PDE inverse.
