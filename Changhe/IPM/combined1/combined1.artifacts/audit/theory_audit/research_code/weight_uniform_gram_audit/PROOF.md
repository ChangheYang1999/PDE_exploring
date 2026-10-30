# Weight-uniform necessary budgets for two fixed Gram schemes

Written at 2026-10-29T14:56:10.457815+00:00 before the checker. This independently audits T2's WU and WU3
and gives an exact minimization of the weight w1.

## Statement, spaces and hypotheses

All functions are real on R2. Lebesgue L2 uses the Euclidean component norm.
For 0<s<=2^-10 let J=(1-Delta)^(1/2), omega=(1+4|X|^2)^(2/5), and

 P=||omega D^2 J^s h||2, a_h=||D J^s h||2, b_h=||J^s h||2.

D^2 is the ordered Cartesian Hessian. Either take the completion of compact
smooth S1 functions under X^2=P^2+w1*a_h^2+w2*b_h^2, or the TB version
X^2=P^2+w1*a_h^2+w2*E0(h)^2 with its original combined low component
E0(h)^2=b_h^2+(20/21)||Lambda^-1 J^s h||2^2. In either case the only norm fact
needed here is X(h)>=sqrt(w2)||h||2. The TB version keeps E0 as one
component with one weight. No independent reweighting of its two summands
is covered. Normalization, when required, restricts to a subset of this
ball and cannot enlarge this necessary budget.

For positive m2<m1 and beta>m2 let mu>0, w1>=2, w2>=1, and suppose

 G(mu)=[[m2-mu,-O,-5],[-O,w1*(m1-mu)-40,-3*w1],
        [-5,-3*w1,w2*(beta-mu)]] is positive semidefinite, O=347/10. (1)

Let K and v be the exact constants defined below. Require C>=K and
cU>=v. Consider a radius r>=0 with the strictly positive high margin

                    mu-C*s-cU*r/sqrt(s)>0.                    (2)

The two original rows have (m2,m1,beta)=(1/2,9/10,2) and
(1/2,9/10,11/4). Under (1)-(2), every h with X(h)<=r satisfies

 ||h||2 < 33469/10^10   or   ||h||2 < 40249/10^10,             (3)

respectively. These are 3.3469e-6 and 4.0249e-6. Relative to the exact
registered sharpw and TB-sharp family ceilings, their upper factors are
1.1746 and1.0612. The previously accepted candidate007 fixed-c necessary
L2 floor d=4769166867/10^12 exceeds them by factors at least1424.9 and
1184.9. The first two bounds imply T2's weaker WU upper bounds.

Three purely hypothetical rows replace (m2,m1) by(61151/10^5,99116/10^5).
For beta=2,11/4,4 their respective bounds are50757/10^10,61373/10^10,
37927/(5*10^9). These are conditional algebraic sensitivity bounds;
these matrix floors are not certified for007. All exact parameters,
upper gains and lower distance factors are in data/parameters.json.

This theorem is a necessary budget bound. It constructs no high or low
inverse and verifies no background hypotheses. It cannot exclude a
correction class which does not embed into this L2 ball. The actual IPM
closure additionally needs the accepted maximal realization, domain,
source range, canonical velocity and normalization hypotheses; none is
removed by this calculation. C>=K and cU>=v are explicit restrictions
on the selected uniform estimates, not lower bounds on every possible
valid commutator or velocity constant.

## Exact elimination of both weights

Positive semidefiniteness and O>0 imply p=m2-mu>0. Put a=m1-mu>0,
c=beta-mu>0, q=a*w1-40, E=40p+O^2. The leading2x2 minor implies
pq>=O^2. Equality is impossible: the determinant in that case is
-9p*w1^2-30O*w1-25q<0. Hence z=pa*w1-E=pq-O^2>0.

Direct determinant expansion gives

 det G=w2*c*z-[9p*w1^2+(30O+25a)*w1-1000].                  (4)

Substitute w1=(z+E)/(pa). The numerator bracket times pa^2 is

             9z^2+(18E+30O*a+25a^2)z+(3E+5O*a)^2.          (5)

To check the last coefficient, expand it and use E-40p=O^2; the cross
coefficient30O equals1041. Dividing (4)-(5) by the positive denominator
and using9z+S^2/z>=6S, S=3E+5O*a>0, yields the exact lower bound

        w2 >= [1440p+(6O+5a)^2]/(c*p*a^2) =: W(mu).         (6)

Equality in this weight minimization is attained algebraically at
z=S/3 and w1=(2E+5O*a/3)/(pa), w2=W(mu). This statement is about(1),
not attainability of all other analytic constants or a PDE solution.
The leading2x2 block is then positive definite and its Schur complement
is zero, so G is positive semidefinite. If the separate lower weight
constraints exclude this algebraic point, (6) still remains necessary.

This derivation confirms T2's determinant formula and its minimization,
without repeating its20000-cell minimization in w1. It also avoids any
loss from the separate2x2-minor relaxation of WU.

## Elimination of s and an exact polynomial certificate

From(2) and the norm embedding,

 ||h||2 <= r/sqrt(w2)
          < sqrt(s)*(mu-C*s)/(cU*sqrt(w2)).                  (7)

The cubic in sqrt(s) is maximized at s=mu/(3C). Thus its squared
supremum over all s>0 is4mu^3/(27C*cU^2*w2). Enlarging the allowed s
range is safe for this upper bound. Replacing C,cU by smaller positive
constants k=39068/100 and u=15871/10000 and then using(6) gives

 ||h||2^2 < 4mu^3*c*p*a^2/[27*k*u^2*(1440p+(6O+5a)^2)].    (8)

