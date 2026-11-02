# bot_research

Research artifacts for the two-player tower-defense game of this project: candidate and final bots, the evaluation
harness, experiments, result tables, a few representative replays, the workers' notes and the report. Everything
here was written during one research run on the unchanged engine and the bundled balanced rules; no file outside
this folder was modified.

The final bot is `bots/best.py` (function `decide`), the policy called best_v9e in the report. Read
`reports/REPORT.md` first: it opens with a summary, then gives the decision rules, tournament results, ablations,
validation evidence, counters, known failures, runtime, reproduction commands and integrity checks.
`reports/RULES.md` records the game contract established from the source.

## Layout

- `bots/best.py`: final entry point. `bots/defense/`, `bots/economy/`, `bots/counters/`: the workers' bots
  (defensive maps and fortresses, economy and timing policies, targeted counters and validation opponents).
- `harness/`: match runner on the unchanged engine (`match.py`), tournaments (`tournament.py`), scripted starts
  (`scenarios.py`), baselines, the exact combat model (`gamekit.py`), traces and the integrity check (`integrity.py`).
- `experiments/lead/`, `experiments/defense/`, `experiments/economy/`, `experiments/validation/`: experiment
  scripts, pools, queues, frozen bot copies (`experiments/lead/frozen/`) and analysis scripts
  (`experiments/lead/analysis/`).
- `runs/`: smoke logs, per-run summaries (`summary.md`, `summary.json`), the `results.jsonl` tables of the final
  runs and a small set of representative replays.
- `notes/`: the workers' notes (assumptions, measurements, failure cases, uncertainty).
- `reports/`: the report, the rules contract and the integrity baseline.
- `tests/`: tests of the final bot, the harness and the combat model.
- `tmp/`: empty scratch directory used as TMPDIR.
- `protected_files.sha256.json`: the project's protected-file manifest (unchanged).

## Smoke command

Run from the original game project root, the directory containing `td_game/`, `td_bots/` and `.venv/`, with this
folder placed there as `bot_research/`. This published bundle does not include the engine or Python environment.
The command gives the log a timestamp because the runner does not overwrite existing logs.

```
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle --output "bot_research/runs/best-vs-idle-$(date -u +%Y%m%dT%H%M%S%N).jsonl"
```

Last recorded run (2026-11-01T00:16:50Z, output `runs/best-vs-idle-final-20261101T0016Z.jsonl`): player 0 wins in
8 rounds (base destroyed), HP 800 against -5. The idle opponent checks integration, not strength.

## Reproduction

From that game project root, set the environment once before using the commands below:

```sh
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp"
```

The engine is deterministic for identical inputs. Reproducing a game also requires the same bot decisions;
wall-clock planning cutoffs can change those decisions and game outcomes with machine load (report, section 7).

- Tests of this folder:
  `.venv/bin/python -B -m unittest bot_research.tests.test_best bot_research.tests.test_harness bot_research.tests.test_gamekit`
- The project's own tests (unchanged): `.venv/bin/python -B -m unittest discover -s tests`
- Integrity against the recorded starting state (`reports/integrity_baseline.json`):
  `.venv/bin/python -B -m bot_research.harness.integrity --json bot_research/runs/NEW_NAME.json`
- One match, both bots given as `module:function` or `module:@make?option=value` specs:
  `.venv/bin/python -B -m bot_research.harness.match --bot-a BOT --bot-b BOT --output bot_research/runs/NEW_NAME.jsonl`,
  trace with `.venv/bin/python -B -m bot_research.experiments.lead.trace bot_research/runs/NEW_NAME.jsonl --rounds 1-12`
