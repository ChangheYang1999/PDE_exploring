# Dilation, sector separation and a compact high-order axis row

## Exact spaces and statement

Let a=17/4, eta=5/4, W(r)=max(1,r)^(2a-eta), and

 R=L2_P(|x|^(-2a)W(r)dX), E=X.grad,
 g(t)=exp(-t/2) for t<0, g(t)=exp(27t/4) for t>=0.

The parity P is even in x and odd in y. Let H_g^N be the space of distributions f on the line with weak derivatives through order N in L2(g dt), with the sum-of-squares norm. Let chi_s be smooth away from0, homogeneous of degree0 and even under both coordinate reflections. Fix0<theta_0<theta_1<pi/2, and require chi_s=1 within angle theta_0 of either vertical half-axis and chi_s=0 outside angle theta_1 of them. Take0<=chi_s<=1.

For an integer M>=0 define the Hilbert graph space

 R_(M,s)={h in R:E^j(chi_s h) in R for0<=j<=M},
 ||h||_(M,s)^2=||h||_R^2+sum_(j=1)^M ||E^j(chi_s h)||_R^2.

All derivatives are distributional. For M=0 this is simply R. Let alpha(t) be real and belong to W^(N+1,infinity) on every compact interval. For0<=j<=N+1 require finite constants with

 |alpha(t)|<=C, |alpha^(j)(t)|<=C exp(2t) for t<0 and j>=1,
 |alpha^(j)(t)|<=C exp((k-3)t) for t>0, 0<k<1.

Let chi_0(y) be a fixed radial cutoff, equal1 near0 and0 for large y, with bounded weak t derivatives through order N. Define the canonical raw trace and strain by the continuous extensions of the full-plane velocity:

 T_h(y)=U_2[h](0,y), c[h]=T_h'(0), V_h(t)=T_h(exp(t))/exp(t).

