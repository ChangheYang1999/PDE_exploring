"""Smooth candidate from a fixed-point forward state: rho_c(X) = Gt_mean xi(X)^2, xi(X) = u0 e^{m1 T} from the backward orbit of X to the
inner ring (lead's representation rho = |xi|^{1/m1} G; here G := constant = its orbit mean).  This is C^2 at the node by construction
and coincides with the forward steady state on every orbit where Gt equals its mean.  Rescaled by the symmetry rho -> mu rho(X/mu),
mu = Gt_mean, so that rho_xx(0) = 2.  Output: zetasolve initial state (zeta = sign(xi) |xi| sqrt(Gt), modes on the Disc grid).
Usage: python3 tests/pfwd_to_zeta2.py state.npz out.pt Nr Nth R [lr0=-11] [dt=0.01] [prefactor=s] [smooth=1]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint
from ipm2polar import Disc
torch.set_default_dtype(torch.float64)
fn, outf = sys.argv[1], sys.argv[2]; Nr, Nth, R = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
opt = dict(lr0=-11.0, dt=0.01, prefactor='s', smooth=1, L=1.0)
for a in sys.argv[6:]:
    k, v = a.split('='); opt[k] = v if k == 'prefactor' else (int(v) if k == 'smooth' else float(v))
d = np.load(fn); g = torch.tensor(d['g'], device='cuda'); lr = d['lr']; args = json.loads(str(d['args'])); p = args['p']; cl = 1.0 / p
par = args['par']
if isinstance(par, str): par = [float(v) for v in par.split(':')]
Nrf, Nthf = g.shape
FP = FixedPoint(p, len(par), Nr=Nrf, Nth=Nthf, lo=float(lr[0]), hi=float(lr[-1]), lr0=opt['lr0'], nA=1024, dt=opt['dt'])
S = FP.S; rho = S.r[:, None] ** p * g; Wr, Wt = S.velocity(rho); dg = S.diagnostics(g, Wr, Wt, krings=(20,))
m1 = cl - dg['c_moment']; e1 = (1.0, 0.0)
# Gt_true from the far-field orbits: log Gt_true = p*hi + log A - 2 log|u0| - 2 m1 T
T, u0, w0, th0, it = FP.trace(Wr, Wt, e1)
A = FP.Afun(par)(FP.thA)
logGt = p * float(lr[-1]) + torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T
w = (torch.cos(FP.thA).abs() > 0.02).double()
mean = float((w * logGt).sum() / w.sum()); std = float(torch.sqrt((w * (logGt - mean) ** 2).sum() / w.sum()))
Gt = math.exp(mean); mu = Gt
print("state %s: p = %.5f, c_l = %.5f, m1(moment) = %.5f; Gt_true mean %.4f (log std %.4f over the far field); scaling mu = %.3f" % (fn, p, cl, m1, Gt, std, mu))
# Disc grid points, mapped to the forward state by X -> X/mu
dev = 'cuda'
D = Disc(Nr, Nth, R, L=opt['L'], K=2, tail='power2', device=dev, smooth=bool(opt['smooth']), prefactor=opt['prefactor'])
rD = torch.tensor(D.r_np, device=dev); thp = D.theta_p
RR, TH = torch.meshgrid(rD, thp, indexing='xy')          # [Np, Nr]
lr_start = torch.log(RR / mu).reshape(-1); th_start = TH.reshape(-1)
print("forward-state radii covered: [%.2e, %.2e] (grid [%.2e, %.2e]); inner ring e^%g" % (float(torch.exp(lr_start).min()), float(torch.exp(lr_start).max()), math.exp(lr[0]), math.exp(lr[-1]), opt['lr0']))
assert float(lr_start.min()) > opt['lr0'] + 0.3, "Disc inner nodes fall inside the inner ring; lower lr0 or reduce mu"
T2, u02, w02, th02, it2 = FP.trace_from(Wr, Wt, lr_start, th_start, e1)
xi = u02 * torch.exp(m1 * T2)                              # slow coordinate at X/mu (sign from u0)
zeta = (math.sqrt(mu * Gt) * xi).reshape(RR.shape)         # zeta_mu(X) = sqrt(mu Gt) xi(X/mu)  -> ~ x near 0
# diagnostics of the construction: compare rho_c = zeta^2 with the forward state's rho at the same points (interpolated), per radius band
rho_fs = S.r[:, None] ** p * g
ci = (lr_start - S.lo) / S.d; cj = th_start / S.dth
rho_at = S.interp(rho_fs, ci, cj, rho_fs[-1:].expand(2, -1)).reshape(RR.shape) * mu
ratio = (zeta ** 2 / torch.clamp(rho_at, min=1e-300))
for lo_, hi_ in ((0, 1), (1, 10), (10, 100), (100, 1e9)):
    m_ = (RR >= lo_) & (RR < hi_) & (rho_at > 1e-3 * rho_at.max())
    if m_.any(): print("   rho_c / rho_forward on Newton radii [%g, %g): median %.4f, min %.4f, max %.4f" % (lo_, min(hi_, R), float(ratio[m_].median()), float(ratio[m_].min()), float(ratio[m_].max())))
qz = D.to_modes(zeta) / D.rk
v = D.pack(qz, cl); qz2, _ = D.unpack(v)
out = D.zeta_residual_modes(qz2, torch.tensor(cl, device=dev), return_all=True)
tp = D.taylor_psi(out['p']); Rz = out['Rz']
from zetasolve import weight_zeta
wz = weight_zeta(D, p); rel = Rz.abs().max(dim=0).values / wz
print("init state: psi_xy(0) = %.5f (c_l - 1/2 = %.5f), psi_yy(0) = %.2e; zeta residual / w_zeta by band:" % (float(tp[2]), cl - 0.5, float(tp[3])))
for lo_, hi_ in ((0, 1), (1, 10), (10, 100), (100, 1e9)):
    m_ = (D.r >= lo_) & (D.r < hi_)
    if m_.any(): print("   r in [%g, %g): max %.2e median %.2e" % (lo_, min(hi_, R), float(rel[m_].max()), float(rel[m_].median())))
torch.save(dict(q=qz2.cpu(), cl=float(cl), args=dict(Nr=Nr, Nth=Nth, R=R, L=opt['L'], K=2, cl0=cl, prefactor=opt['prefactor'], smooth=bool(opt['smooth']), tail='power2', ay=0.0, source=fn, mu=mu, Gt=Gt),
                hist=[], r=D.r_np, xi=D.xi_np, kappa=D.kappa_np), outf)
print("saved", outf, "(tracer steps %d, %d points)" % (it2, lr_start.numel()))
