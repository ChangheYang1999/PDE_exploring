"""C(theta)/(1+k) = (c_l-1)(Th1e-Th1f)/(1+k), the predicted limit of r^(1-k) R/N_v, on stored coefficients."""
import sys, json, numpy as np
sys.path.insert(0, '.')
from far1 import run
from far1_axis import axis
p = sys.argv[1]; N = 1 << 15
o, (th, T0, T1f, T1e) = run(p, N=N, verbose=False)
k = 1/o['c_l']; cl = o['c_l']
out = {}
for t0 in [0.1, 0.3, 0.6, 0.818, 1.0, 1.2, 1.4, 1.5, 1.55, 1.565]:
    i = np.argmin(np.abs(th-t0))
    out['%.4f' % th[i]] = (cl-1)*(T1e[i]-T1f[i])/(1+k)
Vr, e, f = axis(p, N)
out['pi/2'] = (cl-1)*(e-f)/(1+k)
for kk, v in out.items(): print('theta', kk, 'C/(1+k) %+.5e' % v)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
