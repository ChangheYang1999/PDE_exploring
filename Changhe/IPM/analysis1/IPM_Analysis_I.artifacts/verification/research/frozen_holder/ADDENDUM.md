# Review resolutions for topic74

Written 2026-10-20T23:59:52.979949+00:00, after four substantive actualClaudeOpus5.5 reviews. The original PROOF.md and computed inputs remain unchanged. This addendum supplies the details requested during review and corrects overstatements in the reviews.

## Core density used in section2
In Fourier variables write Q=B zeta dot grad_zeta. Choose smooth cutoffs chi_R supported where 1/(2R)<|zeta|<2R, equal1 where1/R<|zeta|<R, with |Q chi_R|<=C independent ofR. For f inD(Q), distributional product differentiation gives Q(chi_R f)=chi_R Qf+(Qchi_R)f. The final term tends to0 inL2 because its support lies in the two shrinking L2 tails; chi_Rf andchi_RQf converge inL2.
For a compactly supported annular g, convolution with a compactly supported mollifier rho_epsilon preserves annular support for small epsilon. The commutator is

 Q(g*rho_epsilon)-(Qg)*rho_epsilon=g*k_epsilon,
 k_epsilon(w)=B w dot grad rho_epsilon(w)+tr(B)rho_epsilon(w).

It has integral0, uniformly boundedL1norm and support shrinking to0. Thus

 ||g*k_epsilon||2 <=integral |k_epsilon(w)| ||g(.-w)-g||2 dw ->0

by strong continuity of translations, uniformly over shrinking support. Mollification therefore converges in the Qgraphnorm. This proves the asserted smooth annular Fourier core, and bounded perturbation gives the same core forL. The needed closed transport generator follows directly by Fourier conjugation of the explicit strongly continuous dilation group.

## Minor points in upper and packet reviews
The original statement 'q>1, so the low input series converges' is logically sufficient. Its minimal condition is q+2>0. No incorrect convergence implication is used. For W choose a nonnegative smooth frequency bump on a small set where the nonzero limit has nearly constant phase, multiply by that phase, and use the complex sesquilinear pairing. This gives a nonzero limit. Its real or imaginary part gives a real test with the corresponding reflected Fourier support and a nonzero pairing. The reflected original-x parity alternative has two separated supports; it is not an input supported only nearP.

## Dependencies and details for both order1 logarithms
The logs review was given section5 in isolation. The omitted dependencies were already in the unchanged proof: S_t andQ_t are(4)-(5), 0<=Q_t<=1 is used in(6), and the full localL2tail estimate is(17), independently accepted by the packet review. Equations(19) and(23) follow from(4) by ordinary Fourier inversion and the two symmetric sin carriers. If c is the real part of the chosen nonzero limit pairing in(24), reverse its phase to make c>0. The uniform convergence proved with the two integrable tau majorants gives J0 such that every J>=J0 and every j in the stated range has realpart at leastc/2. Since the count is >=c_0 J, the realpart of the sum is >=cc_0J/2. Applying(17) gives(25). No cancellation estimate is missing.
The review's phrase 'convergent in the C1-sup norm' is stronger than what its cited estimate shows. Equation(21) bounds the y derivative only. What is needed and proved is convergence of that derivative integral uniformly, together with L2 convergence of the function. For any compact test, distributional differentiation commutes with the L2 limit; the derivative agrees with its uniform continuous limit, which justifies(3). No integrability of the s derivative is needed for this lower bound. For each fixedN, the upperbound can also give bounded first derivatives by taking a sufficiently high input order since q>1.
For the second-y-derivative tail in(23), Q_t commutes with derivatives and |Q_t|<=1. The absolute Fourier integral of the second derivative of phi(s)psi(y)sinNy is <=C N², giving the uniform spatial bound used there. The vanishing first twoYmoments hold for everyS because What vanishes on an entire strip aroundnu0.

## Fixed smooth forcing ceiling
All tests in section6 are chosen with frequency support in a small compact subset ofkappa>0,nu>0 where the continuous limit(26) has nonzero fixed imaginary sign. The pairing is sesquilinear as above. R is always the L2selected inverse fromsection2 and(5) is its semigroup integrand; the negative time integral of(5) is the resolvent formula. The proof never treats(5) alone as a resolvent integral. Nonzero fixed forcing is obtained with realeven smoothu,v of nonzero integral, thenphi=u*u,psi=v*v. Fornu>0 all factors in ifhat are nonnegative and positive at sufficiently small frequencies.
The ceiling review's description of the negative-tau weight by itself omits growth of the norm factor, but its conclusion is valid: the full prefactor times norm is bounded byC exp(C|tau|), while Schwartzdecay in e^(A|tau|)kappa dominates any such fixed exponential.

## Scope
The theorem remains only the specified frozenL2 realization with compact forcing. Variablecoefficientgraphdensity, quantitative fullIPMinverse, forcingnormsandnonlinearclosure remainOPEN. The logarithm at inputordera is an upper bound only; sharpness of that logarithm isOPEN. All numerical constants are illustrations at explicitly chosen exactrationalparameters, not enclosures of exactprofilederivatives.
