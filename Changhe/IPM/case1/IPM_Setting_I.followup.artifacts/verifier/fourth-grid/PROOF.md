# Independent verification of the fourth resolution

Date: 2026-10-20. This protocol precedes any evaluation of the new 84 by 35 field. It is a finite-data verification plan with its exact mathematical definitions and dependencies, not an existence or convergence theorem.

## Field and mathematical quantities

Freeze the numerical researcher's published artifacts/data/dnB_n84m35S.npz byte for byte. Interpret the binary nodal table at ideal Chebyshev-Lobatto radial nodes and warped angular midpoint nodes, using ../inverse/PROOF.md. Only the nodal table, c_l, L and beta determine this represented density. The solver's auxiliary scalar C is recorded but is not a free velocity parameter.

Let U be the canonical whole-plane inverse of this density, with its symmetric principal-value convention. Put W(X)=c_l X+U(X), R=W.grad rho-rho, E=-partial_x U_2+partial_y U_1-partial_x rho, N_f=|rho|+sum_i |W_i partial_i rho|, and N_v=|rho|+|X.grad rho|+|U.grad rho|. For positive denominators, report the absolute normalized residuals. The 58-point sample is the identical saved physical set used for the other resolutions and scales. A finite maximum is not a continuum supremum.

## Independent checks and their meaning

Use only this verifier's reconstruction, split paired full-plane kernel, eighth-order Cartesian differences and analytic chain-rule gradients. Search for the first nonzero positive axis root in the stated bracket or expanding scan. Check its local velocity Jacobian at two step sizes. Evaluate R at the eight prescribed special points, including two points beside that root, and E at those latter two points. Check both reflections and U(0)=0. Compare two angular/radial inverse rules and three density-difference steps; the differences are sensitivity measurements and are not certified errors of the canonical integral. L is a compactification scale and imposes no finite physical boundary.

For the tail, let H be an integer with H^2>=2N(2M-1), let B_0 be an integer upper bound on the absolute nodal values and let C=L^3 H B_0. Provided L>=1 and 0<1/c_l<1/5, tensor discrete orthogonality gives |rho(Y)|<=C |Y|^(1/5) for |Y|>=1, as proved in ../exterior-tail/PROOF.md. For |X|<=a<R, opposite-source pairing and the convergent exterior multipole expansion then give

    |U_(|Y|>R)(X)| <= (5C/2) a R^(-4/5)/(1-a^2/R^2)^2.

Use R=10^30, rational upper bounds for a and exact rational arithmetic for this omitted exterior term. The Euclidean velocity estimate is separate from the interior quadrature comparison. Propagation to R uses the computed gradient and fixed computed normalizer and is labelled accordingly.

The nodal first radial row must be identically one to give the cubic normalization rho=x^2 y+O(r^5). Import all binary inputs through the exact JSON interface. The two independently proved whole-plane center formulas in ../center-moment/PROOF.md and ../center-moment-trapezoid/PROOF.md each enclose psi_xy(0), with their own truncation bounds. Their overlap is a consistency check. A nonzero enclosure of 3c_l-1-psi_xy(0) refutes the canonical identity for this fixed interpolant, without an adjustable harmonic strain. The entire sublinear harmonic velocity with the required symmetries is zero, by the Liouville argument in ../inverse/PROOF.md.

The jet certificate in ../center-regularity/PROOF.md tests the forbidden fifth-order angular components and transport-balance determinant. If either enclosure excludes zero, state the corresponding exclusion for this fixed represented field. If it contains zero, retain OPEN rather than assuming a positive result. None of these tests decides the regularity of a possible limiting density. Likewise, failure of the frozen identity or transport equation excludes this interpolant, not all profiles in the admissible class.

## Provenance and scope

The programs are copied from this verifier's refreshed-third-grid topic and retain only this verifier's own imports. Record their source hashes and all substitutions. Do not execute or import a numerical-lane implementation. The supplied solver residual, matrix singular values and refreshed Ritz values are attributed data unless independently recomputed. A fourth stagnation does not establish a minimum, a family, a kernel or a smooth limit. The present checks can refute the YES_inf standard for the frozen field; they cannot establish NO_inf for the coupled class.
