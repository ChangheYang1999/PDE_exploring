# Holder control and a canonical velocity limit at infinity

Status: independently derived, reviewed by the actual claude-opus-5-5 endpoint, and checked again by the verifier. This strengthens the continuous angular-limit theorem by using the gradient bound in the primary class. It does not assert smooth angular data or a second asymptotic coefficient.

## Statement and notation

Assume the exact primary hypotheses in ../inverse/PROOF.md and ../origin/PROOF.md. In particular rho is smooth locally, even in x and odd in y, rho_y(0)=a0!=0, and

    |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^gamma,
    0<gamma<1,  c_l>1,
    W=c_l X+U,  div U=0,  W.grad rho=rho.

The velocity is the canonical inverse. Set p=1/c_l. Then the angular limit Theta0 from ../far_field/PROOF.md belongs to C^alpha of the circle for every 0<alpha<1. For every compact annulus away from zero,

    q_R(Z):=R^-p rho(RZ) -> q_infinity(Z):=|Z|^p Theta0(arg Z)

uniformly as R tends to infinity, and the q_R have uniformly bounded C^alpha norms on that annulus for every alpha<1. The rescaled velocities satisfy

    R^-p U(RZ) -> U_infinity(Z)=canonical_inverse[q_infinity](Z)

uniformly on compact annuli. The limiting velocity is homogeneous of degree p. In particular U=O(r^p). For every alpha<1 the density limit has the error estimate

    sup_theta |r^-p rho(r,theta)-Theta0(theta)| <= C_alpha r^-alpha(1-p)

for sufficiently large r. The nonzero axis coefficient forces gamma>=p. The growth estimate improves the original exponent when gamma>p; when gamma=p it retains that exponent. All conclusions are conditional on an exact profile. They do not construct one.

## 1. Uniform Holder estimates for the velocity at the original growth scale

For R>=1 put f_R(Z)=R^-gamma rho(RZ). On each fixed compact annulus, f_R and its first derivatives are uniformly bounded. Globally,

    |f_R(Z)| <= C(R^-1+|Z|)^gamma <= C(1+|Z|)^gamma.

For Z in a fixed annulus, choose a smooth cutoff equal to one in a neighborhood of that annulus, supported in a slightly larger annulus. Its product with f_R has a uniformly bounded Lipschitz norm and compact support. A mean-zero, smooth homogeneous kernel of degree -2 maps this family to a uniformly C^alpha family, for every alpha<1. To verify this without an off-center principal-value issue, let f denote the compactly supported, uniformly Lipschitz density and use the same kernel displacement variable z at both queries:

    Tf(X)=integral_|z|<1 K(z)[f(X-z)-f(X)] dz
           +integral_|z|>=1 K(z)f(X-z) dz.

The first integral is absolutely convergent and uses the circle mean-zero property of K. For two query points separated by h<1/4, split that common z-integral at |z|=h. On |z|<h the difference of the two bracketed increments is at most 2 Lip(f)|z|, giving O(h). On h<=|z|<1 it is at most 2 Lip(f)h, giving O(h log(1/h)). The second integral varies by O(h), since f is uniformly Lipschitz, the query set and support are bounded, and the contributing z stay away from zero. The contact term -f e2/2 is Lipschitz. These estimates give the required C_alpha h^alpha bound, including a uniform bound for the value of Tf. No unmatched off-center constant principal value is estimated separately.

The complementary density is separated from the query annulus. Its contribution has uniformly bounded first derivatives. On bounded sets this follows from the separation and the displayed global bound. In the exterior, differentiate the kernel in the query variable; its magnitude is O(|Y|^-3), and integral_1^infinity s^(gamma-2) ds converges. The value of the exterior integral is defined with the parity subtraction K(-Y), as in the inverse proof. That subtraction is independent of the query and does not affect this derivative estimate.

The inverse commutes with dilation and is linear. Therefore R^-gamma U(RZ)=inverse[f_R](Z) has a uniformly bounded C^alpha norm on each compact annulus. In particular, uniformly for r large,

    ||theta -> U(r cos(theta),r sin(theta))||_(C^alpha) <= C_alpha r^gamma.

In that displayed line the argument is r(cos(theta),sin(theta)); the polar radial and tangential components below are written V and Q.

## 2. Holder control of the accumulated transport time

Use the notation from ../far_field/PROOF.md, with fixed initial radius R0, radial field V=W.e_r, tangential field Q=W.e_theta, angular trajectory theta(r,beta), and

    H(r,beta)=integral_R0^r [1/V(s,theta(s,beta))-p/s] ds.

The exact Jacobian formula in that proof gives uniform upper and positive lower bounds for partial_beta theta(r,beta), for all r>=R0. Thus all angular flow maps and their inverses have uniform Lipschitz constants.

By Section 1 and V>=c_l r/2,

    ||theta -> 1/V(r,theta)-p/r||_(C^alpha) <= C_alpha r^(gamma-2).

Indeed the angular variation of V is O_Calpha(r^gamma), whereas the product of the two denominators in the reciprocal difference is bounded below by a constant times r^2. Composition with theta(r,beta) preserves the estimate because that map is uniformly Lipschitz. The bound is integrable in r. Consequently H(r,.) has a uniform C^alpha bound and converges uniformly to H_infinity in C^0. Its limit is C^alpha with the same bound. This is valid for every alpha<1.

