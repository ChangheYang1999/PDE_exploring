# Lead exploration (2026-10-18): time-step dependence of the forward stationary state (a referee audit found m1 at
# p = 0.1 moves 0.372 -> 0.528 -> 0.591 for ds = 0.02, 0.01, 0.005). Usage: python3 dscheck.py state.npz p kind par ds1,ds2,.. s_run
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
st = np.load(sys.argv[1]); p = float(sys.argv[2]); kind = sys.argv[3]; par = float(sys.argv[4])
dss = [float(v) for v in sys.argv[5].split(',')]; srun = float(sys.argv[6])
if kind == 'cos2':
    Af = lambda t: np.cos(t) ** 2
elif kind == 'sin3':
    Af = lambda t: np.cos(t) ** 2 * np.exp(-par * np.sin(3 * t))
lr, th = st['lr'], st['th']; r = np.exp(lr); l = 1 / p
g = st['g']
for ds in dss:
    t0 = time.time()
    n = int(round(srun / ds))
    hist = []
    for blk in range(4):
        g, info = FE.evolve(p, Af, g, lr, th, n // 4, ds=ds)
        wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p)
        M = PF.node_matrix(l + wr[20] / r[20], wt[20] / r[20], th)
        hist.append(round(float(np.linalg.eigvalsh(0.5 * (M + M.T))[0]), 6))
    print(json.dumps(dict(p=p, kind=kind, par=par, ds=ds, steps=n, m1_hist=hist, dgds=info['dgds'], wall=round(time.time() - t0))), flush=True)
    np.savez('../runs/dscheck_%s_p%g_ds%g.npz' % (kind, p, ds), g=g, lr=lr, th=th)
