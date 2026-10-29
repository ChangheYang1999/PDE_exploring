"""Independent physical-time transport on retained backward T3 paths.

The rational prescribed potential is specified in the standalone proof.
No lead or numerics-lane transport implementation is imported.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp, quad


def profile(u,c_l,k):
    mu=(1+c_l)/(k-1);A=-(c_l+mu)/2;B=-2-3*c_l+mu;C=2-(c_l+mu)/2
    d=1+u;P=A+B*u+C*u*u;P1=B+2*C*u
    return P/d**3,P1/d**3-3*P/d**4,2*C/d**3-6*P1/d**4+12*P/d**5


def jets(r,z,c_l,k):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float));s=r*r;t=z*z
    F,F1,F2=profile(s+t,c_l,k)
    pz=F+2*t*F1;psz=F1+2*t*F2;pzz=6*z*F1+4*z*t*F2
    ar=c_l-pz;az=c_l+2*F+2*s*F1
    return {'phi':z*F,'phi_z':pz,'ar':ar,'az':az,'b':2*pz-1,
            'br':4*r*psz,'bz':2*pzz,'Drr':ar-2*s*psz,'Drz':-r*pzz,
            'Dzr':8*r*z*F1+4*r*s*z*F2,'Dzz':az+4*t*F1+4*s*t*F2}


def transport_points(r,z,c_l=.74,k=2.75,*,source_radius=1e-5,rtol=2e-10,atol=2e-12):
    if not (.6<=c_l<=.74 and 2<=k<=3):raise ValueError('outside proved portrait rectangle')
    r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float));shape=r.shape
    r=r.ravel();z=z.ravel();n=r.size
    if np.any(r<=0) or np.any(z<=0):raise ValueError('strictly positive coordinates required')
    target=np.stack((np.log(r),np.log(z)))
    def path_rhs(t,flat):
        lr,lz=flat.reshape(2,n);d=jets(np.exp(lr),np.exp(lz),c_l,k)
        return np.stack((d['ar'],d['az'])).ravel()
    def arrived(t,flat):
        lr,lz=flat.reshape(2,n)
        return float(np.max(np.hypot(np.exp(lr),np.expm1(lz)))-source_radius)
    arrived.terminal=True;arrived.direction=-1
    back=solve_ivp(path_rhs,(0.,-400.),target.ravel(),method='DOP853',events=arrived,
                   dense_output=True,rtol=rtol,atol=atol)
    if not back.success or not len(back.t_events[0]):raise RuntimeError('backward source cutoff not reached')
    logs=back.y[:,-1].reshape(2,n);rs,zs=np.exp(logs);delta=1+c_l;mu=delta/(k-1)
    F,F1,F2=profile(1.,c_l,k);Hz=(2*c_l-mu+1)/delta
    Hs=(2*(F1+2*F2)-4*F1*Hz)/(2*(c_l-.5))
    h0=1+Hs*rs*rs+Hz*(zs-1)
    if np.any(h0<=0):raise RuntimeError('source Taylor value not positive')
    initial=np.stack((np.log(h0),2*Hs*rs/h0,np.full(n,Hz)/h0,np.full(n,2*Hz/delta)))
    def scalar_rhs(t,flat):
        lr,lz=back.sol(t).reshape(2,n);d=jets(np.exp(lr),np.exp(lz),c_l,k)
        H,gr,gz,e=flat.reshape(4,n)
        return np.stack((d['b'],d['br']-d['Drr']*gr-d['Dzr']*gz,
                         d['bz']-d['Drz']*gr-d['Dzz']*gz,2*np.exp(2*H)*gz-delta*e)).ravel()
    fwd=solve_ivp(scalar_rhs,(back.t[-1],0.),initial.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not fwd.success:raise RuntimeError('scalar/variational transport failed')
    H,gr,gz,e=fwd.y[:,-1].reshape(4,n);h=np.exp(H)
    return {'h':h.reshape(shape),'h_r':(h*gr).reshape(shape),'h_z':(h*gz).reshape(shape),'e':e.reshape(shape),
            'backward_duration':-float(back.t[-1]),'backward_nfev':int(back.nfev),'forward_nfev':int(fwd.nfev),
            'backward_steps':len(back.t),'source_distance':float(np.max(np.hypot(rs,zs-1))),
            'source_radius':source_radius,'rtol':rtol,'atol':atol,'c_l':c_l,'k':k,
            'path_method':'Retained dense DOP853 backward path; no forward coordinate replay'}


def axis_reference(z,c_l=.74,k=2.75):
    delta=1+c_l;mu=delta/(k-1);B=(2*c_l-mu+1)/delta
    def w(v):
        F,F1,_=profile(v*v,c_l,k)
        return v*(c_l+2*F),c_l+2*F+4*v*v*F1
    def integrand(v):
        if abs(v-1)<1e-7:return B
        W,W1=w(v);return (W1-delta)/W
    h=float(np.exp(quad(integrand,1.,float(z),epsabs=2e-11,epsrel=2e-11,limit=200)[0]))
    W,_=w(z)
    e=2*B/delta if z==1 else 2*h*(h-1)/W
    return h,float(e)
