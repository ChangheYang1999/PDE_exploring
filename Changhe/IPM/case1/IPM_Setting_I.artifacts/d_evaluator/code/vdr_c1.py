"""Re-solve from construct1 with the verifier's dynamic-rescaling solver vdr.DR (lead request 21:01Z), verifier.

Initial data: the construct1 global trial formula (gen_shape.shape_rho on final_shape.npz, physical units) sampled on the
DR log grid, odd sine modes m <= M by exact DST on the closed quadrant. Evolution: rho_tau = rho - W.grad rho,
c_l(tau) = (1 + c(tau))/3 (identity, no fitted c_l), ghost jet x^2 y at r < r0 (a(0) = 1), power-law ghosts at r > R.
Diagnostics: max|rho_tau| absolute and relative to max(|rho| + |c_l X.grad rho| + |U.grad rho|) by radial band and next
to P; c_l, x*, mu1, h(P) = 2 c_l - w'(x*); max change of the modes from the initial data by band.
Usage: python3 vdr_c1.py '{"mode": "check"|"run", "N":.., "r0":.., "R":.., "M":.., "tmax":.., "cfl":.., "out": prefix}'
"""
import sys, json, time
import numpy as np
from scipy.interpolate import CubicSpline
from vdr import DR
from gen_shape import shape_rho

SHAPE = 'final_shape.npz'
BANDS = [[0, 0.01], [0.01, 1], [1, 2], [2, 10], [10, 100], [100, 1e3], [1e3, 1e4], [1e4, 1e9]]


def init_modes(dr, nq=None):
    d = np.load(SHAPE, allow_pickle=True)
    nq = nq or max(2 * dr.M + 2, 642)
    th = np.linspace(0, np.pi / 2, nq)
    rho, H, info = shape_rho(d, dr.r, th)
    rho[:, 0] = 0.0
    dth = th[1] - th[0]
    wq = np.full(nq, dth)
    wq[0] = wq[-1] = 0.5 * dth
    Fall = (4 / np.pi) * rho @ (np.sin(np.outer(np.arange(1, 2 * nq, 2), th)) * wq).T   # (N, all odd modes)
    F = Fall[:, :dr.Mh].T.copy()
    tail = float(np.abs(Fall[:, dr.Mh:]).max() / np.abs(Fall).max()) if Fall.shape[1] > dr.Mh else 0.0
    return F, info, tail


def diag(dr, F, k, F0=None):
    G, cl, c, d = dr.rhs(F, k, want=True)
    r = dr.r
    Rg = d['R']                       # W.grad rho - rho on the collocation grid
    nm = d['norm']
    out = dict(cl=float(cl), c=float(c), ident=float(3 * cl - c - 1), rho_tau_abs=float(np.abs(Rg).max()),
               rho_tau_rel=float(np.abs(Rg).max() / nm.max()))
    trim = 6
    # exact axis points (rho = 0 there by parity) are excluded from pointwise ratios
    offax = np.abs(np.sin(2 * dr.th)) > 1e-9
    for a, b in BANDS:
        sel = (r >= a) & (r < b)
        sel[:trim] = False
        sel[-trim:] = False
        if sel.sum() == 0:
            continue
        R, Nn = Rg[sel], nm[sel]
        mask = (Nn > 1e-8 * Nn.max()) & offax[None, :]
        out['band[%g,%g]' % (a, b)] = [float(np.abs(R).max() / Nn.max()), float((np.abs(R[mask]) / Nn[mask]).max())]
    # axis: w = r * spd at theta = 0, x*, mu1, h(P)
    w = r * d['spd'][:, 0]
    ch = np.where((w[:-1] < 0) & (w[1:] >= 0) & (r[:-1] > 0.5))[0]
    if len(ch):
        j = ch[0]
        sl = slice(max(j - 6, 0), j + 7)
        cs = CubicSpline(r[sl], w[sl])
        rt = cs.roots(extrapolate=False)
        rt = rt[(rt > r[j] - 1e-12) & (rt < r[j + 1] + 1e-12)]
        xs = float(rt[0]) if len(rt) else float(r[j] - w[j] * (r[j + 1] - r[j]) / (w[j + 1] - w[j]))
        mu1 = float(cs(xs, 1))
        out.update(x_star=xs, mu1=mu1, hP=float(2 * cl - mu1))
        # near-P disk |X - P| < 1 (and 0.25) on the collocation grid
        th = dr.th
        X = r[:, None] * np.cos(th)[None, :]
        Y = r[:, None] * np.sin(th)[None, :]
        for rad in (1.0, 0.25):
            m = ((X - xs) ** 2 + Y ** 2 < rad ** 2) | ((X + xs) ** 2 + Y ** 2 < rad ** 2)
            msk = m & (nm > 1e-8 * nm.max()) & offax[None, :]
            if msk.sum():
                out['nearP_%g' % rad] = [float(np.abs(Rg[m]).max() / nm[m].max()), float((np.abs(Rg[msk]) / nm[msk]).max())]
    if F0 is not None:
        dF = np.abs(F - F0).max(0)
        sc = np.abs(F0).max(0) + 1e-300
        out['dF_rel'] = {('%g' % t): float(dF[np.argmin(abs(r - t))] / sc[np.argmin(abs(r - t))]) for t in (0.01, 0.15, 1.5, 4, 8.6, 100)}
    return out, G, w


