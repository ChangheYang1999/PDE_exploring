# 48-Hour Research Task: Nonexistence of Decaying Rotating Self-Similar Euler Profiles

## 0. Mission and working directory

Start by examining:

`Changhe/Euler/approach3`

This contains our previous numerical exploration of three-dimensional rotating self-similar Euler profiles, including the degree-6 free-parameter experiments.

**Your mission is to spend up to 48 hours investigating whether nontrivial, smooth, spatially decaying rotating self-similar Euler profiles can exist.**

The primary approach should be theoretical: **work toward proving nonexistence**, rather than attempting to construct another numerical candidate.

Do not restrict attention to small or large rotation rates. We want a result for arbitrary finite \(\omega\), ideally uniform in \(\omega\).

Use the original Euler project as reference material only. Create a new workspace:

`Changhe/Euler/approach3/nonexistence_48h/`

Do not modify existing simulation code, checkpoints, active jobs, or numerical results.

Organize several independent research agents, with one coordinating agent responsible for the overall proof strategy, mathematical consistency, and final synthesis.

Do not spend the entire 48 hours repeating existing literature or running numerical optimizations. The main objective is to establish genuinely new mathematical restrictions or a rigorous nonexistence theorem.

---

## 1. Exact mathematical problem

We study the three-dimensional incompressible Euler equations on the whole space:

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0.
\]

Consider rotating self-similar solutions with profile equation

\[
\boxed{
(1-c_l)U+
\big[(c_lI-\omega J)y+U\big]\cdot\nabla U
+\omega JU+\nabla P=0,
}
\]

\[
\boxed{\nabla\cdot U=0,}
\]

where

\[
J=
\begin{pmatrix}
0&-1&0\\
1&0&0\\
0&0&0
\end{pmatrix}.
\]

Here:

- \(U:\mathbb R^3\to\mathbb R^3\) is the unknown velocity profile.
- \(P:\mathbb R^3\to\mathbb R\) is the pressure.
- \(c_l>0\) is the spatial similarity exponent.
- \(\omega\in\mathbb R\) is the logarithmic rotation rate.

The primary range is

\[
\boxed{\frac25<c_l<\frac12.}
\]

However, whenever possible, extend the results to the larger range

\[
0<c_l<\frac12.
\]

The essential boundary condition is

\[
\boxed{
\lim_{|y|\to\infty}U(y)=0.
}
\]

This condition is mandatory. Do not replace it with linear growth, nonzero constant far-field velocity, or a nondecaying homogeneous asymptotic profile.

We seek nontrivial smooth solutions. Start with

\[
U\in C^2(\mathbb R^3)
\]

and determine the weakest regularity actually required.

Initially, do not assume \(U\in L^2\), integrable vorticity, or any special rate of decay. Those would make the problem much easier but could miss the range we care about.

Treat pressure carefully. Derive the consequences of the profile equation and its Poisson equation, rather than silently imposing an unjustified harmonic-pressure normalization.

### Primary conjecture

Investigate whether the following statement is true:

**Conjecture.** For every

\[
\frac25<c_l<\frac12,\qquad \omega\in\mathbb R,
\]

the only smooth divergence-free solution of the rotating self-similar Euler profile equation satisfying \(U(y)\to0\) as \(|y|\to\infty\) is

\[
\boxed{U\equiv0.}
\]

Try to prove this conjecture.

Do not assume it is true. If a counterexample exists, identify it and explain exactly why the proposed nonexistence mechanisms fail.

### Scope restrictions

Do not impose:

- Axisymmetry.
- Two-fold or other \(m\)-fold symmetry.
- \(z\)-odd or \(z\)-even symmetry.
- Smallness of \(U\).
- Smallness or largeness of \(\omega\).
- A priori proximity to an axisymmetric profile.
- A finite Fourier truncation as part of the theorem.

The theorem must address the full three-dimensional profile PDE.

---

## 2. Literature review and independent verification

Begin by studying the following works.

### Reference A: Constantin–Ignatova–Vicol (2026)

