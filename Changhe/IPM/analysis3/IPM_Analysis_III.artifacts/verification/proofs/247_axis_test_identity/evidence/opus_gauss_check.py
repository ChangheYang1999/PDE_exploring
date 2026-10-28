import sympy as sp
x,y=sp.symbols('x y',real=True)
g=-(y**3/6)*sp.exp(-y**2)
gp=lambda n: sp.diff(g,y,n)
a=2*g-gp(2); bb=gp(4)-12*gp(2)+12*g
V=sp.exp(-x**2)*(g+x**2*a/2+x**4*bb/24)
Vxx0=sp.simplify(sp.diff(V,x,2).subs(x,0))
print("V_xx(0,y) + g'' =",sp.simplify(Vxx0+gp(2)))
print("V_xx(0,y) - (2g-g'') =",sp.simplify(Vxx0-(2*g-gp(2))))
print("c_d = d/dy V_xx(0,0) =",sp.diff(Vxx0,y).subs(y,0))
print("check psi_xy(0)=V_xxy(0):",sp.diff(V,x,2,y,1).subs({x:0,y:0}))
d=-(sp.diff(V,x,2)+sp.diff(V,y,2))
P=sp.simplify(d*sp.exp(x**2+y**2))
P=sp.expand(P)
print("d*exp(r^2) polynomial:",sp.Poly(P,x,y).is_polynomial if hasattr(sp.Poly(P,x,y),'is_polynomial') else True)
q,r=sp.div(sp.Poly(P,x,y),sp.Poly(x**4*y,x,y))
print("remainder of division by x^4 y:",r)
# axis series of V
print("V series in x:",sp.simplify(sp.series(V,x,0,5).removeO().coeff(x,2)+gp(2)/2))
# leading y^3 change in axis(R) from replacing b=-g'' by 2g-g'': dw=2g, f~y
f=y
dw=2*g
dax=sp.series(dw*sp.diff(f,y)-2*sp.diff(dw,y)*f,y,0,5)
print("change in axis(R) if (9) used, f=y model:",dax)
