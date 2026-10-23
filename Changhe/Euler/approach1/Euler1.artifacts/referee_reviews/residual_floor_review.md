The proposed corollary is correct with a fixed modulus of continuity for the second derivatives. Its nondegeneracy condition passes to the limit exactly as proposed. There are useful strengthenings: no pressure bounds are needed; approximate incompressibility can be handled by a joint residual floor; and an \(L^2\) residual on one explicitly specified, sufficiently large ball suffices. The proof does not provide an explicit numerical residual floor. Below, “proved” means proved using the supplied, audited Theorem L1 and, for the fixed-ball strengthening, its audited local dynamical argument.

I use \(\langle y\rangle=(1+|y|^2)^{1/2}\), Euclidean norms for vectors, and Hilbert–Schmidt norms for derivative tensors. Matrix operator norms are indicated explicitly. All constants and regularity moduli must be fixed across the class.

The notation throughout is
\[
V=cy+U,\quad G=DU,\quad G_{ij}=\partial_jU_i,\quad
S=\tfrac12(G+G^T),\quad \Omega=\operatorname{curl}U,\quad
R_m=(1-c)U+GV+\nabla P.
\]
The accepted L1 input says: for \(0<c<1/2\), a \(C^2\) exact solution \(R_m=0\), \(\operatorname{div}U=0\) on \(\mathbb R^3\), with \(U=o(|y|)\) and countable \(\{V=0\}\), has \(\Omega=0\) and constant \(U\); if \(U\to0\), then \(U=0\).

**A precise corollary.** Fix \(0<c<1/2\), \(K\geq1\), and \(\delta>0\), and put
\[
d=1-\frac1c,\qquad
R_b=\left(\frac{2K}{c}\right)^c,\qquad
R_N=(2K)^{1/(2-d)}.
\]
Consider \(U\in C^3(\mathbb R^3;\mathbb R^3)\) and \(P\in C^1(\mathbb R^3)\) satisfying
\[
\begin{split}
|D^jU(y)|&\leq K\langle y\rangle^{d-j}\quad(j=0,1,2),\\
\|D^3U\|_\infty&\leq K,\qquad
\|D^2U\|_\infty=1,\\
|cy+U(y)|+|\det(cI+DU(y))|&\geq\delta
       \quad (|y|\leq R_b),\\
\operatorname{div}U&=0.
\end{split}
\tag{1}
\]
There is \(\varepsilon_0(c,K,\delta)>0\) such that every such pair satisfies
\[
\|(1-c)U+(cy+U)\cdot\nabla U+\nabla P\|_{L^\infty(\mathbb R^3)}
\geq\varepsilon_0.
\tag{2}
\]
The assertion is vacuous if the class is empty. No bound on \(P\), no normalization of its additive constant, and no condition at infinity on \(P\) are required.

**Proof.** Suppose there is a sequence satisfying (1) with momentum residual \(R_{m,n}\to0\) uniformly. The derivative bounds give, by Arzelà–Ascoli and a diagonal subsequence,
\[
U_n\longrightarrow U\quad\hbox{in }C^2_{\mathrm{loc}}.
\tag{3}
\]
The limit is \(C^2\), divergence free, and satisfies all three pointwise decay bounds. In particular \(U(y)\to0\).

Pressure compactness can be avoided. Set
\[
F_n=(1-c)U_n+DU_n(cy+U_n),\qquad
F=(1-c)U+DU(cy+U).
\]
Then \(F_n\to F\) in \(C^1_{\mathrm{loc}}\). Since
\[
\operatorname{curl}F_n=\operatorname{curl}R_{m,n}
\]
in distributions, \(\operatorname{curl}F=0\). The simply connectedness of \(\mathbb R^3\) gives a potential \(P_*\) with \(\nabla P_*=-F\). Since \(F\in C^1\), \(P_*\in C^2\). Thus \((U,P_*)\) solves the exact profile equations. Equivalently, for this uniform-residual argument, normalize \(P_n(0)=0\); the identity \(\nabla P_n=R_{m,n}-F_n\) gives convergence of their gradients on compact sets and reconstructs the same pressure.

