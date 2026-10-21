# Angular refinement: matching the compared subspaces

Date: 2026-10-20. Status: independent algebraic audit of supplied floating matrices, not a certificate of a continuum derivative.

## Statement, objects and method

The saved state dnSB has N=120 radial intervals and M=48 angular nodes. Its nodal density factor is a tensor Chebyshev polynomial, with angular coordinate s related to physical theta by theta=s+0.45 sin(2s). The two supplied target states have the same N, radial map, c_l, C and physical angular coordinate, and M=64 or96. The target files contain Q1, an orthonormal basis of ten interpolated directions, D1, their central finite-difference actions at step10^-4, V1, the original interpolated directions, and z1, the projected state. No solver or inverse from the numerics lane is imported or executed in this audit.

The code independently applies a cosine transform to each angular nodal row, evaluates that polynomial at the new Gauss nodes, and compares with V1 and z1. It uses NumPy QR and SVD to check orthogonality, reconstruction, singular values and action norms. The original directions are columns of Vsoft_unscaled, the first ten physical-node-normalized matrix singular vectors. They are not the first ten Ritz vectors of the separately supplied24-dimensional action matrix.

The source matrix file contains an orthonormal Q with24 columns and supplied action matrix D. Set Q0 to an independently computed orthonormal basis of the ten columns Vsoft_unscaled. Since Q0 lies in range(Q), form

    D0 = D (Q^T Q0).

This is the restriction of the supplied linear action matrix to the same ten-dimensional source subspace. It does not independently recompute finite differences in the Q0 directions. Any error in the supplied actions remains, and applying a combination of finite differences is not literally an exact derivative computation.

## Exact linear algebra behind the comparison

If Q has orthonormal columns and Q0 lies in its range, Q Q^T Q0=Q0. For an exact linear operator J and D=JQ, one has D0=JQ0. Thus singular values of D0 give the operator's singular values on that ten-dimensional subspace in the chosen Euclidean norms. They need not equal the ten smallest singular values of D: minimizing over a larger24-dimensional space permits additional cancellations. In particular, comparing the two smallest24-space Ritz values with ten-space target values changes both discretization and subspace. It cannot isolate the effect of angular refinement.

If Q1 is orthonormal and V1=Q1 T, the action on each unit-normalized original interpolated vector is D1 T_j/|V1_j|. The singular values of D1 minimize over all combinations and are not those individual norms. This distinction is material here. The target orbit residual norms also change with the target discretization; they are not density approximation error norms. Indeed angular interpolation to M>=48 preserves the exact polynomial density representation, before rounding.

## Independently recomputed numbers

The coarse ten-space singular values from D0 are

    2.57986467649e-6, 9.64119152375e-6, 2.89261937064e-5,
    9.29517537242e-5, 1.92109024879e-4, 3.51825986921e-4,
    5.01067318842e-4, 6.62791827912e-4, 8.85928164658e-4, 1.12697813553e-3.

The24-space values instead begin1.71970255120e-6 and2.92879371511e-6. The source subspace reconstruction error is1.77e-15 in Frobenius norm. The target Q1 orthogonality and V1 reconstruction errors are below1.6e-15. Independently reconstructed target state and direction entries differ by at most4.27e-14 and1.69e-14, respectively. Thus the intended angular interpolation is confirmed to rounding precision.

For M=64 the ratios of the supplied target Ritz values to the matched coarse ten-space values are

    10.304, 7.971, 5.973, 3.310, 2.091, 1.781, 2.727, 3.950, 4.156, 5.623.

For M=96 they are

    11.762, 9.487, 6.299, 3.614, 2.136, 1.797, 2.720, 3.872, 4.517, 6.511.

The M=96/M=64 Ritz ratios begin1.142 and1.190, and the largest ratio is1.190. They do not stay exactly fixed. Most of the change occurs between M=48 and64 in these samples. This observation alone does not identify its cause or establish saturation as M tends to infinity.

The first original unit direction has action8.60579e-6 in the source supplied matrix,1.16497e-3 on M=64, and1.34605e-3 on M=96. These individual actions differ from the minimum singular values. Other individual-vector norms and all hashes are in verification/audit.json. Recomputed target singular values and action norms agree with their JSON summaries to less than3e-17.

## Verdict and scope

CONFIRMED: the saved interpolation and matrix-summary arithmetic. REFUTED as readings of these files: that only the two softest directions change materially; that each other Ritz value changes by less than a factor two; that no further change occurs from M=64 to96; or that the source24-space Ritz vectors themselves were the ten interpolated inputs. The phrase "exact actions" must mean numerical central finite-difference actions, with unresolved approximation error.

OPEN: a resolution-independent kernel, the finer grids' own soft directions, a nonlinear family, and a continuum angular truncation error. A non-stationary projected state does not furnish a finer stationary branch. No matched radial-only test is present, so attributing the5.5e-3 residual on(144,56) solely to radial truncation is unsupported. Those tests change both N and M.

Dependencies: the explicit saved representation, cosine orthogonality, orthonormal projection and SVD. No formal build is used. Every displayed decimal is a floating calculation, not an interval enclosure. The exact finite-dimensional identities above explain what that calculation can test.
