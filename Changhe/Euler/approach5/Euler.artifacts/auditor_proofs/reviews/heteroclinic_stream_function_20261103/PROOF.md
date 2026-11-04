# A stream-function obstruction at a nonflat irrotational endpoint

Status: CONFIRMED as A543-A544 after full independent postread and source comparison. A545 corrects the printed monotonicity; A546 rejects the separate jet-compatibility claim in the global rank class. No computation was run.

## 1. Exact statement

Let 0<c<1/2, omega be any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, a=1-2c and kappa=1+c. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U=o(|x|) uniformly, U.curl U=0 everywhere.

Write B=Ax+U, W=curl U, H=P+|U|²/2+(Ax).U, g=U.B. Let q be an irrotational carrier equilibrium in the closure of {W!=0}, with

    B(q)=W(q)=0, u=U(q)!=0, DW(q)!=0,
    DB(q)^T u=rho u,
    spec DB(q)={rho,lambda,eta},
    lambda=rho+kappa<0<eta=-a-2rho, rho<-kappa.          (1)

These are the A541 first-family data when a bounded equilibrium vortex half-line has a hyperbolic nonflat endpoint q. The local conclusions below can also use (1) as explicit hypotheses, with the rank identity dH wedge dg=0 near q in place of its global A413 source.

Put mu=-a-rho>0. On a sufficiently small simply connected patch of the regular surface Sigma={H=H(q)} through q there is a C2 function psi, normalized by psi(q)=0, such that

    d psi=i_W nu, B psi=mu psi,                         (2)

where nu is the area form defined by the ambient oriented volume and the transverse coordinate h=H-H(q). Both B and W are tangent to Sigma, and W=0 exactly where d psi=0. The local unstable curve of B on Sigma is irrotational. The function psi is zero on both the stable and unstable curves.

If rho<-2kappa, the local stable curve on Sigma is also irrotational. Consequently a vortical W-line which is a B-orbit and converges to this q must satisfy

    -2(1+c)<=rho<-(1+c).                                (3)

For sigma=rho/(rho+kappa), this interval is equivalent to sigma>=2. The function sigma is strictly increasing as rho increases in this interval, with sigma=2 at rho=-2kappa and sigma tending to infinity as rho approaches -kappa from below.

This is a local necessary condition for a specified nonflat hyperbolic endpoint. It excludes neither endpoints with DW=0 nor general bounded limit sets. No velocity decay or derivative bound at infinity is assumed.

## 2. The regular invariant surface and its differentiability

The profile equation gives grad P in C1, hence P,H,g in C2. At q, the Lamb identity gives grad H(q)=-au!=0. Because one derivative of one component of W is nonzero at q, that derivative stays nonzero near q. The zero set of that component is a C1 hypersurface, and {W=0} is contained in it. Thus {W!=0} is dense on a neighborhood. The confirmed global rank identity A413 extends by continuity to this whole neighborhood.

The C2 submersion theorem and dH wedge dg=0 imply g=G(H) there, with G in C2. Indeed in coordinates (h,s,z), differentiation of g in the s,z directions vanishes, so it is a function of h; restriction to a C2 transverse section gives its C2 regularity. At q, g(q)=0 and

    grad g(q)=DB(q)^T u=rho u=-(rho/a)grad H(q).

Therefore

    B h=-aG(H(q)+h)=b(h), b(0)=0, b'(0)=rho.           (4)

The level h=0 is invariant under B. It is invariant under W because WH=0. Its tangent plane at q is u perpendicular, and the two restricted eigenvalues are lambda and eta. All eigenvalues in (1) are distinct: rho differs from lambda by kappa; eta is positive and the others are negative.

For the regularity needed below, choose s,z to be two linear ambient coordinates whose restrictions to the tangent plane are independent. The C2 level is the graph of a C2 function of (s,z). The components of B restricted to the surface, expressed as the derivatives of these linear coordinates, are linear projections of B composed with this C2 graph. Hence this two-dimensional vector field is C2. This argument is important: a general C2 change of three-dimensional coordinates need only push a C2 vector field to a C1 field. Only the restricted components in the chosen linear coordinates are used.

## 3. Stream function and exact normalization

Complete (h,s,z) to local coordinates, choosing orientation so that the Euclidean volume has the form

    vol=m(h,s,z) dh wedge ds wedge dz, m>0.

The Jacobian m is C1, and nu=m(0,s,z) ds wedge dz is a positive C1 area form on Sigma. Since W h=0 and div W=0, the coordinate divergence identity gives

    partial_s(m W^s)+partial_z(m W^z)=0.

Thus i_W nu is a closed C1 one-form. On a small simply connected patch it equals d psi for a C2 function psi, with the chosen normalization. Nondegeneracy of nu gives W=0 if and only if d psi=0.

