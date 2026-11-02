# An exact rational certificate for damage under every affordable response

## Statement

Use the bundled balanced rules on the 12 by 12 board, with 250 combat ticks,
unit movement, one arrival damage value and initial HP per minion type,
single-target guns and eight-neighbor splash. Fix a legal defender building
set B and its nonnegative integer gold G before construction. Fix an ordered
package P appended after e active roster entries of the attacker. The types
of those earlier entries may be arbitrary. The defender may add any legal
buildings costing at most G before combat; it cannot remove existing ones.
No further construction occurs during combat.

Let L* be the sum, over the board's disjoint 2 by 2 blocks, of the minimum of
3 and the number of cells not occupied by B, minus 1. Package entry j starts
at tick s_j = (e+j) mod 250. Keep the eligible entries E with s_j <= 249-L*.
If E is empty, return the bound zero. Otherwise let m be the number of
its distinct start ticks and set H = min(250, max(s_j)+L*-min(s_j)).

For every existing splash turret, bound its contribution to one copy by
10 times the smaller of 7 and the number of its eight neighboring cells
that are on the board and not occupied by B. Sum these bounds to obtain S0.
For an existing gun, let c be the smaller of its unoccupied in-board range
cell count and the range bound 15, 20 or 27 for radius 2.5, 3 or 3.5.
Sum damage(gun) times min(H,m*c) over existing guns to obtain Gamma0.

For a new gun of type t, define v_t = damage(t)*min(H,m*C_t), using the
same global range bound C_t. Let U(g) be any rational upper bound on the
largest sum of v_t attainable by a multiset of new guns costing at most g.
An exact unbounded integer knapsack is one option; g*max_t(v_t/cost_t) is
another. For each integer k from 0 through floor(G/60), set

    S_k = S0 + 70*k,
    Gamma_k = Gamma0 + U(G-60*k),
    a_j = max(hp(P_j)-S_k, 0).

Discard entries with a_j=0 when computing the following lower bound. Let
T_k be the sum of their arrival damage values over the remaining entries.
Let F_k be the fractional knapsack optimum that maximizes removed arrival
damage with weight a_j per copy, capacity Gamma_k, and at most one of each
remaining entry. Define

    B_exact = max(0, min_k (T_k-F_k)).

Then the package's own base damage is at least ceil(B_exact), for every
affordable legal defender response. Consequently total damage, including
any earlier roster entries, is also at least ceil(B_exact). Fractions and
the final ceiling must be computed exactly for this certificate.

## Proof

A shortest grid path is induced: an edge between nonconsecutive path
vertices would shorten it. Its vertices in any 2 by 2 block therefore
number at most three, since all four would contain a cycle. Its vertices
avoid the existing buildings, so its length is at most L*, regardless of
additional buildings. Every eligible package copy which survives to its
base arrival reaches that base by tick 249. It cannot be lost merely to the
round boundary.

The eight cells neighboring a splash turret form an eight-cycle in the
side-adjacency graph. An induced path cannot contain the entire cycle, so
at most seven are route cells. Existing occupied cells further reduce this
number. Each moving copy visits each route cell once and receives at most
one splash hit there per turret. Its cumulative splash damage is at most
S_k if the defender bought exactly k new splash turrets.

The range-forest result in the neighboring range_forest proof bounds the
number of route cells in a gun's range by C_t. Its independent finite
certificates give 15,20,27 for the three bundled ranges. Existing blocked
and out-of-board cells can only lower the count. Package copies with the
same start tick share their position while alive. With m eligible start
ticks, the total number of ticks on which at least one eligible package
copy is in a fixed gun's range is at most m*c. It is also at most H: every
such copy can be on the map only between its start and its start plus
L'-1, where the actual path length L' is at most L*. A gun deals damage to
at most one copy at each tick. Hence damage(gun)*min(H,m*c) bounds all its
damage to eligible package copies together. Earlier roster entries or
ineligible package entries can consume shots, but cannot increase this
bound. Adding the existing and new gun bounds gives Gamma_k.

A package copy that dies must receive total damage at least its HP. If its
HP exceeds S_k, it therefore consumes at least a_j of the gun-damage
budget. Overkill does not invalidate this lower bound. Copies with a_j=0
can conservatively be treated as dead without consuming gun damage. Among
the other copies, the actual dead subset is feasible in the integral
knapsack with capacity Gamma_k. Relaxing the zero-or-one choices to
fractions can only increase removed arrival damage. Thus surviving eligible
copies deal at least T_k-F_k. All those survivors arrive before the round
ends, as shown above.

The actual response has some allowed number k of new splash turrets. Its
new gun spend is at most G-60*k; walls, factories, unspent gold and other
purchases only reduce available gun spend. Taking the minimum over k covers
every response. Damage cannot be negative. Finally actual arrival damage
is an integer, so it is at least the ceiling of an exact rational lower
bound. This proves the claim.

## Computing the fractional optimum

Sort positive-weight items by the exact rational ratio of arrival damage
to weight, in descending order. Fill that order up to capacity, taking a
fraction of the last available item if needed. If a lower-ratio item is
taken while a higher-ratio item is not full, transfer a positive amount of
weight to the higher-ratio item. Value does not decrease. Repeating this
exchange yields the greedy ordering, proving its optimality. Grouping
identical types into bounded counts preserves this optimum.

## Dependencies and scope

The proof uses the unchanged combat and construction rules, the elementary
shortest-path argument above, and the range_forest proof with its completed
finite search evidence. It is an informal proof with exact-arithmetic
implementation checks, not a theorem-prover result. The building set must
be legal, the balanced rule constants must match, and the input e must count
active entries after expiration. The implementation rejects other rules.
The certificate may be very conservative and asserts no strategic value,
optimal attack, or superiority of the resulting policy. Verification
artifacts are registered in the adjacent verification directory.
