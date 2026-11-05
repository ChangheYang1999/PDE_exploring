# Independent review of the Q far weight commutator estimate

Status: analytic identities and constants reviewed. This review does not certify missing numerical producers or the complete IPM energy.

The coordinator's decomposition uses \(E=\operatorname{Sym}(bWU c-bU)\), \(c=W^{-1}\), \(H=I-P_\mu\). Define \(E_{UH}=\operatorname{Sym}(bWU Hc-bUH)\). Direct operator multiplication gives exactly
\[
 EH=E_{UH}+\tfrac12bWU[c,H]
 +\tfrac12(cU^*W-U^*)[b,H]+\tfrac12cU^*[W,H]b.
\]
Indeed the difference of the adjoint terms contains \(cU^*[Wb,H]-U^*[b,H]\), and \([Wb,H]=W[b,H]+[W,H]b\). No coefficient commutation has been assumed.

The centrally odd weighted Beurling bound is proved separately in CENTRAL_ODD_WEIGHTED_BEURLING.md. It yields the first term by
\[
 W(x)^\alpha|c(x)-c(y)|\le2|x-y|+2^\alpha|x-y|^\alpha,
\]
and \(|b|W^{1-\alpha}\le B(2R)^{1-\alpha}\) on the coefficient support. The middle term uses the adjoint of the valid S1 weighted-velocity estimate; its vector input has the correct two output parities because it is \([b,H]G\).

For the last term, \(|W(x)-W(y)|\le2|x-y|\). When \(b(y)\ne0\) and \(|x-y|\le R/2\), one has \(W(x)\ge R\), giving the coefficient bound \(2B|x-y|/R\). On the complementary region it is at most \(2B|x-y|\le8B|x-y|^3/R^2\). The stated Gaussian first and third moment bound follows.

The symmetric kernel for \(E_{UH}\) is
\[
 \tfrac12 k_{UH}(x-y)\cdot
 \frac{(W(x)-W(y))(W(x)b(x)-W(y)b(y))}{W(x)W(y)}.
\]
If \(|x-y|\le R/2\) and it is nonzero, one endpoint is at least \(R\) from the origin and the other at least \(R/2\). The denominator is at least \(2R^2\). The bound \(L_d|x-y|^2/R^2\) is therefore safe. On the complementary region the bound \(8B|x-y|^3/R^2\) is safe.

The heat representation is \(UH=\int_0^t\mathcal H p_s\,ds\), \(t=1/(2\mu^2)\), with the appropriate selected Hessian row \(\mathcal H p_s\). Its vector modulus is at most \(p_s(r^2/(4s^2)+1/(2s))\). Gaussian radial moments and integration in \(s\) give precisely
\[
 \int r^2|k_{UH}|\le5/\mu^2,\qquad
 \int r^3|k_{UH}|\le3\sqrt{2\pi}/\mu^3.
\]
Any delta terms on the diagonal vanish from the commutator kernel because of the coefficient differences.

One cutoff detail matters for \(L_d=\|D(W\chi_Fb)\|_\infty\). If \(|\nabla\chi_F|\le2/R\) on \(R\le r\le2R\), then \(W/R\le4+1/R\), so its cutoff contribution is bounded by \((8+2/R)B\). A smaller value near \(4B\) would require a different logarithmic cutoff derivative bound. The coordinator's safe value
\[
 L_d\le [2+2(4+1/R)]B+\sqrt{4+R^{-2}}\,R D_R
\]
is valid. The last term follows by multiplying each exact far expansion and remainder monomial by \(r\) before taking the supremum: all resulting powers remain negative. It does not follow by multiplying an unweighted uniform Hessian bound by an unbounded weight.
