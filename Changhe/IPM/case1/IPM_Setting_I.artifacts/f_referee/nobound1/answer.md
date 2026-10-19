I did not obtain \(c_l\leq1\), either generally or under (Hmin). Several proposed sign arguments are false for smooth, positive test densities with the prescribed symmetry and normalization. Other arguments give valid identities but no contradiction.

Throughout, write \(l=c_l\), \(k=1/l\), and \(U[f]\) for the canonical velocity of a density \(f\). The counterexamples below are explicitly distinguished from actual profiles.

**1(a). Harmonic weights: FAILS as a positivity argument.**

Define
\[
\mathcal Q[f]
=\int_{\mathbb R^2}f\,U[f]\cdot\nabla(r^{-3}\sin3\theta)\,dX.
\]
For a profile, the checked identity gives
\[
\mathcal Q[\rho]=\pi(l-1)(3l-1).
\]
But the proposed functional inequality \(\mathcal Q[f]\leq0\) fails even when \(f\) is smooth, strictly positive in \(Q\), rapidly decreasing, and has the prescribed cubic normalization.

An explicit counterexample is
\[
f=x^2y e^{-r^2}.
\]
Its exact values are
\[
c[f]=\frac18,\qquad
\boxed{\mathcal Q[f]=\frac{3\pi}{512}(64\log2-43)>0.}
\]

Here is a calculation of the quadratic form. More generally, put
\[
f=x^2yF(r)=R(r)(\sin\theta+\sin3\theta),
\qquad R=r^3F/4.
\]
Writing \(\psi=S_2\sin2\theta+S_4\sin4\theta\), the forcing coefficients are
\[
f_2=R'+R/r,\qquad f_4=(R'-3R/r)/2.
\]
The modal Green formula and angular integration give
\[
\mathcal Q[f]=\frac{3\pi}{32}\int_0^\infty
\left[
\frac12r^3F^2
-2r^{-3}F(r)\int_0^r s^5F(s)\,ds
+4r^{-5}F(r)\int_0^r s^7F(s)\,ds
\right]dr.
\]
For \(F=e^{-r^2}\), substituting \(s=ur\) in the iterated integrals reduces the bracketed integral to
\[
\frac1{16}+\int_0^1\frac{-u^5+2u^7}{(1+u^2)^2}\,du
=4\log2-\frac{43}{16}.
\]
Its positivity follows, for example, from
\[
\log2
=2\sum_{j\geq0}\frac{(1/3)^{2j+1}}{2j+1}
>\frac{56}{81}>\frac{43}{64}.
\]

Furthermore,
\[
f_L=x^2y e^{-r^2/L^2}
\]
retains \(a(0)=1\) and satisfies
\[
c[f_L]=L^2/8.
\]
Thus positivity, symmetry, normalization, and the canonical law alone do not give \(c\leq2\). These functions do not satisfy the transport equation. A sign inequality restricted to actual profiles remains a possible, unproved theorem.

There is little additional freedom among full-plane homogeneous harmonic weights. If
\[
\phi=r^{-d}A(\theta),
\]
harmonicity requires \(A''+d^2A=0\). Periodicity and the relevant parities select positive odd integers \(d\). In the admissible interval \(k+2<d<5\), the only nontrivial choice is \(d=3\), with angular factor \(\sin3\theta\).

For the quadrant, the positive homogeneous harmonic weight vanishing on both axes is
\[
r^{-2}\sin2\theta.
\]
Its degree lies outside the guaranteed convergence interval. Other boundary behavior requires separate estimates.

Positive, nonharmonic quadrant weights do not automatically repair the sign. Here is a counterexample construction for
\[
\phi_d=r^{-d}\sin2\theta,\qquad 3<d<5.
\]
Let \(b=x^2y e^{-r^2}\), and let \(f\) be the even-x, odd-y reflection of a nonnegative smooth bump supported in a small disk around \((3,1)\). Then \(f=0\) near the origin and \(c_f>0\). Set
\[
b_{M,R}(X)=b(X)+MRf(X/R).
\]
These densities retain the normalization and strict positivity in \(Q\). As \(R\to\infty\), the added velocity converges locally to
\[
Mc_f(-x,y).
\]
Its self-contribution to the weighted quadratic form scales as \(M^2R^{3-d}\), hence vanishes. The other contribution involving the distant density also vanishes. Consequently,
\[
\int_Q b_{M,R}U[b_{M,R}]\cdot\nabla\phi_d
\longrightarrow
\int_Q bU[b]\cdot\nabla\phi_d+Mc_fJ_d,
\]
where direct angular integration gives
\[
J_d
=\int_Q b(-x,y)\cdot\nabla\phi_d
=\frac{2(d+2)}{105}\Gamma\!\left(\frac{5-d}{2}\right)>0.
\]
Choosing \(M\) large and then \(R\) large makes the quadratic form positive.

