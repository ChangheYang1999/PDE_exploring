# Lead (2026-10-18): inner-radius domain study for the forward evolution. Extend a log-polar state inward to
# r_min = e^lrmin (same spacing; g on the new cells from rho/r^2 frozen at the first ring: g = g_0 (r/r_0)^(2-p)) and relax
# to dg/ds < tol at the same datum (x-even Fourier datum, fpeval basis). Usage: python3 mkdomin.py in.npz out.npz p a1,..,aK lrmin
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
d = np.load(sys.argv[1]); p = float(sys.argv[3])
a = np.array([float(v) for v in sys.argv[4].split(',')]); K = len(a); lrmin = float(sys.argv[5])
g, lr, th = d['g'], d['lr'], d['th']
drho = lr[1] - lr[0]
nadd = int(round((lr[0] - lrmin) / drho))
lnew = lr[0] - drho * np.arange(nadd, 0, -1)
lr2 = np.concatenate([lnew, lr])
g2 = np.vstack([g[0][None, :] * np.exp((2 - p) * (lnew - lr[0]))[:, None], g])
Af = FE.datum_fn(a, K)
g2, info = FE.evolve(p, Af, g2, lr2, th, 400)
steps = info['steps']
while info['dgds'] > 1e-8 and steps < 6000:
    g2, info = FE.evolve(p, Af, g2, lr2, th, 100, tol=1e-8); steps += info['steps']
print(json.dumps(dict(steps=steps, dgds=info['dgds'], lrmin=float(lr2[0]), Nr=len(lr2))), flush=True)
np.savez(sys.argv[2], g=g2, lr=lr2, th=th, args=json.dumps(dict(p=p, a=a.tolist(), src=sys.argv[1], lrmin=float(lr2[0]))))
