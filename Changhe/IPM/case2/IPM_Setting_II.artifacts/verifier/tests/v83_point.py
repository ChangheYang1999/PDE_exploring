"""V83: one-line summary of an own-format solve O.npz (with O.log from tests/fs_run.py and O_div68.log from tests/v68_div.py):
m1 (solver final), err_fullT, D_lawcorr div / dir (fd1), law-residual spreads on t in [-8, 9.5] (upper / lower, div / dir fd1),
and the window minima of |V|/r and of alpha = V_r/r over ALL radial nodes for th in [80, 100] and [260, 280] deg (own velocity,
code/fwdstat.py), with the (t, deg) of each minimum.
Usage: python3 tests/v83_point.py O    (O without .npz)"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
O = sys.argv[1]
d = np.load(O + '.npz', allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
            dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy(); sp = np.sqrt(al**2 + be**2)
t = np.log(F.r.cpu().numpy()); deg = np.degrees(F.th.cpu().numpy())
out = dict(state=O.split('/')[-1], par=args['par'], p=p, nt=nt)
summ = None
for l in open(O + '.log'):
    if l.startswith('SUMMARY '): summ = json.loads(l[8:])
if summ is not None:
    out['m1'] = round(float(summ['final']['m1']), 6); out['err_fullT'] = float('%.3g' % summ['err_fullT'])
try:
    s = open(O + '_div68.log').read(); dv = json.loads(s[s.index('\n{') + 1:])
    out['D_div_fd1'] = dv['D_lawcorr_div_fd1']; out['D_dir_fd1'] = dv['D_lawcorr_dir_fd1']
    for side in ('upper', 'lower'):
        out['spread_%s_div/dir' % side] = [dv['axis'][side][k]['spread_of_law_residual']['-8..9.5'] for k in ('div_fd1', 'dir_fd1')]
except Exception as e:
    out['div68'] = 'unreadable: ' + str(e)[:60]
for nm, lo, hi in (('upper', 80, 100), ('lower', 260, 280)):
    mj = (deg >= lo) & (deg <= hi)
    for q, f in (('min|V|/r', sp), ('min alpha', al)):
        z = f[:, mj]; i, j = np.unravel_index(np.argmin(z), z.shape)
        out['%s %s' % (nm, q)] = [round(float(z[i, j]), 4), round(float(t[i]), 2), round(float(deg[mj][j]), 2)]
print('POINT ' + json.dumps(out), flush=True)
