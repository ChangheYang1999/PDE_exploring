"""Verifier's independent solver (verifier): dynamic rescaling rho_tau = rho - W.grad rho, W = c_l X + U,
c_l(tau) = (1 + c(tau))/3, c = psi_xy(0) = int f_3 r^{-2} dr (formula C3), on a log-polar grid.

Representation: rho = sum_{m odd <= M} f_m(r) sin(m t) (parity built in), f_m on a uniform grid in u = log r, r in [r0, R].
U: verifier's gauge-fixed polar inverse (vfast.FastInverse). u-derivative: 8-point upwind-biased finite differences
(7th order), choosing the bias by the sign of the radial speed W_r/r at each collocation point. theta: collocation at
Nt >= 3M/2 equispaced points, modes recovered by discrete sine projection. Ghost values: r < r0 from the exact center jet
rho = x^2 y (f_1 = f_3 = r^3/4, i.e. a(0) = 1), which is the inflow data at the inner circle near the y-axis;
r > R from the far-field power law f_m(R) (r/R)^k, k = 1/c_l (outflow everywhere at r = R).
Time stepping: classical RK4. Optional exponential filter in m.
"""
import sys, json, time
import numpy as np
from vpolar import LogGrid
from vfast import FastInverse


def fd_weights(offsets, h, order=1):
    xs = np.asarray(offsets, float) * h
    V = np.vander(xs, len(xs), increasing=True)
    return np.linalg.inv(V)[order] * (1 if order == 1 else 2)


class DR:
    def __init__(self, N=400, r0=1e-5, R=1e3, M=31, Nt=None, filt=None):
        self.g = LogGrid(N, r0, R)
        self.N = N
        self.M = M
        self.ms = np.arange(1, M + 1, 2)
        self.Mh = len(self.ms)
        self.Nt = Nt or int(np.ceil(3 * (M + 1) / 4) * 4)   # full circle: 3/2-rule for modes <= M
        self.th = 2 * np.pi * np.arange(self.Nt) / self.Nt
        self.S = np.sin(np.outer(self.ms, self.th))        # (Mh, Nt)
        self.C = np.cos(np.outer(self.ms, self.th))
        self.P = self.S * (2.0 / self.Nt)                   # projection
        self.nmax = M + 1
        self.ns = np.arange(2, self.nmax + 1, 2)
        self.Sn = np.sin(np.outer(self.ns, self.th))
        self.Cn = np.cos(np.outer(self.ns, self.th))
        self.inv = FastInverse(self.g, self.nmax)
        h = self.g.h
        self.wp = fd_weights(range(-4, 4), h)   # bias left (for positive speed)
        self.wm = fd_weights(range(-3, 5), h)   # bias right (for negative speed)
        self.r = self.g.r
        self.ghost_lo = 4
        self.ghost_hi = 4
        rl = self.r[0] * np.exp(-h * np.arange(self.ghost_lo, 0, -1))
        self.jet_lo = np.zeros((self.Mh, self.ghost_lo))
        self.jet_lo[0] = rl ** 3 / 4
        if self.Mh > 1:
            self.jet_lo[1] = rl ** 3 / 4
        self.rh_ratio = np.exp(h * np.arange(1, self.ghost_hi + 1))
        self.filt = None
        if filt:
            self.filt = np.exp(-filt[0] * (self.ms / M) ** filt[1])[:, None]
        self.beta_lo = np.maximum(self.ms, 3).astype(float)
        self.hv = None   # angular hyperviscosity (rate, p): mode m is damped by exp(-rate dt (m/M)^(2p)) per step
        self.ghost_follow_k = False   # if True, the outer ghosts use the same exponent k as the velocity tail
        # inner outflow closure: at angles where the radial speed at r0 is negative (outflow through the inner circle), the
        # bias-right stencil must not read the jet ghosts. If True, the first three points use ghost-free upwind stencils
        # with offsets [0,2], [-1,2], [-2,3] (orders 2, 3, 5; s = r+2, r+1, r+1 upwind/downwind points, Iserles-stable).
        self.inner_outflow_free = False
        self.cl_fixed = None          # if set, c_l is frozen at this value (diagnostic: removes the c_l(tau) coupling)
        self.wm_b = [fd_weights(range(-j, (2 if j < 2 else 3) + 1), h) for j in range(3)]

    def velocity(self, F, k):
        r = self.r
        A = F[:, -1] / r[-1] ** k
        p, dp, c = self.inv.solve(F, (A, k), (F[:, 0], self.beta_lo))
        psr = dp.T @ self.Sn                          # (N, Nt)
        pst = (self.ns[:, None] * p).T @ self.Cn
        return psr, pst, c

    def rhs(self, F, k_prev=None, want=False):
        r = self.r[:, None]
        # c and c_l first (needs tail exponent: iterate once with previous k)
        k = k_prev if k_prev is not None else 0.7
        psr, pst, c = self.velocity(F, k)
        cl = (1 + c) / 3 if self.cl_fixed is None else self.cl_fixed
        rho = F.T @ self.S                            # (N, Nt)
        rho_t = (F * self.ms[:, None]).T @ self.C
        # u-derivative with ghosts, per mode then on grid
        kk = k if self.ghost_follow_k else (1.0 / cl if cl > 1 else k)
        Fhi = F[:, -1:] * self.rh_ratio[None, :] ** kk
        Fe = np.concatenate([self.jet_lo, F, Fhi], axis=1)   # (Mh, N+8)
        Ne = Fe.shape[1]
        j0 = self.ghost_lo
        idx = np.arange(self.N) + j0
        Dp = sum(self.wp[q] * Fe[:, idx + (q - 4)] for q in range(8))
        Dm = sum(self.wm[q] * Fe[:, idx + (q - 3)] for q in range(8))
        if self.inner_outflow_free:
            for j, w in enumerate(self.wm_b):
                Dm[:, j] = F[:, 0:len(w)] @ w     # offsets -j..(len(w)-1-j) about point j
        Ur = -pst / r
        Ut = psr
        spd = cl + Ur / r                             # du/dtau
        rho_u = np.where(spd > 0, Dp.T @ self.S, Dm.T @ self.S)
        Rgrid = rho - spd * rho_u - (Ut / r) * rho_t  # = rho - W.grad rho
        G = Rgrid @ self.P.T                          # (N, Mh)
        if want:
            Xg = rho_u
            Ug = Ur * rho_u / r + Ut * rho_t / r
            return G.T, cl, c, dict(rho=rho, R=-Rgrid, norm=np.abs(rho) + np.abs(cl * Xg) + np.abs(Ug), spd=spd,
                                    Ur=Ur, Ut=Ut, psr=psr, pst=pst, rho_u=rho_u, rho_t=rho_t)
        return G.T, cl, c

    def dt_cfl(self, F, cfl, k):
        _, cl, c, d = self.rhs(F, k, want=True)
        r = self.r[:, None]
        su = np.abs(d['spd']).max()
        st = np.abs(d['Ut'] / r).max()   # d theta/d tau = W_theta/r = U_theta/r, U_theta = psi_r
        return cfl / max(su / self.g.h, st * self.M), cl

    def step(self, F, dt, k):
        k1, cl, _ = self.rhs(F, k)
        k2, _, _ = self.rhs(F + 0.5 * dt * k1, k)
        k3, _, _ = self.rhs(F + 0.5 * dt * k2, k)
        k4, _, _ = self.rhs(F + dt * k3, k)
        Fn = F + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if self.filt is not None:
            Fn = Fn * self.filt
        if self.hv is not None:
            Fn = Fn * np.exp(-self.hv[0] * dt * (self.ms / self.M) ** (2 * self.hv[1]))[:, None]
        return Fn, cl

    def init_field(self, L2, k0):
        r = self.r
        F = np.zeros((self.Mh, self.N))
        prof = (1 + r ** 2 / L2) ** ((k0 - 3) / 2)
        F[0] = r ** 3 / 4 * prof
        F[1] = r ** 3 / 4 * prof
        return F


