# Weighted Beurling estimate on centrally odd functions

Status: proved homogeneous and inhomogeneous weighted velocity bounds. These are auxiliary operator estimates, not a stationary-existence certificate.

For real scalar \(f(-x)=-f(x)\), and \(0\le\alpha<2\),
\[
 \boxed{\|r^\alpha U[f]\|_2\le\frac{2}{2-\alpha}\|r^\alpha f\|_2.}
\]
For \(W=(1+4r^2)^{1/2}\) and \(1\le\alpha<2\), this implies
\[
 \boxed{\|W^\alpha U[f]\|_2\le
 2^{(\alpha-1)/2}\frac{2}{2-\alpha}\|W^\alpha f\|_2.}
\]

Here \(U=(-R_1R_2,R_1^2)\). The estimates concern real scalar inputs with the stated central symmetry. The S1 space is contained in that class.

To prove them, write the Beurling transform \(B=\partial\bar\partial^{-1}\), with Fourier symbol \(e^{-2i\theta}\). For a homogeneous angular mode \(r^\lambda e^{im\theta}\), direct polar differentiation gives
\[
 B(r^\lambda e^{im\theta})
 =\frac{\lambda+m}{\lambda-m+2}r^\lambda e^{i(m-2)\theta}.
\]
Weighted Mellin Plancherel uses the vertical line
\(\lambda=-1-\alpha+i\tau\). Thus its multiplier modulus squared is
\[
 \frac{(m-1-\alpha)^2+\tau^2}{(m-1+\alpha)^2+\tau^2}.
\]
Central oddness restricts \(m\) to odd integers, so \(m-1\) is even. For \(0\le\alpha<2\), the supremum over those integers and real \(\tau\) is
\[
 \|B\|_{L^2(r^{2\alpha})\to L^2(r^{2\alpha})}
 =\frac{2+\alpha}{2-\alpha}.
\]
The exceptional \(m=1\) ratio has modulus one. The supremum arises from the nearest nonzero even integer of the unfavorable sign and \(\tau=0\). This calculation can first be made on smooth functions compactly supported in \(0<r<\infty\), using angular Fourier series and the unitary Mellin transform, and then extended by density. There is no assertion on all parity sectors when \(\alpha\ge1\).

For real \(f\), the complex velocity satisfies the exact Fourier-multiplier identity
\[
 U_2[f]+iU_1[f]=-\tfrac12(f+Bf).
\]
Its complex absolute value is the Euclidean velocity norm. The triangle inequality and the preceding Beurling norm give the homogeneous boxed bound.

Finally, with \(s=4r^2\) and \(1\le\alpha<2\),
\[
 1+s^\alpha\le(1+s)^\alpha\le2^{\alpha-1}(1+s^\alpha).
\]
Apply the unweighted velocity bound \(\|U f\|_2\le\|f\|_2\) and the homogeneous estimate to the two terms in the upper bound, then use the lower bound on the input. This proves the inhomogeneous boxed estimate and records the exact weight convention.
