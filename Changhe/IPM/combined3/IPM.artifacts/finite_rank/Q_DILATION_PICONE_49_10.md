# Improved global dilation damping by an explicit Picone weight

Status: proved. This supersedes the smaller global constants in the earlier rational SOS note. It remains only an auxiliary damping estimate.

Let \(W^2=1+4r^2\), \(\ell=\nabla\log W\), and \(T=WJ^{-2}W^{-1}\). On S1,
\[
 \boxed{\operatorname{Re}\langle TG,G\rangle
 \ge\frac{39}{49}\|J^{-1}G\|_2^2.}
\]
The proof uses the positive radial comparison function
\[
 s(r)=\frac{r e^{-r}}{(1+r/4)^{3/2}},\qquad
 \frac{(-\partial_r^2-r^{-1}\partial_r+1+r^{-2})s}{s}
 =\frac{51r+264}{4r(r+4)^2}.
\]
Its right side is at least \((49/10)|\ell|^2\). After multiplication by the positive denominator this assertion is the polynomial inequality
\[
 P(r)=5024r^5+17152r^4-46096r^3+21120r^2+510r+2640\ge0.
\]
For \(r\ge1\), writing \(u=r-1\),
\[
 P=350-1810u+35984u^2+72752u^3+42272u^4+5024u^5>0,
\]
because the initial quadratic has minimum
\(350-1810^2/(4\cdot35984)=11775375/35984>0\).
For \(0\le r\le1\), writing \(v=1-r\),
\[
 P=350+1810v+v^2(35984-72752v+42272v^2-5024v^3).
\]
Since \(v^3\le v^2\), its parenthesis is at least
\(35984-72752v+37248v^2\), whose minimum is
\(267479/582>0\). All identities and rational signs are checked by the companion script.

Picone's identity, first on smooth tests supported on an annulus, and angular Poincare on S1, now give
\[
 \|f\|_{H^1}^2\ge k\|\ell f\|_2^2,\qquad k=49/10.
\]
Annular tests are dense in H1S1: the small-origin cutoff error is controlled by \(\|f/r\|_2\), and the large-radius cutoff error by the H1 norm. Thus the inequality holds on H1S1, including complex tests.

Write the inverse of \(T\) as \(M=H_0+B_0\), where the symmetric form is \(H_0[f]=\|f\|_{H^1}^2-\|\ell f\|_2^2\), and the skew form is
\[
 B_0(f,h)=\langle\ell\partial_rf,h\rangle-\langle\ell f,\partial_rh\rangle.
\]
The radial phase \(e^{i\lambda\log W}\) preserves S1 and is an H1 isomorphism. Completing the square shows that \(H_0\pm i\lambda B_0\) is unitarily gauge-equivalent in its form expression to
\[
 \|f\|_{H^1}^2-(1+\lambda^2)\|\ell f\|_2^2.
\]
Taking \(\lambda^2=k-1\) proves that the skew part, relative to \(H_0\), has norm at most \(1/\sqrt{k-1}\).

For the bounded operator \(V=J^{-1}MJ^{-1}=H+B\), one has \(H\le I\). With \(A=H^{-1/2}BH^{-1/2}\), the preceding form bound gives \(\|A\|\le1/\sqrt{k-1}\). Thus
\[
 \operatorname{Re}V^{-1}=H^{-1/2}(I-A^2)^{-1}H^{-1/2}
 \ge\frac{k-1}{k}H^{-1}\ge\frac{k-1}{k}I.
\]
Since \(T=J^{-1}V^{-1}J^{-1}\), the boxed estimate follows. The inverse/domain argument is the same coercive bounded-form construction already recorded in QNORM_BACKGROUND_IDENTITY.md.