This rules out another positivity-only sign argument. It does not rule out a different weight combined with additional information from the profile equation.

**Weights centered at \(P\): PROVED identity, but no bound.**

A singular weight cannot simply be translated from the origin to \(P\), because \(\rho\) vanishes only linearly there.

Let
\[
Z=X-P,\qquad
\phi_P=|Z|^{-3}\sin(3\arg Z),\qquad g_*=g(x_*),
\]
and define circular principal values
\[
I_P=\operatorname{PV}\int\rho\phi_P,\qquad
Q_P=\operatorname{PV}\int\rho[U-U(P)]\cdot\nabla\phi_P.
\]
The strain formula, including its local correction, gives
\[
I_P=\pi(1-l+g_*/4).
\]

The inner boundary flux does not vanish. Indeed,
\[
\rho=g_*Z_2+O(|Z|^2),\qquad
W=((2l-1)Z_1,Z_2)+O(|Z|^2),
\]
so
\[
\lim_{\eta\downarrow0}
\int_{|Z|=\eta}\rho\phi_PW\cdot n\,dS
=\frac{\pi g_*}{2}(l-1).
\]
This follows from
\[
\int_0^{2\pi}\sin\theta\sin3\theta\cos^2\theta\,d\theta=\frac\pi4,
\]
while replacing \(\cos^2\theta\) by \(\sin^2\theta\) gives \(-\pi/4\).

The outer flux vanishes by sublinear growth. Therefore
\[
(1-l)I_P+Q_P=-\frac{\pi g_*}{2}(l-1),
\]
and hence
\[
\boxed{Q_P=-\pi(l-1)\left(l-1+\frac{g_*}{4}\right).}
\]
This is consistent with \(l>1\).

A proposed opposite sign for this quadratic form also needs additional hypotheses. For the positive upper-half-plane test density \(f=ye^{-r^2}\), centered at the origin, its principal-value quadratic form is
\[
\frac{3\pi}{16}(1-2\log2)<0.
\]
The same modal calculation reduces it to
\[
-\frac{3\pi}{4}\int_0^1\frac{u^5}{1+u^2}\,du.
\]
This test has the linear wall vanishing appropriate to \(P\), rather than the cubic vanishing at the original origin.

**1(b). Wall representation: PROVED with a convergence qualification. Positivity comparison: FAILS without additional global information.**

The proposed formula has the correct sign and constant:
\[
w(x)=lx+\frac2\pi\lim_{R\to\infty}
\int_{\substack{t>0\\s^2+t^2<R^2}}
\frac{t(x-s)\rho(s,t)}
{((x-s)^2+t^2)^2}\,ds\,dt.
\]
It follows directly by pairing the upper and lower half-plane contributions to \(K_1\).

At \((s,t)=(x,0)\), the wall condition gives \(\rho(s,t)=O(t)\). The absolute integrand is then \(O(((x-s)^2+t^2)^{-1/2})\), which is locally integrable.

At infinity, however, the unpaired integral need not converge absolutely. For example,
\[
\rho=x^2y(1+r^2)^{(k-3)/2},\qquad 0<k<1,
\]
has an absolute tail comparable on suitable sectors to
\[
\int^\infty r^{k-1}\,dr.
\]

Using evenness in \(s\), the convergent version is
\[
\frac2\pi\int_{s,t>0}t\rho(s,t)
\left[
\frac{x-s}{((x-s)^2+t^2)^2}
+\frac{x+s}{((x+s)^2+t^2)^2}
\right]ds\,dt.
\]
The paired kernel is \(O_x(r^{-3})\); its tail is absolutely integrable because \(\gamma<1\).

Differentiation introduces a local term:
\[
\boxed{
U_1'(x,0)=
\frac2\pi\operatorname{PV}\int_{t>0}
\frac{t(t^2-3(x-s)^2)\rho(s,t)}
{((x-s)^2+t^2)^3}\,ds\,dt+\frac{g(x)}4.
}
\]
To check the correction, differentiate with a moving half-disk of radius \(\eta\) deleted. Its boundary contribution tends to
\[
\frac{2g(x)}{\pi}\int_0^\pi\sin^2\theta\cos^2\theta\,d\theta
=\frac{g(x)}4.
\]
The remaining leading logarithm has zero angular mean.

