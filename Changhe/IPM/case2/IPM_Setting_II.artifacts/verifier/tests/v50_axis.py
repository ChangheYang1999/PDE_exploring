"""V50: own orbit-free y-axis test of an x-even forward state (notes of the lead analyst 01:47Z item 2 asks for it in the candidate protocol;
explore/axcheck.py not used). Own derivation: on x = 0 an x-even state has rho = rho_x = rho_y = 0, V_1 = 0, d_x V_2 = 0, so two
x-derivatives of V.grad rho = rho give b h' = (1 - 2a) h, h = rho_xx(0, y), b = V_2(0, y), a = d_x V_1(0, y) = 2l - b' (div V = 2l);
one x-derivative of V.grad xi = m1 xi gives b k' + (a - m1) k = 0, k = d_x xi(0, y), k(0) = 1 (xi = x + ... at the node). Hence
    b (log h/k^2)' = 1 - 2 m1,   and at m1 = 1/2:  h/k^2 = 2 G(+-inf) on the upper / lower half-axis (rho ~ G xi^2 at the node).
In polar form on the axis: h = r^(p-2) g_thth (g = rho/r^p, rho_r = 0 there), b' = d_r V_r, so with alpha = V_r/r and t = log r:
    a = 2l - alpha - d_t alpha,   d_t log k = (m1 - a)/alpha,   d_t log(h/k^2) = (1 - 2 m1)/alpha.
Far field: g_thth -> 2 exp(F(+-90)) for A = cos^2 exp(F).
Usage: python3 tests/v50_axis.py STATE.npz [GFIX_PROFILE.npz]   (state from tests/fs_run.py; profile from tests/v43_gfix.py)."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]
d = np.load(fn, allow_pickle=True)
args = json.loads(str(d['args']))
p = float(d['p']); r0 = d['r']; th = d['th']; nt = len(th)
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), r0), 'grid mismatch'
assert np.allclose(F.th.cpu().numpy(), th)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); m1 = nd['m1']; l = 1.0/p
alpha, beta, _, _ = F.fields(rho)
g = (rho/F.R**p).cpu().numpy(); al = alpha.cpu().numpy(); be = beta.cpu().numpy()
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0.0                  # Nyquist dropped

def at(f, ths, deriv=0):
    """spectral value (deriv 0) or second angular derivative (deriv 2) of each radial row at angle ths."""
    fh = np.fft.fft(f, axis=1)/nt
    fh[:, nt//2] = 0.0
    fac = np.exp(1j*mm*(ths - th[0]))*((1j*mm)**deriv)
    return np.real(fh @ fac)

Imat = F.Imat.cpu().numpy(); tu = F.tu.cpu().numpy(); dti = F.dti
out = dict(state=fn.split('/')[-1], p=p, m1=round(m1, 6), e1_deg=round(nd['e1_deg'], 4), nt=nt, tmin=tmin, tmax=tmax)
res = {}
for name, ths in (('upper', math.pi/2), ('lower', 3*math.pi/2)):
    a_u = Imat @ at(al, ths); gtt_u = Imat @ at(g, ths, 2); b_u = Imat @ at(be, ths)
    da = np.gradient(a_u, dti)
    a = 2*l - a_u - da
    integrand = (m1 - a)/a_u
    logk = np.concatenate([[0.0], np.cumsum(0.5*(integrand[1:] + integrand[:-1])*dti)])
    with np.errstate(divide='ignore', invalid='ignore'):
        logh = np.log(np.abs(gtt_u)) + (p - 2)*tu
    q = logh - 2*logk                                                   # log h/k^2
    pred_slope = (1 - 2*m1)/a_u
    rows = []
    for tt in (-8, -6, -4, -2, 0, 2, 4, 6, 8, 9.5):
        i = int(round((tt - tmin)/dti))
        rows.append([tt, round(float(q[i]), 4), round(float(np.gradient(q, dti)[i]), 5), round(float(pred_slope[i]), 5),
                     round(float(logk[i]), 4), round(float(gtt_u[i]), 5), round(float(b_u[i]), 6)])
    msk = (tu >= 0) & (tu <= 9.5)                                     # axis layer resolved there (law slope check)
    res[name] = dict(rows_t_logh_over_k2_slope_predslope_logk_gthth_beta=rows,
                     logh_over_k2_range_t_0_9p5=[round(float(q[msk].min()), 4), round(float(q[msk].max()), 4)],
                     far_gthth=round(float(gtt_u[-1]), 5), log_kappa_far=round(float(logk[-1] + (1 - p/2)*tu[-1]), 5),
                     log_G_axis=round(float(np.median(q[msk]) - math.log(2)), 4))
out['axis'] = res
out['log_G_upper_minus_lower'] = round(res['upper']['log_G_axis'] - res['lower']['log_G_axis'], 4)
if len(sys.argv) > 2:
    pr = np.load(sys.argv[2])
    the = pr['the']; lg = pr['logGt']; A = np.cos(the)**2
    msk = np.abs(np.cos(the)) > 0.05
    g0 = float(lg[msk].mean())
    out['gfix_mean_logGt_cos>0.05'] = round(g0, 4)
    out['axis_minus_mean'] = dict(upper=round(res['upper']['log_G_axis'] - g0, 4), lower=round(res['lower']['log_G_axis'] - g0, 4))
    near = {}
    for c0 in (90.0, 270.0):
        for dd in (-10, -5, -3, -2, -1, -0.5, 0.5, 1, 2, 3, 5, 10):
            k = int(np.argmin(np.abs(np.degrees(the) - (c0 + dd))))
            near['%g' % (c0 + dd)] = round(float(lg[k]) - g0, 4)
    out['gfix_near_zeros_minus_mean'] = near
print(json.dumps(out), flush=True)
