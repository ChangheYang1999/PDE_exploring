"""Independent five-dimensional stream reconstruction with interface jumps."""
from functools import lru_cache
import numpy as np
from independent_pressure import GreenPoisson
from piecewise_pressure import InterfaceGreenPoisson


def jump_mode_coefficients(ell,dimension,radius,value_jump,derivative_jump):
    ell=np.asarray(ell,dtype=float);denom=2*ell+dimension-2
    inner=-(radius*derivative_jump+(ell+dimension-2)*value_jump)/denom
    outer=(ell*value_jump-radius*derivative_jump)/denom
    return inner,outer


class StreamInterfaceCorrection(GreenPoisson):
    """Only the surface contribution; the interior trace is used at R=a."""
    def __init__(self,field,*,lmax=24,nangle=64):
        super().__init__(lambda r,z:np.zeros_like(r),dimension=5,decay_power=field.alpha,
                         lmax=lmax,nangle=nangle,nradial=4,scale=field.phi.length)
        self.surfaces=[]
        for i,a in enumerate(field.interfaces):
            mu=self.mu;r=a*np.sqrt(1-mu*mu);z=a*mu
            traces=[]
            for element in [i,i+1]:
                jets=field.jets(r*r,z,1,element=element)['phi']
                radial=2*a*(1-mu*mu)*jets[1,0]+mu*jets[0,1]
                traces.append((jets[0,0],radial))
            j=(traces[1][0]-traces[0][0])@self.projector
            h=(traces[1][1]-traces[0][1])@self.projector
            inner,outer=jump_mode_coefficients(self.ell,5,a,j,h)
            self.surfaces.append(dict(radius=float(a),value_jump=j,derivative_jump=h,inner=inner,outer=outer))

    @lru_cache(maxsize=256)
    def radial(self,R):
        R=float(R)
        if R<0:raise ValueError('negative radius')
        p=np.zeros(self.lmax+1);dp=np.zeros_like(p);ell=self.ell
        for surface in self.surfaces:
            a=surface['radius']
            if R<=a:
                value=surface['inner']*(R/a)**ell
                if R:derivative=ell*value/R
                else:
                    derivative=np.zeros_like(p)
                    if self.lmax:derivative[1]=surface['inner'][1]/a
            else:
                value=surface['outer']*(a/R)**(ell+3)
                derivative=-(ell+3)*value/R
            p+=value;dp+=derivative
        return p,dp


class ReconstructedStream:
    def __init__(self,field,*,lmax=24,nangle=64,nradial=48):
        self.bulk=InterfaceGreenPoisson(field.eta,interfaces=field.interfaces,dimension=5,
            decay_power=field.alpha,lmax=lmax,nangle=nangle,nradial=nradial,scale=field.phi.length)
        self.surface=StreamInterfaceCorrection(field,lmax=lmax,nangle=nangle)
    def evaluate(self,r,z):
        p,g=self.bulk.evaluate(r,z);s,h=self.surface.evaluate(r,z)
        return p+s,g+h
    def on_spheres(self,radii,mu):
        p,g=self.bulk.on_spheres(radii,mu);s,h=self.surface.on_spheres(radii,mu)
        return p+s,g+h
