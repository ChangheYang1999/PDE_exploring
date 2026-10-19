"""V51(i): which exits carry the strain integral M = int rho r^-3 sin 3th dX = pi (l - m1)?  (test of specification M25(c) "the windows
set G(+-inf), hence rho on most of the node region, hence DV(0)" and of referee result 16 item 2/3 heuristics).  Own code: every grid point
(r_i, th_j) is traced forward to the exit circle r = r_max with FwdStat.trace (the characteristic map the solver itself uses);
the contribution w_i rho_ij r_i^-1 sin 3th_j dth (trapezoid in t = log r) is binned by the exit angle.
Also checks rho_ij = e^{-s} r_max^p A(th_exit) (the solver's own formula, consistency only).
Usage: python3 tests/v51_mexit.py STATE.npz [nstep]."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]
nstep = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
d = np.load(fn, allow_pickle=True)
args = json.loads(str(d['args']))
p = float(d['p']); r0 = d['r']; th0 = d['th']; nt = len(th0)
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), r0), 'grid mismatch'
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); m1 = nd['m1']; l = 1.0/p
alpha, beta, _, _ = F.fields(rho)
t = np.log(r0); Nr = len(t)
T0 = torch.tensor(np.repeat(t, nt), dtype=DT, device='cuda'); TH0 = torch.tensor(np.tile(th0, Nr), dtype=DT, device='cuda')
the, s = F.trace(alpha, beta, T0, TH0, nstep=nstep)
the = torch.remainder(the, 2*math.pi).cpu().numpy().reshape(Nr, nt); s = s.cpu().numpy().reshape(Nr, nt)
par = [float(v) for v in str(args['par']).split(':')]
def Afun(x):
    f = np.zeros_like(x)
    for k, xk in enumerate(par):
        n = k + 1
        f = f + xk*(np.sin(n*x) if n % 2 == 1 else np.cos(n*x))
    return np.cos(x)**2*np.exp(f)
rr = d['rho']
rho_char = np.exp(-s)*np.exp(p*tmax)*Afun(the)
big = rr > 1e-6*rr.max()
w = np.zeros_like(t); dt = np.diff(t); w[:-1] += dt/2; w[1:] += dt/2
c = (w/r0)[:, None]*rr*np.sin(3*th0)[None, :]*(2*math.pi/nt)
Atail = rr[-1]/r0[-1]**p
tail = r0[-1]**(p - 1)/(1 - p)*float((Atail*np.sin(3*th0)).sum())*2*math.pi/nt
M = float(c.sum()) + tail
ed = np.degrees(the)
out = dict(state=fn.split('/')[-1], nt=nt, nstep=nstep, m1=round(m1, 6), M=round(M, 5), M_over_pi=round(M/math.pi, 6),
           l_minus_m1=round(l - m1, 6), tail=round(tail, 5),
           rho_char_relerr_max=float(np.max(np.abs(rho_char[big] - rr[big])/rr[big])))
fr = {}
for c0 in (90.0, 270.0):
    for hw in (1, 2, 5, 10, 20, 30):
        sel = np.abs(((ed - c0) + 180) % 360 - 180) < hw
        fr['%g+-%g' % (c0, hw)] = round(float(c[sel].sum())/M, 4)
out['fraction_of_M_by_exit_window'] = fr
# by exit sector and by radius
rows = []
for a, b in ((-99, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 99)):
    sr = (t >= a) & (t < b)
    up = np.abs(((ed - 90) + 180) % 360 - 180) < 10; lo = np.abs(((ed - 270) + 180) % 360 - 180) < 10
    cs = c[sr]
    rows.append([a, b, round(float(cs.sum())/M, 4), round(float(cs[up[sr]].sum())/M, 4), round(float(cs[lo[sr]].sum())/M, 4)])
out['by_t_band_total_upwin10_lowwin10'] = rows
hist, edges = np.histogram(ed.ravel(), bins=72, range=(0, 360), weights=c.ravel())
out['M_hist_5deg_bins'] = [round(float(v)/M, 4) for v in hist]
print(json.dumps(out), flush=True)
