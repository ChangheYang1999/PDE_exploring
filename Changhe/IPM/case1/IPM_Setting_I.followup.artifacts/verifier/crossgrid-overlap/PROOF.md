# Comparing perturbations at fixed physical points

Date: 2026-10-20. Status: exact differentiation and finite-data comparison. No convergence theorem is asserted.

## Statement, hypotheses and notation

For each saved nodal field let c=c_l>1, k=1/c, L>0, and |beta|<1. Its density is

    rho(x,y)=x^2 y exp[(k-3) ell/2] b(q,s),
    ell=log(1+(x^2+y^2)/L^2),
    q=1-exp[-(1-k)ell/2],
    theta=s+(beta/2)sin(2s),

with reflection parities outside the first quadrant. Here b is the finite tensor polynomial reconstructed from the saved nodes. A parameter direction consists of a polynomial delta b defined by its nodal values, a scalar delta c, and an auxiliary scalar delta C which does not occur in this density formula. L and beta remain fixed. At physical points with rho nonzero its relative variation is exactly

    delta rho/rho = delta b(q,s)/b(q,s)
       - delta c ell/(2c^2) [1-(1-q)b_q(q,s)/b(q,s)].       (1)

In general this differs from both delta b(q,s)/b(q,s) and the interpolant of the nodal ratios delta b_ij/b_ij. Comparisons at two finite grids, even with overlap arbitrarily close to one in a specified norm, do not alone prove convergence of individual directions, subspaces, or continuum kernels.

## Proof

Hold x,y fixed. Differentiating k=1/c gives delta k=-delta c/c^2. The angular coordinate does not change because beta is fixed. Differentiating q gives delta q=-(1-q)ell delta k/2. Differentiating the prefactor gives its logarithmic derivative ell delta k/2. The product and chain rules therefore give

    delta rho = x^2 y exp[(k-3)ell/2]
      {delta b + ell delta k [b-(1-q)b_q]/2},

which proves (1) after division by rho. The auxiliary scalar delta C contributes zero. All differentiations are justified since c>1 and b is a finite polynomial in its interpolation coordinates.

Interpolation is a linear map, not a quotient-preserving map. For example the linear interpolants of b=1+x and delta b=1 on the nodes x=0,1 have actual ratio 1/(1+x), whereas interpolation of the two nodal ratios gives 1-x/2. These differ at x=1/2. Thus interpolation of nodal ratios cannot replace the quotient of the two interpolants without a separate error estimate. The last term in (1) also need not vanish.

For two sampled direction matrices A,B with positive diagonal weight matrix W, define their individual absolute overlaps by

    |A_i^T W B_i| / sqrt[(A_i^T W A_i)(B_i^T W B_i)].

If the columns are linearly independent, take thin QR factorizations of W^(1/2)A and W^(1/2)B. The singular values of Q_A^T Q_B are the principal cosines of their spans in this finite weighted inner product. This follows because Q_A,Q_B are orthonormal bases and changing either basis multiplies the matrix by an orthogonal factor. The cosines belong to [0,1]. They measure the given sampled spaces only. In particular a single favorable pair of grids cannot constrain a third grid, and hence cannot prove convergence. A small action under a discretized operator also needs operator consistency and derivative error estimates before it implies a continuum near-kernel.

## Numerical method and scope

The code reconstructs each tensor polynomial by its own DCT coefficient conversion, evaluates it by separate radial and angular polynomial matrices, and uses (1). It computes three distinct comparisons: interpolation of nodal ratios, quotient of interpolated variations and states, and physical relative density variation. The first reproduces the stated numerics metric without importing its code. The two others quantify its interpretation. Every comparison uses the same fixed physical polar points for both states.

The reported norm uses radii geometrically spaced from 0.02 to 20000, midpoint angles in (0,pi/2), and weights r times the finite-difference radial cell width times the angular width. Both the full window and its r<200 subset are checked, at 160 by72 and320 by144 sampling resolutions. The area weight emphasizes large radii for fields of comparable relative amplitude; this fact follows directly from the factor r dr. It is not a near-field norm. Rank and within-space Gram condition numbers are recorded. Direct finite parameter differences independently test (1) at fixed physical points.

The source directions are the first six stored node-norm matrix singular vectors from each completed state. They are supplied data, not independently recomputed singular vectors. This calculation checks their stated overlap and physical meaning. It does not verify their residual actions or establish a nonlinear family. Own full-plane physical checks of the two states are in ../grid-states and ../inverse, and previous matched-action audits are in ../angular-refinement and ../far-row. Exact source hashes, code and floating evidence are adjacent. No formal build is used.
