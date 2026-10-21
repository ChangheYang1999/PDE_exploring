# Normalization and the full differential

**Status: CONFIRMED**, with the integrability hypotheses specified below. In particular, merely saying that the tail is \(C^{2,\theta}\), without requiring \(\theta+\beta>1\), is insufficient.

This result uses the finite-part identity in `FINAL_REPORT.md`, §6.3.1(i). The implication from this functional to an obstruction for a PDE profile uses §6.3.1(h), separately; no existence of a PDE profile is used here.

## 1. Definition and normalization

Throughout this file \(A>2\), \(\beta=2/A\), and \(e>0\). A compatible normalized trace satisfies
\[
w(0)=w(1)=0,\quad w'(0)=-A,\quad w'(1)=A,\quad w(u)<0\quad(0<u<1).
\]
It is odd and smooth near zero, smooth on the open interval, and \(C^2\) through 1. For the formulas below it suffices to have
\[
w=-Au+d_3u^3+d_5u^5+d_7u^7+R,\qquad
|R^{(i)}(u)|\le C u^{7+\sigma-i}\quad(i=0,1,2),
\]
where \(\sigma>\beta\), together with
\[
|w''(u)-w''(1)|\le C(1-u)^\theta,\qquad \theta+\beta>1.
\]
The latter is an endpoint condition, not a Hölder seminorm over all pairs of points.

