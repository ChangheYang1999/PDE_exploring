# Own check of fred28 (3.4) / (1.6): for arbitrary a, b, f (a != 0), with D = a d_s + b d_y,
#   K_n = f^[n] - (f_y/a) a^[n-1],  E = a f_s + b f_y - f,  V = a_s + b_y,
#   (D + n b_y - 1) K_n - F_n = E^[n] - (a^[n-1]/a) E_y - f_y V^[n-1],
# F_n as in (1.12). Generic sympy functions; the difference times a^2 is expanded and must vanish identically.
# Also: (1.5) equals (1.12) at n = 4, and the transport/divergence reductions (1.7), (1.8).
import sympy as sp
s, y = sp.symbols('s y')
a, b, f = [sp.Function(n)(s, y) for n in 'abf']
def dy(e, k=1): return sp.diff(e, y, k) if k else e
D = lambda e: a*sp.diff(e, s) + b*sp.diff(e, y)
E = a*sp.diff(f, s) + b*sp.diff(f, y) - f
V = sp.diff(a, s) + sp.diff(b, y)
u = sp.diff(f, y)/a
def Fn(n):
    t1 = (sp.diff(a, y)*dy(a, n-1)/a - dy(a, n))*(sp.diff(f, s) + b*sp.diff(f, y)/a)
    t2 = -sum(sp.binomial(n, k)*dy(a, k)*sp.diff(dy(f, n-k), s) for k in range(1, n))
    t3 = -sum(sp.binomial(n, k)*dy(b, k)*dy(f, n+1-k) for k in range(2, n))
    t4 = (sp.diff(a, s) - (n-1)*sp.diff(b, y))*u*dy(a, n-1)
    return t1 + t2 + t3 + t4
res = {}
for n in (2, 4, 6, 8):
    K = dy(f, n) - u*dy(a, n-1)
    lhs = D(K) + (n*sp.diff(b, y) - 1)*K - Fn(n)
    rhs = dy(E, n) - dy(a, n-1)/a*sp.diff(E, y) - sp.diff(f, y)*dy(V, n-1)
    d = sp.expand(sp.simplify((lhs - rhs)*a**2))
    res[n] = d
    print('n = %d: (lhs - rhs) a^2 expands to' % n, d, flush=True)
# (1.5) against (1.12) at n = 4
fs = lambda *ks: sp.diff(f, *ks)
F4_15 = ((sp.diff(a, y)*dy(a, 3)/a - dy(a, 4))*(sp.diff(f, s) + b*sp.diff(f, y)/a)
         - 4*sp.diff(a, y)*sp.diff(dy(f, 3), s) - 6*dy(a, 2)*sp.diff(dy(f, 2), s) - 4*dy(a, 3)*sp.diff(dy(f, 1), s)
         - 6*dy(b, 2)*dy(f, 3) - 4*dy(b, 3)*dy(f, 2)
         + (sp.diff(a, s) - 3*sp.diff(b, y))*sp.diff(f, y)/a*dy(a, 3))
print('(1.5) - (1.12)|_{n=4} =', sp.simplify(F4_15 - Fn(4)))
# (1.8): D u = -A u - (a_y/a)(f_s + b f_y/a) when D f = f and a_s + b_y = A + 1: residual in terms of E, V
A = sp.Symbol('A')
Du = D(u)
pred = -(V - 1)*u - sp.diff(a, y)/a*(sp.diff(f, s) + b*sp.diff(f, y)/a)   # A u = (V - 1) u when V = A + 1
r18 = sp.simplify((Du - pred)*a**2 - a*sp.diff(E, y))
print('(1.8a): (D u - pred) a^2 - a E_y =', r18)
r18b = sp.simplify(D(dy(a, 3)) - (-a*dy(b, 4) + b*dy(a, 4)) - a*dy(V, 3))
print('(1.8b): D a_yyy - (-a b_yyyy + b a_yyyy) - a V_yyy =', r18b)
