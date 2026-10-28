# 48-Hour Follow-Up Campaign: Joint Optimization of c_l and omega at Angular Degree 6

## 0. Mission and working directory

Continue the existing numerical investigation of rotating backward self-similar solutions of the three-dimensional incompressible Euler equations.

**Working directory: `Changhe/Euler/approach3`**

This is a follow-up to the completed 96-hour rotating Euler investigation. Inspect the existing code, numerical results, checkpoints, documentation, and previous campaign report before modifying anything.

The previous campaign explored many fixed parameter values but devoted insufficient computational resources to optimizing the scaling exponent `c_l` and rotation parameter `omega` simultaneously.

The primary objective of this follow-up is to correct that deficiency.

**Hard requirements:**

1. Restrict the entire 48-hour scientific campaign to **main angular degree L = 6**.
2. Keep the existing toroidal-poloidal representation, spherical-harmonic basis, radial Chebyshev basis, and existing far-field correction channels unchanged.
3. Treat `c_l` and `omega` as genuine optimization variables alongside all spectral coefficients.
4. Use the available, authorized A100 GPUs efficiently through parallel independent optimization experiments.
5. Investigate several distinct initializations and parameter regions rather than concentrating exclusively near a previously chosen pair.
6. Establish whether the Degree 6 optimizer approaches genuine stationarity before attributing residual stagnation to insufficient basis resolution.
7. Independently verify the most promising results.
8. **Do not launch Degree 8 or higher main-degree optimization during this campaign.**

The authorized duration is 48 hours of actual wall-clock time, starting from a recorded campaign timestamp.

This is an execution task, not merely a request for an implementation plan.

Create a new dedicated experiment directory under `approach3`, for example:

`degree6_free_parameters_48h/`

Preserve previous checkpoints, source code snapshots, and validation data. Never overwrite the frozen results of the previous campaign.

Reuse existing code wherever reliable. Avoid unnecessary rewrites or duplication of large datasets.

If code changes are necessary, keep them identifiable, versioned, and reversible.

All reports and documentation should be written in English.

---

## 1. Mathematical problem

We seek smooth, nonzero, genuinely non-axisymmetric, decaying profiles satisfying

\[
R_u=(1-c_l)U+W\cdot\nabla U+\omega JU+\nabla P=0,
\]

where

\[
W=(c_lI-\omega J)y+U,
\qquad
Jy=(-y_2,y_1,0),
\]

together with

\[
\nabla\cdot U=0,
\qquad
-\Delta P=\operatorname{tr}((DU)^2).
\]

The pressure is the decaying full-space Newton pressure. Do not introduce an artificial finite-radius pressure boundary condition or an independent harmonic pressure correction.

The primary parameter range is

\[
\boxed{\frac25<c_l<\frac12,\qquad \omega>0.}
\]

Negative omega is equivalent to positive omega by reflection, as established in the previous campaign.

Both parameters are unknowns.

The optimization variables must be

\[
\boxed{
X=(a_1,\ldots,a_N,c_l,\omega),
}
\]

where the coefficients include all active toroidal, poloidal, and far-correction basis coefficients.

The original fixed-parameter runs are initial guesses, not predictions of the correct parameter values.

Do not favor `c_l = 0.45`, `omega = 1`, or any other pair unless the freely optimized equations provide evidence for it.

Do not minimize `c_l` as an independent objective. The aim is to solve the Euler profile equation, not to drive the exponent artificially toward the lower boundary.

---

## 2. Freeze the Degree 6 representation

Use the existing representation

\[
U=\nabla\times(Ty)+\nabla\times\nabla\times(Sy).
\]

Preserve the existing:

- Real spherical-harmonic and regular solid-harmonic construction.
- Main angular cutoff `L = 6`.
- Radial Chebyshev basis, mappings, and radial coefficient counts of each restarted state.
- Toroidal and poloidal envelopes.
- Smooth angular twist.
- Far-field correction channels.
- Full-space pressure construction.
- Dilation and azimuthal phase gauges.
- Existing symmetry classes and their corresponding basis definitions.

