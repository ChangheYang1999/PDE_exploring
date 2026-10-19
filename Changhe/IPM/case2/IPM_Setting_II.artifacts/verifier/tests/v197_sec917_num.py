"""V197: independent quadrature checks of Proposition 2.1 (Section 9.17, frozen candidate 5f37a2bf). Not derived from
the lead's trunc_pred.py / trunc_poly.py / strain_g.py / check_917.py (not read).
Evaluator for rho = x^2 on a domain D star-shaped with respect to X: in polar coordinates about X, Y = X + t e_th,
(x + t cos th)^2 = x^2 + 2 x t cos th + t^2 cos^2 th, and the circular principal value of int K(X - Y) rho dY is
    int_0^{2 pi} K(e_th) [x^2 log T(th) + 2 x cos th T(th) + cos^2 th T(th)^2 / 2] dth,
T(th) the exit distance (the log term uses int K(e_th) dth = 0). Then U(X) = that - x^2 e_2/2 (Step 1 local term) and
W_D = U(X) - U(0). The boundary is parametrized by its polar angle phi about 0, th = arg(Gamma(phi) - X), and
dth = (d x Gamma')/|d|^2 dphi (star-shapedness about X is checked: this Jacobian must be positive)."""
import numpy as np
from scipy.special import hyp2f1
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
Xs = [(0.5, 0.3), (-0.7, 0.4), (0.2, -0.9), (0.9, 0.0)]
# T1 disk: independent potential matching gives U = (xy/4, R^2/8 - (7x^2 + y^2)/8) (V197 sym test)
Rd = 3.0
err = max(np.abs(U_x2(X, lambda p: Rd + 0 * p) - np.array([X[0] * X[1] / 4, Rd**2 / 8 - (7 * X[0]**2 + X[1]**2) / 8])).max() for X in Xs)
ok('T1 disk R = 3: p.v. formula with local term -rho e_2/2 equals the potential-matching velocity', err < 1e-10, 'max err %.2e' % err)
err_wrong = max(np.abs(U_x2(X, lambda p: Rd + 0 * p) + np.array([0, X[0]**2]) - np.array([X[0] * X[1] / 4, Rd**2 / 8 - (7 * X[0]**2 + X[1]**2) / 8])).max() for X in Xs)
ok('T1 control: the opposite local term +rho e_2/2 fails', err_wrong > 0.1, 'err %.3f' % err_wrong)
Wcirc = lambda X: np.array([X[0] * X[1] / 4, -(7 * X[0]**2 + X[1]**2) / 8])
# angular moments by quadrature
def moments(rho0, delta, R, n=8192):
    ph = 2 * np.pi * np.arange(n) / n; c2 = np.cos(ph)**2; w = 2 * np.pi / n
    G = (c2 * np.exp(3j * ph) * rho0(ph)).sum() * w; I = (c2 * np.exp(3j * ph) * delta(ph)).sum() * w
    J = (c2 * np.exp(4j * ph) * np.log(rho0(ph))).sum() * w
    E = (c2 * np.exp(4j * ph) * np.log1p(delta(ph) / (R * rho0(ph)))).sum() * w
    return G, I, J, E
def pred_c(X, R, G, I, J, E=0.0):
    Xb = X[0] - 1j * X[1]
    return cplx(Wcirc(X)) + (1j / np.pi) * (R * G + I) * Xb + (3j / (2 * np.pi)) * (J + E) * Xb**2
