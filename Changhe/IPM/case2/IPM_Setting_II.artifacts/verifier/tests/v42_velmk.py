import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']
Nr, Nth = g0.shape; r0 = np.exp(lr0)
rho0 = r0[:, None]**p*g0
# angular spectrum of rho per band
Fm = np.abs(np.fft.rfft(rho0, axis=1))
for lo_, hi_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3)):
    k = (lr0 >= lo_) & (lr0 < hi_)
    tot = Fm[k].max(axis=0)
    print('band %g..%g' % (lo_, hi_), 'max|rho_m|/max|rho_0|: m=8 %.1e m=16 %.1e m=32 %.1e m=48 %.1e m=56 %.1e m=61 %.1e m=64 %.1e' % tuple(
        (Fm[k][:, mm]/Fm[k][:, 0]).max() for mm in (8, 16, 32, 48, 56, 61, 64)))
res = {}
for mk in (61, 50, 40, 30):
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=5, q=8, nt=Nth, dti=0.01, nstep=10, mkeep=mk)
    rr = F.r.cpu().numpy(); lrr = np.log(rr)
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    am, bm, _, _ = F.fields(torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda'))
    res[mk] = (CubicSpline(lrr, am.cpu().numpy(), axis=0)(lr0), CubicSpline(lrr, bm.cpu().numpy(), axis=0)(lr0))
    del F; torch.cuda.empty_cache()
for mk in (50, 40, 30):
    row = {}
    for lo_, hi_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0)):
        k = (lr0 >= lo_) & (lr0 < hi_)
        row['%g..%g' % (lo_, hi_)] = '%.1e/%.1e' % (np.abs(res[mk][0] - res[61][0])[k].max(), np.abs(res[mk][1] - res[61][1])[k].max())
    print('mkeep', mk, 'vs 61', json.dumps(row))
np.savez('velmk_me.npz', a=res[61][0], b=res[61][1])
