"""A second numerical representation: values projected on shell Chebyshev grids.

Only scalar phi/q values enter the projection. All derivatives of the
interpolant use transformed Chebyshev coefficients, never candidate jets.
The s,z derivative operators are independently transformed through R,mu.
"""
from __future__ import annotations
from functools import lru_cache
from math import comb
import numpy as np
from numpy.polynomial.chebyshev import chebder,chebval2d
from scipy.fft import dct
from independent_fields import PotentialField


@lru_cache(maxsize=None)
def chain_operator(ds,dz):
    # (R power, mu power, R derivative order, mu derivative order) -> factor.
    terms={(0,0,0,0):1.}
    for direction in [0]*ds+[1]*dz:
        result={}
        def add(key,c):
            if c:result[key]=result.get(key,0.)+c
        for (p,q,a,b),c in terms.items():
            if direction==0:
                add((p-2,q,a,b),.5*(p-q)*c)
                add((p-1,q,a+1,b),.5*c)
                add((p-2,q+1,a,b+1),-.5*c)
            else:
                add((p-1,q+1,a,b),(p-q)*c)
                if q:add((p-1,q-1,a,b),q*c)
                add((p,q+1,a+1,b),c)
                add((p-1,q,a,b+1),c)
                add((p-1,q+2,a,b+1),-c)
        terms={key:c for key,c in result.items() if c}
    return tuple((key,c) for key,c in terms.items())


class ShellProjection:
    def __init__(self,value,lower,upper,*,radial_degree=20,angular_degree=24,trim_relative=0.,factor_power=0.,numeric_dtype=np.float64):
        if lower<=0 or upper<=lower:raise ValueError('projection shell must avoid the origin')
        self.lower=float(lower);self.upper=float(upper);self.mid=(lower+upper)/2;self.half=(upper-lower)/2
        self.length=self.half;self.dtype=np.dtype(numeric_dtype).type;self.factor_power=self.dtype(factor_power)
        nr,na=int(radial_degree),int(angular_degree)
        pi=np.arccos(self.dtype(-1));x=np.cos(pi*np.arange(nr+1,dtype=self.dtype)/nr);mu=np.cos(pi*np.arange(na+1,dtype=self.dtype)/na)
        R=self.mid+self.half*x
        s=R[:,None]**2*(1-mu[None,:]**2);z=R[:,None]*mu[None,:]
        values=np.asarray(value(s,z),dtype=self.dtype)*R[:,None]**self.factor_power
        coeff=dct(dct(values,type=1,axis=0),type=1,axis=1)/(nr*na)
        coeff[[0,-1],:]*=.5;coeff[:,[0,-1]]*=.5
        threshold=trim_relative*np.max(np.abs(values));removed=np.abs(coeff)<threshold
        self.trimmed_l1=float(np.sum(np.abs(coeff[removed]))) if trim_relative else 0.
        if trim_relative:coeff[removed]=0.
        self.coefficients=coeff;self.value_scale=float(np.max(np.abs(values)))
        self.metadata={'radial_degree':nr,'angular_degree':na,'lower':lower,'upper':upper,
                       'trim_relative':trim_relative,'trimmed_coefficient_l1':self.trimmed_l1,'factor_power':float(self.factor_power),'coefficient_dtype':str(coeff.dtype),'numeric_mantissa_bits':np.finfo(self.dtype).nmant,
                       'input_value_scale':self.value_scale,
                       'last_radial_modes_l1':float(np.sum(np.abs(coeff[-3:,:]))),
                       'last_angular_modes_l1':float(np.sum(np.abs(coeff[:,-3:])))}

    @lru_cache(maxsize=None)
    def partial_coefficients(self,a,b):
        return chebder(chebder(self.coefficients,m=a,axis=0),m=b,axis=1)/self.half**a

    def evaluate(self,s,z,ds=0,dz=0):
        s,z=np.broadcast_arrays(np.asarray(s,dtype=self.dtype),np.asarray(z,dtype=self.dtype))
        R=np.sqrt(s+z*z)
        if np.any(R<self.lower*(1-2e-13)) or np.any(R>self.upper*(1+2e-13)):
            raise ValueError('evaluation outside its independently projected shell')
        mu=z/R;x=(R-self.mid)/self.half;out=np.zeros_like(R);cache={}
        for (p,q,a,b),factor in chain_operator(ds,dz):
            if (a,b) not in cache:
                value=np.zeros_like(R);falling=self.dtype(1)
                for k in range(a+1):
                    if k:falling*=(-self.factor_power-k+1)
                    if falling:
                        value+=comb(a,k)*falling*R**(-self.factor_power-k)*chebval2d(x,mu,self.partial_coefficients(a-k,b))
                cache[a,b]=value
            out+=factor*R**p*mu**q*cache[a,b]
        return out

    def jet(self,s,z,order):
        return {(a,b):self.evaluate(s,z,a,b) for a in range(order+1) for b in range(order+1-a)}


def extended_values(expansion,s,z):
    """Value-only evaluation of the original finite sum in long double.

    This is independent of the scalar derivative recurrence. Coefficients and
    exponents retain the exact binary values in the saved float64 artifact.
    """
    dtype=np.longdouble;s,z=np.broadcast_arrays(np.asarray(s,dtype=dtype),np.asarray(z,dtype=dtype))
    rho=dtype(expansion.length)**2+s+z*z;out=np.zeros_like(rho)
    for term in expansion.terms:
        c=dtype(term.coefficient);beta=dtype(term.beta)
        if expansion.kernel=='power':
            out+=c*(s/rho)**term.i*(z/np.sqrt(rho))**term.j*rho**(dtype(term.i)+dtype(term.j)/2-beta)
        else:out+=c*s**term.i*z**term.j*np.exp(-beta*(s+z*z))
    return out


def project_shell(field,lower,upper,*,extended=False,**kwargs):
    def values(scalar):
        if extended:return lambda s,z:extended_values(scalar,s,z)
        return lambda s,z:scalar.evaluate(s,z)
    dtype=np.longdouble if extended else np.float64
    phi=ShellProjection(values(field.phi),lower,upper,factor_power=field.alpha,numeric_dtype=dtype,**kwargs)
    q=ShellProjection(values(field.q),lower,upper,factor_power=field.alpha+1,numeric_dtype=dtype,**kwargs)
    return PotentialField(phi,q,field.c_l)
