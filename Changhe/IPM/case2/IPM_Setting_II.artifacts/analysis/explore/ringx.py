# Lead (2026-10-18): ring-fit node eigenvalues m1(r) of a forward state on rings k = 0..kmax and their r -> 0
# extrapolation m1(r) = m0 + beta r (+ gamma r^2). The O(r) term is the strain of the density inside the ring
# (~ (14/(15 pi)) (C_+ - C_-) r for rho ~ C_+- x^2 above / below the weak axis).
# Usage: python3 ringx.py state.npz p [kmax=60]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); p = float(sys.argv[2]); l = 1 / p; kmax = int(sys.argv[3]) if len(sys.argv) > 3 else 60
g, lr, th = d['g'], d['lr'], d['th']; r = np.exp(lr); rho = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rho, lr, th, p)
ks = np.arange(0, kmax + 1, 2); m1 = []; m2 = []
for k in ks:
    M = PF.node_matrix(l + wr[k] / r[k], wt[k] / r[k], th); ev = np.linalg.eigvals(M).real; ev.sort(); m1.append(ev[0]); m2.append(ev[1])
m1 = np.array(m1); rr = r[ks]
out = dict(lr0=float(lr[0]), ring={int(k): round(float(v), 6) for k, v in zip(ks[::5], m1[::5])})
for kfit in (20, 40, 60):
    sel = ks <= kfit
    c1 = np.polyfit(rr[sel], m1[sel], 1); c2 = np.polyfit(rr[sel], m1[sel], 2) if sel.sum() > 4 else [np.nan] * 3
    out['fit_k%d' % kfit] = dict(m0_lin=round(float(c1[1]), 6), beta=round(float(c1[0]), 1), m0_quad=round(float(c2[2]), 6),
                                 rms_lin=float('%.2g' % np.sqrt(np.mean((np.polyval(c1, rr[sel]) - m1[sel]) ** 2))))
print(json.dumps(out))
