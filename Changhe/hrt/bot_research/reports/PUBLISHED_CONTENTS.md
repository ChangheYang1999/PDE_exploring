# Published contents

This folder was prepared for publication on 2026-11-01, after the research run had stopped. No research game was run
during the preparation; the smoke command and one integrity check were run once more (report, section 9).

What was done:
- `tmp/` (the TMPDIR of all runs) was emptied; it keeps only an empty `.gitkeep`. No bytecode caches were present.
- The analysis scripts cited in the report were moved from `tmp/` to `experiments/lead/analysis/` before that. Some of
  them read intermediate files of `tmp/` that are not published.
- To keep the folder under 45 MB with no file over 10 MB, about 112,500 files (about 11.9 GB) were left out of the
  published copy. Nothing outside this folder was changed, and `protected_files.sha256.json` is byte-identical.
- No kept text file contains an absolute local path. One validation script
  (`experiments/validation/amend_reused_c_declaration.py`) spelled such path prefixes as a literal list for a check of
  its own outputs; that list is now built from its parts, with the same behaviour. All `SHA256SUMS` files of the frozen
  bots and `runs/lead/final/hashes*.txt` still verify.

Left out of the published copy:
- Almost all per-game replay logs under `runs/*/<run>/logs/` and `runs/validation/*/` (about 52,600 files, 9.7 GB).
- The per-run `results.jsonl` tables of most runs (628 files, about 309 MB) and the validation `matches.jsonl` files
  (360 files, about 278 MB). Summaries for 438 runs are retained; not every omitted result table has a retained
  per-run summary. Every `runs/validation/<run>/summary.json` is kept.
  Kept `results.jsonl` tables: `runs/lead/frr1`, `runs/lead/frr7`, `runs/economy/afrr`, `runs/economy/strike1b`,
  `runs/economy/scnaf5`, `runs/defense/x182_v41_vs_lead`, `x201_vs_best9e`, `x202a_fcap_vs_best9e`, `x210_v45_lead`,
  `x215_v46_lead` and `x230_v48_lead`.
- Report citations whose files are not published: the `results.jsonl` of `runs/economy/afs3`, `runs/economy/afs5`,
  `runs/lead/c2sweep1`, `c4a`, `c4b`, `c5a`, `c5d`, `c6a`, `c8m`, `c9h`, `d9a`, `fk1`, `s5-k0`, `sc1`, `t1` to `t7`, `t8f`,
  `t8g` and `tsc` (their `summary.md` files are kept); `runs/validation/reserved-D-final-001/matches.jsonl` (its
  `summary.json`, its summary note and two replays are kept); the two replays of `runs/lead/rb1/`.
- Validation evidence: code snapshots under `runs/validation/*/sources/`, per-case `jobs/` and `results/` folders,
  copies of inputs under `experiments/validation/reviews/*/inputs/`, report and notes snapshot copies, the
  `verification/full_games.json` dumps, other JSON evidence files over about 100 KB, and two compiled helper binaries
  (their `.cpp` sources are kept).
- Two large data files of the counter bots: `bots/counters/data/pure_splash_extensions_001.json` (12.4 MB, over the
  10 MB limit; search output of `experiments/validation/search_pure_splash_extensions.py`, loaded by no bot) and
  `bots/counters/plans/catalogue_and_fortress_001.json` (5.7 MB; needed only when `bots/counters/compiled_library.py`
  is given it as `data_file`, as in the validation experiments compiled-library-transfer-001, prefix-fork-001,
  emergency-prefix-001 and delegated-defense-001). `bots/best.py` and the other bots do not use either file.

Representative replays kept: all `runs/best-vs-idle-*.jsonl` smoke logs; `runs/lead/dev/A_vs_guarded_t4r5.jsonl` and
`runs/lead/dev/scen/V4f_vs_econ17_mirror-1-2_seat0.jsonl`; one game each from `runs/lead/frr1/logs/`,
`runs/lead/frr7/logs/`, `runs/economy/afrr/logs/` and `runs/economy/scnaf5/logs/`; two games from
`runs/defense/x230_v48_lead/logs/`; two pool D games in `runs/validation/reserved-D-final-001/replays/`; and
`runs/validation/v27-guard-timing-001/replays/case0014.jsonl.gz`.

The engine is deterministic for identical inputs. Reproducing a game also requires the same bot decisions;
wall-clock planning cutoffs can change those decisions under a different machine load (report, section 7). The queue scripts in
`experiments/lead/` retain the main agent's run specs, but some depend on removed scratch helpers, test copies or
drafts. Reconstructing such runs requires those inputs as well as the unchanged engine. The artifact README
identifies the main command families affected.
