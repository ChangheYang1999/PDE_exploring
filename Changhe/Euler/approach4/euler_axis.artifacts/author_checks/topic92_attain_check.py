# Lead cross-check of the topic 92 attainment result (top Legendre coefficient of the bulk pressure source f = tr(DU^2)).
# Independent of the verifier's checker:
# (1) generic fields phi = a(R) mu^N + lower, q = b(R) mu^M + lower with random rational radial polynomials (including
#     negative powers) in every angular power; f from the Cartesian Jacobian (same construction as topic92_check.py);
#     at a fixed radius the monomial coefficient of mu^D of f (exact Gauss-Legendre projection, 50 digits) is compared
#     with T_phi, T_q or T_phi + T_q according to N > M, M > N, N = M;
# (2) sharpness: symbolic T_phi for a = R^k and T_q for b = R^k, and the values at k = N + 2 and k = M + 2;
# (3) the Jacobi expansion used for the ball basis, against sympy's jacobi;
# (4) the exact top source coefficient at R = 1 of two frozen exports (degrees 50 and 88), from the binary coefficients as
#     exact rationals, with the ball basis built here from BASIS.md, compared with the verifier's rounded table values.
import sympy as sp, mpmath as mp, numpy as np, json, random, datetime, time
t0=time.time()
mp.mp.dps=50
x,y,z=sp.symbols('x y z',real=True)
Rs,mus,ts=sp.symbols('R mu t',real=True)
random.seed(921)
res=[]
def check(name,ok,val=None):
    res.append(dict(check=name,ok=bool(ok),value=None if val is None else str(val))); print(('PASS' if ok else 'FAIL'),name,val if val is not None else '')
rnd=lambda: sp.Rational(random.randint(-9,9) or 1, random.randint(1,7))
def radial(): return rnd()*Rs**-1+rnd()+rnd()*Rs+rnd()*Rs**2+rnd()*Rs**3
def Tphi(a,N):
    a1=sp.diff(a,Rs); a2=sp.diff(a,Rs,2)
    return ((N+2)**2*a1**2+((-N*a-(N+1)*Rs*a1)**2+(N*a-Rs*a1)**2)/Rs**2+2*(N*(N+3)*a-Rs*a1)*(-3*a1-Rs*a2)/Rs)
def Tq(b,M): return 2*b*(Rs*sp.diff(b,Rs)-M*b)
def gauss(n):
    xs=[mp.cos(mp.pi*(k+mp.mpf(3)/4)/(n+mp.mpf(1)/2)) for k in range(n)]; nodes=[]; weights=[]
    for x0 in xs:
        for _ in range(100):
            p0,p1=mp.mpf(1),x0
            for kk in range(2,n+1): p0,p1=p1,((2*kk-1)*x0*p1-(kk-1)*p0)/kk
            dp=n*(x0*p1-p0)/(x0**2-1); dx=p1/dp; x0-=dx
            if abs(dx)<mp.mpf(10)**-45: break
        nodes.append(x0); weights.append(2/((1-x0**2)*dp**2))
    return nodes,weights
def lcP(D): return sp.Rational(sp.factorial(2*D),2**D*sp.factorial(D)**2)
# (1) generic leading-coefficient check
for (N,M) in [(4,2),(2,5),(3,3)]:
    D=2*max(N,M)+2
    a=[radial() for j in range(N+1)]; b=[radial() for j in range(M+1)]
    ph=sum(a[j]*mus**j for j in range(N+1)); qq=sum(b[j]*mus**j for j in range(M+1))
    cart=lambda e: e.subs({Rs:sp.sqrt(x**2+y**2+z**2),mus:z/sp.sqrt(x**2+y**2+z**2)})
    P=cart(ph); Q=cart(qq)
    U=[-x*sp.diff(P,z)-y*Q, -y*sp.diff(P,z)+x*Q, 2*P+x*sp.diff(P,x)+y*sp.diff(P,y)]
    X=[x,y,z]; J=sp.Matrix(3,3,lambda i,j: sp.diff(U[i],X[j])); f=(J*J).trace()
    fl=sp.lambdify((x,y,z),f,'mpmath')
    R0=sp.Rational(137,100); n=D+6; nodes,weights=gauss(n)
    vals=[fl(mp.mpf(137)/100*mp.sqrt(1-m**2),0,mp.mpf(137)/100*m) for m in nodes]
    cD=(2*D+1)/mp.mpf(2)*mp.fsum(w*v*mp.legendre(D,m) for w,v,m in zip(weights,vals,nodes))
    mono=cD*mp.mpf(sp.N(lcP(D),60))
    T=(Tphi(a[N],N) if N>=M else 0)+(Tq(b[M],M) if M>=N else 0)
    Tv=mp.mpf(sp.N(T.subs(Rs,R0),60))
    check('mu^%d coefficient of f equals the top-coefficient formula (N=%d, M=%d)'%(D,N,M),abs(mono-Tv)<mp.mpf(10)**-35*(1+abs(Tv)),
          '%s vs %s'%(mp.nstr(mono,15),mp.nstr(Tv,15)))
    # degrees above D vanish
    above=max(abs((2*l+1)/mp.mpf(2)*mp.fsum(w*v*mp.legendre(l,m) for w,v,m in zip(weights,vals,nodes))) for l in range(D+1,min(n,2*n-D)))
    check('Legendre coefficients above D vanish for the generic field (N=%d, M=%d)'%(N,M),above<mp.mpf(10)**-35*(1+abs(cD)),mp.nstr(above,5))
