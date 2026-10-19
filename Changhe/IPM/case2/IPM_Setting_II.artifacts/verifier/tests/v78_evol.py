"""V78: semi-Lagrangian pseudo-time evolution WITH velocity updates (own code; the numerical researcher's forward evolution is the
object being checked, none of its code is used). State on the uniform grid lr = -14..10 (dlr 1/30), Nth angles, g = rho / r^p.
Step: g <- exp(-ds + p (t_f - t)) I[g](t_f, th_f), foot = Phi_ds(X) by RK4 with my velocity (code/fwdstat.py) of the current
state, recomputed every nv steps; I = interpolating cubic B-spline (as tests/v76_fixedpt.py: (1, 4, 1) / 6 prefilter, FFT in th,
dense inverse in lr, 12 pad rows, inflow rows g = A above lr_max, replicated rows below lr_min) or local cubic Lagrange.
Stationary points: V.grad rho = rho, the same as the exit-map fixed points of code/fwdstat.py.
key=value arguments: init (own format rho, r, th, p, args; or g, lr, th with x or X), x (colon list, overrides), p (overrides),
nth (re-interpolate to nth angles), ds (0.02), nstep (1500), nv (1), kind (bspline | lag), clip (1: hull clip to the 4 surrounding grid values), rep (100), out (npz, g format), tcheck (1: exact exit-map defect of the
start and of the end state, smode arclength orbits, after import to my grid), tmin (-14), mand (0: none; else my Anderson
solver polish is NOT run here).
Printed: per rep steps s, max|dg/ds| / ring max (rings with ring max > 1e-12), my m1, min alpha; at the end max|log(g_end /
g_start)| by region (g > 1e-3 ring max)."""
import sys, math, json, time, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64; dev = 'cuda'
a = dict(init='', x='', p='', ds='0.02', nstep='1500', nv='1', kind='bspline', clip='0', rep='100', out='', tcheck='0', tmin='-14')
for s_ in sys.argv[1:]:
    k, v = s_.split('=', 1); a[k] = v
d = np.load(a['init'], allow_pickle=True)
lr0 = np.linspace(-14.0, 10.0, 721); dlr = lr0[1] - lr0[0]
if 'rho' in d.files:
    p = float(d['p']); th0 = d['th']; r_ = d['r']
    x = np.array([float(v) for v in json.loads(str(d['args']))['par'].split(':')])
    g0 = CubicSpline(np.log(r_), d['rho']/r_[:, None]**p, axis=0)(lr0)
else:
    th0 = d['th']
    x = d['x'] if 'x' in d.files else d['X'][:-1]
    p = float(d['p']) if 'p' in d.files else float(d['X'][-1])
    g0 = CubicSpline(d['lr'], d['g'], axis=0)(np.clip(lr0, d['lr'][0], d['lr'][-1]))
if a.get('nth') and int(a['nth']) != len(th0):          # periodic cubic re-interpolation in th
    thn = 2*math.pi/int(a['nth'])*np.arange(int(a['nth']))
    g0 = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([g0, g0[:, :1]], 1), axis=1, bc_type='periodic')(thn)
    th0 = thn
if a['x']: x = np.array([float(v) for v in a['x'].split(':')])
if a['p']: p = float(a['p'])
Nr, Nth = g0.shape; dth = 2*math.pi/Nth
assert np.allclose(th0, dth*np.arange(Nth))
ds = float(a['ds']); nstep = int(a['nstep']); nv = int(a['nv']); rep = int(a['rep'])
K = len(x); jj = np.arange(1, K + 1)
def Afun(t):
    ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*t[None, :]), np.cos(jj[:, None]*t[None, :]))
    return np.cos(t)**2*np.exp(x @ ph)
F = FwdStat(p, Afun, tmin=float(a['tmin']), tmax=10, ppu=3, q=8, nt=Nth, dti=0.01, nstep=800)
F.smode = True; F.hs = 0.03; F.nmax = 6000
rr = F.r.cpu().numpy(); lrr = np.log(rr)
M = CubicSpline(lr0, np.eye(Nr), axis=0)(np.clip(lrr, lr0[0], lr0[-1])); M[lrr < lr0[0]] = 0.0
Mt = torch.tensor(M, dtype=DT, device=dev); Rp = F.R**p
def to_mine(g):
    return Rp*(Mt @ g)
def m1_of(g):
    return float(F.node(to_mine(g))['m1'])