*On putative self-similarity for incompressible 3D Euler*

https://arxiv.org/abs/2602.17570

Particularly relevant:

- The \(c_l\ge2/5\) finite-energy constraint.
- The \(c_l\ge1/2\) result under outgoing assumptions.
- The axisymmetric \(c_l\ge1/2\) theorem.
- The similarity Bernoulli function.
- Lagrangian trajectories and stagnation points.
- Vorticity stretching and invariant circulation.

Determine exactly which arguments extend to rotating profiles and which fail.

The major challenge is to remove the outgoing assumption and axisymmetry.

### Reference B: Pineau–Vicol (2026)

*On rotated backwards self-similar solutions of the incompressible 3D Navier–Stokes equations*

https://arxiv.org/abs/2607.09619

Study their treatment of rotating similarity coordinates and weighted energy identities.

Determine whether any of their estimates or geometric ideas survive in the inviscid Euler setting.

Do not import estimates relying essentially on viscosity.

### Reference C: Chae–Shvydkoy

*On formation of a locally self-similar collapse in the incompressible Euler equations*

https://arxiv.org/abs/1201.6009

Also review relevant Liouville theorems of Dongho Chae.

Establish precisely which nonexistence results require \(L^p\) integrability, decay of vorticity, or assumptions incompatible with our desired far-field class.

### Reference D: New Liouville preprint — mandatory independent audit

*A Liouville theorem below the half-scaling exponent for three-dimensional Euler profiles*, Dylan Z. Liu.

https://zenodo.org/records/23461703

This record was created in October 2026 and claims a very strong nonexistence theorem for ordinary stationary Euler similarity profiles satisfying

\[
0<c_l<\frac12,\qquad U\in C^1,\qquad U=o(|y|).
\]

Its abstract also mentions rotationally discretely self-similar solutions.

**Do not assume this preprint is correct.**

Obtain and read the actual manuscript, independently audit its main proof, and determine:

1. Whether the advertised theorem is genuinely proved under its stated assumptions.
2. Whether there are hidden assumptions on pressure, flow completeness, invariant sets, or backward trajectories.
3. Whether its rank obstruction and center-stable manifold arguments are valid.
4. Whether the rotating Euler profile equation is covered directly, conditionally, or not at all.
5. Whether its techniques can be extended to arbitrary \(\omega\).

Pay particular attention to the distinction between ordinary, discretely self-similar, and continuously rotating self-similar profiles.

Write an independent audit. A paper abstract is not a proof.

---

## 3. First theoretical direction: exact integral identities

Derive all useful global identities from the rotating Euler profile equation.

We particularly care about identities that are independent of \(\omega\), or in which rotation contributes an antisymmetric term that disappears after integration.

### Energy identity

Under sufficient integrability and vanishing boundary fluxes, multiplying the profile equation by \(U\) gives

\[
\left(1-\frac52c_l\right)
\int_{\mathbb R^3}|U|^2\,dy=0.
\]

Thus, for \(c_l\ne2/5\), a nontrivial profile in the appropriate finite-energy class is impossible.

But our actual condition is only \(U\to0\), not \(U\in L^2\).

The key task is to extend this reasoning to weaker decay classes.

Investigate:

- Localized energy identities with radial cutoffs.
- Annular energy flux.
- Pressure fluxes at infinity.
- Weighted \(L^2\) estimates.
- Morrey-type bounds.
- Sharp lower bounds on energy growth in large balls.
- Whether the expected far-field profile is compatible with those bounds.

Do not infer \(U\in L^2\) merely from \(U\to0\).

Try to prove that a nonzero solution forces a lower bound on

\[
E(R)=\int_{|y|<R}|U(y)|^2\,dy
\]

which conflicts with decay or another exact identity.

If a contradiction requires additional quantitative decay, identify the precise borderline exponent and prove the resulting conditional theorem.

---

## 4. Second theoretical direction: Lagrangian flow, Bernoulli structure, and circulation

This should be one of the highest-priority research tracks.

