"""r1_read (theory_agent_1, 2026-11-03 shift 6): the (R1) reading of theory_v15 V15-4 (b) 3 (HEURISTIC planning model).
Usage: python3 -B r1_read.py D4 D5 D6   (uppers of D_m(a_n) on the whole plane, as decimals)
Prints the m = 6 core-split margin of n6s_mu72.py at the plan of record (b0 0.55, mu 72) and at the registered
fallback (b0 0.515, mu 68), with D_m(a_r) from the radial identity D_m(a_r)^2 <= D_m(a_n)^2 - K_m (K_m exact from the
CONFIRMED endpoints of AT-1453, AT-1454). A margin >= 0 is necessary for the window in this model; it is not a
certificate: the price P/D, the sups and ||a_+||_1 (R4) are separate."""
import math, os, sys
from fractions import Fraction as Fr
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'n6s_core.py')).read()
ns = {'__file__': os.path.join(here, 'n6s_core.py'), '__name__': 'r1_read'}
exec(src[:src.index('M4c = 1024*c')], ns)
q, ehf_parts, SPLITS, tq_exact, A4c, c = (ns[k] for k in ('q', 'ehf_parts', 'SPLITS', 'tq_exact', 'A4c', 'c'))
M4c = 1024*c; NU = 1/40
LB = {4: Fr(7716296798651, 50000000), 5: Fr(701148547241569, 50000000), 6: Fr(93161147644159911, 50000000)}
UB = {4: Fr(9958486957, 12500000000), 5: Fr(20680828134801, 1000000000000), 6: Fr(65383366747743, 62500000000)}
K = {m: LB[m] - UB[m] for m in (4, 5, 6)}
def t6(v, d6): return v**(q + 1 - 6)*d6/math.sqrt(4*math.pi*(6 - q - 1))
def margin(mu, b0, dn):
    a, a4, tl, enu, r = ehf_parts(dict(SPLITS['erflog 8, rho 1'], M4=1.0), b0, mu, NU)
    B = r - enu - a
    if any(dn[m]**2 <= float(K[m]) for m in dn): return float('nan'), B
    d = {m: math.sqrt(dn[m]**2 - float(K[m])) for m in (4, 5, 6)}
    m4 = math.sqrt((d[4]*d[6] + d[5]**2)/(2*math.pi))
    tlc = (4/3)**q*tq_exact(3*mu/4) + (8/mu)**q*tq_exact(mu/2)
    return B - A4c*(M4c + m4)/mu**4 - tlc - ((4/3)**q*t6(3*mu/4, d[6]) + (8/mu)**q*t6(mu/2, d[6])), B
dn = {4: float(sys.argv[1]), 5: float(sys.argv[2]), 6: float(sys.argv[3])}
print('D_m(a_n) uppers: D4 %s, D5 %s, D6 %s' % tuple(sys.argv[1:4]))
for b0, mu, tag in ((0.55, 72, 'plan of record'), (0.515, 68, 'fallback')):
    m0, B = margin(mu, b0, dn)
    print('b0 %.3f, mu %d (%s): B(mu) %.5f, margin %.5f -> %s' % (b0, mu, tag, B, m0,
          'passes the budget (HEURISTIC)' if m0 >= 0 else 'fails the budget'))
