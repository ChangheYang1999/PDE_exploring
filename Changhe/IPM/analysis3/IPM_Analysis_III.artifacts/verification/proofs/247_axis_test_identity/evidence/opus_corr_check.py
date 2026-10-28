import sympy as sp
x,y=sp.symbols('x y',real=True)
g=-(y**3/6)*sp.exp(-y**2)
g2=sp.diff(g,y,2)
a=2*g-g2; bb=sp.diff(g,y,4)-12*g2+12*g
V=sp.exp(-x**2)*(g+x**2*a/2+x**4*bb/24)
print("x^2 coeff of V + g''/2:",sp.simplify(sp.series(V,x,0,4).removeO().coeff(x,2)+g2/2))
print("(2g-g'')/2-g + g''/2:",sp.simplify(a/2-g+g2/2))
tr=(y-sp.Rational(7,3)*y**3+sp.Rational(2,3)*y**5)*sp.exp(-y**2)
print("-g'' - stated trace:",sp.simplify(-g2-tr))
print("V_xx(0,y) - stated trace:",sp.simplify(sp.diff(V,x,2).subs(x,0)-tr))
print("derivs at 0 of -g'' and 2g-g'':",sp.diff(-g2,y).subs(y,0),sp.diff(2*g-g2,y).subs(y,0))
print("difference:",sp.simplify((2*g-g2)-(-g2)))
f3=sp.Symbol('f3'); f=y+f3*y**3
dw=2*g
print("2g f'-4g'f series:",sp.series(dw*sp.diff(f,y)-2*sp.diff(dw,y)*f,y,0,6))
