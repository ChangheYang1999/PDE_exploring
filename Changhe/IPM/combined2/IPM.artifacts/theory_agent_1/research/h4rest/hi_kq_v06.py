# Least HI' cuts of NR-34 at the rate R = beta_* - b0 - e_up read from a near check result file (eps_rest = 0 inside
# R), for the three T_IS coefficients K = c_tr' + 5q/2, K_q = c_tr' + q and K_half = c_tr' + q/2, at the certified
# origin lower L2 = 2 * 1899576001577/10^12 (AT2564) and at the strain-axis point lower u = 5123210549166463/10^15
# (AT2752, AT2753; conditional on the Fourier hypotheses), with the directed necessary u_3 uppers R mu^2/(phi K_half)
# at the tested cuts and the exclusions at u for each coefficient. Same arithmetic as hi_kq_v04.py (exact rationals
# for R and the lowers, arb at 256 bits, directed 12-place displays). On near_check_v07.result.json it must
# reproduce the cuts of NR-34 (d) and AT2774, AT2775 (the asserts below check this when that file is the input).
# hi_kq_v06 (theory_agent_1, NEAR_CHECK_v09): as hi_kq_v05, and in addition it prints, for each coefficient, the least integer
# cut at u (the least integer above the enclosure, which must not contain an integer) and adds these integers to the
# tested cuts; on near_check_v08.result.json it must reproduce research/h4rest/hi_kq_v05.out (asserts below).
# Usage (from the lane root): python3 -B research/h4rest/hi_kq_v06.py <near check result json>
import json, sys, hashlib, os
from fractions import Fraction as Fr
import flint
flint.ctx.prec = 256
arb = flint.arb
c = Fr(4076476460239181, 2251799813685248)
q = Fr(21, 10)
L2 = Fr(3799152003154, 10**12)
U = Fr(5123210549166463, 10**15)
REG = Fr(704955805507, 10**12)
TEST = {"11/20": [208, 224, 241], "103/200": [72, 76, 82, 88]}
def A(x): return arb(x.numerator) / x.denominator
def exact(x):
    m, e = x.man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))
def dec(x, d=12):
    lo = exact(x.mid()) - exact(x.rad()); hi = exact(x.mid()) + exact(x.rad())
    fl = (lo * 10**d).__floor__(); ce = -((-hi * 10**d).__floor__())
    f = lambda n: ("%d.%0" + str(d) + "d") % divmod(n, 10**d)
    return f(fl), f(ce)
def rat(s):  # the result files write exact decimals; Fraction parses them exactly
    return Fr(s)
path = sys.argv[1]
raw = open(path, "rb").read()
res = json.loads(raw)
assert rat(res["beta_star_lower"]) == REG and rat(res["eps_rest_upper"]) == 0
l2 = arb(2).log()
ctr = 4 * ((A(q) * l2).sinh() - A(q) * l2.sinh()) / l2**3
phi = (1 + arb(5).sqrt()) / 2
KS = [("K = c_tr' + 5q/2", ctr + A(5 * q / 2)), ("K_q = c_tr' + q", ctr + A(q)), ("K_half = c_tr' + q/2", ctr + A(q / 2))]
print("input %s (SHA256 %s)" % (os.path.basename(path), hashlib.sha256(raw).hexdigest()))
print("program %s (SHA256 %s)" % (os.path.basename(__file__), hashlib.sha256(open(__file__, "rb").read()).hexdigest()))
print("beta_* =", REG, " L2 =", L2, " u =", U, " eps_rest = 0 inside R")
OUT = {}
for case in res["cases"]:
    b0, e = rat(case["b0"]), rat(case["e_up"])
    R = REG - b0 - e
    assert R > 0 and R == rat(case["h4_rate_margin_lower"])  # the near check rounds its margin down; equality is checked
    print("%s (b0 = %s, mu = %s): e_up = %s, R = beta_* - b0 - e_up = %s = %.12e" % (case["label"], case["b0"], case["mu"], case["e_up"], R, float(R)))
    for kn, K in KS:
        for ln, low in (("L2", L2), ("u", U)):
            lo, hi = dec((phi * K * A(low) / A(R)).sqrt())
            OUT[(case["b0"], kn[:kn.index(" ")], ln)] = (lo, hi)
            print("    %-22s at %-2s least cut in [%s, %s]" % (kn, ln, lo, hi))
    least = {}
    for kn, K in KS:
        lo, hi = OUT[(case["b0"], kn[:kn.index(" ")], "u")]
        n = int(Fr(hi).__ceil__()); assert Fr(lo) > n - 1 and Fr(hi) < n  # no integer in the enclosure
        least[kn[:kn.index(" ")]] = n
    print("    least integer cut at u: " + ", ".join("%s %d" % kv for kv in least.items()))
    for m in sorted(set(TEST[case["b0"]]) | set(least.values())):
        cells = []
        for kn, K in KS:
            ceil = A(R) * m * m / (phi * K)
            assert bool(ceil < A(U)) or bool(ceil > A(U))
            cells.append("%s %s" % (kn[:kn.index(" ")], "excluded" if bool(ceil < A(U)) else "open"))
            if kn.startswith("K_half"):
                nu = dec(ceil, 6)
        print("    mu_r %3d: K_half necessary u_3 upper in [%s, %s]; at u: %s" % (m, nu[0], nu[1], ", ".join(cells)))
if os.path.basename(path) == "near_check_v08.result.json":  # reproduction of hi_kq_v05.out
    assert OUT[("11/20", "K", "u")] == ("309.243782858499", "309.243782858500")
    assert OUT[("11/20", "K_half", "L2")] == ("207.419342729543", "207.419342729544")
    assert OUT[("11/20", "K_half", "u")] == ("240.866843317484", "240.866843317485")
    assert OUT[("103/200", "K", "u")] == ("104.594457368805", "104.594457368806")
    assert OUT[("103/200", "K_half", "u")] == ("81.467561100353", "81.467561100354")
    print("reproduction of hi_kq_v05.out at NEAR_CHECK_v08: OK")
if os.path.basename(path) == "near_check_v07.result.json":  # reproduction of NR-34 (d), AT2754, AT2774, AT2775
    assert OUT[("11/20", "K_half", "L2")] == ("207.422143510389", "207.422143510390")
    assert OUT[("103/200", "K_half", "L2")] == ("70.154855285062", "70.154855285063")
    assert OUT[("11/20", "K", "u")] == ("309.247958573514", "309.247958573515")
    assert OUT[("11/20", "K_q", "u")] == ("259.658193085923", "259.658193085924")
    assert OUT[("11/20", "K_half", "u")] == ("240.870095739522", "240.870095739523")
    assert OUT[("103/200", "K", "u")] == ("104.594646520173", "104.594646520174")
    assert OUT[("103/200", "K_q", "u")] == ("87.822267436028", "87.822267436029")
    assert OUT[("103/200", "K_half", "u")] == ("81.467708428434", "81.467708428435")
    print("reproduction of NR-34 (d) and AT2774, AT2775 at NEAR_CHECK_v07: OK")
