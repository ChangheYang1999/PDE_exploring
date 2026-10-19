"""V74 helper: min V_r/r (alpha) of a lead/numerics-format state (g, lr, th) interpolated to my grid (as in tests/fs_run.py),
with my velocity; also min |V|/r. Usage: python3 tests/v74_alpha.py STATE.npz p tmin nt"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
fn, p, tmin, nt = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=10, ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
d = np.load(fn); g0, lr0, th0 = d['g'], d['lr'], d['th']
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
    G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy(); sp = np.sqrt(al**2 + be**2)
au = (F.Imat @ torch.tensor(al, device='cuda')).cpu().numpy(); tu = F.tu.cpu().numpy()
i, j = np.unravel_index(np.argmin(al), al.shape); iu, ju = np.unravel_index(np.argmin(au), au.shape)
neg = al <= 0
out = dict(min_alpha=float(al.min()), at_t=float(lrr[i]), at_deg=float(np.degrees(thn[j])), min_alpha_interp=float(au.min()),
           interp_at_t=float(tu[iu]), interp_at_deg=float(np.degrees(thn[ju])), n_nonpos=int(neg.sum()),
           t_range_nonpos=[float(lrr[neg.any(1)].min()), float(lrr[neg.any(1)].max())] if neg.any() else None,
           g_lo=float(lr0[0]))
k, m = np.unravel_index(np.argmin(sp), sp.shape)
out['min_speed_over_r'] = float(sp.min()); out['speed_at'] = [float(lrr[k]), float(np.degrees(thn[m]))]
out['alpha_beta_at_speed_min'] = [float(al[k, m]), float(be[k, m])]
print(json.dumps(out))
