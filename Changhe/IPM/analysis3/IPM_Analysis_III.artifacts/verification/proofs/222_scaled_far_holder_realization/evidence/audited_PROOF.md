# Scaled far Holder norms: bounded coupling and a logarithmic endpoint obstruction

## Exact space and statements

Let k=1615536043799051/9007199254740992, ell=1/k and p=2k-1. Fix 0<alpha<1, p<=beta<k and gamma>4k. Let rho0, F0, canonical U, c, H0 and M0 be the exact joined normalized trial and columns in topics213/217. Fix a smooth radial cutoff chi, equal1 on B2 and0 outside B4. For j>=0 let R_j=2^j and A_j={R_j<=|X|<=4R_j}. The annuli overlap.

Define Z=Z_(alpha,beta,gamma) to consist of continuous functions h on the plane, even in x and odd in y, with h(0,y)=0 for every y, and finite norm

 ||h||Z=||chi h||E2+sup_(j>=0) R_j^(-beta)
       (||h||Linf(A_j)+R_j^alpha [h]_(C^alpha(A_j)))
       +||h||L2(w_gamma),                         (1)
 w_gamma=(1+|X|^2)^(-gamma/2).

Here [.]_(C^alpha(A_j)) is the usual Euclidean two-point seminorm with both points in A_j, and E2 is exactly the bounded, horizontally alpha-Holder and vertically x^2-weighted alpha-Holder norm of proof 213, including the supremum. The local cutoff in (1) is fixed. In particular (1) does NOT impose the global weighted vertical seminorm of topics213-221. It does retain the physical vanishing on the vertical axis. Smooth compact functions supported away from the axes are allowed, subject to the parities.

The following statements hold with qualitative constants for every fixed displayed alpha,beta,gamma and cutoff.

1. Z is Banach. Its strain c is bounded. The renormalized coupling

 Cren h=U[h].grad rho0+c[h]H0

is bounded Z->Z. The residual F0 belongs to Z. For a cutoff beta_R=1-chi_*(X/R), where chi_* is smooth radial,1 on B1 and0 outside B2, its noncompact coupling has output-tail bound

 ||beta_R U[.].grad rho0||Z->Z
 <=C(R^(k-1)+R^(beta+k-gamma/2)),                  (2)

which tends to0. The bound for c depends on this norm and is not the universal 4/pi bound of the former global E2 target.

2. If beta>p, the full moving-tail column M0 belongs to Z. The full A0=T+C0, C0=Cren+c[.](M0-H0), is a closed realization on precisely

 D_Z={h in Z:V.grad h belongs to Z distributionally},
 V=ell X+U[rho0], T=V.grad-1.

Both C0 and Cren have small output tails on Z. These are realization and mapping statements, not inverse statements.

3. At beta=p, the actual M0 does NOT belong to Z. There is an explicit nonzero r^p log r angular coefficient at frequency1043. A compact smooth q in D_Z with J(q)=0,c[q]=1 has A0 q outside Z. Thus the whole maximal transport-domain bounded-coupling assertion fails for the full moving-tail operator at this endpoint, although Cren is bounded and F0 belongs. A logarithmic enlargement, beta>p, or another compatible domain is needed to include the exact column. No particular repair is proved necessary among all possible choices.

4. The cubic normalization J remains nonclosable on smooth c=0 inputs in the actual full A0 graph when beta>p. No inverse, closed cubic constraint, nonlinear theorem, or actual profile is obtained by this change of far norm. In particular this topic supplies no complement inverse or Sobolev injectivity condition (I).

## Basic norm consequences and canonical velocity

Convergence in Z implies local uniform convergence. Cauchy difference bounds pass to the uniform local limit and identify the weighted L2 limit, proving completeness. The parities and axis condition are closed under local uniform convergence.

Write N=||h||Z. The near E2 factor gives a C^alpha bound on B2 because its vertical differences there cost at most4N|Delta y|^alpha. The overlapping annuli supply the ordinary C^alpha bounds on every fixed larger compact set. Finite covers and subdivision across their overlaps give the same bound for pairs in such a compact set, with a constant depending on its radius. Globally,

 |h(X)|<=CN(1+r)^beta,
 ||h(R.)||Linf({1/2<=|X|<=4})
       +[h(R.)]_C^alpha({1/2<=|X|<=4})<=CN R^beta           (3)

for R>=2, after enlarging the fixed annulus by a finite number of overlapping A_j. The negative exponent beta causes no issue at the origin because 1+r replaces r in the first bound.

