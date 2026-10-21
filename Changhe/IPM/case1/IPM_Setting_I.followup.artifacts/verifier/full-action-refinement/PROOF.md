# Full sampled-matrix inverse sensitivity at 72 nodes and L=16

Date: 2026-10-20. This is a finite-dimensional identity and a numerical protocol, written before the new refinement runs. It gives no continuum spectral or quadrature-error theorem.

Fix either of the exact states, frozen directions and58 physical points of ../third-grid-actions/PROOF.md or ../scale-actions/PROOF.md. Keep the main run's density values, Cartesian gradients, direction gradients, positive normalizers N_i, domain matrix M and c_l direction row d fixed. For fourteen directions h_j and V_j=T h_j, the main matrix is

    A_ij=[(c_l X_i+U_i).grad h_j(X_i)
           +(V_j(X_i)+d_j X_i).grad rho(X_i)-h_j(X_i)]/(N_i sqrt(58)).

Only the canonical inverse evaluations are varied. Recompute all58 rows, including every base velocity and all14 direction velocities, at angular/radial rules(2048,24,0.1) and(4096,24,0.1), where the last two numbers give Gauss order and maximum logarithmic panel width. Compare with the main(4096,32,0.075) rule. The first difference changes only angular quadrature, and the second only radial quadrature. The exterior radius remains10^30. Every rule uses the same separately implemented whole-plane split kernel; no periodic box or harmonic gauge is introduced.

For two such evaluations define delta U and delta V as their velocity differences. Direct subtraction of the displayed formula gives exactly

    delta A_ij=[delta U_i.grad h_j(X_i)
                 +delta V_j(X_i).grad rho(X_i)]/(N_i sqrt(58)).

No term differentiating N_i is included because this is the numerator derivative in a fixed output norm. For k=4,10,14 and the main thin QR factorization M_k=Q_k T_k, the corresponding physical matrix difference is delta B=delta A_k T_k^(-1). Compute it by a linear solve, retaining all58 rows. Its spectral norm is at most its Frobenius norm. For any two exact finite matrices of the same dimensions, the min-max characterization of singular values and the triangle inequality imply |sigma_j(B+delta B)-sigma_j(B)|<=||delta B||_2: for every unit vector z, ||(B+delta B)z|| differs from||Bz|| by at most||delta B||_2, and taking the successive min-max extrema preserves that bound. This statement bounds the difference between the two finite rules if their matrix arithmetic is exact. It does not bound either rule's error against the canonical operator.

Also recompute the unit-c_l action costs in each rule using the QR formula proved in the source protocols. Changes in those costs are sensitivities on these finite spans. They are not PDE lower bounds. Keep the existing exterior-tail bounds separate; their propagation through numerical gradients is labelled accordingly. Finite-difference and analytic gradient comparisons have their own records and are not attributed to this inverse-only experiment.

Every input file is already frozen in this verifier's directory. The run records its proof/code hashes, the state and direction hashes, and the prescribed point hash; its atomic output can resume without changing any input. The summarizer requires completed main and refinement arrays and checks every row, direction, state and configuration. These runs replace selected12-row sensitivity by full58-row sensitivity for the stated two cases. The earlier selected records remain valid and immutable. No measured refinement change is called a certified quadrature bound, a continuum singular value or either task endpoint.
