# 24-Hour Intensive Research Campaign: Close the Stationary IPM Existence Proof

## CRITICAL INSTRUCTIONS — READ FIRST

**Previous workspace:** `Changhe/IPM/combined2`

**New workspace:** `Changhe/IPM/combined3`

**Strict time budget: 24 hours of sustained research.**

**The sole success criterion is a complete, rigorous, fixed-parameter existence theorem for stationary self-similar IPM near the current numerical profile.**

This is NOT a preliminary investigation, feasibility study, or planning exercise. It is an intensive continuation of an existing research program that already has substantial theoretical and numerical results.

### Non-negotiable execution rules

1. **Do not stop merely because an intermediate estimate fails.** A failed sufficient condition is not a proof that the existence argument cannot be closed. Find a better estimate, change the decomposition, or pursue an alternative analytical mechanism.

2. **Do not stop after deriving conditional theorems, identifying obstacles, or producing promising numerical results.** These are intermediate milestones, not completion criteria.

3. **Do not stop after completing the three proposed improvements.** Their purpose is to close the full existence argument. If they are insufficient, continue improving or replacing them.

4. **Do not restart the project.** Read and inherit the authoritative results, proofs, numerical fields, and verification machinery from `combined2`. Work exclusively in `combined3`.

5. **Do not spend the campaign merely making plans or preparing reports.** Prioritize actual mathematical derivations, implementation, numerical computation, and rigorous certification.

6. **Continue working until either the complete theorem is proved or the 24-hour hard deadline is reached.** Do not treat a temporary obstacle, unsuccessful experiment, or partial conclusion as a reason to terminate early.

7. **Do not claim success without proof.** Every numerical inequality used in the final theorem must be rigorously certified, and every required analytical assumption must be proved or reduced to a rigorously verified condition.

8. **If the 24-hour deadline is reached without closure, deliver the strongest established results and the exact remaining gaps.** Never replace a missing proof with an assumption, numerical heuristic, or unsupported declaration.

The research should be aggressive, persistent, and adaptive, while maintaining full mathematical rigor.

---

# 1. Mathematical objective

Study the stationary self-similar IPM system
\[
\boxed{
\begin{aligned}
(c_lX+u)\cdot\nabla\rho&=\rho,\\
-\Delta\psi&=\partial_x\rho,\\
u&=\nabla^\perp\psi.
\end{aligned}}
\]

Fix
\[
\boxed{
c_l=\bar c_l=
\frac{4076476460239181}{2251799813685248}.
}
\]

The similarity exponent must not vary.

The original Candidate 007 remains unchanged. The primary corrected numerical reference is Candidate 013, denoted by \(\rho_*\), with associated velocity \(u_*\).

Its residual is
\[
F_*=(c_lX+u_*)\cdot\nabla\rho_*-\rho_*.
\]

The previous campaign rigorously certified
\[
\boxed{
\|F_*\|_2<7.961207\times10^{-7},
}
\]
and
\[
\boxed{
\|J^{21/10}(WF_*)\|_2<0.00555458,
}
\]
where
\[
J=(1-\Delta)^{1/2},
\qquad
W(X)=\sqrt{1+4|X|^2}.
\]

A conditional existence theorem is already available.

**Your job is to turn this conditional theorem into an unconditional existence theorem by rigorously verifying or improving all remaining estimates.**

Do not prioritize further residual minimization unless it becomes demonstrably necessary for closure.

---

# 2. Existing correction equation and energy estimates

Given a perturbation \(k\), consider
\[
\boxed{
(c_lX+u_*+U[k])\cdot\nabla g
+U[g]\cdot\nabla\rho_*-g=-F_*,
}
\]
where
\[
U[g]=\nabla^\perp(-\Delta)^{-1}\partial_xg.
\]

The required correction estimates are in
\[
L^2(\mathbb R^2)
\cap
\left\{
g:J^{21/10}(Wg)\in L^2
\right\}.
\]

The existing \(L^2\) bound is
\[
\boxed{
\|g\|_2
\le\frac47\|F_*\|_2
\le4.549261\times10^{-7},
}
\]
subject to the actual solvability conditions.

For the high-regularity estimate, let
\[
G=J^{21/10}(Wg),\qquad
R=(R_1,R_2)^T,
\]
with
\[
R_j=\partial_j(-\Delta)^{-1/2}.
\]

