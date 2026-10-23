**Adversarial referee report on Theorem L2**

**Verdict: PROOF CORRECT WITH REPAIRABLE GAPS.** The repairs are local proof-writing details, supplied below: specify an adapted norm in the null-graph estimate, and supply the box dimensions and first-exit argument in the alternative dynamical capture proof. The primary Bernoulli-gradient capture proof works under exactly the stated \(C^2\) hypothesis. I found no counterexample and no missing assumption on the stagnation set. With the explicit justifications below, the theorem is proved.

There is a version qualification. The file at the requested path identifies itself as v3, **2026-10-23 07:14Z**, rather than 07:20Z. It changed during this audit. The later text explicitly repairs the topology chart choice, chooses \(q\) near \(p\) to preserve the saddle spectrum, and expands the parenthetical claim about rank-two zeros outside \(E\). The classifications below apply to that later text, whose SHA-256 when inspected was
`48c76438fe5995496033c69a396ec089f0dd2aafac41d2b1d18435a6f1ab62b0`.
I also identify the omissions in the earlier text. I did not modify the source.

This is an independent mathematical verification, not machine-checked formalization or a novelty assessment. A Python/Bedrock consultation requesting Claude Opus 5.5 failed at credential retrieval for the configured `cline-profile`; no response from that model was obtained, and no other model was silently substituted. External literature access failed at DNS resolution. Accordingly, the proof below does not rely on the notes' previous referee endorsements, their external theorem citations, or their numerical existence claim at \(c=1/2\).

**Statement and notation.** Assume \(0<c<1/2\), \(U\in C^2(\mathbb R^3;\mathbb R^3)\), and a pointwise pressure gradient satisfying
\[
 (1-c)U+(cy+U)\cdot\nabla U+\nabla P=0,\qquad
 \operatorname{div}U=0,\qquad U(y)=o(|y|).
\]
Here the last condition is uniform outside sufficiently large balls, as usual for little-oh at infinity. Set
\[
 V=cy+U,\quad G=DU,\quad A=DV=cI+G,\quad
 S=\tfrac12(G+G^T),\quad \Omega=\nabla\times U,\quad
 \kappa=1-2c>0,
\]
\[
 N=\{V=0\},\qquad E=\{p\in N:\lambda_{\max}(S(p))\ge1\}.
\]
Let \(\Phi_s\) be the flow of \(V\), \(x(t)=\Phi_{-t}(a)\), and \(K=\alpha(a)\) its backward limit set.

The theorem concludes that \(U\) is constant. A nonzero constant is allowed: for \(U=b\), the pressure is
\[
 P(y)=-(1-c)b\cdot y+P_0.
\]
Only when \(U\to0\) must both \(U=0\) and \(P=P_0\).

**Classification of the steps.**

| Location | Classification | Finding |
|---|---|---|
| Section 1, hypotheses and L1' | CORRECT | The uncountable-set assertion in L1' follows from compactness, not countability. |
| Section 2, Step 0 | CORRECT | \(C^2\) gives the required flow, pressure regularity, and classical curl equation. |
| Section 2, Step 1 | CORRECT | Sublinearity traps every backward orbit and makes \(N\) compact. |
| Section 2, Step 2 | CORRECT | Invariance and the Lyapunov identity put every alpha-limit set in \(N\), including uncountable ones. |
| Section 2, Step 3 | CORRECT | Matrix order, transpose estimate, exponential factor, and time reversal are correct. |
| Section 2, Step 4 | CORRECT | Compactness gives a uniform strict strain gap whenever \(K\cap E=\varnothing\). |
| Section 2, Step 5 | CORRECT | Each exceptional equilibrium has a contracting direction for \(V\). |
| Section 7.1 | CORRECT | \(P,H\in C^2\), \(B\in C^1\), and the gradient and rank identities are valid. |
| Section 7.2 | CORRECT | Rank is at least two at \(E\), with both an expanding and a contracting direction. |
| Section 7.3 | CORRECT in the later text | Choosing \(r\ne p\) first and shrinking the chart resolves the earlier omission. |
| Section 7.4, primary proof | CORRECT | The gradient inequality holds on a full ball; its constant level is the correct \(h(a)\); the length estimate gives capture. |
| Section 7.4, alternative proof | GAP, repairable | The last trapping sentence needs a thin box, a transverse-boundary separation, and a first-exit argument. These are supplied below. |
| Section 7.4, rank-one parenthesis | CORRECT | In fact the primary capture proof already handles every rank-two zero. |
| Section 7.5 | GAP in the literal norm bookkeeping, repairable | Spectral projections need not be orthogonal. Use a direct-sum norm, or retain projection constants. The graph and nullity conclusions are correct. |
| Section 7.6 | CORRECT | The trapping set contains all backward orbits staying in \(B_{p_i}\), including those converging to an equilibrium other than \(p_i\). |
| Section 7.7 | CORRECT | An open null set is empty; the harmonic gradient estimate gives constancy from sublinearity. |

No step essential to the theorem is false. The two remaining repairs do not strengthen its hypotheses. The alternative capture proof is redundant; omitting it entirely would leave a complete proof once the norm convention in 7.5 is made explicit.

**Step 0: regularity, completeness, and curl — CORRECT.** Continuity and sublinearity give a global linear growth bound \(|V(y)|\le C(1+|y|)\). Local existence and uniqueness follow from \(V\in C^1\). Gronwall bounds on finite time intervals, for both \(V\) and \(-V\), preclude finite-time escape. Thus the flow exists for all real times. Differentiating the ODE with respect to initial data twice is legitimate on each compact time interval because \(V\in C^2\). The inverse of \(\Phi_s\) is \(\Phi_{-s}\), so these maps are \(C^2\) diffeomorphisms. No global bound on \(DU\) or \(D^2U\) is required.

The equation gives
\[
 \nabla P=-(1-c)U-GV\in C^1.
\]
Consequently \(P\in C^2\); even if “pointwise” initially means only that the partial derivatives exist, their displayed continuous \(C^1\) representatives give this conclusion. Hence \(\nabla\times\nabla P=0\).

