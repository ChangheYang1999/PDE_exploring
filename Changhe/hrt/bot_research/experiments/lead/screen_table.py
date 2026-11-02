"""One line per screen_known run: candidate HP difference per (tier, attack round), seat 0, with
the match length when the game ended early, and the minimum over both seats.

    .venv/bin/python -B -m bot_research.experiments.lead.screen_table runs/lead/s5-k0 [...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def line(run_dir):
    rows = [json.loads(x) for x in open(Path(run_dir) / "results.jsonl", encoding="utf-8")]
    if not rows:
        return f"{Path(run_dir).name}: no results yet"
    cells, worst = [], None
    for r in rows:
        side = r["candidate_side"]
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        worst = diff if worst is None else min(worst, diff)
        if side != 0:
            continue
        s = r["spec_b"]
        if "schedule=" in s:   # public_schedule counter: the last declared wave
            rnd, tier, _ = json.loads(s.split("schedule=")[1].split("&")[0])[-1]
        else:
            rnd = s.split("attack_round=")[1].split("&")[0]
            tier = s.split('tier="')[1][:5] if 'tier="' in s else "m"   # "m": mixed-package counter
        cells.append(f"{tier[-1]}@{rnd}:{diff}" + ("" if r["rounds"] == 50 else f"(r{r['rounds']})"))
    cand = rows[0]["spec_a"] if rows[0]["candidate_side"] == 0 else rows[0]["spec_b"]
    params = cand.partition("?")[2] or "default"
    return f"{Path(run_dir).name} [{params}] min {worst}: " + " ".join(cells)


def main(argv=None):
    for d in (sys.argv[1:] if argv is None else argv):
        if (Path(d) / "results.jsonl").exists():
            print(line(d))


if __name__ == "__main__":
    main()
