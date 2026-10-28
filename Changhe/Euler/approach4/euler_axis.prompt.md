# 24-Hour Numerical Investigation of Smooth Axisymmetric Self-Similar 3D Euler Profiles with Swirl

## Mission and execution authorization

You are responsible for executing a substantial, reproducible **24-hour numerical research campaign** to investigate smooth, globally defined, axisymmetric backward self-similar profiles of the unforced three-dimensional incompressible Euler equations.

This is an actual numerical research task, not merely a request to propose an algorithm, build a code scaffold, or conduct a literature review.

The primary target is a nontrivial, globally decaying, smooth axisymmetric profile **with nonzero swirl**, with a freely optimized similarity exponent

\[
\boxed{\frac12<c_l<\frac34.}
\]

Investigate the critical case \(c_l=1/2\) separately.

The range \(2/5<c_l<1/2\), which was the target of an earlier non-axisymmetric investigation, must first be subjected to the rigorous exclusion described below. Do not spend substantial computational resources optimizing smooth profiles in a class already ruled out by a valid theorem.

The available research server reportedly has eight NVIDIA A100 GPUs, multicore CPUs, and substantial RAM. Inspect the actual allocation and hardware before scheduling jobs. Use the GPUs and CPU cores productively, but do not assume all eight GPUs or any particular memory capacity are available.

The maximum authorized actual campaign wall-clock duration is **24 hours**, including development, numerical discovery, refinement, independent validation, and final reporting.

Organize the campaign as follows:

| Stage | Campaign hours | Duration | Objective |
|---|---|---|---|
| I | 0–7 | 7 hours | Mathematical tests, implementation, broad discovery |
| II | 7–18 | 11 hours | Refinement, continuation, full-space matching |
| III | 18–24 | 6 hours | Independent verification and adversarial tests |

Protect the last six hours for verification, even if promising candidates have not converged.

Do not stop after a few failed optimizations, but do not pad the runtime with unnecessary computation. An early termination is appropriate if a rigorous theorem covers the complete proposed target class, if there is a genuine resource/safety problem, or if an externally imposed execution limit prevents continuing.

All reporting and documentation must be in English.

Use the notation \(c_l\) consistently. Do not introduce a rotation parameter for an axisymmetric profile: rigid rotations about its symmetry axis act trivially on the similarity equation.

Keep the entire experiment in a dedicated directory, preferably:

`axisymmetric_euler_24h/`

Do not modify existing unrelated research files. Use an isolated software environment and retain reproducible checkpoints.

---

## 0. Mandatory mathematical feasibility audit

Before large numerical jobs, examine the following result:

**Peter Constantin, Mihaela Ignatova, and Vlad Vicol, "On putative self-similarity for incompressible 3D Euler," arXiv:2602.17570v3 (2026).**

https://arxiv.org/html/2602.17570v3

In particular, independently read and check Theorem 4.5, its hypotheses, and its proof.

The theorem rules out nontrivial smooth globally self-similar axisymmetric Euler profiles with \(c_l<1/2\) under specified sublinearity and far-field bounds.

The relevant axisymmetric circulation variable is

\[
\Gamma=rU^\theta.
\]

It satisfies

\[
\boxed{
(1-2c_l)\Gamma+
(c_l r+U^r)\partial_r\Gamma+
(c_l z+U^z)\partial_z\Gamma=0.
}
\]

For \(c_l<1/2\), bounded backward meridional characteristics and regularity imply that \(\Gamma\) vanishes. The subsequent swirl-free potential-vorticity equation forces the vorticity to vanish under the theorem's assumptions.

Your tasks are:

1. Verify the theorem's exact assumptions rather than relying on its abstract.
2. Verify that the original target of smooth, globally decaying profiles with the prescribed power-law far field is covered.
3. Identify precisely which conditions would have to fail for an alternative axisymmetric construction with \(c_l<1/2\) to escape the theorem.
4. Confirm that the theorem does not automatically exclude the proposed \(c_l>1/2\) search.
5. Record the status of the critical case \(c_l=1/2\).

Do not confuse smooth full-space profiles with profiles possessing limited regularity, boundaries, anisotropic scaling, or only local/asymptotic self-similarity.

Time-box this initial audit to approximately 60–90 minutes unless a genuine mathematical contradiction requires immediate attention. Implementation and hardware tests may proceed concurrently.

**The main numerical search must focus on the admissible, not-yet-excluded regime.**

---

## 1. Exact self-similar Euler formulation

Let

\[
\tau=T-t,\qquad y=\frac{x-x_*}{\tau^{c_l}},
\]

and consider the backward self-similar ansatz

\[
u(x,t)=\tau^{c_l-1}U(y),
\]

\[
p(x,t)=\tau^{2c_l-2}P(y).
\]

The stationary profile satisfies

