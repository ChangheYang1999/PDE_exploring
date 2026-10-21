# Supplement to identity34.py: (3.4) also for odd n = 3, 5, 7 (the hand proof (3.5)-(3.7) is for every n >= 2),
# and the two auxiliary identities (3.6), (3.7) of fred28 for generic a, b, f.
import sympy as sp
s, y = sp.symbols('s y')
a, b, f = [sp.Function(n)(s, y) for n in 'abf']
def dy(e, k=1): return sp.diff(e, y, k) if k else e
D = lambda e: a*sp.diff(e, s) + b*sp.diff(e, y)
E = a*sp.diff(f, s) + b*sp.diff(f, y) - f
V = sp.diff(a, s) + sp.diff(b, y)
u = sp.diff(f, y)/a
def Fn(n):
    t1 = (sp.diff(a, y)*dy(a, n-1)/a - dy(a, n))*(sp.diff(f, s) + b*u)
    t2 = -sum(sp.binomial(n, k)*dy(a, k)*sp.diff(dy(f, n-k), s) for k in range(1, n))
    t3 = -sum(sp.binomial(n, k)*dy(b, k)*dy(f, n+1-k) for k in range(2, n))
    t4 = (sp.diff(a, s) - (n-1)*sp.diff(b, y))*u*dy(a, n-1)
    return t1 + t2 + t3 + t4
r36 = sp.simplify((D(u) - ((1 - V)*u - sp.diff(a, y)/a*(sp.diff(f, s) + b*u) + sp.diff(E, y)/a))*a**2)
print('(3.6) residual:', r36, flush=True)
for n in (3, 5, 7):
    r37 = sp.simplify(D(dy(a, n-1)) - (a*(dy(V, n-1) - dy(b, n)) + b*dy(a, n)))
    K = dy(f, n) - u*dy(a, n-1)
    lhs = D(K) + (n*sp.diff(b, y) - 1)*K - Fn(n)
    rhs = dy(E, n) - dy(a, n-1)/a*sp.diff(E, y) - sp.diff(f, y)*dy(V, n-1)
    d = sp.expand(sp.simplify((lhs - rhs)*a**2))
    print('n = %d: (3.7) residual %s; (3.4) residual times a^2: %s' % (n, r37, d), flush=True)
