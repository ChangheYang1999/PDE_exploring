# Exact brackets for the scalar family ceilings

## Statement and scope

This result audits T2 handoff BE and the frozen37-check family-ceiling
calculation. It concerns necessary radius restrictions in the registered
fixed-c real S1 scalar charts. It does not prove an inverse, certify a
reference profile or enlarge a sufficient existence region. Let s>0,
mu>0, C>0, cU>0 and W2>0. Suppose a chart norm controls
sqrt(W2)*||h||_L2, its radius is r, and its required high rate satisfies

 mu-C*s-cU*r/sqrt(s)>0.                              (1)

All L2 norms use Lebesgue measure on R2. For the Bessel norms this control
follows from s>=0 and unitary Plancherel. Extra Hessian, derivative and
negative-norm terms are nonnegative. The scalar norm weights and rate
parameters are those of the frozen theory_v01 and theory_v03.

Then every correction in such a ball satisfies ||h||_L2<b(mu,C,cU,W2),
where

 b = (2*mu/3)*sqrt(mu/(3*C))/(cU*sqrt(W2)),
 b^2 = 4*mu^3/(27*C*cU^2*W2).                       (2)

For the following parameters, the supremum in (2) lies strictly between
the given rational endpoints. The endpoints are part of the exact
statement; decimal notation denotes rational numbers.

| Family | mu | C | cU | sqrt(W2) | Lower | Upper |
| --- | --- | --- | --- | --- | --- | --- |
| FW-A2-Db | 1/10 | 4800 | 5 | 512 | 6.8625e-8 | 6.8626e-8 |
| TB-rebal | 297/1000 | 4800 | 5 | 512 | 3.5125e-7 | 3.5126e-7 |
| bL, betaL=1 | 151/500 | 397 | 8/5 | 1024 | 1.9567e-6 | 1.9568e-6 |
| bL, betaL=7/5 | 359/1000 | 397 | 8/5 | 1024 | 2.5361e-6 | 2.5362e-6 |
| sharpw | 97/250 | 397 | 8/5 | 1024 | 2.8495e-6 | 2.8496e-6 |
| sharp | 259/1000 | 401 | 8/5 | 512 | 3.0926e-6 | 3.0927e-6 |
| TB-sharp | 297/1000 | 402 | 8/5 | 512 | 3.7929e-6 | 3.7930e-6 |

Thus all seven scalar bounds are below3.7930e-6. The old statement that
TB-rebal3.5125e-7 is rounded upward is false. It is below the supremum;
3.5126e-7 is a valid upward replacement. For that family specifically,

 1 < b/(3.5125e-7) < 1.0000136.                      (3)

For the original graded family, assume the component norm and positive
top margin in source/graded_PROOF.md. Then its necessary L2 bound is

 bG=50/(651*sqrt(28248)),
 45697/10^8 < bG < 25/54684.                         (4)

The finite proof below verifies these strict inequalities by integer
arithmetic after squaring positive quantities. Arb evaluation is used
only for comparison with the independently computed peer enclosures.

## Proof of the scalar supremum

Equation (1) implies

 ||h||_L2 <= r/sqrt(W2)
           < (mu-C*s)*sqrt(s)/(cU*sqrt(W2)).

Set u=sqrt(s). The numerator is f(u)=mu*u-C*u^3. Its derivative
mu-3*C*u^2 is positive for0<u<sqrt(mu/(3*C)), zero at that point,
and negative afterward. Its unique positive maximum is therefore
(2*mu/3)*sqrt(mu/(3*C)). This proves (2), without asserting that all
other chart conditions can be met at the maximizing parameter. Since
all bracket endpoints are positive, a<b<z is equivalent to
a^2<4*mu^3/(27*C*cU^2*W2)<z^2. Each expression is rational. Substitution
of the seven parameter rows proves their brackets and (3). Comparing
each square with (3.7930e-6)^2 proves the common ceiling directly.

## Proof for the original graded family

In the notation of source/graded_PROOF.md, n^2=r2^2+2*r1^2+r0^2
controls ||h||_H^(2+s)^2 and hence ||h||_L2^2. Positivity of

 1/2-4708*s-(217/50+(1049/5)*s)*n/sqrt(s)

implies n<(50/217)*sqrt(s)*(1/2-4708*s). Maximizing the cubic in
sqrt(s) gives s=1/28248 and maximum50/(651*sqrt(28248)). Squaring the
positive endpoints of (4) proves both strict rational comparisons.
This is an upper restriction, not a proved attainable box radius.

## Consequences and limits of the rounding repair

The existing scalar distance exclusions that use the largest ceiling
3.7930e-6 are unchanged. The original graded exclusions use25/54684
and are unchanged. No division by the incorrectly rounded TB-rebal
number is needed for either conclusion.

The endpoint certificate audited in T4-443 has cutoff K(beta) of the
form A*beta^(-a)-B0, where A>0, a=delta/(-q-1)>0 and B0>=0. Its
derivative is negative. Since the exact TB-rebal ceiling is larger
than3.5125e-7, an upper bound for K at that printed radius remains
an upper bound at the exact ceiling. A lower bound need not remain
valid. In particular the old two-sided row interval is not an enclosure
at the exact radius. The already proved certificate obstruction from
3.5125e-7 upward, and the current-list full CI cap below2.66323e-8,
therefore survive this repair. The two small Db targets still have the
separate OPEN status stated in T4-443 and T4-452.

For a distance factor, write p=3.5125e-7, q=D/p and R=b/p. Equation(3)
gives D/b=q/R>q/1.0000136. Thus a displayed lower factor f is retained
if f<=q/1.0000136. If the original positive factor f is rounded down
and has at most four significant digits, let u be its last displayed
unit. Then f/u<=9999. Since0.0000136*9999<1,

 (f-u)*1.0000136 < f <= q,

so f-u remains a strict lower factor at the exact ceiling. This is a
general rounding lemma; the historical O3 and C4 ratio tables are not
individually accepted by it. Their actual entries need a separate audit.

The newly established sharpw and TB-sharp brackets discharge the bracket
hypothesis isolated by T4-443 repair5 for those families. They also supply
the bracket premises referenced by T2 for factors R2 and R3, but this
result alone does not independently audit the factor formulas. The
printed-target and exact-family factors should remain separately labeled.

## Evidence and verdict

All13 frozen source files are recorded in data/input_sources.json. The
source rates, weights, peer program and handoff BE were inspected.
The checker reads copied data only and executes no peer code. It binds
the previously accepted reach and repair results to their proofs, checks
the eight exact brackets and (3), and verifies the derivative and cubic
identities using rational coefficients. No spatial integration is repeated.

CONFIRMED: the six downward-to-upward scalar brackets other than TB-rebal,
the repaired TB-rebal bracket, the graded bracket, the relative correction
and the scoped persistence consequences above. REFUTED: the historical
claim that3.5125e-7 bounds the TB-rebal family from above. No inverse,
attainability or existence conclusion is added.
