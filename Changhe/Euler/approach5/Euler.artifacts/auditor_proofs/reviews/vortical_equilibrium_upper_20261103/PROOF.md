# The upper vortical-equilibrium range is impossible

Status: A496 CONFIRMED after full independent reconstruction and full postwrite reading of every argument, including the local contraction lemma. The lower vortical range and irrotational equilibria are not excluded here.

## 1. Exact statement and confirmed inputs

Let0<c<1/2,omega be any finite real number,J(y1,y2,y3)=(-y2,y1,0),A=cI-omega J,a=1-2c>0,kappa=1+c. Suppose U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U(y)=o(|y|) uniformly, U.curl U=0 everywhere.

Write B=Ay+U,W=curl U,H=P+|U|^2/2+(Ay).U,g=U.B. At a vortical carrier equilibrium p, B(p)=0,W(p)!=0, A468 gives a real rho with

    spec DB(p)={rho,kappa,-a-rho}.

The assertion is rho<=-a. Thus the bad upper vortical range rho>=a is empty in this entire helicity-free uniformly sublinear class. Neither U->0 nor bounded DU is assumed. The lower bad range rho<=-2a, nonzero irrotational carrier equilibria and flat periodic witnesses remain open. This is not profile nonexistence or unconditional C2 basin coverage.

The exact inputs are A413, dH wedge dg=0 on{W!=0}; A468, the displayed spectrum, DB(p)W(p)=kappa W(p) and dg(p)=-(rho/a)dH(p); and A478, an equilibrium with U=0 in closure{W!=0} has an irrotational neighborhood. The full equation gives

    dH=(-aU+B cross W)^flat, BH=-ag, WH=0,
    [B,W]=-kappa W, div B=3c,
    d(U^flat)=i_W vol.

The actual pressure is used. Momentum gives grad P in C1 and hence H in C2; g is C2 and all one-forms below are C1. No extra pressure gauge is imposed.

## 2. Completeness and the regular level

Uniform sublinearity makes |B(y)|<=C(1+|y|), so its C1 flow Phi_t is complete for all real times. For some R0, y.B(y)>=c|y|^2/2 when |y|>=R0. Every backward orbit stays in the ball of radius max(R0,|y|), because the backward vector field points into its boundary. This proves bounded past without any derivative bound.

At a vortical equilibrium, A478 rules out U(p)=0, so dH(p)=-aU(p)^flat is nonzero. Let M be the connected component through p of

    {H=H(p), dH!=0, W!=0}.

It is an embedded C2 regular level surface. In a neighborhood of every one of its points, rank gives dg=m dH with m in C1. Differentiating gives dm wedge dH=0, so both g and m are locally constant along each connected regular level. On M, therefore,

    g=0, m=-rho/a, dg=-(rho/a)dH.                    (1)

The last constant follows by evaluating at p. Both B and W are tangent to M. For B, finite-time invariance needs justification since M need not be closed. In each regular chart, g is a C2 function of H, and the scalar ODE H'=-ag(H) preserves H(p). Along an orbit in M,

    Phi_t^*dH=e^(rho t)dH.                         (2)

This follows from L_B dH=d(BH)=-a dg=rho dH. The invertible finite-time derivative flow prevents dH from vanishing at a finite limiting endpoint; the Cauchy law prevents W from vanishing there. Completeness and local continuation therefore extend the orbit inside this same component for every finite positive or negative time.

## 3. A globally contracting conormal

Put alpha=U^flat and

    beta=alpha+dH/a=(B cross W)^flat/a.

Cartan's formula and the exact identities yield

    L_B alpha=dg-(B cross W)^flat=dg-dH-a alpha,
    L_B beta=-a beta, Phi_t^*beta=e^(-at)beta.       (3)

Moreover beta(B)=beta(W)=0, d beta=i_W vol, and L_W beta=0. The last equality follows from beta(W)=0 and i_W i_W vol=0. In particular beta wedge d beta=0. Where B,W are independent, their span is exactly ker beta.

These identities need only C1 one-forms. Local charts for this plane field can be constructed directly from B and W: if gamma(z) is a transverse C1 curve, the map

    (t,s,z) -> Phi_t Theta_s gamma(z)

is C1 and locally invertible, since its first two derivatives span B,W by the Cauchy law. Here Theta denotes the local W flow; global completeness of W is not needed. In each such box, beta=f dz with f continuous, bounded above and away from0 after the box is reduced. These boxes suffice for the contraction argument below; no stronger Frobenius regularity is imported.

On M, U is normal. Where B,W are independent, this follows from U.B=U.W=0. Where they are dependent, the Lamb identity gives dH=-aU^flat directly. Hence

    alpha=lambda dH, beta=k dH,
    k=lambda+1/a, U=(k-1/a)grad H.

The coefficient k is C1 on M and k(p)=0. Equations(2)-(3) imply

    k(Phi_t q)=e^(mu t)k(q), mu=-a-rho.             (4)

If mu!=0, k has nonzero differential along M at p. Indeed differentiation of beta=k dH, using B(p)=0,k(p)=0, gives

    d_M k(p)(v)dH(p)=(DB(p)v cross W(p))^flat/a.    (5)

The tangent plane is invariant under DB(p). Its W direction has eigenvalue kappa; its quotient by that line has eigenvalue mu. For any tangent v independent of W(p), DB(p)v-mu v is parallel to W(p), so the right side of(5) is nonzero if mu!=0. This argument also covers mu=kappa and needs no diagonalizability. Thus k is not identically zero on any neighborhood of p in M.

## 4. The local contraction lemma, including its uniform constants

