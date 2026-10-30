"""Directed (downward) decimals for the T2-W4 lower bounds (fix after c1-t4 T4-173).

weighted_weak_sharp.py printed m.lower().str(12, radius=False), which rounds to nearest, so a printed decimal can
exceed the certified lower endpoint.  This script recomputes, at 512 bits, the radius
    m = 2|I| / (D + sqrt(D^2 + 4 C_U H |I|)),   D = M + C_U C,
from the balls stored in data/weighted_weak_sharp_results.json (each printed ball contains the computed ball, so the
recomputed ball contains the true value), and writes the lower endpoint floored to 8 and to 12 significant digits
with exact rational arithmetic.  m is increasing in |I| and decreasing in M, C, H, so the arb lower endpoint is a valid
lower bound.  Output: data/wws_directed_floor.json and a table on stdout.
Run from artifacts/:  python3 -B arith/wws_directed_floor.py
"""
import json, hashlib
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx

ctx.prec = 512
root = Path(__file__).resolve().parents[1]
src = root / "data/weighted_weak_sharp_results.json"
data = json.loads(src.read_text())
CU = {"1": arb(2), "6/5": arb(808233) / 500000}


def exact_lower(x):
    """Exact rational value of the lower endpoint of the arb ball x."""
    lo = x.lower()
    man, exp = lo.mid().man_exp()
    return Fraction(int(man)) * (Fraction(2) ** int(exp))


def floor_sig(q, digits):
    """Largest decimal with `digits` significant digits that is <= q (q > 0); returned as a string."""
    assert q > 0
    e = 0
    while q >= Fraction(10) ** (e + 1):
        e += 1
    while q < Fraction(10) ** e:
        e -= 1
    scale = Fraction(10) ** (digits - 1 - e)
    n = (q * scale).numerator // (q * scale).denominator
    val = Fraction(n) / scale
    assert val <= q
    s = f"{n}"
    p = e - (digits - 1)        # val = n * 10^p
    if p >= 0:
        return s + "0" * p
    k = -p
    if len(s) <= k:
        s = "0" * (k - len(s) + 1) + s
    return s[:-k] + "." + s[-k:]


rows = []
for kind in ("single", "span"):
    for x in data[kind]:
        I = abs(arb(x["pairing"]))
        M, C, H = arb(x["M"]), arb(x["C"]), arb(x["H_upper"])
        cu = CU[x["a"]]
        D = M + cu * C
        r = 2 * I / (D + (D * D + 4 * cu * H * I).sqrt())
        q = exact_lower(r)
        old = Fraction(x["m_lower"])
        rows.append(dict(kind=kind, candidate=x["candidate"], a=x["a"], k=x.get("k"),
                         ball=r.str(30), floor8=floor_sig(q, 8), floor12=floor_sig(q, 12),
                         old_decimal=x["m_lower"], old_exceeds_lower=bool(old > q)))
        print(f"{kind:6s} {x['candidate']:10s} a={x['a']:4s} k={str(x.get('k')):6s} m in {r.str(15)}"
              f"  floor8 {rows[-1]['floor8']:>14s}  old {x['m_lower']:>18s}  old>lower: {old > q}")

n_bad = sum(r_["old_exceeds_lower"] for r_ in rows)
print(f"{n_bad} of {len(rows)} stored decimals exceed the certified lower endpoint (T4-173 found 20 of 34)")
out = dict(source=str(src.relative_to(root)), source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(), rows=rows)
(root / "data/wws_directed_floor.json").write_text(json.dumps(out, indent=1))
