# A common supported flat velocity and pressure zero

Status: independent reconstruction of LIT201. The conclusions below are confirmed at the exact global hypotheses in Section1. The cited planar elliptic theorem remains an explicit external dependency. No unrestricted Euler nonexistence theorem is claimed.

## 1. Exact theorem and notation

Let 2/5<c<1/2, let omega be any finite real number, and set

    Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax,
    a=1-2c, b=2(1-c), p=(1-c)/c,
    d=p-1=a/c, q=b/a=2p/d, eta=a/b=1/q.

Suppose U in C2(R3;R3) and P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1)                         (1)

for a finite constant C. The helicity equation is global. Let V and P2 be the actual leading velocity and canonical pressure tails, and define on D=R3 minus{0}

    W=curl V, k=X.V, S=P2-|V|^2/2.

Fix any alpha in (0,1). The established regularity is V in C^(1,alpha)_loc(D), P2 in C^(2,alpha)_loc(D), hence S in C^(1,alpha)_loc(D). Write G=W|S2, K=k|S2, h=S|S2 and

    T0={w in S2: V(w)=0, DV(w)=0, S(w)=0} intersect supp G.

Then

    U!=0 implies T0!=empty.                         (2)

At a velocity zero S=P2, so the pressure tail also vanishes at the supplied point. The theorem asserts existence of at least one common zero, not pressure vanishing at every supported flat velocity zero.

There is also a support conclusion. Set Z=int_D{k=0}, V0=1_Z V, W0=curl V0 and E0=supp(V0|S2). Then

    boundary E0 subset T0.                          (3)

In particular any nonempty proper support of V0 supplies a point of T0. Supports and boundaries are relative to D or S2 as indicated. Constants may depend on omega; no uniform estimates as |omega| tends to infinity are asserted.

## 2. The extended field and the actual pressure scalar

The previously established actual-tail identities are

    grad k=X cross W-aV,
    X.k=-ak, X.S=-bS, W.k=W.S=0,                    (4)
    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    W(exp(tA)x)=exp(-t)exp(-omega tJ)W(x).

The scalar transports hold on every actual partial W curve. A963 excludes noninterior vortical k-zeros. A973-A985 give

    boundary Z subset {V=DV=W=0} intersect supp W,
    V0 in C^(1,alpha)_loc(D), DV0=1_Z DV,
    div V0=0, W0=1_Z W.                             (5)

For clarity, the extension has no interface derivative: at a boundary point V=DV=0, differentiability gives V0=o(distance), and its derivative is continuous across the boundary. A segment joining opposite sides of a convex coordinate ball meets the boundary. Subtracting DV there proves the same local alpha-Holder estimate as for DV. This proves the regularity in (5) without a regular boundary assumption.

On Z, k=grad k=0, so (4) gives X cross W=aV. Off Z both extended fields vanish. Continuity yields globally on D

    X.V0=0, X cross W0=aV0, W0.S=0.                 (6)

The field V0 inherits twisted homogeneity since Z is invariant under exp(tA). The scalar in (6) is the original S of the full tail. No separate pressure for V0 is introduced.

The identity X cross W0=aV0 gives supp V0 subset supp W0. Conversely, a neighborhood on which V0=0 has W0=0. Thus supp V0=supp W0 subset supp W. Homogeneity transfers these support relations to the sphere.

## 3. Angular equations, including the rotation terms

Put zeta(w)=Jw and gamma=omega/c. For tangent vectors define R_w e=w cross e. On S2 write

    v=w.V0, Y=V0-vw,
    rho=w.W0/c, F=W0-rho Aw.

Both Y and F are tangent. The constraint X.V0=0 gives v=gamma zeta.Y. Taking the tangential component of X cross W0=aV0 gives

    c R_w F=aY, F=-(a/c)R_w Y.                     (7)

Indeed X cross W0=X cross F, and (-omega zeta) cross F is normal. In particular F is C^(1,alpha), even though W0 initially has only C^alpha regularity.

For any twisted field of radial degree -m with radial component u and tangential component T at r=1, its divergence in x=r exp(-gamma log(r)J)w is

    r^(-m-1)[(2-m)u+gamma zeta.grad_S u+div_S T].   (8)

