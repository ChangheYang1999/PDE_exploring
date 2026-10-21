# Referee answer

**Verdicts.**

1. **PROVED, by route (b).** Smoothness propagates along every finite, nonstationary \(W\)-trajectory into a region where \(\rho\) is smooth. The proof below uses a localized energy estimate and an explicit resolvent regularization. It does not use the propagation proposition attributed to Taylor.
2. **PROVED WITH CORRECTIONS.** The localization assertion is valid. One must specify the normalization at infinity, distinguish the principal-value multiplier from the full velocity multiplier, and justify uniform differentiation of the tail. The earlier tail calculation has the right powers; it is incomplete, rather than incorrect.
3. **PROVED WITH CORRECTIONS.** The direct argument produces a continuous third transverse trace and a distributional third axis equation. By itself it does not produce a classical \(w'''\) or a classical \(F_3\). It proves \(B_3=0\) under the stated bounded-trace hypothesis when \(B_3\) is given its canonical weak, equivalently derivative-free, interpretation. If the original integral is required to have a classical integrand, that interpretation or an additional regularity argument is necessary. Part (1) supplies the latter independently. The same argument at only \(C^{2,\alpha}\) regularity does not establish the fifth-order step; moreover, \(A=2\) is a fifth-order centre resonance.

All arguments concern actual solutions of the stated profile equation. No existence claim for such profiles is made.

I read the specified local proofs and report passages. The attempted Opus collaboration failed during credential retrieval, before any model was called; there was no Opus consultation or verified model identity. Also, I did not obtain a verified copy of Taylor's source text. An earlier progress message claiming otherwise was incorrect. The proof here avoids that source entirely.

I prove localization first because it is needed in both other parts. Throughout, \(C^{k,\alpha}\) means classical Hölder regularity, \(H^s\) is the inhomogeneous \(L^2\) Sobolev space, and distributional derivatives of continuous functions are interpreted by integration by parts.

## (2) Canonical normalization and localization

### 2.1 The kernels and the normalization

Write \(q\) for any one of
\[
\rho,\qquad \chi\rho,\qquad (1-\chi)\rho.
\]
These functions have the required parities and satisfy a bound of the form (A3), with possibly different constants. The normalization (A2) is not needed for defining their velocities.

The kernels have zero integral on every circle centred at zero and satisfy
\[
|\partial^\nu K(Z)|\le C_\nu |Z|^{-2-|\nu|},\qquad Z\ne0.
\tag{2.1}
\]
For every centred annulus,
\[
\int K(-Y)q(Y)\,dY=0.
\tag{2.2}
\]
Indeed, the first component of the integrand is odd in \(y_1\), and the second is odd in \(y_2\). At zero this integrand is locally integrable: oddness in \(y_2\) and \(C^1\) regularity imply \(q(Y)=O(|Y|)\).

Consequently the symmetric truncation in (V2) can be written
\[
U[q](X)=-\frac{q(X)}2e_2+
 \operatorname {PV}\int_{\mathbb R^2}
       \bigl(K(X-Y)-K(-Y)\bigr)q(Y)\,dY.
\tag{2.3}
\]
The principal value here is only at \(Y=X\). Its existence follows by subtracting \(q(X)\) in a small ball centred at \(X\), using the zero circular mean and
\[
|q(Y)-q(X)|\le C_X|Y-X|.
\]
For \(|Y|>2|X|+1\), the mean-value theorem gives
\[
|K(X-Y)-K(-Y)|\le C|X||Y|^{-3}.
\tag{2.4}
\]
The radial majorant at infinity is therefore \(C_X r^{\gamma-2}\), which is integrable precisely under the sufficient condition \(\gamma<1\). This proves existence of the symmetric truncation and its equality to (2.3). It also proves linearity for the displayed decomposition.

For clarity about the growth regimes:

* If \(\gamma<0\), the unsubtracted tail is already absolutely integrable.
* If \(\gamma=0\), that absolute convergence is not guaranteed; the unsubtracted radial majorant is \(r^{-1}\).
* If \(0<\gamma<1\), it is likewise not guaranteed; subtraction improves \(r^{\gamma-1}\) to \(r^{\gamma-2}\).

Parity makes the removed constant exactly zero in all three cases. It is not an unspecified choice of a velocity constant.

Let
\[
E(Z)=-\frac1{2\pi}\log|Z|.
\]
Integration by parts on a punctured disk, followed by letting its radius tend to zero, gives
\[
-\Delta E=\delta_0,\qquad
-\partial_{12}E=\operatorname {PV}K_1,\qquad
\partial_{11}E=\operatorname {PV}K_2-\frac12\delta_0.
\tag{2.5}
\]
Here the delta coefficient in the last identity is
\(- (2\pi)^{-1}\int_0^{2\pi}\cos^2\theta\,d\theta=-1/2\);
the mixed angular average is zero. The ordinary derivatives away from zero are exactly the displayed kernels. These observations, including the boundary terms, prove (2.5) distributionally.

For compactly supported \(q\), the full velocity multiplier is thus
\[
\widehat{U[q]}(\xi)=m(\xi)\widehat q(\xi),\qquad
m(\xi)=
\left(\frac{\xi_1\xi_2}{|\xi|^2},
      -\frac{\xi_1^2}{|\xi|^2}\right),\quad \xi\ne0.
\tag{2.6}
\]
Its value at \(\xi=0\) is irrelevant in \(L^2\). The multiplier of the principal-value integral alone is
\[
\tau(\xi)=
\left(\frac{\xi_1\xi_2}{|\xi|^2},
      \frac{\xi_2^2-\xi_1^2}{2|\xi|^2}\right).
\tag{2.7}
\]
Thus one should write either \(U[q]=m(D)q\), or
\(U[q]=\tau(D)q-qe_2/2\), not add the local term a second time.
There is no additional Fourier distribution supported at zero in (2.6): for a smooth compact input the kernel convolution is locally bounded by cancellation and is \(O(|X|^{-2})\) at infinity, hence belongs to \(L^2\). Its difference from the bounded-multiplier answer has Fourier support at zero by (2.5), and an \(L^2\) function with that support is zero. Approximation gives the formula for the other compact inputs used here.

Equations (2.5)–(2.6) imply
\[
\operatorname {div}U[q]=0,\qquad
\operatorname {curl}U[q]=-\partial_xq.
\tag{2.8}
\]
For noncompact \(q\), apply this first to even radial cutoffs \(q_R\). On a fixed compact set, the difference between \(U[q_R]\) and (2.3), and each positive-order derivative of that difference, is a separated tail. Bounds (2.1)–(2.4) show local convergence, including first derivatives. This proves (2.8) for \(q\). Reflection in each coordinate proves the stated velocity parities.

Here is also the required sublinear bound; it does not follow merely from writing a formal convolution. Put \(r=|X|\ge2\). In \(B(X,r/2)\), subtract \(q(X)\). The gradient bound in (A3) gives a contribution \(O(r^\gamma)\). In
\(B(0,2r)\setminus B(X,r/2)\), bound the kernel by \(Cr^{-2}\). Beyond \(2r\), use (2.4). Including the local term gives
\[
|U[q](X)|\le C
\begin{cases}
r^\gamma,&\gamma>-2,\\
r^{-2}(1+\log r),&\gamma=-2,\\
r^{-2},&\gamma<-2.
\end{cases}
\tag{2.9}
\]
For the middle region this uses
\[
r^{-2}\int_0^{2r}t(1+t)^\gamma\,dt;
\]
the outer region is bounded by
\(Cr\int_{2r}^\infty t^{\gamma-2}\,dt\).
These estimates prove \(U[q](X)=o(|X|)\).

Finally, uniqueness in (V3) fixes every remaining gauge. The difference \(H\) of two such fields has zero divergence and curl, so both components are distributionally harmonic. They are smooth: mollify on a ball and apply a fixed smooth radial averaging kernel supported in a smaller ball. The harmonic mollifications equal their averages. Their local \(L^1\) convergence and differentiation of that fixed averaging kernel show that the limit equals its own smooth average. Differentiating the averaging identity yields
\[
|\nabla H(X)|\le C R^{-1}\sup_{B(X,2R)}|H|.
\]
Sublinear growth, followed by \(R\to\infty\), makes the right side tend to zero. Thus \(H\) is constant. The two odd parities make both constants zero. Linear harmonic gauges are excluded by the sublinear condition.

This proves (V2) \(=\) (V3), with the normalization asserted in the question, for all three densities.

### 2.2 Smoothness and bounds for the separated tail

Let \(q=(1-\chi)\rho\), and let \(N\) be the open set on which \(\chi=1\). On every compact subset of \(N\), separation from \(\operatorname{supp}q\) proves smoothness of the bounded part of the integral. For the unbounded part, choose a centred radius \(R>2\sup_{X\in N}|X|+2\). This is possible because \(\chi\) is compactly supported. Subtract \(K(-Y)\) only outside \(R\), which is legitimate by (2.2).

For \(n\ge1\), the differentiated tail has radial majorant
\[
C_n r^{-2-n}(1+r)^\gamma r,
\]
whose integral converges because \(n>\gamma\). For \(n=0\), use (2.4). These are locally uniform majorants for every derivative, so differentiation under the integral is justified by dominated convergence.

There is even a uniform bound on all of \(N\), if desired; one need not silently assume that its closure is separated from \(\operatorname{supp}q\). All derivatives of \(1-\chi\) vanish at every \(X\in N\). Taylor's formula therefore gives, for every integer \(M\),
\[
|1-\chi(Y)|\le C_{\chi,M}|X-Y|^M
\quad(X\in N,\ |X-Y|\le1).
\tag{2.10}
\]
For a derivative of order \(n\), choose \(M>n\) in (2.10). The local radial integral is bounded by a constant times
\(\int_0^1t^{M-n-1}\,dt\).
The remaining bounded region has no singularity. If
\[
\mathcal M_\gamma=\sup_Y(1+|Y|)^{-\gamma}|\rho(Y)|,
\]
the resulting estimates are
\[
\sup_N|\partial^\nu U[(1-\chi)\rho]|
\le C_{\nu,\chi,\gamma}\mathcal M_\gamma.
\tag{2.11}
\]
The constant includes the size of the support of \(\chi\) and the chosen radius \(R\). The local term vanishes on \(N\).

This proves the requested bound, in a slightly stronger homogeneous form than \(C(1+\mathcal M_\gamma)\).

### 2.3 The local multiplier estimates

For completeness, the Hölder estimate needed here has a short direct proof. Decompose either kernel into annular kernels
\[
K=\sum_{j\in\mathbb Z}K_j,\qquad
\operatorname{supp}K_j\subset\{c2^j<|Z|<C2^j\},
\]
using a smooth radial partition of unity. Each \(K_j\) has integral zero. For compactly supported \(v\in C^\alpha\),
\[
\|K_j*v\|_\infty\le C[v]_\alpha2^{j\alpha}\quad(j\le0),
\qquad
\|K_j*v\|_\infty\le C2^{-2j}\|v\|_1\quad(j>0).
\tag{2.12}
\]
These bounds prove uniform convergence. For a displacement of length \(h\le1\), sum (2.12) over \(2^j\le h\). Over \(h<2^j\le1\), use
\[
\|\nabla K_j*v\|_\infty
\le C[v]_\alpha2^{j(\alpha-1)}.
\]
The resulting geometric sums are \(O(h^\alpha)\). The terms \(2^j>1\) contribute at most \(Ch\|v\|_1\), by the corresponding \(2^{-3j}\) derivative bound. Thus the principal-value operator maps compactly supported \(C^\alpha\) functions to \(C^\alpha\).

Derivatives commute with convolution distributionally. Apply the same argument to every \(\partial^\nu v\), \(|\nu|\le k\), to obtain the \(C^{k,\alpha}\) assertion. The local term has the same regularity.

By (2.6) and Plancherel,
\[
\|U[v]\|_{H^s}\le C\|v\|_{H^s},
\qquad s\in\mathbb R.
\tag{2.13}
\]
This is a global bound whenever \(v\in H^s\). The multipliers are smooth homogeneous symbols of degree zero away from \(\xi=0\). If “order-zero symbol” is understood to require smoothness also at zero, cut off the low frequencies. For compactly supported inputs the omitted low-frequency piece is smooth: its Fourier transform has compact support and all polynomial moments are integrable, also for compactly supported distributional inputs. No assertion about smoothness of the angular multiplier at zero is needed.

It follows that
\[
U[\rho]=U[\chi\rho]+U[(1-\chi)\rho]
\tag{2.14}
\]
has \(C^{k,\alpha}\), respectively \(H^s_{\rm loc}\), regularity on \(N\) under exactly the local hypotheses in the question. The second term is \(C^\infty\).

One can also use an arbitrary compact cutoff \(\eta\), without parity, locally: \(U[\eta\rho]\) is its ordinary compact-support convolution, and \(U[\rho]-U[\eta\rho]\) has a smooth separated tail where \(\eta=1\). This follows by subtracting the compact convolution from (2.3). Its additive constant is inherited from (2.3), rather than fixed by parity of the individual summands.

**Assessment of the earlier sketch.** Its parity cancellation and the conditions \(\gamma<1\), \(n>\gamma\) are correct. It omits the local principal value, the delta term, the sublinear estimate and gauge uniqueness, the local Hölder/Sobolev mapping argument, and uniform justification of differentiation. Those omissions are supplied above.

**External results used in (2).** Only the foundational Fourier and integration facts stated in the final source list. The singular-integral estimates, normalization, harmonic uniqueness argument, and tail estimates have been proved here.

## (1) Smoothness propagation: a physical-space proof

The point of the following proof is to avoid a propagation theorem whose rough-symbol hypotheses would themselves need auditing. We prove a one-derivative local estimate and iterate it at integer Sobolev orders.

### 1.1 Two elementary estimates

Let \(R\) be any of the constant Fourier multipliers in (2.6), including a finite matrix of such multipliers. Its symbol satisfies
\[
|m(\xi)|\le C,\qquad |\nabla m(\xi)|\le C|\xi|^{-1}\quad(\xi\ne0).
\]
Hence
\[
|\eta|\,|m(\eta)-m(\xi)|\le C|\xi-\eta|.
\tag{1.1}
\]
To check this, if \(|\eta|\le2|\xi-\eta|\), use boundedness. Otherwise the segment joining \(\xi\) to \(\eta\) stays at distance at least \(|\eta|/2\) from zero, and the mean-value theorem applies.

If \(\chi\in C_c^{2,\alpha}(\mathbb R^2)\), Fourier convolution, (1.1), and Young's inequality give
\[
\|[\chi,R]\partial_jv\|_2
\le C\left(\int |\zeta|\,|\widehat\chi(\zeta)|\,d\zeta\right)\|v\|_2
\le C_\chi\|v\|_2.
\tag{1.2}
\]
The integral is finite. Indeed, \(C_c^{2,\alpha}\subset H^{2+\eta}\) for \(0<\eta<\alpha\), and Cauchy–Schwarz applies to that integral. The inclusion follows directly by integrating the squared Hölder increment of \(D^2\chi\) against \(|h|^{-2-2\eta}\,dh\). Its equivalence to the Fourier \(H^\eta\) seminorm follows from Plancherel and the identity
\[
\int_{\mathbb R^2}\frac{|e^{ih\cdot\xi}-1|^2}{|h|^{2+2\eta}}\,dh
=c_\eta|\xi|^{2\eta},
\]
obtained by rotation and scaling. Thus (1.2) includes an explicit proof of the cutoff gain used below.

We also need a product estimate. For compactly supported bounded \(v,z\in H^m\), \(m\ge1\), and nonnegative integers \(a+b=m\),
\[
\|D^av\,D^bz\|_2
\le C_m\bigl(\|v\|_\infty\|z\|_{H^m}
                  +\|z\|_\infty\|v\|_{H^m}\bigr).
\tag{1.3}
\]
Here and below such notation includes each individual partial derivative of the specified order.

Here is a proof, including the interpolation ingredient. For \(0<a<m\), split \(D^av\) into a smooth low-frequency part at scale \(t\) and dyadic higher-frequency bands. The low part is bounded by \(Ct^{-a}\|v\|_\infty\). On a band of spatial scale \(s\), division by \(|\xi|^{2m}\), using
\[
|\xi|^{2m}=\sum_{|I|=m}\frac{m!}{I!}\xi^{2I},
\]
expresses that band as \(s^{m-a}\) times a finite sum of Schwartz convolutions of \(D^Iv\). A scaled Schwartz convolution is bounded pointwise by a constant times the Hardy–Littlewood maximal function of its input: split its kernel into dyadic spatial annuli and sum their rapidly decreasing bounds. Summing the bands \(s=2^{-j}t\) gives
\[
|D^av|\le C\bigl(t^{-a}\|v\|_\infty+
                   t^{m-a}M(|D^mv|)\bigr).
\]
Optimizing \(t\) and taking \(L^{2m/a}\) norms gives
\[
\|D^av\|_{2m/a}
\le C\|v\|_\infty^{1-a/m}\|D^mv\|_2^{a/m}.
\tag{1.4}
\]
For reference, the maximal-function \(L^2\) bound used in this calculation follows as follows. Greedy selection of disjoint balls whose fivefold dilations cover any finite family proves
\(|\{Mf>\lambda\}|\le C\|f\|_1/\lambda\).
Apply this to \(f\,1_{\{|f|>\lambda/2\}}\), since the complementary part has maximal function at most \(\lambda/2\), and integrate
\(2\lambda|\{Mf>\lambda\}|\) in \(\lambda\). Fubini gives \(C\|f\|_2^2\). Exhaustion removes the finite-family restriction. This proves the bound needed in (1.4).

The endpoint cases of (1.4) are immediate. Hölder with exponents \(2m/a,2m/b\), followed by weighted arithmetic–geometric mean, proves (1.3). Smooth approximation proves the assertion for the stated Sobolev functions. Local versions follow by inserting cutoffs.

### 1.2 A local one-derivative propagation lemma

Consider a finite system
\[
Pu=W\cdot\nabla u+\sum_{\nu=1}^J B_\nu(X)R_\nu u+C(X)u=F.
\tag{1.5}
\]
Assume globally, after extension from a bounded neighborhood if necessary,
\[
W\in C_b^{2,\alpha},\qquad B_\nu,C\in C_b^{1,\alpha},
\qquad u\in L^2,\qquad F=Pu\in H^{-1}.
\tag{1.6}
\]
Suppose a compact nonstationary trajectory arc has a flow tube on which \(F\in H^1_{\rm loc}\), and \(u\in H^1\) near its forward endpoint. Then \(u\in H^1\) near every earlier point of the arc.

The coefficients can be real or complex matrices, except that \(W\) is real. No positivity or self-adjointness of the order-zero terms is assumed.

**Flow cutoff.** A sufficiently thin tube has coordinates \((t,s)\) with \(W\cdot\nabla=\partial_t\). Indeed, take a transverse interval through the trajectory and apply the \(C^{2,\alpha}\) flow; its differential is invertible on the central arc. Compactness and uniqueness permit a thinner interval on which this is a tube. A repeated trajectory can be shortened by removing complete periods. The differentiability assertion follows by differentiating the flow integral equation twice; bounded \(DW,D^2W\), Gronwall, and the Hölder bound give \(C^{2,\alpha}\) dependence.

For any prescribed \(\lambda>0\), choose compactly supported \(C^{2,\alpha}\) functions \(\chi,e\) in this tube such that \(\chi>0\) near the earlier point, \(e\) is supported in the region where \(u\in H^1\), and
\[
D(\chi^2)\ge\lambda\chi^2-K_e e^2,\qquad D=W\cdot\nabla.
\tag{1.7}
\]
Explicitly take \(\chi=\eta(s)e^{\lambda t/2}\theta(t)\). Let \(\theta\) rise from zero before the point to be estimated, and let it decrease to zero only in the terminal regular region. Then
\[
D(\chi^2)=\lambda\chi^2+
2\eta(s)^2e^{\lambda t}\theta(t)\theta'(t).
\]
A cutoff \(e\) covering the negative part of \(\theta'\) proves (1.7). Extend these functions by zero outside the tube.

**Regularization.** Put
\[
J_\varepsilon=(1-\varepsilon^2\Delta)^{-1},\quad
u_\varepsilon=J_\varepsilon u,\quad
v=\nabla u_\varepsilon,\qquad 0<\varepsilon\le1.
\]
Then \(u_\varepsilon\in H^2\),
\[
\|u_\varepsilon\|_2\le\|u\|_2,\qquad
\|v\|_2\le C\varepsilon^{-1}\|u\|_2,
\tag{1.8}
\]
and the exact identity
\[
Pu_\varepsilon=J_\varepsilon F+E_\varepsilon u_\varepsilon,\qquad
E_\varepsilon=-\varepsilon^2J_\varepsilon[\Delta,P]
\tag{1.9}
\]
holds distributionally. This follows by multiplying the commutator identity by \(1-\varepsilon^2\Delta\); it is not an asymptotic expansion.

The useful forms of its coefficients are
\[
[\Delta,W\cdot\nabla]z
=2\partial_i((\partial_iW_j)\partial_jz)
       -(\Delta W_j)\partial_jz,
\tag{1.10}
\]
\[
[\Delta,B]z
=\partial_i((\partial_iB)z)+(\partial_iB)\partial_i z.
\tag{1.11}
\]
Repeated indices are summed. Formula (1.11) only uses first derivatives of \(B\), including when \(B\) is merely \(C^{1,\alpha}\).

Define
\[
L_{\varepsilon,\ell i}=\varepsilon^2\partial_\ell J_\varepsilon\partial_i,
\qquad M_{\varepsilon,\ell}=\varepsilon^2\partial_\ell J_\varepsilon.
\]
Their \(L^2\) norms are at most \(1\) and \(C\varepsilon\), respectively. Their cutoff commutators obey
\[
\|[\chi,L_{\varepsilon,\ell i}]\|_{2\to2}
\le C\varepsilon\|\nabla\chi\|_\infty,\qquad
\|[\chi,M_{\varepsilon,\ell}]\|_{2\to2}
\le C\varepsilon^2\|\nabla\chi\|_\infty.
\tag{1.12}
\]
Here is a kernel verification that also handles the singularity in \(L_\varepsilon\). Use
\[
J_\varepsilon=\int_0^\infty e^{-t}e^{t\varepsilon^2\Delta}\,dt.
\]
For the Gaussian kernel \(G_s\),
\[
\int |z|\,|\partial_{\ell i}G_s(z)|\,dz\le Cs^{-1/2},
\qquad
\int |z|\,|\partial_\ell G_s(z)|\,dz\le C.
\]
Multiply by \(\varepsilon^2\) and integrate with \(s=t\varepsilon^2\). The resulting first moments are \(C\varepsilon\) and \(C\varepsilon^2\). Multiplication by
\(\chi(X)-\chi(Y)\) and Young's inequality prove (1.12); any delta contribution commutes and disappears. Truncating the \(t\)-integral first justifies this argument for the distribution kernel.

Equations (1.8), (1.10)–(1.12), and (1.2) give the crucial estimate
\[
\|\chi\nabla E_\varepsilon u_\varepsilon\|_2
\le K_0\|\chi v\|_2+C_\chi\|u\|_2,
\tag{1.13}
\]
where \(K_0\) is independent of \(\chi,\lambda,\varepsilon\), and depends only on the bounded coefficient norms and the finite system.

To make the localization in (1.13) explicit, its transport terms are sums of
\[
L_\varepsilon((\partial W)v),\qquad
M_\varepsilon((\Delta W)v).
\]
Move \(\chi\) through \(L_\varepsilon,M_\varepsilon\). The principal terms contain \(\chi v\); the errors are bounded by (1.12) times (1.8). Its \(B_\nu R_\nu\) terms are sums of
\[
L_\varepsilon((\partial B_\nu)R_\nu u_\varepsilon),\qquad
M_\varepsilon((\partial B_\nu)R_\nu v).
\]
The first has an \(L^2\) bound by \(\|u\|_2\). In the second first move \(\chi\) through \(M_\varepsilon\), using (1.12) and (1.8), and then use
\[
\chi R_\nu v=R_\nu(\chi v)+[\chi,R_\nu]\nabla u_\varepsilon
\]
and (1.2). The terms involving \(C\) are identical with \(R_\nu=I\). This proves every term in (1.13), without differentiating \(\Delta W\) or \(\partial B_\nu\).

Two other bounds are uniform in \(\varepsilon\):
\[
\|\chi\nabla J_\varepsilon F\|_2\le C_F,\qquad
\|e\nabla J_\varepsilon u\|_2\le C_u.
\tag{1.14}
\]
For the first insert a smooth cutoff equal to one on a neighborhood of \(\operatorname{supp}\chi\). The localized part of \(F\) belongs to \(H^1\). The other part is in \(H^{-1}\) and is separated from \(\operatorname{supp}\chi\). All derivatives of the kernel of \(J_\varepsilon\), restricted to a fixed positive separation, are bounded uniformly for \(0<\varepsilon\le1\), with arbitrarily fast decay at infinity. This follows directly from the same Gaussian integral: polynomial factors are absorbed by
\(\exp(-t-|z|^2/(4t\varepsilon^2))\).
Pairing the separated kernel with \(H^{-1}\), or its first \(Y\)-derivatives with \(L^2\), proves the first bound. More explicitly, the separated kernel and its first \(Y\)-derivatives have uniformly bounded squared integrals in \((X,Y)\) for \(X\) in the compact support of \(\chi\), which is the required \(H^{-1}\)-to-\(L^2\) bound. The second bound is the same argument, using the local \(H^1\) regularity of \(u\) near \(\operatorname{supp}e\).

**Energy estimate.** Differentiate (1.9). The differentiated equation for \(v\) has transport part \(Dv\), order-zero terms
\[
(DW)v,\quad B_\nu R_\nu v,\quad Cv,
\]
and the additional terms
\[
(\partial B_\nu)R_\nu u_\varepsilon,\quad
(\partial C)u_\varepsilon,\quad
\nabla J_\varepsilon F,\quad
\nabla E_\varepsilon u_\varepsilon.
\]
Take the real \(L^2\) pairing with \(\chi^2v\). Integration by parts is legitimate since \(v\in H^1\), and
\[
\operatorname{Re}\int\chi^2\overline v\,Dv
=-\frac12\int\bigl(D(\chi^2)+(\operatorname{div}W)\chi^2\bigr)|v|^2.
\]
Use (1.2) to move \(\chi\) through each \(R_\nu\), and then (1.13)–(1.14). There is a constant \(K_1\), independent of \(\chi,\lambda,\varepsilon\), such that
\[
\frac{\lambda}{2}\|\chi v\|_2^2
\le K_1\|\chi v\|_2^2+C_\chi\|\chi v\|_2+C_\chi.
\tag{1.15}
\]
The terminal term is bounded by the second estimate in (1.14). The constants denoted \(C_\chi\) may depend on the chosen tube, \(\lambda\), the known norms of \(u,F\), and terminal regularity, but are finite and independent of \(\varepsilon\).

Choose \(\lambda>2K_1+2\) before constructing \(\chi\). Inequality (1.15) bounds \(\chi\nabla u_\varepsilon\) uniformly in \(L^2\). Weak compactness and \(u_\varepsilon\to u\) in \(L^2\) imply \(\chi\nabla u\in L^2\). Since \(\chi>0\) near the point in question, \(u\in H^1\) there. This proves the lemma.

Notice the exact coefficient threshold: two bounded derivatives of \(W\), one bounded derivative of the order-zero coefficients, and a small positive Hölder exponent for constructing cutoffs satisfying (1.2). There is no hidden requirement that the order-zero term be \(C^{2,\alpha}\).

### 1.3 Applying and iterating the lemma

Let \(\mathcal O\) be the open set of points whose forward trajectories enter the given smooth open set \(V\) in finite time along a nonstationary arc. Openness follows from continuous dependence of the flow and compactness of each such arc. Every point on an arc before its terminal point also belongs to \(\mathcal O\).

By part (2), \(W\in C_{\rm loc}^{2,\alpha}\), and \(W\) is smooth where \(\rho\) is smooth. Initially \(\rho\in H^2_{\rm loc}(\mathcal O)\).

Suppose inductively that
\[
\rho\in H^k_{\rm loc}(\mathcal O),\qquad k\ge2.
\]
Part (2) implies the same local \(H^k\) regularity for \(U\). Fix one compact trajectory tube in \(\mathcal O\) with terminal portion in \(V\), and a compact cutoff equal to one on a neighborhood of this tube. Set \(u_I=\partial^I(\eta\rho)\), \(|I|=k\). This is a finite \(L^2\) system on the plane.

On the tube, differentiate \(D\rho=\rho\) \(k\) times. The terms in which exactly one derivative lands on \(W\) are a matrix, with entries formed from \(DW\), acting on the \(u_I\). The terms in which all \(k\) derivatives land on \(W\) are
\[
\nabla\rho\cdot R u_I
+\text{a locally }H^1\text{ term}.
\tag{1.16}
\]
Indeed, \(\partial^I(c_\ell X)=0\) for \(k\ge2\), and
\(\partial^I U[\rho]=R\partial^I(\eta\rho)+\) a smooth separated-tail term. Multiplying that smooth term by \(\nabla\rho\in C^{1,\alpha}\) gives an \(H^1\) term.

The remaining products are
\[
(\partial^J U)\,\nabla\partial^{I-J}\rho,
\qquad 2\le |J|\le k-1.
\tag{1.17}
\]
They belong locally to \(H^1\). To verify this, take one additional derivative. The two factors then have orders between \(2\) and \(k\), with total order \(k+2\). Apply (1.3), with \(m=k-2\), to cutoff versions of \(D^2U,D^2\rho\). Their \(L^\infty\) norms are finite by \(C^{2,\alpha}\), and their \(H^{k-2}\) norms are finite by the induction hypothesis. The undifferentiated products are handled by the same estimate with smaller total order. For \(k=2\) there are no products (1.17).

Thus the localized system has exactly the form (1.5), with \(B_\nu,C\in C^{1,\alpha}\), and \(F\in H^1\) near the tube. Extend the coefficients using a smooth cutoff from a slightly larger compact neighborhood. Globally \(Pu\in H^{-1}\), since \(u\in L^2\) and the extended coefficients have the bounded derivatives in (1.6). Near the terminal portion \(u\in H^1\), because \(\rho\) is smooth there.

All differentiations just made are valid distributionally. One justification is to mollify \(U,\rho\) locally: they converge in \(H^k\) and \(C^2\); the highest transport derivative converges in \(H^{-1}\), and (1.3) controls the remaining products. No derivative of an unknown \(H^{k+1}\) function was assumed in deriving its equation.

The lemma proves \(u_I\in H^1\) near the initial point. Therefore
\[
\rho\in H^{k+1}_{\rm loc}(\mathcal O).
\]
The open set \(\mathcal O\) is fixed throughout this induction. For each point and each order, all estimates take place on a compact tube and use finitely many finite local norms. No uniform bound as a tube approaches a zero of \(W\) is asserted or needed.

Induction gives every integer Sobolev order. Fourier inversion and Cauchy–Schwarz imply \(H^m_{\rm loc}\subset C^\ell_{\rm loc}\) in two dimensions whenever \(m>\ell+1\). Hence \(\rho\) is \(C^\infty\) near \(z_0\).

For the open positive-axis segment, every point reaches a sufficiently small positive-axis point in finite forward time: on any intervening compact segment \(w<0\) is bounded away from zero. That point lies in the smooth neighborhood of the origin. Thus this proves (C1), indeed with all orders.

**External results used in (1).** The foundational Fourier, integration, Hilbert-space compactness, and ODE facts stated at the end. The cutoff commutator, interpolation/product estimate, regularization estimate, localization, and propagation argument were proved above. No Taylor, Bony, Hörmander propagation, or paradifferential regularity theorem is an input. The real-principal and nonradial requirements are replaced here by the explicit real, nonvanishing vector field and its flow tube.

## (3) The direct third-order argument, without invoking (1)

In this section assume only \(C^{2,\alpha}\) regularity along the segment, the stated first-source geometry, and smoothness near zero. Part (1) is not used.

### 3.1 The identity and the continuous forcing

Put \(f=\rho\), \(W=(a,b)\), and restrict to a compact tube where \(a\ne0\). Define
\[
K=f_{yy}-\frac{f_y}{a}a_y.
\]
The claimed identity is correct:
\[
(D+2b_y-1)K=F,
\tag{3.1}
\]
\[
F=\left(\frac{a_y^2}{a}-a_{yy}\right)
           \left(f_x+\frac{bf_y}{a}\right)
       -2a_yf_{xy}
       +(a_x-b_y)\frac{f_y}{a}a_y.
\tag{3.2}
\]
Here is an algebraic verification that records exactly which equations are used. If \(E=af_x+bf_y-f\), expansion and collection of derivatives gives
\[
(D+2b_y-1)K-F
=E_{yy}-\frac{a_y}{a}E_y
       -f_y\,\partial_y(a_x+b_y).
\tag{3.3}
\]
The three terms on the right vanish because \(E=0\) and \(a_x+b_y=A+1\). Formula (3.3) can also be obtained by differentiating \(E\) twice, using
\[
D f_y=(1-b_y)f_y-a_yf_x,
\]
and expanding \(D((f_y/a)a_y)\). Thus it uses neither the curl equation nor a third derivative of a coefficient after the cancellation. I also checked (3.3) symbolically.

For \(C^2\) data, (3.3) and (3.1) hold in distributions. Local mollification proves this directly: terms of order three are interpreted as derivatives of continuous second derivatives, while all coefficients multiplying them are sufficiently differentiable for integration by parts. Alternatively, (3.3) is an identity between first derivatives of continuous expressions plus continuous terms. Its right side vanishes distributionally. In particular \(DK\) is continuous by (3.1).

Use the axis notation
\[
w=a(x,0),\quad h=b_y(x,0)=A+1-w',\quad
g=f_y(x,0),\quad a_2=\tfrac12a_{yy}(x,0).
\]
Uniformly on compact subsegments, parity and \(C^2\) regularity give
\[
\frac{f_x}{y}\to g',\quad
\frac b y\to h,\quad
\frac{a_y}{y}\to2a_2,\quad
a_{yy}\to2a_2,\quad f_{xy}\to g'.
\tag{3.4}
\]
Consequently \(F/y\) extends continuously across the axis, with value
\[
L=-6a_2g'+\frac{2a_2g}{w}(w'-2h).
\tag{3.5}
\]
For example, divide the first term of (3.2) by \(y\): its limit is
\(-2a_2(g'+hg/w)\). The other two limits are
\(-4a_2g'\) and \(2a_2g(w'-h)/w\), giving (3.5). This calculation only uses second derivatives.

### 3.2 Characteristics and existence of the third trace

The use of characteristics for (3.1) is valid even though \(K\) was initially only continuous. In flow coordinates \(\Phi(t,s)\), the Jacobian satisfies
\[
\partial_t J=(\operatorname{div}W)(\Phi)J.
\]
The weak equation \(DK=G\), after this change of variables in its test integral, becomes
\(\partial_t(K\circ\Phi)=G\circ\Phi\) in distributions. For almost every \(s\), the fundamental theorem for a distribution with continuous derivative gives its integral formula in \(t\). Continuity of both sides extends that formula to every \(s\). This also proves the formula when a continuous zeroth-order coefficient is present, by an integrating factor. The change of variables is legitimate with \(C^1\) test functions; smooth approximation of such tests gives the same weak identity.

Off the axis put \(q=K/y\). Because \(b=yB\) with \(B\) continuous, trajectories starting off the axis stay off it:
\[
y(t)=y(0)\exp\!\left(\int_0^t B(\Phi_s)\,ds\right).
\]
Equation (3.1) becomes
\[
(D+c)q=\widetilde F,\qquad
c=2b_y-1+b/y,\qquad \widetilde F=F/y.
\tag{3.6}
\]
Both coefficients extend continuously across the axis, with values \(3h-1\) and \(L\).

Fix an axis point \(x_0\in(0,x_*)\). Choose a fixed finite \(T\) such that its forward trajectory ends in the smooth neighborhood of zero, still at a positive \(x\). A thin compact tube about this arc has \(a\ne0\), and all sufficiently nearby starting points also end in that smooth neighborhood at time \(T\). There \(K/y\) is smooth, since \(K\) is smooth and odd in \(y\).

The characteristic formula is
\[
q(X)=e^{\int_0^T c(\Phi_tX)\,dt}q(\Phi_TX)
 -\int_0^T e^{\int_0^s c(\Phi_tX)\,dt}
                  \widetilde F(\Phi_sX)\,ds.
\tag{3.7}
\]
The continuous extensions of \(c,\widetilde F\), compactness, and continuous dependence of the flow allow passage to the axis in (3.7). Thus \(q\) has a continuous extension \(M\), locally uniformly along the open segment. Its axis equation is
\[
wM'+(3h-1)M=L.
\tag{3.8}
\]
In particular \(M\in C^1\), since \(w\ne0\) and the other quantities are continuous.

Since \(f_{yy}(x,0)=0\),
\[
f_{yyy}(x,0):=\lim_{y\to0}\frac{f_{yy}(x,y)-f_{yy}(x,0)}y
=M(x)+\frac{2g(x)a_2(x)}{w(x)}
\tag{3.9}
\]
exists and is continuous in \(x\). With \(G_3=f_{yyy}(x,0)/6\), this is precisely
\[
M=6G_3-\frac{2ga_2}{w}.
\tag{3.10}
\]
Integrating the locally uniform expansion of \(f_{yy}\) twice also gives
\[
f(x,y)=g(x)y+G_3(x)y^3+o(y^3)
\]
locally uniformly in \(x\). This is a transverse trace statement; it does not assert \(C^3\) regularity in a two-dimensional neighborhood.

### 3.3 What the third axis equation means

Differentiating the transport equation once at the axis gives
\[
wg'=(1-h)g=(w'-A)g.
\tag{3.11}
\]
Initially \(g\in C^{1,\alpha}\), but on the open segment (3.11) improves it to \(C^{2,\alpha}\). Differentiating the curl equation once in \(y\) gives
\[
a_2=\frac{g'-w''}{2}.
\tag{3.12}
\]
Thus \(a_2\) is in general only \(C^\alpha\); no classical \(a_2'\) has yet been established.

Substitute (3.10) into (3.8), use (3.5) and (3.11), and differentiate continuous functions distributionally. The result is
\[
wG_3'+(3h-1)G_3
=-a_2g'+\frac g3a_2'=:F_3.
\tag{3.13}
\]
For explicit checking, the right side before division by six is
\[
L+2w(ga_2/w)'+2(3h-1)ga_2/w
=-6a_2g'+2ga_2'.
\]
Products such as \(ga_2'\) mean
\((ga_2)'-g'a_2\). They are well-defined derivatives of continuous functions plus continuous functions. The notation
\(b_3=-a_2'/3\) is therefore valid as a distributional coefficient identity; it does not establish the classical trace \(b_{yyy}/6\).

To formulate the integration precisely, put
\[
\beta=\frac2A\in(0,2),\qquad
m=-\frac wg>0,\qquad
Q=\frac{a_2}{g^3},\qquad
H=H_3=A^\beta g^3m^{-\beta},\qquad Z=\frac{G_3}{H}.
\tag{3.14}
\]
The normalization near zero and (3.11) imply \(g>0\) on the segment. Also
\[
m'=-A/g,\qquad
F_3=\frac{g^4}{3}Q',\qquad
Z'=-\frac{A^{-\beta}}3\,m^{\beta-1}Q'.
\tag{3.15}
\]
All these identities make sense with the just-described distributional convention.

There is no need to integrate an undefined product or to suppose that \(Q'\) is a measure. On any compact interval \([u,v]\subset(0,x_*)\), define
\[
\int_u^v m^{\beta-1}\,dQ
:=[m^{\beta-1}Q]_u^v
-(\beta-1)\int_u^v m^{\beta-2}m'Q\,dx.
\tag{3.16}
\]
The last integrand is continuous. Equation (3.15) says exactly
\[
Z(v)-Z(u)=-\frac{A^{-\beta}}3
                          \int_u^v m^{\beta-1}\,dQ.
\tag{3.17}
\]
This is the required weak integration formula. It coincides with ordinary integration whenever \(Q\) is locally absolutely continuous.

Near zero all functions under consideration are smooth. Parity and the normalization give
\[
g=x^2\widetilde g(x),\quad w=-Ax\widetilde w(x),\quad
H=x^{6+\beta}\widetilde H(x),
\tag{3.18}
\]
where the tilded functions are smooth, positive and even, with value one at zero. Also \(G_3\) is smooth and even. Hence
\[
Z=x^{-6-\beta}S(x),\qquad S\ \hbox{smooth and even}.
\]
A finite Taylor expansion of \(S\) shows that the finite-part constant of \(Z\) at zero is zero: the exponents are \(2j-6-\beta\), none of which is zero for \(0<\beta<2\). Analyticity or convergence of a Taylor series is not assumed.

More generally, if this finite-part constant is \(C_0\) and \(Z\to l_3\) at the source, (3.17) gives
\[
C_0=l_3+B_3^{\rm weak},\qquad
B_3^{\rm weak}:=-\operatorname{fp}\int_0^{x_*} Z'\,dx
=\frac{A^{-\beta}}3\operatorname{fp}
                         \int_0^{x_*}m^{\beta-1}\,dQ.
\tag{3.19}
\]
Here the endpoint integral is the limit of (3.16), not a claim that \(Q'\) is a function. This precisely states the sense in which the direct argument supports the integration and the finite part.

### 3.4 The bounded-trace theorem and its derivative-free functional

Assume now that the trace in (3.9) is bounded as \(x\uparrow x_*\). I prove the endpoint convergence needed to identify (3.19) with the report's derivative-free formula, without any additional Hölder threshold.

First \(g\) has a finite positive limit \(g_*\). Indeed,
\[
\frac{g'}g=\frac{w'-A}{w},
\]
and the right side extends continuously to \(x_*\), with value \(w''(x_*)/A\), because \(w\in C^{2,\alpha}\) and \(w'(x_*)=A\). Its integral is finite. Thus
\[
m\sim \frac A{g_*}(x_*-x),\qquad
Q\to Q_*=\frac{a_2(x_*)}{g_*^3}.
\tag{3.20}
\]
Bounded \(G_3\) gives
\[
Z=O(m^\beta),\qquad l_3=0.
\tag{3.21}
\]

A useful extra consequence is
\[
Q-Q_*=O(m).
\tag{3.22}
\]
This is stronger than the \(C^\alpha\) endpoint bound available a priori. To prove it, use \(m\) as a coordinate and denote the corresponding functions by \(q(m),z(m)\). Equation (3.15) becomes
\[
q'=-3A^\beta m^{1-\beta}z'
\]
in distributions. The continuous function
\[
-3A^\beta\left[
m^{1-\beta}z(m)
-(1-\beta)\int_0^m t^{-\beta}z(t)\,dt
\right]
\]
has precisely this derivative and tends to zero at \(m=0\), by (3.21). It therefore equals \(q(m)-Q_*\). Both displayed terms are \(O(m)\), proving (3.22). This argument does not assume bounded variation of \(q\) or \(z\).

For \(\beta\ne1\), integration by parts in (3.19), with \(Q_*\) subtracted, now gives
\[
B_3^{\rm weak}
=\frac{(\beta-1)A^{1-\beta}}3\,
\operatorname{fp}\int_0^{x_*}
(Q-Q_*)m^{\beta-2}g^{-1}\,dx.
\tag{3.23}
\]
The source endpoint is absolutely integrable: (3.22) makes its size
\(O(m^{\beta-1})\), and \(dx/dm=-g/A\).
The source boundary term \((Q-Q_*)m^{\beta-1}\) tends to zero.

The finite-part boundary term at zero is also zero. To verify this explicitly, \(a_2\) is smooth and odd there, so
\[
Q=x^{-5}\times(\hbox{smooth even function}),\qquad
m=(A/x)\times(\hbox{smooth positive even function}).
\]
The exponents in \(Qm^{\beta-1}\) are \(-4-\beta+2j\), and those in \(Q_*m^{\beta-1}\) are \(1-\beta+2j\). Neither list contains zero for \(0<\beta<2\), \(\beta\ne1\). A finite Taylor expansion again suffices.

For \(\beta=1\), the weight in (3.19) is constant. The finite part of \(Q\) at zero is zero, and \(A=2\), so
\[
B_3^{\rm weak}=Q_*/6.
\tag{3.24}
\]
Thus (3.23)–(3.24) are exactly the derivative-free formulas in §6.3.1(i). Under the bounded-trace hypothesis their endpoint convergence follows from the equation itself; the separate sufficient condition \(\theta+\beta>1\) is unnecessary here.

Finally \(C_0=0\) by (3.18) and \(l_3=0\) by (3.21). Equation (3.19) proves
\[
\boxed{B_3^{\rm weak}=0.}
\tag{3.25}
\]

The precise answer to the wording of task (3)(b) is therefore:

* **Yes**, without (C1), for the obstruction functional defined by (3.23)–(3.24), equivalently the weak extension (3.19). The hypotheses are exactly the admissible profile assumptions, first-source geometry, smoothness near zero, and bounded third transverse trace at the source. The trace itself was constructed above.
* **Not as an assertion about an already classical integrand** \(F_3/(wH_3)\), unless that interpretation is supplied or further regularity is proved. The missing step is \(a_2'\), equivalently the relevant combination involving \(w'''\), being a classical or locally integrable function. The direct trace argument does not establish it. Local absolute continuity of \(a_2\) would suffice for the ordinary integral interpretation on compact subintervals. Part (1) proves much more and therefore recovers the report's original classical formulation as well.

