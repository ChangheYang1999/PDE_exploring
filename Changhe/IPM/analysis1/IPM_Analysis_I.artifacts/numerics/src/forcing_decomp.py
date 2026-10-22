"""N10 (lead 04:57Z), FLOATING, own code: decomposition of the localized forcing tau eps~ near P into a smooth polynomial model and a remainder.
tau = 1 on B_{r1}(P), 0 outside B_{r2}(P) (e^{-1/t} step, same as pdisc_fft/aux_R); model = least-squares polynomial in (x - x_*, y), odd in y,
total degree <= 5 (9 monomials), fitted on supp tau (points with tau > 0); reported: ||tau eps~||, ||tau model||, ||tau (eps~ - model)|| in H^s
(unitary FFT on the periodic box of half-width Lb centred at P), the relative rms misfit on supp tau, the linear model y d_y eps~(P), and the
Gaussian-window norms ||exp(-|X-P|^2/(2 sigma^2)) eps~||_{H^s} for the given sigmas.  Fields from the trial's modes as in src/aux_R.py.
Usage: python3 src/forcing_decomp.py n Lb r1 r2 s sigmas(comma) out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import make_interp_spline
from modal_fit import Trial
from trial_green import TrialGreen
from aux_R import step, XS


def fields(G, X, Y, sel):
    tt = np.log(np.hypot(X[sel], Y[sel])); th = np.arctan2(Y[sel], X[sel])
    tg = np.arange(tt.min() - 1e-4, tt.max() + 1e-4, 1e-5)
    Rm, Rtm = G.rho_modes(tg); psim, dpsim = G.psi_at(tg)
    R_ = make_interp_spline(tg, Rm, k=7, axis=0)(tt); Rt_ = make_interp_spline(tg, Rtm, k=7, axis=0)(tt)
    P_ = make_interp_spline(tg, psim, k=7, axis=0)(tt); dP_ = make_interp_spline(tg, dpsim, k=7, axis=0)(tt)
    j = np.arange(Rm.shape[1]); fr = 2 * j + 1; fn = 2.0 * G.n
    S_r = np.sin(np.outer(th, fr)); C_r = np.cos(np.outer(th, fr)); S_p = np.sin(np.outer(th, fn)); C_p = np.cos(np.outer(th, fn))
    rho_t = np.einsum("pj,pj->p", Rt_, S_r); rho_th = np.einsum("pj,pj->p", R_ * fr[None, :], C_r); rho_v = np.einsum("pj,pj->p", R_, S_r)
    r = np.exp(tt); ct, st = np.cos(th), np.sin(th)
    rho_x = (ct * rho_t - st * rho_th) / r; rho_y = (st * rho_t + ct * rho_th) / r
    psi_t = r * np.einsum("pn,pn->p", dP_, S_p); psi_th = np.einsum("pn,pn->p", P_ * fn[None, :], C_p)
    psi_x = (ct * psi_t - st * psi_th) / r; psi_y = (st * psi_t + ct * psi_th) / r
    V1 = G.c_l * X[sel] - psi_y; V2 = G.c_l * Y[sel] + psi_x
    return V1 * rho_x + V2 * rho_y - rho_v


def main(n, Lb, r1, r2, s, sigmas, out):
    t0 = time.time()
    T = Trial(np.load("data/trial_v2_h0.008.npz")); G = TrialGreen(T); G.build()
    dx = 2 * Lb / n; xs = XS - Lb + dx * np.arange(n); ys = -Lb + dx * np.arange(n)
    X, Y = np.meshgrid(xs, ys, indexing="ij"); dist = np.hypot(X - XS, Y)
    rmax = max(r2, 8 * max(sigmas)); sel = dist < min(rmax, 0.999 * Lb)       # fields on the whole window (Gaussian tail e^{-32} beyond 8 sigma)
    eps = np.zeros_like(X); eps[sel] = fields(G, X, Y, sel)
    tau = 1.0 - step((dist - r1) / (r2 - r1))
    # polynomial model, odd in y, degree <= 5, least squares on supp tau
    supp = tau > 0; xx = (X - XS)[supp]; yy = Y[supp]
    mons = [(a, b) for b in (1, 3, 5) for a in range(0, 6 - b)]
    A = np.column_stack([xx ** a * yy ** b for (a, b) in mons]); coef, *_ = np.linalg.lstsq(A, eps[supp], rcond=None)
    model = np.zeros_like(X); model[supp] = A @ coef
    misfit = float(np.sqrt(np.mean((eps[supp] - model[supp]) ** 2) / np.mean(eps[supp] ** 2)))
    lin = np.zeros_like(X); dy0 = coef[mons.index((0, 1))]; lin[supp] = dy0 * yy
    DYP = -2.2528e-8 * 29.749490663333                                  # exact d_y eps~(P) = (mu~ - 1) g (S7 identity; certified balls)
    linP = np.zeros_like(X); linP[supp] = DYP * yy
    kx = 2 * np.pi * np.fft.fftfreq(n, d=dx); KX, KY = np.meshgrid(kx, kx, indexing="ij"); K2 = KX ** 2 + KY ** 2; dk = (2 * np.pi / (n * dx)) ** 2
    def Hs(f): F = np.fft.fft2(f) * dx * dx / (2 * np.pi); return float(np.sqrt(((1 + K2) ** s * np.abs(F) ** 2).sum() * dk))
    def frac_above(f, kc): F = np.fft.fft2(f) * dx * dx / (2 * np.pi); P = (1 + K2) ** s * np.abs(F) ** 2; return float(P[K2 > kc ** 2].sum() / P.sum())
    res = dict(n=n, Lb=Lb, dx=dx, r1=r1, r2=r2, s=s, npatch=int(supp.sum()), sup_tau_eps=float(np.abs(tau * eps).max()), dy_eps_P_model=float(dy0),
               Hs_tau_eps=Hs(tau * eps), Hs_tau_model=Hs(tau * model), Hs_tau_remainder=Hs(tau * (eps - model)), Hs_tau_linear_fitcoef=Hs(tau * lin), Hs_tau_linear_exact_dyP=Hs(tau * linP), dy_eps_P_exact=DYP,
               Hs_tau=Hs(tau), misfit_rel_rms=misfit, frac_Hs_energy_above_1000=frac_above(tau * eps, 1000), frac_above_3000=frac_above(tau * eps, 3000),
               model_coefficients={"%d,%d" % m: float(c) for m, c in zip(mons, coef)}, gauss={})
    for sg in sigmas:
        w = np.exp(-dist ** 2 / (2 * sg ** 2)); res["gauss"][str(sg)] = dict(Hs_w_eps=Hs(w * eps), Hs_w_remainder=Hs(w * (eps - model)), sup_w_eps=float(np.abs(w * eps).max()))
    for kk, vv in res.items():
        if isinstance(vv, (float, int)): print("  %-26s %s" % (kk, vv))
    print("  gauss", res["gauss"])
    json.dump(res, open(out, "w"), indent=1); print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    main(int(a[1]), float(a[2]), float(a[3]), float(a[4]), float(a[5]), [float(x) for x in a[6].split(",")], a[7])
