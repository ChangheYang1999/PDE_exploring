"""Convert a forward-evolution state (runs/pfwd/*.npz: g on the log-polar grid, rho = r^p g) into an initial state for
code/zetasolve.py (zeta = signed sqrt(rho), modes on the Chebyshev-Fourier grid of ipm2polar.Disc), after rescaling the state
by the symmetry rho -> mu rho(X/mu) so that rho_xx(0) = 2 (mu = C where rho ~ C x^2 near the node, C from the m = 0 mode
rho_0(r) ~ C r^2/2 on r in [r_a, r_b]).  x-even states only (zero set = y axis; zeta = sign(cos th) sqrt(rho)).
Usage: python3 tests/pfwd_to_zeta.py state.npz out.pt Nr Nth R [ra=1e-3] [rb=1e-2] [prefactor=s] [smooth=1]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from scipy.interpolate import CubicSpline
from ipm2polar import Disc
torch.set_default_dtype(torch.float64)
fn, outf = sys.argv[1], sys.argv[2]; Nr, Nth, R = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
opt = dict(ra=1e-3, rb=1e-2, prefactor='s', smooth=1, L=1.0)
for a in sys.argv[6:]:
    k, v = a.split('='); opt[k] = v if k == 'prefactor' else (int(v) if k == 'smooth' else float(v))
d = np.load(fn); g = d['g']; lr = d['lr']; th = d['th']; args = json.loads(str(d['args'])); p = args['p']; cl = 1.0 / p
r = np.exp(lr); rho = r[:, None] ** p * g                          # [Nr_f, Nth_f]
Nth_f = len(th)
# jet coefficient C from the m = 0 mode: rho_0(r) = mean_th rho = C r^2 / 2 (+ O(r^3))
rho0 = rho.mean(axis=1)
msk = (r >= opt['ra']) & (r <= opt['rb'])
Cs = 2 * rho0[msk] / r[msk] ** 2
C = float(np.exp(np.mean(np.log(Cs))))
# also the m = 2 mode: rho_2 = (1/N) sum rho e^{-2 i th} -> C r^2 / 4
rho2 = (rho * np.exp(-2j * th)[None, :]).mean(axis=1)
C2 = float(np.mean(4 * rho2[msk].real / r[msk] ** 2))
print("jet coefficient C from m=0: %.6f (spread %.1e over r in [%g, %g]); from m=2: %.6f; p = %g, c_l = %g" % (C, Cs.std() / C, opt['ra'], opt['rb'], C2, p, cl))
mu = C
# target grid
dev = 'cuda'
D = Disc(Nr, Nth, R, L=opt['L'], K=2, tail='power2', device=dev, smooth=bool(opt['smooth']), prefactor=opt['prefactor'])
rD = D.r_np                                                        # Chebyshev radii (node 0 is r = R)
lr_eval = np.log(rD / mu)                                         # rho_new(r) = mu rho(r/mu)
if lr_eval.min() < lr[0] or lr_eval.max() > lr[-1]:
    print("WARNING: evaluation radii outside the forward grid: [%g, %g] vs [%g, %g]" % (lr_eval.min(), lr_eval.max(), lr[0], lr[-1]))
# cubic spline along lr for every forward angle, of log-scaled rho (rho can vanish -> interpolate rho itself)
vals = np.zeros((len(rD), Nth_f))
for k in range(Nth_f):
    cs = CubicSpline(lr, rho[:, k])
    vals[:, k] = mu * cs(np.clip(lr_eval, lr[0], lr[-1]))
# Fourier resampling in theta to the padded Disc grid theta_p (Np points)
thp = D.theta_p.cpu().numpy(); Np = len(thp)
F = np.fft.rfft(vals, axis=1) / Nth_f                               # modes 0..Nth_f/2
Mf = D.M                                                             # keep exactly the target's modes (no aliasing in to_modes)
E = np.exp(1j * np.outer(thp, np.arange(Mf + 1)))                    # [Np, Mf+1]
rho_t = (F[:, :Mf + 1] @ E.T).real * 2.0 - F[:, :1].real             # sum_m c_m e^{im th} + c.c. (m>0 twice)
rho_t = rho_t.T                                                      # [Np, Nr]
neg = rho_t < 0
xe = np.abs(rho_t - rho_t[(Np // 2 - np.arange(Np)) % Np, :]).max() / np.abs(rho_t).max()
print('x-odd part of rho on the target grid (relative): %.2e' % xe)
print("rho on the target grid: min %.3e max %.3e; negative fraction %.3f (set to 0)" % (rho_t.min(), rho_t.max(), neg.mean()))
zeta = np.sign(np.cos(thp))[:, None] * np.sqrt(np.maximum(rho_t, 0.0))
zt = torch.tensor(zeta, device=dev)
qz = D.to_modes(zt) / D.rk
v = D.pack(qz, cl)
qz2, _ = D.unpack(v)
# diagnostics: residual of the ORIGINAL equation through zetasolve's machinery
out = D.zeta_residual_modes(qz2, torch.tensor(cl, device=dev), return_all=True)
tp = D.taylor_psi(out['p'])
Rz = out['Rz']
print("after projection: jet of zeta (0, grad) via Taylor rows handled by the solver; psi_xy(0) = %.5f (c_l - 1/2 = %.5f), psi_yy(0) = %.2e" % (float(tp[2]), cl - 0.5, float(tp[3])))
from zetasolve import weight_zeta
w = weight_zeta(D, p)
rel = (Rz.abs().max(dim=0).values / w)
rr = D.r
for lo_, hi_ in ((0, 1), (1, 10), (10, 100), (100, 1e9)):
    m_ = (rr >= lo_) & (rr < hi_)
    if m_.any(): print("   zeta residual / w_zeta on r in [%g, %g): max %.2e median %.2e" % (lo_, min(hi_, R), float(rel[m_].max()), float(rel[m_].median())))
torch.save(dict(q=qz2.cpu(), cl=float(cl), args=dict(Nr=Nr, Nth=Nth, R=R, L=opt['L'], K=2, cl0=cl, prefactor=opt['prefactor'], smooth=bool(opt['smooth']), tail='power2', ay=0.0, source=fn, mu=mu),
                hist=[], r=D.r_np, xi=D.xi_np, kappa=D.kappa_np), outf)
print("saved", outf)
