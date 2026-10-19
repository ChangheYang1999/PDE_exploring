# Lead's fp_ls (scripts/b3_ls.py, copied logic) with the LS sample restricted to |u| >= u_lo (origin layer excluded).
import sys, io, contextlib
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.special import roots_jacobi
L = 'b3_wonly_export.py'
sys.argv = ['x', sys.argv[1]]
ns = {'__file__': L, '__name__': 'lead'}
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(open(L).read(), ns)
print(buf.getvalue().strip().splitlines()[-6:][0])
d = ns['d_w']
def fp(d, delta, deg, u_lo, npts=400, nfft=64, njac=120):
    p3, be, xs = d.p3, d.beta, d.xs
    q = 1 - p3
    t = np.cos(np.pi * (np.arange(npts) + 0.5) / npts)
    t = t[np.abs(t) * delta >= u_lo]
    ph = (1 - delta * t) ** (be - 1) * d.phi_x(xs * delta * t)
    c = C.chebfit(t, ph, deg)
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
    return float((I0 + I1).real), fit
for u_lo in (0.0, 0.005, 0.01, 0.0178, 0.03, 0.04, 0.06):
    for delta in (0.3, 0.4, 0.5):
        row = [fp(d, delta, deg, u_lo) for deg in (8, 10, 12, 14, 16)]
        print('u_lo %.4f delta %.1f deg 8..16:' % (u_lo, delta), ' '.join('%7.3f' % v for v, _ in row), '| fit %.0e' % max(f for _, f in row))
