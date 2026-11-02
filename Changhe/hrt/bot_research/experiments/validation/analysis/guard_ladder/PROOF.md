# A second guard upgrade can invalidate a second attack prediction

## Exact mathematical statement

Fix the bundled balanced rules. Let a defender contain only splashes in a
specified legal sequence of distinct cells. Let P be its actual shortest
route, of L steps, and let S be ten times the number of pairs (route cell
before the base, splash cell) at Chebyshev distance one. For an active roster
of N entries all having HP h and base damage d, the number of arrivals is
zero if h <= S. If h > S, it is the number of indices k in {0,...,N-1}
for which (k mod 250) + L <= 249; total base damage is d times this count.
This assumes no guns or other damaging buildings and the stated unchanged
spawn, move and attack ordering.

## Proof

An entry's copy is born at tick k mod 250. It stays on its spawning cell
through that tick and moves once on each later tick. At every visited cell
before the base, all adjacent splashes deal their ten damage to that copy,
independently of every other copy. Thus a copy that would arrive receives
exactly S before arrival. If h <= S it dies before it can arrive; a late
copy can instead be cleared before completion, which also gives no arrival.
If h > S it survives every such attack. Arrival occurs at its birth tick
plus L if that is at most249, and the copy is then removed before turret
fire. This proves both the count and its multiplication by d.

Every advertised prefix is checked by rebuilding it through apply_action,
recomputing the original shortest_path, and comparing original simulate_map
for every tier at counts1 and251. Data values are inputs to those checks,
not proofs by themselves. Legal prefixes need not preserve S automatically;
this construction checks monotonicity explicitly.

## Development hypothesis

The previously validated two-guard schedule stops the lead's round6 tier2
attack. A further timed upgrade with S >= 180 should stop a subsequent
tier3 attack, potentially exhausting fail_limit=2 in the same way. This is
a full-game hypothesis, not a consequence of the arrival formula: the new
purchase changes cash, the tier5 wave, future actions and the opponent's
response. A current-mode opponent may answer with a higher tier instead.

Use the exact existing empty-layout guard prefix as the starting point,
extend it by greedy legal-cell search until S first reaches180, and store
all cells, routes and exposures in exact JSON. No claim of globally minimal
cost is made. Compare upgrades at rounds8,9,10 against the fail_limit=2 and
current-mode variants on the unchanged engine, both player assignments.
Retain all results. These are outcome-informed counter development, not
held-out validation. Prefix checks and game evidence are in verification/;
no proof-assistant formalization is claimed.
