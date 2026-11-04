# A zero of U dot B on a regular vortical level has multiplier at least one

Status: CONFIRMED in A521-A523 after complete source read, independent reconstruction, full postread and comparison with the existing configured-model coordinator check. The core statement and selected corollaries are separated from the additional source local spectral table.

## 1. Exact hypotheses and conclusions

Fix 0<c<1/2, any finite real omega, a=1-2c>0, kappa=1+c, J(x1,x2,x3)=(-x2,x1,0), and A=cI-omega J. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U(x)=o(|x|) uniformly, U.curl U=0 everywhere.             (1)

Set B=Ax+U, W=curl U, H=P+|U|^2/2+(Ax).U, g=U.B and

    beta=U^flat+dH/a=(B cross W)^flat/a.

The exact identities and confirmed A413,A478,A496 imply the theorem below. No derivative bound or velocity decay is assumed beyond uniform sublinearity; the source uses bounded U, and Section2 checks the stated extension explicitly.

At every point x with W(x)!=0, dH(x)!=0 and g(x)=0, define

    lambda(x)=grad g(x).grad H(x)/|grad H(x)|^2.

Then lambda(x)>=1.

Two consequences hold at a nonzero irrotational equilibrium p in closure{W!=0}, with u=U(p), F=DB(p), K=DW(p)!=0 and F^T u=rho u:

1. The A469 second family

       spec F={rho,(-a-rho)/2,(1+4c-rho)/2}

   is impossible whenever rho>0. This includes all its positive bad range rho>=3a.
2. In the A469 first family spec F={rho,rho+kappa,-a-2rho}, if rho>0, a sufficiently small neighborhood in regular H coordinates satisfies

       {W=0}={g=0}={H=H(p)}, {W!=0}={H!=H(p)}.

   This describes a separating irrotational level; it does not exclude that family.

A periodic corollary is stated separately in Section8. No claim is made here about every row of the source's invariant-manifold table, about negative equilibrium ranges, or about K=0 equilibria.

## 2. Completeness, regularity and level identities

Uniform sublinearity gives, outside a sufficiently large ball,

    B(x).x/|x| >= (c/2)|x|,
    |B(x)| <= C(1+|x|).

Thus the B-flow Phi_t is complete in both directions and every negative semiorbit stays in a compact ball. The first inequality prevents inward-time escape through the containing sphere; the second excludes finite-time escape. A048 gives the complete W-flow Gamma_s. These facts replace the source's bounded-U estimates and require no additional decay.

The equation makes grad P C1, so H and g are C2. The exact identities are

    grad H=-aU+B cross W, BH=-ag, WH=Wg=0,
    [B,W]=-kappa W,
    beta(B)=beta(W)=0, Phi_t^*beta=exp(-at)beta.               (2)

On the regular vortical set, A413 gives dg=lambda dH, with lambda C1. Differentiating gives d lambda wedge dH=0. Therefore g and lambda are constant on each connected regular vortical H-level component. On the component Sigma through a point with g=0, write its constant multiplier as lambda0. Then

    g=0, dg=lambda0 dH, BH=0,
    Phi_t^*dH=exp(-a lambda0 t)dH                           (3)

along its orbits.

For clarity, Sigma is invariant under every finite B-time. Initially its orbit is vortical by Cauchy transport. The equations for g and the covector dH give g=0 and nonvanishing dH while the orbit is in Sigma. Since lambda=lambda0 there, the finite-time covector law in(3) precludes loss of regularity at a finite endpoint. Continuity and connectedness extend the orbit in the same component. This is not a claim that an arbitrary complete H-level is invariant.

Helicity zero also gives the vector identity

    grad H cross beta^sharp=gW.                             (4)

Hence on Sigma, beta=k dH for a C1 scalar k, and Lie differentiation using(2)-(3) gives

    Bk=a(lambda0-1)k.                                      (5)

