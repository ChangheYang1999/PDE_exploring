# Hand-check of checker result 151 manufactured DR state.
import sympy as sp
x,y=sp.symbols('x y',real=True); r2=x**2+y**2
psi=-x*y/(4*(1+r2)); rho=y*(r2+2)/(2*(1+r2)**2)
print('Poisson', sp.simplify(-sp.diff(psi,x,2)-sp.diff(psi,y,2)-sp.diff(rho,x)))
c=sp.diff(psi,x,y).subs({x:0,y:0}); a=sp.diff(rho,y).subs({x:0,y:0}); print('c',c,'a',a)
C=3; cw=sp.Rational(1); cw=c/(1-C); cx=C*cw; print('cw',cw,'cx',cx)
U1=-sp.diff(psi,y); U2=sp.diff(psi,x)
rt=cw*rho-((cx*x+U1)*sp.diff(rho,x)+(cx*y+U2)*sp.diff(rho,y))
s=sp.series(sp.series(rt,x,0,4).removeO(),y,0,4).removeO()
P=sp.Poly(sp.expand(s),x,y)
print('a_tau',P.coeff_monomial(y),'b_tau',P.coeff_monomial(x**2*y),'e_tau',P.coeff_monomial(y**3))
# at the checker's point
print('rho_tau(1/7,4/21)=',sp.nsimplify(sp.simplify(rt.subs({x:sp.Rational(1,7),y:sp.Rational(4,21)}))))
