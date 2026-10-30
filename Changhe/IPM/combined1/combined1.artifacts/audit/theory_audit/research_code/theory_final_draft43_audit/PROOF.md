# Independent audit of THEORY_FINAL draft 43

## Statement and precise scope

This audit concerns the 1933-line draft generated at 14:09Z on
29 October 2026, SHA256
`a3b59ce9cedb7c9c3307c4bff1fac47af57bfa076717c1d426dfc487c2218c21`.
Its baseline is the independently audited 1897-line draft 39,
SHA256 `28f5f6ce4bd47463335e8b76b07bdfb53a1c6445bd9e1f0552a81dbb1ae5b97b`.
All 48 changed word blocks have been read. The claim is that the changed
mathematical assertions are valid with the hypotheses below, that the
23 numerical rows use conservative factors, and that the specific
publication repairs requested in T4-453 and T4-454 are made. This is not
a second complete audit of every unchanged claim or the closure matrix.

The scalar chart fixes the exponent c, its leading far-field data and
the origin normalization c[h]=0. Functions and corrections are real,
S1-symmetric on R2. The velocity is the canonical divergence-free IPM
velocity, including its local/contact contribution. Lebesgue measure is
used, and Hessian norms count ordered Cartesian derivatives. Write
J=(1-Delta)^(1/2), omega=(1+4|x|^2)^(2/5), and

 X_(s,w)(h)^2 = ||omega D^2 J^s h||_2^2
                  + w1 ||D J^s h||_2^2 + w2 ||J^s h||_2^2.

The correction space is the normalized S1 subspace on which this norm is
finite; s>=0 and w1,w2>0. In particular X_(s,w)(h)>=sqrt(w2)||h||_2.
The conditional existence results still require their signed background
margin, coefficient hypotheses, operator realization and nonlinear
estimates, as specified in source/draft39_PROOF.md and its predecessors.
No coefficient computation here supplies a missing inverse. A scaling
direction with a nonintegrable leading tail is outside this L2 chart.
The original graded box and the decaying-weight dyadic space are distinct;
no unproved comparison with L2 is used for the latter.

## 1. Radius ceilings and the distance table

For each scalar family with positive rate

 mu - C s - cU r/sqrt(s) > 0,

a correction in the radius-r ball satisfies

 ||h||_2 <= r/sqrt(w2)
           < (mu sqrt(s)-C s^(3/2))/(cU sqrt(w2)).

The numerator has unique positive maximum at s=mu/(3C): its derivative
in u=sqrt(s) is mu-3C u^2. Hence the square of its L2 supremum is

 b^2 = 4 mu^3/(27 C cU^2 w2).

The seven exact rational rows in data/bracket_parameters.json give these
suprema. Comparing rational squares proves that all seven are below
3.7930e-6, sharpw is below 2.8496e-6, and

 3.5125e-7 < b_TB-rebal < 3.5126e-7.

The original graded argument, already proved in source/brackets_PROOF.md,
gives bG=50/(651 sqrt(28248)). Its square is 625/2992882662, below both
(25/54684)^2 and (4.5717e-4)^2. Thus the corrected displayed ceilings are
valid upper bounds. The legacy fixed radius 2^-23 is exact, not a decimal
approximation to an optimized supremum. No interpretation of this table
extends to a dyadic norm that does not dominate L2.

Let D=||h||_2 for an admissible stationary correction and suppose the
accepted weak test proves D>d. If the ball's admissible distance is at
most b and b<=B, then d/B>q implies D/B>q. Thus q>1 excludes that ball.
All 23 numerical distance rows are checked by exact rational division
using B=3.7930e-6, 2.8496e-6 and 25/54684. The preceding 22 rows retain
exactly the data and factors accepted by T4-453. The new row truncates the
independently proved 026 floor downward:

 D > 0.001355907204057457 > 0.001355907204.

Even the truncated value divided by these three B's is strictly above
357.4, 475.8 and 2.965 respectively. The fixed-c weak stationary equation,
real S1 L2 correction, canonical L2-bounded velocity, integrable weak
products and justified whole-plane cutoff limit are the hypotheses of
the frozen 026 proof. Its accepted 63-moment enclosure is a dependency;
no spatial integration is repeated in this audit. The reciprocal
N4-377 through N4-379 acceptances are recorded in the frozen N4 ledger.
These floor comparisons do not rank the actual distances of candidates.