The derivative kernel changes sign. This is a substantive obstruction to a positivity comparison. For instance, adding an upper-half-plane positive bump near \((1,3)\), with the required reflections, decreases \(c\); a bump near \((3,1)\) increases it. The amplitudes can be arbitrary, while the cubic normalization remains unchanged.

There is also an exact coupled counterexample to any argument using only the differential equations and the listed first-wall-segment conditions. For arbitrary \(l>1\), put \(A=2l-1\) and
\[
\begin{aligned}
g(x)&=2A\sin^2(x/\sqrt{2A}),\\
w(x)&=-A\sqrt{A/2}\sin(\sqrt{2/A}\,x),\\
\rho(x,y)&=g(x)y,\\
\psi(x,y)&=(lx-w(x))y.
\end{aligned}
\]
Then
\[
w'=-A+g,\qquad w''=g',\qquad wg'=(g-2A)g.
\]
Consequently,
\[
-\Delta\psi=\rho_x,\qquad
W=(w,(2l-w')y),
\]
and
\[
W\cdot\nabla\rho
=[wg'+(2l-w')g]y=\rho.
\]
The cubic coefficient is one. The first positive wall zero is
\[
x_*=\pi\sqrt{A/2},
\]
and
\[
w<0\text{ on }(0,x_*),\quad
w'(0)=-A,\quad w'(x_*)=A,\quad h(x_*)=1,\quad g(x_*)=2A.
\]

These are **not admissible profiles**: their density and velocity violate the growth requirements, and there are further wall zeros. They prove that the local coupled equations and all the specified first-segment data do not bound \(l\). Whether the full canonical wall integral together with all global hypotheses implies a bound remains unresolved.

**1(c). Invariant density and first integral: PROVED. A recurrence contradiction: FAILS.**

Under positivity,
\[
\operatorname{div}(\rho^{-2l}W)
=2l\rho^{-2l}-2l\rho^{-2l-1}W\cdot\nabla\rho=0.
\]
Since \(Q\) is simply connected, there is a globally defined function \(H\) satisfying
\[
H_x=-\rho^{-2l}W_2,\qquad
H_y=\rho^{-2l}W_1.
\]
Thus
\[
W\cdot\nabla H=0.
\]
Under (Hmin), \(H\) has no critical point in \(Q\).

But the invariant measure is infinite, even near an ordinary wall point:
\[
\rho^{-2l}\sim g(x)^{-2l}y^{-2l},
\qquad
\int_0^\eta y^{-2l}\,dy=\infty.
\]
Finite-measure recurrence therefore does not apply.

More explicitly, the local coordinates \(s=\log\rho\) and \(H\) satisfy
\[
\det\frac{\partial(s,H)}{\partial(x,y)}=\rho^{-2l},
\qquad
\frac{ds}{dt}=1,\qquad \frac{dH}{dt}=0.
\]
An invariant infinite measure is entirely compatible with translation in \(s\).

The linear saddle model provides a concrete check:
\[
W=(-(2l-1)x,(4l-1)y),\qquad \rho=x^2y.
\]
For every \(l>1\),
\[
H=x^{1-4l}y^{1-2l}
\]
is its first integral with the displayed derivatives. This model is not a coupled canonical profile, but it disproves any contradiction based on the invariant-density identity alone.

**1(d). Energy arguments: FAILS in their natural forms.**

If all integrals and boundary terms were justified, multiplication by \(y\) would give
\[
(1+3l)\int\rho y+\int\rho U_2=0.
\]
Two integrations by parts, using \(U_2=\psi_x\) and \(\rho_x=-\Delta\psi\), give
\[
\int\rho U_2=-\int|\nabla\psi|^2.
\]
Thus
\[
\int|\nabla\psi|^2=(1+3l)\int\rho y.
\]
Under positivity, its signs are compatible with every \(l>1\).

For finite radius, the correct identity is
\[
\begin{aligned}
\int_{B_R}|\nabla\psi|^2
={}&(1+3l)\int_{B_R}\rho y
-\int_{\partial B_R}\rho y\,W\cdot n\\
&+\int_{\partial B_R}\psi(\partial_n\psi+\rho n_x).
\end{aligned}
\]
It follows directly from the divergence identity and the same integrations by parts.

For a homogeneous far field of degree \(k\), the potential moment and its dilation flux both have order \(R^{k+3}\). The flux cannot be dropped. If the velocity also has degree \(k\), the Dirichlet energy has order \(R^{2k+2}\). These asymptotic statements are conditional on such a far field existing.

A positive cutoff does not preserve the dissipative sign. For
\[
f=x^2y e^{-r^2},
\]
one has \(U_2=y(1/8+o(1))\) near zero. Hence any nonzero, nonnegative smooth radial cutoff supported sufficiently near zero satisfies
\[
\int\chi fU_2>0.
\]
This explicitly refutes the weighted analogue of the unweighted dissipation inequality. A successful localized energy argument would need to control the additional terms, not discard them.

**1(e). Wall and y-axis comparisons: FAILS as local arguments; a nonlocal comparison remains unproved.**

The exact family in 1(b) already shows that the first wall segment, including the coupled differential equations there, permits arbitrary \(l>1\).

On the y-axis, under (Hmin), set
\[
v(y)=W_2(0,y)>0,\qquad q(y)=\rho_{xx}(0,y)/2>0.
\]
The transverse characteristic identity gives
\[
vq'=(2v'-(4l-1))q.
\]
This is a transport identity, not an elliptic maximum principle.

