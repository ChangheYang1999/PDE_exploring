# Independent half-damping proof and a combined global/far IMS bound

The operator agent independently checked the root/finite-rank agents' new Q-norm dilation argument. The result below is proved in its full S1 form; no profile-dependent numerical input is needed.

Let \(T=WJ^{-2}W^{-1}\), \(W=\sqrt{1+4r^2}\), and \(l=\log W\). Then on the S1 subspace,
\[
\boxed{\operatorname{Re}\langle TG,G\rangle\ge\tfrac12\|J^{-1}G\|_2^2.}
\tag{1}
\]
This strengthens the previously proved nonnegativity and the earlier one-third bound.

## Bounded-form proof, including domains

For h in H1 and S1, put Fr=||h||2, Dr=||partial_r h||2, and Da=||r^-1 partial_theta h||2. Angular Poincare on each circle is valid because S1 has no angular mode zero. Since grad l is radial and |grad l|<=min(1,1/r),
\[
H_0[h]=\|\nabla h\|_2^2+\|h\|_2^2-\|h\nabla l\|_2^2
\ge D_r^2+F_r^2.
\]
Also H0>=||grad h||2², because |grad l|<=1. Consequently
\[
\tfrac12\|h\|_{H^1}^2\le H_0[h]\le\|h\|_{H^1}^2.
\tag{2}
\]
The skew part of M=T^-1=WJ²W^-1 has form
\[
B_0(h,v)=\langle\nabla h,v\nabla l\rangle-\langle h\nabla l,\nabla v\rangle.
\]
Only radial derivatives enter. Therefore
\[
|B_0(h,v)|\le D_r(h)F_r(v)+F_r(h)D_r(v)
\le\sqrt{H_0[h]H_0[v]}.
\tag{3}
\]
On scalar L2S1, let V=J^-1 M J^-1=H+B be its bounded form realization. Equation (2) gives I/2<=H<=I. Equation (3) says the skew-adjoint A=H^-1/2 B H^-1/2 has norm at most one. Hence
\[
V=H^{1/2}(I+A)H^{1/2},\qquad
\operatorname{Re}(I+A)^{-1}=(I-A^2)^{-1}\succeq I/2.
\]
Both inverses exist by coercivity, equivalently Lax--Milgram. Thus
\[
\operatorname{Re}V^{-1}\succeq\tfrac12H^{-1}\succeq I/2.
\]
The explicit T is bounded on L2 by its exponentially decaying Bessel kernel and the elementary weight-ratio bound. For a Schwartz S1 input, TG is Schwartz and solves M(TG)=G, so uniqueness of the coercive H1 weak inverse identifies T with J^-1 V^-1 J^-1. Density extends that identity and proves (1). No unbounded inverse is manipulated without this bounded-form realization.

## Independent review of the root's localization note

The kernel moments, far-block error 2/R², and IMS error in `../Q_DILATION_LOCALIZATION.md` are valid. In particular the exact Bessel-resolvent kernel moments are pi/2, 4, and 9pi/2 at orders one, two, and three. The weight-ratio estimate bounds the symmetric kernel by K(z)(1+2|z|). The phase Lipschitz constant is 3pi/(4R), so the stated T-IMS constant follows by Schur's test. Its positive pointwise kernel difference is used only as an absolute row bound, not as a positive-operator assertion.

There is a useful further combination. Use the same radial partition chi_N²+chi_F²=1 from that note. Its near block now has the half bound (1), while its far block has the full p² bound with the 2/R² error. The p² localization itself satisfies
\[
\left|\|pG\|_2^2-\|p\chi_NG\|_2^2-\|p\chi_FG\|_2^2\right|
\le\frac{9\pi^2}{8R^2}\|G\|_2^2.
\]
Combining these inequalities yields
\[
\boxed{\operatorname{Re}\langle TG,G\rangle
\ge\tfrac12\|pG\|_2^2+\tfrac12\|p\chi_FG\|_2^2
-\frac{98}{R^2}\|G\|_2^2.}
\tag{4}
\]
Indeed the exact error numerator is
\[
2+\frac{9\pi^2(4+9\pi)}{32}+\frac{9\pi^2}{16}<98.
\]
This bound retains global low-order damping as well as additional far damping. Every subsequent form must use exactly the indicated localized p norm or pay its own localization error.

For conversion to a physical localization of pG, the Bessel kernel of p=J^-1 has first absolute moment one. Hence ||[p,chi_F]||<=3pi/(4R). For any 0<delta<1,
\[
\|p\chi_FG\|_2^2\ge(1-\delta)\|\chi_FpG\|_2^2
-(\delta^{-1}-1)\frac{9\pi^2}{16R^2}\|G\|_2^2.
\tag{5}
\]
This optional conversion is explicit and must be included if used.