The ambient divergence is div B=3c. Combining Lie differentiation of vol with (4), or directly differentiating mB^h with respect to h at h=0, gives

    L_(B|Sigma) nu=(3c-rho)nu.

The exact bracket [B,W]=-kappa W consequently yields

    d(B psi)=L_B(i_W nu)
            =i_[B,W] nu+i_W L_B nu
            =(3c-rho-kappa)d psi=mu d psi.

The difference B psi-mu psi is constant. Evaluating at q, where B=0 and psi=0, makes that constant zero, proving (2).

Let N=grad H and define f=(B cross W).N/|N|² on this regular level. The area form agrees with contraction of vol by N/|N|² when evaluated on tangent vectors. Therefore

    f=nu(B,W), B psi=nu(W,B)=-f,
    f=-mu psi.                                         (5)

This proves the exact constant and sign. It avoids the unnecessary argument about a ratio on a quotient of vortex curves.

The same calculation applies locally on the regular vortical H-level through a vortical equilibrium p with the same rho and mu>0. There psi(p)=0, d psi(p)!=0, and its local zero curve is the W-line through p. Formula (5) holds there as well. This is a local assertion on a simply connected patch, not existence of a global stream function on a possibly multiply connected level.

## 4. The unstable curve is irrotational

The ambient linearization F=DB(q) has largest eigenvalue eta. In a fixed norm defined by an eigenbasis, continuity of DB gives a neighborhood on which the variational equation has the bound

    ||D Phi_T(x)||<=C exp((eta+epsilon)T)

for every segment staying in that neighborhood. The local one-dimensional unstable curve on Sigma is also an ambient unstable curve. Along its negative orbit,

    |Phi_(-T)(y)-q|<=C_y exp(-(eta-epsilon)T).

Here epsilon>0 can be chosen arbitrarily small, and the whole negative segment stays in the chosen neighborhood after restricting y. Since W(q)=0 and W is C1, its size at the negative endpoint is bounded by a constant times that distance. The exact Cauchy law gives

    |W(y)|<=C_y exp((-kappa+2epsilon)T).

Choose 2epsilon<kappa and let T tend to infinity. Thus W=0 on the unstable curve. Consequently d psi=0 there and psi=psi(q)=0.

On the local stable curve, (2) gives psi(Phi_t y)=exp(mu t)psi(y). Its forward orbit converges to q, so continuity and mu>0 imply psi(y)=0. At this stage its normal derivative, and hence W there, need not vanish.

## 5. A quadratic passage estimate excludes rho<-2kappa

The restricted vector field is C2 by Section2. Its stable and unstable curves are C2. Write them in eigenline coordinates as z=h_s(s) and s=h_u(z), with both graph derivatives zero at q. A simultaneous C2 change of coordinates makes them the axes. As in the A542 proof, the transformed field need not be C2. Nevertheless each transformed component vanishes on the corresponding invariant axis; apply the mean-value theorem to the original components while holding the other coordinate fixed. This factors the equations as

    s'=s(lambda+r_1(s,z)), z'=z(eta+r_2(s,z)),
    r_i(s,z)->0 as (s,z)->(0,0).                         (6)

The coordinate change is C2, so psi remains C2. The stable axis is z=0 and the unstable axis is s=0. By Section4,

    psi(s,0)=0, psi(0,z)=0, d psi(0,z)=0.                (7)

Assume rho<-2kappa. Choose epsilon>0 with

    rho+2kappa+3epsilon<0,
    lambda+epsilon<0<eta-epsilon,

and a small rectangle on which |r_i|<=epsilon. Fix a small s0!=0. Start at (s0,z0), with 0<z0<delta and delta a fixed positive height inside the rectangle, and stop at the first time T when z(T)=delta. Equation (6) makes z increase and |s| decrease, so the entire segment remains inside. Moreover T tends to infinity as z0 tends to zero, and

    |s(T)|<=|s0| exp((lambda+epsilon)T),
    z0>=delta exp(-(eta+epsilon)T).                     (8)

The last two identities in (7) and bounded second derivatives of psi near the compact exit segment give

    |psi(s(T),delta)|<=C|s(T)|².

Transport (2) and (8) now yield

    |psi(s0,z0)|/z0
       <=(C|s0|²/delta)
          exp((-mu+2lambda+eta+3epsilon)T)
       =(C|s0|²/delta)exp((rho+2kappa+3epsilon)T)->0.    (9)

Because psi(s0,0)=0 and psi is differentiable, this one-sided quotient already implies partial_z psi(s0,0)=0. Also partial_s psi(s0,0)=0 by (7). Hence d psi=0 on the stable curve, and W=0 there. The same conclusion holds for both signs of s0; no second passage estimate from negative z0 is necessary for a differentiable function.

