# The first early-wall guard against updated timing forecasters

Declared 2026-10-31T17:59:04.099458+00:00, before this extended timing matrix.

## Fixed target and exact claims

The target remains the unchanged EarlyWallGuard(witness="guard00"). Test every one of the twenty timing settings used in delegated_forecaster and forced_early_forecaster, in both physical assignments. The ten round/tier pairs are (3,tier2), (3,tier3), (4,tier3), (4,tier4), (5,tier3), (5,tier4), (6,tier4), (7,tier4), (7,tier5), (8,tier5). Each uses defense_first=false and true, attack_share=1 and count_cap=200. For each target the attacker privately instantiates that target's exact policy, including witness or branch parameters. These are forty new games, with eighty old matching-setting games used as explicit controls.

H1: guard00 avoids defeat in all forty games. H2: guard00's W/D/L outcome is never worse than the forced-early delegated target on the matching setting and assignment, and is strictly better at least once. Also report every transition from the adaptive delegated target without making a separate selection rule from those results. W/D/L order is L < D < W. A single regression refutes H2, even if the total win or nonloss count improves.

The known round-three/tier2/defense_first=false guard00 pair from early_wall_policy is repeated explicitly as an end-to-end reproducibility control; it is not an extra independent observation. Its earlier outcome was a draw. All other nineteen settings are new for this target at this declaration. The guard was selected by the earlier component ranking and then expanded after eight teammate wins; this remains development research.

## Why the private model is legitimate

The attacker receives the same public observation as any bot. To predict its opponent's decision at round r, it gives a privately instantiated target the public observation with that opponent's player index, advanced through preceding public history. It has no live engine reference or pending opponent action. Conditional on synchronized target state and deterministic target computations, induction on the rounds makes the private target state equal to the actual target state immediately before each decision. The same input then gives the same action. This is a conditional prediction argument, not a claim that a shared machine makes wall-clock-limited planners deterministic. Each actual predicted action is checked against the independently regenerated target action and the recorded action.

Given both predicted submissions, the attacker's own placement is a private computation. The unchanged original combat routine checks its forecast residual against the real incoming combat. Exact prediction does not establish a globally best response: the attacker considers only its programmed timing, tier and finite purchase rule. Retuning its model when the target changes means the paired controls compare vulnerability to a matching-model adversary family, not performance against one unchanged opposing policy.

## Gates and dependencies

Before new complete games, independently check eight prefixes through round eight: four representative settings in both assignments, namely (3,tier2,false), (4,tier3,true), (5,tier4,false), and (8,tier5,true). Verify actual and predicted target actions, original incoming combat, legal submissions and unchanged inputs. Preserve any component failure and stop dependent games until explained. The existing sixteen early-wall prefixes and direct four-tier2 budget/defense component remain separate evidence.

Full games use the original engine and configuration. Require complete strict accounting, both assignments, archived source and every JSON input, original-engine replay, fresh reconstruction of both complete policies, and fresh forecast checks. Record actual attack counts so an unaffordable or rejected attack hypothesis is not counted as a successful strike. Report final HP, ending round, filtered guard proposals, errors, rejections and actual decision times. Dependencies are early_wall_policy/PROOF.md, early_wall_guard_001.json, early_wall_guard.py, the stateful public timing implementation, and the complete old control receipts.
