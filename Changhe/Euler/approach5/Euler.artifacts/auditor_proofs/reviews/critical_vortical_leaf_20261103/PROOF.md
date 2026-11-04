# Critical vortical Bernoulli leaves

## 1. Exact setting and dependencies

Let 0<c<1/2, omega be any real number, J the generator of rotations about the third axis, A=cI-omega J, a=1-2c and B(y)=Ay+U(y). Assume U belongs to C2(R3), P to C1(R3), div U=0, U.curl U=0 and

    ((1-c)I+omega J)U+DU B+grad P=0,
    |y||U(y)|+|y|^2|DU(y)| -> 0.

Set Omega=curl U, H=P+|U|^2/2+(Ay).U and g=U.B. No pressure gauge is imposed in this definition. The already audited A413, whose complete proof was reread, gives H,g in C2, grad H=-aU+B cross Omega, BH=-ag, Omega H=Omega g=0, [B,Omega]=-(1+c)Omega, and dg wedge dH=0 where Omega is nonzero. It also excludes nonconstant periodic vortex lines. The source's reference to Section5 for the rank identity should point to Section3 of that proof; the identity itself is available. Completeness of the vortex flow follows directly here because Omega is bounded. The linear-growth carrier is complete as well.

Let N={Omega!=0,grad g!=0}. At q in N with grad H(q)=0 let L be the connected component of {g=0} intersect N through q. The assertions in Sections2-5 and7 below hold under exactly these assumptions. Section6 has the additional natural-decay tail hypotheses of C50 Section1, including 2/5<c<1/2. The pinned revised C54 source is the version dated16:37:01Z. No formal verification is claimed.

## 2. Constant critical leaf and bounded geometry

On N write grad H=mu grad g, with mu C1. Equality of mixed derivatives gives dmu wedge dg=0. In a product chart for g this means mu=m(g), where m is C1. Since BH=-ag, the critical point has g(q)=0. Local constancy on the connected zero-level component gives mu=0 and H=h0=H(q) on L.

Differentiate BH=-ag. On L its result is Hess H B=-a grad g. Also Hess H=m'(0) grad g tensor grad g there. Consequently

    m'(0) B.grad g=-a.

The local values of m'(0) agree on chart overlaps meeting L and are locally constant along L. They therefore have one common nonzero value. With kappa=a/m'(0),

    B.grad g=-kappa on L,
    H=F(g) locally, F'(0)=0, F''(0)=a/kappa.

The chart equality for H follows by integrating m and fixing H=h0 on the zero-level plaque.

Direct differentiation gives

    grad g=DU^T Ay+A^T U+2DU^T U.

Hence |B.grad g| is bounded by (|A||y|+|U|)(|A||y||DU|+|A||U|+2|DU||U|), which tends to zero at infinity under the stated decay. The nonzero constant kappa forces L to be bounded. By continuity its compact closure satisfies g=0, grad H=0, H=h0 and B.grad g=-kappa. In particular B and grad g do not vanish on that closure, and |grad g| has a positive lower bound there.

A finite implicit-function cover of the closure places the zero level in finitely many C2 graph charts with bounded first derivative and bounded base domains. Their graph areas bound the area of L. This argument does not require finitely many components of L inside a chart or any regularity of its relative boundary.

## 3. Vortex invariance and the edge

The bracket and Omega g=0 give Omega(Bg)=0. Along the complete vortex line starting at a point of L, g remains zero and Bg remains -kappa. Uniqueness prevents a nonzero vortex line from reaching a zero of Omega in finite time. Thus the entire connected orbit remains in N and in the same zero-level component L. It is bounded.

