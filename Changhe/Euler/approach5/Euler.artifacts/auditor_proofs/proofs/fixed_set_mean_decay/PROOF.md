# Escaping means and invariant-basin lower bounds

This is the independent audit of C32, in the team records. The limits, averaged bounds and basin dichotomy below are conditional theorems. The further description of all fixed-set mean methods as closed is not a mathematical consequence of them.

## Exact hypotheses and existing inputs

Let \(2/5<c<1/2\), \(\omega\in\mathbb R\), and let \(U\in C^2(\mathbb R^3;\mathbb R^3)\), \(P\in C^1(\mathbb R^3)\) solve

\[
\operatorname{div}U=0,\qquad
(1-c)U+\omega JU+(Ay+U)\cdot\nabla U+\nabla P=0,
\quad A=cI-\omega J.
\]

Assume that \(U\) is bounded, \(U(R\,\cdot)\to0\) in distributions, and

\[
\int_1^\infty \sup_{|y|\geq r}|DU(y)|\,\frac{dr}{r}<\infty.
\tag{D}
\]

Uniform velocity decay can replace the first two assumptions. Set

\[
B=Ay+U,\quad W=\operatorname{curl}U,\quad
\Phi_t=\operatorname{flow}(B),\quad\Psi_t=\Phi_{-t},
\quad a=1-2c,\quad k=(1-c)/c.
\]

Normalize pressure as the canonical pressure, with no added constant, and define \(H_0=P+|U|^2/2+(Ay)\cdot U\), \(h=U\cdot W\).

The already proved scattering and tail results A209-A210, A355 and A361 supply the following precise inputs. With \(D_0=\|U\|_\infty/c\), there is a continuous map \(S\), a compact null set \(K=S^{-1}(0)\), and a \(C^1\) volume-preserving diffeomorphism

\[
S:\mathbb R^3\setminus K\longrightarrow\mathbb R^3\setminus\{0\},
\qquad S\Phi_t=e^{tA}S,
\qquad |\Phi_t y-e^{tA}S(y)|\leq D_0.
\tag{1}
\]

Also \(|S(y)-y|\leq D_0\). There are continuous tail fields \(V,\widetilde W=\operatorname{curl}V\) on the punctured space. Put \(\tau(z)=(Az)\cdot V(z)\) and \(\widetilde h=V\cdot\widetilde W\). Uniform spatial bounds and orbit limits are

\[
\begin{array}{c|c|c}
F& |F(y)|\leq C(1+|y|)^{-\lambda/c}&
\text{normalized orbit limit off }K\\ \hline
H_0&\lambda=a&e^{at}H_0(\Phi_t y)\to\tau(Sy)\\
U&\lambda=1-c&e^{(1-c)t}e^{\omega tJ}U(\Phi_t y)\to V(Sy)\\
h&\lambda=2-c&e^{(2-c)t}h(\Phi_t y)\to\widetilde h(Sy).
\end{array}
\tag{2}
\]

The scalar tails, and the norm of the vector tail, scale under \(e^{tA}\) with exponent \(-\lambda t\). The tail Lamb identity is

\[
aV+\widetilde W\times Az+\nabla\tau=0
\tag{3}
\]

in distributions, with the first two terms continuous.

The statements about basins below have a further explicit premise: countably many compactly supported full-\(\Psi\)-flow ergodic probabilities \(\nu\), disjoint open invariant essential domains \(D_\nu\), and full-volume physical basins inside them, covering \(\{W\ne0\}\) up to a null set. Their basins are defined by convergence against every continuous compactly supported observable. A308 and A223 provide this premise at \(C^\infty\); it is not assumed automatic at bare \(C^2\).

All profile flows used here are complete. For \(\Phi\) this follows from bounded \(U\); condition (D) also bounds \(DU\), and hence the vorticity field, when its complete volume-preserving flow is used in the signed-helicity consequence.

## 1. Exact escaping means

For every bounded measurable \(Q\), the limits are