There are explicit compatible positive data for every \(l>1\). With \(B=4l-1\), take
\[
v(y)=y\frac{B+ly^2}{1+y^2},
\qquad
q(y)=\frac{y}{(1+y^2)^2}
\left(\frac{B+ly^2}{B}\right)^{(l+1)/(2l)}.
\]
Differentiation verifies the ODE, and
\[
v\sim By,\quad q\sim y\quad(y\downarrow0),
\]
while
\[
v\sim ly,\quad q\asymp y^{1/l-2}\quad(y\to\infty).
\]
Thus the local normalization, positivity, and expected transverse far-field scaling are mutually compatible for arbitrary \(l>1\). These are axis data, not a construction of the nonlocal field.

**2. The limit \(l\downarrow1\): some degeneration is PROVED, but the proposed limiting profile is CONDITIONAL.**

A rigorous statement follows immediately from the checked growth theorem:
\[
\gamma\geq1/l.
\]
Therefore a sequence \(l_n\downarrow1\) cannot have a single growth exponent \(\gamma<1\) valid for all sufficiently large \(n\), even allowing the constants to depend on \(n\).

This proves degeneration of the growth class. It does **not** prove that the core collapses, that local regularity deteriorates, or that profiles approach \(y\).

The resonant strain gives a more quantitative conditional statement. Suppose, for example, that outside \(R\),
\[
\rho=r^k\Theta(\theta),
\qquad
\Theta_3=\frac1\pi\int_0^{2\pi}\Theta(\theta)\sin3\theta\,d\theta.
\]
Writing \(\delta=1-k\), the exact tail contribution is
\[
\boxed{c_{\rm tail}=\frac{\Theta_3R^{-\delta}}{\delta}.}
\]
Consequently, if the inner strain remains uniformly bounded and \(c\to2\), then
\[
\Theta_3R^{-\delta}=O(\delta).
\]
For approximate homogeneous tails, a uniform bound on the remainder in the strain integral is additionally required. Neither a uniform tail decomposition nor a sign for \(\Theta_3\) follows from the given assumptions.

The state
\[
\rho=y,\qquad U=0,\qquad l=1
\]
solves the differential equations, but there are three qualifications.

First, it cannot be a \(C^1_{\mathrm{loc}}\) limit of the normalized densities, because
\[
\nabla\rho_n(0)=0
\]
for every \(n\). Under (Hmin), all profiles vanish on the entire y-axis, so \(y\) cannot even be their locally uniform full-plane limit. An outer limit resembling \(y\) would require weaker convergence, rescaling, or a layer along the y-axis.

Second, the critical velocity selection is discontinuous. Consider
\[
f_\delta=y(1+r^2)^{-\delta/2},\qquad 0<\delta<1.
\]
These are smooth sublinear densities, converging locally smoothly to \(y\). Their only density mode is \(\sin\theta\), with streamfunction forcing
\[
f_2(r)=-\frac{\delta}{2}r^2(1+r^2)^{-\delta/2-1}.
\]
The Green formula gives
\[
\psi_{xy}(0)
=\frac12\int_0^\infty \frac{f_2(r)}r\,dr
=-\frac14
\]
for every \(\delta\). The forcing tends smoothly to zero on bounded sets, and the remaining regular homogeneous mode has this fixed strain. Hence
\[
\boxed{U[f_\delta]\longrightarrow (x/4,-y/4)}
\]
locally smoothly, rather than \(0\).

Literal circular truncation of the linear density \(y\) gives the same linear strain. Thus the equivalence between circular truncation and the \(o(r)\) characterization must not be extended beyond the sublinear class.

