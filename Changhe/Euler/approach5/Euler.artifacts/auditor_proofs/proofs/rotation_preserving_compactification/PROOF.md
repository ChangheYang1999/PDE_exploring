# Compactification preserving the rotational Killing field

Written: 2026-11-02T21:50:49Z. A205: CONFIRMED for the elementary compactification, localization and derivative estimates. The subsequent finite-regularity dynamical construction remains an explicit external premise.

## Statement

Let r>=2 be an integer, c>0, omega real, U in C^r(R3,R3), and U(y)=o(|y|) uniformly. Let J y=e3 cross y and B=cy-omega Jy+U. Choose R2>R1 large enough that

    c|y|^2+U(y).y >= b0 |y|^2    for |y|>=R1,

with b0>0. Let rho be a smooth radial function equal to one on the closed R1-ball, positive on the open R2-ball and zero outside it. Set

    X_omega=omega Jy-rho(cy+U).

In stereographic coordinates this extends to a C^r vector field on the round S3. It equals -B on the inner ball and is a rigid rotation on the exterior. Every positive-entropy ergodic probability of an integer-time map is carried by the original compact backward-flow core in the inner ball.

Write Y=-rho(cy+U) for the extended compactly supported field, g for the round metric and

    L=max_(S3) ||sym_g(nabla Y)||.

If F is the time-one map, then

    R(F)=lim_(n->infinity) log(max(||DF^n||_infinity,||DF^(-n)||_infinity))/n <= L.

The bound has no explicit omega term for fixed c,U,rho. It is not a common bound for different unknown profiles U_omega.

## Proof

Uniform sublinearity implies at most linear growth of B and hence completeness. Euclidean rotations extend under stereographic projection to round-sphere isometries, so Jy extends to a smooth Killing field. Y vanishes outside a compact coordinate subset and extends by zero, preserving C^r regularity.

In the annulus R1<|y|<R2,

    (1/2) d|y|^2/dt=-rho(c|y|^2+U.y)<0.

For any starting radius below R2, rho has a positive minimum on the interval from R1 to that radius, giving finite entrance into the inner ball. The ball is forward invariant. Annular points are nonrecurrent, so every invariant probability gives them zero mass. The exterior restriction is an isometry, hence has zero entropy for every invariant probability. A positive-entropy ergodic probability therefore lies in the inner ball; invariance puts it in the intersection of its forward images. There the compactified and original flows agree. The argument applies to every integer-time map.

For v_t=DTheta_t v, covariant differentiation gives

    d|v_t|_g^2/dt=2<sym_g(nabla X_omega)v_t,v_t>_g
                 =2<sym_g(nabla Y)v_t,v_t>_g.

The rotational term disappears because it is Killing. Thus both forward and backward derivatives have norm at most exp(L|t|). The sequence of maxima in R(F) is submultiplicative, so its logarithmic growth limit exists and is at most L.

## Sharper growth when W is actual vorticity

Assume also div U=0, W=curl U, [B,W]=-(1+c)W and 0<c<1/2. Put a=1-2c, d=3c and theta=B cross W. Then

    curl theta=-dW-[B,W]=aW.

Every C1 scalar function has derivative zero at almost every point of its zero set. Applying this componentwise to theta shows that theta=0 and W!=0 occur only on a null set. Exact bracket and carrier transport, together with the determinant identity, give

    (D Psi_t)^T theta(Psi_t x)=exp(a t)theta(x).

Each backward orbit lies in a compact ball. Bounding theta there yields

    ||D Psi_t(x)|| >= exp(a t)|theta(x)|/M_x.

Consequently the largest lower derivative exponent is at least a at almost every vortical point. Equivalent Euclidean and round metrics on the trapping ball give the same exponential rate. This is the already confirmed A027 estimate, rechecked here for its use with the compactification.

## Finite-r threshold: what is and is not established

The actual source in the team records defines R(F) using both forward and backward derivatives, as above. Theorem E assumes a positive-volume set with lambda_1>3R(F)/(r-1). Its remarks (3)-(4), printed pages 13-14, state that after geometric times are obtained the later measure and capture arguments require only C1+ regularity.

Thus the numerical inequality

    r>=3 integer,    r-1>3L/(1-2c)

is a sufficient strict growth threshold for that external construction on any positive-volume vortical residual set. This is a conditional source application, not a verification of the source's complete construction. Its endpoint Lipschitz compactness issue is recorded in A202.

For a finite-r localization argument, A201 can replace the infinite-flatness step: the stable curve through a typical irrotational hyperbolic point lies in {W=0}, contradicting transverse intersection with the original vortical image strips. The remaining basin-capture deduction is still under cross-agent review. No C2 existence or nonexistence theorem follows. In fact the source's k=1 C2 criterion would require lambda_1>3R(F), impossible since lambda_1<=R(F).
