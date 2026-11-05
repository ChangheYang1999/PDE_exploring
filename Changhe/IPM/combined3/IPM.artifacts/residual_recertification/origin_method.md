# Fresh origin certificate

The adopted origin region is the closed disk \(r\le R_o=1/1000\).
Its fresh source-derived bounds are
\[
\int_{r\le R_o}|F|^2<1.939250900121531\,10^{-25},
\]
\[
E_{2,o}:=\int_{r\le R_o}|(1-\Delta)G|^2
 <1.581805452196423\,10^{-11},
\]
\[
E_{3,o}:=\int_{r\le R_o}
 (|(1-\Delta)G|^2+|\nabla(1-\Delta)G|^2)
 <1.599795660385484\,10^{-5},\qquad G=(F,2xF,2yF).
\]
Exact containing dyadic endpoints, rather than these rounded displays,
are in `origin_large_certificate.json`.

## Potential coefficients and their analytic remainder

Each grouped exact potential is
\(r^n A(r^2)\cos(n\theta)\) or
\(r^n A(r^2)\sin(n\theta)\), where
\[
A(s)=(1+s)^b(t+s)^{-v}P\left(\frac{s}{t+s}\right),\qquad t\ge1/8.
\]
All source coefficients and all finite coefficients of the degree-16
Taylor expansion of \(A\) are evaluated exactly over the rationals.
The circle \(|s|=\eta=1/32\) lies strictly inside the common domain
of analyticity.  Bounding the grouped polynomial by Horner evaluation
with absolute coefficients and using \(|t+s|\ge t-\eta\),
\(|1+s|\ge1-\eta\), supplies an explicit upper \(M\) for \(|A|\).
Cauchy gives \(|a_k|\le M\eta^{-k}\).

For a Cartesian derivative of order \(d\), the Fourier coefficient
\(\ell^1\) norm of a differentiated homogeneous harmonic is bounded
by \((2n+2k+d)^d\).  With \(N=17\ge2d\) and
\(z=R_o^2/\eta<1/4\), the consecutive majorants of the omitted terms
have ratio at most \(2z\).  Thus the differentiated omitted series
is bounded uniformly by
\[
\frac{M(2n+2N+d)^d}{\eta^N(1-2z)}
 R_o^{n+2N-d}.
\]
The two Laplacian terms are included separately for the density.
The program retains field derivatives through density order four and
velocity order three, sufficient for three residual derivatives.

`origin_certificate.py` regenerates and saves the complete grouped finite
field coefficient enclosures and the remainder coefficient enclosures.
Its default disk is smaller, but its saved finite coefficients do not
depend on that disk.  To enlarge the disk, the new program multiplies
the saved remainder coefficient by \((1-2z)^{-1}\).  The old saved
coefficient already contains a geometric factor greater than one; retaining
that factor is conservative.  It does not assume the smaller disk's final
field bounds remain valid on the larger disk.

## Residual cancellation and complete error accounting

The exact low residual polynomial is reconstructed directly from the
source potentials using
\[
F=c\,r\partial_r\rho-\rho+u_1\rho_x+u_2\rho_y.
\]
Keeping residual powers through 10 requires only potential harmonics
through 13 and radial Taylor index through six.  The scalar field is odd
under central reflection, so there are no even residual powers.  The
linear residual cancels exactly.  Fourteen nonzero coefficients remain;
the first power is three.  Rational Fourier convolutions preserve every
low-order cancellation before any interval rounding.

The complete degree-16 field polynomials also produce a bound for every
omitted finite residual power \(p>10\).  Dilation contributes
\(|cp-1|\) times the density coefficient absolute sum.  Each nonlinear
product contributes the convolution of the two field coefficient
absolute sums.  A homogeneous term of degree \(p\) is a regular
polynomial in Cartesian coordinates: initially this follows from
\(r^n e^{in\theta}=(x+iy)^n\) and the Taylor expansion in \(r^2\),
and Cartesian differentiation preserves it.  Hence its angular harmonic
degree is at most \(p\), with the same parity.  Each differentiation has
Fourier \(\ell^1\) operator norm at most the current polynomial degree.
An order-\(j\) derivative of an omitted term therefore has absolute
upper \((p)_j R_o^{p-j}\) times its saved coefficient upper.

If \(P_\alpha,E_\alpha\) bound the finite field and analytic tail
derivatives, respectively, the analytic error of a product derivative
is bounded by the complete Leibniz sum of
\[
\binom\alpha\beta
(P_{u,\beta}E_{\nabla\rho,\alpha-\beta}
 +E_{u,\beta}P_{\nabla\rho,\alpha-\beta}
 +E_{u,\beta}E_{\nabla\rho,\alpha-\beta}).
\]
The dilation error is bounded by
\[
cR_o(E_{\rho,\alpha+e_x}+E_{\rho,\alpha+e_y})
 +\bigl|c\,|\alpha|-1\bigr|E_{\rho,\alpha}.
\]
The retained exact residual derivatives, omitted finite derivatives,
and all analytic errors are summed.  The result is a uniform upper
\(B_\alpha\) for each actual \(|\partial^\alpha F|\), \(|\alpha|\le3\).

## Positive regional energies

For \(\alpha=(i,j)\), componentwise vector derivative bounds are
\[
B_\alpha,\quad 2R_oB_\alpha+2iB_{\alpha-e_x},\quad
2R_oB_\alpha+2jB_{\alpha-e_y}.
\]
Squaring, summing with ordered tensor multiplicity
\(\binom{i+j}{i}\), and multiplying by \(\pi R_o^2\)
gives containing uppers \(T_0,T_1,T_2,T_3\) for the regional
ordered tensor energies of \(G\).  The unweighted residual energy
is at most \(\pi R_o^2B_0^2\).

To avoid any regional integration-by-parts boundary term, the
adopted positive local energies use triangle bounds:
\[
E_{2,o}\le(\sqrt{T_0}+\sqrt{2T_2})^2,
\qquad
E_{3,o}\le E_{2,o}+(\sqrt{T_1}+\sqrt{2T_3})^2.
\]
The factor \(\sqrt2\) is the trace bound for a two-dimensional Hessian.
No assertion that a regional binomial Sobolev sum equals a regional
\((1-\Delta)\) energy is used.

All arithmetic after exact source grouping uses 384-bit Arb enclosures.
Raw enclosures include every finite coefficient absolute sum, every
tail coefficient sum, each residual derivative error category, and exact
dyadic final upper endpoints.  Input and program SHA256 bindings are
retained.  Both programs use the preserved exact source and the explicit
analytic expansion algorithm; no historical residual endpoint enters.

Reproduce by running `origin_certificate.py` followed by
`origin_large_certificate.py --field-data <new-origin-certificate.json>`.
Both accept `--ipm-root`, `--output`, and an exact rational `--radius`.
