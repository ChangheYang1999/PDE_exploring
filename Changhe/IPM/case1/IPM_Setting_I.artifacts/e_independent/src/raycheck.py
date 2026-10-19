"""Independent real-space velocity check by the paired-ray formula (no modes, no disk, no closure):
  U(X) = (1/2pi) int_0^pi (-sin phi, cos phi) int_0^inf [f(X + s e_phi) - f(X - s e_phi)] ds dphi,  f = d_x rho,
which is grad^perp of psi = (1/2pi) int log(1/|X-Y|) f(Y) dY written in target-centred polar coordinates (the kernel singularity cancels
against the area element); the pairing of opposite rays makes the s-integral absolutely convergent for f = O(|Y|^(k-1)), k < 1, and gives
U = O(|X|^k) with U(0) = 0: the canonical sublinear inverse of SPEC (V1)/(V2).
Quadrature: composite Gauss-Legendre in s on each ray with breakpoints clustered geometrically at s = 0 (target) and at s = |X . e_phi| (the
closest approach to the origin), plus the y-axis crossing; truncated at S_max with the paired tail O(|X| S_max^(k-1)); angular integral by
composite Gauss-Legendre with breakpoints clustered at the direction from X to the origin (or by the midpoint trapezoid rule).
Usage:
  python3 src/raycheck.py test_decay                 # rho = (2r^2-4) y e^{-r^2}: closed-form U
  python3 src/raycheck.py test_grow                  # rho = x^2 y (1+r^2)^{(k-3)/2}, k = 0.17933: U from 1D modal integrals (scipy quad)
  python3 src/raycheck.py cand <shape.npz> <fields.npz> <out.json> [cfg=...]   # candidate at export nodes
cfg string: key:value pairs separated by commas: ngl, ratio, smin, dmin, Smax, phimode (gl|trap), nphi (trap), amin, nglphi.
"""
import sys, json, time, math
import numpy as np, torch
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # rayshape.py lives next to this file
from rayshape import load_shape, ShapeEval, DT

dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
DEFAULT = dict(ngl=16, ratio=1.5, smin=1e-3, dmin=1e-3, Smax=1e15, phimode='gl', nphi=2048, amin=1e-4, nglphi=16, smode='geo', ang=0.03, kfac=2.0, phimax=0.0, lookahead=1, chunk=4000000, pcluster=0, xstar=0.0)


def parse_cfg(s):
    cfg = dict(DEFAULT)
    if s:
        for kv in s.split(','):
            k, v = kv.split(':')
            cfg[k] = type(DEFAULT[k])(v) if not isinstance(DEFAULT[k], str) else v
    return cfg


def gl_panels(breaks, ngl):
    xg, wg = np.polynomial.legendre.leggauss(ngl)
    a = breaks[:-1][:, None]; b = breaks[1:][:, None]
    s = (a + b) / 2 + (b - a) / 2 * xg[None, :]
    w = (b - a) / 2 * wg[None, :]
    return s.ravel(), w.ravel()


def geometric(lo, hi, ratio):
    """lo, lo*ratio, ... <= hi (lo > 0)."""
    n = int(np.floor(np.log(hi / lo) / np.log(ratio))) + 1
    return lo * ratio ** np.arange(n)


def ray_breaks(X, e, cfg):
    """Breakpoints in s > 0 for the pair of rays X +- s e."""
    Smax = cfg['Smax']
    br = [np.array([0.0]), geometric(cfg['smin'], Smax, cfg['ratio']), np.array([Smax])]
    sc = abs(float(X @ e))            # closest approach to the origin along one of the two rays
    if sc > 0:
        g = geometric(cfg['dmin'], max(sc, cfg['dmin']) * 1.0001, cfg['ratio'])
        br.append(sc - g[g < sc]); br.append(sc + geometric(cfg['dmin'], Smax, cfg['ratio']))
        br.append(np.array([sc]))
    if abs(e[0]) > 1e-14:             # y-axis crossing of one of the rays
        br.append(np.array([abs(X[0] / e[0])]))
    b = np.concatenate(br)
    b = b[(b >= 0) & (b <= Smax)]
    b = np.unique(np.round(b, 14))
    # drop near-duplicate breakpoints (relative gap < 1e-9)
    keep = np.r_[True, np.diff(b) > 1e-9 * np.maximum(b[1:], 1e-300)]
    return b[keep]


