# What the two-way grid transfer measures

Date: 2026-10-20. Status: finite array audit and an exact counterexample to an inference. The continuum family question remains open.

## Objects, hypotheses and statement

Let V contain k supplied parameter directions, including the density nodes, c_l and C, in the unscaled Euclidean coordinate norm. Let I transfer their density part by the source tensor interpolant to a second grid of the same compactification scale and angular map, and leave the last two coordinates unchanged. Here both scales are L=8. At fixed c_l the compactified radial coordinate is the same on both grids. Hence the transfer is a linear interpolation in q and s, even when the residual is then evaluated at a separately solved target state with a different c_l. It is not a test of the linearization at the projected source state.

Write IV=QT, where Q has orthonormal columns. Suppose the stored columns D_j are the measured centered differences [F(z+hQ_j)-F(z-hQ_j)]/(2h). The singular values of D are the singular values of this measured linear map on the Q coordinates. The reconstructed action on the j-th unit interpolated direction is the j-th column of DT divided by |(IV)_j|. This follows from IV=QT and linearity of the map Qx -> Dx. For nonlinear F this reconstruction is not exactly its centered difference on a new combined direction at the same finite h. That requires a separate remainder estimate or a direct measurement.

If the true derivative satisfies ||D-DF(z)Q|| <= eta, each restricted singular value differs by at most eta, by the variational characterization and the triangle inequality. A columnwise bound e gives only eta <= sqrt(k)e. Comparing steps for one column does not bound every column or the derivative truncation error. Without eta, numerical singular values are not rigorous upper bounds on exact derivative singular values. Conditional on controlled eta, minimax gives upper bounds for the ordered small singular values of the full matrix, not lower bounds or a kernel dimension.

Independent tensor DCT reconstruction, NumPy QR/SVD and saved-state comparison check the target arrays and all target action summaries. The source ten-direction Ritz numbers have only scalar JSON summaries: D0 is not in the cross-grid PT file. They cannot be independently reconstructed from that file. A later source Ritz artifact can supply separate action data. Data provenance and this limitation are part of the verdict.

## Why a converging pair of soft subspaces is insufficient

Even exact singular values and converging right directions, together with consistency on a dense core, need not identify the continuum kernel. Here is an explicit example. The continuum operator on l2 is the identity. On span(e1,...,en), n>=2, define

    A_n = I + n e1 tensor e_n.

For every finitely supported x, A_n x=x for all sufficiently large n. Thus the matrices are consistent on the dense core of finitely supported vectors. They are also the exact Jacobians of the linear equations F_n(x)=A_n x, with unique root zero. But

    v_n = (e1 - e_n/n)/sqrt(1+n^-2)

has unit norm, tends strongly to e1, and |A_n v_n|=1/sqrt(n^2+1) tends to zero. The exact smallest singular value of the two-dimensional block [[1,n],[0,1]] is

    2/(sqrt(n^2+4)+n),

so the true smallest singular value also tends to zero. Its right singular vector tends to e1. The continuum identity has no kernel. Uniform stability or appropriate operator convergence fails: ||A_n|| grows like n. All assertions follow by direct multiplication and the determinant-one singular-value relation. Finite-dimensional arithmetic in code/audit.py checks sample instances without substituting for the proof.

This example does not claim that the IPM discretization has this defect. It refutes the unconditional inference that observed convergence of soft vectors alone rules out a numerical mode. With only two grids, even the stated convergence is an observation of agreement at two resolutions, not a limit theorem. Physical and parameter metrics must also be specified, as in ../crossgrid-overlap/PROOF.md.

## Scope of the experiment

Large actions after interpolation show that these transferred directions are not soft in the target measured system. They do not exclude softer directions computed independently on that target grid. Small target actions, with an error bound, constrain the target derivative but do not alone establish a nonlinear family. The two-way experiment can demonstrate transfer sensitivity; it cannot decide isolation, kernel dimension, a smooth branch, or either endpoint. All supplied action entries remain supplied numerical data. No numerics solver, residual, differentiation or inverse code is imported or executed by this audit.
