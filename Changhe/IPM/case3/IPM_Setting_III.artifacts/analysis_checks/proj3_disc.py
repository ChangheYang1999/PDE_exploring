# Independent Cartesian check of proj3 Steps 6-7 (disc theorem): build rho, psi as polynomials, compute R directly.
import sympy as s
x,y,c,a,H,th,r=s.symbols('x y c a H th r',real=True)
f1,g1,f2,g2=s.symbols('f1 g1 f2 g2')
D=c-1; M=a/4-D; z=x**2+y**2
# rho = y f(z) + (3x^2y-y^3) g(z)/z, f = a+f1 z+f2 z^2, g = g1 z + g2 z^2
rho=y*(a+f1*z+f2*z**2)+(3*x**2*y-y**3)*(g1+g2*z)
# moments: T = M - g1 z/2 - g2 z^2/4 ; J = a/4 + f1 z/6 + f2 z^2/8 ; K = g1 z/8 + g2 z^2/10 ; S = H z ; L = 0
T=M-g1*z/2-g2*z**2/4; J=a/4+f1*z/6+f2*z**2/8; K=g1*z/8+g2*z**2/10; S=H*z
u=(T-J)/2; v=(S-K)/2
voz=(H-g1/8-g2*z/10)/2
psi=u*2*x*y+voz*(4*x**3*y-4*x*y**3)
psi=s.expand(psi)
# check -Lap psi = rho_x up to order 4 in (x,y) (psi exact to order 6)
def trunc(e,n):
    p=s.Poly(s.expand(e),x,y); return sum(cf*x**i*y**j for (i,j),cf in p.terms() if i+j<=n)
lap=-(s.diff(psi,x,2)+s.diff(psi,y,2))-s.diff(rho,x)
print('poisson residual to order 4:',s.simplify(trunc(lap,4)))
U1=-s.diff(psi,y); U2=s.diff(psi,x)
R=s.expand((c*x+U1)*s.diff(rho,x)+(c*y+U2)*s.diff(rho,y)-rho)
def proj(e,n,k):
    h=trunc(e,n)-trunc(e,n-1)
    return s.simplify(s.integrate(s.expand_trig(h.subs({x:s.cos(th),y:s.sin(th)})*s.sin(k*th)),(th,0,2*s.pi))/s.pi)
print('psi_xy(0)=',s.diff(psi,x,y).subs({x:0,y:0}))
P13=proj(R,3,1); P33=proj(R,3,3)
sol1=s.solve([P13,P33],[f1,g1],dict=True)[0]
F=a**2-(4*c+20)*a+128*c-64
print('f1 check',s.simplify(sol1[f1]-(-24*H*a*(a-4*c+4)/F)),' g1 check',s.simplify(sol1[g1]-8*H*a*(a-4*c-4)/F))
P15=proj(R,5,1); P35=proj(R,5,3); P55=proj(R,5,5)
sol2=s.solve([P15.subs(sol1),P35.subs(sol1)],[f2,g2],dict=True)[0]
C5=s.factor(s.simplify(P55.subs(sol1).subs(sol2)))
G=a**2-(12*c+36)*a+32*c**2+384*c-160
P=(15*a**4+(200-560*c)*a**3+(6704*c**2-2320*c-2816)*a**2+(-29056*c**3-8512*c**2+63616*c-26048)*a
   +40960*c**4+61440*c**3-245760*c**2+184320*c-40960)
print('C5 check',s.simplify(C5-(-384*H**2*a*P/(5*F**2*G))))
print('C5 at c=3',s.factor(C5.subs(c,3)))
# linear matrices at orders 1,2 vs A(lambda) of (20)
lam=s.symbols('lam')
Am=s.Matrix([[(c+1)*lam/2-a/4, D*lam/2+2*D-a/4-a/lam],[D*lam/2-a/4+a/(lam+4), c*lam+D-a/2]])
Ic=a**2-4*((c+2)*lam-D)*a+4*(c**2+4*c-1)*lam**2-8*D*(c-3)*lam
print('16 det A - I_c:',s.simplify(16*Am.det()-Ic))
J1=s.Matrix([[s.diff(P13,f1),s.diff(P13,g1)],[s.diff(P33,f1),s.diff(P33,g1)]])
print('order-1 matrix / A(2):',[s.simplify(J1[i,j]/Am.subs(lam,2)[i,j]) for i in range(2) for j in range(2)])
J2=s.Matrix([[s.diff(P15,f2),s.diff(P15,g2)],[s.diff(P35,f2),s.diff(P35,g2)]])
print('order-2 matrix / A(4):',[s.simplify(J2[i,j]/Am.subs(lam,4)[i,j]) for i in range(2) for j in range(2)])
# b, e signs: b=f1+3g1, e=f1-g1
print('b',s.factor((sol1[f1]+3*sol1[g1])),' e',s.factor(sol1[f1]-sol1[g1]))
# intermediate formulas used in the appendix text
print('C5 intermediate:',s.simplify(P55-(-2*H*f1+(D-a/20)*g2-s.Rational(3,4)*g1**2)))
Q2=s.Matrix([6*H*g1-s.Rational(5,12)*f1**2-f1*g1/2+s.Rational(3,2)*g1**2, 4*H*f1+f1**2/12-f1*g1/4])
lhs=Am.subs(lam,4)*s.Matrix([f2,g2])+Q2
print('order-2 system:',s.simplify(lhs[0]-P15),s.simplify(lhs[1]-P35))
print('order-1 system:',s.simplify(Am.subs(lam,2)*s.Matrix([f1,g1])+s.Matrix([0,2*a*H])-s.Matrix([P13,P33])))
# H=0: cubic part vanishes unless F=0
print('det A(2)*16 - F:',s.simplify(16*Am.subs(lam,2).det()-F))
# exceptional set check for c=2,3: I(n+sqrt2, 2j) != 0
for cc in (2,3):
    j,nn=s.symbols('j nn',integer=True)
    I2=(Ic.subs({c:cc,lam:2*j})).subs(a,nn+s.sqrt(2))
    print(cc,s.expand(I2))