This follows from ordinary polar divergence: at fixed physical angle the twisted angle differentiates by gamma zeta/r. For W0, u=c rho, T=F-omega rho zeta and m=p+1. Since div_S zeta=0, the angular derivative terms cancel, leaving

    div_S F=a rho.                                 (9)

This calculation is valid first in distributions, where div W0=0; both sides of (9) are continuous, so the final equation is pointwise. Equation W0.S=0 and X.S=-bS give

    F.grad_S h=b rho h.                             (10)

For V0, use m=p, u=gamma zeta.Y, T=Y in (8). The result is

    div_S(D0 Y)+(2-p)gamma zeta.Y=0,
    D0=I+gamma^2 zeta tensor zeta.                   (11)

Here I is the tangent-plane identity. The sign and coefficient of the drift are retained for arbitrary omega.

## 4. The local elliptic theorem and its exact source scope

On a simply connected coordinate disk compactly contained in {h!=0}, put beta=|h|^eta. It is positive C^(1,alpha), with a positive lower bound. Equations (9)-(10) imply

    div_S(F/beta)
      =beta^(-1)(a rho-eta F.grad_S h/h)=0.

By (7), the one-form dual to Y/beta is closed. The ordinary Poincare lemma therefore gives a real f in C^(2,alpha) with Y=beta grad_S f. Equation (11) becomes

    div_S(beta D0 grad_S f)
       +(2-p)gamma beta zeta.grad_S f=0.            (12)

The principal matrix is symmetric and uniformly positive definite. In smooth local coordinates, multiply by the positive metric area density. The resulting equation is div(C grad f)+e.grad f=0, where C is symmetric uniformly positive definite and Lipschitz, e is bounded, and there is no zeroth-order term.

The external result used is the local argument in G. Alessandrini and R. Magnanini, The index of isolated critical points and solutions of elliptic equations in the plane, Annali della Scuola Normale Superiore di Pisa, series4,19(4)(1992),567-589, Section2, printed570, equations (2.1)-(2.7). Its displayed operator has Lipschitz symmetric principal coefficients and bounded drift. Its determinant normalization is removed as follows. With delta=sqrt(det C), divide the equation by delta to obtain

    div((C/delta) grad f)
      +[e/delta+(C grad delta)/delta^2].grad f=0.    (13)

The new principal determinant is1; the new coefficients remain Lipschitz and the drift bounded. The added drift sign is positive. Thus the exact local source hypotheses hold.

That local published result states that, unless f is locally constant, its gradient zeros are isolated of finite positive multiplicity m and have index -m. The same generalized analytic representation proves local unique continuation from an open constant region. We use this local result as a cited dependency. We do not reconstruct its uniformization and similarity principles, and do not invoke its later global boundary-value theorems. The actual primary PDF was independently retrieved; printed567-570 and589 were read, and printed570 was rendered and visually inspected because text extraction omits its equations.

Multiplying a vector by positive beta preserves index. The positive definite metric converting a coordinate gradient to grad_S f also preserves it: the interpolation between that matrix and the identity is positive definite at every point of a sufficiently small loop. Consequently on {h!=0}, either Y vanishes locally or its zeros are isolated with negative integer index. Finally Y=0 is equivalent to V0=0 because v=gamma zeta.Y.

No ellipticity bound at h=0 is obtained by this argument. The 1994 pure divergence-form paper is not a substitute citation for (12), which contains a drift.

## 5. Boundary of the support

Let w0 be in boundary E0. If h(w0)!=0, choose a connected coordinate disk about w0 contained in {h!=0}. It meets the open complement of E0, so Y=0 on a nonempty open subset. The local analytic representation in Section4 forces grad f, hence Y, to vanish on the connected disk. This contradicts w0 in the support. Therefore h(w0)=0.

At a boundary point of the support, V0=DV0=0 by continuity from its open complement. Moreover E0 subset closure Z. If w0 lies in Z, V=V0 near it. Otherwise it lies in boundary Z, where (5) already gives V=DV=0. Finally E0 subset supp G by Section2. These observations prove (3).

