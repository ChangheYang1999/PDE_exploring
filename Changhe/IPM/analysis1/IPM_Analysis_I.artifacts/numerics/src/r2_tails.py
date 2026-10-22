"""R2 tail contributions (rigorous, Arb balls): the squared weighted L2 norm int |eps~/m|^2 dX/(1+u^2) over the two tail regions
r >= r_T,out and r <= r_T,in, from the certified tail majorants of src/cert_tail.py and src/cert_inner_tail.py (NUM_REPORT 7.3).
Outer tail: for r >= r_T,out the certificate gives W (1+u)^delta / m <= C_out (ball upper endpoint, valid for all r >= r_T,out), and
sup_theta |eps~| <= W, so int_{r >= r_T} |eps~/m|^2 dX/(1+u^2) <= 2 pi C_out^2 int_{r_T}^inf (1+u)^{-2 delta} r dr/(1+u^2)
<= 2 pi C_out^2 L^2 int_{U_T}^inf u^{-1-2 delta} du = pi C_out^2 L^2 U_T^{-2 delta} / delta,  U_T = r_T/L (u/(1+u^2) <= 1/u, (1+u)^{-2 delta} <= u^{-2 delta}).
Inner tail: for r <= r_T,in the certificate gives W/m <= C_in, so int_{r <= r_T} |eps~/m|^2 dX/(1+u^2) <= 2 pi C_in^2 r_T^2 / 2 = pi C_in^2 r_T^2.
The tail boundaries are formed in Arb from the stored knots (e^{t0+17}, e^{tmin-5}), not from the rounded r_T of the tail files; L, r_T, delta > 0 asserted.
All *_endpoint fields are exact decimal CEILINGS of the Arb upper endpoints (version 2, after verifier topic 182); the bracketed ball strings are
nearest-rounded displays of the balls, not bounds.
Usage: python3 src/r2_tails.py [tag]   (tag '' = the X3 trial; 'v3_h0.004', 'v4_M230', 'v5_R0knot2'); writes runs/r2_tails[_tag].json
"""
import sys, os, json, re
from flint import arb, ctx
ctx.prec = 200
lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag = sys.argv[1] if len(sys.argv) > 1 else ""
suf = ("_" + tag) if tag else ""


def jload(p):
    import gzip
    p = os.path.join(lane, p)
    if not os.path.exists(p) and os.path.exists(p + ".gz"): return json.load(gzip.open(p + ".gz", "rt"))
    return json.load(open(p))


def ball_upper(s):
    """upper endpoint (arb) of a printed ball '[m +/- r]' (decimal strings read exactly into arb, radius added)."""
    m, r = re.match(r"\[\s*([-0-9.eE+]+)\s*\+/-\s*([-0-9.eE+]+)\s*\]", s).groups()
    return arb(m) + arb(r) + arb(m).rad() + arb(r).rad()   # the decimal->arb conversion radii are added explicitly


tail = jload("runs/cert_tail%s.json" % suf); itail = jload("runs/cert_inner_tail%s.json" % suf)
summ = {r["tag"]: r for r in jload("runs/variants_summary.json")}[tag]
import numpy as np
T = np.load(os.path.join(lane, "data/trial_%s.npz" % (tag if tag else "v2_h0.008")))
L = arb(float(T["L"])); k = arb(float(T["k"]))
delta = arb(1) / 2 - k                                                         # the exact exponent 1/2 - k (stored k)
knots = T["knots"]; t0 = arb(float(knots[-1])); tmin = arb(float(knots[0]))   # stored doubles, exact
rT_out = (t0 + 17).exp(); rT_in = (tmin - 5).exp()                            # the EXACT tail boundaries e^{t0+17}, e^{tmin-5} as Arb balls
assert abs(float(rT_out) - tail["r_T"]) < 1e-5 * tail["r_T"] and abs(float(rT_in) - itail["r_T"]) < 1e-9 * itail["r_T"], "tail files belong to another boundary"
assert L > 0 and rT_out > 0 and rT_in > 0 and delta > 0
assert abs(float(delta) - tail["delta"]) < 1e-15, "the tail file must use delta = 1/2 - k"
C_out = ball_upper(tail["tail_bound_weighted"]); C_in = ball_upper(itail["bound_W_over_m"])
U_T = rT_out / L
outer2 = arb.pi() * C_out ** 2 * L ** 2 * U_T ** (-2 * delta) / delta
inner2 = arb.pi() * C_in ** 2 * rT_in ** 2
fin = arb(summ["middle"]["L2"]) + arb(summ["outer"]["L2"]) + arb(summ["inner"]["L2"])   # outward-summed per-cell pieces (upper bounds)
tot2 = fin + outer2 + inner2
from fractions import Fraction
from decimal import Decimal, ROUND_CEILING, getcontext
getcontext().prec = 80; getcontext().rounding = ROUND_CEILING


def exact_ceil(b, digits):
    """decimal with `digits` significant digits >= the EXACT upper endpoint of the Arb ball b (dyadic mantissa/exponent -> Fraction -> Decimal, all
    operations rounded toward +infinity). Used for every printed endpoint (verifier topic 182 found nearest-rounded endpoint displays in version 1)."""
    m, e = b.upper().man_exp(); fr = Fraction(int(m)) * (Fraction(2) ** int(e))
    d = Decimal(fr.numerator) / Decimal(fr.denominator); q = Decimal(1).scaleb(d.adjusted() - digits + 1)
    return format(d.quantize(q, rounding=ROUND_CEILING), "e")


out = dict(tag=tag, C_out_upper=str(C_out.str(12, radius=False)), delta=str(delta.str(17, radius=False)), r_T_out=tail["r_T"], U_T=str(U_T.str(12, radius=False)),
           outer_tail_sq_upper=str(outer2.str(8)), outer_tail_sq_upper_endpoint=exact_ceil(outer2, 10),
           C_in_upper=str(C_in.str(12, radius=False)), r_T_in=itail["r_T"], inner_tail_sq_upper=str(inner2.str(8)), inner_tail_sq_upper_endpoint=exact_ceil(inner2, 10),
           finite_regions_sq=str(fin.str(12)), total_sq=str(tot2.str(12)), total_R2_upper=str(tot2.sqrt().str(12)),
           finite_R2_upper=str(fin.sqrt().str(12)), total_R2_upper_endpoint=exact_ceil(tot2.sqrt(), 12), finite_sq_upper_endpoint=exact_ceil(fin, 12), finite_R2_upper_endpoint=exact_ceil(fin.sqrt(), 12), r_T_out_exact=rT_out.str(20), r_T_in_exact=rT_in.str(20), outer_R2=str(arb(summ["outer"]["L2"]).sqrt().str(10)), middle_R2=str(arb(summ["middle"]["L2"]).sqrt().str(10)),
           inner_R2=str(arb(summ["inner"]["L2"]).sqrt().str(10)))
for kk, vv in out.items(): print("%-22s %s" % (kk, vv))
json.dump(out, open(os.path.join(lane, "runs/r2_tails%s.json" % suf), "w"), indent=1)