The leading far-field behavior is controlled by

\[
\alpha=\frac{1-c_l}{c_l},
\]

and the twisted azimuthal coordinate

\[
\chi=\varphi+\frac{\omega}{c_l}\log r.
\]

The smooth core twist used in the existing representation is

\[
\psi(r)=\frac{\omega}{2c_l}
\log\left(1+\frac{r^2}{R_0^2}\right).
\]

The basis depends on both free parameters.

**Do not mistakenly keep the basis fixed while only changing the explicit coefficients in the Euler equation.**

The angular degrees already used by the existing nonlinear far-field correction channels may exceed six. Preserve those channels as before; the restriction `L = 6` refers to the main angular expansion.

Do not add new angular harmonics, radial basis functions, or correction-channel functions in the main campaign.

You may increase quadrature accuracy, verification resolution, and solver precision when necessary. These are numerical validation changes, not changes in the mathematical basis.

Keep both the original even-azimuthal-mode class and any already implemented unrestricted-mode Degree 6 class available. Do not silently enlarge the basis associated with an existing checkpoint.

---

## 3. Implement mathematically correct free-parameter derivatives

This is the most important implementation requirement.

The optimizer must differentiate the entire residual and the implemented loss with respect to both `c_l` and `omega`.

In particular,

\[
\frac{\partial\alpha}{\partial c_l}
=-\frac1{c_l^2},
\]

\[
\frac{\partial\psi}{\partial c_l}
=-\frac{\omega}{2c_l^2}
\log\left(1+\frac{r^2}{R_0^2}\right),
\]

\[
\frac{\partial\psi}{\partial\omega}
=\frac1{2c_l}
\log\left(1+\frac{r^2}{R_0^2}\right).
\]

These derivatives propagate into the toroidal and poloidal potentials, velocity, velocity gradient, vorticity, nonlinear terms, far-field corrections, and pressure.

At fixed coefficient coordinates, let `U_p` denote the derivative of the represented velocity with respect to a parameter `p`.

The pressure derivatives must satisfy

\[
-\Delta P_p
=2\operatorname{tr}(DU\,DU_p),
\]

with the full-space decaying pressure convention.

For an independent analytic check, the parameter derivatives of the momentum residual are

\[
\begin{aligned}
\partial_{c_l}R_u={}&-U+(1-c_l)U_{c_l}
+(y+U_{c_l})\cdot\nabla U\\
&+W\cdot\nabla U_{c_l}
+\omega JU_{c_l}+\nabla P_{c_l},
\end{aligned}
\]

and

\[
\begin{aligned}
\partial_{\omega}R_u={}&
(1-c_l)U_\omega
+(-Jy+U_\omega)\cdot\nabla U\\
&+W\cdot\nabla U_\omega
+JU+\omega JU_\omega+\nabla P_\omega.
\end{aligned}
\]

Validate these identities independently of the production automatic-differentiation implementation.

### Derivative verification

Before launching the large campaign:

1. Test the `c_l` and `omega` Jacobian columns against centered finite differences with multiple step sizes.
2. Test the complete implemented loss gradient, including normalization and parameter-dependent weights, not only the raw PDE residual.
3. Include representative non-axisymmetric fields, existing checkpoints, and manufactured smooth fields.
4. Test several parameter pairs, not merely `(0.45, 1)`.
5. Test near-origin, intermediate-radius, and far-field points.
6. Cross-check selected cases using extended precision.
7. Verify that the pressure derivatives include the dependence of the source and exterior integrals on both parameters.

For instance, compare analytic or automatic derivatives against steps near `1e-3`, `1e-4`, `1e-5`, and smaller when numerical conditioning permits.

Require a clear convergence or roundoff plateau consistent with the expected finite-difference order.

Choose quantitative tolerances from measured precision and conditioning; document them before examining final results.

If the free-parameter derivatives fail validation, correct them before conducting large-scale optimization. Do not silently substitute frozen-parameter Jacobians.

### Parameter constraints

Use a smooth or reliably bound-constrained formulation that preserves

