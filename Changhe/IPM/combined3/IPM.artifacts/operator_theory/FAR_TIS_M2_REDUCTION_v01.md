# TIS needs only a second Fourier moment in the p norm

Let S be a real symmetric matrix coefficient with an ordinary measurable Fourier transform and finite
\[
M_2(S)=(2\pi)^{-2}\int|\zeta|^2\|\widehat S(\zeta)\|_{\mathrm{op}}\,d\zeta.
\]
For every test G, with \(v=\mathcal RG\), \(p=J^{-1}\), \(m=|D|J^{-1}\), and \(n=1-m\), the exact form is
\[
T_{IS}(S;G)=q[\langle Snv,nv\rangle+\langle Spv,pv\rangle-2\langle Sv,nv\rangle].
\]
Then
\[
\boxed{|T_{IS}(S;G)|\le\frac q2M_2(S)\|pG\|_2^2.}
\tag{1}
\]
This improves the earlier sufficient moment bound involving \(3M_2+2M_4\). It makes no numerical assertion about the actual moment.

For a complete proof, polarize the form in Fourier variables \(\xi,\eta\), and put \(r=|\xi|\), \(t=|\eta|\), \(J_r=\sqrt{1+r^2}\). The scalar multiplier multiplying \(\widehat S(\xi-\eta)\) is exactly
\[
n(r)n(t)+p(r)p(t)-n(r)-n(t)
=m(r)m(t)+p(r)p(t)-1
=-\frac{J_rJ_t-rt-1}{J_rJ_t}.
\]
The nonnegative numerator satisfies the exact rationalization identity
\[
J_rJ_t-rt-1=\frac{(r-t)^2}{J_rJ_t+rt+1}
\le\frac{|\xi-\eta|^2}{2}.
\]
Replace the two G factors divided by Jr,Jt by the Fourier factors of pG. The Riesz-direction vectors at xi and eta have norm one almost everywhere, so their contraction with the matrix coefficient is at most its operator norm. Young's convolution inequality, followed by Plancherel, proves (1) with precisely the displayed normalization. Points xi=0 or eta=0 are null sets.

For \(S_f=(1-\chi)\operatorname{Sym}Du_*\), exact structure gives all required qualitative Fourier premises. A practical certified upper follows from full-plane Frobenius derivative norms:
\[
M_2(S_f)\le\left(\frac{D_2D_4+D_3^2}{2\pi}\right)^{1/2},\quad
D_j=\||D|^jS_f\|_{L^2,\mathrm F}.
\tag{2}
\]
The scalar NR-25 Cauchy--Schwarz proof applies verbatim to the vector of matrix entries, using operator norm <= Frobenius norm. It requires no finite D0 norm: the weighted Fourier quantity |zeta|² S_fhat is L2, which is supplied by D2; the same frequency Cauchy--Schwarz weights used in NR-25 are then integrable. The physical derivative norms are \(D_2=\|\Delta S_f\|_{2,F}\), \(D_3=\|\nabla\Delta S_f\|_{2,F}\), \(D_4=\|\Delta^2S_f\|_{2,F}\).

The exact finite angular representation reduces those norms to radial integrals, with no angular truncation. Computing and rigorously enclosing them is a new obligation; a floating-point quadrature screen is not a certificate.
