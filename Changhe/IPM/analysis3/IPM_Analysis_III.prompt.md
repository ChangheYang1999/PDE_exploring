# S2 — 18-Hour Rigorous Theory and Computer-Assisted Inverse Research for the Full-Plane IPM Profile (case1)

## 0. Mission and workspace requirements

This is an 18-hour mathematical research project aimed at rigorously establishing the existence of an exact full-plane self-similar IPM profile near the numerical S2 solution.

The numerical project is located at:

`~/Changhe/IPM/case1`

If this exact path does not exist, resolve `Changhe/IPM/case1` from the actual user home or project root. Do not silently use `case4` or any other project.

**The original `case1` directory must remain strictly read-only.**

Before conducting any numerical or symbolic experiment:

1. Inspect the source directory and identify the numerical solution, code, coefficients, basis and existing verification artifacts.
2. Create a separate directory outside `case1`, for example `~/Changhe/IPM_theory_runs/S2_case1_18h_<timestamp>`.
3. Copy the ENTIRE original `case1` directory into the new research workspace.
4. Run all numerical tests and theoretical experiments on that copy.
5. Store all new calculations, reports, generated files, caches and modified programs outside the original directory.
6. Inspect absolute paths, symlinks and imported code to ensure that no calculation writes to the source directory.

Never modify or delete the original data, and never use the original working directory for experiments.

### Primary objective

Obtain a complete rigorous a posteriori existence theorem for the S2 numerical profile if possible.

There are **four research avenues**.

The first three concern different theoretical estimates:

1. \(L^2\)-based, weighted Sobolev and negative-order estimates.
2. \(C^\alpha\)-based estimates for \(h\) itself, avoiding \(C^\alpha\) estimates of \(h_x\) whenever possible.
3. Control of the singular functional \(c[h]\) through weighted local estimates and finite-rank reduction.

The fourth is a separate and independent computer-assisted approach:

4. A rigorous finite-basis approximate inverse with certified off-basis and infinite-dimensional remainder estimates.

**Avenue IV is independent of Avenues I–III.**

It must not assume that their estimates have been proved.

Conversely, the first three avenues should not require the finite-basis method to work.

The research may explore each approach independently, then combine verified results if mathematically useful.

The goal is closure of the actual nonlinear problem, not merely a conditional estimate or a promising numerical result.

Existing numerical data may be used freely in the copied workspace.

Rigorous analytical reasoning, computer algebra, high-precision numerical experiments and validated interval arithmetic are all allowed.

Purely numerical evidence is insufficient for a final existence claim.

## 1. Identify the S2 numerical solution and exact equation

We study the full-plane stationary self-similar IPM system

\[
F(\rho):=(c_lX+U[\rho])\cdot\nabla\rho-\rho=0,
\qquad X=(x,y)\in\mathbb R^2,
\]

with

\[
U[\rho]=(-\psi_y,\psi_x),
\qquad -\Delta\psi=\partial_x\rho.
\]

The intended parity is

\[
\rho(-x,y)=\rho(x,y),
\qquad
\rho(x,-y)=-\rho(x,y).
\]

The canonical inverse should respect the actual full-plane growth and symmetry conditions, with no additional harmonic velocity.

This is the **S2, x²y-leading branch**.

Near the origin,

\[
\boxed{
\rho(x,y)=x^2y\,a(x,y),
\qquad a(0)=1.
}
\]

The reference X3 numerical state has approximately

\[
c_l\simeq5.57536261,
\qquad
k=\frac1{c_l}\simeq0.17936053.
\]

The full numerical project may contain newer data. Inspect it carefully and determine the latest accepted approximation.

Do not assume that the numerical approximation is exactly stationary, exactly normalized or smooth to all orders.

A previous extensive a posteriori investigation of the X3 branch found several important theoretical obstructions, local theorems and certified residual bounds. Use such prior results if the supporting material is available, but independently verify their hypotheses and relevance to the current `case1` state.

### Normalization and full linearization

The \(x^2y\) coefficient of the stationary equation gives

\[
\boxed{
3c_l-c[\rho]=1,
}
\]

where

\[
c[\rho]=\psi_{xy}[\rho](0).
\]

Thus

\[
c_l=\frac{1+c[\rho]}3.
\]

For perturbations \(h\),

\[
\delta c_l=\frac13c[h].
\]

The full linearization at a background \(\bar\rho\) is expected to be