- Pool tournament (both seats): `bot_research/experiments/lead/run_pool.sh POOL NAME "'BOT' ..." --keep-logs losses`,
  pools in `experiments/lead/pools.py`; table with
  `.venv/bin/python -B -m bot_research.experiments.lead.matrix bot_research/runs/lead/NAME/results.jsonl` and checks
  (rejected actions, bot errors, slowest call) with
  `.venv/bin/python -B bot_research/experiments/lead/check_runs.py bot_research/runs/lead/NAME/results.jsonl`.
  `run_pool.sh` pins two cores with `taskset -c 20,21 nice -n 19`; edit the core list for another machine.
- Final round robins and their max-min mixtures: specs in `experiments/lead/rr_specs.sh`;
  `python3 bot_research/experiments/lead/analysis/rr_table.py bot_research/runs/lead/frr1/results.jsonl NAME=SUFFIX ...`
  and `python3 bot_research/experiments/lead/analysis/rr_nash.py bot_research/runs/lead/frr1/results.jsonl none NAME=SUFFIX ...`
  (the second needs numpy and scipy).
- Condition-by-condition comparison of two runs:
  `python3 bot_research/experiments/lead/analysis/cmp_runs.py A.jsonl SUBSTR_A B.jsonl SUBSTR_B`.
- The workers' experiments are described with their commands in `notes/defense.md`, `notes/economy.md` and
  `notes/validation.md`; the validation campaigns keep their scripts and summaries under `experiments/validation/`.

The detailed reproduction commands below list the archived queue scripts and their associated runs.

## What was removed before publication

The scratch directory `tmp/` was emptied, caches were deleted, and to keep the folder small most per-game replay
logs and bulky intermediate evidence files were not published. Result tables were kept where size allowed. The
analysis scripts that the report cites were moved from scratch into `experiments/lead/analysis/`; a few of them read
intermediate files that were not kept. The queue scripts in `experiments/lead/` record the main agent's run specs,
but some also depend on removed scratch helpers, frozen-test copies or drafts. They cannot all run unchanged from
this published copy. See `reports/PUBLISHED_CONTENTS.md` for the omitted files and the limitations below.

## Detailed reproduction commands

The following command record was retained from the report. Paths written as `experiments/...` or `runs/...`
identify files relative to `bot_research/` unless a command states another working directory. `POOL`, `NAME`, `BOT`,
`FILE`, suffix labels and ellipses are placeholders to fill from the named specs and recorded run. Use a fresh
output name, and adjust the fixed `taskset` core lists for the local machine.

Several historical commands require material omitted from this bundle: early cycle-8/9 queues call helpers in
`tmp/`; `freeze_v9c.sh` through `freeze_v9f.sh` use removed test copies or drafts; `opt_search.py` and
`opt_search2.py` import `tmp/test_best_v9f_V33C.py`; the gate analyses also read omitted intermediate tables.
The current test command above uses the retained `tests/` directly. The archived scripts and analysis-source
docstrings retain their historical paths so the recorded source hashes remain meaningful.

The analysis scripts cited in this report (comparison, table, matrix and trace scripts) were written in the scratch
directory during the run and were moved to `experiments/lead/analysis/` for publication; the commands below give
their published locations. Some of them read intermediate files of the scratch directory, which was emptied before
publication, and most per-game replays and bulky intermediate evidence files were left out to keep the folder small
(`reports/PUBLISHED_CONTENTS.md`). The queue scripts named below record the main agent's run specs; regenerating a
run also requires any omitted helper or input it used. Opponents with a wall-clock cutoff may take other branches
under a different machine load (report, section 7); the workers' runs are described in their notes.

All commands from the project root with `PYTHONDONTWRITEBYTECODE=1` and
`TMPDIR="$PWD/bot_research/tmp"`; analysis runs were pinned with `taskset -c 20,21 nice -n 19`.

- Smoke game: `.venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide
  --bot-b td_bots.protocol:idle --output bot_research/runs/best-vs-idle-000001.jsonl` (the runner does not
  overwrite an existing log, so a rerun needs a new output name).
