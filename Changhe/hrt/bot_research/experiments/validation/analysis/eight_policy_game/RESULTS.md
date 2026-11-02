# A fixed eight-policy table after the signal repair

Checked 2026-10-31T19:51:41.807377+00:00.

H1 L is nonnegative against every included policy: REFUTED.
H2 the old B/H/J mixture remains nonnegative against L: REFUTED. Its payoff against L is -1/3.

B is frozen best_v9e, C is the private-D timing attacker, D the adaptive Fortress38 delegate, G the early-wall guard, H the HP-triggered grower, I the private-H timing attacker, J the common-prefix response selector, and L the repaired twenty-wall signal attacker. Sources and exact parameters are pinned in the parent declarations. B is a frozen earlier nominee, not a claim about whichever bot is finally installed.

| Row | B | C | D | G | H | I | J | L |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 0 | 1 | -1 | -1 | -1 | 1 | 1 | 1 |
| C | -1 | 0 | 1 | -1 | -1 | 0 | 0 | 0 |
| D | 1 | -1 | 0 | 0 | 0 | -1 | -1 | -1 |
| G | 1 | 1 | 0 | 0 | -1 | 1 | -1 | 1 |
| H | 1 | 1 | 0 | 1 | 0 | -1 | -1 | -1 |
| I | -1 | 0 | 1 | -1 | 1 | 0 | 0 | 0 |
| J | -1 | 0 | 1 | 1 | 1 | 0 | 0 | -1 |
| L | -1 | 0 | 1 | -1 | 1 | 0 | 1 | 0 |

This table contains ten new games and 62 explicitly reused records, for 72 games and 36 assignment pairs. Every pair has identical normalized histories. The ten new games pass strict accounting, original-engine replay, source/data checks and 708 fresh external decisions. The reused parent receipts and their inputs are rechecked, including exact decompression of archived replays. No extra games are counted from arithmetic verification.

An exact optimal mixture in B,C,D,G,H,I,J,L order is ['1/5', '0', '0', '1/5', '1/5', '0', '1/5', '1/5']. Its column payoffs are ['0', '3/5', '1/5', '0', '0', '1/5', '0', '0']. The finite value is zero. Exact normalization, nonnegativity, column lower bounds and skew-symmetric opposing upper bounds are independently checked after the solver proposes the vector. The three eight-dimensional fixtures also pass.

Pure policies nonnegative against every column: none. Directed three-policy cycles: B > C > D > B; B > I > D > B; B > I > H > B; B > J > D > B; B > J > G > B; B > J > H > B; B > L > D > B; B > L > H > B; G > I > H > G; G > L > H > G; G > L > J > G.

The old certificate remains valid on its original seven columns. Any failure on L limits its extension, not that earlier restricted proof. This new certificate is likewise limited to the eight fixed policies, measured standard start and checked histories. It does not prove a full-game equilibrium, robustness to changed starts or invariant behavior under different clock-limited search outcomes. The extension was selected after development results and is not held out. Pool D is unchanged.