`0.4 < c_l < 0.5` and `omega > 0`.

One possible implementation is

`c_l = 0.4 + 0.1 * sigmoid(z_c)`

`omega = exp(z_omega)`.

This is illustrative, not mandatory.

Inspect conditioning near the parameter boundaries. A transformed parameter gradient may become small merely because the transformation saturates.

Always report derivatives and convergence diagnostics in physical `c_l, omega` coordinates as well as optimizer coordinates.

Do not interpret parameterization saturation as mathematical convergence.

The optimization must be capable of moving omega substantially away from its initial value, including below `0.1` or above `10` when the numerical evidence warrants it.

Any numerical trust region on parameter steps is for stability, not an assumption about the location of the solution.

---

## 4. GPU utilization and computational profiling

The previous campaign used an A100 server but did not provide sufficient per-iteration profiling to identify the main performance bottleneck.

Start by inspecting the actual resources:

- Number and identity of available GPUs.
- GPU memory capacity and current free memory.
- Which GPUs are authorized for this project.
- CPU core allocation and affinity restrictions.
- System RAM and available disk space.
- Existing processes and other users' workloads.
- CUDA and numerical software environment.

The previous machine reportedly had eight A100-SXM4-80GB GPUs, but not all eight were dedicated to this project.

A late-stage CPU allocation restriction was also recorded in the previous campaign. Determine whether any such restriction remains active.

Do not assume all GPUs or CPU cores are available.

### Profile representative Degree 6 iterations

Benchmark an existing Degree 6 state on one GPU before expanding the workload.

Measure:

1. Velocity and derivative assembly time.
2. Full-space pressure source and pressure reconstruction time.
3. Residual and objective evaluation time.
4. Jacobian construction time.
5. Linear-system solve time.
6. Trial-step evaluation and line-search or trust-region overhead.
7. CPU-to-GPU data transfer and synchronization time.
8. Peak GPU memory, peak system RAM, and GPU utilization.
9. Accepted optimization steps per wall-clock hour.

Use synchronized device timings where asynchronous GPU execution would otherwise make the results misleading.

Compare fixed-parameter and free-parameter evaluation costs.

In particular, determine how much additional time the two parameter derivatives require.

### Parallelization strategy

**Use data parallelism across independent optimization starts as the default.**

A typical Degree 6 experiment should occupy one GPU, unless benchmarks demonstrate that a different allocation is materially faster.

When enough GPUs are authorized and CPU resources allow, launch multiple independent free-parameter experiments simultaneously.

For example:

- With eight authorized GPUs, use approximately six for parallel optimization and up to two for validation, profiling, or independent checks.
- With six authorized GPUs, use approximately four or five for optimization and the remainder for validation or overflow.
- With fewer resources, adapt the queue accordingly.

These are examples, not fixed allocations.

The actual worker count must respect GPU memory, CPU capacity, pressure-computation throughput, RAM, and other projects.

Do not run many workers on a single GPU if this lowers total throughput.

Do not split one small Degree 6 linear solve across multiple GPUs unless profiling demonstrates an advantage.

Use concurrent independent starts, batched basis evaluations where appropriate, and optimized linear algebra to keep authorized GPUs productive.

Avoid CPU oversubscription from nested BLAS, OpenMP, and worker threads.

If GPU utilization remains low, identify whether the bottleneck is CPU pressure computation, data transfers, GPU kernels, Jacobian formation, synchronization, or the linear solver.

Improve the bottleneck when feasible rather than simply launching more identical workers.

Record per-GPU utilization and GPU-hours used by the project, distinguishing allocations from measured utilization and consumed work.

Do not modify system-wide installations, interfere with other projects, or exceed authorized resource quotas.

---

## 5. Numerical solver and conditioning

Retain the existing Degree 6 solver as a reproducible baseline.

The previous campaign observed severe Jacobian conditioning in some Degree 6 states and frequent iteration-limit or time-limit stops.

Therefore, optimizer convergence is a central research question.

Initially use the existing Levenberg–Marquardt implementation with correct free-parameter derivatives.

