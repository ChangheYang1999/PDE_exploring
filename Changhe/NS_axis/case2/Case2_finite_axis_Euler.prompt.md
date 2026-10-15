# Codex 24-hour research mission — CASE 2: exclude the finite-axis, no-swirl ancient Euler branch

## Exact goal and binary success criterion

**Objective:** Under the physical hypotheses below, **derive a contradiction for every legitimate finite-axis ancient Euler limit extracted from the one fixed finite-energy axisymmetric NS trajectory**. The limiting Euler equation alone is not the original problem: the contradiction must come from what the fixed viscous NS solution forces the limit to inherit.

The only accepted conclusive endpoints are `COMPLETE_EXCLUSION` (full theorem under all the stated assumptions, no additional Type-I/time-decay hypothesis) or `COMPLETE_FIXED_DATA_COUNTEREXAMPLE` (a rigorously constructed actual fixed-datum finite-time NS singularity satisfying these assumptions and producing this Case 2 limit). A stationary or traveling Euler vortex ring, prescribed-source model, or arbitrary ancient Euler field is **not** a counterexample to the physical theorem. No partial estimate counts as success.

## 1. Exact physical equations and assumptions

Consider one fixed smooth, decaying, divergence-free, axisymmetric NS initial datum `u_0`, viscosity `1`, with
\[
E_0=\|u_0\|_{L^2(\mathbb R^3)}^2<\infty,
\qquad G=\|ru_0^\theta\|_\infty<\infty,
\]
`G` arbitrarily large but fixed. Assume a hypothetical first singular time `0<T_*<infty` for the **full** axisymmetric NS system
\[
\partial_tu+u\cdot\nabla u+\nabla p=\Delta u,\qquad\nabla\cdot u=0.
\]
Define the historical functions
\[
\begin{aligned}
M(t)&=\sup_{0\le s\le t}\|u(s)\|_\infty,&
S(t)&=\sup_{0\le s\le t}\|u^\theta(s)\|_\infty,\\
D(t)&=\sup_{0\le s\le t}\|\nabla u(s)\|_\infty,&
H(t)&=\sup_{0\le s\le t}\|\nabla^2u(s)\|_\infty.
\end{aligned}
\]
The only extra quantitative regularity input is the **historical shape relation**
\[
\boxed{M(t)H(t)\le C_*D(t)^2}\tag{A}
\]
for all sufficiently late `t<T_*`. Do NOT assume historical gradient Type I, finite ancient energy, a favorable vorticity sign, finite axial support, or `L^1(eta)` bounds.

Work on the **NO-swirl-ancient-NS-extraction branch**, denoted `Q1=NO`, using the precise predicate in the earlier decision tree. Prior work argues, with the original NS Liouville theorem and actual first-crossing records,
\[
\boxed{\frac{S(t)}{M(t)}\to0,\qquad \frac{D(t)}{M(t)^2}\to0}\quad (t\uparrow T_*).\tag{B}
\]
**Independently audit (B)**; do not call Euler Liouville to prove it. `Q1=NO` denies the existence of a swirl-record sequence satisfying a unified local full-velocity bound and its weighted `|y|^{-4}` quadratic mild-tail condition; it does **not** assert that swirl vanishes in the original NS trajectory.

The actual coupled physical quantities remain
\[
\Gamma=ru^\theta,\quad q=\Gamma/r^2=u^\theta/r,\quad\eta=\omega^\theta/r,
\]
with
\[
(\partial_t+b\cdot\nabla)\Gamma=(\partial_{rr}-r^{-1}\partial_r+\partial_{zz})\Gamma,
\quad
(\partial_t+b\cdot\nabla)\eta=\Delta_5\eta+\partial_z(q^2),
\]
`b=(u^r,u^z)` recovered from `eta` by `-Delta_5 phi=eta`, `u^r=-r phi_z`, `u^z=2phi+r phi_r`. Do not replace `q` by a freely prescribed source when proving the physical theorem.

## 2. Exact Case 2 gradient normalization and limit

