# Higher scalar jets on the compact critical limit set

Status: LIT194 CONFIRMED A966-A969 after complete source and independent proof postreads. The normalized transport strengthens the source conclusion to every point of the compact limit set. The proof does not use the stronger C2 exclusion A963.

## 1. Exact hypotheses and statements

Fix an integer r>=2, 2/5<c<1/2 and any finite real omega. Put Jx=(-x2,x1,0), A=cI-omega J, a=1-2c>0, kappa=1+c and p=(1-c)/c. Let U in C^r(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

with finite C. The equation gives P in C^r. Use B=Ax+U, Omega=curl U, the complete flows Phi,Gamma, the canonical pressure constant Pinf, and

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2.

Let O be the Gamma saturation of the forward escaping set, and let L in C1(O) be the established transported scalar. Suppose y0 in O is a vortical zero of L that is not interior to {L=0}. Let C0 be the ambient closure of its full joint leaf, and K0=alpha_B(y0).

For 2<=m<=r, let C_(m-1) be the points of C0 at which all H and Q derivatives of orders 0 through m-1 vanish. Inductively this is a closed jointly invariant set. At a point in it, both m-th derivative tensors are multiples of the m-fold tensor power of U. Where D^m H is nonzero,

    D^m Q=mu D^m H,   1-m/2<=mu<=1.                    (1)

Where D^m H=0, D^m Q=0 too. The simultaneous vanishing sets C_m are closed and invariant under both flows.

LIT194 concludes that K0 intersects every C_m, and for smooth U contains an infinitely flat point of both H and Q. A stronger conclusion holds: K0 is contained in every C_m available at the stated regularity. Thus every point of K0, and every joint leaf through it, has all those jets zero. If U is globally real analytic, the proposed y0 cannot exist.

These are conditional implications about the proposed critical configuration. A963 already excludes it under the C2 version of the same hypotheses. The present proof deliberately does not use A963, so the higher-order mechanism and the analytic consequence are checked on their own. Neither argument removes global zero helicity or natural gradient decay.

## 2. First-order inputs and local scalar coordinates

The confirmed A897 and A936-A941 give throughout C0

    L=dL=H=dH=Q=dQ=0,
    aU=B cross Omega!=0,
    Phi_t^*(U.dx)=exp(-at)U.dx,
    BH=-a(H-Q), BL=-aL,
    Omega H=Omega Q=Omega L=0.

The set C0 lies in O, is closed and invariant under both flows, and contains only noninterior zeros of L. Its joint leaves are intrinsic affine planes, without a claim of properness. Their global affine coordinate theta satisfies theta(Phi_t x)=theta(x)+t. The set K0 is nonempty, compact and invariant under Phi.

On the open vortical set the rank identities dQ wedge dH=dL wedge dH=0 hold. The regular-H trichotomy A922 says that a vortical zero of L with dH!=0 is either an interior zero, or has H=Q=0 and dL=dH!=0. In particular, in a region where H!=0 and dH!=0, every zero of L is interior.

A538 and its locally Lipschitz transfer, checked in A955, give at each y in C0 the pointwise estimate

    |L(y+v)|<=C_(y,alpha)|v|^(1+alpha),  alpha<1.       (2)

This does not assert Holder continuity of DL in a neighborhood, and uses only C1 scattering and finite vortex maps.

## 3. Normal tensors and the ratio bounds

Suppose C_(m-1) is jointly invariant and y lies in it. Each component of D^(m-1)H is zero along both the B and Omega curves through y. Differentiating along them makes D^m H annihilate B and Omega in one slot. Symmetry then gives annihilation in any slot. The same applies to Q. Since these two tangent vectors are independent, both tensors are pure powers of the normal covector U.

Assume D^m H(y)!=0, and choose a fixed transverse vector n such that D^m H(y)[n,...,n]!=0. The C1 function f=D^(m-1)H[n,...,n] has nonzero gradient at y. Its zero set is one local C1 surface. The rank-two joint plaque through y lies in that surface, and its local parametrization has full tangent rank. The inverse-function theorem on the surface shows that it fills a smaller local surface patch. All lower H and Q derivatives vanish on this patch.

Write the surface as u=j(v) in fixed transverse linear coordinates. Shrink the box so that the m-th transverse H derivative stays nonzero with one sign. Taylor expansion from the surface gives, on each punctured side,

    |H(v,u)| comparable to |u-j(v)|^m,
    |partial_u H(v,u)| comparable to |u-j(v)|^(m-1).    (3)

Small admissible nonzero H levels on either side are connected graphs over a smaller tangential ball. The rank identities therefore give Q=q(H) and L=l(H), separately on each side, with q,l C1 away from zero. The scalar transport implies

    l(eta)=(eta-q(eta))l'(eta).                         (4)

The zero set of L on either connected punctured side is relatively closed by continuity and relatively open by the regular-H trichotomy, since H!=0 there. Each side is thus identically zero or nowhere zero in L. If both sides were zero, their union with the plaque would be a zero neighborhood of y. Hence at least one side has l nowhere zero.

Along a fixed transverse line, the Taylor expansion at y and (2)-(3) yield

    q(eta)/eta -> mu,
    |l(eta)|<=C_alpha|eta|^((1+alpha)/m),               (5)

where mu is the ratio of the two pure normal tensors. This applies for even or odd m; choose the sign of the admissible H values on the chosen side. With x=|eta|, equation (4) becomes

    d log|ell(x)|/dx=1/(x-qtilde(x)),
    qtilde(x)/x -> mu.                                 (6)

If mu<1-m/2, choose beta satisfying 1/(1-mu)<beta<2/m. For small x the right side of (6) is positive and at most beta/x. Integration from x to a fixed positive x1 gives |ell(x)|>=C x^beta. Choose alpha<1 with (1+alpha)/m>beta; this contradicts (5). If mu>1, the right side of (6) is at most -gamma/x for some gamma>0, giving |ell(x)|>=C x^(-gamma), contrary to continuity at zero. Thus (1) holds, including its non-strict endpoints.

With M_m=max(1,m/2-1), this proves

    ||D^m Q||<=M_m||D^m H||                            (7)

where the H tensor is nonzero. No sign for Delta Q follows in general; at m=2 its sign may match a negative Delta H.

## 4. Integrated top-jet transport and joint invariance

Fix y in C_(m-1) and pull back the m-tensors by applying D Phi_t in every slot. Denote the resulting tensors at y by F(t),G(t), respectively. Differentiate m times in the initial point the integrated identity

    H(Phi_t z)-H(z)=-a integral_0^t (H-Q)(Phi_s z) ds.

Along the orbit in C_(m-1), every lower scalar derivative is zero, so all chain-rule terms containing a higher derivative of the flow disappear. Since H,Q and Phi_t are C^m, the differentiation under a finite time integral is valid and gives

    F'(t)=-aF(t)+aG(t).                                (8)

It requires no (m+1)-st scalar derivative.

If F(0)=0 but G(0)!=0, then F(t)=atG(0)+o(t), so F(t)!=0 for sufficiently small nonzero t. Applying (7) after pullback gives ||G(t)||<=M_m||F(t)||, contradicting continuity at zero. Here pullback preserves the scalar proportionality exactly; no comparison of two arbitrary tensor norms through different maps is being assumed. Thus F=0 forces G=0, and (7) applies at every time. The differential inequality from (8) and two-sided Gronwall show that F(0)=0 forces F=G=0 for all real times. This proves Phi invariance of C_m.

For Gamma invariance, use H composed with Gamma_s=H and Q composed with Gamma_s=Q. Both endpoints lie in C_(m-1), where all lower scalar jets vanish. The m-th order Taylor formula for H and Q, composed with the first-order expansion Gamma_s(y+v)=Gamma_s(y)+D Gamma_s(y)v+o(|v|), therefore gives congruence of the top m-tensors. Invertibility of D Gamma_s proves invariance. C1 regularity of this map suffices even when m>2, because all lower jets are zero. Closedness follows from continuity of the scalar derivatives.

## 5. The source's compact-plaque degeneration argument

For completeness, the geometric induction in LIT194 also passes. Choose z in K0 intersect C_(m-1). The closure of its joint leaf N_z lies in C_(m-1), and its compact backward limit K lies in K0 intersect C_(m-1). Suppose D^m H is nonzero everywhere on K.

At each w in K, the function f used in Section 3 has one regular zero surface. Every nearby point of C_(m-1) lies on it, and the joint plaque through w fills it after shrinking. Since N_z accumulates at w, this plaque meets N_z and belongs to that same leaf. A further smaller closed plaque patch is compact in the intrinsic leaf topology. This is a local uniqueness argument and does not assume global embeddedness or properness.

Finitely many such smaller boxes cover K. The late backward carrier tail lies in their union and in C_(m-1), hence in finitely many intrinsic compact plaque patches of N_z. Its theta coordinate would be bounded, contrary to theta(Phi_(-t)z)=theta(z)-t. Thus D^m H=0 at some point of K; Section 4 gives D^m Q=0 there too. Induction proves the finite-order source claim. For smooth U, nested nonempty compact subsets K0 intersect C_m have a nonempty intersection, supplying one infinitely flat point and its invariant joint leaf.

## 6. Stronger compact-set conclusion from normalized transport

One can avoid the geometric argument and obtain all of K0, not just one point. Suppose inductively that K0 lies in C_(m-1). On K0 write

    D^m H=h_m U tensor ... tensor U,
    D^m Q=q_m U tensor ... tensor U,

with m factors. The continuous coefficients are bounded, because K0 is compact and |U| has a positive minimum there. Kelvin transport and (8) imply, along every orbit in K0,

    d h_m(Phi_t y)/dt=a[(m-1)h_m(Phi_t y)+q_m(Phi_t y)]. (9)

Indeed the pulled-back tensors are exp(-mat)h_m(Phi_t y) and exp(-mat)q_m(Phi_t y), times the fixed nonzero tensor U(y) to the m-th power. Differentiating this expression in (8) proves (9) at the stated C^r regularity.

If h_m(y)!=0, the vanishing invariance in Section 4 prevents a zero at any finite time. Equation (1) then gives

    am/2 <= d log|h_m(Phi_t y)|/dt <= am.              (10)

The positive lower bound makes |h_m| grow at least exp(amt/2) as t tends to positive infinity. This contradicts boundedness on the compact invariant K0. Thus h_m=q_m=0 on K0. Starting with K0 contained in C1, induction gives K0 contained in every C_m up to r. If U is smooth, every point of K0 is infinitely flat in both scalars. Invariance gives the same vanishing on its full joint saturation.

The inequalities also recover the backward rate in A958 when m=2. They do not prove that every point of the entire generally noncompact C0 is flat.

## 7. Analytic consequence and scope

If U is real analytic on R3, the profile equation gives real analytic grad P, hence locally real analytic P, H and Q. At any point of K0 all Taylor coefficients of H and Q vanish by Section 6. They vanish on a neighborhood, and real analytic continuation on connected R3 gives H=Q=0 globally. In particular P-Pinf=|U|^2/2. Dotting the momentum equation with U gives

    (B+U).grad(|U|^2/2)=-(1-c)|U|^2.

The continuous decaying function |U|^2 attains a maximum. Its gradient is zero there, so the displayed identity forces the maximum to be zero. Thus U=0, contrary to the initial vortical point. The source analytic consequence is valid without any claim that L or V is analytic.

The full seven-section source LIT194 was read and each regularity, side-selection, transport, plaque and compactness step was independently reconstructed above. The theoretical pass criterion is a valid top-jet transport equation at C^r and degeneration without a properness assumption. No computation or formal build is needed. The C2 exclusion A963 is stronger than this analytic corollary and was not used in the proof. Open scalar-zero regions, flat tail-velocity zeros and the general bare-decay conjecture remain outside the conclusion.