\[
\boxed{
\mathcal Lh
=
V\cdot\nabla h-h
+
\left(U[h]+\frac{c[h]}3X\right)
\cdot\nabla\bar\rho,
}
\]

where

\[
V=\bar c_lX+U[\bar\rho].
\]

Verify all signs, coefficients and normalization terms independently.

Do not replace this with the fixed-\(c_l\) linearization without explicitly stating the change.

### Scaling

The equation is invariant under

\[
\rho_\lambda(X)=\lambda\rho(X/\lambda).
\]

For an \(x^2y\)-leading profile, this transforms the leading coefficient by \(\lambda^{-2}\).

Therefore the normalization \(a(0)=1\) eliminates the spatial scaling degree of freedom at the formal level.

The scaling tangent

\[
K=\rho-X\cdot\nabla\rho
\]

satisfies

\[
J(K)=-2,\qquad
J(h):=\left.\frac{h}{x^2y}\right|_{X=0},
\]

under the necessary regularity assumptions.

Consequently, S2 does not have the same remaining scaling freedom as S1.

However, the condition \(J(h)=0\) must be continuous or closed in the chosen correction space.

An earlier investigation showed that it is not closed in several natural weak weighted norms. Do not overlook this functional-analytic issue.

## 2. Precise objective and acceptable outcomes

We would like to establish a rigorous inverse estimate for the complete linearized operator, together with the nonlinear estimates necessary to correct the numerical profile.

A schematic target is

\[
\boxed{
\|h\|_X\le K\|\mathcal Lh\|_Y,
}
\]

where \(X\) includes the correct weighted, regularity, axis-jet and far-field conditions.

This inequality must not be assumed.

A genuine inverse theorem requires appropriate injectivity, surjectivity and domain statements.

We then want a nonlinear theorem giving a correction \(h\) and an exact solution \(\rho=\bar\rho+h\).

Investigate each of the four avenues to see whether it can provide this result.

The strongest possible outcome is a complete existence proof.

A rigorous obstruction to a proposed norm or inverse method is also valuable, but should lead to a revised method rather than simply ending the project.

If no approach closes within 18 hours, deliver the best mathematically rigorous results and precisely identify the first missing inequality in each avenue.

## 3. Research Avenue I — \(L^2\)-based estimates

### 3.1. Understand the origin obstruction

Near the origin, using the normalization \(c[\rho]=3c_l-1\), the transport field has linearization

\[
DV(0)=
\begin{pmatrix}
-(2c_l-1)&0\\
0&4c_l-1
\end{pmatrix}.
\]

Write

\[
A=2c_l-1,\qquad
D=4c_l-1.
\]

Thus

\[
V(X)\approx(-Ax,Dy).
\]

The origin is a saddle.

An earlier negative-order energy analysis produced an indefinite matrix at the origin,

\[
M(0)=\operatorname{diag}(2-c_l,5c_l).
\]

For \(c_l\approx5.57536\), the first eigenvalue is negative.

Re-derive this identity independently and verify exactly what estimate it rules out.

Do not pursue the same unweighted coercivity inequality if it has already been rigorously disproved.

### 3.2. Existing weighted-space obstructions

Earlier X3 analysis found the following method-specific difficulties:

- Center-concentrated quasimodes invalidate same-norm inverse estimates in a critical weighted \(H^1\)-type space.
- Increasing the singular radial weight in the tested family does not remove these quasimodes.
- A weighted factor supremum space also admits near-kernel sequences.
- Some axis-weighted spaces invert the frozen saddle transport but fail to accommodate the full nonlocal linearization.
- The center normalization is not a closed constraint in some weaker topologies.
- Certain nonlinear transport terms are not continuous in a single transport graph norm.

Before constructing a new proof, determine which of these claims have valid rigorous supporting arguments and whether they apply to the current numerical state.

Do not waste time repeatedly testing estimates already ruled out on their natural domains.

A modification that changes the function space, domain, jet constraints or target norm is allowed, but explain precisely why the counterexample no longer applies.

### 3.3. Search for a compatible weighted Hilbert realization

Possible directions include:

**A. Anisotropic weighted Sobolev spaces.**

Exploit the saddle geometry rather than using isotropic weights.

Investigate conormal derivatives, logarithmic coordinates, weighted Fourier spaces and characteristic-adapted norms.

Prove the mapping properties of the complete linearized operator, including the nonlocal term.

**B. Axis jets plus weighted remainder.**

Decompose

