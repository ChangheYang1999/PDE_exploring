# Reciprocal weight-elimination review and exact relaxed supremum intervals

Written 2026-10-29T15:20:23.104852+00:00 before code. This result accepts the new algebraic part of
T2's reciprocal review of T4-462. T2 originated the earlier WU3 numbers;
its agreement on those original numbers is not independent evidence.

## Statement and exact hypotheses

Use the real S1 weighted Sobolev norm and its TB variant from the frozen
T4-462 proof: X(h)^2=P^2+w1*a_h^2+w2*b_h^2, or replace b_h^2 by
E0^2=b_h^2+(20/21)||Lambda^-1 J^s h||2^2. Here J=(1-Delta)^(1/2),
omega=(1+4r^2)^(2/5), P=||omega D2J^s h||2,
a_h=||DJ^s h||2, b_h=||J^s h||2 and0<s<=1/1024. The domain is the
completion of compact smooth S1 functions for that norm. Both norms
satisfy X(h)>=sqrt(w2)||h||2. Retain the complete original hypotheses
on the selected constants C>=K and cU>=v, the positive high margin
mu-C*s-cU*r/sqrt(s)>0 and the positive semidefinite matrix

 G=[[m2-mu,-O,-5],[-O,w1(m1-mu)-40,-3w1],
    [-5,-3w1,w2(beta-mu)]], O=347/10,

with0<m2<m1,beta>m2,w1>=2,w2>=1 andmu>0. Exact values of all seven
(m2,m1,beta) rows are frozen in data/parameters.json. Put
k=39068/100<K andu=15871/10000<v. For0<=mu<=m2 define

 f(mu)=4mu^3(beta-mu)(m2-mu)(m1-mu)^2 /
        [27k u^2{1440(m2-mu)+(6O+5(m1-mu))^2}].             (1)

The denominator is strictly positive on this whole interval. Every
admissible correction satisfies||h||2^2<f(mu), as proved in T4-462.
For each row take the exact rational mu_0 obtained from its saved
8-decimal argmax_mu string, without treating it as an exact maximizer.
Set q=f(mu_0) andepsilon=1/10000000. The claim checked here is

       q <= max_(0<=mu<=m2) f(mu) < q(1+2epsilon).          (2)

Consequently sqrt(q)<=sqrt(max f)<sqrt(q)(1+epsilon).
The seven resulting six-significant-digit rounded displays are
3.34629e-6,4.02421e-6,5.07475e-6,6.13623e-6,7.58412e-6,
4.07386e-6,4.10620e-6. The original rigorous WU3 ceilings remain
unchanged; this is verification of the new supremum assertion, not
new evidence for the full PDE scheme. All rational q, polynomial
coefficients, partition leaves and directed intervals will be saved.

## Weight elimination and sign audit

Set p=m2-mu, a=m1-mu,c=beta-mu,E=40p+O^2,z=pa*w1-E.
Positive semidefiniteness forcesp>0 andz>0: ifp=0 the nonzero O
contradicts its principal minor; ifz=0 the determinant is
-9p*w1^2-30O*w1-25(a*w1-40)<0. Thus0<mu<m2 andallp,a,c>0.
Direct determinant expansion gives

 det G=w2*c*z-[9p*w1^2+(30O+25a)w1-1000].

Afterw1=(z+E)/(pa), multiply the bracket bypa^2 to get
9z^2+(18E+30Oa+25a^2)z+(3E+5Oa)^2.
SetS=3E+5Oa>0. The exact square identity
9z+S^2/z-6S=(3z-S)^2/z>=0 therefore yields

       w2>=W(mu)=[1440p+(6O+5a)^2]/(cpa^2).               (3)

Atw1*=(2E+5Oa/3)/(pa),w2*=W(mu),z=S/3>0 anddetG=0.
The leading2x2 block is positive definite and its Schur complement
vanishes, soG is positive semidefinite. For all seven rows the exact
inequalities2O^2/(m2*m1)>2 and36O^2/(beta*m2*m1^2)>1 hold.
Sincep<=m2,a<=m1,c<=beta, these provew1*>2 andw2*>1 for every
0<mu<m2, not only a sampled near-maximizer. Thus(3) is the exact
minimum over the allowed weights for each such mu in these rows.
It does not assert attainability of the other analytic constants.

Maximizing s(mu-Cs)^2 over its positive domain gives4mu^3/(27C)
at s=mu/(3C). Applying the norm embedding and replacingC,cU by the
smaller positivek,u gives(1). Enlarging the original s range is safe
for an upper bound. The beta-monotonicity and bL conclusion remain
as in T4-462; none of the inverse, background or normalization
hypotheses is supplied by this finite scalar calculation.

## Proof and certification of the supremum bracket

The exact rational pointmu_0 lies in(0,m2), so continuity gives
max f>=q>0. The function extends continuously to both endpoints.
WriteN(mu)=4mu^3(beta-mu)(m2-mu)(m1-mu)^2 and
D(mu)=27k u^2[1440(m2-mu)+(6O+5(m1-mu))^2].
To prove the upper bound in(2), it suffices to prove the degree7
polynomialQ(mu)=q(1+2epsilon)D(mu)-N(mu)>0 on[0,m2].
The checker computes all coefficients exactly. Under mu=m2*t,
convert its power coefficientsd_j to Bernstein coefficients
b_i=sum_(j<=i)d_j*binom(i,j)/binom(7,j). Their basis functions
are nonnegative and sum to1. Positive coefficients prove strict
positivity on the closed interval. Exact midpoint de Casteljau
subdivision produces a finite partition; every leaf is also checked
by independent affine recomposition of the original polynomial.
Contiguous rational endpoints with first0 andlast1 prove coverage.
This gives the upper bound in(2) without using the peer's bisection
program, golden search, float values or its unsaved exact witness.

Because(1+epsilon)^2>1+2epsilon, square roots give the stated
relative interval. To certify a six-digit rounded displayd, check
(d-half_unit)^2<q andq(1+2epsilon)<(d+half_unit)^2 with exact
rational endpoints. This identifies the entire supremum interval
inside its decimal rounding cell. It does not call the displayed
decimal an exact supremum or a directed lower bound.

## Source and scope audit

The new Opus review independently confirms the closed-form elimination,
its equality case, necessary budgets and bL extension. Its original
WU3 source relationship is explicit. T2's symbolic identities are
read, not executed here. The own checker binds both review targets,
its52-check result and script, and uses its source decimalmu values
only as exact rational test proposals. Their provenance cannot affect
validity of(2). The raw sup_lower_witness string was formatted through
floating point; without a directed check it must not be consumed as
a rational lower certificate. This audit saves exact point andq data
and outward endpoint fractions. We do not reproduce the historical
leaf counts or the unsaved binary argmax, and make no such claim.

The supremum in(2) usesk=390.68,u=1.5871. It is not the different
relaxed problem using exactK,v, still less the full prescribed
weight-dependent commutator constants. All are upper relaxations of
the selected analytic scheme. The accepted exclusion ceilings and
all24 fixed-c weak witnesses are unchanged. No global optimality,
new inverse, candidate-existence or correction-distance claim follows.
Configured Opus5.5 collaboration is through the existing theory lane;
this lane cannot observe the model provider's actual identity.
