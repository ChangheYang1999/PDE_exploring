# Lead (2026-10-18): two-control search for m1 = 1/2 and D_ax = 0 in the x-even forward class (lead code).
# Datum A = cos^2 exp(sum a_j phi_j) (fpeval basis sin th, cos 2th, sin 3th, cos 4th, sin 5th, cos 6th), p fixed. Controls:
# u = a_2 shift (y-even, toward the vertical when negative) and s = amplitude of an endpoint-preserving y-odd mode
# ('s13': s (sin th + sin 3th) = 4 s sin th cos^2 th; 's51': s (sin 5th - sin th)); both modes vanish at th = +-pi/2.
# Residual R = (m1 - 1/2, D_ax) with m1 from the node tracer (fpeval.node_and_G) and D_ax from the axis ODE (as dsum.py);
# the axis-law spread (max - min of log h/k^2 - law on lr >= -6, each half-axis) is reported: D_ax is meaningful only
# when it is small. FD Jacobian, then Broyden with backtracking. Warm starts from the last accepted state.
# Usage: python3 twoctl.py restart.npz p x0(6, comma) mode u0 s0 out_prefix [hu=0.05 hs=0.05 maxit=6 nmin=300 nmax=4000 tol=1e-8]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF

st = np.load(sys.argv[1]); p = float(sys.argv[2]); l = 1 / p
x0 = np.array([float(v) for v in sys.argv[3].split(',')]); mode = sys.argv[4]
z = np.array([float(sys.argv[5]), float(sys.argv[6])]); pref = sys.argv[7]
opt = dict(hu=0.05, hs=0.05, maxit=6, nmin=300, nmax=4000, tol=1e-8)
for a in sys.argv[8:]:
    k, v = a.split('='); opt[k] = int(v) if k in ('maxit', 'nmin', 'nmax') else float(v)
lr, th = st['lr'], st['th']; r = np.exp(lr); Nth = len(th)
kk = np.fft.rfftfreq(Nth, 1.0 / Nth)


def xof(z):
    x = x0.copy(); x[1] += z[0]
    if mode == 's13':
        x[0] += z[1]; x[2] += z[1]
    else:
        x[4] += z[1]; x[0] -= z[1]
    return x


def axis(g, m1):
    rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
    gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), Nth, axis=1)
    q = {}
    for name, j in (('up', Nth // 4), ('down', 3 * Nth // 4)):
        h = r ** (p - 2) * gtt[:, j]; Vr = l * r + wr[:, j]
        a = 2 * l - np.gradient(Vr, r); f = -(a - m1) / Vr
        logk = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
        law = np.concatenate([[0], np.cumsum(0.5 * ((1 - 2 * m1) / Vr[1:] + (1 - 2 * m1) / Vr[:-1]) * np.diff(r))])
        q[name] = np.log(np.abs(h)) - 2 * logk - law
    w = lr >= -6
    return float(q['down'][-1] - q['up'][-1]), float(np.ptp(q['up'][w])), float(np.ptp(q['down'][w]))


def evaluate(z, g):
    x = xof(z)
    Af = lambda t: np.cos(t) ** 2 * np.exp(x @ FE.basis(np.atleast_1d(t).ravel(), 6)).reshape(np.shape(t))
    g1, i1 = FE.evolve(p, Af, g, lr, th, opt['nmin']); steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=opt['tol']); steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=2048)
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']; deg = np.degrees(ng['thA'])
    pk = lambda d0: float(lgt[np.argmin(np.abs(deg - d0))])
    Dax, spu, spd = axis(g1, ng['m1'])
    info = dict(x=x.round(6).tolist(), m1=ng['m1'], D_ax=Dax, spread_up=spu, spread_down=spd, D_samp=pk(269) - pk(89),
                steps=steps, dgds=dg)
    return np.array([ng['m1'] - 0.5, Dax]), g1, info, (ng['thA'], lgt)


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
R, g, d, prof = evaluate(z, st['g'])
log(dict(it=0, z=z.tolist(), R=R.tolist(), **d, wall=round(time.time() - t0)))
np.savez(pref + '_it0.npz', g=g, lr=lr, th=th, x=np.array(d['x']), p=p, m1=d['m1'], thA=prof[0], logGt=prof[1])
J = np.zeros((2, 2))
for j, hh in enumerate((opt['hu'], opt['hs'])):
    zj = z.copy(); zj[j] += hh
    Rj, _, dj, _ = evaluate(zj, g)
    J[:, j] = (Rj - R) / hh
    log(dict(col=j, Jcol=J[:, j].tolist(), **dj, wall=round(time.time() - t0)))
for it in range(1, opt['maxit'] + 1):
    dz = np.linalg.solve(J, -R); lam = 1.0; acc = False
    while lam > 0.1:
        zt = z + lam * dz
        Rt, gt, dt, pt = evaluate(zt, g)
        if np.isfinite(Rt).all() and np.linalg.norm(Rt) < (1 - 0.2 * lam) * np.linalg.norm(R):
            acc = True; break
        log(dict(it=it, reject_lam=lam, z_try=zt.tolist(), R_try=Rt.tolist(), **dt, wall=round(time.time() - t0)))
        lam *= 0.5
    if not acc:
        log(dict(it=it, stop='no decrease')); break
    s = zt - z; y = Rt - R; J = J + np.outer(y - J @ s, s) / (s @ s)
    z, R, g, d, prof = zt, Rt, gt, dt, pt
    log(dict(it=it, z=z.tolist(), R=R.tolist(), lam=lam, **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, x=np.array(d['x']), p=p, m1=d['m1'], thA=prof[0], logGt=prof[1])
    if np.linalg.norm(R) < 2e-3:
        break