The transported amplitudes

    A_r(beta)=R0^-p exp(H(r,beta)) rho(R0,beta)

are uniformly C^alpha. Composing with the uniformly Lipschitz inverse angular maps shows that B_r(theta)=r^-p rho(r,theta) is uniformly C^alpha. Their uniform limit Theta0 is therefore C^alpha. Moreover H_infinity and theta_infinity have the rates from the preceding proof. Composing the C^alpha amplitudes with inverse maps gives initially

    ||B_r-Theta0||_infinity <= C_alpha r^-alpha(1-gamma).

No derivative of Theta0 has been asserted.

## 3. Uniform estimates on rescaled annuli

The preceding angular estimates also control radial variation. At fixed beta,

    |partial_r H(r,beta)| <= C r^(gamma-2),
    |partial_r theta(r,beta)| <= C r^(gamma-2).

For r,s comparable to a large R, integration gives changes bounded by C R^(gamma-2)|r-s|. The inverse maps beta(r,theta) have the corresponding bound, since their angular derivatives are uniformly bounded. Combine these bounds with the uniform C^alpha dependence of H and A_r on beta. It follows that, on each fixed annulus a<=|Z|<=b,

    Z -> R^-p rho(RZ)=|Z|^p B_(R|Z|)(arg Z)

has uniformly bounded C^alpha norm. The factor R^(gamma-1) arising from a unit displacement in Z is bounded for R>=1. Uniform convergence on the same annulus follows from the already proved fixed-angle limit, uniformly at radii between aR and bR.

Also, the previous theorem gives the global bound |rho(X)|<=C(1+|X|)^p. Thus

    |q_R(Z)| <= C(R^-1+|Z|)^p <= C(1+|Z|)^p.

The same bound holds for q_infinity, which has the inherited parity.

## 4. Passing the full-plane inverse to the limit

Fix a compact query annulus. In the canonical kernel formula for q_R, split off a small disk of radius delta about each query. Subtract the value at the query there. The uniform local C^alpha estimate bounds this contribution by C delta^alpha, uniformly in R and the query. The same estimate holds for q_infinity.

Use the hybrid canonical formula: K(Z-Y) in the bounded origin-centered region, with the local query subtraction just described, and K(Z-Y)-K(-Y) only in the far exterior. The removed K(-Y) term integrates to zero on every origin-centered exterior annulus by central oddness. Thus no K(-Y) singularity is introduced at the origin. On the remaining bounded integration region, the kernel is nonsingular. The densities converge uniformly away from zero. A small disk about zero contributes arbitrarily little uniformly, because its distance from the queries is positive and the global bound in Section 3 bounds the density there. Dominated convergence, or this explicit small-disk removal followed by uniform convergence, handles that region.

In the far exterior use K(Z-Y)-K(-Y). Uniformly in the query, its magnitude is O(|Y|^-3). The density bound in Section 3 gives a tail bound C integral_L^infinity s^(p-2) ds, which tends to zero as L tends to infinity. The contact terms converge uniformly. Taking first the bounded-region limit, then delta to zero and L to infinity, proves uniform convergence of the canonical velocities on the query annulus.

The limiting density is homogeneous of degree p, locally C^alpha off zero and locally Holder at zero with some positive exponent, for example any exponent below min(p,alpha). Its parity and sublinear growth define the same canonical kernel inverse. At zero the symmetric angular cancellation gives velocity zero. A change of variables in the kernel integral proves U_infinity(lambda Z)=lambda^p U_infinity(Z) for lambda>0. The div-curl equations pass distributionally; uniqueness follows from the harmonic sublinear difference argument in the inverse proof.

Uniform convergence on the unit circle yields U=O(r^p). This improvement did not assume a gradient bound with exponent p.

## 5. The improved rate for the density

Return to the trajectory argument with the newly proved U=O(r^p). The tails in H and theta now have size O(r^(p-1)), because 1/V-p/r and Q/(rV) are O(r^(p-2)). The amplitudes A_r and their limit already have uniform C^alpha bounds from Section 2. The same composition argument therefore gives

    ||B_r-Theta0||_infinity <= C r^(p-1)+C_alpha r^-alpha(1-p)
                                  <= C_alpha_prime r^-alpha(1-p).

The relative error in B_r has exponent approaching p-1. After multiplication by r^p, this approaches, but does not reach, the formal second-power scale 2p-1 as alpha tends to one. It neither proves differentiability of Theta0 nor justifies substituting Theta0' into a classical second-term equation.

## Dependencies and scope

The proof uses only the canonical kernel and its first derivative bounds, the original first-derivative growth bound for rho, and the exact angular-Jacobian identity already proved. The local singular-integral Holder estimate is supplied by the three-region argument in Section 1. A careful review should check that estimate, the uniform radial/angle composition in Section 3, and the order of limits in Section 4. No general boundedness of a Riesz transform on arbitrary continuous functions is used. No topology of the interior characteristic flow or sign condition on rho away from the y-axis is assumed.
