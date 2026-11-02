# Removing three round-two tier1 purchases

Checked 2026-10-31T18:35:39.856612+00:00.

H1, at least one previous defender loss becomes a draw or win: CONFIRMED. H2, at least one defender avoids its former four A/B losses: CONFIRMED.

All 24 new conditions and all 24 audited controls are included. There are 12 repaired defender losses and 0 worsened W/D/L outcomes. All retained actions are legal in these executions.

Each cell gives the defender outcome, defender:attacker HP and ending round. Both assignments are shown together only when these quantities agree.

| Defender | Schedule | Original | Without three tier1 | First defender action difference |
|---|---|---|---|---|
| fortress41 | A | L 505:780 r50 | W 520:500 r50 | 3 |
| fortress41 | B | L 505:765 r50 | L 660:765 r50 | 3 |
| best_v9e | A | L 85:734 r50 | W 660:542 r50 | 3 |
| best_v9e | B | L 505:755 r50 | L 660:755 r50 | 3 |
| V33C | A | L 505:674 r50 | L 520:698 r50 | 3 |
| V33C | B | L 505:703 r50 | W 800:755 r50 | 3 |
| P5TNUBM | A | L 505:674 r50 | W 800:602 r50 | 3 |
| P5TNUBM | B | L 505:703 r50 | W 800:729 r50 | 3 |
| delegated_adaptive | A | W 350:-40 r8 | W 380:-40 r8 | None |
| delegated_adaptive | B | W 350:-40 r8 | W 380:-40 r8 | None |
| delegated_early | A | L 350:380 r50 | D 380:380 r50 | None |
| delegated_early | B | W 350:296 r50 | W 380:296 r50 | None |

Transitions, counted from the defender perspective: {"L->D": 2, "L->L": 6, "L->W": 10, "W->W": 6}. All 2064 new-game decisions were independently regenerated for both actual policies. All 12 assignment pairs have original histories checked; 12 new assignment pairs have identical complete canonical histories.

The only requested-schedule intervention is deleting the three tier1 purchases. The receipt checks this at every common completed round; policy-level equality at later, censored rounds is covered by the 100-round component check. Round-one records agree exactly. The receipt retains every defender and attacker action, gold balance, factory count, path length, HP and incoming damage.

This intervention changes direct damage, hit bounties and the defender's observable history together. Its result does not isolate bait-induced defensive spending from those other effects. A first defender action difference can also follow a changed HP comparison or budget. These are development conditions with known targets, not an estimate against unknown opponents.

Reproduce the six bait-removal manifests using the commands retained in runs/validation/bait-removal-001-pipeline.log. Independent original-engine replay, strict source and result accounting, complete data archives, action legality and observation immutability all pass.
