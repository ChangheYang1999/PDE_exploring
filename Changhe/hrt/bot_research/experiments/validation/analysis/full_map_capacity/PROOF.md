# A full map has fixed defensive capacity

## Statement and hypotheses

Use the unmodified bundled balanced engine on the 12 by 12 grid, with 250 ticks per round. The graph has the engine's four-neighbor edges. A legal defender map has current shortest route P = (p_0,...,p_L), from spawn to base. Every cell not on P is occupied by a wall or turret. Buildings cannot be removed or upgraded under the legal action interface.

Let S be the sum of all splash damage a speed-one copy would receive at route cells p_0,...,p_(L-1). The base cell is excluded because arrival precedes turret attacks. Let D be the sum of the per-tick damage of all non-splash turrets. Consider n distinct active roster entries of one minion type, each with HP H > S and base damage b. Each selected entry has dense active-roster index k satisfying k mod 250 <= 249-L. Other active entries may be present.

Then no legal construction can add a building to this map. In the specified round at least

    max(0, n - floor(250 D / (H-S)))

of the selected copies reach the base, contributing at least b times this number in base damage. In particular, n(H-S) > 250D guarantees at least one selected arrival. This is a statement about the completed combat round; it does not assume that the defender survives the damage.

## Proof

A shortest route is simple. No two nonconsecutive vertices of P are adjacent: replacing the intervening subpath by that edge would give a shorter route. Thus the graph induced by the unoccupied cells is exactly the path P. A building outside P is rejected because its cell is occupied. A building at either endpoint is expressly forbidden. Removing any other vertex of P disconnects spawn from base, so constructing there is rejected by the path-legality check. The action interface has no removal or upgrade operation. Therefore all accepted future actions leave the building list, route and turret statistics unchanged.

A newly spawned copy starts at p_0. In each later tick a living copy advances one route vertex. The engine has no collision or slowing operation, and other copies do not obstruct it. Before arrival, a selected copy visits each encountered nonterminal vertex at most once. Its total splash damage before death or arrival is therefore at most S. Simultaneous selection and stacking of turret attacks does not change this bound.

Each non-splash turret selects at most one copy per tick and adds at most its catalog damage to that copy's damage accumulator. Across 250 ticks, the sum of all non-splash damage assigned to all copies is at most 250D. A selected copy that is killed must have received at least H damage, hence at least H-S non-splash damage. Consequently no more than floor(250D/(H-S)) selected copies can be killed. Overkill only consumes more of the same finite damage budget; damage assigned to unselected copies cannot increase the number of selected deaths.

The selected entry with index k spawns at t = k mod 250. If it is not killed earlier, it arrives at tick t+L. The hypothesis t <= 249-L places arrival within the simulated ticks 0 through 249. It is therefore neither cleared unfinished nor carried into another round. Every selected copy not killed arrives and deals b base damage before any attack at the base cell. Subtracting the death bound proves the claim.

## Counting eligible entries

If all N active entries are of the selected type, dense indices are 0 through N-1. The number satisfying the arrival cutoff is exactly

    n = floor(N/250) (250-L) + min(N mod 250, 250-L).

Each complete index block supplies 250-L eligible residues, and the final prefix supplies the stated minimum. Expired entries are removed before dense indexing; original roster IDs do not determine spawn phases. The 12 by 12 grid guarantees L <= 143 for a simple route, so 250-L is positive.

## Dependencies and scope

The argument uses `td_game/actions.py` for construction legality and the absence of removal, `td_game/pathfinding.py` for shortest routes, `td_game/combat.py` for dense indexing, ordering and damage, and `td_game/balanced.json` for the standard speed-one catalog and 250-tick horizon. It independently checks and slightly generalizes the economy lane's Proposition F. It is an informal proof, not a machine-checked theorem.

The construction obstruction is necessary for permanence, but the damage bound also holds for any map whose buildings stay fixed during the combat. The bound can be loose because it credits every gun with firing on every tick. It makes no claim that a player can afford the required roster, that the game lasts until a proposed flood, or that an attacking player survives. In particular, a statement about every growing opponent eventually winning requires those further hypotheses. S >= H invalidates this particular capacity argument; it is not by itself a certificate that every finite-horizon copy arrives or dies in a specified way.

Component verification uses legally reached maps, attempts every building type on every grid cell, checks the bound against the unchanged combat implementation on multiple roster sizes, and includes roster wrap and expiry cases. Those finite checks supplement the proof. They do not establish policy strength.
