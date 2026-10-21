"""verifier: residual evaluator (written for this run).

Given a density object with  eval(r, th) -> (rho, rho_r, rho_th)  (torch, shape (len(r), len(th))), a panel layout in
t = log r (vinv.Panels) and an angular grid of Nth points theta_j = (j + 1/2) 2 pi / Nth (no point on an axis), compute
  f_n (sin 2n theta coefficients of d_x rho), the canonical psi_n by vinv.solve_modes, U = (-psi_y, psi_x),
  R = (c_l X + U).grad rho - rho, the normalizations N_f = |W_1 rho_x| + |W_2 rho_y| + |rho| and
  N_v = |rho| + |X.grad rho| + |U.grad rho|, parity diagnostics, and c = psi_xy(0) by three formulas.
"""
import math, time
import numpy as np
import torch
from vinv import Panels, solve_modes

DT = torch.float64


def theta_grid(Nth, dev):
    j = torch.arange(Nth, dtype=DT, device=dev)
    return (j + 0.5) * 2 * math.pi / Nth


def analyse_sin(F, th, kmax):
    """(2/N) sum_j F_j sin(k theta_j) and cos, k = 0..kmax, for F (Nr, N) on the shifted grid."""
    N = F.shape[1]
    delta = float(th[0])
    S = torch.fft.rfft(F, dim=1)[:, :kmax + 1]
    k = torch.arange(kmax + 1, dtype=DT, device=F.device)
    S = S * torch.exp(-1j * k * delta)[None, :]
    return -(2.0 / N) * S.imag, (2.0 / N) * S.real      # sin coeffs, cos coeffs


