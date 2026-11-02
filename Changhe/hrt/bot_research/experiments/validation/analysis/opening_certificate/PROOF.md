# An 89-gold first-round defense

## Exact statement and hypotheses

Use the unchanged bundled balanced rules, an empty initial 12 by 12 map,
100 initial gold, and no pre-existing attackers. In round 1, player P builds
one gun2 at (3,2), walls at (x,1) for x = 0,1,2,3,4, and walls at (6,y) for
y = 0,1,2,3. Build the turret first and then the walls in those listed orders.
Player P buys no other buildings in this round. Against every legal round-1
submission by the other player, P takes zero base damage in round 1.
The claim holds in either player assignment. It does not assert that this
opening maximizes later winning chances or has minimum possible cost.

## Notation and argument

A route index is the number of steps from spawn. A copy purchased in position
k of the attacker's minion-purchase subsequence, starting at k = 0, spawns at
tick k. The first-round budget permits at most six copies, so there is no
modulo wrap. Other purchases may be interspersed but cannot increase the
attacker's available gold before combat.

The turret costs 80 and the nine walls cost 9, for a legal total of 89. No
building occupies an endpoint. A final route exists, so every prefix of this
construction also has a route. Direct breadth-first search with the bundled
right, down, left, up neighbor order gives the 22-step route:

(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (5,1), (5,2), (5,3), (5,4),
(6,4), (7,4), (8,4), (9,4), (10,4), (11,4), (11,5), (11,6), (11,7),
(11,8), (11,9), (11,10), (11,11).

The gun's radius is 3. Its covered route indices are exactly 1 through 9,
with no gaps. It deals 22 damage to the frontmost in-range copy every tick.
A tier1, tier2, or tier3 needs respectively 1, 4, or 9 hits. Higher tiers
cost more than the entire initial budget and cannot be bought.

Let n1, n2, n3 count these three types. Their costs impose
15 n1 + 40 n2 + 100 n3 <= 100. The total required hits are at most 9:
if n3 = 1, all other counts are zero and nine hits suffice. Otherwise n2
is 0, 1, or 2. For n2 = 0 there are at most six tier1, requiring six hits;
for n2 = 1 there are at most four tier1, requiring at most eight hits;
for n2 = 2 there is at most one tier1, requiring at most nine hits.

Here is why nine total hits suffice despite the gun's single-target rule.
The k-th copy enters coverage at tick k+1 and, if still alive, leaves it
after tick k+9. The gun serves the earliest surviving copy first, since it
is furthest along the route. Starting at tick 1, there is no idle service
tick before all copies die: after k+1 completed copies, at least k+1 hits
have been fired, so the next copy has entered coverage by the next tick.
Every copy's completion tick is therefore its prefix sum of required hits,
which is at most 9. Its exit deadline is k+9, at least 9. By induction over
the copies, none leaves coverage before receiving all required hits.
Thus all copies die by tick 9, before reaching the base at route index 22.

Opponent buildings and factories affect only the opponent's map or later
income. They cannot change this route, purchase additional minions during
combat, or alter the proof. Action interleaving has no cross-player effect
on construction or purchase legality. This proves the assertion for every
legal submission and both player assignments.

## Dependencies, inputs, and verification

The argument uses the balanced costs, HP, gun2 damage and radius; the
single-target rule in `td_game/combat.py`; purchase settlement before combat;
and the bundled shortest-path tie order. The exact proposed construction is
registered in `certificate.json`. The independent check is
`experiments/validation/verify_opening_certificate.py` relative to
`bot_research/`.

That check enumerates every ordered minion sequence costing at most 100 by
budget recursion, builds this defense through original Engine actions, and
replays every sequence in both assignments. It also records the route and
coverage, checks the hit-count bound, and hashes its input and original
sources. Its evidence is registered in `verification/evidence.json`.
The argument above explains the guarantee; the finite replay is an
implementation cross-check. No formal theorem-prover verification is claimed.

## Scope

This is a one-round certificate from the standard start. A previously
purchased roster, more than 100 initial gold, later route changes, or different
rules fall outside the statement. Retaining these buildings may constrain
later defensive layouts and slows first-round factory growth. Those strategic
costs require whole-game evaluation.
