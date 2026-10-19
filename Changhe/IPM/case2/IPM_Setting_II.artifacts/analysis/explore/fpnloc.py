# Lead exploration (2026-10-18): Newton for the forward fixed-point problem with a basis adapted to the zero
# windows. x-even datum A = cos^2 exp(F), F = sum_{j<=K} a_j phi_j (fpeval x-even Fourier modes) + sum_k b+_k exp(-(1 - sin th)/w_k)
# + sum_k b-_k exp(-(1 + sin th)/w_k) (bumps of angular width sqrt(w_k) at the zeros th = 90, 270 deg; functions of sin th, so
# x-even). Unknowns (a, b+, b-, p). Residual: LSQ coefficients of log Gt - mean on [1, basis] (uniform weight on
# |cos th| > cut) and wm (m1 - 1/2). FD Jacobian, Broyden updates, backtracking; fresh FD Jacobian after a rejected step.
# Picard on the zero windows is unstable (work log of the lead analyst 01:35Z: the windows set G(+-inf), hence rho near the node and m1),
# so all unknowns are in the Newton block.
# Usage: python3 fpnloc.py restart.npz p0 K w1,w2,.. out_prefix [x0=a..,b+..,b-..] [maxit=12 h=0.03 hp=0.01 nmin=300
#        nmax=4000 tol=1e-8 cut=0.02 nA=2048 wm=1 refresh=0 Jfile=]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); K = int(sys.argv[3])
ws = [float(v) for v in sys.argv[4].split(',')] if sys.argv[4] != '0' else []
pref = sys.argv[5]
opt = dict(x0='', maxit=12, h=0.03, hp=0.01, nmin=300, nmax=4000, tol=1e-8, cut=0.02, nA=2048, wm=1.0, refresh=0, Jfile='')
for s in sys.argv[6:]:
    k, v = s.split('=')
    opt[k] = v if k in ('x0', 'Jfile') else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'refresh') else float(v))
lr, th = st['lr'], st['th']
nb = K + 2 * len(ws)


def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws:
        out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws:
        out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)


def datum(x):
    x = np.asarray(x, float)
    return lambda t: np.cos(t) ** 2 * np.exp(x @ basis(np.atleast_1d(t).ravel())).reshape(np.shape(t))


x = np.array([float(v) for v in opt['x0'].split(',')]) if opt['x0'] else np.zeros(nb)
x = np.concatenate([x, np.zeros(max(0, nb - len(x)))])[:nb]


def evaluate(x, p, g):
    Af = datum(x)
    g1, i1 = FE.evolve(p, Af, g, lr, th, opt['nmin'])
    steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=opt['tol'])
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=opt['nA'])
    thA = ng['thA']
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    w = (np.abs(np.cos(thA)) > opt['cut']) & np.isfinite(lgt)
    X = np.vstack([np.ones_like(thA), basis(thA)]).T[w]
    coef = np.linalg.lstsq(X, lgt[w], rcond=None)[0]
    res = lgt[w] - coef[0]
    deg = np.degrees(thA)
    pk = {str(d0): round(float(lgt[np.argmin(np.abs(deg - d0))] - coef[0]), 4) for d0 in (0, 45, 80, 86, 88, 89, 250, 262, 266, 268, 269)}
    d = dict(m1=ng['m1'], steps=steps, dgds=dg, logGt_range=float(res.max() - res.min()), logGt_std=float(np.std(res)),
             rms_unresolved=float(np.sqrt(np.mean((lgt[w] - X @ coef) ** 2))), pick=pk)
    return np.concatenate([coef[1:], [opt['wm'] * (ng['m1'] - 0.5)]]), g1, d, (thA, lgt - coef[0])


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
R, g, d, prof = evaluate(x, p, st['g'])
log(dict(it=0, x=x.round(5).tolist(), p=p, normR=float(np.linalg.norm(R)), R=R.round(5).tolist(), **d, wall=round(time.time() - t0)))


def fd_jac(x, p, g, R0):
    J = np.zeros((nb + 1, nb + 1))
    for j in range(nb + 1):
        xj = x.copy(); pj = p
        if j < nb:
            xj[j] += opt['h']; hh = opt['h']
        else:
            pj += opt['hp']; hh = opt['hp']
        Rj, _, dj, _ = evaluate(xj, pj, g)
        J[:, j] = (Rj - R0) / hh
        log(dict(col=j, Jcol=J[:, j].round(4).tolist(), m1=dj['m1'], wall=round(time.time() - t0)))
    log(dict(jac='fd', sv=np.linalg.svd(J, compute_uv=False).round(5).tolist()))
    np.savez(pref + '_J.npz', J=J, x=x, p=p)
    return J


if opt['Jfile']:
    J = np.load(opt['Jfile'])['J']
else:
    J = fd_jac(x, p, g, R)
for it in range(1, opt['maxit'] + 1):
    dz = np.linalg.lstsq(J, -R, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.06:
        xt = x + lam * dz[:nb]; pt = p + lam * dz[nb]
        if not (0.05 < pt < 0.95):
            lam *= 0.5; continue
        Rt, gt, dt, proft = evaluate(xt, pt, g)
        if np.isfinite(Rt).all() and np.linalg.norm(Rt) < (1 - 0.2 * lam) * np.linalg.norm(R):
            acc = True; break
        log(dict(it=it, reject_lam=lam, normR_try=float(np.linalg.norm(Rt)), m1_try=dt['m1'], wall=round(time.time() - t0)))
        lam *= 0.5
    if acc:
        s = lam * dz; y = Rt - R
        J = J + np.outer(y - J @ s, s) / (s @ s)
        x, p, R, g, d, prof = xt, pt, Rt, gt, dt, proft
    log(dict(it=it, accepted=acc, lam=lam, x=x.round(5).tolist(), p=round(p, 6), normR=float(np.linalg.norm(R)),
             R=R.round(5).tolist(), **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, x=x, p=p, R=R, thA=prof[0], logGt=prof[1], J=J,
             args=json.dumps(dict(p=float(p), K=K, ws=ws, x=x.tolist(), kind='fpnloc', opt=opt)))
    if not acc or (opt['refresh'] and it % opt['refresh'] == 0):
        J = fd_jac(x, p, g, R)
    if np.linalg.norm(R) < 1e-5:
        break
