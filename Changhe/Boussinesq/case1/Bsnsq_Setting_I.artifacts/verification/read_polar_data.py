"""Data-only reader plus independent Jacobi quadrature for published polar coefficients.

No imports from the numerics lane. Fields and smooth parity quotients use Cartesian
harmonic recurrences. The secondary modal inverse uses independent Gauss-Jacobi
integrals; primary verification velocities come from plane_quadrature instead.
"""
from pathlib import Path
import hashlib
from functools import lru_cache
import numpy as np
from scipy.special import roots_jacobi


def cheb_all(coeff,t):
    """Clenshaw, mode-major coefficients, return shape (modes,*t.shape)."""
    t=np.asarray(t,dtype=np.longdouble)
    c=np.asarray(coeff,dtype=np.longdouble)
    shape=(c.shape[0],)+t.shape
    b1=np.zeros(shape,dtype=np.longdouble);b2=np.zeros_like(b1)
    extra=(None,)*t.ndim
    for k in range(c.shape[1]-1,0,-1):
        b=2*t*b1-b2+c[:,k][(slice(None),)+extra]
        b2,b1=b1,b
    return t*b1-b2+c[:,0][(slice(None),)+extra]


@lru_cache(maxsize=128)
def power_quadrature(n,power):
    # int_0^1 v^power f(v)dv. Divide weights by their known sum to remove 2^power scaling.
    z,w=roots_jacobi(n,0.,float(power))
    w=w/w.sum()/(power+1)
    return (z+1)/2,w


