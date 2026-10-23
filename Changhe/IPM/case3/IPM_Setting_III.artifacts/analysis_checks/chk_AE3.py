# pointwise check of (th-p)(th-s)(th-p-2)F + 2 lam F_zz = 8 (tau d/dtau - s/2 - tau) Phi, Phi=(tau d/dtau-p/2)(tau d/dtau-(p+2)/2)F
from mpmath import mp,mpf,hyp2f1,diff
mp.dps=30
for p in (mpf(1)/4,mpf(1)/2,mpf(3)/4):
    lam=4*p**2/((p+1)**2*(1-p)); s=(p+2)*(p-1)/(p+1)
    F=lambda tau,z: hyp2f1(-p/2,-(p+2)/2,mpf(1)/2,-tau*z**2/lam)
    tau0,z0=mpf('1.3'),mpf('0.8')
    th=lambda f: (lambda z: z*diff(f,z))
    g=lambda z: F(tau0,z)
    def thk(f,k,z):  # th^k f at z via derivatives
        d=[diff(f,z,j) for j in range(4)]
        return [d[0],z*d[1],z*d[1]+z**2*d[2],z*d[1]+3*z**2*d[2]+z**3*d[3]][k]
    t=[thk(g,k,z0) for k in range(4)]
    L=t[3]-(2*p+2+s)*t[2]+(p*(p+2)+s*(2*p+2))*t[1]-p*s*(p+2)*t[0]+2*lam*diff(g,z0,2)
    Dop=lambda f: (lambda tau: tau*diff(f,tau))
    f0=lambda tau: F(tau,z0)
    Phi=lambda tau: tau**2*diff(f0,tau,2)+tau*diff(f0,tau)-(p+1)*tau*diff(f0,tau)+p*(p+2)/4*f0(tau)
    R=8*(tau0*diff(Phi,tau0)-s/2*Phi(tau0)-tau0*Phi(tau0))
    print(float(p),mp.nstr(L,15),mp.nstr(R,15),mp.nstr(L-R,3))
