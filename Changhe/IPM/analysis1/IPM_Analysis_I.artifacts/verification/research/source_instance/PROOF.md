# Instantiation of the local source estimate for modal_v2

Status at proof writing: complete analytic reduction; fresh source enclosures, exact dependency checks and model review are pending. This is topic89. The result is an actual local a priori estimate and a cut-off auxiliary operator statement for the exact normalized trial, conditional on the explicitly audited archive. It is not a global IPM inverse.

## 1. Trial and intended source certificate

Use the exact normalized modal_v2 density of topic15, with canonical stream function -Delta psi=rho_x, velocity U=(-psi_y,psi_x), raw strain sigma=psi_xy(0) and c_l=(1+sigma)/3=1/k. The defining normalization coefficient is the exact real specified in topic15; every archive ball encloses that coefficient's consequences. No midpoint replaces it. The canonical archive and complete original spline polynomials are the same inputs accepted in topics31,84,85.

Put a=4841405518533377/562949953421312 and b=4841405518533711/562949953421312. Define w(x)=V_1(x,0), V=c_l X+U. The fresh certificate must show, separately in Arb and mpmath.iv,

 w(a)<0<w(b),
 10<=w'(x)<=51/5,
 99/100<=mu(x)<=101/100,
 29<=g(x)<=30  for every x in[a,b],                        (1)

where mu=partial_y V_2(x,0) and g=rho_y(x,0). Continuity then gives a zero p in(a,b); w'>0 proves uniqueness on that interval. Parity gives V_2(x,0)=0, partial_y V_1(x,0)=0, partial_x V_2(x,0)=0 and rho_x(x,0)=0. Thus P=(p,0) is an exact equilibrium, DV(P)=diag(A,mu) with A=w'(p), and grad rho(P)=(0,g). Canonical divergence freeness gives div V=2c_l=A+mu exactly. None of these conclusions assumes rho is stationary, and mu is not set equal to1.

## 2. Independent moment and scalar computation

Write rho=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta), t=log r, with H_261=0. For n=1,...,261 put m=2n, I_n'=-(m+4)I_n+H_(n-1), J_n'=(m-4)J_n-H_n. The canonical stream is psi=r^4/2 sum_n(J_n-I_n)sin(mtheta). On one source span [ta,tb], its complete degree7 polynomials are centered at tm=(ta+tb)/2. The accepted archive supplies I_n(ta) and J_n(tb), including their radii.

For t in this span and L=t-ta,R=tb-t,

 I_n(t)=exp(-(m+4)L)I_n(ta)
      +integral_0^L exp(-(m+4)v)H_(n-1)(t-v)dv,
 J_n(t)=exp(-(m-4)R)J_n(tb)
      +integral_0^R exp(-(m-4)v)H_n(t+v)dv.                 (2)

For the first engine, shift all complete polynomials and evaluate each monomial moment as

 integral_0^L exp(lambda v)v^j dv
 =L^(j+1) sum_(q=0)^N (lambda L)^q/[q!(j+q+1)] + error.

For 0<=L<=Lmax and zmax>=|lambda L| with zmax<N+2, the absolute error is at most

 Lmax^(j+1) zmax^(N+1)
 /[(N+1)!(j+N+2)(1-zmax/(N+2))].                          (3)

The bound follows by a geometric majorant for the ratios of successive positive terms. Interval uncertainty in L and shifted coefficients is retained. We use N80 and check its strict hypothesis for every moment.

For the second engine, if lambda!=0 and Q(v)=sum_j q_j v^j, the exact primitive is

 exp(lambda v) sum_l [sum_(j>=l)q_j(-1)^(j-l)j!/(l!lambda^(j-l+1))]v^l.

Differentiating verifies it coefficient by coefficient. Evaluate the endpoints with directed interval arithmetic. For lambda=0 use the exact polynomial integral. This method uses no series remainder. Both methods start from the same pinned canonical endpoint balls but propagate them through different identities.

Polar differentiation at theta=0 gives

 w(x)=c_l x+x^3/2 sum_n m(I_n-J_n),
 mu(x)=c_l+x^2/2 sum_n m[(m+1)I_n+(m-1)J_n-H_(n-1)-H_n],
 g(x)=x^2 sum_j(2j+1)H_j.

