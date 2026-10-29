"""Full-space spherical Green inverses, with no finite-radius boundary data.

Dimension 3 uses Legendre modes and computes pressure. Dimension 5 uses
Gegenbauer C_l^(3/2) and computes the stream potential from eta. All quadrature
uses float64, finite geometric shells, and an integrated infinite exterior.
"""
from __future__ import annotations
from functools import lru_cache
import numpy as np
from scipy.special import roots_legendre, roots_jacobi, eval_gegenbauer, ellipk


def geometric_edges(upper, scale=1.0):
    if upper <= 0:
        return np.array([0.0])
    values=[0.0]
    x=scale/16
    while x < upper:
        values.append(x)
        x*=2
    values.append(float(upper))
    return np.array(values)


def shell_nodes(edges,n):
    x,w=roots_legendre(n)
    a,b=np.asarray(edges[:-1]),np.asarray(edges[1:])
    if len(a)==0:
        return np.empty(0),np.empty(0)
    return ((a[:,None]+b[:,None])/2+(b-a)[:,None]*x/2).ravel(),((b-a)[:,None]*w/2).ravel()


class GreenPoisson:
    def __init__(self,source,*,dimension=3,decay_power=1.0,lmax=16,nangle=48,nradial=32,scale=1.0,tail_factor=32):
        if dimension not in (3,5):
            raise ValueError("only dimensions 3 and 5 are implemented")
        if decay_power<=0 or nangle<=lmax or nradial<4:
            raise ValueError("invalid quadrature parameters")
        self.source=source
        self.dimension=dimension
        self.decay_power=float(decay_power)
        self.lmax=int(lmax)
        self.nangle=int(nangle)
        self.nradial=int(nradial)
        self.scale=float(scale)
        self.tail_factor=float(tail_factor)
        self.ell=np.arange(lmax+1,dtype=np.float64)
        self.lam=(dimension-2)/2
        wexp=(dimension-3)/2
        self.mu,self.wmu=roots_jacobi(nangle,wexp,wexp)
        self.angular=np.stack([eval_gegenbauer(l,self.lam,self.mu) for l in range(lmax+1)],axis=1)
        norms=np.sum(self.wmu[:,None]*self.angular**2,axis=0)
        self.projector=self.wmu[:,None]*self.angular/norms
        x,w=roots_jacobi(nradial,0,self.decay_power-1)
        self.tail_t=(x+1)/2
        self.tail_w=w/(2**self.decay_power)

    def source_coefficients(self,radii):
        radii=np.asarray(radii,dtype=np.float64).reshape(-1)
        r=radii[:,None]*np.sqrt(1-self.mu**2)[None,:]
        z=radii[:,None]*self.mu[None,:]
        values=np.asarray(self.source(r,z),dtype=np.float64)
        return values@self.projector

    def _integrated_outer(self,R,cutoff):
        edges=geometric_edges(cutoff,self.scale)
        edges=np.r_[float(R),edges[edges>R]]
        s,w=shell_nodes(edges,self.nradial)
        f=self.source_coefficients(s)
        kernel=(R/s[:,None])**self.ell if R else np.zeros((len(s),self.lmax+1))
        if R==0:
            kernel[:,0]=1
        outer=np.sum(w[:,None]*s[:,None]*f*kernel,axis=0)
        t=self.tail_t
        f=self.source_coefficients(cutoff/t)
        factored=f/t[:,None]**(self.decay_power+2)
        pref=(R/cutoff)**self.ell if R else np.r_[1.,np.zeros(self.lmax)]
        tail=cutoff**2*pref*np.sum(self.tail_w[:,None]*t[:,None]**self.ell*factored,axis=0)
        return outer+tail

    @lru_cache(maxsize=256)
    def radial(self,R):
        R=float(R)
        if R<0:
            raise ValueError("negative spherical radius")
        denom=2*self.ell+self.dimension-2
        cutoff=max(self.tail_factor*self.scale,16*R)
        if R==0:
            value=np.zeros(self.lmax+1)
            derivative=np.zeros_like(value)
            value[0]=self._integrated_outer(0,cutoff)[0]/(self.dimension-2)
            # At the origin only the linear angular mode contributes to gradient.
            if self.lmax>=1:
                s,w=shell_nodes(geometric_edges(cutoff,self.scale),self.nradial)
                f=self.source_coefficients(s)
                integral=np.sum(w*f[:,1])
                t=self.tail_t
                ft=self.source_coefficients(cutoff/t)[:,1]
                integral+=cutoff*np.sum(self.tail_w*ft/t**(self.decay_power+1))
                derivative[1]=integral/self.dimension
            return value,derivative
        s,w=shell_nodes(geometric_edges(R,self.scale),self.nradial)
        f=self.source_coefficients(s)
        inner=np.sum(w[:,None]*s[:,None]*f*(s[:,None]/R)**(self.ell+self.dimension-2),axis=0)
        outer=self._integrated_outer(R,cutoff)
        value=(inner+outer)/denom
        derivative=(-(self.ell+self.dimension-2)*inner+self.ell*outer)/(denom*R)
        return value,derivative

    def on_spheres(self,radii,mu):
        radii=np.asarray(radii,dtype=np.float64).reshape(-1)
        mu=np.asarray(mu,dtype=np.float64).reshape(-1)
        A=np.stack([eval_gegenbauer(l,self.lam,mu) for l in range(self.lmax+1)])
        D=np.zeros_like(A)
        for l in range(1,self.lmax+1):
            D[l]=2*self.lam*eval_gegenbauer(l-1,self.lam+1,mu)
        vals=[]
        drs=[]
        dzs=[]
        for R in radii:
            p,pR=self.radial(float(R))
            vals.append(p@A)
            if R==0:
                drs.append(np.zeros_like(mu))
                dzs.append(np.full_like(mu,(self.dimension-2)*pR[1] if self.lmax>=1 else 0.0))
            else:
                radial=pR@A
                angular=p@D/R
                drs.append(np.sqrt(1-mu**2)*(radial-mu*angular))
                dzs.append(mu*radial+(1-mu**2)*angular)
        return np.array(vals),np.stack((drs,dzs),axis=-1)

    def evaluate(self,r,z):
        r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64))
        shape=r.shape
        values=np.empty(r.size)
        gradients=np.empty((r.size,2))
        for k,(rr,zz) in enumerate(zip(r.ravel(),z.ravel())):
            R=float(np.hypot(rr,zz))
            mu=zz/R if R else 0.0
            v,g=self.on_spheres([R],[mu])
            values[k],gradients[k]=v[0,0],g[0,0]
        return values.reshape(shape),gradients.reshape(shape+(2,))