The classical identities needed for the curl use at most two derivatives of \(U\):
\[
 \nabla\times[(y\cdot\nabla)U]=\Omega+(y\cdot\nabla)\Omega,
\]
\[
 \nabla\times[(U\cdot\nabla)U]=(U\cdot\nabla)\Omega-(\Omega\cdot\nabla)U.
\]
They give
\[
 \Omega+(V\cdot\nabla)\Omega=G\Omega=S\Omega. \tag{1}
\]
For the last equality, the skew part of \(G\) is the map \(v\mapsto\Omega\times v/2\), which annihilates \(\Omega\). Here \(\Omega\in C^1\), exactly enough for (1).

**Step 1: backward trapping — CORRECT.** Choose \(R_b>0\) with \(|U(y)|\le c|y|/2\) whenever \(|y|\ge R_b\). Then
\[
 V(y)\cdot y\ge \frac c2|y|^2.
\]
For the backward trajectory, while \(|x|\ge R_b\),
\[
 \frac d{dt}|x(t)|^2=-2V(x(t))\cdot x(t)\le-c|x(t)|^2.
\]
If a trajectory starting outside never entered the ball, this exponential estimate would eventually contradict \(|x(t)|\ge R_b\). On the boundary the vector field \(-V\) points strictly inward, so the closed ball is positively invariant for the backward dynamics.

The tails of each backward trajectory therefore have compact closure. Their nested closures are connected because each tail is the continuous image of an interval. Their intersection \(K\) is nonempty, compact and connected. For \(z=\lim_jx(t_j)\), \(t_j\to\infty\), continuity of the flow gives
\[
 \Phi_s(z)=\lim_jx(t_j-s)\in K
\]
for every fixed \(s\in\mathbb R\); using \(-s\) gives full invariance. Every zero of \(V\) lies inside the trapping ball, so \(N\) is compact.

We will also use this elementary consequence: the backward orbit is eventually in **every** open neighborhood of \(K\). Otherwise a sequence of late points outside that neighborhood would have a subsequential limit in \(K\), a contradiction.

**Step 2: alpha-limit sets consist of equilibria — CORRECT.** Define
\[
 H=\frac12|V|^2+P+\frac12c(c-1)|y|^2.
\]
Using \(U=V-cy\) in the equation and
\[
 (V\cdot\nabla)V=\nabla\frac{|V|^2}{2}+\Omega\times V
\]
gives
\[
 \nabla H=-\kappa V-\Omega\times V,\qquad
 V\cdot\nabla H=-\kappa|V|^2. \tag{2}
\]
Thus \(H(x(t))\) is nondecreasing, bounded for large \(t\), and has a finite limit \(h=h(a)\). Every point of \(K\) has \(H=h\). Since \(K\) is invariant, \(H(\Phi_s(z))=h\) for every \(z\in K\) and every \(s\). Differentiating at \(s=0\) in (2) gives \(V(z)=0\). Hence \(K\subset N\).

Nothing here uses countability or local connectedness. Only the later inference “a connected countable compact set is a singleton” uses countability. That inference is also correct: if a connected subset of Euclidean space contains two distinct points, a linear functional separating them maps it onto a set containing a nondegenerate interval, which is uncountable.

