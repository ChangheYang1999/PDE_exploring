# Radial rigidity of the first sine residual

Date: 2026-10-20. Status: independently derived conditional theorem; 35 independent exact arithmetic checks passed at2026-10-20T23:19:22Z. Scope: radial angular quotient rho=y f(r) only. This is not a nonexistence theorem for the full primary class.

## Exact statement and notation

Let ell>1 and D=ell-1. Suppose rho(x,y)=y f(r), r=sqrt(x^2+y^2), is a smooth density on R2, rho_y(0)=a!=0, and

    |rho|+(1+r)|grad rho| <= C(1+r)^gamma,  0<gamma<1.

Let U=(-psi_y,psi_x) be its canonical full-plane velocity: the required parities, div U=0, curl U=-rho_x and U=o(r). Assume psi_xy(0)=-D. Put

    R=(ell X+U).grad rho-rho,
    R1(r)=int_0^(2pi) R(r,theta)sin(theta)dtheta.

Then R1 is not identically zero on (0,infinity). Consequently no such density satisfies the complete first-moment family of result87, and in particular none is an exact profile. No global sign or monotonicity assumption on f is needed.

## Canonical inverse and the projected equation

The smoothness assumption gives f(r)=a+O(r^2) and f'(r)=O(r) near zero, by restricting rho to the vertical axis and dividing its odd smooth restriction by y. At infinity the same restriction and derivative bound give f=O(r^(gamma-1)) and r f'=O(r^(gamma-1)). Define

    J(r)=r^(-4)int_0^r t^3 f(t)dt.

Direct differentiation yields r J'=f-4J. The canonical stream and its polar velocity are

    psi=-(1/2)r^2 J(r)sin(2theta),
    U_r/r=J cos(2theta),
    U_theta/r=(J-f/2)sin(2theta).                              (1)

To check this without assuming a boundary condition, the only source mode is rho_x=(r f'/2)sin(2theta). Inserting the radial amplitude in the polar Laplacian gives -Delta psi=(r f'/2)sin(2theta). Smoothness at zero follows by integrating the smooth even Taylor expansion of f; alternatively J(r)=int_0^1 s^3 f(rs)ds is smooth radial there. The growth estimate gives J=O(r^(gamma-1)) at infinity, so the velocity in (1) is O(r^gamma)=o(r). Thus (1) has all defining properties, and canonical uniqueness excludes adding a strain. Since J(0)=a/4, psi_xy(0)=-a/4, and the center normalization forces a=4D>0.

The elementary angular integrals are

    int sin^2(theta)dtheta=pi,
    int cos(2theta)sin^2(theta)dtheta=-pi/2,
    int sin(2theta)cos(theta)sin(theta)dtheta=pi/2.

Using rho_r=(f+r f')sin(theta) and rho_theta=r f cos(theta) in (1) therefore gives

    R1(r)/(pi r)=(ell-J/2)r f' +D f-f^2/4.                  (2)

These formulas retain the complete plane inverse. In particular J is not an independently adjustable strain parameter.

## Smooth-origin rigidity

Suppose, for a contradiction, that R1(r)=0 for every positive radius. Set t=log r. Near t=-infinity the pair (f,J) tends to (4D,D), and 4ell-2J tends to 2ell+2>0. On an initial half-line the equations are

    dot f=f(f-4D)/(4ell-2J),
    dot J=f-4J.                                            (3)

Let h=4D-f. Then h=O(exp(2t)) and

    dot h=k(t)h,  k(t)=f/(4ell-2J),
    lim_(t->-infinity) k(t)=2D/(ell+1)=lambda,  0<lambda<2.

Choose a number beta with lambda<beta<2 and t0 sufficiently negative that k(t)<=beta and the denominator in (3) is nonzero for t<=t0. If h(t0)!=0, the exact scalar ODE formula implies, for t<=t0,

    |h(t)|=|h(t0)| exp(-int_t^t0 k(s)ds)
           >= |h(t0)|exp(beta(t-t0)).

This contradicts h=O(exp(2t)) as t tends to -infinity. Hence h(t0)=0, and scalar uniqueness gives f=4D on that half-line. Solving dot J=4D-4J there gives J=D+C exp(-4t); boundedness at -infinity forces C=0.

The vector field on the right of (3) is smooth in a neighborhood of the constant pair (4D,D), whose denominator is positive. Ordinary differential equation uniqueness extends this constant solution through any finite endpoint of its interval of equality. If the interval had a finite right endpoint, continuity would give the same constant pair there and local uniqueness would extend it further. It follows that f=4D on every positive radius. But rho=4D y violates the prescribed sublinear growth. This contradiction proves the theorem.

## Dependencies, endpoint scope, and regularity limitation

The proof includes the radial canonical inverse, the angular projection and the full origin ODE argument. Canonical uniqueness is the usual harmonic difference argument: the difference velocity is harmonic and o(r), hence constant, and its parities force zero. A componentwise interior gradient estimate on increasingly large discs proves constancy. Relation to the complete first-moment family uses result87, mellin_transport_projection/PROOF.md, Section2; this relation is not needed for the direct conclusion about R1.

The smooth assumption can be weakened for this argument to f(r)-a=O(r^sigma) for some sigma>2(ell-1)/(ell+1), together with the regularity needed for (1)-(3). At the threshold, the backward ODE argument does not contradict a nonzero h. No existence at lower regularity is asserted. The affine continuation appearing in the contradiction fails the density growth and is not a new admissible canonical profile. For a general angular quotient, projection does not close to (3); no claim about that class follows.

The theorem is invariant under the genuine spatial scaling f(r) -> f(r/lambda_scale). It fixes neither ell nor a by gauge; a=4D here is a consequence of radiality and the actual canonical inverse.
