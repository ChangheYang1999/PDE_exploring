# Early walls in complete games

Checked 2026-10-31T18:17:58.495805+00:00.

The predeclared strict-win claim for guard00 against its updated public-state forecaster is REFUTED. The separate claim that some fixed witness avoids loss on all four teammate opponents is CONFIRMED. All eighty declared conditions are included.

Each policy uses a registered wall layout in round one or two, its selected guard turret in round three, a tier4 purchase in round four when affordable, and the frozen Fortress38 continuation from round five. The earlier component established a feasible cash and defense schedule. This comparison measures the resulting complete games.

Cells give policy outcome, policy:opponent HP and ending round. Equal assignments share a cell. The last column uses a separately updated matching model for each row; it is one fixed attack setting, round three and tier2.

| Witness | best_v9e | Fortress41 | V33C | P5TNUBM | Matching clone |
|---|---|---|---|---|---|
| guard00 | W 770:740 r50 | W 780:740 r50 | W 770:740 r50 | W 770:740 r50 | D 800:800 r50 |
| guard01 | L -210:740 r13 | L -60:740 r12 | L -210:740 r14 | L -350:740 r13 | D 800:800 r50 |
| guard02 | L -1356:740 r16 | L -366:740 r14 | L -630:740 r19 | L -1356:740 r16 | D 800:800 r50 |
| guard03 | L -210:740 r13 | L -60:740 r12 | L -210:740 r14 | L -350:740 r13 | D 800:800 r50 |
| guard04 | L -1190:740 r15 | L -200:740 r13 | L -1190:740 r16 | L -1190:740 r15 | D 800:800 r50 |
| guard05 | L -1190:740 r15 | L -200:740 r13 | L -1190:740 r16 | L -1190:740 r15 | D 800:800 r50 |
| guard06 | L -690:740 r13 | L -540:740 r13 | L -270:740 r14 | L -690:740 r13 | D 800:800 r50 |
| guard07 | L -690:740 r13 | L -540:740 r13 | L -270:740 r14 | L -690:740 r13 | D 800:800 r50 |

Witnesses with no teammate loss: guard00. Choosing among these rows after reading the table is development selection, not held-out validation.

All 3972 freshly regenerated decisions across both policies agree with the recorded actions. The clone audit additionally checks 800 fresh forecasts against actual target actions and original incoming combat. Original-engine replay, complete registered source and data archives, legal submissions and observation immutability checks pass. The guard filtered 0 proposed actions before submission; these are recorded separately from rejected engine actions, of which there were none.

40 of forty physical-assignment pairs have identical complete canonical histories. These are deterministic reproducibility checks. The independent conditions vary the witness and opposing policy, not a random seed.

| Witness | Calls | Total policy decision seconds | Largest policy decision seconds |
|---|---:|---:|---:|
| guard00 | 500 | 99.955960 | 0.560054 |
| guard01 | 204 | 56.248261 | 1.349574 |
| guard02 | 230 | 66.934098 | 1.688059 |
| guard03 | 204 | 55.955181 | 1.570777 |
| guard04 | 218 | 52.121571 | 0.970623 |
| guard05 | 218 | 52.869976 | 1.630097 |
| guard06 | 206 | 57.239688 | 1.594448 |
| guard07 | 206 | 56.604440 | 1.568339 |

Timing covers actual game decisions, excluding subsequent audit replay. All games used one assigned CPU core at low priority with one numerical thread on the shared machine. These timings are execution measurements, not hardware-independent complexity bounds.

The matching forecaster is allowed to decline a purchase that cannot damage its predicted defense. A draw in this column therefore does not mean four tier2 copies were submitted in that game; the direct four-copy defense was checked separately in the earlier-wall component. Other attack rounds, tiers, mixed rosters and adaptive opponents remain outside this matrix.

Reproduce the sixteen manifests listed in early-wall-campaigns-001.json with modules bot_research.experiments.validation.run_data_development (teammates) or bot_research.experiments.validation.run_data_forecasts (clones). Run audit_development_strict, replay_audit, audit_data_archives and check_early_wall_histories for each campaign; clone campaigns also require check_timing_forecaster_histories. Exact bounded commands are retained in runs/validation/early-wall-team-001-pipeline.log and early-wall-clone-001-pipeline.log. Use the existing Python with bytecode disabled, research temporary directory, assigned affinity, low priority and one numerical thread.
