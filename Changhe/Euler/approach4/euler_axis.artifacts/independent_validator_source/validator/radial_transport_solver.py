"""Semi-Lagrangian radial transport with independently evaluated coefficients."""
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.special import roots_legendre


def angular_grid(n):
    if n<7:raise ValueError('At least seven angular nodes')
    return -np.cos(np.linspace(0,np.pi,n))


def angular_moment_weights(mu):
    # The interpolant has degree five on each interval. Multiplying by
    # mu(1-mu^2) gives degree eight, integrated exactly by five Gauss nodes.
    nodes,w=roots_legendre(5);lo=mu[:-1];hi=mu[1:]
    x=((lo+hi)[:,None]/2+(hi-lo)[:,None]*nodes/2).ravel()
    weights=((hi-lo)[:,None]*w/2).ravel()*x*(1-x*x)
    return weights@make_interp_spline(mu,np.eye(len(mu)),k=5)(x)


def radial_step(model,x,mu,h,eta,dx):
    def velocity(t,m):return model(t,m)['v']
    def clip(m):
        if np.max(abs(m))>1+1e-8:raise RuntimeError('Escaped angular interval')
        return np.clip(m,-1,1)
    v1=velocity(x+dx,mu);v2=velocity(x+dx/2,clip(mu-dx*v1/2))
    v3=velocity(x+dx/2,clip(mu-dx*v2/2));v4=velocity(x,clip(mu-dx*v3))
    foot=clip(mu-dx*(v1+2*v2+2*v3+v4)/6)
    hs=make_interp_spline(mu,h,k=5);es=make_interp_spline(mu,eta,k=5)
    y=np.stack([foot,hs(foot),hs.derivative()(foot),es(foot)],axis=1)
    def rhs(t,Y):
        m=clip(Y[:,0]);ell=Y[:,1];k=Y[:,2];e=Y[:,3];d=model(t,m)
        q2=model.K**2*np.exp(2*ell)
        forcing=2*q2/(d['rho']*d['F'])*(-m*d['b']+(1-m*m-m*d['v'])*k)
        return np.stack([d['v'],-d['b'],-d['bm']-d['vm']*k,-d['lam']*e+forcing],axis=1)
    k1=rhs(x,y);k2=rhs(x+dx/2,y+dx*k1/2);k3=rhs(x+dx/2,y+dx*k2/2);k4=rhs(x+dx,y+dx*k3)
    result=y+dx*(k1+2*k2+2*k3+k4)/6
    if not np.all(np.isfinite(result)):raise RuntimeError('Nonfinite transported data')
    return result[:,1],result[:,3],dict(maximum_endpoint_mu_error=float(np.max(abs(result[:,0]-mu))),
                                      maximum_gradient_remap_difference=float(np.max(abs(make_interp_spline(mu,result[:,1],k=5).derivative()(mu)-result[:,2]))))
