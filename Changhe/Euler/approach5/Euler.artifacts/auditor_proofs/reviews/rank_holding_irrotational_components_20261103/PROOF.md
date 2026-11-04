# Rank on an irrotational component and its angular boundary

Status: independent reconstruction of coordinator CO38, Sections2-3. Verdicts A651-A652 confirm the exact conditional conclusions below. This does not prove rank on an arbitrary irrotational component or exclude every component.

## 1. Exact setting

Let 1<p<3/2, c=1/(p+1), omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, and D=R3 minus{0}. Put lambda=p-1, mu=2-p, a=1-2c=c lambda, t=omega/c, and q=2p/lambda. Suppose V in C1,alpha_loc(D;R3), for some alpha>0, is divergence free and satisfies

    V(exp(sA)x)=exp(-(1-c)s)exp(-omega sJ)V(x).

Let P2 in C1(D) satisfy

    P2(exp(sA)x)=exp(-2(1-c)s)P2(x),
    -Delta P2=partial_i partial_j(V_i V_j)

in distributions. Set W=curl V, k=(Ax).V, Pi=P2+|V|2/2, S=P2-|V|2/2. A component Sigma always means a connected component of the OPEN set int{W=0}, not of the closed zero set. It is invariant under the twisted scaling because that connected family of diffeomorphisms preserves the zero set and starts at the identity. Its angular quotient Omega_Sigma is an open connected subset of S2 in coordinates rho=log r, chi=phi+t rho.

Assume V is not identically zero on Sigma and

    dk wedge dS=0 throughout Sigma.                         (1)

Then a single constant D0<0 satisfies

    S=D0 |k|^q throughout Sigma.

With C0=(a2/2)|D0| q(q-1), one has

    r^lambda |k| >= [(1-c)2/(C0(c2+omega2))]^(lambda/2)>0.   (2)

Consequently k and S have no zero on the closure of Sigma in D. On the angular closure, |K| has a positive lower bound and h a strictly negative upper bound, where k=c r^-lambda K and S=r^-2p h. The constants depend on D0,c,omega. They are not uniform over profiles or components.

## 2. Harmonicity and the exact lower bound

The homogeneity identity gives

    grad k=-aV+(Ax) cross W.

Thus on Sigma, V=-grad k/a and Delta k=0. This also proves that k is smooth there, by harmonic regularity, and hence V is smooth. The pressure equation becomes Delta P2=-|DV|2, because DV is symmetric. Its smooth right side makes P2 smooth locally. Since each component of V is harmonic,

    Delta Pi=0,
    S=Pi-|grad k|2/a2,
    Delta S=-(2/a2)|D2 k|2.                                 (3)

All second derivatives used here are interior derivatives on Sigma; no regularity of its boundary is assumed.

On any connected component Sigma' of Sigma intersect{k!=0}, homogeneity says

    (Ax).grad k=-ak,    (Ax).grad S=-2(1-c)S.

In particular grad k!=0 there. Equation(1) makes grad S parallel to grad k. Contracting with Ax yields

    grad S=q(S/k)grad k.

It follows by differentiation, and path connectedness of an open connected set, that S=D0 |k|^q on Sigma' for one real constant D0. Applying Delta and using Delta k=0 gives

    -(2/a2)|D2 k|2=D0 q(q-1)|k|^(q-2)|grad k|2.              (4)

To prove strict negativity and a quantitative bound, differentiate the first homogeneity identity:

    D2 k (Ax)=-(aI+A^T)grad k=-[(1-c)I+omega J]grad k.

Skew symmetry of J gives |[(1-c)I+omega J]v|>=(1-c)|v|. Also |Ax|<=sqrt(c2+omega2)r. The operator norm of a matrix is at most its Frobenius norm, so

    |D2 k|2 >= (1-c)2 |grad k|2/[(c2+omega2)r2].             (5)

Here grad k!=0. Equations(4)-(5) first give D0<0, then

    C0 |k|^(q-2)>=(1-c)2/[(c2+omega2)r2].

Since q-2=2/lambda, this is(2). There is no small-omega premise.

The component Sigma' cannot have a relative boundary point in Sigma. Such a point is away from0 and would have k=0 by continuity, contradicting(2) with the one fixed constant D0 on Sigma'. Thus Sigma' is relatively closed as well as open. Some such component exists, since k identically0 would make V0. Connectedness gives Sigma'=Sigma. The constant and bound therefore hold on the entire component and extend continuously to its closure in D. Finally lambda q=2p gives h=D0 c^q |K|^q and the asserted strictly negative angular bound.

