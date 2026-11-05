# Absorbing a finite compact core into the full coercivity matrix

Status: proved analytic reduction. Numerical finite-core and infinite-tail conditions below remain to be certified for Candidate 013.

Let H be the real S1 part of scalar L2. Its vector Riesz transform R is an isometry into vector L2. Suppose the actual pointwise matrix obeys \(\mathcal M_*(X)\ge\beta_*I\). Choose any \(0<\beta_0<\beta_*\), and any orthonormal smooth scalar basis \(\varphi_1,\ldots,\varphi_N\in H\). Define
\[
\Phi c=\sum_i c_i\varphi_i,\qquad z=\Phi^*G,
\]
\[
\boxed{D_{ij}=\int(R\varphi_i)^T(\mathcal M_*(X)-\beta_0I)^{-1}(R\varphi_j)\,dX.}
\tag{1}
\]
The entries are finite, because the inverse is bounded by \((\beta_*-\beta_0)^{-1}I\). The matrix D is positive definite: R is an isometry, the coefficient inverse is positive definite almost everywhere, and the basis is linearly independent.

## A lower bound valid for all G, including off-core directions

For every coefficient vector c, matrix Cauchy–Schwarz gives
\[
|c^Tz|^2
=|\langle RG,R\Phi c\rangle|^2
\le\left[\int(RG)^T(\mathcal M_*-\beta_0I)(RG)\right]c^TDc.
\]
Taking the supremum of \(|c^Tz|^2/(c^TDc)\) yields
\[
\boxed{\int(RG)^T\mathcal M_*(RG)
\ge\beta_0\|G\|_2^2+z^TD^{-1}z.}
\tag{2}
\]
This is a global quadratic-form inequality. It is not obtained by dropping the off-diagonal blocks of a compression, which would be invalid.

Suppose an actual self-adjoint compact remainder satisfies
\[
\|\mathcal K_c-\Phi A\Phi^*\|_{2\to2}\le\varepsilon,
\quad A=A^T,
\tag{3}
\]
and the exact background energy has the decomposition proved in `EXACT_COMPACT_DECOMPOSITION.md`,
\[
\mathfrak Q_*(G)=-\int(RG)^T\mathcal M_*(RG)-qc\|J^{-1}G\|_2^2
+\langle\mathcal K_cG,G\rangle.
\]
If
\[
\boxed{D^{-1}-A\succeq0,\qquad\varepsilon<\beta_0,}
\tag{4}
\]
then (2)–(3), retaining the negative multiplier favorably, prove
\[
\boxed{\mathfrak Q_*(G)\le-(\beta_0-\varepsilon)\|G\|_2^2.}
\tag{5}
\]
No low-order price is needed for this implication. An independently computed finite-core Gram price remains useful for comparing the alternative invariant-ball route.

## A certified upper enclosure of D suffices

If \(\overline D\succeq D\) is positive definite, it is enough to certify
\[
\overline D^{-1}-A\succeq0.
\]
Indeed inverse order reverses on positive matrices, so \(D^{-1}\succeq\overline D^{-1}\). The check is equivalent to the largest eigenvalue of \(\overline D^{1/2}A\overline D^{1/2}\) being at most one; A need not be positive. Errors in the finite A approximation must be charged in (3) or enclosed in the matrix inequality, with their full scope stated.

A simple whole-plane tail enclosure for D is available for any radius L:
\[
\left\|D-D_{|X|\le L}\right\|_{\mathrm{op}}
\le\frac1{\beta_*-\beta_0}\sum_{i=1}^N\int_{|X|>L}|R\varphi_i|^2.
\]
The right-hand side bounds the positive tail by its trace. For Gaussian Hermite functions the Riesz transforms have explicit radial special-function representations, so this is a concrete certificate obligation rather than a finite-box assumption.

The actual application still requires the complete background matrix certificate, actual finite matrices, their integration and rounding enclosures, and especially the global operator-norm tail (3). A favorable sampled finite matrix supplies none of these missing tail conditions by itself.
