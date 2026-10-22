"""Globally fixed harmonic moments plus local Poisson integrals (packet172).

The source reader and all quadrature are the verifier's implementation.
Never fit a harmonic moment to the B2 strain. E alone cannot validate moments.
"""
from dataclasses import dataclass
import numpy as np
from scipy.integrate import quad_vec
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings


def weighted(values,log_factors):
    v=np.asarray(values,float);a=np.asarray(log_factors,float)
    ans=np.zeros_like(v);nonzero=v!=0
    ans[nonzero]=np.sign(v[nonzero])*np.exp(np.log(abs(v[nonzero]))+a[nonzero])
    return ans


class CenterMomentInverse(AdaptiveModalInverse):
    def __init__(self,modes,count,settings,switch=.1,split=1.,exact_M2=None):
        super().__init__(modes,count,settings)
        self.switch=float(switch);self.split=float(split)
        self.moment_evidence={};self.local_evidence=[];self.C=self.global_moments()
        if exact_M2 is not None:
            self.moment_evidence['M2_quadrature']=float(self.C[0])
            self.moment_evidence['M2_exact_rounded']=float(exact_M2)
            self.moment_evidence['M2_quadrature_error_vs_exact_rounded']=float(self.C[0]-float(exact_M2))
            self.C[0]=float(exact_M2)
        self.moment_evidence['scaled_moments']=self.C.tolist()
        self.moment_evidence['definition']='C_n=switch^(n-2) M_n, n>=2; only M2 optionally replaced by the exact rational source moment'

    def global_moments(self):
        n=self.n[1:];ss=self.settings;beta=1/ss.decay
        def inside(t):
            r=self.split*t*t;H=np.asarray(self.modes(r))[1:]
            return weighted(H,(n-2)*np.log(self.switch/r))*(2/t)
        def outside(t):
            r=self.split*t**(-beta);H=np.asarray(self.modes(r))[1:]
            return weighted(H,(n-2)*np.log(self.switch/r))*(beta/t)
        a,e,info=quad_vec(inside,0.,1.,epsabs=ss.epsabs,epsrel=ss.epsrel,limit=ss.limit,full_output=True)
        b,f,info2=quad_vec(outside,0.,1.,epsabs=ss.epsabs,epsrel=ss.epsrel,limit=ss.limit,full_output=True)
        self.moment_evidence.update(inner_error_estimate=float(e),outer_error_estimate=float(f),inner_success=bool(info.success),outer_success=bool(info2.success),inner_neval=int(info.neval),outer_neval=int(info2.neval),split=self.split,switch=self.switch)
        return a+b

    def radial(self,r):
        r=float(r)
        if r>self.switch:return super().radial(r)
        if r<=0:raise ValueError('radial evaluation requires r>0')
        if r in self.cache:return self.cache[r]
        n=self.n;st=self.settings
        def local(t):
            z=t*t;H=np.asarray(self.modes(r*z),float)
            A=z**(n+1)*H
            D=weighted(H[1:],(1-n[1:])*np.log(z))
            return np.r_[A,H[0],D]*(2*t)
        raw,err,info=quad_vec(local,0.,1.,epsabs=st.epsabs/r,epsrel=st.epsrel,limit=st.limit,full_output=True)
        A=raw[:self.count];C1=raw[self.count];D=raw[self.count+1:]
        pr=np.zeros(self.count);dp=np.zeros(self.count)
        pr[0]=r*(A[0]-C1)/2;dp[0]=-r*(A[0]+C1)/2
        harmonic=r*self.C*(r/self.switch)**(n[1:]-2)/2
        pr[1:]=(harmonic+r*(A[1:]-D)/2)/n[1:]
        dp[1:]=harmonic-r*(A[1:]+D)/2
        self.cache[r]=(pr,dp)
        self.local_evidence.append({'r':r,'error_estimate':float(err),'success':bool(info.success),'neval':int(info.neval)})
        return pr,dp