Then the complete axis row is

 Gamma_h=(alpha'-alpha)V_h-2alpha V_h'
                    +c[h]chi_0(alpha+alpha'/3).                (1)

For every integer N>=0 under these coefficient hypotheses, set M=max(N-2,0). The map

 Gamma:R_(M,s) -> H_g^N                                      (2)

is bounded and compact. Its norm is finite but is not evaluated here. For the actual normalized modal background, the coefficient hypotheses hold for every integer N<=6, because alpha is C6 and piecewise analytic with bounded seventh weak derivative on the finite knot interval, and its endpoint expansions have the stated bounds. Thus in particular the remainder axis row is compact from R_(4,s) into H_g^6.

This is a theorem for remainder inputs h in R. It does not assert that a full free-jet input E beta belongs to R, and it does not by itself prove the high jet-row hypothesis for the full domain, the high remainder mapping, or a high inverse.

## Canonical dilation and its exact domain

For s real put D_s h(X)=h(exp(s)X). The ratio of W at two radii differing by exp(s) is bounded above and below by positive constants depending only on s. Changing variables therefore proves that D_s is a bounded group on R. It is strongly continuous: prove this first on smooth parity-preserving functions compactly supported away from0 and the vertical axis, then use their density and the local uniform bounds on the group. Its generator is the maximal distributional realization of E. This can be checked in polar logarithmic coordinates by the fundamental theorem for translations and then by distributional difference quotients.

The canonical raw velocity needs no subtraction at infinity on R. Its off-diagonal kernel is homogeneous of degree-2, and the squared kernel times the inverse weight is integrable at infinity because eta<2. Its local part is the ordinary L2 singular integral, including the local -h/2 term of U_2. Hence a change of variables on the smooth core gives

 U[D_s h](X)=U[h](exp(s)X).

Local distributional continuity extends this identity to R. The bounded trace functionals extend the corresponding axis identity:

 T_(D_s h)(y)=T_h(exp(s)y), c[D_s h]=exp(s)c[h].            (3)

If E^j h belongs to R, differentiation of (3) in the graph domain gives

 (y partial_y)^j T_h=T_(E^j h), c[Eh]=c[h].                (4)

The latter identity also follows by integrating by parts against the degree-3 strain kernel. No boundary term is introduced by approximation in the generator graph norm. In particular (4) is not an assertion for an arbitrary R input whose E derivative is undefined in R.

Subtracting a homogeneous linear strain field preserves dilation covariance. A spatially cut off field does not. For the normalized velocity W_0[h]=U[h]+c[h]chi_0 X/3 one has, whenever Eh is in R,

 E W_0[h]-W_0[Eh]=(c[h]/3)(E chi_0)X.                    (5)

The cutoff term is finite rank and supported on a fixed annulus. It cannot be dropped when commuting the complete normalized velocity.

## Three trace derivatives and two derivatives gained by the row

The trace estimates of topics46 and103 give continuous R-dual kernels T_h^(j)(y),0<=j<=3. There is M_3<infinity such that ||T'''(y)||_(R*)<=M_3 for |y|<=1. Parity gives T(0)=T''(0)=0. Set B_0 h=V_h-c[h] and B_q h=partial_t^q V_h for q>=1. Direct differentiation yields

 B_1=T'-T/y,
 B_2=yT''-T'+T/y,
 B_3=y^2 T'''+T'-T/y.                                    (6)

Taylor's formula gives

 ||B_0(y)||_(R*)<=(M_3/6)y^2,
 ||B_1(y)||_(R*)<=(M_3/3)y^2,
 ||B_2(y)||_(R*), ||B_3(y)||_(R*)<=(4M_3/3)y^2             (7)

for0<y<=1. At infinity, the scaled kernel bounds of proof 46 apply for each j<=3: their local integrability condition is a>j+1, which holds even at j=3. Thus

 ||T^(j)(y)||_(R*)<=F_j y^(eta/2-1-j),
 ||partial_t^q V(y)||_(R*)<=C_q y^(eta/2-2), 0<=q<=3.      (8)

Equations (4) imply partial_t V_h=V_((E-1)h). For q>3, transfer q-3 derivatives to the input:

 partial_t^q V_h=B_3((E-1)^(q-3)h).                       (9)

Near0 the right side obeys (7); at infinity it obeys (8). This is why differentiating Gamma N times needs only max(N-2,0) dilation derivatives of the input, rather than N+1. All identities hold first on the smooth graph core and then weakly by the bounded estimates.

For the sector part chi_s h, E commutes with chi_s. Apply (7)-(9) to every derivative of (1). Near0 use the cancellation identity

 Gamma=(alpha'-alpha)(V-c)-2alpha V'+(4/3)c alpha'         (10)

because chi_0=1 there. Every differentiated term is bounded by C exp(2t)||h||_(M,s). At infinity use (1) with chi_0=0 and (8)-(9), giving C exp((k-35/8)t)||h||_(M,s). The squared weighted bounds are exp(7t/2) near negative infinity and exp((2k-2)t) near positive infinity. Both are integrable. On the intervening compact interval the coefficient derivatives and trace kernels are bounded.

A measurable R-dual kernel with integrable squared norm defines a Hilbert-Schmidt map from R to the relevant weighted L2 space. The preceding bounds prove precisely this integrability for each term with at most three derivatives remaining on the trace kernel. Composing such a map with the bounded input maps (E-1)^j chi_s:R_(M,s)->R preserves compactness. The strain terms have finite rank. Therefore each derivative of Gamma up to N is compact into L2(g dt). Their finite product is compact, and the weak-derivative graph defining H_g^N is closed, so this proves compactness into H_g^N for the sector part. No extra input derivative is needed for this argument.

## The part outside the sector

The support of 1-chi_s is outside the smaller sector of angle theta_0. It is not generally outside the larger sector of angle theta_1. If X=(0,y), y>0, and Y is in this support, elementary projection geometry gives

 |X-Y|>=sin(theta_0) max(y,|Y|).                           (11)

The derivative bounds for the degree-2 velocity kernel then imply

 |(y partial_y)^q K(X-Y)|<=C_q(theta_0) max(y,|Y|)^(-2),
 C_q(theta_0)=sum_(j=0)^q S(q,j)(j+1)!/[2pi sin(theta_0)^(j+2)], (12)

where S(q,j) are Stirling numbers of the second kind, with S(0,0)=1. In particular all conormal orders are allowed. Their squared R-dual norms are at most

 C_q(theta_0)^2 I_a [y^(-4) A_(2a+1)(y)+B_(2a-3)(y)],     (13)

where I_a, A and B are the exact elementary integrals of proof 103. The bound is finite for every y>0. Using W(r)^(-1)<=r^(eta-2a) gives the simpler scale bound

 C_q(theta_0)^2 I_a [1/(eta+2)+1/(2-eta)] y^(eta-2).       (14)

After division by y it has the infinity order in (8).

For completeness the cancellation at0 also holds at every conormal order without input derivatives. Replace the kernel by its odd part in the source y coordinate, which leaves its pairing with the odd input unchanged. For |Y|>=2y its Taylor expansion about y=0 is y c_kernel(Y)+O(y^3|Y|^(-5)); applying any fixed conormal derivative preserves the indicated orders. After division by y and subtraction of the constant strain, the remainder kernel is bounded by C_q y^2 |Y|^(-5). Its squared inverse-weight integral is bounded by C_q y^4, since

 integral_0^1 r^(2a-9)dr+integral_1^infinity r^(eta-9)dr<infinity.

For |Y|<=2y, (11)-(12) bound the divided trace by C_q y^(-3), while the subtracted strain kernel is at most C|Y|^(-3). Their R-dual norms on this region are O(y^(a-2))=O(y^(9/4)), which is O(y^2) for y<=1. The same reasoning applies to partial_t^q V for q>=1, where differentiation removes the constant strain. Thus the bounds (7) at every fixed conormal order hold for the separated input.

Every derivative through N of its complete row is consequently a Hilbert-Schmidt map from R to L2(g dt), with the same endpoint powers as above. This proves (2) for the outside-sector part and completes the proof.

## Audit of the proposed reduction

The raw canonical velocity commutes with dilations on its exact graph domain. The cutoff normalization has the correction (5). The geometric separation uses theta_0, the sector on which chi_s is already1. The unrenormalized estimate N_0(y)/y alone does not prove the origin endpoint: N_0 has a nonzero bounded far-source contribution as y tends to0, and division by y loses integrability. The full cancellation (10) is essential.

The theorem also improves the proposed derivative count for remainder inputs by keeping three derivatives on the integrable trace kernel. It does not justify applying an R-dual estimate to E beta, since that input generally fails R membership at the vertical axis. The finite angular jet input must be handled separately. Nor does the argument for an axis trace prove the full two-dimensional mapping of C_R E beta required by the other block hypothesis. Those obligations remain open here.
