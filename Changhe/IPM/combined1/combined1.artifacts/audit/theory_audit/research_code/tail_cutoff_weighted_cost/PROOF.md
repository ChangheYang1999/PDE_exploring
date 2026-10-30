# Weighted residual cost of moving a tail repair outward

This proves R1-035 remark(b) with an explicit finite-radius lower bound.
It concerns the audited T4-314 family and does not assert existence of a
stationary solution or a lower bound for all conceivable repair families.

## Statement and notation

Let q<-1, eta>0, and let F be a measurable residual on the plane satisfying
for r>=R0>=1

    ||F(r,.)-r^q A||_(L2(S1)) <= E r^(q-eta),
    M=||A||_(L2(S1))>0.

The angular measure is dtheta on [0,2pi). Suppose F_L agrees with F on
r<=L. Let E_a=L2((1+r^2)^(-a)dX), where a<=q+1<0. Norms may be infinite.
For every 0<epsilon<1 set

    R=max(R0,(E/(epsilon M))^(1/eta)), kappa=q+1-a>=0.

If E=0 the second term can be omitted. For L>=R,

    ||F_L||_(E_a) >= (1-epsilon) M
        sqrt((L^(2kappa)-R^(2kappa))/(2kappa)), kappa>0,       (1)
    ||F_L||_(E_a) >= (1-epsilon) M sqrt(log(L/R)), kappa=0.   (2)

Consequently, for kappa>0,

    liminf_(L->infinity) ||F_L||_(E_a)/L^kappa
       >= M/sqrt(2kappa),                                 (3)

and at kappa=0 the corresponding liminf after division by sqrt(log L)
is at least M. These are extended-real inequalities if a norm is infinite.

## Proof

The reverse triangle inequality in the angular Hilbert space gives
||F(r,.)||>=M r^q-E r^(q-eta)>=(1-epsilon)M r^q on r>=R.
Since a<0, (1+r^2)^(-a)>=r^(-2a). Restrict the squared norm of F_L
to the annulus R<=r<=L, where it equals F. It is at least

    (1-epsilon)^2 M^2 integral_R^L r^(2q+1-2a) dr.

Integration proves(1) and(2). For fixed epsilon take the liminf and then
let epsilon decrease to zero. This proves(3) and its endpoint version.
No estimate of the residual in the transition annulus is required.

## Application to the potential cutoff

T4-314 proves that both h_L and its canonical velocity vanish on r<=L,
so F(rho+h_L)=F(rho) there, exactly. It also proves

    d_L=||h_L||_2=C L^(q+1), C=||h_1||_2>0.

Putting L=(C/d_L)^(1/(-q-1)) into(1) yields a quantitative tradeoff;
in particular (3) becomes

    liminf_(L->infinity) ||F(rho+h_L)||_(E_a)
         /(C/d_L)^(kappa/(-q-1)) >= M/sqrt(2kappa).

At the endpoint use sqrt(log(C/d_L)/(-q-1)) instead of the power.
Thus this family cannot have both d_L tending to zero and a bounded
weighted residual for a<=q+1. For the campaign q=4gamma-5,
q+1=4gamma-4. In the interval -2<a<=q+1 the repaired residual is
finite, since its next exponent q2=1-9delta is below -3, yet its norm
grows as above. The original residual has infinite E_a norm there.
There is no conflict with unweighted L2 stability, which uses a=0>q+1.

The numerical values of C and any radius chosen using nonrigorous
quadrature remain FLOAT. The proof needs only C finite and positive.
All claims are conditional on the displayed uniform remainder bound;
the exact algebraic campaign profiles supply that bound by their
convergent far-field expansions.
