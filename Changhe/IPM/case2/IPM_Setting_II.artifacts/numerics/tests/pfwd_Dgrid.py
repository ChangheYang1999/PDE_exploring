"""D on the compatibility manifold over a (cos 2th coefficient, p) grid: at each (a_2, p), bisection in a_3 (sin 3th) for m1 = 1/2, then
D = log Gt(269) - log Gt(89), dips, bulk std.  Base datum: N = 6 fixed point.  Usage: python3 tests/pfwd_Dgrid.py tag "a2,..." "p,..." [tol=5e-4]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; A2 = [float(v) for v in sys.argv[2].split(',')]; PS = [float(v) for v in sys.argv[3].split(',')]
tol = float(sys.argv[4].split('=')[1]) if len(sys.argv) > 4 else 5e-4
a0 = [0.2390, -0.7141, -0.21238, 0.1220, 0.1070, -0.0270]
FP = FixedPoint(PS[0], 6, nsteps=900, nA=1440, dt=0.01)
log = open('runs/pfwd/Dgrid_%s.log' % tag, 'a')
def ev(x, p):
    g, Wr, Wt, d, dg, ok = FP.steady(list(x), p)
    Wr, Wt = FP.S.velocity(FP.S.r[:, None] ** p * g); d = FP.S.diagnostics(g, Wr, Wt, krings=(20,))
    m1 = 1 / p - d['c_moment']
    T, u0, w0, th0, it = FP.trace(Wr, Wt, (1.0, 0.0))
    A = FP.Afun(list(x))(FP.thA)
    lg = (torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
    thA = np.degrees(FP.thA.cpu().numpy()); w = np.abs(np.cos(np.radians(thA))) > 0.05
    lg = lg - lg[w].mean(); at = lambda deg: float(lg[int(round(deg / 360 * 1440)) % 1440])
    return m1, dict(D=at(269) - at(89), up=at(89), low=at(269), bulk_std=float(lg[np.abs(np.cos(np.radians(thA))) > 0.3].std()), dgds=dg, ok=ok)
a3_guess = a0[2]
for p in PS:
    for a2 in A2:
        x = list(a0); x[1] = a2
        lo, hi = a3_guess - 0.2, a3_guess + 0.2; nev = 0
        x[2] = lo; mlo, ilo = ev(x, p); flo = mlo - 0.5; nev += 1
        x[2] = hi; mhi, ihi = ev(x, p); fhi = mhi - 0.5; nev += 1
        k = 0
        while flo * fhi > 0 and k < 3:
            if abs(flo) < abs(fhi): lo -= 0.3; x[2] = lo; mlo, ilo = ev(x, p); flo = mlo - 0.5
            else: hi += 0.3; x[2] = hi; mhi, ihi = ev(x, p); fhi = mhi - 0.5
            nev += 1; k += 1
        if flo * fhi > 0:
            rec = dict(a2=a2, p=p, status='no bracket', lo=round(lo, 3), hi=round(hi, 3), m1_lo=round(mlo, 4), m1_hi=round(mhi, 4), D_lo=round(ilo['D'], 3), D_hi=round(ihi['D'], 3), nev=nev)
            print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush(); continue
        for k in range(10):
            mid = 0.5 * (lo + hi); x[2] = mid; mm, im = ev(x, p); fm = mm - 0.5; nev += 1
            if abs(fm) < tol: break
            if fm * flo < 0: hi, fhi = mid, fm
            else: lo, flo = mid, fm
        a3_guess = x[2]
        rec = dict(a2=a2, p=p, a3=round(x[2], 5), m1=round(mm, 5), D=round(im['D'], 4), up=round(im['up'], 4), low=round(im['low'], 4), bulk_std=round(im['bulk_std'], 4), nev=nev, ok=im['ok'])
        print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
print("DGRID_DONE", flush=True)
