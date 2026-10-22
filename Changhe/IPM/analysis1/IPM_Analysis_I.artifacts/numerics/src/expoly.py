"""Exponential-polynomial splines in t = log r and their closed-form Green integrals (float64 version, to be mirrored
in Arb for the certificate).

A radial function g on a cell [t_a, t_b] is  g(t) = sum_q e^{alpha_q (t - t_a)} p_q(t - t_a)  with polynomials p_q
(coefficients in the local variable tau = t - t_a, ascending powers).  The trial's a_m (modal_fit.Trial) are of this
form on every cell: inner (exponentials 2j, constants), spline cells (alpha = 0, degree 7), outer (exponentials, constants).

Green integrals for the mode f_n(s) (sine mode 2n of d_x rho~), with A_n(r) = r^{-2n} int_0^r s^{2n+1} f_n ds and
B_n(r) = r^{2n} int_r^oo s^{1-2n} f_n ds (so psi_n = (A_n + B_n)/(4n), psi_n' = (B_n - A_n)/(2r)):
  cell moment  m_in(cell)  = int_{t_a}^{t_b} e^{(2n+2)(t - t_b)} f_n(e^t) dt        (weight normalized at the right end)
  cell moment  m_out(cell) = int_{t_a}^{t_b} e^{(2-2n)(t - t_a)} f_n(e^t) dt        (normalized at the left end)
  A_n(t_b) = e^{-2n (t_b - t_a)} A_n(t_a) + e^{2 t_b} m_in(cell),   B_n(t_a) = e^{-2n (t_b - t_a)} B_n(t_b) + e^{2 t_a} m_out(cell).
Within a cell, A_n(t) = e^{-2n(t - t_a)} A_n(t_a) + e^{2t} int_{t_a}^{t} e^{(2n+2)(s - t)} f_n ds, similarly B_n.
The first cell (r < rmin, t -> -infinity) and the last (r > R0, t -> infinity) are half-infinite: closed forms with
the convergence conditions alpha > -2n-2 (inner) and alpha < 2n-2 (outer).
Primitive:  int e^{lam tau} tau^j dtau = e^{lam tau} sum_{l=0}^{j} (-1)^l j!/(j-l)! tau^{j-l} / lam^{l+1}   (lam != 0),
            = tau^{j+1}/(j+1)  (lam = 0).
"""
import numpy as np
from math import factorial


def prim_exp_poly(lam, coeffs, tau):
    """Antiderivative at tau of e^{lam tau} p(tau), p given by ascending coefficients. Vectorized in tau (array)."""
    tau = np.asarray(tau, float)
    if lam == 0.0:
        return sum(c * tau ** (j + 1) / (j + 1) for j, c in enumerate(coeffs))
    out = np.zeros_like(tau)
    for j, c in enumerate(coeffs):
        if c == 0.0: continue
        s = np.zeros_like(tau)
        for l in range(j + 1):
            s += (-1) ** l * factorial(j) / factorial(j - l) * tau ** (j - l) / lam ** (l + 1)
        out += c * s
    return np.exp(lam * tau) * out


def integral_exp_poly(lam, coeffs, tau0, tau1):
    """int_{tau0}^{tau1} e^{lam tau} p(tau) dtau (finite limits). For tau1 = +inf requires lam < 0 (p polynomial),
    for tau0 = -inf requires lam > 0."""
    if np.isinf(tau1):
        assert lam < 0
        up = 0.0
    else:
        up = prim_exp_poly(lam, coeffs, tau1)
    if np.isinf(tau0):
        assert lam > 0
        lo = 0.0
    else:
        lo = prim_exp_poly(lam, coeffs, tau0)
    return up - lo


