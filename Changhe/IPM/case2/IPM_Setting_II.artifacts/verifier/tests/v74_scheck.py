"""V74: check of the arclength tracer (FwdStat.trace_s) against the t tracer on a state with V_r > 0, and (optionally) one
exact T step with arclength orbits on an imported lead/numerics-format state. Usage:
  python3 tests/v74_scheck.py OWN.npz [hs]                                   (own format: rho, r, th, p, args)
  python3 tests/v74_scheck.py IMPORT_G.npz p a1:..:aK tmin nt [hs]           (g, lr, th format)"""
import sys, math, json, time, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
def expf(par):
    def A(t):
        f = np.zeros_like(t)
        for j, aj in enumerate(par):
            n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
        return np.cos(t)**2*np.exp(f)
    return A
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
if 'rho' in d.files:
    args = json.loads(str(d['args'])); p = float(d['p']); par = [float(v) for v in args['par'].split(':')]
    tmin = float(args.get('tmin', -12)); nt = len(d['th']); hs = float(sys.argv[2]) if len(sys.argv) > 2 else 0.03
    F = FwdStat(p, expf(par), tmin=tmin, tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
else:
    p = float(sys.argv[2]); par = [float(v) for v in sys.argv[3].split(':')]; tmin = float(sys.argv[4]); nt = int(sys.argv[5])
    hs = float(sys.argv[6]) if len(sys.argv) > 6 else 0.03
    F = FwdStat(p, expf(par), tmin=tmin, tmax=10, ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
    g0, lr0, th0 = d['g'], d['lr'], d['th']
    rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn) or not np.allclose(th0, thn):
        th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
        G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
F.hs = hs; F.nmax = 8000
sc = F.R**p
out = dict(state=fn.split('/')[-1], p=p, nt=nt, hs=hs, m1_state=F.node(rho)['m1'])
al, be, _, _ = F.fields(rho); out['min_alpha'] = float(al.min()); out['min_speed'] = float(torch.sqrt(al**2 + be**2).min())
t1 = time.time(); F.smode = True
Ts, _ = F.T(rho); out['time_s'] = round(time.time() - t1, 1); out['trace_s'] = F.last_trace
out['m1_Ts'] = F.node(Ts)['m1']; out['defect_s'] = float(((Ts - rho)/sc).abs().max())
if out['min_alpha'] > 0:
    F.smode = False; t1 = time.time()
    Tt, _ = F.T(rho); out['time_t'] = round(time.time() - t1, 1)
    out['m1_Tt'] = F.node(Tt)['m1']; out['defect_t'] = float(((Tt - rho)/sc).abs().max())
    out['max|Ts-Tt|/r^p'] = float(((Ts - Tt)/sc).abs().max())
print(json.dumps(out), flush=True)
