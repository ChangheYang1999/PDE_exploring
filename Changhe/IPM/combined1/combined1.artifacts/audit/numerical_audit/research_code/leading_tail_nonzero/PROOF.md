# A nonzero leading density harmonic for candidate 007

## Statement

Let \(c=4076476460239181/2251799813685248\), \(\gamma=1/c\),
\(\delta=1-\gamma\), and \(d=3+\gamma\). Take the exact coefficients of
`C1-N1-007-d2w-j7-e2bal`, with coefficient SHA256
`ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`.
Write its density as \(\rho=-\partial_y\Delta\chi\). Its uniform leading
expansion is

\[
\rho(r,\theta)=r^\gamma\Theta(\theta)+o(r^\gamma).
\]

The coefficient \(b_1\) of \(\sin\theta\) in \(\Theta\) satisfies the strict
exact inequalities \(18<b_1<19\). In particular, \(\Theta\) is nonzero.
This statement concerns the exact rational candidate, not rounded optimizer
coordinates.

## Notation and argument

In a generator block \((j,m)\), the potential is

\[
H_m(x,y)(1+r^2)^{(d-j\delta)/2-m}P(t),\qquad
H_m=\operatorname{Re}(x+iy)^{2m},\quad t=\frac{r^2}{1+r^2}.
\]

The generator polynomials are monomials or monomials times shifted Legendre
polynomials. Their value at \(t=1\) is one. The checker verifies this using
the explicit polynomial coefficients, rather than assuming the value.
It follows that the leading \(j=0\) potential is

\[
r^d\sum_m A_m\cos(2m\theta),
\]

where \(A_m\) is the sum of the raw generator coefficients in block
\((0,m)\). Independently, summing the already verified canonical coefficients
in each such block gives the same rational \(A_m\).

To obtain the density, use the finite complex Fourier representation
\(\sum_n a_n e^{in\theta}\). The coefficients are real,
\(a_0=A_0\), and \(a_{2m}=a_{-2m}=A_m/2\) for \(m>0\). The polar identities

\[
\Delta(r^d e^{in\theta})=(d^2-n^2)r^{d-2}e^{in\theta},
\]
\[
-\partial_y(r^k e^{in\theta})
=\frac{i}{2}r^{k-1}
\bigl((k-n)e^{i(n+1)\theta}-(k+n)e^{i(n-1)\theta}\bigr)
\]

follow by expanding \(\partial_y=\sin\theta\,\partial_r+
r^{-1}\cos\theta\,\partial_\theta\). Apply these identities to every
Fourier coefficient, with \(k=d-2\). The resulting coefficients are pure
imaginary and antisymmetric. Thus the real density is a sine polynomial:
if its coefficient at positive frequency \(n\) is \(i q_n\), then the
real sine coefficient is \(-2q_n\).

This computes every leading density harmonic without using a specialized
formula for \(b_1\). As a separate check, collecting the contributions
from \(n=0,2,-2\) gives

\[
b_1=-A_0d^2(d-2)+\tfrac12 A_1(d^2-4)d.
\]

The retained rational calculation proves \(18<b_1<19\) by integer
comparison and agrees exactly with the independently recorded T4-203
rational value.

## Uniformity and scope

There are finitely many generators. On \(r\geq 1\), each radial factor
admits a convergent expansion in \(r^{-2}\) near infinity, with uniform
angular bounds after any fixed number of derivatives. Branches with
\(j\geq1\) are smaller by at least \(r^{-\delta}\); \(\delta>0\).
Three derivatives reduce the leading degree from \(d\) to \(\gamma\).
These facts prove the asserted uniform density expansion and
\(U[\rho]=(-\chi_{xyy},\chi_{xxy})=O(r^\gamma)\) for this prescribed
potential representation.

The nonzero harmonic supplies a numerical hypothesis of the separately
audited weak tail-pinning theorem. That theorem, its weighted canonical
velocity extension, and any origin regularity assumptions remain separate
dependencies for conclusions about exact solutions. This check proves no
existence result, inverse bound, or exclusion outside the stated affine
chart.

Dependencies: the exact generator representation and its canonical identity
confirmed in N4-163, elementary polar differentiation, and finite rational
arithmetic. Formal sources are not used. Exact coefficients and verification
evidence are retained as JSON alongside this proof.
