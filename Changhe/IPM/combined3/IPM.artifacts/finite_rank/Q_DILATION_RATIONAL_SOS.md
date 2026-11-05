# A rational improvement of global Q-norm dilation damping

Status: proved on S1. This strengthens the independent half and two-thirds bounds without any background-field numerics.

Write \(\ell=\nabla\log W\), \(W^2=1+4r^2\), and set \(t=r^2\). The exact polynomial identity
\[
\begin{aligned}
16t^3-\frac{3196}{125}t^2+9t+1
={}&16t\left(t-\frac{21}{25}\right)^2\\
&+\frac{164}{125}\left(t-\frac{1431}{1640}\right)^2
+\frac{2239}{2050000}
\end{aligned}
\]
is verified using rational coefficients by the companion script. Every term on the right is nonnegative for \(t\ge0\). Consequently, with \(k=1549/500\),
\[
 1+\frac1t-k|\ell|^2
 =\frac{16t^3-(3196/125)t^2+9t+1}{t(1+4t)^2}\ge0.
\]

For S1 functions angular Poincare gives
\(\|f/r\|_2^2\le D_{\rm ang}(f)^2\). Define
\[
 E(f)=\|\ell f\|_2,\qquad
 H_0[f]=D_{\rm rad}(f)^2+D_{\rm ang}(f)^2+\|f\|_2^2-E(f)^2.
\]
The preceding pointwise inequality yields
\[
 H_0[f]\ge D_{\rm rad}(f)^2+(k-1)E(f)^2.
\]
The skew form of \(M=WJ^2W^{-1}\) is
\[
 B_0(f,h)=\langle\ell\partial_rf,h\rangle-\langle\ell f,\partial_rh\rangle.
\]
Thus
\[
 |B_0(f,h)|\le D_{\rm rad}(f)E(h)+E(f)D_{\rm rad}(h)
 \le\frac{\sqrt{H_0[f]H_0[h]}}{\sqrt{k-1}}.
\]
Here the final inequality is the norm of the two-dimensional off-diagonal matrix after scaling the \(E\) coordinate by \(\sqrt{k-1}\).

As in the bounded-form argument in QNORM_BACKGROUND_IDENTITY.md, let \(V=J^{-1}MJ^{-1}=H+B\). Then \(H\le I\), and
\(A=H^{-1/2}BH^{-1/2}\) is skew-adjoint with \(\|A\|\le1/\sqrt{k-1}\). The exact inverse identity gives
\[
 \operatorname{Re}V^{-1}
 =H^{-1/2}(I-A^2)^{-1}H^{-1/2}
 \ge\frac{k-1}{k}H^{-1}\ge\frac{k-1}{k}I.
\]
Therefore
\[
 \boxed{\operatorname{Re}\langle WJ^{-2}W^{-1}G,G\rangle
 \ge\frac{1049}{1549}\|J^{-1}G\|_2^2\qquad(G\in S1).}
\]
The gain in this coefficient over \(2/3\) is exactly \(49/4647\). Multiplying by \(qc\) is legitimate because the fixed parameters have \(q,c>0\). This remains a global favorable damping allowance; its later allocation between terms of the stationary problem must be documented separately.
