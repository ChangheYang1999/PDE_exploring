# The minimizing integer response for sin17 at delta6/13

Status: PROVED inV537. The underlying branch was admitted in242/V528; the stronger complete comparison and exact box replay passed at18:55Z.

## Statement

Let sigma_k be the unit-amplitude tuning response for leading sin(17theta) at delta=6/13, k>=1. The exact minimizing index is2380. The value is defined exactly by the rational compact response S(1/14278); an interval display is not its definition. The assertion is

    inf_(k>=1) |sigma_k| = |sigma_2380|,

with equality only at2380. A stronger sufficient radius follows using the strict bound s=277/10^14. No claim of optimality is made for the majorant radius.

## Proof by a complete integer partition

The admitted242 certificate partitions [0,1/238] into dyadic leaves. Its integer samples are t_k=1/(6k-2), k>=40. Recompute the target response with directed1536-bit arithmetic and let U be an exact rational upper bound on its absolute value. For every singleton except2380, verify |S(t_k)|>U. For every nonsingleton interval, recompute a degree-five Taylor enclosure at1536 bits and verify that its absolute value is greater than U throughout the interval. Verify the leaf addresses, rational endpoints, integer ranges and full coverage again. The singleton at2380 contains the target. Independently recompute the39 earlier integer responses and require each to exceed U.

Every integer k is thereby covered, and every integer other than2380 has response strictly greater than the target. This proves both the infimum formula and uniqueness. The independent real-zero result252 explains why the minimizing integer is near a real zero, but it is not used to infer any global minimum.

## Consequence for the majorant

Require the directed target lower bound to exceed277/10^14. Reuse the separately certified exact density-prefix bounds from242 and build a fresh nonnegative supersolution of the same rational map with L=507/152 and kappa=7938/169. Reconstruct the map and all78 scalar recurrence identities independently. If the box closes at w=2^-q, the same proof gives

    R > 2^(q/6) |epsilon|^(13/6).

The exact box, exponent and every component inequality must be retained. This only sharpens the sufficient bound; it does not locate the true exterior convergence threshold.

Dependencies:149,172,175,232,234,242. All certificate inputs and arithmetic sources are identified by hashes.

## Completed checks and conclusion

All39 direct responses and all38 leaves passed. The partition has22 singleton leaves and16 Taylor leaves. In particular, its interval touching zero is [0,1/15232]; its whole closed Taylor enclosure lies strictly above the target upper bound. Thus the limiting response cannot furnish a competing infimum. The unique target leaf contains k=2380. The exact target is |S(1/14278)|; its directed display is

    2.770618823558535346754423655474072645384209404183058901e-12

with error less than4.63e-67. Every other integer response has absolute value strictly greater than the rational upper bound used for this target.

The fresh1536-bit replay shares the reviewed jet engine with the original native cover calculation. It is a new precision and strict-minimum comparison, not a separately implemented Taylor engine. The underlying242 certificate also has a separately implemented1024-bit manual Taylor replay. These roles are distinguished in the evidence. The stricter comparison took1340.82488seconds.

The exact rational supersolution closes at q=320. A separate map reassembly verifies all78 scalar coefficient identities and every component inequality. Hence for f_1=epsilon sin(17theta), epsilon!=0, a sufficient exterior for the tuned pure density, stream and common-potential series and every fixed weighted derivative is

    r>=R>2^(160/3)|epsilon|^(13/6).

The minimum statement uses the unit-amplitude response; for general epsilon its value is multiplied by |epsilon|^13. The sufficient radius is not asserted to be optimal. The independent theory-part review accepted the argument conditional on precisely these completed checks.
