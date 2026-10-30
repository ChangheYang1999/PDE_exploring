"""NC-T-DYADIC-LAP cell test (theory_v02 section 5.2, T4-107 with NC-T-DYADIC-FLOOR): the scheme FW-T-DYADIC-Y-v1 at
exponent a needs 5^((a-2)/2) N_a(F) < B(a) = sqrt(8 pi) (1 + c - c a)^2 / (1 + a). On a cell [l, h] the test fails at every
a in the cell if 5^((l-2)/2) N_h(F) >= B(l) (N_a nonincreasing in a, B decreasing on the window). Ratios > 1 exclude the cell.
Input: a wlap record (certification/results/<ID>_wlap.json or *_wlap_from_log.json)."""
from fractions import Fraction as Q
import json, sys
from flint import arb, ctx
ctx.prec = 256
c = arb(4076476460239181) / 2251799813685248

def B(a): return (8 * arb.pi()).sqrt() * (1 + c - c * a) ** 2 / (1 + a)

def run(path):
    rec = json.load(open(path)); vals = rec.get('values') or rec.get('WLAP')
    pts = sorted(((Q(k), arb(v['LB']), arb(v['UB'])) for k, v in vals.items() if 'LB' in v), key=lambda x: x[0])
    print(f"{rec['id']}: pointwise ratios 5^((a-2)/2) N_a / B(a) (exact N_a; > 1 excludes a):")
    for a, lo, hi in pts:
        aa = arb(a.numerator) / a.denominator; r = arb(5) ** ((aa - 2) / 2) * hi / B(aa)
        print(f"  a = {str(a):>4}: N_a = {hi.str(14)}  ratio = {r.str(10)}  {'EXCLUDED' if r.lower() > 1 else 'passes (not excluded by this test)'}")
    print("cell ratios 5^((l-2)/2) N_h / B(l) (>= 1 excludes the whole cell [l, h]):")
    out = []
    for (l, lo1, hi1), (h, lo2, hi2) in zip(pts[:-1], pts[1:]):
        la = arb(l.numerator) / l.denominator; r = arb(5) ** ((la - 2) / 2) * hi2 / B(la)
        out.append((str(l), str(h), r.str(12), bool(r.lower() >= 1)))
        print(f"  [{str(l):>4}, {str(h):>4}]: {r.str(12)}  {'EXCLUDED' if r.lower() >= 1 else 'open'}")
    return out

if __name__ == '__main__':
    run(sys.argv[1])