class PolarData:
    def __init__(self,path=None,*,data=None,radial_order=96):
        if data is None:
            raw=np.load(path,allow_pickle=False)
            data={k:raw[k] for k in raw.files}
            self.source=str(Path(path).resolve());self.sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest()
        else:self.source='manufactured coefficient dictionary';self.sha256=None
        self.beta=float(data['beta']);self.L=float(data['L']);self.NT=int(data['NT']);self.NO=int(data['NO']);self.K=int(data['K'])
        self.mu=float(data.get('mu',1/self.beta));self.gammaT=float(data.get('gamma_T',1-2/self.beta));self.gammaO=float(data.get('gamma_O',-1/self.beta))
        self.cT=np.asarray(data['cT'],np.longdouble).reshape(self.NT,self.K)
        self.cO=np.asarray(data['cO'],np.longdouble).reshape(self.NO,self.K)
        self.radial_order=radial_order;self.modal_cache={}
        if abs(self.gammaO+1/self.beta)>1e-12 or abs(self.mu-1/self.beta)>1e-12:
            raise ValueError('this independently derived modal inverse assumes the published mu and gamma_O')
        signs=(-1.)**np.arange(self.K)
        self.a0=float(self.cT[0]@signs/self.L)
        # Exact integral of each Chebyshev polynomial over q in [0,1].
        moment=np.array([1/(1-k*k) if k%2==0 else 0. for k in range(self.K)])
        self.c_exact=float(self.beta/2*(self.cO[0]@moment))

    def geometry(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,np.longdouble),np.asarray(y,np.longdouble))
        u2=(x*x+y*y)/(self.L*self.L);logE=np.log1p(u2)
        invroot=np.exp(-logE/2)/self.L
        a=x*invroot;b=y*invroot;rho2=a*a+b*b
        q=-np.expm1(-np.longdouble(self.mu)*logE/2)
        return x,y,logE,a,b,rho2,q

    def F(self,x,y):
        x,y,logE,a,b,rho2,q=self.geometry(x,y)
        poly=cheb_all(self.cT,2*q-1)
        prev=np.zeros_like(a);cur=np.ones_like(a);result=np.zeros_like(a)
        for m in range(1,2*self.NT):
            if m%2:result+=poly[(m-1)//2]*cur
            prev,cur=cur,2*a*cur-rho2*prev
        return np.exp((self.gammaT-1)*logE/2)*result/self.L

    def G(self,x,y):
        x,y,logE,a,b,rho2,q=self.geometry(x,y)
        poly=cheb_all(self.cO,2*q-1)
        c=a*a-b*b;rho4=rho2*rho2
        prev=np.zeros_like(a);cur=np.ones_like(a);result=np.zeros_like(a)
        for n in range(1,self.NO+1):
            result+=2*poly[n-1]*cur
            prev,cur=cur,2*c*cur-rho4*prev
        return np.exp((self.gammaO-2)*logE/2)*result/(self.L*self.L)

    def Theta(self,x,y):return np.asarray(y,np.longdouble)*self.F(x,y)
    def Omega(self,x,y):return np.asarray(x,np.longdouble)*np.asarray(y,np.longdouble)*self.G(x,y)

    def radial_modes(self,r,temperature=False):
        r=np.asarray(r,np.longdouble);logE=np.log1p((r/self.L)**2)
        q=-np.expm1(-self.mu*logE/2)
        powers=np.arange(1,2*self.NT,2) if temperature else np.arange(2,2*self.NO+1,2)
        c=self.cT if temperature else self.cO;gamma=self.gammaT if temperature else self.gammaO
        shape=(len(powers),)+(1,)*r.ndim
        rho=r/self.L*np.exp(-logE/2)
        return cheb_all(c,2*q-1)*rho[None,...]**powers.reshape(shape)*np.exp(gamma*logE/2)

    def modal_scaled(self,r):
        """Return psi_m/r^2 and psi_m'/r, with continuous values at r=0.

        J_in=int_0^1 v^(m+1) g_m(rv) dv.
        J_out=beta rho^(m-2) E^(gamma_O/2)
          * int_0^1 v^(beta(m-2)) Q_m(1-zv) dv, z=E^(-1/(2beta)).
        Outer quadrature is exact for the finite polynomial data in exact arithmetic.
        """
        r=np.asarray(r,np.longdouble)
        key=(r.shape,r.tobytes())
        if key in self.modal_cache:return self.modal_cache[key]
        flat=r.ravel();logE=np.log1p((flat/self.L)**2)
        rho=flat/self.L*np.exp(-logE/2);z=np.exp(-logE/(2*self.beta))
        p=[];d=[]
        for j in range(self.NO):
            m=2*(j+1)
            v,w=power_quadrature(self.radial_order,m+1)
            rv=flat[:,None]*v[None,:]
            lr=np.log1p((rv/self.L)**2);qr=-np.expm1(-self.mu*lr/2)
            gm=(rv/self.L*np.exp(-lr/2))**m*np.exp(self.gammaO*lr/2)*cheb_all(self.cO[j:j+1],2*qr-1)[0]
            jin=np.sum(gm*w,axis=1)
            vo,wo=power_quadrature(max(32,(self.K+1)//2+2),self.beta*(m-2))
            qo=1-z[:,None]*vo
            integ=np.sum(cheb_all(self.cO[j:j+1],2*qo-1)[0]*wo,axis=1)
            jout=self.beta*rho**(m-2)*np.exp(self.gammaO*logE/2)*integ
            p.append(((jin+jout)/(2*m)).reshape(r.shape))
            d.append(((jout-jin)/2).reshape(r.shape))
        result=np.array(p),np.array(d)
        if len(self.modal_cache)>600:self.modal_cache.clear()
        self.modal_cache[key]=result
        return result

    def H(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,np.longdouble),np.asarray(y,np.longdouble));r=np.hypot(x,y)
        angular=np.divide(x*x-y*y,r*r,out=np.ones_like(r),where=r!=0)
        p,_=self.modal_scaled(r)
        prev=np.zeros_like(r);cur=np.ones_like(r);result=np.zeros_like(r)
        for n in range(1,self.NO+1):
            result+=2*p[n-1]*cur
            prev,cur=cur,2*angular*cur-prev
        return result

    def Psi(self,x,y):return np.asarray(x,np.longdouble)*np.asarray(y,np.longdouble)*self.H(x,y)

    def U_modal(self,x,y):
        # Cartesian parity factors avoid catastrophic cancellation when a backward
        # trajectory approaches an axis exponentially faster than the origin.
        x,y=np.broadcast_arrays(np.asarray(x,np.longdouble),np.asarray(y,np.longdouble));r=np.hypot(x,y)
        c2=np.divide(x*x,r*r,out=np.ones_like(r),where=r!=0)
        s2=np.divide(y*y,r*r,out=np.zeros_like(r),where=r!=0)
        angle=c2-s2;p,d=self.modal_scaled(r)
        Tprev=np.ones_like(r);Tcur=angle.copy()
        Uprev=np.zeros_like(r);Ucur=np.ones_like(r)
        a=np.zeros_like(r);b=np.zeros_like(r)
        for n in range(1,self.NO+1):
            m=2*n
            a-=2*s2*d[n-1]*Ucur+m*p[n-1]*Tcur
            b+=2*c2*d[n-1]*Ucur-m*p[n-1]*Tcur
            Tprev,Tcur=Tcur,2*angle*Tcur-Tprev
            Uprev,Ucur=Ucur,2*angle*Ucur-Uprev
        return np.stack([x*a,y*b],axis=-1)
