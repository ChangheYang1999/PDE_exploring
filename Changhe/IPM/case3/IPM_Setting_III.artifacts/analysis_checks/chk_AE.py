# check: E(z)=1/G(-s/2) int e^-t t^{-s/2-1} 2F1(-p/2,-(p+2)/2;1/2;-t z^2/lam) dt solves (th-p)(th-s)(th-p-2)h=-2 lam h''
# and E ~ A_E z^{p+2} as z->inf, A_E = sqrt(pi) G((p+2-s)/2) lam^{-(p+2)/2}/(G(-s/2)G(-p/2)G((p+3)/2))
from mpmath import mp,mpf,gamma,hyp2f1,quad,exp,inf,diff,sqrt,pi,log
mp.dps=30
for p in (mpf(1)/4,mpf(1)/2,mpf(3)/4):
    K=1; lam=4*p**2*K/((p+1)**2*(1-p)); s=(p+2)*(p-1)/(p+1)
    E=lambda z: quad(lambda t: exp(-t)*t**(-s/2-1)*hyp2f1(-p/2,-(p+2)/2,mpf(1)/2,-t*z**2/lam),[0,1,10,inf])/gamma(-s/2)
    AE=sqrt(pi)*gamma((p+2-s)/2)*lam**(-(p+2)/2)/(gamma(-s/2)*gamma(-p/2)*gamma((p+3)/2))
    # residual at z=0.7 via theta derivatives: th=z d/dz
    z0=mpf('0.7')
    d=[diff(E,z0,k) for k in range(4)]
    th1=z0*d[1]; th2=z0*d[1]+z0**2*d[2]; th3=z0*d[1]+3*z0**2*d[2]+z0**3*d[3]
    # (th-p)(th-s)(th-p-2) = th^3 -(2p+2+s) th^2 + (p(p+2)+s(2p+2)) th - p s (p+2)
    L=th3-(2*p+2+s)*th2+(p*(p+2)+s*(2*p+2))*th1-p*s*(p+2)*d[0]
    res=L+2*lam*d[2]
    zl=mpf(400); ratio=E(zl)/(AE*zl**(p+2))
    print(float(p),'AE',mp.nstr(AE,12),'resid',mp.nstr(res,3),'scale',mp.nstr(abs(L),3),'E(400)/(AE 400^{p+2})',mp.nstr(ratio,10))