Then investigate improvements that preserve the same mathematical objective:

- Column scaling.
- Gauge-null-direction elimination.
- Trust-region globalization.
- Properly safeguarded damping.
- QR, SVD, or matrix-free least-squares alternatives where normal equations become unreliable.
- Block preconditioning that treats the two parameter directions separately.
- Gauss–Newton or Newton-Krylov comparisons when justified by benchmarks.

The basis is fixed, but solver improvements are allowed.

### Important safeguard

The previous campaign observed large objective excursions in some unsafeguarded lagged iterations.

For this follow-up, every accepted step must be evaluated against the actual updated nonlinear objective, including the updated basis and pressure.

Do not accept an apparent improvement based solely on stale parameter-dependent data, lagged weights, or an approximate model.

If a trial step is rejected, record why.

### Reduced parameter sensitivity

For promising states, analyze the Jacobian in blocks:

\[
J=[J_a\ \ J_p],
\]

where `J_a` contains coefficient directions and `J_p` contains the two parameter directions.

Investigate how much of each parameter direction can be absorbed by changes in the spectral coefficients.

Where practical, compute the small reduced parameter system obtained by eliminating or projecting out the coefficient directions.

Use an appropriate scaled norm and remove gauge null directions.

This analysis should help distinguish:

- Genuine sensitivity to `c_l` or `omega`.
- Nearly flat parameter directions.
- Correlated parameter directions.
- Ill-conditioning of the spectral coefficients.
- An actual stationary point of the joint problem.

Do not conclude that a parameter is determined simply because it changes little during an unsuccessful optimization.

---

## 6. Initial states and parameter exploration

Reuse several structurally distinct Degree 6 checkpoints from the previous campaign.

Priority initializations include states near:

- `(c_l, omega) = (0.45, 1)`, including the balanced-core Degree 6 branch.
- `(0.45, 0.3)`, including balanced-core and independent-route lineages.
- `(0.42, 0.3)`, using its saved Degree 6 branch.
- Other useful Degree 6 checkpoints with different non-axisymmetric content, core structures, and far-field coefficients.

Locate the actual saved files and verify them before use. Do not invent checkpoint paths or silently replace missing files with unrelated states.

Preserve their original coefficients and parameters as immutable starting records.

### Main rule

**Every primary discovery run must optimize both `c_l` and `omega` throughout its optimization.**

Fixed-parameter runs are allowed only as diagnostic controls, software regression tests, or matched baselines.

Do not spend most of the campaign repeatedly refining fixed `(c_l, omega)` pairs.

### Explore more than one basin

Use several initialization families:

1. Existing Degree 6 checkpoints with their original parameters.
2. Existing Degree 6 fields with moderately perturbed parameters and correctly re-evaluated basis representations.
3. Small and moderate non-axisymmetric coefficient perturbations of saved states.
4. Independent random poloidal/toroidal initializations.
5. Diverse core and tail structures already representable by the existing Degree 6 basis.
6. Initial parameter samples spread across the target interval and a broad range of positive omega.

For fresh parameter starts, consider a reproducible space-filling design in `c_l` and `log(omega)` rather than selecting a few arbitrary pairs.

Any sampled parameter value is an initial condition, not a fixed constraint.

Parameter perturbations of a saved field should be accompanied by an honest field comparison and, where useful, a refit into the parameter-dependent basis.

Do not assume that preserving coefficients while changing the parameter preserves the physical velocity field.

### Paired optimization experiments

For a selected subset of initial states, compare:

- Fixed-parameter optimization.
- Fully free-parameter optimization.

Use the same initial state, identical basis, comparable computational budgets, and identical independent validation rules.

This comparison should reveal whether freeing the parameters gives an actual advantage.

Allocate only a small minority of computational resources to fixed-parameter controls.

---

## 7. Optimization objective and validation metrics

Initially retain the previous production objective so that comparisons with the 96-hour campaign are meaningful.

Do not silently alter the loss while attributing improvements to free parameters.

