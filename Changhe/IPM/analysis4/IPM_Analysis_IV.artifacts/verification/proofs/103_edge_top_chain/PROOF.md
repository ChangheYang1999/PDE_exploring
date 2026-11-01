# Highest logarithmic columns of the edge-1 recurrence

Status: PROVED highest-column theorem, independently reviewed in V312. This is not a theorem about the complete edge-1 series or the full stationary IPM series.

## Statement and hypotheses

Use the modified recurrence of topic102 with delta=2/3, c=3, F_1=sin(theta), and only the ordered pairs (1,n-1) and (n-1,1), counted once when they coincide. Use the polynomial Poisson inverse with zero resonant stream constants. Write t=log(r), p_n=1-2n/3 and P_n=2-2n/3. Let F_n and G_n be the density and stream angular-log coefficients. Their degree bounds are

    d_n=max(0,floor((n-1)/3)-1),
    e_n=max(0,floor(n/3)-1).

For k>=2, the coefficient of t^(k-1) in G_(3k) has the form

    b_k sin((2k-2)theta).

For this modified recurrence,

    b_2=-9589/73728000000,
    b_3=-37847783/8138627481600000000.

For k>=3, b_(k+1)=R(k)b_k, where

    R(k)=(k-1)(2k-1)P(k) /
      [14400 k^2 (3k-4)(3k-2)(3k+1)(3k+2)(6k-5)(6k-1)],

    P(k)=6480k^5-3132k^4-23454k^3+29472k^2-10791k+880.

Every b_k is negative. Moreover

    lim_k ((k-1)! |b_k|)^(1/k)=1/3240.

The same factorially weighted rate, after taking the full order's nth root, is (1/3240)^(1/3) for each of the three highest-degree density subsequences and each of the three highest-degree stream subsequences. The subseries formed from these highest-degree columns converge absolutely for every finite pair of independent complex variables z,t. No claim about the lower log columns follows.

In particular F_250 has a nonzero t^82 sin(165theta) coefficient. Its exact rational value is in verification/checks.json. Its decimal logarithm is approximately -415.542567453. Exact integer comparison proves that its absolute value is below 2^(-1075), half the least positive binary64 subnormal. Thus a correctly rounded binary64 representation of this particular exact coefficient is zero.

## Derivation of the cycle

The general log-degree induction from topic17 still gives the displayed upper bounds after removing convolution pairs. At order 3k the density degree is at most k-2. The Poisson inverse adds one degree only in the resonant mode 2k-2. This proves the asserted shape of the top stream column.

Put m=2k-2. Normalize that column by b_k and write h_0=sin(m theta). For r=1,2,3, let a_r and h_r be the normalized degree-(k-1) coefficients of F_(3k+r) and G_(3k+r), respectively. We only need h_1,h_2. Set a_0=0. The low profiles used here are f_1=sin(theta), g_1=-3sin(2theta)/20. For n=3k+r the exact top-degree density recurrence is

    2(n-1)a_r = P_(n-1) h_(r-1) f_1'
                 -p_1 h_(r-1)' f_1
                 +P_1 g_1 a_(r-1)'
                 -p_(n-1) g_1' a_(r-1).

The last two terms vanish for r=1. The first two come from the ordered pair (n-1,1); the last two come from (1,n-1). At these orders they are distinct pairs. Every derivative in t lowers degree, so such derivatives cannot contribute here. The highest density inverse divides by 2(n-1). This proves the recurrence without an assumption about the lower columns.

For r=1,2, apply the nonresonant inverse to a_r term by term. A sine term A sin(Ktheta) contributes to h_r

    -A sin((K+1)theta)/(2(K+1+P_(3k+r)))
    +A sin((K-1)theta)/(2(K-1-P_(3k+r))).

Frequencies are signed in this calculation. Fold them using sin(-Ktheta)=-sin(Ktheta), and omit zero frequency. The supports of a_1,a_2,a_3 lie at m plus offsets {+-1}, {+-1,+-3}, and {+-1,+-3,+-5}. At the next resonant order the density coefficient of sin((2k-1)theta) produces

    b_(k+1)/b_k = -[sin((2k-1)theta)]a_3/(2k).

