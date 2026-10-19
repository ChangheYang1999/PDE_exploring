# Lead: quasi-Newton on the numerics' K64 residual with the residual evaluated in the lead code (B-spline transport,
# pforward2 velocity), started from a numerics Jacobian (their bnewton J file, read-only) and corrected by Broyden updates.
# Residual (same form as the numerics' pfwd_bnewton.evaluate): F = [wm (m1 - 1/2), C_1 .. C_K], C = least-squares coefficients
# of centred log Gt on [1, phi_1 .. phi_K] over |cos th| > cut; m1 = grid moment (m1mom.py formula); log Gt = log A - 2 log|u0|
# - 2 m1 (T - p lr_max) from backward orbits to lr0 (as fpeval.node_and_G, with the moment m1).
# Usage: python3 withpf2.py dcbroyden.py J.npz warm_state.npz outprefix [maxit=8 lam=0.05 dxmax=0.15 nmin=300 nmax=2500 lr0=-11 wm=3]
import sys, json, time
import numpy as np
from scipy.interpolate import RectBivariateSpline
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF

Jf, warm, pre = sys.argv[1], sys.argv[2], sys.argv[3]
opt = dict(maxit=8, lam=0.05, dxmax=0.15, nmin=300, nmax=2500, lr0=-11.0, wm=3.0, cut=0.02, nA=2048, tol=1e-8)
for s in sys.argv[4:]:
    k, v = s.split('='); opt[k] = int(v) if k in ('maxit', 'nmin', 'nmax', 'nA') else float(v)
dJ = np.load(Jf); J = dJ['J'].copy(); n = J.shape[0]; K = n - 1
st = np.load(warm); lr, th = st['lr'], st['th']; r = np.exp(lr)
log = open(pre + '.log', 'a')


def emit(d):
    s = json.dumps(d); print(s, flush=True); log.write(s + '\n'); log.flush()


def Fexp(x, t):
    return x[:K] @ FE.basis(np.atleast_1d(t).ravel(), K)


def gtrace(p, g, m1, Af):
    rho = (r ** p)[:, None] * g
    wr, wt = PF.velocity_p(rho, lr, th, p)
    ar = 1.0 / p + wr / r[:, None]; at = wt / r[:, None]
    M = PF.node_matrix(ar[20], at[20], th)
    ev, evec = np.linalg.eigh(0.5 * (M + M.T)); e1 = evec[:, 0] * np.sign(evec[0, 0])
    pad = 8; thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi])
    ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
    Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3); St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
    rhs = lambda x, t: (-Sr.ev(x, np.mod(t, 2 * np.pi)), -St.ev(x, np.mod(t, 2 * np.pi)))
    nA = opt['nA']; dt = 0.01; thA = 2 * np.pi * np.arange(nA) / nA
    x = np.full(nA, lr[-1]); t = thA.copy(); T = np.zeros(nA); live = np.ones(nA, bool); it = 0
    while live.any() and it < 200000:
        xi, ti = x[live], t[live]
        k1 = rhs(xi, ti); k2 = rhs(xi + 0.5 * dt * k1[0], ti + 0.5 * dt * k1[1])
        k3 = rhs(xi + 0.5 * dt * k2[0], ti + 0.5 * dt * k2[1]); k4 = rhs(xi + dt * k3[0], ti + dt * k3[1])
        x[live] = xi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); t[live] = ti + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        T[live] += dt; live = live & (x > opt['lr0']); it += 1
    u0 = (np.exp(x)[:, None] * np.stack([np.cos(t), np.sin(t)], 1)) @ e1
    lgt = np.log(np.maximum(Af(thA), 1e-300)) - 2 * np.log(np.maximum(np.abs(u0), 1e-300)) - 2 * m1 * (T - p * lr[-1])
    return thA, lgt, float(ev[0]), int(live.sum())


Phi = None


def evaluate(x, g0, x0, tag):
    global Phi
    p = float(x[-1]); p0 = float(x0[-1])
    Af = lambda t, x=x: np.cos(t) ** 2 * np.exp(Fexp(x, t)).reshape(np.shape(t))
    g = g0 * np.exp(Fexp(x, th) - Fexp(x0, th))[None, :] * ((r / r[-1]) ** (p0 - p))[:, None]
    t0 = time.time(); steps = 0
    while True:
        g, info = FE.evolve(p, Af, g, lr, th, 100); steps += 100
        if (steps >= opt['nmin'] and info['dgds'] < opt['tol']) or steps >= opt['nmax']:
            break
    w = np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]
    ang = w.mean(axis=1) * 2
    m1 = 1 / p - np.trapz(ang, lr) - ang[-1] / (1 - p)
    thA, lgt, m1ring, nlive = gtrace(p, g, m1, Af)
    msk = (np.abs(np.cos(thA)) > opt['cut']) & np.isfinite(lgt)
    if Phi is None:
        Phi = np.vstack([np.ones_like(thA)[None], FE.basis(thA, K)]).T[msk]
    y = lgt[msk] - lgt[msk].mean()
    C = np.linalg.lstsq(Phi, y, rcond=1e-10)[0]
    F = np.concatenate([[opt['wm'] * (m1 - 0.5)], C[1:]])
    def at(deg): return float(lgt[int(round(deg / 360 * len(thA))) % len(thA)] - lgt[msk].mean())
    d = dict(tag=tag, m1=round(float(m1), 5), m1ring=round(m1ring, 5), p=round(p, 6), normF=float(np.linalg.norm(F)),
             normF_G=float(np.linalg.norm(F[1:])), steps=steps, dgds=float('%.2g' % info['dgds']), nlive=nlive,
             bulk_std=float(np.std(y[np.abs(np.cos(thA[msk])) > 0.3])), up89=at(89), low269=at(269), up88=at(88), low268=at(268),
             rms_unres=float(np.std(y - Phi @ C)), wall=round(time.time() - t0))
    np.savez(pre + '_%s.npz' % tag, g=g, lr=lr, th=th, x=x[:K], p=p, m1=m1, thA=thA, logGt=lgt, xfull=x, F=F)
    return F, g, d


x = np.concatenate([st['x'][:K], [float(st['p'])]])
emit(dict(start=warm, J=Jf, opt=opt, x_J_minus_x=float(np.linalg.norm(dJ['x'] - x))))
F, g, d = evaluate(x, st['g'], x, 'it0'); emit(dict(it=0, **d))
for it in range(1, opt['maxit'] + 1):
    dx = -np.linalg.solve(J.T @ J + opt['lam'] ** 2 * np.eye(n), J.T @ F)
    sc = max(1.0, np.abs(dx[:-1]).max() / opt['dxmax'], abs(dx[-1]) / 0.04); dx = dx / sc
    acc = False
    for lam in (1.0, 0.5, 0.25):
        xt = x + lam * dx
        Ft, gt, dt_ = evaluate(xt, g, x, 'it%d_l%g' % (it, lam))
        s = xt - x; pred = float(np.linalg.norm(F + J @ s))
        J = J + np.outer(Ft - F - J @ s, s) / (s @ s)                       # good Broyden on every trial
        emit(dict(it=it, lam=lam, scale=round(sc, 3), dx_norm=float(np.linalg.norm(s)), pred=pred, **dt_))
        if dt_['normF'] < np.linalg.norm(F):
            x, F, g = xt, Ft, gt; acc = True; break
    emit(dict(it=it, accepted=acc, normF=float(np.linalg.norm(F)), x=[round(float(v), 6) for v in x]))
    if not acc:
        break
