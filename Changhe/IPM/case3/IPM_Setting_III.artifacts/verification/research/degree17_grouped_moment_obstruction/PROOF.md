# Degree17: independent normalized-node reduction

Result275. Initial informal reduction written 2026-10-21T18:44:39.111747+00:00 before any new symbolic computation. No lead or numerics code is imported or reused. At the initial writing the nine-case exclusion was OPEN. The initial proof and later exact check are distinguished below. The original text is frozen in INITIAL_REDUCTION.md.

## Hypotheses and statement to check

Use the proved auxiliary finite-polynomial residue system253/258 and multiplicity lemma261, with lower-degree closure267. Set m=17, n>=1 real, D=17+2n, z=D/(D-1), tau=1/z and T=A0 D-m>0. The underlying polynomial problem requires integer n; proving impossibility for real n>=1 is stronger for the individual cases. Transformed nodes vj are nonzero, distinct, not1 or z, conjugation preserves their positive even weights wj=2muj, and A0 is odd positive. Their count is e+1, e>=2, with m=A0+sum wj. Necessarily

 M_l=A0+sum wj vj^l=0 (1<=l<=e),
 sum 1/(z-vj)=0,
 A0/(z-1)+sum wj/(z-vj)=m/z.

Equal weights are excluded. A unique higher weight is excluded; a unique lower weight2nu below the others2mu requires A0=1 and mu-nu>n. Pairwise distinct weights force real nodes, contradicting M2>0. Enumerate every positive partition of(17-A0)/2 into e+1 integers, with A0 odd. After these necessary exclusions the expected survivors are

 (5;2,2,1,1), (1;3,3,1,1),
 (1;2,2,2,1,1), (3;2,2,1,1,1), (1;2,2,1,1,1,1),
 (1;4,2,1,1), (1;3,2,2,1), (3;3,2,1,1), (1;3,2,1,1,1).

The recursive enumeration, including the completeness of this list, must be checked independently. This is a finite auxiliary class, not the full-plane IPM admissible class.

## Independent change of variables

Put qj=vj/z. Dividing each moment by z^l gives A0 tau^l+sum wj qj^l=0. Multiplying both derivative equations by z gives sum1/(1-qj)=0 and sum wj/(1-qj)=-T. A weight group's monic real polynomial P(q)=product(q-qj) satisfies P'(1)/P(1)=sum1/(1-qj), with nonzero P(1). These equations retain the pole exclusions.

For a monic polynomial P(q)=q^L+c1 q^(L-1)+...+cL, Newton's identities give power sums S_l by
 S_l=-sum_(j=1)^(l-1) cj S_(l-j)-l cl for1<=l<=L,
 S_l=-sum_(j=1)^L cj S_(l-j) for l>L.
Conversely cl=-(S_l+sum_(j=1)^(l-1)cj S_(l-j))/l. These follow by expanding P'/P at infinity. They can also be checked on explicit roots without trusting a symbolic routine.

## Two classes: one quadratic group and a group of degree L

Let U(q)=q^2-pq+c have weight a, and W(q) degree L have weight b, with a!=b. Both polynomials have real coefficients. Set lambda=T/(a-b), which is nonzero. The derivative equations give U'(1)/U(1)=-lambda and W'(1)/W(1)=lambda. Consequently

 c=((lambda+1)p-(lambda+2))/lambda.

For l=1,...,L-1, let S_l(W)=-(A0 tau^l+a S_l(U))/b, and recover the first L-1 coefficients of W by Newton's identities. Finally W'(1)=lambda W(1) fixes its constant coefficient as

 cL=[sum_(j=0)^(L-1)(L-j)cj]/lambda-sum_(j=0)^(L-1)cj, c0=1.

The remaining two necessary equations are M_L=M_(L+1)=0, using the same normalized moments. All divisions are by nonzero lambda, positive D,b and positive integer indices. For the two-quadratic cases (A0,a,b)=(5,4,2),(1,6,2), M2 is a real quadratic in p; if its discriminant is strictly negative for n>=1 it already excludes the case. For the other cases use (A0,a,b,L)=(1,2,4,3),(3,4,2,3),(1,4,2,4). The first choice uses the lower-weight quadratic group and therefore lambda=-n; no positivity assumption on lambda is imposed in this reduction.

## Three classes: two real singletons and one group of degree L

