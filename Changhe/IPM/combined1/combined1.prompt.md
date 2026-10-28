# S1 / IPM — 24-Hour Joint Theory–Numerics Program

## Mission

You have **24 hours of wall-clock research time** to make the strongest possible progress toward a rigorous a posteriori existence proof of an exact self-similar profile for the full-plane IPM equation, using the existing S1 / case4 numerical profile as the starting point.

This task has **two equally important, tightly coupled research tracks**:

- **Track T — Theory:** Derive substantially sharper and/or weaker-space a posteriori estimates, with the explicit goal of relaxing the required residual smallness. Do not regard the existing conditional existence theorem as the final theoretical endpoint.
- **Track N — Numerics:** Repair the incorrect far-field residual asymptotics and keep reducing the residual, through further optimization and, where useful, expanded or redesigned bases.

**You must launch two distinct batches of agents, one dedicated to theory and one dedicated to numerics. Both batches must work concurrently throughout the research window.** They should exchange concrete mathematical requirements and numerical results at regular checkpoints, but must maintain independent workspaces and clearly separated responsibilities.

The objective is not merely to improve either track in isolation. The objective is to bring them together:

\[
\boxed{\text{certified numerical residual}<\text{rigorously allowed residual threshold}.}
\]

The two sides must compare quantities **in exactly the same function spaces and with exactly the same normalization**.

Do not claim that the project has closed unless all hypotheses of an actual existence theorem are rigorously verified for one actual reference profile.

---

## 1. Directories and source-of-truth policy

The available directories are:

- `Changhe/IPM/case4` — existing S1 numerical computations, optimizers, bases, checkpoint states, numerical data, and previous numerical investigations.
- `Changhe/IPM/analysis2` — the recent 18-hour theory investigation, including its conditional existence theorems, linear estimates, far-field analysis, obstructions, and verification artifacts.
- `Changhe/IPM/Holder` — previous work on the Hölder seminorm constants of planar second-order Riesz transforms and related estimates.
- `Changhe/IPM/combined1` — **the only directory in which this new campaign may create, edit, execute, or save its own research artifacts**.

Resolve the true absolute paths using the filesystem, starting from the working directory. Never assume a path exists merely because it was mentioned.

**The first three directories are strictly read-only.**

You may inspect source files, manuscripts, logs, checkpoints and earlier prompts there. You must not modify them, run optimizers or notebooks inside them, install dependencies there, or allow Python/Julia imports to create caches in them.

Before executing existing code, create a complete working copy of the necessary source tree inside `combined1`, including all dependencies needed to reproduce the relevant calculations. Verify that symlinks, output paths, caches and temporary files cannot write back into the protected sources.

Do not interfere with any optimization already running in `case4`.

All new mathematical notes, experimental programs, certificates, candidate coefficients, checkpoint states, logs and final reports belong inside `combined1`.

Suggested structure:

```text
combined1/
  coordination/
  theory/
    hou_literature/
    spaces/
    sharp_constants/
    inverse/
    nonlinear_closure/
    audits/
  numerics/
    source_copy/
    far_field/
    optimization/
    candidate_states/
    certification/
    audits/
  shared/
    theory_requirements/
    numerical_results/
    candidate_snapshots/
  reports/
  checkpoints/
```

If the layout needs adjustment, preserve the ownership separation.

---

## 2. Mathematical problem and existing results

We study

\[
F(\rho;c_l)
=
(c_l X+U[\rho])\cdot\nabla\rho-\rho=0
\]

on \(\mathbb R^2\), where

\[
U[h]=(-R_1R_2h,R_1^2h).
\]

Use the S1 symmetry class: \(\rho\) is even in \(x\) and odd in \(y\).

For a reference profile \(\bar\rho\), the fixed-exponent linearization is

\[
Lh
=
(c_lX+U[\bar\rho])\cdot\nabla h-h
+U[h]\cdot\nabla\bar\rho.
\]

The nonlinear correction equation is

\[
Lh+U[h]\cdot\nabla h=-F(\bar\rho;c_l).
\]

The strain is

\[
c[h]=\partial_yU_2[h](0),
\]

including the necessary local/contact term in its singular-integral representation.

The current S1 analysis treats \(c_l\) and the leading far-field angular profile as fixed, thereby excluding the scaling direction from the correction space. Preserve that logic unless an alternative normalization is rigorously derived.

