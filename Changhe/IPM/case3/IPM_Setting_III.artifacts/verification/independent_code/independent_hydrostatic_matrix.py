"""Own Q basis matrices and complete hydrostatic inverse. Result201 PROOF.md.
No producer code. Analytic Cartesian jets from differentiated Chebyshev recurrence.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.special import roots_legendre
from independent_hydrostatic import finite_nodes,tail_rule,validate_inverse_options


def cheb_jet(z,n):
    z=np.asarray(z,float).reshape(-1);v=np.zeros((len(z),n));d=v.copy();dd=v.copy()
    v[:,0]=1
    if n>1:v[:,1]=z;d[:,1]=1
    for j in range(1,n-1):
        v[:,j+1]=2*z*v[:,j]-v[:,j-1]
        d[:,j+1]=2*v[:,j]+2*z*d[:,j]-d[:,j-1]
        dd[:,j+1]=4*d[:,j]+2*z*dd[:,j]-dd[:,j-1]
    return v,d,dd


class HydrostaticBasisMatrices:
    def __init__(self,q):
        self.q=q;self.nu=len(q.u);self.offs=np.r_[0,np.cumsum([len(c)for c in q.coeff])]
    def jet(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.reshape(-1);y=y.reshape(-1)
        r=np.hypot(x,y);t,sig,w=self.q.coordinates(r)
        c=np.divide(x,r,out=np.ones_like(r),where=r>0);s=np.divide(y,r,out=np.zeros_like(r),where=r>0)
        angle=(c+1j*s)**2;power=np.ones_like(angle)
        Q=w+2*self.q.kappa*sig;T=4*sig*w/Q
        Tz=8*sig*w*((1-2*sig)*Q-sig*w*(2*self.q.kappa-1))/Q**3
        result=np.zeros((len(x),4,self.nu))
        for k in range(self.q.M):
            n=self.offs[k+1]-self.offs[k];scale=2/(1-self.q.tk[k])if self.q.basis=='local'else 1.
            z=(2*t-1-self.q.tk[k])/(1-self.q.tk[k])if self.q.basis=='local'else t
            B,Bt,Btt=cheb_jet(z,n);Bt*=scale;Btt*=scale*scale
            sk=sig[:,None]**k;v=sk*B;vt=sk*Bt;vtt=sk*Btt
            if k:vt+=.5*k*sig[:,None]**(k-1)*B;vtt+=k*sig[:,None]**(k-1)*Bt
            if k>1:vtt+=.25*k*(k-1)*sig[:,None]**(k-2)*B
            ca=power.real[:,None];sa=power.imag[:,None];W=w[:,None]
            H=W*v*ca;Ht=(W*vt-v/2)*ca;Htt=(W*vtt-vt)*ca
            Ha=-2*k*W*v*sa;Haa=-4*k*k*W*v*ca;Hta=-2*k*(W*vt-v/2)*sa
            Hz=T[:,None]*Ht;Hzz=T[:,None]**2*Htt+Tz[:,None]*Ht;Hza=T[:,None]*Hta
            C=c[:,None];S=s[:,None]
            G=y[:,None]*H;Gx=S*C*Hz-S*S*Ha;Gy=H+S*S*Hz+S*C*Ha
            Gxx=np.divide(s,r,out=np.zeros_like(r),where=r>0)[:,None]*(C*C*Hzz+(S*S-C*C)*Hz-2*S*C*Hza+S*S*Haa+2*S*C*Ha)
            G[y==0]=0;Gx[(x==0)|(y==0)]=0;Gxx[y==0]=0
            if np.any(r==0):
                Gy[r==0]=0
                if k==0:Gy[r==0]=(-1.)**np.arange(n)
            sl=slice(self.offs[k],self.offs[k+1]);result[:,0,sl]=G;result[:,1,sl]=Gx;result[:,2,sl]=Gy;result[:,3,sl]=Gxx
            power*=angle
        return result
    def velocity(self,x,y,order=20,tail_order=112,split=64.,inner_scale=.125):
        validate_inverse_options(order,tail_order,split,inner_scale)
        x=float(x);y=float(y);xx=abs(x);yy=abs(y);R=split*max(inner_scale,xx,yy,1.)
        ti,wi=finite_nodes(0.,yy,order,inner_scale);to,wo=finite_nodes(yy,R,order,inner_scale)
        v,w=tail_rule(tail_order,self.q.p);te=R/v;we=w*R*v**(self.q.p-2)
        ti_all=np.r_[ti,to,te];jet=self.jet(xx,ti_all)
        ni,no=len(ti),len(to);co=np.r_[np.zeros(ni),wo,we];ci=np.r_[wi*ti,np.zeros(no+len(te))]
        V1=-(co@jet[:,1,:]);V2=(ci+yy*co)@jet[:,3,:]
        if x<0:V1=-V1
        if y<0:V2=-V2
        if x==0:V1[:]=0
        if y==0:V2[:]=0
        return np.stack([V1,V2])
    def constraint_rows(self,order=None):
        a=np.zeros(self.nu);a[:self.q.N+1]=(-1.)**np.arange(self.q.N+1)
        K=np.concatenate([np.full(self.q.N+1-k,(-1.)**k*self.q.L**(1/self.q.kappa)/2)for k in range(self.q.M)])
        C=-a.copy();t,w=roots_legendre(self.q.N+3 if order is None else order);sig=(1+t)/2;Q=(1-t)/2+2*self.q.kappa*sig
        for k in range(1,self.q.M):
            z=(2*t-1-self.q.tk[k])/(1-self.q.tk[k])if self.q.basis=='local'else t
            B=cheb_jet(z,self.q.N+1-k)[0]
            C[self.offs[k]:self.offs[k+1]]-=k*k*(-1.)**k*((w*Q*sig**(k-1))@B)
        return np.stack([a,K,C])
    def sample_maps(self,X,Y,progress=None,**options):
        X=np.asarray(X,float).reshape(-1);Y=np.asarray(Y,float).reshape(-1);g=self.jet(X,Y)
        v=np.empty((len(X),2,self.nu))
        for i,(x,y)in enumerate(zip(X,Y)):
            v[i]=self.velocity(x,y,**options)
            if progress is not None:progress(i+1,len(X))
        return dict(X=X,Y=Y,G=g[:,0],Gx=g[:,1],Gy=g[:,2],V1=v[:,0],V2=v[:,1],constraints=self.constraint_rows())


def residual_and_jacobian(m,u,c,center=False):
    G,Gx,Gy,V1,V2=[m[k]for k in ('G','Gx','Gy','V1','V2')];gx=Gx@u;gy=Gy@u
    ax=c*m['X']+V1@u;ay=c*m['Y']+V2@u
    R=ax*gx+ay*gy-G@u
    J=ax[:,None]*Gx+ay[:,None]*Gy-G+gx[:,None]*V1+gy[:,None]*V2
    A=m['constraints'][:3 if center else 2];rhs=np.array([1.,1.,1.-c])[:len(A)]
    return np.r_[R,A@u-rhs],np.vstack([J,A])
