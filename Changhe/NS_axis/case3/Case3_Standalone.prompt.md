# CASE 3 — Complete exclusion of the axis-escape, planar ancient Euler branch

**Self-contained, single-prompt mission.** Codex is given no earlier conversation, no mathematical report, no file attachments and no other case prompt. Work on THIS case from the following fully specified physical NS model and branch conditions; do not substitute a standalone two-dimensional Euler classification.

## Exact target

Derive a complete contradiction for the **axis-escape gradient-record** branch from one fixed smooth finite-energy axisymmetric full NS solution satisfying the historical shape hypothesis (A) below. The extracted limit is a nonconstant bounded ancient **planar Euler** flow; such flows are not automatically forbidden. The decisive estimate must come from what a single finite-energy **viscous 3D NS trajectory** forces this limit to inherit. An actual single-fixed-datum singular NS construction meeting every assumption could instead refute the exclusion, but model planar Euler vortices, infinite-energy ancient flows, varying initial data and numerical candidates do NOT.

## Complete common mathematical setting (self-contained; no other prompt or report is supplied)

Work with **one fixed** smooth, decaying, divergence-free, axisymmetric initial velocity $u_0$ on $\mathbb R^3$, generating a maximal classical/mild solution $u$ of the **full three-dimensional Navier--Stokes equations**, with physical viscosity $1$:

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\Delta u,\qquad
\nabla\cdot u=0,\qquad u(0)=u_0.
\]

Assume, for a contradiction, that its first singular time is $0<T_*<\infty$. The **same fixed** $u_0$ and the **same physical solution** must underlie every record, estimate, subsequence, rescaling, and putative limit. Assume $E_0:=\|u_0\|_{L^2(\mathbb R^3)}^2<\infty$ and the explicit circulation condition $G:=\|r u_0^\theta\|_{L^\infty}<\infty$, where $G$ may be arbitrarily large but fixed. $G<\infty$ does **not** follow merely from finite energy. Take enough initial smoothness/decay to justify the classical solution, canonical pressure, spatial extrema and the displayed calculations; never silently add a smallness, Type-I, sign, compact-support or ancient-limit finite-energy assumption.

Use cylindrical coordinates $(r,\theta,z)$, $r=\sqrt{x_1^2+x_2^2}$, and write
\[
u=u^r e_r+u^\theta e_\theta+u^z e_z,
\qquad b=u^r e_r+u^z e_z,
\]
\[
\Gamma=r u^\theta,\qquad q=\frac{u^\theta}{r}=\frac{\Gamma}{r^2},\qquad
\omega^\theta=\partial_z u^r-\partial_r u^z,\qquad
\eta=\frac{\omega^\theta}{r},
\]
\[
\Delta_5=\partial_{rr}+\frac3r\partial_r+\partial_{zz}.
\]
The **exact coupled system** (with smooth axis extensions) is
\[
(\partial_t+b\cdot\nabla)\Gamma
 =\left(\partial_{rr}-\frac1r\partial_r+\partial_{zz}\right)\Gamma,
\]
\[
(\partial_t+b\cdot\nabla)q=\Delta_5 q-2\frac{u^r}{r}q,
\qquad
(\partial_t+b\cdot\nabla)\eta=\Delta_5\eta+\partial_z(q^2),
\]
\[
-\Delta_5\phi=\eta,\qquad u^r=-r\partial_z\phi,\qquad
u^z=2\phi+r\partial_r\phi.
\]
Here the physical angular velocity is $u^\theta=rq$. Do **not** set $b\cdot\nabla\eta=0$ or replace $q$ by an independently prescribed forcing: those are different models. In the five-dimensional lifted measure, $\operatorname{div}_5 b=2u^r/r$, **not zero**, although $\operatorname{div}_{\mathbb R^3}u=0$. Three-dimensional physical axisymmetric integration means $dx=2\pi r\,dr\,dz$.

