"""V66(iv): first-order (fixed-velocity) feedback of a window correction of the inflow datum on the node strain m1.
At fixed V the stationary density is rho(X) = e^{-s} L^p A(th_exit(X)), so A -> A f gives rho -> rho f(th_exit(X)) exactly.
f = exp(w(th) (lg_target - lgGt(th))) with lgGt the deep-stop (e^-12) tracer value of each inflow label (tests/v59_tstop.py npz),
w = 1 for |cos th| < sin 6 deg, cosine taper to 0 at sin 12 deg (the lead's winpic.py windows), separately for the lower window
(around 270 deg), the upper window (around 90 deg) and both. Target: the mean of lgGt over the bulk labels |cos th| > 0.3, or the
value at the window edge (|cos th| = sin 12 deg) on the same side. Prints m1 (moment, fixed p) before and after, and the c change
by radius band.  Usage: python3 tests/v66_winfeed.py STATE.npz TSTOP.npz"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
par = [float(v) for v in args['par'].split(':')]
def Afun(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
F = FwdStat(p, Afun, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800)
S = F.S; w = S.w; r = S.r; t = np.log(r.cpu().numpy())
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
al, be, _, _ = F.fields(rho)
t0 = F.t_nodes[:, None].expand_as(F.R).reshape(-1); th0 = F.TH.reshape(-1)
the, s = F.trace(al, be, t0, th0)
the = np.mod(the.cpu().numpy(), 2*math.pi)
rT = (torch.exp(-s)*F.L**p*torch.tensor(Afun(the), dtype=DT, device='cuda')).reshape(F.R.shape)
ts = np.load(sys.argv[2]); deg = ts['deg']; lg = ts['lg-12']; thl = np.radians(deg)
ac = np.abs(np.cos(thl)); bulk = ac > 0.3; s6, s12 = math.sin(math.radians(6)), math.sin(math.radians(12))
def wfun(th):
    a = np.abs(np.cos(th))
    return np.where(a <= s6, 1.0, np.where(a >= s12, 0.0, 0.5*(1 + np.cos(math.pi*(a - s6)/(s12 - s6)))))
def lg_at(th):
    return np.interp(np.mod(th, 2*math.pi), thl, lg, period=2*math.pi)
bands = ((-99, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 10))
def cband(x):
    rm3 = S.rho_modes(x)[:, 3]; cc = (-2*(w*rm3/r**2).imag).cpu().numpy()
    return {'%g..%g' % b: round(float(cc[(t >= b[0]) & (t < b[1])].sum()), 5) for b in bands}
n0 = F.node(rT); c0 = cband(rT)
out = dict(state=sys.argv[1].split('/')[-1], m1_state=round(F.node(rho)['m1'], 5), m1_T=round(n0['m1'], 5), c_T=round(n0['c'], 5),
           lg_bulk_mean=round(float(lg[bulk].mean()), 4))
edge_lo = float(lg_at(np.array([1.5*math.pi - math.radians(12)]))[0] + lg_at(np.array([1.5*math.pi + math.radians(12)]))[0])/2
edge_up = float(lg_at(np.array([0.5*math.pi - math.radians(12)]))[0] + lg_at(np.array([0.5*math.pi + math.radians(12)]))[0])/2
out['lg_edge_lower'] = round(edge_lo, 4); out['lg_edge_upper'] = round(edge_up, 4)
out['lg_at_270'] = round(float(lg_at(np.array([1.5*math.pi]))[0]), 4); out['lg_at_90'] = round(float(lg_at(np.array([0.5*math.pi]))[0]), 4)
res = {}
for tgt in ('bulk', 'edge'):
    for side in ('lower', 'upper', 'both'):
        wl = wfun(the); lower = np.sin(the) < 0
        sel = np.where(lower, 1.0 if side in ('lower', 'both') else 0.0, 1.0 if side in ('upper', 'both') else 0.0)
        target = lg[bulk].mean() if tgt == 'bulk' else np.where(lower, edge_lo, edge_up)
        fac = np.exp(sel*wl*(target - lg_at(the)))
        r1 = rT*torch.tensor(fac.reshape(F.R.shape), dtype=DT, device='cuda')
        n1 = F.node(r1); c1 = cband(r1)
        res['%s/%s' % (tgt, side)] = dict(m1=round(n1['m1'], 5), dm1=round(n1['m1'] - n0['m1'], 5),
                                          dc_by_band={k: round(c1[k] - c0[k], 5) for k in c0}, max_log_factor=round(float(np.abs(np.log(fac)).max()), 3))
out['window_steps'] = res
print(json.dumps(out, indent=1), flush=True)
