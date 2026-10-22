# Independent check of the beta = 2 origin resonance coefficient for h = Theta_yyy(x,0).
import sympy as sp
x, a, w3, w5, w7, C = sp.symbols('x a w3 w5 w7 C')
N = 9
w = -4*x + w3*x**3 + w5*x**5 + w7*x**7
fc = sp.symbols('F4 F6 F8'); gc = sp.symbols('G1 G3 G5 G7'); hc = sp.symbols('H2 H4 H6')
f = a*x**2 + fc[0]*x**4 + fc[1]*x**6 + fc[2]*x**8
g = sum(gc[i]*x**(2*i+1) for i in range(4))
def trunc(e, n=N):
    e = sp.expand(e); return sum(e.coeff(x, k)*x**k for k in range(n))
# w f' = (w' - 4) f  (beta = 2, k = 4)
ef = trunc(w*sp.diff(f, x) - (sp.diff(w, x) - 4)*f, 10)
sf = sp.solve([ef.coeff(x, k) for k in (4, 6, 8)], fc, dict=True)[0]
f = f.subs(sf)
# w g' + (5 - w') g = f'
eg = trunc(w*sp.diff(g, x) + (5 - sp.diff(w, x))*g - sp.diff(f, x), 9)
sg = sp.solve([eg.coeff(x, k) for k in (1, 3, 5, 7)], gc, dict=True)[0]
g = g.subs(sg)
m = sp.expand(g - sp.diff(w, x, 2))
R = trunc(-3*m*sp.diff(f, x) + sp.diff(m, x)*f, 8)
# h = H2 x^2 + H4 x^4 + H6 x^6 + C x^6 log x; operator w h' + (12 - 3 w') h
L = sp.symbols('L')  # stands for log x
h = hc[0]*x**2 + hc[1]*x**4 + hc[2]*x**6 + C*x**6*L
dh = sp.diff(h, x) + C*x**5   # d/dx of x^6 log x = 6 x^5 log x + x^5
res = sp.expand(w*dh + (12 - 3*sp.diff(w, x))*h - R)
eqs = [res.coeff(L, 0).coeff(x, k) for k in (2, 4, 6)]
sol = sp.solve(eqs, [hc[0], hc[1], C], dict=True)[0]
D = sp.Rational(3, 3520)*a*(-93*a*w3**2 - 360*a*w5 + 2640*w3**3 + 23760*w3*w5 + 49280*w7)
print('C =', sp.factor(sol[C]))
print('C + D/4 =', sp.simplify(sol[C] + D/4))
print('x^6 log coefficient of residual (should vanish identically):', sp.simplify(res.coeff(L, 1).coeff(x, 6)))
print('trig family D:', sp.factor(D.subs({w3: sp.Rational(8, 3), w5: -sp.Rational(8, 15), w7: sp.Rational(16, 315)})))
