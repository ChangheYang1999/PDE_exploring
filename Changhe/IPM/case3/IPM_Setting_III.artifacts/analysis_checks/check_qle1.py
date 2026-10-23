# Independent checks of the main claims of the qle1 external answer (angular-variation exclusion, Gaussian family).
import sympy as sp
th,r,x,y,cl,a,c,t,B=sp.symbols('theta r x y c_l a c t B',positive=True)
D=cl-1; A=2*cl-1
ok=[]
# (1) boundary constant: (4/pi) int_0^{pi/2} cos^2 sin^2 = 1/4
ok.append(sp.simplify(4/sp.pi*sp.integrate(sp.cos(th)**2*sp.sin(th)**2,(th,0,sp.pi/2))-sp.Rational(1,4))==0)
# (2) w' = -k, k = sin^2(4 sin^2 - 3)
w=sp.cos(th)*sp.sin(th)**3; k=sp.sin(th)**2*(4*sp.sin(th)**2-3)
ok.append(sp.simplify(sp.diff(w,th)+k)==0)
# (3) threshold: (pi/4)(1/4 - D/(2A)) = pi/(16 A)
ok.append(sp.simplify(sp.pi/4*(sp.Rational(1,4)-D/(2*A))-sp.pi/(16*A))==0)
# (4) degree version: (pi/4)(1/4 - D/((n-1)A)) = pi((n-3)A+2)/(16(n-1)A)
n=sp.symbols('n',positive=True)
ok.append(sp.simplify(sp.pi/4*(sp.Rational(1,4)-D/((n-1)*A))-sp.pi*((n-3)*A+2)/(16*(n-1)*A))==0)
# (5) cubic jet at a = 2A: recursion 6*e0*c0 + 2*(e1 - a)*c1 = 0 with e0 = 2, e1 = 2A gives c0 = 0
c0,c1=sp.symbols('c0 c1')
ok.append(sp.solve(sp.Eq(6*2*c0+2*(2*A-2*A)*c1,0),c0)==[0])
# q = 1 - c x^2 => q_theta = 2 c r^2 sin cos
q=1-c*(r*sp.cos(th))**2
ok.append(sp.simplify(sp.diff(q,th)-2*c*r**2*sp.sin(th)*sp.cos(th))==0)
# (6) Gaussian family: c/a = -(4/pi) int cos^2 sin^2/(cos^2 + B^2 sin^2) = -1/(1+B)^2, check numerically at several B
for Bv in [1.0,2.0,3.7,10.0]:
    val=-4/sp.pi*sp.Integral(sp.cos(th)**2*sp.sin(th)**2/(sp.cos(th)**2+Bv**2*sp.sin(th)**2),(th,0,sp.pi/2))
    ok.append(abs(float(val.evalf(30))+1/(1+Bv)**2)<1e-15)
# canonical-inverse formula c/a = (4/pi) int_{x,y>0} x y^2 r^-4 q_x dX for q = exp(-x^2 - B^2 y^2), radial integral first
qx=-2*x*sp.exp(-x**2-B**2*y**2)
integrand=(x*y**2/(x**2+y**2)**2*qx).subs({x:r*sp.cos(th),y:r*sp.sin(th)})*r
rad=sp.integrate(sp.simplify(integrand),(r,0,sp.oo),conds='none')
ok.append(all(abs(complex((rad+sp.cos(th)**2*sp.sin(th)**2/(sp.cos(th)**2+B**2*sp.sin(th)**2)).subs({th:tv,B:bv}).evalf(30)))<1e-14 for tv in [0.3,0.9,1.4] for bv in [1,2.5,7]))
# (7) gradient bound of the Gaussian family: |grad rho|^2/a^2 = e^{-2x^2-2B^2y^2}[4x^2y^2 + (1-2B^2y^2)^2]
rho=y*sp.exp(-x**2-B**2*y**2)
g2=sp.simplify(sp.diff(rho,x)**2+sp.diff(rho,y)**2)
ok.append(sp.simplify(g2-sp.exp(-2*x**2-2*B**2*y**2)*(4*x**2*y**2+(1-2*B**2*y**2)**2))==0)
# critical point (0, 1/(sqrt2 B)): grad rho = 0, rho > 0
pt={x:0,y:1/(sp.sqrt(2)*B)}
ok.append(sp.simplify(sp.diff(rho,y).subs(pt))==0 and sp.simplify(sp.diff(rho,x).subs(pt))==0 and sp.simplify(rho.subs(pt))!=0)
# (8) cubic counterjet at c_l = 2, a = 13: H3 = x^2 y + 7/6 y^3 solves the j = 0 recursion, q_theta < 0
Av=3; av=13
ok.append(6*2*sp.Rational(7,6)+2*(2*Av-av)*1==0)
q3=1-(x**2+sp.Rational(7,6)*y**2)
q3p=q3.subs({x:r*sp.cos(th),y:r*sp.sin(th)})
ok.append(sp.simplify(sp.diff(q3p,th)+sp.Rational(1,3)*r**2*sp.sin(th)*sp.cos(th))==0)
# (9) oscillation constant: positive mass of k on (pi/3, pi/2) = 3 sqrt3/16, and (1/(4A))/((4/pi)(3sqrt3/16)) = pi/(3 sqrt3 A)
ok.append(sp.simplify(sp.integrate(k,(th,sp.pi/3,sp.pi/2))-3*sp.sqrt(3)/16)==0)
ok.append(sp.simplify((1/(4*A))/(4/sp.pi*3*sp.sqrt(3)/16)-sp.pi/(3*sp.sqrt(3)*A))==0)
# (10) (4.10): int_0^{pi/2} cos^2 sin^4 = pi/32
ok.append(sp.simplify(sp.integrate(sp.cos(th)**2*sp.sin(th)**4,(th,0,sp.pi/2))-sp.pi/32)==0)
print(len(ok),'checks;', 'ALL PASS' if all(ok) else ('FAIL at '+str([i for i,v in enumerate(ok) if not v])))
