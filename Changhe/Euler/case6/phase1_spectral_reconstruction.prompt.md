# Euler Case6 — Phase 1: High-Fidelity Reconstruction Using a Constrained Spectral Basis

## 0. Overall research plan and scope

We are studying a travelling self-similar axisymmetric Euler profile, currently represented numerically by the existing case6 implementation.

Our research program has three phases:

**Phase 1 — Spectral reconstruction (CURRENT TASK)**

Replace the existing numerical representation with a carefully constructed spectral basis, reconstructing the current case6 profile as accurately as possible.

The spectral representation must enforce exact Poisson coupling and selected finite-order far-field asymptotic cancellations through its coefficient structure.

During Phase 1:

- Keep \(\lambda\) fixed at its current reference value.
- Allow the travelling parameter \(C\) to vary and be fitted.
- Optimize spectral coefficients and \(C\) to reproduce the existing numerical profile.
- Do not optimize the Euler transport residuals directly.

**Phase 2 — Fixed-lambda PDE optimization (FUTURE)**

Starting from the reconstructed spectral checkpoint, keep \(\lambda\) fixed and optimize the Euler transport residuals.

**Phase 3 — Lambda continuation (FUTURE)**

Gradually continue \(\lambda\) from its current reference value toward \(1/2\), optimizing the Euler residuals along the continuation.

**Execute Phase 1 only. Do not begin Phase 2 or Phase 3.**

The purpose of the current task is to obtain a highly accurate, numerically stable spectral representation of the existing case6 solution, with the mathematical constraints built into the representation.

This is an implementation and numerical reconstruction task, not merely a mathematical design exercise.

Use the actual existing case6 checkpoint and implementation. Do not substitute an unrelated example or start a new PDE solution search.

---

## 1. Governing equations and reference parameters

We consider the travelling self-similar axisymmetric Euler profile

\[
(U,\Omega,\Psi)(R,Z),
\qquad R\geq0,\quad Z\in\mathbb R.
\]

The governing equations are

\[
\boxed{
U+V_RU_R+V_ZU_Z=2U\Psi_Z,
}
\]

\[
\boxed{
(1+\lambda)\Omega
+V_R\Omega_R+V_Z\Omega_Z
=2UU_Z,
}
\]

where

\[
V_R=\lambda R-R\Psi_Z,
\]

\[
V_Z=C+\lambda Z+2\Psi+R\Psi_R.
\]

The elliptic equation is

\[
\boxed{
-\Delta_5\Psi=\Omega,
}
\]

with

\[
\Delta_5
=
\partial_{RR}+\frac3R\partial_R+\partial_{ZZ}.
\]

The existing case6 reference parameters are

\[
\boxed{
\lambda=0.4989408258587428,
}
\]

\[
C_{\mathrm{ref}}=9.37120536910309.
\]

### Parameter handling

Throughout Phase 1:

\[
\boxed{
\lambda\equiv0.4989408258587428
}
\]

is fixed.

However,

\[
\boxed{
C\text{ is a free fitting parameter}.
}
\]

Initialize \(C=C_{\mathrm{ref}}\), but allow it to vary during reconstruction.

The objective is to determine whether a different \(C\), together with an improved spectral representation, produces a more accurate reconstruction of the existing numerical fields while respecting the spectral constraints.

Do not artificially constrain \(C=C_{\mathrm{ref}}\).

Do not optimize \(\lambda\), move it toward \(1/2\), or perform any continuation in this phase.

Before implementation, verify the precise PDE conventions, normalization, and coordinate definitions against the existing code.

Preserve the original checkpoint and all existing numerical data.

---

## 2. Primary objective: reconstruct the existing profile

Let

\[
(U_{\rm ref},\Omega_{\rm ref},\Psi_{\rm ref})
\]

denote the existing case6 numerical profile.

We want a spectral approximation

\[
(U_{\rm sp},\Omega_{\rm sp},\Psi_{\rm sp})
\]

that reproduces these fields with the highest practical accuracy.

