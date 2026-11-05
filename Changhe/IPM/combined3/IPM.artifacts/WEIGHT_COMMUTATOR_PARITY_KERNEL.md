# Exact weight-source kernel and the first S1 far multipole

Status: exact identities and parity cancellation proved here. A quantitative global remainder estimate and full high-order finite-rank assembly remain open.

Write \(b=\nabla\rho_*\), \(W=\sqrt{1+4|X|^2}\), and let \(k_j(z)\) be the off-diagonal convolution kernels of \(U_j\). Each \(k_j\) is real, homogeneous of degree −2, and even under central reflection. The possible identity part of \(U_2\) commutes with W and cancels from the following expression. The actual operator
\[
E_Wf=b\cdot[W,U]W^{-1}f
\]
has off-diagonal kernel
\[
e(x,y)=\sum_j b_j(x)k_j(x-y)\left(\frac{W(x)}{W(y)}-1\right).
\tag{1}
\]
Its real self-adjoint part therefore has the exact kernel
\[
\boxed{\operatorname{Sym}e(x,y)
=\frac12\sum_j k_j(x-y)
\frac{(W(x)-W(y))(W(x)b_j(x)-W(y)b_j(y))}{W(x)W(y)}.}
\tag{2}
\]
This follows by adding e(x,y) to e(y,x); the kernels kj are even. Near the diagonal the two differences in (2) are first order, so their product cancels the degree −2 singularity on compact sets. This is an identity, rather than a new norm bound for the fractional conjugate.

## The leading near/far term vanishes on S1

Choose radial smooth near and far cutoffs with separated supports, so \(|y|\ge2|x|\) on a near-output/far-input block. Taylor expansion of the off-diagonal kernel gives
\[
k_j(x-y)=\sum_{|\alpha|\le m}\frac{x^\alpha}{\alpha!}\partial^\alpha k_j(-y)
+\mathcal R_{m,j}(x,y).
\tag{3}
\]
Multiplying (3) by the exact separated weight factors in (1) gives explicit finite-rank terms. For example the near-output block has factors
\[
\begin{array}{ll}
a^{(1)}_{\alpha j}(x)=\chi_N(x)b_j(x)W(x)x^\alpha/\alpha!,
&b^{(1)}_{\alpha j}(y)=\chi_F(y)\partial^\alpha k_j(-y)/W(y),\\
a^{(2)}_{\alpha j}(x)=-\chi_N(x)b_j(x)x^\alpha/\alpha!,
&b^{(2)}_{\alpha j}(y)=\chi_F(y)\partial^\alpha k_j(-y).
\end{array}
\tag{4}
\]
The signs in (4) refer to the real integral operator \(a(x)\int b(y)f(y)dy\). Every factor is an explicit smooth function when the cutoffs avoid the singular origin for its far row.

For S1 f, central oddness alone implies that every even-order \(\alpha\) in (4) vanishes: \(\partial^\alpha k_j\), the radial cutoffs, and W are centrally even in that case. Thus the first nonzero near-output row has \(|\alpha|=1\), not zero.

For a far-output/near-input block expand k(x−y) in y instead. Its corresponding factors include
\[
\chi_F(x)b_j(x)W(x)\partial^\alpha k_j(x)/\alpha!,
\qquad(-1)^{|\alpha|}\chi_N(y)y^\alpha/W(y),
\]
and
\[
-\chi_F(x)b_j(x)\partial^\alpha k_j(x)/\alpha!,
\qquad(-1)^{|\alpha|}\chi_N(y)y^\alpha.
\tag{5}
\]
Again every even-order term vanishes on centrally odd inputs. Since the actual background has \(b=O(r^{-\gamma})\), \(\gamma=1-1/c>0\), the first nonzero output tail in (5) is
\[
b_j(x)W(x)\partial^\alpha k_j(x)=O(r^{-2-\gamma}),\qquad |\alpha|=1.
\tag{6}
\]
In particular its weighted L2 norm is finite: \(W\) times this tail is \(O(r^{-1-\gamma})\). The putative \(r^{-1-\gamma}\) output tail from \(\alpha=0\), whose weighted norm would diverge, cancels by the required parity. The finer even-x/odd-y reflection conditions remove additional terms; they do not weaken this central-odd cancellation.

The parity identity persists under conjugation by the radial operators Jq and J−q: both preserve S1 and central oddness. A finite-rank term \(|a\rangle\langle b|\) in EW becomes \(|J^qa\rangle\langle J^{-q}b|\). Its predual factors are \(WJ^{2q}a\) and \(Wb\), respectively. Their actual integrability must be checked for each factor; it cannot be inferred solely from finite rank.

The implemented smooth algebraic S1 basis in `finite_rank/algebraic_tail_gram.py` has the correct first nonzero tail exponent (6), and its weighted fractional Gram upper bounds are certified through integer Sobolev norms. That basis alone is not an approximation or certificate of the operator in (1). The missing steps are actual multipole coefficients, near/near treatment, derivative remainder bounds for (3) in the Hq spaces, and their full numerical budgets.