\[
\boxed{
(1-c_l)U+(c_l y+U)\cdot\nabla U+\nabla P=0,
}
\]

\[
\boxed{\nabla\cdot U=0.}
\]

Work in cylindrical coordinates \((r,\theta,z)\), with

\[
U=U^r(r,z)e_r+U^\theta(r,z)e_\theta+U^z(r,z)e_z.
\]

Axisymmetry means independence of \(\theta\), not vanishing swirl.

The exact component equations are

\[
\begin{aligned}
0={}&(1-c_l)U^r
+(c_l r+U^r)\partial_rU^r\\
&+(c_l z+U^z)\partial_zU^r
-\frac{(U^\theta)^2}{r}+\partial_rP,
\end{aligned}
\]

\[
\begin{aligned}
0={}&(1-c_l)U^\theta
+(c_l r+U^r)\partial_rU^\theta\\
&+(c_l z+U^z)\partial_zU^\theta
+\frac{U^rU^\theta}{r},
\end{aligned}
\]

\[
\begin{aligned}
0={}&(1-c_l)U^z
+(c_l r+U^r)\partial_rU^z\\
&+(c_l z+U^z)\partial_zU^z+\partial_zP,
\end{aligned}
\]

with incompressibility

\[
\boxed{
\partial_rU^r+\frac{U^r}{r}+\partial_zU^z=0.
}
\]

Implement these primitive-variable equations as an independent residual and validation system.

The target profile must be:

- Nonzero and genuinely swirling.
- Globally \(C^2\) or smoother as a Cartesian vector field.
- Smooth across the entire rotation axis and the origin.
- Uniformly decaying at spatial infinity.
- Compatible with the full-space Euler pressure.
- Free of artificial singularities introduced by cylindrical coordinates.

Do not impose \(U^\theta=0\), \(U^z=0\), \(U(0)=0\), or reflection symmetry across \(z=0\) without mathematical justification.

Do not impose finite kinetic energy, exponential decay, compact support, or a zero boundary condition on a finite computational domain.

A profile discovery alone is not a proof of blowup from smooth finite-energy initial data.

---

## 2. Primary axisymmetric reduced formulation

The primary numerical formulation should use the axisymmetric Euler variables

\[
\Gamma=rU^\theta,\qquad
q=\frac{\Gamma}{r^2}=\frac{U^\theta}{r},
\]

\[
\eta=\frac{\Omega^\theta}{r},
\qquad
\Omega=\nabla\times U.
\]

Introduce the meridional stream potential \(\phi\) via

\[
\boxed{
-\Delta_5\phi=\eta,
}
\]

where

\[
\Delta_5=\partial_{rr}+\frac3r\partial_r+\partial_{zz}.
\]

Recover meridional velocity by

\[
\boxed{
U^r=-r\partial_z\phi,\qquad
U^z=2\phi+r\partial_r\phi.
}
\]

The swirl velocity is

\[
U^\theta=rq.
\]

Define the meridional similarity transport field

\[
W_m=(c_l r+U^r,\ c_l z+U^z).
\]

The reduced stationary system is

\[
\boxed{
q+W_m\cdot\nabla_{r,z}q
+2\frac{U^r}{r}q=0,
}
\]

\[
\boxed{
(1+c_l)\eta+W_m\cdot\nabla_{r,z}\eta
=\partial_z(q^2),
}
\]

\[
\boxed{
-\Delta_5\phi=\eta.
}
\]

Independently derive all three equations from the physical Euler system and the stated similarity ansatz.

Also verify the equivalent circulation equation

\[
(1-2c_l)\Gamma+W_m\cdot\nabla_{r,z}\Gamma=0.
\]

The identity \(\Gamma=r^2q\) must be preserved exactly in numerical evaluations.

### Axis regularity

A smooth axisymmetric Cartesian vector field has the local structure

\[
U^r=rA(r^2,z),\qquad
U^\theta=rB(r^2,z),\qquad
U^z=C(r^2,z),
\]

for smooth scalar functions \(A,B,C\).

Consequently, \(\phi,q,\eta\) should be regular functions of \(r^2\) and \(z\) near the axis.

In particular,

\[
\Gamma=r^2q
\]

vanishes quadratically at the axis, but \(q(0,z)\) is not required to vanish.

Similarly, \(\eta(0,z)\) may be nonzero.

Never evaluate \(U^r/r\), \(\Gamma/r^2\), or \(\Omega^\theta/r\) by a naive division near \(r=0\). Use analytic regular limits derived from the basis.

Implement an origin and axis Taylor audit, including at least quadratic consistency of the primitive and reduced equations.

### Independent formulations

Develop two complementary formulations:

**Formulation A — reduced transport/elliptic system**

Optimize \(q,\eta\), and reconstruct \(\phi\) using the full-space \(\Delta_5\) inverse.

