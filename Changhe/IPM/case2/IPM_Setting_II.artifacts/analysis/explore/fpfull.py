# Lead (2026-10-18): forward fixed-point problem WITHOUT symmetry (full class). Datum
#   A(th) = 4 S(th)^2 exp(F(th)),  S = (cos(D/2) - cos(th - sig))/2,  zeros z+ = sig - D/2, z- = sig + D/2 (free unknowns),
#   F = sum_{j<=K} (x-even and x-odd Fourier modes, fpeval kind 'full') + bumps exp(-(1 - cos(th - z+-))/w) at the zeros.
# Unknowns: (a, z+, z-, p). From the stationary state: m1, e1 (weak eigenvector), signed Xi(th) = u0 e^{m1 T} at the exit
# circle, its two zeros b+- (exits of the strong orbits). Regular residual (M24(c) chart): Fr = log A - 2 log|Xi|
# - 2 log|S_z| + 2 log|S_b| (bounded), its LSQ coefficients on [1, basis] (uniform weight away from the zeros), wz (z - b),
# wm (m1 - 1/2), we e1_y (Setting II orientation: weak direction = e_x). Overdetermined by one (index -1, specification M25(d)):
# Gauss-Newton least squares with FD Jacobian and Broyden updates. Nothing is imposed on the parity of the datum.
# Usage: python3 fpfull.py restart.npz p0 K w1,..|0 out_prefix [x0=a..,b+..,b-.. zp=90 zm=270 maxit=10 h=0.03 hz=0.01
#        hp=0.01 nmin=300 nmax=4000 tol=1e-8 cut=0.03 nA=2048 wz=1 wm=1 we=1 refresh=0 Jfile= evalonly=0]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); K = int(sys.argv[3])
ws = [float(v) for v in sys.argv[4].split(',')] if sys.argv[4] != '0' else []
pref = sys.argv[5]
opt = dict(x0='', zp=90.0, zm=270.0, maxit=10, h=0.03, hz=0.01, hp=0.01, nmin=300, nmax=4000, tol=1e-8, cut=0.03, nA=2048,
           wz=1.0, wm=1.0, we=1.0, refresh=0, Jfile='', evalonly=0)
for s in sys.argv[6:]:
    k, v = s.split('=')
    opt[k] = v if k in ('x0', 'Jfile') else (int(v) if k in ('maxit', 'nmin', 'nmax', 'nA', 'refresh', 'evalonly') else float(v))
lr, th = st['lr'], st['th']
nb = 2 * K + 2 * len(ws)


def S_of(t, zp, zm):
    D = zm - zp; sig = 0.5 * (zp + zm)
    return 0.5 * (np.cos(0.5 * D) - np.cos(t - sig))


def basis(t, zp, zm):
    out = [FE.basis(t, K, 'full')] if K > 0 else []
    for w in ws: out.append(np.exp(-(1 - np.cos(t - zp)) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 - np.cos(t - zm)) / w)[None, :])
    return np.vstack(out)


def datum(x, zp, zm):
    x = np.asarray(x, float)
    def A(t):
        tt = np.atleast_1d(t).ravel()
        return (4 * S_of(tt, zp, zm) ** 2 * np.exp(x @ basis(tt, zp, zm))).reshape(np.shape(t))
    return A


def zeros_of(thA, Xs):
    sc = np.nonzero(Xs * np.roll(Xs, -1) < 0)[0]
    out = []
    for i in sc:
        j = (i + 1) % len(thA); t0 = thA[i]; t1 = thA[j] if j > i else thA[j] + 2 * np.pi
        out.append(np.mod(t0 + (t1 - t0) * Xs[i] / (Xs[i] - Xs[j]), 2 * np.pi))
    return np.array(out)


