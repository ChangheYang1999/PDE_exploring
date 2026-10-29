# Lead cross-check of the verifier's topic 90 (critical pressure moments of a piecewise field).
# Independent sympy rederivation of: (1) surface Green contributions for F delta, J_R delta', (2J_R+D) delta/a;
# (2) the D_1 integration by parts; (3) the l=0 and l=1 Green identities in terms of I0, I1;
# (4) the compact-support reference U=(b+dz)(-y,x,0) in the ball: f, [N].n, C0, C1 and the volume moments.
import sympy as sp
R,s,a,mu,b,d,l=sp.symbols('R s a mu b d l',positive=True)
out=[]
# (1) for R>a the interior Green term is R^{-l-1}/(2l+1) * int s^{l+2} h_l ds
L=sp.Symbol('L',integer=True,nonnegative=True)
Fl,JR,Dl=sp.symbols('F_l J_R D_l')
# int s^{L+2} [F delta(s-a) + J_R delta'(s-a) + (2J_R+D) delta(s-a)/a] ds
term=a**(L+2)*Fl - sp.diff(s**(L+2),s).subs(s,a)*JR + a**(L+2)*(2*JR+Dl)/a
claim=a**(L+1)*(a*Fl-L*JR+Dl)
out.append(('surface Green contribution',sp.simplify(sp.expand(term-claim))))
# (2) D_1 = (3/2) int mu div_S(J_theta e_theta) dmu; on the unit sphere div_S(J_theta e_theta)=(1/sin)d_theta(sin J_theta)
th=sp.symbols('theta',positive=True)
Jt=sp.Function('Jt'); Jr=sp.Function('Jr')
# test with explicit smooth tangential components vanishing at the poles like sin
for Jth,Jrr in [(sp.sin(th)*(1+sp.cos(th)**3),1+sp.cos(th)**2),(sp.sin(th)*sp.cos(th)**2,sp.cos(th))]:
    divS=sp.diff(sp.sin(th)*Jth,th)/sp.sin(th)
    lhs=sp.Rational(3,2)*sp.integrate(sp.cos(th)*divS*sp.sin(th),(th,0,sp.pi))
    Jz=sp.cos(th)*Jrr-sp.sin(th)*Jth
    rhs=-sp.Rational(3,2)*sp.integrate((Jz-sp.cos(th)*Jrr)*sp.sin(th),(th,0,sp.pi))
    out.append(('D_1 identity example',sp.simplify(lhs-rhs)))
    out.append(('D_0 = 0 example',sp.simplify(sp.integrate(divS*sp.sin(th),(th,0,sp.pi)))))
# (3) Green identities with a generic smooth source h(s): l=0 derivative and l=1 integration by parts
h=sp.Function('h')
I0=sp.Integral(s**2*h(s),(s,0,R)); P0=I0/R+sp.Integral(s*h(s),(s,R,sp.oo))
out.append(('P0 prime = -I0/R^2',sp.simplify(sp.diff(P0,R).doit()+I0.doit()/R**2)))
# l=1: P1 = (R^-2 I1 + R int_R^inf h)/3 ; claim P1 = R int_R^inf I1 s^-4 ds, check derivative of P1/R matches
I1=lambda X: sp.Integral(s**3*h(s),(s,0,X))
P1=(I1(R)/R**2+R*sp.Integral(h(s),(s,R,sp.oo)))/3
# d/dR (P1/R) should equal -I1(R) R^-4
out.append(('l=1 Green identity',sp.simplify(sp.diff(P1/R,R).doit()+I1(R).doit()/R**4)))
# asymptotics: I1 = 3Q1 + c/s^2 gives R int_R^inf I1 s^-4 = Q1/R^2 + O(R^-4)
Q1,c=sp.symbols('Q1 c')
val=R*sp.integrate((3*Q1+c/s**2)*s**-4,(s,R,sp.oo))
out.append(('l=1 asymptotic',sp.simplify(val-Q1/R**2-c/(5*R**4))))
# (4) reference field
x,y,z=sp.symbols('x y z',real=True)
w=b+d*z
U=sp.Matrix([-w*y,w*x,0]); X=sp.Matrix([x,y,z])
DU=U.jacobian(X)
out.append(('div U',sp.simplify(DU.trace())))
f=sp.simplify((DU*DU).trace())
out.append(('f + 2 w^2',sp.simplify(f+2*w**2)))
N=DU*U
rr=sp.sqrt(x**2+y**2+z**2)
Nn=sp.simplify((N.T*X)[0]/rr)
# spherical substitution at R=a
ph=sp.symbols('ph',real=True)
sub={x:a*sp.sqrt(1-mu**2)*sp.cos(ph),y:a*sp.sqrt(1-mu**2)*sp.sin(ph),z:a*mu}
Fa=sp.simplify(-(Nn.subs(sub)))  # outer (zero) minus inner trace
out.append(('[N].n formula',sp.simplify(Fa-a*(1-mu**2)*(b+d*a*mu)**2)))
F0=sp.Rational(1,2)*sp.integrate(Fa,(mu,-1,1)); F1=sp.Rational(3,2)*sp.integrate(mu*Fa,(mu,-1,1))
C0=a**2*F0; C1=sp.Rational(1,3)*a**2*(a*F1)   # J = 0
out.append(('C0',sp.simplify(C0-(2*b**2*a**3/3+2*d**2*a**5/15))))
out.append(('C1',sp.simplify(C1-4*b*d*a**5/15)))
fs=f.subs({x:s*sp.sqrt(1-mu**2)*sp.cos(ph),y:s*sp.sqrt(1-mu**2)*sp.sin(ph),z:s*mu})
f0=sp.Rational(1,2)*sp.integrate(fs,(mu,-1,1)); f1=sp.Rational(3,2)*sp.integrate(mu*fs,(mu,-1,1))
out.append(('volume l=0 moment = -C0',sp.simplify(sp.integrate(s**2*f0,(s,0,a))+C0)))
out.append(('volume l=1 moment /3 = -C1',sp.simplify(sp.integrate(s**3*f1,(s,0,a))/3+C1)))
for k,v in out: print(k,':',v)
print('ALL ZERO' if all(sp.simplify(v)==0 for _,v in out) else 'NONZERO PRESENT')