For \(r=|y|\geq R_b>1\), the velocity envelope gives
\[
|U(y)|\leq Kr^d\leq\frac c2r,
\qquad
cy\cdot(cy+U(y))\geq\frac{c^2}{2}r^2.
\tag{4}
\]
Here \(1/(1-d)=c\). These inequalities hold for every candidate and the limit. All zeros of \(V=cy+U\) therefore lie strictly inside \(B_{R_b}\).

For \(|y|\geq R_N\),
\[
|D^2U_n(y)|\leq K|y|^{d-2}\leq\tfrac12.
\]
Consequently the global maximum \(1\) occurs in \(\overline B_{R_N}\). Uniform convergence of \(D^2U_n\) there yields
\[
\max_{\overline B_{R_N}}|D^2U|=1.
\tag{5}
\]
This is the precise reason normalization survives.

Convergence in \(C^1(\overline B_{R_b})\) passes the nondegeneracy inequality to the limit. At any zero \(z\),
\[
|\det DV(z)|\geq\delta>0.
\]
The inverse function theorem makes each zero isolated. The zero set is closed and contained in the compact ball \(\overline B_{R_b}\). If it were infinite, a convergent subsequence of distinct zeros would have a zero as its limit, contradicting isolation at that limit. Hence it is finite. L1 now gives \(U=0\), contrary to (5). This proves (2).

**Regularity and normalization.** The third derivative bound is one convenient way of making \(D^2U_n\) equicontinuous. It can be replaced by
\[
U\in C^{2,\alpha}_{\mathrm{loc}},\qquad
[D^2U]_{C^{0,\alpha}(B_R)}\leq M_R
\quad\hbox{for every }R,
\tag{6}
\]
with one fixed \(0<\alpha\leq1\) and fixed \(M_R\). The floor then also depends on these parameters. A global bound \([D^2U]_{C^{0,\alpha}}\leq K\) is a simple alternative; its floor may be denoted \(\varepsilon_0(c,K,\delta,\alpha)\). More generally, any prescribed local modulus of continuity tending to zero suffices. Membership in \(C^{2,\alpha}\) without a uniform seminorm bound does not suffice.

Uniform \(C^2\) bounds alone really are insufficient for this normalization. Choose a nonzero smooth, compactly supported, divergence-free \(W\), normalized by \(\|D^2W\|_\infty=1\), and define
\[
U_\ell(y)=\ell^2W(y/\ell),\qquad P_\ell=0,\qquad \ell\downarrow0.
\]
Then \(\|D^2U_\ell\|_\infty=1\), \(U_\ell\to0\) in \(C^1\), and a fixed sufficiently large \(K\) gives all the weighted bounds through order two. Moreover,
\[
R_{m,\ell}(y)
=\ell^2\big((1-c)W(x)+cx\cdot\nabla W(x)\big)
 +\ell^3(W\cdot\nabla W)(x),\qquad x=y/\ell,
\]
so \(\|R_{m,\ell}\|_\infty\to0\). For small \(\ell\), \(\|DU_\ell\|_{\mathrm{op},\infty}\leq c/2\), hence
\[
|\det(cI+DU_\ell)|\geq(c/2)^3
\]
everywhere. Thus even the proposed nondegeneracy condition survives, while \(\|D^3U_\ell\|_\infty\) diverges. This example disproves the floor with the uniform continuity assumption removed.

Exact equality in the normalization is not essential. A fixed lower bound
\[
\|D^2U\|_\infty\geq m>0
\tag{7}
\]
together with the stated upper bounds and tail localization gives the same contradiction. This is often easier to certify numerically. A fixed local nontriviality condition can replace both (7) and the second-derivative tail bound.