KNOT_R = None   # physical radii of the spline knots (set by set_knots for the 'adapt' mode)
KNOT_GAP = None
_RMQ = None


def set_knots(kr):
    """Set the knot radii (sorted) and build the sparse table for range-minimum queries over the gaps."""
    global KNOT_R, KNOT_GAP, _RMQ
    KNOT_R = np.sort(np.asarray(kr, float))
    KNOT_GAP = np.diff(KNOT_R)
    tab = [KNOT_GAP.copy()]
    k = 1
    while 2 ** k <= len(KNOT_GAP):
        prev = tab[-1]
        tab.append(np.minimum(prev[:-2 ** (k - 1)], prev[2 ** (k - 1):]))
        k += 1
    _RMQ = tab


def _rmq(a0, a1):
    """min(KNOT_GAP[a0:a1]) for arrays a0 < a1 (vectorised sparse-table query)."""
    ln = a1 - a0
    k = np.floor(np.log2(ln)).astype(int)
    out = np.empty(len(a0))
    for kk in np.unique(k):
        m = k == kk
        t = _RMQ[kk]
        out[m] = np.minimum(t[a0[m]], t[a1[m] - 2 ** kk])
    return out


def knot_spacing(r):
    """Local knot spacing of the radial spline at physical radius r (interpolated), or +inf if KNOT_R is unset."""
    if KNOT_R is None:
        return np.full_like(r, np.inf)
    kr = KNOT_R
    gaps = np.diff(kr)
    idx = np.clip(np.searchsorted(kr, r) - 1, 0, len(gaps) - 1)
    out = gaps[idx]
    out = np.where(r < kr[0], np.inf, out)
    out = np.where(r > kr[-1], np.inf, out)
    return out


def ray_breaks_adapt(X, e, cfg):
    """Marching panelization of s in [0, Smax]: step h(s) = min(ang * r(s) (angular wavelength seen from the origin, only while the
    angle still varies: s < 30|X|), kfac * knot spacing at r(s), ratio-1 times s (geometric growth)), bounded below by smin; plus the
    y-axis crossing. Applied to both rays X +- s e (the step uses the smaller r of the two points)."""
    Smax, ratio, smin = cfg['Smax'], cfg['ratio'], cfg['smin']
    ang, kfac = cfg['ang'], cfg['kfac']
    d = float(np.hypot(*X))
    br = [0.0]
    s = 0.0
    sc = abs(float(X @ e))
    while s < Smax:
        p1 = X + s * e; p2 = X - s * e
        r = min(np.hypot(*p1), np.hypot(*p2))
        h = (ratio - 1) * max(s, smin)
        if s < 30 * d:
            h = min(h, ang * max(r, 1e-3 * d))
        ks = float(knot_spacing(np.array([r]))[0])
        if np.isfinite(ks):
            h = min(h, kfac * ks)
        # do not step across the closest approach to the origin without landing on it
        if s < sc <= s + h:
            h = sc - s if sc - s > 1e-12 * max(sc, 1) else h
        s = s + max(h, smin * 1e-3)
        br.append(min(s, Smax))
    b = np.array(br)
    if abs(e[0]) > 1e-14:
        b = np.r_[b, abs(X[0] / e[0])]
    b = np.unique(b[(b >= 0) & (b <= Smax)])
    keep = np.r_[True, np.diff(b) > 1e-9 * np.maximum(b[1:], 1e-300)]
    return b[keep]


