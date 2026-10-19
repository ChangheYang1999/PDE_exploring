# Lead exploration (2026-10-18): hybrid Newton-Picard for the forward fixed-point problem (x-even data).
# Datum A = cos^2 exp(sum_{j=1}^K a_j phi_j) (fpeval x-even basis), unknowns (a_1..a_K, p). Residual: c = LSQ
# coefficients of log Gt - mean on the K modes (uniform weight on |cos th| > cut) and m1 - 1/2.
# Each iteration (Gauss-Seidel):
#   1. Picard on the high block: a_j <- a_j - omega c_j (j > N); by the symbol at matching (referee result 15) the local
#      multiplier is 1 - e^{-Q}, ~0 at the exits near the zeros of A, < 1 elsewhere.
#   2. Newton on the low block (a_1..a_N, p) with residual (c_1..c_N, wm (m1 - 1/2)); FD Jacobian at the start (or loaded),
#      Broyden updates with the low-block secant pair only; backtracking on the low-block norm.
# Usage: python3 fphyb.py restart.npz p0 K N out_prefix [a0=a1,..] [maxit=10 omega=1 h=0.03 hp=0.01 nmin=300 nmax=4000
#        tol=1e-8 cut=0.05 nA=2048 wm=1 refresh=0 dahmax=0.3]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); K = int(sys.argv[3]); N = int(sys.argv[4]); pref = sys.argv[5]
opt = dict(a0='', maxit=10, omega=1.0, h=0.03, hp=0.01, nmin=300, nmax=4000, tol=1e-8, cut=0.05, nA=2048, wm=1.0,
           refresh=0, dahmax=0.3)
for s in sys.argv[6:]:
    k, v = s.split('=')
    opt[k] = v if k == 'a0' else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'refresh') else float(v))
lr, th = st['lr'], st['th']
a = np.array([float(v) for v in opt['a0'].split(',')]) if opt['a0'] else np.zeros(K)
a = np.concatenate([a, np.zeros(max(0, K - len(a)))])[:K]


def evaluate(a, p, g):
    Af = FE.datum_fn(a, K)
    g1, i1 = FE.evolve(p, Af, g, lr, th, opt['nmin'])
    steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=opt['tol'])
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=opt['nA'])
    thA = ng['thA']
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    w = (np.abs(np.cos(thA)) > opt['cut']) & np.isfinite(lgt)
    X = np.vstack([np.ones_like(thA), FE.basis(thA, K)]).T[w]
    coef = np.linalg.lstsq(X, lgt[w], rcond=None)[0]
    res = lgt[w] - coef[0]
    d = dict(m1=ng['m1'], m2=ng['m2'], steps=steps, dgds=dg, logGt_range=float(res.max() - res.min()),
             logGt_std=float(np.std(res)), rms_unresolved=float(np.sqrt(np.mean((lgt[w] - X @ coef) ** 2))),
             e1=ng['e1'], nlive=ng.get('nlive', -1))
    return coef[1:], ng['m1'], g1, d, (thA, lgt - coef[0])


def RL(c, m1):
    return np.concatenate([c[:N], [opt['wm'] * (m1 - 0.5)]])


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
c, m1, g, d, prof = evaluate(a, p, st['g'])
log(dict(it=0, a=a.round(5).tolist(), p=p, normRL=float(np.linalg.norm(RL(c, m1))), normcH=float(np.linalg.norm(c[N:])),
         cL=c[:N].round(5).tolist(), **d, wall=round(time.time() - t0)))


def fd_jac(a, p, g, R0):
    J = np.zeros((N + 1, N + 1))
    for j in range(N + 1):
        aj = a.copy(); pj = p
        if j < N:
            aj[j] += opt['h']; hh = opt['h']
        else:
            pj += opt['hp']; hh = opt['hp']
        cj, m1j, _, dj, _ = evaluate(aj, pj, g)
        J[:, j] = (RL(cj, m1j) - R0) / hh
        log(dict(col=j, Jcol=J[:, j].round(4).tolist(), steps=dj['steps'], wall=round(time.time() - t0)))
    log(dict(jac='fd', sv=np.linalg.svd(J, compute_uv=False).round(5).tolist()))
    return J


J = fd_jac(a, p, g, RL(c, m1))
np.savez(pref + '_J0.npz', J=J, a=a, p=p)
for it in range(1, opt['maxit'] + 1):
    # 1. Picard on the high block
    if K > N:
        da = -opt['omega'] * c[N:]
        sc = max(1.0, np.max(np.abs(da)) / opt['dahmax'])
        a1 = a.copy(); a1[N:] += da / sc
        c1, m11, g1, d1, _ = evaluate(a1, p, g)
        log(dict(it=it, stage='picard', scale=round(sc, 3), normcH_before=float(np.linalg.norm(c[N:])),
                 normcH_after=float(np.linalg.norm(c1[N:])), normRL=float(np.linalg.norm(RL(c1, m11))), **d1,
                 wall=round(time.time() - t0)))
        a, c, m1, g, d = a1, c1, m11, g1, d1
    # 2. Newton (Broyden) on the low block
    R0 = RL(c, m1)
    dz = np.linalg.lstsq(J, -R0, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.06:
        at = a.copy(); at[:N] += lam * dz[:N]; pt = p + lam * dz[N]
        if not (0.05 < pt < 0.95):
            lam *= 0.5; continue
        ct, m1t, gt, dt, proft = evaluate(at, pt, g)
        Rt = RL(ct, m1t)
        if np.isfinite(Rt).all() and np.linalg.norm(Rt) < (1 - 0.2 * lam) * np.linalg.norm(R0):
            acc = True; break
        log(dict(it=it, reject_lam=lam, normRL_try=float(np.linalg.norm(Rt)), m1_try=m1t, wall=round(time.time() - t0)))
        lam *= 0.5
    if acc:
        s = lam * dz; y = Rt - R0
        J = J + np.outer(y - J @ s, s) / (s @ s)
        a, p, c, m1, g, d, prof = at, pt, ct, m1t, gt, dt, proft
    log(dict(it=it, stage='newton', accepted=acc, lam=lam, a=a.round(5).tolist(), p=round(p, 6),
             normRL=float(np.linalg.norm(RL(c, m1))), normcH=float(np.linalg.norm(c[N:])), cL=c[:N].round(5).tolist(),
             **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, a=a, p=p, c=c, m1=m1, thA=prof[0], logGt=prof[1],
             args=json.dumps(dict(p=float(p), K=K, N=N, a=a.tolist(), kind='fphyb', opt=opt)))
    if not acc:
        J = fd_jac(a, p, g, RL(c, m1))
    elif opt['refresh'] and it % opt['refresh'] == 0:
        J = fd_jac(a, p, g, RL(c, m1))
    if np.linalg.norm(RL(c, m1)) < 1e-5 and np.linalg.norm(c[N:]) < 1e-4:
        break
