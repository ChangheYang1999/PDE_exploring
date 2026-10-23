# Research task: two-fold 3D Euler self-similar profiles by traditional multicore spectral bases, staged z parity, and scaling-invariant residual minimization

## 0. Mission and execution contract

Carry out an actual, long-duration numerical PDE research campaign to search for smooth, genuinely non-axisymmetric, two-fold rotationally symmetric, stationary self-similar profiles of the **full incompressible 3D Euler equations on R^3**, concentrating on

\[
\boxed{\frac25<c_l<\frac12.}
\]

**This is a separate and genuinely different approach from the PINN/neural-network approach.** The main solver must be a finite-dimensional, explicit, smooth **spectral/algebraic basis expansion**, with nonlinear minimization of a **scaling-invariant PDE residual functional**. Use analytical Taylor and far-field expansions to cancel as many low-order residual coefficients as possible *before* numerical optimization. Neural networks may be used only for optional external comparisons, not as the primary representation or solver.

The inspiration is a previous traditional-basis approach to self-similar IPM: form potentials from harmonic polynomials multiplied by flexible algebraic weights such as powers of \(1+R^2\), then obtain physical fields by differentiation so that structural constraints are exact. For orientation, one prior 2D IPM ansatz used

\[
 \chi(x,y)=\sum_{m=0}^{3}\sum_{k=0}^{4}c_{mk}
 \operatorname{Re}[(x+iy)^{2m}](1+x^2+y^2)^{(3+1/c_l)/2-m-\sigma_k},
\]

with \(\sigma_k\in\{0,1,2,\delta,2\delta\}\), \(\delta=(1-1/c_l)/2\), then generated IPM fields from derivatives of \(\chi\). This is only the **design philosophy**, not an Euler ansatz or a permitted reduction. Extend it to a *fully three-dimensional divergence-free vector field*. Do not copy the 2D IPM symmetry, equations, half-space, or scalar potential formulas into Euler.

Execute **at least 96 hours of measured, non-overlapping active numerical experiment time**, resources and permissions permitting, including broad search and independent verification. This is not merely a plan-writing or pilot task. Maintain restartable checkpoints and an auditable ledger; if continuous operation is impossible, record actual executed time and give an exact one-command resume path, without claiming the unexecuted hours.

**Compute strategy:** This is a traditional finite-dimensional basis/least-squares project, not a GPU-first PINN project. **Use genuinely parallel multicore CPU computation as the default and primary backend.** Inspect physical cores, available logical CPUs, CPU affinity/cgroup or scheduler allocation, RAM, NUMA layout, and pre-existing jobs; benchmark threaded quadrature, basis evaluation, Jacobian assembly, numerical linear algebra, and independent multistarts. Use a substantial fraction of the cores actually allocated to this project when efficient and authorized; do not silently run a costly 96-hour campaign on one core. Control BLAS threads versus parallel workers to prevent oversubscription. GPU acceleration is optional only when an actual FP64 benchmark demonstrates an advantage, never a prerequisite; there is **no A100 requirement and no eight-GPU scale-up plan**. Never allocate unauthorized/paid resources.

**Symmetry strategy:** Start with a genuine Euler-compatible reflection about the equatorial plane, so horizontal velocity and pressure are even in z and vertical velocity is odd in z. If a properly tested first phase yields no credible profile, explicitly lift this extra symmetry and search the full two-fold-equivariant three-dimensional class, borrowing the *no-z-parity, optional axially traveling center* philosophy of Ganeshram–Duruisseaux–Anandkumar, not their axisymmetric reduction or PINN solver. Do not wait all 96 hours before releasing the symmetry if it is clearly unproductive.

The desired outcome is credible mathematical/numerical evidence, not an arbitrarily small loss, a preselected exponent, or a claim that elapsed time proves existence.

## 1. Self-similar Euler equations and physical significance

Write \(\tau=T-t>0\) and \(y=(x-x_*)/\tau^{c_l}\), with \(x_*\) on the fixed \(z\)-axis. Set

\[
 u(x,t)=\tau^{c_l-1}U(y),\qquad
 p(x,t)=\tau^{2c_l-2}P(y),\qquad
 \Omega=\nabla\times U.
\]

The exact stationary system is

\[
 \mathcal R_m=(1-c_l)U+(c_l y+U)\cdot\nabla U+\nabla P=0,
 \qquad \nabla\cdot U=0. \tag{E}
\]

A removable axial recentering parameter is allowed:

\[
 V=c_l y+C e_z+U,\qquad
 \mathcal R_m=(1-c_l)U+V\cdot\nabla U+\nabla P.
 \tag{E_C}
\]

The change \(Y=y+(C/c_l)e_z\), \(\widehat U(Y)=U(Y-(C/c_l)e_z)\), removes \(C\). Do not treat \(C\) as a new physical exponent or source of instability. Verify the equations and signs independently.

The vorticity and pressure identities are

\[
 \mathcal R_\Omega=\Omega+V\cdot\nabla\Omega-(\Omega\cdot\nabla)U=0,
 \tag{V}
\]
\[
 -\Delta P=\sum_{i,j}\partial_i U_j\,\partial_j U_i
 =\nabla\cdot[(U\cdot\nabla)U]
 \qquad (\nabla\cdot U=0).
 \tag{P}
\]

The original physical initial data need not equal the similarity profile everywhere. Do not require \(U\in L^2(\mathbb R^3)\). Indeed a nontrivial core contributes physical kinetic energy of order \(\tau^{5c_l-2}\), motivating the range \(c_l>2/5\). For positive viscosity, the corresponding rescaled NS viscosity coefficient is \(\nu e^{-(1-2c_l)s}\), \(s=-\log\tau\); \(c_l<1/2\) makes it decay. **An Euler profile by itself does not establish an NS singularity.**

## 2. Two-stage symmetry hierarchy: start z-reflection-odd, then release it

For **both** stages let \(Q=\operatorname{diag}(-1,-1,1)\). Impose the exact two-fold rotational equivariance

\[
 U(Qy)=QU(y),\qquad P(Qy)=P(y). \tag{S1}
\]

In cylindrical **vector** components, all \(U^r,U^\theta,U^z,P\) are \(\pi\)-periodic in \(\theta\), with angular Fourier modes \(m=0,\pm2,\pm4,\ldots\). Retain both sine and cosine content. The axisymmetric mean is free because nonlinear interactions generate it. A pure \(m=0,\pm2\) cutoff is not invariant under the PDE; resolve generated \(m=4,6,\ldots\) in refinement. Cartesian horizontal components are equivariant vector components, not scalar \(\pi\)-periodic functions.

### Stage A — impose an Euler-compatible odd z symmetry first

