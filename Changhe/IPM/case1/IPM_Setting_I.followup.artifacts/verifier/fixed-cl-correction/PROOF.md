# Independent correction in a finite physical subspace

Date: 2026-10-20. Status: exact finite-dimensional identities and a numerical verification protocol, not a profile existence proof.

## Inputs and fixed parameters

Let rho0 be one frozen nodal trial, with fixed c_l, radial compactification scale L and angular map. Its nodal first row equals1. Let h_a be independent shape variations whose first rows vanish, let v_a=T h_a be their canonical whole-plane velocities, and set U0=T rho0. Here T is the linear parity-preserving canonical velocity operator of the specified profile class. All reconstructions and inverse computations are this lane's implementations.

The initial column span is the14physical directions already evaluated independently. Project their coefficient space onto the simultaneous nullspace of delta c_l and delta C. On this subspace the differentiated density map is exactly the ordinary linear nodal variation: its parameter-derivative part is proportional to delta c_l and vanishes. Holding the auxiliary C fixed is an additional numerical restriction, not a condition forced by the PDE. Its far-field matching equation is not silently imposed by this construction.

For real coefficients z, define rho_z=rho0+sum_a z_a h_a and U_z=U0+sum_a z_a v_a. Linearity of the canonical inverse proves the second equality exactly whenever the fields lie in its domain. Each finite combination retains parity, the prescribed sublinear radial growth and cubic normalization. It need not retain positivity everywhere or any exact profile equation.

## Exact quadratic residual

At any point X with W0=c_l X+U0,

    R_z = W0.grad rho0-rho0
          +sum_a z_a [W0.grad h_a+v_a.grad rho0-h_a]
          +sum_(a,b) z_a z_b v_a.grad h_b.                 (1)

This follows by expanding (W0+sum z_a v_a).(grad rho0+sum z_b grad h_b)-rho0-sum z_a h_a. No Taylor remainder is omitted because c_l and both coordinate maps are fixed and density enters linearly. The Jacobian of the quadratic term is the sum of its two index contractions. The formula concerns the residual numerator. A fixed base denominator may be used for optimization; the actual denominator of rho_z must be recomputed for reporting.

The origin moment c is linear in density. Therefore its defect has the exact affine form

    3c_l-1-c(rho_z) = 3c_l-1-c(rho0)-sum_a z_a c(h_a).   (2)

The moment is computed by a separate angular quadrature and radial integration. It must not be replaced by a harmonic velocity correction. A finite least-squares solution to (2) provides an affine coefficient origin; its nullspace provides free correction directions. Numerical tolerance and moment refinement are reported explicitly.

## Finite trust region and withheld checks

Use the previously fixed58physical points for fitting. Define the shape norm by RMS of h_z(X_i)/(1+|rho0(X_i)|), with no artificial penalty on an auxiliary parameter. A thin QR factor whitens this finite map; reject a singular metric rather than claiming an invisible direction is controlled. On the coefficient subspace satisfying (2), take the minimum-domain-norm particular coefficient and orthonormal free coordinates. Bound the norm of free corrections by a stated trust radius. Optimize the58quadratic residuals divided by their fixed base N_f and sqrt(58), with the exact polynomial Jacobian. This is an independent finite optimizer, not a reuse of the numerics lane's solver.

Choose the initial trust radius before fitting. Report physical shape norm, coefficients, finite objectives and the normalization/identity constraints. Check the optimizer's algebra by direct reconstruction of the resulting nodal field at the fitting points and by direct canonical inversion at selected points. Freeze the result before evaluating a distinct prescribed set of physical points not used in the objective. Such withheld checks can show failure away from fitted samples; they cannot prove a uniform residual bound. In particular, fitting58points does not establish a smooth center, a solution, a family, or a continuum kernel. The exact center tests must be repeated on any saved state.

Dependencies: ../sampled-physical-actions/PROOF.md for the fields, gradients, velocity variations and finite norm; ../inverse/PROOF.md and ../exterior-tail/PROOF.md for the canonical inverse; ../center-regularity/PROOF.md for exact center exclusions. The symbolic identities (1) and (2) are proved above before writing the optimization code.