## 3. The parallel case reaches an actual vortical equilibrium

Suppose x in Sigma has beta(x)=0. If B(x)=0, A496 already gives lambda0>=1: the equilibrium relation is DB(x)^T U(x)=-a lambda0 U(x), and its rho is at most -a.

Otherwise beta=0 along the complete B-orbit by(2). It also propagates along its W-line: d beta=d(U^flat), beta(W)=0 and contraction of d(U^flat) with W=curl U vanishes, so L_W beta=0. Write B=fW on the line. W never vanishes at finite W-time. The bracket gives Wf=kappa, and consequently

    f(Phi_t x)=exp(kappa t)f(x),
    Phi_t x=Gamma_(f(x)(exp(kappa t)-1)/kappa) x.             (6)

As t tends to minus infinity the W-time approaches the finite number -f(x)/kappa. Completeness of W, or just its compact confinement along this segment, gives an endpoint x_*. A finite-time W-flow cannot send a nonzero field value to zero. Formula(6) yields B(x_*)=0 and W(x_*)!=0.

The identity WH=0 makes the W-flow preserve dH, so dH(x_*)!=0. The relation W lambda=0 holds on the regular vortical set by Section2. Thus lambda(x_*)=lambda0. At this actual vortical equilibrium, grad g=DB(x_*)^T U(x_*)=-a lambda0 U(x_*), and A496 implies lambda0>=1. This proves the theorem in the parallel case.

## 4. A transverse contraction lemma with a full crossing proof

Here is the local geometric fact used for the other case. Let L be a compact full B-invariant set. In a neighborhood of L suppose B,W are independent C1 fields, beta is a nonzero C1 one-form annihilating them, and

    Phi_t^*beta=exp(-at)beta, [B,W]=-kappa W,
    a>0, kappa>0.

Let C be closed, invariant under the full B-flow, and contain every sufficiently small surface generated by B and W through points of L. If dist(Phi_(-t)x,L)->0, then x belongs to C. Neither compactness of C nor invariance of a globally bounded W-saturation is required.

Choose nested neighborhoods N0 and N of L with closure N0 inside N and compact closure N on which the frame (B,W,Z) exists, where Z=beta^sharp/|beta|^2. In that frame a variational vector v=bB+wW+rZ satisfies exactly

    b'=f r, w'=kappa w+h r, r'=-a r.                        (7)

The first two columns follow from flow transport of B and the bracket of B,W. The last scalar equation follows by applying beta to v and differentiating its conformal transport. Thus f,h are continuous and bounded on closure N; no derivative of a merely continuous coefficient is taken.

Let |f|<=F0, |h|<=H0 and M>max(F0/a,H0/(a+kappa),1). The cone |b|,|w|<=M|r| is invariant backward while the base orbit remains in N. Indeed for backward duration t>=0,

    |b(-t)|<=|b(0)|+(F0/a)(exp(at)-1)|r(0)|,
    |w(-t)|<=exp(-kappa t)|w(0)|
              +(H0/(a+kappa))(exp(at)-exp(-kappa t))|r(0)|,
    r(-t)=exp(at)r(0).                                      (8)

These inequalities preserve the cone, and frame bounds imply |v|<=C0|beta(v)| inside it.

The two fields generate local C1 surfaces because their bracket stays in their span. Explicitly, compose their local flows with a transverse curve; the bracket law preserves the span under these flows, and the inverse function theorem supplies local coordinates whose last coordinate s is constant on each surface. In each such chart beta=b0 ds with b0 continuous, nonzero and bounded above and below. Compactness of L gives finitely many charts with uniform smaller sizes. In particular nearby points to L and curves of sufficiently short Euclidean length around them lie in one such chart containing a nearby point of L.

Assume x is outside C. After a fixed backward time, the entire negative semiorbit of x lies in N0. This shift preserves membership in C. Take a short Z-curve through x, parameterized so that each half has integral |beta| equal to epsilon. Since C is closed and x is outside it, choose epsilon so that the whole curve misses C. Its negative images also miss C.

