# Builds research/closure_check/near_params_v03.json from the frozen near_params_v02.json (theory_agent_1) and theory_agent_2's
# near_params_r4_vNN.json: the four (R4) values of theory_agent_2's Proposition R4 (status UNAUDITED), the beta_star source
# updated for AT2386 and AT2402 (value and status unchanged), and the Lambda_plus wording of AT2432.
# Usage (from the lane root): python3 -B research/closure_check/mk_params_v03.py <r4 params file> <R4 note label> > research/closure_check/near_params_v03.json
import json, sys
A = json.load(open("research/closure_check/near_params_v02.json"))
B = json.load(open(sys.argv[1]))
NOTE = sys.argv[2]   # e.g. "notes/T2_NEAR_R4_v02.md"
VER = NOTE.rsplit("_", 1)[1].split(".")[0]   # "v02"
assert VER in ("v01", "v02", "v03"), VER
G = A["global"]
for k in G:
    if k not in ("sup_neg_aW2", "sup_pos_aW2", "L1_pos", "Lambda_plus"):
        assert G[k] == B["global"][k], k
for k in ("fixed", "cases"):
    assert A[k] == B[k], k
SRC = ("theory_agent_2 %s, Proposition R4 (CLAIMED; outward ball arithmetic with the Taylor-model panel engine of Theorem C1, "
       "AT-1230 to AT-1234, and the near cut factor; files listed in research/near_r4/SHA256SUMS_near_r4_%s of lane "
       "theory_agent_2); UNAUDITED until theory_audit's audit and numerical_audit's replay; (R4)" % (NOTE, VER))
R = {}
R["sup_neg_aW2"] = dict(value=B["global"]["sup_neg_aW2"]["value"], kind="upper", status="UNAUDITED",
                        source="upper of sup((a_n)_- W^2), W^2 = 1 + 4|x|^2; " + SRC)
R["sup_pos_aW2"] = dict(value=B["global"]["sup_pos_aW2"]["value"], kind="upper", status="UNAUDITED",
                        source="upper of sup((a_n)_+ W^2); " + SRC)
R["L1_pos"] = dict(value=B["global"]["L1_pos"]["value"], kind="upper", status="UNAUDITED",
                   source="upper of ||(a_n)_+||_1 (decimal rounded up); " + SRC)
R["Lambda_plus"] = dict(value=B["global"]["Lambda_plus"]["value"], kind="upper", status="UNAUDITED",
    source="outward upper U of Lambda_+(a_n) = sup max(0, lambda_max Hess a_n), with 0 <= U - F <= 4.330309019e-7; "
           "F = 8(2c - 1) = 2950576553396557/140737488355328, about 20.9651073632, is the origin value and a lower "
           "(AT2364). The FLOAT 20.862082 of near_params_v01 is below F and has no certified replacement (AT2365); its "
           "maximum with F is not a certified upper (AT2366, AT2432), and the value F of near_params_v02 was the "
           "uncertified target U = F. " + SRC)
for k, v in R.items():
    G[k] = v
G["beta_star"] = dict(G["beta_star"])
G["beta_star"]["source"] = (
    "the whole-plane matrix rate of the H4 join (AT2333). Both auditors certify M >= (704955805507/10^12) I on "
    "0 <= r^2 <= 61/67, that is t = r^2/(1 + r^2) in [0, 61/128], the roots 000 to 060 (numerical_audit AN695, AN700, AN706; "
    "theory_audit AT2372, AT2373, AT2384 to AT2386), and M >= (761272835221/10^12) I on r^2 >= 49/15 (AT2400 to AT2402; numerical_audit "
    "AN717). The gap 61/67 < r^2 < 49/15 is not recounted, so this value is not a whole-plane lower (AT2374, AT2403 "
    "OPEN); there the certified level is 3/5 on the certified roots and some roots have no certificate")
A["version"] = "near_params_v03"
A["written"] = ("2026-11-04 shift 8 (theory_agent_1); replaces near_params_v02 (unchanged and frozen) for near_check_v03.py. "
                "Against near_params_v02 only the four (R4) entries (values of %s of lane theory_agent_2, as in its "
                "near_params_r4_%s.json) and the sources of beta_star change" % (NOTE, VER))
A["use"] = A["use"].replace("UNAUDITED (an outward computation of this lane that no audit covers)",
                            "UNAUDITED (an outward computation of a team lane that no audit covers yet)")
assert "a team lane" in A["use"]
print(json.dumps(A, indent=1, ensure_ascii=True))
