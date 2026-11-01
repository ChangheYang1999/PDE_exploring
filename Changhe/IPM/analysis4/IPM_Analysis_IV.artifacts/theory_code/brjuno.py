"""Continued fractions and truncated Brjuno sums B2 = sum_k log(2 q_{k+1})/q_k for alpha = delta/2."""
import mpmath as mp
from fractions import Fraction
mp.mp.dps = 200

def cf_real(x, kmax=60):
    a = []; 
    for _ in range(kmax):
        ai = int(mp.floor(x)); a.append(ai); fr = x - ai
        if fr < mp.mpf(10)**(-150): break
        x = 1/fr
    return a

def cf_frac(fr):
    a = []
    p, q = fr.numerator, fr.denominator
    while q:
        a.append(p//q); p, q = q, p - (p//q)*q
    return a

def convergent_denoms(a):
    q = [1, a[1]] if len(a) > 1 else [1]
    for k in range(2, len(a)):
        q.append(a[k]*q[-1] + q[-2])
    return q

def B2(a, qmax=None):
    q = convergent_denoms(a)
    s = mp.mpf(0); terms = []
    for k in range(len(q)-1):
        t = mp.log(2*q[k+1])/q[k]; s += t; terms.append((q[k], q[k+1], float(t)))
    return s, terms

if __name__ == '__main__':
    d = 1/mp.sqrt(5); al = d/2
    a = cf_real(al, 40); print('delta=1/sqrt5, alpha=delta/2 cf:', a[:20])
    s, t = B2(a); print('B2 (40 terms):', mp.nstr(s, 10)); print(t[:8])
    N = 4076476460239181; D = 2**51
    cl = Fraction(N, D); dl = 1 - 1/cl; al = dl/2
    print('007 delta =', dl, float(dl))
    a = cf_frac(al); print('007 alpha cf (len %d):' % len(a), a)
    q = convergent_denoms(a); print('q_k:', q)
    s, t = B2(a); print('B2 partial (all finite terms):', mp.nstr(s, 10))
    for x in t: print('  q_k=%d q_k+1=%d term=%.4g' % x)
    # golden-type nearby: alpha with cf [0;4,2,1,1,1,...]