def ray_nodes_adapt_vec(X, e, cfg):
    """Vectorised version of ray_breaks_adapt + gl_panels over all rays e (n,2): returns flat arrays (s, w, ray index).
    Same step rule; the closest approach |X.e| and the y-axis crossing |X_0/e_0| are landed on exactly."""
    Smax, ratio, smin = cfg['Smax'], cfg['ratio'], cfg['smin']
    ang, kfac = cfg['ang'], cfg['kfac']
    d = float(np.hypot(*X))
    n = len(e)
    s = np.zeros(n)
    sc = np.abs(e @ X)
    syc = np.where(np.abs(e[:, 0]) > 1e-14, np.abs(X[0] / np.where(np.abs(e[:, 0]) > 1e-14, e[:, 0], 1.0)), np.inf)
    xg, wg = np.polynomial.legendre.leggauss(cfg['ngl'])
    S, W, RID = [], [], []
    rid = np.arange(n)
    while True:
        active = s < Smax
        if not active.any():
            break
        p1 = X[None, :] + s[:, None] * e; p2 = X[None, :] - s[:, None] * e
        r = np.minimum(np.hypot(p1[:, 0], p1[:, 1]), np.hypot(p2[:, 0], p2[:, 1]))
        h = (ratio - 1) * np.maximum(s, smin)
        h = np.where(s < 30 * d, np.minimum(h, ang * np.maximum(r, 1e-3 * d)), h)
        ks = knot_spacing(r)
        h = np.where(np.isfinite(ks), np.minimum(h, kfac * ks), h)
        h = np.maximum(h, smin * 1e-3)
        if KNOT_R is not None and cfg.get('lookahead', 1):
            # look-ahead: if the radius interval swept by either ray during the step contains knots, shrink the step so that the
            # local rule (kfac x gap) applies from the first knot encountered (prevents jumping over narrow structure). Vectorised:
            # the smallest knot gap inside [lo, hi] by a range-minimum (sparse) table over the gap array.
            ra = np.hypot(p1[:, 0], p1[:, 1]); rb = np.hypot(p2[:, 0], p2[:, 1])
            for _ in range(12):
                q1 = X[None, :] + (s + h)[:, None] * e; q2 = X[None, :] - (s + h)[:, None] * e
                r1b = np.hypot(q1[:, 0], q1[:, 1]); r2b = np.hypot(q2[:, 0], q2[:, 1])
                lo = np.minimum(np.minimum(ra, r1b), np.minimum(rb, r2b)); hi = np.maximum(np.maximum(ra, r1b), np.maximum(rb, r2b))
                i0 = np.searchsorted(KNOT_R, lo); i1 = np.searchsorted(KNOT_R, hi)
                has = i1 > i0
                if not has.any():
                    break
                gmin = np.full(n, np.inf)
                a0 = i0[has]; a1 = np.minimum(i1[has], len(KNOT_R) - 1)       # gap indices a0 .. a1-1 (gap i = KNOT_R[i+1]-KNOT_R[i])
                ok = a1 > a0
                gm = np.full(has.sum(), np.inf)
                if ok.any():
                    gm[ok] = _rmq(a0[ok], a1[ok])
                # a single knot inside the interval with no full gap inside: use the gap at that knot
                single = ~ok
                if single.any():
                    j = np.clip(a0[single], 0, len(KNOT_GAP) - 1)
                    gm[single] = KNOT_GAP[j]
                gmin[has] = gm
                too_big = has & (h > kfac * gmin * 1.0001)
                if not too_big.any():
                    break
                h = np.where(too_big, np.maximum(h / 2, kfac * gmin), h)
        # land on the closest approach and on the y-axis crossing
        for c in (sc, syc):
            gap = c - s
            land = (gap > 1e-12 * np.maximum(c, 1)) & (gap < h)
            h = np.where(land, gap, h)
        s_new = np.minimum(s + h, Smax)
        a = s[active]; b = s_new[active]
        mid = (a + b) / 2; hw = (b - a) / 2
        S.append((mid[:, None] + hw[:, None] * xg[None, :]).ravel())
        W.append((hw[:, None] * wg[None, :]).ravel())
        RID.append(np.repeat(rid[active], len(xg)))
        s = s_new
    return np.concatenate(S), np.concatenate(W), np.concatenate(RID)


