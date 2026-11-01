"""Top-mode lower bounds (|b|/R_H)^(1/delta) for the required exterior radius (theory Section 12.6, Remark 3) at
delta = 2/7 and 1/4, B = 4, at the ten roots of Corollaries T_7 and T_8 (roots read from tq_cert_Q7.log, tq_cert_Q8.log),
with the check of R_H against the scalar top recursion (14.22.1) to order 1500. Values rounded down to 7 digits."""
from mpmath import mp, mpf, beta, floor, log10
mp.dps = 50
def RH(delta, B):
    d = 1/(1-delta) - 1
    eta = B - delta; a = 2/eta; b = 2*(B-1)/eta
    return 4*d*(a*beta(a, b))**(1/a), b
def rec(delta, B, N):
    d = 1/(1-delta) - 1; eta = B - delta
    h = [0, mpf(1)]
    for n in range(2, N+1):
        s = sum((2*B*(n-i)/(eta*i+2) - 1)*h[i]*h[n-i] for i in range(1, n))
        h.append(s/(4*d*(n-1)))
    return h
def down(x, sig=7):
    e = int(floor(log10(x))) - sig + 1
    return floor(x / mpf(10)**e) * mpf(10)**e
for Q in (7, 8):
    dl = mpf(2)/Q
    r, bb = RH(dl, 4)
    h = rec(dl, 4, 1500)
    print('Q=%d delta=2/%d R_H=%s  h_n R_H^n n^(1+1/b) at n=100,400,800,1500: %s' % (Q, Q, mp.nstr(r, 12),
          ', '.join(mp.nstr(h[n]*r**n*mpf(n)**(1+1/bb), 6) for n in (100, 400, 800, 1500))))
    roots = [l.split()[-1] for l in open('tq_cert_Q%d.log' % Q) if l.startswith('  [')][:10]
    print('  lower bounds (|b_i|/R_H)^(Q/2), rounded down:', ', '.join(mp.nstr(down((abs(mpf(b))/r)**(1/dl)), 7) for b in roots))
