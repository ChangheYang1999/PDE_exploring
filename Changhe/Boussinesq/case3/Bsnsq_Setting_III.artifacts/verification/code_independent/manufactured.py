"""Closed-form fields for independent inverse and residual checks."""
import numpy as np


class Gaussian:
    """Psi=x(1+y)exp(-r^2), with finite nonzero physical center velocity."""
    name='gaussian'
    decay_power=1.0
    def psi(self,x,y):
        return x*(1+y)*np.exp(-(x*x+y*y))
    def omega(self,x,y):
        r2=x*x+y*y
        return 4*x*((2-r2)+y*(3-r2))*np.exp(-r2)
    def velocity(self,x,y):
        e=np.exp(-(x*x+y*y))
        return np.stack((x*(2*y*(1+y)-1)*e,(1-2*x*x)*(1+y)*e),axis=-1)
    def relative(self,points):
        p=np.asarray(points)
        return self.velocity(p[...,0],p[...,1])-np.array([0,1])
    c=1.0
    v0=1.0


class SlowStream:
    """Psi=x(1+r^2)^q1+x y(1+r^2)^q2.

    q1=(1-delta)/2 and q2=-delta/2, so both vorticity modes
    have r^(-delta) tails and U has sublinear r^(1-delta) growth.
    Velocity is explicit, enabling validation without any inverse reference.
    """
    name='slow_stream'
    def __init__(self,delta=1/3):
        self.decay_power=delta
        self.q1=(1-delta)/2
        self.q2=-delta/2
    def psi(self,x,y):
        z=1+x*x+y*y
        return x*z**self.q1+x*y*z**self.q2
    def omega(self,x,y):
        r2=x*x+y*y
        z=1+r2
        # Lap[P_m f(r^2)]=4 P_m[(m+1)f'+r^2 f''] for harmonic P_m.
        q=self.q1
        v=-4*x*q*z**(q-2)*(2+(q+1)*r2)
        q=self.q2
        return v-4*x*y*q*z**(q-2)*(3+(q+2)*r2)
    def velocity(self,x,y):
        r2=x*x+y*y
        z=1+r2
        q=self.q1
        ux=-2*q*x*y*z**(q-1)
        uy=z**q+2*q*x*x*z**(q-1)
        q=self.q2
        ux-=x*z**q+2*q*x*y*y*z**(q-1)
        uy+=y*z**q+2*q*x*x*y*z**(q-1)
        return np.stack((ux,uy),axis=-1)
    def relative(self,points):
        p=np.asarray(points)
        return self.velocity(p[...,0],p[...,1])-np.array([0,1])
    c=1.0
    v0=1.0  # Explicit stream choice. The ordinary BS moment diverges.
