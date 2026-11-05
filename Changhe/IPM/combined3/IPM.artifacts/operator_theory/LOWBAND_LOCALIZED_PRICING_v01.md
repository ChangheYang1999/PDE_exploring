# A certified localized low-band price and its TIS application

Status: analytic kernel estimate and executed scalar certificate. At the actual near strain coefficient it uses the inherited certified global bound \(\|\operatorname{Sym}Du_*\|_{\infty,\mathrm{op}}\le137/125\). It supplies the particular low-band form bound below. It does **not** bound the remaining high-band, far, transport, or velocity-source forms and does not close existence.

Set \(q=21/10\), \(\nu=1/40\), \(\psi_\nu(\xi)=e^{-(|\xi|/\nu)^4}\), and \(W(x)=\sqrt{1+4|x|^2}\). Let \(R=(R_1,R_2)^T\), \(p=J^{-1}\), \(n=I-|D|J^{-1}\). All scalar multipliers below act componentwise on vectors. Convolution kernels use inverse factor \((2\pi)^{-2}\).

## 1. Kernel bounds with explicit constants

For \(\bar q\in\{q,q-1\}\), let K be the vector kernel of \(R\psi_\nu J^{\bar q}\). For every \(0<\nu\le1/40\),
\[
\boxed{|K(z)|\le\frac{3\nu^2}{10\pi},\qquad
|K(z)|\le\frac4{\pi|z|^2},\qquad
\|K\|_2^2\le\frac{\nu^2}{2\pi}.}
\tag{1}
\]
K is a radial scalar times the radial unit vector, up to a sign.

Here is a complete derivation. Put \(b(s)=e^{-(s/\nu)^4}(1+s^2)^{\bar q/2}\). Angular Fourier integration gives
\[
K(z)=-\frac{z}{2\pi|z|}\int_0^\infty s b(s)J_1(s|z|)\,ds.
\tag{2}
\]
The elementary bound \(|J_1|\le1\) follows from its angular integral representation. Write \(t=s/\nu\), \(\delta=\nu^2\), \(a=\bar q/2\in\{11/20,21/20\}\), \(H(t)=(1+\delta t^2)^a\). Since \(H\le(1+\delta t^2)^2\),
\[
\int_0^\infty s b(s)\,ds
\le\nu^2\left(\frac{\sqrt\pi}{4}+\frac{\nu^2}{2}+\frac{\sqrt\pi\nu^4}{8}\right)
<\frac35\nu^2.
\]
This proves the first bound in (1). For the L2 bound, Plancherel gives
\[
\|K\|_2^2=\frac1{2\pi}\int_0^\infty s b(s)^2\,ds.
\]
Use \((1+\delta t^2)^{\bar q}\le(1+\delta t^2)^3\), \(e^{-2t^4}\le e^{-t^4}\), and
\(\int_0^\infty t^m e^{-t^4}\,dt=\Gamma((m+1)/4)/4\). Its bracket is at most
\(\tfrac12+\tfrac34\delta+\tfrac34\delta^2+\tfrac14\delta^3<1\), using \(\sqrt\pi<2\). This proves the third bound.

For the tail, first establish
\[
\left|\int_0^T J_0(u)\,du\right|<2\quad(T\ge0).
\tag{3}
\]
Indeed the angular representation gives
\[
\int_0^T J_0(u)\,du
=\frac2\pi\int_0^1\frac{\sin(Ts)}{s\sqrt{1-s^2}}\,ds.
\]
Split the denominator as \(1/s+h(s)\), where \(h\ge0\) and \(\int_0^1h=\log2\). The sine integral \(\operatorname{Si}(T)\) lies between zero and \(\operatorname{Si}(\pi)<2\): successive sine lobes have decreasing absolute integrals, and
\[
\operatorname{Si}(\pi)
\le\pi-\pi^3/18+\pi^5/600<2.
\]
The displayed polynomial bound follows from the alternating sine expansion on [0,pi]. The inequalities \(157/50<\pi<22/7\), \(\log2<7/10\) now prove (3). Every rational comparison is checked by the companion script.

