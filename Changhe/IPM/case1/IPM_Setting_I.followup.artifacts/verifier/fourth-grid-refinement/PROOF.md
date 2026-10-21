# Separate angular and radial inverse sensitivities for the fourth grid

Date: 2026-10-20. Protocol written before these additional inverse evaluations.

## Objects and exact finite statement

The state is the byte-frozen84x35,L=8 candidate in ../fourth-grid-actions/data/dnB_n84m35S.npz. The14directions and58physical points are exactly those prepared for that topic. The first ten directions are reconstructed from supplied arrays using the verifier's SVD; four are the verifier's calibration directions. No code from the numerics lane is used. This protocol adds no solver or new continuum claim.

For fixed computed density rho_i, gradient g_i, direction density d_ij, direction gradient h_ij and delta-c_l t_j at point X_i, the unnormalized directional residual with inverse rule r is

    L_(r,ij)=(c_l X_i+U_(r,i)).h_ij
                         +(t_j X_i+V_(r,ij)).g_i-d_ij.

Here U is the velocity of the fixed state and V is the velocity of its density direction, evaluated by the independently implemented full-plane paired kernel integral. Define N_i=|rho_i|+sum_a |(c_l X_i+U_(fine,i))_a g_(i,a)|, fixed from the original fine pass, and

    A_(r,ij)=L_(r,ij)/(sqrt(58)N_i),
    M_(ij)=d_ij/(sqrt(58)(1+|rho_i|)), M_(59,j)=t_j.

All normalizers must be positive. The physical metric is ||M z||_2. We compare nested spans of dimensions4,10,14 only after verifying full column rank of M and of each measured A. These are finite matrices, not norms on a continuum function space.

The original fine pass uses4096angles, radial order32 and logarithmic panel width.075. The two extra full58point passes use2048and4096angles, both radial order24 and panel.1. All use the same exterior radius1e30 and density/directions. The2048-to4096difference changes only angular resolution; the4096extra-to-original difference changes only radial order/panel width. Thus angular and radial sensitivities are separately observed. A pair of agreeing rules is not a rigorous bound on their common error.

At fixed fields and gradients, subtraction gives the exact identity

    A_b-A_a=((U_b-U_a).h+(V_b-V_a).g)/(sqrt(58)N).

It is proved by cancelling the common c_l,density and delta-c_l terms. This identity reconstructs each action from the original and the added velocities. The separate audit instead recomputes each matrix entry directly by scalar loops from the defining formula and independently reconstructs M and N_i.

If M=Q T is a reduced QR factorization, ||M z||_2=||T z||_2, so the measured minimum action in that metric is the smallest singular value of A T^-1. For the unit-c_l cost, assume A has full column rank and t!=0. With A=Q_A R_A, the constrained minimum of ||A z||_2 subject to t.z=1 is1/||R_A^(-T)t||_2 by Cauchy-Schwarz, attained in the corresponding dual direction. The audit uses independent SVD coordinates and checks the constraint and attained cost, rather than repeating the QR computation. It also reports the operator and Frobenius norms of the two action differences after the same metric transformation.

## Scope and verification

This extends the already reviewed finite-matrix protocol of ../full-action-refinement/PROOF.md to the fourth state. No additional mathematical stability assumption is introduced. It tests all58rows, rather than selected points. Source bytes, directions, points, proof, code and imported dependencies are pinned before the new computation and checked afterward. The evolving primary action output is checked only after completion and then pinned in the summary. CPU/GPU density agreement and two Cartesian gradient steps are checked by the original fourth-grid action program; this added program holds those gradients fixed.

The exterior tail estimates and fixed-field center proofs are separate evidence. These inverse differences do not certify the interior quadrature, the full-plane residual, a continuum singular value, a kernel dimension, an isolated profile, a family, or an endpoint. Partial passes are labelled incomplete and are not included in a final finite-matrix claim.