The principal transport commutator has already been incorporated into the pointwise matrix
\[
\boxed{
\begin{aligned}
\mathcal M_*(X)
={}&
\left(
c_l+1+
\frac{(c_lX+u_*)\cdot X}{1/4+|X|^2}
\right)I\\
&-\frac{21}{10}\operatorname{Sym}D(c_lX+u_*)\\
&+
\begin{pmatrix}
\partial_y\rho_*&-\frac12\partial_x\rho_*\\
-\frac12\partial_x\rho_*&0
\end{pmatrix}.
\end{aligned}}
\]

The previous report establishes, under its retained analytic premises,
\[
\boxed{
\mathcal M_*(X)\ge0.704955805507\,I.
}
\]

The main conditional closure plan uses
\[
b_0=0.55,\qquad L_B\le0.3651689966.
\]

The currently available budgets for the remaining high-order commutator contributions are
\[
\boxed{
\varepsilon_{\rm rest}\le0.002328694018,
\qquad
C_{\rm rest}\le9.941475955\times10^9.
}
\]

A fallback configuration permits
\[
\varepsilon_{\rm rest}\le0.009854567905,
\]
with its own low-order budget and additional kernel requirements.

These numbers are starting points, **not constraints that must be preserved if better estimates can be obtained**.

Before changing the argument, recover and check the exact derivations, all relevant operator conventions, and the complete nonlinear loss formula \(L_B\) from `combined2`.

Do not confuse \(L_B\) with the separate matrix loss from Lemma KB.

---

# 3. Priority A — Directly improve the \(L^2\) coercivity for Candidate 013

The previous proof obtains Candidate 013's coercivity by transferring the older Candidate 007 bound and allowing for
\[
\|\nabla(\rho_*-\bar\rho)\|_\infty\le\frac14.
\]

This is potentially wasteful.

Instead, directly estimate
\[
\boxed{
\sup_{\|g\|_2=1}
\int_{\mathbb R^2}
g\,U[g]\cdot\nabla\rho_*\,dX.
}
\]

Obtain the strongest practically certifiable constant \(\beta_{L^2}\) such that
\[
\boxed{
(c_l+1)\|g\|_2^2
-\int g\,U[g]\cdot\nabla\rho_*
\ge\beta_{L^2}\|g\|_2^2.
}
\]

Reuse the existing rigorous quadratic-form verification machinery, adapting it to the full Candidate 013 profile.

Immediately propagate the improved constant into the \(L^2\) correction radius and the final invariant-ball inequality.

Do not spend excessive time polishing this bound if its improvement has negligible influence on closure. Once its benefit is established, move directly to the high-order argument.

---

# 4. Priority B — Use the full pointwise coercivity matrix to improve the residual estimate

The previous argument often replaces the full matrix with
\[
0.704955805507\,I.
\]

This throws away potentially valuable spatial and directional information.

**Retain the complete quadratic form**
\[
\boxed{
\int_{\mathbb R^2}
(RG)^T\mathcal M_*(X)(RG)\,dX.
}
\]

In particular, improve the residual pairing by using
\[
\boxed{
\begin{aligned}
&|\langle J^{21/10}(WF_*),G\rangle|\\
&\quad\le
\left(
\int(RG)^T\mathcal M_*(RG)
\right)^{1/2}\\
&\qquad\times
\left(
\int
(RJ^{21/10}(WF_*))^T
\mathcal M_*^{-1}
(RJ^{21/10}(WF_*))
\right)^{1/2}.
\end{aligned}}
\]

All integrals are over \(\mathbb R^2\).

The Riesz transforms of the residual must be computed or rigorously enclosed. They cannot be replaced by the original residual pointwise.

Tasks:

1. Implement the full-matrix residual evaluation for Candidate 013.
2. Obtain rigorous numerical bounds, including truncation, discretization, and tail errors.
3. Compare its effective contribution with the original global Cauchy–Schwarz estimate.
4. Incorporate the improvement into the actual nonlinear closure calculation.
5. Investigate whether the same full-matrix method can improve the estimates of the remaining commutator quadratic forms.

Do not spend significant resources further optimizing the global minimum eigenvalue if the full-matrix method is more effective.

---

# 5. Priority C — Finite-rank approximation of compact commutators

