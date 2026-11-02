# Final selected policy on reserved pool D

Published 2026-10-31T23:26:30.755552+00:00.

The complete execution and replay audit is CONFIRMED for all 96 declared conditions. The selected candidate is `bot_research.bots.best:decide`, SHA256 `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. Its selection was recorded at 2026-10-31T19:50:37+00:00, before the first D game, and the copied selection note is retained. This pool reports that fixed choice; it is not used to choose between candidates.

The sixteen opponent parameter settings and two prescribed histories were declared at 2026-10-31T18:11:52.885103+00:00. They use known implementation families and were designed after earlier development results. Exact parameter and history separation is audited below; this is not a random sample from an opponent population.

W/D/L is from the candidate's perspective. Standard-start scores are separated from continuation tests, where neither policy is called during its prescribed prefix.

| Start | W/D/L | Seat0 | Seat1 | Worst HP difference | Ending rounds | Maximum timed wrapper call seconds |
|---|---|---|---|---:|---|---:|
| standard | 26/6/0 | 13/3/0 | 13/3/0 | 0 | [9, 10, 11, 12, 13, 14, 17, 50] | 0.726784 |
| asym_130363_2 | 28/0/4 | 14/0/2 | 14/0/2 | -3905 | [10, 11, 12, 13, 35] | 2.823765 |
| mirror_104729_3 | 32/0/0 | 16/0/0 | 16/0/0 | 360 | [10, 11, 20] | 1.233880 |

All 96 conditions have an earliest valid result. The complete accounting retains 0 nonvalid attempts; no selected result has a bot error, rejected submitted action or source drift. Each action history has been replayed through a fresh original Engine and every record compared. Fresh processes reproduce 1532 actual candidate decisions through the direct entry point and default factory, each agreeing with the recorded specification. The 160 prescribed prefix rounds are skipped. No candidate observation is mutated.

The timing wrapper is invoked on every game round, including prescribed turns that only copy prefix actions. Its call counts and aggregate seconds therefore include prefix turns. The receipt reports actual policy calls and prescribed turns separately. Aggregate timings cannot isolate policy-only time; the displayed maximum is a wrapper measurement.

The campaign began 2026-10-31T23:00:03.171603+00:00, after the declared 23:00 UTC start restriction. The final primary game completed 2026-10-31T23:11:43.938125+00:00. Actual elapsed time to that completion was 700.766522seconds; primary match runtimes sum to 648.608606seconds. These shared-machine, low-priority timings do not estimate a portable time bound or the team's total work.

There are 44 distinct complete canonical trajectories among 96 selected results. 48 of 48 physical-assignment pairs have identical canonical histories. Repeated deterministic trajectories are reproducibility checks and provide no additional independent strength evidence.

The recorded prior-use audit found 0 exact normalized-parameter overlaps and 0 exact prescribed-history overlaps. It records 0 unrecognized parameter inputs and 8 unresolved scenario inputs. These counts describe the recognized archived streams and declarations only; they do not establish that an opponent behaves differently from every previous one or that no unrecorded evaluation occurred. The audit JSON retains coverage, inputs and every overlap.

Every selected condition follows. HP is candidate:opponent. No loss is omitted.

| Condition | W/D/L | HP | Ending round |
|---|---|---|---:|
| standard-00-side0 | W | 800:-280 | 10 |
| standard-00-side1 | W | 800:-280 | 10 |
| standard-01-side0 | W | 800:-688 | 11 |
| standard-01-side1 | W | 800:-688 | 11 |
| standard-02-side0 | W | 800:-214 | 13 |
| standard-02-side1 | W | 800:-214 | 13 |
| standard-03-side0 | W | 800:-162 | 13 |
| standard-03-side1 | W | 800:-162 | 13 |
| standard-04-side0 | W | 774:-325 | 9 |
| standard-04-side1 | W | 774:-325 | 9 |
| standard-05-side0 | W | 800:-172 | 13 |
| standard-05-side1 | W | 800:-172 | 13 |
| standard-06-side0 | W | 800:-5 | 11 |
| standard-06-side1 | W | 800:-5 | 11 |
| standard-07-side0 | W | 800:-490 | 14 |
| standard-07-side1 | W | 800:-490 | 14 |
| standard-08-side0 | W | 800:320 | 50 |
| standard-08-side1 | W | 800:320 | 50 |
| standard-09-side0 | W | 800:520 | 50 |
| standard-09-side1 | W | 800:520 | 50 |
| standard-10-side0 | D | 800:800 | 50 |
| standard-10-side1 | D | 800:800 | 50 |
| standard-11-side0 | D | 800:800 | 50 |
| standard-11-side1 | D | 800:800 | 50 |
| standard-12-side0 | D | 785:785 | 50 |
| standard-12-side1 | D | 785:785 | 50 |
| standard-13-side0 | W | 783:-142 | 12 |
| standard-13-side1 | W | 783:-142 | 12 |
| standard-14-side0 | W | 800:-519 | 17 |
| standard-14-side1 | W | 800:-519 | 17 |
| standard-15-side0 | W | 800:253 | 50 |
| standard-15-side1 | W | 800:253 | 50 |
| mirror_104729_3-00-side0 | W | 702:-52 | 10 |
| mirror_104729_3-00-side1 | W | 702:-52 | 10 |
| mirror_104729_3-01-side0 | W | 780:0 | 10 |
| mirror_104729_3-01-side1 | W | 780:0 | 10 |
| mirror_104729_3-02-side0 | W | 360:0 | 10 |
| mirror_104729_3-02-side1 | W | 360:0 | 10 |
| mirror_104729_3-03-side0 | W | 780:-52 | 11 |
| mirror_104729_3-03-side1 | W | 780:-52 | 11 |
| mirror_104729_3-04-side0 | W | 713:-26 | 10 |
| mirror_104729_3-04-side1 | W | 713:-26 | 10 |
| mirror_104729_3-05-side0 | W | 775:-48 | 10 |
| mirror_104729_3-05-side1 | W | 775:-48 | 10 |
| mirror_104729_3-06-side0 | W | 780:-68 | 11 |
| mirror_104729_3-06-side1 | W | 780:-68 | 11 |
| mirror_104729_3-07-side0 | W | 780:-60 | 11 |
| mirror_104729_3-07-side1 | W | 780:-60 | 11 |
| mirror_104729_3-08-side0 | W | 780:-52 | 10 |
| mirror_104729_3-08-side1 | W | 780:-52 | 10 |
| mirror_104729_3-09-side0 | W | 754:-52 | 10 |
| mirror_104729_3-09-side1 | W | 754:-52 | 10 |
| mirror_104729_3-10-side0 | W | 780:-52 | 10 |
| mirror_104729_3-10-side1 | W | 780:-52 | 10 |
| mirror_104729_3-11-side0 | W | 780:-52 | 10 |
| mirror_104729_3-11-side1 | W | 780:-52 | 10 |
| mirror_104729_3-12-side0 | W | 780:-2160 | 20 |
| mirror_104729_3-12-side1 | W | 780:-2160 | 20 |
| mirror_104729_3-13-side0 | W | 780:-2160 | 20 |
| mirror_104729_3-13-side1 | W | 780:-2160 | 20 |
| mirror_104729_3-14-side0 | W | 780:-52 | 11 |
| mirror_104729_3-14-side1 | W | 780:-52 | 11 |
| mirror_104729_3-15-side0 | W | 754:-52 | 11 |
| mirror_104729_3-15-side1 | W | 754:-52 | 11 |
| asym_130363_2-00-side0 | W | 747:-19 | 10 |
| asym_130363_2-00-side1 | W | 747:-19 | 10 |
| asym_130363_2-01-side0 | W | 800:-283 | 11 |
| asym_130363_2-01-side1 | W | 800:-283 | 11 |
| asym_130363_2-02-side0 | W | 800:-595 | 12 |
| asym_130363_2-02-side1 | W | 800:-595 | 12 |
| asym_130363_2-03-side0 | W | 800:-47 | 12 |
| asym_130363_2-03-side1 | W | 800:-47 | 12 |
| asym_130363_2-04-side0 | W | 776:-63 | 10 |
| asym_130363_2-04-side1 | W | 776:-63 | 10 |
| asym_130363_2-05-side0 | W | 790:-15 | 13 |
| asym_130363_2-05-side1 | W | 790:-15 | 13 |
| asym_130363_2-06-side0 | W | 800:-4 | 13 |
| asym_130363_2-06-side1 | W | 800:-4 | 13 |
| asym_130363_2-07-side0 | W | 800:-55 | 11 |
| asym_130363_2-07-side1 | W | 800:-55 | 11 |
| asym_130363_2-08-side0 | W | 760:-4 | 13 |
| asym_130363_2-08-side1 | W | 760:-4 | 13 |
| asym_130363_2-09-side0 | W | 748:-4 | 13 |
| asym_130363_2-09-side1 | W | 748:-4 | 13 |
| asym_130363_2-10-side0 | W | 800:-4 | 13 |
| asym_130363_2-10-side1 | W | 800:-4 | 13 |
| asym_130363_2-11-side0 | W | 660:-30 | 13 |
| asym_130363_2-11-side1 | W | 660:-30 | 13 |
| asym_130363_2-12-side0 | L | -3120:785 | 35 |
| asym_130363_2-12-side1 | L | -3120:785 | 35 |
| asym_130363_2-13-side0 | L | -3120:785 | 35 |
| asym_130363_2-13-side1 | L | -3120:785 | 35 |
| asym_130363_2-14-side0 | W | 764:-75 | 12 |
| asym_130363_2-14-side1 | W | 764:-75 | 12 |
| asym_130363_2-15-side0 | W | 748:-45 | 12 |
| asym_130363_2-15-side1 | W | 748:-45 | 12 |

Reproduce with terminal_validation using the candidate hash in terminal-candidate-declaration-001.json, followed by audit_terminal_campaign, replay_campaign_bounded, summarize_reserved_replays, both terminal separation audits, audit_best_entrypoints_bounded and summarize_entrypoint_audits. Bounded commands and their real timestamps are retained in the campaign pipeline log. Run from the project root with the supplied Python, bytecode disabled, the research temporary directory, an assigned low-priority core and one numerical thread. The complete receipt is verification/final_candidate.json. Protected-file integrity is checked separately against the initial inventory.

These are finite empirical findings on the unchanged bundled rules. They establish neither general superiority nor optimal play. Any later candidate revision must be identified separately and cannot inherit an untouched-validation claim from this pool.
