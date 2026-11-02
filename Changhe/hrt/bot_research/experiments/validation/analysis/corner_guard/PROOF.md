# A 30-gold opening guard against three tier1 copies

## Statement and scope

Use the unchanged bundled balanced rules and the standard empty initial map.
In round 1 player P builds one gun1 at (10,1) and no other building. Factories
and minion purchases are allowed if the whole action list is affordable.
If the opponent buys at most three minions and they are all tier1, P takes
zero base damage that round. The statement holds in either player assignment.
It makes no claim about four or more copies, mixed rosters, a later changed
route, or the opening's eventual game result.

## Proof

The gun costs 30. It occupies neither an endpoint nor a cell on the initial
shortest route, so the placement is legal. The shortest route selected by the
bundled right-first breadth-first search remains

(0,0), (1,0), ..., (11,0), (11,1), ..., (11,11).

Indeed this 22-step route remains available, is still shortest, and no earlier
shortest route in the search order is created by removing a traversable cell.
Number its cells starting with index zero at the spawn. With radius 2.5,
the gun at (10,1) covers exactly indices 8 through 14. On the top row it covers
x = 8,9,10,11, since their squared distances are 5,2,1,2. On the right edge it
additionally covers y = 1,2,3, with squared distances 1,2,5. The next excluded
cells on either side have squared distance 10. Thus the coverage is a single
seven-cell interval, and it is well before the base at index 22.

Tier1 HP is 20 and gun1 damage is 8, so three shots kill a copy and two shots
do not. For n copies, 0 <= n <= 3, their dense roster indices are 0 through
n-1. There is no modulo wrap, and copy k spawns at tick k. Before it arrives
at the base, its path index at tick t >= k is t-k. Its coverage ticks are
therefore k+8 through k+14 inclusive.

There are no other attackers. The gun always chooses the living copy with
the greatest path index, hence the earliest surviving copy. Copy zero receives
shots at ticks 8,9,10 and dies at tick 10. If present, copy one then receives
shots at 11,12,13 and dies at 13. If present, copy two receives shots at
14,15,16 and dies at 16. These shot triples all lie inside the respective
coverage intervals [8,14], [9,15], [10,16]. Each death precedes that copy's
base-arrival tick, respectively 22,23,24. Consequently no copy reaches the
base. Fewer copies only remove the later triples.

Factories and P's own minions do not modify P's map or this combat sequence.
The opponent's buildings and factories affect its own map and later income,
not this route or the already purchased incoming roster. All construction
and minion purchases settle before combat. Swapping assignments leaves this
argument unchanged.

## Dependencies and verification

The exact geometry, stats, purchase timing and combat order come from
`td_game/balanced.json`, `td_game/pathfinding.py`, `td_game/actions.py`,
`td_game/engine.py` and `td_game/combat.py`. The empirical cross-check is
`experiments/validation/search_guard_geometry.py` relative to `bot_research/`.
It enumerates all 142 non-endpoint gun coordinates, checks each with three
tier1 attackers in both assignments using the original Engine, compares the
local simulator, and asserts the claimed coverage and zero damage at (10,1).
Its dated evidence will be registered under `verification/` after execution.
The argument above is standalone and informal. No formal proof assistant is
used, and the finite enumeration is a cross-check rather than a substitute
for the proof.
