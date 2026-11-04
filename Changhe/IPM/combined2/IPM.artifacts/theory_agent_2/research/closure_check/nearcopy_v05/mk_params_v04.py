# Builds research/closure_check/near_params_v04.json from the frozen near_params_v03.json (theory_agent_1) and theory_agent_2's
# near_params_r4_v01.json: the four (R4) entries take the values of Proposition R4 in its version 1, which theory_audit
# CONFIRMS as global uppers after numerical_audit's complete replay (AT2477 to AT2479); every other entry is unchanged.
# Usage (from the lane root): python3 -B research/closure_check/mk_params_v04.py <theory_agent_2 near_params_r4_v01.json> > out.json
import json, sys
from fractions import Fraction as Fr
A = json.load(open("research/closure_check/near_params_v03.json"))
B = json.load(open(sys.argv[1]))
R4 = ("sup_neg_aW2", "sup_pos_aW2", "L1_pos", "Lambda_plus")
G = A["global"]
for k in G:
    if k == "beta_star":   # near_params_v03 rewrote only its source text (AT2386, AT2402)
        assert all(G[k][f] == B["global"][k][f] for f in G[k] if f != "source"), k
    elif k not in R4:
        assert G[k] == B["global"][k], k
assert set(G) == set(B["global"])
for k in ("fixed", "cases"):
    assert A[k] == B[k], k
# the values of theory_agent_2's version 1 file and the certified uppers of theory_audit audit_v756 (AT2478)
V = {k: B["global"][k]["value"] for k in R4}
assert V["Lambda_plus"] == "5901153228680477/281474976710656"
assert V["sup_neg_aW2"] == "2442770293098857/281474976710656"
assert V["sup_pos_aW2"] == "4811915830260861/562949953421312"
assert V["L1_pos"] == "4.161116960"
assert Fr(21605754517791033335004488160772637, 5192296858534827628530496329220096) <= Fr("4.161116960")
F = Fr(2950576553396557, 140737488355328)
assert Fr(V["Lambda_plus"]) - F == Fr(121887363, 281474976710656) < Fr("4.330309019e-7")
SRC = ("theory_agent_2 notes/T2_NEAR_R4_v01.md, Proposition R4 version 1 (Taylor-model panel engine of Theorem C1, AT-1230 to "
       "AT-1234, with the near cut factor; files in research/near_r4/SHA256SUMS_near_r4_v01 of lane theory_agent_2). CONFIRMED "
       "as a global upper for the exact Source013 near coefficient under the admitted C1 source and "
       "containing-arithmetic hypotheses: method AT2447 to AT2449, numerical_audit's complete independent replay AN730 and "
       "theory_audit's actual review AT2477 to AT2479 (theory_audit audit_v756); (R4)")
for k in R4:
    G[k] = dict(G[k])
    G[k]["value"] = V[k]
    G[k]["status"] = "CONFIRMED"
G["sup_neg_aW2"]["source"] = "upper of sup((a_n)_- W^2), W^2 = 1 + 4|x|^2; " + SRC
G["sup_pos_aW2"]["source"] = "upper of sup((a_n)_+ W^2); " + SRC
G["L1_pos"]["source"] = ("upper of ||(a_n)_+||_1, the decimal 4.161116960 rounded up from the certified exact upper "
                         "21605754517791033335004488160772637/5192296858534827628530496329220096 (AT2478); " + SRC)
G["Lambda_plus"]["source"] = (
    "certified upper U of Lambda_+(a_n) = sup max(0, lambda_max Hess a_n). F = 8(2c - 1) = "
    "2950576553396557/140737488355328, about 20.9651073632, is the origin value and a lower (AT2364), and "
    "U - F = 121887363/281474976710656 < 4.330309019e-7 (AT2479). " + SRC)
A["version"] = "near_params_v04"
A["written"] = ("2026-11-04 shift 8 (theory_agent_1); replaces near_params_v03 (unchanged and frozen) for near_check_v03.py. "
                "Against near_params_v03 only the four (R4) entries change: they take the version 1 values of "
                "Proposition R4 (lane theory_agent_2, near_params_r4_v01.json), status CONFIRMED (AT2477 to AT2479). The "
                "smaller version 2 values of near_params_v03 stay UNAUDITED until their 78 fine panels are replayed")
print(json.dumps(A, indent=1, ensure_ascii=True))