The canonical velocity is well defined. The singular kernel has order r^-2 and zero angular mean; subtracting h(X) in a small disk gives an absolutely convergent integral using local C^alpha regularity. At infinity use the canonical subtraction K(X-Y)-K(-Y), which is O(|X||Y|^-3) for |Y|>2|X|. Since beta<k<1, its integral against |h(Y)| is finite. The local multiplier term in U2 has the same bounds as h. The far subtraction integral over each centered annulus is zero by parity: K1 is odd in both coordinates and h is even in x, while K2 is even in y and h is odd in y. This identifies the prescription with centered radial truncations of the usual multiplier and fixes the constant velocity. It also gives U1 odd in x and U2 odd in y.

For every R>=2, elementary kernel estimates give

 ||U[h](R.)||Linf({1<=|X|<=2})
       +[U[h](R.)]_C^alpha({1<=|X|<=2})<=C N R^beta.       (4)

Here the interval -2<beta<1 suffices, and it contains the stated beta range. To prove (4), divide inputs into |Y|<R/4, comparable radii, and |Y|>8R, with smooth overlapping radial cutoffs. For the inner part, the kernel is separated from output and

 R^-2 integral_(|Y|<R/4)|h(Y)|dY<=CN R^beta

because beta>-2. Its output derivative is bounded by CN R^(beta-1), giving the scaled Holder bound. For the outer part, subtraction gives

 R integral_(|Y|>8R)|Y|^-3 |h(Y)|dY<=CN R^beta

because beta<1; its derivative has the corresponding bound CN R^(beta-1). The subtracted constant over that centered region is zero by parity. For comparable radii rescale by R. The cutoff input is compactly supported on a fixed annulus with C^alpha norm at mostCN R^beta by (3). A homogeneous mean-zero order-zero kernel maps such compact C^alpha inputs to C^alpha with a fixed bound. For completeness, its near integral uses h(X-z)-h(X), giving integral_0^1 r^(alpha-1)dr. For a difference of two outputs at distance d<1, split |z|<=2d, bounded by CN d^alpha, and the remaining kernel difference, bounded by CN d integral_(2d)^1 r^(alpha-2)dr plus the smooth outer part. This is O(Nd^alpha) since 0<alpha<1. The finite cutoff-error terms obey the same bound. This proves (4) with no weighted L2 Riesz theorem and no global boundedness assumption on h when beta>0.

The strain kernel is absolutely integrable against h. Near0, chi=1 and |h(x,y)|<=N x^2 |y|^alpha, so the polar integrand has integrable order r^alpha dr. Far from0, |h|<=CN r^beta and the order-minus3 kernel gives integral_1^infinity r^(beta-2)dr<infinity. On the fixed transition region (3) suffices. Therefore

 |c[h]|<=C_(alpha,beta,chi) N.                       (5)

## A cutoff commutator needed for the local axis norm

A local E2 norm cannot be replaced without argument by a global E2 assumption. The following commutator supplies the missing localization step:

 W=[chi,U]h=chi U[h]-U[chi h]

has a bounded global C^(1,alpha) norm, at mostCN. At infinity W=-U[chi h], which and its differentiated tails decay, because chi h is compact and has the physical parities. On a fixed disk, the far part of h contributes a smooth function with all needed derivative bounds by beta<1. For the remaining compact input, the integral kernel is

 (chi(X)-chi(Y))K_i(X-Y),

of order minus1. The local multiplier term commutes and disappears. Differentiate in X. The first term is (partial_l chi)U_i[h], locally C^alpha by (4) and its fixed-disk version. In the second term put z=X-Y and expand

 chi(X)-chi(X-z)=sum_m partial_m chi(X)z_m+O(|z|^2).

The principal derivative kernels z_m partial_l K_i(z) are homogeneous of degree minus2 and have zero angular mean. Indeed integrate partial_l(z_m K_i) on an annulus: its two boundary fluxes agree by homogeneity, so the angular integral of delta_lm K_i+z_m partial_l K_i is zero; K_i itself has zero angular mean. Their C^alpha mapping is the elementary cancellation estimate used above. The Taylor remainder has kernel O(|z|^-1), with differentiated kernel O(|z|^-2) on a fixed disk. Its difference on bounded inputs is O(d(1+log(1/d))), hence O_alpha(d^alpha). Smooth cutoff and separated terms have the same bound. This proves the C^alpha norm of every first derivative of W. The undifferentiated kernel is locally integrable and has the required supremum bound. These arguments also justify distributional differentiation by truncation and its continuous extension.

