# Leading pole hierarchy at every resonance near delta=2/Q

Status: PROVED inV454 after independent theory-part review. The unit-sine all-index response certificate is CONFIRMED inV450. The factorial-root limit explicitly assumes R is nonzero.

## Statement

Let Q>=3 be an integer, delta=2/Q+epsilon, and c=1/(1-delta). Fix a finite real odd sine polynomial f_1 independent of epsilon. At nonresonant parameter values, use the pure-power recursion with the unique even-frequency sine stream inverse. For each fixed order, its angular coefficients are rational functions of epsilon and therefore meromorphic at zero. Let U(n)=max(0,floor(n/Q)-1) and V(n)=max(0,floor((n-1)/Q)-1).

Every coefficient of g_n has pole order at most U(n), and every coefficient of f_n has pole order at most V(n). Let R be the coefficient of sin(theta) in the analytic f_(2Q) at epsilon=0. For k>=2, let sigma_k be the coefficient of sin((2k-1)theta) in the order-(k+1)Q density response to a unit free stream harmonic sin((2k-2)theta) at order kQ. This response is evaluated at delta=2/Q and uses only the analytic low fields f_1,...,f_Q and g_1,...,g_(Q-1).

The coefficient of epsilon^(-(k-1)) in g_(kQ) is v_k sin((2k-2)theta), where

    v_2=R/(4Q),
    v_(k+1)=sigma_k v_k/[2(k+1)Q],
    v_k=R product_(j=2)^(k-1) sigma_j / [(2Q)^(k-1) k!].

The empty product is one. In particular, if R and all sigma_j are nonzero, g_(kQ) has pole order exactly k-1 for every k>=2. No conclusion about convergence at a fixed nonzero epsilon follows from this statement alone.

## Recursion and low-order analyticity

Write P_n=2-n delta. The density divisor is (n-1)(c-1)=(n-1)delta/(1-delta), nonzero and analytic near epsilon=0. The nonlinear numerator consists of the ordered products

    -p_j g_i' f_j + P_i g_i f_j',  i+j=n.

The stream inverse has denominator 2((2j)^2-P_n^2). At epsilon=0 its only possible singularities for positive orders and even sine modes are n=kQ, k>=2, in the single mode2k-2. At n=Q, P_n=0, but there is no zero-frequency odd sine mode. Each potentially singular inverse has a simple pole. Finite Fourier support at every order follows by induction under differentiation and multiplication. Thus all density coefficients through2Q and stream coefficients below2Q are analytic.

## Pole-order induction

Suppose lower orders satisfy the bounds. A nonlinear term has pole order at most U(i)+V(j). If both bounds are positive, then

    U(i)+V(j)
    =floor(i/Q)+floor((j-1)/Q)-2
    <=floor((n-1)/Q)-2
    =V(n)-1.

If only U(i) is positive, i<=n-1 implies U(i)<=V(n). If only V(j) is positive, j<=n-1 gives the same conclusion. If neither is positive, the product is analytic. The density divisor does not increase pole order, so f_n has order at most V(n). A nonresonant stream inverse preserves this bound. At n=kQ the possible extra simple pole gives V(kQ)+1=k-1=U(kQ). At every other order U(n)=V(n). This proves the induction.

The strict inequality for products of two singular factors holds at every order. Such products first occur at4Q+1, but thereafter they still remain below the maximal possible pole order.

## Leading coefficient at a resonant stream inverse

At n=kQ set j=k-1. Then P_n=-2j-n epsilon and

    2((2j)^2-P_n^2)=-8jn epsilon-2n^2 epsilon^2.

If the coefficient of sin((2j-1)theta) in f_n has leading term A epsilon^(-d), the resonant stream coefficient has leading term A epsilon^(-d-1)/(2n). The other neighbouring density coefficient is multiplied by P_n+2j=-n epsilon and cannot contribute at this order. All nonresonant stream coordinates have order at most k-2. At k=2, this gives v_2=R/(4Q).

## Propagation of the top pole to the next resonance

Fix k>=2 and consider n=kQ+r, 1<=r<=Q. The maximal density pole order is k-1. A product with both singular factors has order at most k-2 by the proved strict bound. A term of order k-1 must therefore contain one high factor and one analytic factor. A stream factor can carry order k-1 only from index kQ onward, and a density factor only from kQ+1 onward. Consequently the analytic companion has index at most r<=Q. No coefficient above these low orders enters the top-pole propagation.

Taking the coefficient of epsilon^(-(k-1)) in the recurrence therefore gives exactly its linear response recurrence at delta=2/Q, starting with stream input v_k sin((2k-2)theta) and zero density response at order kQ. Between kQ and(k+1)Q there is no further resonant inverse. At the final density order the resonant obstruction coefficient is v_k sigma_k. The previous inverse calculation yields v_(k+1)=v_k sigma_k/[2(k+1)Q]. Induction gives the product formula. The reasoning also applies if some v_k vanishes: the stated highest Laurent coefficient is then zero, with no assertion about lower coefficients.

## Unit sine at Q=5: certificate to be checked

Topic216 proves R!=0 and sigma_2,sigma_3!=0 for f_1=sin(theta). A fresh exact signed-Laurent Cartesian calculation here will generate the low fields and five-step response as a rational function of k. It will compare that function with the independently stored formula in130, verify the finite small indices separately, and certify a fixed sign of numerator and denominator on the remaining tail by an exact shifted-polynomial coefficient test. Only after those checks and independent review may the all-resonance nonvanishing conclusion be admitted for this example.

## Dependencies and scope

The original potential-derived recursion and stream inverse are proved in topics01 and02. Topic216 records the local pole calculation and the first three resonances. The present proof extends the pole-order argument itself to arbitrary finite order and arbitrary finite leading support. It is an assertion about meromorphic parameter dependence, not a divergent-series theorem, a common neighbourhood valid for every order, or a result about a tuned compatible leading profile.

## Size of the leading Laurent coefficients

Suppose additionally that R is nonzero, no sigma_k vanishes and sigma_k tends to a finite nonzero number sigma_infinity. Taking logarithms of the product formula and applying the arithmetic-mean limit to log|sigma_k| gives

    lim_(k to infinity) (k! |v_k|)^(1/k)=|sigma_infinity|/(2Q).

Indeed, the fixed factorR, the missing initial factor in(2Q)^(k-1), and finitely many initial response factors disappear after taking the kth root. Stirling's formula then gives

    lim_(k to infinity) k |v_k|^(1/k)=e |sigma_infinity|/(2Q).

Thus the scalar series sum_(k>=2) v_k t^k is entire in t. This series records only the highest Laurent coefficient at each resonant order; it is not the stationary far-field series at a fixed epsilon. Neither convergence nor divergence of the full far-field series follows. For the Q=5 unit sine example, the candidate exact limit is

    sigma_infinity=-22057171011707398/16814963483136000000.

The independent rational-function calculation must confirm this value before this numerical specialization is admitted.

## Completed arithmetic certificate

At 2026-10-31T16:17:00+00:00, the independent exact Cartesian rational function agrees with the formula in130. The small-index responses2 through12 are nonzero. The generic degree17 numerator has strictly negative coefficients after the shift k=11+t, while its degree17 denominator has strictly positive coefficients. Hence every response with k>=11 is negative and nonzero. The finite responses at2 and3 are positive; their exceptional mode overlaps are checked separately.

The exact limit is sigma_infinity=-3575370901/2725632000000, equal to the unsimplified expression above. Thus the factorial-root constant in the proposed hierarchy is3575370901/27256320000000. This certificate proves nonvanishing at every index, not just at sampled orders.
