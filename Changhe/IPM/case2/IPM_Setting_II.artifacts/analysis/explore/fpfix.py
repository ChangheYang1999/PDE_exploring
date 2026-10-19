# Lead exploration (2026-10-18): fixed-p solve of the "Gt-constant" condition for the forward route.
# Datum A = cos^2 exp(sum_j a_j phi_j) (x-even modes phi_j of fpeval.basis). For fixed p, iterate
#     a <- a - beta * c(a),   c(a) = weighted least-squares coefficients of (log Gt - mean) on phi_1..phi_N,
# log Gt = log A - 2 log|Xi| (fpeval gmode 'gt'), i.e. A <- A (Gt/mean)^(-beta) ~ d |Xi_A|^2, with Anderson mixing (depth m).
# A zero of c is a state with A = d |Xi|^2 on the resolved modes; it is a Setting II profile iff in addition m1 = 1/2.
# Usage: python3 fpfix.py restart.npz p N out_prefix [maxit=30 beta=1 m=4 nmin=300 nmax=2000 tol=1e-8 a0=... cut=0.05]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); pref = sys.argv[4]
opt = dict(maxit=30, beta=1.0, m=4, nmin=300, nmax=2000, tol=1e-8, a0='', cut=0.05, nA=1024)
for s in sys.argv[5:]:
    k, v = s.split('=')
    opt[k] = v if k == 'a0' else (int(v) if k in ('maxit', 'm', 'nmin', 'nmax', 'nA') else float(v))
lr, th = st['lr'], st['th']
a = np.array([float(v) for v in opt['a0'].split(',')]) if opt['a0'] else np.zeros(N)
if len(a) < N:
    a = np.concatenate([a, np.zeros(N - len(a))])
g = st['g']


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
    fit = X @ coef
    rms_rest = float(np.sqrt(np.mean((lgt[w] - fit) ** 2)))
    c = coef[1:]
    v = np.exp(lgt[w] - coef[0])
    return c, g1, dict(m1=ng['m1'], m2=ng['m2'], steps=steps, dgds=dg, Gt_ratio=float(v.max() / v.min()),
                       Gt_std=float(np.std(lgt[w])), rms_unresolved=rms_rest, e1=ng['e1'])


t0 = time.time()
X_hist, F_hist = [], []
for it in range(opt['maxit'] + 1):
    c, g, d = evaluate(a, g)
    print(json.dumps(dict(it=it, p=p, a=a.round(6).tolist(), c=c.round(6).tolist(), normc=float(np.linalg.norm(c)), **d,
                          wall=round(time.time() - t0))), flush=True)
    np.savez(pref + '_it%d.npz' % it, g=g, lr=lr, th=th, a=a, c=c, p=p,
             args=json.dumps(dict(p=p, N=N, a=a.tolist(), kind='fpfix', opt=opt)))
    if np.linalg.norm(c) < 1e-6:
        break
    # Anderson (type II) on the map a -> a - beta c(a)
    X_hist.append(a.copy()); F_hist.append(-c.copy())
    X_hist = X_hist[-(opt['m'] + 1):]; F_hist = F_hist[-(opt['m'] + 1):]
    if len(X_hist) >= 2:
        dF = np.array([F_hist[i + 1] - F_hist[i] for i in range(len(F_hist) - 1)]).T
        dX = np.array([X_hist[i + 1] - X_hist[i] for i in range(len(X_hist) - 1)]).T
        gam = np.linalg.lstsq(dF, F_hist[-1], rcond=1e-10)[0]
        a = X_hist[-1] + opt['beta'] * F_hist[-1] - (dX + opt['beta'] * dF) @ gam
    else:
        a = a + opt['beta'] * F_hist[-1]
