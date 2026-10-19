# Lead exploration: where does the Nr = 1321 forward state fail to settle? One step, locate max |g_new - g|.
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); p = float(sys.argv[2]); ds = float(sys.argv[3]) if len(sys.argv) > 3 else 0.02
g = st['g']; lr = st['lr']; th = st['th']
Af = lambda t: np.cos(t) ** 2
for k in range(3):
    g1, info = FE.evolve(p, Af, g, lr, th, 1, ds=ds)
    d = np.abs(g1 - g) / ds
    i, j = np.unravel_index(np.argmax(d), d.shape)
    rows = np.argsort(d.max(1))[::-1][:5]
    print(json.dumps(dict(step=k, dgds=float(d.max()), at_lr=float(lr[i]), at_deg=float(np.degrees(th[j])), g_there=float(g[i, j]),
                          worst_rows_lr=[round(float(lr[q]), 3) for q in rows], rowmax=[float(d[q].max()) for q in rows])))
    g = g1