Let \(S=\operatorname{diag}(1,1,-1)\) and impose the *physical vector reflection*

\[
 \boxed{U(Sy)=S U(y),\qquad P(Sy)=P(y).} \tag{S2}
\]

Equivalently, in cylindrical coordinates,

\[
\begin{aligned}
 U^r(r,\theta,-z)&= U^r(r,\theta,z),\\
 U^\theta(r,\theta,-z)&= U^\theta(r,\theta,z),\\
 U^z(r,\theta,-z)&=-U^z(r,\theta,z),\\
 P(r,\theta,-z)&=P(r,\theta,z).
\end{aligned}
\]

**This is what 'odd in z' means in this project. It does not mean that every Cartesian velocity component is odd in z.** Verify that these are exact symmetries of the unforced incompressible Euler system. Since \(QS=-I\), the combined two-fold rotation and z-reflection imply

\[
 \boxed{U(-y)=-U(y),\qquad P(-y)=P(y).} \tag{S3}
\]

Thus \(U(0)=0\), the stationary similarity transport vanishes at the origin in canonical coordinates, only *odd total Taylor degrees* appear in \(U\), and only *even total Taylor degrees* appear in \(P\). Here take \(C=0\): a fixed nonzero \(C e_z\) is not compatible with the reflection about \(z=0\) (apart from special degenerate cases). The parity is a deliberate **restricted initial search branch**, not a theorem about all two-fold profiles.

For the poloidal–toroidal basis in Section 5 and even azimuthal \(m\), this reflection can be enforced exactly by retaining **even \(\ell\) poloidal modes and odd \(\ell\) toroidal modes**; verify this against the Cartesian vector action. Pressure admits even \(\ell\). In the Cartesian-potential basis, project the **velocity** to (S1)–(S2) (and use the correct axial-vector reflection rule for a vector potential when the reflection has determinant \(-1\)); do not naively project a pseudovector potential as if it were a polar vector.

Do not additionally impose individual x/y reflections, no-swirl, axisymmetry, or the location of maximum vorticity.

### Stage B — general two-fold class without z parity

If Stage A produces no convincing profile after genuinely varied seeds, exponents, and independently checked residuals (or is analytically obstructed under its own assumptions), **remove (S2) and (S3) completely**. Keep only (S1), exact incompressibility, smoothness, and justified decay/matching constraints.

Allow **all** \(\ell\ge |m|\) for every even \(m\), in *both* poloidal and toroidal sectors, including the polar parities excluded in Stage A. Pressure must likewise regain both polar parities. Add symmetry-breaking seed coefficients; merely lifting a mask without perturbing a parity-invariant seed can leave an optimizer confined to Stage A.

Borrow the relevant methodological feature of Ganeshram–Duruisseaux–Anandkumar, arXiv:2609.10867: their axisymmetric numerical work uses a traveling axial center and **does not impose z parity**, and reports that z-parity constraints impaired optimization. **Do not switch our problem to their axisymmetric \(\Gamma\)-\(\eta\) equations, use their axisymmetric parity as a boundary condition, or replace our basis solver with a PINN.** Instead use the full 3D equations (E_C) with a free, removable \(C\) if helpful for the optimization landscape, plus one compatible axial-centering gauge. Verify the translation to canonical \(C=0\) coordinates and include translation-induced far-field corrections if working in moving coordinates. Do not impose \(U(0)=0\), an on-axis stagnation point, or a z-reflection gauge on all Stage B profiles.

Compare Stage A and B using the same intrinsic scaling, residual definitions, and independent validation. A candidate with actual z parity may persist in Stage B; do not reject it merely because the larger class allows symmetry breaking. Do not infer nonexistence in Stage A or B from solver failure.

### Common axis regularity

At the fixed axis, Cartesian smoothness for any two-fold-equivariant field gives

\[
 U_1=a(z)x+b(z)y+O(r^3),\quad
 U_2=c(z)x+d(z)y+O(r^3),\quad
 U_3=w(z)+O(r^2),
\]
\[
 a(z)+d(z)+w'(z)=0,\qquad r=(x^2+y^2)^{1/2}.
\]

A general transverse \(2\times2\) matrix is required: genuine two-fold velocity can be \(O(r)\), not necessarily \(O(r^3)\). In Stage A, \(a,b,c,d\) are even functions of z and \(w\) is odd. In Stage B these parity restrictions are absent.

## 3. Mandatory analytical phase I: origin Taylor cancellation, separately for both symmetry stages

**Before large-scale optimization**, derive the local power-series structure of (E_C), including algebraic compatibility and nullspaces. Make as many low-order momentum, divergence, vorticity, and pressure-consistency residual coefficients vanish as the equations permit, before nonlinear coefficient fitting. Do not force an inconsistent Taylor series or set unconstrained higher-order jets to zero by default.

### Stage A: the origin is automatically a stagnation point

Under (S1)–(S3), work in canonical \(C=0\) coordinates and use

\[
 \boxed{U(y)=U_1(y)+U_3(y)+U_5(y)+\cdots,\quad
 P(y)=P_0+P_2(y)+P_4(y)+P_6(y)+\cdots.} \tag{O0}
\]

All \(U_k,P_k\) are homogeneous Cartesian polynomials of the stated degree with the exact discrete symmetry; \(\nabla\cdot U=0\) must be imposed coefficientwise. The restriction to odd/even degrees follows from the **two** discrete symmetries, not from an independent new ansatz. Since \(U(0)=0\), \(V(0)=0\) automatically. Set

\[
 A=\nabla U(0)=\begin{pmatrix}a&b&0\\c&d_0&0\\0&0&e\end{pmatrix},\qquad
 a+d_0+e=0,
\]

using a distinct name for the matrix entry \(c\) and exponent \(c_l\). Degree one in the Euler momentum equation yields

\[
 \boxed{A+A^2+D^2P(0)=0.} \tag{O1}
\]

If \(\Omega(0)=(0,0,c-b)\ne0\), the vorticity equation forces \(e=1\), hence \(a+d_0=-1\). The transverse block \(M=\begin{pmatrix}a&b\\c&-1-a\end{pmatrix}\) satisfies by Cayley–Hamilton

\[
 M+M^2=-\det(M)I_2,\quad
 \boxed{D^2P(0)=\operatorname{diag}(\det M,\det M,-2),}\quad
 P_2=\frac{\det M}{2}(x^2+y^2)-z^2. \tag{O2}
\]

Verify this independently from both momentum and pressure Poisson identities. Treat it as **one branch**; when \(\Omega(0)=0\), do not impose \(e=1\). Include branches with off-axis vorticity maxima despite on-axis symmetry.

For a general stagnation-centered expansion \(U=U_0+\sum_{k\ge1}U_k\), \(V(0)=0\), the homogeneous degree-\(k\) equations are

