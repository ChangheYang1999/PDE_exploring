# S1 — 18-Hour Rigorous Theory Research for the Full-Plane IPM Self-Similar Profile (case4)

## 0. Mission and nonnegotiable rules

This is an 18-hour mathematical research task aimed at obtaining a rigorous a posteriori existence theorem for a numerical self-similar IPM profile.

The numerical project is located at:

`~/Changhe/IPM/case4`

If this path does not exist, resolve `Changhe/IPM/case4` from the actual user home or project root. Do not silently substitute a different project.

**The original directory is strictly read-only.**

Before starting experiments:

1. Inspect the original directory sufficiently to identify the project and its data.
2. Create a completely separate research directory, for example `~/Changhe/IPM_theory_runs/S1_case4_18h_<timestamp>`.
3. Copy the ENTIRE `case4` directory into that research directory, preserving the files and directory structure.
4. Perform all analysis, calculations, code modifications, scratch work and verification in the copied directory or its surrounding research workspace.
5. Never modify, overwrite, regenerate caches inside, or commit changes to the original `case4`.
6. Audit symlinks, absolute file paths and output paths to ensure that experiments cannot write back into the original directory.

You may freely create new proof scripts, high-precision calculations, interval-arithmetic verifiers and experiment directories inside the copied workspace.

The original numerical data should be treated as reference evidence, not as an already certified proof.

### Overall objective

Obtain the strongest possible mathematically rigorous estimates for the full linearized operator around the S1 numerical profile, and use them to establish a genuine nonlinear a posteriori existence theorem if possible.

The research has **three main theoretical components**:

1. \(L^2\)-based / weighted \(H^{-1}\)-based estimates.
2. \(C^\alpha\)-based estimates directly for \(h\), preferably without estimating \(h_x\) in \(C^\alpha\).
3. Control of the singular functional \(c[h]\), using a local transport-adapted weighted estimate and finite-rank reduction.

These three components must ultimately fit into one compatible functional-analytic framework.

Numerical verification is allowed and encouraged. But any final existence claim must be supported by rigorous estimates, not floating-point evidence alone.

Do not assume that our proposed methods work. Investigate them critically, improve them or prove precise obstructions.

The fourth, independent finite-basis inverse certification program belongs to S2, not to this S1 task.

## 1. Recover the exact numerical and mathematical setting

We study the full-plane stationary self-similar IPM equation

\[
F(\rho):=(c_lX+U[\rho])\cdot\nabla\rho-\rho=0,
\qquad X=(x,y)\in\mathbb R^2,
\]

where

\[
U[\rho]=(-\psi_y,\psi_x),
\qquad -\Delta\psi=\partial_x\rho.
\]

The canonical full-plane inverse must be fixed by the actual growth, parity and boundary conditions of the project, with no unprescribed harmonic velocity.

The intended symmetry is

\[
\rho(-x,y)=\rho(x,y),\qquad
\rho(x,-y)=-\rho(x,y).
\]

The numerical solution in `case4` is the **S1, y-leading branch**, not the \(x^2y\)-leading X3 branch.

Its expected behavior near the origin is

\[
\bar\rho(x,y)=a_0y+O(r^3),
\]

with reference numerical values approximately

\[
c_l\simeq1.8085384,\qquad
a_0\simeq10.2975749.
\]

These values are orientation only. Recover the latest accepted numerical state, full coefficients, residual, exponent, normalization and uncertainties directly from `case4`. Do not silently use outdated values.

The origin compatibility relation is expected to be

\[
c_l+c[\rho]=1,
\qquad c[\rho]=\psi_{xy}[\rho](0).
\]

Verify this identity from the stationary equation and the actual normalization convention.

If \(c_l\) is determined by the profile, the full linearization must include its variation.

For the expected normalization,

\[
\delta c_l=-c[h].
\]

Thus, at a background \(\bar\rho\), the full linearized operator should be checked against

\[
\mathcal Lh
=
(\bar c_lX+U[\bar\rho])\cdot\nabla h-h
+
\bigl(U[h]-c[h]X\bigr)\cdot\nabla\bar\rho.
\]

Re-derive the operator independently, verify every sign, and distinguish it from the fixed-\(c_l\) linearization.

The approximate numerical background may not be exactly stationary. Track all residual-dependent errors rather than using exact-solution identities without qualification.

### Scaling freedom

The equation is invariant under

\[
\rho_\lambda(X)=\lambda\rho(X/\lambda).
\]

Since the leading term is \(a_0y\), this transformation does not change \(a_0\).

