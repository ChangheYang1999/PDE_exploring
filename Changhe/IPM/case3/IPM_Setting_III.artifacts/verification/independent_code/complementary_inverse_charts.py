"""Stable full and defect charts, independently derived before tests.

No producer code, derivative matrix or velocity matrix is imported.
"""
import math
from fractions import Fraction as F
from q_exact_jets import chebyshev_in_sigma
import numpy as np
from scipy.special import roots_legendre
from angular_log_inverse import QAngular,AngularLogInverse,endpoint_quotient
from evaluate_smooth_state import ReconstructedSmooth


class FullChart:
    def __init__(self,owner):
        self.owner=owner;self.M=owner.M;self.cl=owner.cl
        self.a=0.;self.c=0.;self.log_core=owner.log_core
    def h_mode(self,logr,index,derivative=False):return self.owner.full_mode(logr,index,derivative)
    def beta2_defect(self,logr):return self.owner.full_beta2(logr)


class ComplementaryQ(QAngular):
    def stable_coordinates(self,logr):
        logr=np.asarray(logr,float);t,s=self.coordinates_log(logr)
        logw=(self.log_core-logr+.5*np.log(np.maximum(s,np.finfo(float).tiny)))/self.kappa
        w=np.where(s<.5,1-s,np.exp(np.minimum(logw,0.)))
        return t,s,w
    def full_mode(self,logr,j,derivative=False):
        logr=np.asarray(logr,float)
        if j>=self.M:
            z=np.zeros_like(logr);return (z,z) if derivative else z
        t,s,w=self.stable_coordinates(logr)
        B=self.polynomial(j,t);C=self.polynomial(j+1,t)
        if j==0:val=w*(B-s*C/2)
        else:val=.5*w*s**j*(B-s*C)
        if not derivative:return val
        Bt=np.polynomial.chebyshev.chebval(t,self.dcoeff[j])
        Ct=np.polynomial.chebyshev.chebval(t,self.dcoeff[j+1]) if j+1<self.M else np.zeros_like(t)
        if j==0:der=-B+2*w*Bt-((1-2*s)*C+2*s*w*Ct)/2
        else:der=((j*w-s)*s**(j-1)*(B-s*C)+w*s**j*(2*Bt-C-2*s*Ct))/2
        return val,der*(2*s*w/(w+2*self.kappa*s))
    def full_beta2(self,logr):
        _,_,w=self.stable_coordinates(logr)
        v=w[...,None]*self.pnodes;u=1-v;t=1-2*v
        f=(v/4+self.kappa*u/2)*(self.polynomial(1,t)-u*self.polynomial(2,t))
        return w*np.sum(f*self.pweights,axis=-1)


