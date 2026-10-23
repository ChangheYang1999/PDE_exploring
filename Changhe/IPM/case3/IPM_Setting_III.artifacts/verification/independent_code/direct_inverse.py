"""Full-plane IPM inverse, written independently by the referee verifier.

The near/interior integral is Cartesian kernel quadrature centred at the
query point. The exterior is a cancellation-subtracted integral centred at
0 on an infinite Jacobi-mapped domain. No angular Poisson modes, lane code,
FFT, finite-box Poisson solve, or fitted harmonic field are used.
"""
from dataclasses import dataclass
import numpy as np
from scipy.special import roots_legendre, roots_jacobi, betainc


def kernel_angle(ex, ey):
    return np.stack((-ex*ey/np.pi, (ex*ex-ey*ey)/(2*np.pi)), axis=-1)


def kernel_difference_scaled(zx, zy, ex, ey):
    """k(z-e)-k(-e), evaluated without subtracting nearby O(1) values."""
    delta = zx*zx+zy*zy-2*(zx*ex+zy*ey)
    q = 1+delta
    qdiff = delta*(2+delta)
    num1 = zx*zy-zx*ey-zy*ex-ex*ey*qdiff
    num2 = zx*zx-zy*zy-2*zx*ex+2*zy*ey-(ex*ex-ey*ey)*qdiff
    return np.stack((-num1/(np.pi*q*q),num2/(2*np.pi*q*q)),axis=-1)


@dataclass(frozen=True)
class Quadrature:
    radial: int = 40
    angular: int = 160
    exterior: int = 64
    outer_factor: float = 4.0
    length: float = 1.0
    exponent: float = 0.5
    exterior_start: float = 0.0
    tail_power: float = 0.0


