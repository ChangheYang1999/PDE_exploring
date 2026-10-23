# Lead check of ver result123 formulas (1)-(8): density-moment canonical inverse.
import mpmath as mp
mp.mp.dps=30
p=mp.mpf(1)/3; al=(1-p)/2; L=mp.mpf('1.7')
w=lambda r:(1+(r/L)**2)**(-al)
sg=lambda r:r**2/(L**2+r**2)
T=lambda j,x:mp.chebyt(j,x)
def hk(k,j,r): return w(r)*sg(r)**k*T(j,1-2*w(r))
ok=[]
# (1)-(2) against direct Green formula with source G_m from rho_x, single basis element k,j
for (k,j) in [(1,2),(2,1),(0,3)]:
    # h_n for this element
    def h(n,r):
        if k==0: return hk(0,j,r) if n==1 else 0
        if n==2*k+1: return hk(k,j,r)/2
        if n==2*k-1: return -hk(k,j,r)/2
        return 0
    def hd(n,r): return r*mp.diff(lambda s:h(n,s),r)
    for m in [2*k, 2*k+2] if k>0 else [2]:
        if m<2: continue
        r=mp.mpf('0.9')
        A=r**(-m-2)*mp.quad(lambda s:s**(m+1)*h(m-1,s),[0,r])
        B=r**(m-2)*mp.quad(lambda s:s**(1-m)*h(m+1,s),[r,mp.inf])
        G=lambda s:(hd(m-1,s)+(2-m)*h(m-1,s))/2+(hd(m+1,s)+(m+2)*h(m+1,s))/2
        P=(r**(-m-2)*mp.quad(lambda s:s**(m+1)*G(s),[0,r])+r**(m-2)*mp.quad(lambda s:s**(1-m)*G(s),[r,1,10,mp.inf]))/(2*m)
        ok.append(('green',k,j,m,abs(P-(B-A)/2)<1e-15))
        # psi'/r
        def Ps(rr):
            A_=rr**(-m-2)*mp.quad(lambda s:s**(m+1)*h(m-1,s),[0,rr]); B_=rr**(m-2)*mp.quad(lambda s:s**(1-m)*h(m+1,s),[rr,mp.inf])
            return rr**2*(B_-A_)/2
        d=mp.diff(Ps,r)/r
        ok.append(('dpsi',k,j,m,abs(d-(m*(A+B)-h(m-1,r)-h(m+1,r))/2)<1e-12))
        # (3) upper moment formula for the element (unsigned)
        hh=m//2; dd=k-hh
        if dd in (0,1) and m>=2:
            Bk=r**(m-2)*mp.quad(lambda s:s**(1-m)*hk(k,j,s),[r,mp.inf])
            beta=(hh-1)/al; ww=w(r)
            I=lambda b:mp.quad(lambda v:v**b*T(j,1-2*ww*v),[0,1])
            F=sg(r)**(hh-1)*ww/(2*al)*sum((-1)**e*mp.binomial(dd,e)*ww**(e/al)*I(beta+e/al) for e in range(dd+1))
            ok.append(('(3)',k,j,m,abs(Bk-F)<1e-15))
# (5),(6) charts and (8) partition for the unsigned lower moment
def A4(m,k,j,q): return mp.quad(lambda u:u**(m+1)*w(L*q*u)*sg(L*q*u)**k*T(j,1-2*w(L*q*u)),[0,1])
def A5(m,k,j,q): return mp.quad(lambda u:u**(m+1+2*k)*(q**2/(1+q**2*u**2))**k*(1+q**2*u**2)**(-al)*T(j,1-2*w(L*q*u)),[0,1])
def A6(m,k,j,q): return q**(-2*al)*mp.quad(lambda u:u**(m+p)*sg(L*q*u)**(al+k)*T(j,1-2*w(L*q*u)),[0,1])
for (m,k,j,q) in [(2,1,2,mp.mpf('0.4')),(4,2,1,mp.mpf('3.3')),(6,3,3,mp.mpf('11.0'))]:
    ok.append(('(5)',m,k,j,abs(A4(m,k,j,q)-A5(m,k,j,q))<1e-15))
    ok.append(('(6)',m,k,j,abs(A4(m,k,j,q)-A6(m,k,j,q))<1e-15))
    if q>=1:
        J=int(mp.ceil(mp.log(q,2))); a=mp.mpf(2)**(-J)
        S=a**(m+2)*A5(m,k,j,q*a)+sum(q**(-2*al)*mp.quad(lambda u:u**(m+p)*sg(L*q*u)**(al+k)*T(j,1-2*w(L*q*u)),[mp.mpf(2)**(-i),mp.mpf(2)**(-i+1)]) for i in range(1,J+1))
        ok.append(('(8)',m,k,j,abs(S-A4(m,k,j,q))<1e-15, 0.5<q*a<=1))
# (7)
for q in [mp.mpf('0.3'),mp.mpf('2.5')]:
    A=mp.quad(lambda u:u**3*(1+q**2*u**2)**(-al),[0,1])
    F=(((1+q**2)**(2-al)-1)/(2-al)-((1+q**2)**(1-al)-1)/(1-al))/(2*q**4)
    ok.append(('(7)',q,abs(A-F)<1e-20))
for o in ok: print(o)
print('ALL', all(all(x for x in o if isinstance(x,bool)) for o in ok))
# (3) with d = 1 (upper mode m+1 = 2k-1)
ok2=[]
for (k,j,m) in [(2,1,2),(3,2,4),(2,0,2)]:
    r=mp.mpf('1.3'); hh=m//2; dd=k-hh; assert dd==1
    Bk=r**(m-2)*mp.quad(lambda s:s**(1-m)*hk(k,j,s),[r,10,mp.inf])
    beta=(hh-1)/al; ww=w(r)
    I=lambda b:mp.quad(lambda v:v**b*T(j,1-2*ww*v),[0,1])
    F=sg(r)**(hh-1)*ww/(2*al)*sum((-1)**e*mp.binomial(dd,e)*ww**(e/al)*I(beta+e/al) for e in range(dd+1))
    ok2.append(('(3) d=1',k,j,m,abs(Bk-F)<1e-15))
for o in ok2: print(o)
print('ALL2', all(o[-1] for o in ok2))