### Current theoretical baseline

The recent `analysis2` report gives the following conditional results:

1. A common linear inverse in a weighted Sobolev space slightly above order two, with inverse constant at most 20 for the fixed background.
2. Simultaneous control of \(H^{-1}\), \(L^2\), Hölder norms of \(h\) and \(\nabla h\), the center moment, and \(c[h]\).
3. A rough-velocity linear inverse obtained by absorbing \(U[k]\cdot\nabla h\) into transport.
4. A two-norm nonlinear contraction, with an explicit residual threshold.

In particular, one proved sufficient condition has the form

\[
N_s(F)\le6.3578288\times10^{-7},
\qquad s=2^{-18},
\]

together with certified background hypotheses, producing an exact correction of size at most \(2^{-16}\).

Here \(N_s\) is built from the weighted second-order energy with a small fractional regularity gain.

The report also constructs weighted and logarithmic correction spaces. Their current thresholds are even more restrictive for the examined numerical references.

**These are baselines, not final targets.**

An optimization of the existing smoothness index and ball radius improves the first threshold by only about 3%. Merely repeating that optimization will not be meaningful progress.

### Current numerical baseline

The `analysis2` report analyzes case4 state 131, approximately

\[
c_l=1.8103192102,\qquad
a_0=\partial_y\bar\rho(0)=10.3002948918.
\]

However, `case4` may contain newer accepted checkpoints. At the beginning, discover the actual latest valid accepted state, its basis, parameters, residual objectives and saved artifacts. Distinguish it explicitly from state 131.

Do not confuse a small collocation/integrated optimization loss with a small rigorous Sobolev or Hölder residual norm.

The state-131 residual has a nonzero growing far-field sector of order approximately

\[
r^{0.1048}.
\]

Consequently, it is not in the unweighted correction space.

The earlier analysis identifies exact stationary far-field recursions and forbidden residual sectors. In particular, the existing six-branch generator architecture has a quantitative obstruction to the unweighted residual threshold over a large but finite range of radial degrees.

A seventh stationary branch eliminates one of these fixed sectors, although the first tested seven-branch reference is still far from satisfying the theorem.

Study the precise statements and their assumptions in `analysis2`; do not extrapolate them beyond their certified scope.

---

## 3. Agent architecture — two independent batches

Launch the following two groups simultaneously.

### Batch T: Theory agents

Assign at least three independent theory agents, preferably four.

**T1 — Hou literature and a posteriori architecture**

Study Thomas Y. Hou and collaborators' relevant computer-assisted and a posteriori stability proofs. Extract techniques that could genuinely improve this S1 problem.

**T2 — Weak spaces and sharp linear estimates**

Construct and analyze alternative function spaces, weighted estimates, Hölder estimates, and linear inverse mechanisms.

**T3 — Nonlinear closure and quantitative constants**

Determine which candidate estimates actually yield a complete nonlinear contraction or Newton-type a posteriori theorem, with computable constants and residual thresholds.

**T4 — Independent theoretical audit**

Check mathematical correctness, hidden derivative losses, normalization, origin and far-field behavior, and unsupported uses of existing theorems. Also investigate an independent alternative when the primary approach stalls.

### Batch N: Numerical agents

Assign at least three independent numerical agents, preferably four.

**N1 — Exact far-field asymptotics and basis constraints**

Derive and implement exact stationary far-field conditions. Identify all unacceptable residual sectors and enforce their cancellation.

**N2 — Optimization and basis development**

Continue from the best usable numerical checkpoint, improve the objective and test expanded or redesigned bases.

**N3 — Full-plane residual norm computation**

Implement and verify the residual norms requested by theory, including derivative-based and weighted norms, with independent evaluation rules and rigorous certification where feasible.

**N4 — Numerical audit and independent reproduction**

Independently recompute key coefficients, asymptotic sectors, residual values and certificates. Investigate conditioning, hidden quadrature errors, angular resolution, and optimization artifacts.

The coordinating agent must not merge these agents into one undifferentiated research task.

Each group has its own files and owns its technical decisions. Exchange results through the `shared/` directory.

If your agent framework cannot support the requested parallelism, report the limitation accurately and use the strongest available independent-worker arrangement. Do not fabricate concurrent work or independent verification.

---

# PART I — TRACK T: IMPROVE THE A POSTERIORI THEORY

