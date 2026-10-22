"""Floating-point (evidence only) fractional Sobolev norms H^s of a smoothly cut-off piece of the trial residual near P:
  f = chi(|X - P|) eps~(X),  chi = 1 on |X-P| <= r1, 0 for |X-P| >= r2 (C^infty bump: chi(d) = Q((d - r1)/(r2 - r1)), Q = e^{-1/(1-u)} smoothstep)
  ||f||_{H^s}^2 = int (1 + |xi|^2)^s |f^(xi)|^2 dxi / (2 pi)^2   on R^2 (f compactly supported), by FFT on a Cartesian grid of spacing dx.
eps~ at the Cartesian points: residual modes eps_N(t) on a fine t-grid (closed-form Green pipeline) interpolated by cubic splines in t,
summed with sin((2N+1) theta). Reports H^s for s in a list, plus the H^k norms by the FFT for cross-check with pdisc_norms.
Usage: python3 pdisc_fft.py trial.npz r1 r2 dx out.json [pad=1.25] [interp_order=7]   (pad = box half-width factor times 9 delta/4; interp_order = radial interpolation degree)
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import make_interp_spline
from modal_fit import Trial
from trial_green import TrialGreen
XS = 8.600063805157177


def bump(u):
    """C^infty step from 1 (u <= 0) to 0 (u >= 1)."""
    u = np.clip(u, 0.0, 1.0); out = np.zeros_like(u)
    m = (u > 0) & (u < 1)
    a = np.exp(-1.0 / (1.0 - u[m])); b = np.exp(-1.0 / u[m])
    out[m] = a / (a + b); out[u <= 0] = 1.0
    return out


def main(path, r1, r2, dx, out, pad=1.25, kint=7):
    T = Trial(np.load(path)); G = TrialGreen(T); G.build()
    # fine t grid covering the patch
    tlo, thi = np.log(XS - r2 - 2 * dx), np.log(XS + r2 + 2 * dx); dt = 1e-5
    t = np.arange(tlo, thi + 0.5 * dt, dt)
    t0 = time.time(); eps = G.residual_modes(t); print("modes at %d radii: %.0fs" % (len(t), time.time() - t0), flush=True)
    N = np.arange(eps.shape[1]); fr = 2 * N + 1
    # Cartesian grid: box [XS - Lb, XS + Lb] x [-Lb, Lb], Lb >= r2 + margin, n = power of two
    Lb = r2 * pad
    n = int(2 ** np.ceil(np.log2(2 * Lb / dx))); dx = 2 * Lb / n
    xs = XS - Lb + dx * np.arange(n); ys = -Lb + dx * np.arange(n)
    X, Y = np.meshgrid(xs, ys, indexing="ij"); R = np.hypot(X, Y); TH = np.arctan2(Y, X); d = np.hypot(X - XS, Y)
    chi = bump((d - r1) / (r2 - r1))
    sel = chi > 0
    tt = np.log(R[sel]); th = TH[sel]
    t0 = time.time()
    cs = make_interp_spline(t, eps, k=kint, axis=0)      # degree-7 (C^6) interpolation in t of the residual modes
    em = cs(tt)                                   # (npts, Nmodes)
    eps_pts = np.einsum("pn,pn->p", em, np.sin(np.outer(th, fr)))
    f = np.zeros_like(X); f[sel] = eps_pts * chi[sel]
    print("eps on %d patch points: %.0fs ; sup|eps| on patch %.3e, sup|chi eps| %.3e" % (sel.sum(), time.time() - t0, np.abs(eps_pts).max(), np.abs(f).max()), flush=True)
    # FFT
    F = np.fft.fft2(f) * dx * dx                  # approximates the continuous Fourier transform (up to phase)
    kx = 2 * np.pi * np.fft.fftfreq(n, d=dx); KX, KY = np.meshgrid(kx, kx, indexing="ij"); K2 = KX ** 2 + KY ** 2
    dk = (2 * np.pi / (n * dx)) ** 2 / (2 * np.pi) ** 2
    P2 = np.abs(F) ** 2 * dk
    res = {"r1": r1, "r2": r2, "dx": dx, "n": n, "pad": pad, "kint": kint, "sup_f": float(np.abs(f).max()), "sup_eps_patch": float(np.abs(eps_pts).max()), "L2_f_direct": float(np.sqrt((f ** 2).sum() * dx * dx))}
    for s in [0, 1, 1.5, 2, 2.25, 2.5, 2.75, 2.8, 3, 3.03, 3.06, 3.1, 3.2, 3.3, 3.4, 3.5, 4]:
        res["H%g" % s] = float(np.sqrt(((1 + K2) ** s * P2).sum()))
        res["homog%g" % s] = float(np.sqrt((K2 ** s * P2).sum()))
    # spectral distribution: fraction of the H^3 norm^2 from |xi| > kc
    for kc in [50, 100, 200, 400, 800]:
        res["H3_frac_above_%d" % kc] = float((((1 + K2) ** 3 * P2)[K2 > kc ** 2]).sum() / ((1 + K2) ** 3 * P2).sum())
    for key in sorted(res): print("  %s = %s" % (key, res[key]))
    json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5], float(sys.argv[6]) if len(sys.argv) > 6 else 1.25, int(sys.argv[7]) if len(sys.argv) > 7 else 7)
