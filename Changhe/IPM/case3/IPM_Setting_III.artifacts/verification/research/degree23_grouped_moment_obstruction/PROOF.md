# The degree-23 finite node obstruction

Written 2026-10-21T22:32:58.107308+00:00 before independent arithmetic. Status: CONDITIONAL on the explicit finite gates below. The producer's declaration of exclusion is not accepted as proof. No conclusion about existence or nonexistence for the full-plane IPM equation follows from this finite auxiliary problem alone.

## Statement, notation, and dependencies

Let A0 be a positive odd integer and let mu1,...,mu_(e+1) be positive integers, where e>=2 and A0+2 sum(mu_j)=23. Write Aj=2mu_j. Let n be an integer at least1, eta=23+2n and T=A0 eta-23. Thus eta>=25 and T>=2. Suppose there are e+1 distinct complex numbers x_j, none equal to0, eta-1 or eta. Their multiset, with weights Aj, is invariant under complex conjugation. The node equations are

    M_l := A0(eta-1)^l + sum_j Aj x_j^l = 0,   1<=l<=e,
    sum_j 1/(eta-x_j) = 0,
    sum_j Aj/(eta-x_j) = -T/eta.

The proposed theorem is that these hypotheses are inconsistent. Integrality of n is part of the statement. The stronger statement for every real n>=1 is not asserted. Two real noninteger configurations have been proposed and receive a separate audit.

The proof uses the independently checked equal-weight, exceptional-weight, real-node, and two-pair implications in research/report79_new_lemma_audit/PROOF.md and its LEMMA_CHECKS.json, and the moment/logarithmic reduction checked in the preceding finite-axis developments. Their hypotheses, especially conjugation invariance and forbidden nodes, are retained here. This proof states its own node theorem. The further corollary d>=25 and P=n+d/2>=27/2 requires the prior reduction from a finite polynomial auxiliary axis ansatz, the oddness of d, the e<=1 exclusions and the verified d<=21 exclusions. It is a corollary for that class only.

## Exhaustive reduction to multiplicity patterns

For each A0 in1,3,...,23, the mu_j form a positive unordered partition of(23-A0)/2 into at least3 parts. A nondecreasing tuple has a unique first entry; recursion on that entry and the remaining sum enumerates every tuple once. A second recursion on the multiplicity of each possible part independently checks the same finite set.

Apply the prior lemmas in the following order. A single weight class is impossible because the two logarithmic equations would imply T=0. If there are two classes with one singleton, let nu be its multiplicity and mu the repeated multiplicity. The exceptional-weight implication excludes nu>mu; for nu<mu it requires A0=1 and mu-nu>n. Therefore A0>=3 or mu-nu<=1 excludes the pattern for all real n>=1. A weight class of odd cardinality contains a real node, by conjugation invariance. Three such classes contradict the real-node bound. Finally two quadratic classes of weights a,b are excluded if T(a+b)>ab. The checker must verify the strict integer margin at T_min=25A0-23 for every use of this condition, rather than infer it from a label.

The two enumerations and the filters are expected to leave49 of153 patterns. Their full tuples, filter witnesses and e values must be compared, not merely their counts. Expected surviving classes are: one exceptional singleton pattern; twelve pair-and-m patterns (typeI); twenty-two two-singleton-and-m patterns (typeII); one cubic-cubic (typeIII); five singleton-pair-pair (typeIV); two cubic-quartic (typeV); four singleton-pair-cubic (typeVI); one cubic-quintic (typeV5); and one singleton-pair-quartic (typeVI4). A structural classification from the cardinalities of equal-weight classes must cover every survivor and identify its coefficient certificate uniquely.

## Reconstruction of the equations

For a monic polynomial p(z)=z^r+c1 z^(r-1)+...+cr, let s_l be the sum of the l-th powers of its roots, with s0=r. Newton's identities give

    s_l + sum_(j=1)^(l-1) c_j s_(l-j) + l c_l = 0  (l<=r),
    s_l + sum_(j=1)^r c_j s_(l-j) = 0             (l>r).

