# The actual inner principal estimate

## Statement

Use the exact normalized modal trial, the weight b and the closed remainder space X_s of proof 123. Choose the actual smooth order s of proof 130: it is nondecreasing along W, equals s_0=41/20 on a uniform horizontal angular strip sufficiently far left, and equals sigma=25/4 on a fixed vertical sector. Let

 T h=V.grad h-h,   D_s={h in X_s:T h in X_s in distributions}.

Fix a compact set K contained in {lambda:Re lambda>-m_x}, where m_x=(3ell-7)/10. Fix a smooth real function chi with chi=1 on (-infinity,0], chi=0 on [1,infinity), and 0<=chi<=1. There are L>2, T_*<-2L, C_K<infinity, and a fixed smooth eta supported in (-L,2L) and equal to one on [-1,L], such that, for every T_0<=T_*, lambda in K and h in D_s,

 ||chi(t-T_0)h||_Xs
 <=C_K[||chi(t-T_0-L)(T-lambda)h||_Xs
             +||eta(t-T_0)h||_Xs].                    (1)

The constants are independent of the translated end T_0. The same assertion holds with the right side's first norm replaced by the full X_s norm of (T-lambda)h. All norms are the global norms applied to the displayed localized functions. The annular error in (1) is a high norm. It has not been replaced by a compact or low-norm error.

This is an estimate for the actual principal operator on its exact maximal high domain. It does not identify the auxiliary vertical space with the physical low space. It uses that a high-domain function belongs to the auxiliary space after localization, and then uses uniqueness there.

## Uniform localizations and coefficient extensions

Write v=h/b. At the left end b=r^(3+delta), delta=9/5. On the vertical chart tau=log y, z=x/y, write h=x^2 y^(1+delta)u. On the horizontal chart tau=log x, z=y/x, write h=x^(3+delta)u_x. The changes from polar coordinates to these charts and their inverses have bounded derivatives on fixed angular strips, independently of translation in t. Their smooth scalar factors have the same property. On a constant-order strip they therefore preserve the indicated isotropic Sobolev norms with uniform comparison constants. Smooth angular and translated radial multiplication is uniformly bounded in X_s. These facts follow either from the dyadic norm and its localized kernels or from the coordinate-invariant local definition in proof 123.

Choose the vertical strip |z|<4z_0 inside the constant-order cofactor sector. By the exact inner exponential-polynomial expansion, all seven required derivatives of q_1+A and q_2-D tend uniformly to zero there as t tends to minus infinity. Here q_i=V_i/X_i, with the parity extension at an axis. Consequently the normalized vertical operator can be extended to the full (tau,z) plane as in proof 133, with

 P_y=partial_tau+B partial_z+C,
 B=-a z+b_1, a=Sigma/D,
 C=delta-lambda/D+c_1,
 ||b_1||_W7+||c_1||_W7<=epsilon.

The extension agrees with the actual normalized operator on the support of every cutoff below. Choose epsilon small enough for proof 133 and also so that

 B(tau,z)/z<=-a/2  for z!=0.                            (2)

Indeed b_1 is odd and ||partial_z b_1||_infinity<=epsilon. Take its extension compactly supported in z, so (2) holds globally. The coefficient of partial_tau is one. The same construction on a fixed horizontal strip gives the stable operator of proof 135. Its required four derivatives are available. All these choices can be made uniformly for T_0<=T_*, by taking T_* sufficiently negative after the finitely many geometric widths have been fixed.

## A vertical estimate without an angular error

Let psi(z) be even, equal to one on |z|<=2z_0, supported in |z|<3z_0. Take a translated left cutoff chi_v(tau), whose transition will be placed in a fixed annulus near T_0. Put w=psi chi_v u and extend it by zero. The defining cofactor condition of X_s gives w in H^sigma, even in z with zero value at z=0. Thus w belongs to

 H_y=L2(|z|^(-9/2) d tau dz).

For clarity, this membership is quantitative: evenness gives the first normal trace zero; twice integrating w_zz and using H^1_z into L-infinity_z bounds the weighted integral near zero by a constant times ||w||_H^3 squared times integral_0^1 z^(-1/2)dz. Compact z support handles the rest.

For f=(T-lambda)h, let F be its vertical cofactor divided by q_2. Directly in distributions,

 P_y w=psi chi_v F+psi chi_v' u+B psi' chi_v u.          (3)

Each term belongs to H_y; it also belongs to H^sigma on its compact z support. This follows for F from f in X_s and q_2>D/2, and for the other terms from h in X_s and the W7 multiplier bounds. Thus w is in the maximal H_y domain of P_y. Proof 133 identifies it with the unique low inverse applied to the right side of (3).

That inverse is minus the integral of the positive-time transport group. At a point |z|<z_0 its integrand samples only the forward characteristic of (1,B). By (2), every sampled normal coordinate has absolute value at most |z| exp(-a s/2)<z_0. The third term of (3) vanishes on this entire characteristic, since psi' is supported where |z|>=2z_0. Therefore its selected inverse is identically zero on |z|<z_0. This is an equality of distributions on that open strip, or follows first for smooth data from the flow formula and then from H_y convergence. The direction of sampling is forward; no claim about propagation of a forcing support in the opposite direction is used.

