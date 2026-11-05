# A direct compactness proof for the remaining old-route commutators

Status: qualitative compactness proved for the actual coefficient class. This supplies no quantitative finite-rank tail and is not used by the preferred local-Q energy argument.

This supplement independently justifies the Ctr, Caw, and Cvs1 compactness claims in `../EXACT_COMPACT_DECOMPOSITION.md` without an appeal to an unavailable archived pseudodifferential-calculus audit program. The proof uses the explicit Fourier Taylor inequalities already proved in the campaign, exact coefficient decay, and Hilbert-Schmidt truncations.

Let q=21/10 and use the unitary dimension-two transform. Write

\[
M_s(a)=(2\pi)^{-1}\int |\zeta|^s|\widehat a(\zeta)|\,d\zeta.
\]

The actual coefficients satisfy \(u\in S^s\), \(s=1/c<1\), and \(b,\widetilde a\in S^{-\gamma}\), \(\gamma=1-s>0\). All needed homogeneous moments exist in the cutoff-limit sense proved below.

## 1. Decaying scalar coefficient commutators

Put \(T_a=[J^q,a]J^{-q}\). The elementary symbol inequality gives

\[
|J(\eta+\zeta)^q-J(\eta)^q|J(\eta)^{-q}
\le q2^{q-2}\{|\zeta|J(\eta)^{-1}+|\zeta|^qJ(\eta)^{-q}\}.
\]

If \(P_{>N}\) is the projection onto \(|\eta|>N\), Young's inequality yields

\[
\|T_aP_{>N}\|_{2\to2}
\le q2^{q-2}\{M_1(a)\langle N\rangle^{-1}
+M_q(a)\langle N\rangle^{-q}\}.
\tag{1}
\]

For a smooth compactly supported a, \(T_aP_{\le N}\) is Hilbert-Schmidt. Its two Fourier kernels are

\[
(2\pi)^{-1}J(\xi)^q\widehat a(\xi-\eta)J(\eta)^{-q}1_{|\eta|\le N},
\qquad(2\pi)^{-1}\widehat a(\xi-\eta)1_{|\eta|\le N}.
\]

Their squared integrals are finite because \(\widehat a\) is Schwartz and the input frequency lies in a bounded disk. Equation (1) makes T a norm limit of compact operators.

For the actual decaying coefficient, set \(a_R=\chi(X/R)a\) with a smooth radial cutoff. Product differentiation and the exact all-order decay give

\[
\|D^j(a_R-a)\|_2=O(R^{1-\gamma-j}),\qquad j\ge1.
\]

The homogeneous Wiener inequalities at derivative pairs (1,3) and (2,4) imply
\(M_1(a_R-a)\to0\) and \(M_q(a_R-a)\to0\). Thus the same full-operator Young bound gives \(\|T_{a_R}-T_a\|\to0\). The limiting commutator is the actual distributional commutator on Schwartz tests, since coefficient cutoffs converge there and J is a continuous tempered multiplier. Therefore T is compact.

Applying this to \(\widetilde a=a_W-c\) proves compactness of Caw. Applying it componentwise to b proves compactness of

\[
\sum_j[J^q,b_j]J^{-q}U_j,
\]

because each Uj is a bounded L2 multiplier. This is Cvs1. Neither proof assumes that the growing coordinate coefficient xb is square-integrable.

## 2. The transport commutator after its principal term

The exact first Taylor term of \([J^q,u\cdot\nabla]J^{-q}\) is

\[
P_u=-q\sum_{kj}(\partial_ku_j)\partial_{kj}J^{-2}.
\]

Let R2,u denote its remainder. The Hessian symbol bound gives

\[
|r_2(\eta+\zeta,\eta)|
\le c_q|\zeta|^2\{J(\eta)^{q-2}+|\zeta|^{q-2}\},
\qquad c_q=q(q-1)/2.
\]

Including the input derivative \(i\eta\) and J^-q gives the operator-tail bound

\[
\|R_{2,u}P_{>N}\|_{2\to2}
\le c_q\{M_2(u)\langle N\rangle^{-1}
+M_q(u)\langle N\rangle^{1-q}\}.
\tag{2}
\]

For smooth compactly supported u, \(R_{2,u}P_{\le N}\) is Hilbert-Schmidt: the two full-commutator kernels have the preceding compact-coefficient form with the extra bounded input factor \(i\eta\), and \(P_uP_{\le N}\) is Hilbert-Schmidt as a compactly supported coefficient times a bounded-disk frequency multiplier. Equation (2) proves compactness of this remainder.

For the actual growing velocity use \(u_R=\chi(X/R)u\). The exact symbol class gives

\[
\|D^j(u_R-u)\|_2=O(R^{1+s-j}),\qquad j\ge2.
\]

Since s<1, the derivative pairs (2,4) imply
\(M_2(u_R-u)\to0\) and \(M_q(u_R-u)\to0\). The full version of (2), with N=0, therefore proves convergence of the remainders in operator norm. Their distributional limit on Schwartz tests is precisely the actual remainder. Thus R2,u is compact. No divergence-free property of the intermediate cutoff velocity is needed for this Fourier estimate.

It remains to compare the exact first Taylor term with the prescribed principal quadratic form. Let \(\widetilde R_j=\partial_jJ^{-1}=mR_j\). Moving one skew-adjoint Bessel Riesz factor through \(\partial_ku_j\) gives

\[
\Re\langle P_uG,G\rangle
-q\langle S\widetilde RG,\widetilde RG\rangle
=q\Re\sum_{kj}\langle[\widetilde R_k,\partial_ku_j]\widetilde R_jG,G\rangle.
\]

Each coefficient \(\partial_ku_j\) is smooth and vanishes at infinity. Its ordinary Riesz commutator is compact by the explicit localized kernel proof in the decomposition note. Also

\[
[\widetilde R_k,a]=R_k[m,a]+[R_k,a]m,
\qquad [m,a]=-[1-m,a].
\]

The multiplier 1-m tends to zero at frequency infinity, so both products with the C0 coefficient a are compact by spatial/frequency localization. Hence the displayed Bessel Riesz commutators are compact. Together with R2,u this proves the actual Ctr compactness.

## 3. Remaining pieces and exact scope

The TIS, TII, Cvs3, and localized pS p pieces have the direct localization/commutator proofs in the decomposition note. The actual weighted EW still uses the explicit inherited NR2 Lemma E kernel proof. That proof is present in `combined2/IPM.artifacts/THEORY_NEW_RESULTS.md`, NR2, and its hypotheses are satisfied: coefficient derivatives decay with \(\gamma>0\), and the weight exponent satisfies \(1<1+\gamma\). The near-diagonal cutoff, remote Schur tail, far Hilbert-Schmidt kernel, differentiated kernels, and compact-cutoff interpolation justify its Hq compactness.

Thus the old compact remainder is qualitatively compact for the actual Candidate013 coefficient class. A certified finite-rank approximation of that entire operator with a closing quantitative tail remains absent. The existing rank-one Cvs3 certificate does not supply it. The favorable \(-qcJ^{-2}\) term remains noncompact and should remain outside this remainder.
