"""H14 gate: AS1C runs against best_v9e's runs on the R13 gate pools (development only).

    python3 tmp/h14_gate.py [--show]

For each pool: AS1C W-D-L, best_v9e W-D-L on the shared conditions, the conditions where AS1C's outcome is worse
(W > D > L), better, and same outcome with a different HP difference; AS1C's max decide time, rejected actions and
bot errors. --show lists every changed condition.
"""
import json, os, sys

L = "runs/lead/"
CAND = "attack_share=1.0&catch_up_share=0.5"
GATE = [  # pool, AS1C run, base file, base substring, expected conditions
    ("PCS", L + "h14pc", L + "g13pc/results.jsonl", "best_v9e:@make", 8),
    ("TIMING", L + "h14tm", L + "bse_tm/results.jsonl", "best_v9e:@make", 32),
    ("TIMING2", L + "h14tm2", L + "tm2/results.jsonl", "foreign_target", 40),
    ("STRIKE1", L + "h14s1", "runs/economy/strike1b/results.jsonl", "best_v9e:@make", 40),
    ("TARGETED2", L + "h14t2", "tmp/base_t8f_v18f.jsonl", "fortress_guns=true&catch_up=true", 48),
    ("f5t", L + "h14f", L + "ab1/results.jsonl", "best_v9e:@make", 76),
    ("PUNISH", L + "h14pu", L + "pu1/results.jsonl", "foreign_target", 34),
    ("BLUFFCOV", L + "h14b", "tmp/base_b9a_v18f.jsonl", "foreign_target", 16),
    ("TARGETED3_P5TF", L + "h14t3", L + "t9k/results.jsonl", "foreign_target", 30),
    ("HANDOFF", L + "h14hd", L + "bse_hd/results.jsonl", "best_v9e:@make", 36),
    ("SCREENED", L + "h14sg", L + "bse_sg/results.jsonl", "best_v9e:@make", 60),
    ("GROWERS", L + "h14g", L + "g9a/results.jsonl", "foreign_target", 142),
    ("GUARDED_MAZE", L + "h14gm", "tmp/base_gm2_v18f.jsonl", "foreign_target", 144),
    ("STAGED", L + "h14st", "tmp/base_st1_v18f.jsonl", "foreign_target", 140),
]
RANK = {"W": 2, "D": 1, "L": 0}


def load(path, sub, excl=None):
    out, meta = {}, {"max": 0.0, "rej": 0, "err": 0, "rows": 0}
    for line in open(path):
        r = json.loads(line)
        s = r["candidate_side"]
        c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
        if sub not in c or (excl and excl in c):
            continue
        meta["rows"] += 1
        if r.get("error"):
            meta["err"] += 1
            continue
        p = r["players"][s]
        meta["max"] = max(meta["max"], r["decide_max_seconds"][s])
        meta["rej"] += p["n_rejected"]
        meta["err"] += len(p["bot_errors"])
        w = r["winner"]
        res = "W" if w == s else ("D" if w is None else "L")
        out[(o, r.get("scenario"), s)] = (res, r["hp_diff_a"] * (1 if s == 0 else -1), r["rounds"])
    return out, meta


def wdl(d, keys):
    res = [d[k][0] for k in keys]
    return f"{res.count('W')}-{res.count('D')}-{res.count('L')}"


show = "--show" in sys.argv
tot = {"n": 0, "worse": 0, "better": 0, "hp": 0}
print("| Pool | n/expected | AS1C | best_v9e | worse | better | same outcome, other HP | max s | rej | err |")
print("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
for pool, run, base, bsub, n in GATE:
    f = run + "/results.jsonl"
    if not os.path.exists(f):
        print(f"| {pool} | not started | | | | | | | | |")
        continue
    a, am = load(f, CAND)
    b, _ = load(base, bsub, "catch_up_share=1.0")
    keys = sorted(set(a) & set(b), key=lambda k: (k[0], str(k[1]), k[2]))
    worse = [k for k in keys if RANK[a[k][0]] < RANK[b[k][0]]]
    better = [k for k in keys if RANK[a[k][0]] > RANK[b[k][0]]]
    hp = [k for k in keys if a[k][0] == b[k][0] and a[k][1] != b[k][1]]
    tot["n"] += len(keys); tot["worse"] += len(worse); tot["better"] += len(better); tot["hp"] += len(hp)
    print(f"| {pool} | {len(keys)}/{n} | {wdl(a, keys)} | {wdl(b, keys)} | {len(worse)} | {len(better)} | {len(hp)} "
          f"| {am['max']:.2f} | {am['rej']} | {am['err']} |")
    if show:
        for tag, ks in (("worse", worse), ("better", better), ("hp", hp)):
            for k in ks:
                o = k[0].split("bots.")[-1].split("lead.")[-1]
                print(f"    {tag:6s} {a[k][0]} {a[k][1]:+6d} r{a[k][2]:<2d} | {b[k][0]} {b[k][1]:+6d} r{b[k][2]:<2d}"
                      f"  {k[1] or 'std'} s{k[2]} {o[:100]}")
print(f"total shared {tot['n']} of 846; worse {tot['worse']}, better {tot['better']}, same outcome other HP {tot['hp']}")
