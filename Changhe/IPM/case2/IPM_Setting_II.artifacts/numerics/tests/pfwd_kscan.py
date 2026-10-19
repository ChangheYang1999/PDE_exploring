"""kappa on the m1 = 1/2 manifold: for each (x1, x2) in a grid, secant in b for c_l - c_mom = 1/2 in
A = cos^2 exp(x1 sin th + x2 cos 2th - b sin 3th), then report kappa(1e-3), kappa(3e-3), kappa(1e-2) (crease amplitude; 1 = smooth node).
Usage: python3 tests/pfwd_kscan.py p tag "x1a,x1b,..." "x2a,x2b,..." [b0=0.12] [Nr=661] [Nth=256] [nsteps=700]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd, datum
torch.set_default_dtype(torch.float64)
p = float(sys.argv[1]); tag = sys.argv[2]; X1 = [float(v) for v in sys.argv[3].split(',')]; X2 = [float(v) for v in sys.argv[4].split(',')]
opt = dict(b0=0.12, Nr=661, Nth=256, lo=-12.0, hi=10.0, nsteps=700, ds=0.02)
for a in sys.argv[5:]:
    k, v = a.split('='); opt[k] = int(v) if k in ('Nr', 'Nth', 'nsteps') else float(v)
S = PFwd(opt['Nr'], opt['Nth'], opt['lo'], opt['hi'], p, dev='cuda')
g = None; log = open('runs/pfwd/kscan_%s.log' % tag, 'a')
def run(x1, x2, b):
    global g
    par = [x1, x2, -b, 0.0]; Afun = lambda th: datum(th, 'expf', par); A = Afun(S.th)
    if g is None:
        g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
    for n in range(opt['nsteps']):
        gn, (Wr, Wt) = S.step(g, opt['ds'], A, Afun)
        if n == opt['nsteps'] - 1: dg = float((gn - g).abs().max()) / opt['ds']
        g = gn
    d = S.diagnostics(g, Wr, Wt, krings=(20,))
    if not math.isfinite(dg) or dg > 1e-2:
        g = None
    return (1 / p - d['c_moment']) - 0.5, d, dg
for x1 in X1:
    for x2 in X2:
        b0, b1 = opt['b0'], opt['b0'] + 0.03
        f0, d0, _ = run(x1, x2, b0); f1, d1, dg = run(x1, x2, b1)
        for it in range(6):
            if abs(f1) < 2e-4 or f1 == f0: break
            b2 = b1 - f1 * (b1 - b0) / (f1 - f0); b0, f0 = b1, f1
            f1, d1, dg = run(x1, x2, b2); b1 = b2
        rec = dict(x1=x1, x2=x2, b=round(b1, 6), m1_moment=round(0.5 + f1, 6), m1_ring=d1['ring20']['m1'], kappa=d1['kappa_axis'], dgds='%.1e' % dg, Rrel=d1['R_rel_bands'])
        print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
print("KSCAN_DONE", flush=True)
