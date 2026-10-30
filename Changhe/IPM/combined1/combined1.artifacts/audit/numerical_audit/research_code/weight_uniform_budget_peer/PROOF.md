# Seven uniform necessary budgets and their finite certificate replay

## Exact theorem and scope

Let J=(1-Delta)^(1/2), omega(X)=(1+4|X|^2)^(2/5), and 0<s<=1/1024.
Use either X(h)^2=||omega D^2 J^s h||_2^2+w1||D J^s h||_2^2
+w2||J^s h||_2^2, or replace the last squared norm by
E0(h)^2=||J^s h||_2^2+(20/21)||Lambda^-1 J^s h||_2^2.
The functions are real on R2, with the S1 restrictions of the registered
scheme if that scheme is invoked. The ordered Cartesian Hessian defines
D^2. The space is the completion of compact smooth admissible functions
for this norm. Both norms satisfy X(h)>=sqrt(w2)||h||_2 by Plancherel.
No independent reweighting of the two E0 summands is considered.

Set O=347/10. Assume positive m2<m1, beta>m2, w1>=2, w2>=1, mu>0,
and the positive semidefinite matrix

 G=[[m2-mu,-O,-5],[-O,w1(m1-mu)-40,-3w1],
                              [-5,-3w1,w2(beta-mu)]].

Assume C>=K and cU>=v for the exact constants below, and r>=0 satisfies
mu-Cs-cU*r/sqrt(s)>0. Then X(h)<=r implies ||h||_2<b, for each row:

| m2 | m1 | beta | b |
| --- | --- | --- | --- |
| 1/2 | 9/10 | 2 | 33469/10^10 |
| 1/2 | 9/10 | 11/4 | 40249/10^10 |
| 61151/10^5 | 99116/10^5 | 2 | 50757/10^10 |
| 61151/10^5 | 99116/10^5 | 11/4 | 61373/10^10 |
| 61151/10^5 | 99116/10^5 | 4 | 37927/(5*10^9) |
| 1/2 | 9/10 | 1+c0 | 20373/(5*10^9) |
| 1/2 | 9/10 | 57/20 | 41069/10^10 |

Here c0=4076476460239181/2251799813685248. The three larger-floor rows
are hypothetical algebraic sensitivity bounds. Their floors are not
asserted certified for any profile. All seven conclusions are necessary
budget bounds, not inverse theorems or verified background hypotheses.
The numerical statement depends on the exact polynomial positivity
certificates checked below. Norm completion does not change the embedding.

## Elimination of the weights

Put p=m2-mu, a=m1-mu, c=beta-mu, q=a*w1-40. Positivity of G and
O>0 imply p>0, then a>0 and c>0 because beta>m2. The leading minor
gives p*q>=O^2. Equality would give determinant
-9p*w1^2-30O*w1-25q<0, so z=p*q-O^2>0. Put E=40p+O^2.
Direct determinant expansion yields

 det G=c*w2*z-[9p*w1^2+(30O+25a)w1-1000].

At w1=(z+E)/(pa), the bracket multiplied by pa^2 becomes
9z^2+(18E+30Oa+25a^2)z+(3E+5Oa)^2.
This identity follows by expansion and E-40p=O^2. With S=3E+5Oa>0,
9z+S^2/z>=6S follows from (3z-S)^2/z>=0. Thus

 w2 >= [1440p+(6O+5a)^2]/(c*p*a^2)=W(mu).

All divisions are by positive quantities. At z=S/3 the identity is an
algebraic equality. No attainability of all analytic constants is inferred.
The lower weight restrictions can only reduce the feasible set.

## Elimination of s and finite positivity

The high margin and norm embedding imply
||h||_2<sqrt(s)(mu-Cs)/(cU*sqrt(w2)). Its squared maximum over s>0
is4mu^3/(27C*cU^2*w2), at s=mu/(3C). Dropping the upper restriction
on s is safe for a necessary upper bound. Let k=39068/100 and
u=15871/10000. The directed constant checks establish K>k and v>u.
Consequently

 ||h||_2^2 < 4mu^3(beta-mu)(m2-mu)(m1-mu)^2 /
   [27*k*u^2*(1440(m2-mu)+(6O+5(m1-mu))^2)].

