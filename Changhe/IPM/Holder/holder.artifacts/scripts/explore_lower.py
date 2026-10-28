# Exploratory lower bound for the two-point gated test function (non-rigorous quadrature).
# u(z) = (1/2) sgn(|z1|-|z2|) (sqrt2 ||z1|-|z2||)^a ; [u]_a <= 1, homogeneous, circle-optimal.
# v_x = clamp(u(w-x), -h, h), h = min(1/2, (1/2)(2 w1)_+^a);  f(w) = v_x(w) - v_x(-w)  (odd, [f]_a <= 1).
# Lower bound: C_a >= T f(x) - T f(y) = 2 p.v. \int K_xx(x-w) f(w) dw  (x = (1/2,0)).
import numpy as np
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(64)
def gl(a, b):
    return 0.5*(b-a)*xg + 0.5*(b+a), 0.5*(b-a)*wg
def W(a): return 2**(1+a/2)/(np.pi*(2+a))
def u(z1, z2, a):
    t = np.abs(z1) - np.abs(z2)
    return 0.5*np.sign(t)*(np.sqrt(2)*np.abs(t))**a
def vx(w1, w2, a, cap=0.5, kappa=1.0):
    h = np.minimum(cap, 0.5*kappa*(2*np.clip(w1, 0, None))**a)
    return np.clip(u(w1-0.5, w2, a), -h, h)
def f(w1, w2, a, **kw):
    return vx(w1, w2, a, **kw) - vx(-w1, -w2, a, **kw)
def Kxx(z1, z2):
    r2 = z1**2+z2**2
    return (z1**2-z2**2)/(2*np.pi*r2**2)
def lower(a, r0=0.25, R1=60.0, nr=60, nphi=64, **kw):
    # region B(x,r0): exact W r0^a/a (f = u_x there provided r0 <= 1/(2+sqrt2))
    tot = W(a)*r0**a/a
    # polar around x: r in (r0, R1), phi in (0,2pi) with many panels
    rb = np.geomspace(r0, R1, nr+1)
    pb = np.linspace(0, 2*np.pi, nphi+1)
    for r_0, r_1 in zip(rb[:-1], rb[1:]):
        r, wr = gl(r_0, r_1)
        for p0, p1 in zip(pb[:-1], pb[1:]):
            ph, wph = gl(p0, p1)
            R, PH = np.meshgrid(r, ph, indexing='ij')
            w1 = 0.5 - R*np.cos(PH); w2 = -R*np.sin(PH)   # w = x - z, z = r e^{i phi}
            val = Kxx(R*np.cos(PH), R*np.sin(PH))*f(w1, w2, a, **kw)*R
            tot += np.einsum('i,j,ij->', wr, wph, val)
    return 2*tot
if __name__ == "__main__":
    for a in [0.02, 0.05, 0.1, 0.25, 0.5, 0.75]:
        L = lower(a)
        print(f"a={a} L={L:.4f} 2/(pi a)={2/(np.pi*a):.4f} L-2/(pi a)={L-2/(np.pi*a):.4f}", flush=True)