\[
\begin{aligned}
0={}&(1-c_l)U_k+[(c_lI+A)y]\cdot\nabla U_k+A U_k
+\nabla P_{k+1}\\
&+\sum_{\substack{i,j\ge2\\i+j-1=k}}
(U_i\cdot\nabla)U_j,\qquad k\ge2. \tag{Ok}
\end{aligned}
\]

The displayed double sum is empty at degree two. **In Stage A, \(U_2=U_4=\cdots=0\) and \(P_1=P_3=\cdots=0\) by symmetry; all even-degree equations must vanish automatically as a consistency check.** For example, the first genuinely nonlinear higher-jet compatibility equation involves the cubic field \(U_3\) and quartic pressure \(P_4\). Derive all recurrences independently using polynomial algebra and solve for as many admissible jet coefficients as practical, ideally through degree 5 or higher. Retain genuine free directions instead of making the approximate profile artificially affine.

### Stage B: restore all allowed Taylor degrees and general axial centering

After removing z parity, keep only (S1). At the axis, \(U(0)=u_0e_z\) need not vanish, \(\nabla P(0)\) may contain an axial component, and **both odd and even polynomial degrees must be retained** when compatible with (S1). Allow \(C\ne0\) as a freely optimized, removable axial translation parameter. Choose a single centering convention and ensure it does not simultaneously fix unrelated jets.

If \(V(0)=0\) happens to hold for a branch, take \(C=-u_0\) and use the stagnation-centered (O1)–(Ok) equations, with the degree-zero condition \(\nabla P_1=-(1-c_l)u_0e_z\). If the chosen origin is **not** a stagnation point, do not apply (O1)–(Ok) unchanged: the Taylor equations contain the extra transport coupling \(V(0)\cdot\nabla U_{k+1}\), and all appropriate constant/linear pressure terms. Derive that general recurrence separately or solve the coupled jet system. Never assume every profile has an axial zero of the similarity transport.

When switching stages, reintroduce all jets excluded by (S2)–(S3), include genuinely symmetry-breaking perturbations, and recompute the local constraints. A Stage A Taylor parametrization with only odd velocity degrees is **not** a full Stage B parametrization.

### Shared small-radius audit

Use exact symbolic or high-precision polynomial algebra to derive allowed jets and compatibility conditions. Check against direct Cartesian differentiation and the vorticity equation. On shrinking spheres and balls, report the observed powers \(\|\mathcal R_m\|(R)\sim R^q\), compared with the first analytically predicted uncancelled term. A small absolute residual at small R is not a substitute for removal of lower-order Taylor coefficients. Also check origin regularity and derivative convergence under angular/radial refinement.

## 4. Mandatory analytical phase II: correct far-field hierarchy and cancellation

Set \(R=|y|\), \(n=y/R\), and

\[
 d=1-\frac1{c_l}\in(-\tfrac32,-1).
\]

**All formulas (F1)-(F9) below are in the canonical \(C=0\) coordinates.** This distinction is essential: the near-origin analysis may instead center an axial stagnation point and have \(C=-u_0\ne0\). The two coordinate descriptions are related by the *exact* translation \(Y=y+(C/c_l)e_z\). If using the stagnation-centered coordinates to test tails, explicitly pull back the canonical asymptotics or include the translation-induced hierarchy \(R^{d-j}\), \(j=1,2,\dots\), and its nonlinear mixtures. In particular, \(C\partial_z(R^dA_1)\) has degree \(d-1\) and must be cancelled; it is **not** part of the pure \(\lambda_k=1-k/c_l\) nonlinear cascade. Never optimize inconsistent origin-centered and canonical tail expansions.

**Stage dependence:** In Stage A every velocity tail coefficient must satisfy \(A_k(-n)=-A_k(n)\) and \(A_k(Sn)=S A_k(n)\); pressure angular coefficients must be even under inversion and z-reflection. Enforce these selection rules in the nonlinear cascade and allowable multipoles (not just in the leading basis). In Stage B delete these restrictions and allow both polar parities, all permitted m=2-compatible pressure multipoles and their matching corrections. An origin-centered z-parity profile has \(C=0\), while a general Stage B moving-center profile may have \(C
e0\); handle the resulting translation cascade before comparing tail residuals.

The natural leading asymptotic search class in canonical coordinates is

\[
 U(R,n)\sim R^d A_1(n),\qquad P(R,n)\to P_\infty,
\]

with \(\Omega,\nabla U=O(R^{-1/c_l})\). This is a *testable asymptotic ansatz*, not a theorem that excludes every other profile class. At leading order the linear similarity operator annihilates \(R^d A_1\), while incompressibility imposes

\[
 (d+2)(A_1\cdot n)+\operatorname{div}_{\mathbb S^2}(A_{1,T})=0,
 \qquad A_{1,T}=A_1-(A_1\cdot n)n.
 \tag{F1}
\]

A **single leading tail cannot cancel the nonlinear residual**. Develop the nonlinear asymptotic hierarchy

\[
 U(R,n)\sim\sum_{k=1}^K R^{\lambda_k}A_k(n),
 \qquad \lambda_k=1-\frac{k}{c_l},
 \tag{F2}
\]
\[
 P(R,n)-P_\infty\sim\sum_{k=2}^K R^{\mu_k}p_k(n)
 +\text{admissible homogeneous-pressure/mixed corrections},
 \qquad\mu_k=2-\frac{k}{c_l}=\lambda_k+1.
 \tag{F3}
\]

The similarity linear operator on the \(k\)-th velocity term has the **exact coefficient**

\[
 (1-c_l)+c_l\lambda_k=1-k.
 \tag{F4}
\]

Thus the \(k=1\) tail is free at the linear level; for every \(k\ge2\), lower-order nonlinear interactions produce a solvable coefficient equation away from angular resonances.

**Derive rather than assume the recursion.** For a homogeneous angular vector \(A_j(n)\), define the ambient Cartesian angular derivative and let

\[
 \mathcal N_k(n)=\sum_{i+j=k}
 \left[\lambda_j(A_i\cdot n)A_j
 +(A_{i,T}\cdot\nabla_{\mathbb S^2})A_j\right].
 \tag{F5}
\]

Then the required identities are

\[
 (1-k)A_k+\mathcal N_k
 +\mu_k p_k n+\nabla_{\mathbb S^2}p_k=0,
 \tag{F6}
\]
\[
 (\lambda_k+2)(A_k\cdot n)
 +\operatorname{div}_{\mathbb S^2}(A_{k,T})=0.
 \tag{F7}
\]

Taking divergence and eliminating \(A_k\) leads to

