# An independent identity check for the generic response

Status: PROVED. All ten exact rational-function identities pass in V328. The actual calculation took134.5797667899169 seconds.

## Statement

Let delta=4/9 and f1=sin(theta)+b sin(3 theta). Let sigma_k(b) be the derivative of the next density obstruction with respect to the unit free stream harmonic at order9k. For k>=10 the signed Cartesian carrier calculation and the rational function retained in164 must agree identically in both k and b.

The comparison below is an exact polynomial identity test. It uses finitely many values of b, but retains k as an indeterminate throughout. It is not a scan of finitely many response indices.

## Degree and interpolation argument

The initial density f_j is a polynomial in b of degree at most j. This follows by induction: the leading degree is one, the density recurrence multiplies terms of total order j, and the particular Poisson inverse is linear with denominators independent of b. The same bound holds for g_j. These statements are needed only through j=9, before the first stream harmonic is chosen.

A unit free harmonic has degree zero in b. Its induced density variation U_r at order9k+r satisfies a linear response recurrence. Its forcing is the unit harmonic acting on f_r, together with products of U_s or its particular stream inverse with the initial coefficients of order r-s. Induction gives degree at most r in b. Thus sigma_k has degree at most9 in b, with coefficients in the rational function field Q(k). The retained generic numerator has the same degree bound and its denominator depends only on k.

Compute the signed Cartesian recurrence at ten distinct rational b values, retaining all radial exponents and angular frequencies as affine functions of k. At each value compare its exact rational response with the retained function by cross multiplication in Q[k]. Ten successful identities imply that their difference, a polynomial in b over Q(k) of degree at most9, vanishes identically. The independently checked carrier support ensures that the generic interpretation is valid at every integer k>=10. Poles are treated separately by the positive shifted-denominator certificate164.

The input low-order coefficients come from the exact Cartesian calculation144. The new calculation uses a separate rational-function implementation backed by exact univariate polynomials. Its Poisson step is checked by two Cartesian derivatives, and its signed coefficients are checked for sine symmetry at every response order. The theory part's Fourier response implementation is not imported.

## Dependencies and scope

This verifies the algebraic function used in164's global minimum proof. It does not itself locate a minimum, supply an interval root, or prove convergence. Those conclusions require the root isolation, coefficient inequalities and majorant certificates in the corresponding topics.
