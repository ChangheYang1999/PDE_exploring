# complex zeros of the numerator of om (1 + u^2) and of w0 nearest to [0, 1], per reference
import sys, json
import sympy as sp, mpmath as mp
mp.mp.dps = 30
u = sp.Symbol('u')
for K in [int(k) for k in sys.argv[1].split(',')]:
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    As = sp.Rational(repr(d['A']))
    qv = sum(sp.Rational(s)*u**(2*k) for k, s in enumerate(d['q_monomial']))
    num = sp.Poly(sp.expand(As*(1 + u) - u**2*(1 - u)*(1 + u)**2*(1 + u**2)*qv), u)
    rts = sp.Poly(num, u).nroots(n=25, maxsteps=200)
    def dist(z):
        z = complex(z)
        x = min(max(z.real, 0), 1)
        return abs(z - x)
    rs = sorted(rts, key=dist)[:4]
    print('K=%d: deg %d; nearest zeros of om (1+u^2) to [0,1]: %s' % (K, num.degree(), ', '.join('%s (dist %.4f)' % (mp.nstr(complex(z), 6), dist(z)) for z in rs)), flush=True)
