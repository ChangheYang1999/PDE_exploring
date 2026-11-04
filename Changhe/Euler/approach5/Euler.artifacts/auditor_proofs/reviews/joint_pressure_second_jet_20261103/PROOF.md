# A common flat second pressure jet under the nodal premise

Status: LIT202 CONFIRMED A1062-A1066 after the complete source and independent seven-section postreads. The stronger scope extensions remain OPEN A1067. No unrestricted nonexistence result is claimed.

## 1. Exact theorem

Let 2/5<c<1/2 and let omega be any finite real number. Put Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), p=(1-c)/c, d=p-1=a/c and q=b/a=2p/d>6. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1)

with a finite C. Let V and P2 be the actual leading velocity and canonical quadratic pressure tails on D=R3 minus{0}. Define W=curl V, k=X.V and S=P2-|V|^2/2. Impose the additional nodal premise

    (N): k(x)=0 implies W(x)=0 for every x in D.

Then U!=0 implies that the compact set

    T2={w in S2: V(w)=DV(w)=P2(w)=grad P2(w)=D2P2(w)=0}
          intersect supp(W restricted to S2)

is nonempty. All listed derivatives are ambient derivatives on D. At every point of T2 the function grad S is differentiable, and S=grad S=D2S=0 there. This assertion does not require a C2 neighborhood for S.

In this actual-profile class, (N) is equivalent to V0=1_Z V being identically zero, where Z=int_D{k=0}. It is not inferred from the displayed profile hypotheses. Neither the conclusion nor this equivalence says that every supported flat velocity zero has zero pressure jets. Constants may depend on omega and the profile.

## 2. Actual identities and the role of (N)

Fix an alpha in (0,1). The established actual-tail theory gives V in C^(1,alpha)_loc, P2 in C^(2,alpha)_loc and

    div V=0, -Delta P2=tr((DV)^2),
    grad k=X cross W-aV,
    X.k=-ak, X.S=-bS, W.k=W.S=0.                 (1)

The scalar invariants are constant along every surviving actual W trajectory. The C1 scattering diffeomorphism Xi from the escaping set to D preserves volume and pushes the original vorticity to W. A360 and A705-A708 supply finite forward arrival at the removed origin for almost every point with W!=0. These hypotheses concern an actual global profile. A locally constructed tail is not enough.

A963 states that every vortical zero of k belongs to Z. On Z, k and grad k vanish, so (1) gives aV=X cross W. If (N) holds, V=W=0 throughout Z. Conversely, if V is zero on Z, then W=curl V is zero there; A963 then excludes every vortical k-zero. Thus (N) and V0=0 are equivalent. Only this equivalence uses A963 in the present proof.

In twisted polar coordinates x=r exp(-(omega/c)log(r)J)w, w in S2, set K=k|S2, h=S|S2 and G=W|S2. Homogeneity gives

    k(x)=r^(-d)K(w), S(x)=r^(-2p)h(w),
    |W(x)|=r^(-p-1)|G(w)|, dx=r^2 dr dA(w).      (2)

The angular rotation is an area-preserving sphere map for each r. The volume formula also follows by its radial-tangential triangular Jacobian; no derivative bound uniform in omega is required.

## 3. A lower bound with both scalar restrictions

Suppose U!=0. Then W is nonzero somewhere. Otherwise the scattering pushforward makes original vorticity zero on the full-measure open escaping set, hence everywhere by continuity. A bounded entire divergence-free curl-free U is componentwise harmonic and constant; the stated decay makes it zero.

By homogeneity, the annulus 1<|x|<2 contains an open set with W!=0. Almost every point there has finite forward lifetime. The union over integer T of the measurable sets with lifetime at most T has full measure in that vortical open set. Choose one such set B_* of positive finite volume and a finite T. Choose positive M_k,M_s strictly larger than the maximum absolute scalar values on the closed starting annulus.

Let chi_epsilon be a smooth radial cutoff equal to one for |x|<=epsilon, zero for |x|>=2epsilon, with |grad chi_epsilon|<=C/epsilon. For small epsilon its initial value is zero on B_*. Along a trajectory from B_*, its limit at arrival is one. The fundamental theorem of calculus on times before arrival and the absolute value inequality give

    1<=integral_0^lifetime |grad chi_epsilon(W_t x).W(W_t x)| dt.

