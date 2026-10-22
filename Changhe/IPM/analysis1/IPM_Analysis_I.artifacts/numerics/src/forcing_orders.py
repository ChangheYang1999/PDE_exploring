"""Rigorous forcing bounds at other fractional orders s in (3, 4) from the PINNED integrals I3, I4 of the forcing certificate (NUM_REPORT 7.10):
by Hoelder, (lam^2 + |xi|^2)^s = [(.)^3]^{4-s} [(.)^4]^{s-3}, so N_lam,s(f)^2 <= I3^{4-s} I4^{s-3}, N <= I3^{(4-s)/2} I4^{(s-3)/2}.
Evaluated in Arb with exact rational exponents and converted outward (ceilings).  Reads the merged JSONs (no change to the pinned files).
Usage: python3 src/forcing_orders.py runs/forcing/v22_p9_merged.json [more.json ...]  -> prints and writes runs/forcing/orders.json
"""
import sys, json
import numpy as np
from fractions import Fraction
from flint import arb, ctx
ctx.prec = 128
ORDERS = [Fraction(61, 20), Fraction(153, 50), Fraction(31, 10), Fraction(7, 2)]      # 3.05, 3.06, 3.1, 3.5
def f_up(x): return float(np.nextafter(float(x), np.inf))
out = {}
for path in sys.argv[1:]:
    d = json.load(open(path)); tag = path.split("/")[-1].replace(".json", "")
    out[tag] = {}
    for lam, r in d["results"].items():
        I3, I4 = arb(r["I3"]), arb(r["I4"]); row = {}
        for s in ORDERS:
            e3 = arb((4 - s).numerator) / (4 - s).denominator / 2; e4 = arb((s - 3).numerator) / (s - 3).denominator / 2
            b = f_up(((I3 ** e3) * (I4 ** e4)).upper()); row[str(s)] = b
        out[tag][lam] = row
        print("%s lam=%s: " % (tag, lam) + ", ".join("s=%s: %.6g" % (s, row[str(s)]) for s in ORDERS))
json.dump(dict(note="N <= I3^((4-s)/2) I4^((s-3)/2) from the pinned I3, I4; Arb with exact exponents, outward float conversion", orders=[str(s) for s in ORDERS], bounds=out), open("runs/forcing/orders.json", "w"), indent=1)
