# Widths in optimizer coordinates and logarithms of physical widths

Status: proved finite-dimensional identities. Neither model is the nonlinear Euler objective.

## Statement and notation

Let p_0=(c_0,w_0) lie in an open subset of R^2 with w_0>0. Let p=Phi(z) be a differentiable parameter map near z_0, with Phi(z_0)=p_0, Phi_2(z)=exp(z_2), and derivative C=diag(C_1,w_0) at z_0, where C_1>0. Let J_p be a real m by 2 parameter Jacobian and J_z=J_p C. Let D_p be a positive diagonal 2 by 2 scaling and set D_z=D_p C. Coefficient columns, their scaling and their permitted subspace are held fixed in both descriptions.

Suppose the coefficient-minimized linear least-squares model in common scaled coordinates h is q(h)=q(0)+g^T h+(1/2)h^T S h, where S is real symmetric positive definite. Its minimizing displacement is h_*=-S^{-1}g. Let e be a unit eigenvector of S with eigenvalue lambda>0. For epsilon>0 and L>0 put t=sqrt(2 epsilon L/lambda).

There are two distinct coordinate interpretations of the same scaled quadratic:

1. The affine optimizer-coordinate model uses z=z_0+D_z^{-1}h. Its logarithmic omega coordinate is exactly z_2. Its minimizing logarithmic coordinate is z_{*,2}=z_{0,2}+(D_z^{-1}h_*)_2, and the signed half-widths along e are exactly +/- a, where a=(D_z^{-1}te)_2. They do not depend on the location of the minimum.
2. The affine physical-coordinate model uses p=p_0+D_p^{-1}h. Write w_*=w_0+(D_p^{-1}h_*)_2. If w_*>0 and both w_*+w_0 a and w_*-w_0 a are positive, its exact signed logarithmic displacements from its physical minimum are log(1+w_0 a/w_*) and log(1-w_0 a/w_*). They generally have unequal magnitudes and generally differ from +/- a.

Both models have rise epsilon L from their respective model minima at the common scaled points h_* +/- te. The models agree under the affine relation delta p=C delta z. They need not agree under the finite nonlinear map p=Phi(z).

## Proof

Since the diagonal matrices commute and are invertible,

J_z D_z^{-1}=J_p C (D_p C)^{-1}=J_p D_p^{-1}.

Thus the scaled parameter columns are identical. The fixed coefficient block and its permitted subspace are also identical, so minimizing over those coefficients gives the same q, g and S. Completing the square gives q(h_*+v)-q(h_*)=(1/2)v^T S v. Substituting v=+/-te gives t^2 lambda/2=epsilon L.

In the optimizer-coordinate affine model, subtracting z_0+D_z^{-1}h_* from z_0+D_z^{-1}(h_*+/-te) gives +/-D_z^{-1}te. The second coordinate equals log omega under the stipulated parameter map, so its displacement is exactly +/-a.

In the physical-coordinate affine model, subtracting p_0+D_p^{-1}h_* from the corresponding two endpoints gives +/-D_p^{-1}te. Since D_z=D_p C, we have D_p^{-1}=C D_z^{-1}; hence the second component of this displacement is +/-w_0 a. Under the stated positivity assumptions, subtracting log w_* from the logs of the two physical endpoints gives the claimed log(1+/-w_0 a/w_*) expressions.

Finally, delta p=C delta z is the tangent map at z_0. A differentiable nonlinear Phi does not in general equal Phi(z_0)+C delta z at finite delta z. In the omega coordinate, the optimizer model minimum maps to w_0 exp((D_z^{-1}h_*)_2), whereas the physical affine minimum is w_0(1+(D_z^{-1}h_*)_2). The two are generally different. This proves the distinction.

## Exact example

Take w_0=1, D_p=D_z=I, S=I, g=(0,-1), e=(0,1), and choose epsilon L=1/200. Then h_*=(0,1), t=1/10 and a=1/10. The optimizer log-coordinate half-widths are +/-1/10. The physical minimum has w_*=2, so its exact log displacements are log(21/20) and log(19/20). Both physical endpoints are positive. These values exhibit the distinction without numerical rounding or a singular matrix.

## Dependencies and scope

Dependencies: the chain rule, inversion of positive diagonal matrices, the spectral theorem in R^2, and the coefficient-minimized quadratic identity in ../PROOF.md. The assumptions do not assert admissibility of the model minimum in a bounded physical c interval, accuracy of a saved floating factor, nonlinear parameter uncertainty, or existence of an Euler solution. A report must label which coordinate model its quoted width uses. The registered branch comparison uses optimizer-coordinate displacements; converting an affine physical width to a logarithm answers a different question.
