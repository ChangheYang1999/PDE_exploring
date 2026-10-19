# V240: Biot-Savart velocity of the truncated stratified density f = chi(|X|/R) A y.
# Direct 2D quadrature of psi(X) = int G(X - Y) d_x f(Y) dY, G = -(1/2pi) log|.|, on the annulus where chi' != 0
# (polar tensor grid, Gauss-Legendre in r, trapezoid in theta); X inside the disk where chi = 1.
import numpy as np
A = 1.7; R = 1.0
def chi_p(t):  # derivative of chi(t): chi = 1 for t <= 1, 0 for t >= 2, C^infinity bump transition
    t = np.asarray(t, float); s = np.clip(t - 1.0, 1e-300, 1 - 1e-16)
    e = lambda z: np.exp(-1.0 / z)
    g = e(s) / (e(s) + e(1 - s))  # rises 0 -> 1 on [1,2]
    dg = g * (1 - g) * (1 / s**2 + 1 / (1 - s)**2)
    return -dg
nr, nt = 400, 1024
xg, wg = np.polynomial.legendre.leggauss(nr)
r = 1.5 + 0.5 * xg; wr = 0.5 * wg
th = np.linspace(0, 2 * np.pi, nt, endpoint=False); wt = 2 * np.pi / nt
Rr, Th = np.meshgrid(r, th, indexing='ij')
Yx, Yy = R * Rr * np.cos(Th), R * Rr * np.sin(Th)
dxf = A * Yy * chi_p(Rr) * Yx / (R * Rr) / R     # d_x [A y chi(|Y|/R)]
W = (wr[:, None] * wt) * R * Rr * R              # area element
def psi(X):
    d = np.hypot(X[0] - Yx, X[1] - Yy)
    return np.sum(-np.log(d) / (2 * np.pi) * dxf * W)
# check the cutoff integral int_0^inf chi'(t) dt = -1
print('int chi_p dt =', np.sum(chi_p(r) * wr))
pts = [(0.3, 0.2), (-0.25, 0.4), (0.5, -0.1), (0.1, 0.1), (0.0, 0.0), (0.4, 0.0)]
for X in pts:
    print(X, 'psi = %.12f   -A x y/4 = %.12f' % (psi(X) - psi((0, 0)), -A * X[0] * X[1] / 4))
h = 1e-3
def U(X):  # U = (-psi_y, psi_x)
    return np.array([-(psi((X[0], X[1] + h)) - psi((X[0], X[1] - h))) / (2 * h),
                     (psi((X[0] + h, X[1])) - psi((X[0] - h, X[1]))) / (2 * h)])
for X in [(0.0, 0.0), (0.3, 0.2), (-0.2, 0.35)]:
    print('U', X, U(X), ' (A x/4, -A y/4) =', (A * X[0] / 4, -A * X[1] / 4))