# (2) sharpness
k,Nn,Mm=sp.symbols('k N M',integer=True)
for (N,kk) in [(0,2),(3,5),(7,9),(5,2),(4,4)]:
    T=sp.simplify(Tphi(Rs**kk,N)-2*Rs**(2*kk-2)*(kk-N)*(kk**2+(N+5)*kk-N))
    check('T_phi(R^%d) = 2 R^(2k-2)(k-N)(k^2+(N+5)k-N) (N=%d)'%(kk,N),T==0)
gen=sp.simplify(Tphi(Rs**k,Nn)/Rs**(2*k-2)-2*(k-Nn)*(k**2+(Nn+5)*k-Nn))
check('T_phi(R^k) closed form for symbolic k, N',gen==0)
check('T_phi(R^(N+2)) = (8N^2+40N+56) R^(2N+2)',sp.simplify(Tphi(Rs**(Nn+2),Nn)-(8*Nn**2+40*Nn+56)*Rs**(2*Nn+2))==0)
check('T_q(R^k) = 2(k-M) R^(2k) and T_q(R^(M+2)) = 4 R^(2M+4)',sp.simplify(Tq(Rs**k,Mm)-2*(k-Mm)*Rs**(2*k))==0 and
      sp.simplify(Tq(Rs**(Mm+2),Mm)-4*Rs**(2*Mm+4))==0)
check('8N^2+40N+56 > 0 for all real N (discriminant negative)',40**2-4*8*56<0)
# (3) Jacobi expansion
for (n_,k_) in [(0,3),(5,4),(24,6),(43,10)]:
    lhs=sp.expand(sp.jacobi(k_,0,sp.Rational(2*n_+1,2),2*ts-1))
    rhs=sp.expand(sum(sp.binomial(k_,m)*sp.binomial(k_+sp.Rational(2*n_+1,2),k_-m)*(ts-1)**(k_-m)*ts**m for m in range(k_+1)))
    check('Jacobi expansion of P_k^(0,n+1/2)(2t-1) (n=%d, k=%d)'%(n_,k_),sp.simplify(lhs-rhs)==0)
# (4) frozen exports
EXP='independent_validation/external_exports/'
ref={'T1_seed_cl0p74_L1_20261029T065203.806505Z':(50,-1.26945035862e-11),'T1_seed_cl0p74_L3_20261029T072143.265106Z':(88,9.65277351994e-26)}
exp_out={}
for d,(Dref,vref) in ref.items():
    Z=np.load(EXP+d+'/coeffs.npz'); meta=json.loads(str(Z['meta_json'])); el=meta['elements'][0]
    assert el['kind']=='ball' and el['radial']=='jacobi'
    Rb=sp.Rational(el['Rhi']).limit_denominator(1000); assert float(Rb)==el['Rhi']
    labels=el['labels']
    def lead(vec,cols):
        lab=[labels[c] for c in cols]
        top=max(int(l[0]) for l,v in zip(lab,vec) if v!=0.0)
        rho=Rs/Rb
        e=sum(sp.Rational(float(v))*rho**top*sp.jacobi(int(l[1]),0,sp.Rational(2*top+1,2),2*rho**2-1)
              for l,v in zip(lab,vec) if int(l[0])==top)
        return top, sp.expand(e*sp.Rational(sp.factorial(2*top),2**top*sp.factorial(top)**2))
    Nt,aR=lead(Z['phi_el0'],el['phi_cols']); Mt,bR=lead(Z['q_el0'],el['q_cols'])
    D=2*max(Nt,Mt)+2
    T=(Tphi(aR,Nt) if Nt>=Mt else 0)+(Tq(bR,Mt) if Mt>=Nt else 0)
    Texact=sp.nsimplify(T.subs(Rs,1)) if False else sp.Rational(T.subs(Rs,1))
    legc=Texact/lcP(D)
    v=float(legc)
    exp_out[d]=dict(N=Nt,M=Mt,D=D,legendre_coefficient=repr(v),exact_nonzero=bool(legc!=0))
    check('export %s: exact top source degree %d at R = 1'%(d.split('_2026')[0],D),D==Dref and legc!=0,'N=%d M=%d'%(Nt,Mt))
    check('export %s: degree-%d Legendre source coefficient agrees with the verifier table'%(d.split('_2026')[0],D),
          abs(v-vref)<=1e-10*abs(vref),'%.11e vs %.11e'%(v,vref))
ok=all(r['ok'] for r in res)
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_checks=len(res),all_pass=ok,
         wall_seconds=round(time.time()-t0,1),exports=exp_out,checks=res)
json.dump(out,open('author_checks/topic92_attain_check_output.json','w'),indent=1)
print('checks',len(res),'all pass',ok,'wall',round(time.time()-t0,1))
