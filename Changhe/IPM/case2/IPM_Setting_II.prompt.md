# Research task II — Fully asymmetric full-plane IPM self-similar profiles with a moving center

You are undertaking an independent mathematical and computational research project. This prompt is **self-contained**: assume no prior discussion, paper, code, or results. Your goal is to achieve **one of two substantial endpoints**:

- **NO (theorem):** Rigorously prove nonexistence of nonzero, admissible profiles for the model below in a precise, mathematically justified and genuinely relevant function class.
- **YES (numerical evidence, not a theorem):** Construct a concrete, reproducible, nontrivial full-plane candidate and provide compelling, independently checked numerical evidence that it persists as resolution and domain size increase.

Do not end with an unverified claim, a single finite-domain computation, a purely formal polynomial solution with an arbitrary Poisson gauge, or an easy nonexistence theorem that only covers bounded decaying densities while the actual target admits growing ones. Continue serious analytic and computational attempts rather than treating partial progress as one of the two requested outcomes. Never fabricate a result if the task remains unresolved.

## MANDATORY EXECUTION CONTRACT — AT LEAST 24 HOURS OF REAL RESEARCH TIME

**This is a hard execution requirement, not a suggestion or an estimated difficulty. Devote a minimum of 24 hours of actual elapsed wall-clock time to the fully asymmetric moving-center investigation before submitting any terminal research result.** The 24 hours begin when you actually start the work, not when the prompt was written or received. Twenty-four model-thinking iterations, 24 CPU-hours accrued in parallel, or 24 hours of mere queued/idle/sleeping time do **not** satisfy this rule. Do not declare success, failure, or completion at hour 2, hour 10, or hour 23 just because you have a promising theorem or a small residual. Twenty-four hours is a **minimum**, not a deadline or permission to stop when the evidence remains weak.

**Start and audit trail.** At the beginning, record the actual local or UTC start time `T0` as an ISO 8601 timestamp with timezone, the computational environment, and the precise problem definition. Maintain a durable chronological log with timestamps recording mathematical results, attempted counterexamples, executed code and commands, solver configurations, numerical outputs, failed attempts, checkpoints, and independent verifier activity. Record `T_end` and the actual elapsed time `T_end-T0` in the final report. Include enough supporting evidence (job timestamps, scripts, output files, or logs) for an independent reader to assess whether the requirement was met. Never invent timestamps, logs, calculations, code execution, or verification.

**Minimum 24-hour research protocol (wall-clock schedule, adaptable across parallel workstreams):**

- **Hours 0–6:** Independently derive the governing identities; audit the correct full-plane inverse, origin normalization, admissibility, and far-field/gauge issues. Pursue nonexistence mechanisms and construct analytic test examples. Begin implementation and regression tests when warranted.
- **Hours 6–14:** Actively pursue either a rigorous NO proof or candidate construction; test competing approaches rather than repeating a stalled argument. Execute and inspect real computations where appropriate. Preserve intermediate data and write down all mathematical gaps.
- **Hours 14–20:** Deepen the most promising line while launching an independent adversarial audit. For a candidate, perform resolution/domain refinements, independent Poisson and transport residual checks, and artifact tests. For a prospective proof, check every assumption, endpoint, integration by parts, and counterexample.
- **Hours 20–24 (and longer if necessary):** Carry out a focused, adversarial verification phase. Attempt to falsify the tentative conclusion, independently reproduce decisive numerical results or rederive the key proof, resolve discrepancies, and prepare reproducibility materials.

**Early discovery is not an early-exit exception.** If an apparently complete NO theorem or convincing YES candidate emerges before the 24-hour minimum, spend the remaining time checking, attempting to break, generalizing where justified, and independently reproducing the result. Do not use passive waiting or `sleep` as a substitute for research. If the environment terminates or imposes a shorter execution limit, preserve checkpoints and use supported continuation facilities; if you cannot genuinely continue for 24 elapsed hours, explicitly disclose that the 24-hour requirement was **not met**. Do not falsely assert compliance or force a YES/NO conclusion unsupported by the evidence.

**Terminal output gate.** A successful terminal report may be issued **only after at least 24 hours** and only when the specified evidentiary standards below have actually been met: `NO` requires a complete rigorous theorem in the claimed class; `YES — numerical evidence` requires concrete reproducible numerical evidence, not a formal identity or isolated small residual. If neither endpoint has been established after 24 hours, keep investigating if resources permit. If further execution is genuinely impossible, report the exact limitation and outstanding gap rather than fabricating either outcome. Include the research/verification timeline in any final report.

## 1. Original IPM and the moving-center reduction

The physical equation is the two-dimensional incompressible porous-media system on the **entire** `R^2`:

\[
\partial_t\varrho+u_{\rm phys}\cdot\nabla\varrho=0,\qquad
u_{\rm phys}=\nabla^\perp\Psi=(-\Psi_{z_2},\Psi_{z_1}),\qquad
-\Delta_Z\Psi=\partial_{z_1}\varrho.
\]

