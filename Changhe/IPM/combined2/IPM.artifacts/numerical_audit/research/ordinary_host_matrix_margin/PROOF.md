# Stronger matrix bounds from a complete ordinary-host reconstruction

This argument precedes the adapter. It is a conditional finite arithmetic statement, not a certificate that the pending host has completed.

## Statement, notation and hypotheses

Fix the Source013 fields and c = 4076476460239181/2251799813685248. For q = 21/10 and eta = 1/4 let

    M = (c+1+V.X/(eta+|X|^2)) I - q Sym DV
        + [[rho_y,-rho_x/2],[-rho_x/2,0]],
    V = cX+u, t = |X|^2/(1+|X|^2), s = 1-t, d0 = 1-3s/4.

Import the field identity

    d0 (M-(3/5)I) = [[a,sin(2theta)e],[sin(2theta)e,b]].

Assume the complete ordinary-host reconstruction and its exact local recount have succeeded for the 42 slabs j = 97,96,...,56. The host record must authenticate every containing interval and its exact source, the successful resource guard, and its complete 32 by 256 product partition. Independent actual review of that host is a separate hypothesis for calling the resulting matrix bounds certified.

Slab j has t in [j/128,(j+1)/128], equivalently |X|^2 in [j/(128-j),(j+1)/(127-j)]. Put sigma = (255-2j)/256 and rho0 = 1/(255-2j), so s = sigma(1+x), -rho0 <= x <= rho0. All endpoints are included. Let aL,bL be the containing lower diagonal endpoints on one product cell, eU the larger absolute endpoint of e, and K the smaller of 1 and the containing upper endpoint of sin(2theta)^2. Let

    D = ((aL-bL)/2)^2 + K eU^2,
    n = isqrt(floor(10^24 D))+1,
    L = (aL+bL)/2 - n/10^12.

For radial index u in {0,...,31}, define xlo = -rho0+2rho0 u/32, xhi = -rho0+2rho0 (u+1)/32, dmin = 1-3sigma(1+xhi)/4 and dmax = 1-3sigma(1+xlo)/4. Set ell = 3/5+L/dmin if L<0, otherwise ell = 3/5+L/dmax. Then M >= ell I on that cell. The least ell over all cells, rounded downward to a multiple of 10^-12, is a valid uniform matrix lower on the slab. The minimum of the 42 slab bounds is valid on 7/9 <= |X|^2 <= 49/15.

## Complete argument

The containing source premise gives a >= aL and b >= bL. Subtracting diag(a-aL,b-bL) decreases a symmetric matrix in the positive-semidefinite order. For the matrix with these lower diagonals, the exact smaller eigenvalue is the diagonal mean minus the square root of half the diagonal difference squared plus the off-diagonal square. Since 0 <= sin(2theta)^2 <= K and |e| <= eU, this eigenvalue is at least the mean minus sqrt(D).

The integer square-root identity implies (n-1)^2 <= 10^24 D < n^2; the implementation explicitly verifies both inequalities. Consequently n/10^12 is a strict upper bound for sqrt(D), and L is a lower bound for the scaled matrix eigenvalue. The affine formula for d0 gives 0 < dmin <= d0 <= dmax. The stated sign-dependent denominator therefore gives L/d0 >= ell-3/5. Division by d0 and addition of 3/5 prove the cell claim.

The checked product index set contains exactly every pair of radial and angular indices, with no duplicates. By the imported containing-cover theorem this covers each slab. Taking a minimum proves its uniform lower bound; rounding downward preserves it. Consecutive closed slabs share their endpoints. Their union is t in [56/128,98/128], equivalently |X|^2 in [7/9,49/15], so taking the least slab lower proves the final assertion.

## Authentication and scope

The adapter takes an explicit local recount path and expected digest. It binds the recount's complete campaign dependency map, requires all 42 slabs in their prescribed order, and checks each archive digest against that map. It verifies source geometry, typed successful primary flags and the complete product partition again. The entire input map is rehashed after arithmetic. It records exact rational bounds and source archive hashes. It does not rerun any foreign program and does not alter the host request, numerical source code or resource allocation.

An actual output remains conditional until the source reconstruction and this stronger recount receive distinct independent review. No global matrix statement follows without the separately admitted inner and outer covers. No gradient or strain improvement, near bound, H4 remainder bound, inverse, invariant ball or stationary existence theorem is asserted. A lower bound below a target is inconclusive about the actual matrix.

Dependencies: ../ordinary_slabs_host_method/PROOF.md and code/recount_v01.py for the complete source and host contract; ../background_matrix_margin_recount/RECTANGULAR_PROOF_v01.md for the same eigenvalue calculation on previously admitted rectangular regions. Exact source archive SHA256: 2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d.
