# Research task I — Full-plane IPM self-similar profiles with even-x / odd-y symmetry

You are conducting an independent, serious mathematical and computational investigation. This prompt is **self-contained**: do not assume access to a paper, previous conversation, code, or previous results. Your job is to reach **one of two substantial outcomes**:

- **NO (theorem):** Prove rigorously that no nonzero, admissible classical profile exists for the problem below, in a clearly specified and genuinely relevant function class. All assumptions and the scope of the theorem must be explicit.
- **YES (compelling numerical evidence, not a theorem):** Produce an explicit, reproducible nontrivial candidate and strong, independently checked numerical evidence that an admissible full-plane profile exists. Numerical evidence must not be described as a proof of existence.

A merely formal identity, a perturbative calculation, a theorem covering only an artificially narrow class, a single low-resolution computation, or an unverified residual is **not** a successful outcome. Continue substantive analytic and computational exploration rather than stopping at a partial observation. Never fabricate a conclusion if the requisite proof or evidence is lacking.

## MANDATORY EXECUTION CONTRACT — AT LEAST 24 HOURS OF REAL RESEARCH TIME

**This is a hard execution requirement, not a suggestion or an estimated difficulty. Devote a minimum of 24 hours of actual elapsed wall-clock time to the even-x / odd-y investigation before submitting any terminal research result.** The 24 hours begin when you actually start the work, not when the prompt was written or received. Twenty-four model-thinking iterations, 24 CPU-hours accrued in parallel, or 24 hours of mere queued/idle/sleeping time do **not** satisfy this rule. Do not declare success, failure, or completion at hour 2, hour 10, or hour 23 just because you have a promising theorem or a small residual. Twenty-four hours is a **minimum**, not a deadline or permission to stop when the evidence remains weak.

**Start and audit trail.** At the beginning, record the actual local or UTC start time `T0` as an ISO 8601 timestamp with timezone, the computational environment, and the precise problem definition. Maintain a durable chronological log with timestamps recording mathematical results, attempted counterexamples, executed code and commands, solver configurations, numerical outputs, failed attempts, checkpoints, and independent verifier activity. Record `T_end` and the actual elapsed time `T_end-T0` in the final report. Include enough supporting evidence (job timestamps, scripts, output files, or logs) for an independent reader to assess whether the requirement was met. Never invent timestamps, logs, calculations, code execution, or verification.

**Minimum 24-hour research protocol (wall-clock schedule, adaptable across parallel workstreams):**

- **Hours 0–6:** Independently derive the governing identities; audit the correct full-plane inverse, origin normalization, admissibility, and far-field/gauge issues. Pursue nonexistence mechanisms and construct analytic test examples. Begin implementation and regression tests when warranted.
- **Hours 6–14:** Actively pursue either a rigorous NO proof or candidate construction; test competing approaches rather than repeating a stalled argument. Execute and inspect real computations where appropriate. Preserve intermediate data and write down all mathematical gaps.
- **Hours 14–20:** Deepen the most promising line while launching an independent adversarial audit. For a candidate, perform resolution/domain refinements, independent Poisson and transport residual checks, and artifact tests. For a prospective proof, check every assumption, endpoint, integration by parts, and counterexample.
- **Hours 20–24 (and longer if necessary):** Carry out a focused, adversarial verification phase. Attempt to falsify the tentative conclusion, independently reproduce decisive numerical results or rederive the key proof, resolve discrepancies, and prepare reproducibility materials.

**Early discovery is not an early-exit exception.** If an apparently complete NO theorem or convincing YES candidate emerges before the 24-hour minimum, spend the remaining time checking, attempting to break, generalizing where justified, and independently reproducing the result. Do not use passive waiting or `sleep` as a substitute for research. If the environment terminates or imposes a shorter execution limit, preserve checkpoints and use supported continuation facilities; if you cannot genuinely continue for 24 elapsed hours, explicitly disclose that the 24-hour requirement was **not met**. Do not falsely assert compliance or force a YES/NO conclusion unsupported by the evidence.

**Terminal output gate.** A successful terminal report may be issued **only after at least 24 hours** and only when the specified evidentiary standards below have actually been met: `NO` requires a complete rigorous theorem in the claimed class; `YES — numerical evidence` requires concrete reproducible numerical evidence, not a formal identity or isolated small residual. If neither endpoint has been established after 24 hours, keep investigating if resources permit. If further execution is genuinely impossible, report the exact limitation and outstanding gap rather than fabricating either outcome. Include the research/verification timeline in any final report.

