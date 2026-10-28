# An actual exterior inverse in scaled far Holder norms

## Exact statement and auxiliary operator

Use the exact joined normalized trial rho0 and k,ell=1/k of proof 222. Fix 0<alpha<1, 2k-1<beta<k and gamma>4k. Let R be sufficiently large, and write Omega_R={X:|X|>R}. Let F_R be the Banach space of continuous physical-parity functions on the closure of Omega_R, vanishing on x=0 there, with norm

 ||h||F_R=sup_(j>=0) r_j^(-beta)
       (||h||Linf(A_(j,R))+r_j^alpha[h]_C^alpha(A_(j,R)))
       +||h||L2(Omega_R,w_gamma),
 r_j=2^j R, A_(j,R)={r_j<=|X|<=4r_j},
 w_gamma=(1+|X|^2)^(-gamma/2).

There is no prescribed inner boundary value. Derivatives and equations below hold distributionally on the OPEN exterior, with continuous extension of the functions to its boundary. Let V=ell X+U[rho0] and T_R=V.grad-1 on

 D_R={h in F_R:V.grad h belongs to F_R distributionally on Omega_R}.

For all sufficiently large R, T_R is a closed bijection D_R->F_R. Its inverse is

 Q_R f(X)=-integral_0^infinity exp(-t) f(Phi_t X)dt,           (1)

where Phi_t is the ACTUAL forward flow of V. The inverse F_R->F_R norm is bounded uniformly for all such R. The graph-domain norm is then bounded because V.grad Q_R f=Q_R f+f.

There is also a genuine, but auxiliary, exterior nonlocal inverse. Fix a smooth radial eta_R(X)=eta(|X|/R), equal0 for |X|<=5R/4 and1 for |X|>=2R. Define E_R h=eta_R h on Omega_R and0 inside, and let P_R be exterior restriction. Let Z be the global scaled space of proof 222. Thus E_R:F_R->Z, and P_R:Z->F_R are bounded uniformly in R. Using the exact full bounded coupling C0 from proof 222, put

 B_R=P_R C0 E_R,
 A_R=T_R+B_R:D_R->F_R.                                  (2)

For sufficiently large R, (2) is a closed bijection on that exact maximal exterior transport domain, with uniformly bounded inverse. The exterior unknown is inserted into the canonical whole-plane velocity through the stated zero-interior cutoff E_R. On |X|>=2R, (2) is the actual full differential expression applied to E_R h. On R<|X|<2R the transport factor is h rather than eta_R h; this distinction is part of the definition.

This is an exterior auxiliary theorem, with no supplied numerical radius or constant. It is not a global inverse, not a projection/complement certificate for Avenue IV, and not an inverse on a closed cubic-normalization subspace. It does not settle the middle annuli, source/origin patching, nonlinear estimates or Sobolev condition(I).

## Uniform actual-flow geometry and differences

The exact finite far Green formulas give

 |U[rho0](X)|<=C r^k, |D U[rho0](X)|<=C r^(k-1),
 div U[rho0]=0.                                          (3)

Choose a fixed R0 so large that the radial component of V is at least ell r/2 on r>=R0/2. An orbit starting outside R>=R0 stays there, tends radially to infinity, and exists for every positive time because V has at most linear growth. As in topics220/221, integrate the error in d(log r_t)/dt=ell+O(r_t^(k-1)). Since r_t>=r exp(ell t/2), its integral is bounded by C r^(k-1)/(ell(1-k)). Therefore, uniformly for R>=R0,

 c r exp(ell t)<=|Phi_t X|<=C r exp(ell t).                 (4)

For the variational equation D Phi_t, (3) gives

 ||D Phi_t(X)||<=exp(ell t) exp(integral_0^t
                         C |Phi_s X|^(k-1) ds)
                  <=C exp(ell t).                         (5)

The constants in (4),(5) can be chosen independent of R>=R0. For two starting points of comparable radius r and distance at most r/4, their connecting segment stays outside r/2>=R0/2. Apply (5) along that segment to get

 |Phi_t X-Phi_t X'|<=C exp(ell t)|X-X'|.                   (6)

The intermediate segment flows are used only to estimate Phi_t; f is evaluated only at the two exterior images. For more separated pairs on an annulus, the supremum part of the norm supplies the Holder bound directly. Smooth dependence and physical parities of V preserve all the parity and axis conditions under Phi_t.

Liouville's formula and exact incompressibility give the exact Jacobian

 det D Phi_t=exp(2ell t).                                  (7)

The image Phi_t(Omega_R) is a subset of Omega_R, and Phi_t is a smooth injection with a smooth inverse on that image. No surjectivity of this image onto the exterior is assumed.

## Scaled Holder inverse estimate and uniqueness

Let N denote the annular part of ||f||F_R. Finite overlaps of the annuli imply the same bound on every comparable-radius enlarged annulus, with a uniform constant. Equations (4),(6) imply

 ||f(Phi_t .)||annular<=C exp(ell beta t) N.                 (8)

To see the seminorm factor explicitly, for an output pair at radius r, the two image radii are comparable to s=r exp(ell t). The input difference is at mostCN s^(beta-alpha)|Phi_t X-Phi_t X'|^alpha for a close pair; (6) bounds this by

 C N r^(beta-alpha) exp(ell beta t)|X-X'|^alpha.

For a separated pair the same estimate follows from (4)'s pointwise bound. The negative beta case merely changes a fixed comparability constant. Thus (8) holds for all the displayed beta.

Since beta<k=1/ell, the integral (1) converges locally uniformly and in the annular norm. Its bound is

 ||Q_R f||annular<=C N/(1-ell beta).                        (9)

