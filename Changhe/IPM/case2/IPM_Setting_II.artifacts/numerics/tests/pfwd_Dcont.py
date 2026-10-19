"""Continuation of the up/down node asymmetry D = log Gt(269) - log Gt(89) along the compatibility manifold (m1 = 1/2) in the lobe-shape
direction: for each cos 2th coefficient a_2 in a list, the sin 3th coefficient a_3 is found by bracketing + bisection so that m1 = 1/2
(p fixed), then D, the two dips and the bulk std are reported.  Base: N = 6 fixed point (p = 0.4957).
Usage: python3 tests/pfwd_Dcont.py tag "a2_1,a2_2,..." [p=0.4957] [tol=3e-4]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; A2 = [float(v) for v in sys.argv[2].split(',')]
opt = dict(p=0.4957, tol=3e-4)
for s_ in sys.argv[3:]:
    k, v = s_.split('='); opt[k] = float(v)
p = opt['p']; a0 = [0.2390, -0.7141, -0.21238, 0.1220, 0.1070, -0.0270]
FP = FixedPoint(p, 6, nsteps=900, nA=1440, dt=0.01)
log = open('runs/pfwd/Dcont_%s.log' % tag, 'a')
def ev(x):
    g, Wr, Wt, d, dg, ok = FP.steady(list(x), p)
    Wr, Wt = FP.S.velocity(FP.S.r[:, None] ** p * g); d = FP.S.diagnostics(g, Wr, Wt, krings=(20,))
    m1 = 1 / p - d['c_moment']
    T, u0, w0, th0, it = FP.trace(Wr, Wt, (1.0, 0.0))
    A = FP.Afun(list(x))(FP.thA)
    lg = (torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
    thA = np.degrees(FP.thA.cpu().numpy()); w = np.abs(np.cos(np.radians(thA))) > 0.05
    lg = lg - lg[w].mean(); at = lambda deg: float(lg[int(round(deg / 360 * 1440)) % 1440])
    return m1, dict(D=at(269) - at(89), up=at(89), low=at(269), bulk_std=float(lg[np.abs(np.cos(np.radians(thA))) > 0.3].std()), dgds=dg, ok=ok)
a3 = a0[2]
for a2 in A2:
    x = list(a0); x[1] = a2
    # bracket in a_3 around the previous solution (m1 decreases with a_3 increasing? slope dm1/da3 ~ -0.9 -> m1 - 1/2 is decreasing in a3)
    lo, hi = a3 - 0.15, a3 + 0.15; nev = 0
    x[2] = lo; mlo, ilo = ev(x); flo = mlo - 0.5; nev += 1
    x[2] = hi; mhi, ihi = ev(x); fhi = mhi - 0.5; nev += 1
    k = 0
    while flo * fhi > 0 and k < 4:      # widen the bracket
        if abs(flo) < abs(fhi): lo -= 0.2; x[2] = lo; mlo, ilo = ev(x); flo = mlo - 0.5
        else: hi += 0.2; x[2] = hi; mhi, ihi = ev(x); fhi = mhi - 0.5
        nev += 1; k += 1
    if flo * fhi > 0:
        rec = dict(a2=a2, status='no bracket', lo=lo, hi=hi, flo=round(flo, 5), fhi=round(fhi, 5)); print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush(); continue
    for k in range(9):
        mid = 0.5 * (lo + hi); x[2] = mid; mm, im = ev(x); fm = mm - 0.5; nev += 1
        if abs(fm) < opt['tol']: break
        if fm * flo < 0: hi, fhi, ihi = mid, fm, im
        else: lo, flo, ilo = mid, fm, im
    a3 = x[2]
    rec = dict(a2=a2, a3=round(a3, 5), p=p, m1=round(mm, 5), D=round(im['D'], 4), up=round(im['up'], 4), low=round(im['low'], 4), bulk_std=round(im['bulk_std'], 4), nev=nev, ok=im['ok'])
    print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
print("DCONT_DONE", flush=True)
