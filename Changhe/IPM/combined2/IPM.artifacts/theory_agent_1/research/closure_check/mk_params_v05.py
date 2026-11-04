# Builds research/closure_check/near_params_v05.json from the frozen near_params_v03.json (theory_agent_1), which carries the
# values of Proposition R4 in its version 2 (lane theory_agent_2) with status UNAUDITED. Two changes: the four (R4) entries
# take status CONFIRMED (theory_audit's actual review of numerical_audit's complete refined replay, AT2520 to AT2522, audit_v767;
# adopted by numerical_audit, exchange v750), and beta_star takes status CONFIRMED as a whole-plane lower (theory_audit's actual review
# of numerical_audit's executed complete background union, AT2534 to AT2536, audit_v771). Every value is unchanged.
# Usage (from the lane root): python3 -B research/closure_check/mk_params_v05.py "<adoption text>" > out.json
#   adoption text: the state of numerical_audit's adoption of the union review AT2534, as read before the run
import json, sys
from fractions import Fraction as Fr
ADOPT = sys.argv[1]
A = json.load(open("research/closure_check/near_params_v03.json"))
B = json.load(open("research/closure_check/near_params_v04.json"))   # the version 1 record, for the unchanged entries
R4 = ("sup_neg_aW2", "sup_pos_aW2", "L1_pos", "Lambda_plus")
G = A["global"]
assert set(G) == set(B["global"])
for k in G:
    if k not in R4:
        assert G[k] == B["global"][k], k
for k in ("fixed", "cases"):
    assert A[k] == B[k], k
# the values of version 2 and the certified uppers of theory_audit audit_v767 (AT2521) and numerical_audit exchange v750
V = {k: G[k]["value"] for k in R4}
assert V["Lambda_plus"] == "5901153228680477/281474976710656"
assert V["sup_neg_aW2"] == "4877321332131611/562949953421312"
assert V["sup_pos_aW2"] == "4806001960566741/562949953421312"
assert V["L1_pos"] == "4.086439259"
L1 = Fr(21218005723912562034147590433407517, 5192296858534827628530496329220096)
assert L1 <= Fr("4.086439259") and Fr("4.086439258") < L1
F = Fr(2950576553396557, 140737488355328)
assert Fr(V["Lambda_plus"]) - F == Fr(121887363, 281474976710656) < Fr("4.330309019e-7")
# version 2 is at most version 1 entrywise (so every term of the program is at most its version 1 value)
for k in R4:
    assert Fr(V[k]) <= Fr(B["global"][k]["value"]), k
assert G["beta_star"]["value"] == "704955805507/1000000000000" and G["beta_star"]["kind"] == "lower"
SRC = ("theory_agent_2 notes/T2_NEAR_R4_v02.md, Proposition R4 version 2 (Taylor-model panel engine of Theorem C1, AT-1230 to "
       "AT-1234, with the near cut factor; finer cells on -1/2 <= log|x| <= 7/2; files in "
       "research/near_r4/SHA256SUMS_near_r4_v02 of lane theory_agent_2). CONFIRMED as a global upper for the exact Source013 "
       "near coefficient under the admitted exact Source013 and C1 containing-arithmetic hypotheses: method AT2467 to "
       "AT2469, numerical_audit's complete independent refined replay and theory_audit's actual review AT2520 to AT2522 (theory_audit "
       "audit_v767), adopted by numerical_audit (exchange v750); AT2523 OPEN; (R4)")
for k in R4:
    G[k] = dict(G[k])
    G[k]["status"] = "CONFIRMED"
G["sup_neg_aW2"]["source"] = "upper of sup((a_n)_- W^2), W^2 = 1 + 4|x|^2; " + SRC
G["sup_pos_aW2"]["source"] = "upper of sup((a_n)_+ W^2); " + SRC
G["L1_pos"]["source"] = ("upper of ||(a_n)_+||_1, the decimal 4.086439259 rounded up from the certified exact upper "
                         "21218005723912562034147590433407517/5192296858534827628530496329220096 (AT2521); " + SRC)
G["Lambda_plus"]["source"] = (
    "certified upper U of Lambda_+(a_n) = sup max(0, lambda_max Hess a_n), unchanged from version 1. F = 8(2c - 1) = "
    "2950576553396557/140737488355328, about 20.9651073632, is the origin value and a lower (AT2364), and "
    "U - F = 121887363/281474976710656 < 4.330309019e-7 (AT2479, AT2522). " + SRC)
G["beta_star"] = dict(G["beta_star"])
G["beta_star"]["status"] = "CONFIRMED"
G["beta_star"]["source"] = (
    "the whole-plane matrix rate of the H4 join (AT2333). theory_audit's actual review of numerical_audit's executed complete "
    "background union (numerical_audit exchange v749) CONFIRMS M >= (704955805507/10^12) I, |grad h| <= 1/4 and "
    "||Sym Du||_op <= 137/125 on the whole plane under the admitted exact-source and containing-arithmetic "
    "hypotheses (AT2534 to AT2536, audit_v771; AT2537 OPEN): the minimum of the inner lower 704955805507/10^12 on "
    "0 <= r^2 <= 61/67 (AT2386), the host lower 890672299617/10^12 on 7/9 <= r^2 <= 49/15 (AT2512 to AT2514; adopted, "
    "numerical_audit exchange v749) and the outer lower 761272835221/10^12 on r^2 >= 49/15 (AT2402). " + ADOPT)
A["version"] = "near_params_v05"
A["written"] = ("2026-11-04 shift 8 (theory_agent_1); replaces near_params_v04 (unchanged and frozen) for near_check_v03.py. "
                "It has the values of near_params_v03 (Proposition R4 version 2, lane theory_agent_2); against near_params_v03 "
                "the four (R4) entries take status CONFIRMED (AT2520 to AT2522; numerical_audit exchange v750) and beta_star "
                "takes status CONFIRMED as a whole-plane lower (AT2534 to AT2536); every value is unchanged")
print(json.dumps(A, indent=1, ensure_ascii=True))
