"""Adaptive physical-radius whole-plane inverse, independent of numerics code.

This supplements, rather than replaces, the Cartesian Duffy inverse.
The input supplies angular sine coefficients of Omega around phi, where
X=(r sin(phi), -r cos(phi)). All physical-radius integration uses SciPy's
adaptive Gauss-Kronrod vector quadrature. No saved Green matrices are used.
"""
from dataclasses import dataclass
import numpy as np
from scipy.integrate import quad_vec

@dataclass
class ModalSettings:
    decay: float
    epsabs: float=2e-10
    epsrel: float=2e-10
    limit: int=2000

class AdaptiveModalInverse:
    def __init__(self, modes, count, settings):
        self.modes=modes
        self.count=int(count)
        self.settings=settings
        self.n=np.arange(1,self.count+1,dtype=float)
        self.cache={}
        self.evidence=[]

    def radial(self,r):
        r=float(r)
        if r<=0: raise ValueError('radial evaluation requires r>0')
        if r in self.cache:return self.cache[r]
        n=self.n; st=self.settings
        # sqrt radius mapping gives additional resolution at small physical radii.
        def inner(t):
            z=t*t
            H=np.asarray(self.modes(r*z),dtype=float)
            return np.r_[z**(n+1)*H,H[0]]*(2*t)
        inner_v,inner_e,inner_i=quad_vec(inner,0.,1.,epsabs=st.epsabs/r,
                                      epsrel=st.epsrel,limit=st.limit,full_output=True)
        beta=1/st.decay
        def outer(t):
            q=t**beta
            H=np.asarray(self.modes(r/q),dtype=float)[1:]
            # q^(n-3) dq/dt; n>=2, and the slowest tail is regularized.
            return beta*t**(beta*(n[1:]-2)-1)*H
        out,out_e,out_i=quad_vec(outer,0.,1.,epsabs=st.epsabs/r,
                                epsrel=st.epsrel,limit=st.limit,full_output=True)
        A=inner_v[:-1]; C=inner_v[-1]
        pr=np.empty(self.count); dp=np.empty(self.count)
        pr[0]=r*.5*(A[0]-C); dp[0]=-r*.5*(A[0]+C)
        pr[1:]=r/(2*n[1:])*(A[1:]+out)
        dp[1:]=r*.5*(-A[1:]+out)
        self.cache[r]=(pr,dp)
        self.evidence.append({'r':r,'inner_error_estimate':float(inner_e),
           'outer_error_estimate':float(out_e),'inner_success':bool(inner_i.success),
           'outer_success':bool(out_i.success),'inner_neval':int(inner_i.neval),
           'outer_neval':int(out_i.neval)})
        return pr,dp

    def relative(self,points):
        points=np.asarray(points,dtype=float).reshape(-1,2)
        ans=np.zeros_like(points)
        for i,(x,y) in enumerate(points):
            r=float(np.hypot(x,y))
            if r==0:continue
            pr,dp=self.radial(r)
            phi=np.arctan2(x,-y)
            sn=np.sin(self.n*phi);cs=np.cos(self.n*phi)
            ur=-np.dot(self.n*pr,cs);ut=np.dot(dp,sn)
            ans[i]=[ur*x/r-ut*y/r,ur*y/r+ut*x/r]
        return ans

class R2ModeSource:
    """Exact angular product identities, using the verifier's SciPy reader."""
    def __init__(self,state,external=False,kind=None):
        self.state=state
        self.external=external
        self.kind=kind or ('external' if external else 'G')
        self.count=state.seed_field.K if self.kind=='native_seed' else state.K
    def __call__(self,r):
        s=self.state
        r=float(r)
        # The reader evaluates each source in its explicitly recorded native basis.
        a=np.asarray(s.radial(r,self.kind),dtype=float)
        coeff=np.zeros(self.count)
        coeff[0]+=a[0]
        for k in range(1,len(a)):
            coeff[k]+=.5*a[k]
            if k>=2:coeff[k-2]-=.5*a[k]
        return r*coeff
