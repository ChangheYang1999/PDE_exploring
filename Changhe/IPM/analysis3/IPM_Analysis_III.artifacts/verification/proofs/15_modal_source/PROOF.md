# Independent canonical modal source from the original coefficients

## Exact object and intended conclusion

Use the exact joined and exactly scalar-normalized modal density of proof 04. All original binary64 inputs are exact dyadic numbers. Inner and outer corrections are defined by exact matching of derivatives through order six at the first and last exact knots. The unique scalar correction is the exact real formula in proof 04, evaluated within its certified enclosure, not an arbitrarily chosen point of that enclosure. This is a different density from raw X3.

The intended certificate locates a zero of w(x)=V_1(x,0), with V=X/k+U[rho], in

    a=4841405518533377/562949953421312,
    b=4841405518533711/562949953421312.

It must independently prove w(a)<0<w(b), and throughout [a,b],

    10<=w'(x)<=51/5, 99/100<=mu(x)<=101/100,
    29<=g(x)<=30,

where mu=partial_y V_2(x,0) and g=rho_y(x,0). Until the calculation and its output audit pass, these inequalities are OPEN. Their proof gives an exact equilibrium P=(p,0), unique in this interval, and supplies the parameter-box association needed by proof 08. It does not prove rho is stationary or mu(p)=1.

## Angular projection and canonical moments

Write

    rho=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta), t=log r,

with H_261=0. Project each factor mode by the exact sine identity of proof 12, so H_j=sum_m P_jm a_m. The last nonzero density mode may be j=260. Repeated signed frequencies are combined, including the low modes.

For n=1,...,261 and m=2n define

    I_n(t)=exp(-(m+4)t) integral_(-infinity)^t
                              exp((m+4)s) H_(n-1)(s) ds,
    J_n(t)=exp((m-4)t) integral_t^infinity
                              exp((4-m)s) H_n(s) ds.

Both are absolutely convergent. At the center H_j is bounded plus positive powers; at infinity H_j=O(exp((k-3)t)), and m>=2 with k<1. They obey

    I_n'=-(m+4)I_n+H_(n-1),
    J_n'=(m-4)J_n-H_n.                                  (1)

The canonical stream is

    psi=(r^4/2) sum_n (J_n-I_n) sin(mtheta).              (2)

To verify the sign and formula, the sin(mtheta) component of partial_x rho is half the sum of the radial derivative of the neighboring density modes, with their angular derivative terms. Insert (1) into the radial Laplacian of (2). It gives -Delta psi=partial_x rho. At zero the solution has only the regular harmonic behavior; at infinity it has the prescribed sublinear-density Green behavior. Equivalently, integration by parts in the convergent canonical radial Green integrals gives (2) directly. The boundary terms vanish by the center and tail exponents stated above. This calculation uses density moments and never differentiates a fitted approximation to generate Poisson forcing.

## Exact endpoint moments

For a projected inner mode

    H(t_-+tau)=C0+sum_(l=1)^7 D_l exp(2l tau)
                       +exp(bi tau)sum_(j=0)^6 E_j tau^j,

its initial I_n equals

    C0/(m+4)+sum_l D_l/(m+4+2l)
                    +sum_j E_j (-1)^j j!/(m+4+bi)^(j+1).

For a projected outer mode

    H(t_++tau)=sum_q A_q exp(alpha_q tau)
                          +exp(-bo tau)sum_(j=0)^6 E_j tau^j,

its final J_n equals

    sum_q A_q/(m-4-alpha_q)
                     +sum_j E_j j!/(m-4+bo)^(j+1).

The exact original exponents and every denominator are checked for the required positive sign. The scalar repair changes only the first leading outer factor coefficient and its uniquely determined matching correction. The interval coefficient is inserted before angular projection, so every endpoint computation is uniform over an enclosure containing the unique repaired object.

## Span propagation and exact elementary moments

For a knot span [l,r] of width h>0, write the exact degree-seven density polynomial as R(u), u=(t-l)/h. Exact B-spline recurrence in rational polynomials followed by outward coefficient arithmetic defines this polynomial, without independently rounding and rejoining pieces.

