# Polynomial weights and homogeneous scalar rigidity

Status: CONFIRMED at the exact scopes in A608, A609. Complete independent proof postread, including the corrected zero-g sign. The unrestricted campaign conjecture remains open.

## 1. Statements and dependencies

Put D=R3 minus{0}, 1/3<c<1/2, a=1-2c, p=(1-c)/c, d=p-1=a/c in(0,1), A=cI-omega J, Jx=(-x2,x1,0), T_t=exp(tA) and Q_t=exp(omega tJ). The finite real omega is arbitrary. A local A2 weight w is positive almost everywhere; w,w^-1 are locally integrable; and the products of their averages over balls in any fixed relatively compact neighborhood are bounded.

Polynomial theorem. If P is a nonzero real polynomial of degree at most l>=1, 0<gamma<1/l, then on every positive-radius ball B in R3,

    (average_B |P|^gamma)(average_B |P|^-gamma)
       <=1+C gamma l/(1-gamma l).

One may take C=96 using the measurable-set Remez inequality, or C=48(l+1)^(1+1/l) using only elementary interpolation.

General scalar theorem. Let nu>a, beta=a/nu, and let sigma be real C1 on D, sigma(T_t x)=exp(-nu t)sigma(x). Assume w=|sigma|^beta is locally A2. Let V be C1, divergence free, and

    V(T_t x)=exp(-(1-c)t)Q_t^T V(x).

Write W=curl V, k=(Ax).V and E=grad k. If W.grad sigma=0 and E cross grad sigma=0 on ALL D, then V=0. If instead V is locally C1,alpha for every0<alpha<1 and rank is assumed only on {W!=0}, then

    W(x)!=0 implies k(x),sigma(x)!=0;
    E(x)=0 implies V(x)=0.

On each vortical component C there is one nonzero real constant d_C with k=d_C|sigma|^beta. This local conclusion does not say V=0 globally.

For the second statement the analytic dependency is the weighted completed-space and origin theorem proved in the team records, A596-A597. Its sole substantial imported regularity result is the signed weak-solution continuity theorem of Fabes, Jerison and Kenig (1982), at the precisely recorded completed energy scope. Sections4-6 below verify every change of scalar and degree. No new regularity theorem is presumed.

## 2. Two interval estimates

Let f be a polynomial of degree at most l on an interval I of length L, with M=sup_I|f|>0. The measurable-set Remez inequality says

    M<=T_l(2L/m-1) sup_F |f|

when F is measurable of length m>0. This is equation(1.1) of Y. Yomdin, Remez-Type Inequality for Discrete Sets, arXiv0911.1937v1, after affine rescaling from[-1,1]. The exact primary statement was read. Its original argument there is attributed to Remez; the inequality is imported, not reproved here. Since T_l(s)<= (2s)^l for s>=1, the sublevel F={|f|<=lambda M}, 0<lambda<=1, satisfies

    |F|<=4 lambda^(1/l)L.

If |F|=0 this is immediate. The requirement M>0 is essential and is retained.

For an independent estimate, choose l+1 points in F separated pairwise by at least delta=m/[2(l+1)]. After j<=l choices, the union of intervals of radius delta about them has measure at most2j delta<m, so a new point remains. Lagrange interpolation gives

    M<=(l+1)(L/delta)^l sup_F |f|.

Thus |F|<=C_l lambda^(1/l)L, C_l=2(l+1)^(1+1/l). This proof also holds for essential supremum after removing the exceptional null set. It does not rely on the imported Remez theorem.

## 3. Three-dimensional sublevels and A2

Let B have radius R and choose x_* in its closure with |P(x_*)|=M=sup_B|P|>0. Each ray x_*+t theta intersects the closed ball in a segment0<=t<=tau(theta)<=2R, possibly of zero length. Convexity is used here. The polynomial on every nondegenerate segment has maximum M at its initial point, so the interval bound with constant C_l applies. In polar coordinates about x_*,

    |{|P|<=lambda M} intersect B|
      <=4R^2 C_l lambda^(1/l) integral_S2 tau(theta)dtheta
      <=32pi C_l R^3 lambda^(1/l)
      =24 C_l lambda^(1/l)|B|.

