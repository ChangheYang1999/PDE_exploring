# Testing every response for Candidate-shaped compatible data

Status: PROVED for root3. All responses have the exact uniform lower bound2^-28, and the rational majorant at z=2^-259 passes. Evidence V307/V308.

## Statement and exact data

At delta=4/9, c=9/5, retain the exact normalized Candidate007 modes from156:

    f_1(theta;b) = sin(theta) + b sin(3 theta)
                  + sum_(j=5,7,...,19) (a_j/a_1) sin(j theta).

Here a_j are the exact coefficients extracted in02, and b is a specified real root of the exact first-obstruction polynomial in156. Number its seven simple real roots increasingly. The nearest profile is root3. The bandwidth parameter is B=20. The first stream resonance is at order9, and subsequent resonances are at9k with frequency4k-2.

Let sigma_k(b) be the derivative of the next density obstruction with respect to the free stream harmonic at order9k. If an exact certificate establishes |sigma_k(b)|>=s>0 for every integer k>=1, then the conditional theorem145 supplies a unique tuned pure density/stream series with geometric Fourier norm bounds. It converges with every appropriately weighted derivative on some finite exterior domain. The reconstructed potential has only the first exceptional logarithmic term, as in145. Multiplying the input by a_1 restores all original harmonics except sin3 and rescales a sufficient exterior radius by a_1^(9/4).

This conclusion is a local exterior solution statement. It does not claim a global canonical stationary extension or convergence for the original exact Candidate exponent.

## Why the certificate covers all responses

The finite linear response uses only density orders1 through9 and stream orders1 through8. These depend on the exact input and contain no free harmonic. At a resonance n=9k, varying its free harmonic cannot produce a quadratic dependence before order2n+1. Since2n+1>n+9, the next obstruction is affine and its linear coefficient is sigma_k. Thus the response can be computed without knowing any earlier tuned harmonics.

Compute sigma_k by the full signed Cartesian recurrence for1<=k<=52. For k>=46 the carrier frequency q=4k-2 is at least182, exceeding BQ=180. The two carriers remain separated. The compact recurrence149 with t=1/q therefore gives exactly the same response. Verify overlap on46<=k<=52 by separate implementations.

Cover the interval0<=t<=1/182 by a finite dyadic tree. For every leaf either evaluate the full compact interval recurrence and certify |sigma(t)|>s, or prove in exact rational arithmetic that no t=1/(4k-2), k>=46, belongs to the leaf. Include the endpoint t=0 in the interval computation to cover the unbounded index tail. Reconstruct the tree from binary addresses and verify exact adjacency, the integer exclusions and every dyadic lower bound independently. Combining this with the finite prefix proves the claimed infimum bound.

The compact implementation here uses dense Laurent polynomials and independent array indexing. The earlier implementation149 uses sparse offset dictionaries. Both express the same derived operators. Agreement of sample values does not replace the derivation or the interval coverage.

## Norm and radius

The exact leading Fourier norm is

    a(b)=1+|b|+sum_(j>=5)|a_j/a_1|.

For root3, the exact interval cover certifies s=2^-28. Apply145 with h=2,Q=9,B=20, L=9/2 and kappa=1150/9. The rational root endpoints and exact higher coefficients give a(b)<1139/1000. These are the only numerical inputs to the majorant.

Write Phi(z,Y) for the polynomial map in145, in the order
Y=(V1,...,V8,E,W). Its value at z=0 is c0+JY, where J is strictly lower triangular and entrywise nonnegative. Set T=(I-J)^-1, Y0=T c0 and

    G(z,Y) = Y0 + T(Phi(z,Y)-Phi(0,Y)).

All coefficients of G are nonnegative. If every component of
G(2^-q,2Y0) is strictly smaller than the corresponding component of
2Y0, the monotone majorant argument145 bounds the series at z=2^-q.
Every strict radius R>2^(9q/4) then gives absolute convergence of the
series and all appropriately weighted derivatives. The strict inequality
provides the margin for polynomial derivative factors. Amplitude epsilon
rescales this sufficient radius by |epsilon|^(9/4).

The certificate records c0, J, Y0, the box and its exact image as rational
numbers. A second implementation from the theory part independently constructs
Phi, c0 and J. Comparing these objects and the images of rational test
vectors checks the actual map, not only its final maximum ratio. Testing
the preceding dyadic point with this same box says only whether that box
passes; it does not prove optimality of the sufficient radius.

## Scope of failure

A finite zero or unresolved interval is not automatically divergence. A failed tail cover is only failure of that certificate. The exact first compatibility in156 does not by itself imply a positive response infimum. Results will be recorded separately for each root tested; a result for the nearest root says nothing about the other six without their own checks.

## Certified result for root3

Let b be the third real root of156, isolated near
0.08937952559048386099606240294798001344828409050235.
For precisely the fixed higher coefficients specified above, every
integer response satisfies |sigma_k(b)|>2^-28. Full Cartesian evaluation
covers1 through52; the compact interval tree covers every k>=46. Its
406 leaves consist of260 certified lower bounds and146 rigorously empty
integer-index intervals. The405 splitting nodes and all endpoints are
replayed in exact rational arithmetic. The three sparse/dense comparisons
and seven full/compact overlap checks pass. The finite-prefix computation
and cover took466.26882861508057 seconds in total, with111.07862646272406
seconds for the cover.

The exact map certificate has maximum component ratio less than0.821 at
z=2^-259; the same box has maximum ratio greater than1.14 at2^-258.
Consequently, for every nonzero real epsilon the leading profile
epsilon*f_1 produces a unique tuned pure density and stream series,
convergent on every exterior domain

    r >= R > 2^(2331/4) |epsilon|^(9/4).

All appropriately weighted derivatives converge absolutely and uniformly.
In particular R=2^583 |epsilon|^(9/4) is sufficient. The potential
reconstruction and its finite exceptional logarithm at the first
resonance follow from145.

Taking epsilon=a_1 restores every original Candidate007 harmonic except
sin3. The exact amplitude satisfies a_1^9<2^38, so R=2^593 is sufficient
for that restored-amplitude profile. The similarity exponent is c=9/5,
not Candidate007's original stored exponent. This theorem does not assert
that all first-compatible roots are convergent, an optimal radius, or a
global stationary extension.
