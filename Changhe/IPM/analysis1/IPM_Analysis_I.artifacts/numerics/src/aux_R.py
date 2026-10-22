"""N9 (lead 02:42Z), FLOATING, independent code: the constants R and E of the auxiliary source inverse (FR 5(o)) for the trial at P = (x_*, 0).
Definitions (lead's note): theta(X) = chi(|X - P|), chi = 1 on [0, 2 delta], 0 on [3 delta, inf), smooth step f(t) = e^{-1/t}/(e^{-1/t} + e^{-1/(1-t)})
with t = (|X - P| - 2 delta)/delta (chi = 1 - f); w = theta (V - D_P (X - P)), D_P = diag(A, mu) = DV(P); q = theta (grad rho~ - (0, g));
unitary FFT f^(k) = (2 pi)^{-1} int f e^{-ik.X} dX; W_r(f) = (2 pi)^{-1} int <k>^r |f^(k)| dk; ||f||_{H^s}^2 = int <k>^{2s} |f^|^2 dk;
alpha_r = 1/(2 sqrt(pi (r-1))), beta_r = 1/(2 sqrt(pi (r-1)(r-2))); P_s(f) = s 2^{s-2} (W_1(f) + alpha_{s-1} ||f||_{H^s});
T_s(w) = s (s-1) 2^{s-4} sum_i (W_2(w_i) + beta_{s-1} ||w_i||_{H^s}); R = T_s(w) + P_s(q_1) + P_s(q_2);
E = ||div w||_inf / 2 + s ||Dw||_{inf,F} + ||q||_inf.
Fields: rho~ and psi~ from the trial's modes (TrialGreen: R_j, d_t R_j; psi_n, psi_r,n on a fine t grid, degree-7 spline interpolation in t to the
Cartesian points, exact angular sums); V = c_l X + (-psi_y, psi_x); Dw and div w by spectral differentiation on the periodic box (w is supported
strictly inside). Cartesian grid: box of half-width Lb centred at P, n x n points.
Usage: python3 src/aux_R.py n Lb delta s out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import make_interp_spline
from modal_fit import Trial
from trial_green import TrialGreen
XS = 8.600063805157177; A_P = 10.1507252438; MU_P = 1 - 2.2528e-8; G_P = 29.749490663333


def step(t):
    t = np.clip(t, 0.0, 1.0); out = np.zeros_like(t); m = (t > 0) & (t < 1)
    a = np.exp(-1.0 / t[m]); b = np.exp(-1.0 / (1.0 - t[m])); out[m] = a / (a + b); out[t >= 1] = 1.0
    return out


def main(n, Lb, delta, s, out):
    t0 = time.time()
    T = Trial(np.load("data/trial_v2_h0.008.npz")); G = TrialGreen(T); G.build(); c_l = G.c_l
    dx = 2 * Lb / n
    xs = XS - Lb + dx * np.arange(n); ys = -Lb + dx * np.arange(n)
    X, Y = np.meshgrid(xs, ys, indexing="ij"); Rr = np.hypot(X, Y); TH = np.arctan2(Y, X); dist = np.hypot(X - XS, Y)
    theta = 1.0 - step((dist - 2 * delta) / delta)
    sel = theta > 0
    # modes on a fine t grid covering the patch
    tt = np.log(Rr[sel]); th = TH[sel]
    tg = np.arange(tt.min() - 1e-4, tt.max() + 1e-4, 1e-5)
    Rm, Rtm = G.rho_modes(tg); psim, dpsim = G.psi_at(tg)
    kint = 7
    R_ = make_interp_spline(tg, Rm, k=kint, axis=0)(tt); Rt_ = make_interp_spline(tg, Rtm, k=kint, axis=0)(tt)
    P_ = make_interp_spline(tg, psim, k=kint, axis=0)(tt); dP_ = make_interp_spline(tg, dpsim, k=kint, axis=0)(tt)
    j = np.arange(Rm.shape[1]); fr = 2 * j + 1; nn = G.n; fn = 2.0 * nn
    S_r = np.sin(np.outer(th, fr)); C_r = np.cos(np.outer(th, fr)); S_p = np.sin(np.outer(th, fn)); C_p = np.cos(np.outer(th, fn))
    rho_t = np.einsum("pj,pj->p", Rt_, S_r); rho_th = np.einsum("pj,pj->p", R_ * fr[None, :], C_r); rho_v = np.einsum("pj,pj->p", R_, S_r)
    r = np.exp(tt); ct, st = np.cos(th), np.sin(th)
    rho_x = (ct * rho_t - st * rho_th) / r; rho_y = (st * rho_t + ct * rho_th) / r
    psi_t = r * np.einsum("pn,pn->p", dP_, S_p); psi_th = np.einsum("pn,pn->p", P_ * fn[None, :], C_p)
    psi_x = (ct * psi_t - st * psi_th) / r; psi_y = (st * psi_t + ct * psi_th) / r
    V1 = c_l * X[sel] - psi_y; V2 = c_l * Y[sel] + psi_x
    w1 = np.zeros_like(X); w2 = np.zeros_like(X); q1 = np.zeros_like(X); q2 = np.zeros_like(X)
    w1[sel] = theta[sel] * (V1 - A_P * (X[sel] - XS)); w2[sel] = theta[sel] * (V2 - MU_P * Y[sel])
    q1[sel] = theta[sel] * rho_x; q2[sel] = theta[sel] * (rho_y - G_P)
    eps = V1 * rho_x + V2 * rho_y - rho_v                                   # the trial residual on the patch
    tau = 1.0 - step((dist - 7 * delta / 4) / (delta / 2))                   # = 1 on B_{7 delta/4}, 0 outside B_{9 delta/4} (as in pdisc_fft)
    feps = np.zeros_like(X); feps[sel] = tau[sel] * eps
    print("fields on %d patch points (%.0fs); check V(P): min|V| on the patch %.2e; sup|w| %.3e, sup|q| %.3e" % (sel.sum(), time.time() - t0, np.hypot(V1, V2).min(), np.hypot(w1, w2).max(), np.hypot(q1, q2).max()), flush=True)
    # unitary FFT on the periodic box: f^(k) = (2 pi)^-1 sum f e^{-ik.X} dx^2 ; k = 2 pi fftfreq
    kx = 2 * np.pi * np.fft.fftfreq(n, d=dx); KX, KY = np.meshgrid(kx, kx, indexing="ij"); K2 = KX ** 2 + KY ** 2; dk = (2 * np.pi / (n * dx)) ** 2
    def hat(f): return np.fft.fft2(f) * dx * dx / (2 * np.pi)
    def Hs(f, s_): F = hat(f); return float(np.sqrt(((1 + K2) ** s_ * np.abs(F) ** 2).sum() * dk))
    def Wr(f, r_): F = hat(f); return float(((1 + K2) ** (r_ / 2) * np.abs(F)).sum() * dk / (2 * np.pi))
    def ddx(f): return np.real(np.fft.ifft2(1j * KX * np.fft.fft2(f)))
    def ddy(f): return np.real(np.fft.ifft2(1j * KY * np.fft.fft2(f)))
    alpha = lambda r_: 1 / (2 * np.sqrt(np.pi * (r_ - 1))); beta = lambda r_: 1 / (2 * np.sqrt(np.pi * (r_ - 1) * (r_ - 2)))
    Hq = [Hs(q1, s), Hs(q2, s)]; Hw = [Hs(w1, s), Hs(w2, s)]; W1q = [Wr(q1, 1), Wr(q2, 1)]; W2w = [Wr(w1, 2), Wr(w2, 2)]
    Ps = [s * 2 ** (s - 2) * (W1q[i] + alpha(s - 1) * Hq[i]) for i in range(2)]
    Ts = s * (s - 1) * 2 ** (s - 4) * sum(W2w[i] + beta(s - 1) * Hw[i] for i in range(2))
    R = Ts + Ps[0] + Ps[1]
    w1x, w1y, w2x, w2y = ddx(w1), ddy(w1), ddx(w2), ddy(w2)
    divw = w1x + w2y; DwF = np.sqrt(w1x ** 2 + w1y ** 2 + w2x ** 2 + w2y ** 2)
    E = float(np.abs(divw).max() / 2 + s * DwF.max() + np.hypot(q1, q2).max())
    # dilation D_ell u(Y) = u(P + ell Y): |f~^(xi)| = ell^-2 |f^(xi/ell)|, so W_r(f~) = (2pi)^-1 int <ell k>^r |f^(k)| dk and
    # ||f~||_{H^s} = ell^-1 (int <ell k>^{2s} |f^|^2 dk)^{1/2}; the components of w carry an extra 1/ell (w~ = w(P + ell Y)/ell).
    kappa = 3.374; a_s = kappa - E; dpar = 1 + (A_P + MU_P) / 2 - kappa + s * DwF.max()        # a_0 - a_s (SPEC 3.15 (S6))
    Fw = [hat(w1), hat(w2)]; Fq = [hat(q1), hat(q2)]; Fe = hat(feps)
    def Wr_d(F, r_, ell): return float(((1 + (ell ** 2) * K2) ** (r_ / 2) * np.abs(F)).sum() * dk / (2 * np.pi))
    def Hs_d(F, s_, ell): return float(np.sqrt(((1 + (ell ** 2) * K2) ** s_ * np.abs(F) ** 2).sum() * dk) / ell)
    def N_lam(F, s_, lam): return float(np.sqrt(((lam ** 2 + K2) ** s_ * np.abs(F) ** 2).sum() * dk))
    dil = {}
    ells = [1.0, delta, 0.01, 0.005, 0.0035, 0.0025, 0.0015]
    if os.environ.get('AUXR_ELLS'): ells = [float(x) for x in os.environ['AUXR_ELLS'].split(',')]
    for ell in ells:
        Hq_ = [Hs_d(Fq[i], s, ell) for i in range(2)]; Hw_ = [Hs_d(Fw[i], s, ell) / ell for i in range(2)]
        W1q_ = [Wr_d(Fq[i], 1, ell) for i in range(2)]; W2w_ = [Wr_d(Fw[i], 2, ell) / ell for i in range(2)]
        Ps_ = [s * 2 ** (s - 2) * (W1q_[i] + alpha(s - 1) * Hq_[i]) for i in range(2)]
        Ts_ = s * (s - 1) * 2 ** (s - 4) * sum(W2w_[i] + beta(s - 1) * Hw_[i] for i in range(2))
        Rt = Ts_ + Ps_[0] + Ps_[1]; bound = (1 + Rt / dpar) ** s / a_s
        dil[str(ell)] = dict(ell=ell, Hs_q=Hq_, Hs_w=Hw_, W1_q=W1q_, W2_w=W2w_, P_s_q=Ps_, T_s_w=float(Ts_), R_tilde=float(Rt), inverse_bound=float(bound),
                             N_forcing=N_lam(Fe, s, 1.0 / ell), bound_times_forcing=float(bound * N_lam(Fe, s, 1.0 / ell)))
        print("  ell %-8g R~ %.4e  bound (1+R~/d)^s/(kappa-E) %.4e  N_{1/ell}(tau eps~) %.4e  product %.4e" % (ell, Rt, bound, dil[str(ell)]["N_forcing"], dil[str(ell)]["bound_times_forcing"]), flush=True)
    res = dict(n=n, Lb=Lb, dx=dx, delta=delta, s=s, A_P=A_P, mu_P=MU_P, g=G_P, c_l=float(c_l), npatch=int(sel.sum()), kappa=kappa, a_s=float(a_s), d_param=float(dpar),
               sup_tau_eps=float(np.abs(feps).max()), Hs_tau_eps=Hs(feps, s), dilation=dil,
               Hs_q=Hq, Hs_w=Hw, W1_q=W1q, W2_w=W2w, P_s_q=Ps, T_s_w=float(Ts), R=float(R),
               E=E, E_parts=dict(div_half=float(np.abs(divw).max() / 2), s_Dw=float(s * DwF.max()), q_inf=float(np.hypot(q1, q2).max())),
               sup_w=float(np.hypot(w1, w2).max()), sup_q=float(np.hypot(q1, q2).max()), minV_patch=float(np.hypot(V1, V2).min()),
               note="FLOATING; spectral derivatives on the periodic box; cutoff chi = 1 - f((|X-P| - 2 delta)/delta), f the e^{-1/t} step")
    for kk, vv in res.items():
        if isinstance(vv, (float, list)): print("  %-10s %s" % (kk, vv))
    json.dump(res, open(out, "w"), indent=1); print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    main(int(a[1]), float(a[2]), float(a[3]), float(a[4]), a[5])
