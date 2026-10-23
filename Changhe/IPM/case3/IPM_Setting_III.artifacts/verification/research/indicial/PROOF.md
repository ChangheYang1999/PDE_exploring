# The local indicial equation and its scope

Status: independently derived necessary equation. Polynomial resonance checks are recorded in verification/. No noninteger global eigenfunction or smooth nonlinear profile is constructed here.

## Statement

Let A=2c_l-1>1 and a0!=0. Freeze the primary center data rho=a0 y+..., psi=(1-c_l)xy+.... For a formal perturbation eta and its local stream function chi, the linear equations at the homogeneous perturbation order are

    L eta := (A x partial_x+y partial_y-1)eta+a0 partial_x chi=0,
    -Delta chi=partial_x eta.

Every such pair satisfies the local differential equation

    (A x partial_x+y partial_y+1)Delta eta
       +(2A-2-a0)partial_xx eta=0.                    (1)

This is a necessary equation; applying Delta may discard a harmonic remainder in L eta. A globally homogeneous eta=r^d Theta with d>1 is not in the canonical sublinear density class, so this formulation does not mean applying the primary full-plane inverse to an admissible global density.

## Derivation

Write D=A x partial_x+y partial_y. Differentiating products gives

    Delta[(D-1)eta]=(D+1)Delta eta+(2A-2)eta_xx.

Also Delta chi_x=-eta_xx. Applying Delta to L eta proves (1).

For noninteger d, a smooth periodic angular function Theta has a unique homogeneous stream function of degree d+1 with the specified parity, provided d+1 is not an even integer. In sine modes this solves

    -[phi''+(d+1)^2 phi]=d cos(theta)Theta-sin(theta)Theta'.

If (1) holds and all angular functions are smooth across both axes, the corresponding L eta is harmonic and homogeneous of degree d. A nonzero smooth periodic harmonic homogeneous function must have integer degree. Thus (1) then implies L eta=0 when d is noninteger. This limited converse relies on global smooth angular matching. It does not hold for a solution defined only on an open quadrant without checking boundary distributions.

For odd integer d, the stream-function mode sin((d+1)theta) is harmonic and is not fixed by the local Poisson equation. Its coefficient is a nonlocal datum in a true profile. Moreover L eta may have a harmonic component of degree d after (1). These exceptional cases must be treated using the original coupled equations.

## The differential equation on an open quadrant

For x>0 write eta=x^d h(t), t=y/x, and set B=2A-2-a0. Then

    eta_xx=x^(d-2)[d(d-1)h-2(d-1)t h'+t^2 h''],
    Delta eta=x^(d-2)k(t),
    k=d(d-1)h-2(d-1)t h'+(1+t^2)h''.

Equation (1) becomes

    [A(d-2)+1]k+(1-A)t k'
       +B[d(d-1)h-2(d-1)t h'+t^2 h'']=0.             (2)

The coefficient of h''' is (1-A)t(1+t^2), so the symmetry axis t=0 is a regular singular point. A trial h=t^s has lowest-power coefficient

    s(s-1)[A d-1+(1-A)s] t^(s-2).

Its formal Frobenius exponents are

    0, 1, s_x=(A d-1)/(A-1).

The subscript x denotes the axis y=0. Oddness in y selects the ordinary odd branch and, where compatible, an odd extension of a fractional branch. A noninteger power with nonzero coefficient is not smooth across the axis. Repeated exponents and integer differences require a separate logarithmic-resonance calculation. Listing exponents does not prove that a particular global solution has a nonzero fractional coefficient.

At the other axis, put eta=y^d g(u), u=x/y. Equation (1) becomes

    (d-1)q+(A-1)u q'+B g''=0,
    q=d(d-1)g-2(d-1)u g'+(1+u^2)g''.

The lowest-power coefficient for g=u^s is

    s(s-1)[d-1-a0+(A-1)s] u^(s-2),

so the corresponding formal exponents are

    0, 1, s_y=(a0+1-d)/(A-1).

Evenness in x imposes even matching at this axis. Both endpoints and the original coupled equations must be checked in any shooting computation. A small Fourier-Galerkin eigenvalue with slowly decaying coefficients is not a certificate of smooth angular matching.

## Polynomial jets and the harmonic datum

For d=n odd, write the homogeneous polynomial density in sine modes sin(k theta), k=1,3,...,n. The local Poisson forcing has even modes m<=n-1. Define the particular chi by assigning its mode sin((n+1)theta) coefficient zero. All other coefficients are fixed by

    chi_m=-f_m/[(n+1)^2-m^2].

Insert this chi into the original L eta=0. The resulting finite matrix is singular precisely when the homogeneous degree-n jet admits a nonzero solution with zero prescribed top harmonic datum. This gives the polynomial resonance curves listed in the verification JSON. The calculation treats the harmonic mode explicitly, and does not cancel a zero numerator against a resonant denominator.

In particular, a formula obtained by analytically continuing a homogeneous inverse from noninteger d can assign a nonzero harmonic mode at d=n even when its forcing vanishes. That convention differs from fixing the harmonic datum to zero and must not be substituted into the jet matrix unnoticed.

## Relation to actual local perturbations

A density equal to r^d Theta near zero can be cut off outside a disk. Its canonical velocity near zero contains the noninteger homogeneous contribution, as well as smooth harmonic jets produced by the exterior. The linear strain term generally changes. A local calculation at fixed center strain must separately account for or cancel that term. The cutoff construction motivates the local indicial operator but does not show that arbitrary local modes extend to a nonlinear whole-plane profile.

For a smooth primary profile, a nonzero term of noninteger total degree is inadmissible at the origin regardless of its angular regularity. Absence of such terms can be a compatibility condition. Neither this observation nor a dimension count proves that c_l is isolated, that a smooth branch exists, or that a finite-regularity family is a family of exact solutions.