The same formula with C_l=4 gives constant96. Letting lambda decrease to0 shows that the polynomial zero set is null. Put q=|P|/M, which lies in[0,1] on B. Layer cake, allowing infinity on this null set, gives

    average_B q^-gamma
       <=1+24C_l integral_1^infinity v^(-1/(gamma l))dv
       =1+24C_l gamma l/(1-gamma l).

Also average_B q^gamma<=1. Their product proves both constants in Section1 and all asserted local integrability. No lower bound on nonzero coefficients is used.

Consequently, if sigma=r^-m P on a compact annular neighborhood with r1<=r<=r2, then |sigma|^gamma is locally A2, with bound

    (r2/r1)^(m gamma)[1+C gamma l/(1-gamma l)]

when m>=0. We use this only for positive Kelvin radial exponents.

## 4. The weighted core with arbitrary scalar degree

The core needed here is this: if w is locally A2 on D, w(T_t x)=exp(-at)w(x), and Y is locally Lipschitz, divergence free, of the velocity degree in Section1, with curl(Y/w)=0 in distributions, then Y=0.

Here is the complete reduction to the previously proved analytic lemma. Since w^-1 is locally integrable, Y/w is locally L1. The distributional Poincare lemma on simply connected D gives a global W1,1_loc potential psi. Its weighted gradient energy is integral |Y|^2/w<infinity locally. The convolution bound, weighted Poincare inequality and truncation proof in A596 Section3 give both the weighted function norm and membership in the local completion of Lipschitz functions. Hence div(w grad psi)=0 in precisely the signed weak-solution space. The imported weighted continuity theorem gives a continuous representative on D.

The degree of Y/w is the covector degree T_t^-T. The weak chain rule and connectedness imply

    psi(T_t x)=psi(x)+eta t

for a real eta: the difference has zero weak gradient, and its continuous additive constant is linear in t. Compactness of the unit sphere now gives |psi(x)|<=C(1+|log r|). No zero-drift premise was inserted.

The weight has radial degree -d. Angular integrability of w and w^-1 follows from integration on one annulus and exact rotational covariance. Their integrals on a radiusR ball centered at0 are constant multiples of R^(3-d) and R^(3+d). Balls close to0 fit in a comparable concentric ball; balls farther away scale to a compact annulus. These observations, with finite-cover local A2 bounds on that annulus, give global A2 on R3.

Velocity homogeneity gives |Y|<=Cr^-p. Radial integration and the preceding angular integrals yield

    integral_(r<epsilon)|Y|^2/w=O(epsilon^(2-p)),
    integral_(r<epsilon)w psi^2
       =O(epsilon^(4-p)(1+|log epsilon|)^2).

Cutting psi off below epsilon adds weighted gradient energy at most C epsilon^(2-p)(1+|log epsilon|)^2. The ordinary weak-gradient boundary error is O(epsilon^2(1+|log epsilon|)); the divergence error for Y is O(epsilon^(2-p)). All tend to0 since p<2. Thus the function extends through0 in the completed weighted energy space, its weak derivative is Y/w, and no point source occurs. The same imported continuity theorem applies at0. Sending t to minus infinity forces eta=0 and then psi constant. This proves Y=0.

Every exponent here depends on the weight degree -a, not on nu separately. The strict p<2 hypothesis and the completed-space theorem have not been weakened.

## 5. Global rank and one component constant

Differentiate velocity homogeneity and the scalar k to obtain

    Ax cross W=aV+E, Ax.E=-ak, Ax.grad sigma=-nu sigma.

Cross the first identity with grad sigma. Where rank holds and W.grad sigma=0 this gives

    grad sigma cross V=(sigma/beta)W.

