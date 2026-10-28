# Frozen saddle Holder estimates and audit of the proposed local extension

## Scope, spaces and dependencies

This proof concerns the whole-plane frozen operator

    T0 = -A x partial_x + D y partial_y - 1,  A>0, D=2A+1.

Its flow is Phi_t(x,y)=(exp(-At)x,exp(Dt)y). All densities are real, even in x and odd in y. Axis values of continuous densities are their continuous values. Weighted measurable spaces below are interpreted off the axes, with the essential supremum. Holder exponents satisfy 0<alpha<1. The only prior dependency is the canonical velocity and its parity in proof 01. This topic does not use an external linearization theorem.

The theory author text audited here is the fixed snapshot in evidence/lead_snapshot.md, SHA-256 recorded in evidence/snapshot.json. The statements below replace the indicated claims where necessary. Constants denoted C are finite and depend only on explicitly fixed smooth cutoffs, A, alpha, and the stated local background norms. They are not certified numerical constants.

## Weighted supremum inverse

For a,b>=0 define E_(a,b) by

    ||f||_(a,b)=ess sup |f(x,y)|/(|x|^a |y|^b).

On the maximal distributional domain {h in E_(a,b): T0h in E_(a,b)}, understood on each open quadrant, if kappa=1+aA-bD>0, T0 is bijective and

    R0 f = -integral_0^infinity exp(-t) f(Phi_t X) dt,
    ||R0|| = 1/kappa.                                      (1)

The integral is absolutely convergent at every point where the weighted bound holds, because its integrand is bounded by ||f|| |x|^a|y|^b exp(-kappa t). Differentiating along a characteristic, or first testing in quadrant logarithmic coordinates, proves T0R0 f=f distributionally. Conversely, a homogeneous solution satisfies exp(-t)h(Phi_t X)=h(X). Its weighted bound tends to zero as t tends to infinity, so h=0. The same characteristic argument for distributions follows by the change of variables (log|x|,log|y|), where the directional derivative has constant coefficients; Fubini reduces it to the one-dimensional distributional fundamental theorem. The graph is closed because weighted convergence implies distributional convergence on compact subsets of a quadrant.

The function |x|^a |y|^b sgn(y) is an eigenfunction with eigenvalue -kappa and norm1. It proves the exact norm in (1). If continuity on axes is additionally imposed, smooth axis approximations give the same norm as a supremum even when this eigenfunction is discontinuous there.

A cutoff of x^2y belongs locally to E_(a,b) exactly when a<=2 and b<=1. Excluding it and having kappa>0 therefore forces a>2: if b>1 then a>(Db-1)/A>2. At a=2,b=1, kappa=0. This confirms H0, with the weighted realization specified. Formula(1) is not restricted to globally bounded h when the weights grow.

## Isotropic and anisotropic Holder inverses