If q' is in the closure of L but outside L, Omega(q') must be zero. Otherwise a connected small regular-level disk through q' meets L and joins q' to the same component. The Lamb identity then gives U(q')=0. Put M=DU(q'). Curl and divergence show that M is symmetric and trace free. The identities on the closure give

    B(q')=Aq', grad g(q')=M Aq',
    (Aq').M(Aq')=-kappa,
    grad P(q')=-M Aq' !=0, P(q')=h0.

Thus q' is nonzero, M is nonzero, and this is not a carrier equilibrium or a flat velocity zero. The Cauchy formula gives Omega=0 along the entire carrier orbit through q'. A nonzero symmetric trace-free 3 by3 matrix has rank at least2, since a rank-one symmetric matrix has nonzero trace.

## 4. Finite invariant measure and nonplanarity

Near the closure define Z=grad g/|grad g|^2 and nu=i_Z vol. Then dg wedge nu=vol. Since div Omega=0 and Omega g=0, Lie_Omega(dg)=0 and Lie_Omega(vol)=0. Therefore dg wedge Lie_Omega(nu)=0. On the two-dimensional level the restriction of Lie_Omega(nu) vanishes. The vortex flow on L preserves the positive area density

    dmu_L=dA/|grad g|.

Section2 shows 0<mu_L(L)<infinity. The flow is complete on L. Poincare recurrence applied to its time-one map and a countable base implies that almost every point returns arbitrarily close to itself along times tending to positive infinity. Applying it to the inverse gives the same assertion backward. The doubly recurrent points are dense because every nonempty open set has positive measure.

Suppose L were homeomorphic to an open subset of S2. Every simple closed curve in L separates it into two sides. For a short transverse arc through a regular recurrent point, join two successive distinct orbit crossings by the intervening orbit segment and the segment of the arc. This is a Jordan curve. Flow uniqueness prevents any crossing of its orbit portion; the flow has one fixed crossing direction through the arc portion. Thus later crossings are strictly ordered farther along the arc, and cannot approach the first crossing. This contradicts recurrence unless the orbit is periodic. Periodic vortex lines are excluded by A413. L is therefore nonplanar.

The ordered-crossing proof uses separation, not the presence of the bounded filling region in the surface domain. Holes and ends create no exception. Hanche-Olsen's complete primary four-page note, version2007-01-16, was already obtained and was reread here; Lemma3 and Corollary4, pp3-4, give this precise argument. No claim that an arbitrary bounded planar orbit is periodic is used. Richards, On the classification of noncompact surfaces (1963), pp259-269, was obtained and read in full. The definition on p260 and Theorems1-3 identify nonplanarity with a nonseparating simple closed curve and represent a planar surface as S2 minus a closed totally disconnected set.

## 5. Compact leaves and finite positive genus

If L is closed, it is a connected compact orientable surface without boundary carrying the nowhere-zero tangent field Omega. Its Euler characteristic is zero, so it is a torus. Its embedding in R3 bounds a bounded domain D. The sign of B.n is constant and nonzero because Bg=-kappa. The flux identity

    integral_L B.n dA=3c volume(D)>0

shows that B points outward everywhere.

If every point of this torus escaped forward, choose a far sphere S_R enclosing it where B.y>0. Each forward orbit hits this sphere exactly once. Its hitting time depends C1 on the starting point by transversality. The resulting map pi:L->S_R has injective differential: a tangent vector in its kernel is a multiple of B, and B is transverse to L. Compactness makes this local diffeomorphism a surjective covering. Since S2 is simply connected, it would be a homeomorphism, contradicting the torus topology. Thus L meets the non-escaping set.

For a possibly noncompact L, its closure is a compact subset of the regular surface Sigma={g=0,grad g!=0}. It lies in the interior of a compact bordered subsurface Sigma0. Every compact bordered subsurface of L is contained in Sigma0; intersection numbers show that its genus is at most genus(Sigma0). Indeed a symplectic set of 2h cycles on a genus-h subsurface keeps its nonsingular intersection matrix in Sigma0, bounding h by genus(Sigma0). Taking an exhaustion gives finite genus for L. Its nonplanarity makes that genus positive. The number of ends need not be finite. These statements use the standard classification of surfaces, not a claimed finite bound on their ends.

## 6. Escaping edge under the additional tail hypotheses

Assume precisely C50 Section1 and its confirmed K3-K6. Let Xi map the escaping set to the punctured tail domain, W=curl V, X=Ax and W composed with Xi=D Xi Omega. At an escaping edge point q', put x=Xi(q'). Then W(x)=0, and images of nearby vortical points of L show x belongs to the support of W.

The work along the carrier through q' has derivative -kappa and value zero at time0, so takes both signs nearby. K4 says range DW contained in R X would make this work nonpositive at every time. Thus this range inclusion is impossible. K5 gives nilpotent DW, DW X=0, and says X in range DW would make work identically zero, also impossible. A nilpotent 3 by3 matrix of rank2 has one-dimensional kernel contained in its range. Since that kernel contains X!=0, rank2 is excluded. Therefore

    DW=w tensor ell, ell(w)=ell(X)=0,
    w!=0, ell!=0, w not parallel to X.

In particular DW squared is zero and ker DW=span{X,w}. If V(x)=0, K6 would instead force range DW=R X. Hence V(x)!=0. This already excludes a T-flat or common-flat tail point. One must not infer DW=0 merely from V=DV=0; the current source correctly removed that invalid implication.

## 7. Further checks, pressure gauge and remaining scope

On L, Omega.g=0 and B.g=-kappa imply that B is not parallel to Omega. The Lamb identity gives aU=B cross Omega!=0. Thus the edge is exactly the intersection of the closure with either {Omega=0} or {U=0}. Continuity also extends

    Hess H=(a/kappa) grad g tensor grad g

to the closure, where it has rank1.

Adding a constant to P adds the same constant to h0. Whenever H along an escaping orbit has a finite limit h_inf, integrating BH=-ag gives h0-h_inf=a integral_0^infinity g dt, interpreted as an improper integral. In the additional natural-decay class and normalized gauge of C49/C52, h_inf=0 and that integral is absolutely convergent. Only in that gauge does the source's sign conclusion h0<0 follow from nonpositive future work and kappa>0. The revised Remark3 makes these distinctions.

The compactly supported axisymmetric field U=curl(psi e_theta), with smooth psi supported away from the axis, is divergence free and helicity free. Its curl is (-psi_zz-psi_rr-psi_r/r+psi/r^2)e_theta, so its nonzero vortex lines are circles. This checks the source's warning that the no-periodic-vortex statement uses the full profile equation. The compactly supported profile exclusion quoted in the target interval follows from (1-5c/2) integral |U|^2=0. No cutoff model is thereby a global profile.

The critical-leaf theorem and these strengthenings are CONFIRMED. They do not address vortical critical points with grad g=0, produce a neighborhood excluding critical leaves, exclude a common flat tail orbit, remove zero helicity or natural decay, or prove the main bare-decay conjecture. Those implications remain OPEN.