Therefore, for epsilon>0,

    curl[(sigma^2+epsilon^2)^(-beta/2)V]
      =epsilon^2(sigma^2+epsilon^2)^(-beta/2-1)W.

The right side tends to0 almost everywhere and is locally dominated by w^-1|W|. The field on the left converges locally L1 to V/w. Thus curl(V/w)=0 distributionally wherever rank holds, including scalar nodes. With global rank, the core proves V=0.

For localized rank let C be a component of {W!=0}. It is preserved by T_t because the twisted action preserves the vortical set and each time segment is connected. On C the same regularization makes G=V/w closed. Distributional homogeneity gives DG Ax=-A^T G, while closedness makes DG symmetric. Hence

    grad[(Ax).G]=A^T G+(DG)^T Ax=0.

There is one real constant d_C with k=d_C w on C, including its nodes by continuity.

If d_C=0 then k=E=0 on C. At its boundary in D, W=E=0 and the displayed cross identity makes V=0. The zero extension Y of V from C is locally Lipschitz: use the first boundary point of a line segment to bound a cross-boundary difference by the local Lipschitz bound for V. Its weak derivative is DV on C and0 almost everywhere off C; a Lipschitz function has derivative0 almost everywhere on its zero set. Thus div Y=0 and its actual curl is the continuous zero extension Z of W. Twisted homogeneity persists, and globally Ax cross Z=aY, Z.grad sigma=0. The regularized calculation gives curl(Y/w)=0. The core would give Y=0, contradicting C being vortical. Therefore d_C!=0.

## 6. Exclusion of nodes and the fixed-Holder chart version

Suppose sigma(x0)=0 inside C. There w=k/d_C is nonnegative and C1,alpha for every alpha<1. At the zero, w and its derivative vanish. A transverse two-dimensional disk to Ax0, swept out by T_t, is a smooth coordinate box. Pullback preserves local A2 since Jacobians and metric distortion are bounded. The factor exp(-at) is bounded and positive on that box; removing it leaves a weight w0 on the transverse disk, independent of t. Testing product cubes gives the two-dimensional A2 condition for w0.

Let v0=1/w0 and K its cube A2 constant. For the ring Q_r minus Q_(r/2), which has three quarters the square's area, Cauchy-Schwarz gives

    v0(Q_(r/2))<=(1-9/(16K))v0(Q_r).

Iteration yields v0(Q_r)<=Cr^delta for some delta>0. The nonnegative C1,alpha zero instead gives w0(z)<=C_alpha|z|^(1+alpha), hence v0(Q_r)>=c_alpha r^(1-alpha). Taking alpha close enough to1 contradicts the upper bound. Thus w,sigma and k are nonzero in C. If E=0 there, Ax.E=-ak gives the same contradiction. If E=W=0, the cross identity gives V=0.

C40 Lemma31 assumes only one fixed alpha, but adds a prescribed nodal chart: a surface with |sigma| comparable to rho^q and q beta<1, or a curve with q beta<1+alpha. The proof in A568 applies at this weaker regularity without changing any degree calculation. Explicitly, off the nodes rank gives k=constant times |sigma|^beta. At a surface node C1 implies |k|<=C rho, incompatible with a nonzero constant when q beta<1. At a curve node the punctured transverse chart is connected, so such a constant makes k have one sign and a local extremum; C1,alpha then gives |k|<=C rho^(1+alpha), again impossible. Constants therefore vanish in all local chambers meeting a node. This makes the zero/nonzero alternatives propagate on a vortical component. A zero constant is excluded by the preceding zero-extension and closed-factor proof, using the local power weight A2 condition q beta<j, j=1 or2, and A568's completed weighted maximum argument. The potential is invariant under T_t because Ax.Y=0, so its maximum on the unit sphere is an interior global maximum on D. No condition at infinity or0 is silently imposed.

This proves the fixed-Holder nodal version and the general A2 version at their distinct, exact regularities. The latter is the hypothesis (G) of C40 Proposition37. It is a consequence of already confirmed A596-A597, not a new unproved premise.
