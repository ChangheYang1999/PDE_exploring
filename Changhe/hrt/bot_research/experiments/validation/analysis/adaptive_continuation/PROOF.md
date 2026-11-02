# Adaptive catalogue with a fresh continuation

## Statement and hypotheses

Let A be the existing AdaptiveCatalogue policy and E the frozen economy20 factory with CONTINUATION_PARAMETERS from catalogue_continuation.py. Every invocation receives only the public observation. Calls begin at round 1, occur exactly once per consecutive reached round, and retain one fixed player index. Assume the component policies have no external effects and do not mutate the supplied observation.

Define C as follows. Until the catalogue is empty, invoke A on the current observation. If the invocation retains at least one model, return exactly its actions. If it first empties the catalogue at round s, discard its proposed actions, initialize one fresh E, and return E's actions on that same observation. At each subsequent round invoke only that E once. Reset both mechanisms at the next round-1 call. Trace annotations have no effect on actions or policy state.

If an opponent satisfies all true-member and synchronized-state hypotheses of ../stateful_catalogue/PROOF.md, C has exactly the same complete trajectory as A from the same initial game state against that opponent. The conditional current-round adaptive-attack statements apply on every retained-model round. Against an outside opponent, after round s, C returns the actions of a fresh E receiving exactly the public observation sequence from s onwards. None of these statements asserts that the outside continuation is stronger.

## Argument

Initially A has the same constructor parameters and private state in C as in its direct use. Under the true-member hypotheses, the retention theorem prevents the catalogue from becoming empty. On each reached round C therefore returns the unmodified actions of A. By induction, the unchanged engine receives the same two action lists in the two comparisons, produces the same public states, and supplies the same next observations. The private state of A advances once per round in both comparisons. Hence the complete trajectories agree, and the adaptive-attack proof applies with the same fixed construction and forecast values.

For an outside opponent, suppose s is the first round with an empty retained set. Earlier parent calls have the stipulated effect. The parent proposal at s is not submitted to the engine. C creates a fresh E exactly then, makes one call with the actual round-s observation, and returns those actions. Inductively, at each later round C calls that same E once with the actual next public observation and returns its result. The discarded parent no longer runs. This proves equality with the stated fresh continuation on the actual observation sequence, without asserting equality to economy20 played from round 1.

Replacing trace fields describing the unused parent attack by an explicit disabled marker does not alter any action or state transition. Actual continuation purchases are counted separately and no marginal-damage certificate is assigned to them.

## Dependencies, limitations, and verification plan

Dependencies are ../stateful_catalogue/PROOF.md, ../catalogue_attack_selection/PROOF.md, ../catalogue_continuation/PROOF.md, and deterministic engine transitions. True catalogue membership is essential for the first claim. The second is a policy-composition identity and provides no outcome guarantee. The initial parent opening can leave E with a less favorable map or economy than direct use.

This argument was written before the new implementation. Component checks will compare the retained branch with an independent AdaptiveCatalogue on the same public observations, compare the continuation with an independently initialized E, check legal actions and input immutability, and use original combat to check executed adaptive attacks. Full-game strength requires separately declared conditions and complete replay audits. No proof-assistant formalization is claimed.
