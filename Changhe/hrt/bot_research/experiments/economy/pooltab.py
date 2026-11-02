"""Per-pool W-D-L per candidate and paired score differences (hrt-w2).

    python3 -B bot_research/experiments/economy/pooltab.py RESULTS POOLS_JSON TAG=SUFFIX [TAG=SUFFIX...]   (from the project root)

RESULTS is a results.jsonl file or a comma-separated list of them. POOLS_JSON maps opponent spec -> list of pools, or
pool -> list of specs. A row belongs to TAG if its candidate spec ends with SUFFIX; a condition is (opponent spec,
scenario, seat), and a later row of the same condition replaces an earlier one. Each pool table uses only the
conditions present for every TAG. Score W 1, D 0.5, L 0. Pairs: the first tag minus each other tag, cluster bootstrap
over opponent specs (4000 resamples, seed 1, 2.5 and 97.5 percentiles)."""
import json, random, sys, collections
files, pj = sys.argv[1], sys.argv[2]
C = [a.split("=", 1) for a in sys.argv[3:]]
P = json.load(open(pj))
if all(isinstance(v, list) and v and v[0].startswith("bot_research") for v in P.values()):
    P2 = collections.defaultdict(list)
    for pool, specs in P.items():
        for s in specs: P2[s].append(pool)
    P = P2
d = {t: {} for t, _ in C}; meta = {t: [0.0, 0, 0] for t, _ in C}
for l in (l for f in files.split(",") for l in open(f)):
    r = json.loads(l); s = r["candidate_side"]; c = r["spec_a"] if s == 0 else r["spec_b"]; o = r["spec_b"] if s == 0 else r["spec_a"]
    for t, suf in C:
        if c.endswith(suf):
            w = r["winner"]; x = 1.0 if w == s else (0.5 if w is None else 0.0)
            hp = r["hp_diff_a"] if s == 0 else -r["hp_diff_a"]
            d[t][(o, r.get("scenario"), s)] = (x, hp, r["rounds"])
            p = r["players"][s]; m = meta[t]
            m[0] = max(m[0], r["decide_max_seconds"][s]); m[1] += p["n_rejected"]; m[2] += len(p["bot_errors"]) + (1 if r.get("error") else 0)
pools = sorted({p for v in P.values() for p in v})
def wdl(v): return f"{sum(x[0]==1 for x in v)}-{sum(x[0]==0.5 for x in v)}-{sum(x[0]==0 for x in v)}"
def boot(keys, a, b):
    opp = sorted({k[0] for k in keys}); by = collections.defaultdict(list)
    for k in keys: by[k[0]].append(a[k][0] - b[k][0])
    mean = sum(sum(by[o]) for o in opp) / len(keys); rng = random.Random(1); ms = []
    for _ in range(4000):
        smp = [rng.choice(opp) for _ in opp]; n = sum(len(by[o]) for o in smp)
        ms.append(sum(sum(by[o]) for o in smp) / n)
    ms.sort(); return mean, ms[100], ms[3899]
print("| pool | n | " + " | ".join(t for t, _ in C) + " |")
print("| --- | ---: | " + " | ".join("---" for _ in C) + " |")
for pool in pools + ["ALL"]:
    keys = None
    for t, _ in C:
        ks = {k for k in d[t] if pool == "ALL" or pool in P.get(k[0], [])}
        keys = ks if keys is None else keys & ks
    if not keys: continue
    print(f"| {pool} | {len(keys)} | " + " | ".join(wdl([d[t][k] for k in keys]) for t, _ in C) + " |")
print()
for t, _ in C: print(f"{t}: max decide {meta[t][0]:.2f} s, rejected {meta[t][1]}, errors {meta[t][2]}, games {len(d[t])}")
t0 = C[0][0]
for t, _ in C[1:]:
    for pool in pools + ["ALL"]:
        keys = [k for k in set(d[t0]) & set(d[t]) if pool == "ALL" or pool in P.get(k[0], [])]
        if len({k[0] for k in keys}) < 2: continue
        m, lo, hi = boot(keys, d[t0], d[t])
        print(f"{t0} - {t}, {pool}: score {m:+.3f} [{lo:+.3f}, {hi:+.3f}] over {len(keys)} games, {len({k[0] for k in keys})} opponents")
