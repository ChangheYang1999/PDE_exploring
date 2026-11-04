# An elementary affine reparametrization tree for smooth curves

## Exact statement

Fix an integer r>=2. Let g:R^m->R^m be a C^r diffeomorphism with bounded derivatives of orders 1 through r and bounded derivative of its inverse. Put L_+=sup||Dg||, L_-=sup||Dg^(-1)|| and M=max(2,L_+,L_-). Choose 0<epsilon<=1 with epsilon^(j-1) sup||D^j g||<=L_+ for 2<=j<=r. Set eta=1/100 and D=50/49.

For a regular embedded curve gamma:[-1,1]->R^m put s=sup|gamma'|. Call it bounded if sup|gamma^(j)|<=eta s for 2<=j<=r, and small if additionally s<=epsilon. There is a constant C_r depending only on r with the following property. Every small bounded gamma has a finite affine interval partition whose normalized image curves g gamma theta_i are small and bounded, and every affine slope is at most 1/100. Tag an image large exactly when its maximum speed is at least epsilon/3.

Each large image has length between epsilon/2 and 2epsilon. There are at most C_r M^(3/(r-1)) small images. For each integer l, at most 16 exp(l) large intervals contain a point where floor(log J_g)=l, with J_g the arclength Jacobian on gamma. The distortion of J_g on each input interval is at most D^2<2.

Iteration gives finite nested original interval partitions. On each depth-n atom, every time-k parameterization, 0<=k<=n, is small and bounded, and has diameter at most 2epsilon 100^(-(n-k)). Every restricted iterate has arclength distortion at most D^2. One-step logarithmic Jacobians oscillate by less than one on every final atom. Curves whose images stay in a common compact set have subsequences converging in C^(r-1), with a Lipschitz derivative of order r-1 in the limit. Large curves cannot converge to a constant. No convergence in the top Lipschitz norm is asserted.

This is a finite geometric theorem. It contains no invariant-measure, basin-coverage or Euler conclusion.

## Proof

A bounded curve has (1-2eta)s<=|gamma'(t)|<=s: integrate gamma'' from a maximum-speed point over a distance at most two. Its speed distortion is at most D. Under an affine restriction of slope b<=1-2eta, the jth-to-first derivative ratio is at most eta b^(j-1)/(1-2eta)<=eta for j>=2. Therefore restrictions of slope at most 1/100 preserve boundedness and smallness. If alpha and beta=g^n alpha are both bounded parameterizations, the ratio |beta'|/|alpha'| has distortion at most D^2. This compares the two endpoint curves directly; no distortion factors are multiplied over time.

Write F=g gamma. The chain rule and the choice of epsilon give

    sup|F^(r)|<=A_r L_+ s,
    min|F'|>=(1-2eta)s/L_-,
    max|F'|<=L_+s,

where A_r depends only on r. In each chain-rule term involving j derivatives on g, the remaining product is at most a constant times s^j. For j>=2 use s<=epsilon; for j=1 use the curve bounds. Consequently sup|F^(r)|/min|F'|<=D A_r M^2 and max|F'|/min|F'|<=D M^2.

Choose a small delta_r<=1/100. Divide the parameter interval into N equal pieces with N=ceil((D A_r M^2/delta_r)^(1/(r-1))). In a normalized piece F_j, put m_j=min|F_j'|. Then sup|F_j^(r)|<=delta_r m_j. The Taylor polynomial P_j of F_j' at zero, of degree r-2, satisfies sup|F_j'-P_j|<=delta_r m_j/(r-1)!. This is a vector Taylor polynomial.

Partition each piece at the real roots of |P_j|^2-(2^k m_j)^2 for the dyadic thresholds between m_j/2 and 4M^2m_j. There are O_r(1+log M) intervals because each nonzero polynomial has degree at most 2(r-2). Identically zero polynomials contribute no cuts. The norm of P_j is bounded below by 0.99m_j and above by (D M^2+0.01)m_j, so these thresholds bracket its entire range. On every resulting closed interval it lies in one dyadic band. Adding the Taylor error shows that the ratio of maximum to minimum of |F_j'| on that interval is less than four. For r=2, P_j is constant and no root cuts are required.

Normalize a resulting interval to obtain G. Affine rescaling preserves

    sup|G^(r)|<=delta_r min|G'|,
    max|G'|<=4 min|G'|.

The elementary interpolation bound

    max_(2<=j<=r) sup|G^(j)|<=B_r(sup|G'|+sup|G^(r)|)

holds for vector-valued curves with a dimension-independent B_r. To see this, apply Taylor's theorem to G' at any x, at r-1 equally spaced points in [x,x+1] or [x-1,x], choosing the interval inside [-1,1]. Invert the fixed Vandermonde matrix to bound derivatives through order r-2 of G' by its supremum and the Taylor remainder. Matrix coefficients are scalars, so the vector estimate follows from the triangle inequality. The last derivative is already on the right. The r=2 case is immediate.

Thus all derivatives of G of orders 2 through r are at most 5B_r min|G'|. Divide G into K_r equal pieces with K_r>=100 and 5B_r/K_r<=eta. The normalized pieces are bounded. Their total number is at most

    C'_r M^(2/(r-1))(1+log M)<=C_r M^(3/(r-1)).

Their original affine slopes are at most 1/100. This bound counts the intermediate bounded pieces, before speed normalization.

Let v be the maximum speed of one such piece. If v<=epsilon, retain it. If v>epsilon, divide it into ceil(v/epsilon) equal pieces. Their maximum speeds are at most epsilon and at least (1-2eta)epsilon/2>epsilon/3. They are bounded by the affine restriction estimate. Hence every further piece is large, while each uncut intermediate piece contributes at most one small output. This proves the small-child count. A large bounded image has minimum speed at least (1-2eta)epsilon/3, so its length exceeds epsilon/2 and is at most 2epsilon.

Both endpoint parameterizations of each branch are bounded, so J_g has distortion at most D^2. If a large branch meets the bin l, its Jacobian is at most D^2 exp(l+1) everywhere. Input arclengths of such branches sum to at most 2epsilon, because their interiors are disjoint. Their output lengths sum to at most 2epsilon D^2 exp(l+1). Dividing by epsilon/2 gives at most 4D^2 e exp(l)<16exp(l) branches. Endpoint overlaps have zero arclength and do not affect the estimate.

For iteration, compose the affine restrictions. On a depth-n atom, its time-k curve is a restriction of the depth-k bounded curve with an additional slope at most 100^(-(n-k)). This proves every diameter and speed estimate. The two-endpoint argument gives the distortion for any restricted time interval, including the full iterate. Its logarithm is at most log D^2<1, yielding the integer-bin oscillation assertion.

Finally, compact image control and uniform derivatives through order r give C^(r-1) subsequential compactness by Arzela-Ascoli. The last retained derivative is Lipschitz by the uniform next-derivative bound. Length is continuous in C1; the uniform lower length bound for large curves excludes a constant limit.

## Audit and dependencies

This independently reconstructs LIT65. Every derivative is a genuine vector derivative, and the polynomial root count is dimension-independent. Neither the 2026 measured-disk norm convention nor its endpoint compactness assertion is used. The inputs are the chain rule, Taylor's theorem, finite polynomial root counting, a proved interpolation estimate and Arzela-Ascoli. No computation or formalization was needed. The immutable submission and its hash are retained in the team records.
