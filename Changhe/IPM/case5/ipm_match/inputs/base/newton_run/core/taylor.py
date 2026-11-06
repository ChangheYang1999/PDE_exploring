"""Direct Fourier solver with the recovered finite Taylor origin manifold.

This solves for the (n-1) free Taylor amplitudes jointly with all nodal
variables. The chart QR is held fixed locally; changing basis between solves
does not affect the profile sensitivities. Explicit second chain derivatives
include R_aa and R_xa, all Taylor parameters, and the quadratic far condition.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from scipy.sparse import coo_matrix,vstack,bmat,csc_matrix
from scipy.sparse.linalg import splu
from scipy.linalg import qr,solve_triangular
from bvp import Model
from origin_manifold import evaluate_origin,make_maps,bracket

def jet_origin_h(c,a,free,da,v,model):
    """D² origin[(da,v),(da,v)], via forward product rules in Taylor recursion."""
    r=[(np.array([a,0.]),np.array([da,0.]),np.zeros(2))]
    ps=[(np.array([0.,1-c,0]),np.zeros(3),np.zeros(3))]
    ro,po=model._jet_maps[('origin_maps',len(free))]
    yy=np.zeros(3*model.n);N=model.n
    for k in range(1,len(free)+1):
        n=2*k+1
        q=np.zeros((3,n+1))
        for i in range(1,k):
            t=ps[i];s=r[k-i]
            q[0]-=bracket(t[0],s[0]);q[1]-=bracket(t[1],s[0])+bracket(t[0],s[1])
            q[2]-=bracket(t[2],s[0])+2*bracket(t[1],s[1])+bracket(t[0],s[2])
        q=q[:,::2];lam=2*k+4*np.arange(k+1)*(c-1)
        e=np.zeros((3,k+1));e[0,k]=free[k-1];e[1,k]=v[k-1]
        for j in range(k-1,-1,-1):
            aa=(2*k-2*j+1)*(2*k-2*j)
            b0=(2*j+3)*(2*j+2);bb=b0*(1-a/lam[j+1]);db=-b0*da/lam[j+1]
            e[:,j]=(-2*(j+1)*q[:,j+1]/lam[j+1]-bb*e[:,j+1]-db*np.array([0,e[0,j+1],2*e[1,j+1]]))/aa
        de=(q-(2*np.arange(k+1)+1)*(a*e+da*np.stack([np.zeros(k+1),e[0],2*e[1]])))/lam
        rh=np.zeros((3,n+1));rh[:,::2]=de
        ph=np.zeros((3,n+2));ph[:,1::2]=e
        r.append(rh);ps.append(ph)
        yg=po[k]@ph[2]
        yy[:N]+=ro[k]@rh[2];yy[N:2*N]+=yg;yy[2*N:]+=2*k*yg
    return yy

class TaylorModel(Model):
    def __init__(self,c,a,n,m,li,lo,order=None,far_order=2,grade=0.,scale_ext=False):
        super().__init__(c,n,m,li,lo,grade=grade)
        self.scale_ext=bool(scale_ext)
        self._scales={}
        for key,zz,extmask in [('node',self.z,np.arange(len(self.z))>m),('mid',(self.z[self.i]+self.z[self.i+1])/2,np.arange(len(self.i))>=m)]:
            rate=extmask[:,None]*(1.-1/c) if scale_ext else np.zeros((len(zz),1))
            self._scales[key]=(np.exp(-rate*zz[:,None]),rate)
        self.sf=self._scales['node'][0];self.ffactor=self.sf[-1,0]
        n=self.n;self.M=n
        self.order=n-1 if order is None else int(order)
        if self.order!=n-1:raise ValueError('Direct formulation requires n-1 free amplitudes')
        order=self.order;self.far_order=far_order
        # Full angular band for the polynomial maps and far quadratic correction.
        self.theta=(np.arange(8*n+8)+.5)*np.pi/(2*(8*n+8))
        sn=lambda k:np.sin(self.theta[:,None]*k)
        cn=lambda k:np.cos(self.theta[:,None]*k)*k
        self.Po=2/len(self.theta)*sn(self.l).T;self.Pe=2/len(self.theta)*sn(self.k).T
        zero=np.zeros(order);self.base=self.origin_raw(a,zero)
        jac=np.stack([self.origin_raw(a,1j*1e-28*e).imag/1e-28 for e in np.eye(order)],axis=1)
        self.Qor,R=qr(jac,mode='economic')
        self.Tr=solve_triangular(R,np.eye(order))
        self.cond_origin=np.linalg.cond(R);self.NN=self.N+order
        # Remove artificial naive BCs; retain all interface and linear Robin rows.
        self.Bm=self.B[2*n+1:];self.bm=self.b[2*n+1:]
        self.B0=coo_matrix((np.ones(3*n),(np.arange(3*n),np.arange(3*n))),shape=(3*n,self.N)).tocsc()
        self._lin_B=vstack([self.B0,self.Bm],format='csc')
        gamma=1/c; q=1+gamma;q2=2*gamma;kk=np.arange(1,4*n,2);ell=np.arange(2,4*n+1,2)
        s0=2/len(self.theta)*sn(ell).T@(np.cos(self.theta)[:,None]*sn(kk))
        s1=2/len(self.theta)*sn(ell).T@(np.sin(self.theta)[:,None]*cn(kk))
        P1=(gamma*s0-s1)/(ell[:,None]**2-q*q)
        P2=((2*gamma-1)*s0-s1)/(ell[:,None]**2-q2*q2)
        PF=((ell+q2)[:,None]*P2-(ell+q)[:,None]*P1)[:n]
        self.Bf1=(cn(ell)@P1[:,:n],sn(kk)[:,:n],sn(ell)@P1[:,:n],cn(kk)[:,:n])
        self.PF=PF@(2/len(self.theta)*sn(kk).T)
    def origin_raw(self,a,e):
        raw=evaluate_origin(self.c,a,e,self)
        raw[2*self.n:]-=2*raw[self.n:2*self.n]
        return raw
    def far2(self,f):
        if self.far_order<2:return f*0
        C,S,G,D=self.Bf1;gam=1/self.c
        return self.PF@(-gam*(C@f)*(S@f)+(1+gam)*(G@f)*(D@f))/(self.c-1)
    def pack(self,x,eta):return np.r_[x.ravel(),eta]
    def unpack(self,Y):return Y[:self.N].reshape(-1,self.d),Y[self.N:]
    def seed_T(self,guess):
        x=self.seed(guess);eta=self.Qor.T@(x[0]-self.base)
        return self.pack(x/self.sf,eta)
    def originDer(self,a,eta):
        fre=self.Tr@eta
        eps=1e-28
        da=self.origin_raw(a+1j*eps,fre).imag/eps
        dp=np.stack([self.origin_raw(a,fre+1j*eps*self.Tr[:,j]).imag/eps for j in range(self.order)],axis=1)
        return da,dp
    def whole(self,Y,a,jac=False):
        x,eta=self.unpack(Y);n=self.n;ni=len(self.i)*self.d
        if jac:r0,M,cache=self.combined(x,a,True,True)
        else:r0=self.residual(x,a)
        off=2*n+1
        o=self.origin_raw(a,self.Tr@eta)
        r=np.r_[r0[:ni],x[0]-o,r0[ni+off:]]
        r[-n:]-=self.ffactor*self.far2(x[-1,:n])
        if not jac:return r
        da,dp=self.originDer(a,eta)
        b=self._lin_B
        if self.far_order>=2:
            eps=1e-28;f=x[-1,:n]
            df=np.stack([self.ffactor*self.far2(f+1j*eps*e).imag/eps for e in np.eye(n)],axis=1)
            rr,cc=np.indices((n,n))
            b=b+coo_matrix((-df.ravel(),((b.shape[0]-n+rr).ravel(),(self.N-self.d+cc).ravel())),shape=b.shape)
        et=coo_matrix((-dp.ravel(),(np.repeat(np.arange(3*n),self.order),np.tile(np.arange(self.order),3*n))),shape=(b.shape[0],self.order))
        J=bmat([[M[:ni],None],[b,et]],format='csc')
        ra=np.zeros(len(r));ra[ni:ni+3*n]=-da
        return r,J,ra,cache
    def HH(self,cache,a,Y,dY,da=1.):
        x,eta=self.unpack(Y);v,de=self.unpack(dY);n=self.n
        Hi=self.hessian_action(cache,v)[:len(self.i)*self.d]
        H0=jet_origin_h(self.c,a,self.Tr@eta,da,self.Tr@de,self)
        return np.r_[Hi,-H0,np.zeros(3*n-1),-2*self.ffactor*self.far2(v[-1,:n])]

def solve_taylor(c,a,n=8,m=128,li=2,lo=40,guess=None,tol=1e-10,maxit=18,verbose=False,far_order=2,grade=0.,scale_ext=False):
    mod=TaylorModel(c,a,n,m,li,lo,far_order=far_order,grade=grade,scale_ext=scale_ext);Y=mod.seed_T(guess)
    norm=lambda v:float(np.max(np.abs(v)))
    ok=False
    for it in range(maxit+1):
        r,J,ra,cache=mod.whole(Y,a,True);err=norm(r)
        if verbose:print('NewtonTaylor',it,err,mod.jump(mod.unpack(Y)[0]),flush=True)
        if err<tol:ok=True;break
        if it==maxit or not np.isfinite(err):break
        try:dx=splu(J).solve(-r)
        except RuntimeError:break
        for e in range(14):
            y=Y+2.**(-e)*dx
            if norm(mod.whole(y,a))<err:Y=y;break
        else:break
    xu,eta=mod.unpack(Y);x=xu*mod.sf
    out=dict(c=c,a=a,n=n,m=m,li=li,lo=lo,x=x,z=mod.z,xdot=mod.ode(x),J=mod.jump(x),
        Jp=np.nan,Jpp=np.nan,res=err,it=it,ok=ok,origin='nonlinear_taylor',far_order=far_order,
        origin_order=mod.order,grade=grade,scale_ext=scale_ext,eta=eta,raw_eta=mod.Tr@eta,origin_basis_cond=mod.cond_origin)
    if scale_ext:out.update(scaled_x=xu,scaled_xdot=mod.ode_at(xu,False,'node'))
    if ok:
        lu=splu(J);v=lu.solve(-ra);H=mod.HH(cache,a,Y,v);w=lu.solve(-H)
        xa,etaa=mod.unpack(v);xaa,etaaa=mod.unpack(w)
        out.update(xa=xa*mod.sf,xaa=xaa*mod.sf,eta_a=etaa,eta_aa=etaaa,res1=norm(J@v+ra),res2=norm(J@w+H),Jp=mod.jump(xa),Jpp=mod.jump(xaa))
    return out
