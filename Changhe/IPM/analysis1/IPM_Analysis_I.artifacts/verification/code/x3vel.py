"""Verifier: canonical full-plane velocity of the X3 trial density, by the exact Green formula in angular modes,
radial integrals by Gauss-Legendre on panels in sigma = log s that are (i) aligned with all spline knots,
(ii) geometrically graded (ratio 1.5, widths <= half the log-distance) toward each target radius, (iii) capped at
width 0.5. No exterior closure: the trial formula is used for all s in [s_min, s_max] = target-dependent with
log-margins 12 (inner) and 60 (outer); the omitted pieces are below 1e-20 relative (see notes).

psi_n(r) = (A_n + B_n)/(4n), psi_n'(r) = (B_n - A_n)/(2r),
A_n(r) = int_0^r (s/r)^{2n} s f_n(s) ds,  B_n(r) = int_r^oo (r/s)^{2n} s f_n(s) ds,  f = d_x rho = sum f_n sin(2 n th).
"""
import numpy as np, torch
from x3rho import Trial

DEV = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
DT = torch.float64


class Modes:
    def __init__(self, T, nth=1024, nmodes=400):
        self.T = T; self.nth = nth; self.nmodes = nmodes
        th = (np.arange(nth) + 0.5) * (np.pi / 2) / nth
        self.th = th
        m = np.arange(T.ang + 1)
        self.cosm = torch.tensor(np.cos(2 * np.outer(m, th)), dtype=DT, device=DEV)
        self.msinm = torch.tensor(-2 * m[:, None] * np.sin(2 * np.outer(m, th)), dtype=DT, device=DEV)
        ct = np.abs(np.cos(th)); st = np.sin(th); p3 = T.p3
        self.A = torch.tensor(ct ** (p3 - 2) * st ** 2, dtype=DT, device=DEV)
        self.A_th = torch.tensor(-(p3 - 2) * ct ** (p3 - 3) * st ** 3 + 2 * ct ** (p3 - 2) * st * np.cos(th), dtype=DT, device=DEV)
        self.c = torch.tensor(np.cos(th), dtype=DT, device=DEV); self.s = torch.tensor(st, dtype=DT, device=DEV)
        n = np.arange(1, nmodes + 1)
        self.S = torch.tensor(np.sin(2 * np.outer(th, n)) * (4 / np.pi) * (np.pi / 2 / nth), dtype=DT, device=DEV)

    def rho_x_grid(self, r):
        """rho_x on r (numpy, (N,)) x th grid; torch (N, nth)."""
        T = self.T
        R = T.radial(r / T.L)
        bm = torch.tensor(R['bm'], dtype=DT, device=DEV); bm_u = torch.tensor(R['bm_u'], dtype=DT, device=DEV)
        sg = torch.tensor(R['sg'], dtype=DT, device=DEV)[:, None]; sg_u = torch.tensor(R['sg_u'], dtype=DT, device=DEV)[:, None]
        base = torch.tensor(R['base'], dtype=DT, device=DEV)[:, None]; base_u = torch.tensor(R['base_u'], dtype=DT, device=DEV)[:, None]
        Hv = base + bm @ self.cosm + sg * self.A[None, :]
        Hr = (base_u + bm_u @ self.cosm + sg_u * self.A[None, :]) / T.L
        Hth = bm @ self.msinm + sg * self.A_th[None, :]
        rr = torch.tensor(r, dtype=DT, device=DEV)[:, None]
        c = self.c[None, :]; s = self.s[None, :]
        x = rr * c; y = rr * s
        Hx = c * Hr - s * Hth / rr
        E = torch.exp(Hv)
        return E * (2 * x * y + x * x * y * Hx)

    def fn(self, r, chunk=4096):
        out = []
        for i0 in range(0, len(r), chunk):
            out.append(self.rho_x_grid(r[i0:i0 + chunk]) @ self.S)
        return torch.cat(out, 0)          # (N, nmodes)


