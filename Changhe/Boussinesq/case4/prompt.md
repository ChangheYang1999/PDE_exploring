# 24-Hour Research Task: Find a Fixed-Beta Boussinesq Blowup Profile with Much Smaller Center Temperature Slope

## 0. Directories and Primary Objective

Working directory:

`/mnt/d/Changhe_D/case4`

Read-only reference project:

`/mnt/d/Changhe_D/case1`

This is a sustained **24-hour numerical research task**.

We already have a promising numerical construction of a stationary self-similar Boussinesq blowup profile, using a generating-function representation that satisfies temperature transport exactly.

However, the existing profile has a very large center temperature slope,

\[
a_0=\partial_y\Theta(0)\approx600.
\]

This large gradient creates serious difficulties for the analytical existence and stability theory.

**Our goal is to construct a comparable numerical profile with substantially smaller \(a_0\), while keeping the similarity exponent fixed exactly at**

\[
\boxed{\beta=3}.
\]

We want to determine how much \(a_0\) can be reduced without losing the quality of the numerical approximation or violating the structural requirements of the construction.

Use the original transport-exact generating-function method as the primary approach. Do not replace it with an unrelated numerical formulation.

All new code, checkpoints, logs, and reports must remain in `case4`. Treat `case1` as read-only. Reuse existing code without copying the entire historical archive.

---

## 1. Understand and Recover the Original Construction

Begin by reading the relevant mathematical and computational files from:

`/mnt/d/Changhe_D/case1/case1/`

Pay particular attention to:

- `Bsnsq_Setting_I.report.md`
- `Bsnsq_Setting_I.artifacts/`
- `IPM_style_Boussinesq_1720/transport_exact/`
- `IPM_style_Boussinesq_1720/experiments/whole_plane_generating_20261027_v1/`
- `IPM_style_Boussinesq_1720/experiments/whole_plane_refinement_20261028_v1/`
- `IPM_style_Boussinesq_1720/experiments/fresh_jacobian_vertical_v1/`

Identify and understand:

1. The original \(\beta=3\) generating-function solution with source amplitude near 600.
2. Its coefficient arrays, core patches, parameterization, and constraints.
3. The latest optimization methods, particularly the reliable LM and Jacobian implementations.
4. The whole-plane residual evaluation machinery.
5. The structural chart certification and exact-center constraints.
6. The best available checkpoints and their validation status.

The original fixed-\(\beta=3\) state is an important baseline.

The later independently qualified state has

\[
\beta\approx2.99999021854,
\]

so it is **not itself a fixed-\(\beta=3\) candidate**.

It may be used as a warm start only after explicitly setting \(\beta=3\), restoring the constraints, and independently reevaluating the fields and residuals.

Do not simply copy its previously reported accuracy or certification status.

---

## 2. Fixed Mathematical Problem

Solve the stationary Boussinesq equations

\[
\boxed{
\begin{aligned}
(3X+U)\cdot\nabla\Omega+\Omega&=\partial_x\Theta,\\
(3X+U)\cdot\nabla\Theta&=\Theta,\\
-\Delta\Psi&=\Omega,\\
U&=\nabla^\perp\Psi.
\end{aligned}}
\]

Maintain the existing A1 symmetry:

\[
\Theta(-x,y)=\Theta(x,y),
\]

\[
\Theta(x,-y)=-\Theta(x,y),
\]

with \(\Omega,\Psi\) odd in both variables.

At the origin require

\[
\Theta(x,y)=a_0y+O(|X|^3),
\qquad a_0>0,
\]

and

\[
\boxed{\Psi_{xy}(0)=-2}.
\]

The exponent \(\beta\) is not an optimization variable.

Do not change \(\beta\) to reduce the residual.

Do not introduce an independent affine velocity background, violate the canonical whole-plane velocity condition, or weaken the origin constraints.

---

## 3. Preserve the Transport-Exact Generating-Function Method

Use the existing representation

\[
y=G_x(x,\eta),
\]

\[
\boxed{
\Theta=a_{\mathrm{src}}\eta,
\qquad
\Psi=3xG_x+\eta G_\eta-6G.
}
\]

Define

\[
\Omega=-\Delta\Psi,\qquad
U=\nabla^\perp\Psi
\]

in physical coordinates.

This construction ensures that, whenever the coordinate chart is admissible,

\[
(3X+U)\cdot\nabla\Theta-\Theta=0
\]

exactly.

Consequently, the only remaining PDE residual is

\[
R_\Omega=(3X+U)\cdot\nabla\Omega
+\Omega-\partial_x\Theta.
\]

Do not add independent temperature or streamfunction corrections that destroy the exact transport identity.

Use the original Chebyshev generating family and Gaussian core patches, together with the existing exact structural constraints.

A crucial distinction is that

