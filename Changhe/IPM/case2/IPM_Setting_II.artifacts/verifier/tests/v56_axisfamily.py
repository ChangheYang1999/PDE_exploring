"""V56(d): specification M25(h) explicit axis family b_o = r (n + l r^2)/(1 + r^2), w_e = eps r^2/(1 + r^2):
log(kappa_+/kappa_-) = 2 n int_0^inf w_e/(b_o^2 - w_e^2) dr = pi eps (l + n)/(l sqrt(4 n l - eps^2)) (claimed). Quadrature check and
the sign / zero statements. Usage: python3 tests/v56_axisfamily.py"""
import numpy as np
from scipy.integrate import quad
for n, l, eps in ((3.5, 2.0, 0.3), (3.5, 2.0, -0.7), (3.53, 2.0175, 1.1), (1.0, 1.5, 0.05), (2.2, 3.0, 2.5)):
    f = lambda r: eps*r**2/(1 + r**2)/((r*(n + l*r**2)/(1 + r**2))**2 - (eps*r**2/(1 + r**2))**2)
    # integrand ~ eps/(n^2) near 0 (finite) and ~ eps/(l^2 r^2) at infinity; check B_+- = b_o +- w_e > 0 on (0, inf)
    rr = np.logspace(-6, 6, 200001); bo = rr*(n + l*rr**2)/(1 + rr**2); we = eps*rr**2/(1 + rr**2)
    q = 2*n*(quad(f, 0, 1, epsabs=1e-14, epsrel=1e-13, limit=500)[0] + quad(f, 1, np.inf, epsabs=1e-14, epsrel=1e-13, limit=500)[0])
    cf = np.pi*eps*(l + n)/(l*np.sqrt(4*n*l - eps**2))
    print('n %.3f l %.4f eps %+.2f  min(b_o - |w_e|) %.3e  quad %+.14f  closed %+.14f  diff %.1e' % (n, l, eps, (bo - abs(we)).min(), q, cf, abs(q - cf)))
