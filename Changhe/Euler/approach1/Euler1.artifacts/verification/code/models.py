"""Forward evaluators written independently of the numerics lane."""
from __future__ import annotations
import numpy as np


class Affine:
    def __init__(self,c_l=.45,a=.2,b=-.4,b2=.7,C=0.):
        self.c_l=c_l; self.C=C
        self.M=np.array([[a,b,0.],[b2,-1-a,0.],[0.,0.,1.]])
        self.S=self.M+self.M@self.M
        self.metadata=dict(kind='affine calibration',c_l=c_l,C=C)
    def __call__(self,x):
        U=x@self.M.T
        P=-.5*np.einsum('ni,ij,nj->n',x,self.S,x)
        if self.C:
            # Add the linear pressure needed for a nonzero axial C.
            P-=self.C*(x@self.M[:,2])
        return np.column_stack([U,P])


class Seed(Affine):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.metadata['kind']='localized potential seed, not a solved Euler profile'
    def __call__(self,x):
        s=np.sum(x*x,axis=1)
        chi=(1+s)**(-1/(2*self.c_l))
        My=x@self.M.T
        q=np.sum(x*My,axis=1)
        U=chi[:,None]*((1-s/(3*self.c_l*(1+s)))[:,None]*My+(q/(3*self.c_l*(1+s)))[:,None]*x)
        P=-.5*chi**2*np.einsum('ni,ij,nj->n',x,self.S,x)
        return np.column_stack([U,P])


class Polynomial:
    """Manufactured Q-equivariant polynomial with nonzero divergence.

    Deliberately tests divergence corrections and absence of extra parity.
    It is not a physical incompressible candidate.
    """
    def __init__(self,c_l=.45,C=.17):
        self.c_l=c_l; self.C=C
        self.metadata=dict(kind='manufactured compressible polynomial',c_l=c_l,C=C)
    def __call__(self,x):
        a,b,z=x.T
        return np.column_stack([.4*a+1.2*b*z+.13*a*z*z,
                                2*a*z-2*a+.3*b+.07*b**3,
                                1.6*a*b-.7*z+.11*z*z,
                                z**3+.2*a*a*z+.7*a*b+.1*b*b*z*z])
