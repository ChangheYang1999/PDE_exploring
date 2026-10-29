"""Independent Jacobi-ball adapter from the exported mathematical definition.

The ball uses an exact finite binomial expansion, not the solver's recurrence.
Shell/exterior Taylor evaluation is inherited from the independently tested
old adapter. No numerical-lane source code is imported.
"""
from fractions import Fraction
from math import comb
from functools import lru_cache
import numpy as np
from piecewise_adapter import PiecewiseField,Taylor2

@lru_cache(None)
def jacobi_binomial_coefficients(k,n):
    # P_k^(0,n+1/2)(2t-1) = sum_m c_m (t-1)^(k-m) t^m.
    out=[]
    for m in range(k+1):
        v=Fraction(1);top=Fraction(2*(k+n)+1,2)
        for j in range(k-m):v*= (top-j)/Fraction(j+1)
        out.append(float(comb(k,m)*v))
    return tuple(out)

class JacobiPiecewiseField(PiecewiseField):
    format='verifier-independent-piecewise-jacobi-v1'
    def __init__(self,metadata,coefficients,**kwargs):
        if metadata['elements'][0].get('radial')!='jacobi':
            raise ValueError('Jacobi evaluator requires explicit radial=jacobi metadata')
        super().__init__(metadata,coefficients,**kwargs)

    def _element_taylor(self,s,z,order,i):
        if self.elements[i]['kind']!='ball':return super()._element_taylor(s,z,order,i)
        alg=Taylor2(order,len(s));e=self.elements[i];Rb=float(e['Rhi']);sj=alg.variable(s,(1,0));zj=alg.variable(z,(0,1))
        t=(sj+alg.multiply(zj,zj))/Rb**2;angular=alg.legendre(zj/Rb,int(e['nmax']),t)
        kmax=int(max(self.radial_keys[i,'phi'][-1],self.radial_keys[i,'q'][-1]));one=alg.constant(1.);u=t-one
        tp=[one];up=[one]
        for k in range(kmax):tp.append(alg.multiply(tp[-1],t));up.append(alg.multiply(up[-1],u))
        result={key:alg.constant(0.) for key in ['phi','q']}
        for n in range(int(e['nmax'])+1):
            for k in range(kmax+1):
                weights={key:self.matrices[i,key][n,k] for key in result}
                if not any(weights.values()):continue
                rad=sum((v*alg.multiply(up[k-m],tp[m]) for m,v in enumerate(jacobi_binomial_coefficients(k,n))),alg.constant(0.))
                term=alg.multiply(angular[:,n],rad)
                for key,v in weights.items():result[key]+=v*term
        return alg,result
    def dilate(self,L):return JacobiPiecewiseField(self.metadata,self.coefficients,dilation=self.dilation*L,provenance=self.provenance)