Choose a fixed small delta>0 and put T_epsilon=log(delta/epsilon)/a. Up to this time, the tangent vectors to the pulled-back curve stay in the cone by(8), and each half has transverse length epsilon exp(at)<=delta by conformal transport. Hence each half has Euclidean length at most C0 delta. Choose delta smaller than the margin from N0 to the boundary of N divided by 2C0. A first-exit continuation argument then proves that the entire pulled-back curve remains inside N for every time up to T_epsilon. This verifies the neighborhood premise needed for the cone calculation; it is not assumed for arbitrarily long curves.

At time T_epsilon, both halves have transverse length exactly delta, while their center tends to L as epsilon tends to zero. In a uniform foliation chart containing the curve and a nearby z_epsilon in L, beta=b0 ds. Its tangent has a nonzero r component of fixed sign, so s is strictly monotone along the curve. Each half changes s by at least delta/sup|b0|. The s coordinates of its center and z_epsilon tend together. The curve must therefore cross the local surface s=s(z_epsilon), which belongs to C. This contradicts its disjointness from C and proves the lemma.

## 5. The nonparallel case and the critical saturation

Return to Sigma, and suppose beta(x)!=0 but lambda0<1. Formula(5) makes |k(Phi_t x)| grow without bound as t tends to minus infinity. Beta is bounded on the compact containing ball of this negative semiorbit. Therefore dH=beta/k tends to zero there, and so does dg=lambda0 dH.

Its alpha-limit set L is nonempty, compact, full B-invariant and lies in

    Crit H intersect Crit g intersect closure{W!=0}.        (9)

Beta never vanishes on L. If beta(z)=0 at z in L, transport makes it zero on its full B-orbit. On L, dH=0, so beta=U^flat and U=0 on that orbit. It must solve y'=Ay, and compactness then forces z=0. At that origin U(0)=0, whereas 0 lies in the vortical closure. This contradicts A478's irrotational-neighborhood theorem. Thus beta is bounded away from zero on L, and

    B cross W=aU=a beta^sharp!=0 on L.

In particular B,W are independent on L and throughout a sufficiently small neighborhood.

Let C be the closure of the complete W-saturation of L. The identities WH=Wg=0 preserve their differentials under finite W-times, so C remains in Crit H intersect Crit g. The bracket conjugacy and full B-invariance of L give full B-invariance of C. By construction it contains the small B,W surfaces through every point of L. Section4 therefore implies x in C, contradicting dH(x)!=0. This excludes lambda0<1 and proves the core theorem.

The critical saturation may be unbounded. The crossing proof uses its closedness, local surfaces and B-invariance, not compactness of the saturation. All compactness arguments concern L or one negative B-orbit.

## 6. Exclusion of the second positive spectral family

Let p satisfy Section1's irrotational equilibrium assumptions with K!=0 and rho>0 in the second family. Put s=(-a-rho)/2<0 and t=s+kappa=(1+4c-rho)/2. The resonance relations K^T u=0 and FK-KF=kappa K imply that K maps the s eigendirection nontrivially into the t generalized eigenspace inside u^perp. It has no other allowed nonzero source direction: potential arrows ending in the transverse rho direction are forbidden by K^T u=0, and the exceptional equality rho=t does not alter the simple s source direction. Thus K has rank one and Kv!=0 for an s eigenvector v.

The s exponent is strictly the most negative one. The local strong stable curve tangent to v exists for the C2 field B, even if the other exponent t is zero or positive or negative. A parameterization gamma(r)=p+rv+o(r) gives W(gamma(r))=rKv+o(r), so its nearby punctured branch is vortical.

