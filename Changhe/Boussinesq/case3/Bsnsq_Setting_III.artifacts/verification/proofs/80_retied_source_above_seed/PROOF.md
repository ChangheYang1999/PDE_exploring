# The source tail when the retied exponent increases

Date:2026-10-20. Status: complete proof. No continuation endpoint is excluded.

## Fixed source and exact transformed coefficient

Let beta_S>1, L>0 and let D be continuous on[0,1] and C1 near1 with D(1)!=0. Along the positive horizontal ray suppose a fixed source has the exact form

    f_S(r,0)=r z_S^(beta_S+1) D(1-z_S),
    z_S=(1+(r/L)^2)^(-1/(2beta_S)).

This applies to the saved r2 seed's E-Omega_S: at y=0 the odd angular cosines vanish, so D(t) is the finite signed sum of the even indexed radial spline coefficients. The origin mask does not alter their values near t1. Packet76 checks D(1)!=0 for the actual beta_S3 seed by exact rational arithmetic.

For a new beta>1 put z=(1+(r/L)^2)^(-1/(2beta)), t=1-z, gamma=beta/beta_S and alpha=gamma-1. Dividing the same physical source by the new radial envelope gives exactly

    T_beta(t)=f_S(r,0)/(r z^(beta+1))
             =z^alpha D(1-z^gamma).                       (1)

Indeed z_S=z^gamma and gamma(beta_S+1)-(beta+1)=gamma-1. This is an algebraic change of coordinates, with L fixed. No fit is involved.

The endpoint behavior is therefore:

    beta<beta_S: |T_beta(t)| tends to infinity as t->1;
    beta=beta_S: T_beta(t)=D(t), with endpoint D(1);
    beta>beta_S: T_beta extends continuously with endpoint0. (2)

For beta_S<beta<2beta_S, T_beta is not C1 at1: its derivative has leading term -alpha D(1) z^(alpha-1). This is loss of regularity in the compactified coefficient, not loss of smoothness of the physical fixed source at a finite point.

## The endpoint error of any finite retied representation

Let a represented source on the same ray be

    f_N(r,0)=r z^(beta+1) P_beta(1-z),

where P_beta is continuous at1, as every finite spline representation is. If beta>beta_S, then

    lim_(r->infinity) r^(1/beta) (f_N-f_S)(r,0)
       =L^(1+1/beta) P_beta(1).                            (3)

To prove this, r^(1+1/beta)z^(beta+1)->L^(1+1/beta), P_beta(1-z)->P_beta(1), while T_beta(1-z)->0. Consequently the full-plane weighted source error is at least the absolute value of the right side. The bound uses only one ray. It can be strengthened using all angular endpoint coefficients.

In particular, a nonzero represented endpoint coefficient can yield a large global weighted error even if all measured finite-radius errors are small. It is NOT asserted that every retied approximation has such an error: choosing the appropriate zero endpoint coefficients removes this particular lower bound, and a fixed continuous T_beta can be approximated uniformly by sufficiently fine continuous splines.

If the represented source has finite angular modes and a nonzero angular r^(-1/beta) coefficient a_N, while beta>beta_S>1, packet78's modal calculation gives

    r^(-(1-1/beta)) B[f_N-f_S](r,phi)->v_(a_N)(phi),

where v_(a_N) is the explicit nonzero angular vector in packet78 with nu=1/beta. The original fixed source contributes0 to this limit, since it decays faster. Thus the same represented tail is visible in the canonical velocity norm. A constant gauge cannot remove it.

For beta<beta_S, packet76 instead gives an infinite source error in the new weight, and packet78 gives an infinite velocity error there. The two sides of beta_S therefore have different conclusions: divergence below, an explicit finite lower bound above. Neither conclusion alone excludes the zero-forcing endpoint.

## Lack of continuity in the retied uniform coefficient norm

The family T_beta, regarded as elements of C([0,1]) for beta>=beta_S, is not continuous at beta_S in the supremum norm: for every beta>beta_S,

    ||T_beta-T_beta_S||_infinity >= |D(1)|,                (4)

because their endpoint values are0 and D(1). The functions do converge pointwise on every t<1 and uniformly on every fixed compact subinterval of[0,1).

More concretely, suppose finite spline coefficients P_beta depend continuously on beta, the basis has a continuous endpoint evaluation, and P_beta_S(1)=D(1). Then P_beta(1)->D(1) as beta decreases to beta_S from above. Equation(3) implies a nonvanishing lower bound for the global weighted source error of that coefficient-continuous family. Such a family cannot give uniformly small errors in these retied norms across beta_S, even though its local physical errors can tend to0.

This statement concerns the indicated approximation family and norms. It is not an obstruction to a formulation that keeps the original source and its original inverse separately, uses a fixed weaker space, or enriches the representation with the original tail.

## Why a finite radial window misses the endpoint change

Write nu=1/beta, nu_S=1/beta_S and delta=nu_S-nu>0 when beta>beta_S. In the leading far field, multiplication by the new source weight changes the old power by r^-delta. The radius at which this factor is q, with0<q<1, is exactly

    R_q=q^(-1/delta),  log R_q=-log(q)/delta.               (5)

This is a formula for the ratio of pure powers, not a claimed error threshold for the full source. As beta decreases to beta_S from above, delta tends to0 and this radius grows faster than any fixed power of1/(beta-beta_S). Thus a very large but finite radial window can still see almost no suppression of the original coefficient, although its correctly weighted endpoint is0.

For the exact compactified factor z^alpha the analogous condition z^alpha=q is z=q^(1/alpha), with physical radius L sqrt(q^(-2beta/alpha)-1). These exact formulas give the same leading exponential scale, since alpha/beta=delta.

## Application and limits

The actual seed has beta_S=3, L=1.5 and the nonzero endpoint certificate in packet76. The ongoing additive-forcing secant has evaluated beta>3 (read-only logs checked separately). The conclusions above apply to any archived represented forcing only after its stage coefficients, scaling by lambda and schema have been independently identified. No coefficient value for an unfinished stage is inferred from its log summary.

Dependencies: elementary endpoint limits, the exact seed certificate of packet76, and the independent canonical modal inversion of packet78. This complete proof precedes any numerical illustration or source-stage audit.
