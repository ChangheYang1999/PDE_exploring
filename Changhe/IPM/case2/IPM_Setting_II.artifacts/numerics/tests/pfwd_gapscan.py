"""Gap scan: can the up/down asymmetry of the node, Delta_z := log Gt(269 deg) - log Gt(89 deg) = log[G(-inf)/G(+inf)], be closed by raising
the datum at its lower zero?  Family: N = 6 fixed-point datum + a Gaussian bump (sigma 8 deg) of amplitude b_l in log A at 270 deg;
for each b_l, p is adjusted by a secant so that m1 = 1/2.  Reports Delta_z, the two dips, the bulk std.  Usage: python3 tests/pfwd_gapscan.py tag "b1,b2,..." [p0=0.4957]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
import pfwd_fp
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; BL = [float(v) for v in sys.argv[2].split(',')]; p0 = float(sys.argv[3].split('=')[1]) if len(sys.argv) > 3 else 0.4957
a0 = [0.2390, -0.7141, -0.2097, 0.1220, 0.1070, -0.0270]
pfwd_fp.BUMPS['Nf'] = 6; pfwd_fp.BUMPS['sigma_deg'] = 8.0
FP = FixedPoint(p0, 8, nsteps=900, nA=1440, dt=0.01)
log = open('runs/pfwd/gapscan_%s.log' % tag, 'a')
def ev(bl, p):
    x = a0 + [0.0, bl]
    g, Wr, Wt, d, dg, ok = FP.steady(x, p)
    m1 = 1 / p - d['c_moment']
    T, u0, w0, th0, it = FP.trace(Wr, Wt, (1.0, 0.0))
    A = FP.Afun(x)(FP.thA)
    lg = (torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
    thA = np.degrees(FP.thA.cpu().numpy()); w = np.abs(np.cos(np.radians(thA))) > 0.05
    lg = lg - lg[w].mean()
    at = lambda deg: float(lg[int(round(deg / 360 * 1440)) % 1440])
    return m1, dict(gap=round(at(269) - at(89), 4), up=round(at(89), 4), low=round(at(269), 4), bulk_std=round(float(lg[np.abs(np.cos(np.radians(thA))) > 0.3].std()), 4), dgds='%.1e' % dg)
p = p0
for bl in BL:
    pa = p
    m1, info = ev(bl, pa); fa = m1 - 0.5
    slope = 0.3                                   # dm1/dp ~ +0.3 (cos^2 family: m1 0.53 at p 0.2 -> 0.61 at p 0.5)
    pb = float(np.clip(pa - np.clip(fa / slope, -0.05, 0.05), 0.25, 0.8))
    for k in range(6):
        if abs(fa) < 3e-4 or abs(pb - pa) < 1e-5: break
        m1b, infob = ev(bl, pb); fb = m1b - 0.5
        if abs(fb - fa) > 1e-6: slope = (fb - fa) / (pb - pa)
        if not (0.05 < abs(slope) < 5): slope = 0.3 * np.sign(slope) if slope != 0 else 0.3
        pn = pb - np.clip(fb / slope, -0.05, 0.05)
        pa, fa, m1, info = pb, fb, m1b, infob
        pb = float(np.clip(pn, 0.25, 0.8))
    rec = dict(b_lower=bl, p=round(pa, 5), m1=round(m1, 5), **info)
    print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
    p = pa
print("GAPSCAN_DONE", flush=True)
