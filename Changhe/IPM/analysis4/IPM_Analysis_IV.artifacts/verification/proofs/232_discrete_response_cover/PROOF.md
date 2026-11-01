# A discrete response certificate with singleton leaves

Status: PROVED certificate theorem, independently reviewed by the theory part at 17:14Z and admitted in V478. The synthetic certificate and rejection checks passed. This theorem does not assert that any particular numerical search terminates.

## Statement

Let h and K be positive integers with 2hK>2, put T=1/(2hK-2), and let sigma_k be a scalar sequence for k>=K. Suppose a function S is defined at t_k=1/(2hk-2) and satisfies S(t_k)=sigma_k. Let s>0 be rational.

Take a finite partition of [0,T] into closed intervals I_j=[a_j,b_j] with disjoint interiors, rational endpoints and positive lengths. Define

    L_j=max(K,ceil((1/b_j+2)/(2h))),
    U_j=floor((1/a_j+2)/(2h)) if a_j>0,
    U_j=+infinity if a_j=0.

For each interval require one of these certificates:

1. Empty: U_j<L_j.
2. Singleton: U_j=L_j=k and a validated point enclosure proves |S(t_k)|>s.
3. Interval: a validated enclosure of S on I_j proves |S(t)|>s throughout I_j.

Then |sigma_k|>s for every integer k>=K. If a separate validated calculation proves the same inequality for 1<=k<K, it holds for every positive integer.

The interval alternative requires S on that entire interval; the empty and singleton alternatives require no evaluation at other real points. Thus a zero of S between adjacent integer samples is compatible with this certificate.

## Proof

For k>=K the denominator 2hk-2 is positive, t_k belongs to (0,T], and k maps strictly decreasingly to t_k. Solving a_j<=t_k<=b_j gives exactly L_j<=k<=U_j, with the upper inequality absent when a_j=0. This uses only reciprocal monotonicity for positive numbers and the definitions of ceiling and floor.

Choose a partition interval containing t_k. It cannot be empty because k lies between its integer bounds. If it is a singleton, its unique allowed integer is k, and the point enclosure proves the conclusion. Otherwise the validated interval enclosure includes S(t_k), so it proves the same conclusion. Repeated partition endpoints cause no problem: either adjacent interval suffices. The finite prefix is then included by its separate checks.

## Exact audit requirements

A binary subdivision representation starts from [0,T]. An address of length d with binary integer value v represents [Tv/2^d,T(v+1)/2^d]. An auditor reconstructs these rational endpoints, sorts the intervals, verifies the first endpoint is zero, the last is T, and every right endpoint equals the next left endpoint. It then recomputes each integer range using exact fractions. A missing interval, incorrect integer exclusion or unverified nonempty leaf invalidates the certificate.

Point and interval enclosures must use exact input data or validated input enclosures. A displayed decimal and a ball containing zero do not certify nonvanishing. For a real dyadic ball with midpoint m and radius r, |m|-r>s is a sufficient exact check. A fresh higher-precision calculation may verify the same leaf and overlap the stored enclosure, but overlap alone is insufficient: the fresh ball must separately prove the bound.

The search may decrease its proposed positive s. Earlier accepted leaves remain valid because their established lower bounds exceed the older, larger target. The final audit uses only the final common target. No finite-precision termination or optimal lower-bound claim is part of this theorem.

## Use for rational far fields

The compact carrier identity of144 and149 supplies S at t_k once 2hk-2>=BQ. The above certificate can replace the integer-exclusion cover in149,223,226 and227. It changes only how the countable response condition is verified; the recurrence, carrier threshold, rational majorant and derivative conclusions are unchanged.

Dependencies: exact reciprocal inequalities; validated interval arithmetic; compact carrier identity144/149 when applied to the IPM recurrence. The proof applies independently of the parameter or the sign of the responses.

## Synthetic certificate checks

The queued implementation check uses S(t)=t-1/8 with h=2,K=1. Its unique zero is not an integer sample; the exact discrete infimum is1/40, attained at k=3. The check independently replays the rational partition and all leaf ranges, both for a valid initial target and for an oversized target that must be decreased. A second example S(t)=t-1/6 has sigma_2=0 and must be rejected. These tests check the acceptance rule and refusal of an actual zero. They do not replace the proof or any IPM response certificate.

The implementation first uses an available separated enclosure of S(0) to lower its proposed target below half that limiting lower bound. This is only target selection. The complete partition still supplies the proof. Without this step an oversized target can make the leftmost branch subdivide forever before the search reaches any singleton; the retained initial search failure records that behavior.