# T2 tuned truncation for several l
rho0 = lambda p: np.exp(-np.cos(4 * p) / 6); m = np.exp(-1 / 6)
for l in (0.8, 1.7, 0.3, -0.4):
    dl = lambda p, l=l: 4 * (l - 0.5) * np.sin(p); S = 4 * abs(l - 0.5)
    G, I, J, _ = moments(rho0, dl, 1e9)
    ok('T2 l = %.2f: G = 0, J = -pi/12, I = i pi (l - 1/2) by quadrature' % l, abs(G) < 1e-12 and abs(J + np.pi / 12) < 1e-12
       and abs(I - 1j * np.pi * (l - 0.5)) < 1e-12)
    rows = []
    for R in (10, 20, 40, 80, 160, 320):
        tf = lambda p, R=R: R * rho0(p) + dl(p)
        e_poly = 0; e_exp = 0; bnd_ok = True
        for X in Xs:
            L = max(1.0, np.hypot(*X))
            Wn = W_x2(X, tf)
            Wpoly = np.array([(0.5 - l) * X[0], (l - 0.5) * X[1] - X[0]**2])
            e_poly = max(e_poly, np.abs(Wn - Wpoly).max())
            G_, I_, J_, E_ = moments(rho0, dl, R)
            FR = abs(cplx(Wn) - pred_c(X, R, G_, I_, J_, E_))
            e_exp = max(e_exp, FR)
            if R >= 4 * L / m + 2 * S / m:
                bnd_ok &= FR <= 20 * L**3 / (m * R) and abs(E_) <= 4 * np.pi * S / (m * R)
        rows.append((R, e_poly, e_exp, bnd_ok))
    print('   l=%.2f  R, |W_DR - W_poly|, |F_R| (exact E_R), bounds:' % l, ['%d %.2e %.2e %s' % r for r in rows], flush=True)
    rat = rows[-2][1] / rows[-1][1]
    # the bounds are O(1/R); here the first-order terms of E_R and M_3 vanish by parity of the modes, so the
    # observed rate is 1/R^2 (ratio 4 per doubling)
    ok('T2 l = %.2f: W_DR -> polynomial solution (rate at least 1/R), |F_R| <= 20L^3/(mR), |E_R| <= 4 pi S/(mR)' % l,
       rows[-1][1] < 0.05 * rows[0][1] and rat > 1.6 and all(r[3] for r in rows), 'ratio per doubling %.2f' % rat)
# T3 G != 0: rho_0 = 1 + 0.3 cos phi, delta = 0.5 cos(2 phi); W - (i/pi) R G Xbar converges, expansion holds
r03 = lambda p: 1 + 0.3 * np.cos(p); d3 = lambda p: 0.5 * np.cos(2 * p)
G3, I3, J3, _ = moments(r03, d3, 1e9)
ok('T3 G = 0.075 pi for rho_0 = 1 + 0.3 cos phi', abs(G3 - 0.075 * np.pi) < 1e-12, 'G = %.6f' % G3.real)
rows = []
for R in (10, 40, 160, 640):
    tf = lambda p, R=R: R * r03(p) + d3(p)
    e = 0; gr = 0
    for X in Xs:
        Wn = cplx(W_x2(X, tf)); G_, I_, J_, E_ = moments(r03, d3, R)
        e = max(e, abs(Wn - pred_c(X, R, G_, I_, J_, E_))); gr = max(gr, abs(Wn))
    rows.append((R, e, gr))
print('   T3 R, |F_R|, max|W|:', ['%d %.2e %.1f' % r for r in rows], flush=True)
ok('T3 strain diverges like R G while the remainder decays', rows[-1][2] > 3 * rows[1][2] and rows[-1][1] < rows[0][1] / 30)
# T4 centered ellipses: field is exactly W_circ + (3i/(2pi)) J Xbar^2 with J = (pi/12)((1-mu)^3 - 1)
for (A, B) in ((1.0, 2.0), (2.0, 1.0), (1.0, 7.0), (1.0, 1.3)):
    qv = (B**2 - A**2) / (B**2 + A**2); mu = (1 - np.sqrt(1 - qv**2)) / qv
    Jc = np.pi / 12 * ((1 - mu)**3 - 1)
    e = 0
    for R in (5.0, 50.0):
        tf = lambda p, R=R: R / np.sqrt(np.cos(p)**2 / A**2 + np.sin(p)**2 / B**2)
        for X in Xs:
            e = max(e, abs(cplx(W_x2(X, tf)) - pred_c(X, 0, 0, 0, Jc)))
    ok('T4 ellipse A=%.1f B=%.1f: W = W_circ + (3i/2pi) J Xbar^2, J = %.5f, J != -pi/12' % (A, B, Jc), e < 1e-9 and Jc > -np.pi / 12, 'err %.1e' % e)
