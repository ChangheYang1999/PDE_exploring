# Verified derivative rules for the positive Stieltjes certificate

## Statement and scope

Use the real homogeneous seminorm

    [f]_alpha = sup_{z != w} |f(z)-f(w)| / |z-w|^alpha,

where 0<alpha<1. Define the Riesz transforms by the circular principal-value kernels and increments modulo constants of ../../01_setup/PROOF.md, with R_1^2=T_xx-I/2. Fix the admissible axis projection witness f of ../../11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md. Its parameters satisfy b>0, shift>=-1/2, and K>0 with [P]_alpha<=K. That proof gives

    D_alpha >= 1 + 4 integral_{X>0,Y>0} V(X,Y)(-d_Y f) dX,
    V(X,Y)=XY/[pi(((X-1/2)^2+Y^2)((X+1/2)^2+Y^2))].

The right-hand side is the exact increment of this witness. Every finite positive lower sum for its integral gives a lower bound for D_alpha.

Fix s in {-1,1}, a strip [l,r] with 0<l<r, X(t)=1/2+s t>0 in its interior, and two exact ratios 0<v_0<v_1. Write

    F(t)=f(X(t),t v_0)-f(X(t),t v_1),
    m=(l+r)/2, h=(r-l)/2.

The witness is nonincreasing in Y>0, so F>=0. Suppose certified enclosures give F(m)>=L_0. If F is continuously differentiable and |F'(t)|<=M_1 on the strip, then

    F(t)>=L_0-M_1 h.                                      (1)

If F' is Lipschitz, |F'(m)|<=M_0, and |F''(t)|<=M_2 almost everywhere, then

    F(t)>=L_0-M_0 h-M_2 h^2/2.                           (2)

Each lower bound, its maximum with zero, and its maximum with any other proved lower bound can be used in the positive Stieltjes rule. If exact subintervals partition [l,r], the minimum of valid lower bounds over all subintervals is another valid strip lower bound.

This statement proves the analytic rules. It accepts no production number and does not attest which source version an earlier process loaded. Those require separate provenance, coverage, recombination and replay audits.

## Proof of the scalar bounds

The fundamental theorem of calculus gives F(t)-F(m)=integral_m^t F'(u)du, proving (1). A Lipschitz derivative is absolutely continuous. Integrating it once more gives the Taylor remainder bound |F(t)-F(m)-F'(m)(t-m)|<=M_2|t-m|^2/2, proving (2). The maximum and subinterval claims follow pointwise. No cancellation or sign assumption on F' is needed.

## Certifying the active branch

On the right half-plane the witness is

    f=max(-H,min(H,G,Q)),
    H=2^(alpha-1)X^alpha,
    G=g+shift,
    Q=-1/2+P(X-1/2,Y)/K.

A strict interval comparison that proves Q<G, Q<H and Q>-H throughout a strip identifies f=Q there. The conditions H<min(G,Q) identify f=H. Either G<-H or Q<-H identifies f=-H. Finally G<Q, G<H and G>-H identify f=G. Each condition is sufficient. An inconclusive comparison simply supplies no derivative bound.

For f=G one also needs a fixed sign of g and one nearest component of the polygon throughout the strip. The polygon consists of the vertical axis, two closed line segments in the upper half-plane and one closed ray, with reflection in the horizontal axis. On Y>=0 the reflected lower components cannot be closer. Strict separation of one component's distance enclosure from the other three proves the required nearest component. Ties need not be resolved.

## Derivatives of the branches

The normalized projection branch is homogeneous and even in its first coordinate. With p(v)=P(1,v),

    Q(X(t),t v)=-1/2+t^alpha p(v)/K,
    Q'=alpha t^(alpha-1)p(v)/K,
    Q''=alpha(alpha-1)t^(alpha-2)p(v)/K.

Also

    H'=2^(alpha-1)alpha X^(alpha-1)s,
    H''=2^(alpha-1)alpha(alpha-1)X^(alpha-2).

The derivatives of -H have the opposite signs. On strips where these expressions are used, their denominators are bounded away from zero; otherwise no finite derivative certificate is obtained.

For the distance branch let z(t)=(X(t),t v), w=(s,v), and let rho(t)>0 be the distance to its uniquely nearest polygon component. Put n=grad rho and d=n dot w. Where the nearest point is an endpoint c, direct differentiation of rho=|z-c| gives

    rho'=d,
    rho''=(|w|^2-d^2)/rho.

Where the nearest point is in the interior of a line segment or ray, rho is distance to its supporting line. Because rho>0 its sign is fixed, and along the affine path rho''=0. At a transition between endpoint and interior projection the two expressions for rho and rho' agree. On a compact strip separated from the component, rho' is therefore Lipschitz, with almost-everywhere bound

    0<=rho''<=(|w|^2-d^2)/rho.                            (3)

For the axis component rho=X and rho''=0. These explicit formulas suffice; no general theorem about arbitrary convex sets is needed.

If the signed-distance sign is sigma in {-1,1}, then

    G'=sigma 2^(alpha-1)alpha rho^(alpha-1)d,
    G''=sigma 2^(alpha-1)[alpha(alpha-1)rho^(alpha-2)d^2
                         +alpha rho^(alpha-1)rho''].

Outward interval evaluation of these formulas and (3) bounds the derivatives of each node branch. Subtracting the node enclosures bounds F' and F''. Strict branch and nearest-component tests hold on the entire strip, so no unaccounted switch occurs in this subtraction.

## Safe powers and interval implementation

For a known nonnegative exact quantity x enclosed by a ball, the map x->x^alpha is increasing. If the ball is not certainly positive, the enclosure [0,U^alpha], where U is an upper bound for x, is valid. If U<=0, the exact quantity is zero. This avoids evaluating a logarithm across zero. Returning no finite candidate is also safe provided the contribution is discarded, since the Stieltjes measure and V are nonnegative.

For a fixed X, V is positive and unimodal in Y>0, as proved in the parent Stieltjes proof. Thus a lower bound B for both endpoint values of V bounds V throughout the vertical cell. A strip variation lower bound A>=0 contributes at least (r-l)AB to the integral. Outward bounds on A, B and r-l therefore suffice.

In particular, a lower endpoint from a direct enclosure, (1), (2), and the exact profile difference l^alpha(p(v_0)-p(v_1))/K when both node branches are Q are compatible candidate rules. For subinterval refinement every subinterval must have been checked before a stronger minimum is accepted. Early termination is safe only when the current minimum already fails to improve the old bound or is nonfinite, and that partial minimum is then rejected.

## Dependencies and remaining checks

Admissibility and the positive integral identity are in the parent Stieltjes and monotone-axis proofs. The derivative argument above is independent of floating optimization. The observed lead source is frozen in preliminary/cert_v7.py. Its strict comparisons, derivative formulas, endpoint kernel rule and rejection of incomplete refinements agree with this proof. Production coverage, source-at-start evidence and numerical reproduction remain separate obligations.
