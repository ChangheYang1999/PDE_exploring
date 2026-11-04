# Equilibrium arcs, degenerate surface limits, and flat vortex endpoints

Status: CONFIRMED in A628-A633, with the exact separate structural and regularity hypotheses below. Complete source and independent proof postreads.

## 1. Setting and exact scopes

The purely surface statements concern a C1 vector field on a C2 surface, with a positive C1 area density. They do not assume an Euler realization. All limit sets below are omega-limit sets of forward-complete nonstationary orbits precompact in that surface.

For the Euler applications let 2/5<c<1/2, omega be any real number, a=1-2c, kappa=1+c, A=cI-omega J, Jx=e3 cross x, and B=Ax+U. On a neighborhood of the orbit and its compact limit set assume a C2 velocity U and C1 pressure solve

    ((1-c)I+omega J)U+(B.grad)U+grad P=0,
    div U=0, U.Omega=0, Omega=curl U.

Set H=P+|U|^2/2+(Ax).U and g=U.B. The equation gives P,H in C2 and

    grad H=-aU+B cross Omega, BH=-ag,
    Omega.H=0, [B,Omega]=-kappa Omega, div B=3c.

Here Omega.H means Omega.grad H. The rank dH wedge dg=0 holds on Omega!=0 by A413. We use the following exact bounded W1 data, already derived in A540-A542 and A614-A616: a nonstationary B-orbit y(t) lies in Omega!=0 on H=H0, tends to a compact invariant K in a regular part of that level, and satisfies

    Omega(y(t))=alpha0 exp(-kappa t)B(y(t)), alpha0!=0.

On K, Omega=0, g=0, dg=-(rho/a)dH with constant rho<=-a, and grad H=-aU!=0. At its equilibria q, F=DB(q) has normal covector eigenvalue rho, F^T U(q)=rho U(q). The two level eigenvalues are lambda<=0<eta, with lambda+eta=d=3c-rho>0. For the jet and endpoint calculations below impose rho<-a, hence mu=d-kappa=-a-rho>0. The witness choice rho<=-2a in the main HF theorem satisfies this strict premise.

These are explicit structural hypotheses, not assertions that every profile has this particular bounded orbit. Their established W1 derivation uses the global sublinear helicity-free profile and the bounded vortex half-line. This note imposes no derivative decay at infinity, symmetry, pressure normalization, or restriction on omega.

## 2. Repelling equilibrium arcs

Let Y be C1 on a surface and vanish on a regular C1 arc. If the transverse eigenvalue is positive at an interior point, that point cannot be in the omega-limit set of a nonstationary orbit.

