# CASE 4 — Close the missing universal first-normalization and nontrivial ancient-limit extraction theorem

**This is one fully self-contained Codex prompt.** You receive no older prompt, report, conversation, local file, or companion mission. The entire physical setting, known selection mechanisms, precise obstruction, candidate scales, prohibitions, and finish line are below. Do NOT search for a previous research file. This is the case that must be solved before a three-successful-limit classification can be called an exhaustive singularity classification.

## Exact mathematical goal and status

The proposed three successful types of ancient limits are: (I) **positive-viscosity full axisymmetric NS with nonzero swirl**, (II) **inviscid no-swirl axisymmetric Euler with the symmetry axis at finite normalized distance**, and (III) **inviscid planar Euler when the original symmetry axis escapes to infinite normalized distance**. These are descriptions **after a successful extraction**, not a proof that every possible singular solution admits such an extraction.

**Case 4 is the missing alternative: all currently tested physically selected first normalizations may lose compactness, boundedness, terminal nontriviality, or the proper pressure/PDE class, so no useful bounded spatially nonconstant ancient limit has been proved.** This is an **unresolved extraction obstacle**, NOT a claim that a real fixed-data singular solution realizing non-extraction exists. No zero, spatially constant, affine, finite-age, unbounded, or merely frozen-profile limit counts as a successful fourth PDE leaf.

**Your required complete theorem:** For *every* hypothetical finite-time singularity of the single fixed-data axisymmetric full NS problem below, prove that there exist real singularity records and a physically justified **first normalization** (not chosen retrospectively after observing a trivial limit) for which, along one single common subsequence,
\[
\boxed{\begin{aligned}
&U_n\to U\quad\text{strongly enough locally on }\mathbb R^3\times(-\infty,0]
\text{ including }\tau=0,\\
&\sup_{y\in\mathbb R^3,\ \tau\le0}|U(y,\tau)|<\infty,\\
&U\text{ is spatially nonconstant (equivalently }\nabla U\not\equiv0),\\
&U\text{ solves a rigorously derived ancient PDE with the correct pressure class}.
\end{aligned}}\tag{GOAL}
\]
**OR** prove directly from the physical system that the remaining genuine no-useful-extraction alternative is impossible. If the proposed universal selection theorem is false, a conclusive counterexample must come from **one actually constructed smooth finite-energy axisymmetric initial datum whose true NS solution has a proven finite-time singularity and violates the precisely formulated selection claim**. Functional toy fields and changing-data solutions do not suffice.

### Critical distinction from Cases 1--3

**DO NOT ASSUME** the historical shape inequality $M(t)H(t)\le C_*D(t)^2$, any Type-I bound, H2 compactness, bounded stream potential, BMO smallness, self-similarity, an affine background to be subtracted, or ancient global finite energy. This case must operate on the original full NS system with smooth finite-energy fixed data and finite $G$ only. If your selected theorem needs one of those extra assumptions, it is partial and NOT a solution to Case 4.

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

## What the physical equations already imply about possible first selections