The approximation should reproduce:

1. The core and intermediate-region geometry.
2. The locations and amplitudes of important extrema.
3. The near-axis structure, including any thin layers.
4. The characteristic spatial length scales.
5. The far-field behavior.
6. The relevant first and higher derivatives.

The spectral representation must preserve the actual structure of the reference profile, not merely achieve a small average error on a conveniently chosen sample.

### What can be optimized

The following may be optimized:

- Free spectral coefficients for \(U\).
- Free spectral coefficients for \(\Psi\).
- Independent leading far-field coefficients.
- Independent multipole coefficients.
- Interior correction coefficients.
- Spectral representation scales, when justified.
- The travelling parameter \(C\).

All dependent coefficients enforcing Poisson and asymptotic cancellation constraints must be reconstructed from the free variables.

### What cannot be optimized

Do not optimize:

- \(\lambda\).
- The Euler PDE residual as an objective.
- Any penalty designed primarily to improve Euler transport consistency rather than reconstruction accuracy.

You may evaluate the PDE residual as a diagnostic, but its numerical value must not guide the training objective or checkpoint selection in this phase.

The fitting objective must be based on agreement with the existing numerical profile.

---

## 3. Fundamental structural requirements

The spectral representation must satisfy two mathematical requirements.

### Requirement A: exact Poisson coupling

Construct

\[
\Psi=\sum_j a_j\phi_j(R,Z)
\]

and define

\[
\boxed{
\Omega=-\sum_j a_j\Delta_5\phi_j(R,Z).
}
\]

Then

\[
\boxed{
-\Delta_5\Psi-\Omega\equiv0
}
\]

must hold identically in exact arithmetic over the entire domain.

It must not merely be approximately satisfied through a loss function.

Alternatively, separate expansions for \(\Omega\) and \(\Psi\) are acceptable only if an exact coefficient map enforces the full Poisson identity.

Prefer the construction in which \(\Omega\) is analytically derived from \(\Psi\).

The coefficient map must be explicitly implemented and independently tested.

Furthermore, verify that the representation corresponds to the canonical decaying Poisson inverse and does not introduce arbitrary globally harmonic components.

### Requirement B: exact finite-order far-field cancellations

The Euler equations generate asymptotic expansions for the transport residuals.

Define

\[
\mathcal R_U
=
U+V_RU_R+V_ZU_Z-2U\Psi_Z,
\]

\[
\mathcal R_\Omega
=
(1+\lambda)\Omega
+V_R\Omega_R+V_Z\Omega_Z
-2UU_Z.
\]

Certain low-decay residual sectors must cancel through algebraic relations among the spectral coefficients.

These cancellations must be enforced exactly, not through large penalty weights.

For a selected finite asymptotic order \(S\), enforce all required residual coefficient equations through that order, including all generated angular harmonics and logarithmic terms.

The order \(S\) is a numerical approximation parameter, not a new physical boundary condition.

Importantly, these constraints must not eliminate legitimate far-field terms in the profile itself.

If exact cancellation is incompatible with reproducing a particular feature of the existing numerical checkpoint, quantify the incompatibility. Do not silently relax the structural constraints.

---

## 4. Coordinate system and treatment of the variable C

The translation term can be removed from the linear far-field operator by introducing

\[
z=Z+\frac C\lambda.
\]

Then

\[
C+\lambda Z=\lambda z.
\]

Define

\[
r=\sqrt{R^2+z^2},
\qquad
\mu=\frac zr.
\]

The far-field transport operator becomes simpler in these coordinates.

Use this moving-center representation where it improves the spectral construction.

However, since \(C\) is free, changing \(C\) also changes the relationship between the spectral coordinates and the original physical coordinates.

Implement this dependence explicitly and differentiably.

**All comparisons with the existing numerical profile must be performed at the same physical points \((R,Z)\).**

Do not compare fields after independently translating or recentering them in a manner that conceals reconstruction errors.

