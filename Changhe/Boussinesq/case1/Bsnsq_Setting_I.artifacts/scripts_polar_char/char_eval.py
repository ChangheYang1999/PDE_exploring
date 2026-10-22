"""Independent evaluation of a characteristic-solver state (charsolve/proj_psi npz: cP, a0, beta).
On an independent log-polar grid (different from the solver's Chebyshev/Gauss grid) the fields are reconstructed by backward
characteristics (charlib2.transport, dt and r_stop chosen here) at every point and at the four FD-displaced points X +- h e_x,
X +- h e_y.  Reported (prompt definitions, pointwise normalized by N = sum of absolute values of the terms):
  R_Theta = W.grad Theta_char - (beta-2) Theta_char   with grad from central FD (independent of the propagator) [and from P],
  R_Omega(basis) = W.grad Omega_basis + Omega_basis - Theta_x,char   (the state's vorticity in the vorticity equation),
  R_Omega(char)  = W.grad Omega_char (FD) + Omega_char - Theta_x,char (ODE/FD consistency only),
  E = Omega_basis - Omega_char (Poisson closure defect), normalized by |Omega_basis| + |Omega_char| and by the proxy scale S_O,
desingularized R_Theta/y, R_Omega/(xy) (absolute), regional maxima by radius, near-axis bins, centre data and far-field amplitudes.
"""
import sys, os, json, math, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charlib2 import *
ap = argparse.ArgumentParser(); ap.add_argument('npz'); ap.add_argument('--json', default=None)
ap.add_argument('--rmin', type=float, default=1e-2); ap.add_argument('--rmax', type=float, default=1e9); ap.add_argument('--per-decade', type=int, default=8)
ap.add_argument('--Nth', type=int, default=36); ap.add_argument('--dt', type=float, default=0.005); ap.add_argument('--rstop', type=float, default=1e-3)
ap.add_argument('--h', type=float, default=1e-3, help='relative FD step (times max(r, 1))'); ap.add_argument('--eps-th', type=float, default=0.01); ap.add_argument('--dump', default=None, help='npz with the reconstructed fields on the evaluation grid (for the verifier)')
args = ap.parse_args()
dv = dev()
d = np.load(args.npz, allow_pickle=True)
beta = float(d['beta']); L = float(d['L']); NO = int(d['NO']); K = int(d['K']); a0 = float(d['a0'])
bas = PsiBasis(beta, NO, K, L=L, gamma_P=float(d['gamma_P']) if 'gamma_P' in d else None, mu=float(d['mu']) if 'mu' in d else None)
cP = torch.tensor(d['cP'], dtype=DT, device=dv).reshape(NO, K)
b = beta - 2.0
# independent grid: log-spaced radii (offset from decades), angles uniform in (0, 90) plus near-axis angles 1, 2, 88, 89 deg
nd = int(round(math.log10(args.rmax / args.rmin) * args.per_decade)) + 1
r = torch.logspace(math.log10(args.rmin), math.log10(args.rmax), nd, dtype=DT, device=dv) * 1.0371 * L
th = torch.tensor(sorted(set([math.radians(a) for a in np.linspace(2.5, 87.5, args.Nth)] + [math.radians(a) for a in (0.01, 0.1, 1, 2, 88, 89, 89.9, 89.99)])), dtype=DT, device=dv)
R, TH = torch.meshgrid(r, th, indexing='ij'); R = R.reshape(-1); TH = TH.reshape(-1)
X0 = R * torch.cos(TH); Y0 = R * torch.sin(TH); N = R.shape[0]
hh = args.h * torch.maximum(R, torch.ones_like(R))
Xs = torch.cat([X0, X0 + hh, X0 - hh, X0, X0]); Ys = torch.cat([Y0, Y0, Y0, Y0 + hh, Y0 - hh])
print(f'# state {args.npz}: beta {beta} NO {NO} K {K} a0 {a0:.6f}; independent grid {nd} radii x {th.shape[0]} angles = {N} points (x5 FD stencil); dt {args.dt} r_stop {args.rstop}', flush=True)
tr = transport(bas, cP[None], a0, beta, Xs, Ys, dt=args.dt, r_stop=args.rstop, T_max=60.0)
fb = bas.fields(cP[None], Xs, Ys)
def split(v): return v[0].reshape(5, N)
Th = split(tr['Th']); Thx_P = split(tr['Thx'])[0]; Thy_P = split(tr['Thy'])[0]; Omc = split(tr['Om']); fail = split(tr['fail'].to(DT)).sum(0) > 0   # any stencil point failed
Omb = split(fb['Om']); Px = split(fb['Psi_x'])[0]; Py = split(fb['Psi_y'])[0]
W1 = beta * X0 - Py; W2 = beta * Y0 + Px
Thx = (Th[1] - Th[2]) / (2 * hh); Thy = (Th[3] - Th[4]) / (2 * hh)
Omcx = (Omc[1] - Omc[2]) / (2 * hh); Omcy = (Omc[3] - Omc[4]) / (2 * hh)
Ombx = (Omb[1] - Omb[2]) / (2 * hh); Omby = (Omb[3] - Omb[4]) / (2 * hh)      # FD of the basis Omega (exact field; FD error only)
Th0 = Th[0]; Omc0 = Omc[0]; Omb0 = Omb[0]
RT = W1 * Thx + W2 * Thy - b * Th0; NT = (W1 * Thx).abs() + (W2 * Thy).abs() + abs(b) * Th0.abs()
RT_P = W1 * Thx_P + W2 * Thy_P - b * Th0; NT_P = (W1 * Thx_P).abs() + (W2 * Thy_P).abs() + abs(b) * Th0.abs()
ROb = W1 * Ombx + W2 * Omby + Omb0 - Thx_P; NOb = (W1 * Ombx).abs() + (W2 * Omby).abs() + Omb0.abs() + Thx_P.abs()
ROc = W1 * Omcx + W2 * Omcy + Omc0 - Thx_P; NOc = (W1 * Omcx).abs() + (W2 * Omcy).abs() + Omc0.abs() + Thx_P.abs()
E = Omb0 - Omc0; NE = Omb0.abs() + Omc0.abs()
F = bas.centre_functionals(dv); cf = cP.reshape(-1); c = float(cf @ F['c']); h10 = float(cf @ F['h10']); h01 = float(cf @ F['h01'])
f10, f01, g00 = jets(beta, a0, h10, h01)
u = R / L; Ecal = 1 + u * u
SO = max(abs(g00), 1e-12) * R ** 2 * Ecal ** (-1.0 - 0.5 / beta) * (0.5 * torch.sin(2 * TH) + args.eps_th)
ok = ~fail
bins = [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6), (1e6, 1e9), (1e9, 1e13)]
def regional(num, den, mask=None):
    out = []
    for lo, hi in bins:
        m = (R >= lo * L) & (R < hi * L) & ok
        if mask is not None: m = m & mask
        if not m.any(): out.append(None); continue
        ratio = (num[m].abs() / (den[m] + 1e-300))
        out.append(dict(rlo=lo, rhi=hi, max_abs=float(num[m].abs().max()), max_norm=float(ratio.max()), argmax_r=float(R[m][ratio.argmax()] / L), argmax_deg=float(TH[m][ratio.argmax()]) * 180 / math.pi))
    return out
