# Explicit conversion from the auxiliary Q ball to the inherited N ball

Status: proved norm inequality with a scalar interval verification. This is a conditional statement about functions in the specified ball, not an existence assertion.

Let \(q=21/10=2+\delta\), \(\delta=1/10\), \(W_2=(1+4r^2)^{1/2}\), and \(W_a=(1+a^2r^2)^{1/2}\), \(0<a\le2\). If
\[
 \|g\|_2\le R,\qquad Q_a(g)=\|W_aJ^qg\|_2\le M,
\]
then, with \(r_0=R/M\),
\[
\boxed{\begin{aligned}
 \|J^q(W_2g)\|_2\le M\big[&
 2/a+2L_\delta r_0^{1/21}+4r_0^{10/21}\\
 &+8L_\delta r_0^{11/21}
 +8r_0^{20/21}+10L_\delta r_0\big],
\end{aligned}}
\]
where
\[
 L_\delta=\frac{\delta\sqrt\pi\,
 \Gamma((1-\delta)/2)}{2\Gamma(1-\delta/2)}
 =\frac{\sqrt\pi\,\Gamma(9/20)}{20\Gamma(19/20)}.
\]
In particular the executable verifies that \(a=5/4\), \(M=1/5\), \(R=4\cdot10^{-7}\) imply the inherited N norm is strictly below0.387.

## A bounded commutator requiring only a Lipschitz constant

The heat representation of the Bessel fractional power gives
\[
 J^\delta f=f+\frac{\delta/2}{\Gamma(1-\delta/2)}
 \int_0^\infty e^{-t}t^{-1-\delta/2}(f-e^{t\Delta}f)\,dt.
\]
For a Lipschitz scalar, vector, or matrix coefficient \(A\), the commutator kernel includes \(A(x)-A(y)\). The first moment of the two-dimensional heat kernel is \(\sqrt{\pi t}\). Therefore Young's inequality and the Gamma integral yield
\[
 \|[J^\delta,A]\|_{2\to2}\le L_\delta\operatorname{Lip}(A).
\]
This applies even to the unbounded Lipschitz weight \(W_2\), first on Schwartz functions and then as a bounded commutator extension. No nonexistent zeroth Fourier moment of the growing weight is used.

## Commuting the full q derivative

The exact identity is
\[
 [J^q,W_2]=[J^\delta,W_2]J^2+
 J^\delta[J^2,W_2],\qquad
 [J^2,W_2]g=-2DW_2\cdot\nabla g-(\Delta W_2)g.
\]
The explicit weight has
\[
 \|DW_2\|_\infty\le2,\quad
 \|D^2W_2\|_{\infty,op}\le4,\quad
 \|\Delta W_2\|_\infty\le8,\quad
 \|\nabla\Delta W_2\|_\infty\le10.
\]
The Hessian eigenvalues are \(4/W_2^3\) and \(4/W_2\). Also
\(\Delta W_2=4/W_2+4/W_2^3\), so
\[
 |\nabla\Delta W_2|\le16r/W_2^3+48r/W_2^5
 \le16/(3\sqrt3)+384/(25\sqrt5)<10.
\]
Apply the preceding fractional commutator inequality to \(DW_2\) and \(\Delta W_2\). It gives
\[
\begin{aligned}
\|[J^q,W_2]g\|_2\le{}&
 2L_\delta\|J^2g\|_2+4\|J^{1+\delta}g\|_2\\
&+8L_\delta\|\nabla g\|_2
 +8\|J^\delta g\|_2+10L_\delta\|g\|_2.
\end{aligned}
\]
The vector commutator for \(DW_2\) uses the Hessian operator-Lipschitz bound4 and the joint gradient norm, so no extra sum of coordinate norms appears.

Finally \(W_2\le(2/a)W_a\), and spectral L2 interpolation between0 and q gives all five powers of \(r_0\) in the box. The inequality first holds on Schwartz functions; the coordinate graph density and the resulting bound extend it to every function in the Qa ball. This supplies an explicit inherited high-norm radius whenever desired, while leaving the fixed physical exponent and center unchanged.
