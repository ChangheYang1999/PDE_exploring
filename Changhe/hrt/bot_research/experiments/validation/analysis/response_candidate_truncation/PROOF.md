# Truncating current-map candidates before testing a response

## Statement and notation

Fix the exact v24 attack routine, one public observation, positive new-purchase
budget, and robust mode. Let C be the list of affordable homogeneous purchases
whose incremental current-map damage divided by purchase cost is at least the
configured threshold tau. Each tier contributes its greatest allowed count,
capped by max_minions. Order C by the exact descending tuple used in v24.
Let R(c) be the total damage of the active roster plus c after the routine's
hypothetical full-budget defensive response, divided by c's purchase cost.
All these evaluations are assumed deterministic and defined.

If C has at least three entries, the first two have R(c) < tau, and a later
entry has R(c) >= tau, v24 returns no attack although at least one purchase
in its own candidate family passes its response criterion. An otherwise
identical routine evaluating every entry of C returns a nonempty purchase
with maximal R among passing entries, with v24's remaining tuple tie-breaks.

## Proof

The robust branch iterates over C[:2], evaluates R, and inserts only entries
with R >= tau into its output list. The two stipulated failures leave that
list empty. The final empty-list branch therefore returns ([], 0). No later
entry of C is evaluated in that branch.

In the untruncated routine, every element of C is visited. The stipulated
later passing element is inserted, so the retained list is nonempty. Sorting
it by the same descending tuples and returning its first element selects
a maximal response ratio, using the same further fields for ties. Thus a
nonempty attack is returned. This finite-list argument does not assume that
current-map and response rankings agree.

## Scope and empirical test

The claim is about a heuristic's internal criterion. R is total post-response
roster damage; it is not necessarily incremental, an actual opponent response,
or a certified lower bound over legal defenses. The current-map filter itself
can still omit useful attacks, and only one count per homogeneous tier is
considered. The result implies neither a game win nor a globally best attack.

The screen-aware round9 guard defeats P5TF in both standard-start assignments.
Its full-history diagnostic is still running when this proof is written.
Test whether any recorded observation meets the hypotheses, then compare
full games of the original routine, the untruncated routine, and current mode.
Use the existing guard, screen-aware guard, pure-splash ladder, heavy drip
and forecast timing as development opponents. All original-engine outcomes
and validation receipts are separate from this program argument.

The source and observation hashes belong in verification/. No proof-assistant
formalization or machine-checked theorem is claimed.
