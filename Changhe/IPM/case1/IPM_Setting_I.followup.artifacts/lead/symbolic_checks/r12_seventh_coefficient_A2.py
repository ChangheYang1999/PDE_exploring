# lead's own check of B_7 = -23/29059430400 at A = 2, L = 2 (verifier's seventh-order resonance result)
import sympy as sp
x = sp.symbols('x', positive=True)
A = 2; L = 2; u = x/L
w = -A*x*(1-u**2)/(1+u**2); g = x**2/(1+u**2); h = A+1-sp.diff(w, x)
d = lambda f: sp.diff(f, x)
a2 = (d(g)-d(d(w)))/2; b3 = -d(a2)/3
G3 = 4*(x/2)**2/(3*(1+(x/2)**2)**3)
F3 = -a2*d(g)-b3*g
print('G3 eq', sp.simplify(w*d(G3)+(3*h-1)*G3-F3))
a4 = (d(b3)+d(G3))/4; b5 = -d(a4)/5
G5 = x**2*(11*x**6+88*x**4-1872*x**2+9984)/(90*(x**2+4)**5)
F5 = -a2*d(G3)-3*b3*G3-a4*d(g)-b5*g
print('G5 eq', sp.simplify(w*d(G5)+(5*h-1)*G5-F5))
a6 = (d(b5)+d(G5))/6; b7 = -d(a6)/7
F7 = -a2*d(G5)-5*b3*G5-a4*d(G3)-3*b5*G3-a6*d(g)-b7*g
H7 = x**17*(1+x**2/4)**(-7)*(1-x**2/4)**(-3)
print('H7 eq', sp.simplify(d(H7)/H7-(1-7*h)/w))
integ = sp.factor(sp.cancel(-F7/(w*H7)))
print('integrand', integ)
num, den = sp.fraction(sp.together(integ))
lp = sp.expand(sp.cancel(integ*x**16))  # polynomial
P = sp.Poly(lp, x)
B7 = 0
for (k,), c in P.terms():
    e = k-16
    assert e != -1
    B7 += c*sp.Integer(2)**(e+1)/(e+1)
print('B7 =', sp.nsimplify(B7), ' natural 2^11 B7 =', sp.nsimplify(2**11*B7))