For each exact row and b it suffices to prove positivity on[0,m2] of
Q(mu)=27*k*u^2*b^2*(1440(m2-mu)+(6O+5(m1-mu))^2)
 -4mu^3(beta-mu)(m2-mu)(m1-mu)^2.
The independent checker reconstructs all eight power coefficients.
On each peer-proposed rational interval t in[A,B], where mu=m2*t,
it substitutes mu=m2*(A+(B-A)y) exactly. If d_j are the resulting
power coefficients, its degree-seven Bernstein coefficients are
b_i=sum_(j<=i)d_j binom(i,j)/binom(7,j). The nonnegative Bernstein
basis sums to1. Strict positivity of every coefficient therefore proves
Q>0 on that interval. Exact adjacency and endpoints prove full coverage
of[0,1]. The peer's partition is proposed data; no subdivision algorithm
or peer arithmetic is trusted or executed. The saved coefficients must
also agree exactly. This proves each stated strict upper bound.

## Exact constants

Set sigma=1/1024, M=sqrt(pi)*Gamma((1-sigma)/2)/2,
W=8sqrt(5)*6^(-3/5)/5, k1=M+8/5, cr=3M/2+32/15,
c8=1+3pi*W/4, dtop=1+pi*W/2, and
K=2dtop+6c8+24(cr+2k1)+32k1.
Set q0=1/(2sqrt(pi)), ps=2^sigma*sqrt(1+sigma)/(2sqrt(pi)),
P0=ps*(1+W*M*sigma)+W*M*sigma/(2sqrt(pi)), and
v=(4/5)q0+q0*(1+4W*M*sigma)+(19/5)P0.
All these are evaluated by outward Arb arithmetic. Their values are
compared with the saved peer containing balls and the exact rational
lower constants k and u. The restriction C>=K,cU>=v is an explicit
hypothesis on selected uniform estimates, not a universal lower bound
on every possible sharper commutator or velocity estimate.

## Unweighted bL and the accepted snapshot witnesses

For the stated unweighted signed low estimate assume
beta_L<=1+c-theta-kappa, theta=ess sup(|grad rho|-rho_y)/2 and
kappa=||K_operator||_HS. These two quantities are nonnegative.
At c=c0 this gives beta_L<=1+c0. If9/5<c<37/20 it gives
beta_L<57/20. Increasing beta adds the nonnegative matrix
w2*(beta_new-beta_old)e3e3^T. Every original feasible point remains
feasible at the enlarged value, even when the original beta_L<=m2.
Thus the two final rows cover all positive rates from this unweighted
margin with the same fixed top floors and uniform constants.

The accepted N4-390 result supplies strict fixed-c distance>1/1000
for each of the24 immutable snapshots002 through026 except011,
with its complete weak-certificate, canonical-velocity and correction
equation hypotheses. Each applicable original-floor budget above is
less than1/1000. Therefore none of those registered balls contains a
stationary correction to those exact profiles at c0. The largest bL
budget is below1/1000 by a factor greater than243. This composition
uses accepted complete residual integrals; it does not rerun them.
The bound for varying c does not extend the fixed-c snapshot witnesses.

The conclusion excludes neither non-L2 corrections nor other weights
in the low equation, separately reweighted E0, improved constants,
other matrix floors or dyadic spaces. No global margin is supplied for
an unchecked candidate. Samples near a relaxed algebraic maximum do
not establish near-optimality of a full scheme whose C depends on the
weights. The new Opus review's finer supremum displays are outside this
finite replay unless separately checked.

## Sources and verification

Read and freeze the full T4 proof, exact parameters, result, code as text,
and the full Opus T2 reciprocal review and its result. Bind the previously
accepted own390 witness and scalar tuple evidence. Verify all selected
stored source hashes before and after the finite replay. The certificate
is OPEN until the checker succeeds; a hash alone is not mathematical
validation. No foreign implementation is imported or executed.
