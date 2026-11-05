# Retaining the full coercivity matrix in the source pairing

Status: elementary implication proved here; actual dual residual certificate remains open.

Write \(H=J^{21/10}(WF_*)\), \(G=J^{21/10}(Wg)\), and
\[
a(G)=\int(RG)^T\mathcal M_*(RG),\qquad
d_F^2=\int(RH)^T\mathcal M_*^{-1}(RH).
\]
Assume \(\mathcal M_*\ge\beta I\), \(\beta>0\), and that the actual frozen equation has the energy inequality
\[
a(G)\le |\langle H,G\rangle|+\delta\|G\|_2^2+C\|g\|_2^2.
\tag{1}
\]
Here \(\delta\) is the sum of all charged remainder and nonlinear losses. No term is omitted from it.
Since \(\sum R_j^*R_j=I\), matrix Cauchy–Schwarz gives
\[
|\langle H,G\rangle|\le d_F\sqrt{a(G)},\qquad a(G)\ge\beta\|G\|_2^2.
\tag{2}
\]
In particular \(d_F\le\|H\|_2/\sqrt\beta\); replacing \(RH(x)\) by \(H(x)\) is invalid.

Suppose \(\|g\|_2\le R\), \(\beta>\delta\), and choose \(M>0\) such that
\[
M\ge\frac{d_F}{2\sqrt\beta},\qquad
(\beta-\delta)M^2-d_F\sqrt\beta M-CR^2\ge0.
\tag{3}
\]
Then (1) implies \(\|G\|_2\le M\). To prove this, for \(N=\|G\|_2\ge M\), the function
\(t\mapsto t-d_F\sqrt t\) is nondecreasing for \(t\ge\beta N^2\), by the first inequality of (3). Thus (1)–(2) imply
\[
(\beta-\delta)N^2-d_F\sqrt\beta N-CR^2\le0.
\]
This upward-opening quadratic has one nonnegative root (including the zero-constant case), and its value at \(M\) is nonnegative by (3). Hence \(N\le M\). An approximation argument gives the same bound when the energy is first justified on a core.

If the established decomposition charges \(e+\varepsilon\) to the high norm and \(L_B\) is the full nonlinear loss, take
\(\delta=e+\varepsilon+L_B\). With \(b_0=\beta-e-\varepsilon\), the self-map condition is
\[
\boxed{CR^2\le M\big[(b_0-L_B)M-n_{\rm eff}\big],\qquad n_{\rm eff}=\sqrt\beta\,d_F.}
\]
It retains the full-matrix gain in the residual while using the scalar lower only in the remaining estimates. A source improvement alone does not certify any operator, commutator, reference-ball, graph or self-map hypothesis.
