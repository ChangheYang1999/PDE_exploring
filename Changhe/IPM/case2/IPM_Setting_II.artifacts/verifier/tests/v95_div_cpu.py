"""V95: CPU variant (one thread) of tests/v68_div.py, otherwise identical.
V68 variant of tests/v63_div.py: h on the axis from the local second difference of g over +-1 grid angle (hfd1) as well as
from the FFT (hsp; Gibbs-oscillating, sign changes, in the core of the 64-mode states, tests/v68_axh.py). Keys D_lawcorr_{div,dir}_{sp,fd1}.
Original V63 doc: divergence error of the computed velocity of a forward state (own code/fwdstat.py velocity) and the y-axis law with
a_dir = d_x V_1 taken directly from the computed field, next to a_div = 2l - dV_r/dr (which assumes div V = 2l).
Own derivation (notes of the lead analyst 05:21Z item 1 raised the point): with V_r = r alpha, V_th = r beta,
    div V = 2 alpha + d_t alpha + d_th beta      (t = log r),   so  err = 2 alpha + d_t alpha + d_th beta - 2l,
and on x = 0 (th = +-pi/2), d_x = -(sin th / r) d_th, e_x = -sin th e_th + ..., which gives d_x V_1 = alpha + d_th beta on both
half-axes (a_dir), against a_div = 2l - alpha - d_t alpha. d_th: FFT (Nyquist dropped); d_t: r d/dr by the per-panel Gauss
Lagrange differentiation matrix (no uniform-grid finite differences). Axis law: d_t log k = (m1 - a)/alpha,
d_t log(h/k^2) = (1 - 2 m1)/alpha, h = r^(p-2) g_thth.
Usage: python3 tests/v68_div.py STATE.npz [m1_override]   (D_lawcorr: lead adir.py convention, D = q_lower - q_upper at t = 9.5
with q = log h - 2 log k - int (1 - 2 m1)/alpha dt, k = 1 and the law integral 0 at t_min)"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
from charsolve import lagrange_diff
DT = torch.float64; torch.set_num_threads(1)
fn = sys.argv[1]
d = np.load(fn, allow_pickle=True)
args = json.loads(str(d['args']))
p = float(d['p']); r0 = d['r']; th = d['th']; nt = len(th)
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800, dev='cpu')
assert np.allclose(F.r.cpu().numpy(), r0), 'grid mismatch'
rho = torch.tensor(d['rho'], dtype=DT, device='cpu')
nd = F.node(rho); m1 = nd['m1'] if len(sys.argv) < 3 else float(sys.argv[2]); l = 1.0/p
alpha, beta, _, _ = F.fields(rho)
al = alpha.cpu().numpy(); be = beta.cpu().numpy(); g = (rho/F.R**p).cpu().numpy()
r = F.r.cpu().numpy(); q = F.q; P = len(r)//q
edges = F.S.edges
xg = np.polynomial.legendre.leggauss(q)[0]
Dg = lagrange_diff(xg)                       # d/dx on [-1, 1]
dal_dr = np.zeros_like(al)
for k in range(P):
    sl = slice(k*q, (k + 1)*q)
    hk = (edges[k + 1] - edges[k])/2
    dal_dr[sl] = Dg @ al[sl]/hk
dt_al = r[:, None]*dal_dr
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0.0
dth_be = np.real(np.fft.ifft(1j*mm*np.fft.fft(be, axis=1), axis=1))
err = 2*al + dt_al + dth_be - 2*l
t = np.log(r)
out = dict(state=fn.split('/')[-1], p=p, nt=nt, m1=round(m1, 6), min_alpha=round(float(al.min()), 5))
i, j = np.unravel_index(np.argmin(al), al.shape)
out['min_alpha_at'] = dict(t=round(float(t[i]), 3), deg=round(float(np.degrees(th[j])), 2))
bands = {}
for a_, b_ in ((-12, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3), (3, 6), (6, 10)):
    msk = (t >= a_) & (t < b_)
    if not msk.any():
        continue
    e = np.abs(err[msk]); ii, jj = np.unravel_index(np.argmax(e), e.shape)
    bands['%g..%g' % (a_, b_)] = dict(max=float('%.3g' % e.max()), rms=float('%.3g' % np.sqrt((e**2).mean())),
                                      at_deg=round(float(np.degrees(th[jj])), 1))
out['div_err_by_t_band'] = bands

def at(f, ths, deriv=0):
    fh = np.fft.fft(f, axis=1)/nt
    fh[:, nt//2] = 0.0
    fac = np.exp(1j*mm*(ths - th[0]))*((1j*mm)**deriv)
    return np.real(fh @ fac)

Imat = F.Imat.cpu().numpy(); tu = F.tu.cpu().numpy(); dti = F.dti
ax = {}
for name, ths in (('upper', math.pi/2), ('lower', 3*math.pi/2)):
    a_al = at(al, ths); a_dtal = at(dt_al, ths); a_dthb = at(dth_be, ths); gtt_sp = at(g, ths, 2)
    j0 = int(round((ths - th[0])/(2*math.pi/nt))) % nt
    gtt_fd = (g[:, (j0 + 1) % nt] - 2*g[:, j0] + g[:, (j0 - 1) % nt])/(2*math.pi/nt)**2
    a_div = 2*l - a_al - a_dtal; a_dir = a_al + a_dthb
    rows = []
    res = {}
    for lab, a, gtt in (('div_sp', a_div, gtt_sp), ('dir_sp', a_dir, gtt_sp), ('div_fd1', a_div, gtt_fd), ('dir_fd1', a_dir, gtt_fd)):
        au = Imat @ a; alu = Imat @ a_al; gu = Imat @ gtt
        integrand = (m1 - au)/alu
        logk = np.concatenate([[0.0], np.cumsum(0.5*(integrand[1:] + integrand[:-1])*dti)])
        with np.errstate(divide='ignore', invalid='ignore'):
            qq = np.log(np.abs(gu)) + (p - 2)*tu - 2*logk
        pred = (1 - 2*m1)/alu
        resid = qq - np.concatenate([[0.0], np.cumsum(0.5*(pred[1:] + pred[:-1])*dti)])   # constant if the law holds
        sel = {}
        for lo, hi in ((-10, -6), (-8, 0), (-6, -2), (0, 9.5), (-8, 9.5)):
            msk = (tu >= lo) & (tu <= hi)
            sel['%g..%g' % (lo, hi)] = round(float(resid[msk].max() - resid[msk].min()), 4)
        i95 = int(np.argmin(np.abs(tu - 9.5)))
        res[lab] = dict(spread_of_law_residual=sel, q_lawcorr_9p5=float(resid[i95]), log_G_axis=round(float(np.median(qq[(tu >= 0) & (tu <= 9.5)]) - math.log(2)), 4))
    diff = np.abs(a_div - a_dir)
    for lo, hi in ((-12, -8), (-8, -4), (-4, 0), (0, 4), (4, 10)):
        msk = (t >= lo) & (t < hi)
        res['max|a_div-a_dir| %g..%g' % (lo, hi)] = float('%.3g' % diff[msk].max())
    ax[name] = res
out['axis'] = ax
for lab in ('div_sp', 'dir_sp', 'div_fd1', 'dir_fd1'):
    out['D_lawcorr_' + lab] = round(ax['lower'][lab]['q_lawcorr_9p5'] - ax['upper'][lab]['q_lawcorr_9p5'], 4)
out['m1_used'] = m1; out['m1_own'] = nd['m1']
print(json.dumps(out, indent=1), flush=True)