The scale gauge is valid: if \(a>0\),
\[
U_a(y)=aU(y/a),\qquad P_a(y)=a^2P(y/a),
\]
then
\[
\|D^2U_a\|_\infty=a^{-1}\|D^2U\|_\infty,\qquad
R_{m,a}(y)=aR_m(y/a).
\]
Take \(a=\|D^2U\|_\infty\) when it is nonzero. However, rescaling changes the weighted bounds, the third derivative bound, and the numerical nondegeneracy margin. A fixed \(K,\delta\) must be checked after normalization.

These polynomial envelopes are sufficient hypotheses, not minimal ones. The global compactness argument uses local \(C^2\) precompactness, a uniform sublinear velocity envelope inherited by the limit, a nontriviality condition that cannot escape to infinity, and a closed condition ensuring the limit has countably many stagnation points. The particular exponent \(d\) is not otherwise essential to that argument.

**Where nondegeneracy must hold.** The limit argument in the question is exactly right: evaluate the limiting inequality at the limiting zero. There is no need first to find nearby zeros of \(V_n\).

One may replace (iv) by the following condition with fixed \(\eta,\delta_1>0\):
\[
|V(y)|\leq\eta,\quad |y|\leq R_b
\quad\Longrightarrow\quad
|\det DV(y)|\geq\delta_1.
\tag{8}
\]
At a zero \(z\) of the limit, \(V_n(z)\to0\), so (8) applies at that same point for all sufficiently large \(n\). Condition (iv) implies (8) with \(\eta=\delta_1=\delta/2\); conversely, (8) implies (iv) with \(\delta=\min(\eta,\delta_1)\).

By contrast, a bound imposed only at the actual zeros of each \(V_n\) is not a closed condition. Locally, the fields
\[
V_n(x)=(n^{-1},cx_2,2cx_3)
\]
have divergence \(3c\) and no zeros, whereas their smooth limit vanishes on the line \(x_2=x_3=0\). Thus \(U_n=V_n-cx\) is divergence free, yet a new degenerate stagnation set appears in the limit. This local example identifies the failure of the proposed closedness argument; it is not asserted to be a counterexample satisfying all the global profile hypotheses. Uniform spatial neighborhoods of the zeros are useful only with an additional lower bound for \(|V|\) outside those neighborhoods, excluding unseen almost-zeros.

There is also a quantitative geometric consequence of (iv). Put \(M=c+K\). At a zero,
\[
\sigma_{\min}(DV)\geq\frac{\delta}{M^2}=:\mu_0.
\tag{9}
\]
Since \(\|D^2U\|_\infty=1\), Taylor's theorem for two distinct zeros \(z,w\) gives
\[
\mu_0|w-z|\leq\tfrac12|w-z|^2.
\]
Hence distinct zeros are at least \(2\mu_0\) apart, and disjoint balls of radius \(\mu_0\) give the crude count
\[
\#N_V\leq(1+R_b/\mu_0)^3.
\tag{10}
\]
These facts apply to the approximate fields as well. They quantify isolation, not the dynamics of their basins.

**Residual norms and divergence defects.** The global contradiction needs only
\[
R_{m,n}\longrightarrow0,\qquad
\operatorname{div}U_n\longrightarrow0
\quad\hbox{in distributions on every compact set}.
\tag{11}
\]
Indeed, the pressure-elimination argument still gives \(\operatorname{curl}F=0\), and the second convergence gives exact incompressibility of the \(C^2\) limit. Thus convergence to zero in \(L^p(B_R)\) for every fixed \(R\), \(1\leq p\leq\infty\), is more than sufficient. No derivative of the divergence defect is needed for this compactness argument.

