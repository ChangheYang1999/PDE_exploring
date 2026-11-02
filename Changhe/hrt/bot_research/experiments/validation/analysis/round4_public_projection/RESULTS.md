# Round-four selection from a public HP projection

Checked 2026-10-31T16:23:07.306650+00:00.

CONFIRMED: the selector beats all four declared nominee opening-count variants. REFUTED: a positive one-round projected lead suffices to select a winning complete policy.

Counter outcomes over forty-eight games per mode: project_adaptive: 38W/0D/10L; project_early: 34W/0D/14L; project_growth: 32W/8D/8L.

The selector delays commitment to round four. It evaluates the proposed corner gun and tier4 against the visible enemy roster and map, assuming no new enemy actions that round. It chooses this early strike only when that calculation gives a positive surviving HP lead, and otherwise continues growth through round six and hands defense to the frozen fortress in round ten. The early branch uses joint wall/turret planning after taking a lead. Both branches have the same first three rounds.

The four changed-opening targets beaten by the adaptive mode are P5M_poke0, P5M_poke2, P5M_poke3, P5M_poke4. Counterexamples where the selected policy loses but its alternative wins are recorded below. Changing the branch planner as well as the selection time means this is not a one-factor comparison with the previous exact-count selector.

- `E25RM`: selected early, target-first HP (320, -9); alternative project_growth, target-first HP (-40, 618).
- `E30`: selected early, target-first HP (320, -9); alternative project_growth, target-first HP (-40, 618).
- `eco3_t1`: selected early, target-first HP (420, -410); alternative project_growth, target-first HP (-40, 800).

Every row below represents both physical assignments, with identical normalized histories. HP and outcomes are from the target's perspective, while projected lead is from the counter's perspective.

