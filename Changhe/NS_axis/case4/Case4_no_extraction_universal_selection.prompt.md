# Codex 24-hour research mission — CASE 4: universally select a bounded, spatially nonconstant ancient limit (NO shape hypothesis)

## Goal — close the missing extraction theorem, not invent a fourth PDE

The first three Cases concern **successfully extracted** full NS, finite-axis axisymmetric Euler, or planar Euler limits. **Case 4 is the unresolved logical possibility that all currently tested FIRST normalizations fail to produce a useful bounded, spatially nonconstant ancient solution.** No one has proved that an actual singular fixed-data NS trajectory realizes such a failure. Your job is to close this logical gap, not label a zero/constant/affine field as a fourth successful ancient PDE.

There are exactly two mathematically conclusive endpoints:

- `COMPLETE_UNIVERSAL_SELECTION`: starting from **any** hypothetical singular trajectory in the class below, prove that ONE physically selected **first normalization**, on one actual common subsequence, yields a globally bounded, sufficiently strong, **spatially nonconstant**, genuinely ancient solution of a precisely identified NS/Euler (or rigorously derived alternative) equation, with its correct pressure class and an applicable inherited structure; OR
- `COMPLETE_BRANCH_EXCLUSION_OR_FIXED_DATA_NO_GO`: prove, from full physical NS, that the putative no-useful-extraction branch is impossible (even without explicitly extracting an ancient profile); OR exhibit a genuine single fixed finite-energy smooth NS datum with finite-time singularity for which your *precisely defined universal selection proposition* is false. A model field or arbitrary sequence of smooth functions is not such a counterexample.

**This Case has NO `M H <= C_* D^2` assumption.** Adding that hypothesis would silently solve the wrong problem by making the Hessian normalized. A conditional selection rule is intermediate only, and absence of a known compactness estimate is not proof of non-compactness.

## 1. Exact physical setting, without (A)

Take **one fixed** decaying, smooth (`H^m` with `m>5/2` plus sufficient decay for spatial records), divergence-free, axisymmetric initial datum `u_0` on `R^3`, viscosity `1`, with
\[
E_0=\|u_0\|_2^2<\infty,\qquad G=\|r u_0^\theta\|_\infty<\infty.
\]
`G` is finite and arbitrarily large, not a small parameter; `G<infty` is explicit and is not inferred from `L^2` alone. Assume a hypothetical first finite singular time `T_*>0` of
\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\Delta u,\qquad\nabla\cdot u=0.
\]
The datum never changes along the argument. Define historical maxima
\[
M(t)=\sup_{0\le s\le t}\|u(s)\|_\infty,\quad
S(t)=\sup_{0\le s\le t}\|u^\theta(s)\|_\infty,\quad
D(t)=\sup_{0\le s\le t}\|\nabla u(s)\|_\infty,\quad
\Omega(t)=\sup_{0\le s\le t}\|\nabla\times u(s)\|_\infty.
\]
`H(t)=sup_{0<=s<=t}||nabla^2u(s)||_infty` can be recorded, **but has no assumed bound in relation to M,D**.

Use the real axisymmetric coupling, not a decoupled model:
\[
\begin{split}
(\partial_t+b\cdot\nabla)\Gamma&=(\partial_{rr}-r^{-1}\partial_r+\partial_{zz})\Gamma,\\
(\partial_t+b\cdot\nabla)\eta&=\Delta_5\eta+\partial_z(q^2),\\
(\partial_t+b\cdot\nabla)q&=\Delta_5q-2(u^r/r)q,\\
-\Delta_5\phi&=\eta,\quad u^r=-r\phi_z,\quad u^z=2\phi+r\phi_r,
\end{split}
\]
where `Gamma=r u^theta`, `q=u^theta/r`, `eta=omega^theta/r`, `b=(u^r,u^z)`.

## 2. Known partial reduction and the exact failure to resolve

**Previously derived first split (audit it):** if
\[
\limsup_{t\uparrow T_*}\frac{S(t)}{M(t)}>0,
\]
then true historical swirl first-crossing records, radius `r_n`, amplitude `S_n`, and clock `r_n/S_n` provide a bounded, nonzero-swirl ancient **full NS** mild limit. The key original equation fact is
\[
-r_nu^r(r_n,z_n,t_n)\ge1,
\qquad S_nr_n\le G.
\]
The case `limsup S/M=0` is the difficult one. Previous work argues from a *bounded ancient no-swirl NS* Liouville theorem that
\[
\boxed{\frac{S(t)}{M(t)}\to0
\quad\Longrightarrow\quad
\frac{D(t)}{M(t)^2}\to0,
\quad\frac{\Omega(t)}{M(t)^2}\to0.}\tag{SEPARATION}
\]
Check records, correct normalization, terminal compactness, and theorem class. Do not apply the same **NS** theorem to an **Euler** limit.

