"""V85: angular profile of the exact-T mismatch log(T rho / rho) near the weak axis (th = 0 and 180 deg) on a few rings of an
imported lead/numerics-format state (g, lr, th, x with p last), as in tests/v80_xT.py (my velocity, arclength orbits). For each
printed point: deg, g / ring max, log(T rho / rho), the exit angle of its orbit (deg) and the exit time s; and the same mismatch
for T computed at half the arclength step (hs / 2), to separate tracer error from the state.
Usage: python3 tests/v85_xTprof.py STATE.npz [nt] [tmin (-14)] [hs (0.03)]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g0, lr0, th0 = d['g'], d['lr'], d['th']; X = d['x'] if 'x' in d.files else d['X']
p = float(X[-1]); par = np.array(X[:-1], dtype=float)
nt = int(sys.argv[2]) if len(sys.argv) > 2 else len(th0); tmin = float(sys.argv[3]) if len(sys.argv) > 3 else -14.0
hs = float(sys.argv[4]) if len(sys.argv) > 4 else 0.03
jj = np.arange(1, len(par) + 1)
def A(t):
    ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*t[None, :]), np.cos(jj[:, None]*t[None, :]))
    return np.cos(t)**2*np.exp(par @ ph)
F = FwdStat(p, A, tmin=tmin, tmax=10, ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy(); deg = np.degrees(thn)
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    G = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([G, G[:, :1]], 1), axis=1, bc_type='periodic')(thn)
G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
al, be, _, _ = F.fields(rho)
t0 = F.t_nodes[:, None].expand_as(F.R).reshape(-1); h0 = F.TH.reshape(-1)
res = {}
for h in (hs, hs/2):
    the, s, nbad = F.trace_s(al, be, t0, h0, h, 16000)
    Ae = torch.tensor(A(the.cpu().numpy()), dtype=DT, device='cuda')
    Tr = (torch.exp(-s)*F.L**p*Ae).reshape(F.R.shape)
    res[h] = (Tr.cpu().numpy(), np.degrees(the.cpu().numpy()).reshape(F.R.shape) % 360, s.cpu().numpy().reshape(F.R.shape), nbad)
gg = rho.cpu().numpy(); rm = np.abs(gg).max(1)
print('state', fn.split('/')[-1], 'p', p, 'nt', nt, 'm1', round(F.node(rho)['m1'], 6), 'not exited', res[hs][3], res[hs/2][3])
sel = [j for j in range(nt) if deg[j] <= 26 or 154 <= deg[j] <= 206 or deg[j] >= 334]
for lv in (-8.5, -9.0, -9.5, -10.0, -11.0):
    i = int(np.argmin(np.abs(lrr - lv)))
    print('ring lr %.3f  ring max %.3g' % (lrr[i], rm[i]))
    print('   deg    g/max     log(T/rho)  log(T/rho) hs/2   exit deg   s')
    for j in sel[::2]:
        with np.errstate(divide='ignore', invalid='ignore'):
            l1 = math.log(abs(res[hs][0][i, j]/gg[i, j])) if gg[i, j] != 0 else float('nan')
            l2 = math.log(abs(res[hs/2][0][i, j]/gg[i, j])) if gg[i, j] != 0 else float('nan')
        print('%7.2f  %8.2e  %10.4f  %10.4f  %10.2f  %8.3f' % (deg[j], gg[i, j]/rm[i], l1, l2, res[hs][1][i, j], res[hs][2][i, j]))