**Step 3: the Cauchy formula — CORRECT.** Write \(J(a,s)=D_a\Phi_s(a)\). Then
\[
 \partial_sJ=A(\Phi_s(a))J.
\]
By (1), \(Z(s)=e^{(1+c)s}\Omega(\Phi_s(a))\) satisfies the same linear ODE, with \(Z(0)=\Omega(a)\). Therefore
\[
 \Omega(a)=e^{(1+c)s}J(a,s)^{-1}\Omega(\Phi_s(a)). \tag{3}
\]
To check the potentially troublesome matrix order, put \(Q(t)=J(a,-t)^{-1}\). Direct differentiation gives \(Q'=QA(x(t))\), not \(AQ\). Hence
\[
 (Q^T\eta)'=A(x(t))^TQ^T\eta,
\]
and
\[
 \frac d{dt}|Q^T\eta|^2
 \le2\bigl(c+\lambda_{\max}(S(x(t)))\bigr)|Q^T\eta|^2.
\]
Taking operator norms and using (3) at \(s=-t\) yields exactly
\[
 |\Omega(a)|\le
 \exp\left(\int_0^t[\lambda_{\max}(S(x(\tau)))-1]\,d\tau\right)
 |\Omega(x(t))|. \tag{4}
\]
The cancellation of \(c\) in this exponent is correct.

**Step 4 and Corollary L1' — CORRECT for arbitrary \(N\).** If \(K\cap E=\varnothing\), then the continuous function \(\lambda_{\max}(S)\) is strictly less than one everywhere on the compact set \(K\). Its maximum there is therefore strictly less than one. There exist \(\eta>0\) and an open neighborhood \(O\supset K\) such that \(\lambda_{\max}(S)\le1-\eta\) on \(O\).

The orbit is eventually in \(O\), by the property proved after Step 1. Vorticity is bounded on its trapped tail. The finite initial part of the exponent in (4) contributes only a constant, so \(|\Omega(a)|\le C e^{-\eta t}\), and \(\Omega(a)=0\).

At an equilibrium, (1) reduces to \(G(p)\Omega(p)=S(p)\Omega(p)=\Omega(p)\). Thus a vortical equilibrium belongs to \(E\). The second assertion of L1', that \(DV\) has a contracting direction at every point of \(E\), follows from the next calculation.

**7.1: Bernoulli gradient and its regularity — CORRECT.** Both \(V\) and \(P\) are \(C^2\), so \(H\in C^2\). The field
\[
 B=\kappa I+C_\Omega,\qquad C_\Omega v=\Omega\times v
\]
is \(C^1\). For every vector \(v\),
\[
 |Bv|^2=\kappa^2|v|^2+|\Omega\times v|^2.
\]
Consequently \(B\) is invertible and
\[
 \kappa|V|\le|\nabla H|
 \le\sqrt{\kappa^2+|\Omega|^2}\,|V|. \tag{5}
\]
In particular the critical set of \(H\) is exactly \(N\).

Differentiating \(\nabla H=-BV\) at a zero of \(V\) removes the term involving \(DB\):
\[
 D^2H(p)=-B(p)A(p). \tag{6}
\]
Since \(B(p)\) is invertible, the kernels and ranks of \(D^2H(p)\) and \(A(p)\) agree. This differentiates only \(C^1\) quantities once; it does not require \(D^3U\), \(D^3P\), or \(D^3H\).

**7.2 and Step 5: rank and spectrum at \(E\) — CORRECT.** We have \(\operatorname{tr}A=3c\).

If \(\Omega(p)\ne0\), then \(A(p)\Omega(p)=(1+c)\Omega(p)\). The other two eigenvalues, counted algebraically over \(\mathbb C\), have sum \(2c-1<0\). At least one has negative real part, and they cannot both be zero. The zero eigenvalue thus has algebraic multiplicity at most one, implying \(\operatorname{rank}A\ge2\).

If \(\Omega(p)=0\), then \(G=S\) and \(A=cI+S\) is symmetric. Its largest eigenvalue is at least \(1+c>0\). Since \(\operatorname{tr}S=0\),
\[
 \lambda_{\min}(S)\le-\tfrac12\lambda_{\max}(S)\le-\tfrac12,
\]
so \(A\) has an eigenvalue at most \(c-1/2<0\). Again its rank is at least two.

Rank three makes \(p\) an isolated zero by the inverse function theorem. At rank two, select two independent rows of \(DV(p)\). The implicit function theorem applied to the corresponding two components of \(V\) produces a \(C^2\) embedded arc \(\gamma\) containing all nearby zeros. A nonzero \(2\times2\) minor remains nonzero after shrinking the neighborhood, so \(\operatorname{rank}DV\ge2\) throughout it. The zero set is relatively closed in this local arc; no claim that it already fills the arc is justified or needed at this stage.

**7.3: topology — CORRECT after the explicit chart choice now in the source.** Let \(p\in K\cap E\) and suppose \(K\ne\{p\}\). A connected set with more than one point cannot have an isolated point: that singleton would be both relatively open and relatively closed. Thus \(p\) cannot be an isolated zero and has rank two.

Choose \(r\in K\setminus\{p\}\) **first**, and then choose a straightening chart around \(p\), with closure avoiding \(r\), inside the neighborhood where all zeros lie on \(\gamma\). Write its coordinates as \((\xi,z)\), with \(\gamma=\{z=0\}\) and \(p=(0,0)\).

If neither one-sided interval starting at zero is wholly in \(K\), there are arbitrarily small \(\xi_-<0<\xi_+\) for which \(\gamma(\xi_-)\) and \(\gamma(\xi_+)\) are not in \(K\). Take a thin open coordinate cylinder
\[
 D=\Psi((\xi_-,\xi_+)\times D_\rho)
\]
with closure inside the chart. Its lateral boundary misses \(N\), because \(N\) lies on the central axis. Each cap meets \(N\) at most at its central point, which was selected outside \(K\). Since \(K\subset N\), this proves \(K\cap\partial D=\varnothing\).

Now \(K\cap D\) is relatively open in \(K\), and is relatively closed because \(K\) has no point on \(\partial D\). It contains \(p\) and misses \(r\). This contradicts connectedness. Hence \(K\) contains a nondegenerate one-sided subarc with endpoint \(p\); shortening it gives a compact arc \(J\).

This proof allows arbitrary exits from and re-entries into the original chart. It uses connectedness of the whole \(K\), not connectedness of its intersection with a chart. If \(K\) originally lay wholly in a larger chart, choosing \(r\) first and shrinking the chart still works. Alternatively, in that special case a connected subset of the arc is an interval. A two-sided arc through \(p\) is unnecessary: an interior point of the one-sided \(J\) is sufficient.

The earlier wording “fix \(r\) outside the chart” omitted the shrinking justification. That was repairable, not a counterexample to the lemma.

**7.4, primary capture proof — CORRECT on a full ball.** Choose \(q\) in the relative interior of \(J\). Shrink a neighborhood of \(q\) so that its portion of \(\gamma\) is contained in \(J\). Within that neighborhood \(N\) is precisely this arc: every zero lies on \(\gamma\), and all points of this portion of \(\gamma\) belong to \(J\subset K\subset N\).

On the arc, differentiating \(V=0\) along its tangent gives \(A(y)T_yJ=0\). Rank is at least two nearby and at most two on the arc, so
\[
 \operatorname{rank}A(y)=2,\qquad \ker A(y)=T_yJ.
\]
Also \(H(y)=h(a)\) on this entire local arc, because it is contained in \(K\). This is the required constant \(h\); no assertion that unrelated nearby critical components have the same value is used.

A \(C^2\) embedded arc has a sufficiently small tubular neighborhood with unique nearest-point projection onto an interior portion of the arc. For completeness, this follows by expressing the arc as a \(C^2\) graph and solving the orthogonality equation
\[
 (y-\gamma(\xi))\cdot\gamma'(\xi)=0
\]
near \(y=q\): its derivative in \(\xi\) at an on-arc point is \(-|\gamma'(\xi)|^2\ne0\). The implicit function theorem gives a \(C^1\) projection, and shrinking the neighborhood excludes other pieces and endpoints. We use only its existence and orthogonality, not second derivatives of the projection.

Put \(n=y-\pi(y)\). On a compact shorter arc, injectivity of \(A(\pi)\) on the normal plane gives a uniform number \(2m>0\) such that
\[
 |A(\pi)n|\ge2m|n|,\qquad n\perp T_\pi J.
\]
Indeed the unit normal bundle over that compact arc is compact, and the continuous function \(|A(\pi)n|\) has no zero there. Boundedness of \(D^2V\) on a compact neighborhood gives the uniform Taylor estimate
\[
 V(y)=A(\pi(y))n+R(y),\qquad |R(y)|\le C_V|n|^2.
\]
After shrinking once more, \(|V(y)|\ge m|n|\).

Taylor's integral formula for the \(C^2\) function \(H\), using \(\nabla H(\pi)=0\) and \(H(\pi)=h\), gives
\[
 |H(y)-h|\le C_H|n|^2.
\]
Here boundedness of \(D^2H\) suffices; no Lipschitz Hessian or third derivative is being assumed. Combining these estimates with (5) yields
\[
 |H(y)-h|^{1/2}\le
 \frac{\sqrt{C_H}}{\kappa m}|\nabla H(y)|,\qquad
 |\nabla H(y)|\le M|V(y)|. \tag{7}
\]
All estimates hold for **every point of a sufficiently small closed ball**
\(\overline B_{r_0}(q)\), chosen inside the tubular neighborhood. They are not estimates only on \(J\), only along the trajectory, or only on one side of the critical level. The absolute value in (7) permits either sign of \(H-h\), so an indefinite transverse Hessian causes no problem.

Along the actual backward orbit, monotonicity gives
\[
 e(t)=h-H(x(t))\ge0,\quad e(t)\downarrow0,\quad
 e'(t)=-\kappa|V(x(t))|^2=-\kappa|x'(t)|^2.
\]
Where \(e>0\) and \(x(t)\in\overline B_{r_0}(q)\), (7) implies
\[
 -\frac d{dt}\sqrt{e(t)}
 =\frac{\kappa|x'(t)|^2}{2\sqrt{e(t)}}
 \ge\frac{\kappa}{2C_0M}|x'(t)|.
\]
Thus any such segment has length at most
\[
 L\bigl(\sqrt{e(t_0)}-\sqrt{e(t_1)}\bigr),\qquad
 L=\frac{2C_0M}{\kappa}. \tag{8}
\]
Choose a sufficiently late return near \(q\) with
\[
 |x(t_0)-q|<r_0/4,\qquad L\sqrt{e(t_0)}<r_0/4.
\]
Both inequalities hold simultaneously along a sequence returning to \(q\), because \(e(t)\to0\).

If there were a first exit from \(B_{r_0/2}(q)\), the orbit up to that exit would lie in \(\overline B_{r_0}(q)\), so (8) would bound its length by less than \(r_0/4\). But the distance from the starting point to that exit is greater than \(r_0/4\). This contradiction proves that no exit occurs. Taking \(t_1\to\infty\) in (8) gives finite total length, hence convergence. Its limit is \(q\), since \(q\) is still a subsequential limit of the same tail. Thus \(K=\{q\}\), contradicting \(J\subset K\).

If \(e\) reaches zero at finite time, monotonicity and the definition of \(h\) force \(H\) to remain constant on the future backward orbit; then \(e'=-\kappa|V|^2\) gives an equilibrium. Uniqueness gives the same contradiction.

This proves that every \(a\) with \(K\cap E\ne\varnothing\) has \(K=\{p\}\) for some \(p\in E\).

**7.4, alternative dynamical proof — repairable omitted trapping detail.** The later source correctly chooses \(q\) close enough to \(p\) that \(A(q)\) has three simple real eigenvalues
\[
 \lambda_s<0,\qquad0,\qquad\lambda_u>0.
\]
At the rank-two point \(p\) these eigenvalues are distinct. Continuity of simple real eigenvalues, and the zero tangent eigenvalue along \(J\), preserve this pattern nearby. It is unnecessary and unjustified to assume \(q\in E\); the later text no longer does so.

A \(C^2\) coordinate change straightening \(J\) transforms a \(C^2\) vector field into at least a \(C^1\) vector field. The loss of one derivative is harmless. Choosing the transverse coordinate vectors to be eigenvectors at \(q\) gives, in forward \(V\)-time,
\[
 \dot s=\lambda_s s+f_s,\quad
 \dot u=\lambda_u u+f_u,\quad
 \dot z=g,
\]
\[
 |f_s|+|f_u|\le\varepsilon(|s|+|u|),\qquad
 |g|\le K_0(|s|+|u|).
\]
The field vanishes identically on the axis \(s=u=0\). Uniform continuity of its derivative therefore makes the displayed transverse remainder small throughout a sufficiently small box. No term depending only on \(z\) remains.

For a trajectory segment in a box with \(|s|,|u|\le\eta\), integrate the stable equation from its initial endpoint and the unstable equation from its terminal endpoint. With \(\beta=\min(-\lambda_s,\lambda_u)\), this yields
\[
 \int(|s|+|u|)\,dt
 \le\frac{2\eta}{\beta}
   +\frac{2\varepsilon}{\beta}\int(|s|+|u|)\,dt,
\]
and hence the stated \(2\eta/(\beta-2\varepsilon)\) bound. For backward dynamics, interchange the stable and unstable roles; the identical integral bound applies. Mixing the eigenvalues of \(V\) with forward time for \(-V\) without this interchange would be a sign error, but it does not change the estimate after correction.

To complete the omitted trapping argument, take a box
\[
 |s|,|u|<\eta,\qquad |z|<\delta
\]
with closure inside the coordinate neighborhood. Choose \(\varepsilon<\beta/2\) and then \(\eta\) sufficiently small relative to \(\delta\) that
\[
 \frac{2K_0\eta}{\beta-2\varepsilon}<\delta/2.
\]
The compact transverse boundary \(\max(|s|,|u|)=\eta\) has positive distance from \(N\), since the only zeros in the closed box lie on its axis. Because \(\operatorname{dist}(x(t),N)\to0\), sufficiently late points cannot lie on this transverse boundary. A sufficiently late return near \(q\), with \(|z|<\delta/4\), cannot first leave through a \(z\)-face either: the integral bound makes its total axial drift less than \(\delta/2\). It is therefore trapped.

Apply the same integral estimate to arbitrarily long trapped segments. The transformed speed is bounded by a constant times \(|s|+|u|\), so the entire tail has finite length and converges to \(q\). This completes the alternative proof, without needing the informal phrase “letting the box shrink.”

**7.4, extra rank-one assertion — CORRECT, and not needed.** The primary capture argument did not use a saddle spectrum at \(q\); it used only a rank-two equilibrium arc, (5), and \(H=h\) on that arc. Thus it also rules out a nonsingleton \(K\) containing any rank-two zero outside \(E\). Rank-three zeros are isolated and cannot belong to a nonsingleton connected \(K\).

At every remaining point \(p\in K\), the rank must be one, since \(\operatorname{tr}A=3c>0\) rules out rank zero. A rank-one matrix of nonzero trace has eigenvalues \(3c,0,0\). If \(\Omega(p)\ne0\), (1) would give an eigenvalue \(1+c\), impossible because \(1+c\ne3c\) in the stated range. Hence \(\Omega(p)=0\), \(A\) is symmetric, and \(S\) has eigenvalues \(2c,-c,-c\). Its largest eigenvalue is \(2c<1\). This confirms the parenthesis without imposing a stratification on \(N\).

**7.5: local null graph — valid after explicit norm bookkeeping.** Translate \(p\) to zero and use \(X=-V\). Write
\[
 X(z)=Lz+R(z),\qquad L=-A(p),\quad R(0)=0,\quad DR(0)=0.
\]
There is an unstable spectral subspace for \(L\), because \(A(p)\) has a negative-real-part eigenvalue. Let
\[
 \mathbb R^3=E^{cs}\oplus E^u
\]
be the real direct sum of the **generalized** eigenspaces for real parts \(\le0\) and \(>0\), respectively. In particular \(d=\dim E^{cs}\le2\). Ordinary eigenspaces would not suffice in the presence of Jordan blocks.

Choose Euclidean norms separately on these subspaces and use the ambient norm
\[
 \|z\|_*=\|z_{cs}\|+\|z_u\|.
\]
Both spectral projections then have norm at most one. This supplies the norm convention missing from the literal displayed inequality \(|w_u(0)|\le D_*\) in the notes. In the original Euclidean norm those projections may be oblique, so projection constants must instead be retained. Either choice gives the same result.

Let \(\beta>0\) be strictly smaller than the smallest positive real part of \(L_u\), set \(\varepsilon=\beta/4\), \(\eta=\beta/2\), and choose \(M_0\ge1\) so that
\[
 \|e^{-tL_u}\|\le M_0e^{-\beta t},\qquad
 \|e^{tL_{cs}}\|\le M_0e^{\varepsilon t}\quad(t\ge0).
\]
Jordan blocks contribute polynomial factors in \(t\). The strict spectral margins absorb those factors into these exponentials. In particular zero-real-part eigenvalues and nontrivial center Jordan blocks are permitted; hyperbolicity of the equilibrium is not assumed.

On a sufficiently small bounded convex neighborhood \(B_p\), the map \(R\) has Lipschitz constant \(\ell\), as small as desired, because \(DR(0)=0\). Use a small ball for \(\|\cdot\|_*\), or any suitable convex neighborhood. Consider two forward \(X\)-orbits \(z,\widetilde z\) staying in \(B_p\) for all \(t\ge0\). Put
\[
 w=z-\widetilde z,\quad r=R(z)-R(\widetilde z),\quad
 D_*=\sup_{t\ge0}e^{-\eta t}\|w(t)\|_*.
\]
This supremum is finite because both orbits are bounded, and \(\|r(t)\|_*\le\ell\|w(t)\|_*\).

Variation of constants gives
\[
 w_{cs}(t)=e^{tL_{cs}}w_{cs}(0)
 +\int_0^t e^{(t-s)L_{cs}}r_{cs}(s)\,ds.
\]
For the unstable part, first write the terminal formula at a finite \(T>t\):
\[
 w_u(t)=e^{(t-T)L_u}w_u(T)
 -\int_t^T e^{(t-s)L_u}r_u(s)\,ds.
\]
The terminal term tends to zero as \(T\to\infty\), by boundedness and the unstable semigroup estimate. This justifies the improper formula used in the notes.

Multiplying by \(e^{-\eta t}\), bounding both integrals, and taking a supremum yields
\[
 D_*\le M_0\|w_{cs}(0)\|
 +M_0\ell\left(\frac1{\eta-\varepsilon}
                +\frac1{\beta-\eta}\right)D_*.
\]
Choose \(\ell\) so the coefficient of \(D_*\) on the right is at most \(1/2\). Then
\[
 \|w(0)\|_*\le D_*\le2M_0\|w_{cs}(0)\|. \tag{9}
\]
Consequently the projection to \(E^{cs}\) is injective on
\[
 T_p=\{b:\Phi_s(b)\in B_p\text{ for every }s\le0\},
\]
and its inverse is Lipschitz. Equivalently, \(T_p\) is the graph of a Lipschitz map from a subset \(D\subset E^{cs}\) into \(E^u\).

No extension of that map to all of \(E^{cs}\), and no smooth manifold theorem, is needed. Here is a direct nullity proof even if \(D\) has not been shown measurable. Because \(T_p\) is bounded, so is \(D\). Partition a bounding \(d\)-dimensional cube into cubes of side \(\delta\). There are \(O(\delta^{-d})\) of them. The graph above each cube that meets \(D\) has diameter \(O(\delta)\), by (9), so it is covered by a three-dimensional ball of volume \(O(\delta^3)\). The total covering volume is \(O(\delta^{3-d})\to0\), since \(d\le2\). Thus \(T_p\) has Lebesgue outer measure zero and is a Lebesgue null set.

This proves the trapping property required also in the countable-case Step 6. It does not merely construct a manifold of orbits converging to the particular center point \(p\); it controls **all bounded backward orbits in the neighborhood**, which is essential for 7.6.

**7.6: finite cover — CORRECT.** Continuity of \(S\) makes \(E\) a closed subset of compact \(N\), hence compact. Choose small open \(U_p\) with \(\overline U_p\subset B_p\), and extract a finite subcover \(U_{p_1},\ldots,U_{p_k}\). The empty-\(E\) case is immediate.

For \(a\in W=\{a:\alpha(a)\cap E\ne\varnothing\}\), capture gives \(x(t)\to p\in E\). Choose \(i\) with \(p\in U_{p_i}\). Since \(p\) is an interior point of \(B_{p_i}\), some ball about \(p\) lies in \(B_{p_i}\). Convergence means that **every** sufficiently late backward point lies in that ball. Choose an integer \(n\ge0\) after this time. For \(b=\Phi_{-n}(a)\) and every \(s\le0\),
\[
 \Phi_s(b)=\Phi_{s-n}(a)\in B_{p_i}.
\]
Therefore \(b\in T_{p_i}\), and
\[
 W\subset\bigcup_{i=1}^k\bigcup_{n=0}^{\infty}\Phi_n(T_{p_i}). \tag{10}
\]
The limit \(p\) need not equal \(p_i\). The definition of \(T_{p_i}\) imposes no such requirement.

As written, \(T_{p_i}\) should indeed use \(B_{p_i}\), because membership in that set is what the displayed argument establishes. It would also be valid to define a smaller trapping set using \(U_{p_i}\): convergence to \(p\in U_{p_i}\) gives a tail in \(U_{p_i}\), and that trapping set is a subset of the null set defined using \(B_{p_i}\). There is no fundamental requirement to use one name rather than the other; the neighborhoods in the definition and the membership argument must agree.

Every \(C^1\) map on \(\mathbb R^3\) is Lipschitz on each compact convex ball, because its derivative is bounded there. A countable covering by such balls shows that it maps null sets to null sets. Thus each \(\Phi_n(T_{p_i})\) is null, and so is their countable union. The argument proves outer nullity of \(W\), so no separate measurability theorem for the alpha-limit assignment is required.

There is no uncountable union of individual basins in (10). This is exactly why an arbitrary compact exceptional set is allowed.

**7.7: vorticity elimination and Liouville — CORRECT.** By Step 4,
\[
 Z=\{a:\Omega(a)\ne0\}\subset W.
\]
Continuity of \(\Omega\) makes \(Z\) open. A nonempty open subset of \(\mathbb R^3\) contains a ball of positive measure, whereas \(W\) is null. Hence \(Z=\varnothing\).

The classical identity
\[
 \Delta U=\nabla(\operatorname{div}U)-\nabla\times(\nabla\times U)
\]
now gives \(\Delta U=0\) componentwise. For a scalar harmonic component \(u\), the interior estimate
\[
 |\nabla u(x_0)|\le\frac3R\sup_{B_R(x_0)}|u|
\]
follows, for example, by differentiating the ball mean-value formula and applying the divergence theorem. Sublinearity implies the supremum on the right is \(o(R)\) for fixed \(x_0\): given \(\epsilon>0\), bound \(u\) on a fixed compact ball and use \(|u(y)|\le\epsilon|y|\) outside it. Dividing the resulting bound by \(R\) and then letting \(\epsilon\to0\) proves \(\nabla u(x_0)=0\). Thus \(U\) is constant everywhere.

**Tests against exact solution families.** These checks are analytic substitutions, not a numerical search. The rotating-strain, stagnation-line, and rank-one affine examples were additionally checked by exact symbolic substitution: all three have zero momentum residual, zero divergence, and satisfy the Bernoulli identity. The computation was local, single-threaded, and memory-limited. These checks cannot enumerate all possible solutions; their purpose is to look for explicit counterexamples and identify which assumptions exclude familiar families.

1. **Constant and affine profiles.** For \(U=My+b\), the necessary and sufficient conditions are
   \[
   \operatorname{tr}M=0,\qquad M+M^2\text{ symmetric},
   \]
   with pressure
   \[
   P=-\tfrac12y^T(M+M^2)y-\bigl(((1-c)I+M)b\bigr)\cdot y+P_0.
   \]
   This follows by direct substitution; the coefficient of \(y\) is \(M+M^2\), independent of \(c\). Every nonzero \(M\) violates sublinearity: select \(v\) with \(Mv\ne0\) and take \(y=tv\). Constants satisfy all the hypotheses and match the conclusion.

   In particular, for \(a\ne0\),
   \[
   U=(-x/2-ay,\;ax-y/2,\;z),\qquad
   P=(1/8+a^2/2)(x^2+y^2)-z^2
   \]
   solves the equations for every \(c\), has \(\Omega=(0,0,2a)\), and
   \[
   \operatorname{spec}DV=\{c-\tfrac12+ia,\ c-\tfrac12-ia,\ c+1\}.
   \]
   For \(0<c<1/2\) it violates **only sublinearity** among the stated hypotheses. Its generic backward trajectories escape in the transverse plane, so the global trapping input really is essential.

2. **An exact vortical profile with an uncountable stagnation set.** For \(b\ne0\), take
   \[
   U=(-cx+by,\;(c-1)y,\;z),\qquad
   P=\frac{c(1-c)}2(x^2+y^2)-z^2.
   \]
   Then
   \[
   \Omega=(0,0,-b),\quad
   V=(by,\;(2c-1)y,\;(1+c)z).
   \]
   For \(c\ne1/2\), \(N=\{(x,0,0):x\in\mathbb R\}\), and the spectrum is
   \(\{0,2c-1,1+c\}\). This is an exact smooth solution for all \(c\), but is not sublinear. For \(c<1/2\), precisely the initial points with \(y=0\) have bounded backward trajectories; they converge to the stagnation line. Their basin is a plane of measure zero. This example agrees with, rather than breaks, the local graph mechanism.

3. **Pure strain and irrotational potential flows.** Every symmetric trace-free \(M\) gives an affine solution, excluded by growth unless \(M=0\). More generally, for a smooth harmonic potential \(\phi\), \(U=\nabla\phi\) solves the profile equation with
   \[
   P=-(1-2c)\phi-c\,y\cdot\nabla\phi-\tfrac12|\nabla\phi|^2.
   \]
   Entire sublinear examples have constant \(U\) by the harmonic estimate above. Nonconstant entire examples have excessive growth; singular potential examples fail global \(C^2\) regularity. In any case these are irrotational, not counterexamples to the vorticity assertion.

4. **Shear flows.** For \(U=(f(y),0,0)\), pressure compatibility requires
   \[
   (1-c)f+cyf'=K
   \]
   with \(K\) constant. On each half-line,
   \[
   f(y)=\frac K{1-c}+C_\pm|y|^{\,1-1/c}.
   \]
   The exponent is negative in the range at issue, so continuity at \(y=0\) forces \(C_\pm=0\). Adding a constant transverse drift merely shifts this singular plane. Thus every entire smooth shear in this range is constant. Nonconstant power shears fail regularity; their singular planes also prevent a uniform three-dimensional little-oh bound at infinity.

5. **Columnar and two-dimensional flows.** For \(U=(0,0,f(x,y))\), pressure compatibility similarly forces \(f-K/(1-c)\) to be homogeneous of degree \(1-1/c<0\) in the transverse variables. Regularity at their origin forces it to vanish.

   For a planar incompressible field \(U=(u_1(x,y),u_2(x,y),0)\), its scalar vorticity obeys
   \[
   \omega+V\cdot\nabla\omega=0.
   \]
   Along a backward orbit, \(\omega(x(t))=e^t\omega(a)\). Sublinearity traps the orbit, so boundedness of \(\omega\) on its compact tail implies \(\omega(a)=0\). This argument works for every \(c>0\). A two-dimensional, three-component field \(U=(u_1(x,y),u_2(x,y),w(x,y))\) has the same equation for its vertical vorticity. The planar part is therefore a constant vector; the remaining equation for \(w\), after shifting the transverse center, is the homogeneous columnar equation just considered. These reductions give no counterexample.

6. **Axisymmetric flow without swirl.** Write \(U=u_r(r,z)e_r+u_z(r,z)e_z\) and \(\Omega=\omega_\theta e_\theta\). For \(r>0\), set \(\eta=\omega_\theta/r\). Equation (1) gives
   \[
   V\cdot\nabla\eta=-(1+c)\eta.
   \]
   Indeed \(V_r=cr+u_r\) and the stretching term is \((u_r/r)\omega_\theta\). A \(C^2\) axisymmetric no-swirl field has \(C^1\) vorticity vanishing on the axis, so \(\eta\) is bounded on compact sets, by a first-derivative bound for vorticity. Off-axis trajectories cannot hit the invariant axis in finite time. Along their backward trajectories,
   \[
   \eta(x(t))=e^{(1+c)t}\eta(a).
   \]
   Compact trapping forces \(\eta=0\), and continuity gives \(\Omega=0\) on the axis as well. Again this independently excludes this reduction for all \(c>0\). It does not apply unchanged to axisymmetry with swirl.

7. **Pure axisymmetric swirl.** For \(U=f(r)e_\theta\), the exact equations away from the axis reduce to
   \[
   (1-c)f+crf'=0,\qquad P_r=f^2/r.
   \]
   Thus, putting \(d=1-1/c\),
   \[
   f=Cr^d,\qquad P=\frac{C^2}{2d}r^{2d}+P_0
   \]
   in the present range. This is an exact solution on \(r>0\), but for \(c<1/2\), \(d<-1\), and it is singular on the axis. It is not an entire \(C^2\) field. Although it decays as \(r\to\infty\), that is not the required uniform condition as \(|(x,y,z)|\to\infty\): approaching the singular axis while sending \(z\to\infty\) also destroys that condition. At \(c=1/2\) this family contains the singular line vortex \(f=C/r\); it is not an endpoint counterexample under the theorem's regularity assumptions.

8. **Strain plus swirl, including Burgers-type candidates.** The ansatz
   \[
   U=-ar\,e_r+f(r)e_\theta+2az\,e_z
   \]
   is divergence free. Direct substitution gives the necessary angular equation
   \[
   (c-a)rf'+(1-c-a)f=0,
   \]
   and the pressure derivatives
   \[
   P_r=a(1-a)r+\frac{f^2}{r},\qquad
   P_z=-2a(1+2a)z.
   \]
   If \(a\ne c\), the swirl must be a power
   \(f=Cr^{(c+a-1)/(c-a)}\). Any nonzero \(a\) already violates sublinearity because of the axial linear strain. If \(a=c<1/2\), the angular equation forces \(f=0\). If \(a=0\), this reduces to the singular pure-swirl case.

   A Gaussian-core Burgers swirl \(f(r)=\Gamma(1-e^{-\mu r^2})/r\) is not a solution of this angular equation in the range \(0<c<1/2\). One cannot import a viscous Burgers vortex into the Euler equation by discarding its viscous term. There is an instructive degeneracy at \(a=c=1/2\): both angular coefficients vanish, so **any** axis-regular smooth \(f\), including this Gaussian-core swirl, gives an exact Euler profile with the displayed pressure. It still has linear strain, and also lies outside the specified range of \(c\).

9. **Beltrami and generalized Beltrami fields.** If \(U\times\Omega=0\), then \((U\cdot\nabla)U=\nabla(|U|^2/2)\). Taking the curl of the profile equation therefore requires
   \[
   \Omega+c(y\cdot\nabla)\Omega=0.
   \]
   Along rays, a nonzero \(\Omega\) would be homogeneous of degree \(-1/c\), incompatible with its continuity at the origin for every \(c>0\). Thus nonzero-vorticity Beltrami fields cannot satisfy this profile equation on all of \(\mathbb R^3\). In the constant-eigenvalue case \(\Omega=\lambda U\), \(\lambda\ne0\), the same identity applies directly to \(U\).

   For example \(U=(\sin z,\cos z,0)\) is a smooth uniformly bounded Beltrami field and an exact steady Euler velocity with constant pressure. It is **not** a solution of the profile equation for any \(c>0\), with any pressure: the displayed curl compatibility fails. Steady Euler and the similarity-profile equation must not be conflated.

10. **Fully periodic bounded fields.** There is also a direct check beyond Beltrami fields. If \(U\) is periodic in three independent directions, subtract the vorticity equation at \(y\) and at \(y+\ell\), for each period vector \(\ell\). Periodicity cancels every term except \(c\,\ell\cdot\nabla\Omega\), so \(\nabla\Omega=0\). A periodic curl has zero cell average, hence \(\Omega=0\). Harmonic periodic \(U\) is constant. Thus smooth nonconstant periodic steady Euler fields fail the profile equation when \(c>0\).

11. **Compactly supported vorticity.** A stronger, independent argument excludes this case. Equation (1) along a complete flow is a homogeneous linear ODE for vorticity, with invertible evolution matrix. Therefore
   \[
   Z=\{\Omega\ne0\}\quad\text{satisfies}\quad \Phi_s(Z)=Z.
   \]
   Meanwhile \(\operatorname{div}V=3c\) gives
   \[
   \det D\Phi_s=e^{3cs}.
   \]
   If \(Z\) had finite positive measure, change of variables would give
   \[
   |Z|=|\Phi_s(Z)|=e^{3cs}|Z|,
   \]
   impossible for \(c>0\) and \(s\ne0\). Compact support of continuous nonzero vorticity gives exactly such a set \(Z\). Thus any complete exact profile with compactly supported vorticity is irrotational, for every \(c>0\). Familiar steady or traveling vortices with compact vorticity do not become similarity profiles merely by choosing a pressure or adding a constant transport drift.

12. **Uniformly bounded exact velocity in general.** Such a velocity satisfies the sublinearity hypothesis. The completed proof therefore excludes every nonzero-vorticity exact \(C^2\) bounded profile for \(0<c<1/2\), including bounded nonperiodic fields not covered by the explicit ansatz calculations above. This last statement uses the proved theorem; it is not a separate classification of all bounded fields. No explicit entire \(C^2\), sublinear, vortical counterexample emerged from these checks.

**Endpoint and supercritical consistency.** “No obstruction” must mean “this proof gives no obstruction.” It must not be read as a proof that an exact entire sublinear vortical solution exists for those exponents.

At \(c=1/2\), \(\kappa=0\). The Bernoulli function is conserved along trajectories, and boundedness no longer forces the alpha-limit set into the zero set. Also \(B=C_\Omega\) is singular, so (5)'s positive lower bound, the critical-set equality, and the rank transfer (6) all fail as general tools. The energy dissipation used in (8) vanishes. Finally the eigenvalue argument at an exceptional equilibrium no longer forces a negative real part.

These are actual failures of implications, not merely bad constants. For the rotating affine example above at \(c=1/2\), backward trajectories with nonzero transverse radius have circles as their alpha-limit sets, while \(N=\{0\}\). Its transverse eigenvalues are \(\pm ia\), so there is no contracting direction for \(V\). This example is linear rather than sublinear and therefore does not prove failure of an endpoint theorem under all the other assumptions. It does demonstrate exactly why the proposed proof cannot pass through the endpoint.

For \(c>1/2\), a more precise description than the notes' summary is needed. We still have \(\kappa\ne0\). Step 2 survives with the direction of monotonicity reversed, and (5) survives with \(|\kappa|\) in its lower bound. The primary rank-two-arc capture argument also survives: use \(e(t)=H(x(t))-h\), so \(e'=-|\kappa||V|^2\). Thus positivity of \(\kappa\), as opposed to nonvanishing, is not the essential failure in those portions.

The decisive failures are spectral. At a vortical equilibrium the remaining eigenvalues sum to \(2c-1>0\); no negative-real-part eigenvalue is forced. On a vortical equilibrium arc the nonzero eigenvalues \(1+c\) and \(2c-1\) are both positive. Such arcs can attract open sets under backward dynamics, so 7.5 has no basis.

Indeed the affine stagnation-line example has, for \(d=2c-1>0\),
\[
 y(t)=y_0e^{-dt},\quad z(t)=z_0e^{-(1+c)t},\quad
 x(t)=x_0-\frac{by_0}{d}(1-e^{-dt})
\]
under backward dynamics. Every point converges to some point of its stagnation line. Sufficiently small initial neighborhoods of a line point remain in a prescribed larger neighborhood for all backward times. Hence its local trapping set contains an open set; the null-graph conclusion would be false if asserted without a contracting direction.

There is an additional failure at irrotational exceptional zeros: for
\[
 U=(-cx,-cy,2cz),\qquad V=(0,0,3cz),
\]
the matrix \(A\) has rank one, while \(\lambda_{\max}(S)=2c\ge1\) when \(c\ge1/2\). This is an exact affine profile with a suitable quadratic pressure. Thus even “every point of \(E\) has rank at least two” fails beyond the stated range. The rank-one parenthetical argument also stops helping, since \(2c<1\) is then false.

The asserted numerical profile at \(c=1/2\), associated in the notes with arXiv:2609.10867, was not independently checked here. Numerical evidence would not by itself establish existence of an exact global \(C^2\) sublinear profile in any event.

**Final assessment.** The theorem is valid with the explicit local justifications in this report. There is no surviving gap involving arbitrary stagnation sets, one-sided arcs, full-ball estimates, \(C^2\) regularity, generalized eigenspaces, or an uncountable union of basins. The remaining edits to the inspected proof are:

1. In 7.5, specify a norm adapted to the spectral direct sum, or include the norms of its projections; justify graph nullity by a covering argument.
2. In the alternative proof of 7.4, choose the transverse box width relative to its axial length, exclude transverse exits by distance to \(N\), and then exclude axial exits by the integral estimate. Keep time reversal consistent. This alternative can instead be deleted.

The earlier chart-choice and saddle-spectrum omissions were already repaired in the later text inspected. No stronger regularity, countability, analyticity, decay rate, strain bound, or finite-energy assumption is needed.

Consequently “rigorous obstruction” is justified for **exact**, global, time-independent, single-scale profiles satisfying the displayed equations, \(C^2\) regularity and uniform sublinearity, with \(0<c<1/2\). This does not prove a computable residual floor, rule out a noncompact sequence of approximate profiles, or exclude other blowup mechanisms. Ending a campaign is warranted by this theorem only insofar as that campaign's mathematical target is exactly this class.
