"""Stagnation-point and homogeneity diagnostics of a genfn state (GPU; short).
W = beta X + U = (x A_tr, y B_tr) with A_tr = W1/x, B_tr = W2/y (A_tr = beta - H - 2 t H_t, B_tr = beta + H + 2 s H_s in the reduced variables).
A stagnation point off the axes needs A_tr = B_tr = 0; on the x-axis A_tr = 0, on the y-axis B_tr = 0. Reports minima of A_tr, B_tr and of
|W|/(beta r) by radial band with locations, plus the local homogeneity exponents p_T = (x Th_x + y Th_y)/Theta and p_O = (x Om_x + y Om_y)/Om
(a radially homogeneous profile r^p f(phi) would have constant p; here p_T runs from 1 at the centre to (beta-2)/beta at infinity).
BETA-3 TOOL (like where2_gpu.py): the model is built with beta = m = 3 and the stored beta is ignored, so the output is valid for beta = 3 states only.
Usage: python3 stag_check.py state.npz [Nt Ns tmin]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
Nt = int(sys.argv[2]) if len(sys.argv) > 2 else 121; Ns = int(sys.argv[3]) if len(sys.argv) > 3 else 150
tmin = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-4
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); beta = mod.beta
if 'beta' in d.files and abs(float(d['beta']) - beta) > 1e-12: print('WARNING: stored beta %.6f != model beta %.6f: beta-3 tool, output invalid for this state' % (float(d['beta']), beta))
if 'core' in d.files:
    from model_core import ModelCore; q_ = d['core']
    mod = ModelCore(J, Kw, q_, m=m_, alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
tau = 0.5 * (1 - np.cos(np.pi * it))
t = 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1) if alpha > 0 else tau
t = tmin + (1 - tmin) * t
s = 0.5 * (1 - np.cos(np.pi * is_))
s = np.concatenate([s, [1e-10, 1e-7, 1e-5, 1e-4, 1e-3, 3e-3, 1 - 3e-3, 1 - 1e-3, 1 - 1e-4, 1 - 1e-5, 1 - 1e-7, 1 - 1e-10]])
t = np.concatenate([t, 1 - np.array([1e-12, 1e-10, 1e-8, 1e-6, 1e-5, 1e-4])])
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
x, eta = ts_to_xeta(T, S, m_, se)
keep = (x > 1e-12) & (eta > 1e-12)
x = torch.tensor(x[keep], device=DEV); eta = torch.tensor(eta[keep], device=DEV)
out = {k: [] for k in ['x', 'y', 'Atr', 'Btr', 'pT', 'pO', 'Om', 'W1', 'W2', 'A']}
for ch in torch.split(torch.arange(x.shape[0], device=DEV), 4096):
    F = fields(mod.basis_matrix(x[ch], eta[ch]) @ c, x[ch], eta[ch], a0, beta)
    y = F['y']; xc = x[ch]; e = eta[ch]
    Th = a0 * e                      # Theta = a0 * eta in this representation
    out['x'].append(xc); out['y'].append(y); out['Atr'].append(F['W1'] / xc); out['Btr'].append(F['W2'] / y)
    out['pT'].append((xc * F['Thx'] + y * F['Thy']) / Th); out['pO'].append((xc * F['Ox'] + y * F['Oy']) / F['Om'])
    out['Om'].append(F['Om']); out['W1'].append(F['W1']); out['W2'].append(F['W2']); out['A'].append(F['A'])
o = {k: torch.cat(v).detach().cpu().numpy() for k, v in out.items()}
x = o['x']; y = o['y']; r = np.hypot(x, y); ph = np.degrees(np.arctan2(y, x))
print('state %s beta %.6f a0 %.4f points %d  (grid Nt %d Ns %d tmin %g + edge rows)' % (sys.argv[1], beta, a0, len(x), Nt, Ns, tmin))
Wrel = np.hypot(o['W1'], o['W2']) / (beta * r)
print('global: min A_tr = W1/x %.6f at (x, y) = (%.4g, %.4g); min B_tr = W2/y %.6f at (%.4g, %.4g); min |W|/(beta r) %.6f at (%.4g, %.4g)' % (
    o['Atr'].min(), x[o['Atr'].argmin()], y[o['Atr'].argmin()], o['Btr'].min(), x[o['Btr'].argmin()], y[o['Btr'].argmin()],
    Wrel.min(), x[Wrel.argmin()], y[Wrel.argmin()]))
print('chart Jacobian A = G_x,eta: min %.6f at (x, y) = (%.4g, %.4g), max %.4g (A > 0 on the sampled set is the chart hypothesis of the exact uniqueness argument)' % (o['A'].min(), x[o['A'].argmin()], y[o['A'].argmin()], o['A'].max()))
print('  centre values expected: A_tr(0) = beta + 2 = %.1f, B_tr(0) = beta - 2 = %.1f; far field: both -> beta = %.1f' % (beta + 2, beta - 2, beta))
print('  band            min A_tr (x, y)                 min B_tr (x, y)                 min |W|/(beta r)   p_T [min, med, max]        p_O [min, med, max]   sign changes of Om (fraction Om<0)')
for lo, hi in [(0, 1e-3), (1e-3, 1e-2), (1e-2, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6), (1e6, 1e8)]:
    m = (r >= lo) & (r < hi)
    if not m.any(): continue
    ia = np.where(m)[0][o['Atr'][m].argmin()]; ib = np.where(m)[0][o['Btr'][m].argmin()]
    print('  [%g, %g): %9.5f (%.3g, %.3g)   %9.5f (%.3g, %.3g)   %9.5f   [%7.4f %7.4f %7.4f]   [%7.4f %7.4f %7.4f]   %.3f' % (
        lo, hi, o['Atr'][ia], x[ia], y[ia], o['Btr'][ib], x[ib], y[ib], Wrel[m].min(),
        o['pT'][m].min(), np.median(o['pT'][m]), o['pT'][m].max(), o['pO'][m].min(), np.median(o['pO'][m]), o['pO'][m].max(), (o['Om'][m] < 0).mean()))
# near-axis rows: A_tr on the x-axis side (smallest y/x) and B_tr on the y-axis side (smallest x/y)
mx = ph < 0.01; my = ph > 89.99
def near_axis(mask, coord, val, name, cname):
    cs = coord[mask]; vs = val[mask]; o_ = np.argsort(cs); cs = cs[o_]; vs = vs[o_]
    decs = [d for d in [1e-3, 1e-2, 0.1, 1, 10, 100, 1e3, 1e4, 1e5, 1e6] if cs.min() <= d <= cs.max()]
    print('  near-%s rows (%s; interpolated along the sampled rows, NOT exact axis values; sampled %s range %.4g .. %.4g): min %.6f at %s = %.4g; values at %s = %s: %s' % (
        name, 'phi < 0.01 deg' if name == 'x-axis' else 'phi > 89.99 deg', cname, cs.min(), cs.max(), vs.min(), cname, cs[vs.argmin()], cname,
        ', '.join('%g' % d for d in decs), ' '.join('%.4f' % np.interp(np.log10(d), np.log10(cs), vs) for d in decs)))
if mx.any(): near_axis(mx, x, o['Atr'], 'x-axis', 'x')
if my.any(): near_axis(my, y, o['Btr'], 'y-axis', 'y')
