# Lead exploration (2026-10-18): joint Newton for the forward fixed-point problem with p free:
#     R(a, p) = ( c(a, p), m1(a, p) - 1/2 ),   c = LSQ coefficients of log Gt - mean on the N x-even modes (fpnewx.py),
# unknowns (a_1..a_N, p). Converged evaluations (dg/ds < tol), FD Jacobian (steps h in a, hp in p), damped Newton with
# backtracking, optional Broyden updates. Start from a converged state (restart npz) and optionally a fixed-p fixed point
# a0. A zero is an x-even Setting II candidate (rho = xi^2) to be re-solved without symmetry and verified independently.
# Usage: python3 fpnewxp.py restart.npz p0 N out_prefix [maxit=6 h=0.03 hp=0.01 nmin=300 nmax=4000 tol=1e-8 a0=... cut=0.05
#        nA=1024 broyden=0 wm=1]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); pref = sys.argv[4]
opt = dict(maxit=6, h=0.03, hp=0.01, nmin=300, nmax=4000, tol=1e-8, a0='', cut=0.05, nA=1024, broyden=0, wm=1.0)
for s in sys.argv[5:]:
    k, v = s.split('=')
    opt[k] = v if k == 'a0' else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'broyden') else float(v))
lr, th = st['lr'], st['th']
a = np.array([float(v) for v in opt['a0'].split(',')]) if opt['a0'] else np.zeros(N)
if len(a) < N:
    a = np.concatenate([a, np.zeros(N - len(a))])


def evaluate(z, g):
    a, p = z[:-1], z[-1]
    Af = FE.datum_fn(a, N)
    g1, i1 = FE.evolve(p, Af, g, lr, th, opt['nmin'])
    steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=opt['tol'])
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=opt['nA'])
    thA = ng['thA']
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    w = (np.abs(np.cos(thA)) > opt['cut']) & np.isfinite(lgt)
    B = FE.basis(thA, N)
    X = np.vstack([np.ones_like(thA), B]).T[w]
    coef = np.linalg.lstsq(X, lgt[w], rcond=None)[0]
    rms_rest = float(np.sqrt(np.mean((lgt[w] - X @ coef) ** 2)))
    v = np.exp(lgt[w] - coef[0])
    R = np.concatenate([coef[1:], [opt['wm'] * (ng['m1'] - 0.5)]])
    return R, g1, dict(m1=ng['m1'], m2=ng['m2'], steps=steps, dgds=dg, Gt_ratio=float(v.max() / v.min()),
                       Gt_std=float(np.std(lgt[w])), rms_unresolved=rms_rest, e1=ng['e1'], nlive=ng.get('nlive', -1))


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
z = np.concatenate([a, [p]])
R, g, d = evaluate(z, st['g'])
log(dict(it=0, z=z.round(6).tolist(), R=R.round(6).tolist(), normR=float(np.linalg.norm(R)), **d, wall=round(time.time() - t0)))
J = None
for it in range(1, opt['maxit'] + 1):
    if J is None or opt['broyden'] == 0 or it % (opt['broyden'] + 1) == 1:
        J = np.zeros((N + 1, N + 1))
        for j in range(N + 1):
            h = opt['hp'] if j == N else opt['h']
            zj = z.copy(); zj[j] += h
            Rj, _, dj = evaluate(zj, g)
            J[:, j] = (Rj - R) / h
            log(dict(col=j, Jcol=J[:, j].round(4).tolist(), steps=dj['steps'], dgds=dj['dgds'], wall=round(time.time() - t0)))
        sv = np.linalg.svd(J, compute_uv=False)
        log(dict(it=it, jac='fd', sv=sv.round(5).tolist()))
        np.savez(pref + '_J%d.npz' % it, J=J, z=z, R=R)
    dz = np.linalg.lstsq(J, -R, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.06:
        zt = z + lam * dz
        if not (0.05 < zt[-1] < 0.95):
            lam *= 0.5; continue
        Rt, gt, dt = evaluate(zt, g)
        if np.isfinite(Rt).all() and np.linalg.norm(Rt) < (1 - 0.2 * lam) * np.linalg.norm(R):
            acc = True; break
        log(dict(it=it, reject_lam=lam, normR_try=float(np.linalg.norm(Rt)), m1_try=dt['m1'], wall=round(time.time() - t0)))
        lam *= 0.5
    if acc:
        if opt['broyden']:
            s = zt - z; y = Rt - R
            J = J + np.outer(y - J @ s, s) / (s @ s)
        z, R, g, d = zt, Rt, gt, dt
    log(dict(it=it, accepted=acc, lam=lam, z=z.round(6).tolist(), R=R.round(6).tolist(), normR=float(np.linalg.norm(R)),
             dz=dz.round(5).tolist(), **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, a=z[:-1], z=z, R=R, p=z[-1],
             args=json.dumps(dict(p=float(z[-1]), N=N, a=z[:-1].tolist(), kind='fpnewxp', opt=opt)))
    if not acc or np.linalg.norm(R) < 1e-6:
        break
