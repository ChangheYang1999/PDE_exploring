# Selected input derivatives of the projected characteristic map

Written 2026-10-21, before the new action evaluator. Status: exact algebra and conditional finite-cutoff transport statements below are proved. Completed numerical comparisons and their limitations are in verification/SUMMARY.md. No fixed point is asserted.

## 1. Definitions and hypotheses

Fix beta>2, a0!=0, lambda, and a finite linear representation z -> G_z of C4, even-in-x divided vorticities on the plane. Write Omega_z=x G_z. Use the canonical once-subtracted whole-plane relative inverse V[Omega], with no added harmonic strain or independent drift. Suppose this inverse is linear on the finite source space and on a separately fixed source f, and its center strain is a linear functional c(z)=q^T z, q!=0. The source has strain c_f. These hypotheses hold for the native r2 basis sources, which are smooth at the center and C4 across their simple radial spline knots used here by the full-plane kernel calculations in P200 and P205. Their vorticity tails decay as r^(-1/beta_basis); the relative inverse converges, even when the un-subtracted absolute velocity does not.

Let c_star=1+beta/2. On the active coefficient coordinates define

 P(z)=z+q(c_star-q^T z-lambda c_f)/(q^T q),
 D=I-q q^T/(q^T q),
 W_z(X)=beta X+V[Omega_{P(z)}](X)+lambda V[f](X).

P is an affine coefficient projection. It enforces center strain and is part of the numerical map being examined; it is not a new symmetry of the physical equations. Fix the stored input z0. For a chosen direction v, put d=Dv and W_h=W_{z0+hv}.

Fix delta>0. Assume W_h is C2 on a common annulus and that, for h in a neighborhood of zero and Y in a compact neighborhood of a tested point, the backward orbit from Y hits |X|=delta transversely, stays within the annulus until that hit, and has positive outward flux W_h.n at the hit. Prescribe Theta=a0 x^2 and Omega=4a0 x/beta there. Let M_delta(z0+hv;Y) be the reconstructed vorticity at Y. This is a scalar transport map with a prescribed velocity. It does not impose that the output vorticity generates that velocity.

## 2. Projection and inverse derivative

Substituting into P gives P(z0+hv)=P(z0)+hDv exactly. Thus q^T Dv=0, Dq=0, D^2=D, and

 W_h=W_0+h V[Omega_d].

The equality follows solely from inverse linearity. Its velocity derivative is exactly V[Omega_d], including the subtraction at the material center. Its center strain is zero. The total center derivative therefore remains diag(beta-c_star,beta+c_star), as does the leading compatible temperature jet. An unprojected inverse action V[Omega_v] would generally test a different map.

In particular, a direction parallel to q changes no velocity and no exact finite-cutoff map output: M_delta(z0+hq;Y)=M_delta(z0;Y). This is a removed input direction. In contrast, an arbitrary v satisfying ||(J-I)v||=||v|| need not be removed: Jv=2v is a counterexample. A scalar norm ratio is not a substitute for the identity Jv=0.

For the native basis, q is recomputed from scalar B-spline integrals as in P200, not read from the numerical lane's inverse matrices. The physical norm ||G_v||_w^2=v^T H v uses P205's full-plane Gram matrix, with w(r)=r^(1/4)+r^(-1/4), R=1. Normalizing by this norm only sets the size of v. It changes neither P nor the prescribed velocity map. Selected singular vectors refer to the finite saved matrix and chosen metric, not to a continuum singular function.

## 3. Finite-cutoff map and its derivative

Write rho=beta-2. For a backward hit X_0 and travel time T, let Phi_t^h be the forward flow. The temperature at Y is exp(rho T) a0 (X_0)_x^2. The hit equation has nonzero time derivative -W_h.n, so the implicit function theorem gives smooth local dependence of T and X_0 on Y and C1 dependence on h. The annulus and compact flow-tube hypotheses prevent loss of this local construction.

At the boundary its full gradient is

 g_0=(2a0 x,0)+n [rho a0 x^2-W_h.(2a0 x,0)]/(W_h.n).

This has the prescribed tangential derivative and satisfies W_h.g_0=rho a0 x^2. Along a forward characteristic solve

 g'=(rho I-DW_h^T)g,  omega'=g_x-omega,
 g(0)=g_0, omega(0)=4a0 (X_0)_x/beta.

Differentiation of W_h.grad Theta=rho Theta gives the displayed gradient ODE. Uniqueness then identifies g with grad Theta. Variation of constants gives omega(T)=exp(-T)omega(0)+integral_0^T exp(-(T-t))g_x(t)dt, so the second scalar equation also holds. These are the P200 arguments applied to the affine input direction rather than lambda. Parameter dependence of the finite-time ODE and transverse hit gives a well-defined derivative dM_delta(z0+hv;Y)/dh at zero under the stated regularity. No delta->0 limit or uniform-in-space derivative theorem follows.

If the map is C5 in h, the centered four-point formula

 [M(-2h)-8M(-h)+8M(h)-M(2h)]/(12h)

has O(h^4) truncation error. This conditional estimate follows by Taylor expansion: the weights annihilate degrees 0,2,3,4 and give coefficient1 for degree1. The implementation uses a piecewise polynomial stream interpolant whose velocity is C1 globally. Therefore a measured step study is evidence about that numerical map; the C5 estimate is not asserted automatically for it. No numerical difference is an interval enclosure.

## 4. Comparison with the saved coefficient matrix

Let J_h denote the saved forward-difference coefficient array supplied by NUM. The independently evaluated physical action is

 a_h(Y)=Y_x G_{J_h v}(Y).

It is compared with the independently reconstructed finite-cutoff derivative above. If the numerical coefficient-fit map were differentiated exactly, its linearity at fixed beta would allow evaluation and coefficient differentiation to commute. However, its fitted output may differ from the finite-cutoff transport output. Accordingly a discrepancy can combine inverse approximation, flow integration, boundary prescription, coefficient fitting, finite-difference error, and cutoff effects. The comparison does not assign the error to one component.

Only finitely many directions and spatial points will be checked. Even agreement in all of them gives no operator-norm bound on J_h-DM, no lower bound for an infinite-dimensional singular value, no exact fixed point, and no existence or nonexistence theorem for B2. The P208 finite-matrix singular values remain statements about that array.

## 5. Manufactured controls and dependencies

The algebra will be checked on deterministic finite vectors: exact projection differences, zero projected strain, idempotence, and removal of q. A synthetic linear observable tests the four-point weights and action orientation, while an exponential observable tests the expected Taylor convergence independently of transport. P200's exact nonlinear transport family tests the characteristic reconstruction and parameter differencing; its outputs and limits remain a named dependency rather than a new test claim. P200's adaptive modal and Cartesian Duffy inverses are separately implemented whole-plane operators. The new direction inverse will also be cross-checked at sampled points by both operators, with two quadrature orders and two stream interpolation grids.

The computation reads NUM data but does not import, execute, or copy NUM solver code. The state, selected matrix, Gram matrix, base-inverse cache and all implementation dependencies will be hashed. Results will distinguish exact controls, floating computations, failed integrations, and open inference steps.

Publication clarification 2026-10-21T22:03:18.446041+00:00: the native degree-five splines are C4 across simple interior knots, not asserted to be globally C-infinity. The finite-cutoff calculation only uses the stated finite differentiability. P213 gives the exact difference between the raw transported map and NUM's map which fits temperature before integrating vorticity. The initial proof is preserved in verification/PROOF_initial.md.