# T5 tall ellipses, semi-axes R and R^2 -> (0, -x^2)
rows = []
for R in (4.0, 16.0, 64.0):
    tf = lambda p, R=R: 1.0 / np.sqrt(np.cos(p)**2 / R**2 + np.sin(p)**2 / R**4)
    e = max(np.abs(W_x2(X, tf, 65536) - np.array([0, -X[0]**2])).max() for X in Xs)
    rows.append((R, e))
print('   T5 R, |W - (0,-x^2)|:', rows, flush=True)
ok('T5 tall ellipses (semi-axes R, R^2) converge to (0, -x^2): a family of centered ellipses whose limit is the c_l = 1/2 polynomial solution',
   rows[-1][1] < 0.02 and rows[-1][1] < rows[0][1] / 5)
# T6 symmetric domain: W^(1) odd in y
r06 = lambda p: np.exp(0.2 * np.cos(2 * p) + 0.1 * np.cos(3 * p)); d6 = lambda p: 0.5 * np.cos(p)
tf = lambda p: 12 * r06(p) + d6(p)
e = max(abs(W_x2((X[0], X[1]), tf)[0] + W_x2((X[0], -X[1]), tf)[0]) for X in Xs)
e2 = max(abs(W_x2((X[0], X[1]), tf)[1] - W_x2((X[0], -X[1]), tf)[1]) for X in Xs)
ok('T6 domain symmetric under y -> -y: W^(1) odd and W^(2) even in y', e < 1e-11 and e2 < 1e-11, '%.1e %.1e' % (e, e2))
# T7 part (b) example: M_R for rho_gamma on D_R = {s < t_R(phi)} by direct quadrature of the real DK
def DK_real(Z):
    # Jacobian of K at Z (2 x 2 x n), by analytic differentiation of K = (-2xy, x^2 - y^2)/(2 pi r^4)
    x, y = Z; r2 = x * x + y * y
    K1x = (-2 * y * r2 + 8 * x * x * y) / r2**3 / (2 * np.pi); K1y = (-2 * x * r2 + 8 * x * y * y) / r2**3 / (2 * np.pi)
    K2x = (2 * x * r2 - 4 * x * (x * x - y * y)) / r2**3 / (2 * np.pi); K2y = (-2 * y * r2 - 4 * y * (x * x - y * y)) / r2**3 / (2 * np.pi)
    return np.array([[K1x, K1y], [K2x, K2y]])
# finite-difference check of DK_real
Zt = np.array([[0.7], [-0.4]]); hh = 1e-6
Kr = lambda Z: np.array([-2 * Z[0] * Z[1], Z[0]**2 - Z[1]**2]) / (Z[0]**2 + Z[1]**2)**2 / (2 * np.pi)
fd = np.stack([(Kr(Zt + hh * np.array([[1], [0]])) - Kr(Zt - hh * np.array([[1], [0]]))) / (2 * hh),
               (Kr(Zt + hh * np.array([[0], [1]])) - Kr(Zt - hh * np.array([[0], [1]]))) / (2 * hh)], axis=1)
ok('T7 analytic DK equals finite differences', np.abs(fd - DK_real(Zt)).max() < 1e-7)
def M_R(gam, R, delta, n=4096):
    ph = 2 * np.pi * np.arange(n) / n
    t = (R**(gam - 1) + delta(ph))**(1 / (gam - 1)) if gam > 1 else R * np.exp(delta(ph))
    a = (gam - 2) / 2
    rad = t * hyp2f1(-a, 0.5, 1.5, -t**2)          # int_0^t (1 + s^2)^a ds
    Zm = np.stack([np.cos(ph + np.pi), np.sin(ph + np.pi)])  # -e_phi; DK(-s e_phi) = s^-3 DK(-e_phi)
    D = DK_real(Zm)
    return (D * (np.cos(ph)**2 * rad)[None, None, :]).sum(axis=2) * (2 * np.pi / n)
