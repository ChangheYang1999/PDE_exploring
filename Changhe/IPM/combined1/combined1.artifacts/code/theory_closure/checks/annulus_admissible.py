"""Admissible L^2 mass of a correction supported in an annulus (c1-t1, theory_v04 section R2 item 6).

Rigorous part (elementary): for h in H^2(R^2) supported in r <= Rout with sine modes n >= n0 only,
||grad h||^2 >= (n0/Rout)^2 ||h||^2 and ||grad h||^2 = <h, -Lap h> <= ||h|| ||Lap h||, so
||D^2 h|| = ||Lap h|| >= (n0/Rout)^2 ||h||. On the support r >= Rin, ||w D^k h|| >= inf w ||D^k h||.
The lemma needs the support and the angular spectrum of the correction h itself; a residual concentrated in
the annulus does not give them (c1-t4 T4-278).
Fixed ball (s_f = 1/5184, R_f = 1351/10^6): ||h|| <= R_f/((1 - d s_f) A), d = 48/25.
Family ceiling: the X radius is at most Xcap = max_s (mu0 - C s) sqrt(s)/cU, attained at s* = mu0/(3C) > s_f,
and X_s >= (1 - d s) E_w holds for 0 < s <= 1/1024, so the conservative uniform repair of T4-278 is
||h|| < Xcap/((1 - d/1024) A). (Draft 1 of this script divided Xcap by (1 - d s_f) A, which T4-278 REFUTES.)
Printed bounds are directed (interval arithmetic, upper bounds rounded up, lower bounds and factors rounded
down); draft 2 printed round-to-nearest values, two of them below the true upper bounds (c1-t4 TEAM_NOTE_v124).
Everything below the 'HEURISTIC' line changes the weights of NORM-T-Xw5184-v1 and keeps Xcap and the comparison
constant, which are not proved for the changed weights.
"""
from fractions import Fraction as Fr
from math import floor, ceil, log10
from mpmath import iv

iv.prec = 200
# Interval arithmetic (mpmath.iv); printed upper bounds are rounded up and lower bounds rounded down
# (directed decimal rounding, c1-t4 TEAM_NOTE_v124 item 2).
X = lambda v: iv.mpf(v)

def _dec(x, dig, up):
    if x == 0:
        return "0"
    e = floor(log10(abs(float(x)))) - dig + 1
    sc = Fr(10) ** (-e)
    m = str(ceil(x * sc) if up else floor(x * sc))
    return f"{m[0]}.{m[1:]}e{e + len(m) - 1}" if len(m) > 1 else f"{m}e{e}"

def _fr(t):
    sign, man, ex, _ = t                   # raw mpf tuple of an interval endpoint
    return (-1) ** sign * Fr(int(man)) * Fr(2) ** int(ex)

def UP(v, dig=10):
    return _dec(_fr(v._mpi_[1]), dig, True)

def DN(v, dig=10):
    return _dec(_fr(v._mpi_[0]), dig, False)

Rin, Rout, n0 = X(20), X(32), X(19)
q = (n0 / Rout) ** 2                       # ||D h|| >= sqrt(q) ||h||, ||D^2 h|| >= q ||h||
omega = lambda r: (1 + 4 * r * r) ** (X(2) / 5)    # A2 top weight
w1, w2 = X(2) ** 15, X(2) ** 20
s = X(1) / 5184
c = X(4076476460239181) / X(2) ** 51
gam = 1 / c
mu0, C, cU = X(97) / 250, X(397), X(8) / 5
Xcap = (2 * mu0 / 3) * iv.sqrt(mu0 / (3 * C)) / cU   # sharpw family ceiling in X units
Xball = X(1351) / 10 ** 6                            # sharpw fixed ball radius
d = X(48) / 25
low = 1 - d * s                                      # X_(s,w) >= (1 - (48/25) s) E_w at the fixed s
lowu = 1 - d / 1024                                  # uniform over the admissible range 0 < s <= 1/1024
d007, d013 = X(4769166867) / 10 ** 12, X(199234339) / 10 ** 11

def report(name, E):
    fam = Xcap / (lowu * E)
    print(f"{name}: E_w/||h|| >= {DN(E, 6)}; fixed ball L^2 mass <= {UP(Xball/(low*E))}, "
          f"family ceiling L^2 mass < {UP(fam)}; "
          f"factors to 013 > {DN(d013/fam, 4)}, to 007 > {DN(d007/fam, 4)}")

print(f"q = (n0/Rout)^2 = {DN(q, 6)}, omega(Rin) >= {DN(omega(Rin), 6)}, Xcap <= {UP(Xcap, 6)}, "
      f"s* = mu0/(3C) >= {DN(mu0/(3*C), 6)} (s_f = 1/5184, 1/1024)")
report("registered sharpw norm, global", iv.sqrt(w2))
report("registered sharpw norm, annulus", iv.sqrt(omega(Rin) ** 2 * q * q + w1 * q + w2))
print("HEURISTIC below (weights changed, sharpw ceiling kept)")
sig0, sig1 = 1 + gam, gam      # L^2 and gradient far-field exponent limits (theory_v01 R3)
W2 = w2 * (1 + Rout ** 2) ** (-sig0)
W1 = w1 * (1 + Rout ** 2) ** (-sig1)
report("decaying low weights from R = 1 at the limit exponents", iv.sqrt(omega(Rin) ** 2 * q * q + W1 * q + W2))
report("top level only (low components removed at r >= 20)", omega(Rin) * q)
crit = (1 + Rin ** 2) ** ((1 - gam) / 2)
report("top level only, critical weight (1+r^2)^((1-gamma)/2), zero far-field rate", crit * q)
