"""Verify kernel normalization and homogeneous-mode multipliers of T = T_xx + i T_xy.

Conventions (PROMPT.md): R_j = d_j (-Delta)^{-1/2}; T_xx = R_1^2 + I/2 = (R_1^2 - R_2^2)/2;
T_xy = R_1 R_2.  Claimed p.v. kernels: K_xx = cos(2 th)/(2 pi r^2), K_xy = sin(2 th)/(2 pi r^2),
so (T_xx + i T_xy) f (x) = p.v. int  e^{2 i th(x-z)} / (2 pi |x-z|^2) f(z) dz.

Test 1 (normalization): f = exp(-r^2).  Exact: (-Delta)^{-1} f radial => R_1^2 f computed
by hand gives T_xx f = (1 - (1+r^2) e^{-r^2}) / (2 r^2) * cos(2 th).  Compare with p.v. kernel
integral at a few points.

Test 2 (homogeneous multipliers): f = r^a e^{i k th}.  T f = lam_k(a) r^a e^{i (k+2) th} (mod
constants when k = -2).  Candidate A: lam_k = (1/2) (k - a)/(k + 2 + a) up to sign.
Candidate B: lam_k = -(1/2) (k + a)/(k + 2 + a).  Compute lam_k = T f(e_1) by a p.v. integral
in polar coordinates centred at e_1 (k != -2), and T f(e_1) - T f(0) for k = -2.
"""
import numpy as np
from scipy import integrate

def K_complex(w):
    # e^{2 i arg w} / (2 pi |w|^2) = w^2/(2 pi |w|^4) = 1/(2 pi conj(w)^2)
    return 1.0/(2*np.pi*np.conj(w)**2)

# ---------- Test 1 ----------
def Txx_gauss_exact(x, y):
    r2 = x*x + y*y
    th = np.arctan2(y, x)
    return (1 - (1 + r2)*np.exp(-r2))/(2*r2)*np.cos(2*th)

def Txx_gauss_pv(x, y):
    # polar coordinates around (x,y): z = p + s e^{i psi}; K(p - z) = cos(2 psi)/(2 pi s^2) (even kernel)
    def inner(s):
        val, _ = integrate.quad(lambda psi: np.cos(2*psi)*np.exp(-((x + s*np.cos(psi))**2 + (y + s*np.sin(psi))**2)),
                                0, 2*np.pi, limit=200, epsabs=1e-13, epsrel=1e-12)
        return val/(2*np.pi*s)
    val, _ = integrate.quad(inner, 0, 12, limit=400, epsabs=1e-12, epsrel=1e-11)
    return val

print("Test 1: T_xx exp(-r^2), exact vs p.v. kernel integral")
for (x, y) in [(0.7, 0.2), (1.5, -0.4), (0.3, 1.1), (2.5, 0.0)]:
    e = Txx_gauss_exact(x, y); n = Txx_gauss_pv(x, y)
    print(f"  point ({x},{y}): exact {e:+.10f}  pv {n:+.10f}  diff {e-n:+.2e}")

# ---------- Test 2 ----------
def lam_direct(k, a):
    """T f (e_1) with f = r^a e^{ik th}, p.v. in polar coordinates about e_1 (valid for k != -2)."""
    def inner(s):
        def g(psi):
            z = 1.0 + s*np.exp(1j*psi)
            return (np.abs(z)**a*np.exp(1j*k*np.angle(z)))
        re, _ = integrate.quad(lambda psi: (np.cos(2*psi)*g(psi)).real, 0, 2*np.pi, limit=400, epsabs=1e-13, epsrel=1e-12)
        im, _ = integrate.quad(lambda psi: (np.cos(2*psi)*g(psi)).imag, 0, 2*np.pi, limit=400, epsabs=1e-13, epsrel=1e-12)
        return (re + 1j*im)/(2*np.pi*s)
    # split radial integral: [0,1-], [1,3], [3, inf) with tail decaying like s^{a-2}
    pieces = []
    for (lo, hi) in [(0, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, 8.0), (8.0, 64.0), (64.0, 2000.0)]:
        re, _ = integrate.quad(lambda s: inner(s).real, lo, hi, limit=400, epsabs=1e-11, epsrel=1e-10)
        im, _ = integrate.quad(lambda s: inner(s).imag, lo, hi, limit=400, epsabs=1e-11, epsrel=1e-10)
        pieces.append(re + 1j*im)
    return sum(pieces)

def candA(k, a): return 0.5*(k - a)/(k + 2 + a)
def candB(k, a): return -0.5*(k + a)/(k + 2 + a)

print("\nTest 2: T_xx(r^a e^{ik th})(e_1) by p.v. quadrature about e_1 with the REAL kernel cos(2psi) (tail cut at s=2000);\n  this equals (lam_k + lam_{-k})/2 for the complex multipliers lam_k; compared with candidates A, B")
for a in [0.3, 0.6]:
    for k in [-4, -3, -1, 0, 1, 2, 3]:
        v = lam_direct(k, a)
        avgA = 0.5*(candA(k,a) + candA(-k,a)) if k != -2 and k != 2 else float('nan')
        avgB = 0.5*(candB(k,a) + candB(-k,a)) if k != -2 and k != 2 else float('nan')
        print(f"  a={a} k={k:+d}: T_xx value {v.real:+.6f}{v.imag:+.1e}i   (candA(k)+candA(-k))/2 {avgA:+.6f}   (candB(k)+candB(-k))/2 {avgB:+.6f}   [k=+-2: tail-divergent, not comparable]")
