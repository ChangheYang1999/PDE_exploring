"""Radial-degree range of the A2 six-branch family exclusion for the new thresholds (c1-t1, theory_v01).

Re-evaluates the A2 P33 Route U lower bound (A2 scripts/check_p33_p35_constants.py, function six(K); copied logic,
same formulas) for the six-branch generator family with radial degree K:
    H_lb(K) = D_K sqrt((pi/2) sum_m e_m^2/(m^2 + Q_n)),   ||F||_H >= H_lb(K) for every coefficient choice,
and finds the largest K with H_lb(K) above each Hdot^-1 requirement:
  FW-A2-Db       N_s >= (1-34*2^-18) 512 sqrt(20/21) H  vs 1/1572864       (A2: K = 3675)
  FW-T-TB-rebal  N_s >= (1-34*2^-16) 512 sqrt(20/21) H  vs 3/327680
  graded boxes   gamma_H >= H (G-c) vs phi_H (c1-t1 box 27.8*1.272594e-9; T4 box 205/6442450944)
Input: data/nb_stableA2_exact.annular.json (copy of A2 certificates/P25_admissible_tail_gap/, leading sine
coefficients of the fixed sector). Float search, then mpmath iv (400 bits) at K_max and K_max + 1.
Usage: python3 -B six_branch_K.py > six_branch_K.out
"""
import json
import sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as Q
from pathlib import Path
from mpmath import iv, mp

iv.prec = 400
mp.prec = 200
HERE = Path(__file__).resolve().parent
c = Q(4076476460239181, 2251799813685248); g = 1 / c; d = 1 - g
e6 = {int(m): Q(v) for m, v in json.loads((HERE / "data" / "nb_stableA2_exact.annular.json").read_text())['leading_sine_coefficients'].items()}


def H_lb(K, lib):
    I = (lambda q: iv.mpf(q.numerator) / q.denominator) if lib is iv else (lambda q: mp.mpf(q.numerator) / q.denominator)
    astar = 7 * d / 2 - 2
    exps = [l * d / 2 + k - 2 for l in range(1, 13) for k in range(2 * K + 5) if l * d / 2 + k - 2 >= astar]
    n = len(exps)
    logD = -lib.log(I(2 * astar + 1)) / 2
    for a in exps:
        if a != astar:
            logD += lib.log(I(abs(a - astar))) - lib.log(I(a + astar + 1))
    cn = n - lib.mpf(1) / 2 + lib.log(lib.mpf(2 * n - 1)) / 8
    Qn = 4 * cn ** 2 + lib.mpf(4) / 3
    return lib.exp(logD) * lib.sqrt(lib.pi / 2 * sum((I(e * e) / (m * m + Qn) for m, e in e6.items()), lib.mpf(0)))


def req(lib):
    w = lambda s: (1 - lib.mpf(34) * s) * 512 * lib.sqrt(lib.mpf(20) / 21)
    return {"FW-A2-Db": (lib.mpf(1) / 1572864) / w(lib.mpf(2) ** -18),
            "FW-T-TB-rebal-v1": (lib.mpf(3) / 327680) / w(lib.mpf(2) ** -16),
            "FW-T-TB-graded-v1 c1-t1 box": lib.mpf(278) / 10 * lib.mpf("1.272594e-9"),
            "FW-T-TB-graded-v1 T4 box": lib.mpf(205) / 6442450944,
            "FW-T-TB-sharp-v1 (c1-t2 T2-R2, CLAIMED)": (lib.mpf(5289) / 50000000) / w(lib.mpf(2) ** -13)}


for K in (75, 3675, 3676):
    h = H_lb(K, iv)
    print(f"check K={K}: H_lb = {mp.nstr(mp.mpf(h.a), 10)}; ratio to D(b) requirement = {mp.nstr(mp.mpf((h / req(iv)['FW-A2-Db']).a), 10)}", flush=True)
rf = req(mp)
for name in rf:
    lo, hi = 1, 4000
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if H_lb(mid, mp) > rf[name]:
            lo = mid
        else:
            hi = mid
    a, b = H_lb(lo, iv), H_lb(lo + 1, iv)
    ri = req(iv)[name]
    print(f"{name}: requirement H <= {mp.nstr(mp.mpf(ri.a), 8)}; excluded for K <= {lo} "
          f"(iv: H_lb({lo}) > req: {bool(a.a > ri.b)}; H_lb({lo + 1}) < req: {bool(b.b < ri.a)})", flush=True)