- Tests: `.venv/bin/python -B -m unittest bot_research.tests.test_best bot_research.tests.test_harness
  bot_research.tests.test_gamekit` (bot, harness and combat-model tests) and the project's own suite
  `.venv/bin/python -B -m unittest discover -s tests` (section 9).
- Pool tournaments: `bot_research/experiments/lead/run_pool.sh POOL NAME "'BOT' ..." --keep-logs losses`
  with POOL from `experiments/lead/pools.py` (frontier5, targeted, scen, ...); results in
  `runs/lead/NAME/results.jsonl`; tables with
  `.venv/bin/python -B -m bot_research.experiments.lead.matrix bot_research/runs/lead/NAME/results.jsonl` and checks
  with `.venv/bin/python -B bot_research/experiments/lead/check_runs.py bot_research/runs/lead/NAME/results.jsonl`
  (both from the project root).
- Forecaster screens: `MODEL=v13 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh
  PREFIX 'JSON parameters'`, summarized by `experiments/lead/screen_table.py`.
- Single games and traces: `.venv/bin/python -B -m bot_research.harness.match --bot-a BOT --bot-b BOT
  --output FILE`, then `.venv/bin/python -B -m bot_research.experiments.lead.trace FILE --rounds 1-12`;
  quick seat-0 results with `experiments/lead/quick_games.py`.
- Identity of a frozen bot and its development twin: `experiments/lead/same_actions.py`.
- Queues that produced the cycle-6 and cycle-7 runs: `experiments/lead/queue_c6e.sh` (t3) and
  `experiments/lead/queue_c7b.sh` (t4; stopped after starting it), `experiments/lead/queue_c7d.sh` (t5;
  stopped after starting it) and `experiments/lead/queue_c7f.sh` (t7, c8a, s13, s14, rr1, rr2); t6 was
  started by hand with `run_pool.sh latest t6 ...`.
- Cycles 8 and 9: `experiments/lead/queue_c8.sh`, `queue_c9a*.sh` and `queue_c9b*.sh` (each later version
  replaced the earlier one while its running tournament was left to finish; the header comment of every
  file says what it replaced and why). Pools TARGETED2, FOREIGN_OPP (`foreign`), `new_foreign` and
  `old_foreign` are in `experiments/lead/pools.py`. Development modules `experiments/lead/v18.py`
  (mid_joint, fortress_guns, foreign_target, catch_up), `v19.py` (two more foreign targets) and `v20.py`
  (mid_level).
- Freeze checks: `experiments/lead/freeze_v9b.sh` (run for best_v9b, log `runs/lead/freeze_v9b.log`):
  identity of the frozen file and its twin on the standard start (`same_actions.py`) and under scripted
  openings (`same_actions_scen.py`), the bot tests and the smoke game.
- Cycles 10 and 11 (sections 5.12-5.14): `experiments/lead/queue_v33a.sh` and `queue_v33b.sh` (the V33C gate, runs
  x33*), `queue_bse.sh` (best_v9e on SCREENED, HANDOFF and TIMING: bse_sg, bse_hd, bse_tm), `queue_frz2.sh` (replaced
  `queue_frz.sh`; the freeze checks `bash experiments/lead/freeze_v9f.sh V33C` (run in bot_research; the script changes to the
  project root itself), log `runs/lead/freeze_v9f.log`, then
  af2-af7), `queue_af.sh` (af2g, af3g, af14g, af8-af13), `queue_v33ma.sh` (the V33M gate, run xm_f; stopped),
  `queue_ab1b.sh`, `queue_ab2.sh`, `queue_ab3.sh` and `queue_ab4.sh` (the best_v9e ablations ab1-ab17). Each file's
  header says what it replaced and why. `freeze_v9f_doc.sh` (a docstring-only correction of best_v9f) was written
  and not run. The option-exercise scenario search:
  `BEST_MODULE=bot_research.experiments.lead.frozen.best_v9f PYTHONPATH=. .venv/bin/python -B bot_research/experiments/lead/analysis/opt_search.py`
  and `... bot_research/experiments/lead/analysis/opt_search2.py POOL SEAT [MAX_ROUNDS]`, output `runs/lead/opt_search/`. Pool tables:
  `python3 bot_research/experiments/lead/analysis/pool_table.py LABEL=RUN[,RUN...] ... -- SUFFIX=NAME ...`.