Define the **historical** quantities, with suprema always taken over the *same full interval* $[0,t]$:
\[
\begin{aligned}
M(t)&=\sup_{0\le s\le t}\|u(s)\|_{L^\infty},
&S(t)&=\sup_{0\le s\le t}\|u^\theta(s)\|_{L^\infty},\\
D(t)&=\sup_{0\le s\le t}\|\nabla u(s)\|_{L^\infty},
&H(t)&=\sup_{0\le s\le t}\|\nabla^2u(s)\|_{L^\infty},\\
\Omega(t)&=\sup_{0\le s\le t}\|\operatorname{curl}u(s)\|_{L^\infty}.
\end{aligned}
\]
All derivative norms are Cartesian tensor norms, not just derivatives of scalar cylindrical coefficients. Historical $M,D,H$ must never be replaced by instantaneous values without a proof. The circulation maximum principle yields $\|\Gamma(t)\|_\infty\le G$; the energy inequality gives $\|u(t)\|_2^2+2\int_0^t\|\nabla u(s)\|_2^2ds\le E_0$. The rescaled total energy is generally **not** bounded, so an ancient limit is not assumed globally $L^2$.

At a genuine first-crossing record of $S(t)$, choose $t_n\uparrow T_*$ and $(r_n,z_n)$ with
\[
S_n=S(t_n)=|u^\theta(r_n,z_n,t_n)|\to\infty,\quad r_n>0.
\]
For the fixed sign attaining the positive signed maximum, the angular NS equation and $\partial_t |u^\theta|\ge0$, vanishing spatial first derivatives, and nonpositive Laplacian give the **record identity**
\[
-r_nu^r(r_n,z_n,t_n)\ge1.
\]
Thus $S_n/M(t_n)\le r_nS_n\le G$, and $S(t)^2\le G D(t)$ by $|u^\theta|/r\le|\nabla u|$. Audit attainment, time quantifiers, signs, and regularity before applying these formulas. A swirl **amplitude** record is not a $\Gamma$ record, and $\partial_z(q^2)$ vanishes at a smooth $u^\theta$ extremum; do not mistake this record for the strongest $\eta$ forcing point.

For an arbitrary **first rescaling of the actual raw velocity**,
\[
U_n(y,\tau)=B_n^{-1}u(x_n+\ell_n y,t_n+T_n\tau),\quad
P_n=\frac{T_n}{B_n\ell_n}p(x_n+\ell_n y,t_n+T_n\tau),
\]
its exact equation is
\[
\partial_\tau U_n+\beta_n U_n\cdot\nabla U_n+\nabla P_n
=\nu_n\Delta U_n,\quad \nabla\cdot U_n=0,\quad
\beta_n=\frac{T_nB_n}{\ell_n},\quad \nu_n=\frac{T_n}{\ell_n^2}.
\]
The backward rescaled time interval is $[-t_n/T_n,0]$; a **genuinely ancient** limit requires $t_n/T_n\to\infty$. The axis in the new coordinates must be tracked explicitly. Rescaling is not permission to subtract an arbitrary affine strain, use time-dependent Galilean frames, choose different initial data, invent a free pressure gradient, or change the physical PDE. Prove any standard mild/canonical-pressure claim, strong convergence needed for the nonlinearity, and convergence through the terminal record time $\tau=0$.

## General proof and evidence restrictions

- A theorem is successful only if it concerns this **single fixed finite-energy NS trajectory** and all the stated branch hypotheses. Independently constructed Euler/NS ancient fields, toy scalar growth laws, changing-data sequences, and numerical flows may **test a lemma** but are never fixed-data singularity counterexamples.
- Separate **proved facts**, **candidate lemmas to verify**, **additional hypotheses**, and **unproved conclusions**. Verify even the established-looking estimates in this prompt; correct a false formula and continue research rather than building on it.
- Avoid nonlinear Grönwall/exponential closures in uncontrolled meridional quantities. Seek critical-scale, polynomial, signed, transport, localization, cancellation, comparison, pressure or diffusion arguments; estimates must survive arbitrarily large finite $G$.
- Check every length, time, amplitude and viscosity power; the original axis, $r=0$, $r\to\infty$, high-frequency concentration, pressure far fields, quantifier order, changing observation cylinders, and potentially divergent normalized energy.
- Do not apply a bounded ancient **Navier--Stokes** Liouville theorem to an ancient **Euler** flow. Do not infer nontriviality from a gradient point value when only $C^0$ convergence is known, or infer non-extraction from failure to prove a sufficient bound.
- You may independently consult published papers if the environment permits, but **no attached report, previous chat, external task specification, or local research file will be supplied**. Everything necessary to understand this mission is written in this one prompt. Any external theorem you use requires its precise hypotheses and a proof of applicability; do not rely on an inaccessible attachment.