You may run separately labeled diagnostic variants with different optimizer scaling or residual weighting if the original objective reveals a concrete conditioning problem.

Always evaluate every promising result using the same physical Euler residual and the previously registered independent diagnostics.

In particular, report:

- `rho_u^max` on both standard and half-offset dyadic shell families.
- The single-term momentum residual ratio `sigma_u^max`.
- The nonlinear and separated-group residual ratios.
- Weighted absolute residual `a_max`.
- Core-ball residuals centered at the vorticity maximum.
- Vorticity residual `R_Omega`.
- Origin Taylor and vorticity residuals.
- Divergence and pressure-Poisson defects.
- Far-field leading and first nonlinear coefficient matching.
- Renormalized energy `E_ren`.
- Total helicity `H_tot`.
- Non-axisymmetry and nontriviality guards.
- Core resolution, spectral decay, and tail-onset diagnostics.

Maintain the registered gauge

\[
\int_{S^2}|F|^2\,dS=1
\]

and the azimuthal phase gauge.

Do not add an independent core-scale or vorticity-amplitude normalization that removes a physical degree of freedom.

Recompute holdout diagnostics for the actual optimized parameter values.

When comparing states at different `c_l`, account explicitly for the changed far-field exponent and parameter-dependent weights. Report physical, fixed-gauge quantities on common evaluation domains alongside the registered weighted diagnostics.

### Avoid false improvements

Reject apparent progress caused by:

- Collapse toward zero velocity.
- Collapse toward axisymmetry.
- Drift toward `omega = 0`.
- Artificial approach to the parameter boundaries.
- Increasingly unresolved core concentration.
- Large high-frequency coefficients.
- Moving the core outside the sampled region.
- Pushing the nonzero tail onset to unbounded radius.
- Cancellation from inaccurate pressure or angular derivative tables.
- A decreasing relative residual accompanied by a large increase in absolute core residual.

Such states remain useful diagnostic results but are not profile candidates.

Retain the previously registered Tier S, Tier R, and Tier A requirements. In particular, the shell threshold `rho_u^max <= 1e-2` alone does not establish a candidate.

Do not relax the acceptance conditions to declare success.

### Pressure and field consistency

The previous campaign also identified potential inconsistencies caused by separately rounded angular polynomial and derivative tables.

Check that the evaluated velocity, its supplied Jacobian, the divergence, and the source used in the pressure computation correspond to the same differentiable field.

Use targeted tests to determine whether such defects materially affect Degree 6 calculations.

Do not mistake agreement among several evaluations of the same inconsistent source for independent pressure accuracy.

---

## 8. Forty-eight-hour execution plan

Start the campaign clock only after recording the current timestamp, resource allocations, software versions, and working state.

The following is the preferred schedule. Adjust within the overall budget when essential correctness problems require additional time.

### Phase I — Hours 0–4: Free-parameter implementation and profiling

Objectives:

- Locate and validate existing Degree 6 checkpoints.
- Implement or repair the complete parameter-dependent Jacobian.
- Validate the `c_l` and `omega` derivatives.
- Benchmark one GPU.
- Determine the optimal concurrent worker count.
- Test checkpoint/resume.
- Start the multi-GPU job queue.

If derivative validation or pressure correctness is not achieved within four hours, prioritize correctness and extend this phase as necessary.

Do not use an unvalidated solver for a large production run merely to satisfy the schedule.

### Phase II — Hours 4–36: Broad parallel joint optimization

This is the main discovery phase.

Run many independent Degree 6 free-parameter optimizations concurrently on authorized GPUs.

Use diverse parameter starts, basis coefficient perturbations, and field structures.

Maintain several promising branches instead of spending all resources on the single state with the lowest current loss.

After an initial screening, allocate longer runs to promising states.

Use adaptive job budgets:

- Short pilots to detect immediate failure or collapse.
- Medium-length runs for promising free-parameter trajectories.
- Longer continuations when the residual continues to decrease.
- Termination or restart when progress stalls and the diagnostic evidence is sufficient.

Use measured throughput, not an arbitrary fixed number of iterations, to distribute computational resources.