For bounded continuous f define

    [f]_x = sup |f(x,y)-f(x',y)|/|x-x'|^alpha,
    [f]_(y,p) = sup |f(x,y)-f(x,y')|/(|x|^p |y-y'|^alpha),
    ||f||_E = ||f||_infinity+[f]_x+[f]_(y,p),  p>=0.

For p=0 the denominator |x|^p is1, including on the axis. For p>0 the quotient condition and continuity require f(0,y)=0. Write E=C^alpha_p for the resulting Banach space. Completeness follows from uniform convergence and lower semicontinuity of both difference quotients. These norms are locally equivalent to ordinary C^alpha when p=0. For p>0, restriction to |x|<=R has ordinary Holder seminorm at most [f]_x+R^p[f]_(y,p), up to the harmless equivalence between the sum and Euclidean distances.

On D(T0)={h in E:T0h in E distributionally}, if

    kappa_p=1+pA-Dalpha>0,

T0 is bijective and its inverse(1) satisfies

    ||R0 f||_infinity <= ||f||_infinity,
    [R0 f]_x <= [f]_x/(1+Aalpha),
    [R0 f]_(y,p) <= [f]_(y,p)/kappa_p.                    (2)

Indeed the two differences under the integral acquire the factors exp(-Aalpha t) and exp((-pA+Dalpha)t), respectively. The integrals give(2). The distributional equation follows by testing and the bounded inverse by dominated convergence. Every bounded homogeneous solution is zero, by exp(-t)h(Phi_t X)=h(X). The domain is closed since E embeds locally into continuous functions and differentiation is distributionally continuous. Strong continuity of translations in the large Holder norm is not needed for this argument.

For the ordinary isotropic Holder seminorm and alpha<1/D, the flow has Lipschitz constant exp(Dt), so

    [R0 f]_alpha <= [f]_alpha/(1-Dalpha).                 (3)

This proves S(a).

## The sharp threshold, including equality

The condition kappa_p>0 is necessary for bounded inversion on E, for every p>=0. The test proposed in the theory author text, |x|^p chi(x)psi(y), is not in E when 0<p<alpha. The following construction repairs that membership problem and also handles equality.

Choose a nonnegative even smooth chi, equal1 on [-1,1] and zero outside[-2,2]. Put

    q=max(alpha-p,0)/alpha,
    Phi(z)=sgn(z)|z|^alpha chi(z).

If q>0 set

    f(x,y)=|x|^alpha chi(x) Phi(y/|x|^q), x!=0,
    f(0,y)=0.                                           (4)

If q=0 set f(x,y)=|x|^p chi(x)Phi(y). Both formulas give the correct parity and compact support. For q>0, at fixed x, scaling of the y seminorm gives

    [f(x,.)]_alpha <= C |x|^(alpha-qalpha)=C|x|^p.

Away from x=0, differentiation in x gives |partial_x f|<=C|x|^(alpha-1): Phi and z Phi'(z) are bounded, with derivatives interpreted away from z=0. Integration of this bound proves uniform alpha-Holder continuity in x on either half-axis; across0 use |f(x,y)|<=C|x|^alpha. Thus f belongs to E. For q=0 the same conclusion follows from p>=alpha and the fixed cutoffs.

Fix 0<x0<1/2 and 0<y<x0^q. Until

    T(y)=log(x0^q/y)/(D+Aq),

both cutoffs sampled by the trajectory equal1, so

    f(Phi_t(x0,y))=x0^p y^alpha exp((-pA+Dalpha)t).

The forcing is nonnegative for y>0 along the entire trajectory. Since R0f(x0,0)=0, its y quotient is at least

    |R0f(x0,y)|/(x0^p y^alpha)
       >= integral_0^T(y) exp(-kappa_p t)dt.              (5)

The right side diverges as y tends to0 if kappa_p<=0. The bounded solution exists for this bounded forcing, but is not in E. Thus (2)'s threshold is sharp, including the critical exponent. In particular S(a)'s endpoint alpha=1/D also fails as a bounded inverse on C^alpha_0. This failure uses admissible Holder data; it does not assert that every smooth forcing has a logarithmic singularity at that endpoint.

For p=2 one has kappa_p=D(1-alpha)>0 for every alpha<1. For the smooth resonant forcing f=x^2y chi(r), with a radial cutoff equal1 near0, formula(1) instead gives, for fixed sufficiently small nonzero x and y tending to0,

    R0f(x,y)=-(x^2y/D)log(1/|y|)+O_x(x^2|y|).           (6)

The integrand's polynomial factor is exactly constant under exp(-t)Phi_t. The interval on which the cutoff equals1 has length D^(-1)log(1/|y|)+O_x(1), and the two transition intervals have bounded lengths. For a smooth cutoff the remaining integral is an integral of chi, not literally the measure of its support.

## Smooth-data cusp at the isotropic threshold

Let f be compactly supported C1, with the stated parity. Then

    M_f=integral_0^infinity u^(-1-1/D) f(0,u)du

converges: near0 use |f(0,u)|<=||partial_y f||_infinity u and D>1; at infinity use compact support. Substituting u=y exp(Dt) in(1) gives

    R0f(x,y)=-(y^(1/D)/D)
       integral_y^infinity u^(-1-1/D)
          f(x(y/u)^(A/D),u)du.                           (7)

For every fixed x the integrand converges pointwise to u^(-1-1/D)f(0,u). Uniform domination is given by C u^(-1/D) on(0,1) and C u^(-1-1/D) on(1,infinity), because f(x',0)=0. Dominated convergence proves

    R0f(x,y)=-(M_f/D)y^(1/D)+o(y^(1/D)), y->0+.

For f=y chi(r), chi nonnegative, nonzero and smooth, M_f>0. The bounded solution is therefore not C^alpha for alpha>1/D. This confirms S(b). It is a whole-plane bounded-solution statement; a local equation with unspecified boundary values has additional homogeneous solutions.

## A correct local coupling statement

Assume rho is C4 on B_(delta0), even in x, odd in y, rho(0,y)=0 and rho=x^2y+O(r^4) at0. The parity is required: without it, rho=x^2y+xy^3 obeys the other displayed assumptions but rho_x(0,y)=y^3. Division by x twice, using Taylor's integral remainder, gives

    rho_x=x a1, rho_y=x^2 a2,
    ||a1||_(infinity,Bdelta)<=Cdelta, ||D a1||<=C,
    ||a2||<=C, ||D a2||<=C,

uniformly for small delta. Only these bounds are needed. Explicitly a1=integral_0^1 rho_xx(sx,y)ds, while a2=integral_0^1(1-s)rho_xxy(sx,y)ds. Their first derivatives require at most four derivatives of rho. Odd y parity gives rho_xx(0,0)=0, and hence the stated O(delta) bound for a1. The actual modal trial is C4 at0 by its inner expansion, although its nonpolynomial degree5 angular term prevents C5 regularity there; see proof 33.

Let chi_delta be smooth, supported in Bdelta, equal1 on B_(delta/2), with ||Dchi_delta||<=C/delta. If U belongs to C^alpha(Bdelta), U(0)=0, and

    F=chi_delta U dot grad rho,

extended by0, then

    ||F||_infinity <= Cdelta^(2+alpha)||U||_(C^alpha(Bdelta)),
    [F]_x <= Cdelta^2 ||U||_(C^alpha(Bdelta)),
    [F]_(y,1) <= Cdelta ||U||_(C^alpha(Bdelta)).           (8)

For a complete product estimate, write F=xH1+x^2H2 with Hj=chi_delta aj Uj, extended by0. The cutoffs imply [chi_delta a1]_alpha<=Cdelta^(1-alpha), [chi_delta a2]_alpha<=Cdelta^(-alpha), and ||U||_infinity<=delta^alpha[U]_alpha. Hence [H1]_alpha<=Cdelta||U||_C^alpha and [H2]_alpha<=C||U||_C^alpha, giving the y estimate at each fixed x. The coefficients chi_delta rho_x and chi_delta rho_y have sup norm Cdelta^2 and alpha seminorm Cdelta^(2-alpha); the product rule gives the x estimate. These estimates also hold across the support boundary because the cutoff vanishes there. The sup estimate follows directly.

The indicator 1_Bdelta in the theory author statement cannot replace chi_delta. For example take rho=x^2y locally and h=x^2y times a smooth radial cutoff. Then c[h]>0, DU[h](0)=diag(-c[h],c[h]), and

    U[h] dot grad rho=-c[h]x^2y+o(r^3).

On every sufficiently small circle this is nonzero at an interior-quadrant point. Multiplication by the disk indicator creates a nonzero jump there, so no positive Holder seminorm is finite. This is an actual parity-compatible velocity counterexample, not merely an arbitrary vector field.

There is a useful whole-plane repair of the inverse claim. On E=C^alpha_1 define the parity-normalized velocity with U(0)=0. For bounded data, subtract the kernel's value at X=0 in the far integral. The resulting tail is absolutely integrable because its kernel is O(|X| |Y|^(-3)). On B1,

    ||U[h]||_(C^alpha(B1)) <= C_alpha ||h||_E.            (9)

To check(9), split h by a fixed radial cutoff equal1 on B2 and supported in B4. Its local C^alpha norm is bounded by C||h||_E, since |x|<=4. For the compact part, kernel cancellation and the split |Z|<=2d, |Z|>2d, d=|X-X'|, give the standard explicit integrals d^alpha/alpha and d^alpha/(1-alpha); the bounded far part has a Lipschitz difference kernel and is bounded by C||h||_infinity. Reflection gives U(0)=0. This proves(9) directly, without requiring a globally unrenormalized Riesz transform of arbitrary bounded data.

Thus Bdelta h=chi_delta U[h] dot grad rho is bounded E->E with norm C_alpha delta. If alpha<(1+A)/D, (2) and a Neumann series prove that

    T0+Bdelta : D(T0) -> E

is bijective for delta small enough that C_alpha delta max(1,kappa_1^(-1))<1. This is frozen transport with globally defined, localized coupling. It does not include c[h]G/3, replace T0 by the actual V, or specify a boundary realization on Bdelta. Those are separate problems. The bound(8) is the confirmed replacement for S(d); its literal indicator estimate and its unspecified local-domain inverse are not valid as stated.

## Axis-preserving changes of coordinates do not preserve this norm

For every p>alpha, there is a compact f in C^alpha_p and a smooth parity-preserving local diffeomorphism H, preserving both axes and satisfying H(X)=X+O(r^3), such that f composed with H is not locally C^alpha_p.

Choose r_n=4^(-n), w_n=r_n^(p/alpha)/100, a fixed even smooth bump phi with phi(0)=1 and support in[-1,1], and

    g(x)=sum_n r_n^p [phi((x-r_n)/w_n)+phi((x+r_n)/w_n)].

After discarding finitely many terms the supports are disjoint. Each bump has alpha seminorm bounded independently of n. Points in different supports have distance comparable to the larger center unless both belong to the same bump neighborhood; this proves the global alpha bound. Also |g(x)|<=C|x|^p. Let psi be smooth and odd, equal1 near some y0>0, and compactly supported away from0 in y. Then f(x,y)=g(x)psi(y) belongs to C^alpha_p.

On a small rectangle containing (0,y0), set

    H(x,y)=(x(1+epsilon y^2),y), epsilon>0.

This is a smooth local diffeomorphism, preserves the parity reflections and both axes, and differs from identity by a cubic term. Put x_n=r_n/(1+epsilon y0^2). Choose delta_n>0 such that H1(x_n,y0+delta_n)=r_n+2w_n. Then delta_n is comparable to w_n/r_n and tends to0. Both y points remain where psi=1. The composed values differ by r_n^p, while their weighted denominator is x_n^p delta_n^alpha. The quotient is comparable to

    (r_n/w_n)^alpha = C r_n^(alpha-p),

which diverges. A smooth cutoff can extend H to the identity outside a fixed rectangle without changing this argument. Therefore the norm-transfer assertion in Remark2.1 does not follow even from a smooth axis-preserving conjugacy. Whether the actual flow has a special conjugacy with additional mapping estimates remains open. No verdict on the quoted external linearization theorem is needed for this conclusion.

## Infinity and the strain functional

On the exterior region r>=R0>0, define the scaled Holder norm by the supremum of R^(-gamma)(||f||_infinity,A_R+R^alpha[f]_alpha,A_R), R>=R0. The forward-selected inverse of ell X dot grad-1 is bounded for gamma<k=1/ell, with bound1/(1-ell gamma) in this norm. This follows directly by dilating each annulus in the integral(1). The threshold is necessary for this forward formula: f=r^gamma Theta(theta), with a nonzero smooth parity-compatible Theta, makes the integral diverge on any ray with Theta!=0 when ell gamma>=1. This is not a claim about every possible exterior boundary realization.

The homogeneous tail r^k Theta belongs to this exterior norm iff gamma>=k. A nonzero residual leading term r^(2k-1)Epsilon(theta) belongs iff gamma>=2k-1. Thus the stated forward window is 2k-1<=gamma<k, conditional on the nonzero leading coefficient when necessity is claimed. Taking all R>0 rather than R>=R0 also imposes an independent origin condition; the two conventions cannot be interchanged.

For h in C^alpha_p, oddness gives |h(x,y)|<=[h]_(y,p)|x|^p|y|^alpha. Hence the absolute near-origin strain integral is bounded if p+alpha>1, by

    [h]_(y,p) R^(p+alpha-1)/(pi(p+alpha-1))
       times integral_0^(2pi)|sin(3theta)||cos(theta)|^p|sin(theta)|^alpha dtheta.

The Holder spaces alone do not give this conclusion for p+alpha<=1. For p+alpha<1, take a smooth parity-compatible annular bump H, away from both axes, with c[H]!=0, and h_epsilon=epsilon^(p+alpha)H(X/epsilon). Its C^alpha_p norm is uniformly bounded while c[h_epsilon]=epsilon^(p+alpha-1)c[H] diverges. At equality use a homogeneous degree1 angular function supported away from the axes, with the sign of sin(3theta), between an inner cutoff epsilon and a fixed outer cutoff. Its norms stay bounded and its strain grows like log(1/epsilon). These examples can be smooth for each epsilon and supported in a fixed compact set. A separate cubic weighted supremum condition, as proposed elsewhere by the theory author, removes this obstruction.

## Verdicts and remaining scope

H0, S(a), S(b), and S(c) are confirmed with the exact realizations and sharp endpoint proof above. S(d)'s indicator assertion is refuted; (8)-(9) and the specified whole-plane localized inverse are proved replacements. The coordinate-invariance step in Remark2.1 is refuted for the claimed class of maps. The source theorem with mu=1 is not by itself the actual modal source theorem, whose mu is slightly below1; that extension is a separate topic. In two dimensions the implication H^s_loc -> C^(1,alpha)_loc requires s>2+alpha, not merely s>2 for a fixed alpha. No global Holder inverse of the full IPM operator is proved here.
