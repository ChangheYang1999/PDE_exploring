"""V63(b): region where the own velocity has V_r <= 0 on a state in own format: extent in (t, th), and the min |V|/r over that
region (a stagnation point needs V_r = V_th = 0). Usage: python3 tests/v63_vrneg.py STATE.npz"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)),
            q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
al, be, _, _ = [x.cpu().numpy() for x in F.fields(rho)]
t = np.log(F.r.cpu().numpy()); th = np.degrees(F.th.cpu().numpy())
neg = al <= 0
out = dict(state=sys.argv[1], n_neg=int(neg.sum()), min_alpha=float(al.min()))
if neg.any():
    ii, jj = np.nonzero(neg)
    out['t_range'] = [round(float(t[ii].min()), 3), round(float(t[ii].max()), 3)]
    up = th[jj] < 180
    out['th_range_upper'] = [round(float(th[jj][up].min()), 2), round(float(th[jj][up].max()), 2)] if up.any() else None
    sp = np.sqrt(al**2 + be**2)
    out['min_speed_over_r_in_neg_region'] = round(float(sp[neg].min()), 4)
    out['beta_range_in_neg_region'] = [round(float(be[neg].min()), 4), round(float(be[neg].max()), 4)]
# radial profile of min alpha by t
rows = {}
for tt in (-8, -7, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2, -1, 0):
    i = int(np.argmin(np.abs(t - tt))); j = int(np.argmin(al[i]))
    rows['%g' % tt] = [round(float(al[i, j]), 4), round(float(th[j]), 2), round(float(be[i, j]), 4)]
out['min_alpha_by_t_[alpha,deg,beta]'] = rows
print(json.dumps(out))
