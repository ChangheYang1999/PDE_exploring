"""resid_core_check.py -- direct evaluation of R near the origin against the cubic Taylor prediction r01 y + r21 x^2 y + r03 y^3 (from the jets):
at radii 1e-3 .. 3e-1 and angles pi/8, pi/4, 3pi/8 print R, the prediction, and |R|/N_f.  usage: python3 src/resid_core_check.py state.pt"""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from local_exponent import jets
for f in sys.argv[1:]:
    S = qdiag.State(f); cl = S.cl; A = 2 * cl - 1; a0, b, e, c, q1, q2 = jets(S); C0 = cl + c - 1
    r01 = a0 * C0; r21 = (2 * A - C0) * b + 3 * a0 * q1; r03 = (2 + 3 * C0) * e + a0 * q2
    print(f"{f}: a0={a0:.5f} r01={r01:+.3e} r21={r21:+.4f} r03={r03:+.4f}")
    for th in [math.pi / 8, math.pi / 4, 3 * math.pi / 8]:
        rr = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]); o = S.ev(rr, np.full_like(rr, th)); x, y = o['x'], o['y']
        pred = r01 * y + r21 * x * x * y + r03 * y ** 3
        print(f"  th={th:.4f}: " + "  ".join(f"r={r:.0e}: R={R:+.2e} pred={p:+.2e} R/Nf={R/n:+.1e}" for r, R, p, n in zip(rr, o['R'], pred, o['Nf'])))