\[
h=h_{\rm jets}+h_{\rm rem}.
\]

The jet variables should account for the necessary Taylor coefficients along the invariant axes.

The remainder should lie in a carefully chosen anisotropic weighted space.

Derive the coupled equations for the jet variables and the remainder, including all nonlocal compatibility conditions.

Do not assume that weighted Sobolev membership gives classical traces automatically.

**C. Negative-order potential energies with modified symmetrizers.**

Investigate whether a non-isotropic potential energy or a matrix-valued symmetrizer can overcome the sign-indefinite origin.

Establish explicit positivity, or prove that the candidate symmetrizer cannot work.

**D. Different high- and low-order spaces.**

A single same-norm inverse may be impossible or unsuitable.

Investigate a two-norm theorem in which the strong space controls derivatives and the weaker norm controls the nonlinear correction.

Every mapping and bilinear estimate must be stated in compatible spaces.

### 3.4. Source point \(P\)

The X3 numerical profile has a source point near

\[
P=(8.600064,0).
\]

At an exact solution with \(\rho_y(P)\ne0\), its transport eigenvalues are expected to be

\[
2c_l-1,\qquad1.
\]

The local frozen coupled operator is

\[
L_P=
A s\partial_s+\mu y\partial_y-1
-g\mathcal M,
\]

where \(\mathcal M\) has Fourier multiplier

\[
\widehat{\mathcal Mh}(\xi)
=\frac{\xi_1^2}{|\xi|^2}\widehat h(\xi),
\]

and \(g=\bar\rho_y(P)\).

For the reference X3 state,

\[
A\approx10.15,\qquad
\mu\approx1,\qquad
g\approx29.75.
\]

An earlier investigation obtained positive local results for this frozen operator, including explicit inverse bounds in certain Sobolev orders near \(3.1\).

Reassess and reuse these results where valid.

But distinguish carefully between:

- A frozen inverse.
- A localized a priori estimate.
- A localized auxiliary inverse.
- The full variable-coefficient global inverse.

A forcing coefficient such as \(K_1<0.3181\) is not itself a global inverse norm.

The principal goal is to find a way to connect the origin, source, invariant axes and far field.

### 3.5. Far-field realization

The numerical profile has a nontrivial far-field expansion, approximately beginning with

\[
r^{1/c_l}\Theta_0(\theta).
\]

Perturbations of \(c_l\) produce logarithmic terms.

The complete linearization contains

\[
\frac{c[h]}3X\cdot\nabla\bar\rho,
\]

which may fail to belong to a naïvely chosen decaying forcing space.

Separate the necessary leading tail directions and formulate correct matching conditions.

Do not treat nonintegrable tail coordinates as ordinary \(L^2\) correction variables.

### 3.6. Avenue I deliverable

Establish the strongest possible compatible Hilbert-space inverse theorem.

If a full inverse remains unavailable, provide:

- A precise functional space and domain.
- Proven local or global a priori bounds.
- Proven mapping properties.
- Explicit finite-dimensional compatibility conditions.
- Numerically verifiable coefficient inequalities.
- A rigorous explanation of the remaining obstruction.

## 4. Research Avenue II — \(C^\alpha\)-based estimates for \(h\)

This is a separate theoretical line.

**Our priority is \(h\) in \(C^\alpha\), not \(h_x\) in \(C^\alpha\).**

Do not replace the research objective with high-order Schauder estimates unless they are genuinely necessary.

The target is a bound such as

\[
[h]_{C^\alpha_w}
\le
C_\alpha\bigl(
\|\mathcal Lh\|_{Y_\alpha}
+\text{controlled lower-order terms}
\bigr).
\]

### 4.1. Analyze the complete singular-integral coupling

Using

\[
U[h]=(-R_1R_2h,R_1^2h),
\]

write the full equation explicitly.

Distinguish

\[
R_1^2=T_{xx}-\frac12I,\qquad
R_1R_2=T_{xy}.
\]

Explore both the local identity contribution and the sign structure of the complete multipliers.

Do not estimate two first-order Riesz transforms separately and multiply their \(C^\alpha\) norms.

Where useful, exploit the Beurling-transform representation and angular cancellation.

A small, explicit Schauder constant is desirable, but preserving the coupled operator may be more important than an independent sharp Riesz estimate.

### 4.2. Origin saddle

Determine whether a same-order \(C^\alpha\) inverse can exist for the frozen origin operator in a natural Hölder space.

