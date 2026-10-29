# Lead cross-check of topic 92 (angular bandwidth of the bulk pressure source tr(DU^2)).
# Route independent of the verifier's: the velocity is built directly in Cartesian coordinates,
#   U_x = -x phi_z - y q,  U_y = -y phi_z + x q,  U_z = 2 phi + x phi_x + y phi_y,
# which equals U_r = -r phi_z, U_theta = r q, U_z = 2 phi + r phi_r for axisymmetric phi, q; DU is the Cartesian Jacobian.
# Checks: (1) div U = 0 symbolically; (2) at fixed R the Legendre coefficients of f = tr(DU^2) vanish above
# D = 2 max(N,M) + 2 (mpmath, 50 digits, exact Gauss-Legendre projection) and the coefficient of degree D is nonzero;
# (3) f agrees with the spherical-frame formula of the proof at random nonpolar points and at the poles;
# (4) the spherical components A, B, C of the proof agree with the Cartesian velocity.
import sympy as sp, mpmath as mp, json, random, datetime
mp.mp.dps=50
x,y,z=sp.symbols('x y z',real=True)
Rs,mus=sp.symbols('R mu',real=True)
random.seed(92)
def field(N,M):
    # phi = sum_k (a_k + b_k R^2 + c_k R^3) P_k(mu), q similar with degree M; generic rational coefficients
    rnd=lambda: sp.Rational(random.randint(-9,9) or 1, random.randint(1,7))
    ph=sum((rnd()+rnd()*Rs**2+rnd()*Rs**3)*sp.legendre(k,mus) for k in range(N+1))
    qq=sum((rnd()+rnd()*Rs+rnd()*Rs**2)*sp.legendre(k,mus) for k in range(M+1))
    return ph,qq
def cart(e):
    R=sp.sqrt(x**2+y**2+z**2); return e.subs({Rs:R,mus:z/R})
res=[]
def check(name,ok,val=None):
    res.append(dict(check=name,ok=bool(ok),value=None if val is None else str(val))); print(('PASS' if ok else 'FAIL'),name,val if val is not None else '')
for (N,M) in [(3,2),(2,4),(4,4)]:
    ph,qq=field(N,M); D=2*max(N,M)+2
    P=cart(ph); Q=cart(qq)
    U=[-x*sp.diff(P,z)-y*Q, -y*sp.diff(P,z)+x*Q, 2*P+x*sp.diff(P,x)+y*sp.diff(P,y)]
    X=[x,y,z]
    J=sp.Matrix(3,3,lambda i,j: sp.diff(U[i],X[j]))
    div=sp.simplify(J.trace())
    check('div U = 0 (N=%d, M=%d)'%(N,M), div==0)
    f=(J*J).trace()
    fl=sp.lambdify((x,y,z),f,'mpmath')
    # spherical-frame formula of the proof
    A=2*mus*ph-(1-mus**2)*sp.diff(ph,mus); B=-(2*ph+Rs*sp.diff(ph,Rs)); C=Rs*qq; S=1-mus**2
    pr=lambda e: sp.diff(e,mus)
    fs=(sp.diff(A,Rs)**2+(A+mus*B-S*pr(B))**2/Rs**2+(A+mus*B)**2/Rs**2-2*S*(pr(A)+B)*sp.diff(B,Rs)/Rs
        -2*S*C*sp.diff(C,Rs)/Rs-2*mus*C*(mus*C-S*pr(C))/Rs**2)
    fsl=sp.lambdify((Rs,mus),fs,'mpmath')
    Al=sp.lambdify((Rs,mus),A,'mpmath'); Bl=sp.lambdify((Rs,mus),B,'mpmath'); Cl=sp.lambdify((Rs,mus),C,'mpmath')
    Ul=[sp.lambdify((x,y,z),u,'mpmath') for u in U]
    # (2) Legendre projection at fixed R with n Gauss nodes, exact for integrand degree <= 2n-1
    R0=mp.mpf('1.37')
    n=D+8
    xs=[mp.cos(mp.pi*(k+mp.mpf(3)/4)/(n+mp.mpf(1)/2)) for k in range(n)]
    nodes=[]; weights=[]
    for x0 in xs:
        for _ in range(100):
            p0,p1=mp.mpf(1),x0
            for kk in range(2,n+1): p0,p1=p1,((2*kk-1)*x0*p1-(kk-1)*p0)/kk
            dp=n*(x0*p1-p0)/(x0**2-1); dx=p1/dp; x0-=dx
            if abs(dx)<mp.mpf(10)**-45: break
        nodes.append(x0); weights.append(2/((1-x0**2)*dp**2))
    vals=[fl(R0*mp.sqrt(1-m**2),0,R0*m) for m in nodes]
    coef=[(2*l+1)/mp.mpf(2)*mp.fsum(w*v*mp.legendre(l,m) for w,v,m in zip(weights,vals,nodes)) for l in range(n)]
    # coefficients l in (D, n-1-D] are exact projections (integrand degree D+l <= 2n-1)
    lmax_exact=2*n-1-D
    above=max(abs(coef[l]) for l in range(D+1,min(n,lmax_exact+1)))
    scale=max(abs(c) for c in coef)
    check('Legendre coefficients above D=%d vanish (N=%d, M=%d)'%(D,N,M), above<mp.mpf(10)**-40*scale, mp.nstr(above/scale,5))
    check('Legendre coefficient of degree D nonzero (N=%d, M=%d)'%(N,M), abs(coef[D])>mp.mpf(10)**-10*scale, mp.nstr(coef[D]/scale,8))
    # (3) spherical formula at random nonpolar points and at the poles (Cartesian side evaluated exactly on the axis)
    err=0
    for t in range(6):
        Rv=mp.mpf(random.uniform(0.3,3)); m=mp.mpf(random.uniform(-0.99,0.99)); ph_=mp.mpf(random.uniform(0,6.28))
        st=mp.sqrt(1-m**2); xv,yv,zv=Rv*st*mp.cos(ph_),Rv*st*mp.sin(ph_),Rv*m
        err=max(err,abs(fl(xv,yv,zv)-fsl(Rv,m))/(1+abs(fl(xv,yv,zv))))
        # (4) components: U_R = A, U_vartheta = sin(theta) B, U_varphi = sin(theta) C
        Uc=[u(xv,yv,zv) for u in Ul]
        eR=[st*mp.cos(ph_),st*mp.sin(ph_),m]; eT=[m*mp.cos(ph_),m*mp.sin(ph_),-st]; eP=[-mp.sin(ph_),mp.cos(ph_),0]
        dot=lambda a,b: sum(ai*bi for ai,bi in zip(a,b))
        err=max(err,abs(dot(Uc,eR)-Al(Rv,m)),abs(dot(Uc,eT)-st*Bl(Rv,m)),abs(dot(Uc,eP)-st*Cl(Rv,m)))
    check('spherical-frame trace formula and components A, B, C at random points (N=%d, M=%d)'%(N,M), err<mp.mpf(10)**-35, mp.nstr(err,5))
    errp=0
    for m in (mp.mpf(1),mp.mpf(-1)):
        Rv=mp.mpf('0.83'); errp=max(errp,abs(fl(0,0,Rv*m)-fsl(Rv,m)))
    check('spherical formula at the poles (N=%d, M=%d)'%(N,M), errp<mp.mpf(10)**-35, mp.nstr(errp,5))
ok=all(r['ok'] for r in res)
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_checks=len(res),all_pass=ok,checks=res)
json.dump(out,open('author_checks/topic92_check_output.json','w'),indent=1)
print('checks',len(res),'all pass',ok)