Preserve the original case6 normalization and phase convention. If the existing formulation contains a translation gauge freedom, distinguish a physical change in \(C\) from a pure reparameterization.

Do not fix that freedom through an arbitrary new boundary condition.

If reconstruction data do not uniquely determine \(C\), report that identifiability issue rather than assigning unjustified significance to its fitted value.

---

## 5. Recommended globally smooth spectral basis

Use the five-dimensional angular eigenfunctions

\[
Y_\ell(\mu)=C_\ell^{3/2}(\mu),
\qquad \ell=0,1,2,\ldots.
\]

Define the solid harmonics

\[
H_\ell(R,z)=r^\ell Y_\ell(z/r).
\]

These are polynomials in \(R^2,z\), satisfying

\[
\Delta_5H_\ell=0.
\]

For example,

\[
H_0=1,\qquad H_1=3z,
\]

\[
H_2=6z^2-\frac32R^2.
\]

This representation automatically preserves evenness in \(R\) and regularity at the axis.

Do not impose any additional parity in \(Z\).

Introduce a positive numerical length scale \(L\) and define

\[
\boxed{
B_{p,\ell}(R,z)
=
\frac{H_\ell(R,z)}
{(L^2+r^2)^{(p+\ell)/2}},
\qquad p>0.
}
\]

These basis functions are globally smooth and decay as

\[
B_{p,\ell}
\sim r^{-p}Y_\ell(\mu).
\]

Their exact Poisson images are

\[
\boxed{
-\Delta_5B_{p,\ell}
=
d_{p,\ell}B_{p+2,\ell}
+
L^2e_{p,\ell}B_{p+4,\ell},
}
\]

where

\[
d_{p,\ell}
=
(p+\ell)(\ell+3-p),
\]

\[
e_{p,\ell}
=
(p+\ell)(p+\ell+2).
\]

Implement this sparse coefficient map analytically.

Do not rely on automatic differentiation to establish the Poisson identity.

Automatic differentiation may still be used for parameter derivatives during fitting.

### Pure-tail correction basis

The individual rational basis functions introduce additional powers

\[
r^{-p-2},\quad r^{-p-4},\ldots.
\]

These may contaminate the desired asymptotic hierarchy.

To cancel them, define

\[
\boxed{
J_{p,\ell}^{[K]}
=
\sum_{k=0}^{K}
\frac{((p+\ell)/2)_k}{k!}
L^{2k}B_{p+2k,\ell}.
}
\]

Here \((a)_k\) denotes the rising factorial.

Then

\[
\boxed{
J_{p,\ell}^{[K]}
=
r^{-p}Y_\ell(\mu)
+
O(r^{-p-2K-2}).
}
\]

The intermediate tail coefficients vanish exactly.

Select \(K\) large enough that these artificial corrections do not interfere with the protected far-field cancellation order.

### Logarithmic basis functions

Poisson resonances may require terms of the form

\[
r^{-p}(\log(r/L))^mY_\ell(\mu).
\]

Use the globally smooth lifts

\[
\boxed{
J_{p,\ell}^{[K,m]}
=
(-\partial_p-\log L)^mJ_{p,\ell}^{[K]}.
}
\]

Differentiate the complete expression, including its coefficient factors.

Implement the corresponding exact Poisson images.

Do not introduce singular pure-power or logarithmic functions at the origin.

### Near-resonance conditioning

For a Poisson resonance at

\[
p_0=\ell+3,
\]

use stable divided-difference coordinates, such as

\[
\boxed{
Q_{p,\ell}^{[K]}
=
\frac{
J_{p,\ell}^{[K]}
-
L^{p_0-p}J_{p_0,\ell}^{[K]}
}{
(p+\ell)(\ell+3-p)
}.
}
\]

Handle the limit \(p\to p_0\) analytically.

The two terms of each divided difference must both have sufficient far-field correction order. In particular, for protected residual order \(S\), use

\[
\min(p+1,p_0+1)+2(K+1)>S
\]

as a sufficient condition for this construction.

