# NUMERICAL check of the frozen corner formula h = -C x^4 sgn(y) |y|^beta (Prop H0 of S2_L2_THEORY 6).
import numpy as np
from scipy.integrate import quad
k = 1615536043799051 / 2**53; cl = 1 / k; A = 2 * cl - 1; D = 4 * cl - 1
beta = (1 + 4 * A) / D
def bump(u):  # smooth, supported in (1/2, 2), positive inside
    return np.where((u > 0.5) & (u < 2), np.exp(-1 / np.maximum((u - 0.5) * (2 - u), 1e-300)), 0.0)
psi = lambda y: np.sign(y) * bump(abs(y))
def chi(x):
    x = abs(x)
    if x <= 1: return 1.0
    if x >= 2: return 0.0
    a = np.exp(-1 / (x - 1)); b = np.exp(-1 / (2 - x)); return b / (a + b)
f = lambda x, y: x**4 * chi(x) * psi(y)
def h(x, y):
    s0 = np.log(0.5 / abs(y)) / D; s1 = np.log(2 / abs(y)) / D
    return -quad(lambda s: np.exp(-s) * f(x * np.exp(-A * s), y * np.exp(D * s)), max(s0, 0), s1, limit=200, epsabs=0, epsrel=1e-12)[0]
C = quad(lambda u: u**(-beta - 1) * bump(u), 0.5, 2, epsabs=0, epsrel=1e-13)[0] / D
print(f"A={A:.6f} D={D:.6f} beta=(1+4A)/D={beta:.10f} 2-1/D={2-1/D:.10f} C={C:.6e}")
for x, y in [(0.3, 0.01), (1.0, 1e-3), (2.0, -1e-4), (0.7, 0.2)]:
    ok = abs(x) * (2 * abs(y))**(A / D) <= 1
    print(x, y, h(x, y), -C * x**4 * np.sign(y) * abs(y)**beta, "formula region" if ok else "outside")