For a proposed bound b>0, it suffices to show on0<=mu<=m2 that

 Q_b(mu)=27*k*u^2*b^2*(1440p+(6O+5a)^2)
                         -4mu^3*c*p*a^2 > 0.               (9)

This is a degree7 polynomial with exact rational coefficients. The
checker reconstructs(9) from the parameter JSON, substitutes mu=m2*t,
and converts it to Bernstein form on[0,1]. For a polynomial
sum_j d_j t^j of degree n, its Bernstein coefficients are
b_i=sum_(j<=i)d_j*binom(i,j)/binom(n,j). The Bernstein basis polynomials
are nonnegative and sum to1, so positive coefficients imply positivity
on the entire closed interval. At a midpoint the de Casteljau averaging
recurrence gives exact rational coefficients for both halves. Repeated
subdivision produces a finite dyadic partition whose every coefficient
is positive. Each leaf, its interval and coefficients are saved in JSON;
the checker independently converts the original power polynomial on
every leaf and checks equality. Endpoint coverage, no gaps and no overlap
are checked exactly. Sampling is not used to certify(9).

## Constants and source comparisons

Put sigma=1/1024, M=sqrt(pi)*Gamma((1-sigma)/2)/2,
W=8sqrt(5)*6^(-3/5)/5, k1=M+8/5, cr=3M/2+32/15,
c8=1+3pi*W/4 and dtop=1+pi*W/2. The unchanged uniform top entry is

 K=2dtop+6c8+24(cr+2k1)+32k1.                              (10)

Put q0=1/(2sqrt(pi)), ps=2^sigma*sqrt(1+sigma)/(2sqrt(pi)),
P0=ps*(1+W*M*sigma)+W*M*sigma/(2sqrt(pi)), and

 v=(4/5)q0+q0*(1+4W*M*sigma)+(19/5)P0.                     (11)

These are the constants stated in T2-R2/R3 and WU. Directed Arb arithmetic
checks K>39068/100 and v>15871/10000. The hypotheses retain the same
uniform constants evaluated at sigma; an improved s-dependent estimate
would require a separate analysis. Exact registered family ceilings use
b_fam^2=4mu0^3/(27C*cU^2*w2) with the accepted tuple JSON. All reported
gain upper bounds are checked by squared rational comparison, and all
candidate007 lower factors by exact rational division. No rounded decimal
is substituted for an exact registered ceiling.

## Scope of sharpness and verification

The WU3 upper bounds are rigorous if this finite checker succeeds. The
T2 sampling run is a FLOAT observation at exactly positive definite
weight points. Its budgets use lower approximations to K and v; those
values by themselves are not rigorous lower bounds on the true maxima.
Furthermore choosing C=K and cU=v is an algebraic relaxation. The actual
T2-R3 commutator prescription includes weight-dependent off-diagonal
terms and typically has C>K. Therefore a claim of sharpness for the full
analytic scheme does not follow from that sample. The phrase close to
the true suprema must refer to this relaxed algebraic budget problem,
with its FLOAT qualification, unless separate feasible full constants
are checked. This audit does not certify such sharpness or optimality.

The input manifest freezes the source formulas, claims, scripts (read as
text only), results, the accepted family bracket evidence and007 weak
floor. Hash equality certifies these copies, not unobserved historical
execution. No foreign code, candidate integral or optimizer is executed.
The exact AM-GM elimination is a new independent simplification and is
submitted to the existing Opus theory lanes for reciprocal review.

Pre-code correction: the first draft omitted the TB coefficient20/21 in E0. The source T2_routes_v01 section2 fixes it. Only E0>=b_h is used in this proof; no numerical claim depended on the omitted coefficient. The first draft is retained in verification.


## Extension to every unweighted bL margin

This extension was written before the checker, at 2026-10-29T14:58:43.249237+00:00. The
unweighted signed low estimate has beta_L <= 1+c-theta-kappa, with

 theta=ess sup (|grad rho|-rho_y)/2 >=0,
 kappa=||K||_HS >=0.

The first sign follows pointwise from |grad rho|>=rho_y. The second is
a norm; in its explicit formula both log(2)-1/2 and 3log(2)-2 are
positive. The background assumption 9/5<c<37/20 therefore implies
beta_L<57/20. At the common snapshot parameter c0 it gives
beta_L<=1+c0=6328276273924429/2251799813685248.

Raising beta increases G by the positive semidefinite diagonal matrix
w2*(beta_new-beta_old)*e3*e3^T. Thus every admissible old point remains
admissible at beta_new. Applying (9) at 57/20 bounds all positive beta_L
allowed by this unweighted margin, even when beta_L<=m2: feasibility
at the enlarged beta is all that is used. The same applies at 1+c0.
The respective ceilings, in that order, are 4.1069e-6 and 4.0746e-6.
Both are below 1/1000 by a factor greater than243. Together with the
accepted T4-459 fixed-c weak inequalities, all24 snapshots002--026
except011 are outside every such bL ball. This conclusion fixes c=c0;
the upper budget formula alone also holds for other c satisfying(A).
It does not extend the fixed-c weak exclusions to those other c.

The ceiling gains over sharpw are at most1.4413 and1.4299; the007
floor factors are at least1161.2 and1170.4; the old conservative H18
minimum1232449584/10^12 gives factors at least300.0 and302.4.
The checker verifies these rational comparisons and independently
replays every strict I-D/1000-H/10^6>0 identity in the accepted H18
result. The underlying field integrals remain cited dependencies.

This extension uses exactly the registered floors1/2,9/10 and the
unchanged uniform commutator and velocity prescription. It does not
cover the weighted L2(w^2) alternative (B-L2-w), whose transport weight
can increase its margin above1+c, independent weights inside E0,
improved background constants, or other top floors. The global margin
hypothesis itself is not certified for every snapshot by this argument.
