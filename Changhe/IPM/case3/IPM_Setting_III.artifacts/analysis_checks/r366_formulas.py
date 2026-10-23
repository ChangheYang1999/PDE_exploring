# Lead checks for A.3.66: formula (2), the mode operator, the top stream coefficient,
# the identity for sigma_i n_j - M_i s_j, the bracket, and recurrence (3) against a
# direct Cartesian computation of the top chain (velocity from U = (-psi_y, psi_x)).
import sympy as sp, mpmath as mp
r,t,z,s,p,q=sp.symbols('r t z s p q',positive=True)
ok=[]
# (2): T[r^s (log r)^d] with T f = (1/c) int_1^inf t^{-p-1} f(t r) dt, c=1/p
for d in range(4):
    for sv,pv in [(sp.Rational(-1,3),sp.Rational(1,2)),(sp.Rational(-5,2),sp.Rational(1,3))]:
        lhs=pv*sp.integrate(t**(-pv-1)*(t*r)**sv*(sp.log(r)+sp.log(t))**d,(t,1,sp.oo))
        rhs=pv*r**sv*sum(sp.binomial(d,i)*sp.factorial(i)*sp.log(r)**(d-i)/(pv-sv)**(i+1) for i in range(d+1))
        ok.append(sp.simplify(sp.expand(lhs-rhs))==0)
# mode operator: -Lap(r^{s+1} Q(log r) sin(M th)) = -r^{s-1}[Q''+2(s+1)Q'+((s+1)^2-M^2)Q] sin(M th)
x,y=sp.symbols('x y',real=True); M=4
Q=sp.Function('Q')
R=sp.sqrt(x**2+y**2); th=sp.atan2(y,x)
for Qe in [z**2+3*z+1, z**3]:
    f=R**(s+1)*Qe.subs(z,sp.log(R))*sp.sin(M*th)
    lap=sp.diff(f,x,2)+sp.diff(f,y,2)
    Qd=sp.diff(Qe,z); Qdd=sp.diff(Qe,z,2)
    pred=-R**(s-1)*(Qdd+2*(s+1)*Qd+((s+1)**2-M**2)*Qe).subs(z,sp.log(R))*sp.sin(M*th)
    val=(-lap-pred).subs({x:sp.Rational(3,5),y:sp.Rational(7,5),s:sp.Rational(-2,7)})
    ok.append(abs(sp.N(val,30))<1e-25)
# d_x(r^s z^d sin j th): sin((j+1)th) coefficient r^{s-1}[(s-j) z^d + d z^{d-1}]/2
for j,d in [(3,0),(3,2),(5,1)]:
    f=R**s*sp.log(R)**d*sp.sin(j*th)
    g=sp.diff(f,x)
    sv=sp.Rational(1,3); rv=sp.Rational(17,10)
    gg=sp.lambdify(sp.Symbol('T'),g.subs({s:sv}).subs({x:rv*sp.cos(sp.Symbol('T')),y:rv*sp.sin(sp.Symbol('T'))}),'mpmath')
    mp.mp.dps=30
    coef=mp.quad(lambda T: gg(T)*mp.sin((j+1)*T),[0,2*mp.pi])/mp.pi
    zz=mp.log(rv)
    pred=rv**(sv-1)*((sv-j)*zz**d+(d*zz**(d-1) if d>0 else 0))/2
    ok.append(abs(coef-pred)<1e-20)
# identity sigma_i n_j - M_i s_j = 2 v (n+1) - [u(n+p)+2], and c_ij
u,v,n=sp.symbols('u v n',positive=True)
de=1-p; ni=u*(n+1)-1; si=1-u*de; nj=v*(n+1)-1; sj=1-v*de
ok.append(sp.expand((si+1)*nj-(ni+1)*sj-(2*v*(n+1)-(u*(n+p)+2)))==0)
ok.append(sp.expand(ni+si+2-(u*(n+p)+2))==0)
L=n+p; e1=u+v; e2=u*v
br=v/(u*L+2)+u/(v*L+2)
ok.append(sp.simplify(br-(L*(e1**2-2*e2)+2*e1)/(L**2*e2+2*L*e1+4))==0)
ok.append(sp.simplify(((L*(e1**2-2*e2)+2*e1)/(L**2*e2+2*L*e1+4)).subs(e2,e1**2/4)-2*e1/(L*e1+4))==0)
print('formal',all(ok),len(ok))
# direct Cartesian top chain: A_k from Cartesian velocity products vs recurrence (3)
def chain(nv,pv,K):
    c=1/pv; D=c-1; de=1-pv
    A=[mp.mpf(1)]  # a=1
    nk=lambda k:(k+1)*(nv+1)-1; sk=lambda k:(k+1)*pv-k
    X,Y=sp.symbols('X Y',real=True); RR=sp.sqrt(X**2+Y**2); TH=sp.atan2(Y,X)
    rec=[mp.mpf(1)]
    for k in range(1,K+1):
        tot=0
        for i in range(k):
            j=k-1-i
            beta=-A[i]/(2*(nk(i)+sk(i)+2))
            psi=sp.Float(str(beta),40)*RR**(sp.nsimplify(sk(i))+1)*sp.sin((nk(i)+1)*TH)
            rho=sp.Float(str(A[j]),40)*RR**sp.nsimplify(sk(j))*sp.sin(nk(j)*TH)
            B=-sp.diff(psi,Y)*sp.diff(rho,X)+sp.diff(psi,X)*sp.diff(rho,Y)
            r0=mp.mpf('1.3'); TT=sp.Symbol('T')
            Bf=sp.lambdify(TT,B.subs({X:r0*sp.cos(TT),Y:r0*sp.sin(TT)}),'mpmath')
            cf=mp.quad(lambda T:Bf(T)*mp.sin(nk(k)*T),[0,mp.pi/4,mp.pi/2,3*mp.pi/4,mp.pi,2*mp.pi])/mp.pi
            tot+=cf/r0**sk(k)
        A.append(tot/(k*D))
        cij=lambda i,j: (1-2*(j+1)*(nv+1)/((i+1)*(nv+pv)+2))/4
        rec.append(sum(cij(i,k-1-i)*rec[i]*rec[k-1-i] for i in range(k))/(k*D))
    return A,rec
mp.mp.dps=30
for nv,pv in [(1,mp.mpf(1)/3),(3,mp.mpf(2)/5)]:
    A,rec=chain(nv,pv,3)
    print(nv,[mp.nstr(a,15) for a in A],[mp.nstr(a,15) for a in rec],
          max(abs(a-b) for a,b in zip(A,rec))<1e-18, [mp.sign(a)==(-1)**k for k,a in enumerate(A)])
