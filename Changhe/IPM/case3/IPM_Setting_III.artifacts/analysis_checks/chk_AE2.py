# lighter check of the Laplace representation of the even algebraic solution and of A_E (see chk_AE.py)
from mpmath import mp,mpf,gamma,hyp2f1,quad,exp,inf,sqrt,pi
mp.dps=20
def Fd(k,a,b,c,x):  # k-th x-derivative of 2F1
    f=mpf(1)
    for j in range(k): f*= (a+j)*(b+j)/(c+j)
    return f*hyp2f1(a+k,b+k,c+k,x)
import sys
for p in (mpf(1)/4,mpf(1)/2,mpf(3)/4):
    lam=4*p**2/((p+1)**2*(1-p)); s=(p+2)*(p-1)/(p+1); a,b,c=-p/2,-(p+2)/2,mpf(1)/2
    def Ek(z,k):  # k-th z-derivative, k<=3, via chain rule in x = t z^2/lam (argument -x)
        def integrand(t):
            u=t/lam; x=-u*z**2; F=[Fd(j,a,b,c,x) for j in range(4)]
            # g(z)=F(-u z^2): g'=-2uz F1, g''=-2u F1+4u^2z^2 F2, g'''=12u^2 z F2 - 8u^3 z^3 F3
            g=[F[0],-2*u*z*F[1],-2*u*F[1]+4*u**2*z**2*F[2],12*u**2*z*F[2]-8*u**3*z**3*F[3]][k]
            return exp(-t)*t**(-s/2-1)*g
        return quad(integrand,[0,1,10,60,inf])/gamma(-s/2)
    z0=mpf('0.7'); d=[Ek(z0,k) for k in range(4)]
    th1=z0*d[1]; th2=z0*d[1]+z0**2*d[2]; th3=z0*d[1]+3*z0**2*d[2]+z0**3*d[3]
    L=th3-(2*p+2+s)*th2+(p*(p+2)+s*(2*p+2))*th1-p*s*(p+2)*d[0]
    AE=sqrt(pi)*gamma((p+2-s)/2)*lam**(-(p+2)/2)/(gamma(-s/2)*gamma(-p/2)*gamma((p+3)/2))
    r=[Ek(mpf(zz),0)/(AE*mpf(zz)**(p+2)) for zz in (100,1000,10000)]
    print(float(p),'AE',mp.nstr(AE,12),'rel resid',mp.nstr((L+2*lam*d[2])/abs(L),3),'E(0)',mp.nstr(Ek(mpf('1e-8'),0),8),'ratios',[mp.nstr(x,8) for x in r]); sys.stdout.flush()
