"""Exact arithmetic checks for the T4 correction-based closure criterion.

This verifies algebra and sample sufficient boxes only. It does not certify
any numerical IPM candidate, any derivative bound, or any operator inverse.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
import json
from pathlib import Path


def rational(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def check_box(m, eps, B, r):
    s = Q(1, 2**18)
    sqrt_s = Q(1, 2**9)
    mu = Q(1, 10) - 4800 * s
    A = 5 / sqrt_s
    beta = mu - A*r
    slack = (r-m)*beta - B*r - eps
    expanded = -A*r*r + (mu+A*m-B)*r - mu*m - eps
    assert beta > 0 and r >= m and slack > 0
    assert slack == expanded
    discriminant = (mu+A*m-B)**2 - 4*A*(mu*m+eps)
    alternate = (mu-A*m-B)**2 - 4*A*(B*m+eps)
    assert discriminant == alternate
    return {
        "s": rational(s), "m_upper": rational(m), "epsilon_upper": rational(eps),
        "B_upper": rational(B), "r": rational(r), "mu": rational(mu),
        "A": rational(A), "beta_lower": rational(beta), "slack_lower": rational(slack),
        "discriminant": rational(discriminant),
        "beta_decimal_diagnostic": float(beta),
        "slack_decimal_diagnostic": float(slack),
        "all_exact_checks_passed": True,
    }


boxes = [check_box(Q(1,2**17), Q(1,2**23), Q(1,100), Q(1,2**16)),
         check_box(Q(1,2**16), Q(1,2**25), Q(1,200), Q(3,2**17))]
# Weighted norm bookkeeping. e=(P,128 a,512 b,512 sqrt(b0) H).
assert Q(2,128)==Q(1,64)
assert Q(128,512)==Q(1,4)
assert Q(34,128)==Q(17,64)
assert Q(128*17,512)==Q(17,4)
# Simple rational majorants sufficient for the kernel moment constant 17.
# sqrt(pi) < 9/5 and e < 11/4 imply 5*e*sqrt(pi)/2 +4 <17.
assert Q(5)*Q(11,4)*Q(9,5)/2+4 <17
# beta>0 implies d <3/500, and hence q <3/1897.
assert Q(3,10)*Q(1,50)==Q(3,500)
assert Q(3,500)/(Q(19,5)-Q(3,500))==Q(3,1897)
assert Q(3,1897)<1
result = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
          "scope": "exact scalar algebra and example boxes, no candidate verification",
          "boxes": boxes, "bookkeeping_checks_passed": True}
output = Path(__file__).with_name("scalar_certificate.json")
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
