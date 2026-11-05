## Fresh high-order certification: a direct integer Sobolev estimate

Let \(q=21/10\) and \(V=(F,2xF,2yF)\). Write
\[
E_m=\|J^mV\|_2^2,\qquad J=(1-\Delta)^{1/2}.
\]
No historical tensor-energy enclosure or weight multiplier constant is needed.
Under the weighted \(H^3\) membership proved by the regional estimates,
Fourier differentiation and integration by parts give
\[
Q(F)^2=\|J^qV\|_2^2
-8q\|J^{q-1}F\|_2^2
-4q(q-2)\|\nabla J^{q-2}F\|_2^2.
\]
Both subtracted terms are nonnegative. Hölder's inequality in the vector
Fourier space therefore gives the rigorously applicable implication
\[
\boxed{Q(F)\le E_2^{9/20}E_3^{1/20}.}
\]
The identity first holds for smooth compactly supported functions. Approximation
in the norm consisting of all \(\|D^\alpha F\|_2+\||X|D^\alpha F\|_2\),
\(|\alpha|\le3\), gives the displayed identity and inequality for this source.
Equivalently one may work directly with the distributional Fourier derivatives.

### Positive modal integrands on the finite radial region

Exact symmetry of the sources gives
\(F(r,\theta)=\sum_{n>0,\ n\text{ odd}}f_n(r)\sin(n\theta)\), a finite sum.
For one such mode set
\[
g_n=f_n-f_n''-f_n'/r+n^2f_n/r^2,
\]
\[
g_n'=f_n'-f_n'''-f_n''/r+(1+n^2)f_n'/r^2-2n^2f_n/r^3,
\]
\[
a_{n,\pm}=r g_n-2f_n'\pm2nf_n/r,
\quad
a_{n,\pm}'=g_n+r g_n'-2f_n''
\pm2n(f_n'/r-f_n/r^2).
\]
Then exactly
\[
E_2=\pi\sum_n\int_0^\infty r\left[g_n^2+
2(a_{n,+}^2+a_{n,-}^2)\right]dr,
\]
\[
E_3=\pi\sum_n\int_0^\infty r\left[
g_n^2+(g_n')^2+n^2g_n^2/r^2+
2\sum_{\sigma\in\{-1,1\}}
\left(a_{n,\sigma}^2+(a_{n,\sigma}')^2+
(n+\sigma)^2a_{n,\sigma}^2/r^2\right)\right]dr.
\]
These formulas follow from \(E_2=\|(1-\Delta)V\|_2^2\) and
\(E_3=E_2+\|\nabla(1-\Delta)V\|_2^2\).
For \(2xF\), the two shifted sine amplitudes are \(rf_n\); for \(2yF\),
the shifted cosine amplitudes have opposite signs. Their cross terms cancel
between the two coordinate components, including overlaps from neighboring
values of \(n\). The zero cosine mode at \(n=1\) has angular integral \(2\pi\),
which is exactly accounted for by the factor 2; its sine partner is zero.
Thus the formulas also cover this endpoint mode without exception.

On a panel \([c-h,c+h]\), the code encloses each \(f_n^{(d)}\),
\(0\le d\le3\), using its exact-source Arb Taylor coefficients to degree
\(K\). If \(M\) bounds its modulus on a complex disk of radius \(R>2h\),
put \(z=h/R\). A containing derivative remainder is
\[
\frac{M}{R^d}\frac{(K+1)!}{(K+1-d)!}
\frac{z^{K+1-d}}{1-2z}.
\]
Indeed each successive differentiated Taylor-tail term has ratio at most
\(2z\) when \(K\ge2d\). Horner interval evaluation of the polynomial,
followed by this remainder and the displayed positive integrands, bounds
its panel integral by interval supremum times the exact width \(2h\).
All final panel upper endpoints are stored as exact rational numbers.

### Endpoint derivative envelopes

Suppose an endpoint region has fresh containing upper bounds
\(N_j\ge\|D^jF\|_2\) and \(B_j\ge\||X|D^jF\|_2\), for the full ordered
Cartesian tensors and \(0\le j\le3\). The coordinate product rule gives
\[
\|D^jV\|_2\le L_j:=N_j+2B_j+2\sqrt{j(j+1)}N_{j-1},
\]
where the last term is zero for \(j=0\).
For the last term, the full ordered Frobenius norm of
\(\sum_{\ell=1}^j\delta_{i,k_\ell}D^{j-1}F\) is exactly
\(\sqrt{j(j+1)}|D^{j-1}F|\); this follows by summing diagonal and cross
Kronecker contractions. An independently simpler containing coefficient
\(2j\sqrt2\) is also valid.

On the whole plane the integer Bessel energies are binomial sums of ordered
tensor energies. For a regional upper bound one should not simply replace
\(\|(1-\Delta)V\|_2^2\) by such a binomial sum, because the regional
integration-by-parts identity would acquire boundary terms. Instead the
pointwise differential formula gives the safe regional bounds
\[
\|(1-\Delta)V\|_{2,\Omega}\le L_0+\sqrt2 L_2,
\]
\[
\|\nabla(1-\Delta)V\|_{2,\Omega}\le L_1+\sqrt2 L_3.
\]
Thus its contributions are bounded by
\[
E_{2,\Omega}\le(L_0+\sqrt2L_2)^2,
\quad
E_{3,\Omega}\le(L_0+\sqrt2L_2)^2+(L_1+\sqrt2L_3)^2.
\]
These inequalities use only tensor contraction and the triangle inequality,
so they are valid separately on the origin disk and infinite exterior.
They add directly to the finite-region positive modal integrals.