def synth(a_cos, b_sin, th, N):
    """sum_k a_k cos(k theta_j) + b_k sin(k theta_j) on the shifted grid; a, b (Nr, kmax+1)."""
    delta = float(th[0])
    kmax = a_cos.shape[1] - 1
    k = torch.arange(kmax + 1, dtype=DT, device=a_cos.device)
    X = torch.zeros((a_cos.shape[0], N // 2 + 1), dtype=torch.complex128, device=a_cos.device)
    X[:, :kmax + 1] = (a_cos - 1j * b_sin) * torch.exp(1j * k * delta)[None, :]
    X[:, 0] = X[:, 0] * 2  # (N/2) irfft gives X_0/2 + Re sum_k X_k e^{i k theta}; doubling X_0 returns a_0
    out = torch.fft.irfft(X, n=N, dim=1) * (N / 2.0)
    return out


class TrialDensity:
    """Adapter: vgen.Trial -> eval(r, th) = (rho, rho_r, rho_theta)."""
    def __init__(self, trial):
        self.tr = trial

    def eval(self, r, th):
        rad = self.tr.radial(r, 1)
        an = self.tr.angular(th)
        rho, rhot = self.tr.field(rad, an, 1)
        return rho[0], rho[1], rhot[0]


class Evaluation:
    def __init__(self, dens, breaks, p, Nth, c_l, mu_left=(4.0,), mu_right=None, dev='cuda', chunk=1500,
                 nmax=None, keep_fields=True, verbose=True):
        t0 = time.time()
        self.pan = pan = Panels(breaks, p)
        self.Nth = Nth
        self.c_l = c_l
        th = theta_grid(Nth, dev)
        self.th = th
        r = pan.r
        Nr = pan.N
        kmax = Nth // 2 - 2
        if nmax is None:
            nmax = kmax // 2
        self.ns = np.arange(1, nmax + 1)
        rho = torch.empty((Nr, Nth), dtype=DT, device=dev)
        rr = torch.empty_like(rho)
        rt = torch.empty_like(rho)
        for i0 in range(0, Nr, chunk):
            a, b, c = dens.eval(r[i0:i0 + chunk], th)
            rho[i0:i0 + chunk], rr[i0:i0 + chunk], rt[i0:i0 + chunk] = a, b, c
        co, si = torch.cos(th)[None, :], torch.sin(th)[None, :]
        rt_ = torch.as_tensor(r, dtype=DT, device=dev)[:, None]
        rx = co * rr - si * rt / rt_
        ry = si * rr + co * rt / rt_
        sn, cs = analyse_sin(rx, th, kmax)
        # parity diagnostics of d_x rho: only sin(2n theta) allowed
        allowed = sn[:, 2:2 * nmax + 1:2]
        self.parity = dict(
            sin_even_max=float(allowed.abs().max()),
            sin_odd_max=float(sn[:, 1::2].abs().max()),
            cos_max=float(cs.abs().max()),
            tail_mode_rel=float(allowed[:, -8:].abs().max() / allowed.abs().max()))
        f = allowed.cpu().numpy()                       # (Nr, nmax): f_n(r)
        phi = (r ** 2)[:, None] * f
        t1 = time.time()
        psi, dpsi, tail = solve_modes(pan, phi, self.ns, mu_left=mu_left, mu_right=mu_right)
        self.tail = tail
        t2 = time.time()
        # c = psi_xy(0): (i) (1/2) int e^{-2t} phi_1 dt ; (ii) 2 psi_1 / r^2 at t_min ; (iii) int rho_3(r) r^-2 dr
        w = np.exp(-2 * pan.t) * phi[:, 0]
        ci = 0.5 * pan.integrate(w)
        # tails of (i): left phi_1 ~ e^{4t}: int_{-inf}^{t0} = w(t0)/2 ; right from the fitted power laws
        ci_left = 0.5 * w[0] / 2.0
        ci_right = 0.0
        if mu_right is not None:
            ar = tail['alpha_right'][:, 0]
            nl = 2 * p + 1
            t0r = pan.t[-nl:].mean()
            for a_, m_ in zip(ar, mu_right):
                ci_right += 0.5 * a_ * np.exp(m_ * (pan.t[-1] - t0r)) * np.exp(-2 * pan.t[-1]) / (2 - m_)
        self.c_int = ci + ci_left + ci_right
        self.c_int_parts = (ci, ci_left, ci_right)
        self.c_psi = 2 * psi[0, 0] / r[0] ** 2
        sr, _ = analyse_sin(rho, th, 4)
        rho3 = sr[:, 3].cpu().numpy()
        self.c_rho = pan.integrate(np.exp(-pan.t) * rho3) + np.exp(-pan.t[0]) * rho3[0] / 2.0
        # velocity synthesis
        nn = torch.as_tensor(self.ns, dtype=DT, device=dev)
        psi_t = torch.as_tensor(psi, device=dev)
        dpsi_t = torch.as_tensor(dpsi, device=dev)
        A = torch.zeros((Nr, kmax + 1), dtype=DT, device=dev)
        B = torch.zeros_like(A)
        A[:, 2:2 * nmax + 1:2] = 2 * nn[None, :] * psi_t           # psi_theta = sum 2n psi_n cos
        B[:, 2:2 * nmax + 1:2] = dpsi_t                             # r psi_r = sum dpsi_n sin
        Z = torch.zeros_like(A)
        psith = synth(A, Z, th, Nth)
        rpsir = synth(Z, B, th, Nth)
        Ur = -psith / rt_
        Uth = rpsir / rt_
        t3 = time.time()
        U1 = Ur * co - Uth * si
        U2 = Ur * si + Uth * co
        x = rt_ * co
        y = rt_ * si
        W1 = c_l * x + U1
        W2 = c_l * y + U2
        R = W1 * rx + W2 * ry - rho
        Nf = (W1 * rx).abs() + (W2 * ry).abs() + rho.abs()
        Nv = rho.abs() + (x * rx + y * ry).abs() + (U1 * rx + U2 * ry).abs()
        self.R, self.Nf, self.Nv = R, Nf, Nv
        if keep_fields:
            self.rho, self.rx, self.ry, self.U1, self.U2 = rho, rx, ry, U1, U2
        self.psi_modes, self.dpsi_modes, self.f_modes = psi, dpsi, f
        self.times = (t1 - t0, t2 - t1, t3 - t2, time.time() - t3)
        if verbose:
            print('eval: Nr %d Nth %d nmax %d; times dens %.1fs solve %.1fs synth %.1fs resid %.1fs' %
                  ((Nr, Nth, nmax) + self.times), flush=True)

    def region_max(self, mask_fn, norm='f'):
        N = self.Nf if norm == 'f' else self.Nv
        r = torch.as_tensor(self.pan.r, dtype=DT, device=self.R.device)[:, None]
        th = self.th[None, :]
        m = mask_fn(r, th)
        q = (self.R.abs() / N)
        q = torch.where(m, q, torch.zeros_like(q))
        v = float(q.max())
        idx = int(torch.argmax(q))
        i, j = divmod(idx, q.shape[1])
        return v, float(self.pan.r[i]), float(self.th[j])

    def axis_w(self):
        """w(x) = W_1(x,0) = c_l x - psi_y(x,0) at the radial nodes, psi_y(x,0) = (1/r) sum 2n psi_n(r)."""
        r = self.pan.r
        P1 = (2 * self.ns[None, :] * self.psi_modes).sum(1) / r
        return self.c_l * r - P1, P1
