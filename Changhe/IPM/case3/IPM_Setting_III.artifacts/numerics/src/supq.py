"""supq.py -- sampled sup of q = rho/(a0 y) = w b/a0 over a dense polar set (log radii 1e-4 .. 1e6 x 128 angles) for saved Q states (lead 01:24Z item 2)."""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
rr = np.exp(np.linspace(np.log(1e-4), np.log(1e6), 400)); th = (np.arange(128) + 0.5) * math.pi / 256
for f in sys.argv[1:]:
    S = qdiag.State(f); RR, TT = np.meshgrid(rr, th, indexing='ij'); o = S.ev(RR, TT); q = o['w'] * o['b'] / S.a0
    i = np.unravel_index(np.argmax(q), q.shape); j = np.unravel_index(np.argmin(q), q.shape)
    print(f"{f.split('/')[-1]}: a0={S.a0:+.5f} cl={S.cl:.6f} sup q = {q[i]:.6f} at (r={RR[i]:.3g}, th={TT[i]:.3f}); inf q = {q[j]:.3e} at (r={RR[j]:.3g}, th={TT[j]:.3f}) (sampled)")
