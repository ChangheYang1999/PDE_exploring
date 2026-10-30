# Independent quartic origin jet of candidate 019

## Statement and hypotheses

Use the exact rational raw generator list of C1-N1-019-legqs50-cont12,
with c = 4076476460239181/2251799813685248, gamma = 1/c and
delta = 1-gamma. Let chi be its prescribed smooth even-even potential,
rho = -partial_y Delta chi, and u = (-partial_xyy chi, partial_xxy chi).
The latter is the canonical velocity in the previously audited potential
class; this calculation checks its local jet and does not independently
reprove that global identification.

The claim is that c + partial_y u2(0) = 1 exactly, that
partial_y rho(0) > 0, and that the full quartic coefficients determining
these identities equal the independently stored N4 origin certificate.
The sign of the density slope is certified in exact rational arithmetic.
This statement does not assert stationarity away from the origin.

## Exact local expansion

Write H_m = Re((x+i y)^(2m)), z = x^2+y^2 and
p = (3+gamma-j delta)/2 for branch j. A shifted Legendre polynomial has

    P_N(2t-1) = sum_(k=0)^N (-1)^(N+k) C(N,k) C(N+k,k) t^k.

For a generator with parameters (m,w,N,q,R), each of these summands in
chi is the raw coefficient times its displayed integer Legendre
coefficient times

    H_m z^(w+k) (1+z)^(p-m) R^(2q)/(R^2+z)^(w+q+k).

For monomials use N = 0, q = 0, R = 1. For ordinary Legendre terms use
q = 0, R = 1. This is an exact algebraic rewriting of the compactified
radial generator, so its Taylor coefficients can be computed without
numerical differentiation. Positivity of R^2 gives analyticity at zero.

Put a = m+w+k. A term can contribute to the quartic jet only if a <= 2.
Its coefficient of H_m z^(2-m) is the raw coefficient times the integer
Legendre coefficient times

    R^(-2(w+k)) sum_(i=0)^(2-a)
      binomial(p-m,i) binomial(-(w+q+k),2-a-i) R^(-2(2-a-i)).

The generalized binomial coefficients are exact rationals. Sum these
contributions into B_m for m = 0,1,2. All omitted terms vanish to order
at least six and cannot change any fourth derivative at the origin.
Since H_0 = 1, H_1 = x^2-y^2 and H_2 = x^4-6x^2y^2+y^4, the quartic
coefficients are

    A40 = B0+B1+B2, A22 = 2B0-6B2, A04 = B0-B1+B2.

Consequently partial_y u2(0) = 4 A22, and
partial_y rho(0) = -4 A22-24 A04. These formulas prove the certificate
once the finite rational identities and positive-slope comparison in
the checker pass. The odd density and velocity components vanish at
the origin by parity. The check covers every raw coefficient that can
contribute; high angular modes are omitted only by their exact order
of vanishing.

## Dependencies and verification

Raw coefficients remain in exact JSON. The checker uses an independent
local power series, not the full polar reconstruction, Cartesian field
code, or a finite-difference approximation. Its evidence records the
input hashes, exact quartic coefficients, the normalization identity,
the positive slope, all N4 comparisons and the actual time. Arb is used
only to provide an outward decimal enclosure of an already positive
exact rational slope. The canonical potential-to-velocity identification
is the dependency in ../scaled_field_audit/PROOF.md.
