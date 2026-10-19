"""V90 (lead team notes 08:14Z item 5): for own-format states, with my velocity (code/fwdstat.py) on all radial nodes:
min over t of B_+/r = alpha(t, 90 deg) and of B_-/r = alpha(t, 270 deg) with the t of the minimum; min |V|/r over the whole
plane and over 80-100 deg, and min alpha = V_r / r, each with (t, deg).
Usage: python3 tests/v90_axmin.py OWN1.npz [OWN2.npz ...]"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
                dti=0.01, nstep=800)
    rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
    al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy(); sp = np.sqrt(al**2 + be**2)
    t = np.log(F.r.cpu().numpy()); deg = np.degrees(F.th.cpu().numpy())
    j90 = int(np.argmin(np.abs(deg - 90))); j270 = int(np.argmin(np.abs(deg - 270)))
    out = dict(state=fn.split('/')[-1], par=args['par'])
    for nm, j in (('B+/r min', j90), ('B-/r min', j270)):
        i = int(np.argmin(al[:, j])); out[nm] = [round(float(al[i, j]), 4), round(float(t[i]), 2)]
    def mn(f, mask, nm):
        z = np.where(mask[None, :], f, np.inf); i, j = np.unravel_index(np.argmin(z), z.shape)
        out[nm] = [round(float(z[i, j]), 4), round(float(t[i]), 2), round(float(deg[j]), 2)]
    allm = np.ones(nt, bool); win = (deg >= 80) & (deg <= 100)
    mn(sp, allm, 'min|V|/r all'); mn(sp, win, 'min|V|/r 80-100'); mn(al, allm, 'min alpha all')
    print('AXMIN ' + json.dumps(out), flush=True)
