# Public damage-triggered defense after the early strike

Written 2026-10-31T16:41:37.927860+00:00, before implementation and experiments.

## Exact policy and empirical question

Keep the existing route-gated selector, its early round-four gun1 and tier4 purchase, and its growth branch. Change only the early continuation: from round5, if defense has not yet begun and the current visible enemy roster would cause positive base damage on the current own map, activate the existing joint wall/turret defensive planner immediately. Otherwise keep the existing positive-HP-lead trigger. The projection is an original-engine local simulation on copies of public state, with no new enemy action. Let the control rule none disable this added trigger. A constant-round rule always is an optional diagnostic, not the proposed default.

The empirical hypothesis is that the damage rule preserves the early branch's win against the common-prefix baseline target and repairs its loss against the common-prefix tier1 flood. This is a third continuation, so a successful repair does not contradict the two-by-two result in ../indistinguishable_prefix/PROOF.md. Full games, not a one-round projection, are required to establish the hypothesis.

## Observation and prefix argument

Before round5 the added trigger is inactive, so the old and new early continuations have the same decisions and state relevant to decisions. The outer selector's round-four predicate is therefore unchanged. A current-damage projection reads only configured rules, the active public roster, the own visible buildings and round. It constructs independent PlayerState copies and the shortest path on the own visible map, then calls the unchanged original combat routine. Mutating the copies does not expose or change the live game. Positive simulated damage is only a condition for activating defense, not a guarantee about hidden current purchases or the outcome.

After activation, the same TemplateHandoff implementation proposes construction, checks its actions sequentially on a local copy and buys affordable factories. The wrapper must preserve those checks and record its activation reason. If the damage rule never activates before the old HP trigger, the old and new full trajectories agree, subject to reproducibility of shared planners. If rule none is selected, the new wrapper must reproduce the old policy on the whole checked history. The growth branch is unchanged, including its existing clock cutoff.

## Component and full-game checks

First recover round5 from the completed anonymous-prefix flood game with the old early branch. Verify every earlier event with the original engine. Check the visible damage value, legal proposed emergency construction, input immutability, and outgoing/incoming combat under the actual recorded target action. This is an on-history component check only. Then declare and run both target continuations against damage and none modes in both assignments, retaining all outcomes. The none histories must match the prior old early/adaptive controls. Every new full game requires strict/source/data accounting, original-engine replay and fresh regeneration of all new counter decisions.

A broader transfer matrix, if warranted, must be declared separately and retain regressions. These development tests do not alter the installed best_v9e or its completed final validation. No global robustness or optimality claim follows from a successful local repair.
