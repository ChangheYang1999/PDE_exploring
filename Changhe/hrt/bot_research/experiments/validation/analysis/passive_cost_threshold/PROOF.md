# The public roster-cost exemption has a 45-gold first crossing

## Statement and hypotheses

Use the unchanged bundled balanced rules and the exact Insurer._passive
predicate in experiments/lead/v24.py, configured with passive_until=5 and
passive_bait=40. Suppose the observing player reaches round3. Its opponent
has no turret and its only roster entries bought in round2 or later form an
accepted round2 purchase list L of tier1 and tier2 entries. Then the predicate
is true exactly when 15 n1 + 40 n2 <= 40, where n1 and n2 are the counts in L.
Among all such lists that make the predicate false, the smallest possible
purchase cost is45, attained by exactly three tier1 entries. No assertion is
made about the observing player's submitted actions or the resulting winner.

## Notation and complete argument

The authoritative costs are15 for tier1 and40 for tier2. An accepted purchase
creates a roster entry with its type and bought_round=2. Its12-round lifetime
extends through round13. Combat copies can die or arrive without removing
the roster entry, so every entry of L remains in the round3 public roster.
The predicate first checks whether round3 is after passive_until=5, which it
is not. It next checks whether any opposing building is a turret, which is
false by hypothesis. It finally sums the configured costs of opposing roster
entries with bought_round at least2 and compares the sum to40. Under the
stated roster hypothesis that sum is exactly15 n1 + 40 n2. This proves the
first equivalence, including its non-strict boundary.

For the minimum false case, n2=0 requires15 n1>40, hence n1>=3 and cost>=45.
If n2=1, a false predicate requires at least one additional tier1, so cost is
at least55. If n2>=2, cost is at least80. These exhaust the nonnegative
integer possibilities. The three-tier1 list attains45, establishing the
minimum and the claimed minimizing list up to the indistinguishable copies.

Before the round2 purchases settle, they are absent from the public roster.
A deterministic observing policy whose previous observations agree therefore
cannot choose a different round2 submission because of this pending list.
The earliest public response to the new roster is round3. This statement
concerns information timing, not equality of the later states: the purchase
also changes factories, damage, bounties and future income.

## Scope and dependencies

A turret makes the predicate false regardless of roster cost, and every
round after5 makes it false. First-round roster entries are excluded from
the sum. Additional later purchases change the sum, and expired entries no
longer contribute. The theorem does not assume that the predicate is a sound
classifier of intentions, that a false result causes a particular insurance
purchase, or that crossing it improves the attacking player's outcome.

Dependencies are v24.py, the unchanged configuration, accepted roster creation,
public observations and roster expiration. Original-engine prefixes check
the exact costs, all six declared bait lists, both assignments, the boundary
and a visible-turret intervention. Full-game tests are separate empirical
hypotheses. Verification artifacts and source hashes are kept in verification/.
There is no machine-checked formalization.
