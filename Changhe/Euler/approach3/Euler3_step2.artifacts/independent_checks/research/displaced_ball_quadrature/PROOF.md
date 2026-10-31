# Origin-centered radial integration on a displaced ball

Date: 2026-10-29. Status: complete informal argument. Numerical quadrature accuracy remains a separate question.

## Statement

Let z be a nonzero vector in R^3, d = |z|, a > 0, and e = z/d. Choose any orthonormal vectors e1,e2 perpendicular to e. For -1 <= mu <= 1 and 0 <= phi < 2 pi set

    n(mu,phi) = mu e + sqrt(1-mu^2)(cos(phi)e1+sin(phi)e2).

For every integrable function F on B(z,a), its integral equals the sum of the following full-sphere and cap integrals:

    int_0^max(a-d,0) r^2 dr int_0^(2 pi) dphi int_-1^1 F(r n(mu,phi)) dmu
    + int_|d-a|^(d+a) r^2 dr int_0^(2 pi) dphi int_m(r)^1 F(r n(mu,phi)) dmu,  (1)

where the first term is zero if a <= d, and

    m(r) = (r^2+d^2-a^2)/(2rd).

Endpoints r = 0 have measure zero and may be defined by a limit. For z = 0, the ordinary full-sphere integral for 0 < r < a applies. Dividing (1) by V = 4 pi a^3/3 gives the normalized ball mean.

On each radial interval, use a Gauss rule in r and, at each radius, a Gauss rule in the stated mu interval. Use N equally weighted periodic azimuthal points. If each rule has at least two radial nodes, one mu node and one phi node, the sum of all physical weights is exactly V in exact arithmetic. To integrate first and second Cartesian moments exactly, it suffices to use at least four radial nodes, two mu nodes, and three azimuthal nodes. The moments of the normalized measure are

    mean(y_i) = z_i,
    mean(y_i y_j) = z_i z_j + (a^2/5) delta_ij.                            (2)

## Proof of the domain formula

For y = r n with |n| = 1,

    |y-z|^2 = r^2+d^2-2rd(n.e).

The inequality |y-z| < a is therefore equivalent, for r > 0, to n.e > m(r). There are no admitted directions if r > d+a or if d > a and r < d-a. Every direction is admitted for r < a-d when a > d. On the remaining radial interval |d-a| < r < d+a, m lies between -1 and 1. Spherical coordinates have measure r^2 dr dmu dphi, which proves (1), including the case d = a by omission of the zero-measure origin. An orthonormal frame changes no measure.

## Proof of exact low-order moments

For the cap part, angular integration of the constant is 2 pi(1-m(r)). Multiplication by r^2 gives

    2 pi r^2(1-m(r)) = (pi/d) r [a^2-(r-d)^2],

a polynomial of degree three. The full-sphere part has radial density 4 pi r^2. A Gauss rule with two radial nodes integrates both densities exactly. Angular weights integrate constants exactly. Thus their total is the ball volume V.

For first moments, periodic azimuthal averaging annihilates sin(phi) and cos(phi), leaving r mu e. For second moments, three or more equally spaced azimuthal points annihilate the nonconstant frequencies up to two. The azimuthal average is

    r^2 [mu^2 e_i e_j + (1-mu^2)(delta_ij-e_i e_j)/2].

Two mu nodes integrate these polynomials of degree at most two. After integration in mu and multiplication by r^2 dr, the first-moment cap densities are polynomials of degree at most five, because r^3(1-m^2) is polynomial. The second-moment densities are polynomials of degree at most seven, because r^4(1-m) and r^4(1-m^3) are polynomial. Four radial Gauss nodes integrate those densities exactly. Full-sphere terms need no higher degree.

Alternatively, the exact values follow directly by y = z+x. Odd moments on B(0,a) vanish; rotational symmetry makes its second moment a scalar multiple of the identity, and mean(|x|^2) = 3a^2/5 gives (2). This agrees with the coordinate calculation.

## Scope and implementation requirements

The formula allows a pressure evaluator to use a small set of radii while directions vary with radius. It evaluates the same displaced physical ball as a translated radial rule. Each pressure target radius must still be an exact panel edge of the full-space radial Green quadrature. Interpolating pressure between unregistered radii is not justified by this formula.

The implementation must retain the physical weights and check their sum and the moments (2). It must not normalize away a substantial volume error. Floating-point frame errors and quadrature errors for nonpolynomial fields remain numerical errors. Two resolutions and a separate polynomial control are required before using the rule for a saved field. No uniform quadrature error bound or continuum maximum is claimed.

Dependencies: spherical coordinates, the algebraic ball inequality, elementary polynomial exactness of Gauss and periodic trapezoid rules, and rotational symmetry. No formal verification is supplied.