At a real historical gradient record `(x_n,t_n)` with `D_n=D(t_n)=|nabla u(x_n,t_n)|`, `M_n=M(t_n)`, natural *Euler* scaling would be
\[
\ell_n=M_n/D_n,\quad T_n=1/D_n,\quad
U_n(y,\tau)=M_n^{-1}u(x_n+\ell_n y,t_n+T_n\tau),
\quad\nu_n=D_n/M_n^2\to0.
\]
It ensures
\[
\|U_n\|_\infty\le1,\quad\|\nabla U_n\|_\infty\le1,
\quad |\nabla U_n(0,0)|=1,
\]
but **does not** ensure a bound on `nabla^2 U_n` or strong `C^1` convergence. Thus the terminal gradient can disappear in a merely `C^0` limit. Functional diagnostic: `f_n(x)=sin(nx)/n` has `f_n'(0)=1` and converges uniformly to zero; this is **NOT** an NS counterexample. The missing target is an actually inherited spatial contrast, e.g.
\[
\boxed{\exists R,c>0,\ \exists\text{ one record subsequence}:
\limsup_n\sup_{y\in B_R}|U_n(y,0)-U_n(0,0)|\ge c.}\tag{CONTRAST}
\]
Together with true time/pressure compactness, this secures a spatially nonconstant limit. It is not enough merely to state (CONTRAST) as an assumption; PROVE it, or choose a more suitable first scale where it follows.

A second path attempts a true swirl-radius normalization even when `M/S->infinity`, with a **single bound K independent of local cylinder** and a weighted quadratic Oseen tail. Those are conditional extraction witnesses, not consequences of finite energy. Your selector may choose this path if you actually prove the witness, but cannot simply assume it.

Past reports formulated a two-family `Q3` test (gradient / vorticity records). Its NO branch says every *tested* family loses visible velocity oscillation. This means only an **unresolved barrier for those methods**, not proof that all first normalizations fail. Other physical centers, clocks, amplitudes, or anisotropic geometries remain to be investigated.

## 3. Exact universal-selection theorem to establish

Find a mathematically executable rule, based on **actual singular observables along the one fixed trajectory**, producing `t_n -> T_*`, physical centers `x_n`, positive scales `B_n, ell_n, T_n -> 0` where appropriate, and fields
\[
\boxed{U_n(y,\tau)=\frac{u(x_n+\ell_n y,t_n+T_n\tau)}{B_n}.}\tag{FIRST-SCALE}
\]
Do not preselect an arbitrary parabolic scale. Derive which physical mechanism fixes the chosen time clock. The transformed momentum coefficients are
\[
\beta_n=\frac{T_nB_n}{\ell_n},\qquad
\nu_n=\frac{T_n}{\ell_n^2},\qquad
\frac{\beta_n}{\nu_n}=B_n\ell_n.
\]
Merely computing coefficients is not an equation-extraction theorem: you must justify strong enough convergence to pass the nonlinear term and pressure, determine any defect, and show the selected effective balance actually survives.

**The theorem must prove ALL of these on ONE common subsequence:**

1. `t_n/T_n -> infinity` (genuine ancient backward age), with terminal-time trace included.
2. `sup_{n,y, tau in each available ancient compact window}|U_n| <= C` in a way sufficient for a globally bounded ancient limit; if using local full-space uniform limit instead, specify exact quantifiers and prove `sup_{y,tau<=0}|U|<infty`.
3. Spatial and temporal compactness sufficient for a legitimate **identified PDE** (e.g. strong `L^2_loc` for nonlinearities plus pressure convergence and terminal trace; stronger topology if a derivative is the certificate).
4. A **quantitative spatial nonconstancy certificate that survives that topology**: fixed normalized spatial oscillation, a fixed circulation/vorticity average, or another nonzero nonlinear functional. A single gradient or Hessian point normalization without derivative convergence is insufficient.
5. The actual limit PDE, its full velocity and pressure class, and inherited critical structures (swirl/no swirl, physical axis finite/escaped, circulation/energy tails), with a concrete candidate rigidity estimate. No fake constant, affine, frozen-time, or arbitrary pressure-field leaf.
6. The rule itself must **select** a valid normalization: do not add a downstream question "if the limit is nonconstant" as if that were a successful classification.