def phi_nodes(X, cfg):
    if cfg['phimode'] == 'trap':
        n = cfg['nphi']
        phi = (np.arange(n) + 0.5) * np.pi / n
        return phi, np.full(n, np.pi / n)
    phi0 = math.atan2(-X[1], -X[0])   # direction from X to the origin
    g = geometric(cfg['amin'], np.pi / 2, cfg['ratio'])
    br = np.r_[phi0 - np.pi / 2, phi0 - g[g < np.pi / 2], phi0, phi0 + g[g < np.pi / 2], phi0 + np.pi / 2]
    if cfg.get('pcluster', 0) and cfg.get('xstar', 0) > 0:
        # also cluster at the directions from X to the stagnation points P = (x*, 0) and -P (fine structure of f there), mapped into
        # the interval [phi0 - pi/2, phi0 + pi/2) (the integrand is pi-periodic up to sign)
        for Pt in ((cfg['xstar'], 0.0), (-cfg['xstar'], 0.0)):
            dP = math.hypot(Pt[0] - X[0], Pt[1] - X[1])
            if dP < 1e-6:
                continue
            ph = math.atan2(Pt[1] - X[1], Pt[0] - X[0])
            ph = phi0 - np.pi / 2 + ((ph - (phi0 - np.pi / 2)) % np.pi)
            gP = geometric(cfg['amin'], 0.5, cfg['ratio'])
            br = np.r_[br, ph, ph - gP, ph + gP]
        br = br[(br >= phi0 - np.pi / 2) & (br <= phi0 + np.pi / 2)]
    if cfg['phimax'] > 0:               # bound the panel width everywhere (features of I(phi) away from the origin direction)
        nu = int(np.ceil(np.pi / cfg['phimax']))
        br = np.r_[br, phi0 - np.pi / 2 + np.arange(1, nu) * np.pi / nu]
    br = np.unique(br)
    keep = np.r_[True, np.diff(br) > 1e-7 * cfg['amin']]
    return gl_panels(br[keep], cfg['nglphi'])


