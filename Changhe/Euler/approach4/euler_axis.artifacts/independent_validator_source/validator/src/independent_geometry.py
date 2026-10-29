"""Independent core-scale estimates and physical shell quadratures.

Extrema are finite numerical searches. No completeness or rigorous global
bound is inferred from them.
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import minimize, minimize_scalar, brentq
from scipy.special import roots_legendre
from independent_identities import vorticity_and_jacobian
from independent_tail_audit import leading_coefficients
from independent_farfield import angular_data,evaluate_vector


def omega_squared(field,r,z):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64))
    s=r*r;p=field.phi.jet(s,z,2);q=field.q.jet(s,z,1)
    eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
    return r*r*(q[0,1]**2+eta**2)+(2*q[0,0]+2*s*q[1,0])**2


def angular_vorticity_maximum(field,R,nangle=129):
    theta=np.linspace(0.,np.pi,nangle)
    values=omega_squared(field,R*np.sin(theta),R*np.cos(theta))
    records=[(float(values[0]),0.),(float(values[-1]),float(np.pi))]
    for i in np.flatnonzero((values[1:-1]>=values[:-2]) & (values[1:-1]>=values[2:]) & ((values[1:-1]>values[:-2]) | (values[1:-1]>values[2:])) & (values[1:-1]>0))+1:
        fit=minimize_scalar(lambda t:-float(omega_squared(field,R*np.sin(t),R*np.cos(t))),
                            bounds=(theta[i-1],theta[i+1]),method='bounded',options={'xatol':1e-12})
        records.append((-float(fit.fun),float(fit.x)))
    value,angle=max(records)
    return np.sqrt(max(value,0.)),angle


def core_scale(field,*,nradial=101,nangle=129,starts=12,minimum_power=-12,maximum_power=14):
    scale=max(field.phi.length,field.q.length)
    logs=np.linspace(minimum_power*np.log(2.),maximum_power*np.log(2.),nradial)+np.log(scale)
    radii=np.exp(logs);angles=np.linspace(0.,np.pi,nangle)
    r=radii[:,None]*np.sin(angles);z=radii[:,None]*np.cos(angles)
    values=omega_squared(field,r,z)
    candidates=[]
    # Distinct grid-local maxima prevent every start landing on one peak.
    for i in range(nradial):
        for j in range(nangle):
            block=values[max(0,i-1):min(nradial,i+2),max(0,j-1):min(nangle,j+2)]
            if values[i,j]>=np.max(block):candidates.append((float(values[i,j]),i,j))
    candidates.sort(reverse=True)
    def obj(v):
        R=np.exp(v[0]);t=v[1];rr=R*np.sin(t);zz=R*np.cos(t)
        o,J=vorticity_and_jacobian(field,np.array([rr,0.,zz]))
        dr,dz=(2*o@J)[[0,2]]
        grad=np.array([dr*rr+dz*zz,dr*zz-dz*rr])
        return -float(o@o),-grad
    found=[]
    for _,i,j in candidates[:starts]:
        fit=minimize(obj,[logs[i],angles[j]],jac=True,method='L-BFGS-B',
                     bounds=[(logs[0],logs[-1]),(0.,np.pi)],options={'ftol':1e-15,'gtol':1e-12,'maxiter':200})
        R=float(np.exp(fit.x[0]));theta=float(fit.x[1])
        found.append({'point_r_z':[R*np.sin(theta),R*np.cos(theta)],'R':R,'theta':theta,
                      'vorticity_norm':float(np.sqrt(max(0.,-fit.fun))),'success':bool(fit.success)})
    origin=float(np.sqrt(omega_squared(field,0.,0.)))
    found.append({'point_r_z':[0.,0.],'R':0.,'theta':0.,'vorticity_norm':origin,'success':True})
    best=max(found,key=lambda v:v['vorticity_norm']);peak=best['vorticity_norm']
    if not np.isfinite(peak) or peak<=0:raise ValueError('no positive finite vorticity core scale')
    envelope=[]
    for R in radii:
        value,angle=angular_vorticity_maximum(field,float(R),nangle)
        envelope.append(value)
    envelope=np.asarray(envelope);hit=np.flatnonzero(envelope>=peak/2)
    if len(hit)==0:raise ValueError('half-maximum radius is below the resolved radial scan')
    last=int(hit[-1]);outer_resolved=last<len(radii)-1
    if outer_resolved:
        def half(logR):return angular_vorticity_maximum(field,float(np.exp(logR)),nangle)[0]-peak/2
        root=brentq(half,logs[last],logs[last+1],xtol=2e-12,rtol=2e-12)
        a=float(np.exp(root));halfcheck,halftheta=angular_vorticity_maximum(field,a,nangle)
    else:a=None;halfcheck=None;halftheta=None
    return {'a_eff':a,'max_vorticity':peak,'maximum_point_r_z':best['point_r_z'],
            'maximum_search_boundary':bool(best['R']>=.999*radii[-1]),
            'outer_half_radius_resolved':outer_resolved,'half_radius_value':halfcheck,'half_radius_theta':halftheta,
            'search_radii':radii.tolist(),'shell_maxima':envelope.tolist(),'local_searches':found,
            'global_maximum_proved':False,'half_radius_completeness_proved':False,
            'method':'Logarithmic radius scan, angular local extrema, multistart analytic-gradient search; outermost detected half-maximum crossing.'}


def reporting_gauge(field):
    A,B,terms=leading_coefficients(field)
    mu,w=roots_legendre(max(64,len(A.coef)+len(B.coef)+8))
    data=angular_data(field.alpha,A.coef,B.coef)
    F=evaluate_vector(data,mu,'F');norm2=float(2*np.pi*np.sum(w[:,None]*F*F))
    slower=[row for row in terms if row['classification'] in ['slower than declared leading power','nondecaying or growing'] and row['coefficient']!=0]
    if norm2<=0 or slower:raise ValueError('no valid nonzero declared leading power for reporting gauge')
    L=norm2**(-1/(2*(1+field.alpha)))
    return field.dilate(L),{'dilation_L':L,'input_leading_squared_norm':norm2,
                            'reported_leading_squared_norm':float(L**(2+2*field.alpha)*norm2)}


def shell_quadrature(lower,upper,*,nradial=8,nangle=64,collar=False):
    if lower<0 or upper<=lower:raise ValueError('invalid radial interval')
    xr,wr=roots_legendre(nradial)
    if lower:
        lo,hi=np.log(lower),np.log(upper);R=np.exp((lo+hi)/2+(hi-lo)*xr/2)
        rw=wr*(hi-lo)/2*R**3
    else:
        R=(xr+1)*upper/2;rw=wr*upper/2*R*R
    if collar:
        x,w=roots_legendre((nangle+1)//2);angle=np.arcsin(.05)
        theta=np.r_[(x+1)*angle/2,np.pi-(x+1)*angle/2]
        mu=np.cos(theta);aw=np.r_[w,w]*angle/2
        weight=rw[:,None]*aw[None,:]
        measure='R squared dR dtheta, two axis collars sin(theta)<0.05'
    else:
        mu,aw=roots_legendre(nangle);weight=2*np.pi*rw[:,None]*aw[None,:]
        measure='2 pi R squared dR dmu'
    r=R[:,None]*np.sqrt(1-mu[None,:]**2);z=R[:,None]*mu[None,:]
    return {'radii':R,'mu':mu,'r':r,'z':z,'weights':weight,'measure':measure}


def random_shell(lower,upper,rng,count=256):
    # Uniform in the physical three-dimensional shell measure, with azimuth
    # suppressed because scalar diagnostics are axisymmetric.
    R=np.cbrt(lower**3+(upper**3-lower**3)*rng.random(count));mu=2*rng.random(count)-1
    return {'r':R*np.sqrt(1-mu*mu),'z':R*mu,'weights':np.full(count,4*np.pi*(upper**3-lower**3)/(3*count))}