**This is the highest-priority research direction.**

After moving all principal-order terms to the left-hand side, collect the remaining background commutators into their exact quadratic form \(\mathcal E(g)\).

The desired estimate is
\[
\boxed{
|\mathcal E(g)|
\le
\varepsilon\|J^{21/10}(Wg)\|_2^2
+C_\varepsilon\|g\|_2^2.
}
\]

The challenge is to make both constants compatible with invariant-ball closure.

### C1. Identify the genuinely compact contributions

Reconstruct the exact commutators from `combined2`.

Separate the residual quadratic form into compact and noncompact components.

Prove compactness in the correct operator spaces. Do not infer global compactness merely from a negative pseudodifferential order.

Use spatial localization and coefficient decay where appropriate.

Do not impose the previous decomposition if it introduces unnecessary losses.

### C2. Construct actual finite-rank approximations

For each genuinely compact quadratic form, construct a finite-rank approximation using smooth functions.

If \(K\) is the relevant compact operator, seek \(K_N\) satisfying
\[
\boxed{
\|K-K_N\|_{L^2\to L^2}\le\varepsilon.
}
\]

The remainder then contributes at most
\[
\varepsilon\|G\|_2^2.
\]

Write
\[
K_NG=
\sum_{i,j=1}^N
a_{ij}\langle G,\varphi_j\rangle\varphi_i.
\]

Use
\[
\langle G,\varphi_j\rangle
=
\langle g,WJ^{21/10}\varphi_j\rangle
\]
to control the finite-rank contribution by \(\|g\|_2^2\).

In particular, compute the Gram matrix
\[
B_{ij}
=
\langle WJ^{21/10}\varphi_i,
WJ^{21/10}\varphi_j\rangle,
\]
and obtain a rigorous bound for the finite-rank quadratic form through
\[
\boxed{
C_N=\|B^{1/2}AB^{1/2}\|_{\rm op},
}
\]
where \(A=(a_{ij})\), with the appropriate self-adjoint representation.

This must be implemented, not merely stated as an abstract possibility.

**Produce actual basis functions, matrices, finite-rank tail estimates, and certified constants.**

### C3. Optimize the correct quantity

Do not minimize \(\varepsilon\) independently.

If \(R_*\) is the \(L^2\) radius and \(M\) the high-regularity ball radius, the relevant combined loss is
\[
\boxed{
\varepsilon+\frac{R_*^2}{M^2}C_\varepsilon.
}
\]

Because \(R_*\) is extremely small, a large low-order constant may be acceptable if it buys a substantial reduction in the high-order loss.

Actively investigate different bases, spatial cutoffs, frequency cutoffs, near/far decompositions, and matrix approximation methods.

**If one approximation family fails, try another. Do not stop at the first negative result.**

### C4. Treat the noncompact remainder

For all genuinely noncompact contributions, pursue sharper estimates using:

- Far-field asymptotics and coefficient decay.
- Cancellations among commutator terms.
- Joint quadratic-form estimates instead of term-by-term norm bounds.
- Spatial-frequency localization.
- The full pointwise coercivity matrix.
- Alternative parameter choices or energy decompositions.

If the existing H4-REST methodology cannot meet its budget, replace it with a stronger argument.

The ultimate target is the full form estimate, not certification of one particular intermediate lemma.

---

# 6. Do not neglect the other existence-theorem hypotheses

The previous report also leaves several operator and analytic verification conditions unresolved, including:

- The actual generator and semigroup properties.
- Uniform solvability of the frozen linear equation on the perturbation ball.
- Near-field analytic and localization assumptions.
- Far-field analytic form bounds.
- Reference-ball and graph-witness conditions.
- The complete invariant-ball inequality.

**Do not leave these issues untouched while concentrating exclusively on numerical commutator constants.**

Recover the exact conditions from the original theorem.

For each condition, determine whether it follows from existing results, requires a new analytical proof, or can be reduced to a rigorously computable inequality.

Prove it or verify it.

If necessary, pursue the operator theory and numerical estimates concurrently.

The final theorem must not depend on any unverified assumptions.

---

# 7. Full closure is the mandatory objective

After obtaining improved estimates, recompute the entire invariant-ball argument using the original nonlinear fixed-point theorem.

Do not check only one scalar inequality.

