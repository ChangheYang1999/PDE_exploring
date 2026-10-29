"""Precomputed derivative polynomials for a canonical two-series potential."""
from math import comb, factorial
import numpy as np
from audit_t1_deformation import RationalT1

ORDERS = ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))

class FastTwoSeries(RationalT1):
    def __init__(self, meta):
        self.meta=meta; self.c_l=float(meta['c']); self.p=1/(2*self.c_l); self.aspect=float(meta['a'])
        self.terms=[]; coeff={}; powers=set()
        for series, poly in enumerate(meta['polynomials'], 1):
            for j,k,C in poly:
                j,k=int(j),int(k); C=float(C); d=series*self.p+j+k
                self.terms.append((C*self.aspect**j,j,k,d,self.aspect,1.,series-1))
                for order,(A,B) in enumerate(ORDERS):
                    for i in range(min(A,j)+1):
                        for l in range(min(B,k)+1):
                            h=A+B-i-l; rising=1.
                            for q in range(h):rising*=d+q
                            value=C*comb(A,i)*comb(B,l)*factorial(j)/factorial(j-i)*factorial(k)/factorial(k-l)*(-1)**h*rising
                            key=(series-1,order,j-i,k-l)
                            coeff[key]=coeff.get(key,0.)+value; powers.add((j-i,k-l))
        self.powers=sorted(powers); self.matrix=np.zeros((2,len(ORDERS),len(self.powers)))
        for (series,order,j,k),value in coeff.items():self.matrix[series,order,self.powers.index((j,k))]=value
        self._jet_cache=None
        self.ps=float(self.F(0.,0.,1,0)); self.pz=float(self.F(0.,0.,0,1))
        if abs(float(self.F(0.,0.))-.5)>1e-13:raise ValueError('source strain')

    def all_F(self,s,t):
        s,t=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(t,dtype=float))
        if self._jet_cache is not None:
            old_s,old_t,old=self._jet_cache
            if np.array_equal(s,old_s) and np.array_equal(t,old_t):return old
        shape=s.shape; sf=s.ravel(); tf=t.ravel(); u=1+self.aspect*sf+tf; v=self.aspect*sf/u; w=tf/u
        monomials=np.stack([v**j*w**k for j,k in self.powers])
        polynomials=(self.matrix.reshape(2*len(ORDERS),-1)@monomials).reshape(2,len(ORDERS),len(sf))
        out={}
        for n,(A,B) in enumerate(ORDERS):
            out[A,B]=(self.aspect**A*(u**(-self.p-A-B)*polynomials[0,n]+u**(-2*self.p-A-B)*polynomials[1,n])).reshape(shape)
        self._jet_cache=(s.copy(),t.copy(),out)
        return out

    def F(self,s,t,ds=0,dt=0):
        if (ds,dt) not in ORDERS:raise ValueError('only derivatives through total order two')
        return self.all_F(s,t)[ds,dt]
