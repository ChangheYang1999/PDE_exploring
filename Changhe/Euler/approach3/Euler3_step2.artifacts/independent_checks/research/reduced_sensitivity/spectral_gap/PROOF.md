# What a singular-value discrepancy can bound

Status: proved finite-dimensional statements. Application to the producer Jacobian is conditional on an independently established matrix-error bound, which is currently absent.

## Statement and notation

Let A and B be real m by n matrices, m >= n >= 1. Let sigma_1(A) >= ... >= sigma_n(A) >= 0 be their singular values, including zero values. Write ||.||_2 for the Euclidean operator norm. For 0 < t < 1 define the strict retained count k_t(A) = #{i: sigma_i(A) > t sigma_1(A)}. Suppose sigma_1(A) > 0 and ||A-B||_2 <= delta. Then

|sigma_i(A)-sigma_i(B)| <= delta for all i,

and k_t(A)=k_t(B) whenever

min_i |sigma_i(A)-t sigma_1(A)| > (1+t) delta.                 (1)

Without a bound on ||A-B||_2, a measured discrepancy in sigma_1 alone implies no bound on the retained count. Equality even of every singular value implies no bound on residual projection onto the retained left singular space.

## Proof

For every unit vector x, the triangle inequality gives ||Ax|| <= ||Bx|| + ||A-B||_2, and its reversed version gives the opposite inequality. The min-max formula

sigma_i(A) = min_{dim S = n-i+1} max_{x in S, ||x||=1} ||Ax||

therefore gives sigma_i(A) <= sigma_i(B)+delta and the same inequality with A and B exchanged. For completeness this min-max formula follows by expanding x in an orthonormal eigenbasis of A^T A. The span of the last n-i+1 eigenvectors attains the upper bound sigma_i(A). Every subspace of that dimension intersects the span of the first i eigenvectors in a nonzero vector, whose Rayleigh quotient is at least sigma_i(A)^2, proving the lower bound. Thus no nonsingularity assumption is needed.

Subtract t times the i=1 singular value. The triangle inequality yields

|(sigma_i(A)-t sigma_1(A))-(sigma_i(B)-t sigma_1(B))| <= (1+t) delta.

Under (1), every signed quantity on the left retains its sign. Counting positive signs proves the retained-count assertion. For a threshold fixed externally at t sigma_1(A), rather than recomputed from B, the factor 1+t can be replaced by 1.

To show why a sigma_1 discrepancy does not supply delta, take A=diag(1,0) and B=diag(1,1/2). Their largest singular values are identical, but ||A-B||_2=1/2. Their counts at t=1/4 are 1 and 2. In general |sigma_1(A)-sigma_1(B)| <= ||A-B||_2 is a lower bound on a possible matrix difference, not an upper bound. An observed 1.15e-12 relative discrepancy cannot be inserted as delta without another argument. Rounded SVD outputs add their own errors and are not exact singular values of independently known matrices.

Finally take A=diag(1,0), B=diag(0,1) and r=(1,0)^T. Both singular spectra are (1,0), with the same retained count 1 and the same gap for every t in (0,1). The squared projections of r onto their retained left singular spaces are respectively 1 and 0. Thus equality of spectra and counts does not control stationarity projections, parameter absorption or reduced sensitivity. Such a comparison needs matrix and residual alignment, and quantitative subspace or direct projection controls, beyond a singular-value comparison.

## Application and scope

The saved P3 R factor, its column-normalized version T, and its phase-complement coefficient block A have separately specified matrices and cutoffs. Their cutoff margins must be reported separately. The coefficient block determines reduced-sensitivity truncation; margins of R alone do not determine it. Numerical margins are observations about these saved matrices. They do not validate a full Euler Jacobian, an exact rank, residual quadrature, or a matrix-error bound between saved QR and the unavailable tall Jacobian. The lead's 1e-11 margin rule may be used as an additional conservative reporting filter. Passing that filter is not a proof of perturbation stability without its missing hypotheses.

Dependencies: finite-dimensional spectral theorem, dimension inequality for subspaces, and triangle inequalities. No formal source or machine-checked theorem is supplied; the verification subfolder records arithmetic controls and application evidence.