Introduce the similarity transport field

\[
B(y)=(c_lI-\omega J)y+U(y).
\]

It has

\[
\boxed{\nabla\cdot B=3c_l>0.}
\]

Moreover,

\[
B(y)\cdot y=c_l|y|^2+U(y)\cdot y.
\]

Therefore \(U(y)\to0\) implies strictly outward radial transport sufficiently far from the origin, independently of \(\omega\).

Investigate the global dynamical consequences of these facts.

### Rotating Bernoulli identity

Let

\[
X=c_ly+U,\qquad B=X-\omega Jy,
\qquad \Omega=\nabla\times U.
\]

A candidate exact identity is

\[
\boxed{
(1-2c_l)X+\Omega\times B+\nabla H=0,
}
\]

where

\[
H=P+\frac12|X|^2
+\frac{c_l(c_l-1)}2|y|^2
-\omega(Jy)\cdot X.
\]

Independently check every sign and coefficient.

If the identity is correct, then

\[
\boxed{
B\cdot\nabla H=(2c_l-1)X\cdot B.
}
\]

For \(\omega=0\), this recovers the familiar sign-definite similarity Bernoulli mechanism.

For arbitrary \(\omega\), the term \(X\cdot B\) need not be positive.

This is a central mathematical obstacle.

Try to determine whether there is:

- Another useful Lyapunov function.
- A modified Bernoulli quantity with a sign.
- An averaged monotonicity formula.
- A geometric condition that follows automatically from decay.
- An invariant-measure argument excluding recurrent internal trajectories.
- A way to combine the Bernoulli function with vorticity stretching.

Do not simply assume an outgoing property. Try to prove the required transport properties from the equation and \(U\to0\).

### Circulation

Consider a closed loop \(C(s)\) advected by

\[
\frac{dY}{ds}=B(Y).
\]

Independently establish the circulation identity

\[
\boxed{
\frac{d}{ds}\oint_{C(s)}U\cdot d\ell
=(2c_l-1)\oint_{C(s)}U\cdot d\ell.
}
\]

Therefore

\[
\oint_{C(s)}U\cdot d\ell
=e^{(2c_l-1)s}
\oint_{C(0)}U\cdot d\ell.
\]

Study its consequences for invariant loops, periodic orbits, recurrent trajectories, and bounded invariant sets.

The goal is to extend the existing axisymmetric circulation obstruction to fully non-axisymmetric rotating profiles.

An especially valuable result would be a theorem showing that any nonzero decaying smooth profile with \(c_l<1/2\) necessarily generates an invariant structure incompatible with this circulation law.

---

## 5. Third theoretical direction: vorticity and dynamical rigidity

Derive the exact vorticity profile equation:

\[
\boxed{
\Omega+B\cdot\nabla\Omega
-(\Omega\cdot\nabla)U+\omega J\Omega=0.
}
\]

Study the global flow of \(B\), its deformation gradient, and the transport of the vorticity two-form.

In particular:

- Analyze forward and backward characteristics.
- Distinguish trajectories that escape to infinity, converge to stagnation points, or remain in bounded invariant sets.
- Use the positivity of \(\nabla\cdot B\) correctly.
- Analyze fixed points of \(B\) using the matrix \(\nabla B\).
- Determine what \(c_l<1/2\) forces at stagnation points.
- Investigate invariant curves, invariant surfaces, periodic orbits, and nonpoint backward limit sets.
- Explore whether recurrent trajectories force vorticity to vanish.
- Study how the skew matrix \(-\omega J\) modifies, or fails to modify, stretching estimates.

Do not infer that positive divergence alone rules out periodic orbits. That is not generally true.

If a rank or topological obstruction is found, state it precisely and establish all regularity assumptions required.

A particularly strong result would be a proof that

\[
\Omega\equiv0.
\]

If \(U\) is smooth, divergence-free, curl-free, and decays at infinity, then standard harmonic Liouville arguments yield \(U\equiv0\).

Thus vanishing vorticity would complete the proof.

---

