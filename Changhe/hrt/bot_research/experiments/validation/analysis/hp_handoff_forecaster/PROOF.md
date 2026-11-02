# Timing attacks on the five-policy table's unbeaten grower

## Fixed question and conditions

Let H be precisely the HP-triggered grower in extended-counter-game-campaigns-001.json: the empty-layout guarded opening, six growth rounds, no bait, tier5 purchases, factory cap 2000, purchase cap 1000, 5000 replanning iterations, a round-eight positive-HP-lead trigger and a round-twelve deadline. Its source and parameters are frozen. H has no loss in the completed five-policy table, whose value certificate applies only to those five policies.

The new hypothesis is that H also has no loss against each of twelve matching-model timing policies in both physical assignments, from the standard initial state. The six round/tier pairs are (3,tier2), (3,tier3), (4,tier3), (4,tier4), (5,tier3), (5,tier4), each with defense_first=false and true. Every attacker uses attack_share=1, count_cap=200 and the existing remaining defaults. Twenty-four new games are declared. There is no change to H or to an attacker after its game starts. A single H loss refutes this empirical hypothesis.

Each attacker retains a private H clone, called exactly once per reached round on the public observation with the player index swapped. This is a targeted development challenge selected after seeing the five-policy result. It is neither an untouched validation set nor a general best-response search. A policy identified by this challenge may be investigated later only as a newly selected counter, with that selection stated.

## Prediction argument

Assume the target and private clone start with the same parameters and state, receive identical public observations at each decision, and compute deterministically. Induction on reached rounds makes their internal states and actions identical. No access to a live opponent, pending action or hidden engine state is needed. In this implementation the clone receives a deep copy of the public observation; its state persists across consecutive rounds. The counter's own action may then be selected using that legitimate prediction.

This argument is conditional because wall-clock-bounded planning may vary under load. The actual experiment must compare every predicted action with the recorded target action. A mismatch remains a failure of prediction, even if the game's W/D/L outcome is valid. The attacker's finite purchase heuristic is not proved optimal. A declined purchase with nonpositive predicted gain is recorded, rather than interpreted as a successful attack.

## Component and full-game checks

Before full games, verify four prefixes through round eight: round-three tier2 with defense_first=false and round-five tier4 with defense_first=true, both assignments. Independently instantiate H and its private clone, compare every action, verify both public observations remain unchanged, and compare predicted incoming damage with the original combat and Engine result. Require zero rejected submitted actions. An early terminal result ends that prefix honestly.

For each full game require a complete source/data archive, exact condition accounting, no bot error or rejected submitted action, and independent original-engine replay. Regenerate both policies from fresh instances on the entire recorded history. Separately regenerate the attacker and check its saved trace, target prediction and incoming-damage forecast on every reached round. Record H's final HP first, its W/D/L outcome, final round, real runtime and actual attack count.

The source and result hashes, all failures and both assignments are retained. No duplicate deterministic condition adds an independent random sample. Pool D and the installed best.py remain untouched. Dependencies include extended_counter_game/PROOF.md, stateful_public.py, forecast_timing.py, hp_handoff.py and their frozen implementation/data closure.
