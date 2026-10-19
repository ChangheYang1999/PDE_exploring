"""Hard manufactured test of the paired-ray quadrature (referee request): a growing field with the candidate's exponent, a narrow annular
bump at r0 (width w) and a high angular mode 2m:
   rho = x^2 y g(r) [1 + eps b(r) cos(2 m theta)],  g = (1+r^2)^((k-3)/2),  b = exp(-((r-r0)/w)^2).
Reference: psi by 1D modal Green integrals (scipy quad) of the exact source modes; U = grad^perp psi.
Usage: python3 src/raytest_hard.py [cfg] [m] [r0] [w] [eps]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import raycheck as rc
from scipy.integrate import quad
k = rc.KG
cfgstr = sys.argv[1] if len(sys.argv) > 1 else 'Smax:1e18,smode:adapt,phimax:0.02'
m = int(sys.argv[2]) if len(sys.argv) > 2 else 50
r0 = float(sys.argv[3]) if len(sys.argv) > 3 else 8.6
w = float(sys.argv[4]) if len(sys.argv) > 4 else 0.1
eps = float(sys.argv[5]) if len(sys.argv) > 5 else 0.1

def f_hard(x, y):
    r2 = x * x + y * y; r = torch.sqrt(r2); th = torch.atan2(y, x)
    g = (1 + r2) ** ((k - 3) / 2); gp = (k - 3) * r * (1 + r2) ** ((k - 5) / 2)
    b = torch.exp(-((r - r0) / w) ** 2); bp = -2 * (r - r0) / w ** 2 * b
    c2 = torch.cos(2 * m * th); s2 = torch.sin(2 * m * th)
    A = 1 + eps * b * c2
    A_x = eps * (bp * (x / r) * c2 + b * (-2 * m * s2) * (-y / r2))
    return 2 * x * y * g * A + x * x * y * gp * (x / r) * A + x * x * y * g * A_x

# modes of rho: rho = r^3 g (sin t + sin 3t)/4 * (1 + eps b cos 2mt); (sin t + sin 3t) cos 2mt = 1/2[sin(2m+1)t - sin(2m-1)t + sin(2m+3)t - sin(2m-3)t]
g = lambda s: (1 + s * s) ** ((k - 3) / 2)
gp = lambda s: (k - 3) * s * (1 + s * s) ** ((k - 5) / 2)
b = lambda s: math.exp(-((s - r0) / w) ** 2)
bp = lambda s: -2 * (s - r0) / w ** 2 * b(s)
base = lambda s: s ** 3 * g(s) / 4
basep = lambda s: (3 * s * s * g(s) + s ** 3 * gp(s)) / 4
modes = {1: (lambda s: base(s), lambda s: basep(s)), 3: (lambda s: base(s), lambda s: basep(s))}
for ell, sg in ((2 * m + 1, 1), (2 * m - 1, -1), (2 * m + 3, 1), (2 * m - 3, -1)):
    modes[ell] = (lambda s, sg=sg: sg * eps / 2 * base(s) * b(s), lambda s, sg=sg: sg * eps / 2 * (basep(s) * b(s) + base(s) * bp(s)))
# source modes f_n (sin nt): from each ell: 1/2 (b' - ell b/r) -> n = ell+1 ; 1/2 (b' + ell b/r) -> n = ell-1
fn = {}
for ell, (bl, blp) in modes.items():
    def add(n, fun):
        fn.setdefault(n, []).append(fun)
    add(ell + 1, lambda s, bl=bl, blp=blp, ell=ell: 0.5 * (blp(s) - ell * bl(s) / s))
    if ell - 1 >= 2:
        add(ell - 1, lambda s, bl=bl, blp=blp, ell=ell: 0.5 * (blp(s) + ell * bl(s) / s))
    # ell = 1 gives n = 0 term: 1/2 (b_1' + b_1/r) sin(0) = 0
def fsum(n):
    fl = fn[n]
    return lambda s: sum(f(s) for f in fl)
pts = [r0 - 4 * w, r0 - w, r0, r0 + w, r0 + 4 * w]
def psi_parts(n, r):
    f = fsum(n)
    def Q(fun, a, bnd):
        p = [q for q in pts if a < q < bnd] if np.isfinite(bnd) else None
        if np.isfinite(bnd):
            return quad(fun, a, bnd, points=p if p else None, epsabs=1e-16, epsrel=1e-13, limit=500)[0]
        # infinite: split at pts above a and at 10 r, then to infinity
        cuts = sorted(set([q for q in pts if q > a] + [max(10 * r, a * 2)]))
        tot = 0; lo = a
        for c in cuts:
            tot += quad(fun, lo, c, epsabs=1e-16, epsrel=1e-13, limit=500)[0]; lo = c
        return tot + quad(fun, lo, np.inf, epsabs=1e-16, epsrel=1e-13, limit=500)[0]
    A = Q(lambda s: s ** (n + 1) * f(s), 0, r)
    B = Q(lambda s: s ** (1 - n) * f(s), r, np.inf)
    psi_n = (r ** (-n) * A + r ** n * B) / (2 * n)
    dpsi_n = (-n * r ** (-n - 1) * A + n * r ** (n - 1) * B) / (2 * n)
    return psi_n, dpsi_n
def U_ref(X):
    out = np.zeros((len(X), 2))
    for i, (x, y) in enumerate(X):
        r = math.hypot(x, y); t = math.atan2(y, x); psi_r = psi_t = 0.0
        for n in sorted(fn):
            pn, dpn = psi_parts(n, r)
            psi_r += dpn * math.sin(n * t); psi_t += pn * n * math.cos(n * t)
        psi_x = math.cos(t) * psi_r - math.sin(t) * psi_t / r
        psi_y = math.sin(t) * psi_r + math.cos(t) * psi_t / r
        out[i] = (-psi_y, psi_x)
    return out
X = np.array([[8.598, 0.0352], [8.3, 0.5], [8.6, 2.0], [0.1, 0.05], [1.0, 0.3], [20.0, 5.0], [55.54, 83.12], [19.5, 98.05], [58.5, 294.2]])
Uex = U_ref(X)
print('hard test: m = %d, r0 = %g, w = %g, eps = %g; modes n = %s' % (m, r0, w, eps, sorted(fn)))
# sanity: f_hard vs FD of rho (Cartesian) at a few points
dev = rc.dev
def rho_t(x, y):
    r2 = x * x + y * y; r = torch.sqrt(r2); th = torch.atan2(y, x)
    return x * x * y * (1 + r2) ** ((k - 3) / 2) * (1 + eps * torch.exp(-((r - r0) / w) ** 2) * torch.cos(2 * m * th))
xt = torch.tensor(X[:, 0], device=dev); yt = torch.tensor(X[:, 1], device=dev); h = 1e-6
fd = (rho_t(xt + h, yt) - rho_t(xt - h, yt)) / (2 * h)
print('f_hard vs FD: max rel %.1e' % ((f_hard(xt, yt) - fd).abs() / f_hard(xt, yt).abs().clamp(min=1e-12)).max().item())
rc.set_knots(np.array([r0 - 3 * w, r0 - 2 * w, r0 - w, r0, r0 + w, r0 + 2 * w, r0 + 3 * w]))   # tell the marching rule where the fine structure is
for c in cfgstr.split(';'):
    cfg = rc.parse_cfg(c)
    U, cnt = rc.ray_velocity(f_hard, X, cfg)
    err = np.abs(U - Uex)
    print('cfg %s: nodes/target %d; max|dU| %.2e, max rel %.2e' % (c, int(np.mean(cnt)), err.max(), (np.hypot(err[:, 0], err[:, 1]) / np.hypot(Uex[:, 0], Uex[:, 1])).max()))
    for i in range(len(X)):
        print('   (%.3f, %.3f) U_ref (%.12e, %.12e) dU (%.1e, %.1e)' % (X[i, 0], X[i, 1], Uex[i, 0], Uex[i, 1], U[i, 0] - Uex[i, 0], U[i, 1] - Uex[i, 1]))
