"""Independent backward-then-forward point characteristics for a T1 seed.

No interpolation, radial marching, lead code or numerics code is used.
Values are at finite accuracy and do not certify elliptic closure.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import roots_legendre


def seed_jets(r,z,c_l):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float))
    s=r*r;t=z*z;u=1+s+t;d=1+1/(2*c_l);base=u**(-d)
    F=.5*(1+3*t)*base;Fs=-d*F/u;Ft=1.5*base-d*F/u
    Fss=d*(d+1)*F/u**2;Fst=-1.5*d*base/u+d*(d+1)*F/u**2
    Ftt=-3*d*base/u+d*(d+1)*F/u**2
    pz=F+2*t*Ft;psz=Fs+2*t*Fst;pzz=2*z*(3*Ft+2*t*Ftt)
    ar=c_l-pz;az=c_l+2*F+2*s*Fs
    Drr=ar-2*s*psz;Drz=-r*pzz
    Dzr=8*r*z*Fs+4*r*s*z*Fss;Dzz=az+4*t*Ft+4*s*t*Fst
    return {'phi':z*F,'phi_z':pz,'log_r_speed':ar,'log_z_speed':az,
            'a':2*pz-1,'a_r':4*r*psz,'a_z':2*pzz,
            'Drr':Drr,'Drz':Drz,'Dzr':Dzr,'Dzz':Dzz}


def transport_points(r,z,c_l=.74,*,source_radius=1e-5,rtol=2e-10,atol=2e-12):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float));shape=r.shape
    r=r.ravel();z=z.ravel();count=len(r)
    if np.any(r<=0) or np.any(z<=0):raise ValueError('strictly positive meridional coordinates required')
    if not .5<c_l<.75:raise ValueError('supercritical seed only')
    target=np.stack((np.log(r),np.log(z)))
    def backward(t,flat):
        logs=flat.reshape(2,count);d=seed_jets(np.exp(logs[0]),np.exp(logs[1]),c_l)
        return np.stack((d['log_r_speed'],d['log_z_speed'])).ravel()
    def source_event(t,flat):
        logs=flat.reshape(2,count)
        return float(np.max(.5*np.logaddexp(2*logs[0],2*logs[1]))-np.log(source_radius))
    source_event.terminal=True;source_event.direction=-1
    back=solve_ivp(backward,(0.,-180.),target.ravel(),method='DOP853',events=source_event,rtol=rtol,atol=atol)
    if not back.success or not len(back.t_events[0]):raise RuntimeError('backward source threshold not reached')
    logs=back.y[:,-1].reshape(2,count);rs,zs=np.exp(logs);s=rs*rs;t=zs*zs
    d=1+1/(2*c_l);ps=-d/2;pz=(3-d)/2;eps=c_l-.5;delta=1+c_l
    A=ps/eps;B=3*pz/delta;E=6*pz/delta**2;h0=1+A*s+B*t
    if np.any(h0<=0):raise ValueError('source Taylor initialization not positive')
    initial=np.concatenate((logs,np.stack((np.log(h0),2*A*rs/h0,2*B*zs/h0,E*zs))),axis=0)
    def forward(time,flat):
        y=flat.reshape(6,count);rr,zz=np.exp(y[:2]);d=seed_jets(rr,zz,c_l)
        H,gr,gz,e=y[2:];er=2*np.exp(2*H)*gz-delta*e
        return np.stack((d['log_r_speed'],d['log_z_speed'],d['a'],
                         d['a_r']-d['Drr']*gr-d['Dzr']*gz,
                         d['a_z']-d['Drz']*gr-d['Dzz']*gz,er)).ravel()
    forward_result=solve_ivp(forward,(float(back.t[-1]),0.),initial.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not forward_result.success:raise RuntimeError('forward characteristic failed')
    result=forward_result.y[:,-1].reshape(6,count);h=np.exp(result[2]);e=result[5]
    return {'h':h.reshape(shape),'h_r':(h*result[3]).reshape(shape),'h_z':(h*result[4]).reshape(shape),'e':e.reshape(shape),
            'backward_duration':-float(back.t[-1]),'backward_nfev':int(back.nfev),'forward_nfev':int(forward_result.nfev),
            'endpoint_log_error':float(np.max(np.abs(result[:2]-target))),
            'source_radius':source_radius,'rtol':rtol,'atol':atol,'c_l':c_l}


def strain_quadrature(c_l=.74,nradial=32,nangle=32,**kwargs):
    x,wx=roots_legendre(nradial);x=(x+1)/2;wx=wx/2
    R=x/(1-x);wr=wx/(1-x)**2
    mu,wm=roots_legendre(nangle);mu=(mu+1)/2;wm=wm/2
    r=R[:,None]*np.sqrt(1-mu[None,:]**2);z=R[:,None]*mu[None,:]
    result=transport_points(r,z,c_l,**kwargs)
    density=1.5*result['e']*mu[None,:]*(1-mu[None,:]**2)
    w=wr[:,None]*wm[None,:]
    S=float(np.sum(w*density));positive=float(np.sum(w*np.maximum(density,0)))
    result.update(S=S,S_positive=positive,S_negative=float(-np.sum(w*np.minimum(density,0))),
                  K_for_source_strain=float(np.sqrt(.5/S)) if S>0 else None,
                  nradial=nradial,nangle=nangle,radii=R,mu=mu,h_max=float(result['h'].max()))
    return result