Avoid numerically subtracting nearly equal large coefficients.

---

## 6. Stable near-axis evaluation

The original Poisson equation contains

\[
\frac{3\Psi_R}{R},
\]

which is numerically unstable when computed by direct division at very small \(R\).

The earlier case6 audit identified substantial roundoff amplification near \(R\sim10^{-8}\).

Use

\[
\xi=R^2,
\qquad
U=F(\xi,z),
\qquad
\Psi=G(\xi,z).
\]

Then

\[
\boxed{
\Delta_5G
=
4\xi G_{\xi\xi}+8G_\xi+G_{zz}.
}
\]

Consequently,

\[
\boxed{
\Omega
=
-(4\xi G_{\xi\xi}+8G_\xi+G_{zz}).
}
\]

The transport operator becomes

\[
\mathcal A
=
2\xi(\lambda-G_z)\partial_\xi
+
(\lambda z+2G+2\xi G_\xi)\partial_z.
\]

Thus

\[
\mathcal R_U
=
F+\mathcal AF-2FG_z,
\]

\[
\mathcal R_\Omega
=
(1+\lambda)\Omega+\mathcal A\Omega-2FF_z.
\]

Implement these formulas directly.

The evaluator must work at \(R=0\), at extremely small positive \(R\), and throughout the full numerical domain.

Provide independent high-precision checks near the axis.

---

## 7. Correct Euler far-field asymptotics at the fixed lambda

Let

\[
a=\frac1\lambda.
\]

With the current fixed reference value,

\[
a\approx2.00424569.
\]

The linearized far-field equations permit leading behavior of the form

\[
U\sim r^{-a}f(\mu),
\]

\[
\Psi\sim r^{1-a}g(\mu),
\]

\[
\Omega\sim r^{-a-1}w(\mu).
\]

The leading angular functions must be determined by the reference profile and the equations, not prescribed artificially.

The Poisson relation gives

\[
w=K_{a-1}g,
\]

where

\[
\mathcal L_\mu
=
(1-\mu^2)\partial_{\mu\mu}
-4\mu\partial_\mu,
\]

\[
K_p=-\mathcal L_\mu-p(p-3).
\]

### Nonlinear asymptotic hierarchy

Use common-weight notation

\[
U_\sigma=r^{-\sigma}u_\sigma,
\]

\[
\Psi_\sigma=r^{1-\sigma}p_\sigma,
\]

\[
\Omega_\sigma=r^{-\sigma-1}w_\sigma.
\]

The dynamic leading sector begins at

\[
\sigma=a.
\]

Do not assume that all later exponents are integer multiples of \(a\).

The global Poisson inverse may generate external multipole tails with common weights

\[
h_\ell=\ell+4.
\]

Nonlinear interactions generate sums of existing weights.

The candidate asymptotic set therefore includes combinations of the form

\[
\boxed{
\sigma=na+k,
\qquad
n\ge1,\quad
k\in\{0,4,5,6,\ldots\},
}
\]

together with the independent multipole weights and all terms actually generated below the requested truncation order.

This is a generating rule, not a statement that every such coefficient must be nonzero.

At the reference lambda, mixed multipole–dynamic interactions can occur before some pure nonlinear orders.

Do not omit those interactions.

### Poisson angular multiplier and resonance

For a Gegenbauer mode \(Y_\ell\),

\[
\boxed{
K_{\sigma-1}Y_\ell
=
(\ell+\sigma-1)(\ell+4-\sigma)Y_\ell.
}
\]

Potential Poisson resonances occur at

\[
\boxed{
\sigma=\ell+4.
}
\]

If the resonant forcing is nonzero, logarithmic terms are required.

If the resonant forcing vanishes, do not introduce an unnecessary logarithmic coefficient.

Handle these cases through explicit compatibility checks.

Do not assume every formally possible resonance forces a logarithm.

---

## 8. Exact far-field transport constraints

For a pure-power sector, define

\[
\chi=1-\mu^2,
\]

