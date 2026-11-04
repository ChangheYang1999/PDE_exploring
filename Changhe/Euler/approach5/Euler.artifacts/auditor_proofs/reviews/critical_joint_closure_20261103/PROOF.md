# Closed critical joint leaves and nonzero velocity

Status: C44 conclusions CONFIRMED, A936-A940. Combination with the critical-cycle theorem gives plane leaves only, A941. The general rotating exclusion remains OPEN, A942.

## 1. Exact setting and claims

Let 2/5<c<1/2 and omega be any real number. Set Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Assume U in C2(R3;R3), P in C1(R3) solve pointwise

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

with a finite C. Use the canonical pressure constant Pinf, B=Ax+U, Omega=curl U and complete flows Phi of B and Gamma of Omega. Define

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=H-Q=U.B.

Let K be the compact forward-bounded B core, E=R3 minus K, K_Omega the compact set of points whose whole Omega line lies in K, and O=R3 minus K_Omega. Use the established C1 scalar L on O extending k composed with the scattering diffeomorphism Xi:E->D=R3 minus {0}, where k(x)=(Ax).V(x), V is the actual tail, W=curl V and S=P2-|V|^2/2.

Suppose y0 in O satisfies L(y0)=0, dL(y0)=0, Omega(y0)!=0 and is not interior to {L=0}. Let N={Gamma_s Phi_t y0:s,t in R}, and let Cbar be its ambient closure. Then throughout Cbar,

    H=Q=g=0, dH=dQ=dg=0,
    aU=B cross Omega!=0,
    D2H=(Delta H) U U^T/|U|^2,
    D2Q=(Delta Q) U U^T/|U|^2.

Moreover Cbar lies in O, is closed with empty interior, and is a union of immersed joint leaves of the same noninterior critical type. On Cbar, for all real t,s,

    D Phi_t(y)^T U(Phi_t y)=exp(-at)U(y),
    D Gamma_s(y)^T U(Gamma_s y)=U(y).

At each y in Cbar intersect E,

    D Xi(y)^T V(Xi(y))=U(y)!=0.

Every such tail point has k=dk=S=dS=0 and W!=0. Their set is invariant under twisted dilation and contains the maximal W trajectory in D through each point. If omega=0, no initial point y0 as above exists. Properness, embeddedness of a whole leaf, vanishing Hessians and rotating nonexistence are not claimed.

## 2. Dependencies and the scalar trichotomy

We use the confirmed actual-profile identities and constructions:

    grad H=-aU+B cross Omega, BH=-ag,
    Omega H=Omega Q=0, [B,Omega]=-kappa Omega,
    L composed with Phi_t=exp(-at)L,
    L composed with Gamma_s=L,
    Lie_B(U.dx)=-a U.dx-dQ, Lie_Omega(U.dx)=0.

H,Q are C2, bounded and vanish at infinity. O is invariant under both complete flows and is the union of finite Gamma translates of E. The C1 rank lemma gives dH wedge dL=dQ wedge dL=dQ wedge dH=0 on the vortical set. Scattering gives exp(at)H composed with Phi_t->L and exp(2(1-c)t)Q composed with Phi_t->S composed with Xi in C1 locally on E. These are A810-A814, A209-A210 and A538-A539 at the stated scope. Completeness here follows from the actual bounded derivative and vorticity assumptions, not from any tail field near its removed origin.

We first verify C44 Lemma49, also covered by A922. If L=0, Omega!=0 and dH!=0, a regular H chart gives L=l(H), Q=q(H) and

    l(eta)=l'(eta)(eta-q(eta)).

If H-Q!=0 at the point, linear ODE uniqueness forces l=0 nearby. Otherwise translate finitely by Gamma into E. In the regular H charts the scalar H-flow has an equilibrium at its initial value eta0. Overlapping charts along each finite carrier segment retain the constant slope mu=q'(eta0). The pulled-back covector solves

    Phi_t^*dH=exp(-a(1-mu)t)dH.

It cannot vanish at a finite time, so the continuation covers every forward time. The escaping orbit has constant H=eta0, hence eta0=Q=0. The C1 scattering limit then forces mu<=0. If mu=0, dL=dH and dQ=0. If mu<0, choose eps in (0,-mu). On either punctured side of eta=0 a nonzero l solving the scalar ODE obeys

    |l(eta)|>=C|eta|^(1/(1-mu-eps)).

The exponent is strictly below one. A zero endpoint away from eta=0 contradicts regular ODE uniqueness, while the displayed bound at zero contradicts l in C1 and l(0)=0. Thus l vanishes on both sides, giving an open zero neighborhood. This proves the mutually exclusive alternatives: local zero interior, or dL=dH!=0 with H=Q=dQ=0. In particular noninterior critical L-zeros have dH=0.

## 3. Ambient first derivatives and Hessian directions

The four initial conditions persist on N by the scalar transport laws, invertibility of both flow derivatives, and the vorticity transport. Noninteriority is preserved by these homeomorphisms. Section 2 therefore gives dH=0 on N. The Lamb identity yields aU=B cross Omega, so g=U.B=0. H is invariant under both flows on N. One point of N lies in E; its carrier orbit escapes, forcing the common H value to be zero. Hence Q=H-g=0 on N too.