Investigate the effect of the stable and unstable characteristic directions.

Pay attention to:

- Parity.
- The \(x^2y\) vanishing structure.
- Center normalization.
- Possible anisotropic Hölder metrics.
- Singular behavior along invariant axes.
- Nonlocal coupling and its Fourier symbol.

Do not assume ordinary isotropic \(C^\alpha\) coercivity.

If standard \(C^\alpha\) fails, determine whether an anisotropic or weighted Hölder norm can work while still providing meaningful control of \(h\).

### 4.3. Source regularity

Earlier X3 analysis established a sharp regularity-loss phenomenon for the frozen source inverse at Hölder–Zygmund orders above one.

For suitable \(\sigma>1\), the output order has the form

\[
r(\sigma)=\sigma-\frac{\sigma-1}{A}.
\]

This does not automatically decide the low-order \(0<\alpha<1\) problem.

Investigate the low-order \(C^\alpha\) mapping separately.

Determine whether a useful global \(C^\alpha(h)\) estimate can be obtained without needing a separate \(C^\alpha(h_x)\) estimate.

If derivative control is unavoidable for nonlinear closure, explain the precise derivative loss and formulate a compatible high/low norm alternative.

### 4.4. Variable coefficients and global extension

After analyzing the local frozen operators, study perturbation by the actual numerical coefficients.

Use explicit bounds for the coefficient variations and commutators.

Try to patch local estimates from:

1. The origin.
2. The positive and negative axis source points.
3. Neighbourhoods of the invariant axes.
4. The finite intermediate region.
5. Infinity.

Use available low-order estimates where appropriate.

The result should be a global linear estimate, not merely several unrelated local statements.

### 4.5. Avenue II deliverable

Provide the strongest rigorous \(C^\alpha(h)\) theorem possible, including:

- The admissible \(\alpha\) interval.
- Exact function spaces and constraints.
- Explicit inverse or a priori constants.
- Regularity loss, if any.
- The role of the rank-one \(c[h]\) term.
- Required numerical coefficient bounds.
- Any rigorous obstruction.

Do not falsely claim a same-order inverse if only a weaker mapping has been proved.

## 5. Research Avenue III — The singular functional \(c[h]\)

We need a separate estimate for

\[
c[h]=\psi_{xy}[h](0).
\]

The full-plane singular kernel is expected to be

\[
c[h]
=
\frac1\pi
\int_{\mathbb R^2}
\frac{\sin3\theta}{r^3}h(X)\,dX,
\]

under the correct hypotheses and interpretation.

Check the normalization, convergence and symmetry.

### 5.1. Two-step idea

A previous theoretical construction proposed separating

\[
c[h]=c_{\rm near}[h]+c_{\rm far}[h].
\]

The regular far part can be estimated by a suitable weighted \(L^2\) or other low norm.

The singular near part is controlled by a local weighted \(L^p\) moment through an adjoint transport equation.

For an \(x^2y\)-leading perturbation, a possible local moment is

\[
\mathfrak M_{p,R}[h]
=
\left(
\int_{\Omega_R}\frac{|h|^p}{r^{3p}}\,dX
\right)^{1/p}.
\]

This should control the singular contribution since the kernel behaves like \(r^{-3}\).

However, the earlier model used an expanding field

\[
B_\beta=(x/2,\beta y),
\]

not the S2 saddle

\[
B_0=(-Ax,Dy).
\]

**The earlier adjoint-weight formula cannot simply be copied.**

### 5.2. Construct a saddle-adapted estimate

Investigate:

- Characteristic geometry and suitable local integration regions.
- Incoming and outgoing boundaries.
- Correct adjoint transport equations.
- Positivity and integrability of the adjoint weight.
- Appropriate exponents \(p\).
- Whether a coercive local weighted moment is possible.
- The influence of boundary fluxes along stable and unstable directions.

Explicitly determine whether the required local adjoint weight exists and has usable quantitative bounds.

Do not assume an expanding-flow estimate continues to hold for a saddle.

If this method fails, seek another rigorous singular-functional estimate using weighted elliptic theory, trace/jet decomposition or a dual formulation.

### 5.3. Use the exact normalization cancellation

For S2,

\[
\bar\rho\sim x^2y.
\]

At leading order,

\[
U[h]\sim c[h](-x,y).
\]

Hence

\[
\boxed{
\left(
U[h]+\frac{c[h]}3X
\right)\cdot\nabla(x^2y)=0
}
\]

