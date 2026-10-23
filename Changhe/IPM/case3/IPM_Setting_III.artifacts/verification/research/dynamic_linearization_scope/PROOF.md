# Dynamic linearization, compressed spectra, and the local feedback symbol

Status: analytical audit, written before the companion symbolic check. The UTC creation time and source hashes are in verification/MANIFEST.json. No continuum eigenvalue, instability theorem, or nonexistence endpoint is claimed. This audits numerics' 2026-10-21T07:00Z note independently. Dependencies are the canonical inverse, the linearity of its strain functional, elementary Fourier differentiation, and the exact DR equation of result151.

## 1. Exact continuum linearization

Write c[rho]=psi_xy(0), cw[rho]=-c[rho]/(C-1), cx=C cw, C>1, and F(rho)=cw*rho-(cx*X+U[rho]).grad rho. At a smooth density rho, differentiation in direction h gives

DF(rho)h = cw*h-(cx*X+U[rho]).grad h-U[h].grad rho
             -c[h]/(C-1)*(rho-C*X.grad rho).

This follows by expanding F(rho+epsilon*h) and retaining the coefficient of epsilon; the inverse and c are linear. The last term is the rate-feedback term. A feedback-off operator which freezes both the velocity and rates is cw*h-(cx*X+U[rho]).grad h. Setting only U[h] to zero but retaining rate feedback gives a different operator. At a nonstationary density, this is an instantaneous linearization; perturbations along the evolving trajectory solve a time-dependent linear equation, not the frozen equation for all future times.

## 2. What a compressed spectrum represents

For a finite coefficient Jacobian J and an orthonormal coefficient matrix V, the matrix V^T J V generates the explicitly reduced equation z'=V^T J V z on the chosen coefficient subspace. This is a legitimate Galerkin compression with the Euclidean coefficient inner product. It is not generally the Jacobian of the original integrated equation restricted to an invariant subspace. If V^T J V z=lambda z, the lifted vector v=Vz has full eigenvector residual

Jv-lambda*v=(I-VV^T)Jv.

Therefore a numerical compressed eigenpair should be accompanied by this residual measured in field and coefficient norms, and by dependence on the chosen metric, cutoff and resolution. Equality of a compressed growth rate and an observed short transient is evidence to investigate, not a proof of a continuum eigenmode. The original coefficient parametrization can be ill-conditioned; that does not itself make every eigenvalue meaningless, as result170's exact similarity counterexample shows.

## 3. Local constant-gradient feedback

For the Fourier convention d_x -> i*kx, d_y -> i*ky and nonzero k, the canonical equations give

psi_hat=i*kx*h_hat/|k|^2,
U1_hat=kx*ky*h_hat/|k|^2,
U2_hat=-kx^2*h_hat/|k|^2.

At a frozen constant gradient (0,a), the feedback -U[h].grad rho has symbol a*kx^2/|k|^2. This is exactly the nonlocal feedback symbol. For a>0 its pointwise range is [0,a], and the corresponding constant-coefficient Fourier multiplier is positive semidefinite with L2 norm a. This statement concerns that part of the operator only. It omits transport, reaction cw, rate feedback and variation of the background. At gradient (b1,b2), its symbol instead is (b2*kx^2-b1*kx*ky)/|k|^2. Thus the single origin slope a does not establish a global growth bound for a variable background. These are local symbols, not admissible affine profiles.

A concrete local model illustrates transport of frequency. For positive A>B, let h_t+(Ax,By).grad h=cw*h+a*P h, where P has symbol kx^2/|k|^2. A plane wave has kx(t)=kx0*exp(-At), ky(t)=ky0*exp(-Bt) and amplitude logarithmic derivative cw+a*kx(t)^2/|k(t)|^2. For ky0!=0, r=kx0/ky0 and d=A-B,

integral_0^t kx(s)^2/|k(s)|^2 ds
 = [log(1+r^2)-log(1+r^2*exp(-2*d*t))]/(2*d).

Differentiating proves the formula and its zero initial value. For fixed finite r the feedback contribution saturates as t grows; for ky0=0 it equals t. This shows why the local symbol's supremum alone does not specify long-time behavior of every perturbation. Plane waves are used only to check the local constant-gradient linear model, not as admissible IPM profiles or localized eigenfunctions.

## 4. The claimed nonconvergence consequence does not follow

Even a proved unstable equilibrium can attract trajectories on a stable manifold. The elementary system x'=x, y'=-y has an unstable eigenvalue1 but every solution with x(0)=0 tends to the equilibrium. The exact equilibrium itself is stationary. Thus an instability calculation alone cannot prove that forward DR cannot converge to any profile, without a precise genericity/basin statement. Here the numerically linearized states are stalled approximations, not known exact profiles, and their compressed spectra have not yet been independently recomputed. Assertions about all profiles with slope above a threshold therefore remain OPEN. The numerical feedback comparisons may support a mechanism hypothesis after independent spectrum and trajectory checks; they do not prove the universal consequence in the producer's07:00 note.

No mathematical step above requires accepting the producer's eigenvalues or localization percentages. Those finite data remain to be independently audited with a basis-aware canonical evaluator. The provisional restriction to compressed coefficient directions must be disclosed as a change of the linear evolution being studied.

## 5. Source-level feedback switch and localization metric

Read-only inspection of dr.py and ipm3ql.py shows that feedback=False sets every entry of dflds to zero before linearized_fine and before c[h] is obtained. The map _fine_fields is linear in these arrays. Consequently all dF velocity terms and the rate derivatives vanish, whereas the base F terms still multiply the perturbation's derivatives. This implements the frozen velocity-and-rate operator in section1, followed by the chosen finite projection. This source-level algebra does not establish the accuracy of the producer inverse or numerical Jacobian.

The current dr_vis_modes.py defines localization by summing abs(rho_eig)^2 on the radial and angular nodes with NO quadrature weights. Its reported93..97percent is therefore a fraction of an unweighted nodal squared norm. It is not a fraction of physical area L2 mass. For the stated map r^2=L^2*(1+t)/2*(1-t)^(-2P), the area measure in polar coordinates is

r dr dtheta = r^2*Q(t)/(1-t^2) dt dtheta,
Q(t)=(1-t)/2+P*(1+t).

Logarithmic differentiation of r proves this identity. Any area-norm discretization must include the corresponding weights and justify the exterior tail; a finite nodal sum alone does not prove that a perturbation is globally L2. Even a finite-box area fraction differs from a nodal fraction on a nonuniform radial mesh. The node-based metric may still be useful when named explicitly and checked under changes of map and resolution. It cannot be silently substituted for another norm in a continuum conclusion.
