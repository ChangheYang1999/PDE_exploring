"""Response of the orbit invariant Gt to local changes of the datum near its zeros (re-timing test): for the N = 6 fixed-point datum
(p = 0.4957) add bumps to log A (Gaussian, sigma 8 deg) at 90 and 270 deg and a broad tilt, re-evolve, and report the change of
log Gt at the zeros and in the bulk, and of m1.  A response factor << 1 at the zeros means the dips there cannot be removed by local
changes of A.  Usage: python3 tests/pfwd_response.py"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
import pfwd_fp
from pfwd_fp import FixedPoint, basis
torch.set_default_dtype(torch.float64)
p = 0.4957; a0 = [0.2390, -0.7141, -0.2097, 0.1220, 0.1070, -0.0270]
pfwd_fp.BUMPS['Nf'] = 6; pfwd_fp.BUMPS['sigma_deg'] = 8.0
FP = FixedPoint(p, 10, nsteps=900, nA=1440, dt=0.01)        # basis 6,7 = bumps at 90 / 270 (sigma 8), 8,9 = wide bumps (sigma 16)
def prof(x):
    g, Wr, Wt, d, dg, ok = FP.steady(list(x), p)
    m1 = 1 / p - d['c_moment']
    T, u0, w0, th0, it = FP.trace(Wr, Wt, (1.0, 0.0))
    A = FP.Afun(list(x))(FP.thA)
    lg = (torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
    thA = np.degrees(FP.thA.cpu().numpy()); w = np.abs(np.cos(np.radians(thA))) > 0.05
    return m1, lg - lg[w].mean(), dg
def at(v, deg): return float(v[int(round(deg / 360 * 1440)) % 1440])
m1b, base, dg = prof(a0 + [0, 0, 0, 0])
print("base: m1 = %.5f, dg/ds %.1e; log Gt - mean at 0/45/85/89 | 180/225/265/269: %s" % (m1b, dg, ' '.join('%.3f' % at(base, d_) for d_ in (0, 45, 85, 89, 180, 225, 265, 269))))
cases = [("bump 90 deg, +0.3 (sigma 8)", [0, 0, 0, 0], 6, 0.3), ("bump 270 deg, +0.3 (sigma 8)", [0, 0, 0, 0], 7, 0.3), ("bump 270 deg, +1.0 (sigma 8)", [0, 0, 0, 0], 7, 1.0),
         ("wide bump 270 deg, +0.5 (sigma 16)", [0, 0, 0, 0], 9, 0.5), ("tilt sin th, -0.3 (whole circle)", None, 0, -0.3)]
for name, extra, idx, amp in cases:
    x = list(a0) + ([0, 0, 0, 0] if extra is not None else [0, 0, 0, 0])
    if extra is None: x[0] += amp
    else: x[idx] += amp
    m1, lg, dg = prof(x)
    dl = lg - base
    print("%-36s: m1 = %.5f (dm1 = %+.4f), dg/ds %.1e; d(log Gt) at 0/45/85/89 | 180/225/265/269: %s   [input d log A at 89: %+.3f, at 269: %+.3f]" % (
        name, m1, m1 - m1b, dg, ' '.join('%+.3f' % at(dl, d_) for d_ in (0, 45, 85, 89, 180, 225, 265, 269)),
        float(basis(torch.tensor([math.radians(89.0)]), idx) * amp) if extra is not None else -0.3 * math.sin(math.radians(89)),
        float(basis(torch.tensor([math.radians(269.0)]), idx) * amp) if extra is not None else -0.3 * math.sin(math.radians(269))))