For any fixed continuous weight \(w>0\), convergence of \(\|wR_{m,n}\|_\infty\) to zero implies local uniform convergence, since \(\inf_{B_R}w>0\). A positive floor therefore holds in that weighted norm, with dependence on \(w\). In particular, the requested quantity is
\[
\|\langle y\rangle^{-(2d-1)}R_m\|_\infty
=\|\langle y\rangle^{1-2d}R_m\|_\infty.
\tag{12}
\]
Because \(d<-1\), its weight is at least one, so the unweighted floor already implies the same lower bound in (12). However, the velocity envelopes alone do not ensure that (12) is finite. They bound the linear similarity terms only by \(O(\langle y\rangle^d)\); obtaining residual decay \(O(\langle y\rangle^{2d-1})\) requires additional cancellation. For \(0.4<c<0.5\), \(d\in(-3/2,-1)\), so the proposed weight grows with an exponent between \(3\) and \(4\).

A fixed, unspecified “small” divergence tolerance cannot simply be passed to an exactly divergence-free limit. The correct uniform statement is a joint floor. If \(\mathcal A\) denotes the class with all velocity, regularity, normalization, and stagnation assumptions, but with incompressibility omitted, there is \(b>0\) such that
\[
\|R_m\|_\infty+\|\operatorname{div}U\|_\infty\geq b
\quad (U\in\mathcal A).
\tag{13}
\]
Otherwise a sequence making both terms tend to zero contradicts (11). Consequently the restriction \(\|\operatorname{div}U\|_\infty\leq b/2\) gives the momentum floor \(b/2\). Thus a sufficiently small fixed tolerance exists, but its numerical value is not supplied by this proof. A \(C^1\) divergence tolerance is stronger than necessary.

**A strengthening to one fixed observation ball.** An arbitrary small measurement ball does not suffice: a normalized divergence-free bump can be placed outside it, with all bounds satisfied for a suitable fixed \(K\), and with zero residual inside it. Nevertheless, one can specify a sufficiently large ball explicitly:
\[
R_*=\max\{R_b,R_N\}+\sqrt{30K}+1.
\tag{14}
\]
For the class \(\mathcal A\) just defined, there is \(b_2(c,K,\delta)>0\) such that
\[
\|R_m\|_{L^2(B_{R_*})}
 +\|\operatorname{div}U\|_{L^2(B_{R_*})}
\geq b_2.
\tag{15}
\]
In particular, exact incompressibility gives an \(L^2(B_{R_*})\) momentum floor. Neither residual is required to be small outside this ball. The same statement holds with any fixed \(L^p\), \(1\leq p\leq\infty\), in place of \(L^2\), with a possibly different constant.

Here is the extra argument needed for (15); it is a localization of the proof of L1, rather than an application of L1's global statement. A hypothetical sequence violating (15) has a \(C^2_{\mathrm{loc}}\) limit \(U\), retains (5) and (iv), and solves the exact equations on \(D=B_{R_*}\) after pressure reconstruction on this simply connected ball.

Let \(Y(a,s)\) solve \(\partial_sY=V(Y)\), \(Y(a,0)=a\). The global velocity bounds give a complete \(C^1\) flow of diffeomorphisms. Every backward trajectory starting in \(D\) stays in \(D\), by (4), and eventually enters \(\overline B_{R_b}\). Define
\[
H(y)=\tfrac12|V(y)|^2+P(y)+\tfrac12c(c-1)|y|^2,
\]
using the reconstructed pressure on \(D\). Along the trajectory it satisfies
\[
\frac{d}{ds}H(Y(s))=-(1-2c)|V(Y(s))|^2.
\]
Its alpha-limit set is compact, connected, invariant, and contained in the finite stagnation set. Thus it is a single zero \(z\). If \(\lambda_{\max}(S(z))<1\), the Cauchy estimate from L1 gives
\[
|\Omega(a)|\leq
\exp\!\left(\int_0^t
 [\lambda_{\max}(S(Y(a,-\tau)))-1]\,d\tau\right)
|\Omega(Y(a,-t))|\longrightarrow0.
\tag{16}
\]
Boundedness of \(\Omega\) on the trapping ball and eventual strict negativity of the exponent's integrand justify this limit.

