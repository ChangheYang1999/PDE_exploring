"""FLOATING-POINT companion (evidence only, NOT rigorous) of src/cert_forcing.py: for the same polynomial cutoff tau (p9 or p11) centred at
P = (x_*, 0) with transition 7 delta/4 <= |X - P| <= 9 delta/4, the FFT values of the integer-order quantities I3 = int (lam^2+|xi|^2)^3 |f^|^2,
I4 = int (lam^2+|xi|^2)^4 |f^|^2, the fractional N_lam(f) = (int (lam^2+|xi|^2)^{3.1} |f^|^2)^{1/2} (lam = 1: H^{3.1}) and the Hoelder bound
(I3^{0.9} I4^{0.1})^{1/4} that the certificate uses, for f = tau eps~ (unitary Fourier transform, as in SPEC 3.15 and the lead's forcing_cutoff.py).
Also the sampled maxima of |D^alpha eps~| (|alpha| <= 4, TrialJets: analytic derivatives of the modes, exact angular derivatives, exact
polar-to-Cartesian recursion) on polar grids covering B_{9 delta/4}(P) and B_{3 delta}(P), to be compared with the certified suprema.
Usage: python3 src/forcing_float.py trial.npz delta p9|p11 dx out.json [nt=600 nth=300]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import make_interp_spline
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets

XS = 8.600063805157172
STEP_POLY = {"p9": [0, 0, 0, 0, 0, 126, -420, 540, -315, 70], "p11": [0, 0, 0, 0, 0, 0, 462, -1980, 3465, -3080, 1386, -252]}


def step(kind, u):
    u = np.clip(u, 0.0, 1.0); c = STEP_POLY[kind]
    return sum(ck * u ** k for k, ck in enumerate(c))


def main(path, delta, kind, dx, out, nt=600, nth=300):
    t0 = time.time()
    T = Trial(np.load(path)); G = TrialGreen(T); G.build()
    r_in, r_out = 7 * delta / 4, 9 * delta / 4
    Lb = r_out * 1.25
    n = int(2 ** np.ceil(np.log2(2 * Lb / dx))); dx = 2 * Lb / n
    xs = XS - Lb + dx * np.arange(n); ys = -Lb + dx * np.arange(n)
    X, Y = np.meshgrid(xs, ys, indexing="ij"); R = np.hypot(X, Y); TH = np.arctan2(Y, X); d = np.hypot(X - XS, Y)
    tau = step(kind, 1.0 - (d - r_in) / (delta / 2)); tau[d <= r_in] = 1.0; tau[d >= r_out] = 0.0
    sel = tau > 0
    tlo, thi = np.log(XS - r_out - 3 * dx), np.log(XS + r_out + 3 * dx); dt = 1e-5
    tg = np.arange(tlo, thi + 0.5 * dt, dt)
    eps_modes = G.residual_modes(tg); fr = 2 * np.arange(eps_modes.shape[1]) + 1
    cs = make_interp_spline(tg, eps_modes, k=7, axis=0)
    em = cs(np.log(R[sel])); eps_pts = np.einsum("pn,pn->p", em, np.sin(np.outer(TH[sel], fr)))
    f = np.zeros_like(X); f[sel] = eps_pts * tau[sel]
    print("grid n=%d dx=%.3e, %d points in supp tau, sup|eps| on supp %.4e, sup|f| %.4e (%.0fs)" % (n, dx, sel.sum(), np.abs(eps_pts).max(), np.abs(f).max(), time.time() - t0), flush=True)
    F = np.fft.fft2(f) * dx * dx / (2 * np.pi)                     # unitary continuous transform (up to phase)
    kx = 2 * np.pi * np.fft.fftfreq(n, d=dx); KX, KY = np.meshgrid(kx, kx, indexing="ij"); K2 = KX ** 2 + KY ** 2
    dk2 = (2 * np.pi / (n * dx)) ** 2
    P2 = np.abs(F) ** 2 * dk2
    res = dict(trial=path, delta=delta, cutoff=kind, n=n, dx=dx, sup_eps_supp=float(np.abs(eps_pts).max()), sup_f=float(np.abs(f).max()),
               L2_direct=float(np.sqrt((f ** 2).sum() * dx * dx)), L2_fft=float(np.sqrt(P2.sum())), results={})
    for lam in (1.0, 500.0):
        W = lam ** 2 + K2
        I3 = float((W ** 3 * P2).sum()); I4 = float((W ** 4 * P2).sum()); N31 = float(np.sqrt((W ** 3.1 * P2).sum()))
        res["results"][str(lam)] = dict(lam=lam, I3=I3, I4=I4, order3=np.sqrt(I3), order4=np.sqrt(I4), order_3_1=N31, hoelder_bound=(I3 ** 0.9 * I4 ** 0.1) ** 0.5)
        print("  lam=%g: I3 %.6g I4 %.6g | order-3 %.5g order-4 %.5g | order-3.1 %.5g | Hoelder bound (I3^.9 I4^.1)^(1/2) %.5g" % (lam, I3, I4, np.sqrt(I3), np.sqrt(I4), N31, (I3 ** 0.9 * I4 ** 0.1) ** 0.5), flush=True)
    # sampled derivative maxima on polar grids
    J = TrialJets(G, K=4)
    R3 = 3 * delta; th_max = np.arcsin(R3 / XS) * 1.000001
    t = np.linspace(np.log(XS - R3), np.log(XS + R3), nt); th = np.linspace(0.0, th_max, nth)
    E, _, _ = J.eps_jets(t, th); D = J.polar_to_cart(E, t, th, 4)
    Rg = np.exp(t)[:, None]; dist = np.sqrt(Rg ** 2 - 2 * Rg * XS * np.cos(th)[None, :] + XS ** 2)
    res["sampled_max_D_eps"] = {}
    for ball, rad in (("B94", r_out), ("B3", R3)):
        m = dist <= rad
        res["sampled_max_D_eps"][ball] = {"%d_%d" % k: float(np.abs(D[k][m]).max()) for k in D}
        print("  sampled max |D^alpha eps~| on %s (%d points): " % (ball, m.sum()) + ", ".join("%s: %.3e" % (k, v) for k, v in res["sampled_max_D_eps"][ball].items()), flush=True)
    res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1)
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], float(a[2]), a[3], float(a[4]), a[5], int(a[6]) if len(a) > 6 else 600, int(a[7]) if len(a) > 7 else 300)
