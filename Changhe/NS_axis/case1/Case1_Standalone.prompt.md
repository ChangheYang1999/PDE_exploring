# CASE 1 — Complete exclusion of the swirl-preserving ancient full Navier--Stokes branch

**One copy-paste prompt.** You receive NO earlier chat, manuscript, prompt, report, repository research notes or attachments. Everything needed to define the problem and the existing mathematical leads is contained below. Work only on Case 1. Do not answer with a plan or a conditional theorem.

## Exact desired final result

**Prove a complete contradiction** from the single fixed finite-energy physical Navier--Stokes solution, the historical shape condition (A), and the precise swirl-extraction branch conditions (K) and (TAIL) below. Equivalently, prove that those assumptions cannot lead to a bounded, nonzero-swirl, spatially nonconstant ancient **full Navier--Stokes** limit of strictly positive finite viscosity. Do not merely prove that some stronger condition *would* exclude it. A logically decisive fixed-datum counterexample to the purported exclusion would also settle the conjectured implication, but would have to prove an actual finite-time singularity of one fixed smooth finite-energy initial datum satisfying the branch assumptions. No change of initial data is permitted.

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

## The additional physical hypothesis (A) and the exact Case 1 predicate

In **this case only**, assume the *historical shape estimate*, with one finite fixed constant $C_*$, for all sufficiently late $t<T_*$:
\[
\boxed{M(t)H(t)\le C_*D(t)^2.}\tag{A}
\]
Do not claim (A) follows from general NS regularity; here it is a genuine extra hypothesis. Its temporal *historical* meaning matters.

