"""disagreement_radius.py -- for successive sizes of a chain (same L, gK): the smallest radius r_tol above which the relative difference of 1 - q (and of q)
between the two states stays below tol for all larger sampled r up to 1e3, on the y-axis and the x-axis (lead 00:08Z item 3: measures the core directly).
usage: python3 src/disagreement_radius.py s1.pt s2.pt [s3.pt ...] (consecutive pairs)"""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from local_exponent import axis_q
rr = np.exp(np.linspace(np.log(1e-4), np.log(1e3), 2801))
files = [a for a in sys.argv[1:] if '=' not in a]; S = [qdiag.State(f) for f in files]
qy = [axis_q(s, rr, math.pi / 2) for s in S]; qx = [axis_q(s, rr, 0.0) for s in S]
def r_tol(d, tol):
    bad = np.where(np.abs(d) > tol)[0]; return rr[bad[-1]] if len(bad) else rr[0]
print(f"{'pair':>14s} | 1-q_y: r_1e-2  r_1e-3  r_1e-4 | 1-q_x: r_1e-2  r_1e-3  r_1e-4 | q_y: r_1e-2  r_1e-3  r_1e-4 | q_x: r_1e-2  r_1e-3  r_1e-4")
for i in range(len(S) - 1):
    dfy = (1 - qy[i + 1]) / (1 - qy[i]) - 1; dfx = (1 - qx[i + 1]) / (1 - qx[i]) - 1; dqy = qy[i + 1] / qy[i] - 1; dqx = qx[i + 1] / qx[i] - 1
    out = f"{S[i].N:>5d}->{S[i+1].N:<7d} |"
    for d in [dfy, dfx, dqy, dqx]: out += " " + " ".join(f"{r_tol(d, t):7.3g}" for t in [1e-2, 1e-3, 1e-4]) + " |"
    print(out)