class DirectNewtonPressure:
    """Independent cylindrical Newton integral; azimuth is integrated by K(m).

    This is used only for selected pressure-value checks. It has no harmonic
    expansion. Splitting radial/angular intervals at the evaluation point
    places the integrable kernel singularity at quadrature-cell corners.
    """
    def __init__(self,source,*,decay_power=1.0,nradial=64,nangle=96,scale=1.0,cutoff=64):
        self.source=source
        self.decay_power=decay_power
        self.nradial=nradial
        self.nangle=nangle
        self.scale=scale
        self.cutoff=cutoff

    def evaluate(self,r,z):
        r,z=float(r),float(z)
        R=float(np.hypot(r,z))
        cutoff=max(self.cutoff*self.scale,16*R)
        edges=geometric_edges(cutoff,self.scale)
        if R and R<cutoff:
            edges=np.unique(np.r_[edges,R])
        s,ws=shell_nodes(edges,self.nradial)
        x,w=roots_jacobi(self.nradial,0,self.decay_power-1)
        t=(x+1)/2
        # For source ~s^(-p-2), measure*kernel behaves s^(-p-1).
        st=cutoff/t
        wt=cutoff*w/(2**self.decay_power)*t**(-self.decay_power-1)
        s=np.r_[s,st]
        ws=np.r_[ws,wt]
        if r == 0 and R > 0:
            # At an axial target remove the endpoint singularity analytically.
            # The constant angular kernel integrates to 2/max(s,R). The
            # remaining source vanishes quadratically in u=sqrt(1-sign(z)*mu).
            u,wu=shell_nodes(np.array([0.,np.sqrt(2.)]),self.nangle)
            sign=1. if z>0 else -1.
            mu=sign*(1-u*u)
            sr=s[:,None]*np.sqrt(np.maximum(0.,1-mu[None,:]**2))
            sz=s[:,None]*mu[None,:]
            f=self.source(sr,sz)
            pole=self.source(np.zeros_like(s),sign*s)
            den=np.sqrt((s[:,None]-R)**2+2*s[:,None]*R*u[None,:]**2)
            angular=2*pole/np.maximum(s,R)+np.sum(2*u[None,:]*wu[None,:]*(f-pole[:,None])/den,axis=1)
            return float(.5*np.sum(ws*s*s*angular))
        mu_edges=np.array([-1.,1.]) if not R else np.unique(np.array([-1.,z/R,1.]))
        mu,wmu=shell_nodes(mu_edges,self.nangle)
        sr=s[:,None]*np.sqrt(1-mu[None,:]**2)
        sz=s[:,None]*mu[None,:]
        den=(r+sr)**2+(z-sz)**2
        m=4*r*sr/den
        kernel=ellipk(np.minimum(m,1-np.finfo(np.float64).eps))/np.sqrt(den)
        f=self.source(sr,sz)
        return float(np.sum(ws[:,None]*s[:,None]**2*wmu[None,:]*f*kernel)/np.pi)

    def finite_difference_gradient(self,r,z,relative_steps=(.01,.003,.001)):
        """Independent fourth-order derivatives of the direct Newton value.

        Smooth even extension in r is used at the rotation axis. The complete
        step sequence is retained; its last value is not an error bound.
        """
        r,z=float(r),float(z)
        scale=max(self.scale,float(np.hypot(r,z)))
        rows=[]
        for factor in relative_steps:
            h=float(factor)*scale
            def value(a,b):return self.evaluate(abs(a),b)
            radial=(-value(r+2*h,z)+8*value(r+h,z)-8*value(r-h,z)+value(r-2*h,z))/(12*h) if r else 0.
            axial=(-value(r,z+2*h)+8*value(r,z+h)-8*value(r,z-h)+value(r,z-2*h))/(12*h)
            rows.append({'h':h,'gradient':[radial,axial]})
        return rows
