# Dimension loss from independent saved-piece jumps

## Statement before finite verification

Fix finite real piecewise polynomial radial functions B_j, each with
compact support in a finite logarithmic annulus, and put

    h_mj(x,y)=x^2 y B_j(log r) cos(2m theta), 0<=m<M.

Interpret saved binary64 data as exact dyadic real numbers. Suppose N
selected radial functions admit distinct increasing radii t_1<...<t_N
such that their value-jump matrix A_ij=[B_j](t_i) has A_ij=0 for i<j
and A_jj !=0. These hypotheses must be established on saved data; they
are not consequences of intended B-spline continuity.

Let V be any coefficient space of dimension n whose associated finite
piecewise smooth functions include these MN selected functions as
coordinate columns. Extra columns may be arbitrary finite piecewise
smooth functions with well-defined value traces at the selected circles.
Let T map coefficients to functions. If X is a weighted weak-gradient
space whose weights are positive and locally bounded with bounded
reciprocals on these circles, then

    dim( T(V) intersect X ) <= n - MN.

If the coefficient sets called Fminus, Fminus_noJ, free and free_noJ
contain all selected coordinates, the same bound applies with their
respective column counts. This includes any later constrained or
truncated subspace inside them. The bound does not assume that T is
injective, that a floating nullspace is exact, or that stored singular
vectors are available.

## Proof

The lower triangular matrix A has determinant product_j A_jj !=0. The
jump map on the selected N radial functions therefore has rank N.
For distinct angular modes, the functions cos(2m theta) are linearly
independent. Multiplying their finite combinations by cos^2(theta)sin(theta)
does not destroy independence: that factor is nonzero on an open arc,
and a trigonometric polynomial zero on an arc is identically zero.
At r=exp(t_i), the additional common factor r^3 is also nonzero.
Consequently the jump images of the MN selected functions are linearly
independent across the product of all selected circle trace spaces.
The full jump map J on V has rank at least MN even after extra columns
are added.

For a piecewise smooth function with a nonzero value jump, integration
by parts produces a nonzero circle measure in its distributional gradient.
No L2 function represents that measure: a smooth vector test supported
in a tube of width delta has L2 norm O(sqrt(delta)) while its measure
pairing has a nonzero limit. Local nondegeneracy of the gradient weight
therefore implies X membership only when all these jump traces vanish.
Thus T(V) intersect X is contained in T(ker J). Rank-nullity gives

    dim(T(V) intersect X) <= dim T(ker J)
                         <= dim ker J <= n-MN.

No independence of the full column functions was used. In particular,
a list of q>n-MN functions inside the encoded span cannot be an X-orthonormal
list: either some function is outside X or the list is linearly dependent.
This statement avoids guessing which alternative holds for a floating Q.

## Verification plan and scope

Select every strictly interior mode-zero spline as in topic130. Compute
all its value jumps exactly and order columns by the first nonzero jump.
Verify distinct pivots and all zero entries above the diagonal. Verify
from every saved mode's binary data that the selected radial functions
are exactly identical copies. One method uses exact rational Horner
values; a second uses direct binary64 bit decoding and direct power sums.
For a separate, smaller-arithmetic rank check, reduce all dyadics modulo
an odd prime, verify every diagonal is nonzero, and verify all upper entries
zero. Modular nonzero certifies rational nonzero because dyadic denominators
are invertible modulo the prime.

The optional comparison to a saved retained-column count is a comparison
to a finite JSON report only. No historical SVD, numerical rank or continuum
convergence is certified. The theorem concerns the exact functions encoded
by rounded piecewise coefficients. An intended exactly continuous B-spline
space or a conforming reconstruction is a different space, with an error
estimate still required to transfer rigorous matrix conclusions.
This is not a PDE nonexistence statement or a decisive endpoint.