## 1. Exact mathematical problem

Let `X=(x,y)` range over the **entire** `R^2`. Consider the two-dimensional incompressible porous-media (IPM) transport law

\[
\partial_t\varrho+u_{\mathrm{phys}}\cdot\nabla\varrho=0,\qquad
u_{\mathrm{phys}}=\nabla^\perp\Psi=(-\Psi_y,\Psi_x),\qquad
-\Delta\Psi=\partial_x\varrho.
\]

(The symbol `u_phys` denotes velocity; there is no extra viscosity or auxiliary evolution equation.) We seek a stationary rescaled profile satisfying

\[
\boxed{(c_l X+U)\cdot\nabla\rho=\rho,\qquad
U=(-\psi_y,\psi_x),\qquad
-\Delta\psi=\partial_x\rho\quad\text{on }\mathbb R^2.}
\]

This fixes the density-scaling coefficient to `c_rho=1`; the scalar `c_l` is unknown. There is **no physical boundary** at `y=0` and no wall/Dirichlet Green function. The origin is the fixed self-similar center in this setting.

Impose the following **global parity conditions**:

\[
\boxed{\rho(-x,y)=\rho(x,y),\qquad \rho(x,-y)=-\rho(x,y).}
\]

Choose the full-plane elliptic inverse consistently with these parities, so that `psi` is odd in `x` and odd in `y`. Then `U_1` is odd in `x` and even in `y`, while `U_2` is even in `x` and odd in `y`, hence `U(0)=0`. These are symmetry statements, **not** half-plane boundary conditions.

Preserve the quadratic vanishing in the `x` direction, and normalize the first compatible nonzero Taylor term:

\[
\boxed{\rho(x,y)=x^2y\,a(x,y)\quad\text{near }(0,0),\qquad
 a(0,0)=1,}
\]

with `a` smooth and even in both `x` and `y`. This is deliberately **cubic** at the center: oddness in `y` makes the earlier `rho ~ x^2` normalization impossible. The factorization near the center is part of this strong setting; do not substitute the weaker condition of a cubic jet unless you explicitly distinguish the resulting problem.

Let `c=psi_xy(0,0)`. The imposed symmetries give

\[
U(X)=(-cx,cy)+\text{higher-order terms near }0.
\]

Comparing the `x^2 y` coefficient in the profile PDE yields the **necessary self-consistency condition**

\[
\boxed{3c_l-c=1,\qquad c_l=\frac{1+\psi_{xy}(0,0)}{3}.}
\]

Enforce this identity in analysis and numerical computation; `c_l` must not be chosen independently. If you seek a focusing solution, analyze the physically relevant regime `c_l>0`, but do not silently assume its sign without explanation.

## 2. Essential issue: what does full-space Biot–Savart mean?

Before proving NO or claiming numerical YES, specify a coherent admissible class and **uniquely defined** full-plane velocity law, including allowed behavior as `|X| -> infinity`. For sufficiently decaying data the conventional choice is

\[
U=\nabla^\perp(-\Delta)^{-1}\partial_x\rho
  =(-R_1R_2\rho,\,R_1^2\rho).
\]

But nonzero solutions of `(c_l X+U)·grad rho=rho` may have to be unbounded at infinity; the usual Riesz multipliers need not be canonically defined on growing polynomial profiles. Investigate permissible growth and, if required, a **mathematically specified renormalized** inverse, including subtractions, far-field asymptotics, and gauge conditions. A harmonic polynomial cannot be freely added to `psi`: in particular `lambda*x*y` is harmonic, respects the stated parity, changes `psi_xy(0)` and changes the dynamics. Explain exactly how this ambiguity is eliminated or controlled.

Check elementary maximum-principle / characteristic / integral Liouville obstructions first. In particular, smooth profiles decaying at infinity are trivially ruled out by extremum arguments; this does **not** prove NO for the larger growing-profile problem. Conversely, a formal polynomial solution obtained through a nonunique Poisson inversion is not automatically an admissible physical full-plane IPM profile. Do not choose a restrictive function class solely to obtain an easy NO.

