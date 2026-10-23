# Degree19: independent normalized moment obstruction

Result282. Initial reduction written 2026-10-21T19:47:20.177693+00:00 before new symbolic computation. The degree19 exclusion is OPEN pending the exact identities, complete case enumeration and independent review specified below. This text is a proof of the reductions, not a claim that uncomputed determinants have any sign. All local symbols are defined here. No lead or numerics code is reused.

## Statement and dependencies

The finite auxiliary polynomial axis problem gives an odd degree d, a positive integer n, A0 odd positive, distinct moving complex nodes v1,...,v_(e+1) different from0,1,z, and positive even weights wj=2 muj, with conjugation preserving weights. For d=19 put D=19+2n, z=D/(D-1), tau=1/z and T=A0 D-19>0. Necessarily d=A0+sum wj and

    A0+sum wj vj^l=0, 1<=l<=e,
    sum 1/(z-vj)=0,
    sum wj/(z-vj)=-T/z.

There are e+1 moving nodes and one additional fixed moment node1. These implications and the restrictions below are dependencies from the standalone proofs of253/258/261/275/278, not conclusions inferred from a PASS filename. Degrees below19 have already been independently excluded. An exclusion at19 would yield only the necessary finite-class bounds d>=21 and P=n+d/2>=23/2. It says nothing about all smooth nonpolynomial full-plane profiles or a limit of trial states.

Set qj=vj/z. Then the normalized moments are A0 tau^l+sum wj qj^l=0, and the logarithmic conditions are sum1/(1-qj)=0 and sum wj/(1-qj)=-T. The group polynomial U(q)=prod(q-qj) is monic and real for each common weight; U(1)!=0 and U'(1)/U(1) is the group's logarithmic sum. All singleton groups consist of real nodes.

For U(q)=q^L+c1 q^(L-1)+...+cL define its power sums S0=L and
    Sk=-sum_{j=1}^{k-1} cj S_(k-j)-k ck, 1<=k<=L;
    Sk=-sum_{j=1}^L cj S_(k-j), k>L.
These identities follow by expanding U'/U at infinity. They also recover each ck uniquely from the first k sums. Only nonzero integer indices are divided out.

## Complete patterns to verify

Enumerate positive integer partitions of(19-A0)/2 of length e+1>=3 for all odd A0>0. Equal weights are excluded. A singleton higher than a single other common weight is excluded. A singleton lower weight2nu against common weight2mu requires A0=1 and mu-nu>n. If all weights are distinct, conjugation makes every moving node real and M2>0. More generally at most two moving nodes are real, exactly one when e is even, as proved in278 by a nonnegative polynomial square. Each weight class with odd cardinality forces a real node, so the count of such classes cannot exceed two, or one when e is even. Also the two quadratic class lemma in278 excludes any such partition with A0>=3. These extra rules are required in the enumeration. The expected67 partitions reduce to the following16 survivors, written (A0; multiplicities), in ascending order within the list:

    (1;1,4,4),
    (1;1,1,2,5), (1;1,1,3,4), (1;1,2,2,4), (1;1,2,3,3),
    (1;1,1,1,3,3), (1;1,1,2,2,3),
    (1;1,1,1,1,2,3), (1;1,1,1,2,2,2), (1;1,1,1,1,1,2,2),
    (3;1,1,2,4), (3;1,2,2,3), (3;1,1,2,2,2), (3;1,1,1,1,2,2),
    (5;1,1,2,3), (5;1,1,1,2,2).

Independent enumeration must check exhaustiveness and the bijection between these partitions and the reductions below. The lone three-node pattern requires integer n=1 or2. The other15 reductions will try to exclude all real n>=1, which suffices for the integer problem. No search over a finite n range substitutes for that sign proof.

## TypeI: one pair and one other group

The tuple (A0,a,b,L) denotes a quadratic group U=q²-xq+c of weight a and a degree L group W of weight b. Put lambda=T/(a-b)!=0. The logarithmic equations imply U'(1)/U(1)=-lambda, W'(1)/W(1)=lambda, hence
    c=((lambda+1)x-(lambda+2))/lambda.
Recover the first L-1 coefficients of W from S_l(W)=-(A0 tau^l+a S_l(U))/b. The final coefficient is
    cL=sum_{j=0}^{L-1}(L-j)cj/lambda-sum_{j=0}^{L-1}cj, c0=1,
by W'(1)=lambda W(1). The two remaining necessary equations are M_L=M_(L+1)=0. Divisions are by nonzero constants,D,T. Use the five tuples
    (1,6,2,3), (3,2,4,3), (5,4,2,3), (3,4,2,4), (1,4,2,5).
Negative lambda is permitted. Clearing only the stated nonzero factors gives two polynomial numerators in(x,n); a nonzero resultant on n>=1 would exclude the case, including degree-drop specializations.

## TypeII: two singletons and a common group

The tuple (A0,a,b,w,L) has singleton nodes alpha,beta of distinct weights a,b and L remaining nodes of weight w. Set x=1/(1-alpha), s=1/(1-beta), both real and nonzero. The weighted and unweighted sums give
    s=(-T-(a-w)x)/(b-w), alpha=1-1/x, beta=1-1/s.
