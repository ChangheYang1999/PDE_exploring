# Matching the actual tail scalar across the scattering core

Status: CONFIRMED A736-A740 after full source, dependency and independent-proof reads.

## 1. Exact statement and dependencies

Fix 2/5<c<1/2 and any finite real omega. Put p=(1-c)/c, lambda=2(1-c), kappa=1+c, Jx=(-x2,x1,0), A=cI-omega J. Let U in C2(R3;R3) and P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1),                       (1)

with finite C. Set B=Ax+U, Omega=curl U. Write Phi_t and Gamma_s for their flows. A209-A210 give a continuous actual scattering map Xi, a compact null set K=Xi^(-1){0}, and a volume-preserving C1 diffeomorphism Xi:E=R3 minus K -> D=R3 minus{0}, with

    Xi Phi_t=exp(tA)Xi,
    |Xi(y)-y|<=||U||infinity/c,
    W(Xi y)=D Xi(y)Omega(y).                        (2)

Let V,W and P2 be the actual tails, with the canonical pressure constant Pinf fixed as in A530. Set

    Q=P-Pinf-|U|^2/2,
    S=P2-|V|^2/2,
    F=S composed with Xi on E.

The precise conclusions are as follows. F has equal values at any two points of E on the same complete Gamma line, even if the segment between them crosses K. Define

    K_Omega={y in K: Gamma_s(y) in K for every real s},
    O=R3 minus K_Omega.

K_Omega is a compact null set invariant under Phi and Gamma. There is a unique C1 extension Ftilde of F to O that is constant on all complete Gamma lines in O. It satisfies Ftilde(Phi_t y)=exp(-lambda t)Ftilde(y).

Extend it by0 on K_Omega and call the result Fhat. With h=S on S2 and q=3/(2p) in(1,3/2),

    volume{|Fhat|>a}=(a^(-q)/3) integral_S2 |h|^q dA, a>0.     (3)

Its superlevel sets are bounded, Gamma-invariant and of finite measure. Almost every point of each is recurrent for Gamma_1. Fhat is locally integrable and on all R3 satisfies

    div(Fhat Omega)=0,
    div(Fhat B)=(5c-2)Fhat                           (4)

in distributions, with no deleted core term. Whenever Ftilde(y)!=0, the backward B orbit of y approaches K_Omega in distance. Consequently an empty K_Omega, or local boundedness of Ftilde on O near every point of K_Omega, forces U=0. None of those sufficient conditions is derived from(1).

Natural rates in(1) can instead be supplied by U->0 and DU=O(sqrt(|x|)) through A601. All conclusions retain global zero helicity and the derivative premise. No symmetry, density, angular truncation or bound on omega is imposed.

## 2. The complete original flow and the matching identity

The bounded field Omega is C1, so Gamma is complete; no bound on D Omega at infinity is needed. The C1 field B has at most linear growth, so Phi is complete. Their Jacobians are respectively1 and exp(3ct), since div Omega=0 and div B=3c.

Dot momentum with Omega and the vorticity equation with U. The two skew terms cancel. With H=U.Omega, the result is

    B.grad H=-(2-c)H-Omega.grad(P-|U|^2/2).

Since H is identically0, Omega.grad Q=0. Q is C1; therefore

    Q(Gamma_s y)=Q(y)                               (5)

for every real s and every y, including segments inside K.

The vorticity equation also gives DB Omega-B.grad Omega=kappa Omega. Its variational formula and uniqueness of the complete Gamma flow imply

    D Phi_t(y)Omega(y)=exp(kappa t)Omega(Phi_t y),
    Phi_t Gamma_s=Gamma_(exp(kappa t)s) Phi_t.        (6)

In detail, differentiation of Phi_t Gamma_s(y) with respect to s gives exp(kappa t) times Omega at that point, with the correct initial value. Completeness permits every finite, possibly exponentially large, time on the right.

By A530 and A538, locally uniformly off zero,

    u_t(x)=exp((1-c)t)exp(omega tJ)U(exp(tA)x)->V(x),
    p_t(x)=exp(lambda t)(P(exp(tA)x)-Pinf)->P2(x).

The pressure convergence is C1; the velocity convergence is C^(1,alpha) for each alpha<1. Only their uniform convergence is needed next. Put v_t(y)=exp(-tA)Phi_t(y). By actual scattering v_t(y)->Xi(y). On a compact subset of E the limiting arguments stay in a compact annulus, and so do v_t for all sufficiently large t. Orthogonality of the rotation gives

    exp(lambda t)Q(Phi_t y)
       =p_t(v_t(y))-|u_t(v_t(y))|^2/2 -> S(Xi y)=F(y).        (7)

For y,z=Gamma_s y both in E, (5)-(6) give Q(Phi_t z)=Q(Phi_t y) for every t. Taking the two limits in(7) proves F(z)=F(y). No approximation through the core is used; both limiting arguments separately remain outside the origin.

This matching is stronger than constancy on a single punctured W arc. The latter corresponds only to one connected interval during which the original Gamma curve avoids K.

## 3. Extension to the complement of a jointly invariant core

The union of Gamma translates of E is open. Its complement is exactly K_Omega: a point outside the union has its entire Gamma line in K, and conversely. Thus K_Omega is closed, contained in compact null K, and Gamma-invariant. Equation(6) and Phi_t(K)=K make it Phi-invariant as well, since exp(kappa t) maps all real vortex times onto all real times.

For y in O choose any s with Gamma_s y in E and define

    Ftilde(y)=F(Gamma_s y).                          (8)

Section2 proves independence of s. One chosen s remains admissible in a neighborhood of y because E is open. The function there is a composition of C1 maps: Gamma_s, Xi on E, and S. The C1 regularity of S follows from A530 pressure regularity and A538 velocity regularity. Hence Ftilde is C1 on O. Invariance along the complete Gamma line follows immediately from the definition, and also proves uniqueness among invariant extensions.

