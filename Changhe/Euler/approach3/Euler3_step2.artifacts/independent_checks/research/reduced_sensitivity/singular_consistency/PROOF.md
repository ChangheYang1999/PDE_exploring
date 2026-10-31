# Singular values of a saved QR factor

Status: proved finite-dimensional identities and bounds. Numerical use requires verified hypotheses; ordinary floating-point residual checks alone are not rigorous enclosures.

Let J be a real m by n matrix with m >= n, D a positive diagonal n by n matrix, and Pi an n by n permutation matrix. Suppose J Pi D^{-1}=Q R, where Q is real m by n with Q^T Q=I_n and R is real n by n. Then R and J Pi D^{-1} have exactly the same singular values, including multiplicities and zeros. Indeed their Gram matrices agree: (Q R)^T(Q R)=R^T R. Their squared singular values are the eigenvalues of that common positive semidefinite matrix. A discrepancy between singular values reported from J Pi D^{-1} and R therefore needs an arithmetic or provenance explanation; ill-conditioning of small singular values alone does not permit an arbitrary error in the largest one.

For an a posteriori check, let A,U,V be real n by n matrices, S=diag(s_1,...,s_n), s_1>=...>=s_n>=0, and E=A-U S V^T. Suppose ||U^T U-I||_2<=delta_u<1 and ||V^T V-I||_2<=delta_v<1. Then

max(0, s_1 sqrt((1-delta_u)(1-delta_v))-||E||_2) <= ||A||_2
<= s_1 sqrt((1+delta_u)(1+delta_v))+||E||_2.

For every vector x, the inequalities (1-delta_u)||x||^2 <= ||U x||^2 <= (1+delta_u)||x||^2 follow by evaluating x^T(U^T U-I)x. The analogous statements hold for V, so both matrices are invertible. Submultiplicativity gives ||U S V^T||_2 <= sqrt((1+delta_u)(1+delta_v)) s_1. Also S=U^{-1}(U S V^T)V^{-T}; the inverse norm bounds imply ||U S V^T||_2 >= sqrt((1-delta_u)(1-delta_v)) s_1. Apply the triangle and reverse triangle inequalities to A=U S V^T+E, and use nonnegativity of ||A||_2. Replacing every norm on the right by a proven Frobenius-norm upper bound remains valid, since the sum of squared singular values bounds their largest square.

Dependencies: the spectral theorem for real symmetric matrices, the variational characterization of the operator norm, and the elementary triangle inequalities. The theorem has no hypothesis that A is nonsingular. It is a statement about exact matrices; empirical binary64 reconstructions and orthogonality defects support a numerical diagnostic but do not certify these inequalities with rigorously rounded endpoints. The calculation does not validate a Jacobian from the PDE, an exact rank, a tiny singular value's relative accuracy, or stationarity.
