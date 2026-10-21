# Audit of the normalization and differential

**Verdict: CONFIRMED**, with the trace-space hypotheses below. There is no missing source boundary term or dilation term. The source quotient must be evaluated after cancellation, and finite parts must be differentiated with their subtraction terms.

## Statement, notation, and dependencies

Let \(A>2\), \(\beta=2/A\), \(e>0\), and let
\[
w(0)=w(1)=0,\quad w'(0)=-A,\quad w'(1)=A,\quad w<0\text{ on }(0,1).
\]
Assume \(w\) is \(C^2\) on the closed interval, smooth on its interior if the classical axis identity is to be used, and
\[
w=-Au+d_3u^3+d_5u^5+d_7u^7+R,\qquad
|R^{(i)}|\le C u^{7+\sigma-i},\quad i=0,1,2,
\]
where \(\beta<\sigma\le2\). At the source require
\[
|w''(u)-w''(1)|\le C(1-u)^\theta,\qquad
0<\theta\le1,\quad \theta+\beta>1.
\]
An odd, smooth origin trace satisfies the origin condition.

Reconstruct \(g>0\) by
\[
k=\frac{g'}g=\frac{w'-A}{w},\qquad g/u^2\longrightarrow1,
\]
and put
\[
Q=\frac{g'-ew''}{2g^3},\quad m=-w/g,\quad
K=m^{\beta-2}/g,\quad \kappa=\frac{(\beta-1)A^{1-\beta}}3.
\]
The supplied report's §6.3.1(i) identifies the obstruction with
\[
B=\kappa\,\operatorname{FP}\int_0^1(Q-Q(1))K\,du. \tag{D1}
\]
This audit checks the functional and its differentiation. Its identification with the PDE obstruction uses that supplied identity, not a new PDE regularity theorem.

## 1. Scaling

For \(x=Lu\), \(w_{\rm phys}(Lu)=Lw(u)\), \(g_{\rm phys}(Lu)=L^2g(u)\),
\[
w_{\rm phys}''(Lu)=L^{-1}w''(u),\qquad
g_{\rm phys}'(Lu)=Lg'(u).
\]
Thus, with \(e=L^{-2}\),
\[
Q_{\rm phys}(Lu)=L^{-5}Q(u),\quad
m_{\rm phys}(Lu)=L^{-1}m(u),\quad
K_{\rm phys}(Lu)=L^{-\beta}K(u).
\]
Multiplication by \(dx=L\,du\) gives
\[
B(A,L^{-2},w)=L^{4+\beta}B_3(A,w_{\rm phys}). \tag{D2}
\]
Rescaling an origin cutoff produces the same equality for finite parts: the removed powers have nonzero exponents, and hence introduce no constant or logarithmic scaling anomaly. Since \(g\) depends on \(A,w\) and not on \(e\), (D1) is exactly affine in \(e\).

## 2. The source cancellation and variation of \(g\)

Write \(s=1-u\) and
\[
a=-w/s,\qquad j=(A-w')/s.
\]
The exact removable-quotient formulas are
\[
a(u)=\int_0^1w'(1-ts)\,dt,\qquad
j(u)=\int_0^1w''(1-ts)\,dt,\qquad k=j/a.
\]
Consequently \(a(1)=A\), \(j(1)=w''(1)\), and
\[
k(1)=w''(1)/A,\qquad
k(u)-k(1)=O(s^\theta).
\]
This argument also covers \(w''(1)=0\). No nonzero lower bound for \(w'-A\) is needed.

For a direction with \(v'(0)=v(1)=v'(1)=0\) and the same origin and anchored endpoint controls, define
\[
a_v=\frac{v'}w-\frac{(w'-A)v}{w^2}.
\]
Although the displayed formula has vanishing denominators, its equivalent form is
\[
a_v=\frac{\delta j-k\,\delta a}{a},\quad
\delta j=\int_0^1v''(1-ts)\,dt,\quad
\delta a=-v(u)/s.
\]
Here \(\delta j(1)=v''(1)\) and \(\delta a=O(s)\). Thus
\[
a_v(1)=v''(1)/A,\qquad
a_v(u)-a_v(1)=O(s^\theta). \tag{D3}
\]
At the origin \(a_v=O(u)\). The normalization \(g/u^2\to1\) fixes the integration constant, giving exactly
\[
\delta\log g=\eta_v(u):=\int_0^u a_v(t)\,dt. \tag{D4}
\]
In particular \(\eta_v(1)\) generally is not zero. It is finite, and
\[
\eta_v(1-s)=\eta_v(1)-\frac{v''(1)}A s+O(s^{1+\theta}).
\]
The original proof correctly retains this endpoint variation.

## 3. Local differentiation and the adjoint

Use the original notation
\[
d=\frac{k}{2g^2}-3Q,\quad
D=d+(1-\beta)(Q-Q(1)),\quad
b_*=\frac1{2Ag(1)^2}-\frac e{2g(1)^3}.
\]
Differentiating \(Q=kg^{-2}/2-ew''g^{-3}/2\) and \(K=(-w)^{\beta-2}g^{1-\beta}\) gives
\[
\delta Q=\frac{a_v}{2g^2}-\frac{ev''}{2g^3}+d\eta_v,\qquad
\delta K=K\left[(\beta-2)\frac vw+(1-\beta)\eta_v\right].
\]
By (D3),
\[
\delta Q(1)=b_*v''(1)+d(1)\eta_v(1).
\]
Therefore the differentiated integrand is
\[
K\{\mathscr L(v)+D\eta_v-d(1)\eta_v(1)\},
\]
where
\[
\mathscr L(v)=\frac{a_v}{2g^2}-\frac{ev''}{2g^3}
-b_*v''(1)+(\beta-2)(Q-Q(1))\frac vw.
\]
Define
\[
\mathscr J(t)=\int_t^1K(u)[D(u)-d(1)]\,du
-d(1)\int_0^tK(u)\,du.
\]
For each \(0<t<1\), both integrals are ordinary integrals. At 1,
\[
K=O(s^{\beta-2}),\quad D-d(1)=O(s^\theta),\quad
\mathscr J=O(s^{\beta-1})+O(1).
\]
The first integrability condition is precisely \(\theta+\beta>1\). The second gives integrability of \(\mathscr J a_v\). Also \(\mathscr L(v)=O(s^\theta)\): its first three terms cancel at 1, and its last term is \(O(s^{1+\theta})\). Separating those first three terms into improper integrals would generally be invalid.

On an origin-cutoff interval, Fubini applied to
\[
[D-d(1)]\eta_v-d(1)\int_u^1a_v
\]
produces the asserted adjoint plus boundary products. The potentially nonvanishing product is
\[
\eta_v(\epsilon)\int_\epsilon^1 K[D-d(1)].
\]
Its singular factors have even-power expansions times \(\epsilon^{-4-\beta}\), whereas \(\eta_v\) begins at order \(\epsilon^2\). No product has exponent zero because \(0<\beta<1\). Remainder products tend to zero under \(\sigma>\beta\). The other boundary product is bounded by
\[
O(\epsilon^{1-\beta})\,|\eta_v(1)-\eta_v(\epsilon)|\longrightarrow0.
\]
Thus the first product has zero finite part and the second tends to zero. This proves
\[
D_wB(v)=\kappa\left[
\operatorname{FP}\int_0^1 K\mathscr L(v)
+\operatorname{FP}\int_0^1\mathscr J a_v\right]. \tag{D5}
\]

## 4. Origin jets and differentiation of the finite part

Let
\[
\phi_j=u^j+\frac{j-11}{2}u^9+\frac{9-j}{2}u^{11},\quad j=3,5,7.
\]
They have the prescribed three origin jets and satisfy \(\phi_j(1)=\phi_j'(1)=0\). For
\[
R_\phi=v-\sum c_j\phi_j,
\]
the origin bounds are \(R_\phi^{(i)}=O(u^{7+\sigma-i})\), since \(\sigma\le2\). In (D5),
\[
K R_\phi''/g^3=O(u^{\sigma-\beta-1}),\quad
\mathscr J=O(u^{-4-\beta})+O(1),\quad
a_{R_\phi}=O(u^{5+\sigma}).
\]
All remainder integrals are ordinary and absolutely convergent. Linearity gives exactly the original equations (7) and (8), including all three jet coefficients. This use of \(R_\phi\) in the differential does not make it the remainder used in the norm of the next original proof.

For completeness, the rigorous differentiation rule is best stated using a fixed cutoff \(r\). If the singular origin factor is
\[
F=F_0+F_2u^2+F_4u^4+R_F,
\]
then
\[
\mathfrak F_\beta(F)=
\sum_{j=0,2,4}\frac{F_jr^{j-4-\beta}}{j-4-\beta}
+\int_0^r u^{-5-\beta}R_F(u)\,du. \tag{D6}
\]
The remaining integral is bounded by a constant times
\(u^{\sigma-\Re\beta-1}\). Differentiating in \(A\) inserts powers of \(\log u\), and differentiating at the source inserts powers of \(\log s\). A buffered strip
\[
\Re\beta\le b_+<\sigma,\qquad \Re\beta\ge b_->1-\theta
\]
dominates these logarithmic moments locally uniformly. Coefficients and denominators in the finite sum in (D6) must also be differentiated. The next proof supplies uniform bounds on the nonlinear origin factor and hence justifies this rule for the full trace ball, not merely for analytic one-parameter examples.

## 5. Parameter derivatives

Write \(w=Af\) and \(n=-f/g\). The equation for \(g\) becomes \(g'/g=(f'-1)/f\), so \(g\) is independent of \(A\) at fixed \(f\). Consequently
\[
B=c(A)J,\quad c(A)=\frac{\beta-1}{3A},\quad
J=\operatorname{FP}\int_0^1(Q-Q(1))n^{\beta-2}g^{-1}.
\]
At fixed \(\beta\),
\[
J_A=-\frac e2\operatorname{FP}\int_0^1
[f''g^{-3}-f''(1)g(1)^{-3}]n^{\beta-2}g^{-1}.
\]
Let \(J_\beta\) insert \(\log n\), with the finite parts interpreted by (D6). Since
\[
c'(A)=\frac{A-4}{3A^3},\qquad \beta'=-2/A^2,
\]
one obtains
\[
B_A\big|_f=\frac{A-4}{3A^3}J+
\frac{\beta-1}{3A}\left(J_A-\frac2{A^2}J_\beta\right),
\]
\[
B_e=-\frac{\beta-1}{6}\operatorname{FP}\int_0^1
[f''g^{-3}-f''(1)g(1)^{-3}]n^{\beta-2}g^{-1}.
\]
These are the original (9) and (10). For coordinates
\[
v=w-(A/A_0)w_0,
\]
the total first differential at the reference is \(B_A\Delta A+B_e\Delta e+D_wB(v)\). No extra source-motion derivative is missing: source motion is already represented by \(e=L^{-2}\) and the normalization (D2).

## Scope

This checks the analytic formulas, not the separately checked decimal values. It does not prove the PDE endpoint theorem or imply that an arbitrary compatible trace comes from a PDE profile.