Verify every condition needed to conclude the existence of a correction \(k\) satisfying
\[
\boxed{
\rho=\rho_*+k
}
\]
and
\[
\boxed{
(c_lX+U[\rho])\cdot\nabla\rho=\rho.
}
\]

The proof must preserve the fixed similarity exponent, required symmetry, normalization, and regularity conditions.

The target is an unconditional theorem with explicitly certified hypotheses and constants.

If the original route fails, investigate modifications that preserve the essential \(L^2\) coercivity and compactness mechanism.

You may change auxiliary norms, cutoff parameters, finite-rank bases, proof decompositions, or the high-regularity estimate itself when mathematically advantageous.

**Do not remain attached to an inefficient proof strategy merely because it was used in `combined2`.**

However, do not abandon the existing successful theory without a concrete mathematical reason.

---

# 8. Mandatory 24-hour execution protocol

Treat the 24-hour deadline as a hard research budget, not a target for filling a report.

### At the beginning

Immediately:

- Inspect the authoritative files and certificates in `combined2`.
- Create the independent working environment in `combined3`.
- Reconstruct the exact current closure inequalities and all outstanding hypotheses.
- Identify which numerical certificates and mathematical proofs can be reused.
- Begin the new calculations.

Do not spend an excessive fraction of the available time rewriting previous reports.

### Throughout the campaign

Maintain active work on the problems that are genuinely blocking the theorem.

Use parallel independent research or verification tasks when available and useful.

Whenever a calculation or proposed lemma fails:

1. Diagnose precisely why it failed.
2. Determine whether the obstruction is intrinsic or merely an artifact of the estimate.
3. Try a sharper constant, different decomposition, or alternative method.
4. Resume computation or proof development immediately.

**A failed estimate is not a stopping criterion.**

Maintain restartable checkpoints and a concise, continuously updated ledger of proved and open obligations.

Reports and internal summaries must support active research, not replace it.

### Before declaring success

Independently check the complete logical dependency chain.

Every operator estimate, numerical enclosure, normalization, graph condition, and self-map inequality must have a valid proof or reproducible rigorous certificate.

Do not declare the theorem proved based on floating-point results, conditional estimates, or a formal argument with unresolved assumptions.

### Stopping rule

**Do not voluntarily conclude the campaign before proving the full existence theorem.**

If the theorem remains open, continue working and exploring alternatives for the available 24-hour period.

At the 24-hour hard deadline, stop further research and produce the final report, even if closure has not been obtained.

The final report must clearly distinguish a complete proof from partial progress.

No hypothetical result may be presented as established.

---

# 9. Required final deliverables

Save all work under `Changhe/IPM/combined3`.

The final deliverables must include:

1. The direct Candidate 013 \(L^2\) coercivity analysis and its strongest certified constant.
2. The full-matrix high-regularity residual estimate and its rigorous numerical evaluation.
3. The compact/noncompact decomposition of the remaining commutators.
4. Explicit finite-rank approximations, matrices, and operator-norm certificates.
5. Certified or clearly qualified \((\varepsilon,C_\varepsilon)\) bounds.
6. A complete updated nonlinear closure calculation.
7. Proofs or precise verification results for every remaining operator and analytic condition.
8. An independently checkable final mathematical report.
9. Reproducible code, numerical outputs, and restartable state.

Compare the final results with `combined2`, including the \(L^2\) coercivity constant, effective residual norm, high-order losses, low-order constants, and final invariant-ball margin.

If existence is established, state the exact theorem and provide its complete proof.

If existence is not established by the deadline, give the strongest rigorously justified results and identify the remaining obstruction with explicit formulas and numerical budgets.

Do not conceal, downgrade, or reclassify open obligations merely to declare success.

---

# FINAL DIRECTIVE

**You have 24 hours to push this project as far as mathematically possible, with a complete fixed-parameter existence proof as the single success criterion.**

Do not stop at planning.

Do not stop at a conditional theorem.

Do not stop because one commutator estimate fails.

Do not stop because the first finite-rank approximation is insufficient.

Do not stop after improving numerical constants if the invariant-ball argument remains open.

Continue developing, testing, refining, and verifying alternative estimates until the entire proof closes or the hard 24-hour deadline is reached.

**The objective is a rigorously established exact stationary IPM solution near Candidate 013. Everything else is intermediate progress.**

Begin immediately in `combined3`.
