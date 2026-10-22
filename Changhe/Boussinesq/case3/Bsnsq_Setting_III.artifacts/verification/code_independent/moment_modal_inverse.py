"""Independent whole-plane inverse with the exact second-mode strain moment.

Only verifier modules are used. Sources retain their separate native bases.
"""
from fractions import Fraction
import numpy as np
from scipy.integrate import quad_vec
from adaptive_modal_inverse import AdaptiveModalInverse


def exact_moment2(field,native=False):
    f=field.seed_field if native else field
    knots=f.knots; d=f.degree; raw=np.asarray(f.rawG).reshape(f.K,f.nb)
    moment=Fraction(0)
    for k,sign in [(1,1),(3,-1)]:
        if k>=f.K: continue
        for j in range(k//2,f.nb):
            weight=(Fraction(float(knots[j+d+1]))-Fraction(float(knots[j])))/(d+1)
            moment+=sign*Fraction(float(raw[k,j]))*weight
    return Fraction(float(f.bb))*Fraction(float(f.L))*moment/2


class R2DifferentiableModes:
    def __init__(self,state,native=False):
        self.field=state.seed_field if native else state
        self.spline=self.field.spline if native else state.Gs
        self.derivative_spline=self.spline.derivative()
        self.count=self.field.K
    def both(self,r):
        r=float(r); f=self.field; bb=f.bb; L=f.L
        lz=-np.log1p((r/L)**2)/(2*bb); zeta=np.exp(lz); t=-np.expm1(lz)
        dl=-r/(bb*(L*L+r*r)); dt=-zeta*dl
        D=np.exp((bb+1)*lz); S=self.spline(t); St=self.derivative_spline(t)
        odd=r/np.hypot(r,L); od=L*L/(r*r+L*L)**1.5
        a=D*S; ar=D*(St*dt+(bb+1)*dl*S)
        ar[1::2]=ar[1::2]*odd+D*S[1::2]*od
        a[1::2]*=odd
        def angular(v):
            w=np.zeros(self.count);w[0]=v[0]
            for k in range(1,self.count):
                w[k]+=.5*v[k]
                if k>=2:w[k-2]-=.5*v[k]
            return w
        aa=angular(a)
        return r*aa,aa+r*angular(ar)
    def __call__(self,r):
        r=float(r);a=np.asarray(self.field.radial(r));w=np.zeros(self.count);w[0]=a[0]
        for k in range(1,self.count):
            w[k]+=.5*a[k]
            if k>=2:w[k-2]-=.5*a[k]
        return r*w
    def derivative(self,r):return self.both(r)[1]


class MomentModalInverse(AdaptiveModalInverse):
    def __init__(self,modes,count,settings,moment2,breakpoints=()):
        super().__init__(modes,count,settings)
        if count<2:raise ValueError('Moment formulation requires at least two modes')
        self.moment2=float(moment2)
        self.breakpoints=np.unique(np.asarray(breakpoints,dtype=float))
    def radial(self,r):
        r=float(r)
        if r<=0:raise ValueError('positive radius required')
        if r in self.cache:return self.cache[r]
        n=self.n;st=self.settings
        def inner(t):
            z=t*t;H=np.asarray(self.modes(r*z))
            return np.r_[z**(n+1)*H,H[0],H[1]/z]*(2*t)
        bp=self.breakpoints
        ip=np.sqrt(bp[(bp>0)&(bp<r)]/r)
        iv,ie,ii=quad_vec(inner,0.,1.,points=ip,epsabs=st.epsabs/r,
            epsrel=st.epsrel,limit=st.limit,full_output=True)
        beta=1/st.decay
        def outer(t):
            q=t**beta;H=np.asarray(self.modes(r/q))[2:]
            return beta*t**(beta*(n[2:]-2)-1)*H
        op=(r/bp[bp>r])**st.decay
        if len(n)>2:
            ov,oe,oi=quad_vec(outer,0.,1.,points=op,epsabs=st.epsabs/r,
                epsrel=st.epsrel,limit=st.limit,full_output=True)
            outer_info={'outer_success':bool(oi.success),'outer_status':int(oi.status),
                'outer_message':str(oi.message),'outer_neval':int(oi.neval)}
        else:
            ov=np.array([]);oe=0.;outer_info={'outer_success':True,'outer_status':0,
                'outer_message':'No modes above2','outer_neval':0}
        A=iv[:-2];C=iv[-2];I2=iv[-1];out2=self.moment2-I2
        pr=np.empty(self.count);dp=np.empty(self.count)
        pr[0]=r*.5*(A[0]-C);dp[0]=-r*.5*(A[0]+C)
        pr[1]=r*.25*(A[1]+out2);dp[1]=r*.5*(-A[1]+out2)
        pr[2:]=r/(2*n[2:])*(A[2:]+ov);dp[2:]=r*.5*(-A[2:]+ov)
        self.cache[r]=(pr,dp)
        self.evidence.append({'r':r,'inner_error_estimate':float(ie),'outer_error_estimate':float(oe),
            'inner_success':bool(ii.success),'inner_status':int(ii.status),
            'inner_message':str(ii.message),'inner_neval':int(ii.neval),
            'inner_breakpoints':len(ip),'outer_breakpoints':len(op),
            'moment2':self.moment2,'inner_moment2':float(I2),'outer_moment2':float(out2),**outer_info})
        return pr,dp
