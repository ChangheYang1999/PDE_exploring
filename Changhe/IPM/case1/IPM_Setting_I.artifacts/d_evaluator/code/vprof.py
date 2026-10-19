"""Radial residual profiles of a construct1 export by the verifier's evaluation (vcand.main), saved next to the exporter's,
plus D10 and the y^3 axis-ODE residual of the verifier's own axis traces.
Usage: python3 vprof.py file.npz Mmax out.npz [cfg json merged into the vcand cfg]"""
import sys, json
import numpy as np
from scipy.interpolate import CubicSpline
import vcand
path, Mmax, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
cfg = {'Mmax': Mmax, 'b3': True}
if len(sys.argv) > 4:
    cfg.update(json.loads(sys.argv[4]))
out, ev, ax = vcand.main(path, cfg)
json.dump(out, open(outp.replace('.npz', '.json'), 'w'), indent=1, default=float)
d = np.load(path, allow_pickle=True)
r = d['r']
Rmax = np.abs(ev.R).max(1)
Nmax = ev.Rnorm.max(1)
iR = np.abs(ev.R).argmax(1)
Nt = out['Nt']
th_at = 2 * np.pi * iR / Nt
ex_R = np.abs(d['residual']).max(1) if 'residual' in d.files else np.full(len(r), np.nan)
ex_N = d['denominator'].max(1) if 'denominator' in d.files else np.full(len(r), np.nan)
# y^3 axis ODE with own traces: w G3' + (3h - 1) G3 + W1_2 G1' + W2_3 G1 = 0
x, w, h, G1, G1p, G3 = ax['x'], ax['w'], ax['h'], ax['G1'], ax['G1p'], ax['G3']
G3p = CubicSpline(np.log(x), G3)(np.log(x), 1) / x
terms = np.abs(w * G3p) + np.abs((3 * h - 1) * G3) + np.abs(ax['F3'])
R3 = (w * G3p + (3 * h - 1) * G3 - ax['F3']) / terms
R1 = (w * G1p - (1 - h) * G1) / (np.abs(w * G1p) + np.abs((1 - h) * G1))
# regional statistics requested by the lead (NOTES 20:14Z item 5a): near-P disks |X -+ P| < 1, thin bands at the axes
ths = 2 * np.pi * np.arange(Nt) / Nt
Xg, Yg = r[:, None] * np.cos(ths)[None, :], r[:, None] * np.sin(ths)[None, :]
inner = np.zeros(len(r), bool)
inner[8:-8] = True
absR, Npt = np.abs(ev.R), ev.Rnorm
offaxis = (np.abs(np.sin(ths)) > 1e-12) & (np.abs(np.cos(ths)) > 1e-12)
def stats(mask):
    m = mask & inner[:, None]
    if not m.any():
        return None
    # pointwise ratios: exact axis points (rho = 0 identically there, R and the norm are round-off) are excluded
    mm = m & (Npt > 1e-8 * Npt.max(1)[:, None]) & offaxis[None, :]
    j = np.unravel_index(np.argmax(np.where(mm, absR / np.where(mm, Npt, 1), 0)), absR.shape)
    return dict(relsup=float(absR[m].max() / Npt[m].max()), relpt=float((absR[mm] / Npt[mm]).max()),
                at_r=float(r[j[0]]), at_theta=float(ths[j[1]]), npts=int(m.sum()))
reg2 = {}
if out.get('x_star'):
    xs = out['x_star']
    reg2['near_P'] = stats(((Xg - xs) ** 2 + Yg ** 2 < 1) | ((Xg + xs) ** 2 + Yg ** 2 < 1))
    reg2['near_P_0.25'] = stats(((Xg - xs) ** 2 + Yg ** 2 < 0.0625) | ((Xg + xs) ** 2 + Yg ** 2 < 0.0625))
sth = np.abs(np.sin(ths))[None, :] * np.ones((len(r), 1))
cth = np.abs(np.cos(ths))[None, :] * np.ones((len(r), 1))
for lo, hi in ((r[0], 1.0), (1.0, 2.0), (2.0, 10.0), (10.0, 100.0), (100.0, r[-1])):
    band = np.broadcast_to((r[:, None] >= lo) & (r[:, None] <= hi), absR.shape)
    reg2['xaxis_band_%g_%g' % (lo, hi)] = stats(band & (sth < np.sin(0.05)))
    reg2['yaxis_band_%g_%g' % (lo, hi)] = stats(band & (cth < np.sin(0.05)))
    reg2['all_%g_%g' % (lo, hi)] = stats(band)
out['regions2'] = reg2
json.dump(out, open(outp.replace('.npz', '.json'), 'w'), indent=1, default=float)
sub = (slice(None, None, 4), slice(None, None, 4))
np.savez(outp, r=r, Rmax=Rmax, Nmax=Nmax, th_at=th_at, ex_R=ex_R, ex_N=ex_N, R3=R3, R1=R1, x=x, D10=json.dumps(out['D10']), Rrel_sub=(absR / np.maximum(Npt, 1e-300))[sub], r_sub=r[sub[0]], th_sub=ths[sub[1]])
print(json.dumps(dict(D10=out['D10'], regions2=reg2, c=out['c'], c_l=out['c_l'], ex_global_den=float(np.nanmax(ex_N)) if np.isfinite(ex_N).any() else None,
                      own_global_norm=float(Nmax.max()), r_at_own_norm_max=float(r[Nmax.argmax()]),
                      r_at_ex_den_max=float(r[np.nanargmax(ex_N)]) if np.isfinite(ex_N).any() else None), indent=1))
for rr in [x for x in [1, 2, 5, 10, 30, 100, 300, 1e3, 2e3, 3e3, 5e3, 7e3, 1e4, 3e4, 1e5, 1e6, 1e7, 1e8] if x < r[-20]] + [r[-20], r[-9]]:
    j = min(np.searchsorted(r, rr), len(r) - 1)
    print('r=%9.3f own |R|/bandnorm(r) %.2e  own |R|/global %.2e  ex |R|/global %.2e  theta %.3f  R3 %.1e  R1 %.1e'
          % (r[j], Rmax[j] / Nmax[j], Rmax[j] / Nmax.max(), (ex_R[j] / np.nanmax(ex_N) if np.isfinite(ex_N).any() else np.nan), th_at[j], R3[j], R1[j]))