Choose genuine **historical swirl first-crossing** records $(r_n,z_n,t_n)$ as defined in the common setting, with $S_n\to\infty$; let
\[
\gamma_n=r_nS_n,\qquad T_n=\frac{r_n}{S_n},\qquad
U_n(y,\tau)=\frac{u(r_ny',z_n+r_n y_3,t_n+T_n\tau)}{S_n},
\quad R=|y'|.
\]
This is an axis-centered *spatially isotropic* first scaling of the original raw full velocity, with no affine subtraction. Its exact parameters are $B_n=S_n$, $\ell_n=r_n$, $\beta_n=1$ and
\[
\nu_n=\frac1{r_nS_n}=\gamma_n^{-1}.
\]
The branch **assumes the following two extraction witnesses on one common sequence**, with one $K<\infty$ independent of all finite $L,A$:
\[
\boxed{\limsup_{n\to\infty}
\sup_{|y|\le L,\,-A\le\tau\le0}|U_n(y,\tau)|\le K
\quad \text{for all }L,A<\infty.}\tag{K}
\]
\[
\boxed{\lim_{L\to\infty}\limsup_{n\to\infty}
\sup_{-A\le\tau\le0}\int_{|y|>L}\frac{|U_n(y,\tau)|^2}{|y|^4}\,dy=0
\quad \text{for each }A<\infty.}\tag{TAIL}
\]
These are **assumptions defining this leaf**, NOT results of (A). If you can remove either assumption without changing the theorem, that is welcome, but first solve the stated leaf. In particular, the absence of (K) or (TAIL) belongs to the different extraction problem, not a counterexample to this case.

### What the raw record and its true NS equation give

At the swirl record, $-r_nu^r(r_n,z_n,t_n)\ge1$. Since $|U_n^\theta(1,0,0)|=1$, this becomes $-\gamma_n U_n^R(1,0,0)\ge1$. By (K),
\[
K^2\ge1+\gamma_n^{-2}+o(1),\qquad
\frac1{\sqrt{K^2-1}}\le\liminf_n\gamma_n\le\limsup_n\gamma_n\le G.
\]
Check the limiting inequalities carefully (including strict versus non-strict inequalities and the $K>1$ condition). On a further single subsequence $\gamma_n\to\gamma_*\in(0,G]$; hence $\nu_n\to\nu_*=1/\gamma_*\in(0,\infty)$. Also $r_n\le G/S_n\to0$, and the backward time depth $t_n/T_n=t_nS_n/r_n\to\infty$.

Under (K), (TAIL), and nondegenerate viscosity, a standard candidate argument uses the true full-NS mild equation, Oseen-kernel bounds $|\nabla e^{\nu h\Delta}\mathbb P|(y)\lesssim(|y|+\sqrt{\nu h})^{-4}$, and a near/far decomposition to obtain compactness through $\tau=0$ and inherit a globally bounded ancient **mild full NS** solution $U$, canonical pressure, and
\[
\|U\|_{L^\infty(\mathbb R^3\times(-\infty,0])}\le K,
\quad |U^\theta(1,0,0)|=1,
\quad |\Gamma_U|\le G/\gamma_*,
\quad -\gamma_* U^R(1,0,0)\ge1.
\]
You must independently justify all kernel-tail/time-trace/pressure steps; the label "standard" is not a substitute for a proof. A strong velocity limit that fails to retain the terminal swirl record is NOT sufficient.

The exact scaling identities, useful for checking fixed-data inheritance, are
\[
\Gamma_{U_n}=\frac{\Gamma}{\gamma_n},\quad
q_{U_n}=\frac{r_n^2}{\gamma_n}q,\quad
\eta_{U_n}=\frac{r_n^3}{\gamma_n}\eta,\quad
R^3|\eta_{U_n}|=\frac{r^3|\eta|}{\gamma_n},
\]
\[
\int |U_n|^2dy=\frac1{\gamma_n^2r_n}\int|u|^2dx,
\qquad
\nu_n\!\int\!\int |\nabla U_n|^2dy\,d\tau
=\frac1{\gamma_n^2r_n}\int\!\int|\nabla u|^2dx\,dt,
\]
where the integral regions on either side correspond exactly. These formulas **do not** give a globally finite-energy ancient limit. Neither $\|\eta\|_{L^1}$ nor $\sup r^3|\eta|$ is automatically bounded merely from finite physical energy.

## Explicit mathematical progress to verify and improve (included here, not in attachments)

**A. Critical meridional-vorticity route.** A candidate conditional Liouville mechanism is
\[
\sup_{R>0,Z,\tau\le0}R^3|\eta_U(R,Z,\tau)|<\infty
\quad\Longrightarrow\quad
\sup_{R,Z,\tau\le0} R|V(R,Z,\tau)-c_0e_Z|<\infty
\quad\Longrightarrow\quad U^\theta\equiv0,
\]
where $V=U^Re_R+U^Ze_Z$, $c_0$ would have to be a **single, justified, time-independent** axial constant, and the argument must use the full NS equations and the correct bounded mild class. Each arrow requires independent checking; especially examine whether extra hypotheses on the stream potential, far field, or $\eta$ are tacitly needed. A strong sufficient *physical* estimate would be
\[
\sup_{t_0\le t<T_*}\sup_{r,z}r^3|\eta(r,z,t)|\le C(E_0,G,C_*,u_0),
\]
but this is NOT currently proved. A weaker bound **uniform on every expanding normalized swirl-record cylinder** is equally acceptable if it produces the required ancient bound without constants growing in $n$ or cylinder radius. Prove that the source, drift, and boundary flux together permit it; a free-source heat estimate alone does not.

**B. Radial compression versus angular diffusion.** A second candidate comparison principle asserts that for some $R_0>0$, an ancient solution with bounded circulation, if $-U^R(R,Z,\tau)\le b(R)$ for all $R\ge R_0$, $Z,\tau$, and
\[
\int_{R_0}^\infty R\exp\left[-\frac1{\nu_*}\int_{R_0}^R b(\rho)\,d\rho\right]dR=\infty,
\]
then $U^\theta=0$. Verify the scalar comparison proof and exact hypotheses. A logarithmic endpoint model is
\[
-RU^R(R,Z,\tau)\le \nu_*\left(2+\frac1{\log R}\right)
\quad (R\ge R_0\ge e),
\]
for which the comparison integral behaves like $\int^\infty dR/(R\log R)$ and diverges. The first-crossing inequality only shows compression at $R=1$; the **open physical step** is a global-enough sign/envelope bound on recurrent compression at large normalized $R$. It must follow from full physical NS, (A), finite energy and the Case 1 witnesses, not be assumed.

**C. True coupled-source and pressure facts.** A candidate bound for the extracted swirl is
\[
|\Gamma_U(R,Z,\tau)|\le\frac G{\gamma_*}
\left[1-(1+K\gamma_*R)e^{-K\gamma_*R}\right],
\]
leading to the radial-slice source occupation estimate
\[
\sup_{Z,\tau\le0}\int_0^\infty q_U(R,Z,\tau)^2R\,dR
\le 1+\log\frac{(KG)^2}{2}.
\]
These are **claims for adversarial verification, not license to assume the desired conclusion**. They control neither $\partial_Z(q^2)$ by an absolute spacetime integral nor the transported $\eta$ without drift control. Under (A), a further pressure-Hessian estimate is expected:
\[
\sup_{s\le t}\|\nabla^2p(s)\|_\infty
\lesssim [1+\log_+ C_*]D(t)^2.
\]
Check this from the canonical pressure, near-field cancellation and far-field integration by parts; it controls magnitude, not the sign of $u^r$ required by compression. The exact five-dimensional weighted energy identities involve $\int\eta^2dx$ and $\int r^2q^4dx$; their inward-strain term is still uncontrolled. A differential estimate that is superlinear and not globally closable is only an intermediate result.

**D. The non-negotiable issue.** In the actual PDE, the drift is recovered from $\eta$, and $q$ itself evolves. In particular, do NOT replace
\[
\eta_t+b[\eta]\cdot\nabla\eta=\Delta_5\eta+\partial_z(q^2)
\]
by $\eta_t=\Delta_5\eta+\partial_z(q^2)$ or by Euler transport alone. The free heat source can generate useful sharp model estimates, but cannot close the full coupled case. No unknown $L^1(\eta)$, arbitrary initial $\eta$ moment, favorable sign of $\partial_z(q^2)$, small $G$, or exponential dependence on an uncontrolled critical norm may be silently introduced.

## Mandatory proof agenda and exact acceptance gate

1. Re-derive the case predicate, first-crossing compression, strictly positive finite effective viscosity, ancient-depth scaling and full mild extraction. State every pressure, terminal compactness and tail estimate used.
2. Try a self-contained critical $R^3\eta$ argument with exact annular/axis cutoffs, signed $\partial_Z(q^2)$ integration, five-dimensional $\operatorname{div}_5b$, nonlocal Biot--Savart kernel and *all* fluxes. Optimize constants over large finite $G$, expanding cylinders and ancient time. Independently audit whether this actually implies the proposed Liouville hypothesis.
3. Independently attack the radial-compression comparison via the actual $\Gamma$ equation and real full NS radial momentum/pressure. Test the logarithmic threshold and large-radius returning compression; exclude parasitic pressure modes.
4. Explore other full-system mechanisms if both routes fail: circulation escape, fixed-data energy and dissipation in shrinking physical cylinders, localized pressure/strain, material line geometry, vorticity creation, ancient mild Liouville hypotheses. Do not merely enumerate ideas: obtain explicit inequalities and attack the first unproved arrow in each.
5. **A verified complete result must prove** from exactly (A)+(K)+(TAIL)+fixed data that the normalized limit with $|U^\theta(1,0,0)|=1$ is impossible, or supply a genuine fixed-datum counterexample (with proof of singularity) to the claimed exclusion. Proving only a conditional estimate or a new necessary condition is NOT success.

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
