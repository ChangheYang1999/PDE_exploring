# Testing the complete active roster in a timed guard search

## Exact statement

Use the bundled balanced rules, the empty-map splash guards at (10,1) and
(1,0), and the prefix of three tier1 followed by two tier2. For an extension
by one or two guns, test the complete ordered roster consisting of this
prefix followed by N copies of one tier, for N=1 or60. An accepted witness
must have zero arrivals when the appended roster is one tier3, positive
damage for sixty tier3, and tier3 among the top two damage-per-new-cost
choices over tier3, tier4, tier5 at N=60. These claims concern exactly those
ordered combat inputs, not an isolated copy or every possible active roster.

## Argument

The first three entries are the round1 poke; the next two are the round6
attack in the recorded P5TF history. All are active in round9 because the
roster lifespan is twelve rounds. With no prior expirations they occupy
active indices zero through four. A new tier3 occupies index five and spawns
at tick five. Moving this index to zero would change both the firing times
and the targets selected by the guns, even though the prefix causes no
base damage through the two splash guards.

Reconstruct the entire ordered list with active entries in a fresh player
state and run the original simulate_map on the original shortest path after
legally constructing each gun extension. Its returned hits and damage then
refer to precisely this input. Compare integer damage divided by the cost
of the sixty appended entries for the three choices. Requiring the stated
conditions establishes the finite-input claim. The original prefix alone
must also be checked to cause zero base damage, so these numerators are
incremental relative to that exact prefix.

This argument does not infer a full-game win. During a game, construction
spending changes attacks, income and future roster order. A correct witness
can still lose for those reasons. The real policy applies every construction
action to a private copy of its visible state to check affordability.

## Development hypothesis and scope

The preceding homogeneous-roster guard lost because earlier cheap entries
screened the new tier3 from gun fire. Search the same finite family with the
complete prefix and test the new witness in rounds9 and10 against exact
P5TF and current attacks. Component and full-game evidence are separate.
No arbitrary-map optimum or proof-assistant formalization is claimed.