Use the moving-center ansatz, with `X=(x,y)` and `Z=(z_1,z_2)`,

\[
X=C_l(t)(Z-Z_*(t)),\qquad
\varrho(t,Z)=C_\rho(t)\rho(X),\qquad
\Psi(t,Z)=\frac{C_\rho(t)}{C_l(t)}\psi(X).
\]

Normalize the density-scaling coefficient by

\[
-\frac{\dot C_\rho}{C_\rho^2 C_l}=1,
\qquad
c_l=\frac{\dot C_l}{C_\rho C_l^2} \ \text{constant},
\]

and let the center follow the actual fluid velocity,

\[
\dot Z_*(t)=C_\rho(t) U(0),
\qquad U=\nabla^\perp\psi.
\]

The stationary profile system to be investigated is therefore

\[
\boxed{\begin{aligned}
&(c_lX+U(X)-U(0))\cdot\nabla\rho(X)=\rho(X), && X\in\mathbb R^2,\\
&U=(-\psi_y,\psi_x),\\
&-\Delta\psi=\partial_x\rho, &&X\in\mathbb R^2.
\end{aligned}}
\]

`c_l` is an unknown scalar. **Do not impose any symmetry** in either variable, no boundary at `y=0`, and no fixed-center condition `U(0)=0`. The subtraction `U(X)-U(0)` is essential; it comes from following the fluid center, not from an arbitrary modification of the PDE.

## 2. The only local geometric constraint

At the moving center require a smooth, nondegenerate **rank-one quadratic Taylor jet**

\[
\boxed{\rho(X)=x^2+O(|X|^3)\quad\text{as }X\to0.}
\]

Equivalently `rho(0)=0`, `grad rho(0)=0`, and `D^2 rho(0)=diag(2,0)`, with sufficient differentiability for the stated remainder. This is **only a jet at the center**: do **not** assume `rho(x,y)=x^2 a(x,y)` in a whole neighborhood, do not require the entire line `x=0` to be invariant, and do not impose even/odd parity, positivity, sign-definiteness, or a half-plane boundary condition.

Let `c=psi_xy(0)`. Because `V(X)=c_l X+U(X)-U(0)` vanishes at `X=0`, comparison of quadratic Taylor coefficients in `V·grad rho=rho` yields

\[
\boxed{c_l=\frac12+\psi_{xy}(0),\qquad \psi_{yy}(0)=0.}
\]

The Poisson equation at `X=0` then gives `psi_xx(0)=0`, so

\[
\boxed{\nabla U(0)=\begin{pmatrix}-c&0\\0&c\end{pmatrix}.}
\]

These are **necessary compatibility identities**, not assumptions derived from symmetry. Verify the identities and signs independently. The IPM law singles out the `x` direction via `partial_x rho`, so rotating the rank-one Hessian to the `x` axis is **not** automatically a harmless `without loss of generality` operation; its orientation is a real part of this setting.

The `x^2` coefficient fixes the spatial normalization and precludes convergence to the zero profile. If focusing is intended, pay special attention to `c_l>0`, while clearly identifying which conclusions depend on its sign.

## 3. Fundamental admissibility and gauge problems

The full-plane Poisson equation alone does **not** uniquely determine the velocity without a far-field condition or an explicit Biot–Savart/renormalization prescription. For rapidly decaying data the usual multiplier is

\[
U=\nabla^\perp(-\Delta)^{-1}\partial_x\rho
=(-R_1R_2\rho,\,R_1^2\rho),
\]

but this may cease to have a canonical meaning for growing densities. Specify a physically/mathematically justified class at infinity and a unique construction of `U`; address how low-frequency divergences, subtraction constants, linear/higher harmonic fields, and the moving-center subtraction interact. Removing `U(0)` eliminates a constant drift but does **not** fix arbitrary harmonic shear/strain fields.

**Critical trap:** If the problem is interpreted as *only* the local differential identities with unrestricted polynomially growing `psi`, the following is an exact formal global solution:

\[
\rho(x,y)=x^2,\qquad
\psi(x,y)=-\frac{x^3}{3},\qquad
U(x,y)=(0,-x^2),\qquad c_l=\frac12.
\]

Indeed `-Delta psi=partial_x rho=2x`, `U(0)=0`, and the stationary transport equation holds. It has quadratic-growth velocity and an elliptic inversion that is not uniquely specified by the bare Poisson PDE. **Report this fact, but do not mislabel it as numerical evidence for a meaningful, uniquely normalized Biot–Savart profile**. The primary research target is a genuinely admissible (preferably non-polynomial) solution for a carefully fixed full-space velocity law, or a rigorous theorem excluding such solutions. Do not artificially rule out all growing densities simply because bounded, decaying profiles satisfy an elementary extremum obstruction.

