"""Check that two bot specs submit identical actions under scripted openings (harness scenarios).

    .venv/bin/python -B -m bot_research.experiments.lead.same_actions_scen SPEC1 SPEC2 OUTDIR \
        --opponents OPP [...] --scenarios SCEN [...]

For every opponent, scenario and seat, plays SPEC1 against it with ``harness.match.play_match`` (the
same code path as the tournaments), then SPEC2, and compares the recorded action events (order,
action, accepted) of both players in every round, so the comparison covers the whole trajectory.
Logs go to OUTDIR. Prints one line per pairing and exits 1 on any difference.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from bot_research.harness.match import play_match


def actions_of(path):
    out = {}
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            rec = json.loads(line)
            acts = [(e.get("order"), json.dumps(e["action"], sort_keys=True), e["accepted"])
                    for e in rec["event"] if e["kind"] == "action"]
            out.setdefault((rec["round"], rec["player"]), []).extend(acts)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec1")
    ap.add_argument("spec2")
    ap.add_argument("outdir")
    ap.add_argument("--opponents", nargs="+", required=True)
    ap.add_argument("--scenarios", nargs="+", required=True)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    bad = 0
    for i, opp in enumerate(args.opponents):
        for scen in args.scenarios:
            for seat in (0, 1):
                logs, rows = [], []
                for k, spec in enumerate((args.spec1, args.spec2)):
                    a, b = (spec, opp) if seat == 0 else (opp, spec)
                    f = os.path.join(args.outdir, f"o{i}-{scen.replace(':', '-')}-s{seat}-{k + 1}.jsonl")
                    rows.append(play_match(a, b, f, scenario=None if scen == "none" else scen))
                    logs.append(actions_of(f))
                same = logs[0] == logs[1]
                bad += not same
                d = [r["hp_diff_a"] * (1 if seat == 0 else -1) for r in rows]
                print(f"{'same' if same else 'DIFFERENT'} opp{i} {scen} seat{seat} hp {d[0]:+d} / {d[1]:+d} "
                      f"rounds {rows[0]['rounds']} / {rows[1]['rounds']}  {opp}", flush=True)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