- Cycle 12 (section 5.14): `experiments/lead/queue_g1.sh` and `queue_g2.sh` (the af2g gate under R13, runs g13*,
  then the remaining best_v9e ablations), `queue_g3b.sh` (replaced `queue_g3.sh`, whose specs were wrong; runs gmchk2,
  gy1-gy4, then ab3; stopped at 20:22Z with ab3 incomplete, see the ab3 row of section 5.14), `queue_tm.sh` (gmchk,
  the TIMING2 screen tsc; stopped at 20:20Z during ab10) and `queue_h14.sh A|B`, which replaced the rest of both and the
  two waiting `queue_rr.sh` processes: the H14 gate (runs h14*, compared with best_v9e's runs by
  `python3 bot_research/experiments/lead/analysis/h14_gate.py [--show]`, output `runs/lead/h14_gate.txt` and `h14_gate_show.txt`), and
  then `queue_h15.sh A|B`, which replaced the tail of each `queue_h14.sh` slot after its gate half: the attack-share
  screen (runs s75tm2, s75x, s65tm2, s65x), the ablations ab14-ab17 (it dropped ab4-ab6 and ab10-ab12), the
  prefix-fork run fk1 (checked with `experiments/lead/fork_check.py runs/lead/fk1`) and the final round robins frr1
  and frr2 of section 5.16 (specs in `experiments/lead/rr_specs.sh`, tables with
  `python3 bot_research/experiments/lead/analysis/rr_table.py bot_research/runs/lead/frr1/results.jsonl NAME=SUFFIX ...` from the project root, where the first matching
  suffix names a spec; the max-min mixtures of section 5.16 with the analysis Python and
  `python3 bot_research/experiments/lead/analysis/rr_nash.py bot_research/runs/lead/frr1/results.jsonl none NAME=SUFFIX ...` from the project root). After them, `queue_h16.sh A|B` restored three of the dropped f5t ablations (ab6, ab10,
  ab11) and `queue_h17.sh` played the defence worker's final v46 against the same finalists (frr3 on the standard start, frr4 on
  mirror:1:2 and asym:23:2); `queue_h18.sh` ran the last three dropped f5t ablations (ab4, ab5, ab12); `queue_h19.sh` (frr5) and
  `queue_h20.sh` (frr6) played the defence worker's final v48 against the same finalists, and `queue_h21.sh` played the economy worker's af5
  (frr7 on the scripted starts, frr8 against v48 on the standard start; comparison with V29 and g1:
  `python3 experiments/lead/analysis/cmp_af5_v29.py` run in bot_research; af5 against V29 on the scenario starts of scnaf5:
  `python3 experiments/lead/analysis/cmp_scnaf5.py` run in bot_research). The count of
  distinct gate conditions (section 5.14): `python3 bot_research/experiments/lead/analysis/dedup846.py G1 V29` from the project root
  (variable names of `rr_specs.sh`). Per-round traces of kept logs: `python3 bot_research/experiments/lead/analysis/trace2.py LOG`; the
  rounds in which two logs have the same actions: `python3 bot_research/experiments/lead/analysis/cmp_actions.py LOG_A LOG_B MAX_ROUND`.
- Condition-by-condition comparison of two runs: `python3 bot_research/experiments/lead/analysis/cmp_runs.py A.jsonl SUBSTR_A
  B.jsonl SUBSTR_B`; quick games under scripted openings:
  `PYTHONPATH=. .venv/bin/python -B bot_research/experiments/lead/analysis/qscen.py OUTDIR CAND OPP SCEN`
  (`QSEATS=0` for seat 0 only).