\[
\boxed{
a_0=\partial_y\Theta(0)
=\frac{a_{\mathrm{src}}}{G_{x\eta}(0,0)}.
}
\]

Thus the parameter called `amplitude` or `a0` in some existing source files may not equal the true physical center slope.

**Optimize and report the physical \(a_0\), not merely the source amplitude.**

If possible, impose each desired physical slope as an exact constraint, for example by solving for \(a_{\mathrm{src}}\) in terms of \(G_{x\eta}(0,0)\).

Avoid soft penalties when an exact constraint is available.

---

## 4. Primary Numerical Objective

Continue using the same whole-plane vorticity residual norm:

\[
\boxed{
J=
\frac2\pi
\int_0^{\pi/2}\int_0^\infty
\left(
\frac{r^2R_\Omega}{xy}
\right)^2
\frac{dr}{r}\,d\phi.
}
\]

The quotients on the axes must be interpreted through their smooth extensions.

Temperature transport and Poisson should remain exact.

For each proposed profile, record both

\[
J,\qquad \sqrt J.
\]

Do not rely exclusively on a training-grid objective or pointwise normalized residuals.

Use sufficiently accurate whole-plane quadrature and independent validation to estimate the actual residual norm.

Pay particular attention to the vertical strip, where the earlier best candidate concentrated most of its residual.

The target is not merely a small training loss. We want a profile with:

- Significantly smaller physical \(a_0\).
- Small independently evaluated whole-plane vorticity residual.
- Valid center and phase constraints.
- An admissible globally invertible coordinate chart.
- Correct parity, smoothness, and far-field behavior.
- A canonical sublinear velocity field.

---

## 5. Systematic Continuation Toward Smaller \(a_0\)

The principal numerical experiment should be a continuation in the physical center slope.

Start from the existing fixed-\(\beta=3\) solution near \(a_0=600\).

Try to move gradually toward smaller values, for example

\[
600\to400\to300\to200\to150
\to100\to75\to50\to30\to10.
\]

These are suggested milestones, not mandatory step sizes.

Adapt the steps to the actual conditioning and convergence behavior.

If feasible, continue toward

\[
a_0=5,\quad 2,\quad 1,
\]

or smaller positive values.

We are particularly interested in whether profiles with

\[
\boxed{a_0\lesssim100}
\]

or even

\[
\boxed{a_0\lesssim10}
\]

can achieve residual accuracy comparable to the previous large-\(a_0\) construction.

Do not stop merely because one continuation step fails.

When continuation becomes difficult, investigate:

1. Smaller adaptive parameter steps.
2. Trust-region or damped Levenberg–Marquardt iterations.
3. Pseudo-arclength continuation when simple parameter continuation encounters a fold.
4. Reoptimization of the full coefficient vector after changing \(a_0\).
5. Local multistart optimization near promising states.
6. Improved preconditioning and treatment of nearly singular Jacobians.
7. Targeted refinement of the core and narrow-strip residuals.
8. Increasing the spectral resolution when there is evidence of insufficient approximation power.

Use the existing solver infrastructure wherever possible.

Do not conduct a large blind parameter scan before attempting continuation from the known profile.

---

## 6. Investigate the \(a_0\)-Residual Tradeoff

A central research question is whether reducing \(a_0\) necessarily makes the residual worse.

For each successful continuation state, measure

\[
a_0,\qquad J,\qquad \sqrt J
\]

together with the relevant numerical diagnostics.

Construct an empirical Pareto comparison between physical center slope and independently evaluated residual.

We want to distinguish three possibilities:

**Possibility A: Small \(a_0\) profiles exist and can be accurately approximated.**

In this case, continue improving them, preferably by at least an order of magnitude in \(a_0\) relative to the original profile.

**Possibility B: Smaller \(a_0\) produces an increasingly large residual.**

Determine whether this is caused by a genuine structural incompatibility, an inadequate finite-dimensional approximation space, or limitations of the numerical optimization.

**Possibility C: The continuation branch folds or becomes ill-conditioned.**

Investigate whether another branch exists, whether pseudo-arclength continuation can cross the fold, or whether a different initialization within the same generating-function family can reveal a better solution.

Do not interpret optimizer failure as proof that a Boussinesq profile with smaller \(a_0\) does not exist.

If numerical evidence suggests a positive lower bound on \(a_0\), investigate its mathematical origin using the center constraints, far-field moments, and vorticity transport equation.

Keep numerical conjectures separate from rigorous conclusions.

---

## 7. Protect Against Degenerate or Artificial Solutions

Reducing \(a_0\) must not be achieved by violating the original mathematical problem.

In particular:

