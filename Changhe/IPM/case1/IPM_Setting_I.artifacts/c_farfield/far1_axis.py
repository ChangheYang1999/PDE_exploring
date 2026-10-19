"""Axis limit of the forced first correction: V_r(pi/2) = -F'(pi/2), Theta_1e(pi/2) = -(k+2) V_r(pi/2)/(c_l-1)."""
import sys, numpy as np
import os
_here = os.path.dirname(os.path.abspath(__file__))
for _d in ('c7', os.path.join(_here, '..', 'b_fit_domain')):
    if os.path.isdir(_d): sys.path.insert(0, _d)
from trial import Trial
from numpy.polynomial.chebyshev import chebval, chebder
def axis(path, N=1 << 15):
    t = Trial(path); k, L = t.k, t.L; cl = 1/k; a = t.p3-2
    b1 = t.spline(1.0); bp1 = t.spline(1.0, nu=1)
    T1 = chebval(1.0, t.singular); Tp1 = chebval(1.0, chebder(t.singular))
    th = 2*np.pi*np.arange(N)/N; m = np.arange(t.angular+1)
    c, s = np.cos(th), np.sin(th); ac = np.abs(c)
    cosm = np.cos(2*np.outer(th, m)); sinm = np.sin(2*np.outer(th, m))
    ang = ac**a*s**2; ang_t = 2*ac**(a+1)*np.sign(c)*s-a*ac**(a-1)*np.sign(c)*s**3
    E = cosm@b1+T1*ang; Ep = sinm@(-2*m*b1)+T1*ang_t
    pre = L**(3-k)*np.exp(E); Th0 = pre*c*c*s; Th0p = pre*((c**3-2*c*s*s)+c*c*s*Ep)
    g = k*c*Th0-s*Th0p
    Gh = np.fft.rfft(g)/N; sinco = -2*Gh.imag
    n = np.arange(1, N//4); Gn = sinco[2*n]; Fn = Gn/(4*n*n-(k+1)**2)
    Fp_axis = np.sum(2*n*Fn*np.cos(n*np.pi))
    Vr = -Fp_axis
    Th1e_axis = -(k+2)*Vr/(cl-1)
    Th1f_axis = -L**(1-k)*(np.sum(bp1*np.cos(m*np.pi)))  # singular term vanishes at the axis
    return Vr, Th1e_axis, Th1f_axis
if __name__ == '__main__':
  for p in sys.argv[1:]:
    for N in (1 << 14, 1 << 15, 1 << 16):
        Vr, e, f = axis(p, N)
        print(p.split('/')[-1], N, 'V_r(pi/2) %.7f  Th1e(pi/2) %.6f  Th1f(pi/2) %.6f  f-e %+.4e' % (Vr, e, f, f-e))
