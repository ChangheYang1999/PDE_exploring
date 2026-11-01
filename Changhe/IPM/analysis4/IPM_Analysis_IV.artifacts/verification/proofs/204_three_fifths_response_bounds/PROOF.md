# Uniform response bounds for the four delta3/5 profiles

Status: all four certificates are CONFIRMED, V427, V436, V445 and V421 in increasing-root order.

## Statement and exact inputs

Let delta=3/5, c=5/2, and f1=sin(theta)+b sin(3theta), where b is any of the four real algebraic roots isolated in topic200. Write sigma_k for the coefficient of sin((6k+3)theta) in the response at order10(k+1) to the free stream harmonic at10k. A successful certificate here supplies an explicit rational s>0 such that |sigma_k|>s for every integer k>=1. This establishes a quantitative hypothesis for the rational convergence theorem; it does not give a sharp exterior radius.

## Compact recurrence and its justification

Refine the rational isolating interval for b by exact bisection. Construct the finite density fields F1 through F10 and streams G1 through G9 with the Cartesian interval recurrence, retaining the entire algebraic-root enclosure. The physical signed-Laurent convention is the one proved in topic01.

Put q=6k-2 and t=1/q. A high field has degree -q-alpha and signed carrier exp(iq theta) times an offset Laurent polynomial. Dividing its Cartesian derivatives by q gives the exact operators

    X_t(z^v)=t(v-alpha)z^(v-1)/2-[1+t(v+alpha)/2]z^(v+1),
    Y_t(z^v)=t(v-alpha)z^(v-1)/2+[1+t(v+alpha)/2]z^(v+1).

Here alpha=1+3s/5 for a density response at step s and alpha=3s/5 for its stream. The positive carrier of the free harmonic is1/2. The density response at step r is the ordered linearized advection divided by

    lambda_(10k+r)/q=[1+(2+3(r-1)/5)t]/(2/5).

For a density offset coefficient a_v at step s<10, the particular stream receives

    V_(v+1) += -a_v/[2(v+1-3s/5)],
    V_(v-1) += t a_v/[2(2+(v-1+3s/5)t)].

These identities follow by factoring the quadratic Poisson denominator and canceling its corresponding derivative factor, as in topic149. The first denominator never vanishes because v+1 is even and3s/5 is not an even integer for1<=s<10. Every interval evaluation rejects any unresolved second denominator. The final response is twice the coefficient of offset5 in the step10 density.

For k>=7, q>=40 and the two signed carriers remain separate throughout the ten steps: density offsets have absolute value at most39, and the intermediate stream offsets at most36. Therefore the compact response equals sigma_k on the entire required tail. The same recurrence is regular at t=0 and gives its limiting response. Full Cartesian responses at finitely many k provide a separate check against the compact formula wherever separation holds.

## Exact coverage argument

Start with the closed interval[0,1/40], corresponding to every integer k>=7 and the limiting endpoint. Bisect rationally. A leaf is accepted if directed interval evaluation gives a response whose exact dyadic midpoint m and radius r satisfy |m|-r>s. A leaf may instead be discarded if it contains no parameter1/(6k-2) with integer k>=7. For a leaf[a,b], the possible integer range is

    max(7,ceil((1/b+2)/6)) <= k <= floor((1/a+2)/6),

where a=0 removes the upper bound. Both tests use exact rational arithmetic. Every split is retained through its binary address. Exact replay reconstructs each leaf from the address, checks that consecutive leaves meet without gaps or overlap, verifies each integer exclusion and each dyadic lower bound, and confirms that the leaves cover the initial interval. The finitely many indices1 through6 are checked by the full response. This proves the stated all-index lower bound.

A finite sample is used only to choose a tentative dyadic s. The certificate must still cover the whole integer tail; a failed cover establishes no bound. Root refinement and all successful response intervals are retained with hashes, code and actual computation time.

## Scope and dependencies

Topic200 certifies the exact initial roots. Topics144 and149 prove the response and compact operators. Topic145 supplies convergence after the resulting lower bound is admitted. The present arithmetic uses no empirical growth rate or assumption about unsampled indices. The canonical logarithmic series and global stationary extension remain separate questions.

## First completed branch

V421 certifies root4 with s=2^(-22), using2202 compact-cover leaves and206.369 seconds of actual computation. The other branches are recorded below.

## Root1 certificate, 2026-10-31T15:28:28+00:00

V427 certifies s=2^(-42). The exact cover has6341 leaves:2645 accepted intervals and3696 intervals with no admissible integer. The finite checks cover indices1 through16. The total actual runtime was565.076 seconds.

## Root2 certificate, 2026-10-31T15:54:57+00:00

V436 certifies s=2^(-42). The exact cover has17866 leaves:7481 accepted intervals and10385 integer-empty intervals. The actual runtime was1612.769 seconds.

## Root3 certificate, 2026-10-31T15:57:12+00:00

V445 certifies s=2^(-31). The exact cover has2229 leaves:935 accepted intervals and1294 integer-empty intervals. The actual runtime was204.615249 seconds.
