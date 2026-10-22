"""Adaptive radial canonical inverse, independent of fit code and inverse matrices.

This is a third check alongside the primary physical-space Duffy method.
Exact identities: research/inverse/adaptive_modal/PROOF.md.
"""
import numpy as np
from scipy.integrate import quad_vec
from numpy.polynomial.chebyshev import chebval


class CoefficientModes:
    def __init__(self,profile):
        self.p=profile
        self.frequencies=2*np.arange(1,len(profile.cg)+1)

    def __call__(self,r):
        p=self.p
        if r<=0:return np.zeros(len(self.frequencies))
        logq=2*np.log(r/p.length)
        logden=np.logaddexp(0.0,logq)
        rho2=np.exp(logq-logden)
        if p.mapname=='xi':
            arg=1-2*np.exp(-logden)
            logscale=logq-p.sigma_g*logden+p.sigma_g*np.log(2)
        else:
            arg=2*np.exp(-logden/(2*p.beta_map))-1
            logscale=logq-p.sigma_g*logden
        # The r^2 multiplier is combined with the decaying envelope in logs.
        g=(p.length**2*np.exp(logscale))*rho2**np.arange(len(p.cg))*chebval(arg,p.cg.T)
        b=np.zeros(len(g))
        for ell,v in enumerate(g):
            b[ell]+=v/4
            if 1-ell>0:b[0]+=v/4
            elif 1-ell<0:b[ell-2]-=v/4
        return b


def radial_integrals(modes,r,tail_power,tolerance=1e-10):
    n=np.asarray(modes.frequencies)
    exponent=1/tail_power
    inside=lambda s:s**(n+1)*modes(r*s)
    def outside(t):
        s=t**exponent
        return exponent*t**(exponent*(n-2)-1)*modes(r/s)
    settings=dict(epsabs=tolerance,epsrel=tolerance,norm='max',limit=2000,
                  workers=1,quadrature='gk21',full_output=True,cache_size=16000000)
    a,ea,ia=quad_vec(inside,0,1,**settings)
    b,eb,ib=quad_vec(outside,0,1,**settings)
    info=dict(error_inside=float(ea),error_outside=float(eb),
              success=bool(ia.success and ib.success),
              status_inside=int(ia.status),status_outside=int(ib.status),
              message_inside=ia.message,message_outside=ib.message,
              neval_inside=int(ia.neval),neval_outside=int(ib.neval),
              intervals_inside=len(ia.intervals),intervals_outside=len(ib.intervals))
    return a,b,info


def at_radius(modes,r,tail_power,tolerance=1e-10):
    n=np.asarray(modes.frequencies)
    a,b,info=radial_integrals(modes,r,tail_power,tolerance)
    return dict(psi=r*r*(a+b)/(2*n),psi_r=r*(-a+b)/2,
                sigma=float(r*np.sum(a+b)/2),
                sigma_prime=float(np.sum(-(n+1)*a+(n-1)*b)/2),info=info)


def velocity(modes,points,tail_power,tolerance=1e-10):
    points=np.asarray(points,float);u=np.zeros_like(points);infos=[]
    for i,(x,y) in enumerate(points):
        r=float(np.hypot(x,y))
        if r==0:
            infos.append(dict(origin=True));continue
        ph=np.arctan2(y,x);v=at_radius(modes,r,tail_power,tolerance)
        n=np.asarray(modes.frequencies)
        ur=-np.sum(n*v['psi']*np.cos(n*ph))/r
        up=np.sum(v['psi_r']*np.sin(n*ph))
        u[i]=[ur*np.cos(ph)-up*np.sin(ph),ur*np.sin(ph)+up*np.cos(ph)]
        # Exact symmetry of the finite sine series, not a denominator floor.
        if x==0:u[i,0]=0.0
        if y==0:u[i,1]=0.0
        infos.append(v['info'])
    return u,infos