\[
\begin{aligned}
e^{pat}\int_Q|H_0(\Phi_t y)|^pdy
&\longrightarrow \int_{S(Q\setminus K)}|\tau|^p,
&&0<p<3c/a,\\
e^{p(1-c)t}\int_Q|U(\Phi_t y)|^pdy
&\longrightarrow \int_{S(Q\setminus K)}|V|^p,
&&0<p<3c/(1-c),\\
e^{p(2-c)t}\int_Q|h(\Phi_t y)|^pdy
&\longrightarrow \int_{S(Q\setminus K)}|\widetilde h|^p,
&&0<p<3c/(2-c).
\end{aligned}
\tag{4}
\]

Each right side is finite.

To prove all three at once, put \(s=|S(y)|\) and use the corresponding \(\lambda\) in (2). If \(e^{ct}s\geq2(D_0+1)\), (1) gives \(|\Phi_t y|\geq e^{ct}s/2\), so

\[
e^{\lambda t}|F(\Phi_t y)|\leq C s^{-\lambda/c}.
\]

If \(e^{ct}s<2(D_0+1)\), the boundedness of \(F\) and \(e^{\lambda t}\leq[2(D_0+1)/s]^{\lambda/c}\) give the same bound. For \(Q\subset B_R\), the image \(S(Q\setminus K)\) lies in \(B_{R+D_0}\). Volume preservation therefore gives

\[
\int_Q |S(y)|^{-p\lambda/c}dy
\leq\int_{|z|<R+D_0}|z|^{-p\lambda/c}dz<\infty
\]

precisely when \(p\lambda<3c\). Dominated convergence and (2) prove (4).

The same proof gives convergence in the \(L^p\) sense, including the usual integral interpretation when \(p<1\), for the normalized scalar fields and for the rotated vector \(e^{(1-c)t}e^{\omega tJ}U(\Phi_t y)\). It does not give an unrotated vector limit when \(\omega\ne0\). Norm means in (4) need no rotation because rotations preserve length.

At \(p=2\), both \(H_0\) and \(U\) lie in this range. Their displayed exponential rates are exact leading orders only when the corresponding limiting integral is positive. A zero limit gives a little-oh conclusion and does not determine a next rate.

## 2. The exact volume identity and averaged core bounds

For every continuous \(F\), \(p>0\), bounded Borel \(Q\), and fixed time,

\[
e^{3ct}\int_Q|F(\Phi_t y)|^pdy
=\int_{\mathbb R^3}|F(x)|^p1_Q(\Psi_t x)\,dx.
\tag{5}
\]

This follows by \(x=\Phi_t y\) and \(\det D\Phi_t=e^{3ct}\).

Assume the basin premise, \(|F|^p\in L^1\), and \(\nu(\partial Q)=0\) for every \(\nu\). Write

\[
E_0=\mathbb R^3\setminus\bigcup_\nu D_\nu,\quad
a_T(x)=T^{-1}\int_0^T1_Q(\Psi_t x)\,dt,
\]

\[
C_F(Q)=\sum_\nu \nu(Q)\int_{D_\nu}|F|^p.
\]

Physicality and the boundary condition give \(a_T(x)\to\nu(Q)\) at almost every point of \(D_\nu\). This follows by approximating the indicator from above and below with continuous functions. Integrating (5) in time and using dominated convergence on the union of domains gives

\[
\frac1T\int_0^T e^{3ct}\int_Q|F\circ\Phi_t|^p\,dt
=C_F(Q)+r_T+o(1),
\tag{6}
\]

where

\[
0\leq r_T=\int_{E_0}|F|^pa_T
\leq\int_{E_0\cap\{W=0\}}|F|^p.
\]

The last inequality is up to a null set, by coverage. Thus the lower and upper limiting bounds differ by at most the displayed residual integral. If \(F=0\) on the uncovered vorticity zero set, the average converges to \(C_F(Q)\). No convergence of \(r_T\) is asserted otherwise.

The boundary condition is essential. Compact invariant supports lie in \(K\), since their forward \(B\)-orbits are bounded. For \(Q=K\), its volume is zero, so the left side of (5) is zero. But \(\nu(K)=1\). Indicator averages outside \(K\) therefore cannot converge to \(\nu(K)\).

For open bounded \(Q\), the one-sided portmanteau bound gives \(\liminf_Ta_T(x)\geq\nu(Q)\) in each basin. Fatou, without requiring integrability of \(|F|^p\), yields

