# Global weak prices for the Gaussian Ew high/cross comparison

Status: proved estimates in terms of specified background constants. The scalar calculator's default field constants are assumptions awaiting actual certificates. The low form \(E[P_\mu G]\) remains outside this result.

Let \(W=W_a=(1+a^2r^2)^{1/2}\), \(0<a\le2\), \(c=W^{-1}\), \(b=\nabla\rho_*\), \(P_\mu=e^{\Delta/(2\mu^2)}\), \(H=I-P_\mu\), and \(G=WJ^qg\), \(q=21/10\). Define
\[
 E=\operatorname{Sym}(b\cdot WUc-b\cdot U),\qquad
 E_{UH}=\operatorname{Sym}(b\cdot WUHc-b\cdot UH).
\]
Assume the actual finite constants
\[
 B_0=\sup|b|,\quad B_1=\sup W|Db|_F,\quad
 D_j=\||D|^j b\|_2,\quad X_j=\||D|^j(xb)\|_2
\]
at the orders used below. Then explicit finite constants \(K_W,K_B,K_T\), defined next, give
\[
 \boxed{|E[G]-E[P_\mu G]|
 \le\frac{a(1+\sqrt2)(B_1+aB_0)}{\mu^2}\|G\|_2^2
 +K_{\rm weak}\|g\|_2\|G\|_2,}
\]
\[
 K_{\rm weak}=\sqrt3B_0K_W+(\sqrt3+1)K_B+\sqrt3K_T.
\]
The constants require no spatial coefficient cutoff and no higher-derivative supremum cover.

## Exact comparison and the UH part

Direct multiplication gives
\[
 EH=E_{UH}+\tfrac12bWU[c,H]
 +\tfrac12(cU^*W-U^*)[b,H]+\tfrac12cU^*[W,H]b.
\]
The symmetric kernel of \(E_{UH}\) is
\[
 \tfrac12 k_{UH}(x-y)\cdot
 \frac{(W_x-W_y)(W_xb_x-W_yb_y)}{W_xW_y}.
\]
Consequently its operator norm is at most
\((a/2)L_d M_2(UH)\), where \(L_d\le B_1+aB_0\).
The exact off-diagonal kernel, with \(t=1/(2\mu^2)\) and \(v=r^2/(4t)\), is
\[
 k_{UH}=\frac{e^{-v}}{\pi r^2}
 \left(-(1+v)\cos\theta\sin\theta,
 -\tfrac12+(1+v)\cos^2\theta\right).
\]
Its squared angular factor is \(1/4+v(1+v)\cos^2\theta\). Angular Jensen and
\(\sqrt{1/4+v/2+v^2/2}\le1/2+v/\sqrt2\) prove
\[
 M_2(UH)=\int r^2|k_{UH}|\le(1+\sqrt2)/\mu^2.
\]
Any delta part of \(U_2H\) disappears from this kernel because the weight difference vanishes on the diagonal.

Using \([c,H]G=-c[P_\mu,W]J^qg\), the first comparison term has norm at most
\(\sqrt3B_0K_W\|g\|_2/2\). Here the weighted S1 velocity bound gives
\(\|bWU c\|\le\sqrt3B_0\); no growing \(\sup Wb\) is introduced.
The middle term is bounded by \((\sqrt3+1)K_B\|g\|_2/2\), where
\[
 K_B\ge\|[b,P_\mu]WJ^q\|.
\]
The last term is bounded by \(\sqrt3K_T\|g\|_2/2\), where
\[
 K_T\ge\|c[W,P_\mu]bWJ^q\|.
\]
The adjoint weighted-velocity estimates are valid on the output parity pair of S1; all displayed Gaussian and radial weight operators preserve those parities.
Finally \(E-PEP=HE+PEH\), self-adjointness and \(\|P\|\le1\) yield the box.

## Explicit Gaussian bounds

All kernel differentiation below is in the input variable, so it estimates an operator followed by \(J^q\) by adjoint Sobolev interpolation. Let \(p(x)=\mu^2(2\pi)^{-1}e^{-\mu^2r^2/2}\). The full tensor derivative majorants are
\[
 |D^jp|\le G_j(r)p,\quad
 G_0=1,\ G_1=\mu^2r,\ G_2=\mu^4r^2+\sqrt2\mu^2,\ 
 G_3=\mu^6r^3+2\sqrt3\mu^4r.
\]
For positive-coefficient polynomials \(F\), the calculator evaluates exactly
\[
 L_1(F)=\int F(r)p\,dx,\qquad L_2(F)=\left(\int F(r)^2p^2\,dx\right)^{1/2},
\]
using
\[
 \int r^kp\,dx=(\sqrt2/\mu)^k\Gamma(1+k/2),\quad
 \int r^kp^2\,dx=\frac{\mu^{2-k}}{4\pi}\Gamma(1+k/2).
\]
For a kernel with derivative operator bounds \(S_j\), \(0\le j\le3\), set
\[
 A_2=S_0+\sqrt2S_2,\quad
 A_3=\sqrt{A_2^2+(S_1+\sqrt2S_3)^2},\quad
 K=A_2^{3-q}A_3^{q-2}.
\]
Indeed the Laplacian contracts a rank2 tensor with norm \(\sqrt2\); the same factor handles gradient-Laplacian at order3. Spectral Holder interpolation for \(J^q\) applied to the adjoint proves the final formula.

