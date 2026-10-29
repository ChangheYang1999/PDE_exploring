"""Interface-split full-space pressure and explicit stress surface corrections.

The derivation and signs are recorded in research/interface_pressure/PROOF.md.
All quadrature includes an infinite exterior. No candidate P values are inputs.
"""
from __future__ import annotations
from functools import lru_cache
import numpy as np
from scipy.special import roots_legendre, roots_jacobi, eval_legendre, ellipk
from numpy.polynomial import Legendre
from independent_pressure import GreenPoisson,DirectNewtonPressure,geometric_edges,shell_nodes

class InterfaceGreenPoisson(GreenPoisson):
    def __init__(self,source,*,interfaces=(),**kwargs):
        super().__init__(source,**kwargs)
        self.interfaces=np.asarray(interfaces,dtype=float)
        if np.any(self.interfaces<=0):raise ValueError('interfaces must be positive')
    def edges(self,upper):
        return np.unique(np.r_[geometric_edges(upper,self.scale),self.interfaces[self.interfaces<upper]])
    def _integrated_outer(self,R,cutoff):
        edges=self.edges(cutoff);edges=np.r_[float(R),edges[edges>R]]
        s,w=shell_nodes(edges,self.nradial);f=self.source_coefficients(s)
        kernel=(R/s[:,None])**self.ell if R else np.zeros((len(s),self.lmax+1))
        if R==0:kernel[:,0]=1.
        outer=np.sum(w[:,None]*s[:,None]*f*kernel,axis=0)
        t=self.tail_t;f=self.source_coefficients(cutoff/t)
        factored=f/t[:,None]**(self.decay_power+2)
        pref=(R/cutoff)**self.ell if R else np.r_[1.,np.zeros(self.lmax)]
        return outer+cutoff**2*pref*np.sum(self.tail_w[:,None]*t[:,None]**self.ell*factored,axis=0)
    @lru_cache(maxsize=4096)
    def panel_moments(self,lower,upper):
        # Normalize each radial power on its own panel. Only the two panels
        # cut by a new target radius require fresh source evaluations.
        x,w=roots_legendre(self.nradial)
        s=(lower+upper)/2+(upper-lower)*x/2;w=w*(upper-lower)/2
        f=self.source_coefficients(s)
        inner=np.sum(w[:,None]*s[:,None]*f*(s[:,None]/upper)**(self.ell+self.dimension-2),axis=0)
        kernel=(lower/s[:,None])**self.ell if lower else np.zeros((len(s),self.lmax+1))
        if not lower:kernel[:,0]=1.
        outer=np.sum(w[:,None]*s[:,None]*f*kernel,axis=0)
        return inner,outer
    @lru_cache(maxsize=64)
    def tail_moments(self,cutoff):
        t=self.tail_t;f=self.source_coefficients(cutoff/t)
        return cutoff**2*np.sum(self.tail_w[:,None]*t[:,None]**self.ell*f/t[:,None]**(self.decay_power+2),axis=0)
    @lru_cache(maxsize=256)
    def radial(self,R):
        R=float(R)
        if R<0:raise ValueError('negative radius')
        denom=2*self.ell+self.dimension-2
        requested=max(self.tail_factor*self.scale,16*R,2*max(self.interfaces,default=0.))
        cutoff=self.scale*2.**np.ceil(np.log2(requested/self.scale))
        if R==0:
            value=np.zeros(self.lmax+1);derivative=np.zeros_like(value)
            value[0]=self._integrated_outer(0,cutoff)[0]/(self.dimension-2)
            if self.lmax:
                s,w=shell_nodes(self.edges(cutoff),self.nradial);f=self.source_coefficients(s)
                integral=np.sum(w*f[:,1]);t=self.tail_t;ft=self.source_coefficients(cutoff/t)[:,1]
                integral+=cutoff*np.sum(self.tail_w*ft/t**(self.decay_power+1))
                derivative[1]=integral/self.dimension
            return value,derivative
        edges=np.unique(np.r_[self.edges(cutoff),R]);inner=np.zeros(self.lmax+1);outer=np.zeros_like(inner)
        for lower,upper in zip(edges[:-1],edges[1:]):
            im,om=self.panel_moments(float(lower),float(upper))
            if upper<=R:inner+=im*(upper/R)**(self.ell+self.dimension-2)
            else:outer+=om*(R/lower)**self.ell
        outer+=self.tail_moments(float(cutoff))*(R/cutoff)**self.ell
        return (inner+outer)/denom,(-(self.ell+self.dimension-2)*inner+self.ell*outer)/(denom*R)


def interface_trace(field,element,r,z):
    """One-sided U, DU and convection in the cylindrical orthonormal frame."""
    data=field.jets(r*r,z,2,element=element);p,q=data['phi'],data['q'];s=r*r
    ur=-r*p[0,1];ut=r*q[0,0];uz=2*p[0,0]+2*s*p[1,0]
    urr=-p[0,1]-2*s*p[1,1];urz=-r*p[0,2]
    utr=q[0,0]+2*s*q[1,0];utz=r*q[0,1]
    uzr=8*r*p[1,0]+4*r*s*p[2,0];uzz=2*p[0,1]+2*s*p[1,1]
    V=np.stack([ur*urr+uz*urz-r*q[0,0]**2,
                ur*utr+uz*utz-p[0,1]*ut,ur*uzr+uz*uzz],axis=-1)
    return np.stack([ur,ut,uz],axis=-1),V


