# A public response signal chosen by the opponent

Declared 2026-10-31T19:21:38.413100+00:00, before any wall-signal policy call.

## Statement and hypotheses

Use the exact H, I and J policies from shared_prefix_response. H is the lead8/deadline12 HP grower. I is the round-three tier2 attacker with a private H model. J advances both H and I on their common first move, then chooses H if the opponent has at least twenty walls and an empty roster on round two, otherwise I. This choice stays fixed.

Construct K19 and K20 from I by replacing only its first returned factory list with the first nineteen or twenty cells of the existing guard00 wall witness, followed by as many factories as its remaining gold affords. Advance I's private H model on the first public observation before replacing the list; every later decision is I's unchanged rule on the actual history. Both policies buy no first-round minion. All parameters, wall order and source/data hashes are fixed in the two manifests before any prefix or full-game call.

H1: K20 wins against J in both assignments and the complete histories equal K20 against H after normalizing player names and physical assignment. H2: K20's outcome against J is strictly better, under W>D>L, than K19's against J and than K20's against I. Twelve full games test each of K19/K20 against J,H,I in both assignments, all from the standard start with the unchanged balanced engine. These are selected development hypotheses, not held-out predictions. A contrary complete outcome refutes the corresponding hypothesis.

## Conditional argument

The existing wall witness is legal in its recorded order. Deleting its suffix cannot disconnect a path that exists after the whole sequence: every path in the fully blocked board also exists when some of those blocks are absent. Nevertheless, replay the shorter prefixes with the original action checker to verify boundaries, costs and all other construction rules. Factories spend only remaining gold. The new policies use their own public observation and one private model initialized normally; no target object, private action or displayed name is read.

At the second observation K20 has twenty walls and no roster, so J's public predicate selects H. K19 has nineteen and no roster, so it selects I. Provided the shared-prefix determinism hypotheses in shared_prefix_response/PROOF.md hold, each selected branch has the same state as a standalone instance from round one. Induction then gives action equality on the actual history. Because dependencies have wall-clock limits, compare whole histories empirically rather than assuming their choices are deterministic under all loads.

The two adjacent wall counts are not by themselves a causal ablation of the selector: the extra wall also changes cost and possibly income. The fixed-response games supply the missing controls. Equal K20-J and K20-H histories identify H as the executed response; comparing that same K20 with I holds the attacker rule fixed. K19-J versus K19-I checks the other branch. No conclusion says wall construction alone is free or irrelevant.

## Verification and scope

Check twelve eight-round prefixes for legal actions, unchanged observations and the declared wall count. The H-model predictions must exactly match the actual target against H and against J with twenty walls; mismatches against other targets are recorded, not treated as policy errors. Then require all twelve full games, both assignments, source/data archives, strict condition accounting, original-engine replay, fresh regeneration of both external policies, and a separate attacker/forecast trace check. Report exact outcomes, final HP, ending rounds, actual purchases, model mismatches, errors, rejected actions and observed decision timings. Equal seat swaps are not independent samples.

The game result hypotheses remain OPEN until all these checks pass. Even if they hold, the conclusion is a failure of this specific threshold rule against these two selected timing policies. It does not rule out stronger public-history adaptation, establish an optimal unrestricted strategy, or use pool D. The installed best.py is not called.
