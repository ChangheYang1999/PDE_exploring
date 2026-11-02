"""Condition-by-condition comparison of this lane's bots with best_v9e on the lead's R13 gate pools (hrt-w2).

    python3 bot_research/experiments/economy/gate_vs_base.py SPECFILE [SPECFILE...] [--show]   (from the project root)

Each SPECFILE holds one candidate spec (exact match against the candidate side of a result row). The candidate's
rows are collected from the lane runs in RUNS; best_v9e's rows come from the base files the lead's gate script
(bot_research/tmp/h14_gate.py) uses. A condition is (opponent spec, scenario, seat); only conditions present in the
base file of a pool are counted, so the base file defines the pool. Outcome ranks W > D > L (engine winner).
For each pool: shared conditions, W-D-L of both bots on them, the conditions where the candidate is worse or
better, and those with the same outcome and another HP difference. If a candidate has two rows for one condition
(the same match in two runs) with different results, the condition is reported as a conflict and left out.
"""
import json, os, sys

L = "bot_research/runs/lead/"
T = "bot_research/tmp/"
E = "bot_research/runs/economy/"
GATE = [  # pool, base file, base candidate substring, expected conditions (from h14_gate.py)
    ("PCS", L + "g13pc/results.jsonl", "best_v9e:@make", 8),
    ("TIMING", L + "bse_tm/results.jsonl", "best_v9e:@make", 32),
    ("TIMING2", L + "tm2/results.jsonl", "foreign_target", 40),
    ("STRIKE1", E + "strike1b/results.jsonl", "best_v9e:@make", 40),
    ("TARGETED2", T + "base_t8f_v18f.jsonl", "fortress_guns=true&catch_up=true", 48),
    ("f5t", L + "ab1/results.jsonl", "best_v9e:@make", 76),
    ("PUNISH", L + "pu1/results.jsonl", "foreign_target", 34),
    ("BLUFFCOV", T + "base_b9a_v18f.jsonl", "foreign_target", 16),
    ("TARGETED3_P5TF", L + "t9k/results.jsonl", "foreign_target", 30),
    ("HANDOFF", L + "bse_hd/results.jsonl", "best_v9e:@make", 36),
    ("SCREENED", L + "bse_sg/results.jsonl", "best_v9e:@make", 60),
    ("GROWERS", L + "g9a/results.jsonl", "foreign_target", 142),
    ("GUARDED_MAZE", T + "base_gm2_v18f.jsonl", "foreign_target", 144),
    ("STAGED", T + "base_st1_v18f.jsonl", "foreign_target", 140),
]
RUNS = ["gate1", "fam2b", "g1chk", "grow1", "gmaze1", "hand2", "hand3", "stdg", "stdg2", "fresh5a", "fresh5b",
        "smoke31", "g1fg", "g1ff", "g1fm", "g1fc", "pcs1", "hand4", "afs6", "afs5", "fresh6",
        "afq56", "afg5"]
RANK = {"W": 2, "D": 1, "L": 0}


def outcome(r, s):
    w = r["winner"]
    return ("W" if w == s else ("D" if w is None else "L"), r["hp_diff_a"] * (1 if s == 0 else -1), r["rounds"])


def load_base(path, sub, excl="catch_up_share=1.0"):
    out = {}
    for line in open(path):
        r = json.loads(line)
        s = r["candidate_side"]
        c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
        if sub not in c or excl in c or r.get("error"):
            continue
        out[(o, r.get("scenario"), s)] = outcome(r, s)
    return out


def load_cand(spec):
    out, conflict, meta = {}, set(), {"max": 0.0, "rej": 0, "err": 0}
    for run in RUNS:
        f = E + run + "/results.jsonl"
        if not os.path.exists(f):
            continue
        for line in open(f):
            r = json.loads(line)
            s = r["candidate_side"]
            c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
            if c != spec:
                continue
            if r.get("error"):
                meta["err"] += 1
                continue
            p = r["players"][s]
            meta["max"] = max(meta["max"], r["decide_max_seconds"][s])
            meta["rej"] += p["n_rejected"]
            meta["err"] += len(p["bot_errors"])
            k = (o, r.get("scenario"), s)
            v = outcome(r, s)
            if k in out and out[k] != v:
                conflict.add(k)
            out.setdefault(k, v)
    for k in conflict:
        out.pop(k)
    return out, conflict, meta


def wdl(d, keys):
    res = [d[k][0] for k in keys]
    return f"{res.count('W')}-{res.count('D')}-{res.count('L')}"


show = "--show" in sys.argv
bases = {pool: load_base(b, sub) for pool, b, sub, _ in GATE}
for sf in [a for a in sys.argv[1:] if a != "--show"]:
    spec = open(sf).read().strip()
    a, conflict, meta = load_cand(spec)
    print(f"## {os.path.basename(sf)}: {len(a)} conditions in lane runs, {len(conflict)} conflicts, "
          f"max decide {meta['max']:.2f} s, rejected {meta['rej']}, errors {meta['err']}")
    print("| Pool | shared/expected | candidate | best_v9e | worse | better | same outcome, other HP |")
    print("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
    tot = {"n": 0, "worse": 0, "better": 0, "hp": 0, "a": [], "b": []}
    for pool, _, _, n in GATE:
        b = bases[pool]
        keys = sorted(set(a) & set(b), key=lambda k: (k[0], str(k[1]), k[2]))
        if not keys:
            print(f"| {pool} | 0/{n} | | | | | |")
            continue
        worse = [k for k in keys if RANK[a[k][0]] < RANK[b[k][0]]]
        better = [k for k in keys if RANK[a[k][0]] > RANK[b[k][0]]]
        hp = [k for k in keys if a[k][0] == b[k][0] and a[k][1] != b[k][1]]
        tot["n"] += len(keys); tot["worse"] += len(worse); tot["better"] += len(better); tot["hp"] += len(hp)
        tot["a"] += [a[k][0] for k in keys]; tot["b"] += [b[k][0] for k in keys]
        print(f"| {pool} | {len(keys)}/{n} | {wdl(a, keys)} | {wdl(b, keys)} | {len(worse)} | {len(better)} | {len(hp)} |")
        if show:
            for tag, ks in (("worse", worse), ("better", better)):
                for k in ks:
                    o = k[0].split("bots.")[-1].split("lead.")[-1]
                    print(f"    {tag:6s} {a[k][0]} {a[k][1]:+6d} r{a[k][2]:<2d} | {b[k][0]} {b[k][1]:+6d} r{b[k][2]:<2d}"
                          f"  {k[1] or 'std'} s{k[2]} {o[:100]}")
    ca = "-".join(str(tot["a"].count(x)) for x in "WDL")
    cb = "-".join(str(tot["b"].count(x)) for x in "WDL")
    print(f"| total | {tot['n']}/846 | {ca} | {cb} | {tot['worse']} | {tot['better']} | {tot['hp']} |")
    print()