Work in an ordinary smooth chart in which the arc is y=f(s), f C1. Set r=y-f(s), retaining s. Although this coordinate change need not make the transformed field C1, the fundamental theorem of calculus in the ORIGINAL y variable gives

    s'=r A(s,r), r'=r C(s,r),
    A(s,r)=integral_0^1 partial_y Y1(s,f(s)+u r) du,
    C(s,r)=integral_0^1 [partial_y Y2-f'(s)partial_y Y1](s,f(s)+u r) du.

The coefficients are continuous. At r=0, C is precisely the transverse eigenvalue. On a small closed rectangle choose |A|<=M and C>=b>0. Every backward trajectory staying in it obeys

    |r(-t)|<=|r(0)|exp(-bt),
    |s(-t)-s(0)|<=M|r(0)|/b.

Choose an inner rectangle with half the s width and sufficiently small r width. These estimates exclude every backward boundary exit from the larger rectangle. Original C1 existence and uniqueness, and compact containment, extend that negative orbit for all time.

If a nonstationary orbit accumulated at the central arc point, fix an earlier orbit point, which is not an equilibrium. Choose the larger rectangle to omit it. A sufficiently late visit to the inner rectangle forces the earlier point into the larger rectangle by uniqueness, a contradiction.

For the Euler setting, on a regular neighborhood set N=grad H/|grad H|^2, f=BH and X=B-fN. Then XH=0, X=B on K and on the orbit, and for nu=(i_N volume)|_{H=H0},

    div_nu X=3c-Nf-f div N=d on K.

The formula follows in local coordinates with H as the first coordinate. At an equilibrium DX restricted to the level equals F restricted to U(q)^perp because df=rho dH there. A regular C1 arc of equilibria in K has a zero tangent eigenvalue and transverse eigenvalue d>0. The lemma excludes each interior point. Any nonconstant C1 parameterized curve has a point with nonzero derivative and hence a regular subarc. Thus K cap {B=0} contains no nonconstant C1 curve of equilibria, without a nonflatness assumption. This statement is for the level orbit; an ambient orbit may approach the arc in the negative normal direction.

## 3. Finite isolated semihyperbolic equilibria in an expanding surface set

Let Lambda be a compact invariant set for a C1 surface field X. Suppose a positive C1 density has div_nu X>=gamma>0 on a neighborhood of Lambda. Assume its equilibria are finite and each is either a hyperbolic saddle or an isolated surface zero with eigenvalues 0 and eta>0. Isolation is in the surface neighborhood, not only relative to Lambda. Every external precompact nonstationary orbit with omega-limit contained in Lambda converges to one equilibrium.

The hyperbolic local blocks and global finite-section argument were proved in A614. Here is the additional local argument needed for the zero eigenvalue. A local C1 center curve and transverse strong unstable curve exist. Flatten the center curve by a graph map. The transverse equation is r'=r C(s,r), C>=b>0. Straighten the strong unstable curve by s to s-h(r), retaining r; the center curve remains r=0. Uniqueness and the sign of r' are preserved, even though one uses only the continuous transformed coefficients. The invariant strong unstable axis separates the two center sides.

Because the equilibrium is isolated, the scalar field on each punctured center side has a fixed nonzero sign. Choose small side boundaries incoming on attracting center sides and outgoing on repelling center sides, and upper and lower outgoing boundaries. On each attracting side there is one incoming center crossing. An off-center point near it cannot cross the unstable axis or exit through an incoming side. It exits forward through the upper or lower boundary. Its passage time tends to infinity as its incoming transverse coordinate tends to zero, since C is bounded above. On each punctured half incoming interval the original C1 flow gives a strictly monotone C1 passage map to the corresponding outgoing half arc, so it has a unique endpoint limit. The outer endpoint at the incoming corner maps to the same outgoing corner; strict monotonicity and the separating unstable axis keep the other limit away from both block corners. Restriction to a shorter incoming interval preserves that property. The inverse passage extends continuously by sending its singular image endpoint to the incoming center crossing. Only the equilibrium can have a complete orbit in this block: off-center points exit forward, and nonzero center points exit in one time direction.

These are precisely the local properties used in A614. For clarity, the rest of that argument is as follows. Area expansion and invariance imply nu(Lambda)=0. Flow boxes then show zero one-dimensional measure of its intersections with transversals. Choose the preceding finitely many blocks and finitely many flow boxes for the remaining regular part, with a finite disjoint union T of compact transverse arcs and endpoints outside Lambda. Zero transverse measure allows the corner and intersection gaps to miss Lambda. All regular Lambda orbits meet these sections in at least one time direction. Write Q=Lambda cap T. There are only finitely many incoming stable-center or stable-saddle crossings C whose next return takes infinite time. Regular branches cover the compact remainder of Q; the local singular branches cover punctured neighborhoods of C. Thus a finite collection of return branches suffices near Q.

In the flux coordinate i_X nu, every finite return of time tau has |P'|=exp integral_0^tau div_nu X >=exp(gamma tau). Compact disjoint sections have a common positive minimum return time h. Their inverse extensions are therefore exp(-gamma h)-Lipschitz and send Q intersect closure(image) into Q, including the singular endpoints. Embed the sections as disjoint intervals with positive gaps. Choose epsilon below the gaps and below every positive distance to Q of a branch image endpoint. If z in an image is within epsilon of Q, a nearest point of Q belongs to that closed image: any intervening endpoint either belongs to Q and is closer, or contradicts the epsilon choice. Hence

    dist(P^(-1)z,Q)<=exp(-gamma h)dist(z,Q).

An external orbit accumulating at a regular point has infinitely many late intersections with positive distances delta_n to Q tending to zero. The displayed inequality instead forces delta_(n+1)>=exp(gamma h)delta_n. This is impossible. The omega-limit consists of finitely many equilibria and is connected, hence is a singleton.

The invariant-measure variant A615 is unchanged: if every invariant probability is supported on the finite equilibria and each trace is positive, a C1 change of density gives uniform positive divergence. For Euler, use the surface field X of Section2 and its positive divergence near K. Isolation of ambient B-zeros alone does not imply isolation of X-zeros without further information.

## 4. Hyperbolic endpoints, including flat endpoints

In the Euler setting assume y(t) actually converges to q, with lambda<0<eta. Then lambda>=-kappa. No density of Omega!=0 near q is assumed.

Write the level locally as a C2 graph over its tangent plane. The two linear tangential coordinate components of B restricted to that graph form a C2 planar field Y. It agrees with B wherever B is level tangent, in particular on the given orbit. It has a C2 stable and unstable curve with eigenvalues lambda,eta. Straightening these curves gives

    s'=s(lambda+r1), z'=z(eta+r2), r1,r2 ->0.

The straightening is C2; estimates need only continuity of the displayed coefficients. Omega is tangent to every nearby H level and divergence free. Therefore i_Omega nu is a closed C1 one-form on the entire small level disk. Let dpsi=i_Omega nu and psi(q)=0; psi is C2.

Let D be the connected component of the nonzero-vorticity part of this disk containing the stable orbit branch. The ambient rank identity locally gives g=G(H) near each point of D. Its value and the coefficient G'(H0) are locally constant along D, thus constant on D. Along the given orbit g=0; continuity of dg at q gives G'(H0)=-rho/a. Hence on D, B is tangent, Y=B, div_nu Y=d. Cartan's identity and [B,Omega]=-kappa Omega give d(Ypsi-mu psi)=0. Since psi is constant and zero on the stable orbit, the integration constant is zero. Thus

    Ypsi=mu psi on D and its closure.

Fix (s0,0) on the orbit. Nearby (s0,z0), z0>0, are in D. Their trajectories remain in D until exiting a small rectangle through z=delta: finite-time B transport preserves nonzero vorticity. As z0->0, exit times T tend to infinity and exit points tend to u*=(0,delta). Passing to limits for each fixed backward time shows that the entire backward unstable segment from u* to q belongs to closure D and is a B-orbit.

The eigenvalue eta is the largest real ambient eigenvalue, since rho<0 and lambda<0. An adapted norm, followed by shrinking the neighborhood, gives for arbitrary small epsilon>0

    |Phi_(-T)u*-q|<=C exp(-(eta-epsilon)T),
    |D Phi_T(Phi_(-T)u*)|<=C exp((eta+epsilon)T).

The Cauchy law, Omega(q)=0 and local Lipschitz continuity of Omega imply |Omega(u*)|<=C exp((-kappa+2epsilon)T). Thus Omega(u*)=0, dpsi(u*)=0, and the extended transport equation with mu>0 gives psi(u*)=0.

If lambda<-kappa, choose epsilon with lambda+kappa+3epsilon<0. The passage estimates give |s(T)|<=|s0|exp((lambda+epsilon)T) and z0>=delta exp(-(eta+epsilon)T). Taylor's theorem at u* and transport then yield

    |psi(s0,z0)|/z0
      =exp(-mu T)|psi(s(T),delta)|/z0
      <=C exp((lambda+kappa+3epsilon)T) ->0.

So partial_z psi(s0,0)=0. The tangential derivative is already zero along the stable branch. This contradicts its nonzero vorticity and proves lambda>=-kappa.

Use the original linear tangential coordinate as parameter on the C2 stable graph. Its scalar equation is s'=lambda s+O(s^2), which implies |s(t)| comparable to exp(lambda t), with a nonzero limiting amplitude. Therefore

    |Omega(y(t))| comparable to |y(t)-q|^(1-kappa/lambda).

The exponent is at least two. If U is smooth, the stable graph and restriction of Omega are smooth; Taylor expansion through an integer above this finite exponent forces that exponent to be an integer m>=2. At a nonflat endpoint, the previously audited spectral identity lambda=rho+kappa gives rho=-m kappa/(m-1). The integer is the order along the stable curve, not necessarily the first nonzero ambient jet order.

## 5. An exceptional-rate convergent endpoint must be flat

Assume y(t)->q, rho=-kappa, and the level eigenvalues are 0,d>0. Then D Omega(q)=0.

Suppose the derivative were nonzero. Some first component derivative of Omega remains nonzero in a ball, so Omega cannot vanish on any open subball. Its nonzero set is dense there. The rank identity consequently extends everywhere, and g=G(H) on a small submersion box. In coordinates h=H-H(q), B^h=b(h), b'(0)=-kappa, and Omega^h=0. The tangential components on h=0 are a C2 planar field. A local C2 center-stable curve contains the converging orbit; flatten it by a C2 change retaining h. Along the orbit (0,s(t),0),

    B=(0,f(s),0), f(0)=f'(0)=0, f(s(t))!=0,
    F(t)=[[-kappa,0,0],[v1,f',a1],[v2,0,g1]], g1->d>0.

All coefficients are bounded. Put alpha=alpha0 exp(-kappa t) and C=D Omega-alpha DB, initially in ambient coordinates. Differentiating the exact Cauchy flow identity and the push-forward identity for B gives

    C(t)=exp(-kappa t)D Phi_t C(0)(D Phi_t)^(-1),
    C'=[F,C]-kappa C.

This needs only B C2 and Omega C1. Under the C2 coordinate change, the second derivative coordinate terms in D Omega-alpha DB cancel because Omega=alpha B along the orbit. Thus C is a tensor there, and its evolution remains valid in the flattened coordinates without a third coordinate derivative.

The first row of C is (kappa alpha,0,0). Differentiating Omega=alpha B in time gives CB=-kappa alpha B. Since f!=0, write

    C=[[kappa alpha,0,0],[p,-kappa alpha,r],[q1,0,w]].

The exact commutator equation is

    w'=-kappa w,
    r'=(f'-g1-kappa)r+a1(w+kappa alpha),
    q1'=g1 q1+(kappa alpha-w)v2,
    p'=f'p+2kappa alpha v1+a1 q1-r v2.

Continuity bounds every entry. First w=O(exp(-kappa t)); the uniformly extra damping g1-f'>d/2 eventually gives the same estimate for r. Boundedness selects the terminal-value solution of the unstable q1 equation,

    q1(t)=-integral_t^infty exp(-integral_t^u g1)(kappa alpha(u)-w(u))v2(u) du,

so q1=O(exp(-kappa t)). Finally p'=f'p+O(exp(-kappa t)). Since (log|f(s(t))|)'=f'(s(t))->0, the reciprocal of |f(s(t))| grows at most subexponentially. Variation of constants therefore gives

    p(t)=f(s(t))[p(t0)/f(s(t0))
          +integral_t0^t O(exp(-kappa u))/f(s(u)) du] ->0.

The integral converges and f(s(t))->0. All entries of C tend to zero, and D Omega=C+alpha F tends to zero, contradicting D Omega(q)!=0. This proves the statement.

Combined with Section3: at rho=-kappa, a bounded W1 configuration with finitely many equilibria, all nonflat and isolated as surface zeros, is impossible. Finiteness and surface isolation have not been derived in general.

## 6. Finite vorticity jets and resonance

At an equilibrium q in the Euler setting write u=U(q)!=0. Assume Omega is C^m in a neighborhood, all derivatives of orders below m vanish at q, and its order-m derivative is nonzero. In particular m>=2 at a first-order-flat point. These extra derivatives are not supplied by U C2.

The leading homogeneous vector polynomial Omega_m satisfies

    Omega_m(exp(tF)x)=exp(-kappa t)exp(tF)Omega_m(x),
    u.Omega_m=0, div Omega_m=0.

One can obtain the first identity by inserting the leading Taylor polynomial into the Cauchy formula and using Phi_t(q+x)=q+exp(tF)x+o(|x|), without presuming higher derivatives of the flow. The helicity and divergence identities give the remaining two equations.

Choose linear coordinates (x,s,z) with x the normal covector u and plane eigenvalues lambda,eta. In diagonal coordinates the divergence-free polynomial has form Omega_m=(0,partial_z Psi,-partial_s Psi), with Psi of degree m+1, defined modulo x^(m+1). Its equation is

    (rho x partial_x+lambda s partial_s+eta z partial_z)Psi=mu Psi.

The x-only gauge can be removed since (m+1)rho!=mu. Thus some monomial x^i s^j z^k satisfies

    i+j+k=m+1, k>=1, i rho+j lambda+k eta=mu.

If F has a Jordan block, triangularization on the invariant plane and the quotient polynomial space gives the same diagonal weights, so this remains a necessary resonance. Positivity of mu and nonpositivity of rho,lambda imply k>=1.

For m=2 the three monomials with k>=2 have positive weight-minus-mu: 3c-2lambda+kappa, eta+kappa, and 2eta-lambda+kappa. The remaining monomials x^2z,xsz,s^2z respectively give lambda=2rho+kappa, rho=-kappa, lambda=-kappa. Consequently lambda=0 forces rho=-kappa/2 or -kappa. The leading polynomials (0,x^2,0) and (0,xs,-xz) realize the corresponding linearized identities only; they are not Euler germs.

For general m and lambda=0, put n=i-k+1. The resonance becomes

    rho=-(kappa+3c(k-1))/n,
    n>=1, k>=1, n+2k<=m+2.

The numerator is positive and rho<0, so n>=1; the degree bound follows by eliminating i. If every flat equilibrium has a finite nonzero jet and rho avoids the union of these exceptional sets (also including m=1), all equilibria are hyperbolic. Compactness then makes their set finite and Section3 applies. This is a conditional statement, not unique continuation at infinitely flat points.

A nonzero finite jet with the stated neighborhood regularity implies local vorticity density: its particular nonzero component derivative stays nonzero in a ball, excluding any open zero region. This fact has no analogue from mere first-order flatness.

## 7. Local algebra does not exclude an equilibrium curve

At an irrotational equilibrium, M=DU is symmetric and trace free, F=A+M. Put L=(1-c)I+omega J. Differentiating the profile equation gives

    grad P=-Lu, Q=D2P=-LM-MF=-M-M^2+omega[M,J].

If Fv=0, then Mv=-Av and Qv=LAv. Hence v.Qv=c(1-c)|v|^2+omega^2|Jv|^2>0. This is compatible with a curved equilibrium arc, since neither its pressure gradient nor its acceleration vanishes in general.

For completeness, along a regular C1 equilibrium curve gamma with v=gamma', u=-A gamma and Fv=0, so u'=Mv=-Av and u.v=0 from F^T u=rho u. If T=D2U and Nv=T(v,.), differentiating along the curve gives Nv symmetric and trace free and

    Nv^T u+F^T Mv=rho Mv.

No acceleration is used. If gamma is C2 with w=gamma'', then additionally Fw+T(v,v)=0 and (A gamma).w=-c|v|^2. Differentiating the profile equation once more at the equilibrium is legitimate even with only U C2: in D(grad P)=-L DU-D2U[B,.]-DU DB the potentially rough term has derivative T(Fv,.) because B(q)=0 and D2U is continuous. Thus

    D2(grad P)(q)[v,w]=-(L+M)T(v,w)-T(v,Fw)-T(w,Fv).

Let K1=D Omega(q). The first jet satisfies [F,K1]=kappa K1, u^T K1=0, tr K1=0, and along the curve K1 v=0. If Omega is C2 near q, put W2=D2 Omega(q). Differentiating the bracket, helicity and divergence identities gives

    F W2(v,w)-W2(v,Fw)-W2(w,Fv)
      =kappa W2(v,w)+K1 T(v,w)-T(v,K1 w)-T(w,K1 v),
    u.W2(v,w)+(Mv).K1 w+(Mw).K1 v=0.

Along a C2 curve also W2(v,v)+K1 w=0. Along a C1 curve with this extra vorticity regularity, differentiation of the first-jet equation gives [Nv,K1]+[F,W2(v,.)]=kappa W2(v,.). These are exact identities with the regularity just stated; no second curve derivative or second vorticity derivative is inferred from the original C1-curve/C2-velocity premises.

An exact local example for omega=0 uses cylindrical radius r>0, R>0 and rho<0:

    phi=(rho/4-c/2)(r^2-2z^2)-(rho R^2/2)log r,
    U=grad phi, P=-a phi-|grad phi|^2/2-cx.grad phi.

The potential is harmonic, and direct differentiation gives the full local profile equation. The carrier satisfies B_r=(rho/2)(r-R^2/r), B_z=(3c-rho)z, B_theta=0. The circle r=R,z=0 consists of equilibria with eigenvalues rho,0,3c-rho. It is singular on the axis, not globally sublinear, and has no adjacent nonzero vorticity. It therefore does not contradict Section2 or the global conjecture.

At a first-order-flat point, T=D2U is a fully symmetric trace-free cubic tensor. If local rank gives g=G(H), differentiating twice yields

    T_u+MF+F^TM=rho M+zeta u tensor u,
    zeta=a^2 G''(H(q)), zeta |u|^2=2 tr(M^2).

This is a compatibility equation, not a further spectral obstruction by itself. Indeed contraction of a symmetric trace-free cubic tensor with a fixed nonzero u maps onto all symmetric trace-free matrices. In coordinates u=e1, prescribe T_1ij as the desired matrix. Its trace supplies the first cubic trace equation, and choose T_222,T_233 and T_223,T_333 to satisfy the other two. The trace equation above makes the required right side trace free.

## 8. An infinitely flat reduced model and remaining gaps

Choose d>kappa>0 and, near (s,z)=(0,0), set

    Y=-s^2 partial_s+(d+2s)z partial_z,
    F0(s)=s^2 exp(-kappa/s) for s>0, and 0 for s<=0,
    psi=-F0(s)z, Omega_Sigma=(-F0(s),F0'(s)z).

These are smooth. The identity s^2 F0'=(kappa+2s)F0 gives

    div Y=d, div Omega_Sigma=0,
    Ypsi=(d-kappa)psi, [Y,Omega_Sigma]=-kappa Omega_Sigma.

The origin is an isolated equilibrium with eigenvalues 0,d. On z=0,s>0, s(t)=s0/(1+s0 t), Y=exp(kappa/s)Omega_Sigma, and tau=exp(kappa/s)/kappa obeys tau'=kappa tau. Thus a nonzero incoming vorticity field can converge to an infinitely flat degenerate endpoint while satisfying these reduced area and transport equations. This is a two-dimensional model, not a three-dimensional Euler velocity with its actual curl.

Still open: arbitrary infinite equilibrium sets with no regular arcs; isolation or finite-order nonvanishing of degenerate points; and exclusion of allowed flat or hyperbolic endpoint connections using the full global profile equations. None of the local models is a global counterexample.

Sources: Theory Agent B in the team records Section4h and in the team records, in the team records, verify_identities.py (accompanying artifacts) were read. The 19 source symbolic checks were inspected but not rerun; all conclusions above have independent analytic derivations. Inner model consultation failed before any response, so it is not counted. Existing configured-model agent exchange continues and focused comparison is requested separately. No computation was needed in this audit.
