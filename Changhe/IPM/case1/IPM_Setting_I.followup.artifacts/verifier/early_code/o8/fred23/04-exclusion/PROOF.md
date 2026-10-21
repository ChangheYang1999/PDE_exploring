# The resulting conditional exclusion theorem

**Question (4): CONFIRMED with the hypotheses stated below.** This is a local exclusion in parameter and trace space. It does not exclude the full class \(\mathcal P_\infty\), and no membership of a putative exact profile in the certified ball has been established.

## Exact statement

Let \(A_0=10.150725\), \(L_0=8.6000638\), \(e_0=L_0^{-2}\), and let \(w_0\) be the exact fitted reference defined in the first proof and its JSON. There is **no** pair \((\rho,c_l)\) satisfying all the following conditions.

1. It is a real exact Setting I profile on \(\mathbb R^2\):
   \[
   W\cdot\nabla\rho=\rho,\quad W=c_lX+U,\quad
   U=(-\psi_y,\psi_x),\quad-\Delta\psi=\partial_x\rho,
   \]
   with the canonical sublinear velocity law and the stated even-\(x\), odd-\(y\) symmetries. It lies in \(\mathcal P_\infty\): \(\rho\in C^{2,\alpha_{\rm base}}_{\rm loc}\) for some \(0<\alpha_{\rm base}<1\), and \(\rho=x^2ya(x,y)\) near zero with \(a\) smooth and \(a(0)=1\). The local regularity of \(W\) required in condition 3 is part of that condition; it is not left as an implicit appeal to a far-field mapping estimate.
2. Put \(A=2c_l-1>2\). There is a first positive source \(P=(L,0)\), \(L>0\), such that \(w_{\rm phys}(x)=W_1(x,0)\) obeys
   \[
   w_{\rm phys}<0\ (0<x<L),\quad w_{\rm phys}'(0)=-A,\quad
   w_{\rm phys}(L)=0,\quad w_{\rm phys}'(L)=A.
   \]
   The profile and velocity are smooth near each point of the open axis segment \(0<x<L\). It would suffice to impose the finite regularity needed for the classical third axis equation; smoothness is a convenient explicit hypothesis.
3. The following sufficient source condition holds, for an exponent \(0<\alpha_P<1\) with \(\alpha_P>1-2/A\): either \(\rho,W\) are \(C^{2,\alpha_P}\) near \(P\); or they are \(C^2\) there and there exist \(C,\kappa,r_0>0\) such that
   \[
   |\rho_{yy}(x,y)|\le C|y|^{\alpha_P},\qquad
   |(W_1)_{yy}(x,y)-(W_1)_{yy}(P)|
   \le C|(x-L,y)|^{\alpha_P}
   \]
   whenever \(L-r_0<x<L\) and \(|y|<\kappa(L-x)\).
4. Normalize \(\widetilde w(u)=w_{\rm phys}(Lu)/L\), \(e=L^{-2}\), and \(v=\widetilde w-(A/A_0)w_0\). This is a compatible trace difference, smooth near zero and on the open interval. Its second derivative extends continuously to 1 and the norm below is finite. At \(r=1/2,\sigma=1,\theta=9/10\), either
   \[
   |A-A_0|\le0.06,\quad |e-e_0|\le0.0003,\quad
   N_{\rm raw}(v)\le4.5\,10^{-6},
   \tag{1}
   \]
   or
   \[
   A=A_0,\quad e=e_0,\quad N_{\rm raw}(v)\le5\,10^{-6}.
   \tag{2}
   \]
   Here \(N_{\rm raw}\) is, explicitly,
   \[
   \sum_{j=3,5,7}|c_j|
   +\sup_{0<u\le1/2}u^{-6}|(v-c_3u^3-c_5u^5-c_7u^7)''|
   +\sup_{[1/2,1]}|v''|
   +\sup_{1/2\le u<1}\frac{|v''(u)-v''(1)|}{(1-u)^{9/10}},
   \]
   with \(c_j\) the Taylor coefficients. Alternatively use the compatible remainder \(v-\sum c_j\phi_j\) and replace the two radii by, respectively,
   \[
   \frac4{415}(4.5\,10^{-6}),\qquad
   \frac4{415}(5\,10^{-6}).
   \tag{3}
   \]

