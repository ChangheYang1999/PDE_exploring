# Gram identity for a column-scaled QR record

Statement. Let m >= n, J be a real m by n matrix, P an n by n permutation matrix, and D a diagonal n by n matrix with strictly positive entries. Suppose J P D^{-1} = Q R, where Q is m by n, Q^T Q = I_n, and R is n by n upper triangular. Rank deficiency of J is allowed. Then

    R^T R = D^{-1} P^T J^T J P D^{-1},
    P^T J^T J P = D R^T R D.

In particular, an unscaled Gram matrix (J P)^T (J P) cannot in general be compared directly with R^T R. Either scale the columns of J P by the saved diagonal D before forming its Gram matrix, or multiply R^T R by D on both sides. The saved D must be used when testing the saved record's identity; recomputing a new D may conceal a scale mismatch.

Proof. Transpose J P D^{-1} = Q R and multiply it by the original equality. As D is real diagonal it equals its transpose, and Q^T Q = I_n gives (J P D^{-1})^T (J P D^{-1}) = R^T Q^T Q R = R^T R. The left side is D^{-1} P^T J^T J P D^{-1}. Multiplication by D on both sides gives the second identity. No inverse of J or R was used, so rank deficiency is allowed.

Singular-value consequence. Under exactly the preceding hypotheses, the n singular values of J P D^{-1}, with multiplicity and including zeros, equal those of R. Indeed their squares are the eigenvalues of their Gram matrices, and the proved identity makes these matrices equal. A column permutation does not change singular values; the scaling diagonal must still correspond to the permuted columns. This consequence does not remove a phase direction or compute the coefficient-space projection required for reduced parameter sensitivity.

Scope. These are exact real arithmetic identities, not a bound on floating point QR errors. An equality of Gram matrices alone does not establish equality of Jacobian matrices, because left multiplication by an orthogonal matrix preserves a Gram matrix. Endpoint coordinates, residual values, code identity and other saved witnesses must therefore be bound separately. The verification folder contains the numerical source audit; formalization was not performed.
