# Lead (2026-10-18): velocity_p of pforward.py with exponential-integrator weights in the per-mode radial
# convolutions (exact for piecewise-linear integrands on each log-r cell). The trapezoid weights of pforward.velocity_p are
# inaccurate when |m| dlr is not small (angular layers), which shows up as div W != 0 (specification M25(i)). Same interface.
import numpy as np
import p0_forward as P1


def _w(am, D):
    # E0 = int_0^D e^{-m u} du, E1 = int_0^D u e^{-m u} du; returns (near-end weight, far-end weight) = (E0 - E1/D, E1/D)
    x = am * D; e = np.exp(-x)
    small = x < 1e-4
    xs = np.where(small, 1.0, x)
    E0 = np.where(small, D * (1 - x / 2 + x * x / 6), (1 - e) / np.where(am > 0, am, 1.0))
    E1 = np.where(small, D * D * (0.5 - x / 3 + x * x / 8), D * D * (1 - e * (1 + xs)) / (xs * xs))
    return E0 - E1 / D, E1 / D


def velocity_p(rhoD, lr, th, p):
    Nr, Nth = rhoD.shape
    drho = lr[1] - lr[0]
    r = np.exp(lr)
    c, s = np.cos(th)[None, :], np.sin(th)[None, :]
    q = (c * P1.d_rho(rhoD, drho) - s * P1.d_th(rhoD)) / r[:, None]
    Q = np.fft.fft(q, axis=1) / Nth
    m = np.fft.fftfreq(Nth, 1.0 / Nth).astype(int)
    am = np.abs(m).astype(float)
    keep = (np.abs(m) != Nth // 2)
    h = Q * np.exp(2 * lr)[:, None]
    hq = Q * r[:, None]
    lam = np.exp(-am * drho)
    wn, wf = _w(am, drho)
    Al = np.zeros((Nr, Nth), complex)
    Al[0] = h[0] / (am + 2.0)
    for k in range(1, Nr):
        Al[k] = lam * Al[k - 1] + wn * h[k] + wf * h[k - 1]
    I = np.zeros((Nr, Nth), complex)
    I1 = np.zeros((Nr, Nth), complex)
    I[0] = h[0] / 2.0
    I1[0] = hq[0]
    for k in range(1, Nr):
        I[k] = I[k - 1] + 0.5 * drho * (h[k - 1] + h[k])
        I1[k] = I1[k - 1] + 0.5 * drho * (hq[k - 1] + hq[k])
    Ag = np.zeros((Nr, Nth), complex)
    big = am >= 2
    Ag[-1, big] = h[-1, big] / (am[big] - 1.0 - p)
    for k in range(Nr - 2, -1, -1):
        Ag[k, big] = lam[big] * Ag[k + 1, big] + wn[big] * h[k, big] + wf[big] * h[k + 1, big]
    one = am == 1
    Ag[:, one] = -r[:, None] * I1[:, one]
    Wr = np.zeros((Nr, Nth), complex)
    Wt = np.zeros((Nr, Nth), complex)
    nz = (am >= 1) & keep
    amn = np.where(am >= 1, am, 1.0)
    psi = (Al + Ag) / (2.0 * amn[None, :])
    dpsi = (-Al + Ag) / (2.0 * r[:, None])
    Wr[:, nz] = (-1j * m[None, :] * psi / r[:, None])[:, nz]
    Wt[:, nz] = dpsi[:, nz]
    z = am == 0
    Wt[:, z] = -I[:, z] / r[:, None]
    return np.real(np.fft.ifft(Wr * Nth, axis=1)), np.real(np.fft.ifft(Wt * Nth, axis=1))