The \(h'\) bound is on \(e=L^{-2}\), not on \(L\) itself. The source \(L\) and the axis are normalized before the norm comparison; source alignment cannot be omitted. The inequalities \(\sigma>\beta\), \(\theta+\beta>1\), \(\beta=2/A\), hold throughout (1), including the buffer used in the radius proof.

## Proof and analytic dependencies

The only source regularity result used here is the endpoint theorem supplied in FINAL_REPORT §6.3.1(h). In the explicit form needed, an exact profile satisfying conditions 2 and 3 obeys

$$
|\partial_y^3\rho(L-s,0)|\le C s^{\alpha_P-1},\qquad
l_3:=\lim_{x\uparrow L}G_3(x)/H_3(x)=0,
\tag{4}
$$

where \(G_3=\partial_y^3\rho(x,0)/6\) and \(H_3\) is defined below. Its nonlinear endpoint estimate is a supplied analytic dependency, not something established by the numerical certificate. This proof does not replace that theorem by a frozen-model argument.

We give the remaining axis argument to fix signs and to avoid requiring a full two-point Hölder norm where only the anchored modulus was certified. Write \(g=\rho_y(x,0)\), \(w=w_{\rm phys}\), \(h=(W_2)_y(x,0)\), \(a_2=(W_1)_{yy}(x,0)/2\), and \(b_3=(W_2)_{yyy}(x,0)/6\). Smoothness on the open axis justifies the Taylor coefficients of the PDE, divergence, and curl equations:

$$
h=A+1-w',\quad wg'=(w'-A)g,\quad
a_2=(g'-w'')/2,\quad b_3=-a_2'/3,
$$

$$
wG_3'+(3h-1)G_3=F_3,\qquad
F_3=-a_2g'+a_2'g/3.
\tag{5}
$$

The curl sign is \(\partial_xW_2-\partial_yW_1=-\rho_x\), as follows directly from the stated stream function convention. Near zero \(g/x^2\to1\); the first-order equation in (5) and \(w<0\) therefore give \(g>0\) on the open interval. The trace regularity and \(w'(L)=A\) give a finite positive value of \(g\) at \(L\) by the reconstruction proof.

For \(\beta=2/A\), put

$$
H_3=A^\beta g^{3+\beta}(-w)^{-\beta}.
$$

Differentiation of its logarithm, using (5), gives
\(wH_3'+(3h-1)H_3=0\). Hence
\[
(G_3/H_3)'=F_3/(wH_3).
\tag{6}
\]
It also gives \(H_3/x^{6+\beta}\to1\) at zero and
\(H_3\asymp(L-x)^{-\beta}\) at the source. Thus (4) indeed implies \(l_3=0\).

Set \(Q=a_2/g^3\), \(m=-w/g\). From (5),
\(F_3=g^4Q'/3\), \(m'=-A/g\), and
\(wH_3=-A^\beta g^4m^{1-\beta}\). Therefore

$$
B_3:=-\operatorname{FP}\int_0^L\frac{F_3}{wH_3}\,dx
=\frac1{3A^\beta}\operatorname{FP}\int_0^L Q'm^{\beta-1}\,dx
=\frac{(\beta-1)A^{1-\beta}}3
\operatorname{FP}\int_0^L(Q-Q(L))m^{\beta-2}g^{-1}\,dx .
\tag{7}
$$

Here is the endpoint justification for the last equality. The anchored trace modulus gives an anchored \(\theta\)-modulus for \(Q\), by the tail reconstruction and product estimates in the radius proof. Thus \((Q-Q(L))m^{\beta-1}=O((L-x)^{\theta+\beta-1})\to0\). This is enough for the source boundary term and integrability; it does not assert that an anchored modulus is a full two-point \(C^\theta\) norm. At zero, the smooth odd trace gives even Taylor expansions for the smooth factors in \(Q\) and \(m\). The boundary product has powers \(-4-\beta,-2-\beta,-\beta,2-\beta,\ldots\), none zero. Its finite-part boundary value is zero. The origin remainder is integrable after the three singular terms are subtracted, as also proved in the first two functional proofs. These facts justify (7).

Since \(\rho=x^2ya\) with smooth \(a\) near zero, \(G_3\) is smooth and even there. The normalized factor \(H_3/x^{6+\beta}\) is likewise smooth, even, and positive. Therefore \(G_3/H_3=x^{-6-\beta}\) times a smooth even function. Taylor expansion through degree 6 leaves a remainder \(O(x^8)\); since \(6<6+\beta<7\), its finite part is zero. Integrating (6) with \(l_3=0\) yields

$$
B_3=\operatorname{FP}_{x\downarrow0}G_3/H_3=0.
\tag{8}
$$

Finally the exact change of variables in the first proof gives
\(\mathcal B(A,e,\widetilde w)=L^{4+\beta}B_3\).
The certified functional theorem in [../02-radius/PROOF.md](../02-radius/PROOF.md) gives \(\mathcal B>0.14\) under (1) or (2). The norm conversion in the third proof gives the same conclusion under (3). This contradicts (8), proving the stated exclusion.

One may alternatively replace condition 3 by the explicit endpoint condition \(l_3=0\), or by boundedness of \(\partial_y^3\rho\) along the left axis near \(P\). Under that stronger direct endpoint hypothesis the proof above needs no appeal to the supplied nonlinear endpoint theorem.

## What is not proved

The theorem does not show that an exact profile close to sampled trial data lies in any of these norm balls. The large distances between equally good fitted references are evidence of the sensitivity, while the counterexamples in the third proof establish the missing implication at the level of compatible traces. No certified accuracy of the trial as an exact solution, or quantitative complex continuation bound on an exact trace, is available here.

The definition of \(\mathcal P_\infty\) alone does not impose \(\alpha_P>1-2/A\), the cone bounds, or \(l_3=0\). Profiles outside those source hypotheses, outside the parameter intervals, or outside the trace balls are not excluded. The observed pointwise sign condition \((H_-)\) on a grid is not proved by this work.

The report asserts propagation of smoothness from zero along the open axis, but explicitly records an unchecked cited estimate in §6.3.1(f). To avoid silently resolving that issue, condition 2 retains open-axis smoothness as an explicit hypothesis. If that propagation result is accepted, this extra hypothesis follows for the corresponding profiles; the source and trace-closeness hypotheses still remain.

No existence theorem, classification theorem, exclusion of all \(\mathcal P_\infty\), or condition on the higher odd obstructions is obtained. The rigorous new numerical result is a positive obstruction on this exact reference and on the stated nearby compatible traces.