Let X be a complete C1 vector field with flow F_t, and eta a C1 one-form with eta(X)=0 and F_t^*eta=e^(-at)eta,a>0. Suppose a compact full-flow-invariant set K has eta!=0. Let C be a closed full-flow-invariant set containing K that, near K, is a union of full local plaques of ker eta. Suppose this distribution has the C1 boxes described above. Then

    dist(F_(-t)x,K)->0 as t->infinity implies x in C. (6)

To prove this, take finitely many nested boxes about K. In every larger box eta=f dz with uniform0<m<=|f|<=M and uniform Lipschitz bounds on coordinates and their inverse. Choose smaller and intermediate boxes whose closures lie inside the next ones. Their distances to the next boundaries have a positive minimum.

For x sufficiently close to K, a nearest point y of the closed set C exists and satisfies |x-y|=dist(x,C)<=dist(x,K). Both lie in a common intermediate source box. Replace y by the point y' of its plaque with x's two tangential coordinates. Since C contains the full plaque, y' lies in C. A transverse coordinate segment gamma from x to y' stays in the larger box and has

    integral_gamma |eta|<=C1 dist(x,C).             (7)

The constant depends only on the finite boxes. Its length is also bounded by a fixed multiple of dist(x,C).

Fix T>0. Compactness and invariance of K, plus continuity of F_T on a neighborhood of K, give a sufficiently small neighborhood N_T of K so that each image F_T gamma lies in one destination larger box and both its endpoints lie in an intermediate box there. To see uniformity, for every z in K choose a smaller destination box containing F_T z; finitely many source neighborhoods cover K. Shrinking N_T and the source segment lengths ensures this condition. The allowable N_T may shrink with T, which is harmless.

The endpoint F_T y' lies in C. Inside the destination box, moving in its plaque to the tangential coordinates of F_T x shows

    dist(F_T x,C)<=C2 integral_(F_T gamma)|eta|
                 =C2 e^(-aT) integral_gamma|eta|
                 <=C0 e^(-aT)dist(x,C), x in N_T. (8)

Here C2 uses only the same finite coordinate bounds and m; it is independent of T. The curve need not be straight: its change of z is bounded by m^-1 times the integral. The plaque move stays in the larger box by the intermediate margin. Thus C0 is independent of T, while N_T need not be.

Choose one fixed T with theta=C0 e^(-aT)<1. If the backward orbit approaches K, choose x0=F_(-t0)x so its entire earlier orbit lies in N_T. Iterating(8) from F_(-nT)x0 to x0 gives

    dist(x0,C)<=theta^n dist(F_(-nT)x0,C)->0.

The rightmost distances are bounded since they are at most the distances to compact K and tend to0. Closedness gives x0 in C, and invariance gives x in C. No compactness of C, global product structure, or uniform-in-T flow derivative bound is assumed.

## 5. Excluding mu<0

Assume rho>-a, equivalently mu<0. By(5), choose any q in M close to p with k(q)!=0. A stable-manifold construction is unnecessary: every backward carrier orbit is bounded, and(4) already gives |k(Phi_(-t)q)|->infinity. On that bounded orbit U is bounded by local continuity, so U=(k-1/a)grad H gives dH->0. Equation(1) gives dg->0 as well.

Its alpha-limit K is nonempty, compact, invariant under every finite B time, and the full backward orbit approaches K. On K,

    H=H(p), g=0, dH=dg=0, aU=B cross W.             (9)

If W vanishes at r in K, its entire carrier orbit has W=0 by the linear Cauchy transport law. By(9), U=0 there; hence the orbit solves y'=Ay and has radius e^(ct)|r|. Compact invariance forces r=0. But then B(0)=U(0)=0 and0 is in closure{W!=0}, because it is a limit of the vortical q orbit. A478 supplies an irrotational neighborhood, contradicting this limit. Therefore W has no zeros on K.

If B and W are dependent at a point of K, the dependence persists under the derivative flow, because both are transported by DPhi_t and W has only the additional nonzero scalar factor e^(-kappa t). Again(9) makes U=0 along the full orbit, forcing the same impossible origin. Thus beta is nonzero everywhere on K.

Let C be the closure of the union of all maximal W-orbits meeting K. Since WH=0, local W flow preserves dH, so this saturation lies in Crit(H). Also

    -a Wg=W(BH)=[W,B]H+B(WH)=kappa WH=0,

and it preserves Crit(g). Thus C is a closed subset of Crit(H) intersect Crit(g). It need not be bounded. The Cauchy conjugation of the local W flow by the complete B flow, with vortex time rescaled by e^(kappa t), maps maximal W-orbits onto maximal W-orbits. Since K is B-invariant, C is B-invariant. Continuity of local W flow makes its closure locally W-invariant as well.

Near K, B,W are independent and span ker beta. In each chart from Section3, C contains the full connected plaque through any of its points: successive small B and W flows cover the plaque, and closedness gives extension to its chart boundary. Thus all hypotheses of Section4 hold with eta=beta and X=B. The backward orbit of q approaches K, so q belongs to C. But C lies in Crit(H) and q belongs to M, where dH!=0. This contradiction proves rho<=-a.

## 6. Scope and comparison record

The argument does not use compactness of the full W-saturation. It uses only finite regular boxes about its compact invariant subset K. It also does not use the local stable curve; the regular level, nonzero k near p and boundedness of all backward orbits suffice. These observations independently resolve the precise gap identified in Theory Agent C's W1 notes.

The complete415-line coordinator source and66-line coordinator check were read. The original source calls its model consultation failed and the coordinator checked its main exclusion afterward. The independent audit certifies only Sections1-5 above, not every negative-range geometric assertion in that source. Existing coordinator and Theory Agent C configurations are the primary model; this is configuration evidence, not provider runtime attestation. No new model client or computation is used. All conclusions hold for each fixed arbitrary omega, with no uniform parameter estimates claimed.