\[
\liminf_{T\to\infty}\frac1T\int_0^T
e^{3ct}\int_Q|F\circ\Phi_t|^p\,dt
\geq C_F(Q).
\tag{7}
\]

The right side may be infinite. If a bound \(\int_Q|F\circ\Phi_t|^p\leq Ce^{-\ell t}\) holds for all sufficiently large \(t\), with \(\ell>3c\), the left side is zero. One may begin the average at that sufficiently large time; a fixed time shift does not change basin averages. Therefore \(F\) vanishes almost everywhere, and by continuity everywhere, on each open \(D_\nu\) with \(\nu(Q)>0\).

When \(|F|^p\in L^1\), (5) bounds the scaled integrand by \(\int|F|^p\). The same conclusion follows if the fast upper bound fails only on a set of times of zero asymptotic density. A bound merely on a set of positive density does not yield it.

For \(F=h\), a signed version of (6) holds: \(h\in L^1\) by (2), and \(h=0\) on \(\{W=0\}\). The vortex-invariant helicity balance gives \(\int_{D_\nu}h=0\), so the signed time average is zero, and the positive and negative helicity averages agree. This imports the already proved balance, not a new sign restriction.

## 3. Thresholds and what is not an expansion

For an observable in (2), when \(p\lambda<3c\), (4) gives an escaping term of order \(e^{-p\lambda t}\) if its coefficient is positive. Any contribution in (5) restricted to a fixed bounded set of \(x\) is \(O(e^{-3ct})\).

When \(p\lambda>3c\), the spatial bound in (2) gives \(|F|^p\in L^1\). Equation (5) then gives an unaveraged upper bound \(O(e^{-3ct})\), while (6)-(7) give averaged lower bounds. They do not give a matching unaveraged asymptotic.

If \(S(Q\setminus K)\) contains a punctured ball and the continuous homogeneous tail is nonzero, its formal \(p\)-power integral diverges for \(p\lambda\geq3c\). Angular integration of its norm is positive; twisted rotations preserve angular area, leaving a radial integral proportional to \(\int_0^\epsilon r^{2-p\lambda/c}dr\). If \(Q\) stays a positive distance from \(K\), its bounded image stays away from zero and no such divergence occurs.

At the critical power, the majorant in Section 1 gives the bound \(O((1+t)e^{-3ct})\). Indeed integrate the minimum of a bounded value and \(Ce^{-p\lambda t}s^{-p\lambda/c}\) in the volume coordinate \(s=|S(y)|\), splitting at a constant times \(e^{-ct}\). At \(p\lambda=3c\), the outer radial integral is logarithmic, of order \(t\).

For \(p=2\), \(2a=3c\) occurs at \(c=2/7\), and \(2(1-c)=3c\) at \(c=2/5\). These are algebraic crossover values. The theorem here is proved in \(2/5<c<1/2\); no extension of all its hypotheses to the other values is being asserted.

Equations (4) and (6) are not a two-term expansion of one quantity. In particular, they do not prove an unaveraged correction with coefficient \(C_F(Q)\), and a zero escaping coefficient leaves the next rate undetermined.

There is also a precise box version of the positive-coefficient case. Suppose
\(y=\Gamma_\tau\Psi_r\gamma(s)\) is a \(C^1\) coordinate box \(E\), with its
Jacobian \(J(s,r,\tau)\) bounded above and below by positive constants and
parameters in fixed bounded intervals. The exact commutation relation gives
\[
\Phi_t y=\Gamma_{\tau e^{(1+c)t}}\Phi_{t-r}\gamma(s).
\]
Put \(L=e^{(1+c)t}\). Substituting \(\sigma=L\tau\) yields the exact identity
\[
\begin{split}
&\int ds\,dr\int_{\tau_0L}^{\tau_1L}
 |H_0(\Gamma_\sigma\Phi_{t-r}\gamma(s))|^2
 J(s,r,\sigma/L)\,d\sigma\\
&\hspace{35mm}=L\int_E|H_0(\Phi_t y)|^2dy.
\end{split}
\]
If \(\int_E|\kappa_0|^2>0\), (4) makes this weighted box average asymptotic to
\(L^{1-2a/(1+c)}\int_E|\kappa_0|^2\). Dropping the bounded positive weight
gives matching upper and lower orders, not that same coefficient. If the
chosen starting plaque lies in the invariant support, the starting points
\(\Phi_{t-r}\gamma(s)\) do too. This calculation concerns the displayed box
average; it is not an assertion of a pointwise vortex occupation rate or an
unweighted \(\nu\)-average.

