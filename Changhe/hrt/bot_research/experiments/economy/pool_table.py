"""Per-pool W-D-L, clipped mean and worst HP difference of candidates from a tournament results file (hrt-w2).

Usage: python3 pool_table.py RESULTS POOLS_JSON TAG=SUFFIX [TAG=SUFFIX ...]
POOLS_JSON maps each opponent spec to the list of pool names it belongs to (for example opp_gate1_pools.json).
A candidate is selected by the spec ending with SUFFIX (exact suffix match; give the longest distinguishing suffix).
Outcomes are the engine's (winner field); HP differences are from the candidate's side, clipped to [-800, 800] for
the mean. Also prints bot errors, rejected actions and the largest decide call of the candidate.
"""
import json
import sys
from collections import defaultdict


def main():
    res, pools = sys.argv[1], json.load(open(sys.argv[2]))
    cands = [a.split("=", 1) for a in sys.argv[3:]]
    rows = defaultdict(lambda: defaultdict(list))
    for line in open(res):
        r = json.loads(line)
        s = r["candidate_side"]
        c = r["spec_a"] if s == 0 else r["spec_b"]
        o = r["spec_b"] if s == 0 else r["spec_a"]
        tag = next((t for t, suf in cands if c.endswith(suf)), None)
        if tag is None:
            continue
        hp = r["hp_diff_a"] if s == 0 else -r["hp_diff_a"]
        w = r["winner"]
        x = 0 if w is None else (1 if w == s else -1)
        p = r["players"][s] if isinstance(r.get("players"), list) else {}
        err = len(p.get("bot_errors", [])) + (1 if r.get("error") else 0)
        rej = p.get("n_rejected", 0)
        dm = r["decide_max_seconds"]
        dm = dm[s] if isinstance(dm, list) else dm
        for name in pools.get(o, ["(not in pools)"]) + ["ALL"]:
            rows[tag][name].append((x, hp, err, rej, dm, r["rounds"]))
    names = sorted({n for t in rows for n in rows[t]}, key=lambda n: (n == "ALL", n))
    print("| pool | " + " | ".join(t for t, _ in cands) + " |")
    print("| --- |" + " --- |" * len(cands))
    for n in names:
        cells = []
        for t, _ in cands:
            v = rows[t].get(n, [])
            if not v:
                cells.append("-")
                continue
            W = sum(a[0] > 0 for a in v); D = sum(a[0] == 0 for a in v); L = sum(a[0] < 0 for a in v)
            clip = sum(max(-800, min(800, a[1])) for a in v) / len(v)
            cells.append(f"{W}-{D}-{L} ({len(v)}), clip {clip:+.0f}, worst {min(a[1] for a in v)}")
        print(f"| {n} | " + " | ".join(cells) + " |")
    for t, _ in cands:
        v = rows[t].get("ALL", [])
        if v:
            print(f"{t}: games {len(v)}, bot errors {sum(a[2] for a in v)}, rejected actions {sum(a[3] for a in v)}, "
                  f"largest decide call {max(a[4] for a in v):.2f} s, rounds {min(a[5] for a in v)}-{max(a[5] for a in v)}")


if __name__ == "__main__":
    main()
