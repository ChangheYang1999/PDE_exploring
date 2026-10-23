I read `EQUATIONS.md` in full and compared the relevant statements with `PROMPT.md` and the supplied v3 paper. Independent symbolic checks also confirmed the residual identities and seed formula.

**1. CORRECT — §§1.1–1.4.**

Direct differentiation gives
\[
u_t=\tau^{c_l-2}\bigl[(1-c_l)U+c_l(y\cdot\nabla)U\bigr],
\]
so (E) has the stated signs. For the moving center, the additional transport coefficient is \(-z_c'\tau^{1-c_l}\); hence
\[
z_c'=-C\tau^{c_l-1},\qquad z_c=z_*+\frac C{c_l}\tau^{c_l}.
\]
The stated canonical change of coordinates removes \(C\).

Writing \(\delta=\nabla\cdot U\), direct product differentiation gives exactly
\[
\nabla\cdot R_m=\delta+V\cdot\nabla\delta+\operatorname{tr}(G^2)+\Delta P,
\qquad
\nabla\times R_m=R_\omega+\delta\Omega.
\]
Both defect signs are correct.

Substituting \(U=V-c_l(y+C e_3/c_l)\) gives the stated Bernoulli identity and
\[
V\cdot\nabla H=(2c_l-1)|V|^2+V\cdot R_m.
\]
At a **nonzero** interior vorticity maximum, the exact vorticity equation gives \(\Omega\cdot G\Omega=|\Omega|^2\). The spatial scaling and invariance of vorticity amplitude are correct.

**2. CORRECT — cylindrical system.**

Differentiating the moving basis contributes
\[
(V\cdot\nabla)U
=(DU^r-(U^\theta)^2/r)e_r
 +(DU^\theta+U^rU^\theta/r)e_\theta
 +(DU^z)e_3.
\]
This verifies both geometric terms; no additional \(c_lU^\theta\) term occurs. The divergence and all three cylindrical vorticity components are correct:
\[
\Omega^r=r^{-1}\partial_\theta U^z-\partial_zU^\theta,\quad
\Omega^\theta=\partial_zU^r-\partial_rU^z,\quad
\Omega^z=r^{-1}\partial_r(rU^\theta)-r^{-1}\partial_\theta U^r.
\]

**3. ERROR — spectral classification; the regularity formulas are correct.**

The even cylindrical frequencies, odd horizontal Cartesian frequencies, vector group average, and axis Taylor expansion are correct. The identities
\[
U_1\pm iU_2=e^{\pm i\theta}(U^r\pm iU^\theta)
\]
give precisely the stated factors \(r^{|n\pm1|}\). They are necessary smoothness conditions; an infinite Fourier reconstruction also requires appropriate convergence of modes and derivatives.

The following classifications are wrong:

- \(E_2=0,\ E_4>0\) does **not** imply four-fold symmetry. Simultaneous \(n=4\) and \(n=6\) content has fundamental period \(\pi\).
- Likewise, \(E_2=E_4=0\) does not imply axisymmetry (§7.2).
- Axisymmetry requires every nonzero cylindrical angular mode to vanish. Four-fold symmetry requires every occupied frequency to be divisible by four.

Requiring resolvable \(E_2\) implements the prompt’s chosen search criterion; it is not a characterization of all fundamentally two-fold fields. In the Parseval formula, count \(n=0\) once, not twice through the notation \(\sum_{\pm n}\).

**4. CORRECT — curl projection, with one wording qualification.**

For orthogonal \(O\),
\[
\nabla\times[O F(O^Ty)]
 =\det(O)\,O(\nabla\times F)(O^Ty).
\]
Thus the stated \(Q\)-projection commutes with curl.

The explanation that a projection “must” use a rotation is too broad. Reflection-equivariant velocities can be constructed using an **axial-vector** transformation law for the potential. What fails for reflections is using the same polar-vector action on both potential and velocity.

**5. ERROR — blanket claims about derivative gauges; the centering statements in §6 are otherwise correct.**

For the decaying target class, the listed continuous freedoms are correct. To remove translation ambiguity, write
\[
U_h(y)=U(y-he_3),\qquad C_h=C-c_lh.
\]
A nonzero \(h\) therefore does not preserve \(C=0\). Canonical \(U(0)=0\) is a genuine restriction.

For a canonical decaying profile, \(c_lz+U_3(0,0,z)\) changes sign. If its zero is \(z_0\), then
\[
\widetilde U(y)=U(y+z_0e_3),\qquad \widetilde C=c_lz_0
\]
satisfies \(\widetilde V(0)=0\). This centering exists but need not be unique.

The derivative discussion needs correction:
\[
D^kU_a(y)=a^{1-k}D^kU(y/a).
\]
First derivatives cannot fix spatial scale, but higher derivatives can: for example, \(0<\|D^2U\|_\infty<\infty\) permits the gauge \(\|D^2U_a\|_\infty=1\). Some first-derivative **components** can also fix rotation phase. The listed vorticity-amplitude constraints are correctly identified as nongauges.

A maximum on a fixed finite grid, or a norm with fixed spatial weight, is not exactly scale covariant. These are numerical gauge surrogates whose nondegeneracy must be checked.

**6. ERROR — affine classification; the seed identities are correct.**

A general \(Q\)-equivariant linear field has
\[
M=\begin{pmatrix}a&b&0\\c&f&0\\0&0&e\end{pmatrix}.
\]
The necessary and sufficient conditions here are
\[
a+f+e=0,\qquad (1-e)(b-c)=0,
\]
because
\[
(M+M^2)_{12}-(M+M^2)_{21}=(1+a+f)(b-c).
\]

Consequently:

- The vortical branch \(b\ne c\) requires exactly \(e=1,\ f=-1-a\).
- The symmetric branch \(b=c\) allows every symmetric trace-free block matrix.
- “Up to an overall factor” is false for the vortical branch. Scaling \(M\) by \(\lambda\) produces antisymmetric part proportional to \(\lambda(1-\lambda)(M-M^T)\).

For the section 10 matrix, \(M+M^2=\operatorname{diag}(k,k,2)\), the explicit curl formula, \(A_\infty\), extra symmetries, and numerical defaults all check out.

The displayed cylindrical formulas in §10 describe **\(My\)**, not the localized seed. To make this explicit, define
\[
f=-\tfrac12+(a+\tfrac12)\cos2\theta+\tfrac{b+c_M}{2}\sin2\theta,
\quad
g=\tfrac{c_M-b}{2}+\tfrac{b+c_M}{2}\cos2\theta-(a+\tfrac12)\sin2\theta,
\quad
\eta=\frac1{3c_l(1+R^2)}.
\]
Then
\[
U_{\rm seed}^r=\chi r[(1-\eta z^2)f+\eta z^2],\quad
U_{\rm seed}^\theta=\chi r(1-\eta R^2)g,\quad
U_{\rm seed}^z=\chi z[1+\eta r^2(f-1)].
\]
The stated criterion for nonzero \(n=2\) content remains correct.

Also, §7.2’s constant solution is an exact **unforced** Euler solution with a linear pressure. A pressure gradient is not itself an external body force. Reject this solution because it violates the required decay.

**7. UNCLEAR — Chae attribution; the principal tail calculations are correct.**

The linear similarity operator annihilates degree
\[
d=1-\frac1{c_l}.
\]
Spherical divergence gives
\[
\nabla\cdot(R^dA)=R^{d-1}\bigl[(d+2)A_r+\operatorname{div}_{S^2}A_T\bigr],
\]
including the stated zero-flux consequence.

The first nonlinear correction has degree \(2d-1\), with linear coefficient \(-1\). The nonlinear degree sequence \(d+k(d-1)\) is correct **as a formal sequence**, not an exhaustive expansion. Pressure multipoles can add other degrees: a matched pressure quadrupole \(R^{-3}Y_2\), for example, produces a velocity correction of degree \(-4\). Generic second pressure-source moments need not converge in this exponent range, so such coefficients require tail subtraction or matching.

For \(F=\operatorname{tr}(G^2)=\partial_i\partial_j(U_iU_j)\),
\[
\int_{B_R}F=O(R^{2d+1}),\qquad
\int_{B_R}y_kF=O(R^{2d+2}).
\]
Thus monopole cancellation needs \(d<-1/2\), while dipole cancellation needs \(d<-1\). Both hold here; the weaker threshold alone does not establish both cancellations.

For a nonzero leading angular tail,
\[
\int_0^\rho r^{2d+2}\,dr<\infty
\iff d>-\tfrac32
\iff c_l>\tfrac25.
\]
This concerns the limiting outer singular field. At every pre-blowup time a smooth profile is locally square integrable. The core scaling, cancellation of the time exponent in the outer matching calculation, and failure of global \(U\in L^2\) are correct.

**Chae limitation:** I could not retrieve the published CMP paper because external DNS access failed. The supplied sources do not contain its theorem statement. I therefore do not certify §8.5’s attribution or its exact published hypotheses.

The guardrail I can derive directly, under bounded strain and sufficient cutoff justification, is
\[
\left(1-\frac{3c_l}{p}\right)\int|\Omega|^p
 =\int(\Xi\cdot S\Xi)|\Omega|^p.
\]
Writing \(K=\|S\|_{\mathrm{op},\infty}\), this excludes nonzero vorticity whenever
\[
\Omega\in L^p,\qquad p<\frac{3c_l}{1+K}.
\]
Integrability for all sufficiently small positive \(p\) suffices. A single \(p<3c_l\) also suffices with the additional conditions \(\nabla U\to0\) and \(U=o(R)\): an exterior cutoff first forces compactly supported vorticity, after which the small-\(p\) argument applies. These distinctions must appear before attributing a theorem.

The natural nonzero vorticity tail has integrability threshold \(p>3c_l\). Moreover, a nonzero, globally smooth angular tail of the stated degree cannot be both divergence free and irrotational: its potential would be harmonic homogeneous of degree \(d+1\in(-1/2,0)\), impossible by the spherical Laplacian eigenvalue condition.

**8. ERROR — §9.1 misstates Theorem 4.3 and overstates several consequences.**

Comparison with the [supplied v3 text](analysis/sources/2602.17570v3.txt):

| Result | Audit |
|---|---|
| Theorem 2.1 | Correct. More precisely, initial vorticity is \(C^1\), initial velocity has finite kinetic energy, and the stated global gradient bound holds until blowup. |
| Remark 2.2 | Correct: the uniform velocity \(L^p\) bound gives \(\gamma\ge p/(p+3)\). |
| Theorem 3.4 | Correct but underspecified. It states \(\|\nabla\Omega\|_\infty^{3/(p+3)}\|\Omega\|_p^{p/(p+3)}\ge C_p^{-1}\), for \(p>\max\{3\gamma,1\}\), assuming (3.8). |
| Theorem 3.8 | Correct, with \(c_*\ge0\). At the stagnation point, \(S\Omega=\Omega\); trace zero gives \(\lambda_{\min}(S)\le-1/2\), while outgoing requires \(\gamma+\lambda_{\min}(S)\ge c_*\). |
| Theorem 3.9 | Correct. Definition 3.7 includes finitely many stagnation points and the local inequality at every one, allowing \(c_*=0\). |
| Theorem 4.3 | **Incorrectly summarized.** It assumes a **meridional fixed point with nonzero swirl** and concludes \(\gamma=1/2\). This is not a zero of the full transport field. At that point the swirl equation gives \((1-2\gamma)U^\theta=0\). |
| Theorem 4.5 / Remark 4.6 | Correct for **nontrivial** profiles satisfying the stated hypotheses. Remark 4.6 retains (3.5) and (3.8); it is not an unrestricted statement about every smooth swirl-free profile. |

Two further errors:

- Centering at an axis stagnation point gives \(U(0)+Ce_3=0\), **not** \(U(0)=0\). The sentence equating these conditions when \(C\) is free is wrong.
- Axisymmetric exclusion supplies no quantitative lower bound making the \(n=2\) component “\(O(1)\).” Other nonaxisymmetric modes may dominate, and no claimed separation from the axisymmetric class is proved.

**9. CORRECT — residual definitions and normalized metrics.**

The four residuals, divergence-defect corrections, and term-normalized denominators agree with PROMPT §11. The additional nonlinear-scale tail normalization is appropriate.

The importance-sampling formula requires \(q\) to be the probability density **relative to physical volume on \(D\)**. A computational-coordinate density needs its Jacobian.

The validation instructions remain incomplete relative to PROMPT §11: explicitly require reconstruction from saved parameters, selected finite-difference or interpolation checks, and checks for unresolved angular modes and nonlinear aliasing.

**Requirements from PROMPT §§3–8 not explicitly carried through:**

- Rotationally periodic identification on a fundamental wedge, rather than wall or reflection conditions.
- Several strengths of temporary nonaxisymmetry penalties, followed by relaxation and persistence tests against validation/refinement errors.
- Nearby trajectory checks when assessing outgoing behavior; eigenvalues of the nonsymmetric \(\nabla V\) alone do not establish a quadratic outgoing inequality.
- Explicit accounting for vector-potential derivative cost: momentum involves second derivatives of \(A\), and the vorticity residual involves third derivatives.

Opus 5.5 collaboration was unavailable: the configured Bedrock profile could not retrieve credentials. No Opus model was used.