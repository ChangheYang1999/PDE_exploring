# The measured counter cycle involving best_v9b

## Exact statement and hypotheses

Fix the unchanged bundled balanced rules and the ordinary standard start.
Let B be bots.best:decide with SHA256
`dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7`.
Let E be frozen economy17 with free_fallback="zero" and
foreign_attack_from=11. Let G be GuardGeometry with roster=["tier1"] and
its unchanged default x=10, y=1 and economy17 continuation parameters.
G buys the gun and one tier1 in round 1, spends its remaining gold on
factories, and starts the fresh economy17 continuation in round 2.

The empirical premises are the six recorded games, one game per physical
assignment for each unordered pair. Every game passes the earlier strict
source, legality and original-engine replay audits. The results, stated
with the winner first, are G over B, 800:795; B over E, 795:785; and E over
G, 795:753. All six games end at the round-50 limit. The two assignment
histories for each pair are identical after player normalization.

Conditional on these audited records, no one of B, E and G beats every
other policy in this measured three-policy set. These records do not define
self-play entries or a complete empirical game matrix.

## Argument

Suppose B beat every other listed policy. Its recorded loss to G contradicts
that assertion. Suppose E beat every other listed policy. Its recorded loss
to B contradicts that assertion. Finally G loses to E. Each candidate for a
policy that beats both alternatives therefore has a recorded counterexample.
The three directed winning edges form the cycle G -> B -> E -> G.

The evidence extractor checks the exact policy specifications across the
three pairs, the strict result hashes, the corresponding successful replay
receipts and their input hashes, and the current source attestations. It
also checks that the live best source and frozen best_v9b source have the
same registered hash. It runs no new game. This guards against accidentally
combining different guard parameters or different versions of the lead bot.

## Dependencies, verification and limits

The six games are selected from best-v9b-counter-model-free-001 and
guard-geometry-transfer-001. The index is
runs/validation/best-v9b-counter-cycle-index-001.json. Verification/evidence.json
records its hash and the extractor hash. The original replay receipts remain
in their respective campaigns.

This is a retrospective empirical result, not a proof about all legal
opponents or starts. It supplies three distinct paired conditions, not six
independent random samples. The small HP margins matter for the exact
round-limit outcome but do not establish resilience to rule changes.
No randomized mixture or unique equilibrium is claimed here. The separate
counter_cycle/PROOF.md theorem would require its complete stated matrix,
including diagonal entries. No proof-assistant formalization is claimed.