at leading order.

This cancellation is crucial.

Subtract the leading Taylor velocity and density profiles before estimating the remainders.

The challenge is to show that the renormalized velocity terms admit sufficiently small coefficients near the origin.

Do not assume smallness merely from formal vanishing orders.

Derive rigorous inequalities such as

\[
\left|\text{renormalized coupling}\right|
\le
\eta(R)\mathfrak M_{p,R}[h]
+
C(R)\|h\|_{\rm regular},
\]

and prove or disprove

\[
\eta(R)\to0\qquad(R\to0).
\]

### 5.4. Close the singular estimate

The desired structure is

\[
\boxed{
\Delta_R\mathfrak M_{p,R}[h]
\le
\text{forcing}
+
C(R)\|h\|_{\rm regular},
}
\]

with an explicit, rigorously positive \(\Delta_R\).

Then derive

\[
|c[h]|
\le
C_c\|\mathcal Lh\|_Y
\]

or a compatible augmented inverse bound.

Treat the exponent variation as a rank-one term only after the singular functional has been proved bounded on the chosen domain.

If appropriate, reduce the remaining problem to a finite matrix and certify its invertibility.

### 5.5. Avenue III deliverable

The goal is an actual bound for \(c[h]\), with explicit constants and a positive closure margin.

If this cannot be obtained, identify exactly whether the obstruction comes from:

- The adjoint weight.
- Boundary fluxes.
- Velocity remainders.
- Weighted elliptic bounds.
- The chosen function space.
- The finite-rank reduction.

Do not present an unproved positive gap as a theorem.

## 6. Research Avenue IV — Independent rigorous finite-basis inverse certification

**This avenue is independent of Avenues I–III.**

Its objective is to transform the existing finite-section numerical inverse diagnostics into a genuine infinite-dimensional computer-assisted proof.

Do not assume the weighted energy, Hölder or singular-functional estimates of the previous avenues.

This avenue must build its own mathematically complete inverse framework, possibly using different spaces and norms.

### 6.1. Recover the previous numerical basis and experiments

The earlier finite-section study used an angular/radial representation of the form

\[
\boxed{
h(r,\theta)
=
r^3\sum_{m=0}^{M-1}
B_m(\log r)\Phi_m(\theta),
}
\]

with

\[
\Phi_m(\theta)
=
\cos^2\theta\sin\theta\cos(2m\theta).
\]

The radial components involved:

- Logarithmic radial splines.
- Near-origin power-law pieces.
- Far-field power laws and prescribed tails.
- Matching constraints at joining radii.
- Optional free far angular profiles.

Earlier numerical experiments used \(M=16\), \(M=24\), different radial resolutions, and matrices with thousands of retained columns.

Recover the exact construction from `case1`, including every basis function, weight, Gram matrix, collocation rule and normalization constraint.

Do not rely only on descriptive summaries.

Determine whether the saved computation is reproducible in the copied workspace.

### 6.2. Fix the conforming-basis issue

Previous analysis found that some spline basis functions had small but nonzero discontinuities at internal joins.

This is not harmless for a continuum Sobolev estimate.

A discontinuity can make a function fail to belong to \(H^1\), regardless of how small its jump is.

Similarly, a derivative jump can make \(Lh\) fail to belong to an \(H^1\)-type forcing space.

Therefore, construct a genuinely conforming basis.

Possible choices include:

- Exact continuous B-splines.
- \(C^1\), \(C^2\) or higher-order splines with analytically imposed joining conditions.
- Exact Hermite constructions.
- Smooth spectral basis functions with compatible origin and far-field behavior.

The regularity order must be matched to the chosen operator domain and forcing norm.

Prove that every basis function and its image under the full linearized operator belong to the claimed spaces.

Also verify:

- Origin normalization.
- Axis vanishing and parity.
- Far-field asymptotics.
- Nonlocal strain.
- Matching conditions.
- Any independent tail coordinates.

A tiny floating-point error in a continuity condition is not an acceptable substitute for exact conformity.

### 6.3. Define the finite-dimensional matrix rigorously

Let \(X\) and \(Y\) denote the chosen infinite-dimensional domain and forcing spaces.

Define finite-dimensional projections

\[
P_N:X\to X_N,
\qquad
Q_M:Y\to Y_M.
\]

Study

\[
A_{M,N}=Q_M\mathcal LP_N.
\]