If \(\lambda_{\max}(S(z))\geq1\), the local algebra in L1 gives a contracting direction for \(DV(z)\). Specifically, if \(\Omega(z)\ne0\), then \(DV(z)\Omega(z)=(1+c)\Omega(z)\), and the other two eigenvalues have sum \(2c-1<0\); if \(\Omega(z)=0\), the matrix is symmetric and its smallest eigenvalue is at most \(c-1/2<0\). The local center-unstable manifold therefore has dimension at most two and contains every sufficiently local backward-trapped orbit. The backward basin of \(z\), restricted to \(D\), lies in a countable union of forward images of that manifold and has measure zero. This is precisely the local trapping property used in the audited L1 proof; that proof cites the discrete-time formulation [LSJR, Theorem 7], applied to the inverse-time map with generalized eigenspaces.

The finitely many exceptional basins have measure zero, and (16) handles every other point. Continuity gives \(\Omega=0\) throughout \(D\). Since \(\operatorname{div}U=0\) there, each component of \(U\) is harmonic on \(D\).

For completeness, the needed harmonic estimate has a direct constant. If a vector-valued harmonic \(u\) satisfies \(|u|\leq K\) on a neighborhood of \(\overline B_r(x)\), differentiating the ball's Poisson kernel twice at its center gives
\[
D^2u(x)=\frac{15}{r^2}
\fint_{\mathbb S^2}u(x+r\omega)\otimes
 \left(\omega\otimes\omega-\tfrac13I\right)\,d\sigma(\omega).
\]
The Hilbert–Schmidt norm of the parenthesized matrix is \(\sqrt{2/3}<1\). Hence
\[
|D^2u(x)|\leq\frac{15K}{r^2}.
\tag{17}
\]
For every \(x\in\overline B_{R_N}\), (14) allows \(r=\sqrt{30K}\) in (17), giving \(|D^2U(x)|\leq1/2\). This contradicts (5), proving (15). The radius in (14) is explicit; the positive number \(b_2\) is still not.

With the normalization \(\|D^2U\|_\infty\geq m>0\), the same proof uses
\[
R_N=(2K/m)^{1/(2-d)},\qquad
R_*=\max\{R_b,R_N\}+\sqrt{30K/m}+1.
\tag{18}
\]

**What is quantitative, and what remains unproved.** Write \(\kappa=1-2c>0\). Several parts of the proposed route have effective estimates:

1. From (4), a trajectory starting at radius \(r>R_b\) enters the trapping ball within backward time
   \[
   T_b\leq\frac2c\log(r/R_b).
   \tag{19}
   \]
   This bounds entry into the large ball, not entry into a neighborhood of the final equilibrium.

2. The Bernoulli identity for approximate solutions is exactly
   \[
   (1-2c)V+\Omega\times V+\nabla H=R_m,\qquad
   V\cdot\nabla H=-\kappa|V|^2+V\cdot R_m.
   \tag{20}
   \]
   It does not require incompressibility. If \(\|R_m\|_\infty\leq\varepsilon\), \(H\) decreases wherever \(|V|\geq2\varepsilon/\kappa\), apart from equality at a zero. But it need not decrease everywhere. On a trapped trajectory,
   \[
   \frac{\kappa}{2}\int_{-T}^0|V(Y(s))|^2\,ds
   \leq\operatorname{osc}_{B_{R_b}}H
       +\frac{\varepsilon^2T}{2\kappa}.
   \tag{21}
   \]
   The last term prevents taking \(T\to\infty\) as in the exact proof. Pressure is not an obstruction to bounding the oscillation here: on \(B_R\),
   \[
   |\nabla P|\leq\varepsilon+(1-c)K+K(cR+K),
   \]
   which bounds \(\operatorname{osc}_{B_R}P\) by \(2R\) times the right-hand side.

