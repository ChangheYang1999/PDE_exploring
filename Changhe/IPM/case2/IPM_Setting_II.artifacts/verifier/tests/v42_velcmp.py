"""V42: compare the lead's velocity (analysis/explore/pforward.py velocity_p, imported read-only as an external comparator)
with my exact-Green velocity (code/fwdstat.py -> code/charsolve.py) on the SAME density, on the lead's log-polar grid.
The lead's radial recursion is the trapezoid rule for the kernel e^{-|m| |u - v|}: for constant h its weight is
(d/2) coth(|m| d/2) instead of 1/|m|, relative error ~ (|m| d)^2/12, large for |m| d ~ 1 (m = 64, d = 0.033: +34%).
Usage: python3 tests/v42_velcmp.py FILE p  (lead/num npz with g, lr, th, or own npz with rho, r, th, p -> resampled to 661 x nt)."""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
sys.path.insert(0, '../analysis/explore')
from fwdstat import FwdStat
import pforward as LP
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True)
if 'g' in d.files:
    g0, lr0, th0 = d['g'], d['lr'], d['th']
else:   # own state: resample to a lead-type grid 661 x nt on [-12, 10]
    r0 = d['r']; th0 = d['th']; gq = d['rho']/r0[:, None]**float(d['p']); lq = np.log(r0)
    lr0 = np.linspace(-12, 10, 661); g0 = CubicSpline(lq, gq, axis=0)(np.clip(lr0, lq[0], lq[-1]))
Nr, Nth = g0.shape
assert np.allclose(th0, 2*np.pi*np.arange(Nth)/Nth)
r0 = np.exp(lr0)
Wr_L, Wt_L = LP.velocity_p(r0[:, None]**p*g0, lr0, th0, p)
out = {}
for ppu in (3, 5):
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=8, nt=Nth, dti=0.01, nstep=10)
    rr = F.r.cpu().numpy(); lrr = np.log(rr)
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
    alpha, beta, W1, W2 = F.fields(rho)
    a_m = CubicSpline(lrr, alpha.cpu().numpy(), axis=0)(lr0); b_m = CubicSpline(lrr, beta.cpu().numpy(), axis=0)(lr0)
    a_L = l + Wr_L/r0[:, None]; b_L = Wt_L/r0[:, None]
    bands = {}
    for lo_, hi_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3), (3, 9.5)):
        k = (lr0 >= lo_) & (lr0 < hi_)
        bands['%g..%g' % (lo_, hi_)] = dict(dalpha=float(np.abs(a_m[k] - a_L[k]).max()), dbeta=float(np.abs(b_m[k] - b_L[k]).max()),
                                          beta_scale=float(np.abs(b_m[k]).max()), alpha_min=float(a_m[k].min()))
    out['ppu%d' % ppu] = bands
    if ppu == 3: a3, b3 = a_m, b_m
    else:
        out['my_ppu3_vs_ppu5_dbeta'] = float(np.abs(b3[(lr0 > -11.5) & (lr0 < 9.5)] - b_m[(lr0 > -11.5) & (lr0 < 9.5)]).max())
print(json.dumps(dict(file=f.split('/')[-1], Nr=Nr, Nth=Nth, d=float(lr0[1] - lr0[0]), **out)), flush=True)
