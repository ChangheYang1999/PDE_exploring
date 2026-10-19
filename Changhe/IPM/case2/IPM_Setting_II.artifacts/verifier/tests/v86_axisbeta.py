"""V86: angular velocity on the weak axis near the node of an imported lead/numerics-format state (g, lr, th, x with p last) or
an own-format state (rho, r, th, p, args), with my velocity (code/fwdstat.py). On the x-axis (th = 0) beta = V_th / r = V_2 / x.
For the linear part diag(m1, m2) beta(t, 0) = 0; a quadratic term V_2(x, 0) = -k x^2 gives beta = -k r and an invariant
curve y = kappa x^2 with kappa = k / (m2 - 2 m1) through the node, i.e. at angle th ~ kappa r from the axis.
Printed per ring: t, alpha(0), beta(0), beta(180), -beta(0) / r, kappa = -beta(0) / r / (m2 - 2 m1), kappa r (rad, deg).
Usage: python3 tests/v86_axisbeta.py STATE.npz [nt] [dev (cuda | cpu)]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
dev = sys.argv[3] if len(sys.argv) > 3 else 'cuda'
if 'rho' in d.files:
    args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
                dti=0.01, nstep=800, dev=dev)
    rho = torch.tensor(d['rho'], dtype=torch.float64, device=dev)
else:
    g0, lr0, th0 = d['g'], d['lr'], d['th']; X = d['x'] if 'x' in d.files else d['X']; p = float(X[-1])
    nt = int(sys.argv[2]) if len(sys.argv) > 2 else len(th0)
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=-14.0, tmax=10, ppu=3, q=8, nt=nt, dti=0.01, nstep=800, dev=dev)
    rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn) or not np.allclose(th0, thn):
        G = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([G, G[:, :1]], 1), axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device=dev)
nd = F.node(rho); m1, m2 = nd['m1'], nd['m2']
al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy()
r = F.r.cpu().numpy(); t = np.log(r); j0 = 0; j180 = nt//2
print('state', fn.split('/')[-1], 'p', p, 'nt', nt, 'm1', round(m1, 6), 'm2', round(m2, 4), 'm2 - 2 m1', round(m2 - 2*m1, 4))
print('    t     alpha(0)   beta(0)    beta(180)   -beta(0)/r    kappa      kappa r (deg)')
for tt in np.arange(-13.5, -2.9, 0.5):
    i = int(np.argmin(np.abs(t - tt))); k = -be[i, j0]/r[i]; ka = k/(m2 - 2*m1)
    print('%6.2f  %9.5f  %10.3e  %10.3e  %11.4g  %10.4g  %8.3f' % (t[i], al[i, j0], be[i, j0], be[i, j180], k, ka,
                                                                    math.degrees(math.atan(ka*r[i]))))
