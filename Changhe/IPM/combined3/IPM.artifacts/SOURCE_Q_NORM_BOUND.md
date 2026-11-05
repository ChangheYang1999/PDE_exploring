# A certified source upper in the auxiliary norm Q(f)=||W Jq f||

Status: analytic bound and scalar verification. It inherits the expressly listed source tensor and multiplier bounds from combined2. It supplies no background coercivity or existence assertion.

Write \(q=21/10\), \(h=WF_*\), \(f=\|F_*\|_2\), \(n=\|J^qh\|_2\), and \(K=\||D|^qF_*\|_2\). The inherited multiplier bound gives \(K\le(9619/5000)n\). Put
\[
d_j=f^{1-j/q}K^{j/q},\qquad j=1,2.
\]
Fourier interpolation proves \(\|\nabla F_*\|_2\le d_1\), \(\|\nabla^2F_*\|_2\le d_2\).
Let \(T_j=\||D|^jh\|_2^2\), for j=0,1,2,3, using the full tensor convention. Then
\[
H_2=(T_0+2T_1+T_2)^{1/2}=\|J^2h\|_2,\qquad
H_3=(T_0+3T_1+3T_2+T_3)^{1/2}=\|J^3h\|_2.
\]

Define the unit vector field
\[
\mathbf b(X)=\frac{(1,2x,2y)^T}{W(X)},\qquad |\mathbf b|=1.
\]
For \(\widetilde T_s=\|J^sF_*\|_2^2+4\sum_j\|J^s(x_jF_*)\|_2^2\), one has
\(\widetilde T_s^{1/2}=\|J^s(\mathbf b h)\|_{L^2(\mathbb R^2;\mathbb R^3)}\).
The following deliberately coarse integer estimates suffice:
\[
\boxed{\widetilde T_2^{1/2}\le A_2:=H_2+4d_1+12f,\qquad
\widetilde T_3^{1/2}\le A_3:=H_3+7d_2+130d_1+1391f.}
\tag{1}
\]

## Explicit derivative constants and proof of (1)

The normalization map b satisfies
\[
\|WDb\|_{\mathrm{op}}\le2,\quad W|Db|_{\mathrm F}\le3,
\quad W|\Delta b|\le8,\quad W|D^2b|_{\mathrm F}\le48,
\quad W|D^3b|_{\mathrm F}\le864.
\tag{2}
\]
For the first two, its induced metric is \(4W^{-2}I-16W^{-4}XX^T\). For the Laplacian bound, setting t=4r² gives
\[
W^2|\Delta b|^2
=16(t^3+9t^2+12t+4)/(1+t)^4\le64,
\]
since the difference of \(4(1+t)^4\) and the numerator polynomial is \(4t+15t^2+15t^3+4t^4\ge0\).
For the last two bounds differentiate a=W−1:
\[
a_i=-4x_iW^{-3},\quad a_{ij}=-4\delta_{ij}W^{-3}+48x_ix_jW^{-5},
\]
\[
a_{ijk}=48(\delta_{ij}x_k+\delta_{ik}x_j+\delta_{jk}x_i)W^{-5}
-960x_ix_jx_kW^{-7}.
\]
The product rule for b=(1,2x,2y)a and \(|x_i|/W\le1/2\) bounds each weighted vector second derivative by 24 and each third derivative by 288. There are respectively four and eight ordered spatial derivatives; hence their Frobenius norms are at most 48 and \(288\sqrt8<864\). These bounds include all vector components.
Also \(|\nabla\log W|\le1\), \(|\nabla W|\le2\), \(|D^2W|_{\mathrm F}\le6\), and \(\Delta W/W\le8\).

Expand
\[
J^2(bh)=bJ^2h+E_2,\qquad E_2=-2Db\nabla h-(\Delta b)h.
\]
Using \(\nabla h=W(\nabla F_*+F_*\nabla\log W)\), (2) gives
\(\|E_2\|_2\le4d_1+12f\), proving the first inequality of (1).
Differentiating the displayed E2 identity gives four terms,
\[
\nabla E_2=-2D^2b\nabla h-2DbD^2h-(\nabla\Delta b)h-(\Delta b)\nabla h.
\]
The weighted derivative bounds and \(W|\nabla\Delta b|\le\sqrt2\,864<1224\) prove
\[
\|\nabla E_2\|_2\le4d_2+120d_1+1352f,
\quad\|E_2\|_{H^1}\le4d_2+124d_1+1364f.
\]
Since b is a unit vector, its gradient cross term cancels, yielding
\[
\|bJ^2h\|_{H^1}\le H_3+3\|W^{-1}J^2h\|_2
\le H_3+3d_2+6d_1+27f.
\]
Adding these estimates proves the second inequality in (1).

## Fractional interpolation and the exact weighted Fourier identity

Componentwise spectral interpolation gives
\[
\widetilde T_q\le\widetilde T_2^{3-q}\widetilde T_3^{q-2}.
\]
Fourier differentiation of the exact quadratic weight \(W^2=1+4r^2\), followed by integration by parts, gives
\[
\boxed{\|WJ^qF_*\|_2^2
=\widetilde T_q-8q\|J^{q-1}F_*\|_2^2
-4q(q-2)\|\nabla J^{q-2}F_*\|_2^2\le\widetilde T_q.}
\tag{3}
\]
For example at q=2 the correction is exactly \(-16\|JF_*\|_2^2\). The identity can first be proved for Schwartz inputs, then extended by density in the integer vector norms just bounded. It uses no pointwise substitution for a Riesz transform.

Combining (1)–(3) proves the concrete source estimate
\[
\boxed{Q(F_*)\le A_2^{9/10}A_3^{1/10}.}
\]
The companion Arb calculation verifies the stated rational outward bound. Source tensor inputs are rounded upward from combined2 `theory_audit/research/source013_moment_refinement/verification/result_v01.json` and retain that certificate's scope. This lemma is intended for the new auxiliary Q-norm argument; it does not alter the original Candidate 013 profile or exponent.
