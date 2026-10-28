import sympy as sp
x,y=sp.symbols('x y',real=True)
k,A,ell0,a=sp.symbols('k A ell0 a',real=True)
F=lambda n: sp.Function(n)(y)
f,f4,u,v,b,z,z4=[F(n) for n in ['f','f4','u','v','b','z','z4']]
Ru,Rv,Rb=[F(n) for n in ['Ru','Rv','Rb']]
H=sp.Function('H')(x,y)
def vel(Q,R):
    # parity-respecting divergence-free model: U1 odd in x, U2 even in x
    U1=-x*sp.diff(Q,y)+x**3*(-sp.diff(R,y)/3)
    U2=Q+x**2*R
    assert sp.simplify(sp.diff(U1,x)+sp.diff(U2,y))==0
    return U1,U2
rho0=x**2*f+x**4*f4
zeta=x**2*z+x**4*z4
h=x**4*H
Uu=vel(u,Ru); Uv=vel(v,Rv); Ub=vel(b,Rb)
grad=lambda q:(sp.diff(q,x),sp.diff(q,y))
dot=lambda U,g:U[0]*g[0]+U[1]*g[1]
T=lambda q: ell0*(x*sp.diff(q,x)+y*sp.diff(q,y))+dot(Uu,grad(q))-q
def axis(q):
    q=sp.expand(q)
    return sp.simplify(sp.limit(q/x**2,x,0)) if False else sp.simplify(sp.expand(q/x**2).subs(x,0))
nu=sp.Symbol('nu',positive=True)
lam=a/ell0
F0=T(rho0)
Xg=x*sp.diff(rho0,x)+y*sp.diff(rho0,y)
M0=(Xg+T(zeta)+dot(Uv,grad(rho0)))/nu
ch=a*nu
A0h=T(h)+dot(Ub,grad(rho0))+ch*M0
Rh=A0h-lam*F0
K=lambda q,G: q*sp.diff(G,y)-2*sp.diff(q,y)*G
D=lambda G:(ell0*y+u)*sp.diff(G,y)+(2*ell0-1-2*sp.diff(u,y))*G
print('axis(F0)-Df:',sp.simplify(axis(F0)-D(f)))
print('axis(U[h].grad rho0)-K_b f:',sp.simplify(axis(dot(Ub,grad(rho0)))-K(b,f)))
print('axis(T zeta)-Dz:',sp.simplify(axis(T(zeta))-D(z)))
print('axis(X.grad rho0)-(yf\'+2f):',sp.simplify(axis(Xg)-(y*sp.diff(f,y)+2*f)))
print('axis(U[zeta].grad rho0)-K_v f:',sp.simplify(axis(dot(Uv,grad(rho0)))-K(v,f)))
# T h: x^4 H with H generic smooth; check T h / x^2 -> 0 at x=0
Th=sp.expand(T(h)/x**2)
print('axis(T h):',sp.simplify(Th.subs(x,0)))
w=b+a*(v-u/ell0)
print('identity (1):',sp.simplify(axis(Rh)-(K(w,f)+lam*f+a*D(z))))
# identity (2)-(3): 1D, both signs of y
chiI=sp.Function('chiI')
for s in [1,-1]:
    t=sp.Symbol('t',positive=True)  # t=|y|
    Y=s*t
    finf=s*A*t**(k-2)
    chi=chiI(t)
    # derivatives w.r.t. y: d/dy = s d/dt
    dy=lambda G: s*sp.diff(G,t)
    uu=sp.Function('u')(t); ff=sp.Function('f')(t); ww=sp.Function('w')(t)
    E=lambda G: ell0*Y*dy(G)+(2*ell0-1)*G
    Kq=lambda q,G: q*dy(G)-2*dy(q)*G
    DD=lambda G:(ell0*Y+uu)*dy(G)+(2*ell0-1-2*dy(uu))*G
    print('sign',s,': y finf\'-(k-2)finf =',sp.simplify(Y*dy(finf)-(k-2)*finf),
          '; E finf at ell0=1/k:',sp.simplify(E(finf).subs(ell0,1/k)))
    print('   D-(E+K_u) on generic G:',sp.simplify(DD(ff)-E(ff)-Kq(uu,ff)))
    zz=-k**2*chi*sp.log(t)*finf
    Dz_claim=-k**2*(chi*sp.log(t)*Kq(uu,finf)+(ell0*Y+uu)*(dy(chi)*sp.log(t)+chi/Y)*finf)
    print('   Dz - claim (ell0 generic):',sp.simplify((DD(zz)-Dz_claim).subs(ell0,1/k)))
    chip=s*sp.Derivative(chi,t)  # chi' as function of y
    lhs1=Kq(ww,ff)+a*k*ff+a*DD(zz)   # (1) with lambda=a k
    rhs3=Kq(ww,ff)+a*k*(ff-chi*finf)-a*k**2*(chi*sp.log(t)*Kq(uu,finf)+chi*(uu/Y)*finf
          +(ell0*Y+uu)*dy(chi)*sp.log(t)*finf)
    print('   (1)-(3) at ell0=1/k:',sp.simplify((lhs1-rhs3).subs(ell0,1/k)))
    print('   (1)-(3) with ell0 generic (should NOT vanish):',sp.factor(sp.simplify(lhs1-rhs3)))
    r4=rhs3.subs(sp.Derivative(chi,t),0).subs(chi,1).doit()
    rhs4=Kq(ww,ff)+a*k*(ff-finf)-a*k**2*((uu/Y)*finf+sp.log(t)*Kq(uu,finf))
    print('   (3)|chi=1 - (4):',sp.simplify(r4-rhs4))
# Gaussian trace
g=-y**3*sp.exp(-y**2)/6
print('-g\'\' - stated b:',sp.simplify(-sp.diff(g,y,2)-(y-sp.Rational(7,3)*y**3+sp.Rational(2,3)*y**5)*sp.exp(-y**2)))
print('b\'(0)=c[d]:',sp.diff(-sp.diff(g,y,2),y).subs(y,0))
# homogeneity: axis of r^k cos^2(theta) Phi(theta) on x=0, y>0 and y<0
Phi=sp.Function('Phi')
for s in [1,-1]:
    yy=sp.Symbol('Y',positive=True)*s
    r=sp.sqrt(x**2+yy**2); th=sp.atan2(yy,x)
    P=r**k*sp.cos(th)**2*Phi(th)
    print('axis(r^k cos^2 Phi) sign',s,':',sp.simplify(sp.limit(P/x**2,x,0,'+')))
