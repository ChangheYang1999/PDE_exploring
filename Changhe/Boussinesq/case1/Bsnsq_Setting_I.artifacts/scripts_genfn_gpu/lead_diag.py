"""Sampled necessary-condition diagnostics for the authors' Propositions 33 / 37 / 38 (class ST<, g < 0) on a stored beta = 3 state (authors' request
2026-10-22T02:24:43Z). Everything is evaluated on the stored function by the root-inverted physical fields of gphys_local.py (G_x(x, eta) = y) and
central finite differences where a derivative is not in model.fields; sampled values only, no bounds.
(1) g = Omega_xy(0) and a0 (from the jets of the state: limit of Omega_x(0, y) / y at the smallest height, and the stored a0);
(2) horizontal axis, x log-spaced 1e-4 .. 1e8 (nx points): V = W1(x, 0), tau = Theta_y(x, 0), U1_x(x, 0) by central FD (relative step d), max U1_x and location;
(3) sign of Theta on the open upper half-plane: min of Theta / y on a polar grid (r 1e-4 .. 1e8 x phi in (0, 90) deg); Theta = a0 eta and y = G_x(x, eta) with
    A = G_x,eta > 0 give eta > 0 for y > 0 identically where A > 0, so the sample is a check of the evaluation;
(4) graph of G_T (zero of Theta_x along vertical lines x_j): interpolated zero y* (log-linear), and at (x_j, y*): Theta_y, W2, Theta_xy (FD in y), U2_x (FD in x),
    plus the Omega zero of the line; min / max of U2_x over the graph points;
(5) vertical axis, y log-spaced 1e-4 .. 1e8 (ny points): s = Theta_xx(0, y), z = Omega_x(0, y), C = U2_xx(0, y) as in vaxis.py (x = 0, h, 2h, h = hrel max(y, 0.1)),
    y_C = inf {a0 C < 0}, y_s = inf {s > 0}, y_z = inf {z > 0}, both-sign flags, U2_yy(0, y_s) by a second difference in y.
Usage: python3 lead_diag.py state.npz outprefix [--nx 2000 --ny 2000 --lines 1e-3,1e-2,...]"""
import sys, math, numpy as np, torch, hashlib
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from jets import monos, DT
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0; se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
m_ = int(d['m']) if 'm' in d.files else 3
assert (int(d['fb']) == 0) if 'fb' in d.files else True, 'beta-3 states only'
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
if 'core' in d.files:
    from model_core import ModelCore; mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
beta = mod.beta; out = sys.argv[2]
opt = lambda k, dflt, typ=float: typ(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else dflt
nx = opt('--nx', 2000, int); ny = opt('--ny', 2000, int); hrel = opt('--hrel', 1e-3); dfd = opt('--d', 1e-4)
lines = [float(v) for v in opt('--lines', '1e-3,3e-3,1e-2,3e-2,0.1,0.3,1,3,10,30,100,300,1e3,3e3,1e4,1e5,1e6', str).split(',')]
L1, ix1 = monos(1); L2, ix2 = monos(2)
def Gx_of(x, e): return (mod.basis_matrix(x, e, p=1)[ix1[(1, 0)]] @ c)
def eta_of(x, y):
    lo = torch.zeros_like(y); hi = torch.maximum(y, torch.ones_like(y)) * 1e-3
    for _ in range(200):
        g = Gx_of(x, hi); m = g < y
        if not m.any(): break
        lo = torch.where(m, hi, lo); hi = torch.where(m, hi * 4, hi)
    for _ in range(80):
        mid = 0.5 * (lo + hi); g = Gx_of(x, mid); m = g < y
        lo = torch.where(m, mid, lo); hi = torch.where(m, hi, mid)
    e = 0.5 * (lo + hi)
    for _ in range(4):
        B = mod.basis_matrix(x, e, p=2) @ c
        e = e - (B[ix2[(1, 0)]] - y) / B[ix2[(1, 1)]]
    return e
def F_at(x, e):
    out = {}
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 4096):
        F = fields(mod.basis_matrix(x[ch], e[ch]) @ c, x[ch], e[ch], a0, beta)
        for k, v in F.items(): out.setdefault(k, []).append(v.detach())
    out = {k: torch.cat(v) for k, v in out.items()}; out['eta'] = e; return out