## 3. Required analytic investigation

1. Derive the stationary equation and the symmetry/normalization constraints independently. Check every sign, the orientation `nabla^perp psi=(-psi_y,psi_x)`, and the full-plane elliptic operator.
2. Classify meaningful far-field growth and regularity regimes. Examine whether the fixed center, the two invariant axes, and transport of vanishing impose global obstructions. Establish useful exact identities (characteristics, level sets, weighted energy, divergence constraints, moment or sign identities) without assuming unjustified decay or deleting boundary-at-infinity terms.
3. Search seriously for a **rigorous nonexistence theorem** in an appropriate broad admissible class; rule out clearly defined subcases when possible, while recognizing when the main existence question remains open.
4. In parallel, look for nontrivial solutions through asymptotic expansions, symmetry-compatible angular representations, continuation, nonlinear elliptic/transport coupling, or numerical fixed-point/Newton methods. An artificial evolution may be used only as a numerical solver, not substituted for the stationary PDE being verified.

## 4. Required computational investigation if no rigorous NO is obtained

Implement and actually run an independently verifiable solver (Python, Julia, or equivalent); do not merely outline an algorithm. Treat the **full-plane** nonlocal inverse, not a half-plane wall problem. You may exploit symmetry to reduce computation, but reconstruct and independently test the solution on `R^2`.

At minimum:

- Fix `a(0)=1` through an appropriate stable representation that analytically enforces the `x^2 y` factor and parity. Do not let the optimization converge to `rho=0`, a vanishing leading coefficient, or a spurious low-order polynomial/gauge artifact.
- Solve for `rho`, `psi` (or a correctly normalized Biot–Savart representation), and `c_l` **self-consistently**. Explicitly check `c_l=(1+psi_xy(0))/3` by a method independent of the quantity used to fit `c_l`.
- Report both the transport residual `R=(c_l X+U)·grad rho-rho` and elliptic residual `E=-Delta psi-partial_x rho`; monitor symmetry, axis vanishing, normalization, `U(0)=0`, and growth/asymptotic conditions. Compute both meaningful absolute and normalized residual norms, including regions near and away from the axes where `rho` vanishes.
- Increase **both** spatial resolution and computational domain; report results for at least three genuinely distinct resolutions and three domains, unless a rigorous method eliminates a particular limit. Check residual convergence **on fixed interior regions** and separately bound or quantify errors from far-field truncation and the nonlocal inverse. Never identify small residual on one bounded box with a global solution.
- Perform independent validation with different differentiation/integration methodology or a separately implemented residual evaluator; verify against known manufactured test fields and parity checks. Examine conditioning, near-zero cancellations, and spectral/grid aliasing.
- Supply the candidate explicitly (coefficients, data file, or executable generator), reproducible scripts, parameters, convergence tables, plots if useful, and a precise far-field model. Numerically quantify how strongly the evidence supports a global profile rather than a finite-domain artifact.

A persuasive YES should have small **normalized** residuals (ideally around `1e-6` or better where feasible), systematic improvement under refinement, stable normalization and `c_l`, and nonlocal/far-field error checks; an arbitrary residual threshold without convergence evidence is not sufficient. Make clear that even compelling computations are **not** a rigorous existence proof.

## 5. Independent adversarial verification and final answer

Separate a **researcher** who develops the proof/candidate from a **verifier** who independently audits all analytic steps or recomputes the numerical residuals. The verifier must specifically look for: hidden wall boundary conditions, harmonic-gauge freedom, forgotten far-field terms, wrong parity, wrong `x^2 y` jet, independent fitting of `c_l`, convergence to the zero state, and finite-box artifacts.

The main deliverable must be exactly one of:

**NO — Rigorous nonexistence.** State a precise theorem for the targeted admissible class, supply a complete proof with all asymptotic assumptions justified, and explain whether it excludes every profile covered by the stated model or only a subclass.

**YES — Strong numerical existence evidence.** Provide a concrete nonzero candidate, complete computational methodology and reproducibility artifacts, independently validated transport/Poisson residuals, domain/refinement evidence, and honest limits of what numerics establish.

Do not label a restricted trivial observation as a general NO or a formal/inaccurately normalized approximate solution as YES. Partial progress is not one of the two requested successful deliverables; keep working within available resources, but never invent proof or computational data.