Consequently, the origin coefficient \(a_0\) does NOT eliminate the scaling freedom.

The infinitesimal scaling direction is

\[
K=\rho-X\cdot\nabla\rho.
\]

At an exact profile,

\[
\mathcal LK=0,
\]

provided \(K\) belongs to the chosen domain and the normalization-dependent linearization is correctly included.

We must impose one additional scaling normalization. A natural candidate is a condition on the leading far-field angular profile.

Verify that this condition is continuous in the selected function space and transverse to the scaling direction. Do not merely impose it formally.

## 2. The desired full estimate

Let

\[
\bar\rho=\text{numerical approximation},\qquad
\rho=\bar\rho+h.
\]

We seek an estimate of the form

\[
\boxed{
\|h\|_{X_{\rm low}}
+
\|h\|_{X_\alpha}
+
\mathfrak M[h]
+
|c[h]|
\le
C_{\rm inv}\|\mathcal Lh\|_Y,
}
\]

after appropriate normalization and treatment of the far-field parameters.

Here:

- \(X_{\rm low}\) is an \(L^2\)-based or negative-Sobolev correction space.
- \(X_\alpha\) controls \(h\) itself in a suitable \(C^\alpha\) norm.
- \(\mathfrak M[h]\) is a local singular weighted moment used to control \(c[h]\).
- \(Y\) is the correct forcing space, potentially with high- and low-regularity components.

The displayed estimate is a TARGET, not an assumed theorem.

It may require an augmented inverse with finitely or infinitely many explicit tail coordinates, or a two-norm/tame formulation.

If the estimate is impossible, identify the precise counterexample or functional-analytic obstruction and propose a mathematically consistent replacement.

Ultimately, derive explicit nonlinear closure conditions and check them against the accepted numerical residual.

## 3. Research Avenue I — \(L^2\)-based estimates

### 3.1. Begin with the negative-order energy

Investigate

\[
-\Delta\Phi=h,\qquad
E(h)=\|\nabla\Phi\|_{L^2(\mathbb R^2)}.
\]

Carefully establish when the inverse and pairing are well-defined in the selected spaces.

Derive from first principles the exact quadratic form obtained by testing the linearized equation against \(\Phi\).

In earlier exploratory work, this led to a matrix involving the background velocity gradient and background density gradient, with favorable positivity at the origin for S1.

Re-derive the matrix and its coefficients independently. Do not assume an earlier formula is automatically correct.

At the origin, determine the exact coercivity margin using the numerical values, including their uncertainties.

Then ask whether this favorable local structure survives globally.

### 3.2. Far-field obstruction

Ordinary unweighted \(\dot H^{-1}\) may fail because the numerical self-similar profile and its residual have nonintegrable far-field behavior.

Study the asymptotic expansion

\[
\rho(r,\theta)\sim
\sum_{n\ge1}r^{p_n(c_l)}\Theta_{n-1}(\theta),
\qquad
p_n(c_l)=\frac{n}{c_l}-(n-1).
\]

The current theory project has considered subtracting approximately six asymptotic orders.

Check the actual expansion, its logarithmic resonances, the angular equations, and its numerical accuracy from the `case4` data.

Crucially, the numerical exponents are not exact.

If \(c_l\) varies,

\[
\partial_{c_l}r^{p_n(c_l)}
=
-\frac{n}{c_l^2}r^{p_n(c_l)}\log r.
\]

These logarithmic variations must be included.

The leading angular profile \(\Theta_0\) may also vary. It is generally a function, not a single scalar.

Do not assume these variations lie in the ordinary remainder space.

### 3.3. Compare two possible methods

**Method A: explicit far-field subtraction.**

Write

\[
\rho=\rho_{\rm asym}(c_l,\Theta_0)+h,
\]

with enough asymptotic orders that \(h\) has a meaningful negative-order energy.

Determine the minimum subtraction order, exact far-field normalization, remainder space and derivative bounds required.

**Method B: weighted negative-order energy.**

Consider, for example,

\[
w_s(r)=\left(1+\frac{r^2}{R_0^2}\right)^{-s/2},
\qquad
g=w_sh,
\qquad
E_s(h)=\|\nabla(-\Delta)^{-1}g\|_2.
\]

Derive the exact weighted energy identity, including:

- Derivatives of the weight.
- Variable transport coefficients.
- Nonlocal commutators.
- The contribution of \(c[h]\).
- Variations of \(c_l\) and \(\Theta_0\).

Do not discard any indefinite commutator or cross term.

A previously considered heuristic exponent window is

