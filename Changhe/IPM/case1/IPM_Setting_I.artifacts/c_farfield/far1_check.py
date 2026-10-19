import sys, numpy as np
sys.path.insert(0, '.')
# usage: python3 far1_check.py [coef_shape.npz [export_fields.npz]] (defaults: the candidate and its export)
SHAPE = sys.argv[1] if len(sys.argv) > 1 else 'c6g_shape.npz'
EXPORT = sys.argv[2] if len(sys.argv) > 2 else 'c6gx_fields.npz'
from far1 import run
o, (th, Th0, Th1f, Th1e) = run(SHAPE, verbose=False)
k = o['k']; L = o['L']; cl = o['c_l']
z = np.load(EXPORT, mmap_mode='r')
r = np.array(z['r']); tq = np.array(z['theta'])
print('r range', r[0], r[-1], 'theta', tq[0], tq[-1], len(tq))
# recompute F on the export angles by re-running FFT synthesis at those angles
from far1 import Trial
N = len(th)
# interpolate F, F' from the uniform grid (periodic, fine) -- use the run internals again
import far1
t = Trial(o['path'])
# psi0 angular F: rebuild quickly
m = np.arange(t.angular+1); a = t.p3-2
b1 = t.spline(1.0); from numpy.polynomial.chebyshev import chebval; T1 = chebval(1.0, t.singular)
c, s = np.cos(th), np.sin(th); ac = np.abs(c)
E = np.cos(2*np.outer(th, m))@b1+T1*ac**a*s**2
Ep = np.sin(2*np.outer(th, m))@(-2*m*b1)+T1*(2*ac**(a+1)*np.sign(c)*s-a*ac**(a-1)*np.sign(c)*s**3)
pre = L**(3-k)*np.exp(E); T0 = pre*c*c*s; T0p = pre*((c**3-2*c*s*s)+c*c*s*Ep)
g = k*c*T0-s*T0p
Gh = np.fft.rfft(g)/N; sinco = -2*Gh.imag; j = np.arange(len(Gh))[2::2]; Gn = sinco[2::2]; n = j//2
Fn = Gn/(4*n*n-(k+1)**2)
F = lambda x: np.sin(np.outer(x, j))@Fn
Fp = lambda x: np.cos(np.outer(x, j))@(j*Fn)
Fq, Fpq = F(tq), Fp(tq)
U1 = z['U1']; U2 = z['U2']
for rr in [100*L, 446*L, 1000*L, 3000*L, 5000*L]:
    i = np.argmin(np.abs(r-rr))
    ct, st = np.cos(tq), np.sin(tq)
    Ur = U1[i]*ct+U2[i]*st; Ut = -U1[i]*st+U2[i]*ct
    Ur0 = -r[i]**k*Fpq; Ut0 = (k+1)*r[i]**k*Fq
    sc = np.max(np.abs(Ut0))
    print('r/L %.0f  max|Ur-Ur0|/max|Ut0| %.3e  max|Ut-Ut0|/max|Ut0| %.3e   r^(k-1) %.3e' % (r[i]/L, np.max(np.abs(Ur-Ur0))/sc, np.max(np.abs(Ut-Ut0))/sc, r[i]**(k-1)))
# far residual profile along near-axis columns
res = z['residual']; den = z['denominator']
for jt in [len(tq)-2, len(tq)-4, len(tq)-10, 300]:
    th0 = tq[jt]
    dth = np.interp(th0, th[:N//4+1], (Th1f-Th1e)[:N//4+1])
    print('column theta %.5f  dTh1 = Th1f-Th1e %+.3e' % (th0, dth))
    for rr in [500*L, 900*L, 1000*L, 2000*L, 4700*L, 8000*L, 9500*L]:
        i = np.argmin(np.abs(r-rr))
        print('   r/L %6.0f  residual/denominator %+.3e   predicted (c_l-1)(Th1e-Th1f) r^(k-1)/(1+k) %+.3e' % (r[i]/L, res[i, jt]/den[i, jt], -(cl-1)*dth*r[i]**(k-1)/(1+k)))