**Formulation B — stream-potential/primitive system**

Represent \(\phi,q\) directly, compute \(\eta=-\Delta_5\phi\), and independently verify the original Euler momentum equation with reconstructed pressure.

Compare conditioning, accuracy, computational expense, and convergence.

Do not use the same differentiated residual routine for both independent validations.

---

## 3. Manufactured tests and consistency checks

Before expensive optimization, implement independently constructed manufactured fields.

Include smooth axisymmetric fields with nonzero swirl, for example using

\[
\phi=e^{-(r^2+z^2)}(1+a z),
\]

\[
q=e^{-(r^2+z^2)}(b+c z),
\]

for multiple nonzero choices of \(a,b,c\).

These are operator tests, not purported unforced Euler solutions.

Verify:

1. Exact divergence cancellation from the stream-potential representation.
2. The identity \(\Omega^\theta/r=-\Delta_5\phi\).
3. Equivalence of the \(q\)- and \(\Gamma\)-equations.
4. Cylindrical primitive momentum versus Cartesian momentum residuals.
5. Correct swirl curvature terms.
6. Axis and origin limits.
7. Pressure Poisson normalization and signs.
8. Numerical derivatives against symbolic or automatic differentiation.
9. Jacobian-vector products against independent directional finite differences.
10. Covariance under the exact spatial dilation symmetry.

Use float64 in all final residual calculations.

Check the actual dtype of arrays, transforms, derivatives, dot products, and reductions if JAX or another automatic-differentiation framework is used.

Do not proceed to large runs while any fundamental operator identity fails.

---

## 4. Far-field asymptotics: primary search class

Define spherical radius

\[
R=\sqrt{r^2+z^2},
\]

and polar angle \(\vartheta\) through

\[
r=R\sin\vartheta,\qquad z=R\cos\vartheta.
\]

Let

\[
\boxed{
\alpha=\frac{1-c_l}{c_l}.
}
\]

For the primary target \(1/2<c_l<3/4\),

\[
\frac13<\alpha<1.
\]

The expected leading far-field behavior is

\[
\boxed{
U_0=R^{-\alpha}F(\vartheta),
}
\]

\[
\Omega_0=O(R^{-1/c_l}).
\]

This is a search assumption, not a theorem applying to every decaying solution.

The angular vector field \(F\) has spherical components

\[
F=F_R e_R+F_\vartheta e_\vartheta+F_\theta e_\theta,
\]

where \(e_\theta\) denotes the azimuthal swirl direction.

The leading linear similarity equation is

\[
(1-c_l)U_0+c_l(y\cdot\nabla)U_0=0.
\]

The leading incompressibility condition is

\[
\boxed{
(2-\alpha)F_R+
\frac1{\sin\vartheta}
\partial_\vartheta(\sin\vartheta F_\vartheta)=0.
}
\]

The azimuthal component \(F_\theta\) is not fixed by this divergence condition.

It must, however, satisfy the regularity conditions at both poles.

### Convenient far-field potentials

One useful compatible representation is

\[
\phi_0=R^{-\alpha}A(\mu),
\qquad
q_0=R^{-(\alpha+1)}B(\mu),
\]

where

\[
\mu=\cos\vartheta.
\]

These imply

\[
F_R=2\mu A-(1-\mu^2)A',
\]

\[
F_\vartheta=(\alpha-2)\sin\vartheta\,A,
\]

\[
F_\theta=\sin\vartheta\,B.
\]

Here a prime on \(A\) denotes differentiation with respect to \(\mu\).

Verify these relations directly.

For the corresponding potential vorticity,

\[
\eta_0=R^{-(\alpha+2)}E(\mu),
\]

with

\[
E=-\left[
\alpha(\alpha-3)A+
(1-\mu^2)A''-4\mu A'
\right].
\]

Check this formula using the five-dimensional Laplacian.

The far-field angular coefficients \(A,B\) must be free optimization variables.

Do not freeze one chosen far-field pattern.

Use several substantially different initial angular profiles, including profiles with dominant poloidal and swirl contributions.

### Angular momentum at infinity

Since

\[
\Gamma=rU^\theta,
\]

the expected swirl tail satisfies

\[
\Gamma_0=
R^{1-\alpha}\sin^2\vartheta\,B(\mu).
\]

For \(c_l>1/2\), \(1-\alpha>0\).

Thus a nontrivial swirling velocity can decay even while its circulation variable \(\Gamma\) grows with radius.

Do not incorrectly impose \(\Gamma\to0\) at infinity.

Indeed, requiring a decaying \(\Gamma\) would eliminate important candidate profiles through the stationary circulation equation.

This distinction is essential.

---

## 5. First nonlinear far-field correction

Independently derive and test the first nonlinear correction.

