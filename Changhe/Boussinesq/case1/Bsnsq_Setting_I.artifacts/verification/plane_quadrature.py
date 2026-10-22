"""Astra whole-plane quadrature, independent of the inherited modal solver.

Interior: target-centred rays ending on an origin-centred circle.
Exterior: origin-centred polar coordinates with an infinite rational map.
The far kernel is algebraically subtracted before floating-point evaluation.
No tail fit, finite-box boundary data, spectral mode projection, or solver imports.
All arrays fit in angular x radial panels; process one target at a time.
"""
from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss

@dataclass(frozen=True)
class Rule:
    radial: int = 80
    angular_panels: int = 24
    angular_order: int = 12
    outer_multiplier: float = 2.0
    outer_minimum: float = 2.0
    map_power: float = 6.0


def unit_gauss(n):
    x,w=leggauss(n)
    return (x+1)/2,w/2


def angle_gauss(panels,order):
    q,w=unit_gauss(order)
    width=2*np.pi/panels
    a=(width*(np.arange(panels)[:,None]+q)).ravel()
    weights=np.broadcast_to(width*w,(panels,order)).ravel()
    return a,weights


def log1pmx_over_square(z):
    """(log(1+z)-z)/z^2, continuously defined as -1/2 at zero."""
    z=np.asarray(z)
    out=np.empty_like(z)
    small=np.abs(z)<0.04
    s=z[small]
    # Alternating series n=2,...,14, Horner evaluated.
    t=np.full_like(s,-1/14)
    for n in range(13,1,-1):
        t=t*s+((-1)**(n+1))/n
    out[small]=t
    b=z[~small]
    out[~small]=(np.log1p(b)-b)/(b*b)
    return out


def evaluate(omega,points,rule=Rule()):
    """Return {velocity[N,2], psi[N], metadata}; omega must have A1 parity.

    omega accepts NumPy arrays. Values are required at arbitrary whole-plane points,
    including the actual exterior nodes. No derivative of omega is requested.
    """
    pts=np.atleast_2d(np.asarray(points,dtype=float))
    a,aw=angle_gauss(rule.angular_panels,rule.angular_order)
    ca,sa=np.cos(a),np.sin(a)
    q,qw=unit_gauss(rule.radial)
    omq=1-q
    result_u=[];result_p=[];max_r=0.0;min_r=float('inf')
    for x,y in pts:
        radius=np.hypot(x,y)
        R=max(rule.outer_minimum,rule.outer_multiplier*radius)
        if not R>radius:raise ValueError('the target must lie strictly inside the inner circle')
        xe=x*ca+y*sa
        L=-xe+np.sqrt(xe*xe+R*R-radius*radius)
        rho=L[:,None]*q[None,:]
        vals=np.asarray(omega(x+rho*ca[:,None],y+rho*sa[:,None]))
        inner_by_angle=np.sum(vals*(L[:,None]*qw),axis=1)
        u1=-np.sum(aw*sa*inner_by_angle)/(2*np.pi)
        u2=np.sum(aw*ca*inner_by_angle)/(2*np.pi)
        # Integrate the constant-density logarithmic singularity analytically.
        local=float(np.asarray(omega(np.asarray(x),np.asarray(y))))
        rem=np.sum((vals-local)*np.log(rho)*rho*(L[:,None]*qw),axis=1)
        const=local*(L*L/2)*(np.log(L)-0.5)
        psi=-np.sum(aw*(rem+const))/(2*np.pi)
        r=R*omq**(-rule.map_power)
        max_r=max(max_r,float(r[-1]));min_r=min(min_r,float(rho.min()))
        ex=ca[:,None];ey=sa[:,None]
        invr=1/r[None,:]
        xe2=xe[:,None]
        r2=radius*radius
        z=(-2*xe2+r2*invr)*invr
        denom=1+z
        num_x=x-2*ex*xe2+ex*r2*invr
        num_y=y-2*ey*xe2+ey*r2*invr
        outer_om=np.asarray(omega(ex*r[None,:],ey*r[None,:]))
        measure=rule.map_power*qw/omq
        weight=aw[:,None]*measure[None,:]*outer_om/(2*np.pi)
        u1+=np.sum(weight*num_y/denom)
        u2-=np.sum(weight*num_x/denom)
        # r^2[log|X-Y|-log|Y|+(X.Y)/|Y|^2], evaluated stably.
        scaled_log=0.5*(r2+(-2*xe2+r2*invr)**2*log1pmx_over_square(z))
        psi-=np.sum(weight*scaled_log)
        result_u.append([u1,u2]);result_p.append(psi)
    return {'velocity':np.array(result_u),'psi':np.array(result_p),
            'metadata':{'method':'target-ray interior plus algebraically subtracted infinite exterior',
            'rule':rule.__dict__,'largest_exterior_radius_sampled':max_r,
            'smallest_interior_ray_radius_sampled':min_r,
            'tail_model':None,'finite_outer_cutoff':None}}


def origin_strain(omega,rule=Rule(),radial_scale=1.0):
    """Psi_xy(0) from its full-plane moment, with no artificial inner/outer cutoff."""
    a,aw=angle_gauss(rule.angular_panels,rule.angular_order)
    q,w=unit_gauss(rule.radial)
    r=radial_scale*q/(1-q)**rule.map_power
    log_jac=1/q+rule.map_power/(1-q)
    ca,sa=np.cos(a),np.sin(a)
    vals=omega(ca[:,None]*r[None,:],sa[:,None]*r[None,:])
    return float(np.sum(aw[:,None]*(ca*sa)[:,None]*vals*(w*log_jac)[None,:])/np.pi)
