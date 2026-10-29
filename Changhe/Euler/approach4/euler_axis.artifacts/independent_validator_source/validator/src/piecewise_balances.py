"""Finite-ball identities with classical residual work and interface flux jumps."""
import numpy as np
from scipy.special import roots_legendre
from independent_pressure import geometric_edges,shell_nodes
from independent_identities import vorticity_and_jacobian


def trace_values(field,r,z,element=None):
    if element is None:
        p=field.phi.jet(r*r,z,2);q=field.q.jet(r*r,z,1)
    else:
        d=field.jets(r*r,z,2,element=element);p,q=d['phi'],d['q']
    s=r*r
    U=np.stack([-r*p[0,1],r*q[0,0],2*p[0,0]+2*s*p[1,0]],axis=-1)
    eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
    omega=np.stack([-r*q[0,1],r*eta,2*q[0,0]+2*s*q[1,0]],axis=-1)
    return U,omega


def pressure_spheres(pressure,radii,mu):
    radii=np.asarray(radii);mu=np.asarray(mu)
    if hasattr(pressure,"on_spheres"):return pressure.on_spheres(radii,mu)
    return pressure(radii[:,None]*np.sqrt(1-mu*mu)[None,:],radii[:,None]*mu[None,:])


def sphere_flux(field,pressure,R,mu,weights,element=None):
    sin=np.sqrt(1-mu*mu);r=R*sin;z=R*mu
    U,omega=trace_values(field,r,z,element)
    P,_=pressure_spheres(pressure,[R],mu);P=P[0]
    e=np.sum(U*U,axis=-1)/2;h=np.sum(U*omega,axis=-1)
    un=U[:,0]*sin+U[:,2]*mu;on=omega[:,0]*sin+omega[:,2]*mu
    factor=2*np.pi*R*R
    return np.array([factor*np.dot(weights,(e+P)*un+field.c_l*R*e),
                     factor*np.dot(weights,h*(un+field.c_l*R)+(P-e)*on)])


def piecewise_ball_balance(field,pressure,R,*,nangle=48,nradial=24):
    """Pressure callable must have continuous values at the interfaces.

    The external radius must avoid interfaces. The pressure gradient may jump.
    No interface contribution is hidden in a bulk source or residual norm.
    """
    interfaces=np.asarray(getattr(field,'interfaces',[]),dtype=float)
    if R<=0 or np.any(abs(interfaces-R)<1e-13*max(1.,R)):
        raise ValueError('use a positive non-interface radius')
    mu,w=roots_legendre(nangle);sin=np.sqrt(1-mu*mu)
    external=sphere_flux(field,pressure,R,mu,w)
    jump=np.zeros(2);details=[]
    for i,a in enumerate(interfaces):
        if a>=R:break
        inner=sphere_flux(field,pressure,a,mu,w,i)
        outer=sphere_flux(field,pressure,a,mu,w,i+1)
        contribution=outer-inner;jump+=contribution
        details.append(dict(radius=float(a),inner_energy_flux=float(inner[0]),outer_energy_flux=float(outer[0]),
                            energy_jump=float(contribution[0]),helicity_jump=float(contribution[1])))
    edges=np.unique(np.r_[geometric_edges(R,field.phi.length),interfaces[interfaces<R]])
    rs,wr=shell_nodes(edges,nradial)
    r=rs[:,None]*sin[None,:];z=rs[:,None]*mu[None,:]
    xyz=np.stack([r,np.zeros_like(r),z],axis=-1)
    U,JU=field.cartesian(xyz,True);omega,JO=vorticity_and_jacobian(field,xyz)
    _,gradient=pressure_spheres(pressure,rs,mu)
    gp=np.stack([gradient[...,0],np.zeros_like(r),gradient[...,1]],axis=-1)
    W=field.c_l*xyz+U
    M=(1-field.c_l)*U+np.einsum('...ij,...j->...i',JU,W)+gp
    curlM=omega+np.einsum('...ij,...j->...i',JO,W)-np.einsum('...ij,...j->...i',JU,omega)
    weight=2*np.pi*(wr*rs*rs)[:,None]*w[None,:]
    E=float(np.sum(weight*np.sum(U*U,axis=-1)/2));H=float(np.sum(weight*np.sum(U*omega,axis=-1)))
    ew=float(np.sum(weight*np.sum(U*M,axis=-1)))
    hw=float(np.sum(weight*(np.sum(omega*M,axis=-1)+np.sum(U*curlM,axis=-1))))
    ed=float(external[0]-(5*field.c_l-2)*E);hd=float(external[1]-(4*field.c_l-2)*H)
    return dict(R=float(R),energy=E,helicity=H,energy_flux=float(external[0]),helicity_flux=float(external[1]),
                energy_defect=ed,helicity_defect=hd,energy_residual_work=ew,helicity_residual_work=hw,
                energy_interface_jump=float(jump[0]),helicity_interface_jump=float(jump[1]),
                energy_corrected_error=ed-ew-float(jump[0]),helicity_corrected_error=hd-hw-float(jump[1]),
                interfaces=details,volume_quadrature_points=int(weight.size))
