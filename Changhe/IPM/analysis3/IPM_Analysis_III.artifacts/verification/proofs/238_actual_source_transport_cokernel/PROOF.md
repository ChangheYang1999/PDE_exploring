# Actual source cusps give an infinite cokernel for transport alone

## Exact statement and background

Let rho0 be the exactly joined, scalar-normalized modal trial and V=ell X+U[rho0], ell=1/k, k=1615536043799051/9007199254740992. The exact source P=(p,0), p>0, has

 DV(P)=diag(A_s,mu_s),
 10<A_s<51/5, 99999997745/10^11<mu_s<99999997750/10^11<1,
 A_s+mu_s=2/k.

These are the source quantities of topics15 and209, not the origin saddle coefficients. Put

 a=1/A_s, b=mu_s/A_s.

Then0<b<a<1/10 and a>5/51. Proof 209 gives a smooth exact local conjugacy Psi, tangent to the identity at P, with

 DPsi(X)V(P+X)=diag(A_s,mu_s)Psi(X),
 Psi1(s,-y)=Psi1(s,y), Psi2(s,-y)=-Psi2(s,y).

Its analytic neighborhood and the spectral hypotheses have already been independently checked from the original data. No new conjugacy radius or certified number is claimed here.

Fix

 a<alpha<1, 2k-1<beta<k, gamma>4k.

Let Z2 be exactly the scaled quadratic-axis target of proof 228, and Z3 the full joint-cofactor target of proof 236. On either Z=Z2 or Z3 set

 T=V.grad-1, D_Z(T)={h in Z:V.grad h belongs to Z distributionally}.

Then the algebraic quotient Z/T(D_Z(T)) is infinite-dimensional. In particular T is not onto either target. The quotient already contains infinitely many linearly independent classes represented by smooth compact physical-parity forcings with exact c=J=0. This includes every1/10<=alpha<1 for the actual source, because1/A_s<1/10.

The theorem concerns transport alone. It does not give a cokernel or non-surjectivity statement for A0 or Lren, whose source Riesz term changes the equation. It makes no assertion at alpha<=1/A_s, about the range of the actual F0, or about profile existence.

For clarity, the norms used below are as follows. Z2 consists of continuous even-x, odd-y h, zero on x=0, with the local E2 norm, dyadic annular norm

 sup_(R=1,2,4,...) R^(-beta){||h||infinity
       +R^alpha[h]_(x,alpha)+R^(2+alpha)[h]_(y,2,alpha)},

and L2(w_gamma), where the vertical seminorm divides differences by x^2|dy|^alpha and w_gamma=(1+r^2)^(-gamma/2). Z3 requires a continuous cofactor g=h/x^2 with

 ||chi g||C^alpha+sup_R R^(2-beta)(||g||infinity+R^alpha[g]C^alpha)
                  +||h||L2(w_gamma)<infinity.

The local cutoff chi equals one near zero and vanishes outside a fixed disk, and annuli are R<=r<=4R as in the cited definitions. The proof only needs their local Holder comparison near P, compact smooth forcing membership and the physical bound |h(X)|<=C||h||Z |X|^beta at infinity. It does not rely on boundedness of the full coupling on Z3.

## Local norm facts at the off-axis source

On a sufficiently small fixed disk about P, physical x is bounded away from zero. Each of Z2 and Z3 controls the ordinary full C^alpha norm there. For Z2, connect two nearby points by one horizontal and one vertical segment; the x^2 factor in the vertical difference is uniformly bounded. A finite collection of annular or local norm pieces controls those segments. For Z3, multiply the controlled cofactor by the smooth factor x^2. Thus

 ||h||C^alpha(K)<=C_K||h||Z                                           (1)

on a slightly smaller source disk K.

Every smooth function supported in these source disks and reflected with the physical parities belongs to both targets. Near the vertical axis it is zero, so no division by x is singular. Only finitely many annuli meet the support, and the weighted L2 integral is finite. The same holds for its actual transport image, since the disks lie wholly within analytic background cells. This proves all the forcing and forcing-domain membership used below.

