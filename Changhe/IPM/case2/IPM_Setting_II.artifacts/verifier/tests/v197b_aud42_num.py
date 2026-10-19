"""V197b: independent checks of the new mathematical content of the referee audit 42 replacements 5 and 6 (moving-center disks,
rotated ellipses). Evaluator copied from tests/v197_sec917_num.py (own code; same p.v. formula with local term
-rho e_2/2, polar parametrization about X)."""
import numpy as np
P = []
def ok(name, val, info=''):
    P.append(bool(val)); print('%-92s %s %s' % (name, bool(val), info), flush=True)
def Kv(th):
    return np.stack([-np.sin(2 * th), np.cos(2 * th)]) / (2 * np.pi)
def U_x2(X, tfun, n=8192):
    ph = 2 * np.pi * np.arange(n) / n
    t = tfun(ph)
    k = np.fft.fftfreq(n, 1.0 / n)
    tp = np.real(np.fft.ifft(1j * k * np.fft.fft(t)))
    G = np.stack([t * np.cos(ph), t * np.sin(ph)])
    Gp = np.stack([tp * np.cos(ph) - t * np.sin(ph), tp * np.sin(ph) + t * np.cos(ph)])
    d = G - np.asarray(X, float)[:, None]
    T = np.hypot(d[0], d[1]); th = np.arctan2(d[1], d[0])
    jac = (d[0] * Gp[1] - d[1] * Gp[0]) / T**2
    if jac.min() <= 0:
        raise ValueError('not star-shaped about X')
    x = X[0]
    f = x**2 * np.log(T) + 2 * x * np.cos(th) * T + np.cos(th)**2 * T**2 / 2
    val = (Kv(th) * f * jac).sum(axis=1) * (2 * np.pi / n)
    return val - np.array([0.0, x**2 / 2])
def W_x2(X, tfun, n=8192):
    return U_x2(X, tfun, n) - U_x2((0.0, 0.0), tfun, n)
cplx = lambda v: v[0] + 1j * v[1]
Wcirc = lambda X: np.array([X[0] * X[1] / 4, -(7 * X[0]**2 + X[1]**2) / 8])
Xs = [(0.5, 0.3), (-0.7, 0.4), (0.2, -0.9), (0.9, 0.0)]
# B1: disk B(d, R) containing 0: W = W_circ + (i/4)(a + ib) Xbar exactly (replacement 5)
emax = 0
for (a, b, R) in [(0.7, -0.4, 3.0), (-1.3, 0.9, 4.0), (2.0, 1.5, 5.0), (0.0, 0.0, 2.5)]:
    tf = lambda p, a=a, b=b, R=R: (a * np.cos(p) + b * np.sin(p)) + np.sqrt(R**2 - a**2 - b**2 + (a * np.cos(p) + b * np.sin(p))**2)
    for X in Xs:
        if np.hypot(X[0] - a, X[1] - b) < R - 0.5:
            Wn = cplx(W_x2(X, tf)); Xb = X[0] - 1j * X[1]
            emax = max(emax, abs(Wn - cplx(Wcirc(X)) - 0.25j * (a + 1j * b) * Xb))
ok('B1 moving-center disks: W_{B(d,R)} = W_circ + (i/4)(a + ib) Xbar (4 disks, 4 points)', emax < 1e-10, 'max err %.1e' % emax)
# B1 control: the sign of the strain term
Xc = (0.5, 0.3); a, b, R = 0.7, -0.4, 3.0
tf = lambda p: (a * np.cos(p) + b * np.sin(p)) + np.sqrt(R**2 - a**2 - b**2 + (a * np.cos(p) + b * np.sin(p))**2)
ewrong = abs(cplx(W_x2(Xc, tf)) - cplx(Wcirc(Xc)) + 0.25j * (a + 1j * b) * (Xc[0] - 1j * Xc[1]))
ok('B1 control: the opposite sign -(i/4)(a + ib) Xbar fails', ewrong > 1e-2, 'err %.3f' % ewrong)
# B2: rotated fixed ellipses: J(theta) = (pi/12)((1 - mu e^{2i theta})^3 - 1) from the definition of J, and the field
# is exactly W_circ + (3i/(2 pi)) J Xbar^2 (replacement 6)
n = 8192; ph = 2 * np.pi * np.arange(n) / n; w = 2 * np.pi / n
ej = 0; ef = 0
for (A, B, th0) in [(1.0, 1.6, 0.3), (1.0, 3.0, 1.1), (2.0, 1.0, -0.7), (1.0, 1.3, np.pi / 4)]:
    rho0 = lambda p: (np.cos(p - th0)**2 / A**2 + np.sin(p - th0)**2 / B**2)**-0.5
    q = (B**2 - A**2) / (B**2 + A**2); mu = (1 - np.sqrt(1 - q**2)) / q
    J = (np.cos(ph)**2 * np.exp(4j * ph) * np.log(rho0(ph))).sum() * w
    G = (np.cos(ph)**2 * np.exp(3j * ph) * rho0(ph)).sum() * w
    Jp = (np.pi / 12) * ((1 - mu * np.exp(2j * th0))**3 - 1)
    ej = max(ej, abs(J - Jp), abs(G))
    for Rr in (3.0, 7.0):
        for X in Xs:
            Wn = cplx(W_x2(X, lambda p: Rr * rho0(p))); Xb = X[0] - 1j * X[1]
            ef = max(ef, abs(Wn - cplx(Wcirc(X)) - (3j / (2 * np.pi)) * J * Xb**2))
    print('   A=%.1f B=%.1f theta=%.3f mu=%.4f J=%.6f%+.6fi |J+pi/12|=%.4f' % (A, B, th0, mu, J.real, J.imag, abs(J + np.pi / 12)))
ok('B2 rotated ellipses: G = 0 and J = (pi/12)((1 - mu e^{2i theta})^3 - 1) by quadrature of the definition', ej < 1e-12, 'max err %.1e' % ej)
ok('B2 rotated ellipses: W_{D_R} = W_circ + (3i/(2pi)) J Xbar^2 exactly (R = 3, 7; F_R = E_R = 0)', ef < 1e-10, 'max err %.1e' % ef)
# B2 control: the opposite rotation sign mu e^{-2i theta} is wrong for theta = 0.3
A, B, th0 = 1.0, 1.6, 0.3
rho0 = lambda p: (np.cos(p - th0)**2 / A**2 + np.sin(p - th0)**2 / B**2)**-0.5
q = (B**2 - A**2) / (B**2 + A**2); mu = (1 - np.sqrt(1 - q**2)) / q
J = (np.cos(ph)**2 * np.exp(4j * ph) * np.log(rho0(ph))).sum() * w
ok('B2 control: mu e^{-2i theta} in place of mu e^{2i theta} fails', abs(J - (np.pi / 12) * ((1 - mu * np.exp(-2j * th0))**3 - 1)) > 1e-2)
# B3: min over theta of |J(theta) + pi/12| = (pi/12)(1 - |mu|)^3 > 0 (closed form), checked on a grid
gm = True
for mu in (0.1, 0.5, 0.9, 0.99, -0.7):
    tt = np.linspace(0, np.pi, 20001)
    v = np.abs((np.pi / 12) * (1 - mu * np.exp(2j * tt))**3)
    gm &= abs(v.min() - (np.pi / 12) * (1 - abs(mu))**3) < 1e-9 and v.min() > 0
ok('B3 |J(theta) + pi/12| = (pi/12)|1 - mu e^{2i theta}|^3 >= (pi/12)(1 - |mu|)^3 > 0', gm)
print('ALL', all(P), len(P), flush=True)
