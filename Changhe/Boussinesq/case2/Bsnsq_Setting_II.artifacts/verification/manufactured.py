"""Analytic manufactured Poisson pairs, independent of all solver code."""
import numpy as np

class PolynomialRadialStream:
    def __init__(self, exponent=None, anisotropy=1.0):
        self.exponent = exponent
        self.anisotropy = anisotropy

    def radial(self, q):
        if self.exponent is None:
            h = np.exp(-q)
            return h, -h, h
        a = self.exponent
        h = (1+q)**(-a)
        return h, -a*h/(1+q), a*(a+1)*h/(1+q)**2

    def psi(self, p):
        x,y = np.moveaxis(np.asarray(p),-1,0)
        h,_,_ = self.radial(x*x+self.anisotropy*y*y)
        return x*y*h

    def omega(self, p):
        x,y = np.moveaxis(np.asarray(p),-1,0)
        k = self.anisotropy
        _,hp,hpp = self.radial(x*x+k*y*y)
        return -x*y*(6*(1+k)*hp+4*(x*x+k*k*y*y)*hpp)

    def velocity(self, p):
        x,y = np.moveaxis(np.asarray(p),-1,0)
        h,hp,_ = self.radial(x*x+self.anisotropy*y*y)
        return np.stack([-x*(h+2*self.anisotropy*y*y*hp),
                          y*(h+2*x*x*hp)],axis=-1)
