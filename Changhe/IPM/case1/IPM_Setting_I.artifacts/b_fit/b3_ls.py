"""Noise-robust finite-part B_3 from exported construct1 axis traces (lead).
Same formula as b3_diag.AxisData.b3_fp, but the even function Phi(u) = (1-u)^{beta-1} phi(x* u) is fitted by least squares
(400 Chebyshev points, degree deg, odd coefficients dropped) on [-delta, delta] instead of interpolated with 24 nodes.
Interpolation amplifies the ~1e-8 noise of the exported traces by the Chebyshev growth on |u| = delta/2 (about 1.6^n) and
by rho0^{q+1}/|q+1| (q = 1 - p3), which made b3_fp vary by a factor 8 with delta on final_candidate.npz.
Prints B_3 / x*^{2-p3} (natural units) for delta in {0.3, 0.4, 0.5}, deg in {8, ..., 20}, both a2/b3 variants.
Usage: python b3_ls.py fields.npz"""
import sys
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.special import roots_jacobi
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from b3_diag import AxisData

z = np.load(sys.argv[1])
cl = float(z['c_l'])
x = z['axis_x']
sel = x < 40
x = x[sel]


def odd(f):
    S = CubicSpline(x ** 2, f[sel] / x)
    return lambda t: np.asarray(t) * S(np.asarray(t) ** 2)


def even(f, p=0):
    S = CubicSpline(x ** 2, f[sel] / x ** p)
    return lambda t: np.asarray(t) ** p * S(np.asarray(t) ** 2)


def fp_ls(d, delta, deg, npts=400, nfft=64, njac=120):
    p3, be, xs = d.p3, d.beta, d.xs
    q = 1 - p3
    t = np.cos(np.pi * (np.arange(npts) + 0.5) / npts)
    ph = (1 - delta * t) ** (be - 1) * d.phi_x(xs * delta * t)
    c = C.chebfit(t, ph, deg)
    odd_rel = np.max(np.abs(c[1::2])) / np.max(np.abs(c))
    c[1::2] = 0.0
    fit = np.max(np.abs(C.chebval(t, c) - ph)) / np.max(np.abs(ph))
    rho0 = delta / 2
    uc = rho0 * np.exp(2j * np.pi * np.arange(nfft) / nfft)
    coef = (np.fft.fft(C.chebval(uc / delta, c)) / nfft / rho0 ** np.arange(nfft))[: nfft // 2]
    coef[1::2] = 0
    e = q + np.arange(nfft // 2) + 1
    I0 = np.sum(coef * rho0 ** e / e)
    tj, wj = roots_jacobi(njac, be - 1, 0.0)
    uu = rho0 + (1 - rho0) * (1 + tj) / 2
    I1 = ((1 - rho0) / 2) ** be * np.sum(wj * uu ** q * d.phi_x(xs * uu))
    return float((I0 + I1).real), fit, odd_rel


wf = odd(z['axis_w'])
xs = brentq(wf, 1.0, 30.0)
hf, g1, g1p = even(z['axis_h']), even(z['axis_G1'], 2), odd(z['axis_G1_prime'])
print(f'{sys.argv[1]}: c_l = {cl:.10f}, x* = {xs:.10f}, p3 = {6 + 2 / (2 * cl - 1):.9f}, x*^(2-p3) = {xs ** (-4 - 2 / (2 * cl - 1)):.5e}')
for nm in ('', '_finite_difference'):
    d = AxisData(wf, hf, odd(z['axis_A2' + nm]), even(z['axis_B3W' + nm]), g1, g1p, cl, xs, ncheb=96)
    for delta in (0.3, 0.4, 0.5):
        row = [fp_ls(d, delta, deg) for deg in (8, 10, 12, 14, 16, 20)]
        print(f'  a2/b3 {nm or "solver":18s} delta {delta}: B3 natural (deg 8,10,12,14,16,20):',
              ' '.join(f'{v:.4f}' for v, _, _ in row), f' | rel fit {max(f for _, f, _ in row):.0e}, odd {max(o for _, _, o in row):.0e}')
