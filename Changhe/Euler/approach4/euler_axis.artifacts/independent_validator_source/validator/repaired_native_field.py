"""Explicit source-strain repair on an independently evaluated native field."""
import numpy as np
from numpy.polynomial import polynomial as poly

class RepairedNativeField:
    def __init__(self,base,source):
        if base.dilation!=1:raise ValueError('Native coordinates required')
        self.base=base;self.c_l=base.c_l;self.interfaces=base.interfaces
        self.z0=float(source['z0']);self.epsilon=float(source['epsilon']);self.delta=float(source['repair_radius'])
        self.H=[np.array([0.,1.])]
        for _ in range(3):self.H.append(poly.polysub(poly.polyder(self.H[-1]),poly.polymul(self.H[-1],np.array([0.,2/self.delta**2]))))
    def jets(self,s,z,order,*,element=None):
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float));t=z-self.z0
        out={key:{ab:value.copy() for ab,value in jet.items()} for key,jet in self.base.jets(s,z,order,element=element).items()}
        E=self.epsilon*np.exp(-(s+t*t)/self.delta**2)
        for (a,b),value in out['phi'].items():value+=E*(-1/self.delta**2)**a*poly.polyval(t,self.H[b])
        return out
