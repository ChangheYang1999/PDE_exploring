# Lead exploration (2026-10-17): Newton (finite-difference Jacobian, backtracking) for the forward
# fixed-point problem R(a, p) = 0 of fpeval.py (datum A = cos^2 exp(sum a_j phi_j), x-even modes; unknowns a, p).
# Usage: python3 fpnewton.py restart.npz p0 N out_prefix [maxit=8] [nbase=800] [nfd=500] [ha=0.02] [hp=0.004] [a0=...]
#        [kind=xeven|full] [wpow=4] [gmode=g|gt]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); pref = sys.argv[4]
opt = dict(maxit=8, nbase=800, nfd=500, ha=0.02, hp=0.004, a0='', kind='xeven', wpow=4, gmode='g')
for s in sys.argv[5:]:
    k, v = s.split('=')
    opt[k] = v if k in ('a0', 'kind', 'gmode') else (int(v) if k in ('maxit', 'nbase', 'nfd', 'wpow') else float(v))
lr, th = st['lr'], st['th']
a = np.array([float(v) for v in opt['a0'].split(',')]) if opt['a0'] else np.zeros(N)
nun = len(a)


def F(z, g0, nsteps):
    a, p = z[:-1], z[-1]
    Af = FE.datum_fn(a, N, opt['kind'])
    g, info = FE.evolve(p, Af, g0, lr, th, nsteps)
    ng = FE.node_and_G(p, Af, g, lr, th)
    R, diag = FE.residual(p, a, N, opt['kind'], ng, opt['wpow'], opt['gmode'])
    return R, g, dict(m1=ng['m1'], m2=ng['m2'], dgds=info['dgds'], **diag)


z = np.concatenate([a, [p]])
t0 = time.time()
R, g, d = F(z, st['g'], opt['nbase'])
log = lambda rec: print(json.dumps(rec), flush=True)
log(dict(it=0, z=z.round(6).tolist(), normR=float(np.linalg.norm(R)), R=R.round(6).tolist(), **d, wall=round(time.time() - t0)))
for it in range(1, opt['maxit'] + 1):
    J = np.zeros((len(R), len(z)))
    for j in range(len(z)):
        h = opt['hp'] if j == len(z) - 1 else opt['ha']
        zj = z.copy(); zj[j] += h
        Rj, _, dj = F(zj, g, opt['nfd'])
        J[:, j] = (Rj - R) / h
    sv = np.linalg.svd(J, compute_uv=False)
    dz = np.linalg.lstsq(J, -R, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.05:
        zt = z + lam * dz
        if not (0.02 < zt[-1] < 0.98):
            lam *= 0.5; continue
        Rt, gt, dt = F(zt, g, opt['nbase'])
        if np.linalg.norm(Rt) < (1 - 0.25 * lam) * np.linalg.norm(R):
            acc = True; break
        lam *= 0.5
    if acc:
        z, R, g, d = zt, Rt, gt, dt
    log(dict(it=it, accepted=acc, lam=lam, z=z.round(6).tolist(), normR=float(np.linalg.norm(R)), R=R.round(6).tolist(),
             sv=sv.round(5).tolist(), dz=dz.round(5).tolist(), **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, z=z, R=R, J=J, args=json.dumps(dict(p=float(z[-1]), N=N, a=z[:-1].tolist(),
             kind='fp', opt=opt)))
    if not acc:
        break
    if np.linalg.norm(R) < 1e-6:
        break