- Maintain \(\beta=3\) exactly.
- Maintain the exact strain condition \(\Psi_{xy}(0)=-2\).
- Do not allow the chart Jacobian to vanish or change sign.
- Keep the intended nontrivial center temperature jet.
- Do not abandon the canonical whole-plane elliptic inverse.
- Preserve the far-field behavior required by the original construction.
- Do not hide residual errors through normalization or inappropriate weights.
- Do not add arbitrary temperature or streamfunction degrees of freedom that violate transport exactness.

The physical spatial dilation symmetry preserves \(a_0\). Therefore, reducing \(a_0\) through a change of spatial scale is not a genuine improvement.

Any successful smaller-\(a_0\) profile must represent an actual change in the profile shape.

---

## 8. Independent Validation and Numerical Reliability

The previous project demonstrated that a low training loss is insufficient for accepting a candidate.

Reuse its strongest verification methods.

For promising states, perform:

1. Independent whole-plane residual integration using different quadrature rules.
2. Dense off-grid tests near the origin, axes, and narrow strips.
3. Far-field tail analysis.
4. Center-constraint verification.
5. Global chart-invertibility tests.
6. Verification of exact coefficient and constraint semantics, rather than relying solely on rounded floating-point caches.
7. Resolution and precision sensitivity checks.
8. Independent comparison against the original fixed-\(\beta=3\) baseline.

The existing chart certificates are state-specific. A certificate for an earlier coefficient vector cannot automatically certify a new candidate.

For the strongest candidates, attempt a rigorous structural chart certificate using the available interval methods.

If full rigorous residual certification is too expensive, clearly distinguish numerical validation from rigorous interval bounds.

Never label a candidate independently qualified or rigorously certified unless it has actually passed the corresponding validation requirements.

---

## 9. Computational Strategy for a 24-Hour Campaign

This task should involve actual numerical experiments, not just theoretical planning.

Use the existing Python implementations and checkpoints.

First confirm that the baseline state can be loaded and evaluated correctly at exactly \(\beta=3\). Then begin the lower-\(a_0\) continuation.

Maintain resumable checkpoints and record numerical parameters for each run.

Organize the computation into successive stages:

**Stage I — Baseline recovery.**

Recover the original fixed-\(\beta=3\) profile and establish a trustworthy numerical baseline.

**Stage II — Moderate slope reduction.**

Explore the range from approximately 600 to 100.

**Stage III — Aggressive slope reduction.**

For promising branches, investigate \(a_0<100\), with particular interest in \(a_0\le10\).

**Stage IV — Accuracy improvement.**

Select the best smaller-\(a_0\) profiles and improve their residuals using the strongest available optimization methods.

**Stage V — Independent validation.**

Subject the best candidates to more accurate independent whole-plane checks and structural tests.

The stages may overlap or be reordered if numerical evidence justifies doing so.

If a method fails, diagnose the failure and continue exploring alternative numerical strategies within the same mathematical construction.

Respect the available WSL memory, CPU resources, and storage capacity.

Avoid excessive parallel processes and unbounded checkpoint generation. Preserve important raw evidence and accepted states, but do not duplicate the multi-gigabyte reference archive.

Do not modify the source project or make unnecessary Git changes.

---

## 10. Deliverables

Save the numerical results and research outputs under:

`/mnt/d/Changhe_D/case4`

Provide at least:

- `CONTINUATION_REPORT.md`: continuation strategy, successful branches, failures, and numerical diagnostics.
- `RESULTS.csv`: a comparison table for tested \(a_0\) values, independently measured residuals, validation status, and checkpoint paths.
- `BEST_CANDIDATE/`: the best overall smaller-\(a_0\) profile, including its coefficients, exact parameter definitions, and sufficient information to reproduce it.
- `VALIDATION_REPORT.md`: independent numerical accuracy checks and structural verification.
- `FINAL_REPORT.md`: the final mathematical and numerical conclusions.

Save the actual working scripts, configuration files, and checkpoints required to reproduce accepted results.

Do not create a new copy of every source file for each experiment.

In the final report, answer:

1. What is the smallest positive physical \(a_0\) reached with a numerically credible profile?
2. What is its independently evaluated whole-plane residual?
3. How does it compare with the original fixed-\(\beta=3\), \(a_0\approx600\) profile?
4. Is there a clear trend or tradeoff between \(a_0\) and residual accuracy?
5. Does the numerical continuation encounter folds, loss of chart invertibility, or other structural difficulties?
6. Is there numerical evidence that the original large value of \(a_0\) is necessary?
7. Which candidate is most promising for a subsequent rigorous a posteriori existence proof?

**The primary goal is to find an actual, substantially smaller-\(a_0\) numerical profile, not merely to recommend how such a computation might be performed.**

Conduct the investigation throughout the available 24-hour research period, preserving reproducible progress and adapting the strategy when necessary.

If a high-quality small-\(a_0\) profile cannot be found, provide a careful numerical diagnosis, not an unsupported nonexistence claim.

Write the final report in English.