On E, scalar homogeneity and (2) give F(Phi_t z)=exp(-lambda t)F(z). If z=Gamma_s y is an admissible endpoint for (8), then Phi_t z=Gamma_(exp(kappa t)s)Phi_t y is another admissible endpoint. Applying (8) proves the scaling law on all O. Differentiating gives

    B.grad Ftilde=-lambda Ftilde,
    Omega.grad Ftilde=0.

The value0 extension on K_Omega is measurable, and both flow laws remain exactly true there because that set is invariant. This does not define a value of the tail scalar at the punctured origin or a tail flow through that origin.

## 4. Exact level distribution, boundedness and recurrence

O minus E is a subset of K and has zero volume. Values assigned there or on K_Omega do not alter a distribution function. On E use the determinant1 diffeomorphism Xi, followed by twisted polar coordinates x=exp((log r)A/c)w. Since S(x)=r^(-2p)h(w) and dx=r^2 dr dA,

    volume{|Fhat|>a}
      =integral_S2 integral_0^infinity
           1_(r^(-2p)|h(w)|>a)r^2 dr dA
      =(a^(-q)/3)integral_S2 |h|^q dA.

This proves(3), including its constant. The angular function h is continuous and bounded. For an E point in the superlevel set, |Xi(y)|< (||h||infinity/a)^(1/(2p)); (2) bounds |y| by this radius plus ||U||infinity/c. Any remaining points lie in bounded K. Thus the full superlevel set, including its possible null additions, is bounded.

Exact Gamma invariance of Fhat makes every superlevel invariant. Gamma_1 is an invertible volume-preserving map of this finite-measure set, so Poincare recurrence applies. Applying measurable recurrence to a countable Euclidean ball base proves almost every point returns to each of its neighborhoods along positive integers. The closure of the superlevel is compact and Gamma-invariant because every Gamma_s is a homeomorphism and preserves the set exactly. This conclusion gives recurrence, not a periodic curve.

For a compact set C0 of finite volume, layer-cake integration bounds

    integral_(C0)|Fhat|
       <=volume(C0)+[one third integral_S2 |h|^q]
                              integral_1^infinity a^(-q) da,

which is finite because q>1. No global L1 assertion is made: the distribution at small levels has a different integrability issue.

## 5. Global weak transport without a core defect

Let psi be smooth and compactly supported. Change variables x=Phi_t y, use det D Phi_t=exp(3ct), and the exact scaling law of Fhat, including on K_Omega. Then

    integral Fhat(y)psi(Phi_t y)dy
       =exp((lambda-3c)t)integral Fhat(x)psi(x)dx.    (9)

For t in a bounded neighborhood of0, all preimages of the support lie in one compact set. The derivative of psi(Phi_t y) is uniformly bounded there, and Fhat is locally integrable. Dominated convergence differentiates(9) at0. It yields

    integral Fhat B.grad psi=(lambda-3c)integral Fhat psi,

which is precisely the second equation in(4), since3c-lambda=5c-2. The identical calculation with Gamma, its determinant1 and exact Fhat invariance gives the first equation. No pointwise derivative on K_Omega and no formal integration by parts across an unknown singular boundary is used. A core-supported defect would contradict this complete flow identity.

## 6. Backward growth and the exact remaining condition

Bounded U gives along backward B time the scalar estimate r'<=-cr+||U||infinity whenever r>0. Consequently each backward orbit stays in a fixed compact ball. If Ftilde(y)!=0, its value along that orbit has magnitude exp(lambda t)|Ftilde(y)|, which tends to infinity as t tends to infinity.

For any epsilon>0, the portion of the fixed ball at distance at least epsilon from K_Omega is a compact subset of O. Ftilde is continuous and bounded on it. The growing orbit value eventually prevents visits there. Hence dist(Phi_(-t)y,K_Omega)->0. If K_Omega were empty, continuity would bound Ftilde on the whole trapping ball, a contradiction.

More generally, suppose each point of K_Omega has a neighborhood on whose intersection with O the function Ftilde is bounded. A finite cover of compact K_Omega, followed by continuity on the remaining compact portion of any ball, bounds Ftilde on every such ball. The same growth argument forces Ftilde=0. Thus S=0 on D. The annular Poisson-mean identity A707 forces V=0; exact scattering, continuity across the null core and harmonic Liouville then give U=0.

Conversely, if U is nonzero, A707 gives S not identically0, so Ftilde has a nonzero value somewhere. K_Omega is therefore nonempty and the preceding local boundedness condition fails somewhere. This does not imply K_Omega contains nonzero vorticity, a periodic orbit, or any specified geometry. Irrotational carrier equilibria can belong to it.

## 7. Audit scope and model exchange

The matching proof uses the actual global scalar Q, its complete original vortex transport, canonical pressure normalization and the exact commutation relation. The pressure stability and scalar compatibility proofs A530-A531 were reread in full. A209-A210, A538 and A707 supply the separately confirmed geometric, regularity and zero-scalar conclusions. The full LIT178 source was read and pinned before this reconstruction.

The superlevel recurrence is compatible with finite-time return of individual tail arcs: the original vortex curve can cross the core and start another escaping interval. Completeness is never transferred to the punctured tail flow. The matching, weak distribution identities and compact-core reduction are necessary constraints, not a proof of the campaign conjecture. The extra derivative and global-helicity hypotheses remain.

A focused response from the existing configured model agents is requested through working files; none on this new matching result has yet been counted as received. CO43 separately provides the received continuation on the critical-flux proof. Provider runtime is not independently attested. No numerical computation, formal build or new model client was used.