## 6. Fourth theoretical direction: Fourier-mode coupling and symmetry breaking

Do not impose symmetry, but exploit Fourier decomposition as an analytical tool.

Write

\[
U(r,\theta,z)=
\sum_{m\in\mathbb Z}
u_m(r,z)e^{im\theta}
\]

in cylindrical components, with the appropriate reality and regularity constraints.

The rotating term becomes

\[
-im\omega u_m.
\]

The nonlinear term couples modes through

\[
k+\ell=m.
\]

Derive the exact infinite Fourier system, keeping all cylindrical geometric terms and pressure constraints.

Then investigate:

1. Whether decay and the Euler equation force any nonzero mode to vanish.
2. Whether the angular mean can be controlled without assuming axisymmetry.
3. Whether high angular modes can be excluded using angular regularity and rotation.
4. Whether intermode energy or circulation identities lead to cancellation.
5. Whether there is a nonlinear spectral gap or rigidity mechanism for arbitrary \(\omega\).
6. Whether a hypothetical non-axisymmetric profile must have a specific, impossible distribution of Fourier energy.

You may analyze truncations \(|m|\le L\) to identify candidate inequalities, but **a theorem about fixed \(L\) is not a theorem about the full Euler PDE**.

Any passage \(L\to\infty\) requires estimates uniform in \(L\).

Do not assume a profile is a small perturbation of an axisymmetric one. The conjecture includes finite-amplitude non-axisymmetric solutions.

---

## 7. Fifth direction: far-field rigidity and pressure

We require

\[
U(y)\to0.
\]

Try to determine what the stationary profile equation itself forces about its decay rate.

Investigate whether a nonzero decaying solution must have an asymptotic form such as

\[
U(y)\sim |y|^{-\alpha}F(\widehat y),
\]

and derive the correct angular equation including rotation and pressure.

Do not assume a homogeneous asymptotic expansion exists without proof.

If possible, establish it from the PDE.

Important issues:

- The pressure Poisson equation
  \[
  -\Delta P=\partial_iU_j\,\partial_jU_i.
  \]
- Harmonic ambiguity in pressure.
- The difference between \(U\to0\) and derivative decay.
- Possible oscillatory or nonhomogeneous far-field behavior.
- Slow algebraic tails with infinite total profile energy.
- Boundary fluxes through large spheres.
- Whether \(\omega\) changes the admissible asymptotic exponents.
- Whether characteristic angular dynamics lead to nontrivial log-periodic tails.

Particularly investigate whether a nonzero decaying profile necessarily develops a tail that violates global smoothness, circulation conservation, or a suitable energy identity.

If one can rigorously exclude all allowed far-field tails, that would provide an alternative nonexistence proof.

---

## 8. Counterexample and consistency audit

Even though the main goal is nonexistence, assign an independent agent to search for ways the conjecture could fail.

This agent must not merely repeat the other agents' arguments.

Test known explicit Euler solutions and candidate profiles:

- Purely linear strain or rotating linear flows.
- Irrotational and potential flows.
- Steady Euler fields.
- Axisymmetric profiles with and without swirl.
- Non-axisymmetric rotating steady states.
- Homogeneous Euler solutions.
- Translation and Galilean transformations.
- Profiles with nonzero constant far-field limits.
- Singular solutions at the origin.
- Solutions with insufficient regularity.
- Profiles with infinite kinetic energy.

For each potential example, check the actual target conditions:

\[
U\in C^2(\mathbb R^3),\qquad
\nabla\cdot U=0,\qquad
U(y)\to0,
\]

and the complete Euler profile equation.

Do not count examples violating smoothness or decay.

Also check whether existing literature contains genuine counterexamples.

If a candidate refutes the conjecture, stop trying to prove the false statement and explain the counterexample rigorously.

If the conjecture remains plausible, identify every known mechanism that a proof must exclude.

---

## 9. Numerical work is secondary

The original project contains GPU-based numerical searches of Euler profiles.

You may inspect the methods, parameter choices, basis, and results.

