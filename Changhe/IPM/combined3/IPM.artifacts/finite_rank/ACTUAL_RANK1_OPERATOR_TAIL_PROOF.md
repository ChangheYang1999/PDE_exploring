# Actual Candidate013 rank-one source certificate

Status: actual smooth finite-rank A matrix, exact B Gram enclosure, and certified operator tail. The tail upper is not sufficient for the existence budget. The local integer proof supersedes this route for closing the theorem.

Let \(K=C_{vs3}\) be the actual Candidate013 self-adjoint source remainder,
\[
 K=-\tfrac12\sum_{j,k}[R_j,[R_k,K_{jk}^{\rm mat}]],\qquad
 K^{\rm mat}=\begin{pmatrix}-\rho_y&\rho_x/2\\\rho_x/2&0\end{pmatrix}.
\]
Use the exact normalized real S1 Schwartz function
\[
 \phi(x,y)=\sqrt{2/\pi}\,y\,e^{-(x^2+y^2)/2},\qquad\|\phi\|_2=1.
\]
Set \(P=|\phi\rangle\langle\phi|\), \(A_{11}=\langle K\phi,\phi\rangle\), and \(K_N=PKP=A_{11}P\).

The replay source_rank1_certificate_replay_v01.json certifies an enclosure centered at approximately \(-0.0686740077826094\), with error below \(1.4\cdot10^{-10}\). Its exact finite-dimensional B Gram for the inherited norm is
\[
 B_{11}=\|W_2J^{21/10}\phi\|_2^2
 =76.242484695914049819\ldots,\qquad W_2^2=1+4r^2.
\]
The original complete quadrature/endpoint proof is in FINITE_RANK_CHECKPOINT.md. The new replay binds every module and both actual candidate inputs before and after execution; all hashes agree. It writes a new output and preserves the previous computation.

The actual whole-space Hilbert–Schmidt certificate in the independent coercivity output L2_signed_far_v05/result.json gives
\(\|K\|_{\rm HS}\le0.710328127935052\).
For any Hilbert–Schmidt operator, \(T\mapsto PTP\) is an orthogonal projection in Hilbert–Schmidt space. Consequently
\[
 \|K-K_N\|_{\rm op}
 \le\|K-K_N\|_{\rm HS}
 =\sqrt{\|K\|_{\rm HS}^2-|A_{11}|^2}.
\]
The assembler subtracts the certified lower endpoint of \(|A_{11}|^2\), never its upper endpoint. Its saved interval is below the rational adopted value
\[
 \boxed{\epsilon=7071/10000.}
\]
The statement holds on full L2 and hence on its invariant S1 subspace.

For \(G=J^q(W_2g)\),
\[
 |\langle G,\phi\rangle|
 =|\langle g,W_2J^q\phi\rangle|
 \le\sqrt{B_{11}}\|g\|_2.
\]
Thus the actual finite-rank absolute price is \(C_N=|A_{11}|B_{11}<1309/250\), and
\[
 \boxed{|K[G]|\le\epsilon\|G\|_2^2+(1309/250)\|g\|_2^2.}
\]
Because \(A_{11}<0\), the one-sided upper estimate can discard the finite part and use \(K[G]\le\epsilon\|G\|_2^2\). The displayed finite price nevertheless records the requested absolute matrix/Gram calculation.

The inherited N2 pairing above is distinct from \(G=W_aJ^qg\); its B Gram must not be reused for that different map. The abstract operator-tail estimate itself is independent of that distinction.

assemble_actual_rank1_tail.py verifies the fresh replay bindings, the actual HS result's code and candidate bindings, every cited core chunk hash, and the exact far-expansion cache hash before writing actual_rank1_operator_tail_certificate.json. All arithmetic combining the enclosures uses Arb.

This completed decomposition demonstrates an actual nonzero smooth basis and matrices with an actual remainder bound. A certified upper exceeding the needed budget does not prove that every other approximation fails or that the stationary equation has no solution. No such obstruction is asserted.