Differentiate the integrated identity H composed with Phi_t-H=-a integral_0^t g composed with Phi_r dr in the initial point. Its left derivative is zero on N for every t. Differentiating in t at zero gives dg=0, hence dQ=0. Since grad H and grad Q vanish on N, differentiating them along the B and Omega curves gives

    D2H B=D2H Omega=D2Q B=D2Q Omega=0.

All these are continuous ambient identities and extend to Cbar, even before knowing whether it lies in O. Once Section 4 proves B and Omega independent there, a symmetric matrix annihilating both is a multiple of the normal projection U U^T/|U|^2; its trace gives the stated Hessian coefficient. These Hessians need not vanish.

## 4. Kelvin transport, nonzero velocity and the domain closure

Every finite global flow map preserves Cbar. With dQ=0 there, the covector Kelvin identity integrates exactly to the two transport equations in Section 1. If U(y)=0 at some y in Cbar, invertibility implies U(Phi_t y)=0 for every real t. Along that entire orbit B=Ax, so Phi_t y=exp(tA)y. Its backward limit is the origin, and closure gives 0 in Cbar and U(0)=0.

Use the confirmed zero-velocity carrier-equilibrium theorem A478, with its actual-profile rank premise A413: U(0)=B(0)=0 has an irrotational neighborhood. That neighborhood meets N, whose points all have Omega!=0, a contradiction. Therefore U is nowhere zero on Cbar. The already established aU=B cross Omega now gives Cbar contained in Reg={B cross Omega!=0}.

The intersection Cbar with K_Omega is compact, invariant under both flows and contained in Reg. If nonempty, it contains a genuine joint-flow plaque because B,Omega are independent. The confirmed compact-plaque exclusion A118 rules this out. Thus Cbar lies in O. Only now is continuity of L and dL invoked on its closure. It gives L=dL=0 throughout Cbar. A point of Cbar interior to {L=0} would have a zero neighborhood meeting N, contradicting the noninteriority of every point of N. Hence Cbar has empty interior and consists entirely of the same critical type.

Each full joint orbit through Cbar is the corresponding connected immersed leaf: the orbit is locally open in the rank-two leaf by its flow chart, and a connected leaf cannot split into disjoint open orbits. The confirmed affine-leaf classification A143 gives planes or open annuli intrinsically. Cbar need not be one such leaf or a lamination with separately proved transverse regularity.

There is now a further exclusion: A934 proves that a vortical carrier cycle in O lies in an open L-zero region. Every point of Cbar is a noninterior zero, so Cbar contains no carrier cycle. Each intrinsic annular joint leaf would contain a carrier cycle by A143. Thus every leaf in Cbar is an immersed plane. This conclusion still supplies neither properness nor a global embedded surface.

## 5. Tail transfer and the nonrotating exclusion

Write z_t=exp(-tA)Phi_t and u_t(z)=exp((1-c)t)exp(omega tJ)U(exp(tA)z). Since exp(tA)^T=exp(ct)exp(omega tJ), the carrier Kelvin identity is exactly

    D z_t(y)^T u_t(z_t(y))=U(y).

For y in E the C1 scattering limit and locally uniform velocity-tail convergence give D Xi(y)^T V(Xi(y))=U(y)!=0. The identical zero value and ambient differential of Q along the orbit, together with the C1 pressure-tail limit, give S=dS=0 at Xi(y). The L relation gives k=dk=0. The vorticity pushforward gives W!=0.

Invariance under twisted dilation follows from Xi(Phi_t y)=exp(tA)Xi(y). A maximal W trajectory is the Xi image of the connected component of its original Omega line lying in E. The image cannot end at a finite point of D while the original component fails to continue in E, because Xi is a diffeomorphism. This proves the precise maximal-trajectory assertion without treating the whole Omega line as contained in E.

If omega=0, the backward carrier orbit through y0 is bounded, so its alpha-limit set is nonempty, compact and invariant, contained in Cbar. On Cbar, U.B=0 and B=cy+U give

    B(|y|^2)=2|B|^2/c.

On the compact alpha-limit set B is nowhere zero, hence the right side has a strictly positive minimum. Integrating along its full invariant flow contradicts boundedness of |y|^2. Thus no such y0 exists when omega=0. This directly verifies the A511 input in the needed special case.

## 6. Audit and limits

The full eight-section C44 source was read, including its stated dependencies and unsubmitted Remark53. The trichotomy agrees with A922; the new closure argument strengthens A924 by removing its assumed V!=0 and proves nonvanishing even on the entire ambient closure. All displayed identities were checked by hand; no numerical or symbolic execution is needed for them. The source's informal phrase about a formal infinite normalization is not used.

Remark53's quantitative Hessian comparison is not part of the submitted theorem and is not certified here. Nor does this argument establish second-order flatness, properness, absence of open-zero nodes or nonexistence for omega!=0. The source's residual regular parallel branch is now excluded separately by A897, so its older list of remaining branches should be updated. The actual helicity and derivative assumptions remain essential premises of every conclusion here.