## 4. Study Hou's methods carefully

Start with these references:

1. Jiajie Chen and Thomas Y. Hou, *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data I: Analysis*.

   https://arxiv.org/abs/2210.07191

2. Jiajie Chen and Thomas Y. Hou, *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data II: Rigorous Numerics*.

   https://arxiv.org/abs/2305.05660

3. Jiajie Chen and Thomas Y. Hou, *Analytic finite-rank corrections for singularly weighted estimates in a computer-assisted proof of 3D Euler singularity*.

   https://arxiv.org/abs/2607.15256

4. Thomas Y. Hou, Van Tien Nguyen and Yixuan Wang, *L²-based stability of blowup with log correction for semilinear heat equation*.

   https://arxiv.org/abs/2404.09410

Also inspect relevant previous notes and references in `analysis2` and `Holder`.

Do not spend the whole campaign writing a literature review. Read the actual mathematical proofs and identify reusable quantitative mechanisms.

Priority topics:

- weighted \(L^\infty\), weighted Hölder and mixed energy estimates;
- sharp nonlocal inequalities exploiting signed kernels and cancellations;
- separating a leading operator from troublesome finite-rank or compact corrections;
- numerical approximation of the inverse or of space-time solutions, with rigorous error control;
- analytically enforcing vanishing conditions needed by singular weights;
- sharp pointwise velocity estimates and local kernel decompositions;
- stable normalization and elimination of scaling modes;
- converting numerically computed quantities into explicit sufficient inequalities.

The S1 problem is on the whole plane and has different symmetries and far-field behavior from Hou's boundary Euler/Boussinesq problems. Every imported idea needs a new derivation appropriate to S1.

Write a short technical transfer matrix: method, exact reference, relevant lemma, S1 adaptation, required numerical inputs, plausible improvement, and unresolved obstruction.

## 5. Explore weaker spaces, not merely smaller constants

The current Sobolev approach controls more regularity than may be necessary for the nonlinear fixed point and imposes large low-order weights.

The logarithmic variant in `analysis2` already shows that simply reducing regularity without changing the residual geometry may make the threshold worse.

You must examine more substantive alternatives.

### Route T-A: Weighted \(L^\infty\) and \(C^\alpha\)

Study estimates of the type

\[
\|h\|_{X_{\rm weak}}
\le K\|Lh\|_{Y_{\rm weak}},
\]

where the norms can exploit symmetry, spatial weights, local vanishing, and the actual anisotropic structure of the background.

In particular:

- Start with \(h\), not \(h_x\).
- Preserve the signs of the nonlocal terms wherever possible.
- Do not estimate the two Riesz-transform contributions separately if this destroys a favorable cancellation.
- Determine whether the transport and the signed nonlocal operator jointly give an inverse in a substantially weaker space.
- Study center and far-field components separately where mathematically justified.
- Determine exactly how \(c[h]\) is controlled.

Use the results in `Holder` critically.

The global homogeneous \(C^\alpha\) operator constants of the individual second-order Riesz transforms become large as \(\alpha\) tends to zero. Therefore, assuming that a small \(\alpha\) makes their full operator norms small is invalid.

The goal is a sharper estimate for the **combined linearized S1 operator**, possibly in an adapted space, not simply a sharper isolated Calderón–Zygmund bound.

### Route T-B: Sharper Sobolev and weighted energy estimates

Reconsider the existing quadratic energy.

The currently large hierarchy coefficients, rough-velocity commutators and low-order weighted components may be far from optimal.

Investigate:

- optimizing the relative energy weights using a rigorous matrix positivity problem;
- preserving favorable cross terms instead of discarding them;
- using sharper weighted Riesz bounds and exact matrix inequalities;
- localizing the energy to distinguish origin, intermediate region and far field;
- making the constants spatially dependent rather than using a single global worst-case constant;
- reducing the required extra regularity while still controlling the strain and transport velocity.

The requirement is not merely a formally positive decay rate. The resulting space must admit the residual, make all nonlinear terms meaningful, and yield a complete inverse.

### Route T-C: Hou-style leading operator plus finite-rank correction

Investigate whether we can decompose

\[
L=L_{\rm good}+K
\]

such that \(L_{\rm good}\) has a sharp explicit inverse or coercivity estimate, while \(K\) is numerically certifiable as a compact/finite-rank correction.

