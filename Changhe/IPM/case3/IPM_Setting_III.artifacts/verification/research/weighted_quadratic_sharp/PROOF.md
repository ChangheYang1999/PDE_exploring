# The weighted vertical quadratic form

Date: 2026-10-20. Status: independent analytic reconstruction of the weighted
review's P4--P6. Independent rational certification and operator checks passed at 2026-10-20T19:50:36Z. This result
sharpens result57. It does not give a full-class nonexistence theorem.

## Statement

Use the hypotheses and notation of `../weighted_affine_defect/PROOF.md`:
\(a=\rho_y(0)\ne0\), \(D=\ell-1>0\), \(h=\rho-ay\),
\(\varphi=\psi+Dxy\), \(v=U-(Dx,-Dy)\), and
\(\|h\|_m^2=\int h^2r^{-2m}dX\), where \(2<m<4\).
Define \(d_1=1/4\), \(d_j=1/2\) for \(j\ge2\), and
\[
 b_j(m)=\frac{m^2+4j^2}{4|4j^2-m^2|}.
\]
Let \(J_+(m)\) and \(J_-(m)\) be the bounded self-adjoint Jacobi
operators on \(\ell^2(\{1,2,\ldots\})\) with diagonal \(+d_j\)
and \(-d_j\), respectively, and off-diagonal \(b_j(m)\). Write
\(Q^-(m)=\sup\operatorname{Rayleigh}(J_+(m))\) and
\(Q^+(m)=\sup\operatorname{Rayleigh}(J_-(m))\).
Then
\[
 -Q^-(m)\|h\|_m^2\le\int v_2h r^{-2m}dX
       \le Q^+(m)\|h\|_m^2.                         \tag{1}
\]
These constants are optimal for the full weighted parity space with the
elliptic inverse normalized at the origin, not necessarily for profiles.
At \(m=3\) the following bounds are exact:
\[
 \frac{16327}{10000}<Q^-(3)<\frac{1633}{1000},\qquad
 \frac{704}{1000}<Q^+(3)<\frac{71}{100}.           \tag{2}
\]
Consequently every exact primary profile satisfies
\[
 2\ell-1\le3\sigma+
 \begin{cases}(1633/1000)a,&a>0,\\(71/100)|a|,&a<0,\end{cases}
 \quad \sigma=\sup|\operatorname{sym}DU|_{\rm op}.            \tag{3}
\]
In particular
\[
 G_\rho+G_U\ge\frac{\sqrt2}{3}(2\ell-1),                    \tag{4}
\]
where \(G_\rho=\sup|\nabla\rho|\), \(G_U=\sup|DU|_{\rm F}\).
The sharper sign-dependent version of (3) itself should be retained when
these two suprema are separately available.

## Direct derivation of the vertical operator

The integrability, exact weighted transport identity, and identification
of the actual weighted inverse are proved in result57. In particular
\(H=r^{1-m}h\) and \(G=r^{-m}\varphi\) are square integrable on
the cylinder \((s,\theta)=(\log r,\theta)\), and the elliptic
multipliers on even angular modes have no zeros. We do not replace
\(v_2=U_2+Dy\) by the sublinear velocity \(U_2\).

Fourier transform in \(s\), set \(z=m+i\xi\), and use the
orthonormal density basis \(e_j=\pi^{-1/2}\sin((2j-1)\theta)\).
For any odd positive integer \(n\), direct differentiation gives
\[
 \partial_x[r^{z-1}\sin n\theta]
 =\frac12r^{z-2}\{(z-1-n)\sin((n+1)\theta)
                     +(z-1+n)\sin((n-1)\theta)\}.
\]
Solving \(-\Delta\varphi=h_x\), then differentiating \(\varphi\)
in \(x\), gives the matrix \(T_m(\xi):H\mapsto r^{1-m}v_2\):
\[
 T_{jj}=-d_j,\quad
 T_{j+1,j}=\frac{2j-z}{4(2j+z)},\quad
 T_{j,j+1}=\frac{2j+z}{4(2j-z)}.                \tag{5}
\]
The mode \(n=1\) has no \(\sin0\) contribution, giving its exceptional
first diagonal entry. The two off-diagonal entries in (5) need not be
complex conjugates; a direct operator norm estimate loses information.

Put \(n=2j\). The upper off-diagonal of the Hermitian part of (5) is
\[
 C_j(\xi)=\frac{n^2+m^2+\xi^2}{4(n+z)(n-\bar z)}.
\]
Its modulus is
\[
 |C_j(\xi)|=\frac{n^2+m^2+\xi^2}
 {4\sqrt{(\xi^2+(n-m)^2)(\xi^2+(n+m)^2)}}\le b_j(m).       \tag{6}
\]
The square of four times the left side is
\(1+4m^2n^2/[(\xi^2+(n-m)^2)(\xi^2+(n+m)^2)]\), so its
maximum is at zero radial frequency. Taking absolute values of the mixed
terms in the quadratic form and leaving its diagonal unchanged proves
\[
 -\operatorname{Re}\langle T_m(\xi)u,u\rangle
 \le\langle J_+(m)|u|,|u|\rangle,\qquad
 \operatorname{Re}\langle T_m(\xi)u,u\rangle
 \le\langle J_-(m)|u|,|u|\rangle.
\]
These bounds hold first for finite vectors, then by density, and integrate
by Plancherel to give (1). Also \(Q^+\le Q^-\) by diagonal comparison.