3. With \(q=\operatorname{div}U\), the correct curl equation is
   \[
   \Omega+V\cdot\nabla\Omega-G\Omega+q\Omega
   =\operatorname{curl}R_m.
   \tag{22}
   \]
   Thus the equation in the question is correct for \(q=0\). Put \(f=\operatorname{curl}R_m\), and let \(J(a,s)=D_aY(a,s)\). For \(q=0\), variation of constants gives
   \[
   \begin{split}
   \Omega(a)={}&e^{-(1+c)T}J(a,-T)^{-1}\Omega(Y(a,-T))\\
   &+\int_{-T}^0e^{(1+c)s}J(a,s)^{-1}f(Y(a,s))\,ds.
   \end{split}
   \tag{23}
   \]
   For \(q\ne0\), replace \(f\) in this formula by \(f-q\Omega\).

   Smallness of \(\|R_m\|_\infty\) alone does not bound its curl. In this class the velocity regularity repairs that difficulty locally: (22) bounds the Hölder seminorm of \(f\) directly from \(U\), without pressure bounds. For a smooth mollifier at scale \(h\), on an interior ball,
   \[
   \|f\|_\infty
   \leq C\big(\varepsilon/h+[f]_{C^{0,\alpha}}h^\alpha\big).
   \]
   Optimizing gives \(O(\varepsilon^{\alpha/(1+\alpha)})\), with controlled constants and a fixed surrounding ball. The \(C^3\) version gives a local \(O(\sqrt\varepsilon)\) bound. This addresses the differentiation loss, but not the accumulated integral in (23).

4. There is more spectral information at exact zeros than a generic determinant bound provides. At the “bad” zeros \(\lambda_{\max}(S)\geq1\), the argument above gives an eigenvalue of \(DV\) with real part at most \(-\kappa/2\). In fact, under \(|\det DV|\geq\delta\), every exact zero is hyperbolic, with
   \[
   |\operatorname{Re}\lambda|
   \geq\min\{\delta/(c+K)^2,\ \kappa/2\}
   \quad(\lambda\in\operatorname{spec}DV).
   \tag{24}
   \]
   To check this: when \(\Omega=0\), \(DV\) is symmetric; when \(\Omega\ne0\), one eigenvalue is \(1+c\), and any nonreal pair has real part \(-\kappa/2\). Every real eigenvalue has absolute value at least \(\delta/(c+K)^2\), by the determinant and the upper bound on the other two eigenvalue moduli. Thus absence of a local spectral gap at exact nondegenerate zeros is not the fundamental missing step.

What is missing is a uniform finite-time replacement for the basin argument: bounds for long residence near saddle equilibria, the measure of the relevant finite-time exceptional sets, their transport through the trapping region, and the resulting source accumulation in (23). The exact proof says a countable union of lower-dimensional images has measure zero. It supplies no bound on the measure of its neighborhoods, no effective time after which most trajectories have settled into useful regions, and no stability estimate of this type for approximate solutions. Even a hyperbolic saddle permits arbitrarily long residence for initial points sufficiently close to its invariant manifold. The last-exit time cannot be bounded for every initial point merely from (19).

A successful estimate would have to combine quantitative local invariant-manifold information, global residence/transition estimates, and an estimate converting small vorticity on the resulting large set into a contradiction with the velocity normalization. None of those combined estimates is established by L1 or by the compactness proof above. I therefore do not obtain an explicit \(\varepsilon_0(c,K,\delta)\). This is a limitation of the argument, not a proof that such a computable bound is impossible. Additional certified dynamical estimates could make a quantitative theorem feasible.

**Numerical diagnostics.** A finite grid by itself cannot certify these continuum assumptions. Apply the following checks to a specified smooth reconstruction, with interpolation/roundoff enclosures and an analytic or verified exterior extension. Use the same constants throughout the refinement sequence.

