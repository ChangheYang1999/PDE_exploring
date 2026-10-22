# Check: y-derivative traces of (T),(V) on the x-axis under A2 parity.
import sympy as sp
x,y,b=sp.symbols('x y beta')
k=b-2
# generic parity-compatible fields as truncated series in y with x-dependent coefficients
w,m,q1,q3=[sp.Function(n)(x) for n in ('w','m','q1','q3')]   # W1 = w + m y^2/2 ; W2 = q1 y + q3 y^3/6
f,f3=[sp.Function(n)(x) for n in ('f','f3')]                   # Theta = f y + f3 y^3/6
g=sp.Function('g')(x); Tx2=sp.Function('h')(x)
W1=w+m*y**2/2; W2=q1*y+q3*y**3/6
# impose div W = 2 beta up to y^2
Th=f*y+f3*y**3/6
divW=sp.expand(sp.diff(W1,x)+sp.diff(W2,y))
sol=sp.solve([sp.Eq(divW.coeff(y,0),2*b),sp.Eq(divW.coeff(y,2),0)],[q1,q3])
T=sp.expand((W1*sp.diff(Th,x)+W2*sp.diff(Th,y)-k*Th).subs(sol))
print('y^1:',sp.simplify(T.coeff(y,1)))
print('y^3 (times 6):',sp.simplify(6*T.coeff(y,3)))
Om=g*y
V=sp.expand((W1*sp.diff(Om,x)+W2*sp.diff(Om,y)+Om-sp.diff(Th,x)).subs(sol))
print('V y^1:',sp.simplify(V.coeff(y,1)))
