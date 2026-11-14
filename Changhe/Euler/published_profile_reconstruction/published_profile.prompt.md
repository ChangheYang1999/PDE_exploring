# Research Task: Reconstruct Anima Anandkumar's Euler Self-Similar Profile from Published Numerical Results

## 1. Main objective

Our previous Euler PINN optimization has failed to reproduce the profile constructed by Ganeshram, Duruisseaux, and Anima Anandkumar.

The main difficulty may be initialization: our saved profiles are qualitatively very different from the published solution.

**Instead of continuing from an unrelated numerical branch, construct a new initial guess directly from the paper's published numerical solution, then optimize it toward the exact Euler profile equations.**

Reference paper:

https://arxiv.org/html/2609.10867v2

Existing project:

`/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/`

Our previous comparison:

`/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/visualizations/20261113T2145Z/renders/agd-euler-visualcompare-final-bff0a24dbe39-6857463/comparison.pdf`

The primary goal is **an independently validated, high-accuracy Euler profile that belongs to the same numerical solution branch as the paper**.

This is a numerical construction task. Execute the experiments rather than stopping after a feasibility analysis.

## 2. First priority: recover the author's actual numerical data

Before reconstructing a solution from images, investigate whether the authors have released:

- PINN checkpoints or model weights.
- Spline coefficients or numerical profile tables.
- Source code that evaluates the constructed profile.
- Supplementary numerical datasets.
- Public repositories associated with the paper.

Check the paper, supplementary materials, and referenced repositories.

If actual numerical data are available, prioritize importing them into our existing evaluator.

Do not spend excessive time searching for unpublished data. If no usable data are publicly available, proceed immediately to reconstruction from published figures.

## 3. Reconstruct the axial profiles from Figure 2/S1

The paper provides plots of

\[
U(0,z),\qquad \Omega(0,z),\qquad \Psi(0,z).
\]

Extract approximate numerical data from these curves.

Pay special attention to:

- The location and amplitude of extrema.
- Widths of positive and negative regions.
- Zeros and sign changes.
- Asymmetry between positive and negative \(z\).
- Decay toward spatial infinity.

Digitize the published curves using calibrated axes. Preserve the actual coordinate conventions and amplitude scales.

The current numerical solutions differ drastically from the paper, so do not use the current checkpoints to determine the desired shape.

Fit smooth functions

\[
U_0(z),\quad W_0(z),\quad P_0(z)
\]

to the extracted data.

Treat digitization errors explicitly. Do not present approximate readings from figures as exact numerical values.

## 4. Use the Euler equations to enforce axial compatibility

Do not simply interpolate the three axial curves independently and assume they define a valid Euler profile.

The axisymmetric elliptic equation in our formulation is

\[
-\left(
\partial_{rr}+\frac3r\partial_r+\partial_{zz}
\right)\Psi=\Omega.
\]

Near the symmetry axis, write

\[
\Psi(r,z)=P_0(z)+b(z)r^2+O(r^4).
\]

Then

\[
b(z)=-\frac{W_0(z)+P_0''(z)}8.
\]

Use this identity to construct an elliptically compatible expansion near \(r=0\).

Derive the exact axial transport equations directly from the paper and our implemented PDE, checking all signs and normalization conventions.

Use those equations to refine the extracted axial profiles and determine compatible values of the physical parameters, including the traveling speed \(C\).

Keep the paper's intended similarity exponent \(\lambda=1/2\) for the primary reproduction.

Do not impose an arbitrary swirl amplitude such as \(U(0,0)=1\). The amplitude \(A\) is a physical unknown.

Do not force \(A\geq0.5\), introduce an artificial hinge constraint, or normalize individual fields independently.

## 5. Extend the axial reconstruction to a two-dimensional profile

Construct an initial approximation

\[
U(r,z),\qquad \Psi(r,z),
\]

with

\[
\Omega=
-\left(
\partial_{rr}+\frac3r\partial_r+\partial_{zz}
\right)\Psi.
\]

Use the axial reconstruction as a strong initialization constraint.

Choose flexible radial functions consistent with:

- Regularity at \(r=0\).
- The reconstructed axial curves and their radial derivatives.
- The observed radial widths and three-dimensional shapes in Figure 2.
- The correct full-space asymptotic behavior.
- The canonical five-dimensional Poisson coupling.

Possible methods include radial spline expansions, Gaussian mixtures, or a small neural-network correction to the reconstructed profile.

