# A forcing Q bound without an inherited multiplier constant

Status: proved and independently reviewed. The scalar certificate is source_Q_from_integer_tensors.json; its producer verifies the rounded tensor inputs against the exact inherited rational energy uppers. This supersedes the use of cW in SOURCE_Q_NORM_BOUND.md, without changing the profile or any inherited file.

Let F be the actual residual, h=WF, W=sqrt(1+4r²), q=21/10. The inherited certified inputs are ||F||2<=7.961207e-7 and Tj=||D^j h||2², with containing uppers

T0<=.0000018314, T1<=.000004383, T2<=.00001049, T3<=.133465.

The ordered tensor convention is essential. The exact source metadata fixes Candidate013 and the same rational c. Every rounded inequality is checked by exact rational arithmetic against combined2's source013_moment_refinement certificate.

Put c0=W^-1. Direct radial differentiation gives

||Dc0||infty<=1, ||D²c0||F,infty<=6, ||D³c0||F,infty<=36.

For clarity the third tensor is
\[
(c_0)_{ijk}=48(\delta_{ij}x_k+\delta_{ik}x_j+\delta_{jk}x_i)W^{-5}
-960x_ix_jx_kW^{-7}.
\]
The ordered tensor norm of the first numerator is sqrt(12)r. Its separate radial maxima, at r=1/4 and r=sqrt(3)/4, give
\[
\|D³c_0\|_{\mathrm F,\infty}
\le \frac{768\sqrt{15}}{125}+\frac{5760\sqrt{21}}{2401}
<36.
\]
The Hessian eigenvalues have absolute value at most4, so its Frobenius norm is at most4sqrt(2)<6. The gradient maximum is4/(3sqrt(3))<1.

Tensor Leibniz and F=c0 h now yield
\[
d_3:=\|D³F\|_2\le
\sqrt{T_3}+3\sqrt{T_2}+18\sqrt{T_1}+36\sqrt{T_0}
<.461447731.
\]
Homogeneous Fourier interpolation with f2=||F||2 gives
\[
\|\nabla F\|_2\le d_1=f_2^{2/3}d_3^{1/3},\qquad
\|D²F\|_2\le d_2=f_2^{1/3}d_3^{2/3}.
\]
Thus d1<6.637841e-5 and d2<.005534453, independently of any CE or inverse-weight multiplier theorem.

For completeness the remaining source argument uses the explicit unit frame
nu=(1,2x,2y)/W. The integer product bounds proved in SOURCE_Q_NORM_BOUND.md are
\[
\|J²(\nu h)\|_2\le A_2=H_2+4d_1+12f_2,\quad
\|J³(\nu h)\|_2\le A_3=H_3+7d_2+130d_1+1391f_2,
\]
where H2²=T0+2T1+T2 and H3²=T0+3T1+3T2+T3. Their explicit frame derivative proof is unchanged; none of those steps uses cW.

Fourier differentiation of the quadratic weight gives
\[
\|WJ^qF\|_2²
=\|J^q(\nu h)\|_2²-8q\|J^{q-1}F\|_2²
-4q(q-2)\|\nabla J^{q-2}F\|_2².
\]
The last two terms are nonpositive. Spectral interpolation in the vector Hilbert space consequently gives
\[
\boxed{Q(F)\le A_2^{9/10}A_3^{1/10}
<.007589884556<759/100000<1/125.}
\]
Only the inherited actual source L2 and integer-tensor certificates enter. No background matrix, old Garding estimate, graph witness, or existence premise is used.
