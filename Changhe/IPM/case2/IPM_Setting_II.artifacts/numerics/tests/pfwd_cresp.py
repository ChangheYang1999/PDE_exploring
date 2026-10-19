"""Constrained response (referee audit, item 2): for a shape perturbation z of the datum, retune the sin 3th coefficient beta = a_3 so
that m1 = 1/2 again (secant), and report the change of D = log Gt(269) - log Gt(89) (up/down asymmetry of the node), of the dips and of p.
Base: the N = 6 fixed point (p = 0.4957).  Controls: lower bump (sigma 8), upper bump (sigma 8), cos 2th (a_2), cos 4th (a_4), sin th (a_1), p.
Usage: python3 tests/pfwd_cresp.py tag [amps=0.1,-0.1,0.2]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
import pfwd_fp
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; amps = [float(v) for v in (sys.argv[2].split('=')[1] if len(sys.argv) > 2 else "0.1,-0.1").split(',')]
a0 = [0.2390, -0.7141, -0.2097, 0.1220, 0.1070, -0.0270]; p0 = 0.4957
pfwd_fp.BUMPS['Nf'] = 6; pfwd_fp.BUMPS['sigma_deg'] = 8.0
FP = FixedPoint(p0, 8, nsteps=900, nA=1440, dt=0.01)
log = open('runs/pfwd/cresp_%s.log' % tag, 'a')
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
def retune(x, p, beta_idx=2, tol=3e-4):
    """secant on x[beta_idx] (sin 3th) for m1 = 1/2; returns (x, m1, info, nev)"""
    x = list(x); m1, info = ev(x, p); f = m1 - 0.5; n = 1
    if abs(f) < tol: return x, m1, info, n
    slope = -0.9                         # dm1/da3 ~ -0.9 (from the N = 6 Jacobians)
    for k in range(6):
        xb = list(x); xb[beta_idx] = x[beta_idx] - float(np.clip(f / slope, -0.1, 0.1))
        m1b, infob = ev(xb, p); fb = m1b - 0.5; n += 1
        if abs(fb - f) > 1e-6: slope = (fb - f) / (xb[beta_idx] - x[beta_idx])
        if not (0.1 < abs(slope) < 10): slope = -0.9
        x, f, m1, info = xb, fb, m1b, infob
        if abs(f) < tol: break
    return x, m1, info, n
# base (retuned)
xb, m1b, ib, n = retune(a0 + [0.0, 0.0], p0)
rec = dict(control='base', amp=0.0, x=[round(v, 5) for v in xb], p=p0, m1=round(m1b, 5), D=round(ib['D'], 4), up=round(ib['up'], 4), low=round(ib['low'], 4), bulk_std=round(ib['bulk_std'], 4), nev=n)
print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
controls = [('bump270', 7), ('bump90', 6), ('cos2', 1), ('cos4', 3), ('sin1', 0), ('p', -1)]
for name, idx in controls:
    for amp in amps:
        x = list(xb); p = p0
        if idx == -1: p = p0 + amp * 0.5          # p steps of +-0.05 for amp +-0.1
        else: x[idx] += amp
        x2, m1, info, n = retune(x, p)
        dD = info['D'] - ib['D']
        rec = dict(control=name, amp=amp, p=round(p, 5), beta=round(x2[2], 5), dbeta=round(x2[2] - xb[2], 5), m1=round(m1, 5), D=round(info['D'], 4), dD=round(dD, 4),
                   dD_dz=round(dD / amp, 3), up=round(info['up'], 4), low=round(info['low'], 4), bulk_std=round(info['bulk_std'], 4), ok=info['ok'], nev=n)
        print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
print("CRESP_DONE", flush=True)