def diagnostics(dr, F, k):
    G, cl, c, d = dr.rhs(F, k, want=True)
    r = dr.r
    out = dict(cl=cl, c=c, ident=3 * cl - c - 1)
    for (a, b) in ((1e-3, 1.0), (1.0, 10.0), (10.0, 100.0)):
        sel = (r >= a) & (r <= b)
        R = d['R'][sel]
        out[f'res[{a:g},{b:g}]'] = float(np.abs(R).max() / d['norm'][sel].max())
    # a(0) proxy: f_3 / (r^3/4) at small r
    out['a0_proxy'] = float(F[1, 20] / (r[20] ** 3 / 4))
    # x-axis: W_1(x,0) = (c_l r + U_r) at theta = 0 -> find first sign change of spd at theta=0
    s0 = d['spd'][:, 0]
    ch = np.where((s0[:-1] < 0) & (s0[1:] >= 0))[0]
    if len(ch):
        j = ch[0]
        xs = r[j] - s0[j] * (r[j + 1] - r[j]) / (s0[j + 1] - s0[j])
        out['x_star'] = float(xs)
    return out, G


if __name__ == '__main__':
    cfg = json.loads(sys.argv[1])
    dr = DR(N=cfg.get('N', 400), r0=cfg.get('r0', 1e-5), R=cfg.get('R', 1e3), M=cfg.get('M', 31),
            Nt=cfg.get('Nt'), filt=cfg.get('filt'))
    F = dr.init_field(cfg.get('L2', 4.67), cfg.get('k0', 0.67))
    if cfg.get('restart'):
        F = np.load(cfg['restart'])['F']
    tau, tmax, cfl = 0.0, cfg.get('tmax', 20.0), cfg.get('cfl', 0.5)
    k = cfg.get('k0', 0.67)
    out = cfg['out']
    t_wall = time.time()
    nstep = 0
    dt, cl = dr.dt_cfl(F, cfl, k)
    while tau < tmax:
        if nstep % 20 == 0:
            dt, cl = dr.dt_cfl(F, cfl, k)
            if cl > 1:
                k = 1 / cl
        F, cl = dr.step(F, dt, k)
        tau += dt
        nstep += 1
        if nstep % cfg.get('every', 200) == 0 or tau >= tmax:
            dg, G = diagnostics(dr, F, k)
            dg.update(tau=tau, step=nstep, dt=dt, wall=time.time() - t_wall, maxF=float(np.abs(F).max()),
                      Gmax=float(np.abs(G).max()))
            print(json.dumps(dg), flush=True)
            np.savez(out, F=F, tau=tau, r=dr.r, ms=dr.ms, cfg=json.dumps(cfg))
            if not np.isfinite(F).all():
                break
