"""Exact rescaling of the independent inverse's infinite exterior.

Only our own inverse and coefficient reader are used. See research/log_radius_inverse/PROOF.md.
"""
import numpy as np
from direct_inverse import DirectInverse
from q_checkpoint_reader import QCheckpoint


def factored_kernel(tau,nx,ny,ex,ey):
    v=tau-2*(nx*ex+ny*ey)
    q=1+tau*v
    j=v*(2+tau*v)
    a=tau*nx*ny-nx*ey-ny*ex-ex*ey*j
    b=tau*(nx*nx-ny*ny)-2*nx*ex+2*ny*ey-(ex*ex-ey*ey)*j
    return np.stack((-a/(np.pi*q*q),b/(2*np.pi*q*q)),axis=-1)


class LogTailInverse(DirectInverse):
    def __init__(self,density,config):
        super().__init__(density,config)
        owner=getattr(density,'__self__',None)
        self.scaled_log_density=getattr(owner,'log_scaled_polar_density',None)
        if self.scaled_log_density is None:
            raise TypeError('LogTailInverse requires rho(r,theta)/r^p evaluated from log(r)')

    def infinite_exterior(self,x,y,tail_radius):
        mag=np.hypot(x,y)
        log_r=np.log(tail_radius)-self.power*np.log(self.jt)
        info={'largest_quadrature_log_radius':float(log_r.max()),
              'infinite_exterior_method':'exact log-radius scaled density and factored kernel'}
        if mag==0:return np.zeros(2),info
        tau=np.exp(np.log(mag)-log_r)
        kk=factored_kernel(tau[:,None],x/mag,y/mag,self.ex[None,:],self.ey[None,:])
        hh=self.scaled_log_density(log_r,self.theta)
        factor=self.power*mag*np.exp(-(1-self.config.exponent)*np.log(tail_radius))
        far=factor*np.sum(self.jw[:,None,None]*hh[:,:,None]*kk,axis=(0,1))*self.dtheta
        if not np.isfinite(far).all():raise ArithmeticError('Nonfinite scaled exterior')
        return far,info


class LogRadiusQCheckpoint(QCheckpoint):
    def coordinates_log(self,log_r):
        log_r=np.asarray(log_r,float);shape=log_r.shape
        target_all=log_r.reshape(-1)-np.log(self.L)
        if not np.isfinite(target_all).all():raise ValueError('Finite log radii required')
        small=target_all<=-.5*np.log(2.)
        sigma=np.empty_like(target_all);tq=np.empty_like(target_all)
        for is_small,mask in [(True,small),(False,~small)]:
            target=target_all[mask]
            if not len(target):continue
            log_start=2*target+2*self.kappa*np.log(2.) if is_small else -target/self.kappa
            cap=.5 if is_small else 1.
            lo=np.zeros_like(target);hi=np.full_like(target,cap)
            q=np.exp(np.clip(log_start,-740,np.log(cap)))
            done=log_start<-700
            # At these endpoints the omitted correction is below double precision.
            q=np.where(done,np.exp(np.maximum(log_start,-745)),q)
            for _ in range(96):
                safe=np.where(done,.5,np.maximum(q,np.finfo(float).tiny))
                if is_small:
                    f=np.log(safe)-2*self.kappa*np.log1p(-safe)-2*target-2*self.kappa*np.log(2.)
                    df=1/safe+2*self.kappa/(1-safe)
                else:
                    f=self.kappa*np.log(safe)-.5*np.log1p(-safe/2)+target
                    df=self.kappa/safe+.25/(1-safe/2)
                trial=q-f/df
                scale=1+abs(target)+self.kappa*np.log(2.)
                done|=(abs(f)<=8*np.finfo(float).eps*scale)|(trial==q)|((hi-lo)<=4*np.finfo(float).eps*safe)
                if np.all(done):break
                hi=np.where((f>0)&~done,q,hi);lo=np.where((f<=0)&~done,q,lo)
                trial=np.where((trial>lo)&(trial<hi),trial,(lo+hi)/2)
                q=np.where(done,q,trial)
            if not np.all(done):raise ArithmeticError('Log-radius Newton failed')
            sigma[mask]=q if is_small else 1-q/2
            tq[mask]=2*q-1 if is_small else 1-q
        return tq.reshape(shape),sigma.reshape(shape)

    def log_scaled_polar_density(self,log_r,theta):
        theta=np.asarray(theta,float);tq,sigma=self.coordinates_log(log_r)
        modes=np.array([sigma**k*self.polynomial(k,tq) for k in range(self.M)])
        angular=np.cos(2*np.arange(self.M)[:,None]*theta[None,:])
        radial=(self.L**self.eta/2)*sigma**(self.eta/2)
        return radial[:,None]*np.sin(theta)[None,:]*(modes.T@angular)
