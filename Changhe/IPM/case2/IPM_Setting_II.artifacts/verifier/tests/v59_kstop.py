"""V59: inner-stop bias of the backward-orbit tracer (tests/v43_gfix.py) at the zero windows, and the r_min tail of the axis law
(tests/v50_axis.py). Own derivation: on the half-axes k = d_x xi(0, y) obeys d_t log k = (m1 - a)/alpha (V50); near the node
b = n y + beta y^2 + ..., so the integrand is O(r) and log k(r) = O(beta r / n). The tracer takes Xi = x_stop e^{m1 T}, i.e. it sets
xi = x at the inner stop r_s; for an orbit that reaches r_s on a half-axis the true value is k(r_s) x_stop, so the tracer log Gt
exceeds the true one by 2 log k(r_s). v50_axis normalises log k = 0 at r_min (not at r = 0), so its log G(+-inf) misses -2 tail,
tail = int_{-inf}^{tmin} (m1 - a)/alpha dt ~ C e^{tmin} (C from a fit e^t on [tmin, tmin + 2]).
Usage: python3 tests/v59_kstop.py STATE.npz [GFIX_PROFILE.npz]"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]
d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args']))
p = float(d['p']); th = d['th']; nt = len(th)
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); m1 = nd['m1']; l = 1.0/p
alpha, beta, _, _ = F.fields(rho)
g = (rho/F.R**p).cpu().numpy(); al = alpha.cpu().numpy()
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0.0
def at(f, ths, deriv=0):
    fh = np.fft.fft(f, axis=1)/nt; fh[:, nt//2] = 0.0
    return np.real(fh @ (np.exp(1j*mm*(ths - th[0]))*((1j*mm)**deriv)))
Imat = F.Imat.cpu().numpy(); tu = F.tu.cpu().numpy(); dti = F.dti
out = dict(state=fn.split('/')[-1], m1=round(m1, 6), m2=round(nd['m2'], 6), tmin=tmin, nt=nt)
for name, ths in (('upper', math.pi/2), ('lower', 3*math.pi/2)):
    a_u = Imat @ at(al, ths); gtt = Imat @ at(g, ths, 2)
    a = 2*l - a_u - np.gradient(a_u, dti); ig = (m1 - a)/a_u
    logk = np.concatenate([[0.0], np.cumsum(0.5*(ig[1:] + ig[:-1])*dti)])
    fit = (tu >= tmin + 0.2) & (tu <= tmin + 2.0)
    C = float(np.sum(ig[fit]*np.exp(tu[fit]))/np.sum(np.exp(2*tu[fit])))     # least squares ig ~ C e^t
    tail = C*math.exp(tmin)
    q = np.log(np.abs(gtt)) + (p - 2)*tu - 2*logk; msk = (tu >= 0) & (tu <= 9.5)
    i = lambda tt: int(round((tt - tmin)/dti))
    out[name] = dict(C_fit=round(C, 2), fit_resid_rel=round(float(np.abs(ig[fit] - C*np.exp(tu[fit])).max()/np.abs(ig[fit]).max()), 4),
                     ig_at=[(tt, float('%.4g' % ig[i(tt)])) for tt in (tmin + 0.5, tmin + 2, -9, -6, -4)],
                     tail=round(tail, 6), log_G_axis_rmin_norm=round(float(np.median(q[msk]) - math.log(2)), 4),
                     log_G_axis_tail_corrected=round(float(np.median(q[msk]) - math.log(2)) - 2*tail, 4),
                     logG_t_tail_corrected={'%g' % tt: round(float(q[i(tt)]) - math.log(2) - 2*tail, 4) for tt in (0, 4, 8, 9.5, 9.9)},
                     two_logk_true_at={'%g' % tt: round(2*(float(logk[i(tt)]) + tail), 4) for tt in (-12, -10, -9, -8, -7, -6, -4)})
out['Dz_rmin_norm'] = round(out['lower']['log_G_axis_rmin_norm'] - out['upper']['log_G_axis_rmin_norm'], 4)
out['Dz_tail_corrected'] = round(out['lower']['log_G_axis_tail_corrected'] - out['upper']['log_G_axis_tail_corrected'], 4)
if len(sys.argv) > 2:
    pr = np.load(sys.argv[2]); the = np.degrees(pr['the']); lg = pr['logGt']; th0 = np.degrees(pr['th0']) % 360
    for name, c0 in (('upper', 90.0), ('lower', 270.0)):
        rows = []
        for dd in (-3, -1, -0.5, -0.2, -0.09, 0.09, 0.2, 0.5, 1, 3):
            k = int(np.argmin(np.abs(the - (c0 + dd))))
            rows.append([round(float(the[k]), 3), round(float(lg[k]) - out[name]['log_G_axis_tail_corrected'], 4),
                         round(float(lg[k]) - out[name]['logG_t_tail_corrected']['9.9'], 4), round(float(th0[k]), 3)])
        out[name]['tracer_tstop-9_minus_axis_median_minus_axis_t9.9_stop_angle'] = rows
print(json.dumps(out), flush=True)