\[
1+\frac2{c_l}<s<2+\frac1{c_l},
\]

but its applicability depends on the asymptotic variable being estimated.

Verify rather than assume this window. In particular, check the failure of weighted integrability for freely varying leading \(r^{1/c_l}\Theta_0\).

### 3.4. Main targets

Seek an explicit positive bound

\[
E_{\rm low}(h)
\le
K_{\rm low}\|\mathcal Lh\|_{Y_{\rm low}},
\]

possibly after tail and scaling constraints.

Numerically certify any background-dependent quadratic-form positivity or finite-dimensional spectral inequality needed.

If pure coercivity fails globally, investigate:

- Localized positive energies and complementary estimates.
- Adapted weights.
- Analytic treatment of far-field modes.
- Compact/finite-rank correction methods with proven bounds.
- Suitable negative-order spaces or anisotropic alternatives.

Do not infer surjectivity from coercivity alone.

At the end of this avenue, provide a theorem or a precise conditional theorem with explicit verification tasks.

## 4. Research Avenue II — \(C^\alpha\) estimates directly for \(h\)

This is a central priority.

**Do not make \([h_x]_{C^\alpha}\) the main unknown.**

The target is an estimate for \(h\) itself:

\[
[h]_{C^\alpha_w}
\le
C_\alpha\left(
\|\mathcal Lh\|_{Y_\alpha}
+
\text{already controlled lower-order quantities}
\right).
\]

Here \(C^\alpha_w\) may be an adapted weighted Hölder space, whose definition must be justified.

The operator \(U[h]\) is order zero. Use the exact second-order Riesz transform representation

\[
U[h]=(-R_1R_2h,R_1^2h),
\qquad
R_j=\partial_j(-\Delta)^{-1/2}.
\]

Also use, if advantageous,

\[
T_{xx}=R_1^2+\frac12I,\qquad
T_{xy}=R_1R_2.
\]

### 4.1. Analyze the frozen origin operator

For the expected S1 center data,

\[
DV(0)=\operatorname{diag}(\lambda,1),
\qquad
\lambda=2c_l-1,
\]

and \(\nabla\bar\rho(0)=(0,a_0)\).

The principal coupled frozen operator is

\[
\boxed{
L_0h=
\lambda x\partial_xh
+y\partial_yh
-h+a_0R_1^2h.
}
\]

Verify the formula, including the scaling variation.

Study the complete operator, not merely its transport term.

The multiplier of \(R_1^2\) is nonpositive:

\[
\widehat{R_1^2h}(\xi)
=
-\frac{\xi_1^2}{|\xi|^2}\widehat h(\xi).
\]

Simple absolute-value Schauder estimates lose this structure and may be far too expensive when \(a_0\) is large.

Investigate the exact conjugation identity with

\[
\sigma=\frac{a_0}{\lambda-1},
\]

of the form

\[
\Lambda^\sigma L_0
=
(\lambda x\partial_x+y\partial_y+\sigma-1)\Lambda^\sigma,
\]

on an appropriate domain.

Check its validity and determine whether it yields a useful same-order \(C^\alpha\), Hölder–Zygmund or Besov estimate.

Do not assume the conjugation preserves the desired Hölder space.

Determine:

1. Whether a bounded inverse exists in the chosen Hölder realization.
2. Which boundary, center and far-field conditions are required.
3. Whether a small \(\alpha>0\) is possible.
4. Whether regularity loss or logarithmic effects are unavoidable.
5. The sharpest explicit inverse constant you can derive.

A rigorous obstruction to a same-order inverse is an acceptable research finding, but it must be proved and accompanied by a proposed alternative.

### 4.2. Keep the Riesz cancellation

Investigate sharp and near-sharp bounds for the relevant second-order Riesz operators, particularly

\[
T_{xx},\qquad T_{xy},\qquad R_1^2.
\]

Do not merely multiply the independent \(C^\alpha\) norms of two first-order Riesz transforms.

Their composition must be analyzed at the multiplier or singular-kernel level.

The special relation to the Beurling transform may be useful.

However, do not turn this task into a detached study of optimal Riesz constants if it does not advance the inverse estimate.

Use the complete coupled operator whenever it gives stronger estimates than individual operator norms.

Track all local identity terms, especially the \(-\frac12I\) in \(R_1^2\).

### 4.3. Variable coefficients, origin and far field

Near the origin,

\[
\bar\rho_y-a_0=O(r^2),\qquad
\bar\rho_x=O(r^2)
\]

under the expected smooth expansion.

Verify these rates and constants from the numerical data.

