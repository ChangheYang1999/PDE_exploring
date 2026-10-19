# Lead: evaluate the fpnloc map at a list of points (each from the same restart state).
# Usage: python3 evalx.py restart.npz K ws pointsfile [nmin=300 nmax=4000 tol=1e-8 cut=0.02 nA=2048 report=50 ds=0.02]
# pointsfile: one point per line, "x1,..,xnb p [restart_override.npz] [save.npz]" ; prints m1, steps, logGt rms/range and m1 every `report` steps of the relaxation.
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
st = np.load(sys.argv[1]); K = int(sys.argv[2]); ws = [float(v) for v in sys.argv[3].split(',')] if sys.argv[3] != '0' else []
pts = [l.split() for l in open(sys.argv[4]) if l.strip()]
opt = dict(nmin=300, nmax=4000, tol=1e-8, cut=0.02, nA=2048, report=100, ds=0.02)
for s in sys.argv[5:]:
    k, v = s.split('='); opt[k] = int(v) if k in ('nmin', 'nmax', 'nA', 'report') else float(v)
nb = K + 2 * len(ws); lr, th = st['lr'], st['th']; r = np.exp(lr)
def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws: out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)
for pt in pts:
    xs, ps = pt[0], pt[1]
    x = np.array([float(v) for v in xs.split(',')]); x = np.concatenate([x, np.zeros(max(0, nb - len(x)))])[:nb]; p = float(ps); l = 1 / p
    Af = lambda t, x=x: np.cos(t) ** 2 * np.exp(x @ basis(np.atleast_1d(t).ravel())).reshape(np.shape(t))
    t0 = time.time(); g = np.load(pt[2])['g'] if len(pt) > 2 and pt[2] != '-' else st['g']; steps = 0; hist = []
    while True:
        g, info = FE.evolve(p, Af, g, lr, th, opt['report'], ds=opt['ds']); steps += opt['report']
        rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
        M = PF.node_matrix(l + wr[20] / r[20], wt[20] / r[20], th); hist.append((steps, round(float(np.linalg.eigvalsh(0.5 * (M + M.T))[0]), 5), float('%.2g' % info['dgds'])))
        if (steps >= opt['nmin'] and info['dgds'] < opt['tol']) or steps >= opt['nmax']: break
    ng = FE.node_and_G(p, Af, g, lr, th, nA=opt['nA'])
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    w = (np.abs(np.cos(ng['thA'])) > opt['cut']) & np.isfinite(lgt); res = lgt[w] - lgt[w].mean()
    print(json.dumps(dict(x=x.round(5).tolist(), p=p, m1=ng['m1'], steps=steps, hist=hist, rms=float(res.std()),
                          range=float(res.max() - res.min()), start=pt[2] if len(pt) > 2 else '-', wall=round(time.time() - t0))), flush=True)
    if len(pt) > 3:
        np.savez(pt[3], g=g, lr=lr, th=th, x=x, p=p, m1=ng['m1'], thA=ng['thA'], logGt=lgt)
