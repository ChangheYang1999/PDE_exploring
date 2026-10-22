"""Whole-plane velocity by a Gaussian split, with origin annuli resolving all scales.

The target-centered Gaussian piece removes the kernel singularity. The remainder
is smooth at the target and integrated on origin-centered geometric annuli plus
an infinite mapped tail. Kernel subtraction is algebraic in the far field.
This is an independent physical-space quadrature, not a modal inverse.
"""
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
from scipy.special import roots_genlaguerre
from plane_quadrature import unit_gauss,angle_gauss

@dataclass(frozen=True)
class GaussianRule:
    radial: int=24
    angular_panels: int=24
    angular_order: int=12
    gaussian_order: int=48
    local_fraction: float=.2
    first_radius: float=.125
    annulus_ratio: float=4.
    outer_minimum: float=16.
    outer_multiplier: float=2.
    map_power: float=6.

@lru_cache(maxsize=16)
def local_gauss(n):
    t,w=roots_genlaguerre(n,0.)
    return np.sqrt(t),w


def evaluate_velocity(omega,points,rule=GaussianRule()):
    pts=np.atleast_2d(np.asarray(points,float));angles,aw=angle_gauss(rule.angular_panels,rule.angular_order)
    ex=np.cos(angles)[:,None];ey=np.sin(angles)[:,None]
    q,qw=unit_gauss(rule.radial);lg,lw=local_gauss(rule.gaussian_order)
    values=[];records=[]
    for x,y in pts:
        radius=np.hypot(x,y);ell=rule.local_fraction*max(1.,radius)
        # Pair opposite rays before radial integration. The odd difference divided
        # by rho is smooth in rho^2, so ordinary Laguerre avoids a sqrt(t) endpoint.
        plus=omega(x+ell*ex*lg,y+ell*ey*lg)
        minus=omega(x-ell*ex*lg,y-ell*ey*lg)
        local_values=(plus-minus)/(2*ell*lg)
        average=np.sum(local_values*lw,axis=1)
        u1=-ell**2*np.sum(aw*np.sin(angles)*average)/(4*np.pi)
        u2=ell**2*np.sum(aw*np.cos(angles)*average)/(4*np.pi)
        end=max(rule.outer_minimum,rule.outer_multiplier*radius)
        edges=[rule.first_radius]
        while edges[-1]<end:edges.append(edges[-1]*rule.annulus_ratio)
        panels=[(edges[0]*q,qw/q)]
        for lo,hi in zip(edges[:-1],edges[1:]):
            length=np.log(hi/lo);panels.append((lo*np.exp(length*q),length*qw))
        panels.append((edges[-1]/(1-q)**rule.map_power,rule.map_power*qw/(1-q)))
        for radial,weight in panels:
            r=radial[None,:];xx=ex*r;yy=ey*r
            dx=x-xx;dy=y-yy;d2=dx*dx+dy*dy
            wlocal=np.exp(-d2/ell**2)
            soft=np.divide(-np.expm1(-d2/ell**2),d2,out=np.full_like(d2,1/ell**2),where=d2!=0)
            kx=r*r*soft*dy+yy
            ky=-r*r*soft*dx-xx
            far=radial>2*radius if radius else np.ones(len(radial),bool)
            if np.any(far):
                rf=r[:,far];xe=x*ex+y*ey;r2=radius*radius
                zz=(-2*xe+r2/rf)/rf;den=1+zz
                nx=x-2*ex*xe+ex*r2/rf;ny=y-2*ey*xe+ey*r2/rf
                factor=wlocal[:,far]*rf*rf/d2[:,far]
                kx[:,far]=ny/den-factor*dy[:,far]
                ky[:,far]=-nx/den+factor*dx[:,far]
            density=omega(xx,yy);measure=aw[:,None]*weight[None,:]/(2*np.pi)
            u1+=np.sum(measure*density*kx);u2+=np.sum(measure*density*ky)
        values.append([u1,u2]);records.append({'finite_annuli':len(edges),'last_finite_radius':edges[-1],'largest_exterior_node':float(panels[-1][0][-1]),'local_gaussian_scale':ell})
    return {'velocity':np.asarray(values),'metadata':{'method':'target Gaussian singularity split, origin geometric annuli, infinite exterior','rule':rule.__dict__,'targets':records,'finite_outer_cutoff':None,'fitted_tail':None}}
