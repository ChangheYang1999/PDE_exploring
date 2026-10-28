# Congruence whitening and loss of Gram positivity under rounding

## Statement and scope

Let G_X and G_Y be real symmetric positive-definite finite matrices, and let B be real. Define the squared smallest generalized singular value by

 s_min^2 = inf_(v != 0) (v^T B^T G_Y^(-1) B v)/(v^T G_X v).

For any real square matrix Z of the size of G_Y, put

 W=Z+Z^T-Z^T G_Y Z, K=B^T W B.

If T is an invertible real matrix and T^T(K-s^2 G_X)T is positive semidefinite, then s_min>=s for s>=0. Both this matrix inequality and G_X positivity can be checked after an arbitrary invertible congruence. A Cholesky factorization of a rounded midpoint is only a way to choose the congruence; it is not a positivity certificate.

The companion computation inspects the S0 matrix export as an input artifact. It does not independently reconstruct every matrix entry from the original modal data, and consequently does not certify an S0 singular value. It tests the specific claim that increasing arithmetic precision after rounding a Gram matrix to binary64 repairs a failed factorization.

## Proof of the matrix certificate

Expand the square to obtain

 G_Y^(-1)-W=(I-G_Y Z)^T G_Y^(-1)(I-G_Y Z)>=0.

Thus K<=B^T G_Y^(-1)B. An invertible congruence preserves positive semidefiniteness, so the assumed inequality implies K>=s^2 G_X. Apply both inequalities to every v and divide by its strictly positive Gram norm.

For a real symmetric matrix M and any invertible lower triangular real matrix R, define E=R^(-1) M R^(-T)-I. If the exact infinity norm of E is less than1, then M is positive definite. Indeed E is symmetric and every eigenvalue has absolute value at most its infinity norm. Hence I+E is positive definite, and invertible congruence gives the conclusion. Interval arithmetic may enclose E entrywise; an upper bound on its row-sum norm suffices uniformly for every common underlying real matrix.

If a preconditioner T is itself represented by intervals, its use is legitimate provided one fixes a common real T in those intervals and proves it is invertible. For example, an upper triangular T with every diagonal interval excluding0 gives an invertible matrix for every selection. A successful positive-definiteness certificate for T^T G_X T also implies that this common square T has trivial kernel. No exact-dyadic description of decimal interval entries is needed, but calling them exact dyadics would be inaccurate.

## Counterexample to precision restoration after binary64 rounding

The exact matrix

 G=[[1,1],[1,1+2^(-80)]]

is positive definite: its upper-left minor is1 and its determinant is2^(-80)>0. Binary64 nearest rounding sends all four entries to1, giving a singular matrix. Converting these four rounded numbers into 60-digit or arbitrary-precision numbers leaves the singular matrix unchanged. Therefore high-precision arithmetic must receive the unrounded midpoint, for example through its exact binary mantissa and exponent.

The final interval certificate can still prevent a false positive when a poor preconditioner is used. Thus this defect normally causes failure or poor conditioning; by itself it does not invalidate a successful uniformly enclosed positive-definiteness test.

## Actual-data check and limits

The companion program independently decodes the dyadic balls of the S0 domain Gram, applies its documented angular and scalar weights, and forms the exact same tail-compensation rank-one term. It compares a binary64 Cholesky attempt with a high-precision factorization fed exact midpoint mantissas and exponents. When possible it checks the resulting congruence against the original input balls. The evidence file records actual results and hashes. This is a reproducible audit of the exported matrix, not a certificate of conformity, continuum invertibility, or original-entry correctness.

## Dependencies

Only finite-dimensional real linear algebra and the exact input decoding are used. The inverse-Gram identity is also audited in proof 17. No external numerical values are imported as proven constants.

## Recorded result

The 170 by 170 exported Gram fails binary64 Cholesky. At 100 decimal digits, Cholesky from exact midpoint mantissas succeeds. A 384-bit interval congruence encloses the infinity-norm error below 1.754e-27, and every triangular diagonal interval excludes zero. Thus every common real domain Gram enclosed by this particular reconstructed input is positive definite. The input-matrix SHA-256 is e100b08b6ef0baf4ebb585b10fe1f7e47ddfded28bc3b553464b4838c2661f6e. This assertion is conditional on the correctness of those entry enclosures; the entries were not independently recomputed from the original modal data in this test. No singular-value certificate follows.
