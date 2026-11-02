# Splash immunity is not a necessary condition for stopping a wave

## Statement and hypotheses

Use the bundled balanced rules. On an otherwise empty defender map put five
`gun3` turrets at (3,1), (4,1), (5,1), (6,1), and (7,1). The attacker has exactly
one active tier5 entry, born at tick 0. There are no other active entries.
The map is fixed for the combat. Its splash exposure S is zero, yet the tier5
copy is killed before reaching the base. Thus S < 1500 alone does not imply
a tier5 arrival on a map that may contain guns.

This is a component statement. The verification supplies the construction
and purchase budgets explicitly; it is not a standard-start strength game.

## Complete argument

The route along y=0 from (0,0) to (11,0), then along x=11 to (11,11), remains
unblocked and has the minimum possible length 22. The engine's right-first
breadth-first search selects it. Every proposed building is off that route,
so all five placements are legal. There are no splashes, hence S=0.

A gun3 has range 3.5 and damage 55 per attack tick. For each gun at (x,1),
where 3 <= x <= 7, the seven route cells (x-3,0) through (x+3,0) are in range:
their squared distances are at most 3^2+1^2=10 < 3.5^2. All these cells are
visited before the base. While the single copy is alive, every covering gun
must target it. If it survived through these cells, it would receive at
least 5 * 7 * 55 = 1925 damage, exceeding its 1500 HP. Nonnegative accumulated
damage therefore reaches 1500 at an earlier attack tick, and the copy dies
before arrival. There is no competing gun target. This is also a direct
application of the single-copy exposure result in the reading-order index.

The splash theorem gives the implication S >= 1500 => no arrivals. Negating
its premise does not give the opposite conclusion. On a map containing only
splashes, the stronger pure-splash theorem does characterize arrivals, but
it also requires an eligible spawn phase: birth tick plus route length must
be at most 249. These additional hypotheses cannot be omitted.

## Dependencies and scope

Rules: `td_game/balanced.json`, `td_game/combat.py`,
`td_game/pathfinding.py`, and `td_game/actions.py`. Mathematical dependency:
`../single_copy_exposure/PROOF.md`. The unchanged engine checks the declared
component below; it does not prove full-game strength or affordability at
any specified standard-start round. No proof-assistant formalization is
claimed. Evidence is in `verification/splash_converse.json`.