## The precise Case 3 predicate and the genuine Euler limit

Assume the **historical shape condition** (A) for every sufficiently late time:
\[
\boxed{M(t)H(t)\le C_*D(t)^2}\tag{A}
\]
with fixed $C_*<\infty$. In addition, suppose there is **no** true swirl first-crossing sequence for which the full velocity normalized on its own record radius is uniformly bounded by the **same** constant on all fixed space/ancient-time cylinders and has vanishing Oseen-kernel weighted $|y|^{-4}$ quadratic tails on the very same common sequence. This is a strict branch negation, not merely a gap in some particular proof of compactness. For reference, the candidate swirl scaling is
\[
W_n(y,\tau)=\frac{u(r_ny',z_n+r_ny_3,s_n+(r_n/S_n)\tau)}{S_n},
\]
and the witness pair would be $\limsup_n\sup_{B_R\times[-A,0]}|W_n|\le K$ with one $K$ for every fixed $R,A$ and $\lim_{R\to\infty}\limsup_n\sup_{[-A,0]}\int_{|y|>R}|W_n|^2|y|^{-4}dy=0$ for every $A$.

Reconstruct (rather than silently assuming) the known branch reduction:
\[
\boxed{\frac{S(t)}{M(t)}\to0,\qquad \frac{D(t)}{M(t)^2}\to0\quad(t\uparrow T_*).}\tag{B}
\]
The first implication follows by choosing true historical swirl first crossings when $S/M$ does not tend to zero; the record compression $-ru^r\ge1$ and $rS\le G$ make their swirl-radius scalings nondegenerate, while $S/M\ge c$ gives all-space velocity boundedness and a $C/R$ quadratic far tail. The second follows, conditionally on checking all compactness hypotheses, from the **bounded ancient no-swirl NS / planar NS Liouville** results applied to a *different* standard positive-viscosity scaling when $D/M^2$ does not vanish. Neither step permits applying an NS Liouville theorem directly to an Euler limit.

Select actual **historical gradient first-crossing records**
\[
D_n=D(t_n)=|\nabla u(x_n,t_n)|\to\infty,\qquad M_n=M(t_n),\quad
x_n=(r_n,0,z_n),
\]
and put
\[
\ell_n=\frac{M_n}{D_n},\quad T_n=\frac1{D_n},\quad
\nu_n=\frac{D_n}{M_n^2}\to0,\quad
\alpha_n=\frac{r_n}{\ell_n}=\frac{r_nD_n}{M_n}.
\]
**Case 3 is the common-subsequence regime $\alpha_n\to\infty$.** Center the coordinates at the true record $x_n$, after a fixed rotation around the original symmetry axis:
\[
U_n(y,\tau)=\frac{u(x_n+\ell_n y,t_n+\tau/D_n)}{M_n},\qquad
\partial_\tau U_n+U_n\cdot\nabla U_n+\nabla P_n=\nu_n\Delta U_n.
\]
No affine background or time-dependent axial/azimuthal velocity is subtracted. These are the **original physical velocities** with one time-independent center per $n$.

By (A) and the historical bounds, for all available past times and all $y$,
\[
\boxed{\|U_n\|_\infty\le1,\quad \|\nabla U_n\|_\infty\le1,\quad
\|\nabla^2 U_n\|_\infty\le C_*,\quad |\nabla U_n(0,0)|=1.}\tag{C}
\]
Prove pressure bounds from the canonical physical pressure, including near/far cancellation and absence of parasitic harmonic forcing. Then establish strong $C^1_{x,\mathrm{loc}}$ convergence on cylinders ending at $\tau=0$. (A) is essential for preserving the gradient record: merely $C^0$ convergence would not do. A valid common subsequence yields
\[
\|U\|_\infty\le1,\quad |\nabla U(0,0)|=1,\quad
\partial_\tau U+U\cdot\nabla U+\nabla P=0,
\qquad \tau\le0.
\]
The original axis lies a distance $\alpha_n\to\infty$ from the origin in these variables. Derive carefully from **actual axisymmetry** and the geometry of rotations that, on each fixed compact set in $(y,\tau)$,
\[
\boxed{U(y,\tau)=(V_1(y_1,y_3,\tau),\ 0,\ V_3(y_1,y_3,\tau)),\qquad
\partial_{y_2}U\equiv0.}\tag{PLANAR}
\]
This uses disappearance of normalized swirl $S_n/M_n\to0$, not an artificial planar ansatz. The limiting planar vorticity is
\[
\zeta=\partial_{y_3}V_1-\partial_{y_1}V_3
\quad(\text{the }e_2\text{-component of }\operatorname{curl}U),
\]
and solves $\zeta_\tau+V_1\partial_{y_1}\zeta+V_3\partial_{y_3}\zeta=0$. Since $U$ is bounded, planar, divergence-free, and spatially nonconstant, $\zeta\not\equiv0$ (else its components are bounded harmonic functions on $\mathbb R^2$ and thus constant). The complete smooth bounded planar flow preserves vorticity $L^\infty$ norm backward:
\[
\boxed{\|\zeta(\cdot,-A)\|_{L^\infty(\mathbb R^2)}
=\|\zeta(\cdot,0)\|_{L^\infty}>0\quad\forall A\ge0.}\tag{RIGIDITY}
\]
Check the exact ancient regularity and measure-preserving flow justification. The label "two-dimensional Euler" does not itself supply a contradiction.

## Quantitative necessary restrictions already suggested by finite physical energy

These formulas are provided as specific candidate lemmas to audit, **not** as a complete exclusion. Let $E_0=\|u_0\|_2^2$. The fact that a nonzero normalized gradient survives with $\|\nabla^2U_n\|_\infty\le C_*$ should give, on an $O(\ell_n)$ physical ball, a velocity amplitude $\gtrsim C(C_*)^{-1}M_n$. Since the real 3D velocity is axisymmetric, this feature is repeated around a torus of radius $r_n\gg\ell_n$. Its volume is $\asymp r_n\ell_n^2$; hence the candidate inequality is
\[
\boxed{\frac{r_nM_n^4}{D_n^2}\le C(C_*)E_0.}\tag{E}
\]
Prove the step from gradient record to a *nonzero velocity on a ball*, including how the Hessian bound controls its size and how the entire rotating torus remains disjoint enough for an energy lower bound. It then follows algebraically, using $\nu_n=D_n/M_n^2$, that
\[
\boxed{r_n\le C(C_*)E_0\nu_n^2\to0,
\qquad \frac{D_n^3}{M_n^5}\ge\frac{c(C_*)}{E_0}\,\alpha_n\to\infty.}\tag{E'}
\]
Thus **the physical radii $r_n$ approach the original axis even though the original axis escapes on the far smaller normalized length $\ell_n$**. Confusing these two statements is a serious error.

A stronger proposed genuine-prelimit vorticity-persistence mechanism yields a fixed $\delta,c_U>0$ and for all large $n$
\[
\frac{D(t_n-h/D_n)}{D_n}\ge c_U
\quad \text{for all }0\le h\le \delta\alpha_n.
\tag{LONG-WINDOW}
\]
This is a window increasing to infinite *normalized* length, corresponding to a shrinking *physical* interval of length $\delta r_n/M_n$. It must be proved on the physical solution by cutoffs/transport/viscosity and axisymmetry, **not** by promoting convergence on every fixed window to a changing window $h=h_n$. An associated physical dissipation lower bound is
\[
\int_{t_n-\delta r_n/M_n}^{t_n}\int_{\mathbb R^3}|\nabla u(x,t)|^2dx\,dt
\ \ge c_U r_n^2M_n,
\tag{DISS}
\]
which, combined with finite total physical dissipation and a shrinking physical window approaching $T_*$, gives
\[
\boxed{r_n^2M_n\to0.}\tag{NECESSARY}
\]
Even if all these statements withstand audit, **none is by itself a contradiction**; potential $M_n,D_n,r_n$ growth regimes may satisfy them simultaneously. Distinguish carefully between a restriction on the *same fixed NS solution* and toy numerical exponent choices that merely test compatibility.

## Exact sufficient exclusion target (no extra hypotheses allowed)

Define for fixed $A\ge0$ the historical backward-gradient ratio
\[
d(A)=\limsup_{n\to\infty}\frac{D(t_n-A/D_n)}{D_n}.
\]
If the **physical NS trajectory** forced
\[
\boxed{\lim_{A\to\infty}d(A)=0,}\tag{TARGET-3}
\]
then by $\|\zeta(-A)\|_\infty\lesssim d(A)$ and (RIGIDITY), the Euler limit would have zero vorticity, and a bounded harmonic planar velocity would be constant, contradicting the gradient record. This is **a sufficient target**, not a known estimate. A stronger common target useful for both finite-axis and axis-escape geometries is
\[
\liminf_{A\to\infty}\sqrt{1+A}\,d(A)=0;
\]
but Case 3 only needs the weaker $d(A)\to0$. The order of limits ($n$ first, then $A$) is mandatory.

A genuine gradient Type-I upper bound $D(t)(T_*-t)\le K$ would imply TARGET-3 by
\[
\frac{D(t_n-A/D_n)}{D_n}
\le\frac{K}{D_n(T_*-t_n)+A}\le\frac KA.
\]
**Type-I is not assumed, not proved by the historical shape estimate (A), and cannot be smuggled in.** A pressure-Hessian calculation may give $D'(t)\lesssim D(t)^2$, but this points in the wrong direction: backward integration yields a **lower**, not an upper, gradient bound. A planar Euler Liouville theorem that ignores the true physical prelimit history would not close this case.

## Actual research routes: produce complete derivations, not slogans

1. **A growing-window contradiction:** strengthen (LONG-WINDOW), quantify its minimal dissipation cost using axisymmetric toroidal copying and compare with the full energy budget. Show rigorously that any nonzero planar ancient vorticity must consume an impossible amount of finite physical dissipation, or isolate and close the exact missing power of $r_n,M_n,D_n$.
2. **Localized backward vorticity depletion:** seek a physical estimate strong enough to force the vorticity of the limit to vanish on one fixed planar disk (plus harmonic gradient control there), rather than TARGET-3 globally. All 3D/2D changes of variables, cutoffs, pressure terms, and time intervals must be explicit.
3. **Pressure and temporal geometry:** using (A), the exact NS gradient equation, canonical pressure, possible Euler-length/strain identities and finite energy, produce a **backward upper** gradient bound. Reject any proof that quietly exchanges instantaneous for historical norms or inverts the direction of $D'(t)\lesssim D^2$.
4. **Axis-escape geometry beyond isotropic torus:** analyze whether finite $G$ and the physical distance $r_n\to0$ prohibit persistent planar vorticity, perhaps through additional periodicity/geometric variation/averaged material constraints. Do not infer a false strong Liouville theorem for generic bounded 2D Euler.
5. **Fixed-past versus middle-past transport:** the tiny recent normalized source is not proof that the Euler vortex had no earlier history. Examine actual time-dependent swirl and meridional vorticity, and any surviving mass/energy from the *same* original $u_0$.
6. **Adversarial sharpness:** test every inequality at $\alpha_n\to\infty$ and $r_n\to0$, for arbitrarily large finite $G$, and with sequences satisfying both (E') and (NECESSARY). A compatible growth law is not a counterexample unless realized by a true fixed-data NS singularity.

## Final mathematical acceptance gate

Prove, without adding Type-I or an arbitrary ancient-energy assumption, that **Case 3 cannot occur under (A), the no-swirl-extraction branch, and one fixed finite-energy full NS datum**; alternatively settle it with a rigorously verified actual fixed-datum finite-time NS singularity realizing the leaf. A candidate planar Euler limit, (E) or (DISS), a conditional vorticity-depletion statement, or a different model flow does not count as completion.

## Mandatory minimum 24-hour Codex research and independent audit protocol

**Do not treat an exploratory derivation, a conditionally true lemma, a more favorable exponent, a numerical experiment, a suspected obstruction, or an unverified proof sketch as completion.** The research must continue for **at least 24 hours of documented actual work on this case alone**, unless a hard tool/session/system limit forcibly terminates execution. Four cases do not share one 24-hour budget. If the complete theorem appears earlier, devote the remaining documented research time to independent reconstruction of the proof, counterexample searching against each intermediate lemma, stress tests, removing hidden assumptions, and polishing a fully rigorous manuscript. Do not manufacture elapsed time or claim to have run additional agents when you have not. A prompt cannot override an external hard runtime limit; if that limit intervenes, checkpoint honestly for resumption, without asserting that the time requirement was satisfied.

1. **At the start:** inspect the actual system clock and write the real UTC start time to `RUN_STATUS.md`; create `WORKLOG.md`, `CHECKLIST.md`, `LEMMA_LEDGER.md`, `FAILED_APPROACHES.md`, `PROOF_MANUSCRIPT.md`, `INDEPENDENT_AUDIT.md` and `FINAL_REPORT.md` in the current work directory. These are **output** files to create, not input documents to look for. They may be written in English only. Use exact algebra/computation scripts if helpful but **not** in place of analysis. Persist progress after each substantial attempt and at least once per hour of active work.
2. Maintain a log of actual time worked, issue attacked, attempted inequality, whether it held, the obstruction, and the next alternate approach. Distinguish idle elapsed time from research work. Keep a lemma ledger with `PROVED`, `FALSE`, `CONDITIONAL`, or `OPEN`, with hypotheses and proof locations.
3. Allocate a genuinely independent adversarial verification stage (a separate real agent if supported; otherwise a separate, explicitly independent pass): attempt to invalidate each lemma using exact endpoint tests, alternative subsequences, physical units, axis regularity, nonlocal pressure tails, missing nonlinear terms, unbounded parameters, and fixed-data provenance. A proof rejected in audit returns to research, not to the final answer.
4. Work successively through distinct mechanisms. If a route fails, repair it or try a materially different argument. Do not recycle a failed hypothesis with a new symbol. Do not stop on an `OPEN` or `CONDITIONAL` lemma before the 24 hours of active research have been documented (unless forced out by the environment).
5. **Completion labels:** use `COMPLETE_THEOREM_VERIFIED` only when every arrow is proved under the precise input hypotheses and independently audited. Use `COMPLETE_FIXED_DATA_COUNTEREXAMPLE_VERIFIED` only for an actual single smooth finite-energy initial datum and its rigorously verified singular NS solution satisfying the exact branch predicate, if this is logically relevant to the claim. A standalone ancient solution, toy function or numerical profile never qualifies. In an incomplete forced termination write `UNRESOLVED_NOT_ACCEPTED` and identify the first missing implication and how to resume. Do not present partial results as an accepted final mathematical answer, and do not fake a proof to avoid this status.
6. When the environment approaches a hard limit, write `RESUME_HERE` in `RUN_STATUS.md` with the precise current mathematical obstacle, latest valid bound and constants, unverified step, next experiment/proof avenue, timestamp, and honest accumulated **active** research time. A later continuation must resume the same case from that checkpoint, not start a fresh paper or pretend to have worked overnight.
7. The final accepted output must be one stand-alone English research manuscript with: exact theorem, assumptions, fixed-data branch predicate, fully checked scaling, complete proof, explicit source of each nontrivial fact (proved here or precisely cited published theorem), complete treatment of nonlinear terms and pressure, endpoint and limit-order checks, independently written audit, and a short explanation of why the final theorem **closes the whole specified case**. A time log is necessary but never substitutes for a proof.

**You are not authorized to assume the desired conclusion, to make up a singular solution, or to report a false success.** The aim is a complete result, not the appearance of completion. Start the mathematical investigation immediately after creating the logs; do not spend the full research budget merely surveying the literature.