The singleton weights wa,wb differ from the group weight wq. Let their nodes be alpha,beta and set t=1/(1-alpha), s=1/(1-beta). Both are finite nonzero real numbers. Subtracting wq times the unweighted derivative equation gives

 (wa-wq)t+(wb-wq)s=-T,
 s=(-T-(wa-wq)t)/(wb-wq), alpha=1-1/t, beta=1-1/s.

For l=1,...,L, prescribe the group power sums by
 S_l(Q)=-(A0 tau^l+wa alpha^l+wb beta^l)/wq
and reconstruct every coefficient of monic Q by Newton. The remaining necessary equations are

 A0 tau^(L+1)+wa alpha^(L+1)+wb beta^(L+1)+wq S_(L+1)(Q)=0,
 Q'(1)+(t+s)Q(1)=0.

Use (A0,wa,wb,wq,L)=(1,8,4,2,2),(1,6,2,4,2),(3,6,4,2,2),(1,6,4,2,3). Every division is by nonzero D,t,s and nonzero constant weights or indices. No use of an extra A7 relation is made. If these necessary subsets suffice for a nonzero resultant, that stronger obstruction is valid.

## Exact certificate protocol and limits

Symbolic expansion/resultants are discovery only. For each pair record the full primitive integer numerators, denominators and every factor removed in cancellation. Independent rational polynomial arithmetic must reconstruct the same equations and verify that all removed factors are products of known nonzero constants,D,n or the nonzero t,s. No arbitrary parameter or variable factor may be discarded. An exact Sylvester determinant is zero at a common finite root even when leading coefficients vanish after specialization. A nonzero determinant polynomial on n>=1 therefore excludes the necessary equations with no lost degree-drop branch.

For each determinant polynomial store its exact coefficient factors in JSON. Verify its factor product and positive coefficients after n=1+x, or supply a separate exact sign argument if that test fails. Verify the determinant identity by exact integer evaluations at one more than the degree bound db*deg_n(A)+da*deg_n(B), using an independent Bareiss implementation and a rational Gaussian cross-check. The proof needs both the exact identity and its sign, not just discovery root approximations. No exclusion is claimed until these steps are complete. All arithmetic/certificate inputs and proof versions are hash-bound.

A confirmed degree17 exclusion together with267 would only yield odd m>=19 and P=n+m/2>=21/2 for a nonzero finite auxiliary polynomial axis identity. No degree-uniform residual bound, nonpolynomial obstruction, convergence theorem, full-plane NO or YES follows. Full-plane remains UNRESOLVED. No early finish. Only own-lane writes; no JavaScript/TypeScript/Node, no servers/listeners/tunnels, no RLScience cluster, no Lean/Lake. One heavy single-threaded CPU process at nice19, RAM below16GB.

## Exact elimination certificate and conclusion

Completion of the informal argument 2026-10-21T18:50:12.679886+00:00, before the independent checker is executed. The initial reduction is retained verbatim in INITIAL_REDUCTION.md. Symbolic discovery has supplied candidate exact identities; the first independent checker confirmed them with698checks at2026-10-21T18:50Z; its actual timestamp is in verification/CHECKS_initial698.json. Review repairs below require a fresh checker pass. The certificate SHA256 is 37e6a666f815ed01b97f2808d639946d7cfdcd038ec368766ad50a145f7307e3.

The two q22 cases have discriminants equal to a negative nonzero constant times a squared positive linear factor times a quartic whose coefficients after n=1+x are strictly positive. The negative discriminants exclude every real p. If a leading quadratic coefficient were zero at a parameter, its discriminant would be a square and could not be negative, so no degree-drop exception is lost.

For the other seven cases, form the Sylvester matrix of the two primitive numerators in the variable p or t. Its determinant is the product in the following table. Here F_d denotes the specific degree d integer polynomial stored in that case in certificate.json, not a common polynomial across cases. All factor coefficients, exponents, signs, equation numerators and equation denominators are exact JSON data. Each factor, including F_d, has strictly positive coefficients after the substitution n=1+x. A positive constant term then proves strict positivity for every n>=1.

