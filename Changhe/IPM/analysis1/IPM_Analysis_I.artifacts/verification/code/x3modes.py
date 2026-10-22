"""Verifier: angular modes f_n(r) of f = d_x rho_bar, and radial Gauss-Legendre panels in q (aligned with spline knots).

Method (deliberately different from the generator and from ipmA-num's log-radial Lagrange scheme):
  * angular: midpoint rule on [0, pi/2] (= full-period trapezoid using the parity of f sin(2n th)), N_th points;
  * radial: Gauss-Legendre on panels in q between consecutive distinct spline knots, plus geometrically graded panels
    toward q = 0 and q = 1 (endpoint singularities q^(p3/2), tau^(2/(1-k)), tau = 1-q).
"""
import numpy as np
from x3rho import Trial


def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def q_panels(T, n_grade0=40, n_grade1=60, ratio=0.5, tau_min=1e-14, q_min=1e-14):
    kn = np.unique(T.knots)
    edges = list(kn)
    # graded toward q=0 inside the first knot interval
    a = kn[1]
    g0 = []
    x = a
    while x > q_min:
        x *= ratio
        g0.append(x)
    # graded toward q = 1 inside the last interval
    b = kn[-2]
    g1 = []
    t = 1 - b
    while t > tau_min:
        t *= ratio
        g1.append(1 - t)
    e = np.unique(np.concatenate([[0.0], g0, edges, g1, [1.0]]))
    return e


def nodes_from_edges(e, npt=16, drop_last=True):
    x, w = gl(npt)
    A = e[:-1]; B = e[1:]
    if drop_last:   # omit [0, q_min] and [1 - tau_min, 1]: their contribution is bounded separately
        A = A[1:-1]; B = B[1:-1]
    qn = (A[:, None] + B[:, None]) / 2 + (B - A)[:, None] / 2 * x[None, :]
    wn = (B - A)[:, None] / 2 * w[None, :]
    return qn.ravel(), wn.ravel()


def u_of_q(T, q):
    """u(q) = sqrt((1-q)^(-2/(1-k)) - 1), computed stably; du/dq."""
    k = T.k
    tau = 1 - q
    lt = np.log(tau)
    v = np.expm1(-2 / (1 - k) * lt)        # u^2
    u = np.sqrt(v)
    # dq/du = (1-k) u tau / (1+u^2)  ->  du/dq = (1+u^2)/((1-k) u tau)
    dudq = (1 + v) / ((1 - k) * u * tau)
    return u, dudq


def theta_grid(nth):
    j = np.arange(nth)
    return (j + 0.5) * (np.pi / 2) / nth


def fmodes(T, r, nth, nmodes, chunk=512):
    """f_n(r), n = 1..nmodes, f_n = (4/pi) int_0^{pi/2} rho_x sin(2 n th) dth by the midpoint rule."""
    th = theta_grid(nth)
    S = np.sin(2 * np.outer(np.arange(1, nmodes + 1), th)) * (4 / np.pi) * (np.pi / 2 / nth)   # (nmodes, nth)
    out = np.empty((len(r), nmodes))
    for i0 in range(0, len(r), chunk):
        F = T.fields(r[i0:i0 + chunk], th)
        out[i0:i0 + chunk] = F['rho_x'] @ S.T
    return out


if __name__ == '__main__':
    import sys, time
    T = Trial()
    # spectrum at a few radii
    for r in [0.05, 1.0, 5.0, 8.6, 30.0, 1e3, 1e6]:
        for nth in (1024, 4096):
            fm = fmodes(T, np.array([r]), nth, 2000)[0]
            idx = [0, 9, 49, 99, 199, 299, 499, 999, 1499, 1999]
            print('r=%-8g nth=%5d |f_n| at n=%s:' % (r, nth, [i + 1 for i in idx]), ' '.join('%.2e' % abs(fm[i]) for i in idx))
        sys.stdout.flush()