res = dict(file=args.npz, beta=beta, a0=a0, c=c, h10=h10, h01=h01, g00=g00, nfail=int(fail.sum()), N=N, Tmax=float(tr['T'].max()), nsteps=tr['nsteps'])
res['R_Theta_FD'] = regional(RT, NT); res['R_Theta_P'] = regional(RT_P, NT_P)
res['R_Omega_basis'] = regional(ROb, NOb); res['R_Omega_char'] = regional(ROc, NOc)
res['E_closure_rel'] = regional(E, NE); res['E_closure_proxy'] = regional(E, SO)
near_y = TH > math.radians(80); near_x = TH < math.radians(10)
res['E_closure_rel_near_yaxis'] = regional(E, NE, near_y); res['E_closure_rel_near_xaxis'] = regional(E, NE, near_x)
res['R_Omega_basis_near_yaxis'] = regional(ROb, NOb, near_y); res['R_Theta_FD_near_yaxis'] = regional(RT, NT, near_y)
res['desing_RT_over_y_abs'] = regional(RT / Y0, torch.ones_like(RT)); res['desing_RO_basis_over_xy_abs'] = regional(ROb / (X0 * Y0), torch.ones_like(RT))
res['grad_check_Thx'] = float(((Thx - Thx_P).abs() / (Thx_P.abs() + Thy_P.abs() + 1e-300))[ok].max()); res['grad_check_Thy'] = float(((Thy - Thy_P).abs() / (Thy_P.abs() + 1e-300))[ok].max())
res['grad_check_Thx_rel'] = float(((Thx - Thx_P).abs() / (Thx_P.abs() + 1e-300))[ok & (TH < math.radians(80))].max())
# backward-basin diagnostic (external review finding 12): min over the grid of X.W/|X|^2 (positive everywhere sampled => outward flow, backward flow inward)
res['min_XdotW_over_r2'] = float(((X0 * W1 + Y0 * W2) / (R * R)).min()); res['argmin_XdotW_r'] = float(R[((X0 * W1 + Y0 * W2) / (R * R)).argmin()] / L); res['argmin_XdotW_deg'] = float(TH[((X0 * W1 + Y0 * W2) / (R * R)).argmin()]) * 180 / math.pi
# centre Poisson closure defect: g00_basis = -6 (h10 + h01) vs the jet g00 = 2 f10/(2 beta + 1)
res['centre_closure_defect_rel'] = float((-6.0 * (h10 + h01) - g00) / (abs(g00) + 1e-300))
# far-field amplitudes of the reconstructed temperature: Theta ~ r^{1-2/beta} F(phi); report Theta/(y r^{-2/beta}) at the largest radii
far = R >= 1e6 * L
res['far_Theta_over_y_r^-2/beta_max'] = float((Th0[far] / (Y0[far] * R[far] ** (-2.0 / beta))).abs().max()) if far.any() else None
res['far_Omega_basis_r^1/beta_max'] = float((Omb0[far] * R[far] ** (1.0 / beta)).abs().max()) if far.any() else None
def fmt(tab):
    return '  '.join(('%.1e' % t['max_norm']) if t else '  -  ' for t in tab)