The damping is a component of the background energy. It does not bound the new transport or velocity-source remainders, certify an invariant ball, or establish a stationary solution by itself.

## Sharpened independent audit: the global constant is two thirds

The coordinator's subsequent improvement is valid. Put E=||h grad(log W)||2
and t=r². Its exact pointwise polynomial identity is
\[
1+\frac1t-3\frac{16t}{(1+4t)^2}
=\frac{1+t(4t-3)^2}{t(1+4t)^2}\ge0.
\]
Angular Hardy on S1 therefore gives F²+Dang²>=3E², so
\[
H_0[h]=D_{rad}²+F²+D_{ang}²-E²\ge D_{rad}²+2E².
\]
In the radial skew form the undifferentiated factor is E itself:
\[
|B_0(f,h)|\le D_{rad}(f)E(h)+E(f)D_{rad}(h)
\le\frac1{\sqrt2}\sqrt{H_0[f]H_0[h]}.
\]
The last inequality is the norm of the 2-by-2 off-diagonal matrix with
entries 1/sqrt2 in the metric (Drad,sqrt2 E). Thus the same bounded-form
realization now has ||A||<=1/sqrt2 and
\[
\operatorname{Re}V^{-1}
=H^{-1/2}(I-A²)^{-1}H^{-1/2}
\succeq\frac23H^{-1}\succeq\frac23I.
\]
Consequently
\[
\boxed{\operatorname{Re}\langle WJ^{-2}W^{-1}G,G\rangle
\ge\frac23\|J^{-1}G\|_2^2\quad(G\in S1).}
\tag{6}
\]
All domain and density identifications from the first part are unchanged.
This improves the available global damping to 2qc/3. The older half bounds
remain valid and may still be used, but they no longer give the strongest
available global constant.

## Strongest audited bound: exponential ground state and a gauge identity

The coordinator's exponential supersolution gives the stronger exact result
\[
\boxed{\operatorname{Re}\langle TG,G\rangle
\ge\left(1-\frac{\sqrt3}{8}\right)\|pG\|_2^2.}
\tag{7}
\]
Here is a self-contained form proof. For angular Fourier mode n with
|n|>=1, consider the radial form of H1−k E². Let s(r)=r exp(−r)>0.
Direct differentiation gives
\[
\frac{[-\partial_r^2-r^{-1}\partial_r+1+r^{-2}]s}s=\frac3r.
\]
For k=8/sqrt3 its difference from k ell² is nonnegative. Indeed, setting
z=2r/sqrt3,
\[
(1+4r²)^2-\frac{128}{3\sqrt3}r³
=(z-1)^2(9z²+2z+1)\ge0.
\]
The ground-state identity for an annular compactly supported mode u is
\[
\int(|u'|²+(1+r^{-2}-k\ell²)|u|²)r\,dr
=\int s²|(u/s)'|²r\,dr
+\int\frac{(H_{rad}-k\ell²)s}{s}|u|²r\,dr\ge0.
\]
The higher angular modes add (n²−1)/r²>=0. Annular modes are dense in
the S1 H1 form domain. At the origin one may alternatively use the direct
boundary limit s~r and smooth S1 modes u=O(r); the boundary term vanishes.
Thus H1[h]>=k E[h]² for all complexified S1 tests.

Write l=log W. The skew form is
\(B_0[h]=2i\operatorname{Im}\int\ell\cdot\nabla h\,\overline h\).
Consequently, for every real lambda,
\[
H_0[h]+i\lambda B_0[h]
=\|\nabla(e^{-i\lambda l}h)\|²+\|h\|²
-(1+\lambda²)\|\ell h\|².
\]
The gauge factor is radial, has modulus one, and has bounded gradient;
it preserves S1 and its H1 form domain. Choose lambda²=k−1. The preceding
ground-state inequality makes H0±i lambda B0 nonnegative. Passing to the
bounded relative skew operator A gives I±i lambda A>=0, so
\(||A||²<=1/(k-1)\). Therefore
\[
\operatorname{Re}V^{-1}
=H^{-1/2}(I-A²)^{-1}H^{-1/2}
\succeq\frac{k-1}{k}H^{-1}\succeq\frac{k-1}{k}I.
\]
The already verified identity T=J^-1 V^-1 J^-1 proves (7). In particular,
the clean weaker constants 7/9 and 3/4 also follow. This proof does not
assume positivity of a pointwise integral kernel as an operator.
