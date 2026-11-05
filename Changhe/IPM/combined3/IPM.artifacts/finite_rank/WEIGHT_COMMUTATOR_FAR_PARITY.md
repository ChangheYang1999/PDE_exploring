# S1 parity removes the leading weight-commutator tail

This note proves an exact cancellation and supplies explicit admissible far test functions. It does not assert a norm certificate for the full q=2.1 commutator.

Let b=grad rho*, with bx odd in both x and y and by even in both. Each component of the IPM velocity multiplier U is self-adjoint; its identity term commutes with W. Its nonlocal kernels k1,k2 are even under simultaneous inversion. More specifically k1 is odd in each coordinate and k2 is even in each coordinate.

The q=0 weighted-source commutator has the exact symmetric kernel
\[
e_s(x,y)=\frac12\sum_i k_i(x-y)\frac{(W(x)-W(y))(W(x)b_i(x)-W(y)b_i(y))}{W(x)W(y)}.
\]
Equivalently, as a self-adjoint quadratic operator,
\[
E_W^{sym}=\frac12\sum_i W^{-1}[W,[Wb_i,U_i]]W^{-1}.
\]
These are algebraic identities, not estimates.

## Exact central-parity cancellation

On any radial near/far cut with |x|<|y|, expand k_i(y-x) in homogeneous powers of x. Every degree-n term has y-parity (-1)^n under y→-y. The coefficient factors b_i(y),W(y),W(y)^-1 are all centrally even. Hence every even-n far row is centrally even and pairs to zero with an S1 test G, which is centrally odd. This applies separately to each separated W-ratio and b-factor term. The n=0 far row, including the slowly decaying W(y)b(y)·k(y)~|y|^-1-gamma term, vanishes exactly.

The first surviving homogeneous term has n=1. In the contribution with b(y), only the near factor x2 survives the additional x-even,y-odd symmetry. Its two separated terms are
\[
-\frac12\frac{x_2}{W(x)}[W(y)b(y)\cdot\partial_2k(y)]
+\frac12 x_2[b(y)\cdot\partial_2k(y)],
\]
with the radial near/far windows attached. The slowest far factor is now O(|y|^-2-gamma). In the contribution with b(x), the surviving index pairs are (i,j)=(1,1),(2,2), giving
\[
-\frac12[x_jW(x)b_i(x)][W(y)^{-1}\partial_jk_i(y)]
+\frac12[x_jb_i(x)][\partial_jk_i(y)].
\]
The first omitted nonzero multipole has degree3, not2.

The IPM kernels are real/imaginary components of the Beurling kernel proportional to1/z². Thus on |x|≤|y|/2 their convergent separated expansion follows from
\[
(y-x)^{-2}=\sum_{n=0}^{N}(n+1)x^ny^{-n-2}+y^{-2}\sum_{n>N}(n+1)(x/y)^n.
\]
For t=|x/y|≤1/2, the unsigned remainder is exactly bounded by
\[
|y|^{-2}\frac{t^{N+1}[(N+2)-(N+1)t]}{(1-t)^2}.
\]
Only odd n need be retained after restriction to S1. For a rigorous full-Hq operator approximation, one must still bound the kernel and needed derivatives of its remainder, as well as the comparable-radius part. No such quantitative certificate is claimed here.

## Smooth far functions with a finite low-order price

Let gamma=1-1/c and tau=2+gamma. For odd l define
\[
\phi_l(X)=|X|^l\sin(l\theta)(L²+|X|²)^{-(l+\tau)/2}.
\]
These functions are smooth at the origin, have the correct S1 symmetry, and decay as r^-2-gamma. Their weighted H3 norms are finite. Hence WJ^q phi_l is in L2 and
\(\langle J^q(Wg),\phi_l\rangle=\langle g,WJ^q\phi_l\rangle\)
by smooth cutoff approximation. Schwartz functions are not required for this finite-rank pairing once the weighted Sobolev condition is verified.

A direct Fourier derivative bound gives the PSD Gram majorant
\[
B_{ij}=\langle WJ^q\phi_i,WJ^q\phi_j\rangle
\preceq (1+8q²)\langle J³\phi_i,J³\phi_j\rangle
+8\sum_a\langle J³(x_a\phi_i),J³(x_a\phi_j)\rangle.
\]
The inequality holds for every linear combination. Both sides are diagonal across distinct angular l because W and J commute with rotations and preserve angular harmonics. `algebraic_tail_gram.py` computes the diagonal upper entries through exact rational Cartesian-polar differentiation and beta integrals
\[
\int_0^\infty r^{p+1}(L²+r²)^{-\nu}\,dr
=\tfrac12 L^{p+2-2\nu}B((p+2)/2,\nu-(p+2)/2).
\]
Arb encloses all gamma functions. At L32 and l1,3,…23 every diagonal upper is below0.717 (l1:0.71664308; l23:0.28065113), as saved in `algebraic_tail_gram_L32.json`.

The exact leading far-gradient coefficients of Candidate013 have ten bx sine-even modes n2,…20 and eleven by cosine-even modes n0,…20; the coefficient extraction is saved separately by the numerical agent. Multiplication by derivative IPM kernels produces finitely many odd angular harmonics. Matching these actual far rows and controlling their difference from the smooth phi_l family remains a further task.
