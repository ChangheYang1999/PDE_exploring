"""Lead check of hrt-w3's 846 dedup claim: count distinct (opponent, scenario, seat) keys over the R13 gate pools
and the W-D-L of a candidate and best_v9e on the distinct keys (all, and outside GROWERS/GUARDED_MAZE/HANDOFF/f5t).
python3 bot_research/tmp/dedup846.py SPEC_SH_VAR...  (from the project root; specs from experiments/lead/rr_specs.sh)"""
import json, os, re, subprocess, sys
L, T, E = "bot_research/runs/lead/", "bot_research/tmp/", "bot_research/runs/economy/"
GATE = [("PCS", L + "g13pc/results.jsonl", "best_v9e:@make"), ("TIMING", L + "bse_tm/results.jsonl", "best_v9e:@make"),
        ("TIMING2", L + "tm2/results.jsonl", "foreign_target"), ("STRIKE1", E + "strike1b/results.jsonl", "best_v9e:@make"),
        ("TARGETED2", T + "base_t8f_v18f.jsonl", "fortress_guns=true&catch_up=true"), ("f5t", L + "ab1/results.jsonl", "best_v9e:@make"),
        ("PUNISH", L + "pu1/results.jsonl", "foreign_target"), ("BLUFFCOV", T + "base_b9a_v18f.jsonl", "foreign_target"),
        ("TARGETED3_P5TF", L + "t9k/results.jsonl", "foreign_target"), ("HANDOFF", L + "bse_hd/results.jsonl", "best_v9e:@make"),
        ("SCREENED", L + "bse_sg/results.jsonl", "best_v9e:@make"), ("GROWERS", L + "g9a/results.jsonl", "foreign_target"),
        ("GUARDED_MAZE", T + "base_gm2_v18f.jsonl", "foreign_target"), ("STAGED", T + "base_st1_v18f.jsonl", "foreign_target")]
SEL = {"GROWERS", "GUARDED_MAZE", "HANDOFF", "f5t"}
RANK = {"W": 2, "D": 1, "L": 0}
def rows(path):
    for line in open(path):
        r = json.loads(line); s = r["candidate_side"]
        c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
        if r.get("error"): continue
        w = r["winner"]; yield c, (o, r.get("scenario"), s), ("W" if w == s else ("D" if w is None else "L"))
pools = {}
for p, f, sub in GATE:
    pools[p] = {k: v for c, k, v in rows(f) if sub in c and "catch_up_share=1.0" not in c}
mem = sum(len(d) for d in pools.values())
base, clash = {}, 0
for d in pools.values():
    for k, v in d.items():
        if k in base and base[k] != v: clash += 1
        base.setdefault(k, v)
sel = set().union(*(set(pools[p]) for p in SEL))
rest = set(base) - sel
print(f"memberships {mem}, distinct {len(base)}, base clashes {clash}, distinct outside selection pools {len(rest)}")
spec_sh = open("bot_research/experiments/lead/rr_specs.sh").read()
def wdl(d, ks): x = [d[k] for k in ks]; return f"{x.count('W')}-{x.count('D')}-{x.count('L')}"
print("base", "all", wdl(base, base), "rest", wdl(base, rest))
for var in sys.argv[1:]:
    spec = subprocess.run(["bash", "-c", f". bot_research/experiments/lead/rr_specs.sh; printf %s \"${var}\""], capture_output=True, text=True).stdout
    cand = {}
    for run in sorted(os.listdir(E)):
        f = E + run + "/results.jsonl"
        if os.path.exists(f):
            for c, k, v in rows(f):
                if c == spec and k in base: cand.setdefault(k, v)
    miss = len(set(base) - set(cand))
    for name, ks in (("all", set(base)), ("rest", rest)):
        ks = ks & set(cand)
        worse = sum(RANK[cand[k]] < RANK[base[k]] for k in ks); better = sum(RANK[cand[k]] > RANK[base[k]] for k in ks)
        print(var, name, len(ks), "cand", wdl(cand, ks), "base", wdl(base, ks), "worse", worse, "better", better, "missing", miss)