Possible mechanisms include approximate time-dependent solutions, rigorous semigroup estimates and a computer-assisted inverse certificate.

This may be more effective than insisting that the full nonlocal contribution be absorbed by a coarse analytic inequality.

Prove any necessary complement estimates. A finite matrix singular value alone is not an inverse bound for the infinite-dimensional operator.

Investigate whether the troublesome low-order modes can be treated analytically or by finite-dimensional coordinates.

### Route T-D: A posteriori Newton or approximate-inverse estimates

The existing theorem uses a particular uniform contraction around the reference.

Explore whether a rigorous approximate inverse can give a less restrictive theorem, for example by making the actual Newton correction or preconditioned residual small even when the raw residual norm is large.

Any proposed estimate must include:

- a proved inverse or validated approximate inverse;
- the defect of that inverse;
- a rigorous nonlinear Lipschitz/remainder bound;
- the exact admissible ball;
- compatibility with the normalization and far-field correction class.

A numerical Newton step without a certified inverse is evidence, not a proof.

### Route T-E: Tail-adapted correction spaces

Determine whether explicitly including the first necessary far-field sectors as coordinates can make closure easier than forcing extremely accurate cancellation inside the finite reference.

Do not ignore the non-Fredholm obstruction already proved at the critical far-field exponent.

Any new tail-coordinate construction must specify a strictly subcritical remainder space, a well-defined normalization, the corresponding inverse, and the nonlinear mapping estimates.

Avoid re-proving the failed critical-weight framework without addressing its obstruction.

## 6. Theory outputs must be quantitative

Every serious candidate theorem must be reduced to an explicit closure inequality.

A useful schematic form is

\[
K_H\eta\le r,
\qquad
K_L C_B K_H\eta<1,
\]

together with whatever positivity and normalization conditions are required.

Here \(\eta\) is the residual in the **new forcing norm**.

For each candidate theory, report:

1. Exact domain, range and norms.
2. Whether the linear inverse is proved, conditional, or conjectural.
3. Best current inverse and nonlinear constants.
4. Maximum admissible residual, or a rigorous computable sufficient condition.
5. Required regularity and decay of the numerical residual.
6. Background inequalities requiring numerical certification.
7. Which numerical quantities should be optimized or measured next.
8. An actual comparison with the numerical team's candidate states.

A qualitative statement such as "the inverse has some finite constant" is not sufficient for closure, even if it is mathematically interesting.

If explicit constants are not yet available, isolate them in a small, concrete list of numerical verification targets.

Prioritize a genuine improvement in the allowable residual or in the norm measuring it, not an arbitrarily tiny percentage improvement to an already impractical estimate.

---

# PART II — TRACK N: IMPROVE THE REFERENCE PROFILE

## 7. Reconstruct the actual latest numerical result

Read the numerical handoff, mathematical notes, current basis, optimizer code, checkpoint history, and exact evaluation machinery in `case4`.

Reproduce the latest accepted state in a separate working copy.

Determine:

- its precise \(c_l\), center normalization and leading profile;
- current basis dimension and construction;
- exact meaning of its saved loss function;
- recent optimization history and whether it has genuinely stabilized;
- current residual behavior near the origin, intermediate region and infinity;
- available rigorous integration and differentiation methods;
- memory and CPU requirements for resumed optimization.

Recompute at least one current-state residual independently, including a denser rule than the training rule.

If the archived state differs from the theory report's state 131, record both and explain which is being used.

Do not reset the optimizer to an old state or discard newer accepted progress.

## 8. Repair the far-field asymptotics first

Write the exact stationary asymptotic recursion for the current exponent and leading angular data.

For state 131, with

\[
\gamma=\frac1{c_l},\qquad \delta=1-\gamma,
\]

the principal far-field orders follow

\[
p_n=1-n\delta.
\]

The earlier analysis found that nonstationary sectors with exponent at least \(-2\), including certain radial descendants, prevent the residual from belonging to the existing unweighted correction space.

Use the exact sector definitions in `analysis2`; do not rely on an approximate list or floating cancellation.

Construct candidates that eliminate every such sector exactly.

Compare at least:

- a constrained refit using the existing available basis;
- a suitable expanded basis with an additional stationary far-field branch;
- further branches or descendants if the residual structure justifies them;
- a separate analytic tail-coordinate or potential-level repair if it produces a substantially better certified residual.