| Case | Parameter tuple | Degrees (variable,n) | Determinant degree bound | Constant | Factor degrees and powers |
|---|---|---|---:|---:|---|
| q22a | (5, 4, 2, 2) | [[2, 3], [3, 4]] | discriminant | -8 | 1^2, 4^1 |
| q22b | (1, 6, 2, 2) | [[2, 3], [3, 4]] | discriminant | -4 | 1^2, 4^1 |
| q23a | (1, 2, 4, 3) | [[3, 5], [4, 6]] | 38 | 6400 | 1^6, 1^12, 20^1 |
| q23b | (3, 4, 2, 3) | [[3, 5], [4, 6]] | 38 | -640 | 1^6, 1^12, 20^1 |
| q24 | (1, 4, 2, 4) | [[4, 6], [5, 7]] | 58 | 746496 | 1^6, 1^20, 32^1 |
| s112a | (1, 8, 4, 2, 2) | [[6, 6], [5, 5]] | 60 | 18662400 | 1^9, 1^12, 24^1 |
| s112b | (1, 6, 2, 4, 2) | [[6, 6], [5, 5]] | 60 | -25600 | 1^9, 1^12, 24^1 |
| s112c | (3, 6, 4, 2, 2) | [[6, 6], [5, 5]] | 60 | 81920 | 1^9, 1^12, 24^1 |
| s113 | (1, 6, 4, 2, 3) | [[8, 8], [7, 7]] | 112 | 3057647616000 | 1^16, 1^24, 44^1 |

For clarity, the sign proof uses exact shifted coefficients, not approximate roots. Let A(p,n) and B(p,n) have variable degrees a,b and parameter degrees c,d. Every determinant summand uses b coefficients of A and a coefficients of B. Hence its degree in n is at most bc+ad. Agreement with the JSON product at bc+ad+1 distinct integer n values proves the identity as polynomials over Q; one additional point is checked as a sentinel. Each evaluation is an integer Bareiss determinant with every intermediate division checked for zero remainder. A separate rational Gaussian determinant at n=1,2,3/2 tests the elimination implementation. The finite computations provide exact identity verification, not a sampled sign argument.

The rational reconstruction checker uses sparse Q[p,n] polynomials, independently of symbolic cancellation or resultants. Every denominator is kept as powers of D and lambda (two classes), or D,t,s (three classes), whose nonvanishing is part of the reduction. Cancellation divides by only one of these known nonzero factors and checks the polynomial remainder exactly. It reconstructs the Newton equations, checks cross-multiplication against the stored rational equations, checks that each saved denominator divides the product of allowed factors, and checks the nonzero rational content relating the saved numerator to its primitive polynomial. Thus the computed primitive equations are necessary for an admissible node configuration and no root branch is discarded by clearing denominators.

The Sylvester determinant of two polynomials with a common finite root is zero. This remains true when their leading coefficients vanish on specialization, since the fixed-size determinant is still an algebraic necessary condition. The certified factor signs make each determinant nonzero for every real n>=1. The seven cases are impossible. Together with the two negative discriminants, this excludes all nine surviving partitions. The recursive partition enumeration must establish both their completeness and the applicable prior exclusions. Consequently the finite auxiliary polynomial residue system has no solution with m=17. With the independently proved lower degrees in267, its next possible odd degree is m>=19, and P=n+m/2>=21/2. These are necessary lower bounds, not an existence assertion at the next degree.

This proof uses real n>=1 for these finitely many multiplicity patterns and positive integer multiplicities for the completeness enumeration. It does not exclude the residue system at arbitrary real weights or arbitrary degree, does not produce a profile, and does not address general nonpolynomial full-plane solutions. The independent checker and review evidence determine the recorded verdict. The original698-check run and review are retained; the final gate and VERDICT.md record the checked revision.

## Review repairs 2026-10-21T18:54:13.177374+00:00

Actual Claude Opus5.5 hand-reviewed the argument and code, without executing them, and found no mathematical error. It requested a machine check of the case-to-partition bijection and a frozen library hash. Both are now added. The sparse-polynomial and determinant library reuses our own267implementation; it imports no Sympy, lead-lane or numerics-lane code. Its exact active bytes are compared against a frozen copy in the dependency manifest. A zero remainder from its single-divisor polynomial division is the exact divisibility witness. The constant sign is the product sign because every factor is separately proved positive. The mathematical content of258/261/267 is an explicit dependency, not re-proved merely by reading a PASS record.

One reviewer explanation needs correction: before any elimination the two-class unknowns are the two coefficients of U and L coefficients of W, hence L+2 unknowns, with L+3 necessary equations. Eliminating c and cL leaves L unknowns; L-1 Newton equations leave p, then two moment equations remain. The proof and code already use the correct equations; this repairs only the review's count. The three-class unknowns are two singleton nodes and L coefficients of Q, again L+2, with L+3 necessary equations. Eliminating s and the L Newton coefficients leaves t and two equations. No conclusion relies on an equation count alone.
