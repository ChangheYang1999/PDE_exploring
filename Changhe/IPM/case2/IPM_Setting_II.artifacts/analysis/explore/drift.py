# Lead: drift test. Evolve a restart state at fixed datum (fpnloc basis) without tolerance stop, report m1 (ring)
# and dg/ds every `blk` steps.  Usage: python3 drift.py restart.npz p K ws x0 nblk blk
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
st = np.load(sys.argv[1]); p = float(sys.argv[2]); K = int(sys.argv[3])
ws = [float(v) for v in sys.argv[4].split(',')] if sys.argv[4] != '0' else []
x = np.array([float(v) for v in sys.argv[5].split(',')]); nblk = int(sys.argv[6]); blk = int(sys.argv[7])
nb = K + 2 * len(ws); x = np.concatenate([x, np.zeros(max(0, nb - len(x)))])[:nb]
def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws: out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)
Af = lambda t: np.cos(t) ** 2 * np.exp(x @ basis(np.atleast_1d(t).ravel())).reshape(np.shape(t))
g, lr, th = st['g'], st['lr'], st['th']; l = 1 / p; r = np.exp(lr)
t0 = time.time()
for b in range(nblk):
    g, info = FE.evolve(p, Af, g, lr, th, blk)
    rho = (r ** p)[:, None] * g
    wr, wt = PF.velocity_p(rho, lr, th, p)
    out = {}
    for kr in (10, 20, 40):
        M = PF.node_matrix(l + wr[kr] / r[kr], wt[kr] / r[kr], th); out['m1_k%d' % kr] = float(np.linalg.eigvalsh(0.5 * (M + M.T))[0])
    print(json.dumps(dict(steps=(b + 1) * blk, dgds=info['dgds'], **out, wall=round(time.time() - t0))), flush=True)
