"""V59(b): inner-stop dependence of the backward-orbit tracer log Gt (the V43 tracer: RK4 in t, Xi = e^{t_s} cos(th_s - e1) e^{m1 T})
on a state's own grid, one integration with fixed step h = -0.01 recorded at t_s = -6, -9, -12, -15 (those >= tmin).
The V59 prediction: log Gt(t_s) - log Gt(true) = 2 log k(r_s) on the half-axes, O(r_s) elsewhere.
Usage: python3 tests/v59_tstop.py STATE.npz [ne]"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; ne = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args']))
p = float(d['p']); th = d['th']; nt = len(th)
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
kind = args.get('kind'); assert kind in ('expf', 'expsin3')
par = [float(v) for v in args['par'].split(':')] if kind == 'expf' else [0.0, 0.0, -float(args['par'])]   # expsin3: exp(-par sin 3th)
bump = [float(v) for v in args['bump'].split(':')] if args.get('bump') else None     # as tests/v43_gfix.py (V52)
cmode = float(args['cmode']) if args.get('cmode') else 0.0
sys.path.insert(0, 'tests')
from cwin import cwin_fn
CW = cwin_fn(args['cwin_src']) if args.get('cwin_src') else None     # lead winpic.py window factor (V67)
def Afun(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    A0 = np.cos(t)**2*np.exp(f)*np.exp(cmode*np.sin(3*t)*np.cos(t)**2)*(1.0 if CW is None else CW(t))
    if bump is None: return A0
    s = np.sin(t); bl, bu, w = bump
    return A0*np.exp(bl*np.exp(-(1 + s)/w) + bu*np.exp(-(1 - s)/w))
F = FwdStat(p, Afun, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); m1 = nd['m1']; e1 = math.radians(nd['e1_deg'])
alpha, beta, _, _ = F.fields(rho)
au = F.Imat @ alpha; bu = F.Imat @ beta
the = (torch.arange(ne, dtype=DT, device='cuda') + 0.5)*(2*math.pi/ne)
A = torch.tensor(Afun(the.cpu().numpy()), dtype=DT, device='cuda')
stops = [ts for ts in (-6.0, -9.0, -12.0, -15.0) if ts >= tmin]          # recorded inner stops (state grid permitting)
h = -0.01; nst = int(round((stops[-1] - tmax)/h))
thc = the.clone(); T = torch.zeros_like(thc); t = tmax
def fr(t, th):
    tt = torch.full_like(th, t); a = F.interp(au, tt, th); b = F.interp(bu, tt, th)
    return b/a, -1.0/a
rec = {}
for n in range(1, nst + 1):
    k1t, k1s = fr(t, thc); k2t, k2s = fr(t + h/2, thc + h/2*k1t); k3t, k3s = fr(t + h/2, thc + h/2*k2t); k4t, k4s = fr(t + h, thc + h*k3t)
    thc = thc + h/6*(k1t + 2*k2t + 2*k3t + k4t); T = T + h/6*(k1s + 2*k2s + 2*k3s + k4s); t = tmax + n*h
    for ts in stops:
        if abs(t - ts) < 1e-9:
            logXi = ts + torch.log(torch.abs(torch.cos(thc - e1))) + m1*T
            rec[ts] = ((p*tmax + torch.log(A) - 2*logXi).cpu().numpy(), np.degrees(thc.cpu().numpy()) % 360)
deg = np.degrees(the.cpu().numpy()); mb = np.abs(np.cos(the.cpu().numpy())) > 0.05
out = dict(state=fn.split('/')[-1], nt=nt, tmin=tmin, m1=round(m1, 6), ne=ne,
           mean_cos_gt_0p05={'%g' % ts: round(float(rec[ts][0][mb].mean()), 5) for ts in stops},
           bulk_max_abs_change_cos_gt_0p3_minus9_to_deepest=round(float(np.abs(rec[-9.0][0] - rec[stops[-1]][0])[np.abs(np.cos(np.radians(deg))) > 0.3].max()), 5))
rows = {}
for c0 in (90.0, 270.0):
    for dd in (-10, -5, -3, -2, -1, -0.5, -0.2, -0.09, 0.09, 0.5, 1, 2, 3, 5):
        k = int(np.argmin(np.abs(deg - (c0 + dd))))
        rows['%.3f' % deg[k]] = dict(logGt={'%g' % ts: round(float(rec[ts][0][k]), 4) for ts in stops},
                                     stop_angle={'%g' % ts: round(float(rec[ts][1][k]), 2) for ts in stops})
out['near_zeros'] = rows
def Dd(ts, dd):
    lo = int(np.argmin(np.abs(deg - (270 - dd)))); up = int(np.argmin(np.abs(deg - (90 - dd))))
    return round(float(rec[ts][0][lo] - rec[ts][0][up]), 4)
out['D_d_by_stop'] = {'%g' % dd: {'%g' % ts: Dd(ts, dd) for ts in stops} for dd in (20, 10, 5, 3, 2, 1, 0.5)}
np.savez(fn.replace('.npz', '_v59tstop.npz'), deg=deg, **{'lg%g' % ts: rec[ts][0] for ts in stops}, **{'ang%g' % ts: rec[ts][1] for ts in stops})
print(json.dumps(out), flush=True)
