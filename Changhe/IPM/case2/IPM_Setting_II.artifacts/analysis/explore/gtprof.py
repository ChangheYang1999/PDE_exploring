# Lead (2026-10-18): stationary state for datum z = (a_1..a_N, p) from a restart state, then the full
# log Gt(theta_exit) profile (log Gt = log A - 2 m1 logAn, mean over |cos| > 0.05 removed) and m1; saves an npz.
# Usage: python3 gtprof.py restart.npz a1,..,aN p out.npz [nA=2048]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); a = np.array([float(v) for v in sys.argv[2].split(',')]); p = float(sys.argv[3])
nA = int(sys.argv[5]) if len(sys.argv) > 5 else 2048
N = len(a); Af = FE.datum_fn(a, N); lr, th = st['lr'], st['th']
g, info = FE.evolve(p, Af, st['g'], lr, th, 300); steps = info['steps']
while info['dgds'] > 1e-8 and steps < 4000:
    g, info = FE.evolve(p, Af, g, lr, th, 100, tol=1e-8); steps += info['steps']
ng = FE.node_and_G(p, Af, g, lr, th, nA=nA)
thA = ng['thA']; lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
w = np.abs(np.cos(thA)) > 0.05
lgt = lgt - lgt[w].mean()
deg = np.degrees(thA)
pick = {}
for d0 in (0, 30, 60, 80, 85, 88, 89, 91, 92, 95, 100, 120, 150, 180, 210, 240, 260, 265, 268, 271, 272, 275, 280, 300, 330):
    i = int(np.argmin(np.abs(deg - d0))); pick[str(d0)] = round(float(lgt[i]), 4)
imin = int(np.argmin(np.where(w, lgt, np.inf))); imax = int(np.argmax(np.where(w, lgt, -np.inf)))
print(json.dumps(dict(m1=ng['m1'], m2=ng['m2'], steps=steps, dgds=info['dgds'], range=float(lgt[w].max() - lgt[w].min()),
                      min_deg=float(deg[imin]), max_deg=float(deg[imax]), std=float(lgt[w].std()), logGt=pick)))
np.savez(sys.argv[4], thA=thA, logGt=lgt, g=g, lr=lr, th=th, a=a, p=p, m1=ng['m1'])
