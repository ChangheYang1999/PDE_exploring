"""FLOAT post-processing of data/t4_338_review_results.json for REVIEW_T4_338 R3: for each residual sector (K,L) of
F(R3) in [q* - 3/4, q*) after three cutoffs, the radius beyond which its forced tail ||F_(K,L)|| r^e/(1 - c e) is below
the endpoint coefficient d/(4c) r^q*, namely (||F_(K,L)||/((1 - c e) d/(4c)))^(1/(q* - e)) when the ratio exceeds 1.

Run from artifacts/:  python3 -B arith/t4_338_thresholds.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
R = json.loads((HERE / "data/t4_338_review_results.json").read_text())
c = 4076476460239181 / 2**51
qs = 1 / c - 4
mid = lambda s: float(s.strip("[]").split("+/-")[0])
OUT = {}
for name, row in R["B"].items():
    d4c = mid(row["D"]["d_over_4c"])
    out = []
    for rw in row["below_qstar_after_three"]:
        e = rw["exponent"]
        De = 1 - c * e
        ratio = mid(rw["norm"]) / (De * d4c)
        thr = ratio ** (1 / (qs - e)) if ratio > 1 else 1.0
        out.append({"sector": rw["sector"], "exponent": e, "gap": qs - e, "D": De, "ratio": ratio, "r_threshold": thr})
        print("%s (%d,%d) e = %.6f, q* - e = %.6f, 1 - c e = %.6f, ||F||/((1 - c e) d/(4c)) = %.6g, radius %.4g"
              % (name, rw["sector"][0], rw["sector"][1], e, qs - e, De, ratio, thr))
    OUT[name] = out
(HERE / "data/t4_338_thresholds.json").write_text(json.dumps(OUT, indent=1))