Alternatively, close Case 4 by excluding the **no-usable-extraction** physical asymptotic mechanism directly from NS, but specify exact quantifiers defining that mechanism and prove a contradiction. Distinguish statements about a fixed chosen sequence from existential choice of *some* subsequence: a single trajectory can have multiple subsequential behaviors.

## 4. Research mechanisms that must be genuinely developed

1. **Quantitative contrast from true physical dynamics.** Try earliest velocity doubling records, intrinsic oscillation balls, Lagrangian particle separation, retained signed circulation, localized energy momentum flux, or swirl first-crossing geometry. Derive fixed positive contrast **before** passing to the limit. Check the known time-direction pitfall: velocity doubling gives a lower bound `D(t_j)(t_j-t_{j-1}) >= c`, whereas the desired compactness/visibility argument may need an upper bound—do not reverse it without proof.
2. **Concentration vs viscosity/pressure.** Prove a truly scale-local inverse inequality tied to the full NS evolution that prevents derivative or vorticity concentration from hiding at vanishing normalized width, or derive an alternate scale that resolves the concentration while preserving boundedness. If you use `||nabla^2 u||`, do not smuggle in historical (A).
3. **Helicity/circulation and axisymmetric Biot–Savart constraints.** Investigate whether `Gamma` max principle, near-axis radial geometry, true `eta`/`q` transport, and finite physical energy force a retained velocity increment even when `S/M->0`.
4. **Pressure and remote stress.** Analyze the canonical full-space pressure fixed by original finite energy, far-field Oseen/Leray kernel tails, harmonic pressure modes, and temporal compactness. If allowing a constant axial Galilean change, prove exactly how pressure and fixed-data provenance transform. Do not subtract an affine field or use a time-dependent moving frame to retrofit a desirable PDE.
5. **Other intrinsic first geometries.** If necessary, explore distinct radial and axial lengths `ell_perp`, `ell_z`, derive the anisotropic divergence, Laplacian, transport and pressure operators **exactly**, and establish all five properties before naming any new ancient PDE class. Do not claim every true NS singularity must be isotropic merely because the candidate normalizations were.
6. **Audit scale-family completeness.** A NO result for the two historical gradient/vorticity candidate families is only a local research obstruction, not an unconditional branch characterization. Either prove those families are complete among all admissible genuine first normalizations (with a rigorous minimality argument) or develop a new selection mechanism. Do not advertise a formal three-leaf tree as unconditional if nontriviality remains unproved.

**No assumed Type I, no assumed H2/local-tail compactness, no fixed ancient global energy, no free `q` source, no same-size radial and axial scales without proof, and no small-`G` limit.** Every example used to refute an analytic inequality must be labeled functional/ancient-model versus a true fixed-data NS solution.

## 5. Acceptance and input files

Complete success means every hypothetical singular fixed-data NS trajectory with the assumptions of §1 reaches **some rigorously proved, globally bounded, spatially nonconstant ancient PDE** under a chosen first scale, OR a valid theorem rules out the entire no-extraction alternative. A conditional sufficient selection theorem, a computational search finding preferred scales, or an example of functional noncompactness is intermediate only. If there is no proof at the end of a constrained session, report the **precise missing implication without claiming Case 4 is physically realized**.

Review if present: `NS_axis_intrinsic_balance_RESEARCH_REPORT(1).md`, `NS_axis_Q2_NO_meridional_scale_selection_REPORT(1).md`, `NS_axis_pressure_selected_first_normalization_REPORT(1).md`, `NS_axis_how_to_choose_nontrivial_normalization_GPT_Pro_prompt(1).md`, `NS_axis_Q2_NO_intrinsic_normalization_no_Q3_GPT_Pro_prompt(1).md`, `NS_axis_ancient_PDE_decision_tree_REPORT(1).md`, and original KNSS 2009. Audit each previous result; do not treat the absence of one named file as a reason to stop. This prompt provides the complete main mathematical setting.

---

## Mandatory Codex execution contract — minimum 24 hours of active research

