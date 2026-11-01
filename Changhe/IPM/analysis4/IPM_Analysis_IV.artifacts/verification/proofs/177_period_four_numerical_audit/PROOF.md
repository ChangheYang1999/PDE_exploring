# Independent finite audit of the six period-four numerical runs

Status: finite audit CONFIRMED in V337. The exact existence and response results142/143 already prove convergence. This audit checks finite computed coefficients and reported numerical values; it supplies no empirical infinite-order growth constant.

## Exact problem

Let Q=4, delta=1/2, c=2, and f1=sin(theta)+b sin(3theta), where b is one of the six real roots of the degree-eight first-obstruction polynomial isolated in142. At n=4k, k>=2, add the stream harmonic H_n sin((2k-2)theta) chosen to cancel the density obstruction at n+4. Theorems131/132 and the uniform response certificates143 prove that this defines a unique convergent exterior series.

The independent computation uses the signed Cartesian algebra and the two-continuation tuning argument in167: the obstruction after four more orders is affine in H_n. The two values at H_n=0,1 determine its response exactly; directed interval subtraction and division enclose the tuned H_n. The root interval is propagated throughout without resetting midpoints. Carrier and S1 projections remove only coefficients known to vanish. Compatibility projections are justified first by the exact algebraic root and subsequently by the preceding tuning identity. Every computed Poisson inverse is checked by Cartesian second derivatives. Thus successful interval output encloses the exact prefix.

The audit compares all density and stream coefficients through order40 with the independently generated numerical checkpoint, as well as every tuned harmonic and response through that order. It also recomputes the reported density root-test values at the requested later orders directly from the stored coefficient balls. These latter checks verify interval arithmetic, source binding and table extraction, but do not independently recompute every high-order nonlinear convolution.

## Open final harmonic

The numerical solver may finish when its last density coefficient is computed but before its last resonant stream harmonic is tuned. At a final order N divisible by4, f_N is already determined by H_(N-4), whereas g_N still depends on the yet unknown H_N. Its placeholder H_N=0 must not be called the stream coefficient of the uniquely tuned infinite series. Therefore later-order density norms are admissible, but a stream norm is reported only when its harmonic is present, or when the order is nonresonant. The audit records that distinction explicitly.

## Finite numerical claims

For a real sine polynomial f=sum a_j sin((2j+1)theta), the coefficient l1 norm is sum|a_j|. Ball absolute values and summation enclose this norm. For a strictly positive norm interval, exp(log(norm)/n) encloses its n-th root. A printed finite-order root-test quantity is certified only to the number of decimals resolved by that interval. Fits or proposed limiting radii remain numerical evidence, regardless of prefix length.

Root polynomials, checkpoint hashes, selected coefficient archives, interval norm values, comparison counts and exact execution times are retained. The full external checkpoint remains read-only.

## Completed audit at 2026-10-31T13:12:37+00:00

All six independent prefixes through40 pass. Per root, the calculation checks21808 Poisson coefficients,2616 ordered products,18 provisional continuations and9 compatibility projections. Every one of1640 density and1680 stream coefficients overlaps the separate numerical implementation. All9 harmonic values and responses overlap as well. The full audit took117.78849194385111 seconds.

The density root tests at300, in increasing root order, are approximately1.3285641655,0.2879397361,0.2225314337,0.3709342004,0.8837394666,2.0817673991. Their source norm relative radii are below6.1e-98 in every case. These are finite interval extractions; only orders through40 have their nonlinear recursion independently recomputed here. The final source stream coefficient at300 remains untuned and is excluded.