def phys(x, y): return F_at(x, eta_of(x, y))
T = lambda a: torch.tensor(np.asarray(a, dtype=np.float64), dtype=DT, device=DEV)
cpu = lambda t: t.detach().cpu().numpy()
rep = []; files = []
def save(name, header, arr):
    fn = out + '_' + name + '.txt'; np.savetxt(fn, arr, header=header, fmt='%.10e'); files.append(fn)
# (1) centre
y0 = T([1e-4, 2e-4]); F0 = phys(T([0.0, 0.0]), y0); z0 = cpu(F0['Ox']); g_est = z0 / cpu(y0)
rep.append('(1) a0 (stored) = %.6f; g = Omega_xy(0) ~ Omega_x(0, y)/y at y = 1e-4, 2e-4: %.8f, %.8f (exact centre coefficient: see jetratio.py / the verifier); beta = %.3f' % (a0, g_est[0], g_est[1], beta))
# (2) horizontal axis
xa = np.logspace(-4, 8, nx); X = T(xa); E0 = torch.zeros_like(X)
Fa = F_at(X, E0); V = cpu(Fa['W1']); tau = cpu(Fa['Thy'])
Fp = F_at(X * (1 + dfd), E0); Fm = F_at(X * (1 - dfd), E0)
U1x = cpu((Fp['U1'] - Fm['U1']) / (2 * dfd * X))
save('axis_h', 'x  V=W1(x,0)  tau=Theta_y(x,0)  U1_x(x,0) [central FD, relative step %g]' % dfd, np.c_[xa, V, tau, U1x])
i = int(np.argmax(U1x)); above = xa[U1x > 2 + 1e-9]
rep.append('(2) horizontal axis, %d points x in [1e-4, 1e8]: V > 0 %s (min V %.6e at x %.3e); tau > 0 %s (min tau %.6e at x %.3e); max U1_x(x, 0) = %.10f at x = %.4e; U1_x > 2 + 1e-9 at %d points%s; U1_x at the smallest x: %.10f (limit 2 at the centre)' % (
    nx, 'holds on the samples' if (V > 0).all() else 'FAILS', V.min(), xa[np.argmin(V)], 'holds on the samples' if (tau > 0).all() else 'FAILS', tau.min(), xa[np.argmin(tau)], U1x[i], xa[i], len(above), (' (x from %.3e to %.3e)' % (above.min(), above.max())) if len(above) else '', U1x[0]))
# (3) half plane
r = np.logspace(-4, 8, 241); ph = (np.arange(73) + 0.5) * (math.pi / 2) / 73
R_, P_ = np.meshgrid(r, ph, indexing='ij'); xp = T((R_ * np.cos(P_)).ravel()); yp = T((R_ * np.sin(P_)).ravel())
Fh = phys(xp, yp); q = cpu(a0 * Fh['eta'] / Fh['y']); Amin = float(Fh['A'].min())
j = int(np.argmin(q)); rr = R_.ravel(); pp = np.degrees(P_.ravel())
rep.append('(3) Theta / y on the polar grid 241 x 73 (r 1e-4 .. 1e8, phi (0, 90) deg): min %.6e at (r %.3e, phi %.2f deg), %s; Theta = a0 eta with eta > 0 for y > 0 identically where A = G_x,eta > 0 (sampled min A %.6f)' % (q.min(), rr[j], pp[j], 'Theta > 0 holds on the samples' if q.min() > 0 else 'FAILS', Amin))
save('half_plane', 'r  phi_deg  Theta/y  A', np.c_[rr, pp, q, cpu(Fh['A'])])
# (4) graph of G_T: all lines in ONE batched root inversion, then all graph points in one more (the per-point calls were too slow: 03:1xZ)
yl = np.logspace(-4, 7, ny); nl = len(lines)
XL = T(np.repeat(lines, ny)); YL = T(np.tile(yl, nl)); FL = phys(XL, YL)
Thx_all = cpu(FL['Thx']).reshape(nl, ny); Om_all = cpu(FL['Om']).reshape(nl, ny)
def zeros_of(v):
    sg = np.sign(v); ch = np.where(sg[1:] * sg[:-1] < 0)[0]
    return [float(np.exp(np.interp(0.0, [v[k], v[k + 1]], [np.log(yl[k]), np.log(yl[k + 1])]))) for k in ch], sg[0], sg[-1]
