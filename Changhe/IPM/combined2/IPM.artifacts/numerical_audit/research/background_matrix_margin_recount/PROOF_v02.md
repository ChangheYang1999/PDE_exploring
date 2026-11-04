# Matrix margins from retained balanced-root intervals

This argument is written before the new finite recount. It applies the matrix identity already used in background_capped_matrix_lower/PROOF.md to a successfully admitted balanced root. It does not repeat the source reconstruction.

## Statement

Fix Candidate 007, correction C2-N1-013 and c = 4076476460239181/2251799813685248. Put q = 21/10, eta = 1/4, psi = partial_y chi_007 + phi_013, rho = -Delta psi, u = (-psi_xy, psi_xx), V = cX + u, and

    M = (c + 1 + V.X/(eta + |X|^2)) I - q Sym DV
        + [[rho_y, -rho_x/2], [-rho_x/2, 0]].

Set t = |X|^2/(1 + |X|^2), z = cos(2 theta) and d0 = (1 + 3t)/4. Import the established source identity

    d0 (M - (3/5) I) = [[a, sin(2 theta)e], [sin(2 theta)e, b]].

Let j be a balanced root index, 0 <= j < 127, with radial interval [j/128, (j+1)/128]. Suppose a successfully admitted exact result supplies containing rational intervals for a, b and e on every leaf of a complete angular partition. The fixed source, successful result and prior actual adoption must authenticate. For a leaf z in [z_L,z_U], let a_L and b_L be its lower diagonal endpoints and e_U the maximum absolute endpoint of e. Define

    K = 1, if 0 belongs to [z_L,z_U],
        1 - min(z_L^2,z_U^2), otherwise;
    D = ((a_L-b_L)/2)^2 + K e_U^2.

For d = 10^12, put n = isqrt(floor(D d^2)) + 1, U = n/d and L = (a_L+b_L)/2 - U. Define d_min = (1+3j/128)/4 and d_max = (1+3(j+1)/128)/4, and set

    ell_leaf = 3/5 + L/d_min, if L < 0;
               3/5 + L/d_max, if L >= 0.

Then lambda_min(M(X)) >= ell_leaf on this leaf. The minimum over its complete angular cover is a lower bound on the whole root. If the previously admitted root also proves M >= (3/5)I, the maximum of 3/5 and this minimum is another valid lower bound. These statements are conditional on the imported containing intervals; checking their algebra alone does not independently establish source containment.

## Argument

Decreasing the two diagonal entries to a_L and b_L subtracts a positive semidefinite diagonal matrix. It therefore cannot increase the minimum eigenvalue. For fixed diagonal entries, the smaller eigenvalue is (a_L+b_L)/2 minus the square root of ((a_L-b_L)/2)^2 plus the off-diagonal square. The latter square is at most K e_U^2 throughout the leaf. The integer construction gives ((n-1)/d)^2 <= D < (n/d)^2, so U is a strict upper bound for its nonnegative square root. The scaled minimum eigenvalue is consequently at least L.

Because d0 is positive, division preserves the inequality. For negative L the smaller quotient uses d_min; for nonnegative L it uses d_max. Adding 3/5 proves the displayed bound. Every point of the radial root and every angle lies in some closed leaf by the imported exact partition. Taking the finite minimum proves the root bound. Taking its maximum with an independently proved lower bound is valid because both inequalities hold pointwise.

All new arithmetic is rational except the integer square root, whose defining inequalities are checked exactly. Rounding a lower value x to floor(10^12 x)/10^12 is outward. A lower bound below a proposed target shows only failure of this sufficient interval estimate. It does not exhibit an eigenvalue below the target. Conversely, sampled values cannot prove a uniform bound.

## Dependencies and scope

The source identity and interval-containment result are imported from background_balanced_replay/PROOF.md and the exact root's standalone proof. The eigenvalue formula and directed integer arithmetic also agree with background_capped_matrix_lower/PROOF.md. This adapter accepts a CONFIRMED_LOCAL_COMPONENTS publication, its unique COMPLETED_BALANCED_ROOT_REPLAY archive, and its matching PASS_ADOPTED_BALANCED_COMPONENTS check. It authenticates all publication files, requires the primary aggregate and primary adoption flag to be true, and checks that the archive, receipt and actual-review hashes in the component check agree with the publication. It obtains the index and source from the archive, not absent top-level publication fields. The complete ordered binary angular leaf partition is checked exactly as in version 1. This representation change does not alter the eigenvalue formula or its proof. Standard roots, rectangular slabs and the infinite exterior are not silently included by this adapter.

The motivating corrected H4 comparison uses beta_star - b0, rather than c + 1 - q - b0 without a further proved estimate. This recount can assess only the matrix component of that budget on its selected root. It proves no global matrix bound, near norm, H4 composition, inverse, invariant ball or existence theorem. Any actual numerical output requires its own independent review before a larger matrix constant is called certified.