At \(\xi=0\), successive real sign changes of the angular coefficients
make every mixed term positive, separately for the two signs of the form.
Finite angular vectors approximate each Rayleigh supremum. Multiplying
such a vector by a real smooth factor \(L^{-1/2}\chi(s/L)\), with
\(\|\chi\|_2=1\), concentrates its radial Fourier mass at zero.
Continuity of the finitely many entries and the uniform operator bound
in result57 show convergence of its form to that zero-frequency Rayleigh
quotient. The corresponding density tests are smooth and supported on
annuli. This proves optimality on the weighted class. It asserts neither
transport nor the required affine-density relation for those tests.

## An independent infinite-matrix certificate

This certificate uses an exact Schur complement, not the positive-vector
certificate supplied in the reviewed source. At \(m=3\), write
\(b_j=(4j^2+9)/(4|4j^2-9|)\), and choose \(N=8\).
For a diagonal sign \(s\in\{+1,-1\}\), split \(J_s\) after its
first \(N\) rows. The tail has diagonal \(s/2\) and internal
links \(b_{N+1},b_{N+2},\ldots\). Since these links decrease,
its quadratic form is bounded above by
\[
 \tau_s=\frac s2+2b_{N+1}.
\]
This follows directly from \(2|uv|\le u^2+v^2\), including the
one-sided first tail row. Thus for \(\lambda>\tau_s\), the tail
resolvent is positive and at most \((\lambda-\tau_s)^{-1}I\).
The finite Schur complement of \(\lambda I-J_s\) is consequently
bounded below by the tridiagonal matrix with diagonal
\[
 \lambda-sd_j-\mathbf1_{j=N}\frac{b_N^2}{\lambda-\tau_s}
\]
and off-diagonal \(-b_j\). Define rational pivots
\[
 p_1=\lambda-sd_1,\quad
 p_j=\lambda-sd_j-\mathbf1_{j=N}\frac{b_N^2}{\lambda-\tau_s}
                   -\frac{b_{j-1}^2}{p_{j-1}}\quad(2\le j\le N).
                                                                  \tag{7}
\]
Every pivot is strictly positive for
\((s,\lambda)=(+1,1633/1000)\) and \((-1,71/100)\).
All inputs and pivots in (7) are rational. The retained certificate gives
both their exact fractions and a verifier using only integer arithmetic.
Positive pivots prove a strictly positive finite Schur complement. The
tail also has a strict spectral gap; completing the square gives a strict
positive lower bound for the whole operator. This proves the upper halves
of (2), including strictness.

For the lower halves, apply the same rational elimination to the ordinary
\(8\)-row truncations, without the last diagonal correction, at
\((s,\lambda)=(+1,16327/10000)\) and \((-1,704/1000)\).
The first nonpositive pivot is strictly negative, all preceding pivots
being positive. Completing the earlier squares and selecting the free
coordinate in that row constructs a vector with
\(\langle(\lambda I-J_s)u,u\rangle<0\). Extending it by zero gives
an infinite-dimensional Rayleigh quotient greater than \(\lambda\).
This proves the lower halves of (2). No floating-point eigenvalue or
uncontrolled finite-matrix truncation is used in this argument.

## Consequences, limitations and normalization

In the exact identity of result57 the only elliptic contribution is
\(-a\langle v_2,h\rangle_m\). Use the appropriate side of (1) and
\(X\cdot U/r^2\ge-\sigma\) to obtain
\[
 (m-1)\ell-1\le m\sigma+
   \begin{cases}aQ^-(m),&a>0,\\ |a|Q^+(m),&a<0.\end{cases}       \tag{8}
\]
Together with (2), this proves (3). Since
\(\sigma\le G_U/\sqrt2\), \(|a|\le G_\rho\), and
\(1633/1000<3/\sqrt2\), inequality (4) follows.

The radial compression \(M=\sup_{X\ne0}(-X\cdot U/r^2)\)
can replace \(\sigma\) in (8): it is the term actually used by this
weighted identity. The origin gives \(D\le M\le\sigma\).
If an additional, unproved upper bound \(\sigma\le D+\eta\) holds,
then \(2-\ell\le3\eta+(1633/1000)|a|\), with \(71/100\) in
place of \(1633/1000\) for negative \(a\). This is a conditional
exclusion, not a way to establish that upper bound. A quantitative bound
\(X\cdot W\ge\varepsilon r^2\) similarly implies
\(m\varepsilon\le\ell+1+|a|Q^{\mathrm{sign}}(m)\).

For a non-profile with exact center normalization, the same derivation has
an additional term \(\langle F,h\rangle_m\),
\(F=W\cdot\nabla\rho-\rho\). Thus one must add
\(\|F\|_m/\|h\|_m\) to the right side of (8). Kinematic examples
need not satisfy (3). All terms in the identity scale by
\(\lambda^{4-2m}\), so (1)--(8), their residual version and the
conditional hypotheses respect the genuine spatial dilation.

The other extensions in the reviewed source, including angular weights,
higher Taylor vanishing and non-profile constructions, require separate
scope checks. This proof does not silently include them in its verdict.
