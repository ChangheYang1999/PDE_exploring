# Applying a fixed-state Jacobian correction exactly once

## Statement

Let m,n be positive integers, let M,C be real m by n matrices, let r be in R^m, let D be a diagonal n by n matrix with strictly positive diagonal entries, and let lambda>0. At this fixed state define T(A)=A+C. Then T(M)=M+C and T(T(M))=M+2C. If C is nonzero, the latter is not the corrected matrix T(M). For J=M+C the damped normal matrix J^T J+lambda D is positive definite, and the unique model step is d=-(J^T J+lambda D)^(-1)J^T r.

## Proof

Substitution gives T(T(M))=(M+C)+C=M+2C. Subtracting T(M) leaves C, which is nonzero under the stated hypothesis. For any nonzero x in R^n, x^T(J^T J+lambda D)x=||Jx||_2^2+lambda sum_i D_ii x_i^2>0. Therefore the matrix is invertible. Differentiating the quadratic 1/2 ||r+Jd||_2^2+lambda/2 d^T Dd gives J^T(r+Jd)+lambda Dd; its unique zero is the stated step, and positive definiteness makes it the unique minimizer.

## Dependencies and scope

Only finite-dimensional real linear algebra is used. C may depend on the fixed state but is independent of the input matrix A. For a recording function to add C a second time is incorrect whenever its input already equals M+C. This does not by itself change a previously computed optimizer step. No assertion about convergence of an Euler optimization, pressure approximation, floating-point error, or solution existence follows. Implementation tests must establish the actual order, values and metadata separately. A string label does not determine the matrix it describes.
