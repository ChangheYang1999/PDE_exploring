"""A second physical-space quadrature, with exact fourfold kernel cancellation.

Integrate over the source quadrant in compact Cartesian coordinates. Split
at each target into rectangles and opposite-corner Duffy triangles, cancelling the local
1/distance singularity and the joint-infinity corner by triangular Jacobians. No modal inversion,
Fourier differentiation, finite box, or fitting code is used.
"""
from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss

@dataclass(frozen=True)
class DuffyQuadrature:
    order:int=64
    tail_power:float=.5
    scale:float=1.0

    def map(self,t):
        exponent=1/self.tail_power
        r=self.scale*np.exp(exponent*(np.log(t)-np.log1p(-t)))
        derivative=exponent*r/(t*(1-t))
        return r,derivative

    def inverse_map(self,r):
        if r==0:return 0.0
        t=(r/self.scale)**self.tail_power
        return t/(1+t)


def velocity_duffy(omega,targets,config=DuffyQuadrature()):
    targets=np.atleast_2d(np.asarray(targets,float))
    zeta,weight=leggauss(config.order)
    u=(zeta+1)/2;weight=weight/2
    uu,vv=np.meshgrid(u,u,indexing='ij')
    weights=weight[:,None]*weight[None,:]
    outputs=[]
    for target in targets:
        x,y=abs(target);z=complex(x,y)
        if z==0:
            outputs.append([0.0,0.0]);continue
        px,py=config.inverse_map(x),config.inverse_map(y)
        integral=0j
        for dx in [-px,1-px]:
            if dx==0:continue
            for dy in [-py,1-py]:
                if dy==0:continue
                for opposite in [False,True]:
                    if opposite:
                        p=px+dx-dx*uu*vv
                        q=py+dy-dy*uu*(1-vv)
                    else:
                        p=px+dx*uu*vv
                        q=py+dy*uu*(1-vv)
                    a,ap=config.map(p);b,bp=config.map(q)
                    w=a+1j*b
                    denom=np.conj((z*z-w*w)*(z*z-np.conj(w)**2))
                    kernel=(-4/np.pi)*a*b*np.conj(z)/denom
                    field=omega(np.stack([a,b],axis=-1))
                    jacobian=abs(dx*dy)*uu*ap*bp
                    integral+=np.sum(weights*jacobian*kernel*field)
        outputs.append([integral.real*np.sign(target[0]),integral.imag*np.sign(target[1])])
    return np.asarray(outputs)


def stream_duffy(omega,targets,config=DuffyQuadrature()):
    """Parity-fixed stream function from the convergent quadrant log kernel."""
    targets=np.atleast_2d(np.asarray(targets,float))
    zeta,weight=leggauss(config.order)
    u=(zeta+1)/2;weight=weight/2
    uu,vv=np.meshgrid(u,u,indexing='ij')
    weights=weight[:,None]*weight[None,:]
    outputs=[]
    for target in targets:
        x,y=abs(target);z=complex(x,y)
        if x*y==0:
            outputs.append(0.0);continue
        px,py=config.inverse_map(x),config.inverse_map(y)
        integral=0.0
        for dx in [-px,1-px]:
            if dx==0:continue
            for dy in [-py,1-py]:
                if dy==0:continue
                for opposite in [False,True]:
                    if opposite:
                        p=px+dx-dx*uu*vv
                        q=py+dy-dy*uu*(1-vv)
                    else:
                        p=px+dx*uu*vv
                        q=py+dy*uu*(1-vv)
                    a,ap=config.map(p);b,bp=config.map(q)
                    w=a+1j*b
                    squared_distance=np.abs(z*z-w*w)**2
                    kernel=np.log1p(16*x*y*a*b/squared_distance)/(4*np.pi)
                    field=omega(np.stack([a,b],axis=-1))
                    jacobian=abs(dx*dy)*uu*ap*bp
                    integral+=np.sum(weights*jacobian*kernel*field)
        outputs.append(integral*np.sign(target[0])*np.sign(target[1]))
    return np.asarray(outputs)
