# Explicit streamfunction from the Q ball

This is an analytic statement requiring no numerical certificate and making no existence assertion.

Let q>0, \(W_a(X)=\sqrt{1+a^2|X|^2}\), a>0, and let k be central odd with

\[
Q_a(k)=\|W_aJ^qk\|_2\le M.
\]

The unitary Fourier transform is \((2\pi)^{-1}\int e^{-iX\cdot\xi}k(X)\,dX\). Define

\[
\widehat{\psi_k}(\xi)=\frac{i\xi_1}{|\xi|^2}\widehat k(\xi)
\qquad(\xi\ne0).
\]

Then this defines an ordinary function in H^(q+1), and

\[
\boxed{\|J^q\psi_k\|_2\le M/a,\qquad
\|\psi_k\|_{H^{q+1}}\le\sqrt{1+a^{-2}}M.}
\]

Moreover

\[
-\Delta\psi_k=\partial_xk,\qquad
\nabla^\perp\psi_k=(-R_1R_2k,R_1^2k)=U[k],
\quad \nabla^\perp=(-\partial_y,\partial_x).
\]

## Proof of the low-frequency assertion

Put \(G(\xi)=J(\xi)^q\widehat k(\xi)\). The Q hypothesis implies

\[
G\in H^1(\mathbb R^2_\xi),\qquad
\|G\|_2^2+a^2\|\nabla_\xi G\|_2^2=Q_a(k)^2.
\]

Since J is radial, G is central odd. For almost every radius its angular Fourier series therefore contains only odd nonzero modes. Angular Poincare on the circle gives

\[
\int_0^{2\pi}|G(r,\theta)|^2d\theta
\le\int_0^{2\pi}|\partial_\theta G(r,\theta)|^2d\theta.
\]

Multiplication by \(r^{-1}dr\) and integration yield

\[
\int_{\mathbb R^2}\frac{|G(\xi)|^2}{|\xi|^2}d\xi
\le\int_{\mathbb R^2}|\nabla_\xi G|^2d\xi.
\tag{1}
\]

The inequality first holds for smooth central-odd functions supported away from zero and extends to central-odd H1 functions by density and lower semicontinuity. Equivalently one can apply the circular inequality on each annulus and then use monotone convergence; no value at the single origin frequency is needed.

The stream multiplier has magnitude at most \(|\xi|^{-1}\), so (1) proves

\[
\|J^q\psi_k\|_2^2
\le\|\nabla_\xi G\|_2^2\le M^2/a^2.
\]

Its joint gradient multiplier has norm \(|\xi_1|/|\xi|\le1\). Hence

\[
\|\nabla J^q\psi_k\|_2\le\|G\|_2\le M.
\]

The exact Bessel norm identity
\(\|\psi_k\|_{H^{q+1}}^2=\|J^q\psi_k\|_2^2+\|\nabla J^q\psi_k\|_2^2\)
proves the stated bound. Multiplication of the ordinary Fourier function by \(|\xi|^2\) or by the first-order derivative multipliers proves the elliptic and velocity identities in distributions.

Retaining the two terms jointly gives the sharper bound

\[
\|\psi_k\|_{H^{q+1}}^2\le\|G\|_2^2+\|\nabla_\xi G\|_2^2
\le\max(1,a^{-2})Q_a(k)^2.
\]

In particular \(\|\psi_k\|_{H^{q+1}}\le M\) whenever a>=1. This strengthens the displayed conservative bound without a new hypothesis.

## Application to the actual finite background

The exact unchanged potential formulas are

\[
\rho_{007}=-\Delta\partial_y\chi_{007},\qquad
u_{007}=(-\chi_{xyy},\chi_{xxy}),
\]

\[
h_*=-\Delta\phi,\qquad
U[h_*]=(-\phi_{xy},\phi_{xx}).
\]

Therefore the explicit background streamfunction is

\[
\psi_*=(\chi_{007})_{xy}+\phi_x.
\]

Direct differentiation gives \(-\Delta\psi_*=\partial_x\rho_*\) and
\(\nabla^\perp\psi_*=u_*\). For any Q-ball correction define

\[
\rho=\rho_*+k,\quad u=u_*+U[k],\quad\psi=\psi_*+\psi_k.
\]

These obey both elliptic equations exactly. If the independently established fixed-point equation supplies the stationary transport equation, the triple solves the full requested system. At a=2 the stronger correction bound is \(\|\psi_k\|_{H^{q+1}}\le M\); the earlier \(\sqrt5 M/2\) bound remains valid. For q=21/10 the correction streamfunction is C2,alpha for each alpha<1/10. Its L2 normalization fixes its additive constant.