There is no counterexample to the classical theorem here. The distinction is between what this direct proof alone establishes and the additional regularity needed to read its integrand classically.

### 3.5 Why this does not give the fifth-order step at \(C^{2,\alpha}\)

The third-order cancellation closes because (3.2) contains only derivatives of order at most two, and parity makes its quotient by \(y\) continuous. The conclusion is a third trace, not the bulk regularity needed to differentiate the equation two further times.

At order five the formal forcing is
\[
F_5=-a_2G_3'-3b_3G_3-a_4g'-b_5g.
\tag{3.26}
\]
With only the conclusions of the direct argument, \(a_4,b_5\) have not been constructed as classical traces. Moreover \(b_3=-a_2'/3\) is only a distribution and \(G_3\) is only continuous, in general \(C^\alpha\). Their product in (3.26) has no canonical general distributional meaning. These are concrete failures of the hypotheses needed to repeat the calculation. An additional cancellation theorem would have to be proved; none follows from (3.1).

If one uses part (1), all these coefficients are smooth on the open segment, and the usual hierarchy and endpoint conditions apply. There remains a separate resonance:
\[
p_5=10+\frac4A.
\]
For \(A>1\) it is an even integer exactly when \(A=2\), where \(p_5=12\). At that value the homogeneous \(H_5\) has a smooth even centre germ, so smoothness at zero does not force its coefficient to vanish. Thus the standard conclusion \(B_5=0\) from smoothness and the stated endpoint conditions also requires \(A\ne2\), or an extra condition eliminating the resonant centre coefficient. This observation is not an existence claim for a coupled profile with nonzero resonant coefficient.

**External results used in (3).** Only the foundational integration and ODE facts below. The algebraic identity, passage to characteristics for continuous weak solutions, trace construction, distributional integration, endpoint improvement, finite parts, and resonance check were proved explicitly above.

## Foundational results and sources

For completeness, these are the external mathematical facts used. Their precise mathematical statements are given here; these are not purported verbatim quotations or unverified theorem-number attributions. All specialized PDE estimates used in the answer were proved above.

1. **Fourier inversion, Plancherel, convolution, and differentiation.** With a fixed unitary Fourier normalization on \(\mathbb R^2\), the Fourier transform is unitary on \(L^2\); differentiation corresponds to multiplication by \(i\xi_j\); convolution corresponds to multiplication of Fourier transforms when initially defined for Schwartz functions, and then by density or distributional extension. A bounded measurable multiplier has \(L^2\) norm at most its essential supremum. The same statement with weight \((1+|\xi|^2)^{s/2}\) gives the \(H^s\) multiplier assertion. Source: G. B. Folland, *Real Analysis: Modern Techniques and Their Applications*, second edition, Wiley, 1999, Chapter 8, with distributions as developed in Chapter 9. Used in (1) and (2).
2. **Young, Hölder, and Cauchy–Schwarz inequalities.** In particular, \(\|k*v\|_2\le\|k\|_1\|v\|_2\), and \(\|vz\|_2\le\|v\|_p\|z\|_q\) when \(1/p+1/q=1/2\). Source: Folland, the same book, the \(L^p\) and convolution chapters. Used in (1) and (2).
3. **Lebesgue convergence and iterated integration.** Dominated convergence permits passage of a pointwise limit through an integral under an integrable majorant; Fubini applies to integrable functions and Tonelli to nonnegative functions. Smooth convolution approximates locally integrable functions in their local \(L^p\) spaces, and Sobolev functions in their Sobolev norms after localization. Source: Folland, the same book, Chapters 2, 6, 8, and 9. Used throughout. Every nontrivial majorant or derivative bound required for these applications was supplied above.
4. **Weak compactness in a Hilbert space.** A bounded sequence in \(L^2\) has a weakly convergent subsequence; if it also converges distributionally, its weak limit is that distribution. Source: Folland, the same book, Chapters 5–6. Used once in the regularization limit in (1).
5. **Local ODE flow and inverse function theorem.** A \(C^1\) vector field has a unique local flow, continuously dependent on its initial point, whose derivative solves the variational equation \(\dot V=DW(\Phi_t)V\). For a \(C^{2,\alpha}\) field on a compact flow neighborhood, differentiating the flow equation twice and estimating its increments gives a \(C^{2,\alpha}\) flow there. A \(C^1\) map with invertible derivative has a local \(C^1\) inverse; differentiating the inverse identity preserves the stated higher regularity. Sources: P. Hartman, *Ordinary Differential Equations*, second edition, Birkhäuser, 1982, the existence/uniqueness and dependence-on-initial-data chapters; W. Rudin, *Principles of Mathematical Analysis*, third edition, McGraw–Hill, 1976, Chapter 9, inverse function theorem. Used in (1) and (3). The compact-tube construction, cutoff, and distributional characteristic argument needed beyond these elementary facts were given above.

No unproved propagation estimate, elliptic Schauder estimate, Calderón–Zygmund boundedness theorem, or higher-order trace theorem remains as an input to parts (1)–(2) or to the corrected third-order conclusion. The limitations are the classical-versus-weak interpretation explicitly identified in (3), the failure of that direct \(C^{2,\alpha}\) argument to provide fifth-order data, and the fifth-order resonance at \(A=2\).