\[
D_qF=\chi F'-q\mu F.
\]

For angular functions \(P,F\), define

\[
\boxed{
\mathcal B_{p,q}(P,F)
=
q(\chi P'-2\mu P)F
+
(2-p)\chi PF',
}
\]

and

\[
\boxed{
\mathcal N_{p,q}(P,F)
=
\mathcal B_{p,q}(P,F)-2F D_pP.
}
\]

The required coefficient equations are

\[
\boxed{
0=
(1-\lambda\sigma)u_\sigma
+
\sum_{\alpha+\beta=\sigma}
\mathcal N_{\alpha-1,\beta}(p_\alpha,u_\beta),
}
\]

\[
\boxed{
\begin{aligned}
0={}&
(1-\lambda\sigma)w_\sigma\\
&+
\sum_{\alpha+\beta=\sigma}
\mathcal B_{\alpha-1,\beta+1}(p_\alpha,w_\beta)\\
&-
2\sum_{\alpha+\beta=\sigma}
u_\alpha D_\beta u_\beta,
\end{aligned}
}
\]

with

\[
\boxed{
w_\sigma=K_{\sigma-1}p_\sigma.
}
\]

All nonlinear sums must include the full angular content of the products.

Do not project the nonlinear products prematurely onto the nominal angular truncation.

### Recursive coefficient elimination

At the leading dynamic sector, retain the independent coefficients allowed by the equations.

At each later nonresonant weight:

1. Determine the required \(u_\sigma\) coefficients.
2. Determine the required \(w_\sigma\) coefficients.
3. Recover the corresponding \(p_\sigma\) coefficients through Poisson.
4. Retain independent external multipole coefficients where allowed.
5. Handle any resonant compatibility conditions explicitly.

Where the equations are triangular, use exact algebraic coefficient elimination instead of adding penalty terms.

### Logarithmic sectors

Let

\[
\tau=\log(r/L).
\]

When coefficient functions are polynomials in \(\tau\), use the operators

\[
\boxed{
T_\sigma
=
1-\lambda\sigma+\lambda\partial_\tau,
}
\]

\[
\boxed{
P_\sigma
=
K_{\sigma-1}
+(2\sigma-5)\partial_\tau
-\partial_{\tau\tau}.
}
\]

Implement a finite polynomial-coefficient solver for the resonant equations.

It must reproduce the pure-power equations when the logarithmic degree is zero.

### Choosing the protected asymptotic order

Choose a modest initial protection order \(S\), then increase it systematically if needed.

The first priority is faithful reconstruction of the reference fields.

Do not use an unnecessarily high cancellation order that makes the representation poorly conditioned or unable to fit the checkpoint.

However, once an order \(S\) is selected, its constraints must be enforced exactly.

Report the chosen \(S\), the constrained sectors, and the number of remaining free coefficients.

If the representation needs more angular modes or additional multipole coefficients, increase the representation rather than violating the constraints.

---

## 9. Interior spectral correction space

The asymptotic basis alone may be inadequate for reconstructing the core and near-axis layers.

Add smooth interior correction modes that do not modify the protected far-field coefficients.

A possible family is

\[
\boxed{
I_{n,\ell}^{(M)}
=
B_{M,\ell}
P_n^{(\alpha,\beta)}
\left(
\frac{2L^2}{L^2+r^2}-1
\right),
}
\]

where \(P_n^{(\alpha,\beta)}\) is a Jacobi polynomial.

Choose the decay order \(M\) sufficiently large that these corrections do not affect the protected residual sectors.

For the common-weight protection order \(S\), sufficient choices include

\[
M_U>S,
\qquad
M_\Psi+1>S,
\]

with analogous higher orders for any additional derivative-sensitive conditions.

The exact Poisson image of each \(\Psi\) correction must be included automatically in \(\Omega\).

The interior basis must be flexible enough to reproduce:

- Local extrema and their curvature.
- The thickness and position of near-axis structures.
- Intermediate-scale transitions.
- The correct shapes of all three fields.
- The existing profile's characteristic length scales.

Explore radial and angular enrichment only as necessary for reconstruction.

If a single global radial scale is inadequate, consider a small number of complementary numerical scales or locally adapted smooth basis families, while preserving exact Poisson coupling and protected far-field cancellations.

Do not introduce new physical boundary conditions.

---

## 10. Reconstructing the actual case6 checkpoint

### 10.1 Locate and audit the reference

Inspect the existing case6 package.

Identify:

- The best available checkpoint.
- The actual representation used for each field.
- The coordinate conventions and normalization.
- The reference values of \(\lambda,C\).
- The domain and sampling methods.
- The geometry and locations of important extrema.
- The known near-axis numerical issues.
- The current characteristic spatial scales.
- Existing independent residual evaluations.

Do not assume that the published paper's normalization and the saved checkpoint's implementation are identical without verifying them.

### 10.2 Build a reference dataset

Evaluate the reference fields on representative samples covering:

- The core.
- Near-axis layers.
- Intermediate radii.
- Far-field regions.
- Regions containing extrema and strong derivatives.

Use independent validation samples not included in the reconstruction fit.

Do not let a very large collection of low-amplitude far-field points dominate the fitting objective at the expense of the core.

Likewise, do not fit only the core while losing the far-field structure.

Use appropriate regional weighting and amplitude normalization.

### 10.3 Project into the constrained spectral representation

Construct the spectral coefficients from reference field data.

For each candidate \(C\), the physical-to-spectral coordinate transformation changes accordingly.

Begin with stable linear or variable-projection methods where possible.

Solve for dependent asymptotic coefficients exactly.

Fit the genuinely free coefficients to the reference fields.

Use nonlinear fitting only where required by the constraint parameterization, the variable \(C\), or other essential nonlinear representation parameters.

### 10.4 Fit all three fields consistently

Because

\[
\Omega=-\Delta_5\Psi
\]

holds exactly in the spectral representation, the three fields are not independent.

A reasonable reconstruction objective is

\[
\boxed{
\mathcal L_{\rm recon}
=
w_U E_U
+w_\Omega E_\Omega
+w_\Psi E_\Psi
+w_{\rm deriv}E_{\rm deriv},
}
\]

where each error term measures discrepancy from the reference checkpoint, with well-defined regional weights and normalizations.

The derivative term, when used, must compare derivatives with the reference fields. It is not a PDE residual penalty.

Do not introduce

\[
\|\mathcal R_U\|^2
\quad\text{or}\quad
\|\mathcal R_\Omega\|^2
\]

into the reconstruction loss.

No Poisson residual loss is needed because the Poisson equation is already exact.

Do not add far-field residual penalties for sectors already eliminated algebraically.

### 10.5 Allow C to vary

Initialize

\[
C=9.37120536910309.
\]

Optimize \(C\) jointly with the free spectral coefficients.

Keep

\[
\lambda=0.4989408258587428
\]

unchanged.

Record how the fitted value of \(C\) evolves and whether allowing it to vary materially improves the reconstruction.

When \(C\) changes, recompute the shifted coordinates, the dependent coefficients, and all relevant basis evaluations.

Do not allow arbitrary recentering of the reference data to conceal coordinate or phase errors.

If \(C\) is weakly identifiable because of translation gauge freedom, diagnose the degeneracy explicitly.

### 10.6 Resolution continuation

Start with a relatively small representation and increase its capacity.

Possible refinements include:

- Additional angular modes.
- Additional radial modes.
- More interior correction functions.
- Multiple smooth representation scales.
- A higher protected far-field order.
- Higher-precision calculations near resonances.

At each stage, initialize from the best previous spectral reconstruction.

Judge progress by independent reconstruction accuracy, not by the Euler PDE residual.

Save useful intermediate checkpoints as well as the final best reconstruction.

---

## 11. Independent mathematical and numerical validation

The final implementation must contain tests independent of the fitting loss.

### 11.1 Exact Poisson identity

Verify

\[
-\Delta_5\Psi_{\rm sp}-\Omega_{\rm sp}=0
\]

through the analytic coefficient map.

Independently compare with high-precision differentiation at representative points, including the axis.

Report finite-precision discrepancies separately from the exact algebraic identity.

### 11.2 Canonical global Poisson consistency

Check that the represented fields have the required global decay and exclude arbitrary entire harmonic additions.

For appropriate test points, independently compare the analytic spectral potential with the five-dimensional Newton potential generated by \(\Omega_{\rm sp}\).

### 11.3 Far-field coefficient cancellation

Extract the asymptotic coefficients independently from the final representation.

Verify that all protected residual sectors vanish algebraically, including:

- Mixed dynamic and multipole interactions.
- Generated high angular harmonics.
- Resonant logarithmic terms.
- Corrections induced by the global smooth basis functions.

Do not infer exact cancellation from small sampled far-field residual values alone.

### 11.4 Reconstruction accuracy

On an independent validation set, compare

\[
U_{\rm sp}\ \text{vs.}\ U_{\rm ref},
\]

\[
\Omega_{\rm sp}\ \text{vs.}\ \Omega_{\rm ref},
\]

\[
\Psi_{\rm sp}\ \text{vs.}\ \Psi_{\rm ref}.
\]

Report global and region-wise absolute and relative RMS errors, maximum errors, and the locations of the largest discrepancies.

Also compare important derivatives, extrema, near-axis layers, and characteristic spatial scales.

Include plots of the reconstructed fields, original fields, and their differences if feasible.

### 11.5 Euler residual diagnostic — evaluation only

After reconstruction, independently evaluate

\[
\mathcal R_U,\qquad\mathcal R_\Omega
\]

for the reconstructed spectral profile.

Compare them with the corresponding residuals of the original case6 checkpoint using the same coordinates, sample points, and residual normalizations.

The earlier six-million-point reference audit reported approximately

\[
\mathrm{RMSE}(\mathcal R_U)
=1.12\times10^{-5},
\]

\[
\mathrm{RMSE}(\mathcal R_\Omega)
=1.95\times10^{-5},
\]

\[
\mathrm{RMSE}(\mathcal R_{\rm Poisson})
=3.59\times10^{-5}.
\]

These values are reference diagnostics, not guaranteed accuracies or acceptance thresholds.

The spectral representation should make the Poisson identity exact in arithmetic, but the transport residual may initially increase or decrease.

**Do not optimize the transport residual after observing this comparison.**

The purpose is to determine the quality of the spectral reconstruction as a starting point for Phase 2.

Report both the numerical residuals and any known limitations in the diagnostic sampling.

---

## 12. Required implementation architecture

Produce a reusable implementation with the following components:

**A. Basis evaluator**

Evaluates the rational, Gegenbauer, pure-tail, logarithmic, and interior correction functions and their necessary derivatives.

**B. Exact Poisson mapper**

Reconstructs \(\Omega\) from \(\Psi\) analytically.

**C. Asymptotic coefficient compiler**

Builds the Euler far-field sectors, nonlinear weight combinations, and full generated angular content.

**D. Constraint solver**

Eliminates dependent coefficients, including resonance-compatible logarithmic coefficients.

**E. Parameterization**

Maps the free spectral coefficients and the variable \(C\) into the full profile, with \(\lambda\) fixed.

**F. Reference-field evaluator**

Loads and evaluates the original case6 checkpoint on selected physical points.

**G. Reconstruction fitter**

Minimizes the discrepancy with the reference profile, using suitable conditioning, normalization, and stable optimization algorithms.

**H. Independent validator**

Checks Poisson coupling, asymptotic cancellations, reconstruction accuracy, and Euler residual diagnostics.

**I. Checkpoint exporter**

Saves all free coefficients, derived coefficients, basis configuration, \(C\), fixed \(\lambda\), and normalization information needed to reproduce the profile and initialize Phase 2.

All reported results must be reproducible from saved code and checkpoints.

---

## 13. Work priorities and computational budget

Prioritize the following sequence:

1. Verify the actual reference checkpoint and governing equations.
2. Implement the exact-Poisson spectral evaluator.
3. Verify stable evaluation near the axis.
4. Implement finite-order far-field constraints.
5. Perform the first constrained projection of the actual checkpoint.
6. Identify the dominant reconstruction errors.
7. Increase spectral resolution where those errors occur.
8. Jointly refine the free spectral coefficients and \(C\).
9. Perform independent reconstruction and PDE-residual evaluations.
10. Save and report the best spectral reconstruction.

Do not start a lengthy PDE optimization campaign.

Use computational resources for reconstruction fitting, basis evaluation, resolution comparisons, and independent validation.

Avoid unnecessary high-cost global experiments before a basic spectral reconstruction is working.

If a particular spectral family performs poorly, inspect whether the problem is caused by conditioning, incompatible asymptotic constraints, inadequate angular resolution, or insufficient interior flexibility.

Make targeted improvements rather than abandoning exact Poisson coupling or the required asymptotic structure.

Do not use the mathematical obstruction at fixed \(\lambda<1/2\) as a reason to skip reconstruction. That obstruction concerns exact nontrivial globally smooth PDE solutions in the specified class, not the finite-accuracy approximation of an existing numerical field.

---

## 14. Required final report

At completion, provide the following.

### A. Reconstructed profile

Identify the best spectral checkpoint, its coefficient counts, basis orders, numerical scales, and fitted \(C\).

Confirm that \(\lambda\) remained fixed throughout.

### B. Reconstruction accuracy

Report a table comparing the original and spectral profiles for \(U,\Omega,\Psi\), including independent RMS and maximum errors and their locations.

Show where remaining reconstruction errors are concentrated.

### C. Structural correctness

Report:

- Exact Poisson coefficient identity.
- Canonical inverse consistency.
- Axis regularity.
- Protected far-field sectors.
- Resonance handling.
- The number of free and dependent coefficients.

Clearly separate exact algebraic identities from finite-precision numerical tests.

### D. Transport residual comparison

Report the original and reconstructed Euler transport residuals on identical independent samples.

Do not perform any residual optimization.

### E. Effect of fitting C

Report the initial and fitted values of \(C\).

Explain whether its variation improved reconstruction and whether the fitted value is identifiable under the existing normalization.

### F. Phase 2 initialization

Save the final spectral checkpoint in a form that can be directly loaded by a later PDE optimizer.

Identify the dominant remaining transport residual errors, but do not optimize them.

### G. Unresolved issues

Identify any limitations associated with spectral truncation, near-resonance conditioning, reference-checkpoint accuracy, incompatible far-field coefficients, or inadequate numerical resolution.

---

## 15. Strict stopping condition

**Stop when Phase 1 is complete.**

Do not proceed to:

- Fixed-lambda Euler PDE optimization.
- Changing or continuing \(\lambda\).
- Searching for a new unrelated Euler profile.
- Modifying the reference checkpoint.
- Claiming an exact nontrivial solution from the reconstruction alone.

The final product is a constrained spectral reconstruction of the existing case6 profile.

It must:

1. Keep \(\lambda=0.4989408258587428\) fixed.
2. Allow \(C\) to be fitted.
3. Reproduce the existing numerical fields as accurately as possible.
4. Enforce Poisson coupling exactly.
5. Enforce selected finite-order far-field residual cancellations exactly.
6. Preserve axis regularity and the reference profile's geometry.
7. Provide independent reconstruction and PDE-residual diagnostics.
8. Produce a saved checkpoint ready for Phase 2.

**The success criterion for this phase is reconstruction fidelity under exact structural constraints — not minimization of the Euler transport residual.**

Begin by inspecting the actual case6 code and checkpoint, then implement and test the constrained spectral representation and perform the reconstruction. Do not stop at a theoretical proposal.