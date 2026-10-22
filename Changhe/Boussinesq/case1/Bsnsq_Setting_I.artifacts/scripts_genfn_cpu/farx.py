"""Far limit of the grouped ratio by extrapolation in s = E^(-1/6) (diagnostic): at fixed S = w/wmax, evaluate the
SIGNED ratios R/N2 and R/N at radii where binary64 resolves them (s in a list), fit a polynomial in s and extrapolate to
s = 0. In directions where the leading denominators are positive, R/N2 -> C/N20 as s -> 0 and R/N = O(s).
Usage: python3 farx.py state.npz [deg] [s1,s2,...] [--noise] [--thr t]  (--thr: fit only s values whose noise is <= t)"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); beta = mod.beta
if 'core' in d.files:
    from model_core import ModelCore
    mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam); c = torch.tensor(np.concatenate([d['c'], d['cc']]))
deg = int(sys.argv[2]) if len(sys.argv) > 2 else 3
ss = np.array([float(v) for v in sys.argv[3].split(',')]) if len(sys.argv) > 3 and not sys.argv[3].startswith('--') else np.array([2e-3, 3e-3, 4e-3, 6e-3, 8e-3, 1.2e-2, 1.6e-2])
Ss = np.array([1e-6, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999, 0.9999, 1 - 1e-6, 1 - 1e-8])
T, S = np.meshgrid(ss, Ss, indexing='ij'); x, eta = ts_to_xeta(T.ravel(), S.ravel(), m_, se)
x = torch.tensor(x); eta = torch.tensor(eta)
Bm = mod.basis_matrix(x, eta)
def ratios(cv):
    F = fields(Bm @ cv, x, eta, a0, beta); y = F['y']
    N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (x * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
    return (F['R'] / N2).detach().numpy().reshape(T.shape), (F['R'] / F['N']).detach().numpy().reshape(T.shape), y
q2, q, y = ratios(c)
qn = None
if '--noise' in sys.argv:    # sensitivity of the signed grouped ratio to a 1e-14 relative perturbation of the coefficients
    qn = np.abs(ratios(c * (1 + 1e-14 * torch.tensor(np.random.default_rng(1).standard_normal(c.shape[0]), dtype=c.dtype)))[0] - q2)
r = np.hypot(x.numpy(), y.detach().numpy()).reshape(T.shape); ph = np.degrees(np.arctan2(y.detach().numpy(), x.numpy())).reshape(T.shape)
print('state %s a0 %.4f  s = %s  deg %d' % (sys.argv[1], a0, ','.join('%g' % v for v in ss), deg))
print('  S=w/wmax  phi(s1)   r(s1)      r(s_last)   signed R/N2 at s1 .. s_last                          | extrap s->0  fitres   | R/N at s1')
thr = float(sys.argv[sys.argv.index('--thr') + 1]) if '--thr' in sys.argv else None   # fit only s with noise <= thr
for j in range(len(Ss)):
    keep = np.ones(len(ss), bool) if (thr is None or qn is None) else (qn[:, j] <= thr)
    if keep.sum() < deg + 2:
        print('  %-9.7g only %d resolved s values (noise <= %g): no fit;  noise per s %s' % (Ss[j], keep.sum(), thr, ' '.join('%.0e' % v for v in qn[:, j]))); continue
    co = np.polyfit(ss[keep], q2[keep, j], deg); ext = np.polyval(co, 0.0); fr = np.abs(np.polyval(co, ss[keep]) - q2[keep, j]).max()
    print('  %-9.7g %8.4f  %.2e  %.2e  %s | %+.4e %.1e | %+.2e' % (Ss[j], ph[0, j], r[0, j], r[-1, j], ' '.join('%+.3e' % v for v in q2[:, j]), ext, fr, q[0, j])
          + ('  noise max %.1e at s1 %.1e' % (qn[:, j].max(), qn[0, j]) if qn is not None else '')
          + ('  used %d/%d s, smallest %.1e' % (keep.sum(), len(ss), ss[keep].min()) if thr is not None else ''))
