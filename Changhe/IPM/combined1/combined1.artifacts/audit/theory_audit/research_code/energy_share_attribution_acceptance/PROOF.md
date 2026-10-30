# Which energy has the 72/14/14 shares?

## Exact statement, notation and premises

Let F be the exact full-plane residual of candidate C1-N1-007 at
c=4076476460239181/2251799813685248. Put

 G0=||F||_2, G1=||D F||_2, P2=||omega D^2 F||_2,
 omega=(1+4r^2)^(2/5), J^s=(1-Delta)^(s/2).

D^2 is the complete ordered Cartesian tensor, so its squared norm counts
F_xy twice. Assume the complete component certificates and norm comparison
accepted in N4-180 and T4-238, with the exact positive containing intervals
in the frozen G0 and derivative records. No finite-domain surrogate is
used. Define

 E_*^2=P2^2+2^14 G1^2+2^18 G0^2,
 E_w^2=P2^2+2^15 G1^2+2^20 G0^2,
 X=E_w(J^s F), s=1/5184.

The assertion audited is N4-438: the P2,G1,G0 shares of E_*^2 round to
14%,72%,14%, respectively. Those shares are not the corresponding shares
of X^2. Indeed the actual G0 contribution to X^2 is strictly greater than
1/4. The frozen coordinator report7fd963af... assigns the percentages to
its squared sharpw norm at lines226-227 and993-994, so those two assignments
are REFUTED. The corrected E_* attribution and the bound on the actual X
share are CONFIRMED. The actual fractional P2 and G1 shares are OPEN here.
No optimization floor, inverse, distance ranking or existence follows.

## Complete argument for the shares

Suppose positive exact component C_i lies in [a_i,b_i], with weights w_i>0.
Write A_i=w_i a_i^2 and B_i=w_i b_i^2. The share is

 t_i=w_i C_i^2 / sum_j w_j C_j^2.

It increases in its own squared component and decreases in each other
squared component: differentiate x/(x+y) for x,y>0, or cross-multiply.
Consequently the tighter correlation-preserving interval is

 A_i/(A_i+sum_(j!=i) B_j) <= t_i
       <= B_i/(B_i+sum_(j!=i) A_j).

The simpler interval A_i/sum B_j <= t_i <= B_i/sum A_j is also valid and
contains this tighter one. The checker constructs both independently
from the exact decimal ball endpoints. It compares the simpler intervals
with every exact endpoint saved by N4-438, and checks that both containments
and the old N4-180 component intervals agree. For E_* the intervals lie
strictly inside the nearest-percent cells (13.5%,14.5%), (71.5%,72.5%)
and (13.5%,14.5%). Thus the stated rounded percentages follow. The
unregularized E_w shares instead have the saved approximate values
6.36%,67.67%,25.98%; these are not asserted to be the fractional X shares.
Changing the weights alone already changes the energy decomposition.

## A rigorous lower bound for the actual sharpw G0 share

The Fourier multiplier (1+|xi|^2)^(s/2) is at least1. Plancherel gives
||J^s F||_2 >= ||F||_2. Let a0>0 be the accepted lower endpoint for G0,
and U>0 the accepted upper endpoint of the sharpw upper-comparison ball
in N4-180. That comparison proves X<=U. Hence

 2^20 ||J^s F||_2^2 / X^2 >= 2^20 a0^2/U^2 > 1/4.

The last strict comparison follows by exact rational cross multiplication,
4*2^20*a0^2>U^2. It uses only the accepted unregularized G0 certificate,
the correct fractional sharpw upper bound, and Plancherel. It does not
assume that weighted Hessian multiplication commutes with J^s. In
particular the weight omega creates no issue in this argument because
the lower bound uses only the unweighted zeroth component. The >1/4
conclusion contradicts even the whole rounding cell near14%.

## Report repair, dependence and verification

At both frozen passages replace the share sentence by:

“In the unregularized comparison energy E_*^2=P2^2+2^14 G1^2+2^18 G0^2,
the weighted G1 term contributes about72 percent, and the G0 and P2 terms
about14 percent each (N4-180, corrected in N4-438).”

All previously certified total norms, ratios and distance exclusions remain
valid. This result audits an attribution of prefreeze data. It produces
no new candidate, field integral or fractional-norm evaluation. The root180
accepted input bytes are also compared with their pre-existing T4 copy,
so the acceptance does not rely solely on the new438 report. The source
manifest binds the frozen N4 proof, inactive code, exact result, all ten
recorded inputs, the report and the earlier own acceptance. Hash agreement
checks provenance, not mathematical soundness. The numerical component
and upper-comparison soundness remain the accepted premises above.

The standalone proof is written before the checker. Every input decimal
is converted exactly to a rational; directed comparisons use integer
arithmetic. Peer programs are read but never executed. Existing Opus
reviews of the norm comparison remain the analytic collaboration premise;
the new attribution correction is reported to the theory lanes for their
final errata. This proof is independently derived by monotonicity and
Plancherel, not inferred from the peer's check count.
