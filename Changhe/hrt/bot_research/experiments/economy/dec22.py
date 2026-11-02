"""Decision rule of notes/economy.md 18.22 and 18.25 for the attack-hold sweep (hrt-w2).

    python3 -B bot_research/experiments/economy/dec22.py   (from the project root)

For af6 (runs/economy/afs6) and af5 (runs/economy/afs5) against g1 on the 290 conditions of opp_afsweep.txt (pools in
opp_afsweep_pools.json; g1 rows from gate1, fam2b, g1chk and hand3): a value qualifies if all 290 of its conditions
are present, it has more wins than g1 in total, and on no pool more than 2 fewer wins than g1. If both qualify, the one
with more wins in total is chosen; on a tie, af6. Prints a table and, on the last line, the chosen spec file
(experiments/economy/specs/af6.spec or af5.spec) or NONE.
"""
import json

E = "bot_research/experiments/economy/"
R = "bot_research/runs/economy/"
P = json.load(open(E + "opp_afsweep_pools.json"))
POOL = {s: p for p, ss in P.items() for s in ss}
SUF = {"g1": "fill_threat=true&attack_from=7", "af6": "fill_threat=true&attack_from=6",
       "af5": "fill_threat=true&attack_from=5"}
RUNS = {"g1": ["gate1", "fam2b", "g1chk", "hand3"], "af6": ["afs6"], "af5": ["afs5"]}


def wins(tag):
    out = {}
    for run in RUNS[tag]:
        try:
            lines = open(R + run + "/results.jsonl").readlines()
        except FileNotFoundError:
            continue
        for line in lines:
            r = json.loads(line)
            s = r["candidate_side"]
            c, o = (r["spec_a"], r["spec_b"]) if s == 0 else (r["spec_b"], r["spec_a"])
            if o in POOL and r.get("scenario") is None and c.endswith(SUF[tag]) and not r.get("error"):
                out[(o, s)] = r["winner"] == s
    return out


base = wins("g1")
assert len(base) == 2 * len(POOL), len(base)
pools = sorted(P)
qual = {}
print("| value | conditions | wins | g1 wins | " + " | ".join(pools) + " | qualifies |")
for tag in ("af6", "af5"):
    a = wins(tag)
    per = {p: (sum(a[k] for k in a if POOL[k[0]] == p), sum(base[k] for k in base if POOL[k[0]] == p)) for p in pools}
    tot, tg = sum(a.values()), sum(base.values())
    ok = len(a) == len(base) and tot > tg and all(x >= y - 2 for x, y in per.values())
    if ok:
        qual[tag] = tot
    print(f"| {tag} | {len(a)} | {tot} | {tg} | " + " | ".join(f"{x}/{y}" for x, y in per.values()) + f" | {ok} |")
if not qual:
    print("NONE")
else:
    best = max(qual.values())
    pick = "af6" if qual.get("af6") == best else "af5"
    print(E + "specs/" + pick + ".spec")
