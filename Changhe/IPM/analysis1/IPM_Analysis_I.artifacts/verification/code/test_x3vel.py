"""Manufactured tests of the Green-mode machinery in x3vel.velocity_at: f_n chosen so that the canonical psi_n is known.
psi_n = exp(phi), f_n = -psi_n * (phi'' + phi'^2 + phi'/s - 4n^2/s^2) simplified by hand (1/s^2 terms cancel)."""
import numpy as np, torch
from x3rho import Trial
from x3vel import Modes, velocity_at, DEV, DT

T = Trial(); M = Modes(T, nth=64, nmodes=400)
beta = (T.k + 1) / 2


def case_growth(n):
    def ps(s):
        return np.exp(2 * n * np.log(s) + (beta - n) * np.log1p(s * s))
    def dps(s):
        return ps(s) * (2 * n / s + 2 * (beta - n) * s / (1 + s * s))
    def f(s):
        b = beta - n
        br = 2 * b * (1 - s * s) / (1 + s * s) ** 2 + 8 * n * b / (1 + s * s) + 4 * b * b * s * s / (1 + s * s) ** 2 + 2 * b / (1 + s * s)
        return -ps(s) * br
    return ps, dps, f


def case_gauss(n):
    s0 = np.sqrt(9.0 * n)        # maximum of s^(2n) e^(-s^2/9); normalized to max value 1
    def ps(s):
        return np.exp(2 * n * np.log(s / s0) - (s * s - s0 * s0) / 9)
    def dps(s):
        return ps(s) * (2 * n / s - 2 * s / 9)
    def f(s):
        return -ps(s) * (-4 / 9 - 8 * n / 9 + 4 * s * s / 81)
    return ps, dps, f


rt = np.array([1e-3, 0.05, 1.0, 3.0, 8.6, 50.0, 1e3, 1e5, 1e7])
for n in (1, 2, 5, 30, 100, 400):
    for name, cf in (('gauss', case_gauss), ('growth', case_growth)):
        ps, dps, ff = cf(n)
        def fn(s, n=n, ff=ff):
            out = np.zeros((len(s), M.nmodes)); out[:, n - 1] = ff(s)
            return torch.tensor(out, dtype=DT, device=DEV)
        with np.errstate(all='ignore'):
            o = velocity_at(M, rt, np.array([0.3]), fn=fn)
            ex = ps(rt); dex = dps(rt)
            ok = np.abs(ex) > 1e-250
            # growth case: pointwise relative error; gauss case: error relative to max |psi_n|, max |psi_n'| (=O(1))
            sc1 = np.abs(ex) if name == 'growth' else 1.0 + 0 * ex
            sc2 = np.abs(dex) if name == 'growth' else 1.0 + 0 * ex
            e1 = np.abs(o['psi_n'][:, n - 1] - ex) / sc1
            e2 = np.abs(o['dpsi_n'][:, n - 1] - dex) / sc2
        e1 = np.where(ok, e1, 0); e2 = np.where(ok, e2, 0)
        print('n=%3d %-6s max rel err psi_n %.2e  dpsi_n %.2e  (worst at r=%g; tested r=%s)' % (n, name, e1.max(), e2.max(), rt[np.argmax(e2)], rt[ok]))
