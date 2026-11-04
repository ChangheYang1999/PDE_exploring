# Derivative growth on an absorbing Euler core

This is the independent audit of LIT81. The rate statements below are confirmed. The final coverage implication is conditional on the separately stated interval partition and incoming-measure theorem. It is not a proof of that theorem.

## Statement and notation

Let \(r\geq2\) be an integer, \(0<c<1/2\), and \(\omega\in\mathbb R\). Suppose \(U\in C^r(\mathbb R^3;\mathbb R^3)\), \(P\in C^1(\mathbb R^3)\), and

\[
\operatorname{div}U=0,\qquad
(1-c)U+(B\cdot\nabla)U+\omega JU+\nabla P=0,
\quad B=(cI-\omega J)y+U,
\]

where \(Jy=(-y_2,y_1,0)\). Assume \(U(y)=o(|y|)\) uniformly at infinity. Put

\[
W=\operatorname{curl}U,\quad a=1-2c,\quad \kappa=1+c,
\quad \Psi_t=\text{the flow of }-B.
\]

The flow is complete in both time directions: \(B\) is locally Lipschitz and has at most linear growth. Choose \(R,b>0\) such that \(B(y)\cdot y\geq b|y|^2\) for \(|y|\geq R\). Uniform sublinearity allows \(b=c/2\) and sufficiently large \(R\). Let \(Q_R=\{|y|\leq R\}\).

Define, using the Euclidean operator norm,

\[
M_n(R)=\max\left(1,\max_{Q_R}\|D\Psi_n\|\right).
\]

Then

\[
\Lambda_{\rm core}
=\lim_{n\to\infty}\frac{\log M_n(R)}n
=\inf_{n\geq1}\frac{\log M_n(R)}n
\]

exists, is finite, and does not depend on the admissible radius, on replacing integer time by real time, or on replacing the fixed norm by an equivalent fixed norm. If \(W\not\equiv0\), then

\[
a\leq\Lambda_{\rm core}
\leq\max\left(0,\max_{Q_R}
\lambda_{\max}(-cI-\operatorname{sym}DU)\right).
\tag{1}
\]

For any integer \(r\geq2\), the condition \(\Lambda_{\rm core}<ra\) is equivalent to the existence of a positive integer \(N\) with \(\log M_N(R)<Nra\).

The localized finite-curve estimates use only \(\Lambda_{\rm core}<ra\), rather than a derivative-growth bound for an arbitrary cutoff outside \(Q_R\). Subject to the complete partition and capture theorem specified below, this condition yields countable vortical SRB basin coverage. It is an extra profile-dependent condition, including when \(r=2\).

## Existence and independence of the rate

The strict inward boundary condition makes \(Q_R\) forward invariant. The chain rule therefore gives \(M_{n+m}(R)\leq M_n(R)M_m(R)\). For fixed \(N\), write \(n=qN+s\), \(0\leq s<N\). Then

\[
\frac{\log M_n(R)}n
\leq\frac{q\log M_N(R)}n+
\frac{\max_{0\leq s<N}\log M_s(R)}n.
\]

The upper limit is at most \(\log M_N(R)/N\). Taking the infimum over \(N\), and using the immediate lower bound by that infimum, proves the limit formula. Compact derivative bounds over unit time give finiteness.

Let \(R_1<R_2\) be admissible. While an orbit has radius at least \(R_1\), its radius satisfies \(\dot r\leq-b_1r\). Any integer \(T>\log(R_2/R_1)/b_1\) consequently satisfies \(\Psi_T(Q_{R_2})\subset\operatorname{int}Q_{R_1}\). Once an orbit enters it cannot leave; boundary points enter immediately. If \(C_T=\max(1,\max_{Q_{R_2}}\|D\Psi_T\|)\), the chain rule gives

\[
M_n(R_1)\leq M_n(R_2),\qquad
M_{n+T}(R_2)\leq C_TM_n(R_1).
\]

Dividing logarithms by time proves equality of the two rates.

For \(0\leq s\leq1\), both \(D\Psi_s(y)\) and its inverse matrix are uniformly bounded for \(y\in Q_R\). The inverse variational equation is evaluated along the same forward orbit segment in \(Q_R\), so no backward trapping assumption is required. Writing \(t=n+s\) shows that \(M_t(R)\) and \(M_n(R)\) differ by a uniformly bounded multiplicative factor. Their logarithms divided by time have the same limit. Fixed equivalent norms likewise change operator norms by at most a fixed factor.

The finite-iterate characterization follows directly from the infimum formula. It asserts existence of a strict upper-bound certificate; no derivative norm of an unknown profile has been computed.

## Euler lower bound and strain upper bound

The already checked \(C^2\) identities are

\[
\alpha=(B\times W)\cdot dy,\qquad
d\alpha=a\,\iota_W{\rm vol},\qquad
\Psi_t^*\alpha=e^{at}\alpha.
\tag{2}
\]

Here \(\alpha\) is \(C^1\). At a point where \(\alpha=0\) and \(W\ne0\), the first identity in (2) makes at least one first derivative of a coefficient of \(\alpha\) nonzero. Locally its zero set is contained in a \(C^1\) hypersurface. A countable local cover shows that \(\{\alpha=0,W\ne0\}\) has three-dimensional measure zero.

If \(W\not\equiv0\), its nonzero set is open and nonempty. Hence some point satisfies \(\alpha\ne0\). Exact transport preserves this property. Move the point forward into \(Q_R\) and denote it by \(y\). With \(A_R=\max_{Q_R}|\alpha|>0\), (2) implies