Establish a perturbative localized Hölder estimate with explicit smallness.

Then extend it through the intermediate region and infinity.

Use the \(L^2\)-based estimate from Avenue I to control acceptable low-frequency or low-order remainders.

Identify any needed Schauder commutators and their optimized constants.

Treat the center \(y\)-jet separately where necessary.

The local mode \(y\) is neutral for the frozen transport operator; do not assume its coefficient is controlled by a low-order Hölder seminorm.

The scaling mode must also be handled by the phase condition.

### 4.4. Nonlinearity and derivative loss

The nonlinear correction contains

\[
U[h]\cdot\nabla h.
\]

A \(C^\alpha\) bound for \(h\) alone does not directly bound \(\nabla h\).

Do not hide this derivative loss by treating the quadratic transport term as an ordinary \(C^\alpha\) forcing.

Investigate a characteristic-based, tame, high/low norm or two-norm iteration that is compatible with the previous estimates.

The current priority is still a strong linear estimate for \(h\), not a separate sharp estimate for \(h_x\).

## 5. Research Avenue III — Singular functional \(c[h]\)

We must control

\[
c[h]=\psi_{xy}[h](0).
\]

On the full plane with the appropriate parity, the expected kernel representation is

\[
c[h]
=
\frac1\pi\int_{\mathbb R^2}
\frac{\sin3\theta}{r^3}h(X)\,dX,
\]

with the correct principal-value/renormalized interpretation when needed.

Verify the representation and the normalization from the canonical inverse.

The equivalent half-plane formula has a different factor. Do not confuse them.

A previous theoretical note proposed a two-step method:

1. Split \(c[h]\) into a regular far contribution and a singular near-origin contribution.
2. Control the singular contribution by a local transport-adapted weighted \(L^p\) estimate, using a nonnegative adjoint weight.
3. Use the resulting \(c[h]\) estimate to include its rank-one contribution in a finite-dimensional reduction.

That note analyzed a different local model,

\[
B_\beta=(x/2,\beta y),
\]

with density vanishing like \(x^2\).

**Do not copy that model into S1.**

Here the origin dynamics and leading density are different.

### 5.1. The crucial y-leading difficulty

For S1,

\[
h\sim b_0y+\text{higher-order terms}
\]

may be allowed.

A naïve moment

\[
\int\frac{|h|^p}{r^{3p}}
\]

can diverge even when the singular functional \(c[h]\) is well-defined by cancellation.

Therefore:

- Analyze the angular cancellation of the leading \(y\)-jet.
- Consider an exact subtraction \(h-b_0y\), with appropriate localization and tail correction.
- Determine whether \(c[h]\) can be expressed in terms of a renormalized remainder.
- Do not assume \(h\) has three derivatives merely because the numerical profile is smooth.
- If a jet coefficient must be an independent variable, include it explicitly in the Banach-space realization.

Derive a new weighted \(L^p\) moment adapted to the actual allowed vanishing and parity.

### 5.2. Adjoint transport estimate

Use the S1 frozen field

\[
B_0=(\lambda x,y),
\qquad \lambda=2c_l-1,
\]

rather than the previous \((x/2,\beta y)\) model.

Construct a characteristic-adapted local region and an adjoint weight.

Derive the exact weighted identity, including all boundary fluxes.

Determine the admissible \(p\), the optimal coercive coefficient and explicit constants.

Restore the variable-coefficient and nonlocal terms.

In particular, exploit the leading cancellation

\[
\bigl(U[h]-c[h]X\bigr)
\cdot\nabla(a_0y)=0
\]

at leading order.

The actual quantitative objective is an estimate such as

\[
|c[h]|
\le C_c\left(
\|\mathcal Lh\|_Y
+
\|h\|_{X_{\rm low}}
+
\|h\|_{X_\alpha}
\right),
\]

or a stronger augmented-space estimate.

Try to obtain a strictly positive explicit absorption gap.

Do not assume Taylor remainders are small until their constants and rates have been justified.

### 5.3. Finite-rank reduction

Once the singular functional is controlled, analyze the exponent variation and any other finite-dimensional constraints.

If

\[
\mathcal A=\mathcal L_1+\mathcal L_2,
\]

where \(\mathcal L_2\) is finite rank, derive the exact Schur complement or finite matrix.

For a representation

\[
\mathcal L_2h=\sum_{j=0}^M\ell_j(h)g_j,
\]

the relevant matrix is

\[
M_{ij}=\delta_{ij}+\ell_i(\mathcal L_1^{-1}g_j).
\]

Do not assume \(\mathcal L_1^{-1}\) already exists.