Use the formal expansion

\[
U=R^{-\alpha}F
+R^{-(2\alpha+1)}G+\cdots,
\]

\[
P=R^{-2\alpha}Q+\cdots.
\]

The first nonlinear advection term has the form

\[
(U_0\cdot\nabla)U_0
=R^{-(2\alpha+1)}N(\vartheta).
\]

For axisymmetric spherical components,

\[
N_R=
-\alpha F_R^2
+F_\vartheta\partial_\vartheta F_R
-F_\vartheta^2-F_\theta^2,
\]

\[
N_\vartheta=
(1-\alpha)F_RF_\vartheta
+F_\vartheta\partial_\vartheta F_\vartheta
-\cot\vartheta F_\theta^2,
\]

\[
N_\theta=
(1-\alpha)F_RF_\theta
+F_\vartheta\partial_\vartheta F_\theta
+\cot\vartheta F_\vartheta F_\theta.
\]

Verify these formulas against Cartesian calculations.

The pressure coefficient should formally solve

\[
\boxed{
-\left[
2\alpha(2\alpha-1)+\Delta_{\mathbb S^2}
\right]Q
=
(1-2\alpha)N_R+
\frac1{\sin\vartheta}
\partial_\vartheta(\sin\vartheta N_\vartheta).
}
\]

The velocity correction is then

\[
G_R=N_R-2\alpha Q,
\]

\[
G_\vartheta=N_\vartheta+\partial_\vartheta Q,
\]

\[
G_\theta=N_\theta.
\]

It must satisfy

\[
(1-2\alpha)G_R+
\frac1{\sin\vartheta}
\partial_\vartheta(\sin\vartheta G_\vartheta)=0.
\]

These expressions are provided as formulas to verify, not unquestioned assumptions.

### Pressure resonances and global corrections

Pay special attention to the following issues.

1. The pressure operator has parameter-dependent spherical-harmonic eigenvalues.
2. At \(\alpha=1/2\), corresponding to \(c_l=2/3\), the degree-zero pressure operator is formally resonant.
3. Near \(c_l=1/2\), a degree-one pressure resonance may become relevant.
4. Global pressure multipoles can introduce corrections not captured by a purely local nonlinear expansion.
5. Logarithmic corrections may be necessary at resonant exponents.
6. Some apparent resonances may be eliminated by compatibility conditions or global cancellations.

Do not divide by a small angular-operator eigenvalue without checking the corresponding solvability condition.

Do not assume that the displayed expansion exhausts all possible far-field orders.

If necessary, recover the correct terms by matching to the full-space Poisson integral.

For every candidate, distinguish:

- Coefficients determined by local far-field equations.
- Coefficients determined by the global pressure.
- Free coefficients requiring matching to the inner solution.
- Coefficients that are inconsistent with the original Euler equations.

---

## 6. Numerical representation

Use a spectral representation tailored to axisymmetric geometry.

The primary unknowns may be either \((q,\eta)\) or \((\phi,q)\), with the complementary variables reconstructed exactly.

Near the origin, enforce smoothness using functions of \(r^2\) and \(z\), or a compatible solid-harmonic representation.

For the \(\Delta_5\) operator, consider a spectral basis adapted to its five-dimensional angular structure, including appropriate Gegenbauer functions.

Do not confuse the five-dimensional angular operator for \(\phi\) with the three-dimensional spherical Laplacian used for pressure.

Use:

- A regular inner region including the complete symmetry axis.
- Several radial spectral elements or mapped meridional domains.
- Explicit transition/matching regions.
- A factored far-field representation or carefully compactified exterior.

Factor the fractional power-law decay analytically.

Do not force an unfactored fractional-power endpoint to be analytic under compactification.

Do not assume even or odd \(z\)-parity in the primary search. Both parity classes must be represented.

Optional symmetry-restricted searches may be used as separate experiments, with their restrictions clearly documented.

### Global elliptic inverse

For \(-\Delta_5\phi=\eta\), use a globally consistent inverse with appropriate regularity and far-field behavior.

Compare a spectral elliptic solver against a separate integral/Green-function calculation on representative fields.

A small residual from the transport equations is meaningless if the Biot–Savart reconstruction uses an inconsistent outer boundary condition.

---

## 7. Full-space pressure reconstruction

The actual primitive Euler momentum equation must be checked independently.

Recover pressure from

\[
\boxed{
-\Delta P=
\sum_{i,j=1}^3
(\partial_iU_j)(\partial_jU_i).
}
\]

Use the full-space decaying pressure convention, up to an additive constant.

A radial spherical-harmonic Green-function approach is acceptable.

For the degree-\(\ell\) coefficient \(f_\ell(R)\) of the Poisson source,