Specify exactly how the norms of \(X_N\) and \(Y_M\) correspond to the infinite-dimensional norms.

Compute and rigorously certify:

- Gram matrices.
- Linearized operator matrix entries.
- Nonlocal coupling matrix entries.
- The rank-one \(c[h]\) contribution.
- Smallest singular values or an approximate inverse.
- Matrix inversion errors.
- Quadrature and floating-point errors.

Use exact integration whenever possible, especially for polynomial-exponential radial pieces.

Use interval arithmetic for the remaining finite calculations.

Do not interpret a collocation singular value as a continuum inverse bound before proving the required norm comparison.

### 6.4. Main missing task: off-basis residual

This is the most important new part.

The numerical experiment only sees a finite-dimensional approximation.

The full operator has the decomposition

\[
\boxed{
\mathcal L=
\begin{pmatrix}
Q_M\mathcal LP_N&
Q_M\mathcal L(I-P_N)\\
(I-Q_M)\mathcal LP_N&
(I-Q_M)\mathcal L(I-P_N)
\end{pmatrix}.
}
\]

The first block is the numerically represented matrix.

The other three blocks require separate rigorous control.

In particular, estimate

\[
\|(I-Q_M)\mathcal LP_N\|_{X\to Y},
\]

and investigate

\[
Q_M\mathcal L(I-P_N),
\]

as well as the invertibility of

\[
D_{M,N}=(I-Q_M)\mathcal L(I-P_N).
\]

These are off-basis and infinite-dimensional estimates.

They are NOT the same as estimating higher spatial derivatives of the numerical profile residual \(F(\bar\rho)\).

Do not confuse the two.

### 6.5. Angular and radial tail bounds

Use the analytic structure of the profile, Green operator and chosen basis.

Possible techniques:

- Exact angular Fourier convolution.
- Bounds on angular Fourier tails of the numerical profile.
- Radial spline approximation estimates.
- Weighted orthogonal projection estimates.
- Explicit Green-kernel representations.
- Dyadic frequency decompositions.
- Commutator estimates.
- Anisotropic high-frequency estimates.
- Characteristic transport estimates.

If the background has a finite angular expansion, exploit the exact finite angular bandwidth wherever appropriate.

But account separately for the infinite-dimensional domain and for radial high frequencies.

Do not claim that a small numerical contribution from output modes 32–39 controls all modes 40 and above.

The tail beyond the numerical cutoff must have a proven bound.

### 6.6. Prove invertibility of the infinite-dimensional complement

A finite-dimensional matrix can have a positive smallest singular value while the full operator fails to be bounded below.

Therefore investigate an analytically controlled high-frequency/complement operator.

Possible frameworks include:

**Method A: analytic reference inverse plus finite-rank correction.**

Construct

\[
\mathcal L=\mathcal L_{\rm ref}+\mathcal K,
\]

where \(\mathcal L_{\rm ref}\) has a rigorously controlled inverse on the selected spaces.

Then use finite-dimensional numerics to handle the difficult part of \(\mathcal K\), while analytically bounding the remainder.

Do not assume \(\mathcal K\) is compact or small merely because it contains a Riesz transform.

**Method B: block inverse and Schur complement.**

Prove that the infinite-dimensional high-high block \(D_{M,N}\) is invertible in appropriate spaces and estimate the off-diagonal blocks.

Then certify the finite Schur complement

\[
S_{M,N}
=
A_{M,N}
-
B_{M,N}D_{M,N}^{-1}C_{M,N}.
\]

**Method C: parametrix with verified operator error.**

Construct an infinite-dimensional approximate inverse \(B\), containing an analytic infinite-dimensional component and a numerically certified finite-dimensional correction.

Prove

\[
\boxed{
\|I-B\mathcal L\|_{X\to X}<1
}
\]

and, where two-sided invertibility is needed,

\[
\|I-\mathcal LB\|_{Y\to Y}<1,
\]

with the correct domains and bounded compositions.

Do not attempt to prove the first estimate using a purely finite-rank \(B\) on an infinite-dimensional space: such a construction cannot approximate the identity in operator norm to error less than one.

An analytic infinite-dimensional component is essential.

### 6.7. Respect the known obstructions

The previous X3 investigation proved quasimodes for certain weighted norms.

If the proposed high-frequency inverse estimate contradicts one of these rigorous counterexamples, identify the conflict immediately.

Do not attempt to overcome an actual continuum obstruction merely by increasing the basis dimension.

