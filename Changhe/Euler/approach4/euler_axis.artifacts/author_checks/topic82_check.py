# Lead cross-review of the verifier's topic82 (Gaussian axis tail) and topic77 (gauge comparison) formulas, symbolic.
import sympy as sp
z,A,B,H,beta,a,y,mu,R,k=sp.symbols('z A B H beta a y mu R k',positive=True)
c=1/beta
out={}
# axis first integral: J = w e - 2 h (h-1), J' = (h'/h) J given w h' = (2phi_z-1) h, w e' + (1+c) e = (h^2)', w' = c + 2 phi_z
h,e,w,pz=sp.symbols('h e w pz')
hp=(2*pz-1)*h/w; ep=(2*h*hp-(1+c)*e)/w; wp=c+2*pz
Jp=wp*e+w*ep-2*hp*(2*h-1)
out['J_identity']=sp.simplify(Jp-(hp/h)*(w*e-2*h*(h-1)))==0
# far tail with y = z^(-beta): phi/z = A y + B y^2, phi_z = A(1-beta) y + B(1-2beta) y^2
phiz_over=A*y+B*y**2; phiz=A*(1-beta)*y+B*(1-2*beta)*y**2
gpb=sp.series(2*(phiz+beta*phiz_over)/(c+2*phiz_over),y,0,3).removeO()
tail=sp.expand(sp.integrate(sp.expand(gpb).subs(y,sp.exp(-beta*sp.Symbol('x'))),(sp.Symbol('x'),sp.Symbol('X'),sp.oo),conds='none'))
Xs=sp.Symbol('X'); yy=sp.exp(-beta*Xs)
out['eq4']=sp.simplify(tail-(2*A*yy-(2*beta*A**2+(beta-1)*B)*yy**2))==0
# transported coefficients: h = H z^-beta (1 - 2A z^-beta), e = 2h(h-1)/w, w = c z (1 + 2 beta A y + ...)
hh=H*y*(1-2*A*y); winv_times_z=sp.series(1/(c+2*A*y+2*B*y**2),y,0,3).removeO()
ez=sp.expand(sp.series(2*hh*(hh-1)*winv_times_z,y,0,3).removeO())   # this is z*e
out['T1']=sp.simplify(ez.coeff(y,1)-(-2*H/c))==0
out['T2']=sp.simplify(ez.coeff(y,2)-(2*H/c)*(H+2*A+2*A/c))==0
# 5D Laplacian of R^k F(mu)
F=sp.Function('F'); r,zz=sp.symbols('r zz',positive=True)
Rr=sp.sqrt(r**2+zz**2); f=Rr**k*F(zz/Rr)
lap=sp.diff(f,r,2)+3/r*sp.diff(f,r)+sp.diff(f,zz,2)
target=Rr**(k-2)*(k*(k+3)*F(mu)+(1-mu**2)*sp.diff(F(mu),mu,2)-4*mu*sp.diff(F(mu),mu))
tst=[(sp.Rational(3,5),sp.Rational(2,7)),(sp.Rational(1,3),sp.Rational(5,4))]
okl=True
for rv,zv in tst:
    for Fx in (lambda m: m**3-2*m, lambda m: sp.exp(m)*m):
        ff=Rr**k*Fx(zz/Rr); L=sp.diff(ff,r,2)+3/r*sp.diff(ff,r)+sp.diff(ff,zz,2)
        m_=sp.Symbol('m'); Fm=Fx(m_)
        T=Rr**(k-2)*(k*(k+3)*Fm+(1-m_**2)*sp.diff(Fm,m_,2)-4*m_*sp.diff(Fm,m_))
        for kv in (sp.Rational(-1,3),sp.Rational(7,5)):
            v1=(L.subs(k,kv).subs({r:rv,zz:zv})).evalf(30); v2=(T.subs(m_,zv/sp.sqrt(rv**2+zv**2)).subs(k,kv).subs({r:rv,zz:zv})).evalf(30)
            okl=okl and abs(v1-v2)<1e-25
