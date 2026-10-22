# Exact external constraint rank and the meaning of a numerical SVD cut

## Statement and exact model

Let t_-<t_+ be the exact stored external join radii in logarithmic coordinates of a frozen finite section. Let its M angular factors be Phi_m(theta)=cos(theta)^2 sin(theta) cos(2m theta), m=0,...,M-1. They are linearly independent: divide a vanishing linear combination by cos(theta)^2 sin(theta) on a nonempty open interval and use independence of finite cosine polynomials. Represent h=r^3 sum_m B_m(log r) Phi_m(theta). For each m define the four external matching functionals

    B_m(t_-^-)-B_m(t_-^+), B'_m(t_-^-)-B'_m(t_-^+),
    B_m(t_+^-)-B_m(t_+^+), B'_m(t_+^-)-B'_m(t_+^+).

The claim concerns matching at these two circles only. It imposes no internal spline matching and supplies no Sobolev membership assertion.

Assume that for each m the column family contains four columns with the following radial factors. Two inner columns are exp(alpha_1(t-t_-)) and exp(alpha_2(t-t_-)) on t<t_-, extended by zero to its right, with alpha_1!=alpha_2. Two outer columns are exp(beta_1(t-t_+)) and exp(beta_2(t-t_+)) on t>t_+, extended by zero to its left, with beta_1!=beta_2. The frozen files are to be checked for these precise supports, coefficients, anchoring and distinct exponents before applying the claim. Under these hypotheses the full matrix C of the4M functionals on the coefficient space has exact row rank4M. This stays true after multiplication by any invertible diagonal column scaling and any invertible row scaling.

## Rank proof

For one angular mode, the four chosen columns give the submatrix

    [1 1 0 0; alpha_1 alpha_2 0 0;
     0 0 -1 -1; 0 0 -beta_1 -beta_2].

Its determinant is (alpha_2-alpha_1)(beta_2-beta_1), which is nonzero. Different modes have disjoint selected columns and separate functionals. The selected4M by4M minor is block diagonal with these invertible blocks. Hence rank(C)>=4M; there are only4M rows, so equality follows. Multiplication by invertible matrices preserves rank. With n input coefficients, the external constraint kernel has dimension n-4M. These are coefficient-space dimensions, without an assumption that every encoded field is in a common function space.

## What a truncated singular decomposition does

For any real matrix C and its exact singular value decomposition C=U Sigma V^T, retaining r positive singular values defines C_r=U_r Sigma_r V_r^T. The retained right orthogonal complement is ker(C_r), whose codimension is r. It is the kernel of the r linear combinations U_r^T C of the original row functionals. In general these are not a subset of the original named rows.

A concrete proof of the distinction uses C=[[1,0],[epsilon,epsilon]], with 0<epsilon<1/4. The off-diagonal entry of C C^T is epsilon, so neither eigenvector of that symmetric matrix can be a coordinate vector: multiplication of either coordinate vector produces a nonzero component on the other axis. Thus its leading singular functional combines both original rows with nonzero coefficients. Truncating to rank1 does not mean deleting one named row. The phrase 'dropped the outer C0 rows' can summarize an approximately aligned lost subspace, but an exact identification requires a separate row-space comparison.

If rank(C)=4M but an exact truncated map keeps only r<4M independent constraints, its kernel is strictly larger, by4M-r dimensions. This statement does not show that a subsequently retained and smaller trial space contains a violating vector: that later space must be checked. Nor does a small computed join residual prove exact membership.

## Intended finite audit and scope

The application will read the stored M16 and M24 radial columns with a restricted pickle reader, export only the four selected pure-exponential columns per mode to exact JSON, and check all endpoint and exponent identities using exact rationals. A separate checker will reconstruct the four-column minors from that JSON by Gaussian elimination and by a determinant expansion; it must inspect the original selected source entries independently as well. The small SVD example may be checked symbolically; it is not a numerical surrogate for the actual large singular vectors.

The numerical lane's reported ranks48/64 and72/96, and corrected full ranks, remain source-reported floating computations unless independently reproduced and certified. The exact rank theorem does not certify those SVD outputs, identify all dropped directions, transfer the operator spectrum, repair internal spline jumps or establish an IPM endpoint. Its purpose is to distinguish a mathematically complete external constraint matrix from a tolerance-dependent truncation.