The maximal transport domain is closed: norm convergence in either Z implies local uniform and distributional convergence, and the distributional expression V.grad h identifies any graph limit. This does not require smooth functions to be dense in the Holder norm.

## Exact local homogeneous solutions with an adjustable transverse profile

In the conjugated coordinates (s,y), choose any smooth odd compact function phi on the real line whose positive support is contained in(1,2). Define

 u_phi(s,y)=s^a phi(y/s^b) for s>0,
 u_phi(s,y)=0 for s<=0.                                               (2)

It is smooth away from(s,y)=(0,0). In particular, near a point with s=0,y!=0 it vanishes identically. Its amplitude tends to zero as s tends to zero, so it is continuous at the origin. It is odd in y. On s>0 direct differentiation gives

 (A_s s partial_s+mu_s y partial_y-1)u_phi=0,                          (3)

because A_s a=1 and A_s b=mu_s. No approximate frozen equation is being used: the exact conjugacy transfers(3) to the actual field locally.

Equation(3) also holds distributionally across s=0 and the source. One direct check is that u_phi is locally W^(1,1): on its support |y| is comparable to s^b, so

 |partial_s u_phi|<=C s^(a-1), |partial_y u_phi|<=C s^(a-b),
 integral_0^epsilon s^(a-1)s^b ds<infinity,
 integral_0^epsilon s^(a-b)s^b ds<infinity.

The trace across s=0 is zero. These estimates justify the weak derivatives and produce no delta contribution. Smooth changes of coordinates preserve the distributional identity.

The function is locally C^a. For horizontal differences of length d<=s/2, use |partial_s u_phi|<=C s^(a-1), giving a C^a quotient bounded by C(d/s)^(1-a). For differences comparable to or larger than the smaller positive s, use the supremum bound C s^a; the case of crossing s=0 is included. The y derivative is bounded on a fixed small box because a-b>0. Thus vertical differences are Lipschitz there and hence C^a. Connecting two coordinates proves the joint C^a assertion.

If phi is nonzero and alpha>a, u_phi is not C^alpha at the origin. Choose v0 in(1,2) with phi(v0)!=0 and compare

 (s,v0 s^b) and (0,v0 s^b), s down to zero.

Their distance is s and their value difference is |phi(v0)|s^a. The alpha quotient tends to infinity. A smooth diffeomorphism with invertible derivative preserves this failure, since the corresponding physical points have distance at most Cs. The moving ordinate causes no difficulty: both points approach the source, and a two-point Holder norm tests them.

## Compact actual weak solutions and smooth admissible forcing

Choose a smooth radial cutoff chi_s in the conjugated coordinates, one near zero, with compact support strictly inside the conjugacy chart. On the positive-source disk define

 H_phi(P+X)=chi_s(Psi(X))u_phi(Psi(X)),

and extend by zero outside the chart. Reflect evenly across the physical vertical axis to the disk about -P. The conjugacy's horizontal-axis equivariance and the oddness of u_phi give physical odd-y parity as well. The two disks are disjoint and separated from the physical vertical axis and origin.

H_phi is compact and continuous, locally C^a, smooth away from the two sources, and has physical J=0 because it vanishes near the origin. It is not in either Z at exponent alpha>a when phi!=0, by(1) and the preceding two-point test. Its exact transport image is

 f_phi=T H_phi=(V.grad[chi_s composed Psi])(u_phi composed Psi)        (4)

in the positive disk, with the reflected formula in the other disk. The right side is supported where the cutoff varies, away from the source. There u_phi is smooth, even at portions of s=0 because its angular profile vanishes there in a neighborhood. Therefore f_phi is smooth and compact, with physical parities, and belongs to both targets and their maximal transport domains. It also has J(f_phi)=0. Formula(4) is a distributional identity on the entire plane, by the weak derivative check and the compact cutoff.

This construction is useful because an inadmissible cusp input has an admissible smooth transport image. No analogous image assertion is made for the coupled operator.

