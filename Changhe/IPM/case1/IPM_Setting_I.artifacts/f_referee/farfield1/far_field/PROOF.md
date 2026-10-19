# Far-field identities and the scope of the audit

## Statement and hypotheses

Let \(0<k<1\), \(c_l=1/k\), and let a density on the plane be even in \(x\)
and odd in \(y\). Write \(A(\theta)=\Theta_0(\theta)\),
\(a(\theta)=\Theta_{1f}(\theta)\), and suppose, with the required differentiated
remainders,
\[
\rho=r^k A(1+a r^{k-1}+b r^{2k-2}+h r^{-2}+\cdots).
\]
The velocity is the canonical full-plane inverse of
\(-\Delta\psi=\partial_x\rho\), with \(U=(-\psi_y,\psi_x)\).
Statements about the infinite hierarchy are formal and allow additional
multipole terms. For normalized residuals we work in the open first quadrant,
where \(A>0\); values on axes mean limits. Uniform endpoint estimates require
remainders divisible by the same angular vanishing factors.

For the supplied trial, define
\[
v=|\cos\theta|^{p_3-2}\sin^2\theta,\quad
E=\sum b_m(1)\cos(2m\theta)+T(1)v,
\]
\[
B=\sum b_m'(1)\cos(2m\theta)+2T'(1)v,\qquad
D=\sum b_m''(1)\cos(2m\theta)+4T''(1)v.
\]
Then
\[
A=L^{3-k}\cos^2\theta\sin\theta\,e^E,\quad
a=-L^{1-k}B,\quad b=\tfrac12L^{2-2k}(D+B^2),
\]
\[
h=L^2\left[\frac{k-3}{2}
-r_0^2\sum\max(m-1,0)b_m(1)\cos(2m\theta)
-\frac{p_3}{2}T(1)v\right].
\]
These coefficients concern the formula itself, without imposing transport.

## Proof of the first-order transport identity

