# Weighted velocity bounds using central oddness

Status: proved below by elementary Fourier identities; independent review requested.
This does not certify any remaining commutator norm or existence theorem.

Let \(W(x)=\sqrt{1+4|x|^2}\), and let \(\mathcal O\) be the closed subspace of functions satisfying
\(f(-x)=-f(x)\). The required S1 class (even in the first coordinate, odd in the second) is contained in \(\mathcal O\).
Use the convention
\[
U[f]=(-R_1R_2f,R_1^2f),\qquad
m(\theta)=(\cos\theta\sin\theta,-\cos^2\theta).
\]
Thus \(\widehat{Uf}(r,\theta)=m(\theta)\widehat f(r,\theta)\).
Both components of \(U\) and the vector adjoint \(U^*\) preserve central oddness.

## Angular Hardy inequality

For every \(F\in H^1(\mathbb R^2)\cap\mathcal O\),
\[
\int\frac{|F(\xi)|^2}{|\xi|^2}\,d\xi
\le\int\frac{|\partial_\theta F(\xi)|^2}{|\xi|^2}\,d\xi
\le\int|\nabla_\xi F|^2\,d\xi.
\tag{1}
\]
Indeed central oddness implies that the angular Fourier expansion contains only odd integers; their absolute values are at least one. Apply Parseval on each circle and integrate in \(dr/r\). Initially use smooth functions vanishing near the origin and infinity; the angular inequality itself and approximation extend the assertion to \(H^1\cap\mathcal O\). Equivalently one may apply the angular inequality to almost every circle directly and use polar-coordinate Sobolev derivatives.

## Positive weight

For scalar \(F\), periodic integration by parts in \(\theta\) gives the exact identity
\[
\int|\nabla_\xi(mF)|^2
=\int\cos^2\theta\,|\nabla_\xi F|^2
+2\int\frac{\cos^2\theta}{r^2}|F|^2.
\tag{2}
\]
To check the coefficient in the second term, use
\(|m|^2=\cos^2\theta\), \(|m'|^2=1\), and
\(|m'|^2-(m\cdot m')'=2\cos^2\theta\).
This also holds for complex \(F\), with real parts in the cross term.
By (1), the right-hand side of (2) is at most \(3\|\nabla_\xi F\|_2^2\).
Since \(|m|\le1\), Plancherel yields
\[
\boxed{\|WUf\|_{L^2(\mathbb R^2;\mathbb R^2)}\le\sqrt3\,\|Wf\|_2,\qquad f\in\mathcal O.}
\tag{3}
\]
For the adjoint, with central-odd vector input \(H\),
\[
\|\nabla_\xi(m\cdot H)\|_2
\le\|\nabla_\xi H\|_2+\|H/r\|_2
\le2\|\nabla_\xi H\|_2.
\]
Together with \(|m\cdot H|\le|H|\), this proves
\[
\boxed{\|WU^*H\|_2\le2\,\|WH\|_2.}
\tag{4}
\]
The positive-weight norms include the unweighted part: for example
\(\|WUf\|_2^2\le\|f\|_2^2+12\||x|f\|_2^2\le3\|Wf\|_2^2\).
The multiplier formulas, (1), and density also show that the displayed products have the asserted weak derivatives at \(\xi=0\); no distribution supported at zero is introduced.

## Negative weight

Duality in the central-odd subspaces gives
\[
\boxed{\|W^{-1}Uf\|_2\le2\,\|W^{-1}f\|_2,\qquad
\|W^{-1}U^*H\|_2\le\sqrt3\,\|W^{-1}H\|_2.}
\tag{5}
\]
For example the adjoint of \(W^{-1}UW\), on unweighted central-odd functions, is \(WU^*W^{-1}\), whose norm is at most two by (4). For inputs only in the negative-weight completion, (5) defines the continuous extension; on Schwartz inputs it agrees with the usual Fourier multiplier.

These facts do not follow for each single Riesz transform on this class: \(R_2\) can create an angular mode zero. Consequently (3)–(5) can be used for joint velocity-source forms, but cannot be substituted into a bound of separate \(R_j\) factors. Multiplication by a background coefficient must also be checked for its input/output parity before applying the bounds.

## Immediate consequence for one low-frequency pricing step

Let \(P\) be any radial Fourier multiplier and suppose
\(\|W^{-1}P(D)W\|_{2\to2}\le L_P\).
It preserves central oddness, and (5) implies
\[
\|W^{-1}UP(D)(Wf)\|_2\le2 L_P\|f\|_2.
\]
Thus joint \(U\) pricing has no additional divergent small-frequency cutoff factor. This statement supplies neither a numerical \(L_P\) nor a complete bound on the source commutator.
