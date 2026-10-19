"""B_3 diagnostic for IPM Setting I (lead lane).

Axis data on [0, x*] (x* = first positive zero of w):
  w(x)  = W_1(x,0)              (odd, w ~ -A x at 0, w ~ A (x - x*) at x*, A = 2 c_l - 1)
  h(x)  = d_y W_2(x,0)          (even, h(0) = 2A + 1, h(x*) = 1, w' + h = 2 c_l)
  a2(x) = (1/2) d_y^2 W_1(x,0)  (odd)
  b3(x) = (1/6) d_y^3 W_2(x,0)  (even)
  g1(x) = d_y rho(x,0)          (even, ~ x^2 at 0)
  g1p   = d_x g1
G_3 = (1/6) d_y^3 rho(x,0) solves  w G_3' + (3h - 1) G_3 = F_3 := -a2 g1p - b3 g1,  regular at x*.
Near 0, G_3 = (smooth even) + B_3 H(x), H(x) = x^{p3} e^{E(x)}, E even, E(0) = 0, p3 = 6 + 2/A.

Methods:
  fp  : B_3 = f.p. int_0^{x*} [-F_3/(w H)] dt  (analysis.md 3.2)
  ode : integrate the G_3 ODE from x* (regular branch) to small x, fit even polynomial + B H
  fit : given G_3 samples near 0, fit even polynomial + B H (needs H, i.e. w and h)
Run as a script: manufactured test with exact B_3 (Beta functions).
"""
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.special import gamma, roots_jacobi
from scipy.integrate import solve_ivp


def _cheb_nodes(n, a, b):
    k = np.arange(n)
    t = np.cos(np.pi * (k + 0.5) / n)  # first kind: interior nodes only
    return 0.5 * (a + b) + 0.5 * (b - a) * t, t