If a vortical W-line is a B-orbit converging to q, then H is constant along it by WH=0 and has the limit H(q). Its late orbit therefore lies on Sigma and on the local stable curve of the restricted hyperbolic saddle. Uniqueness of this stable manifold and the preceding conclusion contradict its nonzero vorticity when rho<-2kappa. This proves (3).

## 6. A reduced surface model at and above the endpoint

For any rho in [-2kappa,-kappa), retain lambda,eta,mu and put sigma=rho/(rho+kappa)>=2. On the plane with area form ds wedge dz define

    B0=lambda s partial_s+eta z partial_z,
    psi0=-|s|^sigma z,
    W0=-|s|^sigma partial_s
          +sigma z sign(s)|s|^(sigma-1) partial_z.       (10)

The function psi0 is C2 and W0 is C1, including at s=0. Direct differentiation gives

    i_W0(ds wedge dz)=d psi0, div W0=0,
    [B0,W0]=-kappa W0, B0 psi0=mu psi0,
    div B0=3c-rho.

For the bracket, lambda(sigma-1)=-kappa; for the scalar equation, lambda sigma+eta=mu. On the unstable axis s=0, W0=0. On the stable half-axis s>0,z=0, W0 is nonzero and

    B0=kappa tau W0,
    tau=(-lambda/kappa)s^(1-sigma), B0 tau=kappa tau.

Thus the reduced surface identities permit the endpoint and every value in (3). They do not impose the ambient identities W=curl U and B=Ax+U or the full pressure equation. No exact Euler germ or global decaying profile is constructed. Any separate claim about a third-order full Euler jet requires its own source and coefficient audit and is outside this proof.

Finally,

    d/drho [rho/(rho+kappa)]=kappa/(rho+kappa)^2>0.

The source's word decreasing is an arithmetic error; its endpoint values, interval and sigma>=2 conclusion are correct.

## 7. The cited polynomial does not pass the global rank condition

This is a separate audit of the actual source script, read without executing it. Its translated local coordinates are (x,s,z), its nonzero constant velocity is u, and its amplitude is theta. At omega=0 it sets

    alpha=-2-3c, beta0=-1-2c, gamma=3+5c,
    rho=-2(1+c), lambda=-(1+c), eta=3+6c,
    U=(u+alpha x+theta s²z, beta0 s,
       gamma z-x²/2-beta0 x s²/(2u)),
    B=U+(cx-u,cs,cz).

The displayed curl is

    W=(-beta0 xs/u, x+(beta0/(2u)+theta)s², -2theta sz).

Consequently DW(q)!=0 at q=0. The script only checks helicity through degree2, the vorticity equation through degree2, and that the force truncated at degree3 is curl-free. None of those checks tests the rank identity. Its cubic helicity equals

    -(alpha beta0/u)x²s
      +beta0(beta0/(2u)+theta)s³-2gamma theta sz².

Higher velocity terms could affect this cubic helicity because u!=0, so that expression alone is not used as a finite-jet impossibility argument.

There is a lower-order obstruction in the stipulated global class. Along x=s=0 one has W=0 exactly, U=(u,0,gamma z), and

    grad H=(-au,0,-a gamma z),
    grad g=(rho u,0,2eta gamma z).

Here grad H is the necessary Lamb covector B cross W-aU. Their cross product has s component

    a u gamma(2eta-rho)z
      =2a u(3+5c)(4+7c)z,

with nonzero coefficient for 0<c<1/2 and u!=0. Since DW(q)!=0, the global rank identity extends to a whole neighborhood as in Section2. This linear defect contradicts that identity. Adding velocity terms of degree4 or higher cannot change the linear defect: g changes first at degree4 and its gradient first at degree3, while the Lamb covector changes first at degree4 because B(q)=W(q)=0. Thus the displayed jet cannot extend to a profile in the present global class without changing its lower-order coefficients.

This refutes the particular claim that this script certifies compatibility through third order with the global setting. It does not prove that all alternative endpoint jets fail, nor does it invalidate the reduced surface model or the independently checked truncated equations.

## 8. Dependencies and comparison

The full new source Section4e was read. The argument uses the already confirmed rank identity, bracket, Lamb identity and the exact inherited endpoint data of A540-A541. Ordinary finite-dimensional stable-manifold and submersion results are used with their differentiability checked above. All passage estimates and reduced-model identities are derived explicitly. The proof retains the distinction between an actual endpoint, a general irrotational equilibrium and a reduced surface model.

Existing configured-model team discussion supplies the established premises. The complete actual in the team records referee response was also read and agrees with Sections1-7. That response is an the external referee (a second model), not a model review; its attempted model consultation failed credentials. No focused successful model comparison of this new section has been received. The configured-model coordinator and theory agents can continue the comparison through their files. No new client, computation or formal build was used.