\[
P_\ell(R)=\frac1{2\ell+1}
\left[
R^{-\ell-1}
\int_0^R s^{\ell+2}f_\ell(s)\,ds
+
R^\ell
\int_R^\infty s^{1-\ell}f_\ell(s)\,ds
\right].
\]

Verify this formula and its normalization independently.

Use the analytically resolved exterior to evaluate the integral to infinity.

Quantify truncation errors.

Cross-check selected pressure values and gradients using a separately implemented free-space calculation.

Do not impose \(P=0\) on an artificial finite outer sphere.

Do not add arbitrary harmonic pressure corrections to conceal an Euler momentum residual.

A candidate with a small reduced transport residual but a large primitive momentum residual is not acceptable.

---

## 8. Gauge fixing, scaling, and nontriviality

The stationary Euler profile equation has the exact dilation symmetry

\[
U_L(y)=L U(y/L),
\]

\[
P_L(y)=L^2P(y/L).
\]

It leaves \(c_l\) unchanged.

In reduced variables,

\[
\phi_L(y)=L\phi(y/L),
\]

\[
q_L(y)=q(y/L),
\]

\[
\eta_L(y)=L^{-1}\eta(y/L).
\]

Verify these transformations.

For the primary class with nonzero leading far-field coefficient, use a single dilation gauge such as

\[
\boxed{
\int_{\mathbb S^2}|F|^2\,dS=1.
}
\]

Under dilation, this integral scales by \(L^{2(\alpha+1)}\).

Do not impose a second independent core-size normalization and incorrectly call it another gauge.

In particular:

- Vorticity amplitude cannot be freely normalized by this dilation.
- \(DU(0)\) is invariant under this dilation.
- \(q(0)\) is invariant under this dilation.
- Translation of a core in \(z\) is not automatically a gauge preserving the chosen decaying profile class.

Only quotient exact, verified symmetries.

For the primary \(c_l>1/2\) search, track nonzero swirl in the core and far field.

Use diagnostics such as

\[
\frac{\|U^\theta\|_{\rm diagnostic}}
{\|U\|_{\rm diagnostic}}
\]

and corresponding shellwise quantities.

Do not let the optimizer converge silently to the zero field, a non-swirling field, or a tail disconnected from the interior.

Track the radial location and width of the active core and the radius at which the expected far-field asymptotics actually emerge.

---

## 9. Residuals, norms, and candidate ranking

Construct independently evaluated residuals

\[
R_q=q+W_m\cdot\nabla q
+2\frac{U^r}{r}q,
\]

\[
R_\eta=(1+c_l)\eta+
W_m\cdot\nabla\eta-\partial_z(q^2),
\]

\[
R_{\rm elliptic}=-\Delta_5\phi-\eta,
\]

together with the original radial, swirl, and axial momentum residuals and the divergence residual.

Use all of the following:

1. Absolute residual norms.
2. Per-term relative residual norms.
3. Shellwise RMS residuals.
4. Maximum pointwise residuals.
5. Independent holdout-grid residuals.
6. Origin and axis Taylor residuals.
7. Full-space pressure consistency residuals.
8. Far-field asymptotic coefficient residuals.

For physical three-dimensional volume integrals, use the correct axisymmetric measure

\[
dV=2\pi r\,dr\,dz.
\]

However, do not allow the volume weight to hide large errors near the symmetry axis.

Use separate axis-collar diagnostics and balanced shell objectives.

For far-field matching, assess at least the scaled residuals

\[
R^{2\alpha+1}R_U,
\qquad
R^{2\alpha+2}R_q,
\qquad
R^{2\alpha+3}R_\eta,
\]

when the assumed first nonlinear correction applies.

These are especially important because the leading homogeneous tail cancels the leading similarity operator automatically.

A far-field loss can become numerically small without the nonlinear correction or pressure matching being correct.

Do not rank candidates solely by an average training loss or a relative residual with an artificially enlarged denominator.

Test sensitivity to dilation, matching radius, radial-shell weights, and quadrature resolution.

---

## 10. Hardware and optimization strategy

Inspect the real hardware allocation, GPU memory, CPU cores, available RAM, disk space, and existing jobs.

Test one A100 GPU first using a representative small workload.

If float64 performance and memory use are satisfactory, use the allocated GPUs for parallel independent starting points.

Because the axisymmetric problem is effectively two-dimensional, independent multi-start optimization may be more efficient than distributing one moderate-size problem over eight GPUs.

Use multicore CPUs for:

- Spectral transforms and integration.
- Elliptic solves and preconditioners.
- Full-space pressure reconstruction.
- Independent residual evaluations.
- Checkpoint verification and analysis.

Avoid BLAS/OpenMP oversubscription.

Start with low- to moderate-resolution spectral representations.

Increase angular and radial resolution only when the candidates justify it.

