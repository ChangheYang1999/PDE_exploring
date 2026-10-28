# A strict increment bound for the positive projection remainder

## Statement

Use the real or complex homogeneous Euclidean Holder space, modulo constants, with seminorm [f]_alpha and 0<alpha<1. Let Q_(R,beta) be the positive convolution measure in ../PROOF.md, rotated so that the positive kernel axis has angle beta. Its mass is 1/pi. Put

    mu_(R,beta) = Q_(R,beta) + (1/2 - 1/pi) delta_0,
    eta_alpha = (82/321489) alpha(1-alpha) (11/9)^(alpha-2).

For distinct points x,y, let h=|x-y| and choose R=h/2. Then, uniformly in beta,

    |mu_(R,beta)*f(x) - mu_(R,beta)*f(y)|
        <= (1/2 - eta_alpha) h^alpha [f]_alpha.

Consequently any accepted D upper estimate obtained by removing the two radius-h/2 local projection pairings and then bounding the regular functional can have its additive1/2 term replaced by1/2-eta_alpha. In particular, if B bounds that regular functional at unit increment, then

    D_alpha <= 2^(1-alpha) A_alpha/alpha + 1/2 - eta_alpha + B,
    A_alpha = Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)).

The regular functional may be bounded by any of the accepted phase interpolation constructions. The gain is uniform before phase interpolation, so no identity atom is put into a smaller phase interval. This statement is for R=h/2. It does not alter a formula that uses a different optimized radius without a new scaling argument.

## Density and two disks

By homogeneity and rotation of coordinates, take h=1, x-y=e_1 and R=1/2. Let n be a unit vector along a negative kernel axis, with angle beta+pi/2. The density of Q on either negative angular lobe is

    q(r,theta) = |cos(2(theta-beta))|/(2 pi r^2)

on the radial interval

    (1/2)|sin(2(theta-beta))| <= r <= 1/2,

and zero elsewhere. This follows directly from the polar definition of Q in ../PROOF.md: if t is the angle from the neighboring zero ray, the lower radius is R cos(2t), and cos(2t)=|sin(2(theta-beta))|. Endpoints and zero rays have area measure zero.

Take two Euclidean disks centered at +/-r_0 n, where

    r_0=7/18, epsilon=1/9.

They are disjoint. Any point in either disk has radius between5/18 and1/2 and angular deviation d from its negative axis satisfying |sin d|<=epsilon/r_0=2/7. Hence |d|<pi/4 and

    |cos(2(theta-beta))| = cos(2d) >= 1-2(2/7)^2 = 41/49.

Also,

    (1/2)|sin(2(theta-beta))| <= (2/7)sqrt(1-4/49) = 6sqrt(5)/49 < 5/18.

The last inequality follows on squaring from60025>58320. Therefore both disks lie inside the support of Q, up to their boundary, and throughout them

    q >= (41/49)/(2 pi (1/2)^2) = 82/(49 pi) =: c.

The angular-deviation estimate is the elementary tangent bound for a disk of radius epsilon viewed from a point at distance r_0>epsilon. It is independent of the orientation of n relative to e_1.

## A coupling along the increment direction

Remove from Q the constant-density measure c times area on each of the two disks. The remaining measure is positive. Couple each point of this remainder to the same convolution coordinate at the other evaluation point. Couple the identity atom in the same way. These parts have unit transport distance.

In a selected disk centered at a, write w=a+u, |u|<=epsilon. Couple w to w'=a+(-u_1,u_2), reflection in the line through a perpendicular to e_1. Reflection preserves the uniform area measure on the disk, so the two marginals are exactly the removed constant-density measure. The corresponding evaluation arguments are x-w and y-w'. Their difference is (1-2u_1)e_1. Since2epsilon<1, their distance is1-2u_1.

For |s|<=2epsilon, the second derivative of t^alpha on [1-2epsilon,1+2epsilon] satisfies

    (t^alpha)'' <= -alpha(1-alpha)(1+2epsilon)^(alpha-2) =: -a_alpha.

Taylor's inequality around1 gives

    (1+s)^alpha <= 1 + alpha s - (a_alpha/2)s^2.

The disk is symmetric in u_1 and its area average of u_1^2 is epsilon^2/4. Therefore the average transport cost in that disk is at most

    1 - a_alpha epsilon^2/2.

Each selected disk has mass c pi epsilon^2. The two disks therefore reduce the cost relative to unit translation by at least

    2(c pi epsilon^2)(a_alpha epsilon^2/2)
      = c pi alpha(1-alpha) epsilon^4 (1+2epsilon)^(alpha-2)
      = eta_alpha.

All components together form a coupling of the two translates of mu, whose mass is1/2. Integrating the Holder increment inequality against this coupling proves the normalized statement. At general h, scale the selected disks and all coupling coordinates by h. The density scales by h^(-2), their masses are unchanged and transport costs acquire the factor h^alpha. Complex-valued functions satisfy the same modulus inequality, so no real-part reduction is required.

## Scope and status

The finite positive measure Q has no principal-value ambiguity. Its use inside the local decomposition inherits the already proved origin and infinity convergence statements from ../PROOF.md and ../../../01_setup/PROOF.md. The gain is positive for0<alpha<1 and is O(alpha) at alpha0 and O(1-alpha) at alpha1. It therefore changes neither accepted endpoint asymptotic coefficient nor the accepted constant term at alpha0.

This proof was written before any numerical evaluation of eta_alpha. It is a proposed improvement pending independent analytic cross-read and a separate numerical acceptance for displayed decimal values.