T0 = torch.tensor(np.repeat(lr0, Nth), dtype=DT, device=dev); H0 = torch.tensor(np.tile(th0, Nr), dtype=DT, device=dev)
NP = 12; Np = Nr + 2*NP
top = torch.tensor(np.array([Afun(th0)]*NP), dtype=DT, device=dev)
Tri = (np.diag(4*np.ones(Np)) + np.diag(np.ones(Np - 1), 1) + np.diag(np.ones(Np - 1), -1))/6
Sinv = torch.tensor(np.linalg.inv(Tri), dtype=DT, device=dev)
kk = np.fft.fftfreq(Nth, 1.0/Nth)
sym = torch.tensor((4 + 2*np.cos(2*math.pi*kk/Nth))/6, dtype=DT, device=dev)
lw = lambda s: [-s*(s - 1)*(s - 2)/6, (s + 1)*(s - 1)*(s - 2)/2, -(s + 1)*s*(s - 2)/2, (s + 1)*s*(s - 1)/6]
bw = lambda s: [(1 - s)**3/6, (3*s**3 - 6*s**2 + 4)/6, (-3*s**3 + 3*s**2 + 3*s + 1)/6, s**3/6]
def feet(g):
    al, be, _, _ = F.fields(to_mine(g)); au = F.Imat @ al; bu = F.Imat @ be
    rhs = lambda t, h: (F.interp(au, t, h), F.interp(bu, t, h))
    k1 = rhs(T0, H0); k2 = rhs(T0 + 0.5*ds*k1[0], H0 + 0.5*ds*k1[1]); k3 = rhs(T0 + 0.5*ds*k2[0], H0 + 0.5*ds*k2[1])
    k4 = rhs(T0 + ds*k3[0], H0 + ds*k3[1])
    Tf = T0 + ds/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); Hf = H0 + ds/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    fac = torch.exp(-ds + p*(Tf - T0))
    ci = (Tf - float(lr0[0]))/dlr + NP; cj = torch.remainder(Hf, 2*math.pi)/dth
    i0 = torch.clamp(torch.floor(ci).long(), 1, Np - 3); u = ci - i0
    j0 = torch.floor(cj).long(); v = cj - j0
    w = (lw(u), lw(v)) if a['kind'] == 'lag' else (bw(u), bw(v))
    return dict(i0=i0, j0=j0, wi=w[0], wj=w[1], fac=fac, minal=float(al.min()))
def step(g, ft):
    G0p = torch.cat([g[:1].expand(NP, -1), g, top], 0); Gp = G0p
    if a['kind'] != 'lag':
        Gp = Sinv @ torch.real(torch.fft.ifft(torch.fft.fft(G0p, dim=1)/sym, dim=1))
    out = torch.zeros_like(ft['fac'])
    for ia in range(4):
        ii = ft['i0'] - 1 + ia
        for ib in range(4):
            out = out + ft['wi'][ia]*ft['wj'][ib]*Gp[ii, torch.remainder(ft['j0'] - 1 + ib, Nth)]
    if a['clip'] == '1':                       # clip to the hull of the 4 surrounding grid values of g
        i0, j0 = ft['i0'], ft['j0']; j1 = torch.remainder(j0 + 1, Nth); j0m = torch.remainder(j0, Nth)
        c4 = torch.stack([G0p[i0, j0m], G0p[i0, j1], G0p[i0 + 1, j0m], G0p[i0 + 1, j1]])
        out = torch.minimum(torch.maximum(out, c4.min(0).values), c4.max(0).values)
    return (ft['fac']*out).reshape(Nr, Nth)
def tdefect(g):
    rho = to_mine(g); Tr, info = F.T(rho)
    return float(((Tr - rho)/Rp).abs().max())
t0 = time.time()
G0 = torch.tensor(g0, dtype=DT, device=dev); g = G0.clone()
res = dict(args=a, p=p, x=x.tolist(), Nth=Nth, m1_start=round(m1_of(g), 6))
if a['tcheck'] == '1': res['Tdefect_start'] = float('%.3g' % tdefect(g))
print(json.dumps(res), flush=True)
ft = None
for n in range(nstep):
    if n % nv == 0: ft = feet(g)
    gn = step(g, ft)
    if (n + 1) % rep == 0 or n == 0:
        rm = g.abs().amax(1, keepdim=True); ok = (rm > 1e-12).expand_as(g)
        zz = torch.where(ok, (gn - g).abs()/rm, torch.zeros_like(g)); dlt = float(zz.max())
        ia_, ib_ = np.unravel_index(int(torch.argmax(zz)), zz.shape)
        print(json.dumps(dict(n=n + 1, s=round((n + 1)*ds, 3), dgds=float('%.3g' % (dlt/ds)), m1=round(m1_of(gn), 6),
                              at=[round(float(lr0[ia_]), 2), round(float(np.degrees(th0[ib_])), 1),
                                  float('%.2g' % float(g[ia_, ib_]/rm[ia_, 0]))],
                              minal=round(ft['minal'], 4), wall=round(time.time() - t0, 1))), flush=True)
    g = gn
    if not torch.isfinite(g).all():
        print(json.dumps(dict(n=n + 1, msg='non-finite')), flush=True); break
ge = g.cpu().numpy()
deg = np.degrees(th0)
with np.errstate(divide='ignore', invalid='ignore'):
    l0 = np.log(ge/g0)
okm = g0 > 1e-3*np.abs(g0).max(1, keepdims=True)
reg = {}
for lo, hi in ((-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 9)):
    mi = (lr0 >= lo) & (lr0 < hi)
    for nm, (a_, b_) in (('upper 80-100', (80, 100)), ('lower 260-280', (260, 280)), ('rest', (0, 360))):
        mj = (deg >= a_) & (deg <= b_)
        if nm == 'rest': mj = ~(((deg >= 80) & (deg <= 100)) | ((deg >= 260) & (deg <= 280)))
        m = np.ix_(mi, mj); z0 = np.where(okm[m] & np.isfinite(l0[m]), l0[m], 0.0)
        reg['%g..%g %s' % (lo, hi, nm)] = float('%.3g' % np.abs(z0).max())
fin = dict(m1_end=round(m1_of(g), 6), max_abs_log_gend_over_gstart=reg, wall=round(time.time() - t0, 1))
if a['tcheck'] == '1': fin['Tdefect_end'] = float('%.3g' % tdefect(g))
if a['out']:
    np.savez(a['out'], g=ge, lr=lr0, th=th0, p=p, x=x)
print(json.dumps(fin, indent=1), flush=True)
