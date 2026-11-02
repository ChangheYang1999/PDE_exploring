# Fixed budget handoffs fail to transfer

Checked 2026-10-31T15:26:01.339427+00:00.

REFUTED: the four fixed budget-handoff policies transfer their wins against P5TNUBM to the five declared targets. All 40 transfer games are target wins. The earlier wins remain valid for P5TNUBM only in their tested conditions.

Every row below represents both physical assignments. HP is target:counter; every target wins. These are standard-start development games with no retuning of the counter between targets.

| Target | Fixed counter | HP in each assignment | Final round |
|---|---|---|---:|
| P4TNUB | budget1of2_handoff6 | 800:755 | 50 |
| P4TNUB | budget1of1_handoff6 | 800:755 | 50 |
| P4TNUB | budget1of2_handoff7 | 800:755 | 50 |
| P4TNUB | budget1of1_handoff7 | 800:755 | 50 |
| F36 | budget1of2_handoff6 | 800:-775 | 17 |
| F36 | budget1of1_handoff6 | 800:-2055 | 31 |
| F36 | budget1of2_handoff7 | 800:-215 | 14 |
| F36 | budget1of1_handoff7 | 800:-1755 | 34 |
| F37 | budget1of2_handoff6 | 800:-775 | 17 |
| F37 | budget1of1_handoff6 | 800:-2055 | 31 |
| F37 | budget1of2_handoff7 | 800:-215 | 14 |
| F37 | budget1of1_handoff7 | 800:-1755 | 34 |
| best_v9e | budget1of2_handoff6 | 800:755 | 50 |
| best_v9e | budget1of1_handoff6 | 800:755 | 50 |
| best_v9e | budget1of2_handoff7 | 800:755 | 50 |
| best_v9e | budget1of1_handoff7 | 800:755 | 50 |
| lead8 | budget1of2_handoff6 | 560:520 | 50 |
| lead8 | budget1of1_handoff6 | 560:380 | 50 |
| lead8 | budget1of2_handoff7 | 560:520 | 50 |
| lead8 | budget1of1_handoff7 | 560:520 | 50 |

The counter buys one tier4 in round 5, then stops buying minions at handoff 6 or 7. Its defensive hypotheses append pure-tier purchases costing at most half or all of the public opponent budget, capped at 120 copies. It uses no opponent policy model. P4TNUB and best_v9e concede no damage; the earlier 755:740 advantage against P5TNUBM never arises. Fortress v36 and v37 both survive undamaged and eventually destroy the counter. The lead8 opponent takes damage but finishes ahead. The budget forecast is a finite heuristic set, not an immunity certificate for every affordable roster.

The 40 declared games all pass strict accounting, complete original-engine replay, source/data archive checks, and fresh reconstruction of the counter from public observations. All 20 assignment pairs have identical normalized histories. The 1,584 fresh counter decisions match exactly, leave observations unchanged, and submit legal action lists. There are no bot errors or rejected submitted actions. A total of 520 parent factory proposals are removed locally after the added strike; they are never submitted. No minions are bought after handoff.

The fortress planners retain their wall-clock stopping conditions, so observed agreement is not a universal determinism claim. Player swaps are controls, not independent random samples. No held-out condition or pool C game is used. This complete-policy comparison does not isolate one defensive purchase or prove that every HP-triggered or model-free counter fails.

To reproduce, use each of the three budget-transfer manifests with `run_data_development`, a fresh output directory, `--max-seconds 500 --match-timeout 300`, and `--resume` if necessary. Then run the strict, original-engine replay, data-closure and `check_budget_handoff_histories` checks. Run from the project root using `.venv/bin/python -B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `TMPDIR="$PWD/bot_research/tmp"`, one thread, low priority and the assigned CPU affinity.

Audit inputs:

- `bot_research/runs/validation/budget-transfer-a001-strict.json`.
- `bot_research/runs/validation/budget-transfer-a001-replay.json`.
- `bot_research/runs/validation/budget-transfer-a001-summary.json`.
- `bot_research/runs/validation/budget-transfer-a001-data.json`.
- `bot_research/runs/validation/budget-transfer-a001-histories.json`.
- `bot_research/experiments/validation/budget-transfer-a001.json`.
- `bot_research/runs/validation/budget-transfer-b001-strict.json`.
- `bot_research/runs/validation/budget-transfer-b001-replay.json`.
- `bot_research/runs/validation/budget-transfer-b001-summary.json`.
- `bot_research/runs/validation/budget-transfer-b001-data.json`.
- `bot_research/runs/validation/budget-transfer-b001-histories.json`.
- `bot_research/experiments/validation/budget-transfer-b001.json`.
- `bot_research/runs/validation/budget-transfer-c001-strict.json`.
- `bot_research/runs/validation/budget-transfer-c001-replay.json`.
- `bot_research/runs/validation/budget-transfer-c001-summary.json`.
- `bot_research/runs/validation/budget-transfer-c001-data.json`.
- `bot_research/runs/validation/budget-transfer-c001-histories.json`.
- `bot_research/experiments/validation/budget-transfer-c001.json`.
