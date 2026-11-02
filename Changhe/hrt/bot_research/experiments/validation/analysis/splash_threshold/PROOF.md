# Exact arrival criterion on a pure-splash map

## Statement and hypotheses

Use the bundled combat routine and balanced rules: every minion moves one route step per tick after its spawn tick. Fix a legal defender route P = (p_0,...,p_L), where p_0 is the spawn and p_L is the base. Assume the map contains walls and splash turrets only, and no buildings change during combat. There are T = 250 ticks numbered 0 through T-1.

For every attackable route index i in 0,...,L-1, define

s_i = sum of d_b over splash turrets b with max(|b_x - p_{i,x}|, |b_y - p_{i,y}|) = 1,

where d_b is that turret's configured damage. Put D = sum_{i=0}^{L-1} s_i.

Consider the k-th active roster entry after inactive entries have been removed. Let H_k and V_k be its configured HP and base damage, and let t_k = k mod T. Its combat copy reaches the base if and only if

`t_k + L < T` and `H_k > D`.

Accordingly, the total base damage on this fixed pure-splash map is the sum of V_k over exactly those entries satisfying both inequalities. The number of other active entries and their order do not affect this copy's damage from turrets. Changing their order can still change arrival eligibility by changing t_k.

## Argument

A copy is created at p_0 on tick t_k. It does not move on that tick. On every later tick, if alive, it advances one route index. Thus it occupies p_i for its attack phase on tick t_k+i for i less than L. On tick t_k+L it moves into the base and is removed before the attack phase. This tick exists within the round exactly when t_k+L<T.

At p_i every adjacent splash turret attacks the copy, including diagonally adjacent turrets, and every other splash turret contributes zero. Splash attacks do not choose among copies. The damage at that index is therefore exactly s_i, independent of all other copies. After the attack phase at p_i, the copy's HP, if it has survived to that phase, is H_k minus the prefix sum s_0+...+s_i.

All s_i are nonnegative. If H_k>D, every prefix sum is strictly less than H_k, so the copy survives every attack phase before the base. If H_k<=D, a first prefix sum reaches or exceeds H_k, and the copy is removed at that phase. It cannot reach the base. Combining this observation with the existence of the arrival tick proves the criterion. Summing the configured base damage of arriving copies proves the total-damage formula.

## Consequences

If D is at least the maximum HP of all allowed attacking types, the map takes zero base damage from every finite roster. This remains true for rosters longer than 250, because stacking does not divide or exhaust splash damage. Late copies may be cleared rather than killed, but neither event causes base damage.

If D is smaller, an alive type's order affects only its modulo spawn tick on a pure-splash map. A purchase in a late phase with t_k+L>=T cannot score this round. Cheap purchases can fill those phases so that later purchases wrap to useful phases. Such purchases may still change future rounds through roster lifetime and dense reindexing; the formula is for the current fixed combat only.

## Dependencies and verification evidence

The proof uses `spawn_schedule`, `combat_tick`, and `simulate_map` in `td_game/combat.py`, plus the active-entry predicate in `td_game/state.py`. Source hashes are in `runs/validation/integrity-start.json` relative to the research directory.

Finite checks include `runs/validation/wave-probe-001.jsonl`, `phase-probe-001.json`, and `phase-defense-probe-001.json`. The latter compares candidate purchase lists on fixed synthetic states. It is not a whole-game strength result.

## Exclusions

The formula does not cover guns, which select one frontmost copy and therefore couple copies through targeting. It does not compare alternative building placements, because a building may change the route P and hence every s_i. No optimal placement or whole-game optimality claim is made.