Compare at least two optimization algorithms, such as trust-region Gauss–Newton and L-BFGS or Newton–Krylov.

Use matrix-free Jacobian-vector products where beneficial.

Do not construct unnecessarily large dense Jacobians.

### Parameter search

Begin with fixed-\(c_l\) experiments using values such as

\[
c_l\in
\{0.505,0.525,0.56,0.60,0.64,0.68,0.72,0.74\}.
\]

Treat \(c_l=1/2\) as a separate critical experiment.

After obtaining stable low-resolution branches, free \(c_l\) and optimize it jointly with the field coefficients.

Do not artificially force \(c_l\) toward a chosen target value.

Pay particular attention to parameter behavior near \(c_l=1/2\) and \(c_l=2/3\).

Use many unrelated initializations, including:

- Different smooth meridional cores.
- Different swirl distributions.
- Mixed poloidal and swirl angular coefficients.
- Different effective core scales before gauge fixing.
- Different distributions of vorticity and helicity.
- Symmetric and asymmetric \(z\)-dependencies.
- Random spectral coefficients with controlled amplitudes.
- Candidates from alternative numerical methods.

Do not rely exclusively on perturbations of a single initial field.

---

# STAGE I — Hours 0–7

## Mathematical audit, tested implementation, and broad discovery

Complete the initial theorem audit and exact-operator tests.

Build the primary reduced solver and an independently implemented primitive momentum validator.

Establish a working full-space elliptic inversion and pressure calculation at pilot resolution.

Launch a broad parameter and initialization sweep as soon as the operators pass their tests.

Use the first GPU for correctness testing, then distribute independent search jobs over available hardware.

Aim for approximately 30–100 distinct inexpensive initializations if measured throughput permits.

Prioritize diversity and meaningful independent refinement over meeting a nominal number of starts.

Test spectral truncation and dealiasing with independent quadrature resolutions.

Start work on the second numerical representation during this stage, not after discovery is complete.

### Stage-I deliverables

By hour 7, produce:

- A tested numerical solver.
- Reproducible operator tests.
- The mathematical obstruction audit.
- A completed or running parameter sweep.
- A candidate leaderboard.
- At least one functioning independent validation route.
- A list of the most promising distinct candidate branches.

Every candidate must be accompanied by quantitative residuals and axis/far-field diagnostics.

If nothing is promising, document the causes and use Stage II to change the representation, initialization strategy, or parameter range.

Do not terminate the campaign merely because the first optimization attempts fail.

---

# STAGE II — Hours 7–18

## Refinement, free-parameter continuation, and matching

Select approximately 3–6 structurally different candidate branches.

Increase angular resolution, radial resolution, nonlinear quadrature accuracy, and exterior integration accuracy.

Use at least three meaningful resolution levels for serious candidates, if computationally feasible.

Refine with an appropriate Newton–Krylov, trust-region, or large-scale least-squares method.

Allow \(c_l\) to vary.

Record how the field and exponent respond to continuation.

Test whether any branch approaches:

- \(c_l=1/2\).
- \(c_l=2/3\).
- The upper end of the explored parameter range.
- Vanishing swirl.
- A singular axis or origin.
- A core escaping to large radii.
- Increasingly oscillatory spectral coefficients.
- Unbounded derivatives.

These are important diagnostics, not successful solutions.

### Infinity and pressure

Compare at least two outer-domain treatments.

Substantially vary the matching radius, including factor-of-two changes where feasible.

Verify convergence of

\[
R^\alpha U(R,\vartheta)
\]

toward a nonzero angular profile.

Also test the corresponding derivatives, vorticity, and swirl asymptotics.

Subtract the leading term and investigate the first nonlinear correction.

Do not automatically fit every discrepancy to the predicted power.

Check whether the difference is due to pressure multipoles, resonance, inadequate resolution, or a wrong asymptotic ansatz.

For each surviving candidate, recover the full-space pressure and evaluate the original Euler momentum equation.

Use untouched holdout grids covering the core, symmetry axis, matching zones, and far exterior.

Candidates must be ranked using independent evaluation, not training loss alone.

### Stage-II deliverables

By hour 18, provide either:

- A small set of refinement-stable candidates with complete diagnostics; or
- A quantitative failure map specifying why the tested search classes have not converged.

Do not consume the final six hours by continuing the same unproductive optimization.

---

# STAGE III — Hours 18–24

## Independent and adversarial validation

The purpose of Stage III is to actively find reasons why apparently good numerical candidates might be invalid.

### 1. Independent discretization

Reconstruct leading candidates in a numerically independent representation.

Use different differentiation, quadrature, and elliptic or pressure reconstruction routines.

Compare CPU and GPU computations.

Check selected points using Cartesian finite differences with a step-size convergence study.

Use higher precision for cancellation-sensitive test cases when feasible.