Indeed the resonant Poisson operator is D(4k-D), and its forcing at degree k-1 is -2k times that density coefficient. Matching degree k-1 gives 4k*k times the new degree-k stream coefficient, yielding the factor -1/(2k).

The first density profile is

    a_1= -2(k-1)sin((m+1)theta)/(9k)
          -(k-1)sin((m-1)theta)/(9k).

Substituting this into the two inverses and the two remaining density steps gives the offset +1 coefficient

    [sin((m+1)theta)]a_3 = -2k R(k).

Every intermediate rational coefficient is retained in verification/checks.json, and the stated four recurrence operations reproduce the table. The outer offsets in a_3 are at most 5, so no reflected frequency can coincide with m+1 when k>=3. At k=2 the offset -5 gives sin(-3theta), which must be subtracted from the offset +1 term. This computes the displayed b_3. The displayed b_2 is obtained from the exact order-6 edge recurrence; its density sin(theta) coefficient is -2b_2. The complete rational low-order table and both independent coefficient-identity audits are in topic102. The symbolic cycle agrees with 48 exact coefficient checks through order18, including every resonant scalar in that range.

## Nonvanishing and growth

The denominator of R(k) is positive for k>=3. With x=k-3>=0,

    P(x+3)=6480x^5+94068x^4+522162x^3
           +1398858x^2+1818927x+921445.

All coefficients are positive. Thus R(k)>0 and the negative b_3 remains negative forever. The separate b_2 is also negative. Leading coefficients give lim_k kR(k)=1/3240. Taking logarithmic Cesaro means of the ratios of (k-1)!|b_k| proves its kth-root limit.

The finitely many normalized profiles a_1,a_2,a_3,h_1,h_2 have rational coefficients in k, with no integer poles for k>=3 and bounded limits. Each has a coefficient with a nonzero limit: one may use offset +1 in a_1,a_2,a_3, offset +2 in h_1, and offset +2 in h_2. Therefore their sine-coefficient norms are bounded above and below by positive constants for all sufficiently large k. For k>=4 the relevant positive frequencies are distinct, so folding cannot change this conclusion. Multiplying by b_k gives the stated full-order factorial rates.

For any lambda'>1/3240, the established root limit bounds these unweighted profiles by C(lambda')^k/(k-1)!. Their subseries are bounded by constant multiples of

    |z|^r sum_(k>=2) (lambda' |z|^3)^k |t|^(k-1)/(k-1)!.

This sum is finite for every finite z,t, proving the subseries statement. It imposes no bound on the remaining columns.

## The order-250 countercheck

At k=83,r=1, the degree is k-1=82 and m+1=165. Its coefficient is

    v=b_83 [-2(83-1)/(9*83)],
    b_83=b_3 product_(k=3,...,82) R(k).

All factors are explicit nonzero rational numbers. The stored numerator and denominator give an exact reproducible certificate: if v=u/vden with vden>0, direct integer comparison gives |u|*2^1075<vden. This is the exact comparison underlying the binary64 conclusion; the quoted decimal logarithm is a diagnostic only. The independently frozen float checkpoint has no degree-82 column at order250. It cannot record this exact nonzero coefficient. This establishes the mechanism for loss of high log columns, using the complete cycle derivation above, now independently reviewed in V312.

## Dependencies and verification scope

Topic10 defines the canonical polynomial-log inverse; topic17 proves degree upper bounds; topic44 proves the analogous full-recurrence cycle; topic102 supplies independently generated exact edge coefficients and residual checks. The present derivation retains only the two explicitly stated ordered pairs and does not reuse the full-recurrence scalar ratio. Source and exact JSON are retained alongside this proof. No Lean or numerical interval certificate of the infinite recurrence has been constructed. The independent theory-part review in V312 confirms the all-order result, including a second symbolic cycle and exact low-order implementation.