Apply the high estimate of proof 133 only to the first two terms. On a smaller fixed vertical strip this yields

 ||chi_v u||_Hsigma,vertical
 <=C_K[||psi chi_v F||_Hsigma+||psi chi_v' u||_Hsigma].  (4)

The first term is controlled by the appropriately larger end localization of f. The second is controlled by h in a finite annulus. Since t=tau+(1/2)log(1+z^2), the chart shift is uniformly bounded on the strip. Thus all radial transition supports fit into a polar annulus of a fixed width independent of T_0. The bulk part in this sector is controlled by its cofactor part. Equation (4) is the required actual vertical-sector estimate.

## Finite-time propagation through the intermediate angles

Choose a smooth reflection-invariant horizontal cutoff chi_x supported inside the uniform s_0 plateau and equal to one on a smaller horizontal neighborhood. Put chi_i=1-chi_x. In each quadrant the angles in supp chi_i are bounded away from the horizontal axis. The exact limiting angular field is Sigma sin(theta)cos(theta). On a compact interval from that lower angle to the chosen vertical strip it is strictly positive. The actual field converges uniformly to it; hence, sufficiently far left, a common finite forward time T_f carries every such angle into a smaller vertical strip where (4) applies. Once in that strip it remains there by (2), as long as the characteristic stays in the end. The other quadrants follow by reflection.

The radial speed |q| is globally bounded by a fixed M. Thus a trajectory of duration T_f starting at t<=T_0+1 stays at t<=T_0+1+M T_f. Choose L larger than this displacement, the bounded chart shifts, all cutoff transition widths and an additional fixed margin. Place chi_v's transition after these sampled points but before polar t=T_0+L. Then chi_v=1 at every final point sampled from t<=T_0+1, and all radial transitions in (4) lie where eta(t-T_0)=1. The first term of (4) uses f only where chi(t-T_0-L)=1, after enlarging L once if needed. One can, for example, reserve the first third of L for displacement, the second third for the vertical transition and the final third for the forcing cutoff. The fixed eta can then equal one on the entire transition region and vanish outside (-L,2L).

The actual positive-time semigroup S_a of T is bounded on X_s for every finite a by proof 126 and the actual monotonicity of proof 130. Its bound is uniform in the translated end, since it is a global bound. For h in D_s,

 h=exp(-lambda T_f)S_(T_f)h
       -integral_0^(T_f) exp(-lambda a)S_a f da.        (5)

This identity holds on the exact maximal domain: proof 126 proves that domain is the semigroup generator domain. Multiply (5) by chi(t-T_0)chi_i. In the first term insert the vertical and radial cutoffs already controlled in (4); they equal one at every sampled final point. In the integral insert the larger end cutoff, which equals one at every sampled point of the trajectory. The flow formula makes both insertions exact. Uniform boundedness of multiplication and S_a, followed by (4), gives

 ||chi(t-T_0)chi_i h||_Xs
 <=C_K[||chi(t-T_0-L)f||_Xs+||eta(t-T_0)h||_Xs].       (6)

If needed on a slightly larger radial support for the horizontal step, run the same argument with T_0 replaced by T_0+2. Increasing L by a fixed amount and taking T_* smaller keeps the right side in the form displayed in (6). This finite enlargement is made once. No comparison with the limiting order s_-(theta) is used: the semigroup estimate uses the actual s(t,theta).

## The horizontal cutoff and conclusion

Apply the actual horizontal chart to chi(t-T_0)chi_x h. Its zero extension belongs to ordinary L2 and H^s_0, because the support lies in the constant-order plateau and has bounded z width. Its distributional image under the extended normalized horizontal operator is the sum of the localized forcing, the radial cutoff commutator, and the angular cutoff commutator. Multiplication by the normalization factor -1/q_1 is bounded, since -q_1>A/2 in this end.

The radial commutator is supported in the fixed annulus where eta=1. The angular commutator is supported away from the horizontal axis, and is controlled by (6) with the fixed enlargement just described. Its coefficient has uniformly bounded derivatives. All three terms therefore belong to H^s_0 with norm bounded by the right side of (1). The localized unknown is in the maximal ordinary L2 domain of the horizontal extension. Low uniqueness and the stable high inverse of proof 135 give the same bound for its H^s_0 norm. Transforming back gives the X_s bound for chi(t-T_0)chi_x h; the vertical cofactor component is absent on this support.

Adding this estimate to (6) proves (1). The cutoffs, geometric times, coefficient thresholds and constants were selected using only K and the fixed actual background, and then applied uniformly for T_0<=T_*. This proves the stated quantifiers and the maximal-domain assertion.

## Scope

The finite annular high norm in (1) remains to be controlled by a core estimate. The full coupling also needs an end estimate before T can be replaced by T+C_R. Neither task follows by treating a small coefficient multiplying a derivative as a bounded perturbation; proof 136 proves that this would fail for the actual field. This result asserts no global high inverse or nonlinear existence theorem.
