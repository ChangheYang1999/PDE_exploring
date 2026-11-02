"""Compare two candidates condition by condition (development only).

    python3 tmp/cmp_runs.py RESULTS_A SUBSTR_A RESULTS_B SUBSTR_B [--all]

A candidate is selected by a substring of its spec. Conditions are (opponent, scenario, candidate seat). Prints
the conditions where outcome or HP difference differ (all with --all), then W-D-L of both on the shared ones.
"""
import json, sys


def load(path, sub):
    out = {}
    for line in open(path):
        r = json.loads(line)
        if r.get("error"):
            continue
        s = r["candidate_side"]
        c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
        if sub not in c:
            continue
        w = r["winner"]
        res = "W" if w == s else ("D" if w is None else "L")
        out[(o, r.get("scenario"), s)] = (res, r["hp_diff_a"] * (1 if s == 0 else -1), r["rounds"])
    return out


a, b = load(sys.argv[1], sys.argv[2]), load(sys.argv[3], sys.argv[4])
show_all = "--all" in sys.argv
keys = sorted(set(a) & set(b), key=lambda k: (k[0], str(k[1]), k[2]))
for k in keys:
    if show_all or a[k][:2] != b[k][:2]:
        o = k[0].split("bots.")[-1].split("lead.")[-1]
        print(f"{a[k][0]} {a[k][1]:+6d} r{a[k][2]:<2d} | {b[k][0]} {b[k][1]:+6d} r{b[k][2]:<2d}  {k[1] or 'std'} s{k[2]} {o[:90]}")
for name, d in (("A", a), ("B", b)):
    res = [d[k][0] for k in keys]
    print(f"{name}: {res.count('W')}-{res.count('D')}-{res.count('L')} on {len(keys)} shared conditions; "
          f"worst {min(d[k][1] for k in keys) if keys else None}; only in {name}: {len(set(d) - set(keys))}")