def ray_velocity(fcall, targets, cfg, verbose=False):
    """fcall(x, y) -> f (torch tensors on dev). targets: (n,2) numpy. Returns U (n,2) and per-target node counts."""
    targets = np.atleast_2d(np.asarray(targets, float))
    U = np.zeros((len(targets), 2)); counts = []
    for it, X in enumerate(targets):
        phi, wphi = phi_nodes(X, cfg)
        e = np.stack([np.cos(phi), np.sin(phi)], 1)
        if cfg['smode'] == 'adapt':
            S, W, RID = ray_nodes_adapt_vec(X, e, cfg)
        else:
            S, W, RID = [], [], []
            for j in range(len(phi)):
                b = ray_breaks(X, e[j], cfg)
                s, w = gl_panels(b, cfg['ngl'])
                S.append(s); W.append(w); RID.append(np.full(len(s), j))
            S = np.concatenate(S); W = np.concatenate(W); RID = np.concatenate(RID)
        I = np.zeros(len(phi))
        CH = cfg.get('chunk', 4000000)
        for c0 in range(0, len(S), CH):
            sl = slice(c0, c0 + CH)
            st = torch.tensor(S[sl], device=dev); ex = torch.tensor(e[RID[sl], 0], device=dev); ey = torch.tensor(e[RID[sl], 1], device=dev)
            fp = fcall(X[0] + st * ex, X[1] + st * ey); fm = fcall(X[0] - st * ex, X[1] - st * ey)
            g = ((fp - fm) * torch.tensor(W[sl], device=dev)).cpu().numpy()
            np.add.at(I, RID[sl], g)
            del st, ex, ey, fp, fm
        torch.cuda.empty_cache()
        U[it, 0] = -(wphi * np.sin(phi) * I).sum() / (2 * np.pi)
        U[it, 1] = (wphi * np.cos(phi) * I).sum() / (2 * np.pi)
        counts.append(len(S))
        if verbose:
            print('  target %d (%.4g, %.4g): %d rays x ~%d nodes, U = (%.12e, %.12e)' % (it, X[0], X[1], len(phi), len(S) // len(phi), U[it, 0], U[it, 1]), flush=True)
    return U, counts


# ---------------- manufactured tests ----------------
def f_decay(x, y):
    r2 = x * x + y * y
    return x * y * (12 - 4 * r2) * torch.exp(-r2)


def U_decay(X):
    x, y = X[:, 0], X[:, 1]; r2 = x * x + y * y
    return np.stack([-x * (1 - 2 * y * y) * np.exp(-r2), y * (1 - 2 * x * x) * np.exp(-r2)], 1)


KG = 0.17932838093225903


def f_grow(x, y, k=KG):
    r2 = x * x + y * y
    g = (1 + r2) ** ((k - 3) / 2)
    return x * y * g * (2 + (k - 3) * x * x / (1 + r2))


def U_grow_modal(X, k=KG):
    """psi = psi_2 sin 2t + psi_4 sin 4t with f_2 = (4 r^2 g + r^3 g')/4, f_4 = r^3 g'/8, g = (1+r^2)^((k-3)/2);
    psi_n(r) = (1/2n)[r^-n int_0^r s^(n+1) f_n ds + r^n int_r^inf s^(1-n) f_n ds]."""
    from scipy.integrate import quad
    g = lambda s: (1 + s * s) ** ((k - 3) / 2)
    gp = lambda s: (k - 3) * s * (1 + s * s) ** ((k - 5) / 2)
    fn = {2: lambda s: (4 * s * s * g(s) + s ** 3 * gp(s)) / 4, 4: lambda s: s ** 3 * gp(s) / 8}
    out = np.zeros((len(X), 2))
    for i, (x, y) in enumerate(X):
        r = math.hypot(x, y); t = math.atan2(y, x)
        psi_r, psi_t = 0.0, 0.0
        for n in (2, 4):
            A = quad(lambda s: s ** (n + 1) * fn[n](s), 0, r, epsabs=1e-15, epsrel=1e-13, limit=400)[0]
            B = quad(lambda s: s ** (1 - n) * fn[n](s), r, np.inf, epsabs=1e-15, epsrel=1e-13, limit=400)[0]
            psi_n = (r ** (-n) * A + r ** n * B) / (2 * n)
            dpsi_n = (-n * r ** (-n - 1) * A + n * r ** (n - 1) * B) / (2 * n)
            psi_r += dpsi_n * math.sin(n * t); psi_t += psi_n * n * math.cos(n * t)
        psi_x = math.cos(t) * psi_r - math.sin(t) * psi_t / r
        psi_y = math.sin(t) * psi_r + math.cos(t) * psi_t / r
        out[i] = (-psi_y, psi_x)
    return out


def run_tests(which, cfgs):
    if which == 'test_decay':
        X = np.array([[0.3, 0.2], [1.0, 0.5], [2.0, 0.1], [0.05, 1.5], [1.2, 1.1], [-0.7, 0.4], [0.9, -1.3], [3.0, 0.5]])
        Uex = U_decay(X); f = f_decay
    else:
        X = np.array([[0.1, 0.05], [1.0, 0.3], [3.0, 1.0], [8.6, 0.05], [8.6, 1.0], [20.0, 5.0], [100.0, 30.0], [0.5, 2.0]])
        Uex = U_grow_modal(X); f = f_grow
    print('exact/reference U:'); print(Uex)
    for c in cfgs:
        cfg = parse_cfg(c); t0 = time.time()
        U, cnt = ray_velocity(f, X, cfg)
        err = np.abs(U - Uex)
        print('cfg %-60s  nodes/target ~%d  time %.1f s  max|dU| = %.2e  max|dU|/max|U| = %.2e' % (c, int(np.mean(cnt)), time.time() - t0, err.max(), err.max() / np.abs(Uex).max()))
        if len(sys.argv) > 2 and sys.argv[2] == 'v':
            for i in range(len(X)):
                print('   X (%.3g,%.3g) U_ray (%.14e, %.14e) dU (%.1e, %.1e)' % (X[i, 0], X[i, 1], U[i, 0], U[i, 1], U[i, 0] - Uex[i, 0], U[i, 1] - Uex[i, 1]))


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode in ('test_decay', 'test_grow'):
        cfgs = ['ngl:16,ratio:1.5,smin:1e-3,dmin:1e-3,Smax:1e15,phimode:gl,amin:1e-4,nglphi:16',
                'ngl:24,ratio:1.25,smin:1e-4,dmin:1e-4,Smax:1e15,phimode:gl,amin:1e-5,nglphi:24',
                'ngl:16,ratio:1.5,smin:1e-3,dmin:1e-3,Smax:1e15,phimode:trap,nphi:2048',
                'ngl:16,ratio:1.5,smin:1e-3,dmin:1e-3,Smax:1e12,phimode:gl,amin:1e-4,nglphi:16']
        run_tests(mode, cfgs)


def select_targets(d, mode='full'):
    """Export nodes (r index, theta index) near P and at r = 0.1, 1, 20, 100."""
    r, th = d['r'], d['theta']
    xstar = float(d['axis_x'][np.argmin(np.abs(d['axis_w'][(d['axis_x'] > 1)]))]) if False else None
    # x* from the axis data: first zero of w = W1 on the axis beyond r = 1
    ax, aw = d['axis_x'], d['axis_w']
    m = ax > 1
    i0 = np.where(m)[0][np.argmax(aw[m] > 0)]
    xs = ax[i0 - 1] - aw[i0 - 1] * (ax[i0] - ax[i0 - 1]) / (aw[i0] - aw[i0 - 1])
    sel = []
    def nearest(x, y):
        rr = math.hypot(x, y); tt = math.atan2(y, x)
        return int(np.argmin(np.abs(np.log(r) - np.log(rr)))), int(np.argmin(np.abs(th - tt)))
    if mode == 'far':    # the eight r = 100 and r = 300 nodes of the full set (P-clustered rerun, verifier G65 (c) qualifier)
        sel = []
        for rad in [100.0, 300.0]:
            for it in [48, 144, 240, 336]:
                sel.append((int(np.argmin(np.abs(np.log(r) - np.log(rad)))), it))
        return sel, xs
    if mode == 'vary':   # the four nodes of the referee's table plus r = 300 near the y-axis and the near-origin node
        pts = [(xs - 0.0029, 0.0352), (55.5406, 83.1223), (19.5033, 98.0495), (58.5248, 294.2241), (0.0195, 0.0981), (8.5519, 0.1399)]
        return [nearest(x, y) for x, y in pts], xs
    dxs = [-0.3, -0.05, 0.0, 0.05, 0.3] if mode == 'full' else [-0.3, 0.0, 0.3]
    dys = [0.035, 0.07, 0.14, 0.5, 1.0, 2.0] if mode == 'full' else [0.035, 0.14, 1.0]
    for dx in dxs:
        for dy in dys:
            sel.append(nearest(xs + dx, dy))
    sel.append(nearest(xs, 0.0))
    sel.append(nearest(xs, 0.05))                       # lead request 05:52Z: 0.05 above P
    for it in ([48, 144, 240, 336] if mode == 'full' else [96]):   # lead request 05:52Z: r = 300
        sel.append((int(np.argmin(np.abs(np.log(r) - np.log(300.0)))), it))
    for rad in [0.1, 1.0, 20.0, 100.0]:
        for it in ([48, 144, 240, 336] if mode == 'full' else [96, 288]):
            sel.append((int(np.argmin(np.abs(np.log(r) - np.log(rad)))), it))
    sel = list(dict.fromkeys(sel))
    return sel, xs


def run_candidate(shape, fields, out, cfgstr, mode='full'):
    P = load_shape(shape); E = ShapeEval(P, dev)
    kq = np.unique(P['knots'])[1:-1]
    set_knots(np.sqrt((1 - kq) ** (-2 / (1 - P['k'])) - 1) * P['L'])
    d = np.load(fields)
    sel, xs = select_targets(d, mode)
    r, th = d['r'], d['theta']
    ir = np.array([s[0] for s in sel]); it = np.array([s[1] for s in sel])
    X = np.stack([r[ir] * np.cos(th[it]), r[ir] * np.sin(th[it])], 1)
    cfg = parse_cfg(cfgstr)
    cfg['xstar'] = float(xs)
    print('shape %s\nfields %s\ncfg %s\nx* (export axis) %.6f, %d targets' % (shape, fields, cfg, xs, len(X)), flush=True)
    fcall = lambda x, y: E.rho_f(x, y)[1]
    t0 = time.time()
    U, cnt = ray_velocity(fcall, X, cfg, verbose=True)
    U1, U2, RX, RY, DEN, RES = d['U1'], d['U2'], d['rho_x'], d['rho_y'], d['denominator'], d['residual']   # npz arrays: read once
    Ul = np.stack([U1[ir, it], U2[ir, it]], 1)
    dU = U - Ul
    gx, gy = RX[ir, it], RY[ir, it]
    D = DEN[ir, it]
    impact = np.abs(dU[:, 0] * gx + dU[:, 1] * gy) / np.where(D > 0, D, np.inf)
    rows = []
    print('\n%-10s %-10s %-10s | %-16s %-16s | %-16s %-16s | %-9s %-9s %-9s | %-9s %-9s' % ('x', 'y', 'r', 'U1_ray', 'U2_ray', 'U1_lead', 'U2_lead', 'dU1', 'dU2', '|dU|/|U|', 'impact', 'res_lead'))
    for i in range(len(X)):
        rel = np.hypot(*dU[i]) / max(np.hypot(*Ul[i]), 1e-300)
        print('%-10.5f %-10.5f %-10.5f | %-16.10e %-16.10e | %-16.10e %-16.10e | %-9.2e %-9.2e %-9.2e | %-9.2e %-9.2e' % (
            X[i, 0], X[i, 1], r[ir[i]], U[i, 0], U[i, 1], Ul[i, 0], Ul[i, 1], dU[i, 0], dU[i, 1], rel, impact[i], abs(RES[ir[i], it[i]]) / D[i] if D[i] > 0 else float('nan')))
        rows.append(dict(ir=int(ir[i]), it=int(it[i]), x=float(X[i, 0]), y=float(X[i, 1]), U_ray=[float(U[i, 0]), float(U[i, 1])],
                         U_lead=[float(Ul[i, 0]), float(Ul[i, 1])], dU=[float(dU[i, 0]), float(dU[i, 1])], rel=float(rel), impact=float(impact[i]),
                         D=float(D[i]), res_lead=float(RES[ir[i], it[i]]), rho_x=float(gx[i]), rho_y=float(gy[i]), nodes=int(cnt[i])))
    print('\nsummary: max|dU| = %.3e, max |dU|/|U| = %.3e, max residual impact |dU.grad rho|/D = %.3e, median impact %.3e; time %.0f s' % (
        np.abs(dU).max(), max(rw['rel'] for rw in rows), impact.max(), np.median(impact), time.time() - t0))
    json.dump(dict(shape=shape, fields=fields, cfg=cfg, xstar=xs, c_l=float(d['c_l']), rows=rows), open(out, 'w'), indent=1)


if __name__ == '__main__' and sys.argv[1] == 'cand':
    cfgstr = sys.argv[5] if len(sys.argv) > 5 else ''
    mode = sys.argv[6] if len(sys.argv) > 6 else 'full'
    run_candidate(sys.argv[2], sys.argv[3], sys.argv[4], cfgstr, mode)


def run_centre(shape, cfgstr):
    """c = psi_xy(0) from the real-space velocity: U_2(x, 0)/x -> c as x -> 0 (U_2 even in x, odd in y; U_2(x,0) = c x + O(x^3)).
    Richardson extrapolation over x; compared with the identity c = 3 c_l - 1 of the saved state."""
    P = load_shape(shape); E = ShapeEval(P, dev)
    kq = np.unique(P['knots'])[1:-1]
    set_knots(np.sqrt((1 - kq) ** (-2 / (1 - P['k'])) - 1) * P['L'])
    cfg = parse_cfg(cfgstr)
    xs = np.array([4e-3, 2e-3, 1e-3, 5e-4])
    X = np.stack([xs, np.zeros_like(xs)], 1)
    fcall = lambda x, y: E.rho_f(x, y)[1]
    U, cnt = ray_velocity(fcall, X, cfg, verbose=True)
    # U = (-c x, c y) + O(|X|^3): c = -U_1(x,0)/x (U_1 odd in x, even in y); U_2(x,0) = 0 by oddness in y
    c_est = -U[:, 0] / xs
    cid = 3 * P['c_l'] - 1
    print('shape %s: c_l %.10f, identity c = 3 c_l - 1 = %.10f' % (shape, P['c_l'], cid))
    for i in range(len(xs)):
        print('  x = %.1e: -U_1/x = %.12f (diff from identity %+.2e), U_2 = %.1e (0 by parity)' % (xs[i], c_est[i], c_est[i] - cid, U[i, 1]))
    r1 = (4 * c_est[1:] - c_est[:-1]) / 3        # removes the O(x^2) term
    r2 = (16 * r1[1:] - r1[:-1]) / 15            # removes the O(x^4) term
    print('  Richardson x^2: %s' % ' '.join('%.12f (%+.1e)' % (v, v - cid) for v in r1))
    print('  Richardson x^4: %s' % ' '.join('%.12f (%+.1e)' % (v, v - cid) for v in r2))
    print('  c_l from the real-space c: (1 + c)/3 = %.12f vs stored %.12f (difference %+.2e)' % ((1 + r2[-1]) / 3, P['c_l'], (1 + r2[-1]) / 3 - P['c_l']))


if __name__ == '__main__' and sys.argv[1] == 'centre':
    run_centre(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '')