A common residual routine used by two solvers is not an independent verification.

### 2. Exact identities

Verify the stationary circulation equation

\[
(1-2c_l)\Gamma+W_m\cdot\nabla\Gamma=0
\]

and its characteristic evolution along selected meridional trajectories.

Check the reduced potential-vorticity equation.

For the full Euler profile, independently derive and test the energy-flux identity

\[
\boxed{
(5c_l-2)
\int_{B_R}\frac{|U|^2}{2}\,dy
=
\int_{\partial B_R}
\left[
\left(\frac{|U|^2}{2}+P\right)U\cdot n
+c_lR\frac{|U|^2}{2}
\right]\,dS.
}
\]

For the leading tail, verify the predicted energy growth

\[
\int_{B_R}|U|^2\,dy
\sim R^{5-2/c_l},
\]

including its angular coefficient.

This quantity is generally divergent as \(R\to\infty\) in the proposed search range.

Do not falsely impose global finite kinetic energy.

Inspect local helicity balances with their boundary fluxes. Do not invoke a whole-space helicity identity unless the required integrability and boundary decay have been independently verified.

Also check the vorticity maximum condition: at a nonzero global maximum of \(|\Omega|\), a smooth decaying exact profile must satisfy

\[
\Omega\cdot\operatorname{sym}(DU)\Omega
=|\Omega|^2.
\]

Verify the assumptions under which this identity is used.

### 3. Axis and origin regularity

Evaluate reconstructed Cartesian fields directly across the rotation axis.

Check the Taylor coefficients of \(U^r,U^\theta,U^z\), \(q,\eta,\phi\).

Look for hidden singularities arising from cancellation of individually singular cylindrical expressions.

Check Cartesian derivatives and the smoothness of the velocity vector, not merely its cylindrical component values.

### 4. Robustness tests

Perturb candidate coefficients and re-optimize from nearby initializations.

Change:

- Spectral resolution.
- Quadrature density.
- Radial coordinate mappings.
- Core/exterior matching radii.
- Far-field truncation orders.
- Pressure reconstruction accuracy.
- Numerical weights.
- Optional parity restrictions.
- Initial conditions and optimizer settings.

Compare reconstructed fields after applying only verified gauge transformations.

Search deliberately for residual peaks between collocation nodes, narrow spikes, unresolved oscillations, and core/tail escape.

If a candidate fails, report the precise quantitative defect rather than merely marking it unsuccessful.

### 5. Final theoretical compatibility

Recheck the hypotheses of relevant axisymmetric Euler theorems.

In particular, distinguish:

- Smooth full-space solutions.
- Solutions with boundaries.
- Solutions lacking \(C^2\) regularity.
- Anisotropically self-similar solutions.
- Locally self-similar solutions.
- Globally exact stationary similarity profiles.

A numerical candidate contradicting a proved theorem must be audited carefully before being described as evidence against that theorem.

---

## 11. Acceptance criteria

Pre-register numerical acceptance thresholds before ranking the final candidates.

Suggested targets are:

- Weighted and per-term relative RMS residuals of approximately \(10^{-6}\) or smaller.
- Clear improvement across at least three meaningful refinement levels.
- No unexplained large maximum pointwise residual.
- Stable nonzero swirl in the resolved profile.
- Stable origin and axis regularity diagnostics.
- Stable nonzero far-field angular coefficients.
- Consistent full-space pressure reconstruction.
- Independent agreement of reduced and primitive Euler residuals.
- Stable \(c_l\) under refinement, within measured uncertainty.
- No evidence that the core or tail escapes the computational region.

Aim substantially lower if convergence permits.

Do not relax thresholds simply because one candidate is appealing.

If none of the candidates achieves the targets, report their best independently measured errors anyway.

Use four final outcome labels:

**A. Strong numerical candidate**

A nontrivial profile survives independent residual evaluation, regularity checks, full-space pressure matching, and refinement.

This is not a mathematical existence proof.

**B. Promising but unresolved**

The candidate has meaningful structure or convergence evidence, but significant errors or unresolved asymptotic issues remain.

Quantify each defect.

**C. Unsuccessful numerical search**

No reliable candidate was obtained.

State the explored parameter range, initializations, resolutions, computational budget, and failure mechanisms.

Numerical failure is not a proof of nonexistence.

**D. Rigorous mathematical obstruction**

Use this category only when a complete mathematical argument excludes a clearly stated function class.

The known \(c_l<1/2\) axisymmetric obstruction may be reported separately from the main \(c_l>1/2\) numerical search.

---

## 12. Persistent execution and recovery

Implement a durable campaign supervisor or use the available job scheduler.

Support:

