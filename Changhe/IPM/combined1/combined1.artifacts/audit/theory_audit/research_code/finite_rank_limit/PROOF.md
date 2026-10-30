# The full IPM coupling is not a finite-rank remainder

## Exact statement

Let m be a nonnegative integer. Let \(\bar\rho\) be a real smooth S1 density, with \(\nabla\bar\rho\) and its derivatives through order m bounded. Suppose
\(a_0=\partial_y\bar\rho(0)>0\). On the real S1 subspace of \(H^m(\mathbb R^2)\), define

\[
Qh=U[h]\cdot\nabla\bar\rho,\qquad
\widehat{U[h]}(\xi)=
 \left(\frac{\xi_1\xi_2}{|\xi|^2},-\frac{\xi_1^2}{|\xi|^2}\right)\widehat h(\xi).
\]

For every compact operator K on this subspace,

\[
\|Q-K\|_{H^m\to H^m}\ge a_0.\tag{1}
\]

The same lower bound is witnessed by smooth densities vanishing in a neighborhood of the origin, with exactly zero canonical strain. Thus imposing zero origin jets and zero strain does not remove this obstruction. For m=0 the strain-zero test family is a smooth subspace, not a closed strain kernel in L2.

This is a statement about norm approximation of Q itself. It does not assert noninvertibility of the full transport operator, noncompactness relative to a graph norm, or failure of a decomposition that retains the singular order-zero part in its leading operator. At the origin this coupling has a favorable negative sign.

## Proof

Fix \(\varepsilon>0\). By continuity choose a small disk around zero on which \(|\bar\rho_y-a_0|<\varepsilon\). Choose a nonzero real smooth amplitude A, supported in an annulus strictly inside this disk, even in x and odd in y. Put

\[
f_n(X)=A(X)\cos(nx).
\]

The Hm norm satisfies
\[
n^{-m}\|f_n\|_{H^m}\longrightarrow \frac{\|A\|_2}{\sqrt2},\tag{2}
\]
with the factor n interpreted as 1 when m=0. Indeed the leading derivative is \(\partial_x^mf_n\); all derivatives involving an amplitude derivative are lower by at least one power of n. The two oscillatory modes have disjoint limiting Fourier mass, and their cross term tends to zero by integration by parts.

The multiplier of U tends to \((0,-1)\) along both x-frequency rays. Plancherel and dominated convergence for the Fourier translates of A therefore give

\[
 n^{-m}\|U[f_n]-(0,-f_n)\|_{H^m}\longrightarrow0.\tag{3}
\]

For clarity, after substituting \(\xi=\eta\pm(n,0)\), the symbol difference tends to zero for every fixed eta, is bounded uniformly, and the normalized Sobolev weight is bounded by a constant times \(\langle\eta\rangle^{2m}\). The latter times \(|\widehat A(\eta)|^2\) is integrable. This proves (3) without invoking a pseudodifferential theorem.

Multiplication by each component of \(\nabla\bar\rho\) is bounded on Hm, by Leibniz's rule. The leading derivative of \((\bar\rho_y-a_0)f_n\) again falls entirely on the oscillatory factor. All terms with a coefficient or amplitude derivative are lower order. Equations (2) and (3) imply

\[
 \limsup_{n\to\infty}
 \frac{\|Qf_n+a_0f_n\|_{H^m}}{\|f_n\|_{H^m}}
 \le\varepsilon.\tag{4}
\]

The normalized sequence \(h_n=f_n/\|f_n\|_{H^m}\) converges weakly to zero in Hm. One proof first tests against functions with compact Fourier support, using escape of the two Fourier packets to infinity, and then uses density and the bounded norms of h_n. Thus \(Kh_n\to0\) strongly for every compact K. The reverse triangle inequality and (4) yield
\(\|Q-K\|\ge a_0-\varepsilon\). Sending epsilon to zero proves (1).

## Exact strain correction

Every f_n is zero near zero, so all its origin jets vanish. By the canonical strain formula,

\[
c[f_n]=\frac1\pi\int
 \frac{\sin(3\theta)}{r^3}A(X)\cos(nx)\,dX.
\]

The nonoscillatory integrand is smooth and compactly supported away from zero. Repeated integration by parts in x shows \(c[f_n]=O(n^{-N})\) for every N. The same is true after Hm normalization.

Choose a fixed nonnegative smooth radial eta supported in an annulus away from zero and set
\(\phi(X)=\eta(r)(3x^2y-y^3)\). This is smooth and S1, vanishes near zero, and

\[
c[\phi]=\frac1\pi\int_0^\infty\int_0^{2\pi}
 \eta(r)\sin^2(3\theta)\,r\,d\theta\,dr
=\int_0^\infty\eta(r)r\,dr>0.
\]

Replace h_n by \(h_n-c[h_n]\phi/c[\phi]\). The correction converges to zero in Hm faster than any power of n. The new sequence has strain exactly zero, still vanishes near zero, and retains (2)-(4), weak convergence and the essential-norm bound.

## Consequence for the Hou transfer

Chen and Hou, arXiv:2607.15256v1, Sections 1.3 and 2.4, do not replace the full singular operator by a finite-rank map. They retain a localized singular part and approximate only a smoother part and commutators. Their equations (2.11)-(2.12) explicitly make this split. This distinction is necessary in S1 as well: a finite matrix for the full Q cannot have a uniform norm defect below a0 on the spaces above.

A valid S1 finite-rank program must therefore exhibit its retained principal part, establish a quantitative complement estimate in its chosen domain and range, and only then certify the finite-dimensional block. A finite-section singular value supplies none of those missing bounds.

## Dependencies and verification

The proof uses Plancherel, elementary Fourier translation, Leibniz's rule, compactness on weakly convergent sequences, and the canonical strain formula independently checked in `../operator_audit/PROOF.md`. It does not use floating-point data. The application a0=10.3002948918... requires a source-bound certificate for the chosen reference; (1) itself uses the exact symbolic a0. No claim about the baseline weighted E2 essential norm is made without a separate weighted argument.
