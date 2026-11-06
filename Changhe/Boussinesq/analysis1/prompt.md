# 24-Hour Research Task: Transfer the IPM A Posteriori Existence Framework to Boussinesq Blowup

## 0. Directories and Research Objective

Working directory:

`/mnt/d/Changhe_D/analysis1`

Read-only reference projects:

- `/mnt/d/Changhe_D/case1`
- `/mnt/d/Changhe_D/PDE_exploring/Changhe/IPM/combined3`
- `/mnt/d/Changhe_D/PDE_exploring/Changhe/IPM/combined1`, if needed for the mathematical development.

Create all new research notes, proofs, experiments, and reports exclusively in `analysis1`. Do not modify the reference projects or duplicate their large datasets.

**This is a sustained 24-hour mathematical research task. Do not stop after a preliminary analysis or the first unsuccessful approach.**

Our goal is to determine whether the a posteriori existence framework developed for stationary self-similar IPM can be adapted to the existing Boussinesq blowup profile.

There are two nonnegotiable requirements:

1. Fix the similarity exponent **exactly at \(\beta=3\)**.
2. Work with the genuinely non-small numerical profile, whose physical center temperature slope is approximately \(a_0=600\).

The current numerical residual is not our main concern in this task.

**Assume that the numerical residual can be further optimized to any accuracy required by the theorem.**

The central question is:

> If the residual were sufficiently small, could our existing IPM techniques rigorously prove the existence of an exact smooth Boussinesq profile near the numerical approximation? Or are there fundamental analytic obstacles that cannot be eliminated merely by reducing the residual?

We want to identify and, if possible, eliminate those obstacles.

---

## 1. Read and Reconstruct the Existing Work

First study the Boussinesq project in `case1`, particularly:

- `case1/Bsnsq_Setting_I.report.md`
- `case1/Bsnsq_Setting_I.artifacts/`
- `case1/IPM_style_Boussinesq_1720/MATHEMATICAL_DESIGN.md`
- `case1/IPM_style_Boussinesq_1720/transport_exact/`
- The latest structural certificates, numerical profiles, and whole-plane residual verification methods.

Understand the precise construction, not just its numerical output.

Then carefully study the IPM existence framework in `combined3`, including its relevant rigorous proofs, numerical certification methods, and any unresolved verification dependencies.

Focus on:

- The signed \(L^2\) coercivity mechanism.
- Nonlocal linearized operators and finite-rank or compact-commutator treatments.
- Construction of inverses for frozen transport operators.
- Fixed-parameter nonlinear correction.
- Weighted high-regularity estimates and fractional derivatives.
- Singular weights near the origin.
- Invariant-ball arguments, Schauder fixed points, and contraction estimates.
- The distinction between abstract existence theorems and actual numerical certificates.

Do not simply copy the final inequalities from IPM. Reconstruct the mathematical mechanism and determine exactly which steps survive in Boussinesq.

Do not treat a conditional or incompletely certified IPM result as unconditional.

---

## 2. Fixed Boussinesq Equations

Use the conventions

\[
-\Delta\Psi=\Omega,\qquad
U=\nabla^\perp\Psi=(-\Psi_y,\Psi_x).
\]

Fix \(\beta=3\). The stationary system becomes

\[
\boxed{
\begin{aligned}
(3X+U)\cdot\nabla\Omega+\Omega&=\partial_x\Theta,\\
(3X+U)\cdot\nabla\Theta&=\Theta,\\
-\Delta\Psi&=\Omega.
\end{aligned}}
\]

The symmetry class is

\[
\Theta(-x,y)=\Theta(x,y),\qquad
\Theta(x,-y)=-\Theta(x,y),
\]

with \(\Omega,\Psi\) odd in both variables.

At the origin,

\[
\Theta(x,y)=a_0y+O(|X|^3),\qquad a_0\ne0,
\]

and the required strain is

\[
\Psi_{xy}(0)=-2.
\]

The approximate profile has \(a_0\approx600\).

Do not introduce an independent affine background velocity. Preserve the canonical whole-plane Biot–Savart law and the original far-field conditions.

Be especially careful that the latest qualified numerical state has \(\beta\ne3\). It must not be used as a certified fixed-\(\beta=3\) profile without reimposing the exponent and verifying the resulting fields.

---

## 3. Derive the Exact Correction Equations

Let

\[
\bar\Omega,\quad\bar\Theta,\quad\bar\Psi
\]

denote a fixed numerical reference profile with \(\beta=3\).

Write

\[
\Omega=\bar\Omega+h,\qquad
\Theta=\bar\Theta+g,\qquad
\Psi=\bar\Psi+\psi,
\]

with

