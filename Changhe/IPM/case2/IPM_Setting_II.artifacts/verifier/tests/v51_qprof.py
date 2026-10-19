"""V51(e): Q = int rho V_2/|V|^2 dtau along the backward orbits of a forward state, as a function of the exit angle (test of
specification M25(c) / notes of the lead analyst 01:16Z: "Q ~ 0 at the zero exits, ~4 near th = 0", and of referee result 15: Q = 0 on the zero set at a fixed point).
Tracer as in tests/v47_hfsym.py (own code): RK4 in t = log r from tmax to tstop, d th/dt = beta/alpha, dQ/dt = -q/alpha with
q = (rho/r)(alpha sin th + beta cos th)/(alpha^2 + beta^2) (= rho V_2/|V|^2 in polar form).  Also s_t = 1 - 2 m1 (1 - e^{-Q})
(Gt symbol, lambda = 1, delta m1 neglected) and e^{-Q} (its value at matching).
Usage: python3 tests/v51_qprof.py STATE.npz [ne] [tstop] [nstep]."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]
ne = int(sys.argv[2]) if len(sys.argv) > 2 else 2880
tstop = float(sys.argv[3]) if len(sys.argv) > 3 else -9.0
nstep = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
d = np.load(fn, allow_pickle=True)
args = json.loads(str(d['args']))
p = float(d['p']); r0 = d['r']; nt = len(d['th'])
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), r0), 'grid mismatch'
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); m1 = nd['m1']
alpha, beta, _, _ = F.fields(rho)
au = F.Imat @ alpha; bu = F.Imat @ beta; qu = F.Imat @ (rho/F.R)
the = (torch.arange(ne, dtype=DT, device='cuda') + 0.5)*(2*math.pi/ne)
hh = (tstop - F.tmax)/nstep
th = the.clone(); Q = torch.zeros_like(th); t = torch.full_like(th, F.tmax)
def fr(t, th):
    a = F.interp(au, t, th); b = F.interp(bu, t, th); q = F.interp(qu, t, th)
    return b/a, -q*(a*torch.sin(th) + b*torch.cos(th))/((a*a + b*b)*a)
Qmid = {}
for n in range(nstep):
    k1 = fr(t, th); k2 = fr(t + hh/2, th + hh/2*k1[0]); k3 = fr(t + hh/2, th + hh/2*k2[0]); k4 = fr(t + hh, th + hh*k3[0])
    th = th + hh/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
    Q = Q + hh/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    t = t + hh
    for tm in (0.0, -2.0, -5.0):
        if abs(float(t[0]) - tm) < abs(hh)/2:
            Qmid[tm] = Q.clone()
Qn = Q.cpu().numpy(); ths = np.degrees(the.cpu().numpy())
s = 1 - 2*m1*(1 - np.exp(-Qn))
def at(deg, arr=Qn):
    return round(float(arr[int(np.argmin(np.abs(ths - deg)))]), 4)
out = dict(state=fn.split('/')[-1], nt=nt, m1=round(m1, 6), ne=ne, tstop=tstop, nstep=nstep,
           Q_range=[round(float(Qn.min()), 4), round(float(Qn.max()), 4)], deg_at_Qmax=round(float(ths[np.argmax(Qn)]), 2),
           deg_at_Qmin=round(float(ths[np.argmin(Qn)]), 2), s_t_range=[round(float(s.min()), 4), round(float(s.max()), 4)],
           eQ_min=round(float(np.exp(-Qn.max())), 5))
degs = (0, 15, 30, 45, 60, 75, 80, 85, 88, 89, 89.5, 90.5, 91, 92, 95, 100, 120, 150, 180, 210, 240, 255, 260, 265, 268, 269,
        269.5, 270.5, 271, 272, 275, 280, 285, 300, 330)
out['Q_at_deg'] = {('%g' % dg): at(dg) for dg in degs}
out['Q_partial_to_t'] = {('%g' % tm): {('%g' % dg): at(dg, Qm.cpu().numpy()) for dg in (0, 45, 89, 135, 180, 225, 269, 315)}
                         for tm, Qm in Qmid.items()}
print(json.dumps(out), flush=True)
np.savez(fn.replace('.npz', '_qprof.npz'), the=the.cpu().numpy(), Q=Qn, m1=m1, tstop=tstop)
