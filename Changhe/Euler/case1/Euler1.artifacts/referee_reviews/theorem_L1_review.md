**Verdict: PROOF CORRECT for Theorem L1 and Corollary L1′.** Steps 0–7 require no additional hypothesis. In particular, the backward-time estimate and the center-unstable manifold argument are valid.

The document nevertheless needs corrections: the Cauchy-formula citation is wrong; the curve discussion needs local qualifications; and the numerical residual-floor assertion in §3(d), repeated in §5, is false as stated. These assertions are not used in the proof.

I read `THEORY_NOTES.md` in full. The literature search did not establish novelty; an important overlapping Chae–Wolf result is discussed below.

**Step 0: correct.** Write
\[
V=cy+U,\qquad G_{ij}=\partial_jU_i,\qquad
S=\tfrac12(G+G^T),\qquad \Omega=\nabla\times U.
\]
Sublinearity and continuity give \(|V(y)|\le C(1+|y|)\). Local existence and uniqueness, together with this growth bound, give a complete flow in both time directions. Since \(V\in C^2\), every time map \(\Phi_s\) is a \(C^2\) diffeomorphism, with inverse \(\Phi_{-s}\). No global bound on \(DV\) is needed.

Taking curl gives
\[
\Omega+V\cdot\nabla\Omega=G\Omega.
\]
For the stated matrix convention, the antisymmetric part \(W=(G-G^T)/2\) satisfies
\[
Wx=\tfrac12\Omega\times x.
\]
Thus \(W\Omega=0\), and \(G\Omega=S\Omega\). All differentiations are legitimate under the stated regularity. The discussion of recovering \(P\in C^2\) is redundant because that regularity is already assumed.

**Step 1: correct.** Choose \(R_b>0\) so that
\[
V(y)\cdot y\ge \tfrac c2|y|^2\qquad (|y|\ge R_b).
\]
In backward time \(t=-s\),
\[
\frac{d}{dt}|Y(a,-t)|^2\le-c|Y(a,-t)|^2
\]
while the trajectory is outside the ball. Remaining outside forever would contradict the resulting exponential upper bound. The strict inward direction of \(-V\) on the boundary makes the closed ball backward invariant.

Consequently, every backward trajectory is precompact. Its alpha-limit set is nonempty, compact and invariant. It is connected because it is the intersection of nested compact connected closures of continuous trajectory tails. This uses continuous time; it is not a statement about arbitrary discrete dynamical systems.

Every zero of \(V\) lies inside the ball, so \(N_V\) is compact.

