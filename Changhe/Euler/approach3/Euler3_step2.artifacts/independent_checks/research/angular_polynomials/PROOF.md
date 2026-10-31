# Exact Cartesian polynomial reference for the angular tables

## Statement

Let ell and m be integers with 0 <= m <= ell. Write rho=x^2+y^2+z^2, and define the complex homogeneous polynomial

    Z_(ell,m)(x,y,z) = (x+i y)^m sum_(j=0)^floor((ell-m)/2)
      (-1)^j (2ell-2j)! z^(ell-2j-m) rho^j
      / [2^ell j! (ell-j)! (ell-2j-m)!].

Put N_(ell,m)=sqrt((2ell+1)(ell-m)!/[4 pi (ell+m)!]). The real regular solid harmonics in the campaign convention are N_(ell,0) Z_(ell,0) for m=0 and sqrt(2) N_(ell,m) times the real and imaginary parts of Z_(ell,m) for m>0. They are homogeneous harmonic polynomials of degree ell; their restrictions to the unit sphere are the real orthonormal spherical harmonics with no Condon-Shortley sign.

All Cartesian derivatives of these polynomials can be computed by ordinary monomial differentiation with exact rational coefficients before applying the common normalization. This supplies a reference independent of the production recurrence and derivative ladders.

## Proof

The explicit Legendre polynomial is

    P_ell(t) = sum_(j=0)^floor(ell/2)
      (-1)^j (2ell-2j)! t^(ell-2j)
      / [2^ell j! (ell-j)! (ell-2j)!].

Differentiate it m times. Terms with ell-2j<m vanish; the remaining falling factorial cancels (ell-2j)! in the denominator and replaces it with (ell-2j-m)!. In the convention without the Condon-Shortley sign, the associated function is (1-t^2)^(m/2) d^m P_ell(t)/dt^m. For r>0 and away from the axis, multiply this expression by r^ell exp(i m phi), substitute t=z/r, and use (x+i y)^m=(r sin theta)^m exp(i m phi). Each remaining radial power is r^(2j)=rho^j, giving the displayed polynomial. Polynomial continuity extends the identity to the axis and the origin.

The Legendre differential equation, differentiated m times, gives the associated Legendre equation. Together with the azimuthal factor exp(i m phi), it implies the spherical Laplacian eigenvalue -ell(ell+1). The Cartesian Laplacian of the homogeneous extension r^ell Y is r^(ell-2) times [ell(ell+1)Y+Delta_(S^2)Y], hence zero away from the origin. Since the extension is a polynomial, the Laplacian vanishes everywhere. The usual associated-Legendre integral and the sine/cosine integrals give the stated normalization. Finally, the binomial and multinomial expansions have integer coefficients; the displayed factorial coefficient is rational. Each Cartesian derivative therefore follows by exact rational monomial differentiation.

## Dependencies and scope

Dependencies: the explicit Legendre formula, the Legendre differential equation, its associated-function normalization integral, and the spherical-coordinate Laplacian formula. The numerical implementation uses exact rational coefficients, 70-digit decimal evaluation at the exact binary input coordinates, and an 80-digit mpmath normalization. A selected subset is compared directly with the existing mpmath evaluator. These numerical evaluations are not interval enclosures or formal proofs of rounding error bounds.
