# An exact-count repair for the public roster selector

## Statement and hypotheses

The policy is PublicRosterSelector with one changed predicate: at the first decision after round1, select early if and only if the number of visible opponent tier1 entries bought in round1 equals3. Otherwise select growth. The branches and their parameters are unchanged. The previous predicate count>=3 lost to rush_t1, whose opening count is6, while its growth branch won.

## Argument

The common-opening proof and legal-branch composition proof in ../public_roster_selector/PROOF.md apply without change. The predicate depends only on the public roster, and both branches have identical first-round actions and correctly advanced private states. Replacing the predicate changes neither branch. Therefore, whenever the exact-count predicate selects the same branch as a forced-branch control, equal observations and deterministic branch decisions imply equal complete histories. The inherited wall-clock cutoff prevents an unconditional machine-independent equality claim; exact histories and fresh decisions must be checked.

## Declared evaluation

Use the eight previously studied strong targets and all twelve existing PROFILES. Run the new adaptive policy in both assignments,40 new standard games. Pair every game with its previously recorded forced branch, selecting early only for P4TNUB, P5TNUBM and best_v9e, and growth for all other targets. Verify this selection from the observed first-round roster. The expected40 history equalities are specified before new outcomes. Report all new games and the reused controls separately. This is a repair fitted to the previous development results, not held-out evidence.

## Scope

A positive result establishes only the finite set. No guarantee follows for an opponent that changes its first-round purchases. The classifier can confuse policies with the same initial feature and different later behavior. The next experiment explicitly tests that vulnerability. Pool C is unused.
