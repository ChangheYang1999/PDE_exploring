"""Exact jet comparisons, norm conversion, and interval analytic-bound examples.

The complex analyticity assumptions in PROOF.md are hypotheses, not established
properties of a PDE profile. All arithmetic in these examples is certified.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
import sys
import json
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/"obstruction_certificate/verification"))
from certify import I, iv, record, bounds

ROOT = Path(__file__).resolve().parent


def main():
    numerical = json.loads((ROOT/"numerical_comparison.json").read_text())
    jet_lower = {}
    for name, row in numerical["pairs"].items():
        exact = sum(abs(F(x)) for x in row["jet_differences_exact"].values())
        assert exact == F(row["jet_sum_exact"])
        assert exact > F("0.03")
        jet_lower[name] = str(exact)

    # For phi_j-u^j, the weighted second derivative equals -a*u+b*u^3.
    # a-3*b*u^2 is positive throughout [0,1/2], so the absolute value
    # increases up to its stated rational maximum.
    maxima = {}
    for j, a, b in ((3,288,330), (5,216,220), (7,144,110)):
        assert F(a)-3*F(b)/4 > 0
        maxima[j] = F(a,2)-F(b,8)
    assert max(maxima.values()) == F(411,4)

    a, b, rho, M = F("0.02"), F("0.985"), F(4), F(10)
    radius = F("0.0000045")
    examples = []
    for d in map(F, ("0.05","0.1","0.2","0.3","0.4")):
        v = I((max(a+b,2-a-b)+2*d)/(b-a))
        rd = v+iv.sqrt(v*v-1)
        lam = 1-iv.log(rd)/iv.log(I(rho))
        assert bounds(lam)[0] > 0
        C = I(d**(-3)+d**(-5)+d**(-7)+36*d**(-9)+2*d**(-2))
        C += 6*iv.exp(I(F(1,10))*iv.log(I(F(1,2))))/I(d**3)
        def estimate(delta):
            return C*iv.exp((1-lam)*iv.log(I(M))+lam*iv.log(I(delta)))
        needed = I(M)*iv.exp(iv.log(I(radius)/(C*I(M)))/lam)
        examples.append({"d":str(d), "lambda":record(lam), "C":record(C),
                         "N_bound_delta_1e-7":record(estimate(F("1e-7"))),
                         "N_bound_delta_1e-6":record(estimate(F("1e-6"))),
                         "delta_threshold":record(needed)})
    # Exact sample interpolation illustration, with discs of radius 1/2.
    # E_4 contains those discs about every point of [a,b]: their focal
    # distance sum is <= (b-a)+1, strictly below the ellipse boundary sum.
    dband = F(1,2)
    assert b-a+2*dband < (b-a)*(rho+1/rho)/2
    sample_error, gap = F("0.0000003"), F(1,700)
    uniform_error = sample_error+M*gap**2/(4*dband**2)
    data = {"status":"exact rational and mpmath.iv arithmetic; analytic hypotheses conditional",
            "jet_lower_bounds":jet_lower,
            "conversion_maxima":{str(k):str(v) for k,v in maxima.items()},
            "norm_conversion":str(F(415,4)),
            "examples":examples, "uniform_error_sample_example":str(uniform_error)}
    (ROOT/"analytic_bound_certificate.json").write_text(json.dumps(data,indent=2)+"\n")
    for row in examples:
        print("d",row["d"],"lambda",row["lambda"]["display"],
              "bound",row["N_bound_delta_1e-7"]["display"],
              "threshold",row["delta_threshold"]["display"])
    print("sample uniform bound", uniform_error, float(uniform_error))


if __name__ == "__main__":
    main()
