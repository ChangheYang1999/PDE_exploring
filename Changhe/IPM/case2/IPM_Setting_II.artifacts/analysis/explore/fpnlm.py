# Lead (2026-10-18): trust-region Levenberg-Marquardt / Broyden driver for the fpnloc problem (x-even datum
# A = cos^2 exp(Fourier K + zero-window bumps ws); unknowns (x, p)). Merit in the L2 (Gram) metric: r = (L^T c, wm (m1 - 1/2)),
# c = LSQ coefficients of log Gt - mean on the basis (uniform weight on |cos th| > cut), G = Xc^T Xc / N = L L^T, so |L^T c|
# is the RMS of the in-span part of log Gt - mean. Reason (work log of the lead analyst 02:2xZ): the Newton step of fpnloc is far outside the
# linear regime (G(+-inf) responds like exp(2.5 b) to a window bump b, m1 linearly in G), and the coefficient norm is not an
# honest merit (fnloc1 it 1 accepted a worse profile). Starts from an FD Jacobian of the fpnloc residual (Jfile, wm = 1 there).
# Broyden updates on every trial (accepted or not); optional fresh FD Jacobian every `refresh` accepted steps.
# Usage: python3 fpnlm.py restart.npz p0 K w1,.. out_prefix x0=.. Jfile=.. [wm=5 Delta=0.2 maxit=30 nmin=300 nmax=4000
#        tol=1e-8 cut=0.02 nA=2048 refresh=0 h=0.03 hp=0.01]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); K = int(sys.argv[3])
ws = [float(v) for v in sys.argv[4].split(',')] if sys.argv[4] != '0' else []
pref = sys.argv[5]
opt = dict(x0='', Jfile='', wm=5.0, Delta=0.2, maxit=30, nmin=300, nmax=4000, tol=1e-8, cut=0.02, nA=2048, refresh=0,
           h=0.03, hp=0.01, broyall=0)
for s in sys.argv[6:]:
    k, v = s.split('=')
    opt[k] = v if k in ('x0', 'Jfile') else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'refresh', 'broyall') else float(v))
lr, th = st['lr'], st['th']
nb = K + 2 * len(ws)


def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws: out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)


def datum(x):
    x = np.asarray(x, float)
    return lambda t: np.cos(t) ** 2 * np.exp(x @ basis(np.atleast_1d(t).ravel())).reshape(np.shape(t))


thA0 = 2 * np.pi * np.arange(opt['nA']) / opt['nA']
w0 = np.abs(np.cos(thA0)) > opt['cut']
X1 = basis(thA0).T[w0]; Xc = X1 - X1.mean(0)
Lc = np.linalg.cholesky(Xc.T @ Xc / len(Xc))
T = np.eye(nb + 1); T[:nb, :nb] = Lc.T; T[nb, nb] = opt['wm']


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
    d = dict(m1=ng['m1'], steps=steps, dgds=dg, logGt_range=float(res.max() - res.min()),
             logGt_rms=float(np.sqrt(np.mean((res - res.mean()) ** 2))),
             rms_unresolved=float(np.sqrt(np.mean((lgt[w] - X @ coef) ** 2))), pick=pk)
    R = np.concatenate([coef[1:], [ng['m1'] - 0.5]])
    return T @ R, g1, d, (thA, lgt - coef[0])


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
x = np.array([float(v) for v in opt['x0'].split(',')]) if opt['x0'] else np.zeros(nb)
x = np.concatenate([x, np.zeros(max(0, nb - len(x)))])[:nb]
R, g, d, prof = evaluate(x, p, st['g'])
log(dict(it=0, x=x.round(5).tolist(), p=p, merit=float(np.linalg.norm(R)), **d, wall=round(time.time() - t0)))


def fd_jac(x, p, g, R0):
    J = np.zeros((nb + 1, nb + 1))
    for j in range(nb + 1):
        xj = x.copy(); pj = p
        if j < nb: xj[j] += opt['h']; hh = opt['h']
        else: pj += opt['hp']; hh = opt['hp']
        Rj, _, dj, _ = evaluate(xj, pj, g)
        J[:, j] = (Rj - R0) / hh
        log(dict(col=j, m1=dj['m1'], wall=round(time.time() - t0)))
    np.savez(pref + '_Jg.npz', J=J, x=x, p=p)
    return J