Equations (1) give

    I_n(r)=exp(-(m+4)h)I_n(l)
                  +h integral_0^1 exp(-(m+4)h v) R_(n-1)(1-v)dv,
    J_n(l)=exp((4-m)h)J_n(r)
                  +h integral_0^1 exp((4-m)h v) R_n(v)dv. (3)

Define phi_j(z)=integral_0^1 exp(zv)v^j dv. For real z!=0,

    phi_0(z)=(exp(z)-1)/z,
    phi_j(z)=exp(z)/z-(j/z)phi_(j-1)(z), j>=1,           (4)

and phi_j(0)=1/(j+1). Integration by parts proves (4). Outward high-precision evaluation therefore encloses every moment with no quadrature or truncation remainder. Cancellation may enlarge the interval and must be monitored; it cannot invalidate a successfully outward evaluation. An independent Taylor-series audit checks selected moments, with its explicit exponential remainder.

All spans from t_- to the source span are propagated forward for I, and all spans from t_+ back to the source span are propagated backward for J. Every interval is used exactly once in the required direction. There is no radial tail cutoff. The source span's polynomial and its left I and right J values are retained. Evaluation at any x in [a,b] uses t=log x and the same exact variation-of-constants formulas on the two remaining subintervals, retaining uncertainty in t and every coefficient.

## Source values and derivatives

At theta=0, polar differentiation of (2) gives

    w=x/k+x^3/2 sum_n m(I_n-J_n),
    mu=1/k+x^2/2 sum_n m[(m+1)I_n+(m-1)J_n-H_(n-1)-H_n],
    g=x^2 sum_j (2j+1)H_j.                               (5)

Differentiating the first formula using (1) independently gives

    w'=1/k+x^2/2 sum_n m[-(m+1)I_n-(m-1)J_n+H_(n-1)+H_n]. (6)

Thus w'+mu=2/k identically. Formula (6) can be evaluated directly and compared to 2/k-mu. Parity gives V_2(x,0)=0 and the off-diagonal entries of DV(x,0) equal zero. The source interval is away from all physical axes except y=0, away from the origin and inside the spline region. The exact C6 joins give enough regularity for all point values, derivatives, the intermediate value theorem and strict monotonicity used here.

## Verification record required

Record the original NPZ hash, scalar-repair input hash, precise arithmetic settings, all source-span endpoints, complete mode count, endpoint signs, whole-interval bounds and exact source-code hashes. Recheck the output intervals with a separate program, including the scalar coefficient and source bracket. A numerical midpoint, a sign at a sampled approximate source, or agreement of two floating evaluations is insufficient. No inherited Green table, source interval output or residual certificate enters the calculation.

## Completed certificate and its exact scope

The independent 512-bit reconstruction and 640-bit output audit have passed. The audit reads the read-only original, verifies all output bounds with exact rational comparisons, checks 816392 projected mode evaluations against independent exact de Boor interpolation, checks 19760 elementary moments against a separately bounded power series, and symbolically verifies the stream equation. The evidence files carry actual execution dates.

The endpoint signs are, with decimal endpoints interpreted as exact rationals,

    -3.02523e-12 < w(a) < -3.02522e-12,
     2.99723e-12 < w(b) <  2.99724e-12.

The whole source interval satisfies the coefficient box in the statement, and more precisely

    0.99999997745 < mu(x) < 0.99999997750.

Continuity gives an exact source p in (a,b), and w'>10 gives uniqueness in this interval. This is a local uniqueness assertion, not a count of all sources. The coefficient box now supplies the background association for proof 08's frozen Sobolev inverse.

There is a separate useful consequence for the residual epsilon=V.grad rho-rho. Along y=0 let g(x)=rho_y(x,0). Parity gives rho_x=V_2=partial_y V_1=0 there, so direct differentiation yields

    epsilon_y(x,0)=w(x)g'(x)+(mu(x)-1)g(x).

At the exact source, therefore, epsilon_y(p,0)=(mu(p)-1)g(p). Exact interval multiplication in the output audit proves

    -6.8e-7 < epsilon_y(p,0) < -6.6e-7.

Thus the exact normalized modal density is not a stationary solution. The identity mu(p)=1 belongs to an exact stationary profile with g(p) nonzero, and is not valid for this trial. None of these certificates is a source certificate for raw X3.
