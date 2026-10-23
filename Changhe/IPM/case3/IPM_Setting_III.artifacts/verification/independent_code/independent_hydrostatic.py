"""Independent analytic Cartesian Q jets and complete hydrostatic vertical inverse.
Derivation is in research/independent_hydrostatic_evaluator/PROOF.md.
No producer modules are imported. All quadrature is one-threaded.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from fractions import Fraction as F
from functools import lru_cache
import numpy as np
import gmpy2
from scipy.special import roots_legendre,roots_jacobi


class CartesianQJet:
    def __init__(self,q):
        self.q=q;self.p=q.p;self.M=q.M;self.P=q.kappa
        self.d1=[np.polynomial.chebyshev.chebder(c)for c in q.coeff]
        self.d2=[np.polynomial.chebyshev.chebder(c,2)for c in q.coeff]
        self.a=float(q.polynomial(0,np.array(-1.)))
    def jet(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));r=np.hypot(x,y);t,sig,w=self.q.coordinates(r)
        c=np.divide(x,r,out=np.ones_like(r),where=r>0);s=np.divide(y,r,out=np.zeros_like(r),where=r>0)
        angular=(c+1j*s)**2;power=np.ones_like(angular)
        B=np.zeros_like(r);Bt=B.copy();Btt=B.copy();Ba=B.copy();Baa=B.copy();Bta=B.copy()
        for k,cc in enumerate(self.q.coeff):
            fac=2/(1-self.q.tk[k])if self.q.basis=='local'else 1.
            z=(2*t-1-self.q.tk[k])/(1-self.q.tk[k])if self.q.basis=='local'else t
            b=np.polynomial.chebyshev.chebval(z,cc)
            d=fac*np.polynomial.chebyshev.chebval(z,self.d1[k]);dd=fac*fac*np.polynomial.chebyshev.chebval(z,self.d2[k])
            sk=sig**k;v=sk*b;vt=sk*d;vtt=sk*dd
            if k:vt+=.5*k*sig**(k-1)*b;vtt+=k*sig**(k-1)*d
            if k>1:vtt+=.25*k*(k-1)*sig**(k-2)*b
            ca=power.real;sa=power.imag
            B+=v*ca;Bt+=vt*ca;Btt+=vtt*ca;Ba-=2*k*v*sa;Baa-=4*k*k*v*ca;Bta-=2*k*vt*sa
            power*=angular
        H=w*B;Ht=w*Bt-B/2;Htt=w*Btt-Bt;Ha=w*Ba;Haa=w*Baa;Hta=w*Bta-Ba/2
        Q=w+2*self.P*sig;T=4*sig*w/Q;Tz=8*sig*w*((1-2*sig)*Q-sig*w*(2*self.P-1))/Q**3
        Hz=T*Ht;Hzz=T*T*Htt+Tz*Ht;Hza=T*Hta
        rho=y*H;gx=s*c*Hz-s*s*Ha;gy=H+s*s*Hz+s*c*Ha
        gxx=np.divide(s,r,out=np.zeros_like(r),where=r>0)*(c*c*Hzz+(s*s-c*c)*Hz-2*s*c*Hza+s*s*Haa+2*s*c*Ha)
        rho=np.where(y==0,0.,rho);gx=np.where((x==0)|(y==0),0.,gx);gxx=np.where(y==0,0.,gxx);gy=np.where(r==0,self.a,gy)
        return np.stack([rho,gx,gy,gxx],axis=-1)


@lru_cache(None)
def finite_rule(order):return roots_legendre(order)
@lru_cache(None)
def tail_rule(order,p):
    x,w=roots_jacobi(order,0.,-float(p));return (x+1)/2,w*2**(float(p)-1)


def finite_nodes(lo,hi,order,scale=1.):
    if hi<=lo:return np.empty(0),np.empty(0)
    # Fixed physical cuts, independent of producer nodes; resolve a finite inner scale.
    cuts=[float(lo),float(hi)]
    for v in np.r_[0.,.015625,.03125,.0625,.125,.25,.5,1.,2.,4.]*scale:
        if lo<v<hi:cuts.append(float(v))
    v=max(4*scale,np.finfo(float).tiny)
    while v<hi:
        if v>lo:cuts.append(float(v))
        v*=2
    cuts=np.unique(cuts);a=cuts[:-1];b=cuts[1:];z,w=finite_rule(order)
    return (a[:,None]+(b-a)[:,None]*(z[None,:]+1)/2).ravel(),((b-a)[:,None]*w[None,:]/2).ravel()


def validate_inverse_options(order,tail_order,split,inner_scale):
    for name,value in [('order',order),('tail_order',tail_order)]:
        if isinstance(value,(bool,np.bool_)) or not isinstance(value,(int,np.integer)) or value<1:
            raise ValueError(name+' must be a positive integer')
    if not np.isfinite(split) or split<1:
        raise ValueError('split must be finite and at least 1')
    if not np.isfinite(inner_scale) or inner_scale<=0:
        raise ValueError('inner_scale must be finite and positive')


class VerticalInverse:
    def __init__(self,jet,p,order=20,tail_order=96,tail_scale=32.,inner_scale=1.):
        if not 0<p<1:raise ValueError('An integrable Jacobi tail requires 0<p<1')
        validate_inverse_options(order,tail_order,tail_scale,inner_scale)
        self.jet=jet;self.p=float(p);self.order=order;self.tail_order=tail_order;self.tail_scale=tail_scale;self.inner_scale=inner_scale
    def at(self,x,y):
        x=float(x);y=float(y);xx=abs(x);yy=abs(y);sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
        R=self.tail_scale*max(self.inner_scale,xx,yy,1.)
        inner,iw=finite_nodes(0.,yy,self.order,self.inner_scale);outer,ow=finite_nodes(yy,R,self.order,self.inner_scale)
        v,vw=tail_rule(self.tail_order,self.p);tails=R/v;weights=vw*R*v**(self.p-2)
        jt=self.jet(xx,tails);jo=self.jet(xx,outer);ji=self.jet(xx,inner)
        Ix=float(np.dot(ow,jo[:,1])+np.dot(weights,jt[:,1]));Ixx=float(np.dot(ow,jo[:,3])+np.dot(weights,jt[:,3]))
        Jx=float(np.dot(iw*inner,ji[:,1]));Jxx=float(np.dot(iw*inner,ji[:,3]))
        V1=-sx*Ix;V2=sy*(Jxx+yy*Ixx);Phi=sx*sy*(Jx+yy*Ix)
        # Exact parity values at axes, without dividing by their residual denominators.
        if x==0:V1=0.;Phi=0.
        if y==0:V2=0.;Phi=0.
        return dict(V=[V1,V2],Phi=Phi,dV2_dy=Ixx,tail_V=[float(-sx*np.dot(weights,jt[:,1])),float(sy*yy*np.dot(weights,jt[:,3]))],R_split=R,finite_order=self.order,tail_order=self.tail_order)
    def center(self):return self.at(0.,0.)['dV2_dy']


def exact_hydrostatic_center(coeff,P):
    """Exact Chebyshev product and integral; returns Fraction including every mode."""
    Q=gmpy2.mpq
    def exact(v):
        if isinstance(v,F):return Q(v.numerator,v.denominator)
        if isinstance(v,Q):return v
        a,b=float(v).as_integer_ratio();return Q(a,b)
    P=exact(P)
    def linear(poly,a,b):
        out=[Q(0)]*(len(poly)+1)
        for n,v in enumerate(poly):
            out[n]+=a*v
            if n==0:out[1]+=b*v
            else:out[n-1]+=b*v/2;out[n+1]+=b*v/2
        return out
    a=sum(((-1)**j*exact(v)for j,v in enumerate(coeff[0])),Q(0));out=-a
    for k,row in enumerate(coeff[1:],1):
        poly=list(map(exact,row))
        for j in range(k-1):poly=linear(poly,Q(1,2),Q(1,2))
        poly=linear(poly,(1+2*P)/2,(2*P-1)/2)
        integ=sum((2*v/(1-n*n)for n,v in enumerate(poly)if n%2==0),Q(0))
        out-=k*k*(-1)**k*integ
    return F(int(out.numerator),int(out.denominator))


def quadrature_hydrostatic_center(q,order):
    t,weights=finite_rule(order);sig=(1+t)/2;Q=(1-t)/2+2*q.kappa*sig
    vals=np.zeros_like(t)
    for k in range(1,q.M):vals-=k*k*(-1)**k*Q*sig**(k-1)*q.polynomial(k,t)
    return -float(q.polynomial(0,np.array(-1.)))+float(np.dot(weights,vals))


class AnisotropicRegauge:
    def __init__(self,original,a,K):
        if a<=0 or K<=0:raise ValueError('This comparison requires a>0,K>0')
        self.original=original;self.a=a;self.h=np.sqrt(a);self.length=(a/K)**original.P;self.p=original.p
    def jet(self,x,y):
        f=self.original.jet(self.h*np.asarray(x)/self.length,np.asarray(y)/self.length)
        return f*np.array([self.length/self.a,1/self.h,1/self.a,1/self.length])