def gl(n):
    return np.polynomial.legendre.leggauss(n)


def target_edges(T, sig_t, w0=1e-5, ratio=1.5, cap=0.5, inner=12.0, outer=60.0):
    lo = min(sig_t, np.log(T.L)) - inner
    hi = max(sig_t, np.log(T.L)) + outer
    pts = [sig_t]
    d = w0
    while d < max(sig_t - lo, hi - sig_t):
        pts += [sig_t - d, sig_t + d]
        d = d * ratio if d * (ratio - 1) < cap else d + cap
    # knots in sigma
    qk = np.unique(T.knots); qk = qk[(qk > 0) & (qk < 1)]
    k = T.k
    uk = np.sqrt(np.expm1(-2 / (1 - k) * np.log1p(-qk)))
    pts += list(np.log(T.L * uk))
    pts += [lo, hi]
    e = np.unique(np.array(pts))
    e = e[(e >= lo) & (e <= hi)]
    return e


def velocity_at(M, r_t, th_t, npt=16, verbose=False, fn=None, edges=None):
    """U1, U2, psi and the n-sums at targets (r_t (nr,), th_t (nt,)) tensor grid. Returns dict of numpy arrays."""
    T = M.T
    xg, wg = gl(npt)
    nm = M.nmodes
    nvec = torch.arange(1, nm + 1, dtype=DT, device=DEV)
    psi_n = np.zeros((len(r_t), nm)); dpsi_n = np.zeros((len(r_t), nm))
    for it, r in enumerate(r_t):
        st = np.log(r)
        e = target_edges(T, st) if edges is None else edges(st)
        a, b = e[:-1], e[1:]
        sig = ((a + b)[:, None] / 2 + (b - a)[:, None] / 2 * xg[None, :]).ravel()
        w = ((b - a)[:, None] / 2 * wg[None, :]).ravel()
        s = np.exp(sig)
        F = M.fn(s) if fn is None else fn(s)            # (N, nm)
        sg = torch.tensor(sig - st, dtype=DT, device=DEV)
        wt = torch.tensor(w * s * s, dtype=DT, device=DEV)   # ds = s dsigma, integrand s f_n -> s^2 f_n dsigma
        inn = (sg < 0)
        K = torch.exp(-2 * torch.abs(sg)[:, None] * nvec[None, :])       # (s/r)^{2n} inside, (r/s)^{2n} outside
        Aw = ((wt * inn)[:, None] * K * F).sum(0)
        Bw = ((wt * (~inn))[:, None] * K * F).sum(0)
        psi_n[it] = ((Aw + Bw) / (4 * nvec)).cpu().numpy()
        dpsi_n[it] = ((Bw - Aw) / (2 * r)).cpu().numpy()
    n = np.arange(1, nm + 1)
    S2 = np.sin(2 * np.outer(n, th_t)); C2 = np.cos(2 * np.outer(n, th_t))
    psi = psi_n @ S2
    psi_r = dpsi_n @ S2
    psi_th = (psi_n * 2 * n[None, :]) @ C2
    rr = np.asarray(r_t)[:, None]
    c = np.cos(th_t)[None, :]; s = np.sin(th_t)[None, :]
    psi_x = c * psi_r - s * psi_th / rr
    psi_y = s * psi_r + c * psi_th / rr
    return dict(U1=-psi_y, U2=psi_x, psi=psi, psi_n=psi_n, dpsi_n=dpsi_n)


if __name__ == '__main__':
    import time
    T = Trial()
    # manufactured test of the Green machinery: replace f by an explicit mode with known psi
    # test: psi = x y exp(-r^2/4) -> f_1 = -Lap psi in mode 1 ... done in test_x3vel.py
    M = Modes(T)
    t0 = time.time()
    out = velocity_at(M, np.array([1.0, 8.6, 100.0]), np.array([0.0, 0.3, 1.2]))
    print('time %.1fs' % (time.time() - t0))
    print(out['U1']); print(out['U2'])