| Quantity | Required threshold or certification |
|---|---|
| Similarity exponent | Fix \(c<1/2\). If it varies, keep it in a fixed compact interval \([c_-,c_+]\subset(0,1/2)\); allowing \(c\to1/2\) is another escape from a uniform conclusion. |
| Velocity and tails | For \(j=0,1,2\), certify \(\sup_{\mathbb R^3}\langle y\rangle^{j-d}|D^jU(y)|\leq K\), including the exterior of the computational domain. This also certifies the trapping radius and localization radius above. |
| Compactness | Certify \(\|D^3U\|_\infty\leq K\), or a fixed \(C^{0,\alpha}\) modulus for \(D^2U\). For (15), a fixed local modulus on the observation ball suffices. Monitor this after every rescaling. |
| Nontriviality | Certify \(\|D^2U\|_\infty=1\), or use a fixed window such as \(1/2\leq\|D^2U\|_\infty\leq2\). The latter is sufficient by (7), with \(m=1/2\). |
| Stagnation margin | Certify \(\inf_{\overline B_{R_b}}(|V|+|\det DV|)\geq\delta>0\), or the uniform small-\(|V|\) condition (8). Listing the roots found by a solver does not exclude additional almost-zeros. |
| Incompressibility and momentum | Prefer a reconstruction with \(\operatorname{div}U=0\) identically. Otherwise certify that the divergence defect tends to zero, together with the momentum residual, in \(L^2(B_{R_*})\) or a stronger norm. An unknown nonzero divergence plateau is insufficient. |

For the stagnation diagnostic there is a simple rigorous grid margin. Suppose an \(h\)-net covers \(\overline B_{R_b}\), \(\|DV\|_{\mathrm{op}}\leq M=c+K\), and \(\|D^2U\|_\infty\leq L\). For
\[
g(y)=|V(y)|+|\det DV(y)|,
\]
the determinant derivative formula gives
\[
\operatorname{Lip}(g)\leq M+3M^2L.
\tag{25}
\]
If interval evaluation provides lower bounds \(\underline g_i\) at the net points, the threshold
\[
\min_i\underline g_i-(M+3M^2L)h\geq\delta
\tag{26}
\]
certifies (iv). Here \(L=1\) under exact normalization, and \(L=2\) in the suggested normalization window. Checking a lower singular-value bound on cells where \(|V|\) may be small is another valid implementation of (8).

The conclusion concerns residuals tending to zero with fixed certified bounds. Under exact incompressibility, all sufficiently late members of such a sequence must fail at least one of the velocity/regularity bounds, the fixed nontriviality condition, or the fixed stagnation margin. With approximate incompressibility, failure of the divergence defect to vanish is an additional possibility. If \(K_n\) increases without bound or \(\delta_n\) decreases to zero, individual membership in some varying \(F(K_n,\delta_n)\) gives no contradiction. A merely decreasing residual can also approach a positive floor. The theorem predicts neither a particular numerical tolerance nor a particular refinement level.

The accepted input is L1 and its proof in `THEORY_NOTES.md`, section 2, version dated 2026-10-23 06:50Z. The following external reference details are those recorded in the supplied audited notes; online retrieval was unavailable in this environment. For the underlying exact transport identities, the notes cite [CIV]: P. Constantin, M. Ignatova, and V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3, especially (3.22) and (3.29)–(3.31). L1 is being used as the supplied audited result; it is not identified with CIV's theorem, which the notes state has an additional outgoing hypothesis.

[LSJR] is J. D. Lee, M. Simchowitz, M. I. Jordan, and B. Recht, *Gradient Descent Only Converges to Minimizers*, PMLR 49 (2016), Theorem 7, cited in the notes as a restatement of Shub's local stable-center manifold theorem.

Exact symbolic algebra additionally checked (20), (22), \(G\Omega=S\Omega\), and the Poisson-kernel Hessian coefficient \(15\) in (17). The compactness and dynamical arguments remain informal mathematical proofs.

The requested Claude Opus 5.5 collaboration could not be performed: the configured Python/Bedrock client failed to obtain credentials. No response from that model was obtained or substituted. This report is an independent mathematical check, not a machine-checked formal proof.