The exact representation is flexible, but all three fields must be mutually compatible.

Do not assume the axial curves uniquely determine the full two-dimensional profile.

Use the paper's three-dimensional plots to select several plausible radial extensions, rather than inventing one arbitrary extension.

In particular, our previous profiles showed a narrow positive swirl core and very different streamfunction behavior. The new initialization should reproduce the paper's broad structures and signs before PDE optimization begins.

## 6. Fit the published profile before minimizing the full PDE residual

Use a staged optimization.

**Stage A — Geometric reconstruction**

Fit the published axial curves and available three-dimensional shape information.

Enforce the elliptic relation and axial transport compatibility.

**Stage B — Physics-compatible initialization**

Improve the two-dimensional extension using the full stationary Euler equations while retaining moderate penalties for agreement with the published profile.

Use a multiscale spatial grid covering both the core and the large spatial scales visible in the paper.

**Stage C — Full Euler optimization**

Gradually remove the image-based fitting penalties.

Optimize the original Euler equations, with the actual physical normalization and canonical coupling.

The final candidate must be justified by PDE residuals, not by resemblance to the published image.

## 7. Reuse the previous PINN optimization framework

Reuse our working Boussinesq/Euler PINN infrastructure wherever applicable:

- MLP architecture.
- Adam optimizer.
- Dense SSBroyden1.
- Automatic differentiation.
- GPU training.
- Checkpoint management.
- Independent validators.

Also consider Gauss–Newton or trust-region refinement if the numerical conditioning requires it.

Avoid rebuilding infrastructure that already works.

For initialization, prioritize the reconstructed published profile over our previous post04/post09/120-step candidates.

However, retain those candidates for independent comparison.

## 8. Alternative: convection continuation

If the direct reconstructed initialization fails, investigate the convection-continuation approach described in the paper.

Determine the exact parameterized equations used by the authors.

If appropriate, construct a solution at a simpler convection parameter and continue gradually toward the full Euler equation.

Do not invent a homotopy without checking its relationship to the paper.

This is a secondary strategy after the direct reconstruction attempt.

## 9. Independent validation

For every promising candidate, evaluate:

- Independent \(R_U\) and \(R_\Omega\) RMS.
- Refined maximum residuals.
- Physical weighted vorticity residual \(rR_\Omega\).
- Canonical five-dimensional Poisson consistency.
- Swirl amplitude and spatial scale.
- Traveling speed and other physical parameters.
- Full-space decay and far-field residual.
- Axis profiles and radial geometry.

Validate on fresh Sobol samples, independent grids and local searches near residual peaks.

Do not accept a candidate because its training loss is small.

Avoid weak-vorticity, near-affine or other degenerate profiles that do not resemble the paper's physical construction.

Compare the reconstructed profile against the published figures at multiple stages.

## 10. Computational efficiency

The previous Euler and IPM campaigns spent too much time on short pilots, rebuilding caches and repeated validation.

Avoid repeating this workflow.

Perform the necessary correctness checks once, then conduct sustained optimization.

Reuse the existing GPU infrastructure and canonical Poisson evaluator.

Keep validation inexpensive during training, with comprehensive independent checks at meaningful checkpoints.

Do not spend most of the allocated time writing reports or exploring unrelated theoretical questions.

If one reconstruction is promising, pursue it deeply instead of launching many nearly identical short experiments.

## 11. Required deliverables

Produce:

1. Digitized data for the paper's axial profiles, or the actual published numerical data if available.
2. An initial two-dimensional Euler profile constructed from those data.
3. Plots showing how well the initial guess matches the paper before optimization.
4. Independently validated optimization results.
5. Side-by-side plots of the final candidate and the paper.
6. A comparison against our previous numerical candidates.
7. Saved checkpoints, code, configurations and reproducibility instructions.

Report separately how much improvement comes from matching the published initial shape and how much comes from subsequent PDE optimization.

## 12. Final instruction

**The primary purpose is to find the same solution branch as the published Euler construction.**

Do not merely continue optimizing our existing numerically unrelated profiles.

Use the published solution as prior information to construct a genuinely new, physically compatible initial guess.

Prioritize actual numerical reconstruction and sustained PINN optimization.

If a promising branch appears, continue refining it toward high accuracy.

If the reconstruction fails, identify precisely whether the difficulty comes from insufficient figure data, incompatible axis fitting, the radial extension, or nonlinear optimization.

Do not claim reproduction without independent physical validation.