**This is a research mission, not a request for an early survey or a short proof sketch.** The minimum duration is **24 hours of documented active work** for THIS CASE ALONE; a common session for all four cases does not satisfy that requirement. If a conclusive proof emerges early, use the remaining time to check every inference independently, seek counterexamples to proposed intermediate lemmas, eliminate unnecessary assumptions, and produce a publication-grade proof. An early failed attempt is never a stopping criterion.

1. At start, use the actual system clock (`date -u` or the available equivalent) to record `START_UTC` in `RUN_STATUS.md`. Track each active block with timestamps, its concrete mathematical objective, the calculations actually attempted, and the result. Distinguish active work from idle or disconnected time. Never claim 24 hours elapsed or worked without actual timestamps and activity records.
2. Work in a dedicated folder for this case only. Create/maintain `RUN_STATUS.md`, `CHECKLIST.md`, `WORKLOG.md`, `LEMMA_LEDGER.md`, `ERRORS_AND_COUNTEREXAMPLES.md`, `PROOF_DRAFT.md`, and `FINAL_REPORT.md`. Store auxiliary exact algebra or computations in a `checks/` subfolder. Update persistent files after substantive progress and at least once per hour. Use real file edits, not messages claiming a file was updated.
3. If actual researcher/verifier agents or parallel Codex workers exist, allocate independent proof development and adversarial verification; otherwise perform **two clearly separated passes**. A second pass must explicitly attempt to invalidate every key step. Do not pretend multiple agents ran if they did not.
4. No stand-in theorem, extra bootstrap hypothesis, partial finite-parameter estimate, scalar growth example, conditional Liouville claim, computation, or one special solution counts as a completed answer. Mark such work `INTERMEDIATE ONLY` in the ledger. A complete result must pass every acceptance test in this prompt.
5. Keep searching after a failed technique. Attempt genuinely different analytic mechanisms and maintain a rejection ledger so that failed approaches are not recycled. Consult original literature where access exists and write down the exact theorem statements and assumptions; do not rely on an abstract, a memory of a theorem, or the existence of a title. If internet access is unavailable, work from supplied material and label references that were not checked.
6. Every important estimate must include all constants and their dependencies, the exact space-time domain, the order of limits, and a scaling check. Audit near-axis regularity, far-field pressure/velocity tails, nonlinear terms, and the fixed original datum. **No uncontrolled nonlinear Grönwall or exponential estimates in the critical meridional feedback.** Do not force a favorable sign on the swirl forcing or the radial strain.
7. Prioritize analytic proof. Code is allowed to verify symbolic identities, exponents, inequalities, kernel asymptotics, and potential saturating test functions. Numerical PDE runs, fitted exponents, and synthetic ancient solutions are not proofs. Mathematical obstacles—not software implementation problems—belong in the research verdict.
8. If the environment imposes a session/context/tool time limit, leave a precise `RESUME_HERE` section in `RUN_STATUS.md`: current lemma, exact last valid inequality, precise next step, outstanding counterargument, and cumulative **documented active** time. On restart continue from this checkpoint; never invent elapsed activity. If a hard system limit prevents 24 hours, state `RUN INTERRUPTED — MINIMUM DURATION NOT MET`, not that the mission was completed.
9. Do not send a "final" answer just because a session has reached a convenient point or because an interesting intermediate theorem has been proved. **Accepted final outcomes require the entire principal objective, not partial results.** If a hard limit ultimately forces an unresolved exit, report `UNRESOLVED — NOT A SUCCESS` with the first missing implication rather than fabricating a theorem, a counterexample, or a 24-hour run. An unsolved outcome is truthful but expressly does **not** satisfy the user's success condition.
10. After a purported complete result, spend a distinct adversarial phase on: fixed-data provenance, quantifier negations and subsequences, normalized terminal trace, effective viscosity, pressure gauge, possible constant/affine degeneration, and proof of every needed compactness claim. The verifier may reject a draft; rejected drafts return to active research. Final report must be **self-contained** and written in precise mathematics with a short Chinese executive summary.

**Final report acceptance checklist:** exact theorem; correct assumptions (no hidden extras); complete sequential proof; original rather than invented solution; correct PDE at every scale; well-defined pressure/mild/weak class; no unproved time-direction or limit interchange; independently checked; at least 24 hours of actual documented work. Complete the `CHECKLIST.md` only after all items are genuinely proved. This prompt does not authorize invented claims of success.