## Uniqueness among continuous functions with the allowed far growth

We need uniqueness in a larger class than Z, since H_phi is not in Z. Suppose w is continuous on the plane, satisfies Tw=0 distributionally, and |w(X)|<=C(1+|X|^max(beta,0)) globally, with the sharper bound |w(X)|<=C|X|^beta outside a fixed disk, where beta<k. Then w=0.

Every actual forward trajectory starting strictly inside a quadrant escapes to infinity by the verified zero geometry of topics79 and88. The field is globally Lipschitz, so the forward flow is complete. Once a trajectory reaches a sufficiently large radius, the exact far bound U[rho0]=O(r^k) gives

 d_t log r_t=ell+O(r_t^(k-1)), r_t>=c exp(ell t/2).

The error in the logarithmic derivative is integrable. Consequently r_t is comparable to exp(ell t), with constants allowed to depend on the initial point. This argument uses qualitative escape only; it asserts no numerical escape time or uniform constant near the source.

For a continuous distributional solution, smooth flow boxes give

 w(X)=exp(-t)w(Phi_t X)                                               (5)

along every such trajectory. The one-dimensional distributional fundamental theorem proves this for almost every transverse parameter, then continuity extends it to every parameter. Covering any finite trajectory segment by finitely many flow boxes proves(5) for arbitrary t. Since beta<k, its right side is bounded by C_X exp((ell beta-1)t) and tends to zero. Thus w is zero in every open quadrant. Continuity makes it zero on both axes and at all three equilibria as well.

Now if v in D_Z(T) satisfies T v=f_phi, the difference w=v-H_phi has exactly this continuity, distributional equation and far growth, because H_phi is compact. Hence v=H_phi. For phi!=0 this contradicts H_phi not belonging to Z. Therefore every nonzero f_phi is outside T(D_Z(T)). This is a genuine range obstruction for these constructed smooth forcings, not a conclusion about the actual residual.

## Infinite-dimensional quotient and exact zero strain

Let E be the vector space of smooth odd phi with positive support compactly contained in(1,2). It is infinite-dimensional. The map phi -> f_phi is linear, and the preceding uniqueness argument shows

 f_phi in T(D_Z(T)) implies phi=0.

Thus phi -> [f_phi] is an injective linear map from E into the algebraic quotient Z/T(D_Z(T)). This proves infinite dimension without assuming the range is closed or constructing a bounded projection onto a complement.

To impose exact zero strain on the forcings, define the linear functional lambda(phi)=c[f_phi]. It is well-defined because f_phi is smooth and compact away from the origin, so the canonical strain integral is absolutely convergent. Its kernel has codimension at most one in E and is still infinite-dimensional. Restrict the preceding injective quotient map to this kernel. Every representative then has exact c[f_phi]=J(f_phi)=0. No approximation to zero strain is involved, and no scalar nonzero denominator is assumed if the functional vanishes identically.

The resulting quotient classes are independent even when arbitrary preimages are allowed, since any finite nonzero linear combination corresponds to a nonzero phi and fails the same uniqueness test. This proves the theorem for both Z2 and Z3.

## Scope and dependencies

Proof 209 gives the exact smooth source transport conjugacy and certified rates. Topics79 and88 give actual complete quadrant escape, and proof 228 gives the far growth bounds used to identify the terminal value. The local norm facts and every weak input/image check are proved above. Proof 236 is used only to name its explicit norm, not to import an unreviewed nonlinear or global inverse claim.

The actual coupled source operator contains -g M, with g=rho0_y(P)>0 and M having multiplier xi^2/(xi^2+eta^2). It is not the transport operator(3), so this cusp construction does not prove a full-operator range obstruction. The independently established source inverse with that Riesz term remains compatible with this result. The full Z2 theorem at alpha>1/2 comes from the separate turning mechanism. The new Z3 full inverse remains OPEN, as do alpha<=1/A_s for transport and the range of F0. There is no new numerical computation. Independent independent review is requested before report adoption.
