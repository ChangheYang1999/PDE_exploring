# Lead (2026-10-18): domain study for the forward evolution. Extend a log-polar state to a larger outer radius
# r_max = e^lrmax (same radial spacing; g = A(th) on the new outer cells) and relax to dg/ds < tol at the same datum.
# Usage: python3 mkdom.py in.npz out.npz p a1,..,aK lrmax
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
d = np.load(sys.argv[1]); p = float(sys.argv[3])
a = np.array([float(v) for v in sys.argv[4].split(',')]); K = len(a); lrmax = float(sys.argv[5])
g, lr, th = d['g'], d['lr'], d['th']
drho = lr[1] - lr[0]
nadd = int(round((lrmax - lr[-1]) / drho))
lr2 = np.concatenate([lr, lr[-1] + drho * np.arange(1, nadd + 1)])
Af = FE.datum_fn(a, K)
g2 = np.vstack([g, np.repeat(Af(th)[None, :], nadd, axis=0)])
g2, info = FE.evolve(p, Af, g2, lr2, th, 400)
steps = info['steps']
while info['dgds'] > 1e-8 and steps < 6000:
    g2, info = FE.evolve(p, Af, g2, lr2, th, 100, tol=1e-8); steps += info['steps']
ng = FE.node_and_G(p, Af, g2, lr2, th)
print(json.dumps(dict(steps=steps, dgds=info['dgds'], m1=ng['m1'], m2=ng['m2'], lrmax=float(lr2[-1]), Nr=len(lr2))))
np.savez(sys.argv[2], g=g2, lr=lr2, th=th, args=json.dumps(dict(p=p, a=a.tolist(), src=sys.argv[1], lrmax=float(lr2[-1]))))