\[
 \left[\Delta_{\mathbb S^2}+\mu_k(\mu_k+1)\right]p_k
 =-(\lambda_k+2)(\mathcal N_k\cdot n)
 -\operatorname{div}_{\mathbb S^2}\mathcal N_{k,T},
 \tag{F8}
\]
\[
 A_k=\frac{1}{k-1}
 \left[\mathcal N_k+\mu_k p_k n+\nabla_{\mathbb S^2}p_k\right].
 \tag{F9}
\]

Derive (F5)-(F9) with exact signs and numerical unit tests, remembering that \(\nabla_{\mathbb S^2}\) on a vector acts on its **Cartesian components**, including geometric effects. In particular, the first nonlinear correction is degree \(2d-1=1-2/c_l\), its pressure is degree \(2d=2-2/c_l\), and its linear coefficient is \(-1\). **Do not impose merely a homogeneous leading tail and ask the optimizer to repair an analytically unavoidable \(R^{2d-1}\) defect.**

**Resonances and global pressure matter.** The angular operator in (F8) can become noninvertible for special values of \(c_l\), causing solvability conditions and possibly \(R^\mu\log R\) terms. Detect such exponents rather than regularizing a singular inverse without explanation. In addition, the whole-space Poisson problem can generate exterior harmonic pressure multipoles \(R^{-(\ell+1)}Y_{\ell m}(n)\); their gradients and induced solenoidal velocity corrections may lie **between** successive exponents in (F2). For example, a pressure quadrupole \(R^{-3}Y_{2m}\) has a gradient of degree \(-4\), which can interleave the nonlinear tail levels for the target \(c_l\) range. Its amplitude is determined by global matching, not by an arbitrary external forcing. Do **not** assume the pure \(\lambda_k\) cascade is a complete asymptotic expansion.

Derive the allowable exterior harmonic/mixed terms and their interleaving order, and either include them or show rigorously that a particular coefficient vanishes. Pressure monopole and dipole cancellations, if claimed, must be justified from the global divergence structure and the actual decay/integrability hypotheses. Preserve the possible contribution of finite core moments and do not force the pressure to be exactly homogeneous outside a cutoff.

The tail correction protocol is:
1. Choose a free divergence-free leading angular field \(A_1\).
2. Compute \(\mathcal N_2\), solve (F8) for \(p_2\), and compute \(A_2\).
3. Recursively cancel as many subsequent forced orders as possible, including resonant logarithms when needed.
4. Interleave permitted exterior harmonic pressure/velocity modes and match them with a **whole-space** pressure calculation.
5. Quantify residuals against the **first genuinely uncancelled nonlinear or harmonic order**, not against two large leading linear terms that cancel automatically.

Verify by direct substitution that each added tail correction increases the measured far-field residual decay order on successively more distant shells. If the series proves asymptotic but poorly behaved at moderate \(R\), use smooth algebraic basis transitions, not unjustified hard asymptotics in the core.

## 5. Primary finite-dimensional basis: exactly divergence-free poloidal–toroidal spherical harmonics

Use **real spherical harmonics** \(Y_{\ell m}\), including both cosine and sine functions for \(m=2,4,\dots\) and \(m=0\), with \(\ell\ge|m|\). **Implement two explicit mode masks, not one permanently restricted basis**: in Stage A retain even-\(\ell\) poloidal and odd-\(\ell\) toroidal harmonics, exactly implementing (S2); in Stage B retain *all* \(\ell\) for each sector. This must be checked under the actual vector-reflection action; do not confuse scalar \(Y_{\ell m}\) parity with polar/toroidal vector parity. Never carry the Stage A mask into Stage B.

For \(\ell\ge1\), represent