## 2. Normalized endpoint condition and its range

Retain the exact c, q=1/c-4, delta=1-1/c, alpha=-2q-2>0,
D0=5c-1, angular norm B>0 and g0>0 of the accepted endpoint proof.
A weighted budget Hmax must hold for every stationary correction in the
ball being excluded. A velocity coefficient E must be valid uniformly
on the specified real S1 C1 weighted space, not merely on a tested
function. At radius b the crude cutoff comparison requires

 E sqrt(2 pi) Hmax/B < Emax(b),
 Emax(b) = D0/g0 * (B/(b sqrt(alpha)))^(delta/(-q-1)).

Indeed the necessary cutoff inequality is
B*(D0*B/(sqrt(2pi)*Hmax*g0*E))^((-q-1)/delta)/sqrt(alpha)>b;
all factors and exponents are positive, so raising to
delta/(-q-1) and rearranging gives exactly the displayed condition.
The accepted stationary endpoint lower bound Hmax>=B/sqrt(2pi) makes
E<Emax(b) a weaker necessary condition, not the full test. This repairs
the draft 39 summary without promoting a hypothetical budget to a proof.
For 007, 013 and 014, the frozen endpoint enclosures verify Emax at the
printed graded target is below 7.9417, and at bG is above 7.942167.
With Hmax>=999745, the required E at bG is below 0.2694533; the accepted
largest enclosure is 0.26945243670784104023856... (T4-452). This lies below
the already proved universal lower bound 0.7930365064... .

Since Emax(b) decreases with b, an upper cutoff bound proved at the old
3.5125e-7 radius remains valid at the slightly larger exact TB-rebal
supremum. This argument transfers an upper bound, not a two-sided
numerical enclosure. The factor b_TB-rebal/(3.5125e-7) is below
1.0000136. The distance-table divisors do not use this old display.

The T4-425 splice obstruction in the changed text now explicitly names
its four targets: fixed sharpw, sharpw family, TB-sharp and graded.
At the two small FW-A2-Db targets an improved valid universal coefficient
remains OPEN. The current list of proved coefficients remains separately
blocked there, as T4-443 proves. Neither conclusion excludes a different
stationary-equation estimate or proves unrestricted nonexistence.

## 3. The 016 forcing statement and retained conditional arithmetic

For F in H1(R2) and s>=0, the Fourier multiplier (1+|xi|^2)^(s/2)>=1
implies ||J^s F||_2>=||F||_2 and ||D J^s F||_2>=||D F||_2.
Consequently, whenever X_(s,w)(F) is finite,

 X_(s,w)(F) >= sqrt(w1 ||D F||_2^2 + w2 ||F||_2^2).

If it is infinite the sufficient finite threshold also fails. The
strict G0 and G1 lower enclosures proved in T4-451 therefore force all
ten registered scalar sufficient forcing tests to fail. Their individual
ratios have a common lower bound 3542234. This statement concerns a
minimum over the ten tests for this one candidate; it does not compare
actual norms or distances between candidates. The result does not use
P2, the actual homogeneous Hdot^-1 norm, a Hardy proxy or an upper bound
on a fractional norm. Their remaining certification tasks remain open.
The corrected status also includes the previously confirmed rF component.

The draft's unchanged sharpw conditional arithmetic can be rechecked
exactly with mu=97/250, C=397, s=1/5184, cU=8/5,
r=1351/10^6, eta=4207/20000000, betaL=2. It gives high rate
63092119/405000000>0.1557, reciprocal below 6.4226,
r-eta/0.1557=7/1557000000>0, and contraction factor
r/(2 betaL sqrt(pi s(1+s)))<0.0137200. Its analytic premises retain the
status explained above.

## Dependencies and verdict

Exact inputs, frozen source hashes and accepted result/proof pairs are
listed in data/input_sources.json, data/additional_sources.json and the
manifest. The checker verifies their linkage, all changed-scope phrases,
the 23 rational table rows, all seven scalar squares and the graded
square, the normalized cutoffs and the conditional sharpw arithmetic.
This proof was written and checked before the checker was written.

CONFIRMED, subject to the named accepted analytic and integral
dependencies, are the changed mathematics and repairs of this frozen
draft. No changed assertion examined here is refuted. Later edits are
outside scope. A full challenge of every closure-matrix row is the
separate H18 task; no full-matrix acceptance follows from this audit.
No high inverse or a posteriori existence closure is proved here.
