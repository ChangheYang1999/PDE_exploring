# Exact spline-knot jumps of the residual-subtracted test

## Statement and fixed objects

Use the actual exactly normalized modal background and exact moving-tail chart of topics167,190 and248, with their binding sidecars. In a neighborhood of an interior simple spline knot t_star write

    rho0(r,theta)=r^3 p(theta) sum_(m=0)^259 s_m(t) cos(2m theta),
    t=log r, p(theta)=cos(theta)^2 sin(theta), r_star=exp(t_star).

The exact splines are C6 across the knot and smooth on either side. Every derivative in theta preserves this regularity. Their canonical velocity U0=U[rho0] is also C6 in t with every angular derivative, by the finite modal Green formulas of proof 67. Define the one-sided jumps, right minus left,

    j_m=[s_m^(7)], S(theta)=sum_m j_m cos(2m theta),
    A(t)=sum_m (-1)^m s_m(t), j_A=[A^(7)]=S(pi/2).

Let ell0=1/k, V=ell0 X+U0, T=V.grad-1 and F0=T rho0. The chart density derivative zeta=-k^2 chi_infinity(r) log(r) P_infinity and its canonical velocity U_zeta are smooth near this finite knot circle. All cutoff derivatives are retained. In particular a knot is permitted to lie in the cutoff transition. Put nu=3-c[zeta]>0.

Take a test h with physical parity, finite canonical strain c[h], and h=x^4 H near this knot circle, where both H and the canonical velocity U[h] are smooth there. These are local hypotheses for this statement; the exact Gaussian d of proof 241 satisfies them and separately belongs to the actual maximal high domain. No global high membership of an arbitrary such h is inferred here.

Define

    a=c[h]/nu, lambda=a/ell0,
    M0=(X.grad rho0+T zeta+U_zeta.grad rho0)/nu,
    A0 h=T h+U[h].grad rho0+c[h]M0,
    R_h=A0 h-lambda F0,
    B_h=U[h]+a U_zeta-lambda U0,
    q_h(theta)=B_h(r_star,theta).e_r/r_star,
    q_0(theta)=ell0+U0(r_star,theta).e_r/r_star.

Here e_r=(cos(theta),sin(theta)), and q_h denotes a radial velocity coefficient, not a density or its axis trace. Then R_h is C5 in t at the knot, has smooth one-sided derivatives there, and

    [partial_t^6 R_h](theta)
        =r_star^3 p(theta) q_h(theta) S(theta).        (1)

The known background residual has

    [partial_t^6 F0](theta)
        =r_star^3 p(theta) q_0(theta) S(theta).        (2)

Define the cubic angular cofactor traces on the positive vertical axis by

    gamma_R(t)=lim_(theta->pi/2) R_h(exp(t),theta)/(exp(3t)p(theta)),
    gamma_F(t)=lim_(theta->pi/2) F0(exp(t),theta)/(exp(3t)p(theta)).

These are distinct from proof 248's axis(q)=lim_(x->0)q/x^2: for y=exp(t)>0, the present gamma_q(t)=axis(q)(y)/y. Put

    u(y)=U2[rho0](0,y), v(y)=U2[zeta](0,y),
    b(y)=U2[h](0,y), w(y)=b(y)+a(v(y)-u(y)/ell0).

The exact scalar jumps are

    [gamma_R^(6)]=(w(r_star)/r_star) j_A,
    [gamma_F^(6)]=(ell0+u(r_star)/r_star) j_A.         (3)

If j_A is nonzero and ell0 r_star+u(r_star) is nonzero, then

    [gamma_R^(6)]/[gamma_F^(6)]
         =w(r_star)/(ell0 r_star+u(r_star)).          (4)

For the actual trial the second denominator is positive at every positive radius by the axis-rate certificate V077. Proof 194 independently verifies j_A!=0 at the interior knot of original index700, t_star=4958764014967233/2251799813685248. Thus(4) is an exact identity there. No numerical value or bound for the right side is asserted. For the Gaussian, b=-g'' with g=-y^3 exp(-y^2)/6 and a=1/nu.

## Combined vector identity

The definition of M0 gives, before taking any derivative,

    R_h=T h+a T zeta+B_h.grad rho0+lambda rho0.       (5)