out['lap5']=okl
# pole derivative of the seed profile mu d^-n P(v,w), d = a+(1-a)mu^2, exponent n (p for series 1, beta for series 2)
n=sp.Symbol('n'); P=sp.Function('P')
d=a+(1-a)*mu**2; v=a*(1-mu**2)/d; ww=mu**2/d
Pv,Pw,P0=sp.symbols('Pv Pw P0')
Fm=mu*d**(-n)*sp.Symbol('Pm')  # value part
dF=sp.diff(mu*d**(-n),mu).subs(mu,1)*P0+(mu*d**(-n)).subs(mu,1)*(Pv*sp.diff(v,mu).subs(mu,1)+Pw*sp.diff(ww,mu).subs(mu,1))
out['A1prime']=sp.simplify(dF.subs(n,beta/2)-((1+beta*(a-1))*P0-2*a*Pv+2*a*Pw))==0
F2p=sp.simplify(dF.subs(n,beta))
T2=sp.expand(-(1-2*beta)*(4-2*beta)*P0+4*F2p)
out['T2_elliptic']=sp.simplify(T2-(8*a*(beta*P0-Pv+Pw)-2*beta*(2*beta-1)*P0))==0
# source terms z(b_s s + b_z z^2)(1+R^2)^(-p-1): angular profiles mu(1-mu^2), mu^3, pole derivatives -2, 3; Gaussian mu P_2j: 1+j(2j+1)
out['src']=[sp.diff(mu*(1-mu**2),mu).subs(mu,1),sp.diff(mu**3,mu).subs(mu,1)]
out['leg']=[sp.diff(mu*sp.legendre(2*j,mu),mu).subs(mu,1)-(1+j*(2*j+1)) for j in range(1,6)]
# topic77: Hessian of f(s,z) in Cartesian, and C derivatives
x1,x2,x3=sp.symbols('x1 x2 x3'); fs=sp.Function('f')
ff=fs(x1**2+x2**2,x3); Hs=sp.hessian(ff,(x1,x2,x3))
ss=sp.Symbol('s'); g=sp.Function('g')
out['hess_xx']=sp.simplify(Hs[0,0]-(2*sp.Subs(sp.Derivative(fs(ss,x3),ss),ss,x1**2+x2**2)+4*x1**2*sp.Subs(sp.Derivative(fs(ss,x3),ss,2),ss,x1**2+x2**2)).doit())==0
ph=sp.Function('phi'); C=2*ph(ss,x3)+2*ss*sp.diff(ph(ss,x3),ss)
out['C']=[sp.simplify(sp.diff(C,ss,2)-(6*sp.diff(ph(ss,x3),ss,2)+2*ss*sp.diff(ph(ss,x3),ss,3)))==0,
          sp.simplify(sp.diff(C,ss,x3)-(4*sp.diff(ph(ss,x3),ss,x3)+2*ss*sp.diff(ph(ss,x3),ss,2,x3)))==0]
# dilation: Uhat = L U(y/L) preserves (1-c)U + c y.grad U + U.grad U + grad P with Phat = L^2 P(y/L) (1D model check)
Lm,yv,cc=sp.symbols('L yv cc',positive=True); U=sp.Function('U'); Pp=sp.Function('Pp')
Uh=Lm*U(yv/Lm); Ph=Lm**2*Pp(yv/Lm)
lhs=(1-cc)*Uh+cc*yv*sp.diff(Uh,yv)+Uh*sp.diff(Uh,yv)+sp.diff(Ph,yv)
xi=sp.Symbol('xi'); rhs=Lm*((1-cc)*U(xi)+cc*xi*sp.diff(U(xi),xi)+U(xi)*sp.diff(U(xi),xi)+sp.diff(Pp(xi),xi))
out['dilation']=sp.simplify(lhs.subs(yv,Lm*xi).doit()-rhs)==0
print(out)