For planning purposes, aim for approximately 20–50 substantive optimization experiments if measured throughput and available hardware support that range.

This is a planning target, not a guaranteed count or a reason to run superficial experiments.

Each experiment must have a documented independent initialization or a meaningful, labeled continuation objective.

Keep the number of starts secondary to convergence quality.

### Phase III — Hours 36–44: Deep investigation of the best Degree 6 branches

Select approximately three to five promising, structurally distinct branches.

For each branch:

- Continue free-parameter optimization with a longer budget.
- Test the parameter-gradient and projected-gradient convergence.
- Investigate the smallest relevant Jacobian singular values.
- Compare at least two appropriate optimization strategies if conditioning remains poor.
- Check whether parameter values stabilize under continued optimization.
- Check whether the optimized field remains nontrivial and non-axisymmetric.
- Repeat from modest perturbations to test reproducibility.
- Determine whether residual reduction is slowing because of optimizer stagnation, numerical inaccuracies, or an apparent representation limit.

If a coherent family of nearly stationary solutions appears, investigate continuation in `c_l` and `omega`.

Pseudo-arclength continuation is allowed if ordinary parameter continuation becomes singular or encounters a fold.

Do not spend this phase re-running many indistinguishable fixed-parameter experiments.

### Phase IV — Hours 44–48: Independent validation and report

Freeze the best saved states for validation.

Use fresh holdout points and increased quadrature resolution.

Independently recompute the pressure and momentum residual for the strongest states when the available second implementation permits.

Verify core and far-field diagnostics separately.

Complete a comparison of free-parameter and fixed-parameter results.

Produce a concise scientific report, machine-readable tables, and all restart instructions.

Checkpoint and stop campaign jobs at the 48-hour budget boundary.

**Do not automatically proceed to Degree 8.**

---

## 9. GPU campaign supervisor and checkpoint policy

Use a persistent, restartable supervisor or the available scheduler.

The campaign should not depend on the interactive agent session staying connected.

Maintain:

- An atomic job queue.
- One unique experiment identifier per start.
- GPU affinity and resource limits.
- Random seeds and initial parameter values.
- Optimizer state and damping history.
- Full coefficient and parameter checkpoints.
- Code version and configuration hashes.
- Periodic heartbeats.
- Failure reasons and retry limits.
- An immutable record of every accepted improvement.

Checkpoint at least every 15 minutes and at meaningful accepted improvements.

Test forced interruption and restart on a disposable run before relying on the supervisor.

If a worker fails, preserve its last valid checkpoint and diagnose the failure before retrying.

Never silently reset a long optimization.

Every job must record:

- Initial and final `c_l`, `omega`.
- Initial and final residual diagnostics.
- Objective history and parameter trajectory.
- Full and projected gradient metrics.
- Accepted and rejected steps.
- Stop reason.
- Elapsed wall time.
- GPU and CPU resources.
- Peak GPU and system memory.
- Validation status.

Track which GPUs were actually occupied by productive work.

If authorized GPUs remain idle while valid pending tasks exist, identify and address the scheduler or computational bottleneck.

Avoid wasteful repetition merely to keep a GPU busy.

---

## 10. Criteria for interpreting the result

At the end of 48 hours, distinguish at least the following possibilities.

### Outcome A: Clear improvement from free parameters

Freely optimized `c_l` and `omega` produce a substantial, independently reproducible reduction in the physical Euler residual, while core and far-field diagnostics remain controlled.

Report the optimized parameters, parameter uncertainty, numerical conditioning, and improvements relative to matched fixed-parameter controls.

A small residual is not proof of existence.

### Outcome B: Parameter optimization converges but the residual remains nonzero

The full joint problem reaches credible numerical stationarity, yet the residual remains materially above the discovery threshold.

Investigate the residual structure and whether multiple initializations approach the same stationary state.

This may suggest a finite-basis limitation, but it does not prove one without further evidence.

### Outcome C: Optimization remains incomplete

The residual continues to decline, or optimizer conditioning prevents reliable stationarity.

