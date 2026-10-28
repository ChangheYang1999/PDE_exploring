"""Pin signs of lam_k(a): (T_xx + i T_xy)(r^a e^{ik th}) = lam_k(a) r^a e^{i(k+2) th}.
Claim: lam_k(a) = (k - a) / (2 (k + 2 + a)) for all integer k (k=-2 modulo constants).
Compute  I_k = int [K(e1 - z) - K(-z)] f(z) dz  (absolutely convergent at infinity, p.v. at e1)
with complex kernel K(w) = 1/(2 pi conj(w)^2), f = |z|^a e^{ik arg z}.  Since T f(0) = 0 for
k != -2 (angular cancellation in annuli about 0) and T f(e1) - T f(0) = lam_k for k = -2 as well,
I_k = lam_k for every k.  Polar coordinates about e1, log-substitution for the tail."""
import numpy as np
from scipy import integrate
def lam_formula(k, a): return (k - a)/(2*(k + 2 + a))
def I_k(k, a):
    def inner(s):
        def g(psi):
            z = 1.0 + s*np.exp(1j*psi)
            f = np.abs(z)**a*np.exp(1j*k*np.angle(z))
            Ke1 = np.exp(2j*psi)/(2*np.pi*s*s)          # K(e1 - z), |e1 - z| = s, arg(e1 - z) = psi + pi
            K0 = np.exp(2j*np.angle(z))/(2*np.pi*np.abs(z)**2)  # K(-z) = K(z)
            return (Ke1 - K0)*f*s
        pts = [np.pi] if abs(s-1) < 0.3 else None  # singularity of K(-z) at z=0 (s=1, psi=pi)
        re, _ = integrate.quad(lambda p: g(p).real, 0, 2*np.pi, points=pts, limit=800, epsabs=1e-13, epsrel=1e-11)
        im, _ = integrate.quad(lambda p: g(p).imag, 0, 2*np.pi, points=pts, limit=800, epsabs=1e-13, epsrel=1e-11)
        return re + 1j*im
    tot = 0
    # s in (0,1), (1,2), then t = log s from log 2 to 40
    for (lo, hi) in [(0, 0.5), (0.5, 1.0), (1.0, 2.0)]:
        re, _ = integrate.quad(lambda s: inner(s).real, lo, hi, limit=400, epsabs=1e-11, epsrel=1e-10)
        im, _ = integrate.quad(lambda s: inner(s).imag, lo, hi, limit=400, epsabs=1e-11, epsrel=1e-10)
        tot += re + 1j*im
    re, _ = integrate.quad(lambda t: (inner(np.exp(t))*np.exp(t)).real, np.log(2), 40, limit=800, epsabs=1e-11, epsrel=1e-10)
    im, _ = integrate.quad(lambda t: (inner(np.exp(t))*np.exp(t)).imag, np.log(2), 40, limit=800, epsabs=1e-11, epsrel=1e-10)
    return tot + re + 1j*im
import warnings; warnings.filterwarnings("ignore")
for a in [0.25, 0.7]:
    for k in [-4, -3, -2, -1, 0, 1, 2, 3]:
        v = I_k(k, a)
        print(f"a={a} k={k:+d}: numeric {v.real:+.7f} {v.imag:+.1e}i  formula {lam_formula(k,a):+.7f}  diff {v.real-lam_formula(k,a):+.1e}", flush=True)
