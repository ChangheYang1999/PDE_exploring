# One additional attack against an empty public roster

## Statement, notation and empirical hypotheses

Let G be the fixed EarlyWallGuard("guard00") policy from result 114. It builds its walls in round one, its first splash turret in round three, buys one tier4 in round four when affordable, and uses frozen Fortress38 from round five. The unchanged balanced engine, normal initial state and both physical player assignments are used throughout.

Define G(P) by one additional decision rule: at round five only, if the opponent has no roster entry active in that round, sequentially buy the affordable prefix of package P before invoking the same Fortress38 continuation. The three packages fixed before execution are one tier3, two tier3, and one tier4. Purchases are made in the listed order. The continuation receives a private observation copy whose own gold and roster include these purchases; all other fields are unchanged. Its legal actions follow the package. In every other case call G without changing its actions or observation. This is planning from the public observation and the bot's proposed own actions, not access to any hidden opponent submission.

The five opponents are the exact previously measured best_v9e, Fortress41, P5TNUBM with r1_poke=0, hp_handoff with lead_from=8 and deadline=12, and bait_guard_A specifications. Their complete strings and the ten old control paths are recorded in the declaration. Thirty new games cover all three packages and both assignments. Old controls are reused explicitly, not counted as new games.

H1: at least one package avoids both G losses against P5TNUBM with r1_poke=0 and hp_handoff in both assignments, without any W/D/L regression on the other six conditions. H2: for every package, all complete histories for the three other opponents are identical to their control histories because the rule never triggers. W/D/L is ordered L < D < W. Publish all thirty conditions even if either claim fails.

## Conditional equivalence and validity argument

Before round five, the new rule never runs, so the implementation delegates directly to G on the actual observation. Given the same opponent policy state and observations, the deterministic engine therefore produces the same first four complete rounds. On round five, if the opponent has an active entry, the implementation again delegates directly. The only branch difference has now expired. Induction on later rounds proves identical complete histories whenever the round-five predicate is false, provided the component implementation is correct and both opponent policies are deterministic under these calls.

If the predicate is true, construct a new local PlayerState from the public own snapshot. Every proposed purchase is passed through the original apply_action in order, so acceptance ensures affordability, correct roster lifetime and sequential legality under the unchanged rules. The continuation receives a deep copy of the actual observation with exactly the local own gold and roster substituted. Its roster remaining_rounds fields use the observation's last completed round (current round minus one), matching the original snapshot convention. Other own fields do not change under minion purchase. The opponent observation is untouched. Check every continuation proposal on the same local state before returning accepted actions. This establishes the legality of the returned sequence on the observed pre-action state: another player's interleaved purchases do not alter this player's gold, buildings or roster. The returned list contains only ordinary game actions.

The predicate uses only the public current round and opponent roster lifetimes. It never reads the opponent name, module, pending actions, live engine or unrelated files. The fixed JSON witness is a registered policy dependency.

## Implementation checks and full verification

Before full games, compare a disabled package with G on eight six-round legal prefixes: four simple fixed growth/strike policies and both assignments. For the three packages, check the same twenty-four prefixes. Verify identical first four rounds, complete equality when the predicate is false, legal submitted actions, unmodified observations, correctly recorded package actions and zero filtered continuation proposals. A disabled package must reproduce G exactly through all six rounds.

Freeze source and JSON dependencies before any component or full-game call. For each full game retain original-engine records, exact condition and source attestations, errors, rejected actions, runtime and outcome. Independently replay every record and regenerate both policies from their public histories. Compare the unchanged prefix and all nontriggered control histories. The correctness argument is conditional on the stated code checks and inputs; the strength claims are finite empirical questions, not proofs of optimal play.

## Motivation and scope

Result 115 records G losing 380:500 to hp_handoff and 722:740 to the no-poke P5TNUBM variant. In both controls the opponent's round-five public roster is empty. G has 264 gold then, including the preceding heavy hit's bounty, so each declared package is affordable on those histories. Spending this gold can reduce later factory income and defensive capacity. The follow-up tests that tradeoff rather than assuming more early attack is better.

These targets and packages were chosen after reading development outcomes. This is a targeted development experiment and leaves the installed best.py and terminal reserve D unchanged. Dependencies: results 114 and 115, the frozen Fortress38 continuation, the original balanced configuration, and the original Engine/apply_action semantics.