class ExpPoly:
    """A finite sum of e^{alpha tau} p_alpha(tau) on a cell (local variable tau = t - t_a)."""
    def __init__(self, terms=None):
        self.terms = {}            # alpha -> np.array of ascending coefficients
        if terms:
            for a, c in terms:
                self.add(a, c)

    def add(self, alpha, coeffs):
        coeffs = np.atleast_1d(np.asarray(coeffs, float))
        if alpha in self.terms:
            n = max(len(self.terms[alpha]), len(coeffs)); c = np.zeros(n)
            c[:len(self.terms[alpha])] += self.terms[alpha]; c[:len(coeffs)] += coeffs; self.terms[alpha] = c
        else:
            self.terms[alpha] = coeffs.copy()
        return self

    def scale(self, s):
        return ExpPoly([(a, s * c) for a, c in self.terms.items()])

    def __add__(self, other):
        out = ExpPoly([(a, c) for a, c in self.terms.items()])
        for a, c in other.terms.items(): out.add(a, c)
        return out

    def shift_exp(self, beta):
        """multiply by e^{beta tau}"""
        return ExpPoly([(a + beta, c) for a, c in self.terms.items()])

    def deriv(self):
        """d/dtau"""
        out = ExpPoly()
        for a, c in self.terms.items():
            dc = np.zeros(len(c))
            if len(c) > 1: dc[:-1] += c[1:] * np.arange(1, len(c))
            out.add(a, a * c + dc)
        return out

    def __call__(self, tau):
        tau = np.asarray(tau, float)
        out = np.zeros_like(tau)
        for a, c in self.terms.items():
            p = np.zeros_like(tau)
            for j in range(len(c) - 1, -1, -1): p = p * tau + c[j]
            out += np.exp(a * tau) * p
        return out

    def integral(self, tau0, tau1):
        return sum(integral_exp_poly(a, c, tau0, tau1) for a, c in self.terms.items())


def test():
    rng = np.random.default_rng(0)
    # primitive check by differentiation
    lam, c = 1.7, np.array([0.3, -1.2, 0.5, 2.0])
    tau = np.linspace(-1, 1, 7); h = 1e-6
    d = (prim_exp_poly(lam, c, tau + h) - prim_exp_poly(lam, c, tau - h)) / (2 * h)
    f = np.exp(lam * tau) * np.polyval(c[::-1], tau)
    print("primitive derivative check: %.2e" % np.abs(d - f).max())
    # infinite integral: int_0^inf e^{-2 tau} tau^2 = 2/8 = 0.25
    print("int_0^inf e^{-2tau} tau^2 = %.15f (0.25)" % integral_exp_poly(-2.0, [0, 0, 1.0], 0.0, np.inf))
    print("int_{-inf}^0 e^{3tau} tau = %.15f (-1/9 = %.15f)" % (integral_exp_poly(3.0, [0, 1.0], -np.inf, 0.0), -1 / 9))
    E = ExpPoly([(0.0, [1, 2, 3]), (-1.5, [0.5, 0.1])])
    print("ExpPoly deriv check: %.2e" % np.abs((E(tau + h) - E(tau - h)) / (2 * h) - E.deriv()(tau)).max())


if __name__ == "__main__":
    test()


# ---------------------------------------------------------------------------------------------------------------
# Vectorized (in lam) shifted integrals, stable for small |lam| h (Gauss-Legendre branch) and for large |lam| (closed form)
from numpy.polynomial.legendre import leggauss
_GLX, _GLW = leggauss(32)


def _S(lam, coeffs, tau):
    """Polynomial factor S of the primitive int e^{lam s} p(s) ds = e^{lam tau} S(tau) (entries with lam != 0);
    entries with lam == 0 get the polynomial primitive (no exponential factor to be applied)."""
    lam = np.asarray(lam, float); out = np.zeros_like(lam); nz = lam != 0
    for j, c in enumerate(coeffs):
        if c == 0.0: continue
        s = np.zeros_like(lam)
        for l in range(j + 1):
            s[nz] += (-1) ** l * factorial(j) / factorial(j - l) * tau ** (j - l) / lam[nz] ** (l + 1)
        s[~nz] = tau ** (j + 1) / (j + 1)
        out += c * s
    return out


