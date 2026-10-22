# Check of the single-mode ansatz: Psi = x y h(q), q = x^2+y^2, local jet to fifth order.
import sympy as sp
x,y,b=sp.symbols('x y beta',real=True)
c,d,e,a0=sp.symbols('c d e a0')
q=x**2+y**2
h=c+d*q+e*q**2
Psi=x*y*h
U1=-sp.diff(Psi,y); U2=sp.diff(Psi,x)
Om=-(sp.diff(Psi,x,2)+sp.diff(Psi,y,2))
W1=b*x+U1; W2=b*y+U2
# Theta_x = W.grad Om + Om ; integrate in x from 0 (Theta(0,y)=0)
Tx=sp.expand(W1*sp.diff(Om,x)+W2*sp.diff(Om,y)+Om)
Th=sp.integrate(Tx,(x,0,x))
RT=sp.expand(W1*sp.diff(Th,x)+W2*sp.diff(Th,y)-(b-2)*Th)
P=sp.Poly(RT,x,y)
eqs={}
for (i,j),co in zip(P.monoms(),P.coeffs()):
    if i+j<=5: eqs[(i,j)]=sp.factor(co)
for k in sorted(eqs): print(k,eqs[k])
cs=2*b+2
E1=sp.expand(eqs[(4,1)].subs(c,cs)); E2=sp.expand(eqs[(2,3)].subs(c,cs))
es=sp.solve(E1,e)[0]
print('e =',sp.factor(es))
print('second eq after subst:',sp.factor(E2.subs(e,es)))
print('roots in beta of the polynomial factor:',sp.solve(sp.factor(E2.subs(e,es))/d**2,b))