For a homogeneous density \(r^\alpha A_\alpha(\theta)\),
\[
\partial_x(r^\alpha A_\alpha)
=r^{\alpha-1}(\alpha\cos\theta A_\alpha-\sin\theta A_\alpha').
\]
Also
\[
\Delta(r^{\alpha+1}F_\alpha)
=r^{\alpha-1}((\alpha+1)^2F_\alpha+F_\alpha'').
\]
The source is odd in both Cartesian variables. The symmetry-preserving
streamfunction therefore has only \(\sin(2n\theta)\) modes. Its modal
coefficient is \(G_n/(4n^2-(\alpha+1)^2)\), provided the denominator is nonzero.
For \(\alpha=k\), put \(F=F_0\). Then
\[
U_0=r^k(-F', (k+1)F)
\]
in polar components, and
\[
U_0\cdot\nabla(r^k A)
=r^{2k-1}((k+1)FA'-kF'A).
\]
The drift coefficient at order \(r^k\) is \(c_l k-1=0\). Its coefficient
at order \(r^{2k-1}\) is \(1-c_l\). Consequently the forced first correction
is
\[
e=\Theta_{1e}=\frac{(k+1)FA'/A-kF'}{c_l-1}.
\]
This proves the stated sign and coefficient.

At \(\theta=0\), \(A\sim a_0\theta\) and \(F\sim F'(0)\theta\), so
\(e(0)=F'(0)/(c_l-1)\). At \(\theta=\pi/2\), put
\(t=\pi/2-\theta\). Then \(A\sim a_y t^2\) and
\(F\sim-F'(\pi/2)t\), giving
\(e(\pi/2)=(k+2)F'(\pi/2)/(c_l-1)\).
The fractional angular term has exponent \(p_3-2>4\) and changes neither
leading vanishing order.

## Hierarchy, core terms, and canonical inversion

Set \(\alpha_j=k+j(k-1)\) and \(\beta_j=\alpha_j+1\). Within the pure
power sector,
\[
j(1-c_l)A_j+
\sum_{p+q=j-1}\left[-\alpha_qF_p'A_q+\beta_pF_p A_q'\right]=0.
\]
Only previously determined coefficients occur in the sum. Elliptic
resonance occurs if \(\beta_j=\pm2n\). The first four values, \(j=0,1,2,3\),
avoid resonance for the supplied \(k\). This does not establish a globally
complete pure power series.

For an angular source mode \(f_n(r)\sin(\ell\theta)\), \(\ell=2n\), the
regular canonical inverse is
\[
\psi_n(r)=\frac1{2\ell}\left[
r^{-\ell}\int_0^r s^{\ell+1}f_n(s)\,ds+
r^\ell\int_r^\infty s^{1-\ell}f_n(s)\,ds\right].
\]
Differentiation verifies the radial equation and cancellation of derivative
terms at the moving integration endpoints. Regularity excludes a singular
homogeneous term at the origin, and the growth condition excludes a growing
homogeneous term at infinity.

A compact change in the density produces only the decaying exterior terms
\(r^{-2n}\sin(2n\theta)\), hence starts at \(r^{-3}\) in velocity. This is
compatible with the prohibition on added global harmonic polynomials.
Its transport interaction with the leading density is \(r^{k-4}\), between
the fourth and fifth corrections of the pure power density hierarchy.

For the trial's differentiated tail \(\rho-r^k A=O(r^{2k-1})\), the same
modal formula gives \(U-U_0=O(r^{2k-1})\): the source remainder is
\(O(r^{2k-2})\); for \(\ell=2\), both integrals give
\(\psi-\psi_0=O(r^{2k})\), with an additional \(O(r^{-2})\) core term.
Angular derivative bounds are needed to sum modes and pass to uniform
estimates. The finite spline/angular trial has the regularity needed at the
orders considered here.

## Trial expansion and residual

Put \(\epsilon=(r/L)^{k-1}\). Direct binomial expansion gives
\(1-q=\epsilon(1+O((r/L)^{-2}))\). Taylor expansion of the endpoint spline
and of \(T(1-2\epsilon)\) gives \(-B\epsilon+D\epsilon^2/2+\cdots\) in
the exponent. Exponentiating proves the formulas for \(a,b\).
Expanding the radial logarithm, \(\chi^{\max(m-1,0)}\), and \(s^{p_3/2}\)
gives the coefficient \(h\). Since \(2(1-k)<2\), this geometric correction
is beyond the second relative density order, but before the third.

The residual is
\[
R=(c_l-1)r^{2k-1}A(e-a)+O(r^{3k-2}A).
\]
In the first quadrant,
\[
N_v=r^k A[(1+k)+O(r^{k-1})],
\]
so \(R/N_v=(c_l-1)(e-a)r^{k-1}/(1+k)+O(r^{2k-2})\).
There is an extra \(\operatorname{sgn}(A)\) outside the first quadrant.
At the axes themselves the ratio is undefined; its limit is the relevant
quantity.

For numerical diagnosis, put \(\delta=r^{k-1}\),
\(\alpha_1=2k-1\), and let \(F_1\) solve the angular Poisson equation for
the density \(Aa\) and exponent \(\alpha_1\). Define
\[
C=(c_l-1)(e-a),\quad D_0=(c_l-1)e,\quad
n_1=2ka+|D_0|,
\]
\[
C_2=2(1-c_l)b-\alpha_1F'a
+(k+1)F(a'+aA'/A)-kF_1'+2kF_1A'/A.
\]
Where the signs in the absolute values stabilize,
\[
\frac{R}{N_v}
=\frac{C}{1+k}\delta+
\left[\frac{C_2}{1+k}-\frac{Cn_1}{(1+k)^2}\right]\delta^2
-\frac{2c_lh}{1+k}r^{-2}
+O(\delta^3+\delta r^{-2}).
\]
This explicit expression, not merely the size of \(\delta\), determines
whether a first-order comparison at finite radii is accurate.

For the third pure-power coefficient, define
\[
J=\sum b_m'''(1)\cos(2m\theta)+8T'''(1)v,\qquad
d=-\frac{L^{3-3k}}6(J+3BD+B^3).
\]
Taylor expansion and the cubic coefficient of the exponential give the
formula for \(d\). Put \(a_0=1,a_1=a,a_2=b,a_3=d\), let \(F_j\) be the
angular inverse for \(Aa_j\), and set
\[
D_j=\sum_{p+q=j}\left[
-\alpha_qF_p'a_q+\beta_pF_p(a_q'+a_q A'/A)\right].
\]
The coefficient of \(\delta^{j+1}\) in \(U\cdot\nabla\rho/(r^kA)\) is
\(D_j\). Thus
\[
C_j=j(1-c_l)a_j+D_{j-1},\quad
n_j=(1+\alpha_j)a_j+\operatorname{sgn}(D_0)D_{j-1}
\]
for positive \(j\), as long as the signs defining \(N_v\) stabilize.
Here \(C_1=C\). Formal division by
\((1+k)+n_1\delta+n_2\delta^2+\cdots\) gives
\[
[R/N_v]_{\delta^3}=
\frac{C_3}{1+k}-\frac{C_2n_1}{(1+k)^2}
+C_1\left(\frac{n_1^2}{(1+k)^3}-\frac{n_2}{(1+k)^2}\right).
\]
Mixed geometric terms start at \(\delta r^{-2}\), after \(\delta^3\)
for this \(k\). This establishes the formulas used for the additional
numerical diagnostic.

## Exterior-closure comparison

Suppose a numerical inverse replaces the density beyond \(R\) by a
two-power tail matched to its value and radial derivative at \(R\).
Write \(\Delta f_\ell\) for the true source minus the closure source.
For \(r<R\), the exact change in streamfunction is
\[
\Delta\psi_\ell(r)=\frac{r^\ell}{2\ell}
\int_R^\infty s^{1-\ell}\Delta f_\ell(s)\,ds.
\]
This follows immediately by subtracting the two displayed Green formulas.
There is no interior-source change. With \(s=Re^t\), define
\[
\Delta B_\ell=\int_0^\infty
e^{(2-\ell)t}\Delta f_\ell(Re^t)\,dt.
\]
Then the polar velocity corrections are
\[
\Delta U_r=-\frac R2\sum_{\ell=2,4,\ldots}
(r/R)^{\ell-1}\Delta B_\ell\cos(\ell\theta),\quad
\Delta U_\theta=\frac R2\sum_{\ell=2,4,\ldots}
(r/R)^{\ell-1}\Delta B_\ell\sin(\ell\theta).
\]
The numerical tail comparison evaluates this convergent integral directly
on the supplied formula, retaining the export's interior source and drift.
It diagnoses only the exterior closure; it does not independently bound
interior quadrature or angular discretization errors.

## Endpoint constraints and angular approximation

With \(A,k,L\) fixed, the first-order identity is equivalent to
\[
\sum b_m'(1)\cos(2m\theta)+2T'(1)v=-L^{k-1}e(\theta).
\]
It is linear in the endpoint derivatives. It is generally an
overdetermined function identity in a finite-dimensional space:
the elliptic inverse and products defining \(e\) generate additional
Fourier modes. A finite-grid least-squares or minimax computation is an
approximation test, not an exact solvability theorem.

Also \(N_v\sim(1+k)r^kA\) in the quadrant. The asymptotic coefficient of
the normalized residual, not this denominator, is proportional to \(e-a\).
An improvement factor at a finite radius additionally depends on the
higher terms and, when changed, on \(k,L,A\) and the chosen norm.

## Scope and dependencies

The proof uses direct differentiation, Taylor expansion, and the displayed
radial Green formula. Numerical endpoint derivatives and finite Fourier
approximations are empirical checks, not certified error bounds.
No assertion is made that the supplied trial solves the equation, that
endpoint constraints suffice for a global solution, or that its new fit
will obey a specified finite-radius improvement factor.
