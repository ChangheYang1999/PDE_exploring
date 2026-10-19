# Lead exploration (2026-10-18): Newton for the fixed-p "Gt-constant" problem c(a) = 0 of fpfix.py (x-even datum
# A = cos^2 exp(sum a_j phi_j)), with a finite-difference Jacobian built from CONVERGED evaluations (each perturbed state is
# evolved to dg/ds < tol, starting from the converged base state), damped step with backtracking, and optional Broyden
# updates between full Jacobians. Saves J, the Picard eigenvalues eig(I - J) and the iterates.
# Usage: python3 fpnewx.py restart.npz p N out_prefix [maxit=6 h=0.03 nmin=300 nmax=4000 tol=1e-8 a0=... cut=0.05 nA=1024 broyden=0]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); pref = sys.argv[4]
opt = dict(maxit=6, h=0.03, nmin=300, nmax=4000, tol=1e-8, a0='', cut=0.05, nA=1024, broyden=0)
for s in sys.argv[5:]:
    k, v = s.split('=')
    opt[k] = v if k == 'a0' else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'broyden') else float(v))
lr, th = st['lr'], st['th']
a = np.array([float(v) for v in opt['a0'].split(',')]) if opt['a0'] else np.zeros(N)
if len(a) < N:
    a = np.concatenate([a, np.zeros(N - len(a))])


def evaluate(a, g):
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
    return coef[1:], g1, dict(m1=ng['m1'], m2=ng['m2'], steps=steps, dgds=dg, Gt_ratio=float(v.max() / v.min()),
                              Gt_std=float(np.std(lgt[w])), rms_unresolved=rms_rest, e1=ng['e1'], Tmax=ng['Tmax'])


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
c, g, d = evaluate(a, st['g'])
log(dict(it=0, a=a.round(6).tolist(), c=c.round(6).tolist(), normc=float(np.linalg.norm(c)), **d, wall=round(time.time() - t0)))
J = None
for it in range(1, opt['maxit'] + 1):
    if J is None or opt['broyden'] == 0 or it % (opt['broyden'] + 1) == 1:
        J = np.zeros((N, N)); dm1 = np.zeros(N)
        for j in range(N):
            aj = a.copy(); aj[j] += opt['h']
            cj, _, dj = evaluate(aj, g)
            J[:, j] = (cj - c) / opt['h']; dm1[j] = (dj['m1'] - d['m1']) / opt['h']
            log(dict(col=j, dm1=round(dm1[j], 5), Jcol=J[:, j].round(4).tolist(), steps=dj['steps'], dgds=dj['dgds'],
                     wall=round(time.time() - t0)))
        ev = np.linalg.eigvals(np.eye(N) - J)
        sv = np.linalg.svd(J, compute_uv=False)
        log(dict(it=it, jac='fd', picard_eig_abs=np.sort(np.abs(ev))[::-1].round(4).tolist(), sv=sv.round(5).tolist(),
                 dm1=dm1.round(4).tolist()))
        np.savez(pref + '_J%d.npz' % it, J=J, a=a, c=c, dm1=dm1, p=p)
    da = np.linalg.lstsq(J, -c, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.06:
        at = a + lam * da
        ct, gt, dt = evaluate(at, g)
        if np.isfinite(ct).all() and np.linalg.norm(ct) < (1 - 0.2 * lam) * np.linalg.norm(c):
            acc = True; break
        log(dict(it=it, reject_lam=lam, normc_try=float(np.linalg.norm(ct)), m1_try=dt['m1'], wall=round(time.time() - t0)))
        lam *= 0.5
    if acc:
        if opt['broyden']:
            s = at - a; y = ct - c
            J = J + np.outer(y - J @ s, s) / (s @ s)
        a, c, g, d = at, ct, gt, dt
    log(dict(it=it, accepted=acc, lam=lam, a=a.round(6).tolist(), c=c.round(6).tolist(), normc=float(np.linalg.norm(c)),
             da=da.round(5).tolist(), **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, a=a, c=c, p=p,
             args=json.dumps(dict(p=p, N=N, a=a.tolist(), kind='fpnewx', opt=opt)))
    if not acc or np.linalg.norm(c) < 1e-6:
        break
