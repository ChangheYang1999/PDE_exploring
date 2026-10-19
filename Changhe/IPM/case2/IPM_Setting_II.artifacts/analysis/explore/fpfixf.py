# Lead exploration (2026-10-18): fixed-p Gt solve WITHOUT symmetry (full class) for the forward route.
# Datum A = 4 [sin((th - al_p)/2) sin((th - al_m)/2)]^2 exp(F), F = sum_j (a_j cos j th + b_j sin j th), j = 1..N
# (al_p = pi/2, al_m = -pi/2, F = 0 gives cos^2). Picard map with Anderson mixing on z = (al_p, al_m, a, b):
#   al_+- <- beta_+-  (zeros of the signed weak-eigenfunction trace Xi, i.e. the exit angles of the strong separatrices),
#   F     <- LSQ fit (N full modes + constant) of log(|Xi|^2 / s_beta^2) on |s_beta| > cut,
# i.e. A <- d |Xi_A|^2 (Gt = A/|Xi|^2 constant at a fixed point). Reports m1, the e1 angle and M_12.
# A Setting II profile needs in addition m1 = 1/2 and e1 = (1, 0).
# Usage: python3 fpfixf.py restart.npz p N out_prefix [maxit=30 beta=1 m=4 nmin=300 nmax=2000 tol=1e-8 z0=... cut=0.05]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); pref = sys.argv[4]
opt = dict(maxit=30, beta=1.0, m=4, nmin=300, nmax=2000, tol=1e-8, z0='', cut=0.05, nA=1024)
for s in sys.argv[5:]:
    k, v = s.split('=')
    opt[k] = v if k == 'z0' else (int(v) if k in ('maxit', 'm', 'nmin', 'nmax', 'nA') else float(v))
lr, th = st['lr'], st['th']
z = np.array([float(v) for v in opt['z0'].split(',')]) if opt['z0'] else np.concatenate([[np.pi / 2, -np.pi / 2], np.zeros(2 * N)])
g = st['g']


def sfun(t, ap, am):
    return 2 * np.sin((t - ap) / 2) * np.sin((t - am) / 2)


def Fbasis(t):
    return np.array([np.cos(j * t) for j in range(1, N + 1)] + [np.sin(j * t) for j in range(1, N + 1)])


def datum(z):
    ap, am, c = z[0], z[1], z[2:]
    return lambda t: sfun(t, ap, am) ** 2 * np.exp(c @ Fbasis(t))


def evaluate(z, g):
    Af = datum(z)
    g1, i1 = FE.evolve(p, Af, g, lr, th, opt['nmin'])
    steps = i1['steps']; dg = i1['dgds']
    while dg > opt['tol'] and steps < opt['nmax']:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=opt['tol'])
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=opt['nA'])
    thA = ng['thA']; m1 = ng['m1']
    lxi = m1 * ng['logAn']                                   # log |Xi|
    Xi = np.exp(lxi) * ng['sgn']                             # signed trace (side of the node: sign of u0 = X0.e1)
    # zeros: sign changes of the signed trace
    zs = []
    for k in range(len(thA)):
        k2 = (k + 1) % len(thA)
        if Xi[k] == 0:
            zs.append(thA[k])
        elif Xi[k] * Xi[k2] < 0:
            t1 = thA[k]; t2 = thA[k2] if k2 > 0 else 2 * np.pi
            zs.append(t1 + (t2 - t1) * Xi[k] / (Xi[k] - Xi[k2]))
    zs = np.array(zs)
    # assign to al_p (upper, near pi/2) and al_m (lower, near -pi/2)
    def nearest(target):
        d = np.angle(np.exp(1j * (zs - target)))
        return float(target + d[np.argmin(np.abs(d))])
    bp = nearest(z[0]); bm = nearest(z[1])
    s2 = sfun(thA, bp, bm) ** 2
    w = (np.abs(sfun(thA, bp, bm)) > opt['cut'])
    target = 2 * lxi - np.log(np.maximum(s2, 1e-300))
    X = np.vstack([np.ones_like(thA), Fbasis(thA)]).T[w]
    coef = np.linalg.lstsq(X, target[w], rcond=None)[0]
    rms_rest = float(np.sqrt(np.mean((target[w] - X @ coef) ** 2)))
    znew = np.concatenate([[bp, bm], coef[1:]])
    lgt = np.log(np.maximum(Af(thA), 1e-300)) - 2 * lxi
    wv = (np.abs(sfun(thA, z[0], z[1])) > opt['cut'])
    v = np.exp(lgt[wv] - lgt[wv].mean())
    M = np.array(ng['M']).reshape(2, 2)
    e1 = ng['e1']
    return znew, g1, dict(m1=m1, m2=ng['m2'], steps=steps, dgds=dg, nzeros=len(zs), beta_deg=[np.degrees(bp), np.degrees(bm)],
                          Gt_ratio=float(v.max() / v.min()), Gt_std=float(np.std(lgt[wv])), rms_unresolved=rms_rest,
                          e1_angle_deg=float(np.degrees(np.arctan2(e1[1], e1[0]))), M12=float(0.5 * (M[0, 1] + M[1, 0])))


t0 = time.time()
X_hist, F_hist = [], []
for it in range(opt['maxit'] + 1):
    znew, g, d = evaluate(z, g)
    f = znew - z
    print(json.dumps(dict(it=it, p=p, z=z.round(6).tolist(), normf=float(np.linalg.norm(f)), dal_deg=np.degrees(f[:2]).round(4).tolist(),
                          **d, wall=round(time.time() - t0))), flush=True)
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, z=z, f=f, p=p, args=json.dumps(dict(p=p, N=N, z=z.tolist(), kind='fpfixf', opt=opt)))
    if np.linalg.norm(f) < 1e-6:
        break
    X_hist.append(z.copy()); F_hist.append(f.copy())
    X_hist = X_hist[-(opt['m'] + 1):]; F_hist = F_hist[-(opt['m'] + 1):]
    if len(X_hist) >= 2:
        dF = np.array([F_hist[i + 1] - F_hist[i] for i in range(len(F_hist) - 1)]).T
        dX = np.array([X_hist[i + 1] - X_hist[i] for i in range(len(X_hist) - 1)]).T
        gam = np.linalg.lstsq(dF, F_hist[-1], rcond=1e-10)[0]
        z = X_hist[-1] + opt['beta'] * F_hist[-1] - (dX + opt['beta'] * dF) @ gam
    else:
        z = z + opt['beta'] * f