class AxisData:
    """Callables for w, h, a2, b3, g1, g1p on [-xs/2, xs] (extend to x < 0 by parity:
    w, a2, g1p odd; h, b3, g1 even); cl = c_l."""

    def __init__(self, w, h, a2, b3, g1, g1p, cl, xs, ncheb=96):
        self.w, self.h, self.a2, self.b3, self.g1, self.g1p = w, h, a2, b3, g1, g1p
        self.cl, self.xs = cl, xs
        self.A = 2 * cl - 1
        self.p3 = 6 + 2 / self.A
        self.beta = 2 / self.A
        A, p3 = self.A, self.p3
        # remainder r = (1-3h)/w - p3/x + (2/A)/(x - xs): regular on [-xs/2, xs]
        self.ia, self.ib = -0.5 * xs, xs
        x, t = _cheb_nodes(ncheb, self.ia, self.ib)
        r = (1 - 3 * h(x)) / w(x) - p3 / x + (2 / A) / (x - xs)
        self.r_c = C.chebfit(t, r, ncheb - 1)
        Ri = C.chebint(self.r_c) * ((self.ib - self.ia) / 2)
        Ri[0] -= C.chebval(self._t(0.0), Ri)  # R(0) = 0
        self.R_c = Ri

    def _t(self, x):
        return (2 * np.asarray(x) - (self.ia + self.ib)) / (self.ib - self.ia)

    def F3(self, x):
        return -self.a2(x) * self.g1p(x) - self.b3(x) * self.g1(x)

    def R(self, x):
        return C.chebval(self._t(x), self.R_c)

    def H(self, x):
        """Homogeneous solution normalized H ~ x^p3 at 0 (0 < x < xs)."""
        x = np.asarray(x, float)
        return x ** self.p3 * (1 - x / self.xs) ** (-2 / self.A) * np.exp(self.R(x))

    def E(self, x):
        """H = x^p3 exp(E): E = R - (2/A) log(1 - x/xs) (even if the data have the right parity)."""
        x = np.asarray(x, float)
        return self.R(x) - (2 / self.A) * np.log1p(-x / self.xs)

    def phi_x(self, x):
        """phi = F3/(x^2 omega e^R xs), omega = w/(x (x - xs)); then -F3/(wH) = x^{1-p3} (1-x/xs)^{beta-1} phi."""
        x = np.asarray(x, float)
        om = self.w(x) / (x * (x - self.xs))
        return self.F3(x) / (x ** 2 * om * np.exp(self.R(x)) * self.xs)

    def b3_fp(self, delta=0.4, nloc=24, nfft=64, njac=120, even=True):
        """B_3 = xs^{2-p3} f.p. int_0^1 u^q Phi(u) du, q = 1 - p3, Phi = (1-u)^{beta-1} phi(xs u) (even in u for
        parity-consistent data).
        [0, rho0]: Taylor coefficients Phi_n by FFT on |u| = rho0 (phi continued analytically from a Chebyshev fit on
        [-delta, delta]); f.p. = sum_n Phi_n rho0^{q+n+1}/(q+n+1), with Phi_n log(rho0) if q+n+1 = 0 (that coefficient is
        reported; it vanishes when Phi is even and p3 is not an even integer).
        [rho0, 1]: Gauss-Jacobi with weight (1-u)^{beta-1}.
        even=True (default): Phi is exactly even for parity-consistent data, so the odd Taylor coefficients are set to zero
        before the finite part is taken. Otherwise a spurious odd coefficient Phi_5 ~ 1e-10 is divided by 7 - p3 and the
        result is wrong near c_l = 3/2 (astra audit2 item 3). The measured odd content is reported as odd_rel."""
        p3, be, xs = self.p3, self.beta, self.xs
        q = 1 - p3
        _, t = _cheb_nodes(nloc, -1.0, 1.0)
        ph_c = C.chebfit(t, self.phi_x(xs * delta * t), nloc - 1)
        rho0 = delta / 2
        th = 2 * np.pi * np.arange(nfft) / nfft
        uc = rho0 * np.exp(1j * th)
        Phi = (1 - uc) ** (be - 1) * C.chebval(uc / delta, ph_c)
        coef = np.fft.fft(Phi) / nfft / rho0 ** np.arange(nfft)  # Phi_n
        sc = np.abs(coef[:nfft // 2]) * rho0 ** np.arange(nfft // 2)  # scaled raw coefficients |Phi_n| rho0^n
        odd = float(np.max(sc[1::2]) / np.max(sc))
        n = np.arange(nfft // 2)
        if even:
            coef = coef.copy()
            coef[1::2] = 0.0
        e = q + n + 1
        res = abs(e) < 1e-9
        I0 = np.sum(np.where(res, 0.0, coef[n] * rho0 ** np.where(res, 1.0, e) / np.where(res, 1.0, e)))
        I0 = I0 + np.sum(np.where(res, coef[n] * np.log(rho0), 0.0))
        tj, wj = roots_jacobi(njac, be - 1, 0.0)
        uu = rho0 + (1 - rho0) * (1 + tj) / 2
        I1 = ((1 - rho0) / 2) ** be * np.sum(wj * uu ** q * self.phi_x(xs * uu))
        val = xs ** (2 - p3) * (I0 + I1)
        logc = float(np.abs(coef[n][res]).max()) if res.any() else 0.0
        return val.real, dict(I0=I0.real, I1=I1, imag=abs(val.imag), log_coef=logc, odd_rel=odd,
                              fft_tail=float(np.max(np.abs(coef[nfft // 2 - 4:nfft // 2]) * rho0 ** n[-4:])))

    def g3_ode(self, x_end, eps=1e-3, rtol=1e-12, atol=1e-14):
        """Regular-at-x* branch of the G_3 ODE, integrated from xs - eps down to x_end."""
        xs, A = self.xs, self.A
        # local series at xs: G(xs) = F3/2, (A+2) G'(xs) = F3'(xs) - 3 h'(xs) G(xs)
        dx = 1e-5 * xs
        F3s = self.F3(xs)
        F3p = (self.F3(xs + dx) - self.F3(xs - dx)) / (2 * dx)
        hp = (self.h(xs + dx) - self.h(xs - dx)) / (2 * dx)
        G0 = F3s / 2
        G1 = (F3p - 3 * hp * G0) / (A + 2)
        x0 = xs - eps
        y0 = G0 + G1 * (x0 - xs)

        def rhs(x, y):
            return [(self.F3(x) - (3 * self.h(x) - 1) * y[0]) / self.w(x)]

        sol = solve_ivp(rhs, [x0, x_end], [y0], method='DOP853', rtol=rtol, atol=atol, dense_output=True)
        return sol

    def b3_fit(self, x, g3, npoly=10):
        """Least squares: g3 = sum_{n=1}^{npoly} c_n x^{2n} + B H(x). Returns B and residual."""
        x = np.asarray(x, float)
        cols = [x ** (2 * k) for k in range(1, npoly + 1)] + [self.H(x)]
        M = np.stack(cols, axis=1)
        s = np.max(np.abs(M), axis=0)
        coef, *_ = np.linalg.lstsq(M / s, g3, rcond=None)
        coef = coef / s
        res = g3 - M @ coef
        return coef[-1], np.max(np.abs(res)), coef


def manufactured(cl=1.3, alpha0=0.7, beta0=-0.4, xs=1.0):
    """w = -A x (1-u^2)/(1+u^2)*xs-scaling, exact H, G1; exact B_3 by Beta functions (xs = 1 only)."""
    assert xs == 1.0
    A = 2 * cl - 1
    w = lambda x: -A * x * (1 - x ** 2) / (1 + x ** 2)
    wp = lambda x: -A * (1 - 4 * x ** 2 - x ** 4) / (1 + x ** 2) ** 2
    h = lambda x: 2 * cl - wp(x)
    g1 = lambda x: x ** 2 / (1 + x ** 2)
    g1p = lambda x: 2 * x / (1 + x ** 2) ** 2
    a2 = lambda x: alpha0 * x
    b3 = lambda x: beta0 + 0 * x
    p3 = 6 + 2 / A
    be = 2 / A
    # -F3/(wH) = -(1/A) t^{1-p3} (1-t^2)^{be-1} [2 alpha0 (1+t^2)^2 + beta0 (1+t^2)^3]
    # f.p. int_0^1 t^{1-p3+2m} (1-t^2)^{be-1} dt = (1/2) B(m + 1 - p3/2, be)
    poly = 2 * alpha0 * np.array([1, 2, 1, 0]) + beta0 * np.array([1, 3, 3, 1])  # coefficients of u^m, u = t^2
    Bf = lambda a, b: gamma(a) * gamma(b) / gamma(a + b)
    exact = -(1 / A) * sum(poly[m] * 0.5 * Bf(m + 1 - p3 / 2, be) for m in range(4))
    H_exact = lambda x: x ** p3 * (1 - x ** 2) ** (-be) * (1 + x ** 2) ** (-3)
    return AxisData(w, h, a2, b3, g1, g1p, cl, xs), exact, H_exact


if __name__ == '__main__':
    for cl in (1.3, 1.49999999, 1.5, 1.50000001, 2.2):
        d, exact, Hx = manufactured(cl=cl)
        xx = np.linspace(0.05, 0.95, 7)
        errH = np.max(np.abs(d.H(xx) / Hx(xx) - 1))
        bfp, info = d.b3_fp()
        sol = d.g3_ode(0.02)
        xf = np.linspace(0.02, 0.35, 400)
        g3 = sol.sol(xf)[0]
        bfit, res, _ = d.b3_fit(xf, g3, npoly=12)
        print(f"c_l={cl}: p3={d.p3:.6f}  H rel err={errH:.2e}  exact B3={exact:.12e}")
        print(f"   fp  B3={bfp:.12e}  rel err={abs(bfp/exact-1):.2e}  (I0={info['I0']:.4e}, I1={info['I1']:.4e}, log coef {info['log_coef']:.1e}, odd/even {info['odd_rel']:.1e}, tail {info['fft_tail']:.1e})")
        print(f"   ode+fit B3={bfit:.12e}  rel err={abs(bfit/exact-1):.2e}  fit resid={res:.1e}")
    # smooth case: F3 chosen so that G3 is smooth => B3 = 0
    cl = 1.4
    d0, _, _ = manufactured(cl=cl)
    A = 2 * cl - 1
    Gs = lambda x: x ** 4 / (1 + x ** 2)          # smooth even target
    Gsp = lambda x: (4 * x ** 3 * (1 + x ** 2) - 2 * x ** 5) / (1 + x ** 2) ** 2
    F3s = lambda x: d0.w(x) * Gsp(x) + (3 * d0.h(x) - 1) * Gs(x)
    # realize F3s = -a2 g1p - b3 g1 with a2 = 0, b3 = -F3s/g1
    d1 = AxisData(d0.w, d0.h, lambda x: 0 * x, lambda x: -F3s(x) / d0.g1(x), d0.g1, d0.g1p, cl, 1.0)
    bfp, _ = d1.b3_fp()
    print(f"smooth-target test (exact B3 = 0): fp B3 = {bfp:.3e}  (scale: G3(0.5) = {Gs(0.5):.3e})")
