# Audit of the PDE exclusion theorem

**Verdict: CONFIRMED as a conditional local exclusion**, using §6.3.1(h) and its stated axis-equation inputs as supplied theorems. This audit does not independently prove the microlocal propagation result or the nonlinear source theorem.

The original theorem explicitly assumes trace-space membership, so it does not assert an unjustified regularity upgrade. A shorter statement must retain that assumption. For the report's \(N_\phi\), use the repaired constants in the preceding proofs.

## Precise statement

Fix a compatible reference \(w_0\) at \(A_0>2\), \(e_0>0\), analytic and odd near zero, negative on \((0,1)\), and \(C^3\) through 1. Choose \(r,\sigma,\theta,h,h',\tau\) and certified reference inputs as in the remainder proof, including
\[
e_0-h'>0,\quad A_0-h-\tau>2,\quad
0<\sigma\le2,\quad 0<\theta\le1,\quad
\sigma>\frac2{A_0-h-\tau},\quad
\theta+\frac2{A_0+h+\tau}>1.
\]
Choose either \(N_{\rm mon}\) with its original constants or \(N_\phi\) with its repaired constants. Assume \(0<b_0\le|B(A_0,e_0,w_0)|\), \(m>0\), and let \(\epsilon\) be (32) or any smaller positive number.

There is no profile satisfying all the following hypotheses:

1. It is a Setting I \(P_\infty\) profile: \(\rho\) is real, even in \(x\), odd in \(y\), locally \(C^{2,\alpha_{\rm loc}}\) as in the question, and near zero \(\rho=x^2ya(x,y)\) with \(a\) smooth and \(a(0)=1\). It satisfies the canonical sublinear velocity law and the growth assumptions under which that law and the supplied axis identities hold, and
   \[
   W\cdot\nabla\rho=\rho,\quad W=c_lX+(-\psi_y,\psi_x),\quad
   -\Delta\psi=\partial_x\rho.
   \]
2. \(A=2c_l-1\) obeys \(|A-A_0|\le h\), and the first positive source is \(P=(L,0)\), with \(e=L^{-2}\) satisfying \(|e-e_0|\le h'\).
3. Either \(\rho\) is \(C^{2,\alpha}\) near \(P\) for some \(\alpha>1-2/A\), \(0<\alpha<1\), or \(\rho,W\) are \(C^2\) near \(P\) and for some \(C,\kappa,r_0>0\), with such an \(\alpha\),
   \[
   |\rho_{yy}(x,y)|\le C|y|^\alpha,\qquad
   |(W_1)_{yy}(x,y)-(W_1)_{yy}(P)|\le C|(x-L,y)|^\alpha
   \]
   on \(L-r_0<x<L,\ |y|<\kappa(L-x)\).
4. The normalized trace \(\widetilde w(u)=W_1(Lu,0)/L\) belongs to the compatible affine trace space:
   \[
   \widetilde w(0)=\widetilde w(1)=0,\quad
   \widetilde w'(0)=-A,\quad \widetilde w'(1)=A,\quad
   \widetilde w<0\ \text{on }(0,1).
   \]
   It is smooth and odd near 0, smooth on the open segment when the classical axis identity is used, \(C^2\) through 1, and its direction \(v=\widetilde w-(A/A_0)w_0\) has the weighted remainder and anchored endpoint controls defining the chosen norm, with \(\|v\|\le\epsilon\).
5. The classical third axis equation and the endpoint implication used in §6.3.1(h) apply. This is included in the supplied implication from \(P_\infty\), its axis-propagation input, and item 3. If that implication is not accepted as supplied, impose the classical third axis equation on \((0,L)\) and the applicable endpoint theorem explicitly. Smoothness of \(\rho\) near every point of the open axis segment suffices for the classical differentiation step.

## Why trace membership is legitimate, and what is additional

Smoothness and oddness of the axis velocity at zero follow from the local smoothness of \(\rho\), its parity, and the local order-zero velocity mapping with a smooth far part used in the supplied report. Thus its Taylor expansion has the prescribed odd coefficients and an \(O(u^9)\) remainder with the corresponding two derivative bounds. Scaling by \(L\) and subtracting \((A/A_0)w_0\) cancels the linear coefficient. Either remainder convention then has the required origin bounds for \(\sigma\le2\).

The order-\(y\) part of the transport equation and \(\operatorname{div}W=A+1\) give
\[
w_{\rm phys}g_{\rm phys}'=(w_{\rm phys}'-A)g_{\rm phys},
\quad g_{\rm phys}(x)=\rho_y(x,0),\quad g_{\rm phys}(x)/x^2\to1.
\]
Therefore the positive reconstructed \(g\) equals the normalized physical axis derivative. This checks that the functional is evaluated on the correct \(g\), not on an independently chosen positive function.

The source Hölder hypothesis with exponent \(\alpha\) supplies \(C^{2,\alpha}\) velocity regularity through the supplied mapping property. It does **not** imply the norm's endpoint exponent \(\theta\) if \(\theta>\alpha\). For example, the threshold at the computed reference is about \(0.803\), whereas the certified norm uses \(\theta=0.9\). A profile with only a stated source exponent \(0.85\) is not thereby in that trace space. The cone hypothesis likewise does not state an anchored \(0.9\)-bound for \(w''\). Item 4 is consequently essential and explicit. No implication from the cone hypothesis to that additional axis regularity is being used.

Equivalently, one can extend the norm to have value \(+\infty\) outside its weighted affine domain and interpret the ball condition in that sense. But the regularity domain must be stated at least once; simply suppressing it would obscure the theorem's scope.

## Proof of exclusion

The supplied PDE input is
\[
\text{items 1--5}\ \Longrightarrow\ B_3(c_l,w_{\rm phys})=0.
\]
More explicitly, smoothness at zero sets the homogeneous coefficient \(C_0=0\); the endpoint theorem sets \(\ell_3=0\); and the integrated third axis equation gives \(C_0=\ell_3+B_3\).

The weaker trace norm does not obstruct that integrated identity. Its finite-part origin remainder is \(O(u^{\sigma-\beta-1})\), and its source integrand is \(O((1-u)^{\theta+\beta-2})\). Both are integrable. A full two-point Hölder seminorm was not used in either endpoint passage. The other needed input is the classical equation on the open segment, retained above.

Normalization gives
\[
B(A,e,\widetilde w)=L^{4+\beta}B_3(c_l,w_{\rm phys})=0.
\]
The differential and remainder bound, followed by (32), give
\[
|B(A,e,\widetilde w)-B(A_0,e_0,w_0)|
<\tfrac12|B(A_0,e_0,w_0)|.
\]
The reference value is nonzero, a contradiction. This proves the stated conditional exclusion.

## Numerical instances and scope

The polynomial-reference inventory in the original fourth proof is also consistent with the analytic estimates. In its notation
\[
H(t)=A_0-t(1-t^2)q(t),\qquad
w_0=-u(1-u^2)H(u^2)/(1+u^2).
\]
If \(H>0\), compatibility and negativity follow, and
\(-w_0/[u(1-u)]=(1+u)H(u^2)/(1+u^2)\ge H_{\min}\).
With \(z_0=(1-t)H(t)/(A_0(1+t))\), direct subtraction gives
\[
\frac1{2t}(z_0^{-1}-1)-\frac1{1-t}
=\frac{(1+t)^2q(t)}{2H(t)}.
\]
Thus the reconstructed logarithm is
\[
E_0=-\log(1-t)+T(t),\quad
T(t)=\frac12\int_0^t\frac{(1+s)^2q(s)}{H(s)}\,ds,
\]
and \(g_0=u^2H(u^2)e^{T(u^2)}/[A_0(1+u^2)]\), as claimed. Expansion at 1 gives \(g_0(1)=e^{T(1)}/2\) and \(w_0''(1)=A_0+8q(1)\). The finite jet identifies removable origin limits but does not bound the remaining suprema; those must still be certified. The original inventory correctly separates these reference bounds, the parameter derivatives, and the nonzero obstruction. Agreement of two decimal computations is not substituted for a certified error bound.

For \(w_0=-A_0u(1-u^2)/(1+u^2)\), \(r=1/2,\sigma=1,\theta=0.9\), the theorem holds with

* \(A_0=10.150725,e_0=0.0135206,h=0.06,h'=0.0003,\epsilon=10^{-6}\);
* \(A_0=4,e_0=1/16,h=0.06,h'=0.0003,\epsilon=10^{-8}\);
* \(A_0=4,e_0=1/16,h=h'=0,\epsilon=10^{-7}\).

These simple radii hold in both norm conventions, with different certified constants. They are not the radii of the earlier physical-coordinate \(X\)-ball.

The theorem says exactly that no profile satisfies all the listed hypotheses and the ball condition. It does not say that every \(P_\infty\) profile satisfies the source regularity hypothesis or the ball condition. The reference need not itself come from a profile. No estimate here places the computed trace, a fitted reference, or an exact profile near the computed branch inside these balls. The fitted degree-12 reference needs its own certified obstruction and reference norms.