Independently differentiating w using the ODEs gives

 w'(x)=c_l+x^2/2 sum_n m[-(m+1)I_n-(m-1)J_n+H_(n-1)+H_n]. (4)

One engine forms mu first and uses2c_l-mu; the other forms w' directly and uses2c_l-w'. The algebraic identity is also checked exactly for all261 modes. Whole-interval evaluation proves(1); point evaluations prove the endpoint signs. Each engine must separately pass, not merely overlap the other.

## 3. Regularity and cutoffs on the source disc

The containing disc B_(99/2000)(P) is separated from the origin and lies within the original spline radial region, as checked using exact endpoint inequalities. The factor modes are degree7 splines with simple interior knots and hence C6; the finite density angular combination remains C6 on this disc. To see the spline claim directly, adjacent degree7 pieces satisfy the standard knot recursion, and at a simple knot the matching derivatives through order6 follow by the degree-reducing derivative recursion. At a repeated knot the conclusion would change, so the actual exact knot multiplicities are checked.

No unquantified elliptic regularity theorem is needed here. The ODEs in(2) have C6 forcing and constant coefficients, so I_n,J_n are C7 locally; the canonical anchors are constants for this local claim. Therefore psi is C7, U is C6, V is C6 and rho is C6 across all these joins. In particular V is C4 and rho C5 as required by topic77.

Put delta=33/2000. A concrete smooth cutoff with the needed derivative bound exists as follows. Let F(u)=1 for u<=9/4, F(u)=0 for u>=11/4 and linear of slope-2 between them. Convolve F with any nonnegative C-infinity function supported in[-1/8,1/8] of integral1, and call the result Theta. Then0<=Theta<=1, Theta=1 for u<=17/8, Theta=0 for u>=23/8, and |Theta'|<=2. Define theta(X)=Theta(|X-P|/delta). It is smooth at P because it is constant nearby; theta=1 on B_(2delta), its support is strictly inside B_(3delta), and delta||grad theta||<=2. The remaining chi,tau,zeta cutoffs of topic77 are chosen with its strictly nested supports by the same smoothing construction; no numerical derivative constants for them are claimed.

Define wvec=theta(V-D(X-P)) and qvec=theta(grad rho-(0,g)). They are globally C4 and compactly supported, by smooth extension by zero. Their derivative norms entering topic77's lower-order constant R are finite. The inequalities0<delta<=1 and3delta<p/2 are exact consequences of the bracket.

## 4. Local estimate and auxiliary inverse

The independent Hessian certificates84 and85 hold for every center p in[a,b], so they apply to this exact equilibrium. Topic86 then gives E<22953051/10^8 and kappa-E>314446949/10^8. All local geometric, regularity and cutoff hypotheses of topic77 are now instantiated for this trial, provided the fresh tests(1) and exact linkage checks pass. Its local estimate(26) applies to the stated smooth zero-jet test class and its stated graph completion, with

 K_1=1/(kappa-E)<100000000/314446949<0.3181.

Every other term of that estimate remains present, including the annular and lower-order norms and the remote moments. K_1 alone is not the norm of an inverse operator. The other K_i are finite analytic expressions from the specified cutoffs and coefficients, but are not numerically enclosed here.

For the associated full-plane cut-off auxiliary operator Aop of topic78 on its maximal distributional transport domain in H^(31/10), global compact C4 coefficients and E<kappa now give an actual bounded inverse. Its proved bound is

 ||Aop^(-1)|| <= (1+R/d)^(31/10)/(kappa-E),
 d=1+(A+mu)/2-kappa+s||Dwvec||_infinity,F >=3121/1000.

R is the finite lower-order commutator constant defined in topic77. This is an analytic bound containing an unevaluated finite R, not a reported numerical inverse norm. The rank-one perturbation by canonical strain still requires a separately nonzero denominator. No matching to outer data, global normalized IPM inverse, residual norm or nonlinear closure follows.

The same instantiated source matrix has symmetric part at least99/100. On the whole disc, ||DV-DV(P)||op<73557/5000000<99/200 by topic85 and the segment formula. Thus the nondecreasing radial source cutoff of topic88 has V.grad zeta>=0 there. This verifies the cutoff sign for this trial on this disc only.

All claims refer to exact normalized modal_v2, not to original stored X3 or to an exact stationary solution. This is no decisive endpoint.
