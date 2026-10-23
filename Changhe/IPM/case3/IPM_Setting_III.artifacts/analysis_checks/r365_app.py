# Lead check of the identities used in the draft A.3.65 (own code, independent of the external verification script).
import sympy as s, random
from math import comb
x,y,r,sv,u=s.symbols('x y r s u',positive=True)
W,V=s.symbols('w v')
I=s.I
def S(n,p):   # r^n sin(p th), Cartesian
    return s.expand(s.im(s.expand((x+I*y)**p))*(x**2+y**2)**((n-p)//2))
def Swv(n,p): # same in (w, v)
    return s.expand((W**((n+p)//2)*V**((n-p)//2)-W**((n-p)//2)*V**((n+p)//2))/(2*I))
def P(n,p):
    e=-S(n+1,p+1)/(2*(n+p+2))
    if p>1: e+=-S(n+1,p-1)/(2*(n-p+2))
    return s.expand(e)
dx=lambda e: s.diff(e,x); dy=lambda e: s.diff(e,y); lap=lambda e: s.diff(e,x,2)+s.diff(e,y,2)
res={}
# (a) local form of the modal formula (1): F_k = r^{n-1} for p = 2k+1 gives (2)
ok=True
for n in range(3,14,2):
    for p in range(1,n+1,2):
        k=(p-1)//2
        tot=0
        if k>=1:   # upper integral of mode m=k, local part -int_0^r F_k s^{1-2k}
            up=-s.integrate(sv**(n-1)*sv**(1-2*k),(sv,0,r))
            tot+= (r**2/2)*r**(2*k-2)*up*s.Symbol('SIN%d'%(2*k))
        lo=-r**(-2*(k+1)-2)*s.integrate(sv**(2*(k+1)+1)*sv**(n-1),(sv,0,r))
        tot+=(r**2/2)*lo*s.Symbol('SIN%d'%(2*k+2))
        tgt=-r**(n+1)/(2*(n+p+2))*s.Symbol('SIN%d'%(p+1))
        if p>1: tgt+=-r**(n+1)/(2*(n-p+2))*s.Symbol('SIN%d'%(p-1))
        ok&= s.simplify(tot-tgt)==0
res['(2) is the local form of (1), n<=13']=ok
# term a y: F_0 = a gives -(a/8) r^2 sin 2th
a=s.Symbol('a')
res['a y gives -(a/8) r^2']=s.simplify((r**2/2)*(-r**-4*s.integrate(sv**3*a,(sv,0,r)))+a*r**2/8)==0
# integration by parts of Step 1 with generic functions
m=s.Symbol('m',positive=True,integer=True)
Fm1=s.Function('G')(sv); Fm=s.Function('F')(sv)
fm=s.Rational(1,2)*(s.diff(sv*Fm1,sv)-(2*m-1)*Fm1+s.diff(sv*Fm,sv)+(2*m+1)*Fm)
b=sv*(Fm1+Fm)
res['IBP 1']=s.simplify(sv**(2*m+1)*fm-(s.diff(sv**(2*m+1)*b,sv)/2-2*m*sv**(2*m+1)*Fm1))==0
res['IBP 2']=s.simplify(sv**(1-2*m)*fm-(s.diff(sv**(1-2*m)*b,sv)/2+2*m*sv**(1-2*m)*Fm))==0
# rho_x mode coefficient: for rho = s F_{m-1} sin(2m-1)th + s F_m sin(2m+1)th check the sin 2m th coefficient of d_x
# (done for explicit polynomial F's)
th=s.Symbol('th',real=True)
ok=True
for mm in (1,2,3):
    G=sv**(2*mm-2)*(1+sv**2); F=sv**(2*mm)*(2-sv**2)
    rho=sv*G*s.sin((2*mm-1)*th)+sv*F*s.sin((2*mm+1)*th)
    rx=s.cos(th)*s.diff(rho,sv)-s.sin(th)/sv*s.diff(rho,th)
    coef=s.integrate(s.expand(s.expand_trig(rx*s.sin(2*mm*th))),(th,0,2*s.pi))/s.pi
    f=s.Rational(1,2)*(s.diff(sv*G,sv)-(2*mm-1)*G+s.diff(sv*F,sv)+(2*mm+1)*F)
    ok&=s.simplify(coef-f)==0
res['sin 2m th coefficient of rho_x']=ok
# (b) Step 2 formulas
ok1=ok2=ok3=True
for n in range(3,14,2):
    for p in range(1,n+1,2):
        Sm=lambda q: S(n,q) if q>0 else -S(n,-q)
        ok1&= s.expand(x*dx(S(n,p))-y*dy(S(n,p))-((n-p)*S(n,p+2)/2 if p+2<=n else 0)-(n+p)*Sm(p-2)/2)==0
        e=-S(n,p)/4-((n-p)*S(n,p+2)/(4*(n+p+2)) if p+2<=n else 0)
        if p>1: e+=-S(n,p)/4-(n+p)*Sm(p-2)/(4*(n-p+2))
        ok2&= s.expand(dx(P(n,p))-e)==0
        ok3&= s.expand(dx(S(n,p))-((n-p)*S(n-1,p+1)/2 if True else 0)-((n+p)*S(n-1,p-1)/2 if p>1 else 0))==0
res['(x d_x - y d_y) S']=ok1; res['d_x P S']=ok2; res['d_x S']=ok3
res['Lap S']=all(s.expand(lap(S(m_,k_))-(m_**2-k_**2)*(S(m_-2,k_) if k_<=m_-2 else 0))==0 for m_ in range(2,12) for k_ in range(m_%2,m_+1,2) if k_>0)
res['S in (w,v)']=all(s.expand(Swv(n,p).subs({W:x+I*y,V:x-I*y})-S(n,p))==0 for n in range(1,10,2) for p in range(1,n+1,2))
# (c) P0 and P - P0, norm bounds
def coeffs(g,n):
    pg=s.Poly(s.expand(g),W,V); return [pg.coeff_monomial(W**mu*V**(n-mu)) for mu in range(n+1)]
def norm(g,n): return max(abs(complex(cf))/comb(n,mu) for mu,cf in enumerate(coeffs(g,n)))
random.seed(1); okP0=okPd=True; worst=[0,0,0]
for n in range(3,12,2):
    j=(n-1)//2
    for trial in range(4):
        sk=[s.Rational(random.randint(-9,9),random.randint(1,5)) for _ in range(j+1)]
        g=sum(sk[k]*Swv(n,2*k+1) for k in range(j+1)); gc=coeffs(g,n)
        P0=sum(-s.Rational(1,4)*(gc[mu]/(n-mu+1)+gc[mu-1]/mu)*W**mu*V**(n+1-mu) for mu in range(1,n+1))
        okP0&= s.expand(-4*s.diff(P0,W,V)-(s.diff(g,W)+s.diff(g,V)))==0
        Pg=sum(sk[k]*s.expand(P(n,2*k+1).subs({x:(W+V)/2,y:(W-V)/(2*I)})) for k in range(j+1))
        okPd&= s.expand(Pg-P0+sk[j]*Swv(n+1,n+1)/(4*(n+1)))==0
        ng=norm(g,n)
        worst[0]=max(worst[0],norm(Pg,n+1)*(n+1)/ng)
        worst[1]=max(worst[1],norm(s.diff(Pg,W)+s.diff(Pg,V),n)/ng)
        worst[2]=max(worst[2],norm(I*(s.diff(Pg,W)-s.diff(Pg,V)),n)/ng)
        # norm equals max |s_k|/(2 omega_k)
        assert abs(ng-max(abs(float(sk[k]))/(2*comb(n,j-k)) for k in range(j+1)))<1e-12
res['P0 inverse']=okP0; res['P - P0 = -s_j S_{n+1,n+1}/(4(n+1))']=okPd
res['sampled (n+1)||Pg||/||g||, ||dxPg||/||g||, ||dyPg||/||g|| (bounds 1, 3/2, 3/2)']=[round(t,4) for t in worst]
# U_H components
H=s.Symbol('H',positive=True); psiH=H/2*Swv(4,4)
res['U_H']=[s.expand(-I*(s.diff(psiH,W)-s.diff(psiH,V))+H*(W**3+V**3))==0, s.expand(s.diff(psiH,W)+s.diff(psiH,V)-2*H*Swv(3,3))==0]
# (d) series identities and constants
q=s.Symbol('q')
res['sum_{j>=2}(2j+1)q^j']=s.simplify(s.summation((2*m+1)*q**m,(m,2,s.oo)).args[0][0]-q**2*(5-3*q)/(1-q)**2)==0 if False else s.simplify(sum((2*jj+1)*q**jj for jj in range(2,40))-s.series(q**2*(5-3*q)/(1-q)**2,q,0,40).removeO())==0
res['sum_{k>=3}(2k+1)b^k']=s.simplify(sum((2*jj+1)*q**jj for jj in range(3,40))-s.series(q**3*(7-5*q)/(1-q)**2,q,0,40).removeO())==0
res['(5-3q)/(1-q)^2 at q=1/2']=(5-3*s.Rational(1,2))/(1-s.Rational(1,2))**2
res['C_k constant 4*(1/16)*12*(3/2)']=4*s.Rational(1,16)*12*s.Rational(3,2)
res['64/63*4 <= 8']=s.Rational(64,63)*4<=8
res['middle third: min u(1-u) on [1/3,2/3]']=s.Rational(1,3)*s.Rational(2,3)
# truncated last row margin
c,lam_,d=s.symbols('c lam d'); D=c-1
res['last-row margin']=s.simplify(c*lam_+D-D*(lam_+2*(d-1)+2)/2-(lam_+D*(lam_-2*d+2)/2))==0
res['interior margin']=s.simplify(c*lam_+D-D*(lam_-2*u)/2-D*(lam_+2*u+2)/2-lam_)==0
res['first-row margin']=s.simplify((c+1)*lam_/2-D*lam_/2-lam_)==0
# F > 0 rewrite
a_=s.Symbol('a'); F=a_**2-(4*c+20)*a_+128*c-64
res['F = a(a-4c-20)+128c-64']=s.expand(F-(a_*(a_-4*c-20)+128*c-64))==0
for k_,v_ in res.items(): print(k_,':',v_)
