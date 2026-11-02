# Emergency continuation results

Checked 2026-10-31T16:46:32.713972+00:00.

CONFIRMED: the damage trigger preserves the baseline win and repairs the shared-prefix flood loss.

The damage-triggered continuation wins all four declared games. The disabled control wins two and loses two. Each row below covers both physical assignments, whose complete normalized trajectories agree. Outcomes and HP are from the counter's perspective.

| Target | Counter | Outcome | HP counter:target | Final round | Added trigger activates |
|---|---|---|---|---:|---|
| baseline | emergency_damage | W | 800:740 | 50 | [] |
| baseline | emergency_none | W | 800:740 | 50 | [] |
| flood | emergency_damage | W | 715:80 | 50 | [5] |
| flood | emergency_none | L | -495:420 | 7 | [] |

At the reached round-five flood state, the public current-roster projection is 85 incoming damage. The disabled policy actually receives 215 after the target's new purchases. The repair builds 20 walls and one gun2 at (9,5), then buys nine factories. That construction reduces actual incoming damage in this round to zero, leaving counter HP 715 and target HP 680. The complete repaired game ends 715:80 in round 50. The baseline target still ends 800:740 because the existing HP-lead trigger already starts defense in round five; the new condition does not activate there.

All eight component cases and eight complete games pass. The full checks cover strict accounting, original-engine replay, pinned source and data identity, legal actions, unchanged observations, and 314 freshly regenerated counter decisions. The four disabled trajectories and two repaired-baseline trajectories exactly match their previously recorded route-adaptive controls. The emergency trigger is checked independently at the reached component states. This does not claim that a current-roster projection predicts hidden purchases.

This is a third continuation after the identical opening, so it does not contradict the two-by-two commitment result in ../indistinguishable_prefix/PROOF.md. These are development conditions chosen after diagnosing that failure. No held-out strength claim or change to best_v9e follows. A separately declared 45-target transfer matrix tests whether this repair causes regressions elsewhere.

Reproduction: use run_anonymous_development with emergency-prefix-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_emergency_histories and compare_recorded_controls with emergency-prefix-controls-001.json. Run check_emergency_component for the on-history component check. Use the existing Python environment, disabled bytecode, the research temporary directory, assigned CPU affinity, one thread and low priority. verification/full_games.json pins the evidence and this publisher.