def stress_surface_coefficients(field,lmax,nangle):
    mu,w=roots_legendre(nangle);theta=np.sqrt(1-mu*mu)
    P=np.stack([eval_legendre(l,mu) for l in range(lmax+1)],axis=1)
    DP=np.stack([Legendre.basis(l).deriv()(mu) for l in range(lmax+1)],axis=1)
    norm=(2*np.arange(lmax+1)+1)/2;project=w[:,None]*P*norm;dproject=w[:,None]*DP*norm
    rows=[]
    for i,a in enumerate(field.interfaces):
        traces=[interface_trace(field,k,a*theta,a*mu) for k in [i,i+1]]
        Un=[U[:,0]*theta+U[:,2]*mu for U,V in traces]
        J=traces[1][0]*Un[1][:,None]-traces[0][0]*Un[0][:,None]
        F=(traces[1][1][:,0]-traces[0][1][:,0])*theta+(traces[1][1][:,2]-traces[0][1][:,2])*mu
        JR=J[:,0]*theta+J[:,2]*mu
        rows.append(dict(radius=float(a),F=F@project,J=JR@project,D=-(J[:,2]-mu*JR)@dproject))
    return rows

class InterfaceStressPressure(InterfaceGreenPoisson):
    def __init__(self,field,**kwargs):
        if kwargs.get('dimension',3)!=3:raise ValueError('stress pressure is three-dimensional')
        super().__init__(field.source,interfaces=field.interfaces,**kwargs)
        self.surfaces=stress_surface_coefficients(field,self.lmax,self.nangle)
    @lru_cache(maxsize=256)
    def radial(self,R):
        R=float(R);p,dp=super().radial(R);p=p.copy();dp=dp.copy();l=self.ell
        for s in self.surfaces:
            a=s['radius']
            if R<=a:
                amplitude=(a*s['F']+(l+1)*s['J']+s['D'])/(2*l+1)
                v=(R/a)**l*amplitude
                if R:d=l/R*v
                else:
                    d=np.zeros_like(p)
                    if self.lmax:d[1]=amplitude[1]/a
            else:
                amplitude=(a*s['F']-l*s['J']+s['D'])/(2*l+1)
                v=(a/R)**(l+1)*amplitude;d=-(l+1)/R*v
            p+=v;dp+=d
        return p,dp
    def bulk_radial(self,R):return super().radial(float(R))

class DirectInterfaceNewton(DirectNewtonPressure):
    """Direct Newton value with every radial interface included as a split."""
    def __init__(self,source,*,interfaces=(),**kwargs):
        super().__init__(source,**kwargs);self.interfaces=np.asarray(interfaces,dtype=float)
    def evaluate(self,r,z):
        r,z=float(r),float(z);R=float(np.hypot(r,z))
        cutoff=max(self.cutoff*self.scale,16*R,2*max(self.interfaces,default=0.))
        edges=np.unique(np.r_[geometric_edges(cutoff,self.scale),self.interfaces[self.interfaces<cutoff],R])
        s,ws=shell_nodes(edges,self.nradial)
        x,w=roots_jacobi(self.nradial,0,self.decay_power-1);t=(x+1)/2
        s=np.r_[s,cutoff/t];ws=np.r_[ws,cutoff*w/(2**self.decay_power)*t**(-self.decay_power-1)]
        if r==0 and R>0:
            u,wu=shell_nodes(np.array([0.,np.sqrt(2.)]),self.nangle);sign=1. if z>0 else -1.
            mu=sign*(1-u*u);sr=s[:,None]*np.sqrt(np.maximum(0.,1-mu[None,:]**2));sz=s[:,None]*mu[None,:]
            f=self.source(sr,sz);pole=self.source(np.zeros_like(s),sign*s)
            den=np.sqrt((s[:,None]-R)**2+2*s[:,None]*R*u[None,:]**2)
            angular=2*pole/np.maximum(s,R)+np.sum(2*u[None,:]*wu[None,:]*(f-pole[:,None])/den,axis=1)
            return float(.5*np.sum(ws*s*s*angular))
        mu_edges=np.array([-1.,1.]) if not R else np.unique(np.array([-1.,z/R,1.]))
        mu,wmu=shell_nodes(mu_edges,self.nangle);sr=s[:,None]*np.sqrt(1-mu[None,:]**2);sz=s[:,None]*mu[None,:]
        den=(r+sr)**2+(z-sz)**2;m=4*r*sr/den
        kernel=ellipk(np.minimum(m,1-np.finfo(float).eps))/np.sqrt(den)
        return float(np.sum(ws[:,None]*s[:,None]**2*wmu[None,:]*self.source(sr,sz)*kernel)/np.pi)