Integrate over B_*. Tonelli applies to the nonnegative integrand. At each time before T use the partial volume-preserving flow on the surviving subset. Both scalar invariants remain bounded by M_k,M_s. Enlarging the integration domain therefore gives

    |B_*|<=C T/epsilon
       integral_{epsilon<|x|<2epsilon,
                 |k|<M_k, |S|<M_s}|W(x)| dx.     (3)

All flow maps used here stop before arrival. No continuation through the origin and no completeness of W on D are assumed.

Put tau=epsilon^d. In (2), the radial restriction implies |K|<C1 tau and |h|<C2 tau^q for constants independent of epsilon. The radial integral in (3), including its prefactor, is bounded by a constant times epsilon^(1-p)=tau^(-1). Thus positive constants C0,C1,C2 satisfy

    J(tau):=integral_{|K|<C1 tau, |h|<C2 tau^q}|G| dA
                  >=C0 tau                         (4)

for every sufficiently small tau. This is the joint lower bound. It has no dependence on LIT201 or on its elliptic theorem.

## 4. Pressure jets at a flat velocity zero

Let w0 satisfy V(w0)=DV(w0)=0. On a small ambient ball, the C^(1,alpha) bounds give, with z=x-w0,

    |V(x)|<=C|z|^(1+alpha), |DV(x)|<=C|z|^alpha,
    |DV(x)^T V(x)|<=C|z|^(1+2alpha).              (5)

The last quantity is grad(|V|^2/2), which is therefore differentiable at w0 with derivative zero. Hence

    S(w0)=P2(w0), grad S(w0)=grad P2(w0),
    D2S(w0)=D2P2(w0).                             (6)

Now also assume S(w0)=grad S(w0)=0 and put H=D2P2(w0). Equation (1) and DV(w0)=0 give tr H=0. Differentiating X.S=-bS at this single point is legitimate by (5)-(6), and gives H Aw0=0. If H!=0, the symmetric trace-free matrix H has eigenvalues mu,-mu,0 with mu!=0; its kernel is exactly R Aw0.

Its restriction as a quadratic form to T_w0 S2 is nonsingular and indefinite. Indeed projection from T_w0 S2 to (Aw0)^perp along Aw0 is invertible because w0.Aw0=c>0. It preserves the quadratic form, so this restriction is congruent to the nonsingular indefinite restriction on (Aw0)^perp.

In any fixed smooth angular chart centered at w0, write H_T for that restricted Hessian. The pressure is C^(2,alpha), its gradient is zero at w0, and (5) holds. Taylor's theorem gives on a full disk

    h(z)=Q(z)+O(|z|^(2+alpha)),
    grad h(z)=grad Q(z)+O(|z|^(1+alpha)),
    Q(z)=z^T H_T z/2.                            (7)

The chart's quadratic correction contributes nothing to H_T because the ambient gradient vanishes. The velocity square contributes orders 2+2alpha and 1+2alpha, which are smaller than the respective errors in (7). This is a C1-controlled expansion; it does not assert that h is C2 on the disk.

## 5. Sublevel estimates requiring only that expansion

For any nondegenerate indefinite quadratic form Q on R2, q0(theta)=Q(cos theta,sin theta) has four distinct simple zeros. Choose disjoint small arcs around them where |q0'|>=m1>0 and where its sign is fixed. On the complement |q0|>=m0>0. By (7), uniformly in theta,

    r^(-2)h(r cos theta,r sin theta)=q0(theta)+O(r^alpha),
    r^(-2)partial_theta h(r cos theta,r sin theta)
                                    =q0'(theta)+O(r^alpha).

Shrink the fixed radius R so these errors are at most half the two lower bounds. Choose C_*>0 so that epsilon/r^2<m0/2 whenever r>=C_*sqrt(epsilon). On those radii the sublevel |h|<epsilon is contained in the four arcs. Monotonicity on each arc bounds its angular length by 4epsilon/(m1 r^2). The central disk has area O(epsilon). Integrating the remaining angular lengths against r dr yields

    area_{|z|<R}{|h|<epsilon}
        <=C epsilon(1+|log epsilon|).             (8)

The same bound holds for sphere area since the chart density is bounded. When C_*sqrt(epsilon)>=R, enlarge C to cover the finite remaining epsilon range. Since G is bounded, (8) with epsilon=C2 tau^q gives local joint mass O(tau^q(1+|log tau|))=o(tau). Only q>1 is needed at this step.