def integ_shift(lam, coeffs, tau0, tau1, shift, gl_threshold=1.5):
    """int_{tau0}^{tau1} e^{lam (s - shift)} p(s) ds for an array lam and polynomial p (ascending coeffs).
    tau1 = +inf needs lam < 0, tau0 = -inf needs lam > 0.  Finite intervals with |lam| (tau1 - tau0) < gl_threshold use
    32-node Gauss-Legendre (no cancellation; exact to rounding for degree <= 20 and |lam| h <= 1.5); otherwise the closed form
    e^{lam (tau1 - shift)} S(tau1) - e^{lam (tau0 - shift)} S(tau0)."""
    lam = np.asarray(lam, float); out = np.zeros_like(lam)
    coeffs = np.asarray(coeffs, float)
    if np.isinf(tau1): assert (lam < 0).all(), "tail integral needs lam < 0"
    if np.isinf(tau0): assert (lam > 0).all(), "head integral needs lam > 0"
    finite = not (np.isinf(tau0) or np.isinf(tau1))
    if finite:
        h = tau1 - tau0
        small = np.abs(lam) * h < gl_threshold
    else:
        small = np.zeros_like(lam, bool)
    shift = np.broadcast_to(np.asarray(shift, float), lam.shape)
    if small.any():
        s = 0.5 * (tau0 + tau1) + 0.5 * (tau1 - tau0) * _GLX          # (32,)
        pv = np.zeros_like(s)
        for j in range(len(coeffs) - 1, -1, -1): pv = pv * s + coeffs[j]
        E = np.exp(lam[small, None] * (s[None, :] - shift[small, None]))
        out[small] = 0.5 * (tau1 - tau0) * (E * (pv * _GLW)[None, :]).sum(1)
    big = ~small
    if big.any():
        lb = lam[big]; sb = shift[big]; nz = lb != 0
        def end(tau):
            if np.isinf(tau): return np.zeros_like(lb)
            v = _S(lb, coeffs, tau); e = np.ones_like(lb); e[nz] = np.exp(lb[nz] * (tau - sb[nz])); return v * e
        out[big] = end(tau1) - end(tau0)
    return out


def scaled_integral(lam, coeffs, a, b, extra):
    """exp(extra) * int_a^b e^{lam s} p(s) ds, computed without overflow as exp(extra + lam*sh) * int_a^b e^{lam (s - sh)} p ds
    with sh = b where lam > 0 and sh = a where lam <= 0 (so the shifted exponential is <= 1 on [a, b]). lam, extra arrays."""
    lam = np.asarray(lam, float); extra = np.broadcast_to(np.asarray(extra, float), lam.shape)
    sh = np.where(lam > 0, b, a)
    if np.isinf(b): assert (lam < 0).all()
    if np.isinf(a): assert (lam > 0).all()
    I = integ_shift(lam, coeffs, a, b, sh)
    return np.exp(extra + lam * sh) * I


def test_integ_shift():
    rng = np.random.default_rng(1)
    # B-spline-like polynomial with huge coefficients: (1 - tau/h)^7, h = 0.02, lam = 2, shift 0
    h = 0.02; c = np.array([(-1 / h) ** i * factorial(7) / (factorial(i) * factorial(7 - i)) for i in range(8)])
    exact = sum(c[i] * sum((2.0) ** a * h ** (i + a + 1) / (factorial(a) * (i + a + 1)) for a in range(30)) for i in range(8))
    v = integ_shift(np.array([2.0]), c, 0.0, h, 0.0)[0]
    print("integ_shift small-lam test: %.15e vs series %.15e (rel %.1e)" % (v, exact, (v - exact) / exact))
    # large lam: compare closed form with GL by forcing thresholds
    lam = np.array([300.0]); c2 = rng.normal(size=8)
    v1 = integ_shift(lam, c2, 0.0, 0.004, 0.004); v2 = integ_shift(lam, c2, 0.0, 0.004, 0.004, gl_threshold=1e9)
    print("integ_shift large-lam: closed %.15e  GL %.15e (rel %.1e)" % (v1[0], v2[0], (v1[0] - v2[0]) / v1[0]))
