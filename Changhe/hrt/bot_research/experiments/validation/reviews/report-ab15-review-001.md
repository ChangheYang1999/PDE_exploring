# ab15 report source audit

Recorded: 2026-10-31T22:00:47.037768+00:00. Read-only inspection of development evidence. No games, policy calls, terminal-D parameters, or held-out results were used.

Claim: the ab15 row in `bot_research/reports/REPORT.md` has inconsistent outcome counts because its empty-layout, growth-7, tier2-bait example changes from HP difference +528 to -97 while it says no win becomes a loss.

Verdict: REFUTED for that alleged outcome contradiction. The example becomes a draw when both bases are destroyed. The W-D-L totals, minimum HP difference, transition counts, and statement that no win becomes a loss are all CONFIRMED against the recorded V18FT baseline. A separate naming error is CONFIRMED: the maze layouts among the wins that become draws are `empty` and `lead_opening`, not `cash_rank_1`.

Method: read every results row in ab15 and g9a-g9d without importing project modules. Select the following exact candidate strings, then join by full opponent specification, scenario, and physical candidate seat. Reject duplicate keys and require equal key sets. Determine W/D/L from `winner`, with `None` a draw; calculate candidate HP difference as `hp_diff_a` in seat 0 and its negative in seat 1. Read the final two JSONL records of all four example games and compare their round, HP snapshots, and engine result to their results rows. Read the current engine outcome rule statically. Hash all cited input files. These are checks of recorded development evidence, not fresh gameplay or a full program-equivalence proof between V18FT and frozen best_v9e.

Baseline specification:

```text
bot_research.experiments.lead.v19:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&foreign_target="econ20"
```

Ablation specification:

```text
bot_research.experiments.lead.frozen.best_v9e:@make?big_threat=null
```

The baseline appears only in `bot_research/runs/lead/g9a/results.jsonl`, lines 143-284. g9a has 568 total rows for four candidates; g9b, g9c, and g9d each have 284 rows for two other candidates. Thus the report's `g9a-g9d` points to the larger sweep, while the actual 142 baseline rows are in g9a. All 142 ab15 rows match those baseline keys exactly: 71 opponent specifications, standard starts (`scenario=null`), and 71 games in each physical seat. These are configured conditions, not a claim of 142 independent trajectories.

Result: baseline 66 W, 0 D, 76 L. ab15 88 W, 30 D, 24 L; worst candidate HP difference -735. All 30 ab15 draws have reason `both_bases_destroyed`. The full transition matrix is:

| Baseline outcome | Ablation W | Ablation D | Ablation L | Total |
| --- | ---: | ---: | ---: | ---: |
| W | 56 | 10 | 0 | 66 |
| D | 0 | 0 | 0 | 0 |
| L | 32 | 20 | 24 | 76 |
| Total | 88 | 30 | 24 | 142 |

All ten W-to-D conditions are the following five opponent specifications, each in both seats. In this table, `roster_bait` uses turret coordinates (0,2), turret round 0, bait round 2, tier5, factory cap 2000, and purchase cap 1000. `maze_grower` uses bait round 2, tier5, factory cap 2000, and purchase cap 1000. Line numbers refer to the respective `results.jsonl` files and include both physical seats.

| Opponent | Growth rounds | Bait | Baseline HP difference / end round | Ablation HP difference / end round | g9a lines | ab15 lines |
| --- | ---: | --- | --- | --- | --- | --- |
| roster_bait | 7 | three tier1 | +475 / 14 | -55 / 9 | 179-180 | 37-38 |
| roster_bait | 7 | one tier2 | +528 / 13 | -97 / 9 | 181-182 | 39-40 |
| roster_bait | 8 | two tier1 | +620 / 14 | +310 / 9 | 187-188 | 45-46 |
| maze_grower, empty | 7 | one tier2 | +528 / 13 | -97 / 9 | 235-236 | 93-94 |
| maze_grower, lead_opening | 7 | one tier2 | +388 / 13 | -237 / 9 | 259-260 | 117-118 |

The `cash_rank_1`, growth-7 cases cited in the report instead contribute six L-to-D conditions:

| Bait | Baseline HP difference / outcome | Ablation HP difference / outcome | g9a lines | ab15 lines |
| --- | --- | --- | --- | --- |
| one tier1 | -1130 / L | -505 / D | 279-280 | 137-138 |
| two tier1 | -1135 / L | -510 / D | 281-282 | 139-140 |
| one tier2 | -1132 / L | -237 / D | 283-284 | 141-142 |

The original empty-layout example is numerically correct in both seats:

| Run and results line | Candidate seat | End round | Candidate HP | Opponent HP | Candidate HP difference | Winner field | Reason |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| g9a, 235 | 0 | 13 | 228 | -300 | +528 | 0 | base_destroyed |
| g9a, 236 | 1 | 13 | 228 | -300 | +528 | 1 | base_destroyed |
| ab15, 93 | 0 | 9 | -192 | -95 | -97 | null | both_bases_destroyed |
| ab15, 94 | 1 | 9 | -192 | -95 | -97 | null | both_bases_destroyed |

