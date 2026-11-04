# Smooth periodic return rigidity for an exact bracket pair

Written: 2026-11-02T21:49:22Z. A203: CONFIRMED. Source under review: coordinator regular_plug/local_rigidity, independently cross-checked by the model coordinator.

## Statement

Let X,W be smooth real vector fields and m a smooth positive volume form near a periodic orbit of X. Assume

    [X,W]=lambda W,    div_m X=-delta,    div_m W=0,
    mu=lambda-delta>0,    lambda>mu>0,

and that X and W are independent on the orbit. Put r=lambda/mu. Every local first-return germ of X on a transverse section is smoothly conjugate to

    (u,v) -> (bu,b^(-r)v),    b=exp(mu T)>1,

where T is the period. The return-time function is smoothly cohomologous, locally, to T.

This applies to every vortical regular hyperbolic periodic orbit of a smooth Euler profile, with X=-B, lambda=1+c, mu=1-2c, 0<c<1/2. It applies for arbitrary finite rotation. The statement is local and does not imply a global attractor or an Euler exclusion.

## Exact return coordinates

Set alpha=i_W i_X m. Cartan's formulas give

    L_X alpha=mu alpha,    d alpha=-mu i_W m,    alpha(X)=alpha(W)=0.

Choose a small transverse section saturated by short W arcs. Its tangent space contains W, so d alpha restricts to zero. Since alpha is nonzero on the other section direction, one can choose local coordinates satisfying alpha=du and W=partial_v on the section.

For the return P(z)=Psi_(tau(z))z, differentiation along W gives

    DP W=exp(-lambda tau) W(Pz)+(W tau)X(Pz).

Both the left side and the first term are tangent to the target section; its transversality to X implies W tau=0. Also P*alpha=exp(mu tau)alpha because alpha(X)=0. Thus

    P(u,v)=(F(u),F'(u)^(-r)v+G(u)),
    tau(u)=log(F'(u))/mu.

At a fixed point placed at (0,0), F(0)=G(0)=0 and F'(0)=b. In particular both multipliers are positive; an absolute-value multiplier relation alone omits a necessary condition.

## Smooth linearization, including convergence

Let g=F inverse on a small interval, and put

    q(u)=log(F(u)/(bu)),
    h(u)=-sum_(n>=1) q(g^n(u)),    phi(u)=u exp(h(u)).

The quotient extends smoothly and positively through zero, with q(0)=0. Choose sigma strictly between sup|g'| and 1. For each k>=1 the chain rule gives ||D^k g^n||<=C_k sigma^n. Indeed the highest derivative is multiplied by sup|g'|, and every other term contains at least two lower derivatives; induction and a geometric convolution prove the assertion. The zeroth-order bound on q(g^n(u)) uses q(0)=0, and its differentiated bounds follow by the same chain rule. Therefore the series converges in every C^k norm on one fixed small interval.

We have h(Fu)=h(u)-q(u), phi'(0)=1 and phi(Fu)=b phi(u). After reducing the interval, phi'>0. In coordinates

    U=phi(u),    V=phi'(u)^(-r)v,

the derivative identity phi'(Fu)F'(u)=b phi'(u) transforms P into

    (U,V) -> (bU,aV+H(U)),    a=b^(-r).

Here H is smooth and H(0)=0. Define

    k(U)=-sum_(j>=1) a^(j-1) H(b^(-j)U).

The series and all its derivatives converge geometrically. It satisfies k(bU)-a k(U)=-H(U). Replacing V by V+k(U) gives the diagonal linear germ.

Finally

    tau(u)=T+log(phi'(u))/mu-log(phi'(F(u)))/mu.

This proves the roof assertion without invoking a global Livsic theorem.

## Explicit local germs excluded by this condition

Suppose r=p/q>1 with coprime positive integers p,q. In Euler parameters,

    c=(p-q)/(2p+q),    mu=3q/(2p+q),    lambda=3p/(2p+q).

On a circle coordinate theta of period one and two transverse coordinates, let

    X=partial_theta+mu u partial_u-lambda v partial_v+epsilon H,
    H=(q+1)u^(p+1)v^q partial_u-(p+1)u^p v^(q+1) partial_v,
    epsilon!=0.

For m=dtheta du dv, the two nonlinear divergences cancel, so div X=mu-lambda. The central orbit has period one and multipliers b=exp(mu), a=exp(-lambda), with b^p a^q=1. If L=(mu u,-lambda v), then [L,H]=(p mu-q lambda)H=0. H is homogeneous of degree d=p+q+1. Commuting the local flows gives the transverse time-one expansion

    P(z)=Dz+epsilon D H(z)+O(|z|^(2d-1)),    D=diag(b,a).

If a smooth linearizing conjugacy existed, normalize its derivative at zero to I, since its derivative commutes with D. A first-component monomial u^i v^j is resonant exactly when q(i-1)=pj; a second-component monomial is resonant exactly when qi=p(j-1). There are no nonlinear resonances of degree below d. The conjugacy equations force all its terms of degrees 2 through d-1 to vanish. At degree d they would require

    C_d(Dz)-D C_d(z)=-epsilon D H(z).

The left side has zero coefficients on the two resonant monomials displayed in H, while the right side has nonzero coefficients. This is impossible.

Therefore these germs cannot be the return germs of a smooth exact bracket pair with the stated independent W and positive-volume hypotheses, even after smooth conjugacy, positive smooth time change or change of volume density: those operations preserve the return germ up to smooth conjugacy. At c=2/5, p=7,q=1 gives the degree-nine perturbation epsilon(2u^8 v,-8u^7 v^2). For the open target interval, rational ratios r>7 give further examples.

## Scope

This excludes explicit local constant-divergence germs, not every return map or a global expanding attractor satisfying all periodic data. It proves that the local multiplier relation by itself is insufficient for smooth exact realization. No conclusion about merely C1 realizations follows. No computation or Lean verification is required for these derivative and Taylor identities.