def save_export(path, dr, F, cl, nq=None):
    nq = nq or (dr.M + 1)
    th = np.linspace(0, np.pi / 2, nq + 1)
    rho = F.T @ np.sin(np.outer(dr.ms, th))
    rho[:, 0] = 0.0
    np.savez(path, r=dr.r, theta=th, rho=rho, c_l=cl)


def main(cfg):
    dr = DR(N=cfg['N'], r0=cfg['r0'], R=cfg['R'], M=cfg['M'], Nt=cfg.get('Nt'), filt=cfg.get('filt'))
    dr.inner_outflow_free = cfg.get('inner_outflow_free', False)
    if cfg.get('hv'):
        dr.hv = tuple(cfg['hv'])
    if cfg.get('cl_fixed'):
        dr.cl_fixed = float(cfg['cl_fixed'])
    F0, info, tail = init_modes(dr)
    k = 1 / info['c_l']
    t0 = time.time()
    o, G, w = diag(dr, F0, k)
    o.update(init_tail_share=tail, t_rhs=time.time() - t0, N=dr.N, M=dr.M, Nt=dr.Nt, r0=float(dr.r[0]), R=float(dr.r[-1]))
    dt, cl = dr.dt_cfl(F0, cfg.get('cfl', 0.5), k)
    o['dt_cfl'] = float(dt)
    print(json.dumps(dict(tau=0.0, **o)), flush=True)
    if cfg.get('mode', 'check') == 'check':
        return
    out = cfg['out']
    np.savez(out + '_F0.npz', F=F0, r=dr.r, ms=dr.ms)
    F = F0.copy()
    tau, nstep, tmax = 0.0, 0, cfg.get('tmax', 5.0)
    t_wall = time.time()
    hist = []
    while tau < tmax:
        if nstep % 20 == 0:
            dt, cl = dr.dt_cfl(F, cfg.get('cfl', 0.5), k)
            if cl > 1:
                k = 1 / cl
        F, cl = dr.step(F, dt, k)
        tau += dt
        nstep += 1
        if nstep % cfg.get('every', 400) == 0 or tau >= tmax:
            o, G, w = diag(dr, F, k, F0)
            o.update(tau=tau, step=nstep, dt=dt, wall=time.time() - t_wall)
            print(json.dumps(o), flush=True)
            hist.append(o)
            np.savez(out + '_F.npz', F=F, tau=tau, r=dr.r, ms=dr.ms, cfg=json.dumps(cfg))
            if cfg.get('snap'):
                np.savez(out + '_snap%05d.npz' % nstep, F=F, tau=tau)
            if not np.isfinite(F).all():
                break
            if time.time() - t_wall > cfg.get('wall_max', 1e9):
                break
    save_export(out + '_export.npz', dr, F, cl)
    json.dump(hist, open(out + '_hist.json', 'w'))


if __name__ == '__main__':
    main(json.loads(sys.argv[1]))