info = []
for li, xv in enumerate(lines):
    zT, sT0, sT1 = zeros_of(Thx_all[li]); zO, _, _ = zeros_of(Om_all[li]); info.append((xv, zT, sT0, sT1, zO))
good = [(li, xv, zT[0]) for li, (xv, zT, _, _, _) in enumerate(info) if zT]
px = []; py = []
for li, xv, ys in good: px += [xv, xv, xv, xv * (1 + dfd), xv * (1 - dfd)]; py += [ys, ys * (1 + dfd), ys * (1 - dfd), ys, ys]
PG = phys(T(px), T(py)); keys = ['Thy', 'W2', 'Thx', 'U2', 'eta']; G = {k: cpu(PG[k]).reshape(len(good), 5) for k in keys}
rows = []; U2x_all = []
for li, (xv, zT, sT0, sT1, zO) in enumerate(info):
    if not zT:
        rows.append([xv, np.nan] + [np.nan] * 7); rep.append('(4) line x = %g: NO Theta_x sign change on the samples' % xv); continue
    gi = [g[0] for g in good].index(li); ys = zT[0]
    Thy = G['Thy'][gi, 0]; W2 = G['W2'][gi, 0]; Thxy = (G['Thx'][gi, 1] - G['Thx'][gi, 2]) / (2 * dfd * ys); U2x = (G['U2'][gi, 3] - G['U2'][gi, 4]) / (2 * dfd * xv)
    Thx_res = G['Thx'][gi, 0]; U2x_all.append(U2x)
    rows.append([xv, ys, zO[0] if zO else np.nan, Thy, W2, Thxy, U2x, len(zT), len(zO)])
    rep.append('(4) line x = %g: Theta_x zero y* = %.6f (%d change(s), signs %+d -> %+d; Theta_x at y* after interpolation %.2e), Omega zero %s (%d change(s)); at (x, y*): Theta_y %.6e (%s), W2 %.6e (%s), Theta_xy %.6e (%s), U2_x %.6e (%s)' % (
        xv, ys, len(zT), sT0, sT1, Thx_res, ('%.6f' % zO[0]) if zO else 'none', len(zO), Thy, '> 0' if Thy > 0 else 'NOT > 0', W2, '> 0' if W2 > 0 else 'NOT > 0', Thxy, '> 0' if Thxy > 0 else 'NOT > 0', U2x, '< 0' if U2x < 0 else '>= 0'))
save('graph', 'x  y*(Theta_x=0)  y(Omega=0)  Theta_y  W2  Theta_xy  U2_x  n_changes_Theta_x  n_changes_Omega', np.array(rows))
if U2x_all: rep.append('(4) over the %d sampled graph points: min U2_x %.6e, max U2_x %.6e; Theta_xy > 0 at all sampled graph points: %s; U2_x < 0 somewhere: %s' % (len(U2x_all), min(U2x_all), max(U2x_all), all(r_[5] > 0 for r_ in rows if not np.isnan(r_[5])), min(U2x_all) < 0))
# (5) vertical axis
yv = np.logspace(-4, 8, ny); Yv = T(yv); h = hrel * torch.clamp(Yv, min=0.1)
F0 = phys(torch.zeros_like(Yv), Yv); F1 = phys(h, Yv); F2 = phys(2 * h, Yv)
z = cpu(F0['Ox']); z_fd = cpu((8 * F1['Om'] - F2['Om']) / (6 * h))
s = cpu((8 * F1['Thx'] - F2['Thx']) / (6 * h)); s_fd = cpu(a0 * (16 * (F1['eta'] - F0['eta']) - (F2['eta'] - F0['eta'])) / (6 * h ** 2))
C = cpu((16 * (F1['U2'] - F0['U2']) - (F2['U2'] - F0['U2'])) / (6 * h ** 2))
save('axis_v', 'y  z=Omega_x(0,y)  s=Theta_xx(0,y)[FD of Theta_x]  C=U2_xx(0,y)[FD]  z_fd[FD of Omega]  s_fd[FD of a0 eta]', np.c_[yv, z, s, C, z_fd, s_fd])
def first(mask): 
    w = np.where(mask)[0]; return (yv[w[0]], w[0]) if len(w) else (np.inf, -1)