\[
-\Delta\psi=h,\qquad
u=\nabla^\perp\psi.
\]

Derive the exact correction equations, including all linear and nonlinear terms.

For an approximate reference with exact temperature transport, the natural system is

\[
\begin{aligned}
(3X+\bar U+u)\cdot\nabla h
+h-\partial_xg
+u\cdot\nabla\bar\Omega
&=-R_\Omega,\\
(3X+\bar U+u)\cdot\nabla g
-g+u\cdot\nabla\bar\Theta
&=0.
\end{aligned}
\]

Verify these identities and identify the correct domain, symmetry constraints, and center normalization.

Investigate two formulations:

**Route A: Coupled correction.**

Treat \(h\) and \(g\) as unknowns, using the elliptic inverse to express \(u\) through \(h\).

**Route B: Transport-exact correction.**

Use the existing generating-function representation

\[
y=G_x(x,\eta),
\]

\[
\Theta=a_{\mathrm{src}}\eta,\qquad
\Psi=3xG_x+\eta G_\eta-6G.
\]

Perturb \(G\) while preserving temperature transport exactly.

This reduces the problem to a single remaining vorticity equation, but may introduce derivative loss, chart-invertibility constraints, and nonstandard operators.

Determine which formulation is better suited for a rigorous a posteriori existence theorem. Consider hybrid approaches if necessary.

Do not assume that correcting vorticity while holding temperature fixed preserves the temperature transport equation.

---

## 4. Investigate the Natural Energy Spaces

A particularly important possibility is to use:

- An \(L^2\)-type norm for the temperature correction \(g\).
- A homogeneous \(H^{-1}\)-type norm for the vorticity correction \(h\), equivalently an \(L^2\) norm of \(\nabla\psi\).

The motivation is that

\[
\partial_xg\in H^{-1}
\]

when \(g\in L^2\).

In the vorticity equation, test against \(\psi=(-\Delta)^{-1}h\), not necessarily against \(h\).

Carefully verify all integration-by-parts identities, boundary contributions, and required decay assumptions.

For example, for sufficiently regular and decaying perturbations, the pure temperature transport formally gives

\[
\left\langle
(3X+\bar U)\cdot\nabla g-g,g
\right\rangle
=-4\|g\|_2^2.
\]

For the vorticity equation, investigate the corresponding \(H^{-1}\) identity

\[
\begin{aligned}
&\left\langle
(3X+\bar U)\cdot\nabla h+h,\psi
\right\rangle\\
&\qquad=
-5\|\nabla\psi\|_2^2
-\int_{\mathbb R^2}
\nabla\psi\cdot(D\bar U)\nabla\psi\,dX.
\end{aligned}
\]

Check its validity for the actual whole-plane profiles and determine the contribution of the strain term.

Also investigate the exact cancellations associated with

\[
u=\nabla^\perp\psi,\qquad
u\cdot\nabla\psi=0.
\]

For example, terms involving

\[
\int\psi\,u\cdot\nabla h
\quad\text{and}\quad
\int\psi\,u\cdot\nabla\bar\Omega
\]

may vanish under appropriate integration-by-parts conditions.

These cancellations could be substantially more useful than crude estimates involving \(\|\nabla\bar\Omega\|_\infty\).

Establish which identities survive in weighted spaces.

---

## 5. The Main Difficulty: Large \(a_0\)

The approximate profile has

\[
\partial_y\bar\Theta(0)\approx600.
\]

Consequently, the coupling

\[
u\cdot\nabla\bar\Theta
\]

can be very large near the origin.

A direct perturbative estimate based on

\[
\|\nabla\bar\Theta\|_\infty
\]

may destroy coercivity.

**Do not assume \(a_0\) is small, and do not impose a global smallness assumption on the reference profile.**

Investigate whether the large temperature gradient is genuinely an obstruction to invertibility or only an artifact of an unsuitable energy estimate.

Consider:

1. Coupled energy estimates with optimized relative weights and possible cross terms.
2. Exact cancellations between vorticity and temperature equations.
3. Anisotropic or singular weights adapted to the axes and the origin.
4. Localized coercivity estimates and global patching.
5. Nonperturbative use of the numerical reference state.
6. Spectral nondegeneracy, finite-dimensional unstable directions, and Fredholm alternatives.
7. Adjoint estimates or finite-rank corrections when direct coercivity fails.

Pay particular attention to the methods developed in Chen's singular-weight stability work and to the singular-weight arguments already investigated in the IPM project.

Do not merely cite those arguments. Determine whether their exact hypotheses and commutator estimates apply here.

If a proposed coercivity estimate is false, try to find an explicit test function, model calculation, or spectral mechanism demonstrating failure.

---

## 6. Inverse Operator and Fixed-Point Theory