Instead consider:

- A stronger or anisotropic domain norm.
- A different forcing norm.
- Explicit jet variables.
- Infinite-dimensional compatibility conditions.
- Modified boundary or tail constraints.
- A different analytic reference operator.

The eventual goal remains a rigorous inverse for the full linearization.

### 6.8. Basis avenue deliverable

Produce a mathematically explicit computer-assisted inverse certification framework.

The ideal outcome is a theorem of the form

\[
\boxed{
\|\mathcal L^{-1}\|_{Y\to X}\le K_{\rm cert},
}
\]

with all infinite-dimensional remainders rigorously bounded.

If that cannot be established, prove the strongest partial result available:

- Valid finite-dimensional operator matrices.
- Exact conforming basis construction.
- Certified finite-matrix inverse.
- Certified off-basis estimates.
- An analytic high-frequency theorem.
- Or a rigorous obstruction to the chosen realization.

Clearly distinguish these results.

A finite matrix with a positive numerical singular value is not, by itself, a satisfactory final result.

## 7. Full nonlinear a posteriori closure

The research must ultimately return to the nonlinear equation.

For the normalized S2 problem, write

\[
F(\bar\rho+h)
=
F(\bar\rho)+\mathcal Lh+\mathcal N(h).
\]

Derive \(\mathcal N(h)\) exactly, including the variation of \(c_l\).

Typically, the quadratic term involves

\[
\left(U[h]+\frac{c[h]}3X\right)\cdot\nabla h.
\]

Do not assume this term maps a weak transport graph norm quadratically into itself. Previous research found counterexamples to such assumptions in several candidate spaces.

Construct a valid fixed-point or two-norm/tame iteration where the high-order domain, lower-order norm and forcing spaces are all compatible.

A useful schematic set of closure inequalities is

\[
K_H\eta\le r,
\]

\[
K_LC_BK_H\eta<1,
\]

\[
C_Vr\le r_V.
\]

But these must correspond to a proved theorem with explicit definitions of every constant.

Investigate whether either:

- The combined analytical framework from Avenues I–III, or
- The independent basis-based inverse from Avenue IV

can provide the required inverse estimates.

Do not require both routes to succeed.

One complete rigorous route is sufficient for an existence proof.

Verify that the numerical residual belongs to the forcing space of the successful route.

Account for:

- Center normalization.
- Nonlocal strain.
- Axis jets and their matching.
- Far-field corrections and exponent variation.
- Nonlinear derivative loss.
- Uniformity of inverse bounds over the correction ball.
- All numerical and approximation errors.

Do not claim an exact solution merely because the approximate residual is small.

## 8. Numerical research and certification priorities

The existing `case1` directory contains valuable numerical evidence. Use it as a starting point, not as a substitute for mathematical analysis.

Possible targeted computations include:

1. Reconstructing the actual accepted numerical background.
2. Verifying center strain and source coefficients.
3. Certified coefficient bounds for local inverses.
4. Residual estimates in the actual weighted forcing spaces.
5. Eigenvalue or quadratic-form bounds needed by the theory.
6. Exact conforming basis tests.
7. Certified Gram matrices and finite inverse calculations.
8. Angular and radial tail bounds.
9. Off-basis operator estimates.
10. Finite-rank Schur complements.
11. Parameter optimization for a positive closure margin.

You may run substantial calculations if they advance a concrete theorem.

Prefer analytically justified interval calculations over excessive floating-point resolution.

Whenever a numerical verification task arises, derive the mathematical inequality first, specify the target bound, and then run the experiment.

For every certified number, record:

- The exact mathematical quantity.
- Input file identity and numerical parameter conventions.
- Calculation method.
- Floating-point or interval precision.
- Truncation error.
- Rounding error.
- Final outward enclosure.
- Independent consistency checks.

Do not label an unverified computation as certified.

## 9. Time budget: 18 hours

This S2 task is intended to run concurrently with the S1 task under the same 18-hour wall-clock research window.

Allocate meaningful effort to all four avenues.

Avenue IV deserves substantial independent attention because it provides a potential proof route even if the three analytical estimates fail.

Suggested organization:

### Hours 0–2: Preparation and audit

- Copy the full `case1` directory.
- Identify the latest accepted numerical state.
- Read the existing theoretical and numerical reports if available.
- Identify previously proved obstructions to avoid redundant work.
- Recover the basis and full linearization.

### Hours 2–11: Parallel theoretical investigations