Preserve the leading profile and scaling normalization in the primary experiment.

If changing \(c_l\) or the leading angular data is explored, handle it as a separate experimental chart and inform the theory group. Never silently treat exponent variations as belonging to the fixed-tail correction space.

**Use exact constraints or a certified null-space parameterization. Do not replace mathematically mandatory far-field cancellations by soft penalties and call the result exact.**

For each candidate, produce an exact or rigorously enclosed table of residual sectors, including their exponents, angular coefficients, and the first surviving nonzero sector.

Check that the imposed constraints are compatible with regularity at the origin.

## 9. Continue optimizing residual and adapt the basis

Once a mathematically admissible far-field parameterization is available, optimize the remaining degrees of freedom.

You are allowed to:

- continue from the current accepted numerical state;
- enlarge the basis;
- improve the basis construction or radial/angular distribution;
- use a constrained Gauss–Newton, trust-region or similar method;
- use matrix-free Jacobian products, structured elimination and iterative least-squares methods for large dimensions;
- introduce separate near-origin, intermediate-region and far-field components when justified.

Do not simply assume that more basis functions are always better.

Run controlled comparisons against the existing basis. Measure conditioning, genuine reduction on independent rules, and changes in derivative-based residual norms.

Avoid a long dense optimization that exhausts the 24-hour budget without producing a usable checkpoint. Choose feasible dimensions and exploit CPU parallelism where helpful.

The first objective is mathematical admissibility of the far-field expansion; the second is reducing the residual in a norm that the theory can actually use.

## 10. Optimize and measure rigorous closure norms

The current unweighted theory uses an energy of the schematic form

\[
E_2(F)^2
=
\|\omega D^2F\|_2^2
+
2^{14}\left[
\|\nabla F\|_2^2+
16\left(\|F\|_2^2+\frac{20}{21}\|F\|_{\dot H^{-1}}^2\right)
\right],
\]

with

\[
\omega=(1+4r^2)^{2/5}.
\]

Use the exact definitions and conventions of `analysis2` for certification.

The fractional residual norm is \(N_s(F)=E_2((1-\Delta)^{s/2}F)\).

Track the individual components rather than only their total.

Also implement the alternative weighted/Hölder/low-norm quantities communicated by Batch T.

For every candidate, distinguish explicitly between:

- a training loss;
- an independently recomputed floating-point residual;
- a rigorous lower bound;
- a rigorous upper bound;
- a complete validated norm.

No finite quadrature result is automatically a rigorous global integral.

Use exact radial integration, angular Fourier identities, interval arithmetic, exterior asymptotic bounds and independent evaluators wherever appropriate.

The existing theory report describes an exact Beta-integral method for the rational potential family. Reuse or extend it rather than beginning from an uncontrolled numerical quadrature.

Make the entire far field part of the certification, not merely a finite numerical box.

## 11. Maintain background coercivity while optimizing

A smaller residual alone is insufficient.

Every candidate should also be screened for the background inequalities required by the chosen theory.

Start with the existing matrix coercivity and derivative conditions, then include improved conditions supplied by Batch T.

Implement cheap numerical screening during optimization, followed by rigorous certification for promising candidates.

Do not silently assume that certificates valid for state 131 remain valid after adding basis functions or changing coefficients.

When a candidate violates an existing matrix condition, report whether:

- the violation is rigorously certified;
- it can be removed by optimization;
- the theory group has proved a weaker condition that would permit it.

These distinctions must feed back into the theoretical work.

---

# PART III — THE TWO-WAY INTERFACE

## 12. Required communication protocol

The two agent batches must exchange results through versioned files in `shared/`.

Batch T publishes, at each major checkpoint:

`shared/theory_requirements/theory_vNN.md`

containing:

- candidate forcing norm;
- exact residual regularity and decay requirements;
- necessary far-field cancellation conditions;
- available inverse and nonlinear constants;
- admissible residual threshold, if known;
- matrix positivity and background regularity conditions;
- numerical quantities whose reduction would most improve closure.

Batch N publishes:

`shared/numerical_results/numerics_vNN.md`

containing:

- exact source checkpoint and candidate ID;
- basis and coefficient-file path;
- normalization status;
- exact/certified far-field sector status;
- residual norms and rigorous status of each number;
- locations and scales dominating the residual;
- background coercivity margins and their rigorous status;
- next proposed numerical improvement.

