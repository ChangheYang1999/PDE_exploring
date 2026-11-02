# A public first-roster selector between two counters

## Statement and policy

This is a development hypothesis, not a general opponent-classification theorem. The early branch is the fixed half-budget GuardedRound4Trigger that has beaten P4TNUB, P5TNUBM and best_v9e. The growth branch is GuardHandoff with six growth rounds, no bait, an empty starting wall layout, the fixed two splash guards, the round-nine gun extension, and handoff round10. Its frozen defender uses a fixed 5000-iteration replan and retains its inherited wall-clock cutoff.

The adaptive policy submits the common first-round action list. At its first decision after round1, it counts the public opponent roster entries of type tier1 bought in round1. It chooses the early branch if this count is at least3 and the growth branch otherwise, retaining that choice for the rest of the game. It never reads an opponent name, source identity, model, pending action or private state. The feature and threshold were chosen from development histories. Neither the feature nor the target pool is held out.

## Common-prefix and legality proof

On the bundled standard start, both branches start with an empty map, no minions, 100 gold, no bait and a growth horizon exceeding round1. No timed turret, strike or handoff applies. Each therefore buys floor(100/20)=5 factories and does nothing else. Neither sees the opponent's first-round purchases before returning these actions. The adaptive policy calls both branches on separate copies in round1, checks that the action lists agree, and returns that list. Both branch instances have then received the same legitimate observation they would receive if used alone.

At round2 the roster is public and includes bought_round. The count is therefore a function of the permitted observation. Selecting a branch does not change the actual state: both branch histories agree through round1. From that point, return only the selected branch's actions. Induction shows that its private state has been advanced by exactly its own observed history and that all submitted actions are those of a legal branch policy. The inherited branch validators establish owner-local legality. The wrapper makes deep copies and does not mutate its supplied observation.

Forced early and forced growth modes instantiate the same branches and select the named branch before any decision. With deterministic branch decisions and equal observations, the adaptive full history equals that of the branch it selects. Because the inherited growth planner has a wall-clock cutoff, empirical equality is checked explicitly and is not inferred under arbitrary machine load. No mixed strategy or equilibrium result follows from this selector.

## Tests and limits

Before outcomes, declare48 complete standard-start games: eight previously studied targets, adaptive/forced-early/forced-growth modes, and both assignments. Record all outcomes and all attempts. Verify original-engine replay, legal actions, unchanged observations, exact fresh policy decisions and the visible feature at selection. Compare adaptive histories to both forced controls and identify the selected match explicitly. The hypothesis is that adaptive selection beats more of this finite development set than either fixed branch. No improvement outside these eight targets is claimed. Pool C is untouched.
