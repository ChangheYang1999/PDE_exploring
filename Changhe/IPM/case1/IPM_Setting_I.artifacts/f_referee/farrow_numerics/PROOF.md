# Far-field balance for the IPM profile

Status: conditional asymptotic identities proved below. These identities do
not establish existence of a stationary profile or a differentiable
asymptotic expansion. Numerical checks in this folder are floating-point
diagnostics, not validated bounds.

## Statement and hypotheses

Let \(0<k<1\), \(c_l=1/k\), and use
\(\nabla^\perp=(-\partial_y,\partial_x)\). Suppose a density and its
canonical velocity solve
\[
 (c_l X+U)\cdot\nabla\rho-\rho=0,\qquad
 U=\nabla^\perp(-\Delta)^{-1}\partial_x\rho.
\]
Assume, on the angular domain under consideration,
\[
 \rho=r^k A(\theta)+r^{2k-1}B(\theta)+o(r^{2k-1}),
 \qquad U=r^k V(\theta)+o(r^k).
\]
Require differentiated remainders:
\(r\partial_r o(r^{2k-1})=o(r^{2k-1})\) and
\(\partial_\theta o(r^{2k-1})=o(r^{2k-1})\), with sufficient angular
regularity for the displayed derivatives. Assume the velocity's leading
term is the canonical homogeneous inverse of \(r^k A\). This last
assumption follows from suitable asymptotic and global bounds but is an
explicit hypothesis here; a pointwise density asymptotic alone is not
being used to justify passing a limit through a singular integral.

