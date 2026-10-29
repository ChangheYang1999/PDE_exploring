"""Independent Taylor evaluation of the lead's documented decaying T2 family."""
from math import factorial
import numpy as np
from independent_fields import PotentialField
from piecewise_adapter import Taylor2

class SeedScalar:
    length=1.
    def __init__(self,owner,name):self.owner,self.name=owner,name
    def jet(self,s,z,order):return self.owner.jets(s,z,order)[self.name]
    def evaluate(self,s,z,ds=0,dz=0):return self.jet(s,z,ds+dz)[ds,dz]

class RingSeedField(PotentialField):
    def __init__(self,parameters):
        self.parameters=dict(parameters);self.cache=None
        super().__init__(SeedScalar(self,'phi'),SeedScalar(self,'q'),float(parameters['c']))
    def jets(self,s,z,order):
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float));shape=s.shape
        if self.cache is not None:
            ss,zz,oo,old=self.cache
            if order<=oo and np.array_equal(s,ss) and np.array_equal(z,zz):return old
        alg=Taylor2(order,s.size);sj=alg.variable(s.ravel(),(1,0));zj=alg.variable(z.ravel(),(0,1));one=alg.constant(1.)
        rho=sj+alg.multiply(zj,zj)
        def integer_power(value,n):
            out=one.copy()
            for _ in range(n):out=alg.multiply(out,value)
            return out
        p=self.parameters;c=self.c_l;A=float(p['Finf']);B=c+(1+c)/2-A
        F=A*alg.power(one+integer_power(rho/float(p['b']),3),-1/(6*c))+B*alg.power(one+integer_power(rho/float(p['rho1']),int(p['n'])),-1.)
        phi=alg.multiply(zj,F)
        q=float(p['K'])*alg.multiply(alg.multiply(sj,zj),alg.power((one+rho)/2,-(3+1/c)/2))
        out={name:{(a,b):(raw[k]*factorial(a)*factorial(b)).reshape(shape) for k,(a,b) in enumerate(alg.indices)} for name,raw in [('phi',phi),('q',q)]}
        self.cache=(s.copy(),z.copy(),order,out)
        return out
