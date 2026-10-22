"""Independent reader of the formulas documented in NUM_REPORT.md.

No numerics-lane source is imported. SciPy evaluates the serialized clamped
B-spline coefficients. Differentiation and inverse use the verifier's code.
This reader is for snapshots, which are not submitted successful candidates.
"""
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline

class NumericsState:
    def __init__(self,path,representation="multiplicative"):
        if representation not in ("multiplicative","masked"):
            raise ValueError("unknown representation version")
        self.representation=representation
        with np.load(path,allow_pickle=False) as z:
            self.meta={k:z[k].item() for k in z.files if z[k].ndim==0}
            self.cf=z['cF'].copy();self.cg=z['cG'].copy()
        self.beta=float(self.meta['beta']);self.bb=float(self.meta['beta_basis'])
        self.L=float(self.meta['L']);self.K=int(self.meta['K'])
        self.degree=int(self.meta['deg']);self.Nt=int(self.meta['Nt'])
        self.grade=float(self.meta['grade']);self.mreg=int(self.meta['mreg'])
        breakpoints=np.linspace(0,1,self.Nt+1)**self.grade
        self.knots=np.r_[np.zeros(self.degree),breakpoints,np.ones(self.degree)]
        self.nb=len(self.knots)-self.degree-1
        if len(self.cf)!=self.K*self.nb or len(self.cg)!=self.K*self.nb:
            raise ValueError('serialized dimensions disagree with documented knots')
        self.m=np.minimum(np.arange(self.K),self.mreg)
        cf=self.cf.reshape(self.K,self.nb).copy();cg=self.cg.reshape(self.K,self.nb).copy()
        if representation=='masked':
            for k in range(self.K):
                cf[k,:self.m[k]]=0;cg[k,:self.m[k]]=0
        self.Fs=BSpline(self.knots,cf.T,self.degree,extrapolate=False)
        self.Gs=BSpline(self.knots,cg.T,self.degree,extrapolate=False)

    def divided(self,x,y,kind):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
        shape=x.shape;x=x.ravel();y=y.ravel();r=np.hypot(x,y)
        # expm1 preserves the center's small radial coordinate.
        log_tail=-np.log1p(r/self.L)/self.bb
        t=-np.expm1(log_tail)
        one_minus_t=np.exp(log_tail)
        eta=np.divide(-y,r,out=np.zeros_like(y),where=r!=0)
        eta=np.clip(eta,-1,1)
        angular=np.empty((len(r),self.K));angular[:,0]=1
        if self.K>1:angular[:,1]=eta
        for k in range(2,self.K):angular[:,k]=2*eta*angular[:,k-1]-angular[:,k-2]
        spline=self.Fs if kind=='F' else self.Gs
        power=self.bb+(2 if kind=='F' else 1)
        radial=spline(t)*one_minus_t[:,None]**power
        if self.representation=='multiplicative':
            radial*=t[:,None]**self.m[None,:]
        return np.sum(radial*angular,axis=1).reshape(shape)

    def theta(self,x,y):
        return np.asarray(x)**2*self.divided(x,y,'F')

    def omega(self,x,y):
        return np.asarray(x)*self.divided(x,y,'G')

    def origin_audit(self):
        output={}
        for name,coeff,power in [('F',self.cf,self.bb+2),('G',self.cg,self.bb+1)]:
            c=coeff.reshape(self.K,self.nb)
            d0=self.degree*(c[0,1]-c[0,0])/self.knots[self.degree+1]
            linear=(d0-power*c[0,0])/(self.bb*self.L)
            output[name]={'value_at_origin':float(c[0,0]),'mode_zero_linear_r_coefficient':float(linear),
                         'leading_high_mode_r_squared_documented_formula_only':{str(k):float(c[k,0]/(self.bb*self.L)**2) for k in range(3,self.K)}}
        output['Theta_xxx_one_sided_predicted']=[-6*output['F']['mode_zero_linear_r_coefficient'],6*output['F']['mode_zero_linear_r_coefficient']]
        output['Omega_xx_one_sided_predicted']=[-2*output['G']['mode_zero_linear_r_coefficient'],2*output['G']['mode_zero_linear_r_coefficient']]
        output['a0_error']=output['F']['value_at_origin']-1
        output['b0_error']=output['G']['value_at_origin']-4/self.beta
        return output
