# Maximal growth and the carrier or vorticity zero set

This independently proves the rate characterization in LIT82. Its coverage consequence retains the separate partition and capture premise.

## Exact statement

Assume the hypotheses of the absorbing-core result with \(r=2\), and assume \(W\not\equiv0\). In particular \(0<c<1/2\), \(\omega\) is arbitrary, and the exact Euler profile is uniformly sublinear. Use \(a=1-2c\), \(\kappa=1+c\), \(d=3c\), and the complete flow \(\Psi\) of \(-B\).

For a closed strictly absorbing ball \(Q\), put

\[
K=\bigcap_{t\geq0}\Psi_t(Q),\qquad
Z=K\cap\bigl(\{B=0\}\cup\{W=0\}\bigr).
\]

Both are compact and invariant under the entire flow; \(K\) is nonempty. For a full-flow ergodic invariant probability \(\mu\), let \(\lambda_{\rm top}(\mu)\) be its largest Lyapunov exponent. Then

\[
\Lambda_{\rm core}
=\max_{\substack{\mu\ {\rm flow\ ergodic}\\ \operatorname{supp}\mu\subset K}}
\lambda_{\rm top}(\mu)\geq a.
\tag{1}
\]

The maximum is attained. If \(Z\ne\varnothing\), the maximum

\[
\Gamma_Z=
\max_{\substack{\mu\ {\rm flow\ ergodic}\\ \operatorname{supp}\mu\subset Z}}
\lambda_{\rm top}(\mu)
\]

is also attained. Set \(\Gamma_Z=-\infty\) when \(Z=\varnothing\). The exact formula is

\[
\boxed{\Lambda_{\rm core}=\max(a,\Gamma_Z).}
\tag{2}
\]

Every full-flow ergodic probability on \(K\) giving zero mass to \(Z\) has spectrum \((a,0,-\kappa)\), without an entropy or absolute-continuity conclusion.

For a \(C^r\) profile, \(r\geq2\), the additional condition \(\Gamma_Z<ra\) consequently supplies the growth hypothesis of the conditional coverage theorem. Equivalently, it suffices that every ergodic probability on \(Z\) have largest exponent strictly below \(ra\), because the maximum is attained.

## Reduction from the ball to its invariant core

The sets \(Q_t=\Psi_t(Q)\) are nested nonempty compact sets. They have nonempty intersection \(K\). Applying any fixed flow homeomorphism to the intersection shifts its time endpoint, which leaves the intersection unchanged. Thus \(K\) is invariant in both directions.

Every open neighborhood \(V\) of \(K\) contains \(Q_T\) for some \(T\). Otherwise choose \(t_j\to\infty\) and \(x_j\in Q_{t_j}\setminus V\). A convergent subsequence in \(Q\) has limit in each \(Q_t\) and in the closed complement of \(V\), contradicting the definition of \(K\).

For \(E=Q\) or \(K\), set \(M_t(E)=\max(1,\max_E\|D\Psi_t\|)\). The chain rule gives a rate \(\Lambda_E\). Inclusion gives \(\Lambda_K\leq\Lambda_Q\).

Fix an integer \(N\geq1\) and \(\epsilon>0\). Continuity provides a neighborhood \(V\) of \(K\) on which

\[
\max(1,\|D\Psi_N(x)\|)\leq M_N(K)+\epsilon,\qquad x\in V\cap Q.
\]

Choose \(T\) with \(Q_T\subset V\). For every later orbit segment of length \(N\), the same bound holds because \(Q_t\subset V\) for \(t\geq T\). Initial and final segments have a fixed finite bound. Hence

\[
M_{T+qN+s}(Q)\leq C_{T,N}(M_N(K)+\epsilon)^q,\quad 0\leq s<N.
\]

Taking logarithms, then \(q\to\infty\), \(\epsilon\downarrow0\), and the infimum over \(N\), proves \(\Lambda_Q\leq\Lambda_K\). Thus the ball and core rates agree. No rate of approach to \(K\) has been assumed.

For any nonempty compact invariant \(E\subset K\), also use the untruncated quantity

\[
D_t(E)=\max_E\|D\Psi_t\|,\qquad
\Gamma_E=\lim_{t\to\infty}t^{-1}\log D_t(E).
\]

Subadditivity proves existence. Uniform bounds for derivative and inverse derivative over unit time bound the limit above and below by finite constants. In particular \(\Lambda_E=\max(0,\Gamma_E)\). Keeping this untruncated rate is necessary when the maximal exponent is negative.

## An attained maximizing ergodic measure

We prove the variational assertion for any nonempty compact invariant \(E\subset K\). Over \(E\), consider the compact bundle \(E\times\mathbb {RP}^2\). Invertibility of the derivative gives a continuous complete projective flow

\[
F_t(x,[v])=(\Psi_t x,[D\Psi_t(x)v]).
\]

Write \(X=-B\). For a unit representative \(v\), define

\[
q(x,[v])=v\cdot\operatorname{sym}DX(x)v.
\]

This is continuous and independent of the representative's sign. The variational equation gives

\[
\log|D\Psi_t(x)v|=\int_0^t q(F_s(x,[v]))\,ds.
\tag{3}
\]

For each integer \(n\), compactness provides \(x_n,v_n\), \(|v_n|=1\), attaining \(D_n(E)\). Take a weakly convergent subsequence of the probabilities

\[
\eta_n=\frac1n\int_0^n\delta_{F_s(x_n,[v_n])}\,ds.
\]