If h in D_R solves T_R h=0, the distributional equation and local flow boxes give h(Phi_t X)=exp(t)h(X). The annular bound and (4) give |h(Phi_t X)|<=C||h||F_R r^beta exp(ell beta t). Letting t tend to infinity, beta<k forces h(X)=0. Thus T_R is injective; no inner boundary condition is required, because the admissible growth at infinity selects the solution.

## The weighted L2 component, including large gamma

For gamma<2+2k, (4),(7) and change of variables Z=Phi_t X show

 ||f(Phi_t .)||L2(Omega_R,w_gamma)
 <=C exp(ell(gamma/2-1)t)||f||L2(Omega_R,w_gamma).            (10)

Indeed w_gamma(Phi_(-t)Z)/w_gamma(Z)<=C exp(ell gamma t) for Z in the image, while the inverse Jacobian is exp(-2ell t). The integral over the image is bounded by the full exterior integral. Minkowski in (1) then gives

 ||Q_R f||L2(w_gamma)
 <=C ||f||L2(w_gamma)/(1+ell-ell gamma/2).                   (11)

The denominator is positive precisely under gamma<2+2k. This estimate must not be used at or beyond that threshold.

For gamma>=2+2k use (9)'s pointwise growth instead. Since beta<k,

 gamma-2beta-2>=2(k-beta)>0.

Consequently

 ||Q_R f||L2(w_gamma)
 <=C N R^(beta+1-gamma/2)
       /((1-ell beta)sqrt(gamma-2beta-2)).                  (12)

This is obtained by integrating r^(2beta+1-gamma) from R to infinity. For R>=1 the power of R in (12) is at most beta-k<0, hence it is uniformly bounded. Equations (11),(12) cover ALL gamma>4k. In the second case the scaled supremum norm, rather than the input L2 norm, controls the output L2 norm. There is no missing large-weight endpoint case.

Combining (9) with the appropriate one of (11),(12) proves a uniform constant K with

 ||Q_R f||F_R<=K||f||F_R, R>=R0.                           (13)

## Maximal domain and the exact transport equation

The space F_R is Banach by local uniform limits of the annular bounds and identification with the weighted L2 limit. If h_n and T_R h_n converge in F_R, then local uniform and distributional convergence show that the limit satisfies the transport equation. Thus T_R is closed on D_R, without a claim of norm density of smooth functions.

For continuous f, the identity

 (Q_R f)(Phi_s X)=-exp(s) integral_s^infinity
                                      exp(-v)f(Phi_v X)dv

is valid by the absolute growth bound beta<k. Differentiating in s gives

 V.grad(Q_R f)=Q_R f+f

along every characteristic. Flow boxes imply the same identity distributionally. Both terms on the right lie in F_R by (13), so Q_R f belongs to D_R and T_R Q_R f=f. The boundary limit is continuous by local uniform convergence. Conversely every h in D_R has the characteristic identity, and its endpoint exp(-t)h(Phi_t X) tends to0 by beta<k, giving Q_R T_R h=h. This proves the stated exact bijection and maximal-domain equality.

## Cutoff extension and small nonlocal exterior feedback

The cutoff eta_R is zero on a collar of the inner boundary, so E_R h is continuous globally and has the required parities and axis condition. For R>=4, its local E2 factor in Z vanishes. Its annular Holder factor is bounded uniformly by the exterior norm: on annuli meeting the transition, the cutoff derivative is O(1/R), which after rescaling costs a fixed constant; on other annuli the cutoff is constant. The weighted L2 norm does not increase. This proves ||E_R||<=C uniformly. A finite overlap comparison between the grids 2^j and2^jR proves ||P_R||<=C uniformly. No transport derivative is required for these two bounded maps.

Let chi_* be the cutoff used in proof 222. On Omega_R, the function 1-chi_*(4X/R) equals1. Hence

 B_R=P_R(1-chi_*(4X/R))C0 E_R.

The small output tail of proof 222 gives ||B_R||F_R->F_R<=C epsilon(R/4), where epsilon(s) tends to0 and, for fixed beta>p,

 epsilon(s)<=C(s^(k-1)+s^(beta+k-gamma/2)
                 +(s^(p-beta)+s^(2k-gamma/2))(1+log s)).   (14)

Every exponent in (14) is strictly negative. B_R is therefore bounded with norm tending to0. It preserves the physical parity and axis condition because C0 does.

For R so large that ||B_R||K<1, the exact bounded-operator inverse

 A_R^(-1)=Q_R(I+B_R Q_R)^(-1)                              (15)

exists. It maps F_R into D_R, and both left and right identities follow from the exact transport inverse and its domain. Its F_R norm is at most K/(1-K||B_R||), uniformly bounded once K||B_R||<=1/2. Bounded perturbation preserves the maximal domain and closedness. This proves (2), with its explicit cutoff-extension convention. There is no unexamined pseudodifferential or projection remainder in (15).

For |X|>=2R, E_R h=h and its derivatives agree locally. Thus A0(E_R h)(X)=T_R h(X)+C0(E_R h)(X)=A_R h(X). On the transition annulus the additional transport cutoff term is present, so the exterior inverse does not by itself solve or patch the global equation. Its treatment and matching to the middle/critical regions remain open.

Dependencies: exact far modal bounds from topics35/117; the scaled global space, full-column strict endpoint and small coupling tails from proof 222. All characteristic, weighted L2, maximal-domain and exterior Neumann steps are proved above. Constants and the radius are qualitative, and no numerical computation is used.