\[
e^{an}|\alpha(y)|\leq A_R\|D\Psi_n(y)\|.
\]

This proves the lower bound in (1). It uses neither a regular invariant measure nor any avoidance of zeros by the limiting core.

For the upper bound set \(v_t=D\Psi_t(y)v\). Along the trapped orbit,

\[
\tfrac12\frac{d}{dt}|v_t|^2
=v_t\cdot(-cI-\operatorname{sym}DU(\Psi_t y))v_t.
\]

The rotation matrix contributes zero because it is skew. Gronwall proves the upper bound in (1). This cancellation does not make the actual growth independent of \(\omega\).

## Exact localization of the finite-curve argument

Suppose \(\Lambda_{\rm core}<ra\). Choose

\[
\Lambda_{\rm core}<L<ra,\qquad L/r<\chi<\chi'<a.
\]

For every sufficiently large integer \(p\), \(\max_{Q_R}\|D\Psi_p\|\leq e^{pL}\). Fix such a \(p\), put \(g=\Psi_p\), \(M=e^{pL}\), and only then choose \(0<\epsilon\leq1\) so that

\[
\epsilon^{j-1}\max_{Q_R}\|D^jg\|\leq M,\qquad 2\leq j\leq r.
\tag{3}
\]

All derivatives are bounded because \(g\) is \(C^r\) and \(Q_R\) is compact.

Every current curve and every descendant lies in \(Q_R\). The Taylor argument in A393 expands the parameter map \(g\circ\gamma\); its chain-rule terms evaluate \(D^jg\) only at points \(\gamma(t)\) of that curve. It does not expand along a Euclidean segment leaving \(Q_R\). Thus (3) supplies precisely its required bounds.

Put

\[
L^-_R=\max\left(0,\max_{Q_R}
\lambda_{\max}(cI+\operatorname{sym}DU)\right).
\]

The inverse matrix along each length-\(p\) forward segment has norm at most \(e^{pL^-_R}\). Consequently the tangent ratio for \(g\) lies between \(e^{-pL^-_R}\) and \(e^{pL}\). There are at most \(\lceil p(L+L^-_R)\rceil+5\) relevant integer labels. The inverse bound enters this label count, not the threshold \(ra>L\).

The fixed-word estimate uses \(h=p\chi+2\) and a safe target exponent \(p\chi'-3\). Its small-run decay parameter is

\[
\gamma_*=\frac{rh-pL}{r-1}-\log C_r.
\]

It grows linearly in \(p\), whereas the logarithm of the label count grows logarithmically. The finite-time estimates therefore apply for one sufficiently large fixed \(p\), followed by one fixed \(\epsilon\). Bounds for the finitely many remainder maps preserve the tangent upper exponent when passing to multiples of \(p\).

This paragraph confirms the localization and parameter choices. It does not assume that a labelled overlapping cover is already a partition.

## Conditional coverage interface

The additional premise is the complete endpoint-partition theorem in `in the team records`, or the independent LIT80 greedy construction, together with its original-arc incoming-measure conclusion using A257, A201, A216 and A299. These premises remain explicitly separate until their own verdict.

Given them, the localization above supplies their derivative hypotheses for every positive-volume target in \(\{W\ne0\}\cap\operatorname{int}Q_R\). Remove the null set \(\{\alpha=0,W\ne0\}\). Equation (2) gives tangent operator growth at least \(a\). Since one of three coordinate columns has at least the operator norm divided by \(\sqrt3\), one fixed coordinate direction has upper exponent at least \(a\) on a positive-volume subtarget. Fubini then provides a straight short arc containing a positive-length part of that target. All its descendants stay in \(Q_R\).

Limiting curves also stay in \(Q_R\), as do their fixed inverse iterates, obtained as limits of earlier descendants. An auxiliary \(C^r\) vector field on a closed three-manifold can agree with \(-B\) on a neighborhood of \(Q_R\): multiply by a smooth cutoff in a larger ball and extend by zero through a chart of \(S^3\). Its derivatives on these orbit segments agree exactly with the original flow. No derivative growth of the extension enters (3) or \(L\).

At \(r=2\), uniform second derivatives give \(C^1\) compactness and \(C^{1,1}\) limiting arcs. The separately audited capture interfaces use a \(C^2\) carrier and \(C^1\) vorticity, so no \(C^3\) bootstrap is supplied or needed at this step.

The stated premise then captures part of every positive-volume residual target in a full-flow ergodic physical basin, with spectrum \((a,0,-\kappa)\), entropy \(a\) for \(\Psi_1\), and absolutely continuous unstable conditionals. Distinct basins have positive volume and are disjoint, so there are at most countably many. Residual capture proves coverage inside \(Q_R\). Finally

\[
\mathbb R^3=\bigcup_{n\geq0}\Psi_{-n}(\operatorname{int}Q_R).
\]

Finite-time diffeomorphisms preserve null sets, and basins are invariant. This extends the conditional coverage globally. A223 supplies the corresponding essential domains with its exact hypotheses.

## Verification and scope

The submitted proof was read in full and retained with its hash in the team records. The audit reconstructed the radius comparison, inverse-segment estimate, covector lower bound, parameter order and compact-manifold localization. No numerical computation was used for this result.

The standalone dependencies are elementary ODE theory, compactness, the chain rule, Gronwall, the implicit function theorem and Fubini, together with the exact Euler identities confirmed in A378. A393-A394 supply the finite-curve estimates. The coverage dependencies are expressly conditional as stated above.

There is no proof that \(\Lambda_{\rm core}<2a\) holds for every decaying \(C^2\) profile. There is also no helicity-sign or nonexistence conclusion here.
