"""departure_radius.py -- first radius (scanning outward from 1e-4) where |s(r) - 2| exceeds a tolerance, s = dlog|1-q|/dlog r on both axes
(referee locexp1 item 4; check of the N-dependence of the smoothing radius).  Also prints N r_tol.  usage: python3 src/departure_radius.py states..."""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from local_exponent import axis_q, exponent
rr = np.exp(np.linspace(np.log(1e-5), np.log(0.5), 4001))
print(f"{'state':>26s} {'N':>4s} {'a0':>10s} | tol 0.1: r_y   N r_y   r_x   N r_x | tol 0.05: r_y   N r_y   r_x   N r_x | tol 0.01: r_y  r_x")
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); sy = exponent(rr, 1 - axis_q(S, rr, math.pi / 2)); sx = exponent(rr, 1 - axis_q(S, rr, 0.0))
    m = rr >= 1e-4; out = []
    for tol in [0.1, 0.05, 0.01]:
        ry = rr[m][np.argmax(np.abs(sy[m] - 2) > tol)]; rx = rr[m][np.argmax(np.abs(sx[m] - 2) > tol)]
        out.append((ry, rx))
    print(f"{f.split('/')[-1]:>26s} {S.N:4d} {S.a0:10.5f} | {out[0][0]:.5f} {S.N*out[0][0]:6.3f} {out[0][1]:.5f} {S.N*out[0][1]:6.3f} | {out[1][0]:.5f} {S.N*out[1][0]:6.3f} {out[1][1]:.5f} {S.N*out[1][1]:6.3f} | {out[2][0]:.5f} {out[2][1]:.5f}")