Then the leading equation is \((c_l k-1)A=0\), and the first correction is
\[
 (c_l-1)B=kV_r A+V_\theta A'.
\]
In particular, if \(B=A C\), then away from zeros of \(A\),
\[
 C=\frac{kV_r+V_\theta A'/A}{c_l-1}.
\]
Thus the first correction is determined by the leading angular profile
under these hypotheses. No nonlinear angular equation on \(A\) alone is
imposed at the leading order.

## Canonical homogeneous inverse

Write \(\psi=r^{k+1}\Psi(\theta)\). Direct differentiation in polar
coordinates gives
\[
 \partial_x(r^k A)=r^{k-1}(k\cos\theta A-\sin\theta A'),\quad
 -\Delta\psi=-r^{k-1}(\Psi''+(k+1)^2\Psi).
\]
Consequently
\[
 -\Psi''-(k+1)^2\Psi=k\cos\theta A-\sin\theta A',
 \qquad V_r=-\Psi',\quad V_\theta=(k+1)\Psi.
\]
These are periodic angular equations, restricted to the prescribed
parities. The operator is invertible on periodic Fourier modes because
\(1<k+1<2\) is not an integer. For a mode \(e^{in\theta}\), its inverse
multiplier is \(1/(n^2-(k+1)^2)\). The canonical global velocity excludes
additional harmonic fields; no such field of degree \(k\) is introduced.

## Transport expansion

Let \(\mathcal L=c_l r\partial_r-1\). For every angular function \(F\),
\(\mathcal L(r^a F)=(c_l a-1)r^aF\). Therefore the residual is
\[
 R=r^k(c_l k-1)A+
 r^{2k-1}\{(1-c_l)B+kV_r A+V_\theta A'\}
 +o(r^{2k-1}).
\]
Here the leading velocity multiplying the leading gradient has degree
\(2k-1\); every term containing one of the stated remainders is smaller
under the hypotheses. Since \(k<1\), the two displayed degrees differ.
The first coefficient vanishes because \(c_l k=1\), and the second gives
the claimed formula. A nonlinear equation
\(kV_r A+V_\theta A'=0\) would follow only if the additive first
correction \(B\) were constrained to vanish.

## Residual normalization and the axis

For a trial with the same expansion, define
\[
 F_1=(1-c_l)B+kV_r A+V_\theta A',\qquad
 D_v=|\rho|+|X\cdot\nabla\rho|+|U\cdot\nabla\rho|.
\]
At an angle where \(A\ne0\),
\[
 D_v=(1+k)r^k|A|+o(r^k),\qquad
 \frac{|R|}{D_v}
 =r^{k-1}\frac{|F_1|}{(1+k)|A|}+o(r^{k-1}).
\]
If \(F_1=0\), this only proves \(o(r^{k-1})\). The stronger rate
\(O(r^{2k-2})\) needs a further controlled expansion; it does not follow
from the two-term assumptions alone.

Let \(\theta_*=\pi/2\), \(\delta=\theta_*-\theta\), and suppose
\(A=a\delta^2+o(\delta^2)\), \(A'=-2a\delta+o(\delta)\),
\(a\ne0\), and \(B/A\) has a finite limit. Parity gives
\(\Psi(\theta_*)=0\). If \(v=V_r(\theta_*)=-\Psi'(\theta_*)\),
then \(V_\theta=(k+1)v\delta+o(\delta)\). Hence
\[
 \frac{kV_r A+V_\theta A'}{A}\longrightarrow -(k+2)v.
\]
The required relative correction therefore has axis limit
\(- (k+2)v/(c_l-1)\). Both the raw residual coefficient and its
normalizing denominator vanish quadratically; their quotient need not
vanish. On the exact axis the literal normalized residual is \(0/0\),
so a numerical axis floor is not this transverse limit.

## Spline observation

A degree-seven spline with simple interior knots is \(C^6\). If its
pieces before the last knot \(q_*\) are fixed, any admissible change on
the final interval must have its first seven Taylor coefficients
(orders zero through six) zero at \(q_*\). It is therefore
\(\delta b(q)=a(q-q_*)^7\). This establishes one local degree of
freedom, not eight independently adjustable coefficients, when all
preceding pieces are fixed. Holding a polynomial exactly fixed on any
open part of its last interval fixes it throughout that interval.

## Two further coefficients of this trial formula

This paragraph assumes a termwise differentiable further expansion.
Put \(B=A C\), and let the third homogeneous density coefficient be
\(D=A E\), of degree \(3k-2\). Let \(V^{(1)}\) be the homogeneous
velocity of \(r^{2k-1}B\). The coefficient of \(r^{3k-2}\) in the
residual is
\[
 F_2=2(1-c_l)D+(2k-1)V_rB+V_\theta B'
       +kV^{(1)}_r A+V^{(1)}_\theta A'.
\]
Indeed, these are respectively drift on the third density coefficient,
leading velocity on the second density coefficient, and second velocity
on the leading density coefficient. At a quadratic y-axis zero,
\[
 F_2/A\ \longrightarrow\
 2(1-c_l)E-3V_r C-3kV^{(1)}_r.
\]
For the first transport term use
\((2k-1)-2(k+1)=-3\); for the second use
\(k-2((2k-1)+1)=-3k\).

The explicit trial also has a relative \(r^{-2}\) density term, separate
from the first powers of \(r^{k-1}\). Denote its coefficient by \(G\).
With \(j_m=\max(m-1,0)\),
\[
 G=L^2\left[
 \frac{k-3}{2}-r_0^2\sum_m j_m b_m(1)\cos(2m\theta)
 -\frac{p_3}{2}T(1)|\cos\theta|^{p_3-2}\sin^2\theta
 \right].
\]
This follows by expanding the three factors that explicitly depend on
\(u^{-2}\): the base power, \(\chi^{j_m}\), and the radial multiplier
of the fractional term. Corrections to \(1-q\) itself are of relative
order \(r^{k-3}\), smaller than \(r^{-2}\). For the present
\(k=0.17936\ldots\), \(r^{-2}\) lies between the relative orders
\(r^{2k-2}\) and \(r^{3k-3}\). Drift on \(r^{k-2}AG\) contributes
\(-2c_l AG\,r^{k-2}\) to the residual. Interaction with the velocity
is smaller. These coefficient identities do not bound the omitted
terms at a finite radius.

## Dependencies and scope

The proof uses only polar differentiation, matching distinct powers,
the specified canonical homogeneous inverse, and polynomial
uniqueness. The relevant project conventions were checked in
`lead/SPEC.md`, section 3 and N3. No claim is made about global
solvability for arbitrary \(A\), uniform two-dimensional fractional
regularity, optimizer convergence, or validated numerical error.