Thus the l-th moment fixes a new coefficient with a nonzero integer multiple of its positive weight as pivot. Our reconstruction uses the previously tested rational-polynomial library exact_degree21.py; it is our code, not the producer's generator. Its universal Newton/logarithmic-series tests cover all degrees and moment orders used here. Recheck the relevant hashes and coverage bounds. Compare every reconstructed class polynomial coefficient, solved moment, residual numerator and denominator factor with the frozen data. Integer contents and signs may be removed, but no parameter-dependent factor may be silently discarded.

For two classes with distinct weights w,b, the logarithmic equations are equivalent to

    (w-b) eta p'(eta) + T p(eta)=0,
    (w-b) eta q'(eta) - T q(eta)=0.

Both polynomials are nonzero at eta because their roots avoid eta. If p has degree2, write p=z^2-x z+c2. The first equation fixes

    c2=((T+w-b)x eta-(T+2(w-b))eta^2)/T.

If p has degree3, write p=z^3-x z^2+y z+c3. The same equation fixes c3 with pivot T. For q of degree m, moments1,...,m-1 fix its first m-1 coefficients, and the second logarithmic equation fixes its constant coefficient with pivot -T. For the quadratic class the two residual moments are m,m+1. For the cubic class they are m,m+1,m+2. The only parameter-dependent denominator is a power of T.

For two singleton weights a1,a2 and a repeated weight b, take the first singleton node x. Put S=(T+a1-b)eta-Tx. The second node is

    x2=eta+(a2-b)eta(eta-x)/S.

If S=0, the cleared weighted logarithmic identity has the nonzero remaining factor (a1-b)(a2-b)eta^2/T. This excludes that branch. Moments1,...,m determine the monic polynomial q of the repeated class with nonzero integer pivots. The residual moment m+1 and

    (2eta-x-x2)q(eta)+(eta-x)(eta-x2)q'(eta)=0

are necessary. All denominators divide a nonzero integer times a power of S. Check the eliminated logarithmic identity directly; the formula is not an untested substitution.

For a singleton of weight a at y, a pair of weight w and m nodes of weight b, let D=w-b and define

    L0=1/(eta-y),
    L1=(-T/eta-(a-b)L0)/D,
    L2=( T/eta+(a-w)L0)/D.

Here eta, eta-y and D are nonzero. The two logarithmic equations give these expressions, and L0+L1+L2=0. If L1 L2!=0, write p=z^2-x z+c2 with

    c2=(2eta-x)/L1-eta^2+x eta.

The first m-1 moments fix the first m-1 coefficients of q. Its logarithmic equation q'(eta)=L2 q(eta) fixes its constant coefficient with pivot -L2. The residual moments are m,m+1,m+2. Denominator clearing is allowed only after verifying that the remaining factors are nonzero integers or powers of eta, T, eta-y, numerator(L1), numerator(L2). Every use of the last two is restricted to this regular branch.

## Exceptional branches

In the cubic-cubic case, the first residual numerator is linear in y, say C1(x,eta)y+C0(x,eta). When C1!=0 substitute y=-C0/C1 into the other two moments. When C1=0 the necessary condition C0=0 remains, so Res_x(C1,C0)=0. Check both routes, with the nonzero-C1 denominator ledger. The claimed exceptional degree7 polynomial has a positive shift at eta=25.

For a singleton-pair-m pattern, L1 and L2 cannot both vanish because L0!=0. If L1=0, then y=eta+(a-b)eta/T and L2=T/((a-b)eta). The pair is p=z^2-2eta z+x. The first m-1 moments and the nonzero logarithmic relation for q fix its coefficients. For m>=3 eliminate x between moment m and each of moments m+1,m+2. For m=2, moment2 fixes x with pivot -2w and the last two residuals depend only on eta. No division by L1 occurs.

If L2=0, then y=eta+(a-w)eta/T and L1=T/((a-w)eta). The pair relation fixes c2 in p=z^2-xz+c2. The first m-2 moments determine the first m-2 coefficients of q, q'(eta)=0 fixes its linear coefficient with pivot1, and moment m fixes its constant coefficient with pivot -m b. For m>=3 eliminate x between moment m-1 and each of moments m+1,m+2. When m=2, moment1 fixes x with pivot w. No division by L2 occurs. For the ten singleton-pair patterns this gives twenty branches. The claimed normalized gcd1 must be established separately in every branch.

