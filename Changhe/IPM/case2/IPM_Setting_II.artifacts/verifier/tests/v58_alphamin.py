"""V58: location of min alpha = V_r/r on a forward state (where the star-shaped condition V_r > 0 of my solver is closest to failing).
Usage: python3 tests/v58_alphamin.py STATE.npz"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args']))
p = float(d['p']); th = d['th']; nt = len(th)
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
al = F.fields(rho)[0].cpu().numpy(); t = np.log(F.r.cpu().numpy())
i, j = np.unravel_index(np.argmin(al), al.shape)
print(json.dumps(dict(state=sys.argv[1], m1=round(F.node(rho)['m1'], 6), min_alpha=round(float(al[i, j]), 5), at_t=round(float(t[i]), 3), at_deg=round(float(np.degrees(th[j])) % 360, 2),
      alpha_upper_axis_by_t={'%g' % tt: round(float(al[np.argmin(np.abs(t - tt)), np.argmin(np.abs(np.degrees(th) % 360 - 90))]), 4) for tt in (-10, -8, -6, -5, -4, -3, -2, -1, 0, 2)},
      alpha_lower_axis_by_t={'%g' % tt: round(float(al[np.argmin(np.abs(t - tt)), np.argmin(np.abs(np.degrees(th) % 360 - 270))]), 4) for tt in (-10, -8, -6, -4, -2, 0, 2)},
      min_alpha_by_t={'%g' % tt: [round(float(al[np.argmin(np.abs(t - tt))].min()), 4), round(float(np.degrees(th[np.argmin(al[np.argmin(np.abs(t - tt))])])) % 360, 1)] for tt in (-8, -6, -5, -4, -3, -2, -1, 0)})))
