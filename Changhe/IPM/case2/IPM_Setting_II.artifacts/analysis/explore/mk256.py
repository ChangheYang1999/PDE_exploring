# Lead (2026-10-18): refine a log-polar state to 2x angles (FFT interpolation in theta) and relax to dg/ds < tol.
# Usage: python3 mk256.py in.npz out.npz p [a1,..,aN | 0] [N]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
d = np.load(sys.argv[1]); p = float(sys.argv[3])
N = int(sys.argv[5]) if len(sys.argv) > 5 else 6
a = np.array([float(v) for v in sys.argv[4].split(',')]) if sys.argv[4] != '0' else np.zeros(N)
g, lr = d['g'], d['lr']; Nth = g.shape[1]
G = np.fft.rfft(g, axis=1); G2 = np.zeros((g.shape[0], Nth + 1), complex); G2[:, :G.shape[1]] = G * 2
G2[:, Nth // 2] *= 0.5
g2 = np.fft.irfft(G2, 2 * Nth, axis=1)
th2 = 2 * np.pi * np.arange(2 * Nth) / (2 * Nth)
Af = FE.datum_fn(a, N)
g2, info = FE.evolve(p, Af, g2, lr, th2, 400)
steps = info['steps']
while info['dgds'] > 1e-8 and steps < 4000:
    g2, info = FE.evolve(p, Af, g2, lr, th2, 100, tol=1e-8); steps += info['steps']
ng = FE.node_and_G(p, Af, g2, lr, th2)
print(json.dumps(dict(steps=steps, dgds=info['dgds'], m1=ng['m1'])))
np.savez(sys.argv[2], g=g2, lr=lr, th=th2, args=json.dumps(dict(p=p, a=a.tolist(), src=sys.argv[1])))
