# Codex 24-hour research mission — CASE 3: exclude the axis-escape, planar ancient Euler branch

## Exact goal and binary success criterion

**Objective:** Prove that the axis-escape gradient-record scenario below is impossible for one fixed smooth finite-energy axisymmetric three-dimensional NS solution satisfying the stated hypotheses, by a completely quantitative physical NS argument. The fact that the extracted Euler flow is two-dimensional is NOT itself a contradiction.

The only successful outcomes are `COMPLETE_EXCLUSION` (a full proof excluding this Case 3 under exactly these assumptions, without an unproved Type-I bound) or `COMPLETE_FIXED_DATA_COUNTEREXAMPLE` (a single actual finite-energy smooth initial datum whose finite-time NS singularity realizes Case 3). Standalone ancient 2D Euler flows, model vorticity profiles, or invented varying-data NS sequences are **not** fixed-data counterexamples. A conditional depletion theorem, an improved exponent, or an energy restriction alone is NOT completion.

## 1. Physical fixed-data and historical assumptions

One fixed decaying smooth axisymmetric divergence-free `u_0` on `R^3` generates a full NS solution with viscosity `1`:
\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\Delta u,\quad\nabla\cdot u=0.
\]
Assume for contradiction its first singular time is `0<T_*<infty`. Fix
\[
E_0=\|u_0\|_2^2<\infty,\quad G=\|r u_0^\theta\|_\infty<\infty
\]
with `G` arbitrary finite, not small. Define **historical**
\[
M(t)=\sup_{0\le s\le t}\|u(s)\|_\infty,\quad
S(t)=\sup_{0\le s\le t}\|u^\theta(s)\|_\infty,
\quad D(t)=\sup_{0\le s\le t}\|\nabla u(s)\|_\infty,
\quad H(t)=\sup_{0\le s\le t}\|\nabla^2u(s)\|_\infty.
\]
Assume the historical shape control
\[
\boxed{M(t)H(t)\le C_*D(t)^2}\tag{A}
\]
for sufficiently late times and the earlier swirl-extraction predicate `Q1=NO`. The predecessor argument claims
\[
\frac{S(t)}{M(t)}\to0,\qquad \frac{D(t)}{M(t)^2}\to0\tag{B}
\]
and MUST be independently checked in the correct ancient NS Liouville class (do not use a false general Euler Liouville theorem). `Q1=NO` means no true swirl-first-record subsequence satisfies the uniform local-velocity/mild-tail witness; it does not mean `u^theta=0` physically.

The original coupled axisymmetric equations for `Gamma=ru^theta`, `q=u^theta/r=Gamma/r^2`, `eta=omega^theta/r` remain valid. The angular forcing is `partial_z(q^2)` in the `eta` equation. Keep it in every prelimit estimate even though normalized swirl vanishes in the planar Euler limit.

## 2. Exact Case 3 normalization and geometric meaning

Choose genuine historical gradient first-crossing points `(x_n,t_n)` (after rotation `x_n=(r_n,0,z_n)`) with
\[
D_n=D(t_n)=|\nabla u(x_n,t_n)|\to\infty,\quad M_n=M(t_n),
\quad \ell_n=M_n/D_n,\quad\nu_n=D_n/M_n^2\to0.
\]
Use **record-centered** coordinates (unlike axis-centered finite-axis Case 2):
\[
U_n(y,\tau)=M_n^{-1}u(x_n+\ell_n y,t_n+\tau/D_n),\qquad
P_n=p(x_n+\ell_n y,t_n+\tau/D_n)/M_n^2
\]
(up to a time-dependent additive pressure constant). The effective equation is
\[
\partial_\tau U_n+U_n\cdot\nabla U_n+\nabla P_n=\nu_n\Delta U_n,
\quad\nabla\cdot U_n=0.
\]
The Case 3 geometric predicate is
\[
\boxed{a_n=\frac{r_n}{\ell_n}=\frac{r_nD_n}{M_n}\longrightarrow\infty.}\tag{AXIS-ESCAPE}
\]
The axis is fixed in the **physical** solution but leaves every normalized compact set. From history and (A),
\[
\|U_n\|_\infty\le1,\quad \|\nabla U_n\|_\infty\le1,
\quad\|\nabla^2U_n\|_\infty\le C_*,
\quad|\nabla U_n(0,0)|=1.
\]
After independently proving strong terminal-inclusive compactness and canonical pressure convergence, obtain a globally bounded spatially nonconstant **planar ancient Euler** flow
\[
U(y,\tau)=(V_1(y_1,y_3,\tau),0,V_3(y_1,y_3,\tau)),
\quad \partial_{y_2}U=0,\quad U_2=0.
\]
Its planar vorticity `omega=partial_1 V_3-partial_3 V_1` obeys
\[
\partial_\tau\omega+V\cdot\nabla_{(y_1,y_3)}\omega=0.
\]
For a bounded globally Lipschitz ancient planar Euler flow, transport yields
\[
\boxed{\|\omega(\cdot,-A)\|_\infty=\|\omega(\cdot,0)\|_\infty>0\quad\forall A\ge0.}\tag{E3-invariant}
\]
The nonzero constant must be derived from the surviving spatial nonconstancy and bounded div-curl rigidity, not assumed.

