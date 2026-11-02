# Feasible defenses at the first wall-signal leak

Declared 2026-10-31T19:36:26.457451+00:00, before the alternative planning calls.

## Exact question and selected states

Take the seat-zero attacker against H in three completed subcampaigns: the twenty-wall round-three tier2 attack (wall-signal-20-001), round-three tier3 (wall-signal-delayed-00-001), and round-four tier3 (wall-signal-delayed-01-001). In each select the earliest round with positive received base damage. These are deliberately selected failure states, not independent validation conditions. Their private H predictions were already checked against the opponent's actual action stream.

H1: at each selected state, the recorded private forecast correctly predicts positive residual damage and an alternative legal construction plan fits the same initial gold and prevents all base damage from that same opponent action list. The candidate witness searches are fixed in advance: the frozen economy-v17 free planner with max_steps=30 and the predicted active enemy roster; and the construction actions of a fresh frozen Fortress38 instance with attack=none, round1_poke=0 and replan_iters=5000 on the unmodified public observation. Preserve both proposals and outcomes. A valid witness for each state confirms the existential claim. A failed search leaves existence OPEN, because neither planner is exhaustive.

## Acceptance argument

Replay each prefix through the unchanged original Engine and require exact equality with every original record. Verify the original round and private forecast again from their retained bytes. At the same prefix, replace only the attacker's current action list by one proposed construction list. Require every action to be accepted on a player state reconstructed from its public observation. Then play both current lists through a fresh original Engine. Zero received base damage is a finite witness of feasibility under the fixed opponent response. Earlier action lists, initial gold, rosters and map geometry are identical.

This is a conditional one-round construction witness. It does not define or evaluate a complete bot, prove that the opponent would keep its future actions, or establish a winning continuation. The predicted roster is legitimate information only to the extent that the already synchronized private H model remains exact. The first-leak selection is stated explicitly and cannot support average-case performance claims. The original failed full games remain failed.

## Dependencies and scope

Sources are the three result and replay files, their completed private-forecast receipts, the unchanged engine, and the two frozen planners. All are pinned before planning. Store observations, candidate actions, per-action acceptance, budgets, runtime and complete alternative round records. No installed best.py, terminal-pool policy, server, JavaScript, remote compute or protected-file edit is used.