Reconstruct the positive function \(g\) by
\[
\frac{g'}g=k:=\frac{w'-A}{w},\qquad \frac{g(u)}{u^2}\longrightarrow1.
\]
Set
\[
Q=\frac{g'-ew''}{2g^3},\quad m=-w/g,\quad
K=m^{\beta-2}/g,\quad \kappa=\frac{(\beta-1)A^{1-\beta}}3.
\]
The normalized obstruction is
\[
\mathcal B(A,e,w)=\kappa\,\operatorname{FP}\int_0^1 (Q-Q(1))K\,du.       \tag{1}
\]
The integral is ordinary at 1. At 0, FP removes the three divergent even-power terms of the factor multiplying \(u^{-5-\beta}\). There is no logarithmic resonance since \(0<\beta<1\).

For a physical source \(L\), put \(\widetilde w(u)=w_{\rm phys}(Lu)/L\), \(\widetilde g(u)=g_{\rm phys}(Lu)/L^2\), and \(e=L^{-2}\). Differentiating gives
\[
w_{\rm phys}'(Lu)=\widetilde w'(u),\quad
w_{\rm phys}''(Lu)=L^{-1}\widetilde w''(u),\quad
g_{\rm phys}'(Lu)=L\widetilde g'(u).
\]
Thus compatibility and \(g/u^2\to1\) are preserved,
\[
Q_{\rm phys}(Lu)=L^{-5}\frac{\widetilde g'-e\widetilde w''}{2\widetilde g^3},
\qquad m_{\rm phys}(Lu)=L^{-1}\widetilde m(u).
\]
Substitution in (1), including \(dx=L\,du\), proves
\[
\boxed{\mathcal B(A,L^{-2},\widetilde w)=L^{4+\beta}B_3(A,w_{\rm phys}).} \tag{2}
\]
In particular, varying \(L\) at a fixed normalized shape changes this functional.

## 2. An adjoint formula, including variations of the origin jet

All objects in the next formulas are evaluated at the reference \(w_0\); subscripts 0 are suppressed. Let \(v\) be a compatible direction, so \(v'(0)=v(1)=v'(1)=0\). Put
\[
a_v=\frac{v'}w-\frac{(w'-A)v}{w^2},\qquad
\eta_v(u)=\int_0^u a_v(t)\,dt.                                  \tag{3}
\]
Differentiating the reconstruction equation and its origin normalization proves \(\delta\log g=\eta_v\). Define
\[
d=\frac{k}{2g^2}-3Q,\quad
D=d+(1-\beta)(Q-Q(1)),\quad
b_*=\frac1{2Ag(1)^2}-\frac e{2g(1)^3},
\]
\[
\boxed{\mathscr J(t)=
\int_t^1 K(u)\,[D(u)-d(1)]\,du-d(1)\int_0^t K(u)\,du.}          \tag{4}
\]
Both integrals in (4) are ordinary for \(0<t<1\). This is the adjoint weight for the nonlocal reconstruction. Set
\[
\mathscr L(v)=
\frac{a_v}{2g^2}-\frac{ev''}{2g^3}
-b_*v''(1)+(\beta-2)(Q-Q(1))\frac vw.                           \tag{5}
\]
The exact differential is
\[
\boxed{D_w\mathcal B(v)=\kappa\left\{
\operatorname{FP}\int_0^1K\mathscr L(v)\,du+
\operatorname{FP}\int_0^1\mathscr J\,a_v\,du\right\}.}           \tag{6}
\]
In the first integral the three terms involving \(a_v,v''\), and \(v''(1)\) must remain grouped at 1. Separate integrals of these terms generally diverge there.

Here is an explicit jet-plus-remainder version. For \(j=3,5,7\), define
\[
\phi_j(u)=u^j+\frac{j-11}{2}u^9+\frac{9-j}{2}u^{11}.
\]
These are odd polynomial compatible directions, with the indicated unit \(j\)-jet and zero other jets of orders 3, 5, 7. Write
\[
v=c_3u^3+c_5u^5+c_7u^7+R_v\quad\hbox{near zero},\qquad
R=v-\sum_{j=3,5,7}c_j\phi_j.
\]
Then \(R=O(u^{7+\sigma})\) with the two corresponding derivative bounds (take \(\sigma\le2\)), and
\[
\boxed{D_w\mathcal B(v)=
\sum_{j=3,5,7}c_j\beta_j+
\kappa\int_0^1\left[K\mathscr L(R)+\mathscr J a_R\right]du,}     \tag{7}
\]
where the three explicit constants are
\[
\beta_j=\kappa\,\operatorname{FP}\int_0^1
[K\mathscr L(\phi_j)+\mathscr J a_{\phi_j}]\,du.                 \tag{8}
\]
Thus the only remaining integrals in (7) are ordinary convergent integrals. Formula (8) is a finite-part integral of explicit reference functions, not an unknown coefficient determined by a PDE solve.

### Proof of (6)

Direct differentiation gives
\[
\delta Q=\frac{a_v}{2g^2}-\frac{ev''}{2g^3}+d\eta_v,\qquad
\delta K=K[(\beta-2)v/w+(1-\beta)\eta_v].
\]
Since \(k(1)=w''(1)/A\), one has
\[
a_v(1)=v''(1)/A,\qquad \delta Q(1)=b_*v''(1)+d(1)\eta_v(1).
\]
Consequently the variation of the integrand of (1) is
\[
K\{\mathscr L(v)+D\eta_v-d(1)\eta_v(1)\}.
\]
Rewrite the last two terms as
\[
[D-d(1)]\eta_v-d(1)\int_u^1a_v(t)\,dt
\]
and interchange integrations. At 1, \(D-d(1)=O((1-u)^\theta)\); this justifies the interchange there. At 0, use a lower cutoff \(\epsilon>0\). The difference between the cutoff interchange and (4) is a sum of
\[
\eta_v(\epsilon)\int_\epsilon^1K[D-d(1)],\qquad
d(1)\left(\int_0^\epsilon K\right)
[\eta_v(1)-\eta_v(\epsilon)].
\]
The second tends to zero. The first has zero finite part: its potentially divergent powers are even integers minus \(4+\beta\), and hence never zero. Its other terms tend to zero. This proves (6).

For the remainder in (7), the most singular local term is \(K R''/g^3=O(u^{\sigma-\beta-1})\), which is integrable. Also \(\mathscr J=O(u^{-4-\beta})+O(1)\), \(a_R=O(u^{5+\sigma})\). At 1 the grouped local term is \(O((1-u)^\theta)\), and the adjoint term is integrable. These estimates also justify differentiation by domination; the uniform second-order argument is given in the next proof.

## 3. Parameter derivatives in the requested coordinates

Write \(w=Af\) and \(n=-f/g\). The reconstruction \(g\) depends only on \(f\). Define
\[
c(A)=\frac{\beta-1}{3A},\quad
J=\operatorname{FP}\int_0^1(Q-Q(1))\,n^{\beta-2}g^{-1}\,du,
\]
\[
J_\beta=\operatorname{FP}\int_0^1(Q-Q(1))\,n^{\beta-2}g^{-1}\log n\,du,
\]
\[
J_A=-\frac e2\operatorname{FP}\int_0^1
[f''g^{-3}-f''(1)g(1)^{-3}]\,n^{\beta-2}g^{-1}\,du.
\]
Exponent differentiation includes differentiation of the subtraction terms defining FP. Equivalently, these definitions use the explicit origin subtraction in the next proof, which has no ambiguity about logarithmic finite parts. Then
\[
\boxed{\partial_A\mathcal B\big|_f
=\frac{A-4}{3A^3}J+
\frac{\beta-1}{3A}\left[J_A-\frac2{A^2}J_\beta\right],}         \tag{9}
\]
\[
\boxed{\partial_e\mathcal B\big|_{A,f}
=-\frac{\beta-1}{6}\operatorname{FP}\int_0^1
[f''g^{-3}-f''(1)g(1)^{-3}]\,n^{\beta-2}g^{-1}\,du.}           \tag{10}
\]
These follow by the product rule; \(c'(A)=(A-4)/(3A^3)\) and \(\beta'=-2/A^2\). The dependence on \(e\) is exactly affine.

For the displacement used in the question, put
\[
\Delta A=A-A_0,\quad \Delta e=e-e_0,\quad
v=w-(A/A_0)w_0.
\]
The full first differential is
\[
\boxed{B_A\Delta A+B_e\Delta e+D_w\mathcal B(v),}               \tag{11}
\]
where \(B_A\) means (9) at \(f=w_0/A_0\), and all three derivatives are evaluated at the reference. No extra dilation derivative is missing.

## 4. Numerical parameters that should not be identified

The exact decimal \(L=8.6000638\) gives
\[
L^{-2}=0.013520621456947\ldots,
\]
not exactly \(0.0135206\). The report assigns \(0.325791726307172\) to \(L=8.6\). Its value at \(8.6000638\), and its value at the exact decimal \(e=0.0135206\), are different. The evaluation code records all three.