Recover the monic degree L group Q from S_l(Q)=-(A0 tau^l+a alpha^l+b beta^l)/w for1<=l<=L. The two remaining necessary equations are
    A0 tau^(L+1)+a alpha^(L+1)+b beta^(L+1)+w S_(L+1)(Q)=0,
    Q'(1)+(x+s)Q(1)=0.
Use eight tuples
    (1,10,4,2,2), (1,8,6,2,2), (1,8,2,4,2), (1,4,2,6,2),
    (3,8,4,2,2), (3,6,2,4,2), (5,6,4,2,2), (1,6,4,2,4).
Only D,x,s and nonzero constants are allowed denominator factors. The finite admissible node assumptions imply their nonvanishing.

## TypeIII: two triples

For (1;1,1,1,2,2,2), the cubic group U=q³-xq²+yq-u3 has weight4 and the cubic group W=q³+c1q²+c2q+c3 has weight2. Their logarithmic sums are -n and n. The first gives
    u3=((n+3)-(n+2)x+(n+1)y)/n.
M1 and M2 determine c1,c2 by Newton's identities. W'(1)=n W(1) then gives
    c3=(3+2c1+c2)/n-1-c1-c2.
All these divisions are by D,n or constants. The three remaining necessary equations are M3=M4=M5=0. The first is linear in y after rational simplification; this assertion must be checked exactly. Write its primitive numerator C1(x,n)y+C0(x,n).

The exceptional branch C1=0 requires C0=0. A nonzero resultant Res_x(C1,C0) on n>=1 excludes this entire branch, including any specialization with zero leading coefficients. On the other branch y=-C0/C1. Substitution into M4 and M5 clears only constants,D,n,C1, all known nonzero. Their resultant in x must be certified nonzero on n>=1. No cancellation by an unproved factor of x or n is allowed.

## TypeIV: a singleton and two pairs

For (1;1,1,2,2,3), the singleton alpha has weight6; U=q²-xq+c has weight4 and W=q²-vq+k has weight2. Put t=1/(1-alpha)!=0 and alpha=1-1/t. From L1+L2+t=0 and4L1+2L2+6t=-2n,
    L1=U'(1)/U(1)=-n-2t, L2=W'(1)/W(1)=n+t.
The two exceptional branches are L1=0 or L2=0; they cannot both vanish since n>=1.

When L1 L2!=0, solve
    c=(2-x)/L1-1+x, k=(2-v)/L2-1+v,
    v=-(tau+6alpha+4x)/2
using the two logarithmic relations and M1. The necessary M2 is a quadratic A x²+B x+C with A=12. This leading coefficient is a constant, so division with remainder in x loses no parameter branch. Independently check A=12. Reduce M3 and M4 modulo M2 to r1 x+r0 and r3 x+r2. Every simultaneous solution necessarily satisfies
    N1=r1 r2-r0 r3=0,
    N2=12 r0²-B r0 r1+C r1²=0.
The second identity is the resultant of M2 and its linear M3 remainder. It remains necessary when r1=0; in that case it is12 r0², so the common-root condition still forces r0=0. Thus there is no division by r1. The only allowed denominators are constants,D,t,L1,L2. A nonzero resultant in t of the cleared numerators N1,N2 would exclude this generic branch. The determinant certificate must retain every possible finite common-root specialization.

If L1=0 then t=-n/2, alpha=1+2/n, L2=n/2. U'(1)=0 gives x=2; M1 fixes v; the W logarithmic relation fixes k; M2 fixes c. The remaining M3,M4 are rational functions of n with only D,n and constants in the denominator. A certificate that one is always nonzero, or that their numerators have no common root for n>=1, excludes the branch.
If L2=0 then t=-n, alpha=1+1/n, L1=n. W'(1)=0 gives v=2; M1 fixes x; the U logarithmic relation fixes c; M2 fixes k. The same remaining two moments must be checked. Both branches preserve U(1),W(1)!=0 as hypotheses; proving inconsistency in the relaxed equations is enough.

## Three-node special pattern

For (1;1,4,4), T=2n and n is1 or2. The singleton has v1=z(1-3/n), from its logarithmic relation. With pair sum b1=-(1+2v1)/8 and product b2=(1+2v1²+8b1²)/16, the first two moments vanish. For pi(v)=(v-v1)(v²-b1v+b2),
    pi'(z)=z²-b1z+b2+(z-v1)(2z-b1).
Exact rational evaluation at n=1,2 must give nonzero values. This is a complete check for this branch because the earlier singleton lemma forces n<3 and integer n>=1.

## Certificate protocol and scope

Sympy may discover reductions and determinants. A separate checker using independently implemented exact sparse rational polynomials must reconstruct the equations, all branch identities and all allowed denominators. Record every primitive numerator, rational denominator, constant content and sign certificate in exact JSON. No copied lead polynomial, code or untrusted pickle is executed. The determinant coefficients are verified by exact Sylvester determinants at degree_bound+1 distinct rational parameters, plus a sentinel, where degree_bound=deg_x(B)deg_n(A)+deg_x(A)deg_n(B). Check every Bareiss division exactly and cross-check selected evaluations by rational Gaussian elimination. The factor product is then an identity, not a numerical fit.

