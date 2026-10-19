"""Axis diagnostics (x*, mu1, mu2 = h(P), G1 near P) for DR snapshots in runs/diag3/*.npz (verifier)."""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vpolar import LogGrid
from vfast import FastInverse
from vb3 import axis_traces, find_xstar, local_fit

def snap_axis(F, r, ms, k=0.67):
    N = len(r)
    g = LogGrid(N, r[0], r[-1])
    assert np.allclose(g.r, r)
    nmax = ms[-1] + 1
    inv = FastInverse(g, nmax)
    beta = np.maximum(ms, 3).astype(float)
    p, dp, c = inv.solve(F, (F[:, -1] / r[-1] ** k, k), (F[:, 0], beta))
    cl = (1 + c) / 3
    ax = axis_traces(F, ms, p, dp, inv.ns, r, cl, g.du)
    return ax, cl

if __name__ == '__main__':
    d = np.load(sys.argv[1])
    r, ms = d['r'], d['ms']
    for i, tau in enumerate(d['tau']):
        ax, cl = snap_axis(d['F'][i], r, ms)
        x, w, h, G1 = ax['x'], ax['w'], ax['h'], ax['G1']
        xs = find_xstar(x, w)
        out = dict(tau=float(tau), cl=float(cl), cl_saved=float(d['cl'][i]))
        if xs is not None:
            # mu1 = w'(x*) from the grid derivative of w, h(P) by a cubic spline in log x; mu1 + h(P) = 2 c_l is the check
            # (div W = 2 c_l). The earlier local polynomial fit used too few points on the N = 1300 grid (fixed 19:2xZ).
            from scipy.interpolate import CubicSpline
            g = LogGrid(len(r), r[0], r[-1])
            wp = g.du(w[:, None])[:, 0] / x
            mu1 = float(CubicSpline(np.log(x), wp)(np.log(xs)))
            hP = float(CubicSpline(np.log(x), h)(np.log(xs)))
            out.update(x_star=xs, mu1=mu1, hP=hP, div_chk=mu1 + hP - 2 * cl)
            j = np.searchsorted(x, xs)
            out.update(G1_P=float(G1[j]), G1_max=float(np.abs(G1[x < 10 * xs]).max()))
        lam1 = float(np.polyfit(x[(x > 1e-4) & (x < 1e-3)] ** 2, (w / x)[(x > 1e-4) & (x < 1e-3)], 1)[-1])
        out.update(lambda1=lam1, A_from_cl=2 * cl - 1)
        print(json.dumps({k_: (round(v, 5) if isinstance(v, float) else v) for k_, v in out.items()}), flush=True)