**1. A genuine initial swirl branch can be extracted when it is comparable to the total speed.** If
\[
\limsup_{t\uparrow T_*}\frac{S(t)}{M(t)}>0,
\]
choose historical first-crossing swirl records for which $S_n/M(t_n)\ge c>0$, and use the record-radius scale
\[
W_n(y,\tau)=\frac{u(r_ny',z_n+r_n y_3,t_n+(r_n/S_n)\tau)}{S_n}.
\]
Because $-r_nu^r\ge1$ and $r_nS_n\le G$, one has $c\lesssim r_nS_n\le G$, hence $\nu_n=(r_nS_n)^{-1}$ remains positive and finite; the rescaled velocity is **globally** bounded by $1/c$ on the available past and $|y|^{-4}$ quadratic nonlinear kernel tails decay like $C/(c^2R)$. The time depth diverges. Verify the mild kernel proof of compactness **through terminal time** and the nonzero record $|W_n^\theta(1,0,0)|=1$. This yields a bounded, nonconstant ancient **full NS** limit if all stated analytic steps check out. A failure of a weaker observation scale does not invalidate this actual first-crossing extraction.

**2. The only genuinely difficult sector is the separated-speed regime.** If comparable swirl records do not occur, then
\[
\boxed{S(t)/M(t)\to0.}\tag{SEP}
\]
Here historical gradient/vorticity record analysis plus Liouville results for bounded ancient **positive-viscosity** no-swirl/planar NS suggest the provable limit
\[
\boxed{D(t)/M(t)^2\to0\qquad\text{and}\qquad \Omega(t)/M(t)^2\to0.}\tag{INVISCID}
\]
Audit both claims under the **original** assumptions, with no Hessian relation. The argument for $D/M^2\to0$ is by contradiction: a true historical gradient first crossing, length $1/M_n$, velocity scale $M_n$ and physical parabolic time scale $1/M_n^2$ yield a bounded positive-viscosity ancient NS limit with a nonzero gradient if that ratio stays positive; swirl becomes negligible; the corresponding bounded ancient no-swirl NS or planar NS rigidity should rule it out. Distinguish convergence needed to retain a **gradient** from convergence needed just for velocity. These positive-viscosity NS theorems do NOT eliminate the inviscid Euler case once $D/M^2\to0$.

**3. A natural Euler-scaled gradient first normalization has good velocity bounds but may lose visible variation.** Take a real historical gradient first-crossing record $(x_n,t_n)$ and set
\[
B_n=M_n=M(t_n),\quad \ell_n=\frac{M_n}{D_n},\quad
T_n=\frac1{D_n},\quad \nu_n=\frac{D_n}{M_n^2}\to0,
\]
\[
U_n(y,\tau)=\frac{u(x_n+\ell_n y,t_n+\tau/D_n)}{M_n}.
\]
Then
\[
\boxed{\|U_n\|_\infty\le1,\quad \|\nabla U_n\|_\infty\le1,
\quad|\nabla U_n(0,0)|=1.}\tag{GRAD}
\]
But *without* the absent shape hypothesis,
\[
\|\nabla^2U_n\|_\infty\le\frac{M_nH_n}{D_n^2}
\]
may diverge. Strong local $C^0$ compactness (if established including time and canonical pressure) can lose the recorded gradient. The elementary **non-NS diagnostic** $f_n(x)=n^{-1}\sin(nx)$ has $\|f_n'\|_\infty=1$, $f_n'(0)=1$, but $f_n\to0$ uniformly; this shows why gradient normalization plus only $C^0$ convergence is insufficient. It is **not** a counterexample along a real fixed-data NS singularity. Do not change the logical status of this illustration.

A useful positive certificate would be a genuinely inherited **fixed-scale spatial oscillation** at some selected terminal or ancient time, e.g. for some fixed $R>0$, $c>0$,
\[
\boxed{\limsup_{n\to\infty}\sup_{|y|\le R}
|U_n(y,0)-U_n(0,0)|\ge c.}\tag{OSC}
\]
Stronger space-time versions are allowed; one certificate must hold **on the same subsequence** that has compactness, boundedness, correct ancient depth and a limit PDE. A lower bound at a *vanishing* normalized radius is not enough. A successful intrinsic scale **selection theorem must prove (OSC) or equivalent as part of selecting the scale**. Do not append an after-the-fact decision question "does the limit happen to be nonconstant?" and count NO as solved.

**4. Finite original energy and vorticity yield some genuine restrictions, but not (OSC).** A true historical velocity peak and gradient bound imply a ball of radius $\asymp M/D$ containing velocity $\gtrsim M$ at the time of the peak, hence
\[
\boxed{M(t)^5\le C E_0 D(t)^3.}\tag{ENERGY-BALL}
\]
This yields $M/D\lesssim E_0^{1/5}D^{-2/5}\to0$ on high-gradient records. A heat-kernel/vorticity interpolation also suggests
\[
M(t)\le C E_0^{1/5}\Omega(t)^{3/5},
\]
using the smoothing identity for $u$ and optimizing its length scale. Independently prove the assumptions and dimension powers. These bounds do NOT force normalized Hessians to remain controlled and do not guarantee a fixed-scale oscillation on a *gradient* record. A proposed vorticity clock with $\ell_n=M_n/\Omega_n$ must separately prove spatial regularity: **$\|\nabla u\|_\infty$ cannot be replaced by $\|\omega\|_\infty$** through an unproved $L^\infty$ Calderón--Zygmund estimate.

**5. Some compactness may be accessible even without (A), but that is not the missing nonconstancy step.** For uniformly bounded Lipschitz velocity, investigate the canonical pressure gradient via increments
\[
\nabla p(x)=\int_{\mathbb R^3}K(z)
\big(u(x-z)-u(x)\big)\otimes\big(u(x-z)-u(x)\big)\,dz,
\qquad |K(z)|\lesssim |z|^{-4},
\]
where this is a *schematic representation* needing correct tensor kernel, angular cancellation, possible local distributions, and convergence proof. Differences are $O(|z|)$ near zero and bounded far away; therefore a uniform normalized pressure-gradient bound is plausible, allowing terminal-inclusive time equicontinuity of $U_n$ and an inviscid Euler distributional limit. **Prove**, rather than assert, how viscosity and pressure appear in its temporal modulus, how global pressure is normalized, and how strong velocity convergence passes $U_n\otimes U_n$. Even a sound bounded ancient Euler *constant* limit would not complete the selection theorem.

**6. Actual-speed doubling times only give one temporal direction.** At first crossings of dyadic velocity levels $t_j$, pressure/NS bounds may yield
\[
D(t_j)(t_j-t_{j-1})\gtrsim c,
\]
a **lower** bound. A candidate route to normalized nontriviality needs an *upper* bound on relevant growth intervals or another geometric oscillation control. Do not reverse inequalities. A carefully chosen Lagrangian velocity contrast, energy concentration or local vorticity geometry may be a better intrinsic certificate than a gradient point value. If you introduce a time-dependent center or Galilean shift, derive the induced inertial pressure exactly; a time-dependent frame or affine subtraction is not an unforced NS normalization.

## Exact structure of the 'no usable extraction' question

Do NOT define Case 4 as "the gradient record limit is constant" and then claim it excludes all possible limits. With $S/M\to0$, the failure of one scale leaves open other **first** normalizations: real velocity-increment scales; a genuine vorticity or strain clock; a local swirl core whose global $M/S$ diverges but whose normalized **local** meridional velocity and weighted far tails are controlled; independent axial versus radial lengths; and non-artificial choices of the singularity center. In every candidate, require **at once**:

1. A **computable first selection rule** from the physical $u$, using real first-crossing records or a quantitatively specified observable, with no posterior second zoom or subtraction of a hidden affine background.
2. A single common subsequence and a complete range $\tau\in(-\infty,0]$ with a **globally bounded** limiting velocity, not merely an $L^\infty_{\mathrm{loc}}$ field whose bound depends on cylinder size.
3. Strong compactness sufficient to pass the actual rescaled PDE and canonical pressure, **including the terminal record**; explain any stress defects from weak rather than strong limits.
4. A fixed-scale spatial nonconstancy witness surviving the **same** convergence. If the limit is curl-free, audit possible constant/potential-affine degeneracy under global boundedness.
5. A physically meaningful limiting equation with its *actual* coefficients $\nu_n=T_n/\ell_n^2$ and $\beta_n=T_nB_n/\ell_n$ and its correct ancient mild/weak/pressure class. A scale that freezes the equation but only preserves a trivial spatial constant is not useful.

### Anisotropic first scales are not ruled out by fiat

If physically compelled to choose transverse and axial lengths $\ell_{\perp,n}$ and $\ell_{z,n}$ separately, set $a_n=\ell_{\perp,n}/\ell_{z,n}$, and for a uniform velocity amplitude $B_n$ derive (rather than incorrectly reusing the isotropic formula)
\[
\partial_\tau U_n-\frac{T_n}{\ell_{\perp,n}^2}
(\Delta_{y'}+a_n^2\partial_{33})U_n
+\frac{T_nB_n}{\ell_{\perp,n}}
\big(U_n'\cdot\nabla_{y'}+a_nU_{n,3}\partial_3\big)U_n
+(\nabla_{y'}P_n,a_n\partial_3P_n)=0,
\]
\[
\nabla_{y'}\cdot U_n'+a_n\partial_3U_{n,3}=0,
\quad P_n=\frac{T_n}{B_n\ell_{\perp,n}}p.
\]
If $a_n\to0$ or $\infty$, interpret the singular limit carefully: do not invent a named new ancient PDE before proving full compactness and a surviving nonconstant observable. Axis-centered versus record-centered coordinates must be tracked, not quietly swapped.

## Research program aimed at a theorem, not a taxonomy

A. **Select an intrinsic oscillation or flux scale.** Try first-crossing velocity-increment records (for example, a minimal radius carrying a fixed fraction of a genuinely recorded total velocity contrast), vorticity/strain-dominated scales, energy-ball plus pressure acceleration, and true nonlinear growth times. Prove one physical quantitative oscillation certificate without inserting (A). Check whether selecting a smaller scale causes loss of global Lipschitz bound or collapse of ancient age, and repair it from the full NS dynamics rather than from arbitrary normalization choices.

B. **Combine regularity, compactness and nontriviality into ONE selection theorem.** Prove the global normalized velocity bound, backward age, strong terminal convergence, correct pressure equation, and spatial oscillation on the **same chosen sequence**. If you succeed in only one or two, that is partial. Do not reassign a different subsequence after proving each property unless a legitimate common diagonal extraction preserves every property.

C. **Use the full axisymmetric $q,\eta,\Gamma$ system where general-vector methods fail.** Swirl is truly coupled, $\|\Gamma\|_\infty\le G$, and near-axis geometry changes with the selected scale. Attempt to rule out the high-frequency, small-amplitude degeneration of meridional velocity by its transport, elliptic recovery, pressure and finite physical dissipation. Do not assume $q$ independent, $\eta$ uniformly $L^1$, or favorable signs of $\partial_z(q^2)$.

D. **Adversarially explore the failure alternative.** Construct bounded-function and PDE-compatible *tests* showing what the usual inequalities fail to control, but label their exact evidential class: a functional sequence or independently chosen ancient flow is NOT a genuine fixed-data singular NS counterexample. To prove a selection theorem false for actual singular solutions, you need a true fixed-data example, including a proof of singularity. A failed proof of compactness is not a theorem of noncompactness.

E. **A logically complete decision statement.** At the end, either prove the universal first-normalization theorem (GOAL), or prove an independently valid physical NS estimate directly eliminating the no-extraction alternative. In the theorem, the alternatives positive-viscosity NS / finite-axis Euler / axis-escape planar Euler must be classified **only after** sufficient convergence is proved and without claiming they exhaust every possible anisotropic/equation-coefficient regime unless you prove it. You may find an entirely new, genuinely useful ancient PDE balance; prove its derivation and rigidity relevance rather than creating a cosmetic fourth label.

## Final mathematical acceptance gate

**No additional assumptions beyond one fixed smooth, decaying, finite-energy axisymmetric 3D NS datum, finite arbitrary $G$, and a hypothetical first finite singular time.** A complete success must establish one genuinely nonconstant globally bounded ancient PDE limit from a physically selected first scaling on every such hypothetical singular trajectory, or a fully rigorous direct theorem that leaves no true no-extraction branch; a real fixed-datum counterexample would have to settle actual finite-time NS singularity. A proof only under $MH\le C_*D^2$, or only of local $C^0$ compactness, or only a conditional lemma about (OSC), is **not accepted**.

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
