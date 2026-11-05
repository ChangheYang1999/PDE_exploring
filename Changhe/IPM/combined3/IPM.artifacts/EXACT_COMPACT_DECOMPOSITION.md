# Exact background decomposition and the noncompact negative term

Status: the identities and qualitative compactness below follow from the actual coefficient structure and the cited proved commutator lemmas. No new quantitative norm bound for the full compact operator is asserted here.

Use the actual Candidate 013 coefficients, \(q=21/10\), \(W^2=1+4|X|^2\), and
\[
V=cX+u_*,\quad S=\operatorname{Sym}Du_*,\quad A=cI+S,\quad
a_W=V\cdot\nabla\log W,\quad\widetilde a=a_W-c,\quad d=c+1+a_W,
\]
\[
K=\begin{pmatrix}-(\rho_*)_y&(\rho_*)_x/2\\(\rho_*)_x/2&0\end{pmatrix},\qquad
\mathcal M_*=dI-qA-K.
\]
Here \(K\) denotes a coefficient matrix, rather than the compact operator below. Put \(p=J^{-1}\), \(m=|D|J^{-1}\), \(n=1-m\), and \(v=RG\).
For the unperturbed background generator \(L_*\), its conjugated energy is exactly
\[
\begin{aligned}
\mathfrak Q_*(G)
&=\operatorname{Re}\langle J^qWL_*W^{-1}J^{-q}G,G\rangle\\
&=-\int v^T\mathcal M_*v-qc\|pG\|_2^2+\langle\mathcal K_cG,G\rangle.
\end{aligned}
\tag{1}
\]
All quadratic operators are represented by their self-adjoint real parts. The compact remainder in (1) is
\[
\boxed{\mathcal K_c[G]
=T_{IS}(G)+T_{II}(G)+C_{tr}(G)+C_{aw}(G)
+C_{vs1}(G)+C_{vs2}(G)+C_{vs3}(G)
-q\langle S pRG,pRG\rangle.}
\tag{2}
\]
In particular, the constant negative multiplier \(-qcJ^{-2}\) is retained exactly. Using \(-q(c-\|S\|_\infty)J^{-2}\) instead throws away a potentially large part of the available far-field damping.

## Exact component forms

With all pairings real parts when needed,
\[
\begin{aligned}
T_{IS}(G)&=\frac q2\langle([n,[S,n]]-[p,[p,S]])v,v\rangle,\\
T_{II}(G)&=\frac12\sum_j\langle[[\widetilde a,R_j],R_j]G,G\rangle,\\
C_{tr}(G)&=\langle[J^q,u_*\cdot\nabla]J^{-q}G,G\rangle
-q\langle S mRG,mRG\rangle,\\
C_{aw}(G)&=-\langle[J^q,a_W]J^{-q}G,G\rangle,\\
C_{vs1}(G)&=\langle[J^q,\nabla\rho_*\cdot]J^{-q}U[G],G\rangle,\\
C_{vs2}(G)&=\langle J^q E_W J^{-q}G,G\rangle,\\
E_Wf&=\nabla\rho_*\cdot[W,U]W^{-1}f,\\
C_{vs3}(G)&=\langle\nabla\rho_*\cdot U[G],G\rangle-\langle KRG,RG\rangle.
\end{aligned}
\tag{3}
\]
These are combined2 `theory_agent_2/notes/T2_H4_v01.md`, section 2, with the corrected center substituted. The identity \(m^2+p^2=1\), the real-part double-commutator identity, and \(\sum R_j^*R_j=I\) give (1)–(2) directly. No inequality is used in this rearrangement.