The complete classification of possible asymptotic classes and the distinction between formal polynomial solutions and physically selected nonlocal velocities are integral parts of the task.

## 4. Analytic research program

1. Independently rederive the moving-center stationary PDE, the normalization `c_rho=1`, and both quadratic compatibility conditions. Check every sign and distinguish the physically moving center from merely declaring a stationary origin.
2. Analyze what the local rank-one Hessian does and does not force. In particular, do **not** assume an invariant straight zero line: zeros and double zeros may be transported along a curved trajectory. Determine any valid transport geometry / characteristic identities and local normal-form constraints beyond second order.
3. Determine meaningful far-field classes compatible with the nonlocal full-plane velocity and the stationary equation. Try rigorous Liouville/nonexistence arguments using characteristics, extrema, weighted transport identities, zero-set geometry, elliptic structure, and global growth. State precisely when integrations by parts are justified.
4. Seriously search for non-polynomial admissible profiles without imposing parity inadvertently. Explore suitable asymptotic expansions, continuation methods, coupled elliptic-transport solvers, and alternative center/jet formulations. Clearly identify which possible solutions would be gauge or truncation artifacts.

A theorem only excluding `rho in L^infty` or `rho -> 0` at infinity does not settle the main task unless the chosen physically justified admissible class necessarily has that property. Do not relabel a result about a convenient subset as full NO.

## 5. Numerical program if no full NO theorem is proved

Write and **run** working reproducible code (Python, Julia, or equivalent). Use a genuine two-dimensional **full-plane** representation without artificial reflection symmetry. A stationary Newton, least-squares, spectral, collocation, continuation, or other nonlinear solver is acceptable; whatever it produces must be independently checked against the original stationary PDE and the correctly specified full-space elliptic inverse.

Minimum required checks:

- Enforce the exact local jet `rho(0)=0`, `grad rho(0)=0`, `rho_xx(0)=2`, `rho_xy(0)=rho_yy(0)=0`, without imposing `rho=x^2 a` on an entire neighborhood. Resolve the jet with more than a few noisy finite-difference points.
- Simultaneously determine `rho`, `U` and `c_l`. Verify **independently** that `c_l=1/2+psi_xy(0)` and `psi_yy(0)=psi_xx(0)=0`; compute the derivative matrix of `U` at the center and verify its predicted diagonal form.
- Numerically evaluate the **actual moving-center operator** `R=[c_l X+U(X)-U(0)]·grad rho-rho`, alongside `E=-Delta psi-partial_x rho`. Report absolute and properly normalized `L^2`, weighted and/or supremum residual norms, in central and off-center regions, including neighborhoods of the rank-one vanishing set.
- Refine at least three spatial resolutions and three expanding computational domains; show convergence on fixed interior sets and credible control of far-field/nonlocal truncation. Assess stability of `c_l`, the Taylor jet, asymptotic behavior, and candidate shape. Use a separate verification code or a genuinely independent differentiation/inversion procedure. Check condition numbers and spurious near-nullspace/harmonic modes.
- Test whether the solver has secretly selected an even or odd subspace or converged to the elementary `rho=x^2` polynomial. A candidate with incidental symmetries is permissible if it is not merely an unconstrained harmonic-gauge or polynomial artifact, but asymmetry must never be imposed or excluded by the computational ansatz.
- Provide executable scripts, numerical coefficients or machine-readable candidate data, precise inversion and far-field prescriptions, convergence tables, and direct residual checks. Pursue small normalized errors (around `1e-6` or smaller if practical) **and** stable refinement and domain convergence. Report what remains uncertified.

Do not equate a finite-box residual with global existence or numerical evidence with a proof. In particular, fitting arbitrary far-field boundary conditions or adding harmonic terms to reduce residuals is not an admissible numerical shortcut.

## 6. Independent verification and requested terminal result

Use a two-role process: a **researcher** devises the theorem or computes the candidate; an independent **verifier** actively tries to falsify it. The verifier must check Poisson gauge, asymptotics, center motion, normalization, local Taylor comparison, hidden symmetry, nonlocal truncation, and independently recomputed residuals.

Deliver exactly one successful outcome:

**NO — Rigorous nonexistence:** A complete theorem and proof for a natural, explicitly defined full-plane admissible class, with all hypotheses necessary and justified and the relationship to broader classes stated accurately.

**YES — Strong numerical existence evidence:** A concrete admissible non-polynomial or otherwise physically nontrivial candidate, executable reproducibility artifacts, independent checks of both PDEs and all origin constraints, and clear evidence of convergence with both numerical resolution and spatial domain size. Describe this as evidence, **not** a theorem.

Neither a narrow bounded-profile exclusion nor the trivial unrestricted-polynomial example counts as completing the intended research goal. Partial results are not a successful final deliverable. Do not claim either endpoint without the corresponding proof or computation.