Third, if actual profiles and velocities converge in \(C^1_{\mathrm{loc}}\), their limit necessarily satisfies
\[
(X+U_*)\cdot\nabla\rho_*=\rho_*,
\quad \operatorname{div}U_*=0,
\quad \operatorname{curl}U_*=-\partial_x\rho_*,
\]
and
\[
DU_*(0)=\operatorname{diag}(-2,2).
\]
Local convergence alone does not identify the global velocity selection. Preserving the cubic normalization also requires appropriate uniform control near zero.

**An expansion near \(l=1\): FORMAL, not an asymptotic family of admissible profiles.**

Let \(l=1+\varepsilon\), \(k=1/l\), and assume a leading homogeneous density and velocity
\[
\rho_0=r^k\Theta(\theta),\qquad U_0=r^kV(\theta).
\]
Seek
\[
\rho=r^k\Theta+r^{2k-1}\Theta^{(1)}+\cdots.
\]
At the next order, the transport equation requires
\[
-\varepsilon\Theta^{(1)}
+V\cdot(k\Theta e_r+\Theta'e_\theta)=0,
\]
so
\[
\boxed{
\Theta^{(1)}
=\varepsilon^{-1}V\cdot(k\Theta e_r+\Theta'e_\theta).
}
\]
On a sector where the numerator is of nonzero order one and \(\Theta\) stays away from zero, the relative correction is of order
\[
\frac{r^{-(1-k)}}{\varepsilon}.
\]
Thus the expansion becomes ordered only at radii satisfying
\[
(1-k)\log r\gg\log(1/\varepsilon).
\]
This is an exponentially large spatial scale as \(\varepsilon\downarrow0\). Resonant growth of \(V\) can make it larger.

The elementary expansion
\[
r^{1/(1+\varepsilon)}
=r\left[1-\varepsilon\log r
+O\!\left(\varepsilon^2((\log r)^2+|\log r|)\right)\right]
\]
does not by itself solve the nonlinear profile equation. Constructing a leading stationary state, choosing its velocity consistently, and matching it to the normalized core remain open steps.

**3. Physical remark: FAILS as written; the following corrected statements are PROVED.**

For physical IPM,
\[
q_t+U[q]\cdot\nabla q=0,
\]
substitution of
\[
q(t,z)=s^\alpha P(z/s^\beta),\qquad s=T-t,\qquad\beta=\alpha+1,
\]
gives the exact profile equation
\[
\boxed{\beta X\cdot\nabla P+U[P]\cdot\nabla P=\alpha P.}
\]
This is not the normalized equation with \(P=\rho\). To obtain it from
\[
(lX+U[\rho])\cdot\nabla\rho=\rho,
\]
one may take
\[
\alpha=\frac1{l-1},\qquad \beta=\alpha l,\qquad P=\alpha\rho.
\]
For \(l<1\), this changes the sign of the density and its cubic coefficient.

The positive-amplitude normalized branch instead has the infinite-time representation
\[
s(t)=1+(1-l)t,
\]
\[
\boxed{
q(t,z)=s(t)^{-1/(1-l)}
\rho\!\left(s(t)^{l/(1-l)}z\right).
}
\]
Direct substitution verifies it. Its focusing limit occurs as \(t\to\infty\), and its gradient prefactor is \(s(t)^{-1}\).

For the proposed finite-\(T\) ansatz, the exact gradient scaling is always
\[
\boxed{\nabla_zq=s^{-1}\nabla P(z/s^\beta).}
\]
Therefore:

- The gradient at the exact center is identically zero for a cubic profile, for every \(t\) and every \(l\).
- If \(0<\|\nabla P\|_\infty<\infty\), the global gradient norm grows exactly like \(s^{-1}\).
- When \(l<1\), \(\beta<0\). A fixed profile point carrying a nonzero gradient moves to physical infinity.

At fixed bounded physical positions, the cubic density expansion gives
\[
q(t,z)
=s^{(3l-1)/(1-l)}z_1^2z_2(1+o(1)),
\]
up to the cubic coefficient of \(P\). Hence the density tends to zero locally when \(l>1/3\). The corresponding local gradient conclusion holds if the differentiated cubic expansion is justified, for example if \(P\) is \(C^3\) near zero. A merely continuous factor \(a\) does not itself justify differentiating that expansion.

Thus local decay, global gradient growth at escaping points, and the infinite-time interpretation of the positive normalized branch are different statements. “Not a blowup” without specifying the spatial region, norm, and time orientation is incorrect.

The proofs and symbolic checks are saved in [PROOF.md](PROOF.md). The checks passed. The requested Opus 5.5 consultation could not run: the existing Bedrock profile failed to retrieve credentials before inference. No substitute model was used.