For the remaining exceptional pattern (A0;mu)=(1;5,5,1), the singleton weight2 has node eta(1-8/T), T=eta-23. The first two moments determine the sum and product of the weight10 pair. With pi the product of the pair polynomial and the singleton factor, direct differentiation gives

    pi'(eta)=(299eta^4-10856eta^3+91434eta^2-21896eta+5819)
             /(200(eta-23)^2).

At eta=25+m the numerator is

    3776544+2882304m+398484m^2+19044m^3+299m^4.

All coefficients and the denominator are positive for m>=0. The required identity pi'(eta)=0 is impossible. The formula and its three quoted n=1,2,3 values are checked by exact rational algebra, not assumed from the producer's display.

## Exact elimination and arithmetic obligations

All resultants mean fixed formal-degree Sylvester determinants over the indicated polynomial ring. At a common finite root the Sylvester matrix is singular. This necessary condition holds even when leading coefficients vanish after specializing eta. A nonzero integer content may be divided out. A parameter factor may be divided out only after it has been shown nonzero on the branch in question.

For two residual polynomials in x, eliminate x. For three residual polynomials f0,f1,f2 in an inner variable, compute the three pairwise resultants R01,R02,R12. Remove only the recorded, allowed nonzero factors from each of these three. Then compute the outer resultants of R01 with R02 and R12. Both outer resultants vanish at any solution, so their gcd does too by the polynomial Bezout identity in Q[eta]. The producer's certificate specifies the three inner normalizations; verify all three explicitly. Finally remove powers of eta and T from the gcd and primitive-normalize. This avoids the ambiguity discovered in the preceding degree21 report.

Our determinant implementation uses its own Sylvester matrix and fraction-free Bareiss elimination, with every division checked exact. A second implementation with Fraction Gaussian elimination checks selected integer specializations. If the two polynomials have inner degrees r,s and eta-degrees a,b before specialization, each determinant term has s coefficients of the first polynomial and r of the second. Its eta-degree is at most B=sa+rb. Agreement of the proposed resultant with the exact determinant at B+1 distinct integer points therefore proves the polynomial identity, including cases with degree drops. A rational proportionality constant is permitted for primitive normalization but must be fixed once, nonzero and checked at every point.

For a claimed full gcd G, divide both polynomials by G exactly. Certify the quotient polynomials coprime modulo a prime at which both leading coefficients remain nonzero, with an explicit finite-field Bezout identity. Any nonconstant rational common divisor would have a primitive integer representative by Gauss's lemma and would retain degree at such a prime, a contradiction. This establishes the rational gcd up to a nonzero scalar. The modular computation is exact and does not replace the determinant identity checks.

Convert the final necessary primitive polynomials to full integer coefficient lists. Expand Lambda(25+m) by the binomial theorem and compare every coefficient, degree and minimum with the frozen data. Forty-six of the48 main resultant cases are claimed to have strictly positive coefficients. Together with the exceptional direct formula they exclude47 patterns for every real n>=1. The remaining two patterns are (1;3,3,1,1,1,1,1) and (1;2,2,1,1,1,1,1,1,1). For those, the claimed degree48 and88 polynomials have Lambda(25)<0 and strictly positive coefficients in Lambda(26+m). Thus n=1 is excluded by the nonzero value at25, and every integer n>=2 is excluded because eta>=27. This argument deliberately leaves possible real eta in(25,26).

The independent theorem can be marked CONFIRMED only after the full enumeration, reconstructed coefficients and residuals, all twenty logarithmic branches and the cubic pivot, all exact resultant identities, gcd certificates and all shifted coefficients pass their gates. Exact JSON input is data, not proof. Any failed or unexecuted gate leaves the relevant claim OPEN. The separate noninteger existence audit is not needed for the integer exclusion, but is needed before stating that the stronger real-n claim is false.
