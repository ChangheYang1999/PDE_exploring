# Exact leading-profile comparison across the candidate family

Status: finite exact comparison, initially OPEN numerical-lane reproduction.
The analytic tail-pinning theorem is already audited in T4-189/200/201.

## Statement and method

For every listed potential with the same c=4076476460239181/2251799813685248,
put gamma=1/c, d=3+gamma, delta=1-gamma. A canonical ordinary term is

    C r^(2k)(1+r^2)^((d-j delta)/2-k) cos(2m theta).

Its leading potential amplitude at order r^d is C if j=0 and zero if j>0.
Equivalently, an ordinary generator H_m(1+r^2)^(p_j-m)P(t) contributes
C P(1) in block m when j=0. Monomial and shifted Legendre polynomials have
P(1)=1; the checker derives the latter endpoint from exact coefficients.
A multiscale legqs term carrying four vanishing leading moments contributes
zero at order r^d. This must be checked from its exact formula, not inferred
from a label.

Summing these amplitudes gives A_m. The leading density is obtained by
applying -partial_y Delta to r^d sum A_m cos(2m theta). Its first sine
coefficient is

    b1=-A0 d^2(d-2)+A1(d^2-4)d/2.

Equality of every exact A_m proves equality of the entire leading density
profile. Equality of the first coefficient alone only proves the needed
common nonzero coefficient. The checker records which stronger conclusion
is verified. All branches are finite smooth radial powers, so their
expansions and any fixed number of derivatives are uniform in angle.

## Consequence and scope

If the common leading density is nonzero and the canonical velocity grows
at most r^gamma, T4-201 pins every exact stationary solution in the weighted
affine class h in L2((1+r^2)^(-a)dX), 0<=a<=1+gamma, to the reference c.
Thus any already-proved fixed-c exclusion in a contained correction ball
also excludes solutions at every trial c in that same chart. No exclusion
is created for a ball that has not already been checked; no claim covers a
different nonlinear tail chart. Input hashes and exact comparisons are
necessary for every candidate separately.