Choose **actual historical first-crossing gradient records** `(x_n,t_n)`, rotate around the unchanged physical axis so `x_n=(r_n,0,z_n)`, and set
\[
D_n=D(t_n)=|\nabla u(x_n,t_n)|\to\infty,\qquad M_n=M(t_n),
\quad \ell_n=\frac{M_n}{D_n},\quad \nu_n=\frac{D_n}{M_n^2}\to0.
\]
Axis-centered velocity scaling is
\[
\boxed{U_n(y,\tau)=\frac1{M_n}u((0,0,z_n)+\ell_n y,t_n+\tau/D_n).}
\]
The record is at `y_n=(a_n,0,0)` with
\[
a_n=\frac{r_nD_n}{M_n}\longrightarrow a\in[0,\infty).
\]
This is Case 2: **finite normalized axis distance**. The rescaled momentum equation is
\[
\partial_\tau U_n+U_n\cdot\nabla U_n+\nabla P_n
=\nu_n\Delta U_n,\qquad\nabla\cdot U_n=0,
\]
with canonical pressure `P_n=p/M_n^2` modulo a time function, not an arbitrarily selected harmonic force. Historical bounds and (A) imply
\[
\|U_n\|_\infty\le1,\quad \|\nabla U_n\|_\infty\le1,
\quad \|\nabla^2U_n\|_\infty\le C_*,
\quad |\nabla U_n(y_n,0)|=1.
\]
Verify that a subsequence converges strongly through `tau=0` in the class needed to retain the gradient record, pressure, and nonlinear equation. The prospective limit `U` is globally bounded and spatially nonconstant, has `U^theta=0`, and satisfies **axisymmetric no-swirl Euler**
\[
\partial_\tau U+U\cdot\nabla U+\nabla P=0,
\quad\nabla\cdot U=0,\quad
(\partial_\tau+U\cdot\nabla)\eta_U=0,
\qquad \eta_U=\omega_U^\theta/R.
\]
The velocity remains bounded for all ancient times, but the **ancient limit need not have finite global energy**. Respect the fixed original symmetry axis; no affine subtraction or moving frame.

## 3. Verified/claimed input and the precise missing physical estimate

Earlier Case 2 work claims a nonzero, transported `eta_U` and a rigorous **three-dimensional volume/transport** lower bound
\[
\boxed{\|\omega_U(\cdot,-A)\|_\infty\ge\frac{c_U}{\sqrt{1+A}}}\qquad(A\ge0).\tag{E2-lower}
\]
Its proof must use true 3D Jacobian `2 pi R dR dZ` rather than a fictitious 5D incompressible drift. Audit boundedness, support/material set, `a=0`, and spatially nonconstant implication.

For any fixed `A`, let
\[
d(A)=\limsup_{n\to\infty}\frac{D(t_n-A/D_n)}{D_n}.
\]
A **sufficient physical-history estimate** is
\[
\boxed{\liminf_{A\to\infty}\sqrt{1+A}\,d(A)=0.}\tag{TARGET2}
\]
Then transport lower bound versus the inherited ancient gradient upper bound gives a contradiction. The order is first `n->infty` at fixed `A`, then `A->infty`. Historical gradient Type I would suffice but is **not assumed**. The true objective is to **prove TARGET2 or obtain a different complete fixed-trajectory contradiction from (A) and NS**.

Other previously derived results, all needing adversarial checking:

- Canonical-pressure Hessian `||nabla^2p||_infty <= C(C_*)D(t)^2` and historical growth `0 <= D'(t) <= C(C_*)D(t)^2` almost everywhere. This yields a backward **lower** bound `D(t_n-A/D_n)/D_n >= (1+CA)^{-1}`; it does **not** prove backward depletion or Type-I **upper** bounds.
- Near-axis circulation-Hessian interpolation at actual time `t`:
  \[
  \|q(t)\|_\infty\le C G^{1/3}H(t)^{2/3},\qquad
  \|\partial_z(q^2)(t)\|_\infty\le C G^{1/3}H(t)^{5/3}.
  \]
  The normalized source tends to zero on **fixed recent** intrinsic time windows, but that does NOT control all prior history.