yC, iC = first(a0 * C < 0); ys_, is_ = first(s > 0); yz, iz = first(z > 0)
rep.append('(5) vertical axis, %d points y in [1e-4, 1e8]: y_C = inf{a0 C < 0} = %.6f (previous sample %.6f), y_s = inf{s > 0} = %.6f (prev %.6f), y_z = inf{z > 0} = %.6f (prev %.6f); order 0 < y_C < y_s < y_z: %s; s takes both signs: %s (min %.4e, max %.4e); C takes both signs: %s (min %.4e, max %.4e); z: min %.4e, max %.4e; sign runs (changes) s: %d, C: %d, z: %d' % (
    ny, yC, yv[iC - 1] if iC > 0 else np.nan, ys_, yv[is_ - 1] if is_ > 0 else np.nan, yz, yv[iz - 1] if iz > 0 else np.nan, 'holds on the samples' if 0 < yC < ys_ < yz else 'FAILS',
    (s.min() < 0 < s.max()), s.min(), s.max(), (C.min() < 0 < C.max()), C.min(), C.max(), z.min(), z.max(), int((np.sign(s[1:]) != np.sign(s[:-1])).sum()), int((np.sign(C[1:]) != np.sign(C[:-1])).sum()), int((np.sign(z[1:]) != np.sign(z[:-1])).sum())))
agree_far = np.where((np.abs(z - z_fd) / np.maximum(np.abs(z), 1e-300) > 1e-2))[0]
rep.append('(5) FD cross-checks: |z - z_fd|/|z| > 1 percent first at y = %s; |s - s_fd|/|s| > 1 percent at %d of %d heights (first %s); the far-field values of s and C are finite-difference estimates whose accuracy is not established beyond y ~ 1e3 (the numerical report 3.26 addendum)' % (
    ('%.3e' % yv[agree_far[0]]) if len(agree_far) else 'never', int((np.abs(s - s_fd) / np.maximum(np.abs(s), 1e-300) > 1e-2).sum()), ny, ('%.3e' % yv[np.where(np.abs(s - s_fd) / np.maximum(np.abs(s), 1e-300) > 1e-2)[0][0]]) if (np.abs(s - s_fd) / np.maximum(np.abs(s), 1e-300) > 1e-2).any() else 'never'))
if is_ >= 0:
    dd = 1e-3; PU = cpu(phys(T([0.0, 0.0, 0.0]), T([ys_ * (1 + dd), ys_, ys_ * (1 - dd)]))['U2'])
    U2yy = (PU[0] - 2 * PU[1] + PU[2]) / (dd * ys_) ** 2
    rep.append('(5) U2_yy(0, y_s) at the sampled y_s = %.6f: %.6e (%s; second difference, relative step %g)' % (ys_, U2yy, '> 0' if U2yy > 0 else 'NOT > 0', dd))
rep.append('files: ' + ', '.join('%s sha256 %s' % (f, hashlib.sha256(open(f, 'rb').read()).hexdigest()) for f in files))
txt = 'state %s  a0 %.4f  beta %.3f  nx %d ny %d hrel %g d %g\n' % (sys.argv[1], a0, beta, nx, ny, hrel, dfd) + '\n'.join(rep) + '\n'
open(out + '_summary.txt', 'w').write(txt); print(txt)
