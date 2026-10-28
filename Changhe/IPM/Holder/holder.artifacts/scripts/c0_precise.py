# Higher-accuracy (still heuristic, floating point) evaluation of J(b) and Lambda_0(b).
# Circles about x; on each circle the theta-integrand is split at its kinks (zeros of nu and of K_x),
# located by brentq, and integrated piecewise by Gauss-Legendre. Radial integrals by scipy quad,
# outer region via r = 1/s.
import numpy as np, sys
from scipy.optimize import brentq
from scipy.integrate import quad
GX, GW = np.polynomial.legendre.leggauss(40)
def K(z1, z2, b):
    return np.cos(2*np.arctan2(z2, z1) - 2*b)/(2*np.pi*(z1*z1 + z2*z2))
def nu_polar(r, th, b):
    w1 = 0.5 + r*np.cos(th); w2 = r*np.sin(th)
    return K(0.5-w1, -w2, b) - K(-0.5-w1, -w2, b)
def zeros(fun, a, c, n=720):
    t = np.linspace(a, c, n+1); v = fun(t)
    z = []
    for i in range(n):
        if v[i] == 0.0: z.append(t[i])
        elif v[i]*v[i+1] < 0: z.append(brentq(fun, t[i], t[i+1], xtol=1e-15))
    return z
def piecewise(fun, pts):
    s = 0.0
    for a, c in zip(pts[:-1], pts[1:]):
        if c <= a: continue
        t = 0.5*(c-a)*GX + 0.5*(c+a)
        s += 0.5*(c-a)*np.sum(GW*fun(t))
    return s
def outer_theta(r, b):
    thmax = np.pi if r <= 0.5 else np.arccos(-0.5/r)
    f = lambda th: nu_polar(r, th, b)
    pts = sorted([-thmax, thmax] + zeros(f, -thmax, thmax))
    return r*piecewise(lambda th: np.abs(f(th)), pts)
def inner_theta(r, b):
    f = lambda th: nu_polar(r, th, b)
    kz = [((np.pi/2)*(k+0.5) + b) % (2*np.pi) for k in range(4)]  # zeros of cos(2th-2b)
    pts = sorted([0.0, 2*np.pi] + zeros(f, 0.0, 2*np.pi) + kz)
    g = lambda th: np.abs(f(th)) - np.abs(K(-r*np.cos(th), -r*np.sin(th), b))
    return r*piecewise(g, pts)
def J(b):
    o1 = quad(lambda r: outer_theta(r, b), 0.5, 2.0, limit=200, epsabs=1e-12, epsrel=1e-11)[0]
    o2 = quad(lambda s: outer_theta(1.0/s, b)/s**2, 1e-9, 0.5, limit=200, epsabs=1e-12, epsrel=1e-11)[0]
    i1 = quad(lambda r: inner_theta(r, b), 0.0, 0.5, limit=200, epsabs=1e-12, epsrel=1e-11)[0]
    return o1 + o2 + i1, (o1, o2, i1)
if __name__ == "__main__":
    for b in [eval(s) for s in sys.argv[1:]]:
        Jb, parts = J(b)
        print(f"b={b:.6f} J={Jb:.10f} parts={parts} Lambda0={-(1+np.log(2))/np.pi + Jb:.10f}", flush=True)
