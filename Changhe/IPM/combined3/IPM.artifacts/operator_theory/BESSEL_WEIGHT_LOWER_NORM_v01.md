# An explicit lower-order Bessel/weight commutator bound

Let \(W(x)=\sqrt{1+4|x|^2}\), \(J=(1-\Delta)^{1/2}\), and \(0<a<1\). Then for every Schwartz g,
\[
\boxed{\|W^{-1}J^{2-a}(Wg)\|_2
\le\|J^{2-a}g\|_2+(2-a)\|J^{1-a}g\|_2+(4a+88)\|g\|_2.}
\tag{1}
\]
In particular, at \(a=3-q=9/10\),
\[
\|W^{-1}J^{q-1}(Wg)\|_2
\le\|J^{11/10}g\|_2+\tfrac{11}{10}\|J^{1/10}g\|_2
+\tfrac{458}{5}\|g\|_2.
\tag{2}
\]
This supplies a quantitative interpolation bridge if a separate actual transport-remainder estimate in this lower norm is proved. It does not assert that estimate for Ctr, and it does not assert a global analogous estimate for low-frequency Riesz source commutators.

## Proof

Let B_a be the positive Bessel kernel of J^-a, with mass one and heat representation
\[
B_a(z)=\frac1{\Gamma(a/2)}\int_0^\infty
e^{-t}t^{a/2-1}(4\pi t)^{-1}e^{-|z|^2/(4t)}\,dt.
\]
Taylor-expand the weight at x:
\[
W(x-z)-W(x)=-\nabla W(x)\cdot z+R(x,z).
\]
The elementary derivative bounds for this exact W are
\[
\|D^2W\|_{\infty,\mathrm{op}}\le4,\quad
\|\nabla\log W\|_\infty\le1,\quad
0\le\Delta W\le8.
\]
Consequently, viewing R as a function of y=x-z,
\[
|R|\le2|z|^2,\quad |\nabla_yR|\le4|z|,\quad
|\Delta_yR|\le8.
\tag{3}
\]
Since J^{2-a}=J^-a J²,
\[
W^{-1}J^{2-a}(Wg)=J^{2-a}g
+W^{-1}[J^{-a},W]J^2g
+W^{-1}J^{-a}[J^2,W]g.
\]
The linear Taylor term of the second summand is exactly \(a\nabla\log W\cdot\nabla J^{-a}g\), by Fourier differentiation of \(\langle\xi\rangle^{-a}\).

For the remainder, move J²=1-Delta from g onto the product B_a(z)R(x,z). The kernel is
\[
W(x)^{-1}[R(B_a-\Delta B_a)
-2\nabla_yB_a\cdot\nabla_yR-B_a\Delta_yR].
\tag{4}
\]
The following exact or upper kernel moments suffice:
\[
\int B_a=1,\qquad \int|z|^2B_a=2a,\qquad
\int|z||\nabla B_a|=2,\qquad
\int|z|^2|\Delta B_a|\le12.
\tag{5}
\]
The second follows by mixing the two-dimensional heat-kernel second moment 4t. The third follows by radial integration by parts, since B_a is radial decreasing. For the fourth, use
\(\Delta P_t=(|z|^2/(4t^2)-1/t)P_t\), and bound its absolute second moment by
\(\mathbb E|z|^4/(4t^2)+\mathbb E|z|^2/t=8+4=12\), then mix against the positive Gamma density.

Equations (3)--(5), and W>=1, dominate (4) pointwise by a convolution kernel with L1 norm at most
\[
2(2a+12)+8\cdot2+8=4a+48.
\]
Young's inequality proves this remainder bound. The integrations by parts introduce no contact term at zero: B_a=O(r^{a-2}), while R=O(r²), so the product is O(r^a), its first derivatives are O(r^{a-1}), and the boundary integrals on a shrinking circle are O(r^a). Its second derivatives are locally integrable because a>0. At infinity the Bessel kernel decays exponentially while the weight remainder grows at most quadratically.

The third summand must also be retained. Since
\([J^2,W]g=-2\nabla W\cdot\nabla g-(\Delta W)g\), commute each component of grad W past J^-a. Its leading part is \(-2\nabla\log W\cdot\nabla J^{-a}g\). Combined with the linear Taylor part above, the coefficient is a-2, with absolute value 2-a. For the new commutator remainder, integrate one derivative from g onto
\(B_a(x-y)(\nabla W(y)-\nabla W(x))\). Its absolute L1 kernel norm is at most
\(4\int r|\nabla B_a|+8\int B_a=16\). Its multiplier -2 therefore costs 32||g||2. The last Delta W term costs at most 8||g||2. Summing these with 4a+48 proves the claimed 4a+88 bound and completes (1).

Correction record: the preliminary derivation communicated before this note was complete omitted this third summand. Its coefficients a and 4a+48 were not valid for the full conjugated operator. No numerical certificate in this campaign uses that preliminary statement.

## Explicit interpolation consequence

For q=21/10 and K=||D^qg||2, Fourier subadditivity and interpolation give, for s in {1/10,11/10},
\[
\|J^sg\|_2\le\|g\|_2+\|D^sg\|_2
\le R^{1-s/q}K^{s/q}+R,\quad R=\|g\|_2.
\]
Hence the square of the lower norm in (2) is at most
\[
\left[R^{10/21}K^{11/21}
+\tfrac{11}{10}R^{20/21}K^{1/21}
+\tfrac{937}{10}R\right]^2.
\tag{6}
\]
Any independently certified bound |Ctr|<=C_tr times this lower norm squared can therefore be priced by an explicit one-dimensional scalar maximization or Young's inequality, after using a valid K-to-N estimate. No value of C_tr is supplied here.