Use immutable candidate IDs and hashes. A theory result must refer to an identifiable numerical state, and a numerical result must refer to an identifiable norm definition.

The coordinator maintains:

`shared/closure_matrix.md`

with one row per candidate theoretical framework and numerical state.

For each row, record:

- whether the residual belongs to the forcing space;
- whether all background hypotheses hold;
- numerical residual upper and lower bounds;
- theoretical admissible threshold;
- closure ratio or gap;
- missing proof or certification;
- whether the combination is **PROVED**, **CONDITIONAL**, **NUMERICAL ONLY**, **RULED OUT**, or **OPEN**.

Do not compare a residual measured in one norm to a threshold proved in another.

### Mandatory two-way feedback

Examples of useful feedback:

- If theory finds that an \(L^\infty\)-based norm needs far less accuracy than the old high Sobolev norm, numerics must evaluate and, if promising, optimize that new norm.
- If numerics finds that the residual is concentrated in a narrow angular/radial region, theory must investigate spatially localized constants and weights rather than retaining a global worst-case coefficient.
- If a far-field sector is expensive to eliminate numerically, theory must evaluate whether a tail-coordinate correction is admissible.
- If theory proves a better coercivity margin, numerics must use it to screen a larger feasible family.
- If numerics discovers an apparent near-kernel of the linearization, theory must investigate whether this is a genuine obstruction, a normalization mode, or a basis-conditioning artifact.

Both groups must react to the other group's concrete findings. Two independent final reports without meaningful exchange do not satisfy this task.

---

# PART IV — 24-HOUR EXECUTION PLAN

## 13. Timeline

Run for up to **24 hours of actual wall-clock research**, using the available agent framework and resources.

Do not terminate early merely because an approach fails or a conditional theorem has been obtained.

### Hours 0–2: Baseline and source audit

Theory group:

- Read the main `analysis2` results and proof dependencies.
- Study the relevant `Holder` findings.
- Identify the precise existing closure bottlenecks.
- Begin reading the most applicable Hou proofs.

Numerical group:

- Inspect the actual latest case4 checkpoint.
- Create the isolated numerical working copy.
- Reproduce the current loss and normalization.
- Determine the exact far-field defects.

Coordinator:

- Establish the shared contracts.
- Record source hashes and initial closure matrix.
- Assign agent ownership.

### Hours 2–6: First independent advances

Theory group:

- Formulate at least two genuinely different ways to improve closure.
- Begin rigorous derivations with explicit constants or certifiable constants.
- Determine the first desired residual norms.

Numerical group:

- Implement exact stationary far-field constraints.
- Produce initial repaired candidates.
- Test whether an additional stationary branch is needed.
- Begin short, controlled optimization experiments.

### Hours 6–12: First integration

Exchange candidate norms, constraints and results.

Theory group should prioritize the approach that has the best plausible closure margin, while retaining an independent alternative.

Numerical group should optimize at least one far-field-admissible reference in a theory-relevant norm.

Perform independent verification of major algebraic and numerical claims.

Checkpoint at hour 8 and hour 12.

### Hours 12–18: Strongest improvement phase

Theory group:

- Push the best estimates toward a complete theorem.
- Compute or sharply bound the relevant constants.
- Try finite-rank or numerical inverse correction if coarse energy estimates remain limiting.
- Check nonlinear closure and normalization carefully.

Numerical group:

- Continue optimization with sufficient basis complexity.
- Add targeted basis functions only when controlled experiments support the decision.
- Improve the whole-plane residual bounds.
- Certify promising far-field cancellations and basic matrix margins.

Exchange results again around hours 16–18.

### Hours 18–22: Rigorous validation and reconciliation

Choose the most promising theory–numerics combinations.

Complete as many rigorous upper bounds and mathematical proofs as possible.

Have independent agents attempt to falsify each proposed closure.

Do not spend these hours polishing a candidate that already has a rigorous obstruction larger than its allowed threshold.

### Hours 22–24: Final consolidation

Freeze best validated candidates.

Write the final reports and a concrete continuation plan.

Include resumable numerical checkpoints, independent verification scripts and an exact list of unresolved inequalities.

Do not claim closure if even one condition remains unverified.

---

## 14. Resource and reproducibility requirements