print('# regions:            ' + '  '.join('%5.0e-%-5.0e' % (lo, hi) for lo, hi in bins))
for k in ['R_Theta_FD', 'R_Theta_P', 'R_Omega_basis', 'R_Omega_char', 'E_closure_rel', 'E_closure_proxy', 'E_closure_rel_near_yaxis', 'E_closure_rel_near_xaxis', 'R_Omega_basis_near_yaxis', 'R_Theta_FD_near_yaxis']:
    print('# %-26s max|R|/N: %s' % (k, fmt(res[k])))
print('# max abs R_Theta/y by region:      ' + '  '.join(('%.1e' % t['max_abs']) if t else '  -  ' for t in res['desing_RT_over_y_abs']))
print('# max abs R_Omega(basis)/(xy):      ' + '  '.join(('%.1e' % t['max_abs']) if t else '  -  ' for t in res['desing_RO_basis_over_xy_abs']))
print('# gradient check FD vs propagator: Theta_x %.2e (rel, phi<80: %.2e)  Theta_y %.2e ; nfail %d ; c %.10f h10 %.6e h01 %.6e a0 %.6f g00 %.6f' % (res['grad_check_Thx'], res['grad_check_Thx_rel'], res['grad_check_Thy'], res['nfail'], c, h10, h01, a0, g00))
print('# basin diagnostic: min X.W/|X|^2 = %.4f at r %.3g phi %.2f deg (must be > 0 for the sampled quadrant to flow outward); centre Poisson closure defect (g00_basis - g00_jet)/g00 = %.3e' % (res['min_XdotW_over_r2'], res['argmin_XdotW_r'], res['argmin_XdotW_deg'], res['centre_closure_defect_rel']))
print('# far field (r >= 1e6): max |Theta/(y r^(-2/beta))| %s ; max |Omega_basis r^(1/beta)| %s' % (res['far_Theta_over_y_r^-2/beta_max'], res['far_Omega_basis_r^1/beta_max']))
# angular profile of the closure defect at selected radii (nearest grid radius): Omega_basis/(xy), Omega_char/(xy), ratio
print('# angular profile of Omega/(xy): basis | char  (and relative defect) at radii near 0.3, 1, 1.7, 3, 10, 100')
for rv in [0.3, 1.0, 1.7, 3.0, 10.0, 100.0]:
    i = int(torch.argmin((r - rv * L).abs())); m = (R == r[i])
    xy = (X0[m] * Y0[m]); ob = (Omb0[m] / xy); oc = (Omc0[m] / xy); degs = TH[m] * 180 / math.pi
    line = '  '.join('%4.1f:%+.4f|%+.4f(%.0e)' % (float(dg), float(a), float(b_), float(abs(a - b_) / (abs(b_) + 1e-300))) for dg, a, b_ in zip(degs, ob, oc))
    print('#  r=%.3g: %s' % (float(r[i] / L), line))
if args.dump:
    np.savez(args.dump, x=X0.cpu().numpy(), y=Y0.cpu().numpy(), r=R.cpu().numpy(), phi=TH.cpu().numpy(), Theta=Th0.cpu().numpy(), Theta_x=Thx_P.cpu().numpy(), Theta_y=Thy_P.cpu().numpy(),
             Omega_char=Omc0.cpu().numpy(), Omega_basis=Omb0.cpu().numpy(), W1=W1.cpu().numpy(), W2=W2.cpu().numpy(), Psi_x=Px.cpu().numpy(), Psi_y=Py.cpu().numpy(), T=split(tr['T'])[0].cpu().numpy(), fail=fail.cpu().numpy(),
             beta=beta, a0=a0, c=c, h10=h10, h01=h01, L=L, NO=NO, K=K, cP=cP.cpu().numpy(), gamma_P=bas.gamma_P, mu=bas.mu, dt=args.dt, rstop=args.rstop, source=args.npz)
    print('# dumped fields to', args.dump)
if args.json:
    json.dump(res, open(args.json, 'w'), indent=1)
    print('# saved', args.json)
