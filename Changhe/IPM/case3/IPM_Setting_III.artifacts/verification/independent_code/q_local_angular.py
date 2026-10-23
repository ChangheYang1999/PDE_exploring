"""Shifted-basis input to the independent infinite Green quadrature.
No producer source is imported. All derivatives are scalar polynomial derivatives.
"""
import math
import numpy as np
from scipy.special import roots_legendre
from q_local_checkpoint import QLocalCheckpoint
from log_radius_inverse import LogRadiusQCheckpoint
from angular_log_inverse import endpoint_quotient
from complementary_inverse_charts import ComplementaryQ


class LocalAngular:
    coordinates_log=LogRadiusQCheckpoint.coordinates_log
    stable_coordinates=ComplementaryQ.stable_coordinates
    def __init__(self,path_or_reader):
        q=path_or_reader if isinstance(path_or_reader,QLocalCheckpoint) else QLocalCheckpoint(path_or_reader)
        self.scalar=q
        for key in ['N','M','cl','L','kappa','coeff']:setattr(self,key,getattr(q,key))
        self.polynomial=q.polynomial;self.polynomial_derivative=q.polynomial_derivative
        self.log_core=math.log(self.L)-self.kappa*math.log(2.)
        # Mode zero is unshifted since t_0=-1 exactly.
        assert q.tk[0]==-1
        self.a,self.quotient,self.quotient_rounding_l1=endpoint_quotient(self.coeff[0])
        g,w=roots_legendre(max(48,(self.N+6)//2));self.pnodes=(g+1)/2;self.pweights=w/2
        self.c=-self.a/4+float(self.third_primitive(np.array([1.]))[0])

    def third_primitive(self,s):
        s=np.asarray(s,float);v=s[...,None]*self.pnodes;t=2*v-1
        f=((1-v)/4+self.kappa*v/2)*(self.polynomial(1,t)-v*self.polynomial(2,t))
        return s*np.sum(f*self.pweights,axis=-1)

    def beta2_defect(self,logr):
        _,s=self.coordinates_log(logr);return -self.third_primitive(s)

    def full_beta2(self,logr):
        _,_,w=self.stable_coordinates(logr);v=w[...,None]*self.pnodes;u=1-v;t=1-2*v
        f=(v/4+self.kappa*u/2)*(self.polynomial(1,t)-u*self.polynomial(2,t))
        return w*np.sum(f*self.pweights,axis=-1)

    def mode(self,logr,k,derivative,defect):
        logr=np.asarray(logr,float)
        if k>=self.M:
            z=np.zeros_like(logr);return (z,z) if derivative else z
        t,s,w=self.stable_coordinates(logr)
        b=self.polynomial(k,t);c=self.polynomial(k+1,t)
        if k==0:
            if defect:
                div=np.polynomial.chebyshev.chebval(t,self.quotient)
                value=s*(2*w*div-self.a-w*c/2)
            else:value=w*(b-s*c/2)
        else:value=.5*w*s**k*(b-s*c)
        if not derivative:return value
        bt=self.polynomial_derivative(k,t);ct=self.polynomial_derivative(k+1,t)
        if k==0:d=-b+2*w*bt-((1-2*s)*c+2*s*w*ct)/2
        else:d=((k*w-s)*s**(k-1)*(b-s*c)+w*s**k*(2*bt-c-2*s*ct))/2
        return value,d*(2*s*w/(w+2*self.kappa*s))

    def h_mode(self,logr,k,derivative=False):return self.mode(logr,k,derivative,True)
    def full_mode(self,logr,k,derivative=False):return self.mode(logr,k,derivative,False)
