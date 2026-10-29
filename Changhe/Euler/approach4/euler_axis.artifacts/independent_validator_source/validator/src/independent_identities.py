"""Finite-ball and characteristic diagnostics with explicit residual terms."""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import roots_legendre
from independent_pressure import geometric_edges,shell_nodes


def vorticity_and_jacobian(field,xyz):
    xyz=np.asarray(xyz,dtype=np.float64)
    x,y,z=np.moveaxis(xyz,-1,0);s=x*x+y*y
    p=field.phi.jet(s,z,3);q=field.q.jet(s,z,2)
    eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
    es=-12*p[2,0]-4*s*p[3,0]-p[1,2]
    ez=-8*p[1,1]-4*s*p[2,1]-p[0,3]
    omega=np.stack((-x*q[0,1]-y*eta,-y*q[0,1]+x*eta,2*q[0,0]+2*s*q[1,0]),axis=-1)
    J=np.empty(omega.shape+(3,),dtype=np.float64)
    J[...,0,0]=-q[0,1]-2*x*x*q[1,1]-2*x*y*es
    J[...,0,1]=-2*x*y*q[1,1]-eta-2*y*y*es
    J[...,0,2]=-x*q[0,2]-y*ez
    J[...,1,0]=-2*x*y*q[1,1]+eta+2*x*x*es
    J[...,1,1]=-q[0,1]-2*y*y*q[1,1]+2*x*y*es
    J[...,1,2]=-y*q[0,2]+x*ez
    J[...,2,0]=8*x*q[1,0]+4*x*s*q[2,0]
    J[...,2,1]=8*y*q[1,0]+4*y*s*q[2,0]
    J[...,2,2]=2*q[0,1]+2*s*q[1,1]
    return omega,J


def finite_ball_balance(field,pressure,R,*,nangle=48,nradial=24,residual_integrals=False):
    """pressure(r,z)->(P,[P_r,P_z]); supports vectorized arguments."""
    mu,w=roots_legendre(nangle);sin=np.sqrt(1-mu*mu)
    rr=R*sin;zz=R*mu
    xyz=np.stack((rr,np.zeros_like(rr),zz),axis=-1)
    U=field.cartesian(xyz);omega,_=vorticity_and_jacobian(field,xyz)
    P,_=pressure(rr,zz)
    e=np.sum(U*U,axis=-1)/2;h=np.sum(U*omega,axis=-1)
    normal=np.stack((sin,np.zeros_like(sin),mu),axis=-1)
    un=np.sum(U*normal,axis=-1);on=np.sum(omega*normal,axis=-1)
    eflux=2*np.pi*R*R*np.dot(w,(e+P)*un+field.c_l*R*e)
    hflux=2*np.pi*R*R*np.dot(w,h*(un+field.c_l*R)+(P-e)*on)
    rs,wr=shell_nodes(geometric_edges(R),nradial)
    r=rs[:,None]*sin[None,:];z=rs[:,None]*mu[None,:]
    xyz=np.stack((r,np.zeros_like(r),z),axis=-1)
    U,JU=field.cartesian(xyz,True);omega,JO=vorticity_and_jacobian(field,xyz)
    weights=2*np.pi*(wr*rs*rs)[:,None]*w[None,:]
    e=np.sum(U*U,axis=-1)/2;h=np.sum(U*omega,axis=-1)
    E=float(np.sum(weights*e));H=float(np.sum(weights*h))
    edef=eflux-(5*field.c_l-2)*E
    hdef=hflux-(4*field.c_l-2)*H
    result={'R':float(R),'energy':E,'helicity':H,'energy_flux':float(eflux),'helicity_flux':float(hflux),
            'energy_defect':float(edef),'helicity_defect':float(hdef),
            'energy_relative_defect':float(abs(edef)/(abs(eflux)+abs((5*field.c_l-2)*E)+1e-300)),
            'helicity_relative_defect':float(abs(hdef)/(abs(hflux)+abs((4*field.c_l-2)*H)+1e-300))}
    if residual_integrals:
        _,g=pressure(r,z)
        gp=np.stack((g[...,0],np.zeros_like(r),g[...,1]),axis=-1)
        W=field.c_l*xyz+U
        M=(1-field.c_l)*U+np.einsum('...ij,...j->...i',JU,W)+gp
        curlM=omega+np.einsum('...ij,...j->...i',JO,W)-np.einsum('...ij,...j->...i',JU,omega)
        ework=float(np.sum(weights*np.sum(U*M,axis=-1)))
        hwork=float(np.sum(weights*(np.sum(omega*M,axis=-1)+np.sum(U*curlM,axis=-1))))
        result.update(energy_residual_work=ework,helicity_residual_work=hwork,
                      energy_corrected_error=float(edef-ework),helicity_corrected_error=float(hdef-hwork))
    return result


def characteristic_balance(field,start,interval=(-4.,4.),*,rtol=1e-10,atol=1e-12):
    """Integrate the physical trajectory and the residual correction together."""
    start=np.asarray(start,dtype=np.float64)
    if start[0]<=0:
        raise ValueError('a positive initial cylindrical radius is required')
    k=1-2*field.c_l
    gamma0=float(start[0]**2*field.q.evaluate(start[0]**2,start[1]))
    results=[]
    for endpoint in interval:
        if endpoint==0:continue
        def rhs(t,state):
            r,z=state[:2]
            U=field.cylindrical(r,z,2)['U']
            residual=field.reduced(r,z)['gamma']
            return [field.c_l*r+U[0],field.c_l*z+U[2],np.exp(k*t)*residual]
        sol=solve_ivp(rhs,(0,float(endpoint)),[*start,0.],rtol=rtol,atol=atol,method='DOP853',dense_output=True,max_step=.15)
        times=np.linspace(0,endpoint,81)
        path=sol.sol(times)
        gamma=path[0]**2*field.q.evaluate(path[0]**2,path[1])
        invariant=np.exp(k*times)*gamma
        errors=invariant-gamma0-path[2]
        results.append({'endpoint':float(endpoint),'success':bool(sol.success),'nfev':sol.nfev,
                        'max_corrected_error':float(np.max(np.abs(errors))),
                        'max_uncorrected_change':float(np.max(np.abs(invariant-gamma0))),
                        'min_radius':float(np.min(path[0])),'max_spherical_radius':float(np.max(np.hypot(path[0],path[1]))),
                        'times':times.tolist(),'r':path[0].tolist(),'z':path[1].tolist(),'weighted_gamma':invariant.tolist(),
                        'integrated_residual':path[2].tolist()})
    return results
