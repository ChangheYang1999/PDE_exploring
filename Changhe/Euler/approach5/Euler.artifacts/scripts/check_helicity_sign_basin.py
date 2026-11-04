# Exact symbolic checks of the two examples in an external referee answer (items (4)-(6)).
# (a) local saddle model: div U = 0, Omega = 2b e_z, h = 2b(z+w), Lamb form, full profile equation, periodic orbit.
# (b) tail field V: div V = 0, curl V and V.curl V formulas, tail equation (1-c)V + (Ay.grad)V + omega J V = 0.
import sympy as sp
x,y,z=sp.symbols('x y z',real=True)
c,om,b,R,w,lam,mu=sp.symbols('c omega b R w lambda mu',real=True)
X=sp.Matrix([x,y,z]); r2=x**2+y**2; r=sp.sqrt(r2)
a=1-2*c; kap=1+c
J=sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]]); A=c*sp.eye(3)-om*J
def grad(f): return sp.Matrix([sp.diff(f,v) for v in (x,y,z)])
def div(F): return sum(sp.diff(F[i],v) for i,v in enumerate((x,y,z)))
def curl(F): return sp.Matrix([sp.diff(F[2],y)-sp.diff(F[1],z),sp.diff(F[0],z)-sp.diff(F[2],x),sp.diff(F[1],x)-sp.diff(F[0],y)])
def jac(F): return F.jacobian(X)
ok=True
# exact evaluation at rational points with rational r and rho, for several rational parameter sets
PTS=[(3,4,12),(-4,3,-12),(5,-12,84),(-12,-5,84)]
PARS=[{c:sp.Rational(9,20),om:sp.Rational(7,3),b:sp.Rational(5,7),R:2,w:sp.Rational(-3,4),lam:sp.Rational(2,3),mu:sp.Rational(-5,4)},
      {c:sp.Rational(41,100),om:sp.Rational(-11,5),b:sp.Rational(-3,2),R:sp.Rational(1,3),w:sp.Rational(5,2),lam:sp.Rational(-7,4),mu:sp.Rational(3,5)}]
def check(name,expr,pts=True):
    global ok
    E=expr if isinstance(expr,sp.MatrixBase) else sp.Matrix([expr])
    good=True
    for pr in PARS:
        for (px,py,pz) in (PTS if pts else [(None,None,None)]):
            sub=dict(pr)
            if px is not None: sub.update({x:px,y:py,z:pz})
            for t in E:
                v=sp.nsimplify(sp.simplify(t.subs(sub)))
                if v!=0: good=False
    print(name,'PASS' if good else 'FAIL'); ok=ok and good
# (a)
er=sp.Matrix([x/r,y/r,0]); et=sp.Matrix([-y/r,x/r,0]); ez=sp.Matrix([0,0,1])
Ur=-r/2+a*R**2/(2*r); Ut=b*(r-R**2/r); Uz=z+w
U=Ur*er+Ut*et+Uz*ez
B=A*X+U; Om=curl(U)
check('a.divU',div(U))
check('a.Omega',Om-2*b*ez)
check('a.helicity',U.dot(Om)-2*b*(z+w))
H=(b*(b-om)+a/4)*r2-(2*b**2+a**2/2)*R**2*sp.log(r)-a/2*(z+w)**2
check('a.Lamb',a*U+grad(H)-B.cross(Om))
P=H-U.dot(U)/2-(A*X).dot(U)
check('a.profile',(1-c)*U+jac(U)*B+om*J*U+grad(P))
# periodic orbit r = R, z = -w/kappa: B there is tangential with angular speed -omega
pt={x:R,y:0,z:-w/kap}
check('a.orbit',(B.subs(pt)-sp.Matrix([0,-om*R,0])),pts=False)
# (b) tail field in spherical form, converted to Cartesian
rho=sp.sqrt(x**2+y**2+z**2); k=(1-c)/c
ct=z/rho; st=r/rho
eR=X/rho; eT=sp.Matrix([x*z/(r*rho),y*z/(r*rho),-r/rho]); eP=et
V=rho**(-k)*(2*lam/(2-k)*ct*eR-lam*st*eT+mu*st*ct*eP)
W=curl(V)
check('b.divV',div(V))
Wexp=rho**(-k-1)*(mu*(3*ct**2-1)*eR+(k-1)*mu*st*ct*eT+lam*k*(3-k)/(2-k)*st*eP)
check('b.curl',W-Wexp)
check('b.helicity',V.dot(W)-4*lam*mu/(2-k)*rho**(-2*k-1)*ct**3)
check('b.tail',(1-c)*V+jac(V)*(A*X)+om*J*V)
kt=(A*X).dot(V)
check('b.tailLamb',a*V+W.cross(A*X)+grad(kt))
print('ALL PASS' if ok else 'SOME FAIL')