- Independent job queues.
- GPU assignment and CPU affinity.
- Bounded retries.
- Logs and heartbeats.
- Atomic checkpoints.
- Resume from an interrupted optimizer.
- Saved random seeds.
- Exact coefficient and basis specifications.
- Environment and hardware records.
- Immutable accepted checkpoints.

Checkpoint at least every 15 minutes and after each accepted major improvement.

Test interruption and resume on a disposable job before relying on this system.

Do not assume that an interactive AI conversation remains alive for 24 hours.

Use a real scheduler or durable process supervisor if continued execution across sessions is necessary.

Never fabricate elapsed time, iteration counts, GPU usage, completed jobs, or independently verified residuals.

At the end of the authorized 24-hour budget, checkpoint and terminate only the jobs belonging to this campaign unless continued execution is explicitly authorized.

---

## 13. Required final deliverables

Create a reproducible project containing at least:

- `START_HERE.md`
- `MATHEMATICAL_FORMULATION.md`
- `AXISYMMETRIC_OBSTRUCTION_AUDIT.md`
- `ORIGIN_AND_AXIS_REGULARITY.md`
- `FAR_FIELD_ANALYSIS.md`
- `FULL_SPACE_PRESSURE.md`
- `NUMERICAL_METHODS.md`
- `PARAMETER_SWEEP.csv`
- `CANDIDATE_LEADERBOARD.csv`
- `INDEPENDENT_VALIDATION.md`
- `FAILURE_ANALYSIS.md`
- `FINAL_REPORT.md`
- `RUNBOOK.md`

Also preserve:

- Executable solver and validation scripts.
- Automated operator tests.
- Environment lock files.
- Hardware inventory.
- Optimizer configurations.
- Actual checkpoints and accepted candidate coefficients.
- A hash/integrity manifest.
- Tested commands for launching, monitoring, resuming, and independently validating a saved candidate.

The final report must give actual elapsed time and resource utilization, not planned values.

For every serious candidate, include:

\[
c_l,\quad \alpha,\quad
\text{basis size},\quad
\text{RMS residual},\quad
\text{maximum residual}.
\]

Also report swirl strength, core size, convergence rates, far-field coefficients, pressure errors, and origin/axis regularity measurements.

Include quantitative plots of:

- Residual versus spectral resolution.
- Residual versus spatial radius.
- Spectral coefficient decay.
- Swirl and poloidal field distributions.
- \(c_l\) continuation.
- Far-field convergence.
- Energy flux identity errors.
- Axis and origin residuals.

Produce a single-command independent validation of the best saved candidate without rerunning the optimization.

Produce a single-command resume procedure and test it from a clean process.

If no candidate survives, the final report must clearly identify the most promising next numerical experiment.

---

## 14. References

Check these sources for relevant mathematical restrictions, numerical methods, and axisymmetric Euler formulations.

**[R1]** Peter Constantin, Mihaela Ignatova, Vlad Vicol, *On putative self-similarity for incompressible 3D Euler* (2026).  
https://arxiv.org/abs/2602.17570

**[R2]** Guo Luo and Thomas Y. Hou, *Toward the Finite-Time Blowup of the 3D Axisymmetric Euler Equations: A Numerical Investigation*.  
https://doi.org/10.1137/140966411

**[R3]** Jiajie Chen and Thomas Y. Hou, *Stable Nearly Self-Similar Blowup of the 2D Boussinesq and 3D Euler Equations with Smooth Data II: Rigorous Numerics*.  
https://doi.org/10.1137/23M1580395

**[R4]** PETSc nonlinear solver documentation.  
https://petsc.org/release/manual/snes/

**[R5]** JAX float64 configuration documentation.  
https://docs.jax.dev/en/latest/101/default_dtypes.html

Use the references to check assumptions, implementation choices, and known limitations. Do not transfer bounded-domain results directly to whole-space profiles without verifying the differences.

---

## FINAL EXECUTION INSTRUCTION

Begin immediately with the mathematical feasibility audit, hardware inventory, and operator tests.

Then execute Stage I, Stage II, and Stage III under the strict 24-hour actual wall-clock budget.

The highest-priority scientific question is:

**Does there exist convincing numerical evidence for a nontrivial, globally smooth, globally decaying, axisymmetric self-similar Euler profile with nonzero swirl and \(c_l>1/2\)?**

A closely related secondary question is whether a meaningful profile exists at the critical exponent \(c_l=1/2\).

Do not conceal nonconvergence, pressure inconsistencies, singularity indicators, or failures of far-field matching.

Do not manufacture a candidate by imposing incompatible boundary data.

Do not interpret a small collocation loss as evidence of an exact global solution without independent verification.

Use the allocated computational resources productively, preserve reproducibility, and produce the strongest scientifically defensible conclusion supported by the completed experiments.

**The deliverable is an executed, reproducible, independently audited 24-hour numerical investigation—not merely code, a proposed method, or a low training loss.**