Choose x on that branch sufficiently close to p. Its forward orbit stays in a regular H neighborhood and tends to p. The scalar equation g'=-a lambda g has coefficient tending to rho>0, while g tends to g(p)=0. Its only such solution is g=0 along the orbit. Then H is constant and lambda is constant by Section2, with value -rho/a<1. Section5 forbids this. Hence the second family with rho>0 is impossible. This argument does not assume density of the vortical set, or convergence to an equilibrium for arbitrary trajectories.

## 7. Exact local zero set in the first positive family

For the first family and rho>0, resonance gives rank K=1, K|_(u^perp)=0 and a nonzero transverse derivative into the rho+kappa eigendirection. Here rho is simple and all three eigenvalues are distinct. Also grad g(p)=rho u!=0 and lambda(p)=-rho/a<1. Shrink to a regular neighborhood on which lambda<1. The core theorem makes W vanish at every point of {g=0} there.

Choose a fixed scalar component ell W with nonzero derivative at p. Since its derivative is proportional to dg(p), use g as a local coordinate and divide:

    ell W=g theta,
    theta(g,z)=integral_0^1 partial_g(ell W)(sg,z)ds.

Theta is continuous and theta(p)!=0. After shrinking, ell W vanishes exactly where g=0. Thus W=0 if and only if g=0.

There is also a direct density check needed for the H statement. Since d(ell W) is nonzero throughout a small neighborhood, its zero set is a regular hypersurface; {W=0} is contained in it. Hence the vortical set is dense. The continuous A413 rank identity extends to this whole neighborhood. In regular H coordinates this gives g=G(H), with G(H(p))=0 and G'(H(p))=-rho/a!=0. On a sufficiently small coordinate box, G has only this one zero. Therefore {W=0}={g=0}={H=H(p)} and its two local sides are vortical. This is a description, not nonexistence.

## 8. Periodic consequence, with its extra premises stated

Let Gamma be a nonconstant periodic B-orbit in closure{W!=0} with W=DW=0 and a nonzero U-covector transported at rate rho. The confirmed periodic identities give g=0, dH=-aU!=0 and lambda=-rho/a on Gamma. Assume rho>3c, in particular the coordinator's stated range rho>=2-c since c<1/2. The Floquet exponents are 0,rho,3c-rho, so there is one stable transverse direction and one unstable transverse direction.

If a point x of the local stable cylinder were vortical, its forward orbit would remain vortical and approach Gamma. Take the cylinder small enough that dH!=0 and lambda<1 near Gamma; this is possible because lambda tends to -rho/a<0 on Gamma. The equation g'=-a lambda g has coefficient tending uniformly to rho>0 along this orbit, while g tends to zero. It forces g=0. The core theorem then contradicts lambda<1 at x. Thus W=0 on the local stable cylinder.

A474 separately gives W=0 on the local unstable cylinder at rho>3c. Combining the two conclusions gives irrotationality of both cylinders. This does not give an irrotational neighborhood of Gamma or exclude a periodic witness: nearby vortical points away from those cylinders remain possible. Any regular vortical H-level component incident to Gamma with g=0 and constant multiplier -rho/a is also excluded directly. Incidence and g=0 must be established for the particular component; they are not inferred for every nearby component.

## 9. Audit boundaries and comparison record

The complete 349-line source manuscript and the coordinator's actual configured-model check were read. Its inner second-model attempt failed, and is not counted as a consultation. The coordinator's written rederivation supplies the existing model exchange. The only scope extension made here is replacing bounded U by uniform sublinearity, for which every needed completeness and trapping statement is explicitly proved or cited in Section2. No new computation was run or needed.

The core zero-g theorem uses A413, A478 and A496 and the exact equations. A469 supplies the spectral families and resonance for Sections6-7; A474 and the periodic covector identities are separate inputs for Section8. No new conclusion is claimed for negative rho, K=0, arbitrary helicity, or bare-decay nonexistence. The additional source jet construction and full manifold table are not included in this verdict. All finite omega are allowed; constants and neighborhoods may depend on omega.