## 4. The basin dichotomy

Let \(D=D_\nu\), and put \(\kappa_0=\tau\circ S\) off \(K\). The set \(C_D=S(D\setminus K)\) is open and invariant under every \(e^{tA}\). Exactly one of these holds:

1. \(\kappa_0=0\) on \(D\setminus K\).
2. Every open \(E\subset D\) meeting \(\operatorname{supp}\nu\) has \(\int_E|\kappa_0|^2>0\).

In the second case every such bounded \(E\) has the exact positive leading order in (4) for \(H_0^2\).

To prove the alternative, suppose an open \(E\subset D\) meets the support but has zero integral. Continuity of \(\kappa_0\) off \(K\), and nullity of \(K\), give \(\kappa_0=0\) on \(E\setminus K\). Its transport law \(\kappa_0(\Phi_t y)=e^{-at}\kappa_0(y)\) extends this vanishing to

\[
G\setminus K,\qquad G=\bigcup_{t\in\mathbb R}\Phi_t(E).
\]

The set \(G\) is open, invariant and has positive \(\nu\)-measure. Ergodicity gives \(\nu(G)=1\). Choose a nonnegative continuous compactly supported function in \(G\) of positive \(\nu\)-integral. Every point in the physical basin has a positive time average for that function, hence enters \(G\), and therefore belongs to \(G\) by invariance. The basin has full volume in \(D\). Continuity then extends \(\kappa_0=0\) to all of \(D\setminus K\). This is the first alternative.

In that first alternative, \(\tau=0\) on the open set \(C_D\), so its distributional gradient is zero there. Equation (3) and continuity give

\[
aV=Az\times\widetilde W,\qquad
(Az)\cdot V=0,\qquad V\cdot\widetilde W=0
\quad\text{on }C_D.
\]

The orbit limits in (2) therefore have zero Bernoulli and helicity coefficients there. No additional rate of their vanishing follows.

The two alternatives exclude one another because \(\nu(D)=1\), so there are open subsets of \(D\) meeting the support. In a sign-changing helicity basin, \(H_0\) cannot vanish identically, since \(W\cdot\nabla H_0=-ah\). Thus the averaged lower bound (7) for \(H_0^2\) is positive on any open \(Q\) with \(\nu(Q)>0\), possibly infinite without a global integrability assumption. This does not decide which alternative occurs.

## 5. Scope of the method discussion

The formulas show that the currently proved upper and lower bounds are compatible in the target interval. They do not show that no further Euler estimate can yield a contradiction for fixed-set means. A new estimate using pressure or another consequence of the full equation could be precisely the missing structural argument.

Similarly, expressing the leading constant through \(\tau\) and \(S(Q\setminus K)\) does not prove independence from core dynamics. The scattering map \(S\) itself is constructed from the full velocity. There is no theorem here that one can hold that constant fixed while varying invariant supports arbitrarily. The justified statement is that the formula contains no explicit integral against \(\nu\).

Means against invariant probabilities are different quantities: \(\int|F\circ\Phi_t|^p\,d\nu=\int|F|^p\,d\nu\). Their singular support on the volume-null \(K\) prevents a direct comparison with volume means.

Thus the exact conditional identities and dichotomy are confirmed. An unconditional statement that the \(e^{-2at}\) rate is always attained, a two-term expansion, and a universal impossibility claim for all future fixed-set mean methods are not established.

## Verification

The complete submitted C32 text was read and retained with its hash in the team records. The audit reconstructed the majorant, every change of variables, the boundary countertest, the Fatou argument, the logarithmic endpoint and the invariant saturation used in the dichotomy. No numerical computation was needed.

The dependencies are exactly (1)-(3), the stated basin premise, ordinary compactness and integration theorems, and the previously checked vortex-invariant signed-helicity balance. The pressure normalization and the extra Dini and basin assumptions remain part of every applicable conclusion.