Use available CPU cores efficiently, but prevent the two batches from oversubscribing memory and making each other's computations unreliable.

Inspect actual hardware and running workloads before launching expensive jobs. Do not assume access to GPUs or a cluster.

For large numerical bases, prefer structured or matrix-free methods over unnecessary dense factorizations.

All significant computations must be reproducible from files in `combined1`.

Every rigorous numerical claim must include its data source, algorithm, precision, error bound and reproduction command. Use independent arithmetic paths for critical results where feasible.

Keep frequent checkpoints so the best result is not lost if a process fails.

Do not let long numerical computations block theory agents from continuing their independent work.

---

## 15. Final deliverables

Create the following files in `combined1/reports/`:

**`THEORY_FINAL.md`**

Include the strongest new estimates, complete hypotheses, numerical constants where available, comparison with `analysis2`, precise Hou-derived ideas, failed approaches and counterexamples, and a clear closure theorem or conditional theorem.

**`NUMERICS_FINAL.md`**

Include the best accepted candidate, exact basis and parameters, far-field cancellation certificates, residual norms, independent checks, background margins, optimization history and reproducible restart instructions.

**`JOINT_CLOSURE_FINAL.md`**

This is the primary deliverable.

Begin with a direct answer to the following questions:

1. What is the strongest a posteriori estimate now proved?
2. How much weaker is its function space, or how much larger is its allowed residual, compared with `analysis2`?
3. What is the best numerical reference now available?
4. Does its residual satisfy the regularity and far-field requirements?
5. What is its residual norm in the proposed theory space?
6. Does the nonlinear fixed point close? If not, which precise inequality fails first?
7. What is the smallest remaining obstacle that would actually make closure possible?
8. Should the next campaign prioritize further numerical refinement, a new norm, or a sharper inverse certificate—and on what quantitative evidence?

Include a comparison table of all serious theory–numerics pairs and their gaps.

**`NEXT_24H_PLAN.md`**

Provide a prioritized plan for another campaign, but distinguish indispensable steps from speculative ideas.

**`REPRODUCE.md`**

Give exact commands, inputs and expected checks for reproducing the numerical results and theoretical certificates.

Also retain all intermediate mathematical notes, code and immutable checkpoints.

---

## 16. Standards and prohibitions

These conditions are mandatory:

- Do not modify the source directories `case4`, `analysis2` or `Holder`.
- Do not substitute finite-box or quadrature smallness for a whole-plane rigorous norm.
- Do not confuse a numerical optimization objective with the norm required by a theorem.
- Do not discard far-field sectors without an exact cancellation argument.
- Do not infer infinite-dimensional invertibility from a finite-section singular value.
- Do not assume a global \(C^\alpha\) bound follows from the frozen operator's bound.
- Do not ignore the local/contact term in \(c[h]\).
- Do not fix a scaling mode by a condition that is not continuous in the selected space.
- Do not ignore derivative loss in \(U[h]\cdot\nabla h\).
- Do not regard the existing threshold \(6.36\times10^{-7}\) as the best attainable threshold.
- Do not repeatedly optimize the existing energy weights if doing so produces only negligible improvements.
- Do not claim that a candidate is impossible outside the exact assumptions of a proved obstruction.
- Do not label numerical observations as rigorous theorems.
- Do not stop research merely after demonstrating a conditional existence theorem.
- Do not invent independent audits or claim that artifacts have been verified if only a summary was examined.

A failed direction should produce a precise mathematical reason for failure, after which the responsible agent should move to another promising direction.

## 17. Success criteria

**Full success:** One explicit reference profile satisfies every rigorously verified hypothesis of a complete a posteriori existence theorem, including normalization, far-field conditions, residual smallness and nonlinear contraction.

**Major partial success:** Either a substantially stronger theoretical theorem with a realistic, numerically checkable residual threshold, or a far-field-correct numerical candidate whose rigorous residual is dramatically smaller in an applicable space, preferably both.

**Useful partial success:** The two tracks identify a substantially smaller quantitative gap than before, with a clear, reproducible route to closing the remaining inequality.

A purely qualitative theorem, an unverified tiny loss, or a large collection of unrelated experiments is not sufficient.

**Start both batches of agents immediately. Keep them working and communicating for the 24-hour research window, within the actual execution capabilities of the environment. Prioritize rigorous mathematical progress and quantitative closure over the volume of generated notes.**