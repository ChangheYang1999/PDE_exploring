"""V76b: fixed points of the semi-Lagrangian pseudo-time scheme at FROZEN velocity, for two interpolation kernels, on the
uniform (lr, th) grid of a state file (g, lr, th, x, p). Velocity: mine (code/fwdstat.py) of the given state, computed once.
Step (as in tests/v76_interp.py): g <- exp(-ds + p (t_f - t)) I[g](t_f, th_f), foot = Phi_ds(X) by RK4, I = (a) local tensor
cubic Lagrange (stencil i-1..i+2), (b) interpolating cubic B-spline (coefficients by the (1, 4, 1) / 6 system: FFT in th, dense
inverse in lr with 12 pad rows each side). Inflow rows above lr_max: g = A(th). Iterated from the given state for nstep steps.
Then m1 of each fixed point by my moment (F.node) after import to my grid, and log(g_L / g_B) by region.
Since alpha > 0 the feet move outward and the scheme converges in finite pseudo-time (max exit time about 15 here).
Usage: python3 tests/v76_fixedpt.py STATE.npz [ds] [nstep] [out.npz]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64; dev = 'cuda'
fn = sys.argv[1]; ds = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02; nstep = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
fout = sys.argv[4] if len(sys.argv) > 4 else None
d = np.load(fn, allow_pickle=True)
g0, lr0, th0, p = d['g'], d['lr'], d['th'], float(d['p']); x = d['x']
Nr, Nth = g0.shape; dlr = lr0[1] - lr0[0]; dth = 2*math.pi/Nth
K = len(x); jj = np.arange(1, K + 1)
ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*th0[None, :]), np.cos(jj[:, None]*th0[None, :]))
Ath = np.cos(th0)**2*np.exp(x @ ph)
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=10, ppu=3, q=8, nt=Nth, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr)
def to_mine(g):
    G = CubicSpline(lr0, g, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    return torch.tensor(rr[:, None]**p*G, dtype=DT, device=dev)
def m1_of(g):
    return float(F.node(to_mine(g))['m1'])
al, be, _, _ = F.fields(to_mine(g0)); au = F.Imat @ al; bu = F.Imat @ be
T0 = torch.tensor(np.repeat(lr0, Nth), dtype=DT, device=dev); H0 = torch.tensor(np.tile(th0, Nr), dtype=DT, device=dev)
rhs = lambda t, h: (F.interp(au, t, h), F.interp(bu, t, h))
k1 = rhs(T0, H0); k2 = rhs(T0 + 0.5*ds*k1[0], H0 + 0.5*ds*k1[1]); k3 = rhs(T0 + 0.5*ds*k2[0], H0 + 0.5*ds*k2[1])
k4 = rhs(T0 + ds*k3[0], H0 + ds*k3[1])
Tf = T0 + ds/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); Hf = H0 + ds/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
fac = torch.exp(-ds + p*(Tf - T0))
NP = 12; Np = Nr + 2*NP
ci = (Tf - float(lr0[0]))/dlr + NP; cj = torch.remainder(Hf, 2*math.pi)/dth
i0 = torch.clamp(torch.floor(ci).long(), 1, Np - 3); u = ci - i0
j0 = torch.floor(cj).long(); v = cj - j0
top = torch.tensor(np.array([Ath]*NP), dtype=DT, device=dev)
def pad(g):
    return torch.cat([g[:1].expand(NP, -1), g, top], 0)
def gather(Gp, wi, wj):
    out = torch.zeros_like(u)
    for a in range(4):
        ii = i0 - 1 + a
        for b in range(4):
            out = out + wi[a]*wj[b]*Gp[ii, torch.remainder(j0 - 1 + b, Nth)]
    return out
lw = lambda s: [-s*(s - 1)*(s - 2)/6, (s + 1)*(s - 1)*(s - 2)/2, -(s + 1)*s*(s - 2)/2, (s + 1)*s*(s - 1)/6]
bw = lambda s: [(1 - s)**3/6, (3*s**3 - 6*s**2 + 4)/6, (-3*s**3 + 3*s**2 + 3*s + 1)/6, s**3/6]
wiL, wjL, wiB, wjB = lw(u), lw(v), bw(u), bw(v)
Tri = (np.diag(4*np.ones(Np)) + np.diag(np.ones(Np - 1), 1) + np.diag(np.ones(Np - 1), -1))/6
Sinv = torch.tensor(np.linalg.inv(Tri), dtype=DT, device=dev)
kk = np.fft.fftfreq(Nth, 1.0/Nth)
sym = torch.tensor((4 + 2*np.cos(2*math.pi*kk/Nth))/6, dtype=DT, device=dev)
def coef(Gp):
    c = torch.real(torch.fft.ifft(torch.fft.fft(Gp, dim=1)/sym, dim=1))
    return Sinv @ c
def step(g, kind):
    Gp = pad(g)
    val = gather(Gp, wiL, wjL) if kind == 'lag' else gather(coef(Gp), wiB, wjB)
    return (fac*val).reshape(Nr, Nth)
res = dict(state=fn.split('/')[-1], p=p, ds=ds, nstep=nstep, min_alpha=float(al.min()), m1_start=round(m1_of(g0), 5))
G0 = torch.tensor(g0, dtype=DT, device=dev)
fp = {}
for kind in ('bspline', 'lag'):
    g = G0.clone(); hist = []
    for n in range(nstep):
        gn = step(g, kind)
        if (n + 1) % 250 == 0 or n == 0:
            dlt = float(((gn - g).abs()/(g.abs().amax(1, keepdim=True))).max())
            hist.append([n + 1, float('%.3g' % (dlt/ds)), round(m1_of(gn.cpu().numpy()), 5)])
        g = gn
    fp[kind] = g.cpu().numpy()
    res[kind] = dict(hist=hist, m1=round(m1_of(fp[kind]), 5))
deg = np.degrees(th0)
with np.errstate(divide='ignore', invalid='ignore'):
    lq = np.log(fp['lag']/fp['bspline']); l0 = np.log(fp['bspline']/g0)
ok = g0 > 1e-3*np.abs(g0).max(1, keepdims=True)
reg = {}
for lo, hi in ((-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 9)):
    mi = (lr0 >= lo) & (lr0 < hi)
    for nm, (a_, b_) in (('upper_zero 86-94', (86, 94)), ('x-axis 0-10', (0, 10)), ('bulk 10-80', (10, 80)), ('lower 190-350', (190, 350))):
        mj = ((deg >= a_) & (deg <= b_)) | ((deg >= 360 - b_) & (deg <= 360 - a_)) if a_ == 0 else (deg >= a_) & (deg <= b_)
        m = np.ix_(mi, mj); z = np.where(ok[m], lq[m], 0.0); z0 = np.where(ok[m], l0[m], 0.0)
        reg['%g..%g %s' % (lo, hi, nm)] = [float('%.3g' % np.abs(z).max()), float('%.3g' % np.abs(z0).max())]
res['max|log(g_lag/g_bspline)|, max|log(g_bspline/g_state)| (g > 1e-3 ring max)'] = reg
if fout:
    np.savez(fout, g_lag=fp['lag'], g_bspline=fp['bspline'], lr=lr0, th=th0, p=p, x=x)
print(json.dumps(res, indent=1), flush=True)
