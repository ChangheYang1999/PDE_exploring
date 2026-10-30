# Exact-constant budget displays and directed display successors

## Statements and dependencies

This is a finite audit of T2 handoff BN and the two incorrect delta
approximations in published theory_v08. It changes no candidate verdict.
All numbers used as proof inputs are exact JSON rationals or containing
Arb intervals. A rounded display is never used as an exact extremum.

For the seven triples (m2,m1,beta) of T4-468, let O=347/10,
k=39068/100 and u=15871/10000. Put p=m2-mu, a=m1-mu, c=beta-mu and

 B_(k,u)(mu)=4mu^3 c p a^2/[27 k u^2(1440p+(6O+5a)^2)]

on 0<=mu<=m2. All triples obey 0<m2<m1 and beta>m2, so this is
continuous with a positive denominator. Write S_(k,u)=sqrt(max B_(k,u)).
The exact rational lower and upper squares q and Q in accepted T4-468
satisfy 0<q<=S_(k,u)^2<Q. These proved brackets are the dependency;
this audit neither resamples a maximizer nor repeats the polynomial proof.

Define sigma=1/1024, M=sqrt(pi)Gamma((1-sigma)/2)/2,
W=8sqrt(5)6^(-3/5)/5, k1=M+8/5, cr=3M/2+32/15,
c8=1+3pi W/4, dtop=1+pi W/2, and

 K=2dtop+6c8+24(cr+2k1)+32k1.

Let q0=1/(2sqrt(pi)), ps=2^sigma sqrt(1+sigma)/(2sqrt(pi)),
P0=ps(1+WM sigma)+WM sigma/(2sqrt(pi)), and

 v=(4/5)q0+q0(1+4WM sigma)+(19/5)P0.

For B_(K,v) replace k,u by K,v in the displayed rational function.
All other parameters and the interval for mu stay fixed. The exact rule is

 S_(K,v)=sqrt(k/K)(u/v) S_(k,u).                         (1)

Its seven six-significant-digit rounded values are respectively
3.34624e-6,4.02414e-6,5.07467e-6,6.13613e-6,7.58399e-6,
4.07379e-6,4.10613e-6, in the exact row order of T4-468. This claim is
confirmed only if the whole rescaled containing interval lies strictly
inside the decimal rounding cell. The factor in (1) is below1 and above
1-1.7e-5. Neither rounded list denotes the supremum for the complete
weight-dependent PDE prescription.

For the common canonical profile parameter
c0=4076476460239181/2251799813685248, the exact exponent is

delta=1-1/c0=1824676646553933/4076476460239181.

Its decimal prefix is0.44761123101073246431935044179100532374519968543159.
The two displays0.44764... in theory_v08 are incorrect as decimal prefixes
and as nearest five-decimal roundings. The exact symbolic delta is
unchanged; kappa=4+delta and D=c0 kappa=5c0-1 are also checked exactly.

Finally, the 24 new root_lower and stored_lower displays and eight scalar
upper displays in T2 the review of T4-459 revision2 are directed as labelled.
They refer to the same source-bound weak witnesses and family tuples as
T4-459. The first new list is a lower bound, not an approximation obtained
by rounding to nearest. The finite audit retains the previous source
certificates and changes no weak inequality, radius or exclusion.

## Proof of the constant rescaling and rounding

For every mu, B_(K,v)=k u^2 B_(k,u)/(K v^2). The multiplier is a
positive constant independent of mu. Therefore taking the maximum and
then the positive square root proves(1). In particular its maximizing
mu values and its equality weights are unchanged. Multiply the exact
rational bracket of T4-468 by the containing squared factor, or take
containing square roots first. Directed Arb evaluation of the explicit
Gamma and elementary expressions gives a containing factor interval;
its consistency with the accepted T4-462 enclosures is checked.

If L<=S<=U and d-h<L<=U<d+h, every possible S has nearest rounding d
at half-unit h. All seven quantities are between1e-6 and1e-5, so their
six-significant-digit half-unit is1/(2*10^11). These are exact rational
cell comparisons. Stored endpoints in this audit are independently rounded
outward to exact fractions. T2's factor and rounded values are checked
against them. Its twelve-significant-digit printed enclosure endpoints
are treated as approximate summaries, not imported as directed bounds.

The formulas of T4-462 place these scalar inequalities in context. For
real whole-plane corrections h, its weighted norm has
X(h)^2=P^2+w1 a_h^2+w2 b_h^2, where
P=||(1+4r^2)^(2/5)D2 J^s h||2, a_h=||D J^s h||2,
b_h=||J^s h||2, J=(1-Delta)^(1/2), and0<s<=1/1024.
The TB variant replaces b_h^2 by
E0(h)^2=b_h^2+(20/21)||Lambda^-1 J^s h||2^2 with a single weight.
Its domain is the norm completion of compact smooth real S1 functions.
Both obey X(h)>=sqrt(w2)||h||2. The necessary budget assumes w1>=2,
w2>=1, C>=K, cU>=v, mu-C s-cU r/sqrt(s)>0 and the positive
semidefinite matrix with rows
(p,-O,-5),(-O,w1 a-40,-3w1),(-5,-3w1,w2 c).
T4-462 then gives ||h||2<S_(k,u); choosing the algebraic C=K,cU=v
instead gives S_(K,v). The true prescription can impose larger C,
further conditions on the weights, and separate inverse, background,
normalization and range hypotheses. The present rescaling proves no
attainability for that prescription and supplies none of those hypotheses.

## Proof of the directed weak-root and family displays

For each of the 24 canonical fixed-c snapshots002to026 except011,
accepted T4-459 supplies exact positive I,D,H such that every admissible
real L2 correction with m=||h||2 satisfies I<=D m+H m^2. The canonical
velocity includes the local contact term. The correction is a real
whole-plane distributional stationary correction at the snapshot's c;
no trace condition is used. Normalizing it only restricts the class.
The 24 input certificates establish I-D/1000-H/10^6>0. Therefore the
positive root of H x^2+D x=I exceeds1/1000 and is a necessary lower
bound for m. No changed-c or differently weighted exclusion follows.

Let S=2^200 and let z be the integer with
z^2<=S^2(D^2+4HI)<(z+1)^2. Then

 l=(z/S-D)/(2H)

is a rational lower bound for that root. For each new root_lower_exact
we independently verify that S(2H l+D) is that nonnegative integer,
using the two exact squared inequalities rather than invoking T2's
root routine. Positivity is checked separately. A displayed lower d
with decimal unit u0 is a directed floor precisely when
d<=l<d+u0. The identical test is applied to every stored source lower
endpoint, recovered from its existing containing source certificate.
No numerical integration or source projection is repeated.

For a scalar family with tuple(mu,C,cU,sqrtW2), its accepted squared
ceiling is b2=4mu^3/(27 C cU^2 sqrtW2^2). A seven-significant-digit
upper display d is correct if (d-u0)^2<b2<=d^2 and d-u0>=0. These
exact rational tests verify the eight changed displays, including the
three previous upward-rounding defects. The common upper3.7930e-6,
the original graded bound and all exclusions remain as previously proved.

Every old proof/result and source revision is hash-bound. Foreign scripts
are inspected as text and not executed. Configured Opus5.5 collaboration
is through T2's BN successor and the existing theory lanes; actual provider
identity is unobservable here. No existence, new inverse, optimizer
completeness or best-candidate claim is made.