The final log records agree with these rows. `td_game/engine.py`, lines 111-118, checks both HP values being at most zero first and returns `winner=None` with `reason="both_bases_destroyed"`. It does not compare the negative HP values to break this draw. In particular, -97 is an HP difference, not a loss. Every row in all five inspected result files pins the same engine SHA-256 listed below. The recorded results have zero game errors, source-change flags, rejected actions, bot errors, or scenario errors across these files.

Proposed correction: keep every numeric cell in the ab15 row. Replace `cash_rank_1` with `lead_opening`, specify that the round-9 example is a draw, and make the baseline citation precise as `V18FT in g9a, 66-0-76`. A complete replacement for the ab15 row is:

```text
| ab15 | big_threat=null (no all-gold insurance, rule 3b) | GROWERS | 88-30-24 (-735) | 32 losses become wins, 20 losses become draws, 10 wins become draws (including maze_grower empty and lead_opening with growth 7 and a tier2 bait; for empty, a round-13 win with HP difference +528 becomes a round-9 draw with both bases destroyed and HP difference -97); no win becomes a loss |
```

For an exhaustive description of the ten W-to-D conditions, use the five-row table above. The shorter proposed row says `including`, since the remaining six conditions use roster_bait.

Reviewed report row at the timestamp above:

```text
| ab15 | big_threat=null (no all-gold insurance, rule 3b) | GROWERS | 88-30-24 (-735) | 32 losses become wins, 20 losses become draws, 10 wins become draws (maze_grower empty and cash_rank_1 with growth 7, among them empty growth 7 with a tier2 bait: +528 becomes -97 at round 9); no win becomes a loss |
```

SHA-256 identities of the exact files read follow. `REPORT.md` is a working report and may subsequently change; this digest identifies the bytes reviewed here. Other source and result digests are observations, not a new seal of prior experiments.

| Relative path | SHA-256 |
| --- | --- |
| `bot_research/runs/lead/ab15/results.jsonl` | `5e817ef607f1533b0bcd488bbafbee53195595e76f3e861968ad0bc80f66b198` |
| `bot_research/runs/lead/g9a/results.jsonl` | `0e4768315497b2d6bcf310194de61f2a0c8934014d3598705ed4671a6296dc00` |
| `bot_research/runs/lead/g9b/results.jsonl` | `2203c126f9b7af85893933ea41a145f0a74ad224de2f3cd3339b55503575e86f` |
| `bot_research/runs/lead/g9c/results.jsonl` | `0be6c774d09b13348dc6db6ca017d118b64e11750af0dced92e8e3f752260810` |
| `bot_research/runs/lead/g9d/results.jsonl` | `44f14889e7b6794e7f4361568af6c36bb6453375fa74bf46e9ae80ab98e78b34` |
| `bot_research/runs/lead/g9a/logs/20261031T124659-00235--make-big_threat=100-gun_cap=120-poke_until=3-big_partial=tr-vs--make-layout=-empty--growth_rounds=7-bait=--tier2---bait_rou-std.jsonl` | `b413fa67bd26298b333bcfb33c687389b2c47c67d87857cfaa222da925022e66` |
| `bot_research/runs/lead/g9a/logs/20261031T124659-00236--make-layout=-empty--growth_rounds=7-bait=--tier2---bait_rou-vs--make-big_threat=100-gun_cap=120-poke_until=3-big_partial=tr-std.jsonl` | `afae19dac5643c8989eaf0ded578a5ede660fedd2b0baf2d63926db11289070f` |
| `bot_research/runs/lead/ab15/logs/20261031T212748-00093--make-big_threat=null_best_v9e-vs--make-layout=-empty--growth_rounds=7-bait=--tier2---bait_rou-std.jsonl` | `ce16df16492a029dc79c54b06fbb93ca78b48adc2509bcae8750833908f3599a` |
| `bot_research/runs/lead/ab15/logs/20261031T212748-00094--make-layout=-empty--growth_rounds=7-bait=--tier2---bait_rou-vs--make-big_threat=null_best_v9e-std.jsonl` | `4da970aad89172fc4bb98de71df1e730b1a639eb9dad2c56fd8afb55ff10d7fd` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `bot_research/experiments/lead/pools.py` | `ecef42ec477f117bcfb9a92816fda201e521a13681efd0b0978c881ff2456e63` |
| `bot_research/experiments/lead/frozen/best_v9e.py` | `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87` |
| `bot_research/experiments/lead/v19.py` | `c5610e472bf3f35bb3e093a2cd8734c26f8af01d01b121f1348b95bcadd84b57` |
| `bot_research/tmp/cmp_runs.py` | `3f495aa625cbee2232d1f4037491ac97e27ab0f05392e55caefb688f0865c5e8` |
| `bot_research/reports/REPORT.md` | `a071d310bb23da49bb2a9ef87f7935b70f417d42b335900c09655c84ed66db2a` |

The four log paths above correspond, in order, to g9a results lines 235 and 236, then ab15 results lines 93 and 94. Their last two records were inspected; no replay was executed.
