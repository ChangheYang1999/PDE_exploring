# A decaying velocity with an unbounded pressure mean

## Statement

There is a smooth divergence-free field on `R^3` for which both `U` and `DU` tend to zero but every smooth solution of its pressure Poisson equation has an unbounded spherical mean. The field is not a solution of the full similarity momentum equation for any `c>0` and any finite `omega`.

Thus pressure decay cannot be deduced from the Poisson equation and velocity decay, even after adding derivative decay. The assertion is a kinematic counterexample, not a counterexample to the profile conjecture or to canonical pressure normalization.

## Construction and velocity estimates

Put `R=|y|`, `rho^2=y_1^2+y_2^2`, and

\[
 f(R)=((1+R^2)\log(e+R^2))^{-1/2},\qquad U(y)=f(R)Jy.
\]

The scalar is a smooth function of `R^2`, so the vector field is smooth at zero. Its divergence is zero because `grad f` is radial and `Jy` is tangent to spheres. At infinity,

\[
 |U|\le Rf(R)\longrightarrow0,
 \qquad |DU|\le C(f+R|f'|)=O(R^{-1}(\log R)^{-1/2}).
\]

## Poisson source and the forced mean

Let `g=f^2`. Tangential differentiation leaves `f` unchanged, so

\[
 (U\cdot\nabla)U=f^2J^2y=-g(R)(y_1,y_2,0).
\]

Taking divergence gives

\[
 \partial_iU_j\partial_jU_i=-2g-\frac{\rho^2}{R}g'.
\]

Therefore the pressure equation is

\[
 \Delta P=2g+\frac{\rho^2}{R}g'.                 \tag{1}
\]

For the normalized mean `pbar(R)=(4pi)^-1 integral_(S^2) P(R theta) dtheta`, spherical averaging commutes with the Laplacian. Since the spherical mean of `rho^2` is `2R^2/3`,

\[
 (R^2\bar p')'=2R^2g+\tfrac23R^3g'
                   =\tfrac23(R^3g)'.
\]

Smoothness at the origin sets the integration constant to zero. Integrating again,

\[
 \bar p(R)=P(0)+\tfrac23\int_0^R
               \frac{s\,ds}{(1+s^2)\log(e+s^2)}.             \tag{2}
\]

The derivative of `(1/3) log log(e+R^2)` is `(2/3)R/((e+R^2)log(e+R^2))`. Its difference from the integrand in (2) is

\[
 \tfrac23(e-1)\frac{R}{(1+R^2)(e+R^2)\log(e+R^2)},
\]

which is integrable at infinity. It follows that

\[
 \bar p(R)=\tfrac13\log\log(e+R^2)+C+o(1)\longrightarrow+\infty.
\]

Any entire harmonic correction has constant spherical mean by the mean-value property. It cannot remove the divergence. In particular no pressure solving (1) can tend to a finite constant uniformly at infinity.

## Existence of the pressure

Let `h` denote the smooth right side of (1); it is `O(R^-2/log R)` at infinity. Choose a smooth radial cutoff `chi` equal to zero near zero and one outside a ball. Then

\[
 P(y)=-\frac1{4\pi}\int_{\mathbb R^3}
       \left(\frac1{|y-z|}-\frac{\chi(z)}{|z|}\right)h(z)\,dz
\]

is well-defined. For fixed `y` the difference of kernels is `O_y(|z|^-2)` at infinity. After multiplication by `h` and the radial volume element the tail is integrable. The Newtonian singularity at `z=y` is locally integrable. Applying the Laplacian in distributions yields `h`; local elliptic regularity gives a smooth representative. This supplies at least one smooth solution, so the mean assertion is not vacuous. It also applies to a smooth representative of the canonical pressure.

## Failure of the full profile equation

The field is equivariant under rotations about the third axis, so its rotation-generator term vanishes. The nonlinear acceleration has no azimuthal component. The remaining azimuthal part of the momentum equation is

\[
 (f+cRf')Jy+\frac1\rho\partial_\theta P\,e_\theta=0.
\]

On a fixed circle this requires `partial_theta P=-rho^2(f+cRf')`, a theta-independent value. A single-valued pressure has zero integral of its angular derivative, so `f+cRf'=0` for every `R>0`. For `c>0`, its nonzero solutions are `K R^-1/c`, inconsistent with the smooth positive `f` near zero. Thus the constructed velocity is not a profile.

## Dependencies and audit

The argument uses direct differentiation, spherical averaging, the harmonic mean-value property, the Newtonian fundamental solution and local elliptic regularity. It independently confirms LIT11 in the team records. It does not settle what additional pressure decay the full momentum equation might force.