if opt['Jfile']:
    Jl = np.load(opt['Jfile']); J = T @ Jl['J'] if 'Jg' not in opt['Jfile'] else Jl['J']
else:
    J = fd_jac(x, p, g, R)
D = np.maximum(np.linalg.norm(J, axis=0), 1e-8)
J0 = J.copy()
Delta = opt['Delta']; nacc = 0


def lm_step(J, R, Delta):
    dz = np.linalg.lstsq(J, -R, rcond=1e-10)[0]
    if np.linalg.norm(D * dz) <= Delta:
        return dz, 0.0
    lo, hi = 0.0, 1.0
    f = lambda mu: np.linalg.solve(J.T @ J + mu * np.diag(D ** 2), -J.T @ R)
    while np.linalg.norm(D * f(hi)) > Delta: hi *= 10
    for _ in range(60):
        mid = np.sqrt(lo * hi) if lo > 0 else hi / 10
        if np.linalg.norm(D * f(mid)) > Delta: lo = mid
        else: hi = mid
        if hi / max(lo, 1e-300) < 1.05: break
    return f(hi), hi


for it in range(1, opt['maxit'] + 1):
    z = np.concatenate([x, [p]])
    dz, mu = lm_step(J, R, Delta)
    pred = np.linalg.norm(R + J @ dz)
    zt = z + dz
    if not (0.05 < zt[-1] < 0.95):
        Delta /= 4; log(dict(it=it, p_out=float(zt[-1]))); continue
    Rt, gt, dt, proft = evaluate(zt[:nb], zt[nb], g)
    ok = np.isfinite(Rt).all()
    act = np.linalg.norm(Rt) if ok else np.inf
    rho_ = (np.linalg.norm(R) ** 2 - act ** 2) / max(np.linalg.norm(R) ** 2 - pred ** 2, 1e-30)
    # Broyden only with trials whose linear prediction was not grossly wrong (a far-out trial would corrupt J)
    if ok and (rho_ > 0 or opt['broyall']):
        J = J + np.outer((Rt - R) - J @ dz, dz) / (dz @ dz)
    acc = ok and rho_ > 0.05
    log(dict(it=it, Delta=round(Delta, 4), mu=float('%.3g' % mu), step=float(np.linalg.norm(dz)), pred=float(pred),
             merit_try=float(act), ratio=float(rho_), accepted=bool(acc), m1_try=dt['m1'],
             m1_pred=float(d['m1'] + (J0[nb] @ dz) / opt['wm']), logGt_rms_try=dt.get('logGt_rms'),
             dz=dz.round(5).tolist(), Rt=Rt.round(5).tolist() if ok else None, Rpred0=(R + J0 @ dz).round(5).tolist(),
             steps_try=dt.get('steps'), dgds_try=dt.get('dgds'), wall=round(time.time() - t0)))
    if acc:
        x, p, R, g, d, prof = zt[:nb], zt[nb], Rt, gt, dt, proft; nacc += 1
        log(dict(it=it, x=x.round(5).tolist(), p=round(float(p), 6), merit=float(np.linalg.norm(R)), **d,
                 wall=round(time.time() - t0)))
        np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, x=x, p=p, R=R, thA=prof[0], logGt=prof[1], J=J,
                 args=json.dumps(dict(p=float(p), K=K, ws=ws, x=x.tolist(), kind='fpnlm', opt=opt)))
        if opt['refresh'] and nacc % opt['refresh'] == 0:
            J = fd_jac(x, p, g, R)
    Delta = Delta * 2 if (acc and rho_ > 0.75) else (Delta / 4 if rho_ < 0.25 else Delta)
    Delta = min(max(Delta, 1e-3), 2.0)
    if np.linalg.norm(R) < 1e-4:
        break