Let \(B(s)=b(s)+sb'(s)\). Integration by parts using \(J_1(rs)=-r^{-1}\partial_sJ_0(rs)\), followed by integration against the primitive in (3), yields
\[
\left|\int_0^\infty s b(s)J_1(rs)\,ds\right|
\le\frac2{r^2}\int_0^\infty|2b'(s)+sb''(s)|\,ds.
\tag{4}
\]
All boundary terms vanish: sb tends to zero at zero and infinity; the primitive of J0 vanishes at zero and is bounded, while B tends to zero at infinity.

The last variation integral is invariant under \(s=\nu t\). Direct differentiation of \(e^{-t^4}H(t)\) shows its integrand is
\[
e^{-t^4}\left|(-20t^3+16t^7)H+(2-8t^4)H'+tH''\right|.
\]
The unperturbed integral equals \(1+8e^{-5/4}<7/2\). For both values of a,
\[
0\le H-1\le2\delta t^2+\delta^2t^4,\quad
|H'|\le\tfrac{21}{10}\delta t(1+\delta t^2),\quad
|H''|\le\tfrac{21}{10}\delta(1+\delta t^2)+\delta^2t^2.
\]
The Gamma integrals above bound the total variation by
\[
\frac72+\frac{587}{40}\sqrt\pi\nu^2+\frac{761}{40}\nu^4
\le\frac72+\frac{587}{20}\nu^2+\frac{761}{40}\nu^4<4.
\tag{5}
\]
Equations (2), (4), (5) prove the middle bound of (1). This proof handles the actual Riesz singularity at zero frequency; it does not replace R by a pointwise residual or impose an artificial low-frequency gap.

## 2. Localized pricing without an inverse power of nu

Let a(x) be a real symmetric matrix or any measurable matrix, and define
\[
A_0=\|\|a(x)\|_{\mathrm{op}}\|_2,\qquad
A_1=\|W(x)\|a(x)\|_{\mathrm{op}}\|_2.
\]
Assume these are finite. For \(\Lambda\ge1/\nu\), split the kernel at the **relative** displacement \(|x-y|=\Lambda\). Then
\[
\boxed{\|aR\psi_\nu J^{\bar q}(Wg)\|_2
\le P_\Lambda\|g\|_2+\eta_\Lambda\|Wg\|_2,}
\tag{6}
\]
where
\[
\eta_\Lambda=\frac{4A_0}{\sqrt\pi\Lambda},\qquad
P_\Lambda^2\le\frac{\nu^2}{2\pi}A_1^2+
\left(\frac9{50\pi}+\frac{128}{\pi}\log(\Lambda\nu)\right)A_0^2.
\tag{7}
\]
For \(\bar q=q-1\), the same formula holds with \(J^{q-1}(Wg)=pJ^q(Wg)\).

**Proof.** The far-displacement kernel, as an operator on u=Wg, has Hilbert--Schmidt norm squared at most
\[
A_0^2\int_{|z|>\Lambda}|K(z)|^2\,dz
\le\frac{16A_0^2}{\pi\Lambda^2}.
\]
For the near-displacement kernel acting on g, its Hilbert--Schmidt norm squared is
\[
\int_x\int_{|z|\le\Lambda}|a(x)K(z)|^2W(x-z)^2\,dz\,dx.
\]
Use the exact identity \(W(x-z)^2=W(x)^2-8x\cdot z+4|z|^2\). The cross integral vanishes, since \(|a(x)K(z)|^2\) is even in z. The result is bounded by
\[
A_1^2\|K\|_2^2+4A_0^2\int_{|z|\le\Lambda}|z|^2|K(z)|^2\,dz.
\]
Using the first bound of (1) below \(1/\nu\) and the tail bound above it gives
\[
\int_{|z|\le\Lambda}|z|^2|K(z)|^2\,dz
\le\frac9{200\pi}+\frac{32}{\pi}\log(\Lambda\nu).
\]
Hilbert--Schmidt bounds imply operator bounds; the triangle inequality proves (6). ∎

The far term is bounded by \(\eta_\Lambda N(g)\), since \(\|Wg\|_2\le N(g)\). The large spatial cutoff appears only logarithmically in the weak price, while its high-norm contribution decays like \(\Lambda^{-1}\).

## 3. Actual near strain norms from a closed moment formula

Take \(S=\operatorname{Sym}Du_*\), \(a=S_n=\chi S\), where
\[
\chi(r)=\tfrac12\operatorname{erfc}(\log(r/\sqrt8)/\ell),\qquad
\ell=\log8/(2\sqrt\pi).
\]
Use the inherited certified bound \(\|S\|_{\infty,\mathrm{op}}\le137/125\). For every \(p>0\),
\[
\boxed{I_p:=\int_0^\infty r^{p-1}\chi(r)^2\,dr
=\frac{8^{p/2}}p e^{p^2\ell^2/4}
\operatorname{erfc}\left(\frac{p\ell}{2\sqrt2}\right).}
\tag{8}
\]
To prove it, let Z1,Z2 be independent with density \(e^{-z^2}/\sqrt\pi\), and \(R_i=\sqrt8 e^{\ell Z_i}\). Then \(\chi(r)^2=\Pr(\min(R_1,R_2)>r)\), so \(pI_p=\mathbb E\min(R_1,R_2)^p\). Integrate over \(Z_1\le Z_2\) and its reflection, complete the square in Z1, and use that the difference of the two Gaussian variables has variance one and shifted mean \(p\ell/2\). Its probability of being nonpositive is \(\tfrac12\operatorname{erfc}(p\ell/(2\sqrt2))\), proving (8). Tonelli applies to the nonnegative integrands.

Thus valid actual coefficient bounds are
\[
A_0\le\frac{137}{125}(2\pi I_2)^{1/2},\qquad
A_1\le\frac{137}{125}(2\pi(I_2+4I_4))^{1/2}.
\tag{9}
\]
The executed Arb certificate at 256 bits gives respectively approximately 4.87261878553 and 22.0059307073, in each case bounded by an outward ball. At \(\Lambda=10^6\), the full (7) satisfies rigorously
\[
\boxed{P_\Lambda<99,\qquad\eta_\Lambda<11/10^6.}
\tag{10}
\]
The displayed numbers bound the actual near strain coefficient via the accepted global strain certificate; they do not assume its spatial shape beyond that certificate.

## 4. The n multiplier

The n low factor is handled by \(n=1-|D|p\), without discarding its Riesz structure. The vector kernel KD of \(\nabla\psi_\nu J^{q-1}\) is odd and smooth, with
\[
\|K_D\|_2^2\le\frac{\nu^4}{2\pi},\qquad
\||z|K_D\|_2^2\le\frac{13\nu^2}{2\pi}.
\tag{11}
\]
For the first bound use the polar Plancherel integral and \((1+\delta t^2)^{(q-1)/2}\le1+\delta t^2\). For the second, differentiating the vector Fourier symbol \(i\xi b(|\xi|)\), with \(b=e^{-(s/\nu)^4}(1+s^2)^{(q-1)/2}\), gives
\[
\||z|K_D\|_2^2=\frac1{2\pi}\int_0^\infty s^3b'(s)^2\,ds.
\]
The other two derivative terms cancel by radial integration by parts. Bound \(|H'-4t^3H|^2\le2H'^2+32t^6H^2\), with \(H=(1+\delta t^2)^{11/20}\), \(H\le1+\delta t^2\), \(|H'|\le(11/10)\delta t\), and use the Gamma integrals. The resulting bracket is at most
\(12+32\delta+(6121/200)\delta^2<13\). This proves (11).

The full weighted Hilbert--Schmidt calculation, now with no cutoff needed, gives
\[
\|a\nabla\psi_\nu J^{q-1}(Wg)\|_2
\le P_D\|g\|_2,
\quad P_D^2\le\frac{\nu^4A_1^2}{2\pi}+\frac{26\nu^2A_0^2}{\pi}.
\tag{12}
\]
The actual coefficient bounds (9) give \(P_D<1\), certified by the companion script. Consequently for \(G=J^q(Wg)\),
\[
\begin{aligned}
\|S_n R\psi_\nu G\|_2&\le99\|g\|_2+\eta N(g),\\
\|S_n pR\psi_\nu G\|_2&\le99\|g\|_2+\eta N(g),\\
\|S_n nR\psi_\nu G\|_2&\le100\|g\|_2+\eta N(g),
\end{aligned}\qquad \eta=11/10^6.
\tag{13}
\]

## 5. An unambiguous low-band bound for the actual TIS form

Use the inherited exact expression
\[
T_{IS}(S;G)=q\left(\langle SnRG,nRG\rangle+
\langle SpRG,pRG\rangle-2\langle SRG,nRG\rangle\right).
\tag{14}
\]
There is no L2 norm notation hidden in (14): S is a symmetric matrix multiplication operator, while n and p are Fourier multipliers. Define the precise near low-band piece by
\[
\boxed{T_{IS}^{n,lo}(g)
=T_{IS}(S_n;G)-T_{IS}(S_n;(1-\psi_\nu)G).}
\tag{15}
\]
This uses the quartic cut, not a sharp projection. Let B(F,H) be the polarized symmetric bilinear form of (14), so
\[
B(F,H)=q[\langle S_n nRF,nRH\rangle+\langle S_n pRF,pRH\rangle
-\langle S_n RF,nRH\rangle-\langle S_n nRF,RH\rangle].
\]
Put \(G_l=\psi_\nu G\), \(G_h=(1-\psi_\nu)G\). Then (15) is exactly \(B(G_l,G)+B(G_h,G_l)\). Since R is an L2 isometry and \(p,n,1-\psi_\nu\) are contractions, each bilinear form is bounded, using (13), by
\[
q[398\|g\|_2N(g)+4\eta N(g)^2].
\]
For the second form use its symmetry to place every localized low factor on the side covered by (13). Therefore
\[
\boxed{|T_{IS}^{n,lo}(g)|
\le\frac{8358}{5}\|g\|_2N(g)+\frac{231}{1250000}N(g)^2.}
\tag{16}
\]
Finally Young's inequality with \(\varepsilon_Y=1/4000\) gives the explicit full-plane quadratic-form certificate
\[
\boxed{|T_{IS}^{n,lo}(g)|
\le\frac{1087}{2500000}N(g)^2
+2794246560\|g\|_2^2.}
\tag{17}
\]
Here the high coefficient is 0.0004348; the weak coefficient is exactly 2,794,246,560. Both are strictly inside the original plan-of-record H4-REST aggregate budgets **for this single piece**. The other pieces must fit what remains; they are not set to zero. The algebra in (16)--(17) is checked exactly by the companion script. An alternative Young parameter trades rate against price in the explicit formula
\[
\varepsilon=8q\eta+\varepsilon_Y,\qquad
C=(796q)^2/(4\varepsilon_Y).
\]

## Reproduction and scope

```bash
python -B Changhe/IPM/combined3/IPM.artifacts/operator_theory/verify_lowband_pricing.py \
  --output Changhe/IPM/combined3/IPM.artifacts/operator_theory/lowband_pricing_result.json
```

The code uses rational arithmetic for the analytic majorants and python-flint Arb at 256 bits for pi, logarithms, exponentials, erfc, and square roots. All passing comparisons are interval comparisons with rational thresholds. The only profile-dependent input is the inherited actual global strain bound 137/125. Re-certifying that inherited bound is a separate task.