If T0 is empty, boundary E0 is empty. As the sphere is connected and E0 closed, E0 is either empty or the whole sphere. No smoothness, finite component count or regularity of boundary E0 is assumed.

## 6. The full-support alternative is impossible when T0 is empty

Suppose T0 is empty and E0=S2. The tangent C^(1,alpha) field Y cannot vanish on any open subset. At a zero with h!=0, Section4 therefore gives an isolated negative-index zero.

At a zero with h=0, DV0 cannot vanish: otherwise the inside-Z or boundary-Z argument of Section5 would give a point of T0. Write M=DV0(w). If W0(w)=0, then M is symmetric, trace free and nonzero. Differentiated homogeneity gives M Aw=0 at V0(w)=0. Thus its eigenvalues are mu,-mu,0, with mu!=0, and its kernel is exactly R Aw.

The derivative of Y at this zero is P_w M restricted to T_w S2, where P_w is orthogonal projection. Its determinant is

    det D_S Y=(c^2/|Aw|^2)det(M restricted to (Aw)^perp)<0. (14)

One way to check the factor is to choose an orthonormal basis with third vector Aw/|Aw|. Restriction of the symmetric rank-two quadratic form to the plane with unit normal w multiplies its nonzero determinant by (w.Aw/|Aw|)^2. Since w.Aw=c>0, the zero is nondegenerate of index -1.

If W0(w)!=0, then w is in Z, since the extended vorticity vanishes off Z. In a neighborhood V0=V. A1020, proved by completing an original finite vortex-time endpoint and transferring the quotient spectrum, says that every actual vortical zero of V is a nondegenerate saddle of Y. This gives index -1 here as well. It is essential that V is an actual global profile tail in this step; a local homogeneous model can have positive index.

Thus all zeros of Y are isolated with negative integer index. They form a closed subset of compact S2, so there are finitely many. Poincare-Hopf gives total index2, contrary to this sum; an empty zero set also has sum0 and is impossible. Therefore E0 cannot equal S2 under T0 empty. Together with Section5 this proves V0=0.

An equivalent useful observation is that E0=S2 already implies closure Z=S2, hence k=0 everywhere by continuity and Z=S2. The argument above does not need to assume this strengthening separately.

## 7. Joint scalar flux for the actual partial flow

If V0=0, then the nodal condition

    {k=0} subset {W=0}                              (N)

holds: a vortical k-zero would be in Z by A963, where V=V0=0 on a neighborhood, contradicting nonzero curl.

Suppose U!=0. Then W!=0, because the actual scattering map Xi:E->D is a C1 diffeomorphism with determinant1 and W composed Xi=DXi Omega. Its omitted core is compact and null. W=0 would force Omega=0 on E and by continuity globally, then harmonic Liouville and decay would give U=0.

The original C1 bounded Omega has a complete volume-preserving flow Gamma_t. Until Gamma_t reaches the omitted core, define the partial tail flow Psi_t=Xi composed Gamma_t composed Xi^(-1). Each surviving-time domain is open, and Psi_t is a C1 diffeomorphism onto its image with determinant1. A360 gives finite forward lifetime and terminal origin for almost every nonzero W starting point. These actual-flow facts, including their hypotheses, are retained from the full independent proof in the team records. No complete tail flow through the origin is defined.

Choose a positive-volume measurable subset B_* of {1<|x|<2,W!=0} all of whose arrival times are at most one finite T. It exists by taking the countable union over integer bounds for that lifetime. Put M_k=1+max_{1<=|x|<=2}|k(x)| and M_s=1+max_{1<=|x|<=2}|S(x)|. Every surviving trajectory from B_* remains in {|k|<M_k,|S|<M_s}, because both scalars are invariants of this same flow.

For a radial cutoff chi_epsilon equal to1 inside epsilon and0 outside 2epsilon, with |grad chi_epsilon|<=C_chi/epsilon, the fundamental theorem on each arriving curve gives

    1<=integral_0^lifetime |W(Psi_t x)| |grad chi_epsilon(Psi_t x)| dt.