In this case, do not call the observed residual a basis-resolution floor.

Preserve the best states and quantify the remaining solver problem.

### Outcome D: Parameters are poorly identifiable or run to degenerate limits

The apparent optimum has flat parameter directions, strong coefficient–parameter correlations, boundary saturation, or loss of nontriviality.

Report the measured reduced parameter sensitivity and why a reliable parameter value cannot be inferred.

### Outcome E: Implementation or numerical accuracy prevents a meaningful search

If pressure, derivative, or field-consistency failures cannot be repaired within the campaign, document them explicitly and retain the last valid results.

Never claim that an unsuccessful numerical search establishes nonexistence of rotating Euler profiles.

---

## 11. Required deliverables

Produce a final report in the new Degree 6 campaign directory with:

### A. Main numerical summary

A table containing, for each important branch:

| Run | Initial c_l | Initial omega | Final c_l | Final omega | Initial residual | Final holdout residual | Core residual | Stationarity | GPU-hours |
|---|---|---|---|---|---|---|---|---|---|

Include the standard and half-offset shell results separately.

Distinguish independently checked values from values obtained only by the optimizer.

### B. Parameter evolution

For the best branches, provide plots or numerical tables of:

- `c_l` versus accepted iterations.
- `omega` versus accepted iterations.
- `omega/c_l` versus accepted iterations.
- Momentum residual and objective versus iterations.
- Parameter-gradient norms.
- Core and far-field residual evolution.

Compare several initializations and identify any apparent convergence toward common parameter values.

### C. Performance report

Document:

- Available and authorized GPU resources.
- Number of concurrently active workers.
- Measured throughput in optimization steps per hour.
- Time spent on Jacobian, pressure, residual evaluation, and linear solves.
- GPU utilization and peak memory.
- Total project GPU-hours.
- CPU bottlenecks and any resource restrictions.
- Optimization experiments completed versus attempted.

### D. Mathematical and numerical conclusions

Explain:

1. Whether freeing `c_l` and `omega` materially improved the optimization.
2. Whether the improved parameter values are reproducible across different starts.
3. Whether the joint optimizer reached credible stationarity.
4. Which terms or spatial regions dominate the remaining PDE residual.
5. Whether the current evidence points toward solver limitations, conditioning problems, pressure inaccuracies, or possible Degree 6 representation limitations.
6. What concrete evidence would justify moving to Degree 8.

### E. Reproducibility

Provide:

- Saved coefficients and parameter values.
- All relevant configurations.
- Exact checkpoint paths.
- Code version or hashes.
- Independent validation scripts.
- A one-command resume procedure.
- A frozen final status and resource ledger.

If the full 48-hour campaign cannot actually remain active, state the true completed work, current process state, and exact recovery commands. Never fabricate runs or elapsed time.

---

## 12. Final priority rules

The following priorities override optional experiments:

**Priority 1:** Correct and independently validated joint derivatives with respect to `c_l` and `omega`.

**Priority 2:** High-throughput parallel Degree 6 optimization using available, authorized GPUs.

**Priority 3:** Broad parameter and initialization exploration, without freezing either parameter in production searches.

**Priority 4:** Genuine optimizer convergence, including parameter-direction diagnostics and appropriate conditioning improvements.

**Priority 5:** Independent core, far-field, pressure, and vorticity validation.

**Priority 6:** Clear evidence-based recommendations for any future Degree 8 campaign.

Do not replace the existing basis simply because an optimizer stalls.

Do not spend the 48 hours conducting more fixed-parameter searches as the primary activity.

Do not mistake a small relative residual for an approximate Euler solution if the absolute core residual or global compatibility conditions remain badly violated.

Do not automatically expand to Degree 8 at any time.

**The central question is: With the existing Degree 6 representation, how far can the Euler residual be reduced when c_l, omega, and all spectral coefficients are optimized together, using an efficient and genuinely converged numerical method?**

Execute the campaign, preserve reproducible results, and stop at the 48-hour boundary for scientific review before any increase in angular degree.