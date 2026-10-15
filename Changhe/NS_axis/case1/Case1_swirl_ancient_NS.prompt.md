# Codex 24-hour research mission — CASE 1: exclude the nonzero-swirl ancient full Navier–Stokes branch

## Exact goal and binary success criterion

**Objective:** Starting from **one fixed** smooth, decaying, finite-energy axisymmetric three-dimensional Navier–Stokes trajectory satisfying the exact assumptions below, **prove that the specified swirl-record ancient NS branch cannot occur**. This means establishing a complete contradiction from the physical trajectory, not merely deriving a condition that would imply a contradiction.

Two logically conclusive endpoints are admissible:

- `COMPLETE_EXCLUSION`: a fully verified theorem excluding Case 1 under the hypotheses below, without further unproved conditions; OR
- `COMPLETE_FIXED_DATA_COUNTEREXAMPLE`: a rigorously verified example of ONE fixed smooth finite-energy axisymmetric NS initial datum whose actual solution realizes the entire branch and violates the proposed exclusion. Such an example must establish the claimed finite-time singularity and extraction from that same datum; an independently prescribed ancient NS solution does not count.

A conditional theorem, a critical estimate under an extra unknown norm, or an ancient solution that is not shown to arise from fixed-data NS is **not an accepted result**. Treat this as a high-risk open problem and never infer that a 24-hour budget makes success logically guaranteed.

## 1. Physical setting (fixed for the whole mission)

Let `u=(u^r,u^theta,u^z)` be an axisymmetric smooth solution on `R^3 x [0,T_*)`, with viscosity `nu_phys=1`:

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\Delta u,\qquad \nabla\cdot u=0.
\]

The original datum `u_0` is ONE fixed, decaying, smooth, divergence-free, axisymmetric field, with
\[
E_0:=\|u_0\|_{L^2(\mathbb R^3)}^2<\infty,\quad
G:=\|r u_0^\theta\|_{L^\infty}<\infty.
\]
`G` is arbitrarily large but fixed; it is **not** a small parameter. Assume, for contradiction, a first singular time `0<T_*<infty`. Define **historical** maxima on `[0,t]`, not instantaneous ones:
\[
\begin{aligned}
M(t)&=\sup_{0\le s\le t}\|u(s)\|_\infty, &
S(t)&=\sup_{0\le s\le t}\|u^\theta(s)\|_\infty,\\
D(t)&=\sup_{0\le s\le t}\|\nabla u(s)\|_\infty, &
H(t)&=\sup_{0\le s\le t}\|\nabla^2u(s)\|_\infty.
\end{aligned}
\]
Assume the historical shape hypothesis, only for sufficiently late times,
\[
\boxed{M(t)H(t)\le C_*D(t)^2.}\tag{A}
\]
Do not assume Type-I in time, uniform initial `L^1(eta)`, any ancient `L^2` energy bound, a single-scale ansatz, or a small-swirl condition.

Set
\[
\Gamma=ru^\theta,\qquad q=\frac{u^\theta}{r}=\frac\Gamma{r^2},\qquad
\eta=\frac{\omega^\theta}{r},\qquad \omega^\theta=\partial_z u^r-\partial_r u^z.
\]
The **complete coupled equations** in physical variables are
\[
\begin{split}
(\partial_t+b\cdot\nabla)\Gamma
 &= (\partial_{rr}-r^{-1}\partial_r+\partial_{zz})\Gamma,\\
(\partial_t+b\cdot\nabla)\eta
 &=\Delta_5\eta+\partial_z(q^2),\\
(\partial_t+b\cdot\nabla)q
 &=\Delta_5q-2\frac{u^r}{r}q,
\end{split}
\]
where `b=u^r e_r+u^z e_z`, `Delta_5=partial_rr+3 r^{-1}partial_r+partial_zz`, and the meridional Biot–Savart recovery is
\[
-\Delta_5\phi=\eta,\quad u^r=-r\phi_z,\quad u^z=2\phi+r\phi_r.
\]
Important: `div_5 b = 2u^r/r`, **not** zero. All physical three-dimensional integrals use `dx=2 pi r dr dz`.