Integrate over B_*. Tonelli applies to a nonnegative measurable integrand on the open time-space flow domain. At each time t<T, change variables by the partial diffeomorphism. It gives

    |B_*|<=(C_chi T/epsilon)
      integral_{epsilon<|x|<2epsilon, |k|<M_k, |S|<M_s}|W(x)| dx. (15)

Every change of variables is before the arrival time. No presumed return of an individual null scalar level is used.

Twisted polar coordinates have measure r^2 dr dA and

    |W|=r^(-p-1)|G|, k=r^(-d)K, S=r^(-2p)h.

For tau=epsilon^d, (15) therefore yields positive constants C0,C1,C2, independent of small tau, such that

    integral_{|K|<C1 tau, |h|<C2 tau^q}|G| dA>=C0 tau. (16)

The radial factor after division by epsilon is epsilon^(1-p)=tau^(-1), and 2p/d=q. The two scalar restrictions remain simultaneous throughout this calculation.

## 8. Localization of the joint flux

Assume T0 is empty. For every sphere point there is a neighborhood on which the mass in (16) is o(tau).

Outside supp G it is zero. If K or h is nonzero at the point, the joint sublevel is absent on a smaller neighborhood for sufficiently small tau. At a joint zero K=h=0, condition (N) gives W=0.

If V!=0 there, (4) gives grad k=-aV!=0. Its angular component is nonzero: X.grad k=0 at k=0, while X.w=c prevents a nonzero normal vector from annihilating X. In local coordinates (K,s), condition (N) and Holder continuity give |G|<=C|K|^alpha. The local mass is O(tau^(1+alpha)).

If V=0 but DV!=0, use the full independently proved saddle estimate A832 in the team records, Section2. Its exact local hypotheses are homogeneity, div V=V.W=0, C^(1,alpha) and (N), all satisfied here. There are C1 coordinates (u,v) with bounded Jacobian such that

    c0|uv|<=|K|<=C0|uv|,
    |G|<=C min(|u|,|v|)^alpha.

For completeness, the estimate straightens only the stable and unstable C1 curves of the angular field dual through the area form to the one-form V.dx. The identity C K=K div C and the uniformly integrable Holder error in a hyperbolic passage compare K to the product uv. It does not require a Hessian of k or a C2 linearizing change of coordinates. Integrating in one quadrant split at u=v gives a constant times

    integral_0^R integral_0^min(v,C tau/v) u^alpha du dv
       =O(tau^(1+alpha/2))=o(tau).

The additional h restriction only decreases this mass. Any remaining supported joint zero would have V=DV=0 and h=0, hence belong to T0, contrary to the assumption. A finite sphere cover now makes the full mass o(tau), contradicting (16). Thus U=0. Together with Sections5-6 this proves (2).

## 9. Dependencies, verification and limitations

The independent proof uses A963/A970 for interior vortical zeros, A973-A985 for boundary flatness and zero extension, A1020 for actual vortical saddles, A832 for the nodal saddle mass, and A360/A705-A708 for actual partial-flow return and measure transport. Their necessary regularity, original-flow completeness, compact null core and natural-rate hypotheses are not discarded. The complete A832 and A705-A708 proofs were reread in this audit, as were the boundary and extension arguments. The full nine-section LIT201 source and its separate planar-source scope note were read and compared.

New arguments are Sections3-6 and the explicit joint-scalar localization in Sections7-8. The only new external dependency is the precise local 1992 elliptic theorem in Section4. Verification retains the original source files, their hashes, the independently retrieved primary PDF, extracted text, rendered printed570 and real retrieval times. No numerical computation or formal build is claimed.

The result does not exclude T0, prove S=0 at every supported flat zero, assign a separate pressure to V0, assert ellipticity across h=0, remove global zero helicity, or derive the natural derivative bound from bare decay. In the V0=0 branch, a regular zero of h already has joint mass O(tau^q) and cannot be a concentration point; extending a corresponding critical-pressure refinement through nonzero V0 requires another argument and is not claimed here.

A focused comparison through the existing configured model agents remains requested and pending for this new theorem. Configuration is not provider runtime attestation. No failed nested model call counts as a review, and no new model client or agent is used.