def evaluate(z, g):
    x, zp, zm, pp = z[:nb], z[nb], z[nb + 1], z[nb + 2]
    Af = datum(x, zp, zm)
    g1, i1 = FE.evolve(pp, Af, g, lr, th, opt['nmin'])
    steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(pp, Af, g1, lr, th, 100, tol=opt['tol'])
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(pp, Af, g1, lr, th, nA=opt['nA'])
    thA = ng['thA']; m1 = ng['m1']; e1 = np.array(ng['e1'])
    logXi = m1 * (ng['logAn'] + pp * lr[-1])
    Xs = ng['sgn'] * np.exp(logXi - logXi.max())
    bz = zeros_of(thA, Xs)
    if len(bz) != 2:
        return None, g1, dict(m1=m1, nzeros=int(len(bz)), steps=steps, dgds=dg), None
    # assign b+ to the zero nearest z+
    dpl = lambda a, b: np.abs(np.angle(np.exp(1j * (a - b))))
    if dpl(bz[0], zp) + dpl(bz[1], zm) > dpl(bz[1], zp) + dpl(bz[0], zm):
        bz = bz[::-1]
    bp = zp + np.angle(np.exp(1j * (bz[0] - zp))); bm = zm + np.angle(np.exp(1j * (bz[1] - zm)))
    Sz = S_of(thA, zp, zm); Sb = S_of(thA, bp, bm)
    Fr = np.log(np.maximum(ng['A'], 1e-300)) - 2 * logXi - 2 * np.log(np.abs(Sz) + 1e-300) + 2 * np.log(np.abs(Sb) + 1e-300)
    w = (np.abs(Sz) > opt['cut']) & (np.abs(Sb) > opt['cut']) & np.isfinite(Fr)
    X = np.vstack([np.ones_like(thA), basis(thA, zp, zm)]).T[w]
    coef = np.linalg.lstsq(X, Fr[w], rcond=None)[0]
    res = Fr[w] - coef[0]
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * logXi - coef[0]
    deg = np.degrees(thA)
    pk = {str(d0): round(float(lgt[np.argmin(np.abs(deg - d0))]), 4) for d0 in (0, 45, 80, 86, 88, 135, 180, 250, 262, 266, 268, 315)}
    R = np.concatenate([coef[1:], [opt['wz'] * (zp - bp), opt['wz'] * (zm - bm), opt['wm'] * (m1 - 0.5), opt['we'] * e1[1]]])
    d = dict(m1=m1, e1=e1.round(6).tolist(), bp_deg=float(np.degrees(bp)), bm_deg=float(np.degrees(bm)),
             zp_deg=float(np.degrees(zp)), zm_deg=float(np.degrees(zm)), steps=steps, dgds=dg,
             Fr_range=float(res.max() - res.min()), Fr_std=float(np.std(res)),
             rms_unresolved=float(np.sqrt(np.mean((Fr[w] - X @ coef) ** 2))), pick=pk,
             odd_norm=float(np.linalg.norm(x[K:2 * K])) if K > 0 else 0.0)
    return R, g1, d, (thA, lgt)


log = lambda rec: print(json.dumps(rec), flush=True)
t0 = time.time()
x = np.array([float(v) for v in opt['x0'].split(',')]) if opt['x0'] else np.zeros(nb)
x = np.concatenate([x, np.zeros(max(0, nb - len(x)))])[:nb]
z = np.concatenate([x, [np.radians(opt['zp']), np.radians(opt['zm']), p]])
R, g, d, prof = evaluate(z, st['g'])
log(dict(it=0, z=z.round(5).tolist(), normR=None if R is None else float(np.linalg.norm(R)),
         R=None if R is None else R.round(5).tolist(), **d, wall=round(time.time() - t0)))
if R is None or opt['evalonly']:
    np.savez(pref + '_it0.npz', g=g, lr=lr, th=th, z=z, args=json.dumps(dict(K=K, ws=ws, z=z.tolist(), kind='fpfull')))
    sys.exit(0)
nz = len(z); hs = np.array([opt['h']] * nb + [opt['hz']] * 2 + [opt['hp']])


def fd_jac(z, g, R0):
    J = np.zeros((len(R0), nz))
    for j in range(nz):
        zj = z.copy(); zj[j] += hs[j]
        Rj, _, dj, _ = evaluate(zj, g)
        if Rj is None:
            zj[j] -= 2 * hs[j]; Rj, _, dj, _ = evaluate(zj, g); J[:, j] = (Rj - R0) / (-hs[j])
        else:
            J[:, j] = (Rj - R0) / hs[j]
        log(dict(col=j, Jcol=J[:, j].round(4).tolist(), m1=dj['m1'], wall=round(time.time() - t0)))
    log(dict(jac='fd', sv=np.linalg.svd(J, compute_uv=False).round(6).tolist()))
    np.savez(pref + '_J.npz', J=J, z=z)
    return J


J = np.load(opt['Jfile'])['J'] if opt['Jfile'] else fd_jac(z, g, R)
for it in range(1, opt['maxit'] + 1):
    dz = np.linalg.lstsq(J, -R, rcond=1e-8)[0]
    lam = 1.0; acc = False
    while lam > 0.06:
        zt = z + lam * dz
        if not (0.05 < zt[-1] < 0.95):
            lam *= 0.5; continue
        Rt, gt, dt, proft = evaluate(zt, g)
        if Rt is not None and np.isfinite(Rt).all() and np.linalg.norm(Rt) < (1 - 0.1 * lam) * np.linalg.norm(R):
            acc = True; break
        log(dict(it=it, reject_lam=lam, normR_try=None if Rt is None else float(np.linalg.norm(Rt)), m1_try=dt['m1'],
                 wall=round(time.time() - t0)))
        lam *= 0.5
    if acc:
        s = lam * dz; y = Rt - R
        J = J + np.outer(y - J @ s, s) / (s @ s)
        z, R, g, d, prof = zt, Rt, gt, dt, proft
    log(dict(it=it, accepted=acc, lam=lam, z=z.round(5).tolist(), normR=float(np.linalg.norm(R)), R=R.round(5).tolist(),
             **d, wall=round(time.time() - t0)))
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, z=z, R=R, thA=prof[0], logGt=prof[1], J=J,
             args=json.dumps(dict(K=K, ws=ws, z=z.tolist(), kind='fpfull', opt=opt)))
    if not acc or (opt['refresh'] and it % opt['refresh'] == 0):
        J = fd_jac(z, g, R)
    if np.linalg.norm(R) < 1e-5:
        break
