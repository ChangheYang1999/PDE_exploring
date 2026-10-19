"""V76 (lead team notes 06:47Z item 6): one semi-Lagrangian pseudo-time step on a stationary state (g, lr, th format, uniform
lr and th grids) with the SAME feet, the foot values interpolated by (a) a local tensor cubic Lagrange interpolant (4 x 4
stencil i-1..i+2, j-1..j+2), with and without a clip to the hull of the 4 surrounding grid values, and (b) the prefiltered cubic
B-spline (scipy map_coordinates order 3, periodic pad in th). Written independently of the other two roles' code.
Step: the stationary law is rho(Phi_s X) = e^s rho(X), so g_new(X) = exp(-ds + p (t_f - t)) g(t_f, th_f) with the foot
(t_f, th_f) = Phi_ds(X), dt/ds = alpha = V_r / r, dth/ds = beta = V_th / r (RK4; my velocity, code/fwdstat.py, on the state
imported to my grid). The exact stationary state has g_new = g for every kernel; the printed rate (g_new - g) / (ds g) is the
drift of log g per unit pseudo-time caused by the kernel (plus the common velocity / foot error, the same for all kernels).
Usage: python3 tests/v76_interp.py STATE.npz [ds] [tmin]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
from scipy.ndimage import map_coordinates
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; ds = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02; tmin = float(sys.argv[3]) if len(sys.argv) > 3 else -14.0
d = np.load(fn, allow_pickle=True)
g0, lr0, th0, p = d['g'], d['lr'], d['th'], float(d['p']); x = d['x']
Nr, Nth = g0.shape; dlr = lr0[1] - lr0[0]; dth = 2*math.pi/Nth
assert np.allclose(np.diff(lr0), dlr) and np.allclose(th0, dth*np.arange(Nth))
K = len(x); jj = np.arange(1, K + 1)
def A(th):
    ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*th[None, :]), np.cos(jj[:, None]*th[None, :]))
    return np.cos(th)**2*np.exp(x @ ph)
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=10, ppu=3, q=8, nt=Nth, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
assert np.allclose(thn, th0)
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
al, be, _, _ = F.fields(rho)
au = F.Imat @ al; bu = F.Imat @ be
T0 = torch.tensor(np.repeat(lr0, Nth), dtype=DT, device='cuda'); H0 = torch.tensor(np.tile(th0, Nr), dtype=DT, device='cuda')
def rhs(t, h):
    return F.interp(au, t, h), F.interp(bu, t, h)
k1 = rhs(T0, H0); k2 = rhs(T0 + 0.5*ds*k1[0], H0 + 0.5*ds*k1[1]); k3 = rhs(T0 + 0.5*ds*k2[0], H0 + 0.5*ds*k2[1])
k4 = rhs(T0 + ds*k3[0], H0 + ds*k3[1])
Tf = (T0 + ds/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])).cpu().numpy().reshape(Nr, Nth)
Hf = (H0 + ds/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])).cpu().numpy().reshape(Nr, Nth)
fac = np.exp(-ds + p*(Tf - lr0[:, None]))
# padded grid: 4 inflow rows above lr_max with g = A (far field g -> A), 4 replicated rows below, periodic pad PD in th
PD = 24; NU = 4
top = np.array([A(th0)]*NU); bot = np.array([g0[0]]*NU)
gp = np.concatenate([bot, g0, top], 0); gp = np.concatenate([gp[:, -PD:], gp, gp[:, :PD]], 1)
ci = (Tf - lr0[0])/dlr + NU; cj = np.mod(Hf, 2*math.pi)/dth + PD
def lag_w(u):
    return [-u*(u - 1)*(u - 2)/6, (u + 1)*(u - 1)*(u - 2)/2, -(u + 1)*u*(u - 2)/2, (u + 1)*u*(u - 1)/6]
i0 = np.clip(np.floor(ci).astype(int), 1, gp.shape[0] - 3); u = ci - i0
j0 = np.floor(cj).astype(int); v = cj - j0
wi = lag_w(u); wj = lag_w(v)
lag = np.zeros_like(u)
for a in range(4):
    for b in range(4):
        lag += wi[a]*wj[b]*gp[i0 - 1 + a, j0 - 1 + b]
c4 = [gp[i0, j0], gp[i0, j0 + 1], gp[i0 + 1, j0], gp[i0 + 1, j0 + 1]]
lo, hi = np.minimum.reduce(c4), np.maximum.reduce(c4)
lagc = np.clip(lag, lo, hi)
bsp = map_coordinates(gp, [ci, cj], order=3, mode='nearest')
bspc = np.clip(bsp, lo, hi)
res = {}
with np.errstate(divide='ignore', invalid='ignore'):
    rate = {k: (fac*v_ - g0)/(ds*g0) for k, v_ in (('lag', lag), ('lag_clip', lagc), ('bspline', bsp), ('bspline_clip', bspc))}
deg = np.degrees(th0)
def pick(lrv, dg):
    i = int(np.argmin(np.abs(lr0 - lrv))); j = int(np.argmin(np.abs(deg - dg)))
    return {k: float('%.3g' % rate[k][i, j]) for k in rate} | dict(lr=round(float(lr0[i]), 3), deg=round(float(deg[j]), 2),
                                                                     g=float('%.3g' % g0[i, j]))
pts = [(-13.6, 2.8), (-11.9, 4.9), (-10, 19), (-4.0, 89.3), (-3.3, 89.3), (-4.0, 90.7), (-3.3, 90.7), (-6, 45), (0, 30), (3, 89.3)]
res['points'] = [pick(*q) for q in pts]
gfloor = 1e-3*np.abs(g0).max(1, keepdims=True)      # points with g below 1e-3 of the ring max are excluded (rate ~ 1/g)
def win(lo_, hi_, dlo, dhi, how='meanabs'):
    mi = (lr0 >= lo_) & (lr0 <= hi_); mj = (deg >= dlo) & (deg <= dhi)
    out = {}
    ok = (g0 > gfloor)[np.ix_(mi, mj)]
    for k in rate:
        z = np.abs(rate[k][np.ix_(mi, mj)]); z = np.where(ok & np.isfinite(z), z, 0.0)
        if how == 'meanabs':
            out[k] = float('%.3g' % (z.sum()/max(ok.sum(), 1)))
        else:
            a, b = np.unravel_index(np.argmax(z), z.shape)
            out[k] = [float('%.3g' % z[a, b]), round(float(lr0[mi][a]), 2), round(float(deg[mj][b]), 2),
                      float('%.2g' % (g0[np.ix_(mi, mj)][a, b]/np.abs(g0[mi][a]).max()))]
    return out
res['note'] = 'max entries: [rate, lr, deg, g / ring max]; points with g < 1e-3 ring max excluded'
res['mean|rate| |th-90|<2, lr -6..0'] = win(-6, 0, 88, 92)
res['max|rate| |th-90|<2, lr -6..0'] = win(-6, 0, 88, 92, 'max')
res['max|rate| |th-90|<2, lr -4.2..-3'] = win(-4.2, -3, 88, 92, 'max')
res['max|rate| lower 210-330, lr -12..9'] = win(-12, 9, 210, 330, 'max')
res['max|rate| upper 10-80, lr -12..9'] = win(-12, 9, 10, 80, 'max')
res['max|rate| lr -14..-10 all th'] = win(-13.9, -10, 0, 360, 'max')
res['max|lag-bspline|/ringmax'] = float('%.3g' % (np.abs(lag - bsp)/np.abs(g0).max(1, keepdims=True))[lr0 <= 9].max())
res['min_alpha'] = float(al.min())
print(json.dumps(dict(state=fn.split('/')[-1], p=p, Nr=Nr, Nth=Nth, ds=ds, tmin=tmin, **res), indent=1))
