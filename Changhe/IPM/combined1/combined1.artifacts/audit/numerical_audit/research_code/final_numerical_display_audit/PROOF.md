# Directed displays and supplemental numerical checks

## Statement and dependencies

This is a finite audit of the coordinator report frozen as SHA256 7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743. Its accepted dependencies are N4-024 (d2 L2 residual), N4-139/153/166/180 (007 components and weighted norms), N4-092/111 with T4-111/162 (007 background bounds), N4-252 (four fractional N_s norms), N4-382/355/389 (015/016/017 dyadic exclusions), N4-392/393 (016 complete components and five norm orderings), and the complete 016 bounds N4-431. Their source-integral proofs remain dependencies; hashing does not prove them again.

The comparison table heading "residual LB" cannot apply literally to every displayed number. In row20 and row37, the display G0=4.99 exceeds the certified upper endpoint for d2 G0. In row80, the display ||rF||_2=7.1457012 exceeds the certified upper endpoint for 016. Both are valid nearest-rounded displays in their stated decimal cells, but neither is a directed lower bound. The audit checks the exact frozen lines and preserves this distinction. It does not assert that either exclusion ratio was obtained from that rounded display.

The supplemental checks establish: 007's stated G0/G1 rounding cells; the elementary lower bounds sqrt(2^15 G1^2+2^20 G0^2)>732.35 and 1024 G0>385.72; its accepted Hilbert-Schmidt upper estimate below0.72817, signed rate above2.00215453001767 and complete theta=2/25 cover; the four displayed N_s interval endpoints and ratios above5.7e6; the 016 complete G0/rF displays and five strict forcing-norm orderings relative to007; and the displayed minimum seven-cell ratio floors for015,016,017. These are selected finite comparisons, not certification of every number in the report.

## Proof

Parse each finite decimal and rational as an exact fraction. A ball [c +/- e] denotes [c-e,c+e] with e>=0. The lower endpoint of a lower-bound ball and upper endpoint of an upper-bound ball give containing endpoints for the unknown quantity. The predicate c-e>q proves a strict lower bound; c+e<q proves a strict upper bound. A decimal display d rounded to a unit u is valid if the entire containing interval lies strictly between d-u/2 and d+u/2. It need not be a directed bound. Checking c+e<d proves d cannot be a lower bound on that quantity. All these comparisons reduce to integer multiplication by positive denominators.

For positive containing lower bounds a0<=G0 and a1<=G1, positivity and monotonicity give 2^15 G1^2+2^20 G0^2>=2^15 a1^2+2^20 a0^2. Compare that rational with732.35^2 to avoid a numerical square root. Similarly compare1024a0 with385.72. The 007 background cover's accepted finite partition and endpoint are retained without new point evaluation. The rate estimate is checked by exact rational endpoint comparison.

For an accepted interval L<N_s<U and positive exact registered threshold tau, L/tau is a strict lower bound for the actual failure factor. The four N4-252 endpoints are compared exactly with the report's decimals. For each of the five matched norm instances, U007<L016 implies the actual 007 norm is strictly smaller than the actual 016 norm. This implication concerns the same norm at the same s and weights as stipulated in N4-393, not an ordering of solution distances.

For each dyadic dependency, inspect all seven accepted cell exclusions and take the minimum of its stored strict rational ratio floors. Comparing this minimum with the displayed floor is sufficient to retain the reported numerical floor. The analytic cell interpolation and treatment of the divergent endpoint region remain the accepted dyadic theorem's responsibility. No complete 017 upper norm is inferred.

## Suggested report repair and scope

Rename the table column "residual value or bound". Add: "Entries without an inequality sign or explicit enclosing interval are rounded displays of the cited values. They are not certified directed bounds; ratios use the exact underlying certificates." This permits the existing valid nearest displays while keeping explicit inequalities directed. All previously accepted norm bounds and candidate verdicts are unchanged. No new source integration or candidate computation is performed after the freeze.