If instead S(w0)=0 and grad S(w0)!=0, its angular gradient is nonzero: by X.S=0, a nonzero radial gradient would have nonzero dot product with Aw0. A C1 submersion chart therefore gives area{|h|<epsilon}<=C epsilon locally and local joint mass O(tau^q)=o(tau). This estimate needs no quadratic expansion.

## 6. Exhausting the other angular configurations

At a point outside supp G the integrand is zero on a neighborhood. At a point where K or h is nonzero, the joint sublevel is empty locally for small tau. Consider a supported joint zero K=h=0. By (N), G=0 there.

If V!=0, (1) gives grad k=-aV!=0, and its angular projection is nonzero by X.k=0 and w.Aw=c>0. In a local bi-Lipschitz C1 chart (K,s), condition (N) makes G zero on the whole local curve K=0. Holder continuity gives |G|<=C|K|^alpha. Integration in the chart yields local mass O(tau^(1+alpha)).

If V=0 and DV!=0, the confirmed nodal saddle passage A832 applies. Its exact assumptions are twisted homogeneity, C^(1,alpha) velocity, divergence and helicity zero, and (N). They all hold here. In its C1 coordinates (u,v), with bounded coordinate Jacobians,

    m|uv|<=|K|<=M|uv|,
    |G|<=C min(|u|,|v|)^alpha.                   (9)

For clarity, this input does not differentiate dK or use a Morse lemma. The associated C^(1,alpha) angular field has a hyperbolic saddle. Its C1 stable and unstable graphs straighten to the coordinate axes. Their passage equations are u'=u(nu+e1), v'=v(-nu+e2), with |e_i|<=C(|u|+|v|)^alpha. The integral of this error on every local passage is uniformly bounded. Both K and uv consequently have bounded multiplicative changes along the passage, and a fixed incoming transversal where dK!=0 gives the first comparison in (9). The axes carry K=G=0, giving the second. This is the complete mechanism of the cited input, whose proof has been reread.

To check its integral consequence, split a quadrant into u<=v and v<=u. On the first part integrate u^alpha for 0<u<min(v,C tau/v), then integrate in v. The pieces v<=sqrt(C tau) and v>=sqrt(C tau) each give O(tau^(1+alpha/2)). Reflecting and exchanging coordinates proves local mass o(tau). The extra h restriction can only decrease it.

The only remaining case is a supported joint zero with V=DV=0. If T2 is empty, (6) implies either grad S!=0 or D2P2!=0. In the second case, if the gradient is zero, Section4 gives exactly the nonsingular indefinite angular quadratic form. Section5 therefore gives o(tau) in either case.

A finite subcover of the compact sphere now supplies J(tau)=o(tau), contradicting (4). Thus T2 is nonempty. Its compactness follows from continuity of V,DV,P2,grad P2,D2P2 and closedness of supp G.

## 7. Dependencies, verdict scope and verification

The proof uses the actual-tail regularity and transports, A360/A705-A708 for almost-everywhere arrival and partial volume preservation, A963 only for the optional equivalence of (N), and A832 for the nonflat nodal saddle. The local pressure-jet calculation, the polar sublevel estimate and the compact localization are all proved above. No external Morse or unique-continuation theorem is added.

The pass criterion is a valid o(tau) local mass bound at every supported joint zero with a nonzero first or second pressure jet, under the explicit (N) premise. Sections4-6 meet that criterion with the available regularity. No computation or formal build is needed. The entire seven-section source and the entire independent proof were read and compared before the ledger verdict was finalized.

A flat second pressure jet is compatible with the pressure Poisson equation at a flat velocity zero; its source is already zero there. No third pressure derivative, exclusion of T2, disappearance of the open zero piece, automatic (N), or removal of helicity and derivative assumptions is established. The general common-zero theorem A1057 has no (N) premise, but its conclusion is weaker. Neither theorem subsumes the other by silently adding or removing that premise.

The source is the literature agent the second model/the external referee (a second model) agent. A focused comparison through the existing configured model agents remains pending, with provider runtime unattested. This audit does not count a request as a completed model review. Source snapshots and hashes are retained in verification; no new client, agent or remote computation is used.