The weight bounds used are
\[
 d_1=a,\ d_2=\sqrt2a^2,\ d_3=2a^3,\qquad
 w_0=1,\ w_1=a/2,\ w_2=d_2,\ w_3=d_3,
\]
where \(|D^jW|_F\le d_j\) and \(|D^jW|_F/W\le w_j\). The third derivative estimate follows from the explicit tensor expression: its two terms have maxima at most \((4/3)a^3\) and \((18\sqrt{15}/125)a^3\), whose sum is less than \(2a^3\).

For \(K_W=\|[W,P_\mu]J^q\|\), a slightly sharper direct second-derivative computation is used. Put \(e_r=\sqrt{\pi/2}/\mu\), \(g_1=\mu\sqrt{\pi/2}\). Valid bounds are
\[
 A_{2,W}=ae_r+\tfrac52a\sqrt{2\pi}\mu+2a^2+2ag_1,
\]
\[
 A_{\nabla2,W}=3a+2\sqrt2a^3+4a^2g_1+
 a(20+2\sqrt2+4/e)\mu^2,
\]
\[
 K_W=A_{2,W}^{3-q}(A_{2,W}^2+A_{\nabla2,W}^2)^{(q-2)/2}.
\]
These follow from differentiating \((W_x-W_y)p(x-y)\), using
\(\|\Delta p\|_1=4\mu^2/e\),
\(\int r|\Delta p|\le(5/2)\sqrt{2\pi}\mu\),
\(\int r|\nabla\Delta p|\le16\mu^2\),
\(\|\nabla p\|_1=g_1\), and
\(\|D^2p\|_{F,L^1}\le(2+\sqrt2)\mu^2\).

For the middle operator, the input coefficient is \((b_x-b_y)W_y\). Along the segment joining the endpoints,
\[
 W_y|b_x-b_y|\le B_1r(1+ar).
\]
At derivative order \(l\), its majorant is
\[
 B_1\{w_lr(1+ar)+l w_{l-1}\}
 +\sum_{k=2}^l {l\choose k}w_{l-k}|WD^kb(y)|.
\]
The term \(lw_{l-1}\) is omitted for \(l=0\). Product differentiation with the Gaussian gives \(S_j\): integrate its \(B_1\) part by \(L_1\), and its higher-coefficient parts by the Hilbert–Schmidt bounds \(L_2\|WD^kb\|_2\).
The latter inputs require no new norm certificate:
\[
 \|WD^2b\|_2^2\le D_2^2+a^2X_2^2,\qquad
 \|WD^3b\|_2^2\le D_3^2+a^2X_2X_4.
\]
The identity underlying these bounds is
\(\|xD^jb\|_2^2=X_j^2-j(j-1)D_{j-1}^2\), proved by Fourier differentiation and integration by parts. Then \(X_3^2\le X_2X_4\) by homogeneous L2 interpolation. The exact far decay justifies those integrations and the homogeneous seminorm formulation.

For the third operator the input kernel coefficient is
\(c_x(W_x-W_y)W_yb_y\). Its derivative-order \(l\), coefficient-derivative-order \(k\) polynomial majorant is
\[
 P_{l,k}(r)=(1+ar)\left[
 ar{l\choose k}w_{l-k}
 \sum_{z=1}^{l-k}{l\choose z}d_z{l-z\choose k}w_{l-z-k}\right].
\]
Here \(|D^0b|\le B_0\), \(|Db|\le B_1\), and the \(k=2,3\) terms use the actual unweighted L2 norms \(D_2,D_3\) through Gaussian Hilbert–Schmidt bounds. For each \(j\), sum \({j\choose l}P_{l,k}G_{j-l}\) over \(l,k\), then use \(L_1\) for \(k=0,1\), \(L_2\) for \(k=2,3\). This gives the \(S_j\) and hence \(K_T\).

The executable Q_Ew_Gaussian_weak_price.py records these polynomial operations and Arb scalar prices. Its default background bounds are explicitly marked assumptions. The operator comparison remains useful as a fallback, while the local integer principal formulation may avoid pricing Ew separately.