For the source and scalar-weight joint form it is useful to set \(M=\widetilde aI-K\). If \(\omega(\xi)=\xi/|\xi|\), \(\tau=\langle\xi\rangle/\langle\eta\rangle\), and \(\zeta=\xi-\eta\), then \(T_{II}+C_{aw}+C_{vs1}+C_{vs3}\) has exact Hermitian Fourier kernel
\[
-\frac12\sum_{jk}\widehat M_{jk}(\zeta)
\left[(\omega_j(\xi)-\omega_j(\eta))(\omega_k(\xi)-\omega_k(\eta))
+(\tau^q-1)\omega_j(\eta)\omega_k(\eta)
+(\tau^{-q}-1)\omega_j(\xi)\omega_k(\xi)\right].
\tag{4}
\]
Fourier pairings use the combined2 normalization \((2\pi)^{-4}\iint\cdots\widehat G(\eta)\overline{\widehat G(\xi)}\,d\eta d\xi\). Formula (4) preserves cancellation among the four terms; pricing its entries independently need not be efficient.

## Why these operators are compact globally

The exact-data structural verifier proves all-order background bounds with \(\gamma=1-1/c>0\): \(D^j\nabla\rho_*\), \(D^jDu_*\), and \(D^j\widetilde a\) decay at least as the appropriate powers of \(\langle X\rangle\). In particular \(S,K,\widetilde a\in C_0\), and all needed higher derivatives are bounded and vanish at infinity.

For bounded \(f\in C_0\) and bounded Fourier multiplier \(b\) tending to zero at frequency infinity, \(f(X)b(D)\) is compact. To see this, approximate f and b uniformly by bounded compactly supported functions. Their product operator is Hilbert–Schmidt, since both approximants are L2. This is a spatial and frequency localization proof; no smoothness at \(\xi=0\) is needed.

Apply it to \(b=pR_j\) or \(nR_j\). Expanding the double commutators in \(T_{IS}\) shows each term has a factor of the form \(S pR_j\), \(S nR_j\), or its adjoint. Thus \(T_{IS}\) is compact, as is \(\sum(pR_j)^*S_{jk}(pR_k)\).

For \([R_j,f]\) with the actual smooth decaying coefficients, a direct kernel proof also supplies global compactness. First approximate f uniformly by a smooth compactly supported coefficient; the commutator norm error is at most \(2\|f-f_R\|_\infty\). For the compactly supported coefficient, exclude \(|x-y|<\delta\); the excluded weak singularity has Schur norm \(O(\delta\|\nabla f\|_\infty)\). Then exclude \(|x-y|>L\); since at least one kernel variable lies in the fixed support, this part has Hilbert–Schmidt norm \(O(L^{-1}\|f\|_2)\). The remaining bounded-support nonsingular kernel is Hilbert–Schmidt. This proves compactness of the Riesz commutators, hence of \(T_{II}\) and \(C_{vs3}\), without an inference from order alone.

For \(C_{tr},C_{aw},C_{vs1}\), use combined2 NR-2 (K3) in its stated actual-background scope: subtracting the displayed principal symbol leaves negative-order operators whose coefficient derivatives vanish spatially. The localization criterion just described, applied after the symbol expansion on each localized region and uniform control of its remainder seminorms, proves compactness. This step uses the inherited commutator calculus proof, rather than asserting compactness for arbitrary negative-order operators.

Finally \(E_W\) is compact on Hq by combined2 NR-2 Lemma E, now with its actual coefficient hypotheses discharged by the exact finite algebraic profile and \(1<1+\gamma\). Its proof cuts the near-diagonal weak singularity in space, bounds the remote coefficient tail in Schur norm, and treats the off-diagonal kernel as Hilbert–Schmidt. Conjugation by \(J^q\) gives compactness of \(C_{vs2}\) on L2.

This proves global compactness of \(\mathcal K_c\). It does not give the quantitative finite-rank tail required for existence.

## The genuinely noncompact lower-order term

The multiplier \(J^{-2}\) is bounded, smoothing, and noncompact on \(L^2(\mathbb R^2)\). For any nonzero compactly supported smooth S1 function translated to four reflected distant supports with S1 signs, the resulting normalized sequence converges weakly to zero, while its J−2 image norm stays bounded away from zero: the translated components become asymptotically orthogonal. Thus compactness cannot be inferred from negative order on the whole plane, even after imposing S1 symmetry.

In (1) this term has a favorable sign. It can be kept as an exact negative quadratic form in the finite-rank and far-field verification. The matrix principal form is also noncompact and is retained pointwise. No unfavorable noncompact term is concealed in (2).