For each fixed \(t\), shifting the integration interval changes any continuous test integral by at most \(2|t|\|f\|_\infty/n\). The limit \(\eta\) is therefore invariant under the whole flow. Equation (3) gives \(\int q\,d\eta=\Gamma_E\).

Conversely, for any invariant projective probability \(\zeta\), invariance and (3) yield

\[
\int q\,d\zeta
=\frac1n\int\log|D\Psi_n(x)v|\,d\zeta
\leq\frac{\log D_n(E)}n.
\]

Thus \(\int q\,d\zeta\leq\Gamma_E\). Decompose the maximizing \(\eta\) into full-flow ergodic components. Since all component integrals are at most \(\Gamma_E\) and their average equals it, almost every component attains it. Choose one, \(\eta_*\). Its projection \(\mu\) is full-flow ergodic: the lift of any invariant base set is an invariant projective set.

The compact cocycle and its inverse satisfy the integrability hypotheses of Oseledets. At a regular base point every nonzero vector has a forward Lyapunov exponent from its Oseledets components. Birkhoff applied to \(q\) and (3) shows that for \(\eta_*\)-almost every projective point this exponent is \(\Gamma_E\). Consequently \(\lambda_{\rm top}(\mu)\geq\Gamma_E\). The uniform derivative bound gives the reverse inequality for every invariant base probability. We have proved

\[
\Gamma_E=
\max_{\substack{\mu\ {\rm flow\ ergodic}\\ \operatorname{supp}\mu\subset E}}
\lambda_{\rm top}(\mu),
\tag{4}
\]

with attainment.

This proof does not suppose that the largest exponent is continuous in the base probability, that ergodic probabilities form a compact set, or that a full-flow ergodic probability is ergodic for the time-one map. Flow invariance makes the exponents invariant under every fixed flow time; equivalently, compact remainder estimates pass between continuous and integer times.

## Spectrum off the zero sets

The exact identities are

\[
D\Psi_t(x)B(x)=B(\Psi_t x),\qquad
D\Psi_t(x)W(x)=e^{-\kappa t}W(\Psi_t x),\qquad
\det D\Psi_t=e^{-dt}.
\tag{5}
\]

They make both zero sets invariant. Hence \(Z\) is closed and invariant. If a full-flow ergodic \(\mu\) is not concentrated on \(Z\), it gives \(Z\) zero mass, and both fields are nonzero almost everywhere.

Their norms are bounded on \(K\). The sets

\[
E_j=\{x\in K: |B(x)|\geq1/j,\ |W(x)|\geq1/j\}
\]

increase to a full-measure set. By Poincare recurrence for the measure-preserving time-one map, almost every point in each \(E_j\) returns to it infinitely often. This does not require ergodicity of that map.

At a recurrent Oseledets-regular point, the first identity in (5) gives upper directional exponent at most zero along \(B\), while these returns give a subsequential exponent at least zero. Since the directional limit exists, its exponent is zero. The second identity gives exponent \(-\kappa\) along \(W\) by the same argument. No integrability of \(\log|B|\) or \(\log|W|\) is used.

These directions are independent because their exponents differ. Thus zero and \(-\kappa\) occur among the three Lyapunov exponents. The determinant identity makes their sum \(-d\), so the third is \(\kappa-d=a>0\). This proves the claimed spectrum and largest exponent \(a\).

## Classification and conditional consequence

The absorbing-core lower bound gives \(\Lambda_K=\Lambda_{\rm core}\geq a>0\), so \(\Gamma_K=\Lambda_{\rm core}\). Applying (4) to \(E=K\) proves (1).

Every full-flow ergodic probability on \(K\) either is concentrated on \(Z\), with largest exponent at most \(\Gamma_Z\), or gives \(Z\) zero mass, with largest exponent \(a\). Therefore \(\Lambda_{\rm core}\leq\max(a,\Gamma_Z)\). The reverse inequality follows from the lower bound \(a\) and from \(Z\subset K\). This proves (2), including the empty-set convention.

If \(\Lambda_{\rm core}>a\), every maximizing ergodic probability is concentrated on \(Z\). If all ergodic probabilities on \(Z\) have largest exponent below \(ra\), the attained maximum has that strict bound. Formula (2) then gives \(\Lambda_{\rm core}<ra\).

For a \(C^r\) profile this supplies precisely the additional growth premise of the conditional coverage theorem in the companion proof. At \(r=2\), if the partition and capture theorem is established and its coverage conclusion fails, there must be an ergodic probability on \(Z\) with largest exponent at least \(2a\). This is a contraposition of a sufficient condition. It does not identify that measure as physical, describe its basin, or prove that it exists for every profile.

For example, a full-flow ergodic probability supported entirely on equilibria is a point mass. At an equilibrium \(p\), its largest exponent is the largest real part of an eigenvalue of \(-DB(p)\). The vorticity zero set can also support nonstationary measures. No upper bound for either class is proved here.

## Dependencies, evidence and scope

The full submitted LIT82 proof and its hash are in the team records. This audit reconstructed all arguments, including the projective maximization and recurrence step, without numerical computation.

Dependencies are the exact \(C^2\) identities from A378, the companion absorbing-core proof, compactness of probabilities on a compact metric space, Poincare recurrence, continuous-flow ergodic decomposition, Birkhoff and Oseledets. The projective variational assertion is proved here instead of imported as a separate theorem. If a closed ambient manifold is desired for the standard measure results, a cutoff outside a neighborhood of \(Q\) preserves every cocycle used here.

The primary decay-only nonexistence problem remains open. Neither smoothness nor velocity decay has been shown to exclude the degenerate maximizing measure.