This proves A651. Its contrapositive says that if the closure of a nonzero component meets either{k=0} or{S=0}, rank cannot hold throughout that component. It does not locate a point of rank failure on the boundary and does not show that any zero of k meets the closure of a nonzero component.

## 3. Additional hypotheses for a single cap or band

Retain the basic fields, homogeneities and pressure equation of Section1, but do not assume rank(1) on Sigma. Add

    V.W=0,
    W.grad S=0 on D,
    dk wedge dS=0 on{W!=0},
    S has no zeros on D.                                    (6)

Assume int{W=0} has exactly one connected component Sigma. The following precise configurations are considered separately: its angular quotient is a disk bounded by one C1 Jordan curve, or an annulus bounded by two disjoint C1 Jordan curves with complementary closed disks. These are global single-component configurations, not assertions about one member of a collection.

Set eta=1/q, f=|h|^eta>0, g=K/f. From(6), dg=0 on{W!=0}, and by continuity on its closure. Every point of the complement of Sigma is in that closure. Indeed a point outside the closure of{W!=0} would lie in another component of int{W=0}. Thus g is constant on each connected complementary disk. This last conclusion uses path connectedness of these disks, with interior paths and continuity to their C1 boundaries.

A620 says k has a zero for every nonzero global homogeneous divergence-free helicity-free V in this range. The proof is the closed form curl(V/k)=0, a global potential if k has no zero, its compact level graph, and the vanishing small-sphere flux O(r^(2-p)). A618 separately proves K identically0 forces V0 under the nonvanishing scalar hypotheses: its global potential solves a uniformly elliptic equation with drift on S2 and no zeroth-order term. No scalar symmetry is needed for that zero-K step.

Inside the angular component, harmonicity of k gives the scalar equation

    div_S2(M dK)+t(1-2lambda)ZK-lambda mu K=0,               (7)
    M=g_S2^-1+t2 Z tensor Z, Z=partial_chi.

It is uniformly elliptic on the sphere, with strictly negative zeroth-order coefficient. Maximum and minimum principles therefore apply on the disk or annulus, using continuous boundary values. In particular zero boundary values force K0, and boundary values of one strict sign force that sign throughout, with no assumption on the sign of its normal derivative.

## 4. The cap and band conclusions

For a cap the complementary disk has g=C. If C!=0, K=Cf has its strict sign there and on the boundary, and(7) gives that same sign on the cap. Then k has no zero anywhere, contrary to A620. If C=0, zero boundary values and(7) make K0 also on the cap, hence globally. A618 gives V0. Thus no nonzero tail satisfying(6) can have this single cap configuration.

For a band let C1,C2 be the constants on the two complementary caps. They cannot have the same strict sign, by the same maximum-principle and flux argument. They also cannot have a zero member unless V0. To see this carefully, suppose C1=0. Then K and dK vanish on that complementary cap and on its C1 boundary because K is globally C1. The twisted lift of that boundary is C1 away from0. Extend the harmonic k from the adjacent band side by zero onto the cap side in a local neighborhood. Both its value and its normal first derivative match zero. Integration by parts on either side, justified by C1 interfaces and the continuous first derivative, gives Delta k=0 distributionally across the interface. Equivalently the conormal boundary flux is zero. Weyl regularity makes the extension harmonic, and harmonic analyticity makes it zero in the connected neighborhood because it vanishes on an open side. Interior unique continuation then makes it zero throughout Sigma. Hence both boundary constants are zero, K is zero everywhere, and A618 gives V0.

Consequently for a nonzero tail C1 C2<0. A path inside the connected band between near-boundary points gives an interior zero of K by continuity. Equation(2) shows rank must fail somewhere in Sigma. Alternatively, rank and S nonzero throughout would force g to be one constant there, incompatible with C1!=C2.

The boundary argument does not presume a homogeneous Poisson Dirichlet inverse. It is only harmonic unique continuation for k with matching zero first jet. It also does not assert an interior tangent ball for a general C1 boundary.

## 5. Scope, dependencies and verification

A651 uses only the stated divergence, pressure equation, homogeneities and rank on Sigma. Helicity, scalar transport, A2 and boundary regularity enter neither(2) nor its contrapositive. A652 adds(6), the exact single-component cap/band topology and C1 boundaries, and uses the already independently checked A618/A620. A625's nonzero boundary-value alternative is compatible with these conclusions.

The remaining incidence question, arbitrary component collections, arbitrary nodes of S, and actual full-profile nonexistence are OPEN. The source's Section6 one-sign/period discussion is not part of these verdicts. Complete source and independent reconstruction have been read; no computation is needed. The source is a saved coordinator check from the configured model agent, with model configuration, the primary model, and no independent provider-runtime attestation.