Run as many independent research threads as resources allow:

- Weighted \(L^2\)/Sobolev inverse theory.
- Direct \(C^\alpha(h)\) theory.
- Singular functional \(c[h]\).
- Conforming basis and off-basis inverse theory.

Each thread must derive precise statements and identify numerical certification requirements.

The basis avenue should not depend on the success of the others.

### Hours 11–16: Focused proof development and certification

Concentrate on the most promising avenues.

- Improve theoretical constants.
- Run targeted numerical verification.
- Verify basis-tail or high-frequency estimates.
- Derive finite-dimensional reductions.
- Check nonlinear closure inequalities.
- Test whether the chosen functional spaces are mutually compatible.

If one route offers a plausible complete proof, prioritize it while retaining the other threads' results.

### Hours 16–18: Independent audit and final assembly

- Recheck every theorem and sign convention.
- Verify the local-to-global implications.
- Separate unconditional and conditional results.
- Check whether all numerical verification tasks were actually completed.
- Produce a clear final verdict and reproducible handoff.

Do not terminate early simply because one candidate estimate fails.

If the execution environment is interrupted, save the current proofs, computations and restart instructions.

Record actual work time. Never claim that 18 hours of research were completed merely because an 18-hour window was requested.

## 10. Required deliverables

All outputs must be stored in the copied research workspace, never in the original `case1`.

Create:

- `S2_THEORY_18H_REPORT.md` — comprehensive mathematical report.
- `S2_L2_THEORY.md` — weighted Hilbert-space estimates and obstructions.
- `S2_CALPHA_THEORY.md` — direct Hölder estimates for \(h\).
- `S2_C_FUNCTIONAL.md` — singular functional control.
- `S2_BASIS_CERTIFICATION.md` — independent finite-basis/infinite-dimensional approach.
- `S2_NUMERICAL_CERTIFICATES.md` — independently checked numerical inequalities.
- `S2_CLOSURE.md` — nonlinear existence-theorem status.
- `S2_RESTART.md` — exact reproducibility and continuation instructions.

Supporting code, data and proof files should be included.

### The final report must explicitly answer

**Avenue I — \(L^2\)-based**

- What is the strongest rigorously valid weighted inverse estimate?
- Which older obstructions still apply?
- Can a consistent domain be constructed?

**Avenue II — \(C^\alpha\)-based**

- Can \(h\) be controlled directly in \(C^\alpha\)?
- What is the admissible exponent range?
- Can the complete Riesz coupling and source behavior be handled?
- Is \(C^\alpha(h_x)\) genuinely unnecessary?

**Avenue III — Singular \(c[h]\)**

- Can the saddle-adapted local weighted estimate be proved?
- Can the nonlocal velocity remainders be absorbed?
- Can the rank-one term be reduced rigorously?

**Avenue IV — Basis-based certification**

- Is the finite basis conforming?
- Is the finite inverse rigorously certified?
- What are the off-basis residual bounds?
- Is the infinite-dimensional complement controlled?
- Does the combination yield a genuine inverse theorem?

**Final closure**

- Is a complete nonlinear existence theorem established?
- If not, which precise estimate is missing?
- What is already proved?
- Which constants or inequalities require numerical certification?
- Which research avenue is closest to closure, and why?

## 11. Strict mathematical standards

A claim is a theorem only if it has a complete rigorous proof.

A computer-assisted bound is rigorous only if every numerical and infinite-dimensional error has been controlled.

Every inverse statement must specify the operator domain and range.

Every weighted estimate must verify membership of both the perturbation and its image.

Every normalization must be meaningful and closed in the selected topology.

Every asymptotic exponent perturbation must include its logarithmic variation where appropriate.

Every approximation must account for the full infinite-dimensional operator, not just its discretized matrix.

Do not use an unproved finite-rank approximation, an unverified compactness claim, or a small numerical residual as a substitute for invertibility.

Do not confuse the absence of a proof with a proof of nonexistence.

If a candidate inequality fails, construct a rigorous counterexample whenever feasible.

If a candidate bound is valid but too large for closure, try to improve the theoretical bound and determine whether the loss is intrinsic.

The final objective is a genuine rigorous correction theorem for the S2 numerical profile.

**A complete existence proof by any one valid avenue is the ideal outcome. Otherwise, produce the strongest rigorous advances across all four avenues, with exact numerical verification requirements and a transparent account of the remaining gaps.**
