"""Verifier's residual evaluator (method A, polar grid), verifier.

Given rho as a vectorized callable rho(x, y) (or samples on the verifier's log-polar grid), computes
  U from the polar-mode inverse (vpolar.py, gauge-fixed Green formula),
  R = (c_l X + U).grad rho - rho,   E = -Lap psi - d_x rho,
with derivatives taken by the verifier's own differentiation:
  theta: FFT spectral derivative on the full circle,
  r:     8th-order finite differences in u = log r.
Polar transport form: W.grad rho = c_l r rho_r + (psi_r rho_t - psi_t rho_r)/r.
Normalization of R (SPEC N4): |rho| + |X.grad rho| + |U.grad rho| (pointwise, and sup-based on regions).
"""
import numpy as np
from vpolar import LogGrid, modes_from_samples, psi_modes, center_c, synth


def dtheta(F, order=1):
    Nt = F.shape[1]
    k = np.fft.rfftfreq(Nt, 1.0 / Nt)
    G = np.fft.rfft(F, axis=1) * (1j * k) ** order
    if Nt % 2 == 0 and order % 2 == 1:
        G[:, -1] = 0.0
    return np.fft.irfft(G, n=Nt, axis=1)


def fit_power_tail(r, f, npts=8, k=None):
    """Fit f ~ A r^k on the last npts points (k fixed if given, else fitted in log-log on |f|)."""
    rr, ff = r[-npts:], f[-npts:]
    if k is None:
        good = np.abs(ff) > 0
        if good.sum() < 2:
            return 0.0, 0.0
        k = np.polyfit(np.log(rr[good]), np.log(np.abs(ff[good])), 1)[0]
    A = np.sum(ff * rr ** k) / np.sum(rr ** (2 * k))
    return A, k


class Evaluation:
    pass


def evaluate(rho_samples, g, theta, c_l=None, nmax=None, k_far=None, tail_mmax=None, lo_tail=True, k_self=False):
    """rho_samples[j, i] = rho(r_j, theta_i) on the log grid g and theta_i = 2 pi i/Nt.
    c_l: if None, uses the identity c_l = (1 + c)/3 with c from formula C3.
    k_far: far-field exponent used for the analytic tails (default 1/c_l of the first pass WITHOUT tails).
    k_self (2026-10-18): if True and k_far is None, iterate k_far = 1/c_l with c_l the identity value WITH tails
    (fixed point, 6 passes on c only), so that the outer tail exponent is 1/c_l of the final evaluation. The default
    (False) keeps the earlier behaviour; on fields with R = 1e3 .. 1e4 the two differ by 7e-4 .. 2e-3 in k (G45)."""
    ev = Evaluation()
    Nt = len(theta)
    r = g.r
    if nmax is None:
        nmax = Nt // 2 - 2
        nmax -= nmax % 2
    fm, ev.parity_bad, ev.top_modes = modes_from_samples(rho_samples, nmax + 1)
    # first pass c without tails to get k
    c0 = center_c(g, fm[3])
    cl0 = (1 + c0) / 3 if c_l is None else c_l
    if k_far is None:
        k_far = 1.0 / cl0 if cl0 > 1 else None
    tail_hi = {}
    if k_far is not None:
        for m, f in fm.items():
            if tail_mmax is None or m <= tail_mmax:
                A, k = fit_power_tail(r, f, k=k_far)
                tail_hi[m] = (A, k)
    tail_lo = {}
    if lo_tail:
        for m, f in fm.items():
            be = max(m, 3)
            # r0^be underflows for high modes on small r0: then the inner tail (f_m(r0) (r/r0)^be) is dropped (its
            # contribution f_m(r0) r0/(n + be + 1) is below 1e-300 relative to the data scale anyway)
            den = r[0] ** be
            al = f[0] / den if den > 1e-280 else 0.0
            tail_lo[m] = (al, be)
    ev.c = center_c(g, fm[3], tail_hi.get(3), tail_lo.get(3))
    if k_self and k_far is not None and c_l is None:
        for _ in range(6):
            k_far = 3.0 / (1 + ev.c)
            for m, f in fm.items():
                if tail_mmax is None or m <= tail_mmax:
                    tail_hi[m] = fit_power_tail(r, f, k=k_far)
            ev.c = center_c(g, fm[3], tail_hi.get(3), tail_lo.get(3))
    ev.c_notail = c0
    ev.c_l = (1 + ev.c) / 3 if c_l is None else c_l
    ev.k_far = k_far
    pm = psi_modes(g, fm, nmax, tail_hi or None, tail_lo or None)
    psi, psr, pst = synth(pm, theta)
    ev.psi, ev.psr, ev.pst = psi, psr, pst
    R2 = r[:, None]
    rho = rho_samples
    rho_u = g.du(rho)            # = r rho_r
    rho_t = dtheta(rho)
    ev.rho_r = rho_u / R2
    ev.rho_t = rho_t
    Ur = -pst / R2
    Ut = psr
    ev.Ur, ev.Ut = Ur, Ut
    Xgrad = rho_u                # X.grad rho = r rho_r
    Ugrad = Ur * ev.rho_r + Ut * rho_t / R2
    ev.R = ev.c_l * Xgrad + Ugrad - rho
    ev.Rnorm = np.abs(rho) + np.abs(Xgrad) + np.abs(Ugrad)
    # Poisson residual with independent differentiation of psi (FD in u, spectral theta)
    psi_uu = g.du(psi, order=2)
    psi_tt = dtheta(psi, order=2)
    lap = (psi_uu + psi_tt) / R2 ** 2
    ct, st = np.cos(theta)[None, :], np.sin(theta)[None, :]
    dxrho = ct * ev.rho_r - st * rho_t / R2
    ev.E = -lap - dxrho
    ev.dxrho = dxrho
    ev.fm, ev.pm = fm, pm
    ev.tail_hi = tail_hi
    return ev


def region_stats(ev, g, theta, rmin, rmax, trim=6):
    """sup |R|, sup|R|/sup(norm), max pointwise |R|/norm (excluding axis points where norm ~ 0) on rmin<=r<=rmax.
    trim: drop the first/last grid points (one-sided FD) from statistics."""
    r = g.r
    sel = (r >= rmin) & (r <= rmax)
    sel[:trim] = False
    sel[-trim:] = False
    R = ev.R[sel]
    Nn = ev.Rnorm[sel]
    out = dict(supR=np.abs(R).max(), relsup=np.abs(R).max() / Nn.max())
    mask = Nn > 1e-8 * Nn.max()
    out['relpt'] = (np.abs(R[mask]) / Nn[mask]).max()
    E = ev.E[sel]
    out['supE'] = np.abs(E).max()
    out['relE'] = np.abs(E).max() / np.abs(ev.dxrho[sel]).max()
    return out