Prove its existence in the same function-space realization or state precisely what remains conditional.

Numerically certify finite-matrix invertibility only after the functionals, inverse images and truncation errors are rigorously defined.

## 6. Combine all three estimates

The three parts must be compatible.

Do not prove separate estimates in incompatible spaces and then claim that they close.

Construct a complete functional-analytic formulation including:

- Correction \(h\).
- The S1 scaling phase.
- The leading far angular profile and its allowed perturbations.
- Variations of \(c_l\).
- Any necessary center jet coordinates.
- Weighted low norm.
- Weighted Hölder norm.
- Singular functional \(c[h]\).

Write the full nonlinear correction equation, and derive explicit sufficient conditions for existence.

A possible target is a two-norm theorem involving

\[
K_H,\quad K_L,\quad C_B,\quad C_V,\quad \eta,
\]

with conditions of the form

\[
K_H\eta\le r,\qquad
K_LC_BK_H\eta<1,\qquad
C_Vr\le r_V.
\]

These are only schematic until the norms, solution operator and nonlinear mapping estimates are proved.

You may use an alternative rigorous fixed-point, implicit-function or Nash–Moser mechanism if more suitable.

Verify injectivity and surjectivity, not merely an energy inequality.

### Numerical verification

Use the copied `case4` data to verify quantities such as:

- Far-field exponents and their errors.
- Angular-profile normalization and phase transversality.
- Pointwise or integral coefficient bounds.
- Local frozen inverse constants.
- Weighted energy positivity.
- Hölder perturbation constants.
- Singular functional bounds.
- Residual norms in the actual forcing spaces.
- Finite-dimensional normalization matrices.

Use high precision or interval arithmetic whenever a calculation will enter a theorem.

Separate clearly:

- Rigorous analytical inequalities.
- Certified numerical inequalities.
- Floating-point diagnostics.
- Unverified assumptions.

Do not promote a numerical observation into a proof.

## 7. Time budget: 18 hours

This S1 task is intended to run concurrently with the S2 task, under a shared 18-hour wall-clock research window.

Use the available window productively; do not stop simply because an initial estimate has been found.

Suggested phases:

- Hours 0–2: copy the project, audit numerical data, reconstruct the exact operator and normalization.
- Hours 2–6: weighted \(L^2/H^{-1}\) and far-field theory.
- Hours 6–10: rigorous \(C^\alpha(h)\) analysis, especially the complete frozen coupled operator.
- Hours 10–13: singular functional \(c[h]\) and adapted weighted \(L^p\).
- Hours 13–16: assemble the three estimates and test nonlinear closure, including targeted certified calculations.
- Hours 16–18: independently audit proofs, optimize constants and write the final report.

Reallocate time if one approach yields a more promising rigorous theorem.

If multiple research agents are available, parallel theoretical derivations and independent audits are encouraged, provided all experiments remain inside the copied workspace.

Record start time and actual work performed. Save checkpoints at least hourly.

Do not invent research duration, successful verification, or completed numerical runs.

If interrupted, preserve a reproducible restart state in the research workspace.

## 8. Mandatory deliverables

Inside the copied research workspace, prepare:

- `S1_THEORY_18H_REPORT.md` — the main mathematical report.
- `S1_PROOFS.md` or a corresponding LaTeX file — detailed proofs of accepted theorems.
- `S1_NUMERICAL_CERTIFICATES.md` — numerical inequalities, certification methods and unresolved checks.
- `S1_CLOSURE.md` — full nonlinear closure conditions, actual numerical margins and outstanding gaps.
- `S1_RESTART.md` — reproducible commands and continuation instructions.

The main report must explicitly answer:

1. Can the \(L^2\)-based estimate close? If not, what is the first mathematically precise obstruction?
2. Can a direct \(C^\alpha\) inverse estimate for \(h\) be proved, without making \(h_x\) the primary variable?
3. Can \(c[h]\) be controlled independently of a high-order Hölder estimate?
4. Is the scaling freedom correctly eliminated?
5. Are the far-field exponent and angular perturbations rigorously accommodated?
6. Can the three parts be combined into one inverse?
7. Can the numerical residual and nonlinear estimates close an a posteriori existence theorem?

If full closure is impossible within this research window, obtain the strongest rigorous partial theorems and quantify the exact remaining margins.

Prioritize new mathematical results over general discussion.

**Final success criterion: a complete, rigorously verified existence argument near the S1 numerical profile, or the strongest proved theory and sharply identified remaining obstruction attainable within the 18-hour window.**
