# Exact check that the sine and hyperbolic-sine separated families solve (P) on R^2 (Remark 4.1 and Section 4).
import sympy as sp
x,y,beta=sp.symbols('x y beta',real=True)
b=beta+2; d=2*beta+1
for name,w,Th in [('sin',-(b/2)*sp.sin(2*x),2*b*d*sp.sin(x)**2*y),('sinh',-(b/2)*sp.sinh(2*x),-2*b*d*sp.sinh(x)**2*y)]:
    Psi=(beta*x-w)*y
    U=(-sp.diff(Psi,y),sp.diff(Psi,x))
    Om=sp.diff(U[0],y)-sp.diff(U[1],x)
    W=(beta*x+U[0],beta*y+U[1])
    lap=-(sp.diff(Psi,x,2)+sp.diff(Psi,y,2))
    rV=W[0]*sp.diff(Om,x)+W[1]*sp.diff(Om,y)+Om-sp.diff(Th,x)
    rT=W[0]*sp.diff(Th,x)+W[1]*sp.diff(Th,y)-(beta-2)*Th
    c=sp.diff(Psi,x,y).subs({x:0,y:0})
    a0=sp.diff(Th,x,2,y).subs({x:0,y:0})/2
    print(name,'Omega+Lap Psi:',sp.simplify(lap-Om),' R_V:',sp.simplify(sp.expand(rV.rewrite(sp.exp))),
          ' R_T:',sp.simplify(sp.expand(rT.rewrite(sp.exp))),' c:',sp.factor(c),' a0:',sp.factor(a0))
