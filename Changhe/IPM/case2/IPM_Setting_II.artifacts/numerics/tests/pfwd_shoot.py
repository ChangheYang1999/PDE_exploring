"""Secant shooting for m1[A_b] = 1/2 in a one-parameter family A_b = cos^2 exp(-b sin 3th) (p given), warm restarts.
Usage: python3 tests/pfwd_shoot.py p b0 b1 tag [Nr=661] [Nth=256] [lo=-12] [hi=10] [nsteps=800] [tol=1e-5] [kring=20]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd, datum
torch.set_default_dtype(torch.float64)
p = float(sys.argv[1]); b0 = float(sys.argv[2]); b1 = float(sys.argv[3]); tag = sys.argv[4]
opt = dict(Nr=661, Nth=256, lo=-12.0, hi=10.0, nsteps=800, tol=1e-5, kring=20, ds=0.02, thshift=0.0, a=0.0)
for a in sys.argv[5:]:
    k, v = a.split('='); opt[k] = int(v) if k in ('Nr', 'Nth', 'nsteps', 'kring') else float(v)
S = PFwd(opt['Nr'], opt['Nth'], opt['lo'], opt['hi'], p, dev='cuda', thshift=opt['thshift'])
g = None
def m1_of(b):
    global g
    par = [0.0, opt['a'], -b, 0.0]
    Afun = lambda th: datum(th, 'expf', par); A = Afun(S.th)
    if g is None:
        g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
    t0 = time.time()
    for n in range(opt['nsteps']):
        gn, (Wr, Wt) = S.step(g, opt['ds'], A, Afun)
        if n == opt['nsteps'] - 1:
            dg = float((gn - g).abs().max()) / opt['ds']
        g = gn
    d = S.diagnostics(g, Wr, Wt, krings=(8, opt['kring'], 40, 80))
    rec = dict(b=b, m1=d['ring%d' % opt['kring']]['m1'], m1_rings=[d['ring%d' % k]['m1'] for k in (8, opt['kring'], 40, 80)],
               c_mom=d['c_moment'], deficit=d['c_target'] - d['c_moment'], e1=d['ring%d' % opt['kring']]['e1_deg'], dgds='%.1e' % dg, kappa=d['kappa_axis'],
               Rrel=d['R_rel_bands'], wall=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True)
    return d['ring%d' % opt['kring']]['m1'] - 0.5, rec
f0, r0 = m1_of(b0); f1, r1 = m1_of(b1)
for it in range(12):
    b2 = b1 - f1 * (b1 - b0) / (f1 - f0)
    f2, r2 = m1_of(b2)
    b0, f0, b1, f1 = b1, f1, b2, f2
    if abs(f2) < opt['tol']:
        break
np.savez('runs/pfwd/shoot_%s.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), hist=json.dumps([r2]),
         args=json.dumps(dict(p=p, kind='expf', par=[0.0, opt['a'], -b1, 0.0], Nr=opt['Nr'], Nth=opt['Nth'], lo=opt['lo'], hi=opt['hi'], ds=opt['ds'], thshift=opt['thshift'])))
print("SHOOT_RESULT", json.dumps(dict(p=p, a=opt['a'], b_star=b1, m1=r2['m1'], m1_rings=r2['m1_rings'], c_mom=r2['c_mom'], kappa=r2['kappa'], Rrel=r2['Rrel'], file='runs/pfwd/shoot_%s.npz' % tag)), flush=True)
