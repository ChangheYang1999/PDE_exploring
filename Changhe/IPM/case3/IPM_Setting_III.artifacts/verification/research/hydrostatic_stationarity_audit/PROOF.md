# Hydrostatic numerical stationarity and coefficient-space diagnostics (195)

Written 2026-10-21T09:30:09.817356+00:00, before implementing the checks. Exact statement: for a finite differentiable residual F:R^n->R^m and its Jacobian J, the following SVD identities and counterexamples delimit what the reported hydrostatic diagnostics imply. This is a finite-dimensional theorem and a source/log audit. It does not certify the producer's floating-point Jacobian, nor a continuum eigenpair or hydrostatic profile. All norms below are Euclidean unless explicitly stated.

## Residual decomposition and linearized decrease

Take an SVD J=U diag(s_i) V^T, with r nonzero singular values and orthonormal columns U_i,V_i. Partition the nonzero indices into kept K and dropped D. Let P_K and P_D be the orthogonal projections onto the corresponding LEFT singular vectors. Then

F=P_K F+P_D F+F_perp,  F_perp orthogonal to range(J).

The three terms are mutually orthogonal. In particular, with rho_K=||P_K F||/||F|| and rho_all=||P_K F+P_D F||/||F||,

||P_D F||/||F||=sqrt(rho_all^2-rho_K^2),
||F_perp||/||F||=sqrt(1-rho_all^2).

The row-space residual and the right singular vectors in coefficient space are different objects. In a floating-point thin SVD, 'all' includes every computed column of U. If an exactly zero singular value occurs, its U column is not in the mathematical range; the formula then concerns that reported subspace. Hence rank and range claims from a numerical cutoff must be qualified.

The truncated Gauss-Newton correction d=-sum_(i in K) V_i (U_i^T F)/s_i satisfies Jd=-P_K F. For the LINEARIZED residual,

||F+lambda Jd||^2=||F||^2-(2lambda-lambda^2)||P_K F||^2.

Thus the derivative at zero of one half of the squared norm is -||P_K F||^2. At lambda=1 the predicted fractional squared-norm decrease is rho_K^2. For nonlinear F the actual residual is F(u+d)=F(u)+Jd+o(||d||) as d tends to zero; no useful remainder bound at this chosen full step follows just from the SVD. Every nonzero rho_K gives a strictly negative directional derivative, so it is not exact stationarity on the kept directions. Exact full first-order stationarity is J^T F=0. No first-order test alone certifies a local minimum.

The normalized gradient satisfies

||J^T F||/(smax ||F||) <= sqrt(rho_K^2+tau^2 rho_D^2)

when all dropped s_i<=tau smax, since each kept s_i<=smax and the V_i are orthonormal. Small rho_K and tau therefore give approximate stationarity in this explicitly specified gradient normalization. This is not a coefficient-invariant or continuum norm. Multiplying F by row weights or changing coefficient variables changes the diagnostics.

## Three counterexamples

1. Let J=diag(1,epsilon), F=(0,1), and discard the second singular value. Then rho_K=0 while J^T F=(0,epsilon) is nonzero. The exact correction d=(0,-1/epsilon) gives Jd=-F. If the sampled field map is A=diag(1,epsilon), the field change Ad=(0,-1) has unit size. Therefore small visibility of a unit coefficient vector does not show that a large correcting coefficient move would leave the field unchanged.

2. Let A=diag(1,epsilon), regard V=e1 as the retained visible coefficient space, and J=[[1,1],[0,epsilon]]. The restriction JV has singular value1. Yet v=(-1,1)/sqrt(2) obeys ||Jv||=epsilon/sqrt(2), whereas ||Av||=sqrt((1+epsilon^2)/2), which tends to1/sqrt(2). Removing the weakly sampled coefficient coordinate removes the near-null cancellation, but the original near-null vector is a strongly sampled field. Consequently an improved restricted spectrum alone does not identify every small full-space singular vector as a weakly sampled field.

3. Let a scalar nonlinear residual be f(t)=1+t+B t^2 at t=0, B>2. Its Jacobian is1, rho_K=1 and the full Gauss-Newton step is d=-1. The linearized residual vanishes, while f(-1)=B and its squared norm exceeds its initial value. This explicitly separates a predicted full-step decrease from an actual nonlinear decrease. The negative derivative at zero remains valid.

For coordinate dependence, J=diag(1,epsilon) and u=diag(1,1/epsilon)z give derivative with respect to z equal to the identity. No invariant degeneracy conclusion follows from the small singular-value ratio in u coordinates alone.

## Dilation and its finite representation

Let a canonical linear velocity operator T obey T[g_lambda](X)=lambda T[g](X/lambda), g_lambda=lambda g(X/lambda), and define R_g=(cX+Tg).grad g-g. A direct substitution gives R_(g_lambda)(X)=lambda R_g(X/lambda). Whenever differentiating is justified, L_g(g-X.grad g)=R_g-X.grad R_g. It is zero for an exact solution. A small sampled residual alone gives no bound on its derivative.

A finite mode-by-mode least-squares projection of g-X.grad g is a different trial vector; a reported mode-value projection defect at fitting nodes is not a global or derivative error estimate. Dilation changes an axis amplitude K by lambda^(1-p)K, so its exact tangent changes K by(1-p)K. It is not tangent to the constraint K=1. Since the finite states are not exact solutions, language about tangency to the residual equation must also specify the measured approximate relation.

## Source/log audit and scope

Frozen producer source and raw logs are in verification/INPUTS.json. They show ordinary coefficient Euclidean norms, per-mode sampling-SVD visibility cutoffs, and residual-row Euclidean norms. The sampling map is not whitened. The 12-state stationarity log gives rho_all=.842 at A3N64 and.810 at D3N64. Their orthogonal-complement norm fractions are about.5395 and.5864. The reported difference between rho_K and the visible-subspace ratio exceeds1e-4 for several states, including hsE_c2_N96 (.00904 versus.0120) and oversampledN64 (.112 versus.107). These are direct arithmetic consequences of reported numbers; independent Jacobian reconstruction remains open.

The producer has used different finite-difference maps from the same starts. Changing those maps changes the discrete residual function. These runs show sensitivity to a discretization change and different iteration trajectories. They do not separate which part is due to quadrature error, optimizer behavior or a particular spectral mechanism. The new hsE fields require an independent full-plane evaluation; a static log audit alone does not confirm their continuum residuals.

The exact axis-primitive implementation can be checked against result190 without executing it. Result190's independently implemented compact-polynomial primitive, literal coefficient reconstruction, high-precision witnesses and full-line tests remain the authoritative verifier computation. The producer's later use of that formula is corroboration, not a second independent derivation by this lane. Source changes are frozen so later reruns cannot silently replace the original numerical method.

Verdicts are item-specific: algebra CONFIRMED; the implications disproved by the counterexamples REFUTED; source-to-log numeric pairings CONFIRMED as records only; independently recomputed new matrices and new fields OPEN. Original SettingIII stays UNRESOLVED.
