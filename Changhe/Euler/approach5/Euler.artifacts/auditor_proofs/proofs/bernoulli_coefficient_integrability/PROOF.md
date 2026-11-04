# Integrability of the Bernoulli coefficient and the vanishing threshold

## Exact statements

Retain all hypotheses and notation of in the team records: a decaying C2 Euler profile, 2/5<=c<1/2, arbitrary finite omega, a=1-2c, beta=5-2/c, complete carrier Phi, fixed canonical P0, q=|U|^2/2, H0=P0-q+U.B, and the coefficient K on its invariant full-measure domain G. Define

    p_star=2(1-c)/a, p_critical=3c/a.

Then K belongs to Lp_loc for every 1<=p<p_star. For 2<=p<p_star, bounded measurable Q and T>=0,

    ||sup_(t>=T)|exp(at)H0(Phi_t y)-K(y)||_Lp(Q)
       <= C_(Q,p) exp(-gamma_p T),
    gamma_p=2(1-c)/p-a>0.

More generally, for this carrier any measurable F satisfying F(Phi_s y)=exp(-as)F(y) on an invariant full-measure domain for every real s must be zero almost everywhere if F belongs to Lp_loc for a finite p>=p_critical. Local essential boundedness also suffices. The latter statement uses only bounded U, its divergence-free property, and c,a>0, not the Euler pressure equation.

For 2/5<c<1/2 the guaranteed interval lies strictly below the vanishing threshold: p_critical-p_star=(5c-2)/a>0. At c=2/5 the endpoints agree but the guaranteed integrability remains strict. No conclusion K=0 or U=0 follows from these estimates.

## Fixed pressure in local Lp

For finite p>=2 split the canonical tensor source into B_(2R) and its complement, R>=1. The usual boundedness of double Riesz transforms on Lp, 1<p<infinity, gives

    ||sum R_i R_j(1_(B_2R) U_i U_j)||_Lp^p
       <= C_p integral_B_2R |U|^(2p)
       <= C_p ||U||_infinity^(2p-2) E(2R)
       <= C_p R^beta.

If U=0 the conclusion is immediate. The multiplier here includes its distributional local delta term. The far part is bounded pointwise on B_R by C R^(beta-3), using the exact same absolutely convergent dyadic tail as A277. Therefore

    integral_B_R |P0|^p <= C_p[R^beta+R^(3+p(beta-3))]
                        <= C_p R^beta.

The last inequality follows from 3+p(beta-3)-beta=(p-1)(beta-3)<=0. Also q^p<=C_p |U|^2 because U is bounded. Thus integral_B_R|P0-q|^p<=C_p R^beta. This is the same P0 for every R and p; no annular constants are introduced.

The bound Phi_t Q contained in B_(R_Q exp(ct)) and Jacobian exp(3ct) give

    ||(P0-q) composed Phi_t||_Lp(Q)
       <= C_(Q,p) exp(c(beta-3)t/p)
       = C_(Q,p) exp(-2(1-c)t/p).

## Coefficient estimate and common representative

The exact equation d/dt[exp(at)H0(Phi_t)]=a exp(at)(P0-q)(Phi_t) has right side with Lp norm bounded by C exp(-gamma_p t). Finite-interval Minkowski followed by monotone convergence therefore gives

    ||integral_T^infinity exp(at)|(P0-q)(Phi_t)| dt||_Lp(Q)
       <= C_(Q,p) exp(-gamma_p T)/gamma_p.

On the same G defined by absolute convergence in A288, this pointwise integral already defines K-H0. Thus every Lp limit is the same K. Its tail gives the supremum estimate. H0 is continuous and hence in every local finite Lp; K belongs to the asserted spaces for p>=2. Holder on bounded sets supplies 1<=p<2. Since p_star>2, the whole interval is covered. At p_star the weighted bound is merely constant in time, so this calculation proves no endpoint convergence or endpoint Lorentz improvement.

## Exact kinematic vanishing threshold

Every bounded Q has all negative images Phi_-t Q contained in one compact ball C_Q. Indeed the radial bound is |Phi_-t y|<=exp(-ct)|y|+||U||_infinity/c. For finite p, covariance and change of variables give

    integral_(Phi_-t Q)|F|^p
       =exp((ap-3c)t) integral_Q|F|^p.

The invariant domain and smooth invertibility ensure no exceptional-set problem. If ap>3c, the left side is bounded by integral_C_Q|F|^p<infinity; letting t increase forces integral_Q|F|^p=0. If ap=3c, |Phi_-t Q|=exp(-3ct)|Q| tends to zero. Absolute continuity of the integral of |F|^p on C_Q then makes the left side tend to zero. This proves the endpoint as well. A countable covering by Q proves F=0 almost everywhere. A locally essentially bounded F lies in every finite local Lp, so the same conclusion follows.

## Sharp scalar test and Euler limitation

For the linear carrier B=Ay take F(y)=|y|^(-a/c) off zero and F(0)=0. Its radius scales by exp(cs), so covariance holds at every point and every real time. The local integral at the origin is

    4pi integral_0^R r^(2-ap/c) dr,

finite exactly when p<3c/a. Thus no smaller local Lp threshold can force an arbitrary covariant scalar to vanish. This does not show that the guaranteed p_star bound is sharp for an actual Euler coefficient. For the actual U=0 profile, canonical P0, H0 and K are all zero; this nonzero F is not that coefficient.

Finally p_critical-p_star=(3c-2+2c)/a=(5c-2)/a, giving the strict gap and its endpoint equality. Even a future proof K=0 would require an additional argument for U=0. No computation or formalization is used. The only new analytic input beyond A288/A277 is the standard Lp double-Riesz bound, with its exact exponent range stated above.