The vector W has the velocity parities. In particular

 W1(x,y)/x=integral_0^1 partial_x W1(sx,y)ds

extends continuously through x=0 and is uniformly C^alpha in y, with norm at mostCN. Both W2 and its ordinary C^alpha norm are at mostCN. The exact actual divided density coefficients a1=rho0_x/x and a2=rho0_y/x^2 are globally bounded and Lipschitz: this follows from the origin C^(4,1) expansion, exact compact joins, and far orders r^(k-2),r^(k-3). Therefore

 (W.grad rho0)/x^2=a1(W1/x)+a2 W2

has a bounded uniform vertical alpha seminorm. The ordinary horizontal seminorm and supremum follow from W in C^(1,alpha) and the bounded Lipschitz gradient of rho0. Thus W.grad rho0 belongs to E2 with norm at mostCN.

Now chi h belongs to the GLOBAL E2 space by definition and is compact. Proof 214's bounded coupling applies to it, with its weighted L2 norm bounded by its compact E2 norm. The exact identity

 chi U[h].grad rho0=U[chi h].grad rho0+W.grad rho0          (6)

and the preceding estimates prove the local E2 part of the output. This handles pairs crossing the cutoff and inputs just outside its support. It does not require unproved quadratic axis control on all distant input annuli. The compact column chi H0 is in E2, and (5) controls its scalar coefficient.

## Far coupling, weighted L2 and small tails

The exact trial satisfies, on far annuli with all fixed first and second cylinder derivatives needed here,

 grad rho0=O(r^(k-1)).

Combining its scaled Lipschitz bounds with (4) and the usual Holder product difference gives

 ||(U[h].grad rho0)(R.)||infinity
       +[(U[h].grad rho0)(R.)]_C^alpha<=CN R^(beta+k-1).  (7)

Multiplication by R^-beta in (1) yields CN R^(k-1), so the far part is bounded. The compact annuli are controlled by the fixed-disk C^alpha estimates. The product vanishes on x=0 because both derivatives rho0_x and rho0_y vanish there; its physical parity is preserved.

For the weighted L2 norm the pointwise bound (7) gives

 integral_(r>=R)|U[h].grad rho0|^2 w_gamma dX
 <=CN^2 integral_R^infinity r^(2beta+2k-1-gamma)dr.

It is finite because gamma>4k>2beta+2k. Taking the square root gives CN R^(beta+k-gamma/2). No weighted L2 input estimate was used here; its presence in Z fixes the proposed common target but is not needed for this coupling bound. Combined with (6), (5) and compact H0, this proves Cren bounded on Z.

For R large enough that beta_R vanishes on the support of chi, the local E2 factor of the tail output is zero. The scaled annular cutoff derivatives have size O(1) after rescaling, so (7) gives its far seminorm at mostCN R^(k-1). The preceding L2 integral gives the other term of (2). Both exponents are negative because k<1 and beta<k<gamma/2-k. This proves the entire tail norm, including cutoff-crossing differences.

## Residual and the exact moving-tail column

Proof 117 gives

 F0=r^p S_F(theta)+O(r^(3k-2)), p=2k-1,

with every fixed cylinder derivative, and a nonzero finite angular polynomial S_F. The change from its shifted t notation only multiplies the nonzero coefficient by a positive radial constant. Thus the scaled far factor in (1) is bounded exactly when beta>=p. The ordinary angular Holder bounds follow from the finite smooth angular sums. The residual belongs to the local E2 factor by proof 213, and its weighted L2 condition is exactly gamma>4k, also proof 213. This proves F0 in Z throughout the stated range. For beta<p the nonzero leading coefficient would already violate the supremum part of (1).

Proof 217 proves, with the local axis divisions and compact join regularity,

 M0=O(r^p(1+log r)),
 D_cyl^j M0=O(r^p(1+log r))                         (8)

for the finite derivative orders used in this norm. Its local E2 factor is finite. If beta>p, multiplying (8) by R^-beta proves the scaled far norm is finite. The weighted L2 factor is finite under gamma>4k. Moreover

 ||beta_R M0||Z<=C(R^(p-beta)+R^(2k-gamma/2))(1+log R),     (9)

which tends to0. Equations (5), (2), (9) prove boundedness and small tails for C0. Bounded perturbation of the maximal transport operator proves the closed realization on D_Z: convergence in Z implies local uniform and distributional convergence, so T is closed, and subtracting the bounded C0 establishes equality of the full and transport maximal domains. No dense-domain assumption is used.

## The logarithmic endpoint is genuinely excluded for the full column

