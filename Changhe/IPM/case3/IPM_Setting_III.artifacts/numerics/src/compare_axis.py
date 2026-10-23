"""compare_axis.py -- physical comparison of saved Q states on the y-axis (rho(0,y), q = rho/(a0 y)) and x-axis (rho_y(x,0)/a0) at fixed radii.
usage: python3 src/compare_axis.py state1.pt state2.pt ..."""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
files = [a for a in sys.argv[1:] if '=' not in a]
rr = np.array([1e-3, 1e-2, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0, 1e4, 1e6])
S = [qdiag.State(f) for f in files]
names = [f.split('/')[-1].replace('.pt', '') for f in files]
print('states: ' + ', '.join(f"{n} (N={s.N}, L={s.L}, a0={s.a0:.5f}, K={s.K:.4f})" for n, s in zip(names, S)))
qy = [s.ev(rr, np.full_like(rr, math.pi / 2)) for s in S]; qx = [s.ev(rr, np.zeros_like(rr)) for s in S]
print('rho(0, y) on the y-axis:'); print(f"{'y':>8s} " + " ".join(f"{n:>16s}" for n in names))
for i, r in enumerate(rr): print(f"{r:8.0e} " + " ".join(f"{o['rho'][i]:16.8e}" for o in qy))
print('q = rho/(a0 y) on the y-axis:')
for i, r in enumerate(rr): print(f"{r:8.0e} " + " ".join(f"{(o['w']*o['b']/s.a0)[i]:16.8e}" for o, s in zip(qy, S)))
print('rho_y(x,0)/a0 on the x-axis:')
for i, r in enumerate(rr): print(f"{r:8.0e} " + " ".join(f"{(o['w']*o['b']/s.a0)[i]:16.8e}" for o, s in zip(qx, S)))
print('U1(x,0)/x (strain on the x-axis; -> -c = c_l - 1 at 0):')
for i, r in enumerate(rr): print(f"{r:8.0e} " + " ".join(f"{(o['U1']/o['x'])[i]:16.8e}" for o in qx))
print('U2(0,y)/y (strain on the y-axis; -> c = 1 - c_l at 0):')
for i, r in enumerate(rr): print(f"{r:8.0e} " + " ".join(f"{(o['U2']/o['y'])[i]:16.8e}" for o in qy))
