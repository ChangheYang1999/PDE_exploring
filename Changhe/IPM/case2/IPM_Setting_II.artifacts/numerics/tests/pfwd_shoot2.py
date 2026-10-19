"""Two-parameter shoot for a smooth node: find (x1, b) in A = cos^2 exp(x1 sin th - b sin 3th) with
      F1 = c_l - c_moment - 1/2 = 0   (m1 = 1/2, compatibility)      and      F2 = kappa(r_k) - 1 = 0   (no crease on the weak axis),
by Broyden's method with a finite-difference initial Jacobian and warm restarts.  kappa(r) = axis value / off-axis x^2 law (pfwd.diagnostics).
Usage: python3 tests/pfwd_shoot2.py p x1_0 b_0 tag [rk=0.003] [Nr=661] [Nth=256] [nsteps=800] [tol=2e-4] [maxit=15] [h=0.05]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd, datum
torch.set_default_dtype(torch.float64)
p = float(sys.argv[1]); x1 = float(sys.argv[2]); b = float(sys.argv[3]); tag = sys.argv[4]
opt = dict(rk=0.003, Nr=661, Nth=256, lo=-12.0, hi=10.0, nsteps=800, tol=2e-4, maxit=15, h=0.05, ds=0.02)
for a in sys.argv[5:]:
    k, v = a.split('='); opt[k] = int(v) if k in ('Nr', 'Nth', 'nsteps', 'maxit') else float(v)
S = PFwd(opt['Nr'], opt['Nth'], opt['lo'], opt['hi'], p, dev='cuda')
g = None; log = open('runs/pfwd/shoot2_%s.log' % tag, 'a'); rk_key = '%g' % opt['rk']
def F(x):
    global g
    x1, b = float(x[0]), float(x[1]); par = [x1, 0.0, -b, 0.0]
    Afun = lambda th: datum(th, 'expf', par); A = Afun(S.th)
    if g is None:
        g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
    t0 = time.time()
    for n in range(opt['nsteps']):
        gn, (Wr, Wt) = S.step(g, opt['ds'], A, Afun)
        if n == opt['nsteps'] - 1: dg = float((gn - g).abs().max()) / opt['ds']
        g = gn
    d = S.diagnostics(g, Wr, Wt, krings=(20,))
    f = np.array([1 / p - d['c_moment'] - 0.5, d['kappa_axis'][rk_key] - 1.0])
    rec = dict(x1=x1, b=b, F=[round(float(v), 6) for v in f], m1_ring=d['ring20']['m1'], c_mom=round(d['c_moment'], 6), kappa=d['kappa_axis'],
               dgds='%.1e' % dg, Rrel=d['R_rel_bands'], wall=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
    return f, d
x = np.array([x1, b]); f, d = F(x)
h = opt['h']; J = np.zeros((2, 2))
for j in range(2):
    xp = x.copy(); xp[j] += h; fp, _ = F(xp); J[:, j] = (fp - f) / h
for it in range(opt['maxit']):
    if np.abs(f).max() < opt['tol']: break
    dx = -np.linalg.solve(J, f)
    if np.abs(dx).max() > 0.5: dx *= 0.5 / np.abs(dx).max()
    xn = x + dx; fn, d = F(xn)
    J = J + np.outer(fn - f - J @ dx, dx) / (dx @ dx)
    x, f = xn, fn
np.savez('runs/pfwd/shoot2_%s.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), hist=json.dumps([dict(x1=float(x[0]), b=float(x[1]), F=f.tolist())]),
         args=json.dumps(dict(p=p, kind='expf', par=[float(x[0]), 0.0, -float(x[1]), 0.0], Nr=opt['Nr'], Nth=opt['Nth'], lo=opt['lo'], hi=opt['hi'], ds=opt['ds'])))
print("SHOOT2_RESULT", json.dumps(dict(p=p, x1=float(x[0]), b=float(x[1]), F=f.tolist(), kappa=d['kappa_axis'], m1_ring=d['ring20']['m1'], Rrel=d['R_rel_bands'], file='runs/pfwd/shoot2_%s.npz' % tag)), flush=True)