class SmoothAngular:
    def __init__(self,path):
        self.scalar=ReconstructedSmooth(path);s=self.scalar
        self.N=s.N;self.M=s.M;self.cl=s.cl;self.L=s.L;self.alpha=s.a;self.coeff=s.coeff
        self.polynomial=s.polynomial;self.log_core=math.log(self.L)
        self.a,self.quotient,self.quotient_rounding_l1=endpoint_quotient(self.coeff[0])
        self.dcoeff=[np.polynomial.chebyshev.chebder(c) for c in self.coeff]
        x,w=roots_legendre(max(48,2*self.N+12));self.pnodes=(x+1)/2;self.pweights=w/2
        alpha=F(float(self.alpha))
        powers=[]
        for j in [1,2]:
            cc=self.coeff[j] if j<self.M else [0.]
            powers.append(chebyshev_in_sigma([(-1)**k*F(float(v)) for k,v in enumerate(cc)]))
        p1,p2=powers
        integral=sum((v/F(k+1) for k,v in enumerate(p1)),F(0))-sum((v/F(k+1) for k,v in enumerate(p2)),F(0))+sum((v/(F(k+1)+1/alpha) for k,v in enumerate(p2)),F(0))
        self.exact_a=sum(((-1)**k*F(float(v)) for k,v in enumerate(self.coeff[0])),F(0))
        self.exact_c=-self.exact_a/4+integral/(4*alpha)
        self.c=float(self.exact_c)
    def coordinates(self,logr):
        z=np.asarray(logr,float)-self.log_core
        ld=np.logaddexp(0.,2*z);s=-np.expm1(-ld)
        w=np.exp(-self.alpha*ld);tau=-np.expm1(-self.alpha*ld)
        return -1+2*tau,s,w,tau,np.exp(-ld)
    def _primitive(self,width,upper):
        width=np.asarray(width,float)
        v=1-width[...,None]*self.pnodes if upper else width[...,None]*self.pnodes
        t=1-2*v;sig=-np.expm1(np.log(v)/self.alpha)
        f=self.polynomial(1,t)-sig*self.polynomial(2,t)
        return width*np.sum(f*self.pweights,axis=-1)/(4*self.alpha)
    def full_beta2(self,logr):
        _,_,w,_,_=self.coordinates(logr);return self._primitive(w,False)
    def beta2_defect(self,logr):
        _,_,_,tau,_=self.coordinates(logr);return -self._primitive(tau,True)
    def _mode(self,logr,j,derivative,defect):
        logr=np.asarray(logr,float)
        if j>=self.M:
            z=np.zeros_like(logr);return (z,z) if derivative else z
        t,s,w,tau,one_minus_s=self.coordinates(logr)
        B=self.polynomial(j,t);C=self.polynomial(j+1,t)
        if j==0:
            if defect:val=tau*(2*w*np.polynomial.chebyshev.chebval(t,self.quotient)-self.a)-w*s*C/2
            else:val=w*(B-s*C/2)
        else:val=w*s**j*(B-s*C)/2
        if not derivative:return val
        Bt=np.polynomial.chebyshev.chebval(t,self.dcoeff[j]);Ct=np.polynomial.chebyshev.chebval(t,self.dcoeff[j+1]) if j+1<self.M else np.zeros_like(t)
        ds=2*s*one_minus_s;dw=-2*self.alpha*s*w;dt=-2*dw
        if j==0:der=dw*(B-s*C/2)+w*(Bt*dt-ds*C/2-s*Ct*dt/2)
        else:
            der=(dw*s**j+w*j*s**(j-1)*ds)*(B-s*C)/2+w*s**j*(Bt*dt-ds*C-s*Ct*dt)/2
        return val,der
    def h_mode(self,logr,j,derivative=False):return self._mode(logr,j,derivative,True)
    def full_mode(self,logr,j,derivative=False):return self._mode(logr,j,derivative,False)


def point_fields(model,logr,theta,order=128,chart='auto'):
    logr=np.asarray(logr,float);theta=np.asarray(theta,float)
    assert logr.shape==theta.shape
    use_defect=logr<=model.log_core if chart=='auto' else np.full(logr.shape,chart=='defect')
    out=[None]*len(logr)
    for defect in [True,False]:
        owner=model if defect else FullChart(model)
        inverse=AngularLogInverse(owner,order)
        for th in np.unique(theta[use_defect==defect]):
            ids=np.flatnonzero((use_defect==defect)&(theta==th))
            fields=inverse.fields(logr[ids],np.array([th]))
            for j,k in enumerate(ids):
                v={name:float(val[j,0]) for name,val in fields.items()}
                sine=math.sin(th);cosine=math.cos(th)
                rho=v['H']+owner.a*sine
                rr=v['Fr']+owner.a*(owner.cl+owner.c-1)*sine
                gx=v['grad_radial']*cosine-v['grad_angular']*sine
                gy=v['grad_radial']*sine+v['grad_angular']*cosine
                ux=v['ur']*cosine-v['ut']*sine;uy=v['ur']*sine+v['ut']*cosine
                tx=(model.cl*cosine+ux)*gx;ty=(model.cl*sine+uy)*gy
                nf=abs(tx)+abs(ty)+abs(rho)
                nv=abs(rho)+abs(cosine*gx+sine*gy)+abs(ux*gx+uy*gy)
                out[k]=dict(log_radius=float(logr[k]),theta=float(th),chart='defect' if defect else 'full',rho_over_r=rho,U_over_r=[ux,uy],gradient=[gx,gy],R_over_r=rr,Nf_over_r=nf,Nv_over_r=nv,R_Nf=abs(rr)/nf if nf else None,R_Nv=abs(rr)/nv if nv else None,strain=v['strain'])
    return out
