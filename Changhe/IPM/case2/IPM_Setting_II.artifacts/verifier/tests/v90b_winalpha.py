"""V90b: min of alpha = V_r / r over the upper window 80-100 deg (all radial nodes) with (t, deg), and the same with the window
edges excluded (82-98 deg), for own-format states, my velocity (code/fwdstat.py).
Usage: python3 tests/v90b_winalpha.py OWN1.npz [OWN2.npz ...]"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
                dti=0.01, nstep=800)
    rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
    al, be, _, _ = F.fields(rho); al = al.cpu().numpy()
    t = np.log(F.r.cpu().numpy()); deg = np.degrees(F.th.cpu().numpy())
    out = dict(state=fn.split('/')[-1])
    for nm, lo, hi in (('80-100', 80, 100), ('82-98', 82, 98), ('85-95', 85, 95)):
        z = np.where(((deg >= lo) & (deg <= hi))[None, :], al, np.inf); i, j = np.unravel_index(np.argmin(z), z.shape)
        out['min alpha ' + nm] = [round(float(z[i, j]), 4), round(float(t[i]), 2), round(float(deg[j]), 2)]
    print('WINALPHA ' + json.dumps(out), flush=True)