**Step 2: correct, including the countable case.** The identities
\[
H=\frac12|V|^2+P+\frac{c(c-1)}2|y|^2,\qquad
(1-2c)V+\Omega\times V+\nabla H=0
\]
give
\[
\frac{d}{ds}H(Y(a,s))=-(1-2c)|V(Y(a,s))|^2.
\]
These are precisely the Bernoulli identities in CIV (3.29)–(3.32). ([arxiv.org](https://arxiv.org/pdf/2602.17570v3))

On a compact backward tail, \(H\) is bounded. Monotonicity therefore gives a finite limit \(h\) as \(s\to-\infty\). Continuity implies \(H=h\) throughout \(\alpha(a)\). Invariance then implies that \(H\) is constant along the orbit through each \(z\in\alpha(a)\); hence
\[
0=-(1-2c)|V(z)|^2.
\]
Therefore \(\alpha(a)\subset N_V\).

A connected countable subset of Euclidean space contains at most one point. Indeed, if it contained distinct \(p,q\), its image under \(z\mapsto |z-p|\) would contain the interval \([0,|q-p|]\). Thus countability gives
\[
\alpha(a)=\{p\}.
\]
Precompactness upgrades this to convergence of the entire backward trajectory: otherwise a sequence staying a fixed distance from \(p\) would have another alpha-limit point.

There is **no hidden assumption that the zeros are isolated**. Countable compact zero sets may have accumulation points.

No coercivity or far-field estimate for \(H\) or \(P\) is needed. Also, the note after Step 7 should distinguish strict *monotonicity*, valid for \(c\ne1/2\), from strict *decrease*, valid for \(c<1/2\).

**Step 3: correct, including matrix order and time direction.** Let
\[
J(a,s)=D_aY(a,s).
\]
Then
\[
J_s=(cI+G(Y))J.
\]
Along trajectories,
\[
\frac{d}{ds}\Omega(Y)=(G(Y)-I)\Omega(Y).
\]
Thus \(e^{(1+c)s}\Omega(Y(a,s))\) and \(J(a,s)\Omega(a)\) satisfy the same linear initial-value problem:
\[
\boxed{\Omega(a)=e^{(1+c)s}J(a,s)^{-1}\Omega(Y(a,s)).}
\]

The correct CIV reference is **(3.22)**. Equations (3.24)–(3.26) concern the Weber formula and circulation. ([arxiv.org](https://arxiv.org/pdf/2602.17570v3))

For \(t\ge0\), set \(B(t)=J(a,-t)^{-1}\). Differentiation gives
\[
B'(t)=B(t)\bigl(cI+G(Y(a,-t))\bigr).
\]
The multiplication is on the **right**. Consequently, for fixed \(\eta\),
\[
w(t)=B(t)^T\eta,\qquad
w'=\bigl(cI+G(Y(a,-t))^T\bigr)w,
\]
and
\[
\frac d{dt}|w|^2
\le2\bigl(c+\lambda_{\max}(S(Y(a,-t)))\bigr)|w|^2.
\]
Taking the operator norm and combining with the Cauchy formula yields exactly
\[
\boxed{
|\Omega(a)|
\le
\exp\!\left(\int_0^t
[\lambda_{\max}(S(Y(a,-r)))-1]\,dr\right)
|\Omega(Y(a,-t))|.
}
\tag{*}
\]
No commutation of matrices at different times is being assumed.

An independent sign check is available directly: \(q(t)=\Omega(Y(a,-t))\) satisfies
\[
q'=(I-G)q,\qquad
\frac d{dt}|q|^2\ge2(1-\lambda_{\max}S)|q|^2,
\]
which gives the same inequality.

**Step 4: correct.** If the entire compact set \(\alpha(a)\) avoids
\[
E=\{p\in N_V:\lambda_{\max}(S(p))\ge1\},
\]
continuity supplies a neighborhood \(O\) and \(\eta>0\) with
\[
\lambda_{\max}S\le1-\eta\quad\hbox{on }O.
\]
The trajectory eventually remains in \(O\). Otherwise, precompactness would produce an alpha-limit point outside \(O\).

Vorticity is bounded on the compact backward tail. The finite initial part of the integral in (*) contributes only a finite constant, and the remaining part gives exponential decay. Hence \(\Omega(a)=0\).

The condition concerns the **whole alpha-limit set**. Having merely one good stagnation point in it would not justify this argument.

**Step 5: correct in both cases.** At \(p\in E\), put \(A=DV(p)=cI+G(p)\), so \(\operatorname{tr}A=3c\).

If \(\Omega(p)\ne0\), evaluating the vorticity equation at \(p\) gives
\[
A\Omega(p)=(1+c)\Omega(p).
\]
The other two eigenvalues, counted algebraically, sum to \(2c-1<0\). If they are real, at least one is negative. If they are a complex-conjugate pair, both have real part \(c-\tfrac12<0\).

If \(\Omega(p)=0\), then \(G(p)=S(p)\), so \(A\) is symmetric. Since
\[
\operatorname{tr}S=0,\qquad \lambda_{\max}(S)\ge1,
\]
one has \(\lambda_{\min}(S)\le-\tfrac12\). Therefore
\[
\lambda_{\min}(A)\le c-\tfrac12<0.
\]

These prove the second assertion of L1′. They do not require an outgoing hypothesis.

**Step 6: correct; specify the trapping version of the theorem.** The relevant statement is:

For a \(C^1\) vector field near an equilibrium \(p\), with real generalized spectral splitting
\[
\mathbb R^n=E^s\oplus E^{cu},
\qquad
\Re\sigma(A|_{E^s})<0,\quad
\Re\sigma(A|_{E^{cu}})\ge0,
\]
there exists a local \(C^1\) center-unstable manifold, tangent to \(E^{cu}\), and a sufficiently small neighborhood such that every trajectory remaining there for all negative time belongs to that manifold.

A precise accessible reference is **Lee–Simchowitz–Jordan–Recht, “Gradient Descent Only Converges to Minimizers,” COLT 2016, Theorem 7, p. 6**, which reproduces the stable-center theorem attributed to **Shub, *Global Stability of Dynamical Systems* (1987), Theorem III.7**. Its explicit conclusion includes
\[
\bigcap_{j\ge0}F^{-j}(B)\subset W^{cs}_{\mathrm{loc}}.
\]
I checked the published restatement; I did not inspect Shub’s original book. ([proceedings.mlr.press](https://proceedings.mlr.press/v49/lee16.pdf))

Apply it to
\[
F=\Phi_{-1},\qquad DF(p)=e^{-A}.
\]
An eigenvalue of \(e^{-A}\) has modulus at most one exactly when the corresponding eigenvalue of \(A\) has nonnegative real part. Thus the stable-center disk for \(F\) has the required center-unstable dimension for \(V\). A continuously trapped backward orbit satisfies the discrete trapping condition. Choose the closed ball strictly inside the theorem’s neighborhood.

Use **generalized eigenspaces**, not just ordinary eigenvectors, when stating this for a general nonsymmetric matrix. Complex-conjugate eigenvalues contribute their real spectral dimension. The optimization paper’s simplified eigenvector wording should not be copied literally into the PDE argument.

The trapping assertion can also be verified by the cutoff construction in the notes. After translating \(p=0\), write \(V(x)=Ax+f(x)\), and cut off \(f\) so that its global Lipschitz constant is sufficiently small. For prescribed \(\xi=x_{cu}(0)\), backward trajectories on the graph solve
\[
\begin{aligned}
x_{cu}(s)&=e^{A_{cu}s}\xi+
\int_0^s e^{A_{cu}(s-r)}f_{cu}(x(r))\,dr,\\
x_s(s)&=\int_{-\infty}^s e^{A_s(s-r)}f_s(x(r))\,dr.
\end{aligned}
\]
Choose a positive weight smaller than the stable spectral gap. These equations are a contraction in the corresponding exponentially weighted backward-trajectory space. Their solutions define a Lipschitz graph over \(E^{cu}\). Every bounded backward trajectory satisfies these integral equations—the stable boundary term at \(-\infty\) vanishes—and hence belongs to the graph. This already supplies all the regularity needed for the measure argument.

Center-type manifolds can be nonunique. **Nonuniqueness does not matter:** choose one supplied with the trapping property. The argument needs containment in such a manifold, not uniqueness or equality with the trapped set.

Finally, if \(Y(a,s)\to p\) backward, some integer \(K\ge0\) places its entire earlier tail inside the trapping ball. Hence
\[
\{a:\alpha(a)=\{p\}\}
\subset
\bigcup_{K=0}^{\infty}\Phi_K(W^{cu}_{p,\mathrm{loc}}).
\]
For \(p\in E\), Step 5 gives \(\dim W^{cu}_{p,\mathrm{loc}}\le2\). Such a graph has three-dimensional Lebesgue measure zero. A \(C^1\) diffeomorphism preserves null sets, by local Lipschitz bounds and a countable covering. Therefore the backward basin is null. Uniform manifold sizes across different equilibria are unnecessary.

**Step 7: correct.** Every point has a singleton alpha-limit in the countable set \(N_V\). On basins of good equilibria, vorticity vanishes. The union of the other basins is a countable union of null sets. Thus \(\Omega=0\) almost everywhere, and continuity gives \(\Omega=0\) everywhere.

Now
\[
\Delta U=\nabla\operatorname{div}U-\nabla\times(\nabla\times U)=0.
\]
For each component and fixed \(x\), the interior harmonic estimate gives
\[
|\nabla U_i(x)|
\le \frac C R\sup_{B_R(x)}|U_i|.
\]
Sublinearity makes the right-hand side tend to zero. Hence \(U=b\) is constant. Its pressure is
\[
P(y)=-(1-c)b\cdot y+P_0.
\]
Decay forces \(b=0\).

There is no finite-energy assumption anywhere in this argument.

**The curve heuristic in §3(a) has correct algebra but overstates the global conclusion.** At a regular curve of equilibria, its tangent \(t\) satisfies \(At=0\). At a point with nonzero vorticity,
\[
\sigma(A)=\{0,1+c,2c-1\}.
\]
At a point with zero vorticity and \(\lambda=\lambda_{\max}S\ge1\),
\[
\sigma(A)=\{0,c+\lambda,2c-\lambda\}.
\]
Thus both cases have a simple tangent zero eigenvalue and one positive and one negative transverse eigenvalue.

This gives normal hyperbolicity on a sufficiently small regular curve patch around that point. It does **not** establish normal hyperbolicity of an entire curve from information at one point. A global assertion requires suitable uniformity and treatment of endpoints and singular accumulation points.

For a normally hyperbolic equilibrium curve patch, the local center-unstable manifold has dimension two. It captures backward trajectories that remain in its trapping neighborhood. Global basins require forward images of these local manifolds, as in Step 6. The text should state these qualifications explicitly.

Likewise, Step 4 applies to an alpha-limit set contained entirely in the good part of the curve; it does not follow merely because the alpha-limit set meets that part.

**The surface calculation in §3(b) is correct.** At a regular surface of zeros, \(\dim\ker A\ge2\), so the eigenvalues are \(0,0,3c\). Nonzero vorticity would require the eigenvalue \(1+c\), forcing \(c=1/2\). Therefore \(\Omega=0\) on the surface, \(A\) is symmetric, and
\[
\sigma(S)=\{-c,-c,2c\},\qquad \lambda_{\max}S=2c<1.
\]
Step 4 applies whenever the whole alpha-limit set is contained in this regular surface. Singular points in its closure require separate treatment.

**Section 3(c) correctly identifies limitations of the argument presented.** Compactness of \(N_V\) does not make each stratum compact, and pointwise manifold constructions alone do not control trajectories accumulating on several strata. Real-analytic zero sets admit the relevant stratification machinery, but stratification itself supplies no missing dynamical trapping or convergence argument. ([pmihes.centre-mersenne.org](https://pmihes.centre-mersenne.org/item/10.1007/BF02699126.pdf))

These are gaps in a proposed extension beyond L1, not gaps in L1 itself.

**Section 3(d), and the corresponding residual-floor language in §5, are false as written.** Here is a direct counterexample to that inference.

Choose nonzero divergence-free \(W\in C_c^\infty(\mathbb R^3)\), supported away from the origin, and set
\[
U_\varepsilon=\varepsilon W,\qquad P_\varepsilon=0.
\]
For \(\varepsilon\|DW\|_\infty<c\), the transport field
\[
V_\varepsilon(y)=cy+\varepsilon W(y)
\]
has exactly one zero, at the origin. Indeed,
\[
|V_\varepsilon(y)|
\ge(c-\varepsilon\|DW\|_\infty)|y|.
\]
That zero is nondegenerate, with \(DV_\varepsilon(0)=cI\).

Nevertheless,
\[
U_\varepsilon\longrightarrow0
\quad\text{globally in }C^2,
\]
and its equation residual is
\[
R_\varepsilon
=\varepsilon\bigl((1-c)W+cy\cdot\nabla W\bigr)
+\varepsilon^2(W\cdot\nabla)W
\longrightarrow0
\]
in every fixed \(C^k\) norm. The exact zero profile has the same stagnation structure.

Thus residuals can vanish without stagnation-set degeneration or spatial drift. L1 excludes a **nonconstant exact limiting profile satisfying its hypotheses**. A residual lower bound would require a specified residual norm, a nontriviality normalization, and additional compactness or quantitative estimates. None is proved here.

**For the literature comparison, the exponent conversion is essential.** In the older convention
\[
u(x,t)=(T-t)^{-\alpha/(1+\alpha)}
\,v\!\left(\frac{x-x_*}{(T-t)^{1/(1+\alpha)}}\right),
\]
one has
\[
c=\frac1{1+\alpha}.
\]
Thus \(c<1/2\) means \(\alpha>1\), while the three-dimensional energy-conserving exponent \(\alpha=3/2\) corresponds to \(c=2/5\).

- **Chae, CMP 273 (2007), 203–215.** Theorem 1.1 requires
  \[
  \Omega\in L^p(\mathbb R^3)\quad\text{for every }0<p<p_1
  \]
  for some \(p_1>0\), in its classical-flow setting. The proof already uses vorticity transport and the back-to-label map, together with finite integrated global velocity-gradient bounds on regular time intervals. Consequently, neither the transport mechanism nor a general vorticity Liouville conclusion is new. Its small-\(p\) integrability requirement is absent from L1; the result does not directly prove L1. I read §1, including Theorems 1.1–1.2 and their proofs, in arXiv:math/0601060v2. ([arxiv.org](https://arxiv.org/pdf/math/0601060v2))

- **Chae–Shvydkoy, ARMA 209 (2013), 999–1017.** The velocity exclusions use \(L^p\) assumptions and the associated pressure recovered by a whole-space singular integral. In particular, their velocity theorem excludes the ranges \(\alpha>3/2\) or \(-1<\alpha\le3/p\), under its integrability assumptions. The vorticity theorem assumes strain tending to zero and \(\Omega\in L^p\) for some \(0<p<3/(1+\alpha)=3c\). These are additional conditions, and the velocity theorem does not cover \(1<\alpha<3/2\) merely from sublinearity. The proofs examined use local-energy estimates or exterior vorticity estimates, not the countable-stagnation/center-unstable argument. I read the v2 HTML, cross-checking formulas in the accessible v1 PDF; theorem numbering differs between those versions. ([arxiv.org](https://arxiv.org/html/1201.6009v2), [arxiv.org](https://arxiv.org/pdf/1201.6009v1))

- **Bronzi–Shvydkoy, Indiana University Mathematics Journal 64 (2015), 1291–1302.** Theorem 1.1 concerns a locally self-similar profile embedded in a finite-energy ambient solution, with \(0<\alpha<3/2\), local \(C^3\) regularity and an annular \(L^p\)-growth assumption
  \[
  \int_{|y|\sim L}|v|^p\,dy\lesssim L^\gamma,
  \qquad p\ge3,\quad\gamma<p-2.
  \]
  Its conclusion is either triviality or matching energy growth
  \[
  \int_{|y|<L}|v|^2\,dy\asymp L^{3-2\alpha}.
  \]
  This is not a blanket nonexistence theorem in L1’s range. I read the statement, explanatory remarks, pressure-recovery argument and main proof in arXiv:1310.8611v2. ([arxiv.org](https://arxiv.org/pdf/1310.8611v2))

- **Chae–Wolf.** Their *Energy concentrations and Type I blow-up for the 3D Euler equations*, CMP 376 (2020), includes Corollary 1.5 excluding discretely self-similar solutions at the energy-conserving scale under finite-energy and Type I gradient assumptions. This concerns \(c=2/5\), with hypotheses not imposed in L1. I checked the introduction, theorem/corollary statements and the self-similar argument in §5 of arXiv:1706.02020v2. Their local Type I paper, arXiv:1707.00377, supplies local smallness criteria, not an implication of L1 under its stated assumptions. ([arxiv.org](https://arxiv.org/pdf/1706.02020), [arxiv.org](https://arxiv.org/html/1707.00377v1))

- **An important later Chae–Wolf result must be included:** *On the Discretely Self-similar Solutions to the Euler Equations in \(\mathbb R^3\)*, Journal of Nonlinear Science 33, 115 (2023). Its published abstract states spatial constancy for \(\alpha\ge3/2\), allowing sublinear profile growth. This potentially supplies a stronger predecessor on \(0<c\le2/5\), without a countable-zero hypothesis. **I obtained only the publisher’s abstract, references and exposed appendix, not the main theorem.** I therefore have not verified whether its precise growth, regularity and pressure hypotheses match \(U=o(|y|)\) and arbitrary \(C^2\) pressure here. Its stated exponent range does not cover \(2/5<c<1/2\). ([link.springer.com](https://link.springer.com/article/10.1007/s00332-023-09975-1))

- **Chae’s 2015 maximum-principle paper** also deserves mention. Theorem 1.1 assumes \(\nabla U=o(1)\) and, for \(\alpha>-1\), vorticity decay \(O(|y|^{-k})\) with \(k>\alpha+1=1/c\). This does not directly imply L1 either. I checked its main statements and the exterior-vorticity mechanism. ([arxiv.org](https://arxiv.org/pdf/1308.1051v3))

**CIV is the closest verified predecessor.** Its Theorem 3.9 assumes finite \(N_V\), local outgoing behavior, the far-field bounds (3.8), and normalization (3.7). Outgoing behavior gives
\[
S(p)\ge(c_*-c)I,\qquad
\lambda_{\max}S(p)\le2(c-c_*)<1
\]
when \(c<1/2\); hence every equilibrium is good. L1 replaces that restriction by the null-basin argument and also dispenses with the stronger far-field and normalization assumptions. CIV Theorem 3.8 is consistent with Step 5(i) and the outgoing spectral bound. Its reference [8], a Chae–Wolf paper, concerns **Navier–Stokes**, not Euler. ([arxiv.org](https://arxiv.org/pdf/2602.17570v3))

I found no checked result implying **all of L1 under exactly its stated hypotheses**. That is a bounded literature-search conclusion, not a novelty certification. The inaccessible 2023 Chae–Wolf theorem is a specific remaining bibliographic limitation.

**The sanity check found no applicable counterexample among the profiles examined.**

There are smooth affine profiles with nonzero vorticity and a single stagnation point even for \(c<1/2\). They fail sublinearity. For example, for \(a\ne0\),
\[
U(y)=\left(-\tfrac12y_1-ay_2,\ ay_1-\tfrac12y_2,\ y_3\right),
\qquad
P(y)=\left(\tfrac18+\tfrac{a^2}{2}\right)(y_1^2+y_2^2)-y_3^2.
\]
Direct substitution verifies the profile equation for every \(c\). Here
\[
\Omega=(0,0,2a),\qquad
\sigma(DV)=\{c-\tfrac12\pm ia,\ c+1\}.
\]
For \(0<c<1/2\), \(N_V=\{0\}\), but \(U\) grows linearly and generic backward trajectories escape. This explicitly demonstrates why Step 1’s hypothesis matters. The general affine family also appears in Bronzi–Shvydkoy. ([arxiv.org](https://arxiv.org/pdf/1310.8611v2))

The other checks were:

- **Elgindi’s exact self-similar construction** belongs to the \(C^{1,\alpha}\) setting; it does not supply a \(C^2\) counterexample to L1. ([arxiv.org](https://arxiv.org/html/1904.04795v2), [arxiv.org](https://arxiv.org/abs/1904.04795))
- **Wang–Lai–Gómez-Serrano–Buckmaster (2023)** treats the Luo–Hou boundary scenario through its Boussinesq limiting profile. **Discovery of Unstable Singularities** likewise identifies its Euler results as involving a boundary. These are not whole-space profiles of L1’s class. ([arxiv.org](https://arxiv.org/html/2201.06780v3), [arxiv.org](https://arxiv.org/abs/2509.14185))
- **Martínez-Argüello–Rica, Physical Review Fluids 9, 094401 (2024)** reports a numerical candidate with \(\nu\approx2.03\). Their ansatz identifies \(\nu=c\), so it lies outside L1’s range. I checked the ansatz and reported exponent, not the validity of their numerical construction. ([harvest.aps.org](http://harvest.aps.org/v2/journals/articles/10.1103/PhysRevFluids.9.094401/fulltext))
- **arXiv:2609.10867v2** explicitly reports an approximate profile at \(c=0.5\). L1 excludes neither that exponent nor that candidate. I read its abstract, not its 111-page certification/stability analysis. ([arxiv.org](https://arxiv.org/abs/2609.10867))

I inspected CIV’s relevant sections and bibliography, but did not independently read every cited work.

The requested Opus 5.5 consultation could not run because the configured Bedrock credentials were unavailable. No substitute model was used.