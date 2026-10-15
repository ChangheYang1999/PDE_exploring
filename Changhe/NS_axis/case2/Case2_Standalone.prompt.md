# CASE 2 — Complete exclusion of the finite-axis, zero-swirl ancient axisymmetric Euler branch

**Single self-contained prompt for Codex.** You receive no earlier work, no files, no research history and no other case prompt. All the equations, logical prerequisites, scales, available quantitative leads and the open goal are included here. Do not stop at another conditional Liouville theorem.

## Exact desired result

**Prove that the finite-axis ancient Euler leaf described below cannot be produced by any one fixed smooth, decaying, finite-energy, axisymmetric full NS trajectory satisfying its original hypotheses.** Prove the contradiction in the *physical* NS equations, not by declaring all ancient Euler flows trivial (that statement is false). As the logically opposite decisive outcome, an actual one-fixed-datum finite-time NS singularity satisfying the whole branch predicate would refute the exclusion claim; merely giving an Euler vortex ring or independent ancient Euler solution does not.

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

## The historical shape condition, the initial swirl split, and the Case 2 records

In this case assume, for all sufficiently late times, the **extra historical** condition
\[
\boxed{M(t)H(t)\le C_* D(t)^2}\tag{A}
\]
for a fixed finite $C_*$. This is not claimed for all NS solutions. Begin with the branch where **no genuine swirl first-crossing record sequence** admits the following pair of witnesses on one sequence: a universal bound $K$ for full swirl-radius-rescaled velocity over *all* fixed normalized cylinders and the vanishing weighted kernel tail
\[
\lim_{L\to\infty}\limsup_{n\to\infty}
\sup_{-A\le\tau\le0}\int_{|y|>L}|W_n(y,\tau)|^2|y|^{-4}dy=0
\quad(\forall A<\infty),
\]
where $W_n(y,\tau)=S_n^{-1}u(r_ny',z_n+r_ny_3,t_n+(r_n/S_n)\tau)$. Call this explicit **negation** `NO-SWIRL-EXTRACTION`; it means **every candidate record sequence fails at least one of the two witnesses**, not merely that someone has failed to prove a compactness lemma. Verify its quantifiers, including every further subsequence.

A key preliminary reduction to reconstruct: if $\limsup_{t\uparrow T_*}S(t)/M(t)>0$, genuine first-crossing swirl records have $S_n/M(t_n)\ge c>0$, so automatically $\|W_n\|_\infty\le1/c$ on their entire past and the weighted tail is $\lesssim(c^2L)^{-1}$. The finite positive $r_nS_n$ then gives a nonzero-swirl bounded ancient mild full NS extraction, contradicting `NO-SWIRL-EXTRACTION`. Hence that branch implies
\[
\boxed{S(t)/M(t)\to0.}\tag{B1}
\]
Next, if $D(t)/M(t)^2$ stays bounded away from zero on a gradient-record subsequence, unit-viscosity rescaling at length $1/M_n$ retains a nonzero normalized gradient and loses swirl. Bounded mild NS compactness and the known Liouville results for bounded ancient *no-swirl axisymmetric NS* or *two-dimensional NS* then lead to a contradiction (the axis can be finite or escape). Audit the applicability of those NS theorems and their pressure/terminal trace conditions. The expected implication is
\[
\boxed{D(t)/M(t)^2\to0.}\tag{B2}
\]
The published KNSS bounded ancient NS theorems may be verified and invoked with their exact hypotheses; **do not use them as Euler theorems**.

Choose **real historical first-crossing gradient records** $(x_n,t_n)$, so
\[
D_n=D(t_n)=|\nabla u(x_n,t_n)|\to\infty,\quad M_n=M(t_n),\quad
x_n=(r_n,0,z_n),
\]
with one fixed rotation about the original axis for each record. Set
\[
\ell_n=\frac{M_n}{D_n},\qquad T_n=\frac1{D_n},\qquad
\nu_n=\frac{D_n}{M_n^2}\to0,\qquad
\alpha_n=\frac{r_n}{\ell_n}.
\]
**Case 2 is the subsequential geometric alternative** $\alpha_n\to\alpha_*<\infty$ (including $\alpha_*=0$). Center at the original symmetry axis at height $z_n$, which is a *time-independent* translation along the axis, not a moving-frame subtraction:
\[
U_n(y,\tau)=\frac{u((0,0,z_n)+\ell_n y,t_n+\tau/D_n)}{M_n}.
\]
The actual record lies at $y_n=(\alpha_n,0,0)$, so $|\nabla U_n(y_n,0)|=1$. The exact rescaled equation is
\[
\partial_\tau U_n+U_n\cdot\nabla U_n+\nabla P_n=\nu_n\Delta U_n,
\qquad \nabla\cdot U_n=0.
\]
Historical bounds and (A) imply, for every available past time and all space,
\[
\boxed{\|U_n\|_\infty\le1,\qquad \|\nabla U_n\|_\infty\le1,
\qquad\|\nabla^2U_n\|_\infty\le C_* .}\tag{C}
\]
One should prove canonical pressure estimates and a terminal-inclusive temporal modulus: for example $\|\nabla P_n\|_\infty\lesssim C(C_*)$, $\|\partial_\tau U_n\|_\infty\lesssim C(C_*)$, and then $C^1_x$ compactness up to $\tau=0$. For the pressure estimate, exploit the divergence-free velocity-increment representation or near/far kernel split, not an arbitrary harmonic pressure. The gradient record then survives: $|\nabla U(y_*,0)|=1$.

The candidate limiting $U$ is **globally bounded, nonconstant, axisymmetric and without swirl**, and solves **Euler**, not NS:
\[
\partial_\tau U+U\cdot\nabla U+\nabla P=0,
\quad\nabla\cdot U=0,\quad U^\theta=0,
\quad \tau\le0.
\]
The finite axis survives. In cylindrical variables its transported scalar satisfies
\[
\boxed{\partial_\tau\eta_U+U\cdot\nabla\eta_U=0,
\qquad\eta_U=\omega_U^\theta/R.}\tag{EULER-ETA}
\]
Verify carefully why the full prelimit $\partial_z(q^2)$ vanishes in the correct topology, including near $R=0$. It is invalid to simply delete it because $U_n^\theta\to0$ in $C^0$.

## Precise available analytic leads and the real unresolved physical estimate

**1. Three-dimensional volume-preservation lower bound.** The following is a candidate theorem to prove directly from (EULER-ETA), $\|U\|_\infty\le1$, three-dimensional incompressibility, and nonzero transported $\eta_U$:
\[
\boxed{\|\omega_U(\cdot,-A)\|_\infty\ge\frac{c_U}{\sqrt{1+A}}\qquad(A\ge0).}\tag{LOWER}
\]
A proof strategy: pick a positive-volume set with $|\eta_U|\ge\kappa$ at one time, flow it backward using the actual three-dimensional volume-preserving Euler map, and use the at-most-$A$ material displacement. If all that transported volume lay in $R<\rho$, cylindrical volume in an accessible axial cylinder would be $O(\rho^2(1+A))$. Hence some transported point must have $R\gtrsim(1+A)^{-1/2}$, where $|\omega^\theta|=R|\eta|$. This uses true **3D** volume; replacing it by area $dR\,dZ$ is wrong. Check $\alpha_*=0$, nonzero $\eta$ inheritance and the Euler flow's global regularity and invertibility.

**2. A sufficient contradiction from the *physical trajectory*.** Define
\[
d(A)=\limsup_{n\to\infty}\frac{D(t_n-A/D_n)}{D_n},\qquad A\ge0\text{ fixed},
\]
where $t_n-A/D_n\ge0$ for large $n$. If one could derive
\[
\boxed{\liminf_{A\to\infty}\sqrt{1+A}\,d(A)=0,}\tag{TARGET-2}
\]
then (LOWER) would conflict with the inherited gradient bound and Case 2 would be excluded. **The order of limits is first $n\to\infty$ at fixed $A$, then $A\to\infty$.** A historical gradient Type-I *upper* bound $D(t)(T_*-t)\le K$ would imply the target but is **not** among the premises. Prove TARGET-2 from (A), full physical NS and finite energy, OR find a completely different contradiction; do not insert a Type-I bound as an assumption.

**3. The temporal derivative estimate points the wrong way.** Canonical pressure and (A) suggest $\|\nabla^2p(t)\|_\infty\lesssim C(C_*)D(t)^2$. Differentiating the NS momentum equation and using a maximum principle for $|\nabla u|$ leads to an a.e. historical differential inequality $0\le D'(t)\lesssim C(C_*)D(t)^2$. Backward integration gives
\[
\frac{D(t_n-A/D_n)}{D_n}\gtrsim \frac1{1+CA},
\]
**a lower bound**, NOT the desired upper decay. Check derivative and pressure subtleties. Do not reverse this implication or claim it yields Type-I upper control.

**4. The *actual* swirl source is small on fixed recent windows, but the middle history remains.** Using $\|\Gamma(t)\|_\infty\le G$, Cartesian Hessian regularity, and interpolation near the original symmetry axis, useful candidate inequalities are
\[
\|q(t)\|_\infty\lesssim G^{1/3}H(t)^{2/3},\qquad
\|\partial_z(q^2)(t)\|_\infty\lesssim G^{1/3}H(t)^{5/3}.
\]
In the above $(M,D)$ normalization, the source $\partial_Z(q_{U_n}^2)$ has a pointwise upper bound of order $C(C_*)(G\nu_n)^{1/3}$, and an improved radial-source mass bound of order $C(C_*)G\nu_n$ is plausible from radial concentration. Verify all exponents, geometric factors, and exact norm/measure definitions. A fixed-length recent window therefore loses swirl forcing; **it does NOT follow that the entire earlier interval $[0,t_n]$ contributes negligibly** to $\eta$. An actual nonzero Euler $\eta$ could have been generated far in the physical past and then transported.

**5. A substantial prelimit transport restriction.** One proposed fixed-datum estimate, still to be independently audited, says that if Case 2 survives, then for all sufficiently large $n$ and every admissible $0\le A\le c_U(G\nu_n)^{-1/2}$,
\[
\boxed{\frac{D(t_n-A/D_n)}{D_n}\ge\frac{c_U}{\sqrt{1+A}}.}\tag{WINDOW}
\]
Here $A$ may itself depend on $n$ and increase; this cannot be obtained by blindly extending convergence on fixed ancient-time windows. Its proposed proof uses the true NS vorticity equation, three-dimensional weighted cutoffs, diffusion and source mass, with all inner-axis fluxes included. If correct, it strengthens **necessary persistence** and associated logarithmic energy costs, but it is still a lower bound and **not** an exclusion. Derive an upper cost in conflict with it, prove the source-history budget vanishes, or find an entirely new contradiction.

**6. Optional signed-source route (actual $q$, not an independent model).** The source is $\partial_z(q^2)$, so signed pairings with a backward adjoint gradient may be much smaller than absolute $\int|\partial_z(q^2)|$. Attempt localized adjoint estimates in the physical $dx=2\pi r\,dr\,dz$ measure, control true $\int q^4dxdt$ near shrinking axis tubes, and rigorously include the drift/pressure feedback. This is a research route, NOT an assumed budget. Any comparison with a free-$q$ model is only a heuristic and cannot settle the original coupled system.

## Distinct avenues that must receive actual derivations

(i) Derive TARGET-2 (or a stronger upper depletion) from full NS time geometry using the intrinsic length $\ell(t)=M(t)/D(t)$, pressure, source strength and energy; identify whether required monotonicity/doubling hypotheses are genuine theorems rather than assumptions. (ii) Use three-dimensional material-volume rigidity of $\eta$ in the limit and physical, prelimit, **growing** time windows, not just fixed-$A$ convergence. (iii) Study history splitting into early, middle and recent times: no passage to zero may be asserted until **all** ranges are controlled quantitatively. (iv) Exploit radial concentration of actual swirl forcing, five-dimensional drift divergence and signed cancellation; fully account for the axis and far-$z$ tails. (v) Seek a different inherited Euler Liouville condition or contradiction with fixed physical energy and dissipation without imposing finite global ancient energy. (vi) Attack all potential saturation regimes of $M,D,H,G$ and the record axis position, with polynomial growth tests labeled as *non-NS diagnostics*.

## Final mathematical acceptance criterion

On exactly one fixed finite-energy axisymmetric full NS trajectory satisfying (A) and `NO-SWIRL-EXTRACTION`, **prove that no genuine gradient-record sequence with $\alpha_n\to\alpha_*<\infty$ can produce the stipulated bounded, nonconstant, no-swirl ancient Euler limit**, or rigorously demonstrate an actual fixed-datum NS finite-time singularity realizing the branch. Another conditional $TARGET-2 implies exclusion argument, another estimate for free-$q$, another necessary persistence inequality, or an artificial ancient Euler example is **not** a complete answer.

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
