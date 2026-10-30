# Acceptance of the repaired T2 summary and its decimal sweep

## Statement and scope

For the frozen 17:43:47Z revision of `the T2 final summary`, the four changes requested in T4-491 are valid: the common scalar L2 budget is strictly below 3.7930e-6; the relaxation factor is the stated exact expression, approximately 0.99998313; lower bounds do not rank the actual correction distances; and the graded bound 4.5717e-4 follows from the sharper middle expression, not the coarser rational 25/54684. The repaired moment coefficient is enclosed by (5.04422709906931,5.04422709906932). The 21 computable decimal classifications in handoff BT are independently checkable from the exact formulas below. This is an acceptance of corrections to existing results, not a new candidate existence theorem.

All inherited analytic hypotheses and candidate exclusions remain those of T4-491 and its named dependencies. In particular, an algebraically feasible closure radius is not asserted to satisfy a new candidate's PDE hypotheses. A hash certifies the identity of an input, not its mathematical truth.

## Scalar and graded budgets

For a scheme with rate beta = mu - C s - u r/sqrt(s) and N(h) >= w ||h||_2, positivity implies r/w < (mu-C s)sqrt(s)/(u w). Setting t=sqrt(s), the derivative of (mu-C t^2)t is mu-3C t^2. Its maximum squared, divided by u^2 w^2, is 4mu^3/(27C u^2 w^2). The seven registered scalar rows and separate alternative route were already bounded in T4-491. For TB-sharp, mu=297/1000, C=402, u=8/5, w=512, the square equals 323433/22481469440000000 and lies between (3.7929e-6)^2 and (3.7930e-6)^2.

To refute the former 3.79e-6 deduction, take s=1/4096, b=3791/10^9, r=512b, eta=10^-7. Direct substitution gives beta=1957759/20000000000>0 and beta r>eta. Since pi>3, (c_s r)^2<r^2/(12s(1+s))<(36/1000)^2. Thus the slope condition c_s r<7/10 and low contraction (c_s r)/(19/5-c_s r)<1 hold. Yet r/512=b>3.79e-6.

For graded boxes with m2>0, the inherited estimate is n<sqrt(s)(1/2-4708s)/(217/50). The same derivative calculation gives its maximum at s=1/28248, with square 2500/(651^2*28248). Exact squaring shows this maximum lies between 4.5697e-4 and 4.5698e-4, below 4.5717e-4. But 25/54684>4.5717e-4. The repaired chain therefore uses the middle expression. No positivity is lost by the squaring.

## Exact factor and absence of distance ordering

In the relaxed Gram problem, the squared optimum depends on the commutator and velocity constants only through 1/(K u^2). Replacing rational lower constants k=39068/100 and u=15871/10000 by the exact K00 and v=A'+B' consequently multiplies the optimum's square root by sqrt(k/K00)u/v. T4-473 and T4-491 independently evaluated their explicit gamma-function and pi formulas, giving the strict interval (0.99998312568,0.99998312569). Both endpoints round to 0.99998313 at eight decimal places. The decimal is not equal to the factor.

Statements d_i>L_i impose no relative ordering on the unknown d_i: for any two finite lower bounds, values above both bounds may be chosen in either order. This logical observation also allows infinite distances. The summary correctly retains actual distance ranking as OPEN.

## Moment coefficient and other decimal displays

Write c=4076476460239181/2^51, gamma=1/c and q*=gamma-4. Then -q*-j=4-j-gamma>0 for j=1,2,3. The accepted moment estimate |m|<=8H/[(-q*-1)(-q*-2)(-q*-3)] has exact coefficient

    M = 8/[(3-gamma)(2-gamma)(1-gamma)].

Cross multiplication of positive integer denominators proves 5.04422709906931<M<5.04422709906932. Thus 5.0442<M<5.04423. Replacing the former coefficient by this interval or by 5.04423 is valid. It does not change the exact analytic formula.

For the remaining sweep, use the exact rational c, gamma, delta=1-gamma, the accepted rational universal lower coefficient, thresholds 3/327680,5289/50000000,76219/10^9,4207/20000000, weights 1+32/25+2^14 and 1+32/25+2^15, and floor6091157959/250000000000. For defect boxes set mu=1/10-4800/2^18,A=2560 and use epsilon=((mu-Am-B)^2-4ABm)/(4A), with (m,B)=(2^-17,1/100) or (2^-16,1/200). For dyadic radii use R_univ(a)=sqrt(8pi)(1+c-ca)/(1+a). The other expressions are 25/(868sqrt(pi)), theta=(1-gamma)/(3-gamma),25/(54684*512), and sqrt((4log2-1)/(8pi)). Rational comparisons are exact; transcendental comparisons use outward Arb balls. Five displays equal their expressions exactly; sixteen are rounded. In particular 9.1553e-6-3/327680=17/640000000000>0, so that threshold is written as the exact fraction with an approximate display.

## Verification and dependencies

The independent checker binds the repaired summary, producer's checker as text, result JSON, and handoff BT. It compares every changed block with the frozen T4-491 version, checks the four repairs and the moment interval, independently classifies the 21 displays, and retains historical row wording under the explicit new erratum. The producer code is not executed. T4-491 supplies the already accepted analytic hypotheses and exact factor evaluation; the present proof rederives the changed algebra. Verification evidence is in `verification/`, exact input data in `data/`, and frozen source text in `source/`.
