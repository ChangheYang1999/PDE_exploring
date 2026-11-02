"""Check of the determinism argument of experiments/lead/prefix_fork.py on recorded games (development).

    python3 bot_research/experiments/lead/fork_check.py runs/lead/fk1

For every candidate, seat and opening (bait or none), compares each strike game with fork_round k to the grow game:
the fork's submitted actions must agree in rounds 1..k-1 and the candidate's in rounds 1..k. Prints the first round in
which each side's actions differ (None: never within the game) and exits 1 if any pair breaks the prediction.
"""
import json, re, sys
from pathlib import Path


def actions(path):
    """{player: {round: [submitted actions, accepted or not]}} and the two bot specs."""
    out, bots = {0: {}, 1: {}}, None
    for line in open(path):
        rec = json.loads(line)
        if "match" in rec:
            bots = rec["match"]["bots"]
        if rec["round"] >= 1:
            acts = out[rec["player"]].setdefault(rec["round"], [])
            acts.extend(e["action"] for e in rec["event"] if e["kind"] == "action")
    return out, bots


def first_diff(a, b):
    for r in sorted(set(a) | set(b)):
        if a.get(r, []) != b.get(r, []):
            return r
    return None


games = {}
for path in sorted((Path(sys.argv[1]) / "logs").glob("*.jsonl")):
    acts, bots = actions(path)
    fork = [i for i, s in enumerate(bots) if "prefix_fork" in s]
    if len(fork) != 1:
        continue
    f = fork[0]
    spec = bots[f]
    m = re.search(r"fork_round=(\d+)", spec)
    kind = "strike" if "strike" in spec else "grow"
    opening = "bait" if "bait=" in spec else "none"
    games.setdefault((bots[1 - f], 1 - f, opening), []).append((kind, int(m.group(1)) if m else None, spec, acts, f))

bad = 0
for (cand, seat, opening), rows in sorted(games.items()):
    grow = [r for r in rows if r[0] == "grow"]
    if len(grow) != 1:
        print("no unique grow game for", cand[-60:], seat, opening)
        bad += 1
        continue
    g = grow[0]
    for kind, k, spec, acts, f in rows:
        if kind != "strike":
            continue
        df = first_diff(acts[f], g[3][g[4]])
        dc = first_diff(acts[1 - f], g[3][1 - g[4]])
        ok = (df is None or df >= k) and (dc is None or dc > k)
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} seat {seat} {opening:4s} k={k} fork differs from r{df}, candidate from r{dc}  "
              f"{cand.split('.')[-1][:50]} | {spec.split('?', 1)[-1]}")
sys.exit(1 if bad else 0)