Assume that the numerical residual can be reduced to a prescribed value \(\varepsilon>0\).

Try to formulate and prove a precise a posteriori existence theorem with the following structure:

\[
\boxed{
\text{Quantitative hypotheses on the reference profile}
+\text{ sufficiently small residual}
\Longrightarrow
\text{exact smooth profile at }\beta=3.
}
\]

The theorem should specify:

- The function spaces.
- The exact linearized or frozen operator.
- Its inverse or coercivity assumptions.
- Quantitative constants.
- The residual norm required.
- The nonlinear estimate.
- The size of the correction.
- Origin, symmetry, chart, and far-field compatibility.
- A rigorous mechanism for obtaining high regularity.

First attempt to prove the required inverse and regularity estimates for the actual numerical reference profile.

A conditional theorem is useful as an intermediate result, but **do not stop at a conditional theorem**. Continue trying to establish its hypotheses.

If a fixed-point scheme is available, compare contraction and Schauder approaches. Do not insist on contraction if an invariant convex set and compactness provide a stronger route.

Avoid unproved assumptions of compactness, derivative gain, or uniform high-regularity bounds.

---

## 7. High Regularity and Singular Weights

A weak \(L^2\times H^{-1}\) correction is not automatically a smooth profile.

Establish whether one can bootstrap to the required regularity.

Study:

- Weighted Sobolev and fractional derivative estimates.
- Commutators with the nonlocal elliptic inverse.
- Transport estimates near the axes and the origin.
- Singular weights compatible with the A1 symmetry.
- Higher derivatives of the stationary equations.
- Far-field behavior and appropriate weighted spaces.
- Uniform estimates for frozen nonlinear transport operators.

Be particularly careful about derivative loss in the transport-exact generating-function formulation.

The goal is a genuinely smooth Cartesian profile, not merely a weak solution away from the origin.

---

## 8. Separate Residual Accuracy from Structural Obstacles

Throughout the investigation, distinguish:

**Numerical obstacle:** The residual is not yet small enough.

**Analytical obstacle:** The correction operator is not known to be invertible, a stability estimate fails, or the required regularity cannot be established.

For this task, treat the first obstacle as potentially solvable by further numerical optimization.

Concentrate on the second.

Determine whether the large value \(a_0\approx600\) introduces a genuine lower bound on an unstable mode, a failure of coercivity, or another obstacle that persists even as

\[
\varepsilon\longrightarrow0.
\]

Do not claim that an arbitrarily small residual alone proves existence.

The ultimate finite-time blowup interpretation should also be classified carefully: a smooth whole-plane profile with unbounded far-field temperature does not by itself yield blowup from bounded initial data. Localization and dynamical stability are separate problems and should not be silently assumed.

---

## 9. Research Strategy and Deliverables

Work iteratively throughout the 24-hour research period.

Start from the strongest existing IPM argument and attempt a direct transfer. When a step fails, identify its exact mathematical cause and investigate a modified method. Continue until a rigorous result or a precise obstruction is obtained.

Prefer analytical proofs. Use focused symbolic or numerical tests when they can confirm identities, detect counterexamples, or assess the spectrum of a candidate operator.

Do not launch expensive full-profile optimization in `analysis1`. That is the separate `case4` task.

Keep the output concise and organized, with at least:

- `IPM_TO_BOUSSINESQ_TRANSFER.md`: a step-by-step comparison of the proof mechanisms.
- `ENERGY_AND_INVERSE.md`: detailed mathematical derivations and verified or conditional estimates.
- `EXISTENCE_THEOREM.md`: the strongest precise theorem established, with proof and explicitly identified hypotheses.
- `OBSTRUCTIONS.md`: unresolved obstacles, failed estimates, counterexamples, and proposed remedies.
- `FINAL_REPORT.md`: the overall verdict and prioritized next steps.

Keep detailed computations and supporting scripts only when needed for reproducibility.

In the final report, answer these questions explicitly:

1. If the residual could be made arbitrarily small, would the current \(\beta=3,\ a_0\approx600\) profile admit a rigorous existence proof using the IPM framework?
2. Which parts of the IPM argument transfer without substantial modification?
3. Which steps require genuinely new estimates?
4. Is the large \(a_0\) a fundamental obstruction or merely a quantitative difficulty?
5. What explicit additional bounds would need to be proved or certified?
6. Can the existence theorem be closed now? If not, identify the exact remaining mathematical gaps.

**The priority is to prove as much as possible, not merely to outline possible approaches.**

Do not fabricate a positive result. If an estimate fails, explain precisely why and continue exploring alternatives.

All final mathematical statements must distinguish fully proved results from conditional claims and numerical evidence.

Write the research report in English.