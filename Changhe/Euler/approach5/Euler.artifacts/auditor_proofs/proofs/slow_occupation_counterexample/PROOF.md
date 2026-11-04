# No polynomial occupation rate follows from abstract conservativity

## 1. Statement and scope

There is an invertible conservative ergodic measure-preserving map T on a sigma-finite infinite measure space (X,mu), and a measurable set C of measure1, such that almost every orbit visits C infinitely often in both directions but

    liminf_(n->infinity) n^-epsilon sum_(j=0)^(n-1)1_C(T^j x)=0

for every epsilon>0, simultaneously almost everywhere. A complete measurable conservative ergodic flow has the corresponding continuous-time property. No smooth Euclidean realization, polynomial spatial-growth bound, Euler bracket, actual curl or pressure property is asserted.

## 2. Exact probability construction

For k>=1 take p_k=log2[1/log(k+1)-1/log(k+2)]. The positive series telescopes to1. On the two-sided product Y=N^Z with coordinate law p, let sigma be the left shift and r(y)=y_0. Then

    P(r>=m)=log2/log(m+1), E r=infinity.

The tail sum diverges, for example by comparison with the harmonic series. Distant finite-coordinate cylinder events are independent. Approximation of measurable events by cylinder events proves mixing of sigma, hence its ergodicity and invertibility.

Let X consist of pairs (y,j) with integer 0<=j<r(y), with P times counting measure. Define T to increase j by1 until the top, then send the point to (sigma y,0). The inverse decreases positive heights and at height0 uses the top of the preceding roof. Direct summation over levels and a change of base variable prove preservation. The base C=Y times{0} has measure1, the total space has infinite measure, and restriction to r<=M gives a finite-measure exhaustion.

Every point has a finite future and past visit to C. A T-invariant indicator is constant along its roof and restricts to a sigma-invariant indicator, proving ergodicity. If a wandering set had positive measure, one fixed height slice would have positive measure. Its inverse image in C would still be T-wandering. Probability-space recurrence of the induced map sigma gives a return to this base subset at some finite T-time, a contradiction. The same argument applies to T^-1. Thus T is conservative in both directions.

## 3. Arbitrarily large excursions

Fix epsilon>0. The events

    r(sigma^n y)>=ceil(n^(2/epsilon)), n>=2,

are independent, with probabilities asymptotic to epsilon log2/(2log n). Their sum diverges. The product estimate for probabilities of no event in an interval proves the independent Borel-Cantelli conclusion, so infinitely many occur almost surely.

Put L_n=sum_(j=0)^(n-1)r(sigma^j y) and t_n=L_n+floor(r(sigma^n y)/2). For large selected n, at most n+1 base visits have occurred before t_n, while t_n>=n^(2/epsilon)/3. Hence

    N_(t_n)/(t_n)^epsilon<=3^epsilon(n+1)/n2 ->0.

Intersect the full-probability sets for positive rational epsilon. For any positive real epsilon choose a smaller positive rational q and use its subsequence. The property is unchanged by a fixed finite shift of starting time, since the counts differ by at most twice that shift. The countable tower saturation of the exceptional base set is null. This proves the exact almost-everywhere assertion on X.

## 4. Measurable flow

Suspend T with constant roof1, on X times[0,1), with product measure and the endpoint identification (x,1)=(Tx,0). Translation in the interval coordinate, applying integer T-iterates at crossings, defines a complete invertible measurable measure-preserving flow Gamma. Its invariant sets reduce to T-invariant sets, so the full flow is ergodic. The time-one map is T times the identity of the phase interval, and is conservative by Fubini and conservativity of T. Consequently the flow is conservative. No assertion that its time-one map is ergodic is needed.

Take C_flow=C times[0,1). At integer S the occupation integral differs from N_S(x) by at most2 because only the two endpoint pieces of unit intervals differ. The discrete subsequences prove the continuous-time lower-limit claim. This is a measurable suspension, not a vector field on R3.

## 5. Application to the proposed heuristic

Let a=1-2c and kappa=1+c. If separate Euler-specific estimates on the SAME almost-everywhere orbit gave numerator O(S^(1-2a/kappa)) and denominator at least b_x S^(a/kappa), b_x>0, their ratio would be O(S^(1-3a/kappa)). This tends to zero exactly when 3a>kappa, or c<2/7. The algebra is correct and conditional.

The tower proves that the denominator bound does not follow from conservativity and ergodicity alone. It does not refute such a bound under additional Euler geometry. An SRB-averaged numerator is also not automatically an ambient almost-everywhere numerator. Every integrability, common-measure and rate premise of a Hopf application must be supplied separately. No original-source Hopf theorem is an input to the construction just verified.

## 6. Evidence

The complete LIT70 submission is retained and hashed in the team records. The proof above was checked directly, including tower conservativity, simultaneous exponents, passage to almost every tower point and the flow suspension. No numerical computation, external model invocation or server is involved.
