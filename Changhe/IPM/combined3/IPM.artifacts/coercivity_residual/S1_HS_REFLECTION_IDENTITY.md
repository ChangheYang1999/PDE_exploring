# Exact S1 Hilbert–Schmidt reflection identity

This establishes a representation, not a new numerical S1 bound. The full-space kappa certificate and the numerical reflected correlations are separate tasks.

Use the unitary two-dimensional Fourier transform, so multiplication by a has Fourier integral kernel \(\widehat a(\xi-\eta)/(2\pi)\). Write \(\omega_\xi=\xi/|\xi|\) away from the measure-zero origin. For the gradient-structured self-adjoint remainder

\[
K=\tfrac12[R_1,[R_1,\rho_y]]-\tfrac12[R_1,[R_2,\rho_x]],
\]

its Fourier kernel is

\[
\widehat K(\xi,\eta)
=-\frac{i}{4\pi}G(\xi,\eta)\widehat\rho(\xi-\eta),
\]

\[
G(\xi,\eta)
=(\omega_{\xi,1}-\omega_{\eta,1})(|\xi|-|\eta|)
\det(\omega_\xi,\omega_\eta).
\]

Indeed, direct double-commutator expansion gives

\[
-\frac{i}{4\pi}(\omega_{\xi,1}-\omega_{\eta,1})
\{(\omega_{\xi,1}-\omega_{\eta,1})(\xi_2-\eta_2)
 -(\omega_{\xi,2}-\omega_{\eta,2})(\xi_1-\eta_1)\}
\widehat\rho(\xi-\eta).
\]

The expression in braces is the determinant of \(\omega_\xi-\omega_\eta\) and \(\xi-\eta\), equal to \((|\xi|-|\eta|)\det(\omega_\xi,\omega_\eta)\).

Let \(S_x=\mathrm{diag}(-1,1)\), \(S_y=\mathrm{diag}(1,-1)\), \(S_{xy}=-I\), and \((U_s f)(\xi)=f(s\xi)\). For an S1 background, \(\widehat\rho(S_xk)=\widehat\rho(k)\) and \(\widehat\rho(S_yk)=-\widehat\rho(k)\). The geometric factor changes with the complementary signs, so K commutes with both reflection operators. Thus the orthogonal S1 projector is

\[
P_{S1}=\tfrac14(I+U_{S_x})(I-U_{S_y}).
\]

For each reflection s define the real signed correlation

\[
C_s=\operatorname{Tr}(K^2U_s)
=\int\!\int\widehat K(\xi,\eta)
\overline{\widehat K(\xi,s\eta)}\,d\xi\,d\eta.
\]

Self-adjointness and the reflection commutation justify the second equality. Cauchy–Schwarz gives \(|C_s|\le\|K\|_{HS}^2\), but C_s need not be nonnegative. The exact restricted norm is

\[
\boxed{\|K P_{S1}\|_{HS}^2
=\tfrac14(\kappa^2+C_{S_x}-C_{S_y}-C_{S_{xy}}).}
\]

Equivalently,

\[
C_s=\frac1{16\pi^2}\int\!\int
G(\xi,\eta)G(\xi,s\eta)
\widehat\rho(\xi-\eta)\overline{\widehat\rho(\xi-s\eta)}\,d\xi\,d\eta.
\]

For compact smooth profiles all Fourier manipulations are ordinary integral identities. For the actual sublinear background, first take symmetric smooth cutoffs. The inherited HS identity applied to profile differences gives convergence of K in the HS norm when the Hessians converge in L². Therefore the reflected correlations and the boxed identity pass to the limit. A future numerical Fourier calculation must implement this approximation or justify a distributional Fourier representation; simply treating the growing density as an L² Fourier function is invalid.

## Reducing the two single-reflection correlations

For s=S_x introduce \(k=(a,t)=\xi-\eta\), \(\ell=(b,t)=\xi-S_x\eta\), and \(z=\eta_2\). Then

\[
\xi=((a+b)/2,z+t),\qquad\eta=((b-a)/2,z),
\]

with Jacobian \(d\xi\,d\eta=\frac12\,da\,db\,dt\,dz\). This isolates the source product \(\widehat\rho(a,t)\overline{\widehat\rho(b,t)}\) from one universal geometric z integral. The S_y case similarly shares the first frequency coordinate. For s=−I use \(\xi=(k+\ell)/2\), \(\eta=(\ell-k)/2\), with Jacobian1/4. These are exact reductions; no reflected correlation has yet been numerically certified.
