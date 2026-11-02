# Round-four offense or additional factories

Checked 2026-10-31T18:50:56.352842+00:00.

H1, no round-four purchase avoids both hp_handoff losses: REFUTED. H2, one variant weakly improves every condition and strictly improves at least one: REFUTED.

The no-purchase and tier3 variants retain the early walls, round-three splash and round-five Fortress38 continuation. Remaining round-four gold follows the original factory loop. All 28 new games and fourteen reused control conditions are included.

| Target | Round-four choice | Control | Intervention |
|---|---|---|---|
| P5TNUBM | none | W 770:740 r50 | L 770:800 r50 |
| V33C | none | W 770:740 r50 | L 770:800 r50 |
| best_v9e | none | W 770:740 r50 | L 770:800 r50 |
| delegated_adaptive | none | D 740:740 r50 | L 740:774 r50 |
| delegated_early | none | D 740:740 r50 | L 740:774 r50 |
| fortress41 | none | W 780:740 r50 | L 780:800 r50 |
| lead8 | none | L 380:500 r50 | L 660:788 r50 |
| P5TNUBM | tier3 | W 770:740 r50 | L 770:774 r50 |
| V33C | tier3 | W 770:740 r50 | L 770:774 r50 |
| best_v9e | tier3 | W 770:740 r50 | L 770:774 r50 |
| delegated_adaptive | tier3 | D 740:740 r50 | L 740:774 r50 |
| delegated_early | tier3 | D 740:740 r50 | L 740:774 r50 |
| fortress41 | tier3 | W 780:740 r50 | W 780:774 r50 |
| lead8 | tier3 | L 380:500 r50 | L 520:684 r50 |

The first three complete rounds agree with the original control in all 28 comparisons. All 2800 freshly regenerated decisions agree with the recorded actions; original-engine replay, source archives, exact data registration, action legality and observation immutability pass. There were 0 filtered proposals. 14 of fourteen new assignment pairs have identical complete canonical histories.

The component check includes eight control prefixes and sixteen intervention prefixes. The tier4 implementation exactly reproduces the original on all eight five-round fixtures. Full per-round snapshots, actions, combat summaries, W/D/L transitions and any regressions are retained in verification/full_games.json.

Changes include outgoing damage, bounty income, additional factories and all later responses. Shared continuation code does not isolate any one of those mechanisms. These targets and intervention choices were selected using previous development outcomes, so this is a controlled development comparison, not untouched validation or evidence of universal superiority.

Reproduce the four manifests listed in early-wall-attack-campaigns-001.json and run the component, source, replay and fresh-policy audits shown in runs/validation/early-wall-attack-001-pipeline.log. Use the supplied Python with bytecode disabled, research-local temporary files, one low-priority assigned core and one numerical thread.
