# X3 part of (o3) item 1: subtract the classical s^2 Taylor term (convergent since 2+2A < g*) and the
# analytically continued s^4 term, then compare (G3 - G3(0) - c2 s^2 - c4 s^4)/s^p* with Ke.
import json, numpy as np, mpmath as mp
d = json.load(open('runs/frozen_g3_even.json'))
x, w = np.polynomial.legendre.leggauss(200)
def bump(t, a):
    out = np.zeros_like(t); m = (t > a) & (t < a+1); out[m] = np.exp(-1/((t[m]-a)*(a+1-t[m]))); return out
t1 = 0.5*x+1.5; t2 = 0.5*x+2.5; w = 0.5*w
tn = np.concatenate([t1, t2]); tw = np.concatenate([w, w]); ph = np.concatenate([bump(t1, 1), -bump(t2, 2)])
res = []
for c in d:
    A, g = c['A'], c['g']; b = g/(2*(A-1)); q = 2*A-2; ps = (g-2)/A
    def coef(n):  # coefficient of s^(2n) in the cos expansion, Beta continuation when supercritical
        r = (2+2*n*A)/q
        B = float(mp.beta(r, b-r))
        return (-1)**n/float(mp.factorial(2*n))/(6*np.pi**2)*np.sum(tw*ph*tn**(2*n)*tn**(-2*r))/q*B
    c2, c4 = coef(1), coef(2)
    print('A=%g g=%g  c2 = %.10e  c4 = %.10e  Ke = %.10e' % (A, g, c2, c4, c['Ke']))
    for r in c['rows']:
        s = r['s']; D = r['G3_minus_G0']
        r1 = (D-c2*s**2)/s**ps; r2 = (D-c2*s**2-c4*s**4)/s**ps
        print('   s=%.0e  (D-c2 s^2)/s^p* = %.10e   (D-c2 s^2-c4 s^4)/s^p* = %.10e   rel err %.1e' % (s, r1, r2, abs(r2/c['Ke']-1)))
        res.append(dict(A=A, g=g, s=s, c2=c2, c4=c4, r1=r1, r2=r2))
json.dump(res, open('runs/frozen_g3_even_x3.json', 'w'), indent=1)