Indeed the remaining coefficient of X.grad rho0 is a-lambda ell0=0. The term lambda rho0 comes from subtracting lambda F0, whose zeroth-order term is -rho0. This cancellation is exact and uses the chart operator. A fixed-parameter operator without its normalization column would not give(5).

On the annulus, T h and T zeta are C6 in t, with all angular derivatives needed below, because h and zeta are smooth there and V has the stated C6 finite-mode regularity. The same is true of lambda rho0. The coefficient B_h is C6 in t. Consequently their sixth-derivative traces agree from both sides. All jumps in the sixth derivative of(5) come from B_h.grad rho0.

In logarithmic polar coordinates write

    B_h.grad rho0=(B_h.e_r/r) partial_t rho0
                   +(B_h.e_theta/r) partial_theta rho0.

In the sixth t derivative, the only term whose trace can jump is (B_h.e_r/r) partial_t^7 rho0. Every other product contains at most six t derivatives of rho0 and of B_h. Angular differentiation of rho0 does not change its C6 joining order. The coefficient of the possible jump is evaluated at its common continuous trace. Finally

    [partial_t^7 rho0]=r_star^3 p(theta) S(theta),

because all terms involving fewer than seven derivatives of s_m have zero jump. This proves(1). The same argument with V and the lower-order -rho0 proves(2), agreeing with proof 67.

This argument does not differentiate U0 seven times. C6 velocity regularity suffices for the vector formula. It also keeps T zeta intact: that term is C6 at a finite knot even when the chart cutoff is transitioning there, so its sixth derivative has zero jump. Zero jump does not mean zero size or zero contribution to a norm.

## Passage to the scalar axis trace

The physical parities and tangent velocity make every density term above divisible by x^2 y on this compact annulus, with a smooth angular quotient and the stated one-sided t regularity. For T h the stronger x^4 factor is preserved. For B_h.grad rho0, the x-odd first velocity component and y-odd second component supply the factors lost by the corresponding derivative of rho0. The divided tangent coefficients are smooth angular functions: U0 has finite angular bandwidth and its radial coefficients are C6, while the other velocities in B_h are smooth. Angular division at either axis therefore preserves the required C6 t traces of those coefficients. No unbounded division of a nonzero axis value is used.

It follows that the one-sided sixth t derivatives of these cofactor traces may be computed by dividing the jump formulas(1)-(2) by r_star^3 p and taking theta->pi/2. In differentiating the factor exp(-3t), all terms except its value multiplying the sixth jump involve lower jumps, which vanish because R_h and F0 are C5. The resulting jumps are q_h(pi/2)j_A and q_0(pi/2)j_A. On the positive vertical axis, e_r=(0,1), so q_h(pi/2)=w(r_star)/r_star and q_0(pi/2)=ell0+u(r_star)/r_star. This proves(3), and(4) follows when its denominator is nonzero.

A useful regularity check on the axis formula is that u itself is C7 as a one-dimensional function near each positive knot, although the full two-dimensional velocity is asserted only C6. Divergence freedom gives u'(y)=-partial_x U1(0,y). At x=0,y=r>0, partial_x=-(1/r)partial_theta. Since every angular derivative of U1 has C6 radial coefficients, u' is C6 in y locally, hence u is C7 there. This prevents an unjustified seventh-derivative jump of u from being inserted into the scalar formula. It asserts no C7 regularity of the whole velocity across the knot circle.

## Limits and dependencies

Equations(1)-(4) identify the exact leading derivative jumps at one knot. They do not compare high norms of R_h and F0, isolate a global knot-scale component, or estimate the smooth parts, the other knots, the angular remainder, the cutoff transition or the fractional seminorm. A small or zero jump ratio at one knot does not imply a small high-norm ratio. No value of w, no high-norm upper bound and no violation of(I) or(S) is certified here. The original profile existence and continuum inverse questions remain open.

The proof uses proof 67's actual radial regularity, proof 68/V077's positive axis rate, proof 194's exact nonzero axis jump at index700, proof 241 with its binding clarification for the Gaussian, and topics167,190,248 with their binding sidecars for the exact chart. This is a complete local hand derivation, pending independent audit before theorem adoption. There is no new computation or formal source.
