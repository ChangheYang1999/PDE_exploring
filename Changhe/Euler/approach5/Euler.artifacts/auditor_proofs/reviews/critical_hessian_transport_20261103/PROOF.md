# Hessian transport on noninterior critical leaves

Status: LIT192 and LIT193 CONFIRMED at their actual-profile scope. The stronger conclusion in Section 8 puts the entire backward carrier limit set in the simultaneous second-order-flat set. General critical-node exclusion remains OPEN.

## 1. Statement and notation

Fix 2/5<c<1/2 and any finite real omega. Let Jx=(-x2,x1,0), A=cI-omega J, a=1-2c and p=(1-c)/c. Assume U in C2(R3;R3), P in C1(R3) and a finite constant C satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Put B=Ax+U, Omega=curl U and use their complete flows Phi and Gamma. Normalize the pressure by its established far-field constant Pinf, and define

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2.

The equation makes P, and hence H,Q, C2. Let E be the forward escaping set of B, Xi:E->R3 minus {0} its C1 scattering diffeomorphism, V the actual velocity tail, k(z)=(Az).V(z), O the saturation of E by the complete Omega flow, and L the C1 transported extension of k composed with Xi to O. These are the actual-profile constructions, not freely specified tail fields.

Suppose y0 in O has Omega(y0)!=0, L(y0)=0 and is not interior to {L=0}. Let N be its joint B,Omega orbit and Cbar its ambient closure. Then:

1. At each y in Cbar with D2H(y)!=0 there is mu(y) in [0,1] such that D2Q(y)=mu(y)D2H(y).
2. D2H(y)=0 implies D2Q(y)=0 on Cbar. Simultaneous vanishing is invariant under both complete flows.
3. For every y in Cbar the entire backward carrier limit set alpha_B(y) consists of simultaneous-flat points. Consequently Cbar contains at least one full immersed joint plane on which H=Q=dH=dQ=D2H=D2Q=0.

For the quantitative form, write uniquely on Cbar

    D2H=h U U^T, D2Q=q U U^T,
    h=Delta H/|U|^2, q=Delta Q/|U|^2.

If h(y)!=0, its sign persists along Phi and, for every t<=0,

    exp(2at)|h(y)| <= |h(Phi_t y)| <= exp(at)|h(y)|.

If h(y)=0, both coefficients remain zero on its full joint leaf. All constants in the hypotheses and local estimates may depend on the profile,c,omega; no rotation-independent numerical constant is asserted. Properness, finite surface area and existence of an exhaustion with vanishing Stokes boundary terms are not conclusions.

## 2. Checked dependencies

A897 and its finite-Gamma transfer A934 give dL=0 at every initial point under consideration. C44, independently reconstructed in auditor_proofs/reviews/critical_joint_closure_20261103/PROOF.md (A936-A941), gives on the entire ambient closure

    Cbar subset O, H=Q=0, dH=dQ=0,
    aU=B cross Omega!=0,
    D2H and D2Q are multiples of U U^T,
    L=dL=0, with no point interior to {L=0}.

Every joint leaf in Cbar is intrinsically a plane. The closure conclusion is invoked before using continuity of L there. The flows preserve Cbar. The exact identities used below are

    BH=-a(H-Q), BL=-aL,
    Omega H=Omega Q=Omega L=0,
    dQ wedge dH=dL wedge dH=0 on the open vortical set,
    D Phi_t(y)^T U(Phi_t y)=exp(-at)U(y).

The rank identities are A786-A789/A810-A814 at this scope. A538 supplies V locally C^(1,alpha) for every alpha<1 under the natural full-gradient bound above. Its full independent moving-cutoff proof was reread: it uses local physical-Euler W^(2,q) bounds for every finite q and compact embedding, and does not assume a C2 tail.

The elementary compact-plaque argument in Section 3 is also a separate verification of LIT192. It uses only the C44 closure conclusions and the confirmed affine-leaf classification A143, not LIT193 or the stronger transport result.

## 3. Independent verification of LIT192

At z in Cbar with D2H(z)!=0, choose a fixed Euclidean vector n such that D2H(z)n!=0. The C1 scalar f=n.grad H has a nonzero differential at z, so its local zero set is a single C1 embedded surface S. All critical points of H are in S. The rank-two local joint plaque through z lies in Crit(H), has tangent plane ker D2H(z), and fills an open neighborhood of z in S by the two-dimensional inverse-function theorem. Shrink the ambient box to that neighborhood. Its critical set is exactly this one plaque.