However, this task must not become another long nonlinear optimization campaign.

Use numerical calculations only when they can materially support theoretical work, for example:

- Checking an exact identity or symbolic derivation.
- Finding counterexamples to a proposed inequality.
- Testing whether a candidate Lyapunov function is sign-definite.
- Studying characteristic flows for representative hypothetical backgrounds.
- Finding sharp constants in a conditional inequality.
- Testing a finite-dimensional conjecture before proving it analytically.

Any computation should have a clear theoretical question and an explicit pass/fail criterion.

No amount of failure to find a profile numerically constitutes a nonexistence proof.

Do not consume extensive GPU time unless there is a specific, justified reason.

---

## 10. Multi-agent organization

Use one coordinating agent and at least four independent research functions.

### Coordinator

Responsible for:

- Maintaining the global proof plan.
- Assigning independent mathematical approaches.
- Tracking which assumptions are used.
- Comparing seemingly contradictory conclusions.
- Identifying the strongest promising argument.
- Preventing duplication.
- Reallocating effort as new results appear.
- Producing the final logically consistent theorem and proof-status report.

### Theory Agent A: Integral estimates and far field

Focus on energy identities, weighted estimates, pressure, decay, and possible Liouville arguments.

### Theory Agent B: Lagrangian geometry

Focus on Bernoulli, circulation, stagnation points, invariant sets, and vorticity transport.

### Theory Agent C: Spectral and Fourier methods

Focus on symmetry breaking, all angular modes, nonlinear mode coupling, and whether arbitrary \(\omega\) admits a uniform obstruction.

### Literature and counterexample agent

Independently audit the cited results, especially the new Liouville preprint, and actively search for genuine counterexamples or hidden hypotheses.

### Independent mathematical auditor

Review all proposed proofs adversarially.

For each theorem, check:

- Exact hypotheses.
- Boundary terms.
- Pressure normalization.
- Completeness of characteristic flow.
- Spectral and functional-analytic assumptions.
- Possible circular reasoning.
- Whether nonexistence is proved only for a smaller class.
- Whether the argument remains valid for arbitrary \(\omega\).

The auditor should be involved repeatedly, not only during the final hours.

All agent conclusions must be written to files and made available to the coordinator.

---

## 11. Time allocation — 48 hours

Use the total period as a hard research budget.

### Hours 0–4: Foundation

- Inspect the existing Euler project.
- Verify the exact rotating profile equation.
- Establish the vorticity, Bernoulli, circulation, Fourier, and energy identities.
- Review the key literature.
- Audit the strongest immediately relevant claims.
- Formulate the nonexistence conjecture with precise hypotheses.

### Hours 4–16: Independent proof attempts

Run the theoretical tracks in parallel.

Prioritize arguments that do not require extra assumptions beyond smoothness and decay.

Require every agent to record both promising results and explicit failed proof steps.

### Hours 16–30: Concentrated development

The coordinator identifies the one or two strongest approaches.

Devote greater effort to closing missing lemmas.

Use targeted symbolic or numerical tests where useful.

Avoid starting unrelated numerical searches.

### Hours 30–42: Strengthen results

Try to upgrade conditional results toward the full conjecture.

If full nonexistence appears inaccessible, seek a mathematically substantial partial theorem with assumptions as weak as possible.

Perform independent audits of all major lemmas.

### Hours 42–48: Final verification and synthesis

Recheck the strongest theorem from beginning to end.

Produce a standalone mathematical report with exact derivations, rigorous conclusions, and remaining obstacles.

Do not spend these final hours starting an experiment that cannot be meaningfully evaluated.

Save progress regularly and maintain resumable checkpoints.

---

## 12. Deliverables

Create at least the following files in the new research workspace:

`README.md`

Problem statement, workspace structure, references, and reproducibility instructions.

`LITERATURE_REVIEW.md`

Precise statements of relevant existing theorems, their assumptions, and their applicability to rotating Euler profiles.

`PREPRINT_AUDIT.md`

