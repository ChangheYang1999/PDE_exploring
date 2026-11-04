# Builds research/closure_check/near_params_v06.json from the frozen near_params_v05.json (theory_agent_1). One change: the
# three (R1) entries D4_an, D5_an and D6_an take the decimal uppers of numerical_audit's reviewed whole-plane consumer (the sum
# of the seven regional Laplacian-energy records; numerical_audit exchange v912, research/source013_near_norms/results/
# wholeplane_v02/PROOF.md of lane numerical_audit) with status
# CONFIRMED (theory_audit's actual review AT2869 to AT2871, audit_v872, adopted in numerical_audit exchange v917; checked below).
# Every other entry is unchanged.
# Usage (from the lane root): python3 -B research/closure_check/mk_params_v06.py <D4> <D5> <D6> "<source text>" > out.json
#   D4, D5, D6: the published decimal uppers; source text: the review and adoption IDs and versions, as read
import json, sys, re
from fractions import Fraction as Fr
D = dict(zip(("D4_an", "D5_an", "D6_an"), sys.argv[1:4])); SRC = sys.argv[4]
A = json.load(open("research/closure_check/near_params_v05.json"))
G = A["global"]
old = {k: G[k]["value"] for k in D}
assert old == {"D4_an": "444.194", "D5_an": "4186.35", "D6_an": "63050.4"}, old
# the preview of research/near_preview/sum_v01.out (12:52:12Z): D4 in [444.194, 444.195], D5 in [4186.352, 4186.353],
# D6 in [63050.392, 63050.393]; a published upper must be at least the preview lower and the certified D6 lower 62748
for k, lo in (("D4_an", "444.194"), ("D5_an", "4186.352"), ("D6_an", "63050.392")):
    assert Fr(D[k]) >= Fr(lo), (k, D[k])
assert Fr(D["D6_an"]) >= 62748
# the values are the strict upper endpoints of numerical_audit's executed consumer (numerical_audit exchange v912), whose global brackets
# theory_audit's actual review CONFIRMS (AT2869 to AT2871, audit_v872; AT2872 OPEN)
X = open("../numerical_audit/exchange/audit_v912.md").read()
assert X.startswith("# Numerical audit exchange v912: Whole-plane near consumer and independent arithmetic completed")
rows = dict((int(o), (lo, hi)) for o, lo, hi in re.findall(r"^\| ([456]) \| ([\d.]+) \| ([\d.]+) \|$", X, re.M))
assert {"D4_an": rows[4][1], "D5_an": rows[5][1], "D6_an": rows[6][1]} == D, (rows, D)
Y = open("../theory_audit/exchange/audit_v872.md").read()
assert "The actual whole-plane near assembly is independently CONFIRMED." in Y
assert re.findall(r"^## AT(\d+),", Y, re.M) == ["2869", "2870", "2871", "2872"]
assert re.findall(r"^Verdict: (\w+)", Y, re.M) == ["CONFIRMED", "CONFIRMED", "CONFIRMED", "OPEN"]
Z = open("../numerical_audit/exchange/audit_v917.md").read()
assert Z.startswith("# Numerical audit exchange v917: Whole-plane near derivative norms and NR25 inputs actually admitted")
rz = dict((int(o), (lo, hi)) for o, lo, hi in re.findall(r"^\| ([456]) \| ([\d.]+) \| ([\d.]+) \|$", Z, re.M))
assert rz == rows, (rz, rows)
assert "audit IDs AT2869, AT2870, AT2871, AT2872." in Z
names = {"D4_an": "D_4(a_n) = ||Delta^2 a_n||_2", "D5_an": "D_5(a_n) = ||grad Delta^2 a_n||_2",
         "D6_an": "D_6(a_n) = ||Delta^3 a_n||_2"}
for k in D:
    G[k] = {"value": D[k], "kind": "upper", "status": "CONFIRMED",
            "source": "whole-plane upper of %s (NR-25 normalization; the full Cartesian tensor norm); " % names[k] + SRC}
A["version"] = "near_params_v06"
A["written"] = ("2026-11-04 shift 8 (theory_agent_1); replaces near_params_v05 (unchanged and frozen) for near_check_v03.py. "
                "Against near_params_v05 only D4_an, D5_an and D6_an change: FLOAT values replaced by the certified "
                "whole-plane uppers of numerical_audit's reviewed and adopted consumer; every other entry is unchanged")
B = json.load(open("research/closure_check/near_params_v05.json"))
for k in B["global"]:
    if k not in D: assert G[k] == B["global"][k], k
for k in B:
    if k not in ("global", "version", "written"): assert A[k] == B[k], k
print(json.dumps(A, indent=1, ensure_ascii=True))