for gam in (1.0, 1.5, 1.9):
    cg = 1.0 if gam == 1 else 1 / (gam - 1)
    for (dname, dfun, Dl, sd) in (('1 + sin 3phi', lambda p: 1 + np.sin(3 * p), 1j * np.pi / 2, 2.0),
                                  ('0.7(1 - cos 3phi)', lambda p: 0.7 * (1 - np.cos(3 * p)), -0.7 * np.pi / 2, 1.4)):
        cpred = (1j / np.pi) * cg * Dl
        Mp = np.array([[cpred.real, cpred.imag], [cpred.imag, -cpred.real]])
        out = []
        good = True
        for R in (10.0, 40.0, 160.0):
            M = M_R(gam, R, dfun)
            cR = M[0, 0] + 1j * M[1, 0]
            good &= abs(M[0, 1] - M[1, 0]) < 1e-9 and abs(M[0, 0] + M[1, 1]) < 1e-9
            good &= abs(cR - cpred) <= 2 * cg * sd / R**2 * (1 + 1e-9)
            out.append(abs(cR - cpred))
        ok('T7 gamma=%.1f delta=%s: M_R symmetric traceless, -> (i/pi) c_g Delta, |error| <= 2 c_g sup(delta)/R^2' % (gam, dname), good,
           ' '.join('%.1e' % v for v in out))
# T8 part (a): two exhaustions of rho = x^2 (1 + r^2)^(-3/4) (gamma = 1/2) differ by O(R^(-1/2))
def diff_a(R, X, n=2048, ns=256):
    ph = 2 * np.pi * (np.arange(n) + 0.5) / n
    t2 = R * (1.5 + 0.5 * np.sin(3 * ph))
    xg, wg = np.polynomial.legendre.leggauss(ns)
    tot = np.zeros(2)
    for j in range(n):
        s = R + (t2[j] - R) * (xg + 1) / 2; ws = wg * (t2[j] - R) / 2
        Y = np.stack([s * np.cos(ph[j]), s * np.sin(ph[j])])
        rho = Y[0]**2 * (1 + s**2)**(-0.75)
        kern = Kr(np.asarray(X)[:, None] - Y) - Kr(-Y)
        tot += (kern * rho * s * ws).sum(axis=1)
    return tot * (2 * np.pi / n)
vals = [(R, np.abs(diff_a(R, (0.6, -0.5))).max()) for R in (10.0, 40.0, 160.0)]
print('   T8 R, |W_DR - W_DR\'|:', ['%d %.3e' % v for v in vals], flush=True)
ok('T8 class S (gamma = 1/2): exhaustions by disks and by {s < R(1.5 + 0.5 sin 3phi)} differ by ~R^(-1/2)',
   1.6 < vals[0][1] / vals[1][1] < 2.4 and 1.6 < vals[1][1] / vals[2][1] < 2.4)
# T9 bound check at the threshold R = 4L/m + 2S/m with nonzero M_3 (rho_0 = 1/(1 + 0.5 cos 3phi), m = 2/3, S = 0.3)
r09 = lambda p: 1 / (1 + 0.5 * np.cos(3 * p)); d9 = lambda p: 0.3 * np.cos(2 * p); m9 = 2 / 3; S9 = 0.3
worst = 0; rows = []
for L in (1.0, 2.0):
    Rmin = 4 * L / m9 + 2 * S9 / m9
    for R in (Rmin, 2 * Rmin, 8 * Rmin):
        tf = lambda p, R=R: R * r09(p) + d9(p)
        G_, I_, J_, E_ = moments(r09, d9, R)
        fr = 0
        for al in np.linspace(0, 2 * np.pi, 24, endpoint=False):
            X = (L * np.cos(al), L * np.sin(al))
            fr = max(fr, abs(cplx(W_x2(X, tf, 16384)) - pred_c(X, R, G_, I_, J_, E_)))
        b = 20 * L**3 / (m9 * R); worst = max(worst, fr / b)
        rows.append('L=%.0f R=%.2f |F_R|=%.2e bound=%.2e |E_R|=%.1e<=%.1e' % (L, R, fr, b, abs(E_), 4 * np.pi * S9 / (m9 * R)))
        worst = max(worst, abs(E_) / (4 * np.pi * S9 / (m9 * R)))
print('   T9', rows, flush=True)
ok('T9 |F_R| <= 20 L^3/(m R) and |E_R| <= 4 pi S/(m R) on |X| = L at the threshold radius and above', worst <= 1, 'max ratio %.3f' % worst)
print('ALL', all(P), len(P), flush=True)
