# A certified Gaussian high-frequency Hilbert–Schmidt bound for Cvs3

Status: proved universal operator estimate, including a completed interval certificate for its dimensionless constant. The actual Candidate013 derivative norm is a separate input; no total IPM coercivity or existence is asserted.

For \(P_\mu=e^{\Delta/(2\mu^2)}\), the actual gradient-source operator satisfies
\[
 \boxed{\|C_{vs3}(I-P_\mu)\|_{\rm HS}
 \le\frac{\||D|^3\rho_*\|_2}{4\pi\sqrt3\,\mu}.}
\]
Consequently
\[
 \boxed{|C_{vs3}[G]-C_{vs3}[P_\mu G]|
 \le\frac{\||D|^3\rho_*\|_2}{2\pi\sqrt3\,\mu}\|G\|_2^2.}
\]
The statements apply to the full coefficient \(b=\nabla\rho_*\). Multiplying \(b\) by a spatial cutoff generally destroys its gradient structure, so the boxed constant is not silently asserted for that different operator.

## Exact Fourier reduction

Use the unitary Fourier transform in two dimensions and \(R_j\) symbol \(-i\xi_j/|\xi|\). Put
\[
 K=\begin{pmatrix}-\rho_y&\rho_x/2\\\rho_x/2&0\end{pmatrix},
 \qquad C_{vs3}=-\tfrac12\sum_{j,k}[R_j,[R_k,K_{jk}]].
\]
For \(\zeta=\xi-\eta\), \(d=\xi/|\xi|-\eta/|\eta|\), its Fourier kernel, up to an irrelevant global sign, is
\[
 \frac1{4\pi}d^T\widehat K(\zeta)d
 =\frac{i\widehat\rho(\zeta)}{4\pi}
 d_1(\zeta_1d_2-\zeta_2d_1).
\]
Rotate coordinates so that \(\zeta=s e_1\). If its direction in the original coordinates is \(\varphi\), then
\(d_1^{\rm original}=\cos\varphi\,d_x-\sin\varphi\,d_y\). Reflection in the new second coordinate makes the integral of \(d_xd_y^3\) vanish. Thus the inner frequency integral is bounded by \(s^2|\widehat\rho(\zeta)|^2\) times the larger of
\[
 I_\parallel(s)=\int d_x^2d_y^2(1-e^{-|\eta|^2/(2\mu^2)})^2\,d\eta,
 \quad
 I_\perp(s)=\int d_y^4(1-e^{-|\eta|^2/(2\mu^2)})^2\,d\eta.
\]
The completed universal certificate proves
\[
 \boxed{\max(I_\parallel(s),I_\perp(s))
 \le\frac{s^4}{3\mu^2}\quad(s>0).}
\]
Substituting this bound into the squared Fourier-kernel integral gives the first operator box, because
\(\int|\zeta|^6|\widehat\rho|^2=\||D|^3\rho\|_2^2\).
Self-adjointness and
\(C-PCP=(I-P)C+PC(I-P)\) give the second box.

For Candidate013 the density itself grows mildly at infinity. The reduction is still justified by smooth cutoffs \(\rho_N\): its exact far expansion gives \(D^j\rho=O(r^{1-\gamma-j})\), \(\gamma>0\), so \(D^3(\rho_N-\rho)\to0\) in L2. The boxed estimate makes the high-frequency commutators Cauchy in HS norm. Their distributional limit is the desired actual-coefficient commutator, since all fixed multipliers and the smooth coefficient products converge on Schwartz tests. Constant or linear distribution ambiguities at zero frequency are annihilated by the double commutator.

## Universal interval certificate

Scale to \(\mu=1\), write \(a=s\), \(\eta=r(\cos\theta,\sin\theta)\), \(u=a/r\), and
\[
 D=(1+u^2+2u\cos\theta)^{1/2}.
\]
The stable exact component formulas are
\[
 d_x=\frac{u}{D}\left[1-\frac{(u+2\cos\theta)\cos\theta}{1+D}\right],
 \quad
 d_y=-\frac{u(u+2\cos\theta)\sin\theta}{D(1+D)}.
\]
The displacement is horizontal, so \(|d_x|\le2\) and \(|d_y|\le1\). The latter fact uses that the two second coordinates have the same sign before and after normalization. At intervals containing the removable/single-point Riesz singularity the certificate uses precisely these safe bounds. Elsewhere Arb encloses the displayed formulas. The positive decomposition
\[
 D^2=(1-u)^2+2u(1+\cos\theta)
\]
avoids false negative lower endpoints caused by cancellation.

The finite parameter range \(10^{-4}\le a\le20\) is covered by251 exact rational intervals with ratio21/20. On each interval the radial range \(10^{-8}\le r\le100\) has the same ratio21/20, and \(0\le\theta\le\pi\) is covered by128 Arb arcs. Reflection doubles that angular half-plane. Gaussian factors are bounded at the upper radial endpoint; the polar radial measure is integrated exactly as \((r_{\rm hi}^2-r_{\rm lo}^2)/2\); \(a^{-4}\) is bounded at the lower parameter endpoint. The tiny omitted disk contributes at most \(\pi r_{\min}^6/(3a_{\min}^4)\). For the large omitted radii,
\[
 |d|\le2a/r,\qquad
 a^{-4}\int_{r\ge R}|d|^4\,d\eta\le16\pi/R^2.
\]
All251 interval records pass. Their largest upper bound is less than0.312180, hence strictly below1/3.

The unbounded parameter regimes are analytic. If \(a\ge20\), then
\[
 \int|d|^4\,d\eta\le32\pi a^2,
 \qquad I/a^4\le32\pi/a^2\le0.251328.
\]
If \(0<a\le10^{-4}\), split at \(r=10a\). In the inner disk use \(|d_xd_y|^2\le4\), \(d_y^4\le1\), and \(1-e^{-r^2/2}\le r^2/2\). Their common upper bound after division by \(a^4\) is \((\pi/3)10^6a^2\).

On \(r\ge10a\), Taylor-expand the unit-vector map along the horizontal segment. Its second directional derivative has vector modulus at most \(2/(\sqrt3\,r^2)\). Along the segment the radius is at least \(0.9r\); hence
\[
 d_x=(a/r)\sin^2\theta+e_x,\quad
 d_y=-(a/r)\sin\theta\cos\theta+e_y,\quad
 |e|\le c(a/r)^2,\quad c=100/(81\sqrt3).
\]
Writing \(\varepsilon=c/5+c^2/100\), angular L2 triangle inequalities bound both product integrals by
\[
 (a/r)^4\left[\sqrt{5\pi/64}+\sqrt{2\pi}\,\varepsilon\right]^2.
\]
The angular fourth-degree leading constants are \(5\pi/64\) and \(3\pi/64\), so the first is a valid common bound. Finally,
\[
 \int_0^\infty(1-e^{-r^2/2})^2r^{-3}\,dr=\tfrac12\log2.
\]
The resulting small-parameter upper bound is less than0.270078. It too lies below1/3.

The producer is certify_Cvs3_Gaussian_HS_constant.py, with complete records in Cvs3_HS_universal_v01. The separate consumer verify_Cvs3_HS_one_third.py checks every saved interval, exact parameter coverage, producer/result hashes, and both analytic regimes against1/3. Its output Cvs3_HS_one_third_verified.json records the exact adopted constant. Candidate013's remaining actual derivative-norm certificate is produced separately.
