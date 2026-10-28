# Exact axis identity for residual-subtracted strain tests

## Statement and notation

Fix the exactly normalized modal trial rho0, its scalar ell0=1/k and the exact moving-tail chart of proof 167. Use canonical full-plane velocity U[f]=(-psi_y,psi_x), -Delta psi=partial_x f, with physical parity (density even in x and odd in y) and no added harmonic velocity. Let

    c[f]=partial_y U2[f](0,0),
    T f=(ell0 X+U[rho0]).grad f-f,
    F0=(ell0 X+U[rho0]).grad rho0-rho0,
    zeta=partial_ell rho_ell at ell=ell0,
    nu=n'(ell0)=3-c[zeta].

The chart has nu>0. Its full linearization is

    A0 h=T h+U[h].grad rho0+c[h] M0,
    M0=(X.grad rho0+T zeta+U[zeta].grad rho0)/nu.       (1)

The chart cutoff is zero on a disk B(0,r_chi). Thus zeta vanishes on this disk. Formula (1) follows from the exact chart definition and includes the parameter dependence of the far exponent. It is not the unnormalized fixed-ell linearization.

For |y|<r_chi define the vertical-axis cofactor and velocities

    f(y)=lim_(x->0) rho0(x,y)/x^2,
    u(y)=U2[rho0](0,y),    v(y)=U2[zeta](0,y).

Their derivatives used below exist for the modal trial, including across its radial joins. The formulas also apply to any background with the displayed local cofactor and velocity regularity.

Let h have the physical parity, finite canonical strain c_h=c[h], and zero vertical-axis cofactor on the disk. Concretely it is sufficient that h=x^4 H there with H continuously differentiable, with enough local regularity for the displayed expansions and a C1 canonical velocity. Smooth compact perturbations of this form and the Gaussian direction of proof 241 satisfy these local assumptions. Write

    b(y)=U2[h](0,y),
    R_h=A0 h-c_h F0/(ell0 nu),
    lambda_h=c_h/(ell0 nu),
    w(y)=b(y)+(c_h/nu)(v(y)-u(y)/ell0).               (2)

Then the exact identity on |y|<r_chi is

    lim_(x->0) R_h(x,y)/x^2
        = w(y) f'(y)-2 w'(y) f(y)+lambda_h f(y).     (3)

The value at y=0 is understood by continuous extension. The identity is pointwise algebra, not an estimate in a Sobolev or Holder norm. If h belongs to the actual maximal high domain, the full R_h belongs to the high target by the previously established mapping results, not by (3) alone.

## Axis transport and coupling

Divergence-free parity implies that, for a sufficiently regular canonical velocity associated with a density q,

    U1[q](x,y)=-x partial_y U2[q](0,y)+o(x),
    U2[q](x,y)=U2[q](0,y)+o(1).                       (4)

Indeed U1 is odd in x and U2 is even in x. At x=0, incompressibility gives partial_x U1=-partial_y U2. Taylor expansion gives (4). For the smoothness classes used here the remainders can be differentiated as required to extract the x^2 coefficient.

Since rho0=x^2 f(y)+o(x^2), one obtains

    axis(F0)=(ell0 y+u) f'+(2ell0-1-2u') f,          (5)
    axis(U[h].grad rho0)=b f'-2b' f,                (6)

where axis(q) means the continuous x^2 coefficient at x=0. In (5) the term 2ell0 f comes from ell0 x partial_x rho0. Omitting it changes the identity. The term -2u'f in both formulas is fixed by divergence-free parity, not by a choice of harmonic velocity.

The zero axis cofactor of h makes axis(T h)=0: both the x^2 coefficient of h and its y derivative vanish identically on the disk, and the x transport is tangent to x=0. The sufficient representation h=x^4 H makes this conclusion immediate. Also zeta vanishes in an open disk, hence axis(T zeta)=0 there. Consequently (1) gives

    axis(M0)=((y+v)f'+(2-2v')f)/nu.                 (7)

## Derivation of the chart column

For completeness, in the chart write H0 for the compact normalization column, B(ell)=F_ell(rho_ell)-n(ell)H0, and M0=H0+B'(ell0)/nu. Differentiation with ell and density both varying gives

    B'(ell0)=X.grad rho0+T zeta+U[zeta].grad rho0-nu H0.

The two H0 terms cancel, proving (1). The derivative zeta contains the exact logarithmic far variation. Canonical velocity differentiation is valid in the chart's established weighted spaces; it is one of the smooth-family statements of proof 167. No new differentiation under an unverified divergent integral is being used.

## Proof of the cancellation identity

Substitute (5), (6), (7) and axis(T h)=0 into (2). The coefficient of f' is

    b+(c_h/nu)(y+v)-(c_h/(ell0 nu))(ell0 y+u)
      =b+(c_h/nu)(v-u/ell0)=w.

The coefficient of f is

    -2b'+(c_h/nu)(2-2v')
            -(c_h/(ell0 nu))(2ell0-1-2u')
      =-2b'-2(c_h/nu)v'+(c_h/(ell0 nu))(1+2u')
      =-2w'+lambda_h.

This proves (3) with every parameter and normalization term retained.

The central normalization provides an independent check of the signs. Since u'(0)=c[rho0]=3ell0-1, v'(0)=c[zeta]=3-nu and b'(0)=c_h,

    w'(0)=c_h+(c_h/nu)(3-nu-(3ell0-1)/ell0)
          =c_h/(ell0 nu)=lambda_h.                  (8)

Odd parity gives w(0)=f(0)=0 and unit cubic normalization gives f'(0)=1. Therefore the y-linear coefficient in (3) is lambda_h-2lambda_h+lambda_h=0. With the actual smooth local expansions, axis(R_h)=O(y^3). This is the expected zero cubic jet of a target image and tests the sign of the scalar subtraction.

## The Gaussian direction and a possible design condition

For proof 241's exact Gaussian density d=-Delta V, with

    g(y)=-y^3 exp(-y^2)/6,
    V(x,y)=exp(-x^2)(g(y)+x^2(2g-g'')/2
                            +x^4(g''''-12g''+12g)/24),

the canonical velocity is (-V_xy,V_xx). Thus b=2g-g'', c_d=1 and d is divisible by x^4. The identity applies with

    w_g=2g-g''+(v-u/ell0)/nu,
    lambda_g=1/(ell0 nu).                            (9)

The Gaussian contribution to the axis velocity is explicit. The remaining u and v are the exact modal-background and chart-direction velocities, whose original coefficients and cutoffs must be used in any certified evaluation.

More generally, if an admissible h could be chosen with w(y)=lambda_h y on an interval, then (3) would reduce there to lambda_h(y f'-f). Equivalently its axis velocity would have to satisfy b=lambda_h y-(c_h/nu)(v-u/ell0). This is only an algebraic design condition. No existence of a globally admissible h with that prescribed trace, no transition estimate, and no high-norm smallness follow from it.

## Dependencies and scope

Dependencies: proof 167 for the exact moving-tail chart, smooth logarithmic variation and full column; proof 174 for its exact linearization and normalization; proof 190 for the residual-subtracted test; proof 241, including its binding clarification, for the Gaussian construction and actual high-domain membership. The proof uses the physical strain kernel convention of proof 1.

The result is restricted to the disk on which the chart density derivative vanishes. Outside it, T zeta need not vanish and (7) must retain that term. A one-dimensional axis formula cannot bound the complete high norm, which also includes the bulk remainder and its variable-order derivatives. No numerical norm, violation of the necessary test, inverse, nonlinear closure or profile existence statement is asserted. The analytic identity is derived here and is pending independent review.
