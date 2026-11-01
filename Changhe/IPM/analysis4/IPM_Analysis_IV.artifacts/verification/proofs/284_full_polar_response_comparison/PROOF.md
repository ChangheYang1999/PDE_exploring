# Full comparison of the Cartesian and polar response functions

Status: proof and comparison protocol written before computation. The factor and limit checks in277 are already admitted; equality of the full outputs of the two implementations is a separate check here.

## Statement and hypotheses

For Q=9 or Q=10 set delta=2/Q, c=Q/(Q-2), and f_1=sin(theta)+b sin(3theta). Use the independently verified zero-harmonic coefficients f_1,...,f_Q and g_1,...,g_(Q-1) from267 or281. Let S_C(k,b) be the exact signed-Cartesian response reconstructed in277 or282. Let S_P(k,b) be the output of the theory part's frozen positive-frequency polar response implementation. Both responses measure the coefficient of sin((2k-1)theta) in the change of f_(Qk+Q) caused by adding sin((2k-2)theta) to g_(Qk).

If the exact comparisons below pass, S_C=S_P as rational functions of k and polynomials of b for all k at which the formulas are defined. This supplies a full implementation comparison, beyond equality of denominator factors, coefficient gcds and limiting polynomials. It adds no new convergence radius or asymptotic assertion.

## Polar derivation

For a stream term r^P sin(l theta) and a density term r^p sin(m theta), their Jacobian is r^(P+p-2) times

    [(P m-p l)/2] sin((l+m)theta)
      -[(P m+p l)/2] sin((m-l)theta).

This follows by differentiating in polar coordinates and applying the two sine-cosine product identities. Negative sine frequencies change sign; frequency zero vanishes. Thus the positive-frequency polar advection is independently determined without Cartesian differentiation.

A density coefficient a at frequency m induces stream contributions

    -a/[2(m+1+P_n)] at frequency m+1,
     a/[2(m-1-P_n)] at frequency m-1,

where P_n=2-2n/Q. The second term is omitted when m=1. These are the factored expressions obtained by applying partial_x and dividing by the corresponding nonzero multiplier of -Delta. At a genuine zero multiplier compatibility must be supplied separately; the generic response's intermediate orders Qk+r, 1<=r<Q, have no stream resonance. The verified low prefix handles its own zero-frequency omission.

The polar response starts with the unit stream harmonic at order Qk, propagates the linearized recurrence through Q subsequent orders, and reads the specified final coefficient. At each step the b degree is at most that step's order, because products with a low coefficient have additive degrees. The same bound holds for the Cartesian construction. Therefore both final responses lie in Q(k)[b] with b degree at mostQ.

## Exact comparison

Freeze the theory part's actual source and record its hash. Execute its advection, inverse and response functions using the already audited rational-function arithmetic of173. This shares the rational arithmetic engine but retains the two distinct derivative implementations. Use the independently verified low-prefix polynomial data. At Q+1 distinct rational b values, evaluate every low coefficient exactly, execute the complete polar response over Q(k), and compare with S_C at the same value by exact cross multiplication of rational functions. Also recompute the polar low prefix at those values and compare every coefficient used by the response.

If every comparison is zero, S_C-S_P is a polynomial of degree at mostQ over the field Q(k) with Q+1 distinct roots. It is identically zero. No sampling in k or floating arithmetic enters this identity proof. The generic positive-frequency representation is valid for integer k>=2Q+1; its equality as a rational function supplies the asserted generic comparison. The separately recorded small-carrier checks and nonvanishing arguments retain their own scope.

## Dependencies and limits

Dependencies are01,119,173,267/281 and277/282. The output records the full source hash, exact input hashes, all specialization identities, low-prefix comparisons and actual runtime. A failed equality is retained as a failed check; it must not be replaced by an approximate match. Shared rational arithmetic is explicitly disclosed. This comparison does not independently recertify that arithmetic library.

Completed 2026-10-31T20:56:55+00:00, V578. For Q9, full rational responses agree identically in k at all10 distinct interpolation values of b. Degree at most9 establishes the full polynomial identity in b. The theory part's polar low-order recurrence also matches1539 Cartesian prefix coefficients. Actual runtime36.888051seconds. The full derivative implementations agree. They share the audited Q(k) arithmetic engine, so this is not an independent arithmetic-library check. This closes the full-numerator comparison left OPEN inV573.

Completed 2026-10-31T21:16:02+00:00, V588. For Q10, full rational responses agree identically in k at all11 distinct interpolation values of b. Degree at most10 establishes the full polynomial identity in b. The theory part's polar low-order recurrence also matches2100 Cartesian prefix coefficients. Actual runtime45.680248seconds. The full derivative implementations agree. They share the audited Q(k) arithmetic engine, so this is not an independent arithmetic-library check.
