# A public-budget forecast preserves the early-heavy win

Checked 2026-10-31T15:19:06.282803+00:00.

CONFIRMED: with the declared round5 tier4 opening, a forecast using half or all of the public enemy budget preserves the 755:740 win against P5TNUBM in both assignments, for handoff6 and handoff7. REFUTED: the quarter-budget variant preserves that win. This also refutes a broader claim that these wins require an exact opponent policy model.

Each row represents both physical assignments. Outcome is from the P5TNUBM target's perspective; HP is target:counter. These are standard-start development conditions.

| Counter setting | Target outcome per seat | HP | Final round |
|---|---|---|---:|
| budget1of4_handoff6 | W | 740:-285 | 16 |
| budget1of2_handoff6 | L | 740:755 | 50 |
| budget1of1_handoff6 | L | 740:755 | 50 |
| budget1of4_handoff7 | W | 740:-285 | 16 |
| budget1of2_handoff7 | L | 740:755 | 50 |
| budget1of1_handoff7 | L | 740:755 | 50 |

The counter follows the same screened opening and buys one tier4 in round5. From the handoff onward it constructs hypotheses by appending a pure tier to the visible active roster, using floor(nG/d) of public enemy gold G and a cap of120 new copies. It plans defense against that finite set, buys factories, and buys no more minions. It neither initializes nor queries an opponent policy clone.

The common opening leaves target740 and counter755 after round5. The four successful settings take no later damage. Each quarter-budget game first leaks after handoff in round10, for60 damage, even though every enumerated hypothetical roster has zero residual damage in the checked trace. This exposes inadequate forecast coverage; it does not establish that the greedy planner failed on a covered roster. The hypothesis set does not certify all affordable mixtures or counts beyond its cap.

All12 games pass strict accounting, original-engine replay, and source/data archive checks. Every assignment pair has an identical normalized history. There are no bot errors or rejected submitted actions. Fresh counter instances reproduce all464 decisions from unchanged observations and return legal action lists. The opening filter omits156 unaffordable parent factory proposals, thirteen per game; none is submitted. No minion is bought after handoff.

Twelve descriptive matched comparisons reuse the four exact-model reference games from early-heavy-handoff-001. All complete histories differ. These full-policy interventions change later defense and economy, so they do not isolate one purchase. The earlier visible-only and old-model failures remain valid for those controllers, but do not imply model necessity. Repeated assignments are controls, not independent population samples.

Reproduce with the run_data_development module, --manifest bot_research/experiments/validation/budget-handoff-001.json, a fresh --output-dir, --max-seconds500 and --match-timeout300, then repeat with --resume if needed. Use the project root, .venv/bin/python -B, PYTHONDONTWRITEBYTECODE=1, PYTHONPATH="$PWD", TMPDIR="$PWD/bot_research/tmp", OMP_NUM_THREADS=1, low priority and assigned affinity.

Audit inputs:

- `bot_research/runs/validation/budget-handoff-strict-001.json`.
- `bot_research/runs/validation/budget-handoff-replay-001.json`.
- `bot_research/runs/validation/budget-handoff-summary-001.json`.
- `bot_research/runs/validation/budget-handoff-data-001.json`.
- `bot_research/runs/validation/budget-handoff-histories-001.json`.
- `bot_research/runs/validation/budget-handoff-opening-001.json`.
- `bot_research/runs/validation/budget-handoff-comparison-001.json`.
- `bot_research/experiments/validation/budget-handoff-001.json`.
- `bot_research/experiments/validation/budget-handoff-comparisons-001.json`.
- `bot_research/runs/validation/early-heavy-handoff-summary-001.json`.
- `bot_research/runs/validation/early-heavy-handoff-replay-001.json`.
