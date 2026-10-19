"""V108b (notes of the lead analyst 10:25Z on V102b): is the x-odd DT eigenvector u near 1 an infinitesimal symmetry of the state rho*?
Compares the saved Ritz vector u (tests/v108_xodd_mode.py) with the two x-odd generators applied to the x-even rho*:
  g_x  = d_x rho*   = (cos th d_t rho* - sin th d_th rho*)/r     (x-translation)
  g_th = d_th rho*  = (x d_y - y d_x) rho*                        (rotation)
d_t by exact differentiation of the per-panel interpolant (degree 7 in t on each t-panel, degree i0-1 in r on the core panel
r < e^tmin, d_t = r d_r there); d_th by periodic fourth-order differences (the FFT derivative has Gibbs oscillation at the
angular layers next to the zero, V98). Inner products: (1) the Arnoldi one, sum f g / r^(2p) over the nodes; (2) the same with
the radial Gauss weights in dt. Reports the cosines cos(u, g_x), cos(u, g_th), cos(g_x, g_th), the fraction of |u|^2 in
span{g_x, g_th}, and the fractions of |g|^2 by t band, as for u. CPU, numpy only.
Usage: python3 tests/v108b_overlap.py MODE.npz [STATE.npz]   (the state defaults to args.source of the mode file)"""
import sys, json, math, numpy as np
mo = np.load(sys.argv[1], allow_pickle=True); margs = json.loads(str(mo['args']))
sfn = sys.argv[2] if len(sys.argv) > 2 else margs['source']
d = np.load(sfn, allow_pickle=True); a = json.loads(str(d['args'])); p = float(d['p'])
r = d['r']; th = d['th']; rho = d['rho']; nt = len(th); u = mo['u']
assert np.allclose(r, mo['r']) and np.allclose(th, mo['th']) and u.shape == rho.shape
tmin = float(a.get('tmin', -14)); tmax = float(a.get('tmax', 10)); ppu = int(a.get('ppu', 3)); q = 8
t = np.log(r); i0 = int(np.sum(t < tmin - 1e-12)); npan = int(round((tmax - tmin)*ppu))
assert len(t) == i0 + q*npan, (len(t), i0, npan)
P = np.polynomial.polynomial
edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, npan + 1))])
assert i0 == q, i0
xg, wg = np.polynomial.legendre.leggauss(q)
def dt_of(f):
    out = np.zeros_like(f)
    for k in range(npan + 1):
        sl = slice(q*k, q*(k + 1)); a0, b0 = edges[k], edges[k + 1]
        s = 2*(r[sl] - a0)/(b0 - a0) - 1
        assert np.allclose(s, xg, atol=1e-7), ('panel nodes are not Gauss in r', k)
        C = P.polyfit(s, f[sl], q - 1); out[sl] = (r[sl]*(2/(b0 - a0)))[:, None]*P.polyval(s, P.polyder(C)).T
    return out
wt = np.concatenate([wg*(edges[k + 1] - edges[k])/2/r[q*k: q*(k + 1)] for k in range(npan + 1)])
dt = dt_of(rho)
hth = 2*math.pi/nt
dth = (8*(np.roll(rho, -1, 1) - np.roll(rho, 1, 1)) - (np.roll(rho, -2, 1) - np.roll(rho, 2, 1)))/(12*hth)
C_, S_ = np.cos(th)[None, :], np.sin(th)[None, :]
gx = (C_*dt - S_*dth)/r[:, None]; gth = dth
xi = (nt//2 - np.arange(nt)) % nt
oddness = lambda f: float(np.abs(f + f[:, xi]).max()/np.abs(f).max())
out = dict(mode=sys.argv[1].split('/')[-1], state=sfn.split('/')[-1], lam=float(mo['lam']), p=p,
           oddness=dict(u=float('%.2g' % oddness(u)), gx=float('%.2g' % oddness(gx)), gth=float('%.2g' % oddness(gth))))
# check of d_t on r^p cos^2 (exact derivative p r^p cos^2) and on r^2 cos^2, outside the core panel
for nm, ex, tst in (('rp', p, r[:, None]**p*np.cos(th)[None, :]**2), ('r2', 2.0, r[:, None]**2*np.cos(th)[None, :]**2)):
    e = dt_of(tst)
    out['dt_check_rel_err_' + nm] = float('%.2g' % (np.abs(e[q:] - ex*tst[q:]).max()/np.abs(ex*tst[q:]).max()))
Rp2 = r[:, None]**(2*p)
for lab, W in (('ip_nodes', np.ones_like(r)), ('ip_dt_weights', wt)):
    ip = lambda f, g: float((W[:, None]*f*g/Rp2).sum())
    nu, nx, nth = [math.sqrt(ip(f, f)) for f in (u, gx, gth)]
    G = np.array([[ip(gx, gx), ip(gx, gth)], [ip(gth, gx), ip(gth, gth)]]); bvec = np.array([ip(gx, u), ip(gth, u)])
    co = np.linalg.solve(G, bvec); proj = float(co @ bvec)
    out[lab] = dict(cos_u_gx=round(ip(u, gx)/(nu*nx), 4), cos_u_gth=round(ip(u, gth)/(nu*nth), 4),
                    cos_gx_gth=round(ip(gx, gth)/(nx*nth), 4), frac_u_in_span=round(proj/nu**2, 4))
bands = [(-30, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 11)]
for lab, f in (('u', u), ('gx', gx), ('gth', gth)):
    U = f**2/Rp2; tot = U.sum()
    out['band_frac_' + lab] = {'%g..%g' % (a_, b_): round(float(U[(t >= a_) & (t < b_)].sum()/tot), 4) for a_, b_ in bands}
    A = np.abs(f)/np.sqrt(Rp2); ii, jj = np.unravel_index(np.argmax(A), A.shape)
    out['argmax_' + lab] = [round(float(t[ii]), 2), round(float(np.degrees(th[jj])), 2)]
# band-restricted cosines (Arnoldi inner product) where u lives
bc = {}
for a_, b_ in bands:
    m = ((t >= a_) & (t < b_))[:, None]
    ipb = lambda f, g: float((m*f*g/Rp2).sum())
    nu = math.sqrt(ipb(u, u)); nx = math.sqrt(ipb(gx, gx)); nth = math.sqrt(ipb(gth, gth))
    bc['%g..%g' % (a_, b_)] = [round(ipb(u, gx)/(nu*nx), 3), round(ipb(u, gth)/(nu*nth), 3)]
out['band_cos_u_gx_gth'] = bc
print('OVERLAP ' + json.dumps(out), flush=True)