For each univariate factor use exact expansion at n=1+h. Strictly positive coefficients, including the constant coefficient, prove positivity for every real n>=1. If such a certificate fails, the branch remains OPEN unless another complete sign proof is supplied. Both generic and exceptional branches must close before the degree19 exclusion can be claimed. This is not a degree-uniform theorem, existence result at degree21, uniform residual floor, convergence claim, full-plane YES or full-plane NO.

Operational restrictions: write only this verifier lane. No JavaScript/TypeScript/Node, no servers/listeners/tunnels, no RLScience cluster, no Lean/Lake, no commits/push/posts. One heavy single-threaded process at nice19, below16GB RAM, lane below2GB. Primary full-plane verdict remains UNRESOLVED. T_end is not reached and no early finish is authorized.

## Partition audit repair

2026-10-21T20:02:34.100705+00:00. The first checker retained20 patterns, not16, because it omitted the real-node parity bound and the two-quadratic sufficient condition that had already been independently proved in278. The original proof also mistyped the last surviving partition as (5;1,1,2,2), which has degree17; its correct form is (5;1,1,1,2,2), already represented by tuple(5,4,2,3) in the checked algebra. The original proof, enumeration and FAIL108 are preserved in verification/initial_partition_FAIL108. PARTITION_PROOF.md now supplies the missing exclusions before the checker is revised. No resultant or sign certificate changes.

## Completion after exact gates

2026-10-21T20:03:31.191091+00:00. The initial pending language above records the discovery stage. The complete argument is now as follows. The exact gate for TYPES12_PROOF.md passed1258 checks; the repaired gate for TYPES34_PROOF.md passed674; and the repaired exhaustive partition gate passed128. All individual booleans and the source hashes are stored in the named JSON gates. The exact coefficient certificates are in verification/types_I_II_certificate.json and types_III_IV_certificate.json. These certificates contain all numerator, denominator, primitive-content and factor arrays; no large coefficient table is hardcoded into a formal source. No Lean formalization is claimed.

For each of the thirteen typeI/II patterns, the checker reconstructs the rational Newton equations using independently implemented sparse Fraction polynomials, checks denominator factorization against the explicitly allowed nonzero factors, and checks that primitive reduction removes only a rational scalar over all variables. The table in TYPES12_PROOF.md records numerator degrees, determinant degree bounds and factor degrees/exponents. Every factor has strictly positive coefficients in n-1, including its constant term. Exact Sylvester determinants at more points than the proven degree bound establish the full polynomial identity; Gaussian elimination checks selected values independently of Bareiss. Thus each determinant is nonzero for every real n>=1.

For typeIII the exceptional determinant has degree16, bound16, and factors with degrees/exponents1^1,1^9,6^1. The generic one has degree123, bound123, and1^11,1^42,6^4,46^1. For typeIV the generic determinant has degree234, bound288, and1^36,1^54,6^1,6^1,30^2,72^1. All factors pass the same exact positivity test. The proof in TYPES34_PROOF.md and its rational reconstruction cover C1=0 separately, both L1=0 and L2=0 separately, and the case r1=0 without division by r1. In each exceptional IV branch the degree6 M3 numerator already never vanishes; the degree8 M4 certificate is an additional check. The two forced integer cases in the special pattern give the nonzero exact derivatives stated above.

A common finite root annihilates a fixed formal-degree Sylvester determinant. Its nonzero value therefore excludes all the necessary equations at that parameter, including a drop in a leading coefficient. For the linear/cubic pivot, the universal identity b0A^3-b1BA^2+b2B^2A-b3B^3 is proved by formal determinant expansion in six variables and checked at A=0 as well. Symbolic cancellation of A^3 b(-B/A) was only a discovery tool; the polynomial identity, rather than pointwise division, supplies validity at A=0. The first discovery sign error was caught at check40, corrected by this exact identity and followed by a complete rerun. An exact2-check comparison confirms that all other scientific certificate data are unchanged. The failure and original data remain archived.

The complete67-partition enumeration now uses the real-node parity and two-quadratic lemmas as well as the other inherited exclusions. The corrected16 surviving partitions match the five typeI, eight typeII, typeIII, typeIV and special reductions bijectively. The partition proof gives the finite recursion argument and each discarded case's mathematical reason; integer arithmetic is only bookkeeping for those proved implications. The initial omission of two rules and expected-list typo were caught by the first108-check gate and are retained in its failure archive.

Consequently every possible d=19 partition is excluded. Together with the independently reviewed lower-degree result275, every nonzero identity in the specified finite auxiliary polynomial axis class has odd d>=21 and P=n+d/2>=23/2. These are necessary conditions only; existence at the bounds is not proved. None of the hypotheses used here holds automatically for an arbitrary smooth nonpolynomial full-plane profile, so this result does not decide SettingIII. The primary endpoint remains UNRESOLVED.