Since z belongs to the ambient closure of N, some point of N lies in this box. It is on the plaque through z, so z and that point are on the same joint orbit. Thus z belongs to N. Smaller closed plaques in the box are compact in the intrinsic topology of N. All critical points in the smaller box lie in those plaques; multiple remote sheets cannot enter the box.

The backward carrier orbit through a point of N is bounded by the outward radial drift at infinity. Its nonempty compact ambient limit set K0 lies in Cbar. If D2H were nonzero at every point of K0, finitely many of the smaller boxes would cover K0. The backward orbit eventually lies in their union, since otherwise a bounded subsequence outside the union would give another backward limit point. Being critical for H, that tail then lies in a finite union of intrinsically compact plaques of N.

On an intrinsic plane leaf there are global coordinates (theta,zeta) with B=partial_theta+(1+c)zeta partial_zeta and Omega=partial_zeta. Hence theta(Phi_(-t)y)=theta(y)-t, contradicting intrinsic compactness. Therefore some point of K0 has D2H=0. If y0 is in O rather than E, it is still backward bounded and the same argument applies. The additional closure hypotheses in the submitted LIT192 are supplied by C44 and need not remain extra assumptions in this application.

## 4. Pointwise regularity of the transported scalar

At a critical zero z of k, the actual C^(1,alpha) regularity gives

    |k(z+v)|<=C_(z,alpha)|v|^(1+alpha)

for every alpha<1 on a sufficiently small ball. If y in Cbar intersect E, dL(y)=0 and invertibility of D Xi imply dk(Xi y)=0. Local Lipschitz continuity of Xi transfers this estimate to

    |L(y+v)|<=C_(y,alpha)|v|^(1+alpha).                 (1)

For any other y in Cbar, choose a finite Gamma map carrying y to E. It preserves L and is a C1 local diffeomorphism, so it transfers the same pointwise estimate. No Holder estimate for DL on all of O is inferred from this composition. Estimate (1) at the individual critical point is sufficient.

## 5. Normal Hessian comparison

Let y in Cbar with D2H(y)!=0. The critical plaque from Section 3 is a C1 graph u=j(v) in Euclidean coordinates with transverse coordinate u. Its H value and first derivatives vanish. Shrinking the chart makes H_uu have one strict sign. Taylor's formula in u gives

    |H(v,u)| comparable to |u-j(v)|^2,

and H has a fixed sign on both sides, with H_u nonzero off the plaque. Small nonzero H-levels on either side are connected graphs over a smaller tangential ball. The rank identities imply Q=q_side(H) and L=l_side(H) on each such side, with C1 scalar functions away from zero.

Every L-zero off the plaque is interior to {L=0}: it is vortical and regular for H, and the checked regular-H trichotomy A922 allows a noninterior zero there only at H=Q=0. Here H is nonzero. Thus the zero set is both open and closed on each connected side. On each side L is either identically zero or nowhere zero. At least one side is nowhere zero, since y is noninterior and L=0 on the plaque.

Use that side and put eta=H. Along a fixed transverse line through y, C2 Taylor expansion, the common normal direction of the Hessians, and (1) give

    q_side(eta)/eta -> mu=Delta Q(y)/Delta H(y),
    |l_side(eta)|<=C_alpha |eta|^((1+alpha)/2).          (2)

The exact equations BH=-a(H-Q), BL=-aL yield

    l_side(eta)=(eta-q_side(eta))l_side'(eta).

The factor eta-q_side cannot vanish on the chosen nowhere-zero side. With x=|eta| and the sign absorbed into q_side, this becomes

    d log|ell(x)|/dx=1/(x-qtilde(x)), qtilde(x)/x->mu.  (3)

If mu<0, choose beta strictly between 1/(1-mu) and 1. For small x, the positive right side of (3) is at most beta/x. Integration to a fixed x1 gives |ell(x)|>=C x^beta. Choosing alpha<1 with (1+alpha)/2>beta contradicts (2). If mu>1, the right side of (3) is at most -gamma/x for some gamma>0, forcing |ell(x)|>=C x^(-gamma), contrary to continuity at zero. Hence 0<=mu<=1. Both Hessians have the same rank-one normal direction, so D2Q=mu D2H. The endpoint values are not excluded.

## 6. Integrated Hessian transport at C2 regularity

