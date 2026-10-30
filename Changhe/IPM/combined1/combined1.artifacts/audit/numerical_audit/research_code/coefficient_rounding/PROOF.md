# Absolute accuracy when rationalizing large Galerkin coefficients

## Statement and scope

Let x be the exact midpoint of a finite Arb number, and let B be a nonnegative integer. Exact nearest-dyadic rounding is

q_B(x) = 2^(-B) round(2^B x).

It satisfies |q_B(x)-x| <= 2^(-B-1), with either convention at a tie. A conversion that first rounds x to a fixed number D of significant decimal digits need not satisfy this bound, regardless of how large B is. Its absolute error can grow without bound as |x| grows.

This is a statement about coefficient conversion. A subsequently validated residual computed from the converted coefficients remains a valid certificate. Poor coefficient conversion can make a mathematically sound upper bound useless without making it false. Whether it explains any particular Galerkin result must be checked from that solve's coefficients.

## Proof

Rounding a real number z to its nearest integer changes it by at most1/2. Apply this to z=2^B x and divide by2^B to obtain the dyadic bound.

For decimal conversion, choose integers M>D+2 and J with0<J<M-D-1, and let x=10^M+10^J. Its first D significant digits agree with10^M and its next decimal digit is0. Thus nearest-D-digit decimal rounding returns10^M. The conversion loses10^J. Both values are integers, so subsequent nearest-dyadic rounding at any B>=0 preserves them exactly and cannot recover the lost term. Letting J grow proves unbounded absolute error. Taking M=300,D=200,J=80 is a concrete example.

## Application to a Galerkin potential

If phi=sum_i c_i psi_i and a conversion changes c by e, the energy of the perturbation is e^T G e, where G_ij=<grad psi_i,grad psi_j>. Near linear dependence can require large coefficients even when phi has moderate energy. Fixed significant-digit coefficient conversion can then produce a large perturbation. This observation does not assert that a particular solver's coefficients have such a size.

The safe alternative is to extract the exact midpoint as a rational (or mantissa and binary exponent), then round that exact rational to the chosen dyadic grid. This retains the stated absolute error independently of the exponent of x. One may also retain the exact dyadic midpoint directly. The number of fractional bits should be chosen using the desired function-space error and the basis Gram matrix; a per-coefficient bound alone is not automatically a useful potential error bound.

## Verification and dependencies

The local verification compares an independent exact-integer dyadic converter with the fixed-decimal strategy on the explicit integer above. It checks the installed Arb midpoint-rational interface directly. No source-lane code is executed. The target is the `rationalize` function in N3's `certification/hminus1.py`, whose full source hash is frozen in the verification record. This does not review N3's Galerkin method or invalidate an exact residual bound it computes.