class DirectInverse:
    def __init__(self, density, config=Quadrature()):
        self.density=density
        owner=getattr(density,'__self__',None)
        self.polar_density=getattr(owner,'polar_density',None)
        self.config=config
        if config.angular % 4:
            raise ValueError('Angular resolution must be a multiple of 4.')
        if not 0 < config.exponent < 1:
            raise ValueError('The exterior quadrature exponent must lie in (0,1).')
        t, wt=roots_legendre(config.radial)
        self.t=(1+t)/2
        self.wt=wt/2
        self.mt=((np.arange(8)[:,None]+self.t[None,:])/8).reshape(-1)
        self.mw=np.tile(self.wt/8,8)
        theta=(np.arange(config.angular)+0.5)*2*np.pi/config.angular
        self.theta=theta
        self.ex=np.cos(theta)
        self.ey=np.sin(theta)
        self.k=kernel_angle(self.ex,self.ey)
        self.dtheta=2*np.pi/config.angular
        # R=r0*t^-power; weighting exactly cancels the worst leading tail.
        self.power=(config.tail_power if config.tail_power>0 else min(4.0,1.0/(1-config.exponent)))
        beta=self.power*(1-config.exponent)-1
        jt,jw=roots_jacobi(config.exterior,0,beta)
        self.jt=(jt+1)/2
        self.jw=jw/(2**(beta+1))
        self.beta=beta

    def velocity(self,x,y,parts=False):
        x=float(x); y=float(y)
        mag=np.hypot(x,y)
        scale=max(self.config.length,mag)
        radius=self.config.outer_factor*scale
        local=0.5*scale
        if radius <= mag+local:
            raise ValueError('The outer circle must contain the local subtraction disk.')
        rho0=float(np.asarray(self.density(x,y)))
        half=self.config.angular//2
        ex=self.ex[:half][None,:]; ey=self.ey[:half][None,:]
        rr=(local*self.t)[:,None]
        pair=self.density(x+rr*ex,y+rr*ey)+self.density(x-rr*ex,y-rr*ey)-2*rho0
        near=np.sum(self.wt[:,None,None]/self.t[:,None,None]*pair[:,:,None]*self.k[None,:half,:],axis=(0,1))*self.dtheta

        # Remaining portion of |Y|<radius, expressed about X. This domain
        # supplies the finite constant-density contribution outside the disk.
        dot_scaled=(x/scale)*self.ex+(y/scale)*self.ey
        smax=scale*(-dot_scaled+np.sqrt(dot_scaled*dot_scaled+self.config.outer_factor**2-(mag/scale)**2))
        logspan=np.log(smax/local)
        rr=local*np.exp(self.mt[:,None]*logspan[None,:])
        yyx=x+rr*self.ex[None,:]
        yyy=y+rr*self.ey[None,:]
        rho=self.density(yyx,yyy)
        core=np.zeros(2)
        if mag > 4*self.config.length:
            # Remove the small origin core from query-centred quadrature and
            # integrate it on radial panels about the origin. The kernel is
            # smooth there since the core radius is |X|/2.
            rcore=mag/2
            def cutoff(q):
                u=np.clip(2*q-1,0,1)
                return 1-betainc(10,10,u)
            rho=rho*(1-cutoff(np.hypot(yyx,yyy)/rcore))
            edges=[0., min(self.config.length,rcore)]
            while edges[-1] < rcore:
                edges.append(min(2*edges[-1],rcore))
            for lo,hi in zip(edges[:-1],edges[1:]):
                cr=lo+(hi-lo)*self.t
                cx=cr[:,None]*self.ex[None,:]
                cy=cr[:,None]*self.ey[None,:]
                cv=(self.polar_density(cr,self.theta) if self.polar_density else self.density(cx,cy))*cutoff(cr[:,None]/rcore)
                ck=kernel_difference_scaled(-cx/mag,-cy/mag,-x/mag,-y/mag)
                area_scaled=((hi-lo)/mag)*self.wt*(cr/mag)
                core+=np.sum(area_scaled[:,None,None]*cv[:,:,None]*ck,axis=(0,1))*self.dtheta
        middle=np.sum(self.mw[:,None,None]*logspan[None,:,None]*rho[:,:,None]*self.k[None,:,:],axis=(0,1))*self.dtheta

        # Exterior difference integrates to the original kernel because
        # int k(-e)rho(r e)dtheta=0 by central oddness. Jacobi map goes to infinity.
        outer=np.zeros(2)
        tail_radius=max(radius,self.config.exterior_start)
        current=radius
        while current < tail_radius:
            nxt=min(2*current,tail_radius)
            logstep=np.log(nxt/current)
            rr=current*np.exp(self.t*logstep)
            pd=(self.polar_density(rr,self.theta) if self.polar_density else self.density(rr[:,None]*self.ex[None,:],rr[:,None]*self.ey[None,:]))
            kd=kernel_difference_scaled(x/rr[:,None],y/rr[:,None],self.ex[None,:],self.ey[None,:])
            outer+=np.sum((logstep*self.wt)[:,None,None]*pd[:,:,None]*kd,axis=(0,1))*self.dtheta
            current=nxt
        far,tail_info=self.infinite_exterior(x,y,tail_radius)
        contact=np.array([0.,-rho0/2])
        ans=near+middle+core+outer+far+contact
        if parts:
            return ans,{'near':near.tolist(),'middle':middle.tolist(),'core':core.tolist(),'outer_panels':outer.tolist(),'exterior':far.tolist(),'contact':contact.tolist(),'outer_radius':radius,**tail_info}
        return ans

    def infinite_exterior(self,x,y,tail_radius):
        rr=tail_radius*self.jt**(-self.power)
        ex=self.ex[None,:]; ey=self.ey[None,:]
        kd=kernel_difference_scaled(x/rr[:,None],y/rr[:,None],ex,ey)
        rho=self.polar_density(rr,self.theta) if self.polar_density else self.density(rr[:,None]*ex,rr[:,None]*ey)
        weighted=(self.power*self.jw/self.jt**(1+self.beta))[:,None,None]
        far=np.sum(weighted*rho[:,:,None]*kd,axis=(0,1))*self.dtheta
        return far,{'largest_quadrature_radius':float(rr.max())}

    def velocities(self,points):
        return np.array([self.velocity(*p) for p in np.asarray(points)])


def cartesian_gradient(density,x,y,relative_step=1e-3,length=1.0):
    """Symmetric eighth-order differences; distinct from spectral derivatives."""
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
    h=relative_step*np.maximum(length,np.hypot(x,y))
    weights=np.array([4/5,-1/5,4/105,-1/280])
    gx=np.zeros_like(x); gy=np.zeros_like(y)
    for k,w in enumerate(weights,1):
        gx+=w*(density(x+k*h,y)-density(x-k*h,y))/h
        gy+=w*(density(x,y+k*h)-density(x,y-k*h))/h
    return gx,gy


def residual(density,inverse,points,c_l,step=1e-3):
    points=np.asarray(points,float)
    x,y=points.T
    rho=density(x,y)
    gx,gy=cartesian_gradient(density,x,y,step,inverse.config.length)
    u=inverse.velocities(points)
    tx=(c_l*x+u[:,0])*gx
    ty=(c_l*y+u[:,1])*gy
    ud=u[:,0]*gx+u[:,1]*gy
    xd=x*gx+y*gy
    r=tx+ty-rho
    nf=np.abs(tx)+np.abs(ty)+np.abs(rho)
    nv=np.abs(rho)+np.abs(xd)+np.abs(ud)
    return {'x':x,'y':y,'rho':rho,'rho_x':gx,'rho_y':gy,'u1':u[:,0],'u2':u[:,1],'R':r,'Nf':nf,'Nv':nv,
            'R_over_Nf':np.divide(np.abs(r),nf,out=np.full_like(r,np.nan),where=nf>0),
            'R_over_Nv':np.divide(np.abs(r),nv,out=np.full_like(r,np.nan),where=nv>0)}