Independent audit of the newly identified Liouville preprint, including proof gaps if found.

`EXACT_IDENTITIES.md`

Fully checked derivations of the rotating Euler profile, pressure equation, vorticity equation, Bernoulli identity, circulation formula, and Fourier equations.

`THEOREM_ATTEMPTS.md`

Detailed proof attempts, including unsuccessful arguments and the exact steps that fail.

`COUNTEREXAMPLE_AUDIT.md`

Explicit examples, possible counterexamples, and tests of proposed inequalities.

`PROOF_OBSTRUCTIONS.md`

A prioritized record of unresolved mathematical obstacles.

`FINAL_REPORT.md`

The primary deliverable.

The final report must contain:

1. The strongest rigorously established theorem.
2. Its complete proof.
3. Precise assumptions and regularity requirements.
4. Whether the theorem holds for every \(\omega\).
5. Whether non-axisymmetric profiles are genuinely covered.
6. Whether \(U\to0\) alone is sufficient.
7. The status of the main nonexistence conjecture.
8. Any conditional or partial nonexistence results.
9. Any credible counterexample.
10. The next most promising mathematical step.

Use the labels **PROVED**, **CONDITIONAL**, **NUMERICAL**, **CONJECTURAL**, and **UNRESOLVED** consistently.

Do not label a formal argument as a complete proof.

---

## 13. Standards for success

### Ideal outcome

Prove that for any

\[
\frac25<c_l<\frac12,\qquad \omega\in\mathbb R,
\]

every smooth divergence-free solution of

\[
(1-c_l)U+
[(c_lI-\omega J)y+U]\cdot\nabla U
+\omega JU+\nabla P=0
\]

satisfying

\[
U(y)\to0
\]

must be identically zero.

An even stronger theorem covering \(0<c_l<1/2\) would be highly desirable.

### Acceptable substantial outcome

If the full conjecture cannot be proved, establish a new rigorous result, for example:

- Nonexistence under a sharp, explicitly stated decay condition.
- Nonexistence under a dynamical condition weaker than the known outgoing condition.
- A general restriction on invariant sets or stagnation points.
- A rigidity theorem uniform in arbitrary \(\omega\).
- An inequality showing that any hypothetical solution must possess an unusual, precisely characterized structure.
- A genuine obstruction to a previously plausible proof strategy.
- A rigorous counterexample to the conjecture.

These outcomes are valuable only if fully justified and clearly distinguished from heuristic expectations.

### Unacceptable outcome

Do not present any of the following as a completed nonexistence proof:

- A numerical search that fails to find solutions.
- A proof valid only for finite Fourier truncations.
- An argument assuming axisymmetry.
- An argument using \(U\in L^2\) without proving it or explicitly stating it as an additional assumption.
- A result limited to small or large \(\omega\) while claiming arbitrary \(\omega\).
- A Bernoulli monotonicity argument that ignores the rotating term.
- A proof silently assuming all characteristics escape.
- An unverified citation to a recent preprint.
- A formal asymptotic expansion that does not cover the full nonlinear problem.

## 14. Final instruction

**Spend the 48-hour budget seriously attempting to prove nonexistence.**

The research priority is:

\[
\boxed{
\text{Exact identities}
\longrightarrow
\text{dynamical and analytic rigidity}
\longrightarrow
\text{global Liouville theorem}.
}
\]

Do not limit the analysis to perturbative regimes \(\omega\to0\) or \(|\omega|\to\infty\). These may be used for insight, but the main objective concerns arbitrary rotation rates and potentially finite-amplitude non-axisymmetric solutions.

Think creatively. If an existing proof mechanism fails because of rotation, identify the precise obstruction and attempt to remove it.

Keep the proof standards at research-paper level.

Most importantly, **do not force a nonexistence conclusion if the mathematics does not support it**. The objective is to determine whether these decaying rotating Euler profiles can exist, with nonexistence as the leading hypothesis to investigate.

Continue autonomously through the allotted research period, keep progress reproducible, and finish with the strongest mathematically defensible result.