Along the carrier orbit through y in Cbar define

    F(t)=D Phi_t(y)^T D2H(Phi_t y) D Phi_t(y),
    K(t)=D Phi_t(y)^T D2Q(Phi_t y) D Phi_t(y).

Twice differentiate in the initial point the integrated identity

    H composed with Phi_t-H=-a integral_0^t (H-Q) composed with Phi_s ds.

All relevant functions and the B flow are C2. The terms involving D2 Phi vanish because dH=dQ=0 along the orbit. Differentiation under a finite-time integral is justified by continuous second derivatives on the compact local flow tube. Thus F,K are continuous and

    F'(t)=-aF(t)+aK(t).                                (4)

This does not differentiate D2H spatially or assume H in C3.

If F(0)=0 and K(0)!=0, equation (4) gives F(t)=atK(0)+o(t), nonzero for sufficiently small nonzero t. Section 5 then gives K(t)=mu(t)F(t) with 0<=mu(t)<=1. The inequality ||K(t)||<=||F(t)|| contradicts K(t)->K(0)!=0 and F(t)->0. Thus F(0)=0 forces K(0)=0. Consequently ||K(t)||<=||F(t)|| at every time. Gronwall applied to (4), in either time direction, proves that F(0)=0 implies F=K=0 along the entire carrier orbit.

## 7. Vortex invariance without a C2 vortex flow

H and Q are invariant under Gamma. At a critical point y, compose the second-order Taylor expansion of either scalar with

    Gamma_s(y+v)=Gamma_s(y)+D Gamma_s(y)v+o(|v|).

The vanishing first derivative removes the linear remainder. Therefore

    D2H(y)=D Gamma_s(y)^T D2H(Gamma_s y) D Gamma_s(y),

and the same holds for Q. Invertibility of D Gamma preserves Hessian vanishing. This uses only the C1 Omega flow, which follows from U in C2. Together with Section 6 it proves joint invariance. Combined with Section 3 it already verifies the precise accumulation corollary of LIT193.

## 8. Stronger decay toward the entire backward limit set

The Kelvin identity and D2H=h U U^T give exactly

    F(t)=exp(-2at)h(Phi_t y) U(y)U(y)^T,
    K(t)=exp(-2at)q(Phi_t y) U(y)U(y)^T.

The normal velocity never vanishes on Cbar, so both coefficients are continuous and equation (4) shows h(Phi_t y) is C1 in t, with

    d/dt h(Phi_t y)=a(h+q)(Phi_t y).                    (5)

Where h is nonzero, q/h=mu is in [0,1]. Section 6 prevents a nonzero h from reaching zero in finite time. Hence

    a <= d/dt log|h(Phi_t y)| <= 2a.

Integration gives the quantitative bounds in Section 1. If h(y)=0, Section 6 gives the same upper bound trivially. Since U is bounded, for t<=0

    ||D2H(Phi_t y)||+||D2Q(Phi_t y)||
       <=2 ||U||_infinity^2 |h(y)| exp(at).             (6)

Every backward carrier orbit here is bounded, so any point in alpha_B(y) is a finite ambient subsequential limit. Continuity of both Hessians and (6) give simultaneous flatness at every such point. Their joint saturation stays in Cbar by invariance and consists of complete immersed plane leaves by C44/A941. This stronger conclusion does not use the compact-plaque proof in Section 3; it follows directly from the verified ratio, Hessian transport and Kelvin law.

## 9. What remains open

Second-order flatness on an immersed plane does not provide a proper surface, finite area, surfacewise recurrence, or vanishing boundary circulation on an exhaustion. Even a compact ambient backward limit set may have an unbounded joint saturation. No Stokes integral over such an uncontrolled plane is taken here. A ratio in [0,1] also does not make Delta Q nonnegative when Delta H is negative. Open L-zero regions are outside the noninterior theorem. Global zero helicity and natural full-gradient decay remain hypotheses, so none of these conclusions closes the bare-decay conjecture.

## 10. Verification evidence

Both complete submitted proofs, the full independent C44 reconstruction, the full A538 reconstruction and the relevant source C44 Remark53 were read. All calculations above were checked analytically; no numerical computation, remote client, formal build or server was required. Source hashes and actual review timestamps are in the team records. The existing configured model agents are the collaboration route; a focused comparison of Section 8 is requested through working files, not represented as already received. Provider runtime is not independently attested.
