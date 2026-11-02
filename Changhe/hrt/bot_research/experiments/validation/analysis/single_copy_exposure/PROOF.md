# Single-copy exposure on a fixed legal map

Status: informal theorem about the bundled rules. The algebraic argument below
is complete. An engine cross-check is supplementary and is recorded separately
when performed. No formal proof assistant is used.

## Statement and hypotheses

Use the current balanced configuration: the board is 12 by 12, each combat
round has 250 ticks, all minion speeds are 1, and every turret has cooldown 1.
Fix a legal defender map and its engine-selected route
`p[0], ..., p[L]`, where `p[0]` is the spawn and `p[L]` is the base. During
this combat no building changes. The attacker has exactly one active roster
entry, so exactly one full-HP copy spawns, at tick 0. Let its initial HP be `h`,
and let its base damage be `b`.

For a gun turret `t`, let `C(t)` be the number of route cells among
`p[0], ..., p[L-1]` within its Euclidean range. For a splash turret `t`, let
`C(t)` be the number of those cells among its eight neighboring cells,
including diagonal neighbors. Let `d(t)` be the catalog damage of `t`, and put

`D = sum over all turrets t of d(t) * C(t)`.

Then the copy reaches the base if and only if `h > D`. If it arrives, its
remaining HP is `h - D` and it causes exactly `b` base damage. Otherwise it
causes no base damage and is killed during this combat.

## Proof

The shortest legal route has no repeated vertex. A route with a repeated
vertex contains a cycle whose removal produces a shorter route between the
same endpoints. Since there are 144 board cells, `L <= 143`, so a surviving
copy born at tick 0 reaches the base at tick `L`, strictly before the end of
the 250-tick combat.

The engine leaves a newly spawned copy on the spawn cell during its birth
tick. On each subsequent tick it moves one route step before the attack phase.
Thus, while alive, the copy occupies cell `p[k]` at attack tick `k`, for
`0 <= k < L`. At tick `L`, the engine resolves arrival before turret attacks,
so the base cell contributes no turret damage.

There is no other copy to compete for a gun's target. At each pre-arrival tick,
each gun covering the occupied route cell selects this copy. Each covering
splash also damages it. Cooldown 1 permits every such attack tick. All turret
damage in that tick stacks, and deaths are removed after damage application.
Consequently, until death, the copy's accumulated damage after tick `k` is
exactly the sum of the nonnegative cell damages on `p[0], ..., p[k]`.

If `h > D`, every prefix damage sum is at most `D < h`. The copy remains alive
through all pre-arrival ticks, then arrives with HP `h - D` and causes damage
`b`. If `h <= D`, some first prefix sum is at least `h`. All preceding prefix
sums are below `h`, so the copy is present for that prefix's final attack tick
and is killed there, before arrival. These two cases exhaust the possibilities.

## Dependencies and scope

The movement, targeting, death and arrival order are those in
`td_game/combat.py`; the route is computed by `td_game/pathfinding.py`. Exact
catalog values come from `td_game/balanced.json`. The theorem uses no economic
or opponent-behavior hypothesis.

`D` is potential damage to an isolated copy, not a lower bound on damage to
every copy in a stream. Guns can spend their attacks on earlier copies, so the
same formula does not certify defense against multiple roster entries. Nor
does it certify future maps, future purchases or a policy's strength. Using
`D` to select an attack heuristic requires separate policy experiments.
