"""Top-mode radius R_H = 4d [a B(a,b)]^(1/a) of Section 14.22 (B = L+1, eta = B - delta, a = 2/eta, b = 2(B-1)/eta,
d = c-1) and a check against the scalar top recursion (14.22.1) without restriction; lower bounds (|alpha|/R_H)^(1/delta)
for the required exterior radius (Section 12.6, Remark 3) at given top coefficients alpha."""
import sys
from mpmath import mp, mpf, beta
mp.dps = 30
def RH(delta, B):
    d = 1/(1-delta) - 1
    eta = B - delta; a = 2/eta; b = 2*(B-1)/eta
    return 4*d*(a*beta(a, b))**(1/a)
def rec(delta, B, N):
    d = 1/(1-delta) - 1; eta = B - delta
    h = [0, mpf(1)]
    for n in range(2, N+1):
        s = sum((2*B*(n-i)/(eta*i+2) - 1)*h[i]*h[n-i] for i in range(1, n))
        h.append(s/(4*d*(n-1)))
    return h
for dl in [mpf(2)/5, mpf(1)/2, mpf(1)/3, mpf(4)/9, mpf(3)/5]:
    r = RH(dl, 4)
    h = rec(dl, 4, 1500)
    print('delta=%s R_H=%s  h_1500^(-1/1500)=%s  h_1499/h_1500=%s' % (mp.nstr(dl,6), mp.nstr(r,10), mp.nstr(h[1500]**(-mpf(1)/1500),8), mp.nstr(h[1499]/h[1500],10)))
dl = mpf(3)/5; r = RH(dl, 4)
for b in ['0.0659472179', '0.1093408010', '0.3505637599', '0.5942044255']:
    print('b=%s lower bound (|b|/R_H)^(5/3) = %s' % (b, mp.nstr((mpf(b)/r)**(1/dl), 6)))