It remains to prove that (8)'s logarithm is present for the actual trial, rather than an artifact of an upper bound. Write Phi_q=r^q Theta(theta). The leading angular factor has highest sine frequency n=521 and nonzero coefficient

 a_n=exp((3-k)t_plus) Aout[259,0]/8,
 Aout[259,0]=-8059128652303703/10384593717069655257060992658440192.

The normalization repair affects only the lowest angular coefficient. Proof 35 derives directly from the homogeneous stream equation that

 U[Phi_q].grad Phi_q=r^(2q-1)Q_q(theta),
 [sin((2n+1)theta)]Q_q=-(n-q)a_n^2/[4(n+q+2)].       (10)

In this parameter derivative Theta and a_n are fixed. At q=k the coefficient in (10) is nonzero. The canonical homogeneous velocity depends smoothly on q near k because its finite modal denominators are nonzero. Compact cutoff modifications have decaying multipole velocities and cannot affect the leading powers below.

Outside the chart cutoff zeta=-k^2 partial_q Phi_q at q=k, and rho0=Phi_k+R with R=O(r^p). Differentiating the quadratic expression in (10) therefore shows

 U[rho0].grad zeta+U[zeta].grad rho0
 =-k^2 r^p (2 log(r)Q_k+partial_q Q_q|_(q=k))
       +O(r^(3k-2)(1+log r)),                      (11)

where faster compact multipoles are absorbed. The exact leading linear cancellation in X.grad rho0+(ell r partial_r-1)zeta leaves X.grad R, which has no r^p log r term and angular frequency at most521. Since M0=(X.grad rho0+Lfix zeta)/n'_0 and n'_0>=3,

 M0=r^p log(r)S_M(theta)+O(r^p),
 S_M=-2k^2 Q_k/n'_0.                               (12)

Its sin(1043theta) coefficient is

 k^2(n-k)a_n^2/[2n'_0(n+k+2)]>0.                   (13)

Every factor has its stated exact sign, so no new numerical enclosure is needed. The original highest coefficient is independently reconstructed and checked in proof 35. Equations (12)-(13) prove S_M is not identically zero. At a fixed angle with S_M nonzero, R^-p |M0(R,theta)| grows as a positive constant times log R. Therefore M0 is outside Z at beta=p.

Choose a compact smooth physical-parity q, supported away from both axes and the physical origin, with c[q]=1; rescale the explicit nonzero-strain bump of proof 204. Then J(q)=0 and q,Tq belong to Z. Its canonical velocity is O(r^-3) at infinity by the parity multipole expansion, so U[q].grad rho0=O(r^(k-4)), with the corresponding scaled Holder bounds. Near the origin the bounded-coupling proof above applies. Thus Lfix q belongs to Z even at beta=p. But A0q=Lfix q+M0 does not, by (12). This checks both perturbation and transport image and rules out a bounded full coupling on the entire transport domain at the endpoint. It does not rule out a more restrictive full maximal domain or an endpoint norm with a logarithmic weight.

## Normalization and remaining scope

For beta>p take the exact compact smooth packets h_epsilon of proof 204, with J=1,c=0. Their supports are contained in a fixed disk, and their E2 and actual transport-image norms tend to0 as epsilon^(1-alpha), with an O(epsilon^2) fixed compact strain correction. On a fixed compact set the new annular and L2 factors are bounded by the E2 norm. Hence h_epsilon and T h_epsilon tend to0 in Z. Boundedness of C0 gives A0 h_epsilon->0 in Z. J is therefore not closable on the smooth c=0 actual graph, as claimed. The same reasoning applies to Cren at beta=p.

This norm excludes the bad far packets of topics220/221 and contains the residual. That observation and small coupling tails do not give an inverse for its transport operator or the full A0. The local source and origin constructions may be cut off into this norm because compact E2 outputs, and compact C^alpha outputs separated from the vertical axis, have bounded Z norm; no parametrix error estimate is asserted. The logarithmic endpoint check is essential before any full moving-tail inverse claim. Actual invertibility, the cubic constraint, nonlinear closure and the separate Sobolev campaign remain open.

Dependencies: topics35/117 for exact homogeneous interaction and residual powers; topics203/213/214 for E2 localization, ordinary compact Holder comparison and coupling; proof 217 for the exact column and divided origin estimates; proof 204 for exact normalization packets and compact strain correction. All new annular norms, velocity mapping, cutoff commutator, weighted tail bounds and endpoint exclusion are proved above. No numerical computation or inverse certificate is claimed.