## 3. Existing results: audit, then surpass

The reported **conditional exclusion** follows from backward depletion. Define
\[
d(A)=\limsup_{n\to\infty}\frac{D(t_n-A/D_n)}{D_n}.
\]
The sufficient physical condition
\[
\boxed{\lim_{A\to\infty}d(A)=0}\tag{TARGET3}
\]
forces zero ancient vorticity and contradicts `|nabla U(0,0)|=1`. A still weaker **localized** depletion of actual vorticity in the backward material region may suffice. Historical Type-I gradient control would imply TARGET3 but is NOT assumed, and it has not been established from (A). Your task is to derive TARGET3 or **another complete contradiction** from full physical NS + (A) + fixed finite energy.

Previously reported fixed-datum restrictions (each to be rechecked rigorously):
\[
\boxed{\frac{r_n M_n^4}{D_n^2}\le C(C_*)E_0,}\tag{ENERGY3}
\]
leading to
\[
\frac{D_n^3}{M_n^5}\ge \frac{c(C_*)}{E_0}a_n\to\infty,
\qquad r_n\le C(C_*)E_0\nu_n^2\to0.
\]
Thus physical `r_n -> 0` while **normalized** `a_n -> infinity`. Do not confuse these facts. A more recent proposed *prelimit* persistence window says: for some fixed `delta,c_U>0`,
\[
\frac{D(t_n-h/D_n)}{D_n}\ge c_U
\qquad\text{whenever }0\le h\le\delta a_n.
\tag{LONG-WINDOW3}
\]
Together with axisymmetric copies of a nontrivial planar region, the report derives a physical dissipation lower bound
\[
\int_{t_n-\delta r_n/M_n}^{t_n}\int_{\mathbb R^3}|\nabla u|^2\,dx\,dt
\ge c_U r_n^2M_n,
\qquad\boxed{r_n^2M_n\to0.}\tag{DISS3}
\]
The final limit follows from finite *physical* dissipation near `T_*`, not from a finite energy of the ancient planar limit.

These estimates restrict possible growth regimes but do not alone exclude all of them. Published bounded ancient 2D NS Liouville theorems do NOT exclude this **Euler** limit. The affine velocity and harmonic/pressure modes must be handled using global boundedness and actual normalized canonical pressure.

## 4. Required original research directions

1. **Stronger axisymmetric replication and finite-energy contradiction.** Use axisymmetry to copy a normalized planar vorticity/velocity feature around the original circumference `2 pi r_n`, and quantify the area, thickness `ell_n`, lifetime, and true physical energy/dissipation expense. Try to upgrade (ENERGY3), (LONG-WINDOW3), and (DISS3) into an impossible **positive total cost** that cannot vanish as `n->infinity`. Beware repeated/nested spatial annuli and overlapping time windows: no unjustified sum over `n`.
2. **Actual backward depletion from the physical trajectory.** Seek one-sided temporal estimates on historical `D` or localized vorticity strong enough to imply TARGET3 or localized material depletion. Derive time directions carefully: `D'<=C D^2` only yields a backward **lower** bound. Do not posit an upper Type-I rate or an Euler-length temporal doubling hypothesis.
3. **Planar limit geometry with shrinking physical radius.** Exploit simultaneously `r_n->0`, `a_n->infinity`, bounded original circulation, and exact axisymmetric swirl identities. Analyze whether a planar limit's nonzero transported vorticity can have its entire arbitrarily long past on shrinking physical annuli without violating one fixed solution's finite energy or regularity away from `T_*`.
4. **Pressure, strain, and angular-curvature corrections.** In the prelimit Euler equation retain all `1/r_n` geometric errors quantitatively for windows growing with `a_n`; local fixed-window convergence alone is insufficient. Test whether a signed curvature/pressure trace, radial compression requirement, or angular momentum budget eliminates the planar branch.
5. **Alternative rigidity criterion.** If the global gradient depletion is too strong, derive a precise localized vorticity depletion or a new inherited invariant that contradicts every bounded nonconstant ancient planar Euler field **coming from this fixed original NS solution**, not every abstract 2D Euler flow.

Check all quantities and orders of `n->infinity`, `A->infinity`, `a_n->infinity`, and physical `t->T_*`; use the correct 3D volume element `2 pi r dr dz`. Treat `G` as arbitrary fixed, and allow sign changes and intermittent records. Do not infer no blowup from the failure of a toy power-law ansatz.

## 5. Acceptance and prior material

**A successful exclusion theorem** must yield a contradiction directly from `(A)`, `Q1=NO`, the actual Case 3 geometric sequence, full NS, and one fixed finite-energy datum. A true fixed-data construction realizing Case 3 would also settle the posed dichotomy but must prove actual finite-time singularity. Improved but noncontradictory energy inequalities are intermediate only.

Check local project files if present: `NS_axis_case3_axis_escape_planar_Euler_Liouville_report.md`, `NS_axis_Euler_cases2_3_backward_depletion_research_report_zh.md`, `NS_axis_research_prompt_Euler_cases2_3_backward_depletion.md`, `NS_axis_intrinsic_balance_RESEARCH_REPORT(1).md`. Verify exact cited Euler/NS Liouville theorem hypotheses rather than quoting them generically. The present statement is self-contained if reports are unavailable.

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