| Target | Counter | Selected branch | Projected lead | Target outcome | HP target:counter | Final round |
|---|---|---|---:|---|---|---:|
| P4TNUB | project_adaptive | early | 15 | L | 740:755 | 50 |
| P4TNUB | project_early | early | 15 | L | 740:755 | 50 |
| P4TNUB | project_growth | growth | 15 | L | 520:755 | 50 |
| P5TNUBM | project_adaptive | early | 15 | L | 740:755 | 50 |
| P5TNUBM | project_early | early | 15 | L | 740:755 | 50 |
| P5TNUBM | project_growth | growth | 15 | W | 800:755 | 50 |
| best_v9e | project_adaptive | early | 15 | L | 740:755 | 50 |
| best_v9e | project_early | early | 15 | L | 740:755 | 50 |
| best_v9e | project_growth | growth | 15 | L | 520:755 | 50 |
| F36 | project_adaptive | early | 25 | L | 740:765 | 50 |
| F36 | project_early | early | 25 | L | 740:765 | 50 |
| F36 | project_growth | growth | 25 | L | 240:765 | 50 |
| F37 | project_adaptive | early | 25 | L | 740:765 | 50 |
| F37 | project_early | early | 25 | L | 740:765 | 50 |
| F37 | project_growth | growth | 25 | L | 520:739 | 50 |
| lead8 | project_adaptive | early | 60 | W | 500:380 | 50 |
| lead8 | project_early | early | 60 | W | 500:380 | 50 |
| lead8 | project_growth | growth | 60 | D | -40:-40 | 8 |
| E25RM | project_adaptive | early | 10 | W | 320:-9 | 14 |
| E25RM | project_early | early | 10 | W | 320:-9 | 14 |
| E25RM | project_growth | growth | 10 | L | -40:618 | 10 |
| E30 | project_adaptive | early | 10 | W | 320:-9 | 14 |
| E30 | project_early | early | 10 | W | 320:-9 | 14 |
| E30 | project_growth | growth | 10 | L | -40:618 | 10 |
| rush_t1 | project_adaptive | growth | -145 | L | -40:650 | 8 |
| rush_t1 | project_early | early | -145 | W | 80:-305 | 8 |
| rush_t1 | project_growth | growth | -145 | L | -40:650 | 8 |
| rush_t2 | project_adaptive | growth | -96 | L | -40:560 | 8 |
| rush_t2 | project_early | early | -96 | L | -260:248 | 9 |
| rush_t2 | project_growth | growth | -96 | L | -40:560 | 8 |
| rush_t3 | project_adaptive | growth | -44 | L | -40:462 | 8 |
| rush_t3 | project_early | early | -44 | L | -180:514 | 10 |
| rush_t3 | project_growth | growth | -44 | L | -40:462 | 8 |
| heavy_t4 | project_adaptive | early | 60 | L | 80:680 | 50 |
| heavy_t4 | project_early | early | 60 | L | 80:680 | 50 |
| heavy_t4 | project_growth | growth | 60 | L | -40:800 | 8 |
| eco3_t1 | project_adaptive | early | 60 | W | 420:-410 | 7 |
| eco3_t1 | project_early | early | 60 | W | 420:-410 | 7 |
| eco3_t1 | project_growth | growth | 60 | L | -40:800 | 8 |
| eco5_t1 | project_adaptive | early | 60 | L | 80:770 | 50 |
| eco5_t1 | project_early | early | 60 | L | 80:770 | 50 |
| eco5_t1 | project_growth | growth | 60 | L | -40:800 | 8 |
| eco5_t3 | project_adaptive | early | 60 | L | 80:722 | 50 |
| eco5_t3 | project_early | early | 60 | L | 80:722 | 50 |
| eco5_t3 | project_growth | growth | 60 | D | -40:-526 | 8 |
| eco6_t5 | project_adaptive | early | 60 | W | 80:-180 | 16 |
| eco6_t5 | project_early | early | 60 | W | 80:-180 | 16 |
| eco6_t5 | project_growth | growth | 60 | D | -40:-40 | 8 |
| splash_t2 | project_adaptive | early | 60 | L | 80:764 | 50 |
| splash_t2 | project_early | early | 60 | L | 80:764 | 50 |
| splash_t2 | project_growth | growth | 60 | L | -40:728 | 8 |
| splash3_t4 | project_adaptive | early | 60 | L | 80:260 | 50 |
| splash3_t4 | project_early | early | 60 | L | 80:260 | 50 |
| splash3_t4 | project_growth | growth | 60 | L | -40:620 | 8 |
| gun_t3 | project_adaptive | early | 60 | L | 80:618 | 50 |
| gun_t3 | project_early | early | 60 | L | 80:618 | 50 |
| gun_t3 | project_growth | growth | 60 | L | -40:540 | 8 |
| mixed5 | project_adaptive | early | 60 | L | 80:440 | 50 |
| mixed5 | project_early | early | 60 | L | 80:440 | 50 |
| mixed5 | project_growth | growth | 60 | D | -40:-40 | 8 |
| P5M_poke0 | project_adaptive | early | 60 | L | 740:800 | 50 |
| P5M_poke0 | project_early | early | 60 | L | 740:800 | 50 |
| P5M_poke0 | project_growth | growth | 60 | W | 800:566 | 50 |
| P5M_poke2 | project_adaptive | early | 30 | L | 740:770 | 50 |
| P5M_poke2 | project_early | early | 30 | L | 740:770 | 50 |
| P5M_poke2 | project_growth | growth | 30 | W | 800:692 | 50 |
| P5M_poke3 | project_adaptive | early | 15 | L | 740:755 | 50 |
| P5M_poke3 | project_early | early | 15 | L | 740:755 | 50 |
| P5M_poke3 | project_growth | growth | 15 | W | 800:755 | 50 |
| P5M_poke4 | project_adaptive | growth | -5 | L | 660:740 | 50 |
| P5M_poke4 | project_early | early | -5 | W | 740:-184 | 12 |
| P5M_poke4 | project_growth | growth | -5 | L | 660:740 | 50 |

All144 full games pass strict accounting, original-engine action replay, source/data pinning and fresh policy regeneration. All4778 freshly generated counter decisions reproduce; local wrappers filter1728 proposals before submission. There are no submitted illegal actions or bot errors. All72 assignment pairs and96 declared complete-history controls agree exactly. The controls comprise48 selected-branch comparisons and48 old growth-branch comparisons; they add no independent strength samples.

The separate48-prefix component check validates the local projection against an actual original-engine round with no new enemy action. That conditional result does not predict the opponent's hidden current purchase or later adaptation. The first component implementation double-subtracted mutable HP; it was corrected and rechecked before any of these full games, as documented in COMPONENT_CORRECTION.md.

All targets and opening variants were disclosed development conditions. The fixed branch and feature choices were informed by earlier failures. The growth delegate retains a three-second planner cutoff, so the observed exact reproducibility is not an unconditional load-independence claim. These development conditions were declared before the separate pool C validation began.

Reproduction: use the three declared manifests with run_data_development, followed by audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_projection_histories and compare_recorded_controls. Use the supplied Python environment from the project root, disabled bytecode, bot_research/tmp, assigned affinity, one thread and low priority. The campaign pipeline logs contain the exact commands.