## 2. Precisely defined Case 1 extraction predicate

Choose **actual historical first-crossing swirl records** `(r_n,z_n,t_n)`, with
\[
S_n=S(t_n)=|u^\theta(r_n,z_n,t_n)|\to\infty,\quad
\gamma_n=r_nS_n,\quad a_n=r_n/S_n.
\]
Use the original symmetry axis; translate only in `z`:
\[
U_n(y,\tau)=S_n^{-1}u(r_ny',z_n+r_n y_3,t_n+a_n\tau),\quad
R=|y'|,\quad \nu_n=\gamma_n^{-1}.
\]
At the first-crossing maximum, the exact swirl equation yields
\[
-r_nu^r(r_n,z_n,t_n)\ge1,\quad
|U_n^\theta(1,0,0)|=1,\quad
\gamma_n\le G.
\]

This **Case 1** predicate also assumes the following **same-subsequence** extraction witnesses. There is **one fixed** `K<infty` such that, for every finite `L,A`,
\[
\limsup_n\sup_{|y|\le L,\,-A\le\tau\le0}|U_n(y,\tau)|\le K,\tag{K}
\]
and for each finite `A`,
\[
\lim_{L\to\infty}\limsup_n\sup_{-A\le\tau\le0}
\int_{|y|>L}\frac{|U_n(y,\tau)|^2}{|y|^4}\,dy=0.\tag{TAIL}
\]
**(K) and (TAIL) are branch assumptions, not consequences already proved from (A).** Under them, existing extraction arguments claim a globally bounded ancient mild **full NS** limit `U` with **positive finite** viscosity `nu_*=1/gamma_*`, a nonzero swirl record, and canonical pressure. Re-verify compactness through `tau=0`, the mild tail passage, and
\[
0<\gamma_*<G,\qquad |U^\theta(1,0,0)|=1,
\qquad -\gamma_*U^R(1,0,0)\ge1.
\]
Do not reinterpret this as an Euler, Stokes, decoupled, or free-source limit.

## 3. Known advances to independently audit

Prior reports (`NS_axis_case1_full_NS_swirl_closure_research_report.md`, `NS_axis_case1_swirl_NS_Liouville_research_report.md`) claim the following. **They are leads, not axioms.**

- From (A) and the full canonical pressure, `sup_{s<=t} ||nabla^2 p(s)||_infty <= C(1+log_+ C_*) D(t)^2`.
- A swirl-profile bound for the extracted limit:
  \[
  |\Gamma_U(R,Z,\tau)|\le\frac{G}{\gamma_*}
  \bigl[1-(1+K\gamma_*R)e^{-K\gamma_*R}\bigr].
  \]
- A true-source **radial slice** bound (NOT a global-z integral):
  \[
  \sup_{Z,\tau\le0}\int_0^\infty q_U(R,Z,\tau)^2R\,dR
  \le 1+\log\frac{(KG)^2}{2}.
  \]
- A **conditional** critical-vorticity-to-Liouville route:
  \[
  \sup_{R,Z,\tau\le0}R^3|\eta_U|<\infty
  \;\Longrightarrow\;\sup R|V-c_0e_Z|<\infty
  \;\Longrightarrow\;U^\theta=0,
  \]
  where the ancient mild formulation must justify the *single constant* axial velocity `c_0`. Audit each implication and its true hypotheses.
- A **conditional** radial compression barrier: if `-U^R<=b(R)` for all relevant space-time points and
  \[
  \int_{R_0}^\infty R\exp\!\left[-\nu_*^{-1}\int_{R_0}^R b(\rho)d\rho\right]dR=\infty,
  \]
  then the ancient swirl vanishes. The delicate endpoint is `-R U^R <= nu_*(2+1/log R)` for `R>=R_0>=e`. Verify the scalar comparison and whether the full NS class admits it.
- A polynomial estimate for `int eta^2 dx + nu_*^{-2} int r^2 q^4 dx` has been proposed, but its unclosed signed radial-strain term prevents an actual uniform bound.

Older decoupled/prescribed-`xi` work sometimes inserts `L_T=sup_{s<=T}||eta(s)||_1` into an outer radial Moser step. **Do not make this unproved `L^1` an extra assumption, and do not import a decoupled estimate as a full NS estimate.**

## 4. Required routes and exact closure task

Investigate ALL of the following, followed by substantive alternatives if any fails:

1. **Direct critical eta control from the real physical solution.** The high-priority missing result is
   \[
   \boxed{\sup_{t_0\le t<T_*}\sup_{r,z}r^3|\eta(r,z,t)|<\infty,}
   \]
   or an explicitly quantified *weaker uniform bound on ALL expanding swirl-record cylinders* sufficient to deduce `sup R^3|eta_U|<infty`. Carry true `b[eta]` convection, swirl source, five-dimensional cutoff flux, radial strain, and viscosity. No hidden `L^1(eta)` or sign advantage. Prove constants independent of record `n` and cylinder radius.
2. **Signed compression exclusion without controlling all eta.** Deduce a radial envelope or alternative one-sided mechanism from the *fixed physical trajectory*. In rescaled coordinates identify exactly how the dimensionless observable `-r u^r` transforms; compare the strict `-r_n u^r>=1` at the swirl record to the far-radius critical threshold. Analyze recurrent supercritical compression on expanding annuli, not just pointwise strain at one record.
3. **Nonlinear mild/energy cancellations.** Retain all `V tensor V`, `W tensor W`, and interaction terms; test a compensated energy, near-axis source occupancy, adjoint identities, vorticity sign pairing, or localized `Gamma^2` estimates. If attempting an estimate involving `L^1(eta)`, trace its actual origin and replace it or close it from genuinely inherited data.
4. **Fixed-data historical restrictions.** Use actual finite initial energy, local smoothing away from `T_*`, finite dissipation, circulation maximum principle, pressure structure, and first-crossing inequalities. Check how physical bounds rescale: for example
   \[
   R^3|\eta_{U_n}|=\gamma_n^{-1}r^3|\eta|,
   \qquad \|\eta_{U_n}\|_1=\gamma_n^{-1}\|\eta\|_1.
   \]
   The normalized ancient energy generally diverges; never assume it is bounded.
5. **New applicable Liouville or parabolic maximum mechanism.** Verify exact mild/weak hypotheses and spatial growth classes from KNSS, Lei–Zhang, Lei–Zhang–Zhao, and other relevant work. Establish each hypothesis from THIS physical branch rather than postulating it for the ancient limit.

**Acceptance condition:** Deduce `U^theta ≡ 0` (or another genuine contradiction) from `(A)+(K)+(TAIL)+fixed datum+full NS`, contradicting `|U^theta(1,0,0)|=1`. A new bound alone, even a strong conditional one, is not enough. Do not falsely claim the stronger theorem from (A) alone unless you also prove (K) and (TAIL) or replace them.

## 5. Literature and prior-work files (when present in the working directory)

Read and audit: `NS_axis_research_prompt_case1_full_NS_swirl_closure.md`, `NS_axis_case1_full_NS_swirl_closure_research_report.md`, `NS_axis_case1_swirl_NS_Liouville_research_report.md`, `NS_axis_eta_critical_propagation_with_swirl_research_report_zh(1).md`, `NS_axis_remove_L1_weighted_Linf_research_report_zh(1).md`. Search the repository/project for name variants. If unavailable, the definitions and target above are self-contained; proceed without inventing their contents. Published starting points: KNSS (Acta Math. 2009, arXiv:0709.3599), Lei–Zhang Liouville (arXiv:1011.5066), Lei–Zhang–Zhao (arXiv:1701.00868), and *Criticality of the Axially Symmetric NS Equations* (arXiv:1505.02628). Verify theorems before citing.

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
