"""af5 (frr7, frr8) against V29 and g1 (frr2, frr5, frr6) condition by condition (descriptive).

    python3 tmp/cmp_af5_v29.py

af5 = V29 + attack_from=5 and g1 = V29 + attack_from=7 (specs end with these suffixes). Conditions are (opponent,
scenario, seat). Prints differences in winner, HP difference or length, then counts. af5's games against V29 and g1
are compared with g1 against V29 in the same seat.
"""
import json


def load(path):
    for line in open(path):
        r = json.loads(line)
        if not r.get("error"):
            yield r


def index(rows, me):
    out = {}
    for r in rows:
        for seat, (m, o) in enumerate(((r["spec_a"], r["spec_b"]), (r["spec_b"], r["spec_a"]))):
            if m == me:
                w = r["winner"]
                res = "W" if w == seat else ("D" if w is None else "L")
                out[(o, r["scenario"], seat)] = (res, r["hp_diff_a"] * (1 if seat == 0 else -1), r["rounds"])
    return out


new = list(load("runs/lead/frr7/results.jsonl"))
try:
    new += list(load("runs/lead/frr8/results.jsonl"))
except FileNotFoundError:
    pass
af5 = [s for s in (new[0]["spec_a"], new[0]["spec_b"]) if s.endswith("&attack_from=5")][0]
V29 = af5[: -len("&attack_from=5")]
G1 = V29 + "&attack_from=7"
A = index(new, af5)
old = []
for p in ("runs/lead/frr2/results.jsonl", "runs/lead/frr5/results.jsonl", "runs/lead/frr6/results.jsonl"):
    old += list(load(p))
for name, me in (("V29", V29), ("g1", G1)):
    B = index(old, me)
    same = diff = missing = 0
    for k, v in sorted(A.items(), key=lambda kv: (kv[0][0], str(kv[0][1]), kv[0][2])):
        if k[0] in (V29, G1):
            continue
        if k not in B:
            missing += 1
        elif B[k] == v:
            same += 1
        else:
            diff += 1
            print(name, "DIFF", k[0][-40:], k[1], k[2], "af5", v, name, B[k])
    print(name, "same", same, "different", diff, "not in the old runs", missing)
B = index(old, G1)
for k, v in A.items():
    if k[0] in (V29, G1):
        print("af5 vs", "V29" if k[0] == V29 else "g1", k[1], k[2], v, "| g1 vs V29, same seat:", B.get((V29, k[1], k[2])))
