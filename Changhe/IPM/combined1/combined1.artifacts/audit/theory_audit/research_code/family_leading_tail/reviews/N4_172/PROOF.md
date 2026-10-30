# Equality of the leading tails of the exact reference family

## Exact statement

The inputs are the exact state131, d2 and immutable candidates005
through012, each identified by its source hash in the result. All
have c=4076476460239181/2251799813685248. Set gamma=1/c,
delta=1-gamma and d=3+gamma. For each listed potential chi, define
rho=-partial_y Delta chi and u=(-chi_xyy,chi_xxy). The claim is

    chi=r^d A(theta)+o(r^d),
    rho=r^gamma Theta(theta)+o(r^gamma),
    u=O(r^gamma),

uniformly in angle, with the same entire A and Theta as candidate007.
The first sine coefficient of Theta obeys18<b1<19. This is a claim
about the specified exact functions, including scaled terms in010/011.
It does not assert that they solve the stationary equation.

## Canonical and scaled leading coefficients

A canonical term C r^(2k)(1+r2)^((d-j delta)/2-k) cos(2m theta)
has leading coefficient C at r^d if j=0. Terms with j>0 are
strictly smaller because delta>0. Thus the canonical amplitude
A_m is the exact sum of all coefficients with j=0 at angular
frequency2m. Zero sums are removed before comparing finite maps.
This independently checks the ordinary candidates against T4's
raw-generator endpoint calculation.

For a raw scaled generator write S=r2, H_m=Re(x+iy)^(2m), and

    C H_m (1+S)^(p_j-m)
       [S/(R2+S)]^w [R2/(R2+S)]^q
       L_n((S-R2)/(S+R2)),
    p_j=(d-j delta)/2.

Here w,n,q are nonnegative integers, R is a positive rational,
and L_n is the Legendre polynomial. The first ratio tends to1.
The second is asymptotic to R^(2q)r^(-2q). The Legendre argument
tends to1, where L_n(1)=1. This endpoint follows inductively
from L_0(1)=L_1(1)=1 and
(n+1)L_(n+1)(1)=(2n+1)L_n(1)-n L_(n-1)(1).
Consequently this generator contributes C to A_m exactly when
j=q=0 and zero otherwise. The checker validates all integers
and positive scales. In the frozen010/011 snapshots every scaled
addition has q=4, as separately recorded.

The same endpoint reasoning applies to monomials and ordinary
shifted Legendre generators, with q=0,R=1. We compute a second
leading map from the raw generators wherever both representations
are already available, requiring exact agreement with the canonical
map. The two scaled candidates are checked directly from their
immutable raw coefficients and manifests.

## Density and uniformity

Apply -partial_y Delta to the common homogeneous leading potential.
The independent full Fourier formulas in
../leading_tail_nonzero/PROOF.md give every sine coefficient.
The implementation repeats that finite differentiation and checks
the entire resulting map against N4-165's confirmed007 result.
In particular

    b1=-A_0 d2(d-2)+A_1(d2-4)d/2,

and the exact integer comparisons give18<b1<19. Equality of only
b1 would suffice for nonzero leading density; here equality of
every A_m proves equality of the whole profile.

Each input is a finite sum of smooth factors with denominators
positive on the real plane. Near infinity these factors have
convergent series in r^-2, valid after any fixed number of
derivatives and uniformly in the angle. A lower branch loses at
least delta in radial order, and q>0 loses at least2. Three
derivatives therefore give the claimed density expansion and
velocity growth. The limiting angle polynomials are smooth.

## Analytic consequence and scope

The separately audited weak tail-pinning theorem T4-189/200/201
applies within its canonical weighted affine class
h in L2((1+r2)^(-a)dX), 0<=a<=1+gamma, with all its hypotheses.
The common nonzero leading density pins any exact stationary
solution in that class to the reference c. Each already confirmed
fixed-c correction-ball exclusion thus holds for every trial c
within the same affine class. This supplies no new exclusion for
an unchecked ball, particularly the comparison candidate011,
and it excludes no solution in a different leading-tail chart.

The numerical checker validates immutable coefficient hashes,
exact c, both available amplitude paths, all leading Fourier
coefficients, and the independent T4 family table. Own code runs
only on own frozen inputs. No integration, optimization, new
norm transfer or computer proof assistant is required.