- A proposed **prelimit growing-window persistence** for
  `0 <= A <= c_U (G nu_n)^(-1/2)`:
  \[
  \frac{D(t_n-A/D_n)}{D_n}\ge \frac{c_U}{\sqrt{1+A}}.
  \]
  This is a lower bound, not the missing upper bound, and holds only in its stated range.
- A finite-energy peak-volume estimate `M_n^5 <= C E_0 D_n^3` implies `ell_n -> 0` and controls the physical size of record balls, but does not force TARGET2.

A separate **prescribed/free `q`** exploration has investigated middle-history signed pairings and a shrinking-axis tube `int q^4` budget. It can be useful for discovering cancellations, but is a strictly **different model**: any claimed improvement must be re-proved for the **actual coupled NS `q` dynamics and fixed datum**. Do not import its YES/NO result as a physical theorem.

## 4. Required research avenues, with no early termination

1. **Backward-gradient depletion from the real time evolution.** Find a quantitative mechanism in the full NS dynamics linking the historical growth of `M,D,H` to backward decrease faster than `(1+A)^(-1/2)`, or to a different incompatibility with nonzero transported ancient `eta`. Do not convert `D'<=CD^2` into the wrong time-direction inequality. Search for coupled inequalities with stronger sign/monotonicity, finite-energy contradictions, or irreversible diffusion that are truly available at records.
2. **Past swirl-source elimination.** Work with the exact `eta` equation and actual `Gamma` maximum principle, not `q` as an independent source. Derive a spacetime signed or compensated source-vorticity identity tracking the entire physical history, including `t=0`, near-axis concentration, convective flux, and shrinking record neighborhoods. Prove that inherited nonzero `eta` is impossible, or contradict the finite-energy/history assumptions another way.
3. **Axisymmetric Euler volume geometry plus viscosity.** Quantify how a material set that survives for all ancient times would pull back to increasingly early portions of ONE NS solution. Explicitly account for time-dependent cutoff boundaries, radial Jacobians, lack of global ancient energy, and the order `n`/`A` limits.
4. **Try a robust two-parameter limit.** If `A=A_n` grows, establish prelimit inequalities directly rather than applying compact convergence proved only for fixed `A`. Seek a compatible time window and total dissipation price that contradict a fixed `E_0`. Test all proposed regimes `A_n << (G nu_n)^(-1/2)`, comparable, and larger.
5. **Alternative Liouville or shape relation.** Investigate if (A), exact canonical pressure, and fixed energy yield a stronger scale-invariant necessary constraint that the *bounded no-swirl Euler limit* cannot satisfy. If citing recent Euler-length theorems, verify all required temporal monotonicity, doubling, locality, and type-I conditions; none is automatic from (A).

Stress-test estimates for `a=0`, large finite `a`, arbitrarily large fixed `G`, possible sign-changing `eta`, and long histories. Explicitly distinguish actual NS attainability from compatible Euler toy fields and scalar growth-rate tests.

## 5. Acceptance and report

A complete theorem must show that **Case 2 cannot arise from any one fixed physical NS trajectory with `(A)` and `Q1=NO`**, using no additional Type-I assumption. If disproving this proposition, the counterexample must be a real fixed-data finite-energy NS singular trajectory. Partial persistence estimates, conditional TARGET2 exclusions, and manufactured ancient Euler profiles are not accepted.

Read when available: `NS_axis_case2_finite_axis_Euler_Liouville_report_zh.md`, `NS_axis_Euler_cases2_3_backward_depletion_research_report_zh.md`, `NS_axis_research_prompt_Euler_cases2_3_backward_depletion.md`, plus Case 2 free-`q` historical reports as **diagnostics only**. Audit original sources: KNSS arXiv:0709.3599, and Euler-length work of Constantin–Ignatova–Vicol (verify current actual versions and theorem hypotheses). If attached reports are missing, the full setting and target are above.

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