\[
 \begin{aligned}
 U(R,n)=\sum_{\ell,m}\Big[&
 \frac{\ell(\ell+1)}{R^2}s_{\ell m}(R)Y_{\ell m}(n)n
 +\frac{s'_{\ell m}(R)}{R}\nabla_{\mathbb S^2}Y_{\ell m}(n)\\
 &+t_{\ell m}(R)n\times\nabla_{\mathbb S^2}Y_{\ell m}(n)
 \Big].
 \end{aligned} \tag{B1}
\]

The divergence vanishes **identically** for arbitrary smooth radial \(s,t\). Prove this, test it numerically, and use an independent Cartesian divergence check. Smoothness at \(R=0\) is guaranteed by using regular radial powers with even smooth corrections, for example

\[
 s_{\ell m}(R)=R^{\ell+1}S_{\ell m}(R^2),\qquad
 t_{\ell m}(R)=R^\ell T_{\ell m}(R^2)
 \quad\text{near }0.
 \tag{B2}
\]

A concrete global algebraic radial family is obtained by defining

\[
 q=\frac{R^2}{L^2+R^2},\qquad d=1-1/c_l,
\]
\[
 s_{\ell m}(R)=R^{\ell+1}
 (1+R^2/L^2)^{(d+1-\ell)/2}
 \sum_{j=0}^{N_s} a_{\ell mj}\,\Phi_j(q),
 \tag{B3}
\]
\[
 t_{\ell m}(R)=R^\ell
 (1+R^2/L^2)^{(d-\ell)/2}
 \sum_{j=0}^{N_t} b_{\ell mj}\,\Phi_j(q).
 \tag{B4}
\]

Here \(\Phi_j\) can be Chebyshev, Jacobi, or well-conditioned polynomial combinations in \(q\), with actual endpoint behavior explicitly checked. These give \(U=O(R^d)\) at infinity, allow general \(m=2\) content, and are smooth at the origin. Use appropriate nondimensional factors of \(L\) so conditioning is not driven by units.

**Far-field-aware enrichment:** A general polynomial in \(q\) naturally creates integer \(R^{-2j}\) corrections, whereas (F2) requires fractional relative steps \(R^{-1/c_l}\). Enrich (B3)-(B4) by independent blocks carrying factors

\[
 (1+R^2/L^2)^{-(k-1)/(2c_l)},\qquad k=2,3,\dots,
 \tag{B5}
\]

and by special homogeneous-pressure/multipole-compatible blocks. If the representation is centered at a stagnation point with \(C\ne0\), additionally represent all required translation-induced \(R^{d-j}\) angular modes (or, preferably, apply the exact canonical coordinate translation before the tail expansion). A purely radial \(q\)-polynomial supplies \(R^{-2j}\) steps and **does not** by itself represent the first translation-induced \(R^{-1}\) step. Keep the analytical origin powers (B2) intact. Use constrained leading/tail coefficients so that the forced asymptotic recursions (F6)-(F9) hold to the greatest feasible order rather than fitting inconsistent coefficients independently. Permit additional free angular and transitional corrections that vanish at the relevant endpoints.

Do **not** assume that polynomial regularity at compactified \(q=1\) is natural for fractional tail exponents; explicit fractional powers and, at resonances, logarithms must be represented. Do not suppress subleading powers merely to make Chebyshev convergence appear exponential.

### Alternative basis branch: IPM-style Cartesian harmonic-polynomial potentials

Independently implement or at least pilot a second basis construction, akin to the former IPM calculation:

\[
 \mathcal A(y)=\sum_{i,\ell,j,k} c_{i\ell jk}
 \mathcal S_Q\left[e_i H_{\ell j}(y)
 (1+R^2/L^2)^{-\alpha_{\ell k}}\right],
 \qquad U=\nabla\times\mathcal A.
 \tag{B6}
\]

Here \(H_{\ell j}\) are real homogeneous Cartesian harmonic polynomials, \(\mathcal S_Q F(y)=[F(y)+QF(Qy)]/2\), and the exponents are chosen to realize correct near-origin powers and the required far-field degrees. An initial leading-tail choice is

\[
 \alpha_{\ell,1}=\frac{\ell-1-d}{2},
\]

because curl decreases homogeneous degree by one; add fractions \((k-1)/(2c_l)\) for tail corrections and allow independent radial polynomial factors. Remove gradients of scalar potentials (curl-null directions) from the coefficient space or gauge-fix them by SVD/nullspace analysis. The curl/proper-rotation projection must commute; verify it analytically. **For the Stage A z reflection, a vector potential transforms as an axial (pseudo)vector under the improper reflection**: project \(\mathcal A(Sy)=\det(S)S\mathcal A(y)=-S\mathcal A(y)\), so its curl has the desired polar-vector equivariance \(U(Sy)=S U(y)\). Alternatively, project the computed velocity to the correct symmetry while preserving divergence. In Stage B remove the reflection projection on the potential and restore all permitted modes.

The two basis families need not agree at low truncation: compare attainable approximation power, number of active coefficients, Hessian conditioning, axis accuracy, and tail fidelity. The main method remains **finite-dimensional basis minimization**, not a PINN.

## 6. Explicit local seeds, without freezing an accidental symmetry

For a reproducible first branch take

\[
 M_0=\begin{pmatrix}a&b&0\\c&-1-a&0\\0&0&1\end{pmatrix},
 \qquad \chi(R)=(1+R^2/L^2)^{-1/(2c_l)}.
\]

A smooth equivariant divergence-free seed is

\[
 \mathcal A_{seed}=-\frac13\chi(R)\,[y\times (M_0y)],
 \qquad U_{seed}=\nabla\times\mathcal A_{seed},
 \tag{B7}
\]

since \(\operatorname{tr}M_0=0\) and \(\nabla\times[-y\times(M_0y)/3]=M_0y\). Start, for instance, with \(a=0.2,b=-0.4,c=0.7,c_l=0.45\), alongside many different matrices and genuinely off-axis seed families. A near-origin pressure seed is

\[
 P_{seed}=-\frac12\chi(R)^2\,y^T(M_0+M_0^2)y.
\]

Verify symmetry, smoothness, curl, and leading Taylor coefficients. This family is **only initialization**. Its z parity and full inversion are **appropriate in Stage A**, where they follow from the imposed reflection. In Stage B, those parities are no longer required: explicitly add independent modes of the previously excluded \(\ell\)-parity, symmetry-breaking seeds and off-axis perturbations. Otherwise a solver initialized at this seed may remain stuck in the smaller symmetric subspace despite removal of the mathematical constraint. Search zero-axis-vorticity and off-axis-vorticity branches rather than anchoring everything to the affine core above.

The unlocalized affine \(U=M_0y\), \(P=-y^T(M_0+M_0^2)y/2\) is an **exact residual unit test** for all \(c_l\), but must be explicitly rejected as a final result: it does not have the admissible far field and is affine, even if it has a nonzero \(m=2\) component.

## 7. Pressure: solve the whole-space Poisson problem, not an arbitrary local pressure fit

Prefer one main branch in which velocity coefficients are primary and pressure is *eliminated* by solving (P), followed by a second branch with independently expanded \(P\) and a pressure-Poisson consistency penalty. This reduces false PDE solutions arising from a locally fitted gradient that is inconsistent with the velocity globally.

For each real spherical harmonic, write

\[
 S(y)=\sum_{i,j}\partial_iU_j\partial_jU_i
       =\sum_{\ell,m}S_{\ell m}(R)Y_{\ell m}(n),
\]
\[
 P(y)=\sum_{\ell,m}p_{\ell m}(R)Y_{\ell m}(n),
\]

with pressure constant fixed at infinity where appropriate. The radial Green formula for \(-\Delta P=S\) is

\[
 p_{\ell m}(R)=\frac1{2\ell+1}
 \left[R^{-\ell-1}\int_0^R s^{\ell+2}S_{\ell m}(s)\,ds
 +R^\ell\int_R^\infty s^{1-\ell}S_{\ell m}(s)\,ds\right].
 \tag{P1}
\]

**Derive and unit test (P1), its derivatives, signs, origin regularity, and integrability with our algebraic tails.** Use adaptive/spectral quadrature with analytic or rigorously controlled tail extrapolation. Do not truncate the final integral at the numerical outer radius and call the resulting artificial harmonic field physical pressure. Independently cross-check against Cartesian Fourier-space Leray projection or a separate Poisson solver on enlarged domains, including boundary/tail sensitivity.

A useful pressure-eliminated residual is

\[
 \mathcal R_{proj}=(1-c_l)U+c_l(y\cdot\nabla)U
 +\mathbb P[(U\cdot\nabla)U],
 \tag{P2}
\]

where \(\mathbb P\) is the whole-space Leray projection with all decay assumptions specified. Check consistency of (P2) and (E), rather than assuming an implementation of \(\mathbb P\) is correct.

## 8. Strictly scaling-invariant loss, gauges, and nondegeneracy

Both symmetry stages must use *exactly the same scaling-invariant loss and profile normalization*, making their results quantitatively comparable. In Stage B, translate or optimally center the vorticity distribution consistently before computing the intrinsic enstrophy-median length, so pure changes of the removable axial-coordinate parameter do not masquerade as physical improvement.

The true profile scaling is

\[
 U_a(y)=aU(y/a),\qquad P_a(y)=a^2P(y/a),\qquad C_a=aC,
 \quad a>0.
 \tag{G1}
\]

Neither \(\|\Omega\|_\infty\) nor an arbitrary Taylor derivative is a freely adjustable amplitude gauge. Use exactly one justified length normalization and one pressure-constant gauge, plus axial centering and angular phase gauges only when needed. **Do not optimize an unnormalized raw residual**: spatial scaling can otherwise change numerical objectives without improving the physical solution.

An explicit intrinsic scale for a nonzero decaying-vorticity profile is the *enstrophy median radius* \(L_\Omega\), defined with respect to a fixed properly centered origin by

\[
 \int_{|y|\le L_\Omega}|\Omega(y)|^2dy
 =\frac12\int_{\mathbb R^3}|\Omega(y)|^2dy.
 \tag{G2}
\]

For the target tail, enstrophy is finite. Under (G1), \(L_\Omega[U_a]=aL_\Omega[U]\). Numerically verify convergence of this length under tail refinement; if it is unstable, develop an equally justified, smooth robust intrinsic length and report the change. This is a **gauge**, not an artificial normalization of \(\|\Omega\|_\infty\).

With \(\xi=y/L_\Omega\), define

\[
 \widetilde U(\xi)=U(L_\Omega\xi)/L_\Omega,
 \quad\widetilde P(\xi)=P(L_\Omega\xi)/L_\Omega^2,
 \quad \widetilde C=C/L_\Omega.
 \tag{G3}
\]

These nondimensional fields are **exactly unchanged** by (G1). Evaluate losses in \(\xi\)-space or prove their exact scaling invariance in physical coordinates. A suggested multi-region functional is

\[
 \mathcal L=\sum_{D\in\mathcal D}\big[
 w_{m,D}\varepsilon_m(D)^2+w_{\Omega,D}\varepsilon_\Omega(D)^2
 +w_{P,D}\varepsilon_P(D)^2\big]
 +\mathcal L_{origin\ jets}+\mathcal L_{tail\ coefficients}
 +\mathcal L_{validation\ safeguards}.
 \tag{G4}
\]

If velocity is exactly divergence-free, report independent divergence but need not optimize its loss. For each region \(D\), use term-normalized residuals, for example

\[
 \varepsilon_m(D)=\frac{\|\widetilde{\mathcal R}_m\|_{L^2(D)}}{
 \|(1-c_l)\widetilde U\|_{L^2(D)}
 +\|c_l\xi\cdot\nabla\widetilde U\|_{L^2(D)}
 +\|\widetilde U\cdot\nabla\widetilde U\|_{L^2(D)}
 +\|\nabla\widetilde P\|_{L^2(D)}
 +|\widetilde C|\|\partial_z\widetilde U\|_{L^2(D)}}.
 \tag{G5}
\]

Use physical volume \(d\xi=R^2dR\,d\omega\) for physical \(L^2\) norms. Handle vanishing denominators as degeneracy flags, **never** by hiding the defect behind an arbitrary large floor. Also compute absolute/natural-scale defects and maxima; do not let ratios alone certify a vanishing or affine field.

**Near origin:** include coefficient-wise dimensionless jet penalties \(D^\alpha\widetilde{\mathcal R}_m(0)\) through the computed order, or exact algebraic elimination of those coefficients. Add a shrinking-ball test across at least several decades of radius with explicit orders. The residual at a small radius must not appear successful solely because an uncancelled \(O(R)\) or \(O(R^2)\) term is numerically tiny.

**Far field:** report *two* normalized residuals: (i) the conventional sum-of-PDE-terms ratio; (ii) a sensitive ratio referenced to the **nonlinear/subleading scale** (typically \(R^{2d-1}\) before cancellation, or the next predicted unmatched order afterward), including permissible pressure multipoles. The huge similarity terms cancel on a homogeneous tail and can make (i) misleading. Verify each matching equation (F6)-(F9) and the observed tail defect order directly. Use angular-resolved shell norms, not only an averaged global MSE.

Set physically meaningful safeguards for nonzero vorticity, **resolved** \(m=2\) signal, variation of vorticity, non-affinity, genuinely 3D structure, and confinement to an adequately resolved core. If temporary non-axisymmetry/nondegeneracy penalties are used during initialization, systematically remove them and require persistence under the unmodified PDE loss. Do not minimize \(c_l\) independently of the PDE or call a fixed-input exponent an optimized discovery.

## 9. Multicore CPU-first quadrature, optimization, and numerical accuracy

Use FP64 coefficients, basis evaluation, differentiation, pressure solves, optimization, and independent validation. **Multicore CPU parallelism is a core requirement, not merely an option.** Before computation inspect physical and logical CPU counts, actual CPU-affinity and scheduler/cgroup allocation, memory and swap, NUMA topology where relevant, other jobs, and per-node memory bandwidth. Do not confuse 'many visible threads' with cores the job is actually entitled to use. Create a new isolated directory and protect other users' allocations.

Benchmark single-thread and multi-thread cases, for example 1, 2, 4, 8, 16, 32, ... threads up to the allocated limit, with identical numerical workloads and validation. Select a high-throughput number of cores based on measured scaling and memory pressure. If the machine is dedicated and the allocation permits it, use many physical cores; if shared, respect its scheduler/CPU quota and keep operational headroom. **Do not leave a substantial 96-hour spectral campaign single-threaded by default.** Log cores allocated, worker count, threads/worker, utilization, memory use, measured speedups and any decision not to use the available cores.

Parallelize (when numerically advantageous) independent angular/radial quadrature slabs, Fourier/vector spherical harmonic transforms, expensive basis evaluations and nonlinear interactions, Jacobian/Jacobian-vector assembly, block least-squares calculations, independent multistart branches, fixed-\(c_l\) scans, and independent validation. Use sensible coarse-grained tasks for small spectral coefficient counts. Prevent oversubscription: explicitly coordinate BLAS/OpenMP/MKL/OpenBLAS/Julia threads with the number of worker processes; check CPU pinning/NUMA placement if scaling stalls. Use efficient threaded BLAS/LAPACK and sparse/direct or matrix-free solvers as justified by coefficient size. Avoid needless serialization of data and giant all-to-all transfers between workers. Verify deterministic or numerically reproducible reduction behavior.

**GPUs, including A100s, are optional.** First benchmark CPU multicore performance, since moderate-size dense linear algebra and high-accuracy CPU quadrature may be preferable. Only use GPU if measured FP64 speedup justifies transfer/memory/implementation complexity. No requirement to use one GPU before others; no all-A100 escalation; no unauthorized compute usage.

Use high-order radial quadrature on core and logarithmic shells, suitable angular quadrature, and enough azimuthal points to resolve nonlinear couplings; perform **dealiasing/overintegration**, not only the number of collocation points matching retained modes. Study angular and radial truncations independently. Derive Jacobians, endpoint limits and near-axis regularity analytically instead of evaluating formal 0/0 at machine epsilon.

Before accepting any optimization results, test exact divergence/symmetry, manufactured affine exact solutions and smooth non-affine fields, symbolic Taylor (O1)–(Ok), far-field (F1)–(F9), and pressure Green identities. Compare analytic/symbolic derivatives against independent finite differences. For moderate systems use Gauss–Newton, Levenberg–Marquardt or trust-region nonlinear least squares. For larger ones compare matrix-free Jacobian-vector products, block preconditioning, L-BFGS, and variable projection of pressure/Taylor/tail coefficients. Monitor condition numbers and nullspaces (including vector-potential gauge directions).

Suggested resolution ladder: begin with moderate angular degree and approximately 6–12 radial coefficients per tail block, then increase angular bandwidth, radial degrees, outer domain, fractional/logarithmic tail blocks and independent quadrature. This is a benchmark, not a permanently restricted ansatz. Increase even-m azimuthal harmonics beyond 2 as needed to resolve nonlinear mode generation.

Measure losses in core, axis tube, off-axis peaks, intermediate shells and multiple far-tail shells. Keep training, validation and final untouched audit sets separate; if validation data drive tuning, reclassify them and generate new untouched audit samples.

## 10. Two-stage search plan with an explicit parity-release decision

Search fixed \(c_l\) values such as \(0.49,0.47,0.45,0.43,0.41\), plus an optional \(0.50\) calibration. Later jointly fit \(c_l\) with the basis coefficients once a robust nontrivial branch exists. A fixed-input exponent is not a discovered exponent; a fitted value just below 0.5 is unresolved if sensitivity is comparable to \(0.5-c_l\).

**First run Stage A (z-reflection).** Explore at least several matrix seeds and non-axisymmetric/angular-tail families, the on-axis nonzero-vorticity and zero-vorticity branches, paired off-axis peaks, distinct radial/angular resolutions, and different strengths of exact origin/far-field cancellation. Use a fixed budget of preliminary *active experiment time* (suggested 12–24 hours, with an evidence review by approximately 24 hours; extend only for improving candidates). Explicitly record the symmetry-enforced Taylor orders and parity-compatible pressure multipoles. Do not spend the entire 96 hours polishing an affine, zero or boundary artifact.

**Parity-release trigger.** Switch to Stage B if the initial broad Stage A search has no candidate with resolvable fundamental \(m=2\), nonconstant non-affine vorticity and independently improving local/far-field residuals; if the best branches stall across independent seeds/representations; or if a proved geometric/algebraic obstruction rules out the investigated symmetric class. A failure to find a candidate is not a proof, but **is sufficient reason to enlarge the search space**. Do not impose a rigid numerical threshold as a false existence criterion. If Stage A has a genuinely improving strong branch, retain it and refine; nonetheless allocate an independent symmetry-free control branch within the overall campaign to test whether relaxation helps.

**Then run Stage B (no z parity, Anima-inspired center freedom).** Unlock all excluded poloidal/toroidal and pressure harmonics, allow the general Taylor jets, initialize symmetry-breaking perturbations, and permit the removable axial travel parameter \(C\) with a consistent centering gauge. Run multiple independent starts. The mathematical problem must remain the **full 3D two-fold-equivariant Euler PDE**, not the axisymmetric reduction used in Anima's paper. Any moving-center solution must be transformed back to canonical coordinates and validated there, with translation-aware far-field matching.

For either stage, fit the full coupled 3D velocity and pressure, not an axisymmetric \(\Gamma,\eta\) surrogate, a 2D streamfunction or a forced Euler modification. Optional homotopies for initialization must return to the exact Euler equations for acceptance. Compare Stage A and B on matched intrinsic-scale invariant objectives and untouched validation sets, documenting whether allowing broken z symmetry led to an actual improvement.

A failed finite basis truncation or stalled optimizer proves no nonexistence result. Keep exploring under the full authorized budget; a mathematical obstruction must be precisely formulated and independently verified before claiming exclusion.

## 11. Hardware allocation and CPU parallel scaling decisions

**No A100 requirement.** CPU multithreading/multiprocessing is the primary plan. Detect the current machine, its *authorized* core allocation, available RAM, NUMA nodes, CPU/IO contention, and configured BLAS/Julia/Python threads before starting. A dedicated large CPU server should use a substantial fraction of its available physical cores; a shared server must stay within the scheduler allocation. On a personal laptop, preserve responsiveness and thermals.

Run a short, reproducible scaling benchmark measuring elapsed time and actual numerical agreement for representative angular quadrature, pressure-Poisson solves, Jacobian assembly and nonlinear optimization at 1, 2, 4, 8, ... permitted cores. Choose an efficient configuration. If threading a small linear algebra kernel shows little benefit, retain multicore parallelism at the experiment/seed level rather than reverting the entire project to a single CPU core. Distinguish physical cores from hyperthreads, limit concurrent workers by RAM, and prevent nested threading oversubscription.

Use parallel workers to explore independent c_l values, seed families, the Stage A/Stage B symmetry branches, angular truncations and validation studies. Use separate immutable checkpoint files and a coordination ledger so parallel workers cannot overwrite candidates. Benchmark GPU acceleration only if an actually available, authorized GPU and workload size make this worthwhile; report why CPU or GPU was chosen. **Do not assume 8 A100s, require GPU availability, or budget a compulsory all-GPU run.**

Count active research time as the union of actual experiment intervals, not CPU-core-hours. For example 24 CPU cores running concurrently for 1 hour count as 1 active campaign hour, not 24. Protect other jobs, keep a safe-stop/resume mechanism, and log actual resource utilization rather than nominal reservations.

## 12. Minimum 96-hour measured active experiment schedule

The minimum is **96 hours of actual, non-overlapping active numerical experiments**, including optimization, computational asymptotic tests, independent numerical validation or parameter experiments. Exclude idle, reading, coding, reporting, suspended jobs and setup. Many CPU threads or simultaneous workers do **not** multiply elapsed active wall-clock experiment time. If the execution environment cannot continue, checkpoint and truthfully report only the active time actually completed.

Suggested milestones in cumulative active experiment hours:

- **0–6:** After the non-counted derivation and code setup, conduct active computational unit tests of Euler equations, symmetry masks, vector-potential behavior under reflection, Taylor/parity and far-field recurrences; benchmark multicore execution, run a genuine Stage A pilot and test exact checkpoint/resume. Count only the time spent on active numerical experiments, not coding or literature review.
- **6–24:** Run a broad **multicore Stage A search** across c_l, seeds, both axial-vorticity branches and resolutions; check core/far-field residual orders and pressure matching. By approximately 24 active hours explicitly decide whether to continue a promising symmetric branch and/or release z parity.
- **24–48:** If Stage A was unproductive, carry out **Stage B no-z-parity searches** with all unlocked spectral harmonics, asymmetric seeds, general origin jets and optional traveling C. Compare both bases and higher-order tail cancellation. If Stage A is promising, continue refinement while still giving the general Stage B branch independent exploration time.
- **48–72:** Refine the strongest surviving branches in both classes, enlarge basis and asymptotic orders, fit c_l when justified, and compare on the same scaling-invariant loss. Redirect time from failed symmetry-restricted optimizations to general branches.
- **72–96:** Adversarial independent validation on larger domains, axis/origin jets, asymptotic tail correction orders, whole-space pressure multipoles, nonlinear aliasing, c_l sensitivity and reproducibility. When no candidate survives, continue genuinely different searches rather than idle validation.

Log experiment IDs, start/stop intervals, active seconds (count interval unions), machine/CPU allocations, worker/thread counts, configuration/checkpoint hashes, stages, symmetry masks, losses, regional validation and reasons for branch changes. Use atomic checkpoints roughly every 10–30 minutes and at shutdown. Preserve basis/coefficients, optimizer state, all scalar parameters, RNG and quadrature states, campaign queue and a diverse archive of previous candidates. Provide tested one-command run/status/stop/resume scripts. Guard against numerical NaNs, disk exhaustion, memory pressure, oversubscription and failed checkpoints. Do not claim ongoing background work without a genuinely authorized persistent scheduler/job.

## 13. Independent acceptance tests and scientific status

Each serious candidate, from either stage, must pass independently reproduced checks for:

1. Full Cartesian momentum, exact/independent divergence, curl/vorticity and whole-space pressure Poisson consistency; separately report L2, RMS, high quantiles and sampled maxima.
2. Exact two-fold vector equivariance and resolvable fundamental m=2 content. **For Stage A only**, verify z-reflection and inversion parity exactly; **for Stage B**, confirm the basis and numerical code permit parity-breaking components and that no accidental z parity is hard-coded. A Stage B candidate is allowed to be symmetric if the PDE, rather than a hidden constraint, selects it.
3. Nonzero spatially varying vorticity, substantial best-affine-fit remainder, genuine dependence on three spatial coordinates and meaningful stretching.
4. Stage-specific Taylor compatibility, predicted versus measured small-radius residual slopes, and independent origin smoothness checks. Never evaluate Stage B with only Stage A's odd-velocity jets.
5. Full far-field coefficient matching, parity-appropriate harmonic-pressure multipoles, predicted versus observed residual orders, and stable whole-space pressure/Biot–Savart checks under domain enlargement. Include axial translation effects in Stage B where C is free.
6. Convergence under angular/radial enlargement, more fractional/logarithmic tail blocks, nonlinear dealiasing, quadrature accuracy and numerical precision.
7. Removal of temporary nondegeneracy penalties, robustness under independent initializations, and stable core localization. For Stage A survivors, additionally assess the effect of unrestricted Stage B perturbations without insisting that the final solution break symmetry.
8. Axial/off-axis stagnation geometry, local stretching at a resolved |Omega| maximum, and assumption-by-assumption comparison with relevant self-similarity exclusion theorems.
9. For claimed c_l<1/2, a numerically resolved gap larger than the variation produced by independent refinements and refits.
10. Actual CPU parallel scaling, allocated versus utilized cores, memory usage, oversubscription avoidance, and reproducibility of parallel numerical results.

Heuristic regional relative momentum RMS goals are below 1e-3 for promising screens and 1e-5 or better for strong numerical candidates, **not** universal proof thresholds. The tailored origin/tail defects and independent convergence are essential. A sampled maximum is not a rigorous L-infinity bound. A numerical Euler profile, a stable profile, and physical blowup from one fixed finite-energy datum are different claims.

For source context, audit Ganeshram–Duruisseaux–Anandkumar, arXiv:2609.10867 (no z-parity and traveling axial center in an axisymmetric numerical setting), Constantin–Ignatova–Vicol, arXiv:2602.17570 (conditional geometric restrictions), and standard vector spherical harmonics. Verify exact versions/assumptions, and do not apply axisymmetric no-blowup results to the full m=2 class without proof.

## 14. Required files, reports, and final decision

Produce a fully reproducible isolated research directory containing:

- `EQUATIONS_AND_SYMMETRY.md`: full 3D Euler signs; correct physical z-reflection parity and its inversion consequence; all symmetry masks; Stage A/B equations and axial centering gauges.
- `ORIGIN_TAYLOR.md`: Stage A odd-velocity/even-pressure Taylor recurrences, Stage B general jets with/without axial stagnation, compatibility/nullspaces, exact tests and observed small-radius residual orders.
- `FAR_FIELD_EXPANSION.md`: nonlinear cascade, (F5)-(F9), pressure multipoles, resonances/logs, translation-induced Stage B corrections, parity selection and residual order tests.
- `BASIS_AND_QUADRATURE.md`: poloidal–toroidal and Cartesian-potential bases, Stage A/B harmonic masks, pseudo-vector reflection rules for the potential, regularity and aliasing tests, and quadrature.
- `SCALING_INVARIANT_LOSS.md`: exact invariance proof, intrinsic length and centering, weights/denominators, origin jets and sensitive far-field metrics.
- `PRESSURE_SOLVER.md`: radial Green formula, whole-space and tail treatment, independent checks.
- Runnable spectral optimization, tests, independent validation, CPU scaling benchmarks and one-command run/status/stop/resume scripts; all configurations, coefficients, candidate/checkpoint archives, and an explicit parity-release procedure.
- `CPU_BENCHMARKS.md`: actual physical/allocated cores, thread-worker settings, measured speedups, parallelization and memory/NUMA decisions, optional GPU comparisons if any.
- `CAMPAIGN_LEDGER.jsonl`, `STATE.json`, `PROGRESS.md`, and `NEXT_STEPS.md`, with actual non-overlapping active experiment hours, CPU assignments, symmetry-stage transitions and exact continuation commands.
- `REPORT.md`: both symmetry stages, strongest candidate, full regional residuals, c_l sensitivity, Taylor/tail cancellations, angular spectra, pressure matching, reproducibility, negative findings and remaining gaps. Provide snapshots near 24/48/72/96 cumulative active hours.

In the final report clearly answer: **Did Stage A with z-odd vertical velocity produce a smooth genuine m=2 candidate? Was z parity released and did Stage B's unrestricted two-fold traveling-center search help? Is c_l numerically resolved below 1/2? Which Taylor and asymptotic terms were cancelled analytically? Is whole-space pressure consistent? What does independent refinement show? Was multicore CPU utilized effectively? What prevents a rigorous conclusion?**

Use one honest outcome label: **STRONG NUMERICAL CANDIDATE**, **PRELIMINARY CANDIDATE**, **NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH**, or **RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS**. Failed minimization is never a theorem. If runtime resources prevent completion of the requested 96 active hours, checkpoint and state the actual number with the exact tested resume command; do not invent unexecuted work.
