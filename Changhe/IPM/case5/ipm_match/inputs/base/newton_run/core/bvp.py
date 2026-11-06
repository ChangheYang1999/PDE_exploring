"""Two-domain Fourier Galerkin IPM BVP and exact discrete sensitivities.

State x[z]=(f_odd,g_even,p_even), rho=r f, psi=r² g, p=g_z.
Polynomial products use exact sine convolutions (no quadrature aliasing).
Fourth-order Lobatto/Hermite-Simpson collocation in z=log r.
"""
import numpy as np
from scipy.sparse import coo_matrix, vstack
from scipy.sparse.linalg import splu
from threadpoolctl import threadpool_limits
_BLAS=threadpool_limits(limits=1,user_api="blas")

class Model:
    def __init__(self,c,n,m,li,lo,grade=0.):
        self.c=float(c);self.n=n=int(n);self.m=m=int(m);self.li=float(li);self.lo=float(lo)
        self.z=np.r_[np.linspace(-li,0,m+1),np.linspace(0,lo,m+1)]
        if grade:
            s=np.linspace(0,1,m+1);ci=min(1.5,float(grade))
            self.z=np.r_[-li*np.sinh(ci*(1-s))/np.sinh(ci),lo*np.sinh(grade*s)/np.sinh(grade)]
        self.i=np.r_[np.arange(m),np.arange(m+1,2*m+1)]
        self.h=(self.z[self.i+1]-self.z[self.i])[:,None]
        self.l=2*np.arange(n)+1;self.k=2*np.arange(1,n+1)
        self.G=np.zeros((n,n,n));self.Q=np.zeros_like(self.G);self.C=np.zeros((n,n));self.S=np.zeros((n,n))
        for j,k in enumerate(self.k):
            for m_,l in enumerate(self.l):
                for v,coef in [(l+k,k/2),(l-k,k/2)]:
                    if abs(v)<=self.l[-1]:
                        self.G[(abs(v)-1)//2,j,m_]+=np.sign(v)*coef
                for v,coef in [(k+l,l/2),(k-l,l/2)]:
                    if abs(v)<=self.l[-1]:
                        self.Q[(abs(v)-1)//2,j,m_]+=np.sign(v)*coef
        for j,l in enumerate(self.l):
            for v in [l+1,l-1]:
                if v and v<=self.k[-1]:self.C[v//2-1,j]+=0.5
            for v in [1+l,1-l]:
                if v and abs(v)<=self.k[-1]:self.S[abs(v)//2-1,j]+=.5*np.sign(v)*l
        self.Gf=self.G.transpose(1,0,2).reshape(n,-1).copy()
        self.Qf=self.Q.transpose(1,0,2).reshape(n,-1).copy()
        self.Gt=self.G.transpose(2,0,1).reshape(n,-1).copy()
        self.Qt=self.Q.transpose(2,0,1).reshape(n,-1).copy()
        self.I=np.eye(n);self.I3=np.eye(3*n)
        d=3*n
        self.d=d;self.N=len(self.z)*d
        idr=(np.arange(len(self.i))[:,None]*d+np.arange(d)).reshape(-1,1)
        ic=(self.i[:,None]*d+np.arange(d)).reshape(-1,1,d)
        self.rows=np.broadcast_to(idr.reshape(-1,d,1),(len(ic),d,d)).ravel().copy()
        self.cols=np.broadcast_to(ic,(len(ic),d,d)).ravel().copy()
        self.rows2=np.tile(self.rows,2);self.cols2=np.r_[self.cols,self.cols+d]
        # Linear boundary conditions, including nonzero far-field density forcing.
        B=np.zeros((6*n,self.N)); b=np.zeros(6*n);ba=np.zeros(6*n)
        L=0;IL=m*d;OR=(m+1)*d;E=(2*m+1)*d
        s=np.arange(n)
        B[s,L+s]=1;ba[0]=-1
        B[n+s,L+2*n+s]=1
        B[n+s,L+n+s]=-(self.k-2)
        B[2*n,L+n]=1;b[2*n]=-(1-c)/2
        off=2*n+1
        for j in range(2*n):
            B[off+j,OR+j]=1;B[off+j,IL+j]=-1
        off+=2*n
        for j in range(1,n):
            B[off+j-1,OR+2*n+j]=1;B[off+j-1,IL+2*n+j]=-1
        off+=n-1
        gamma=1/c;beta=1-gamma
        B[off+s,E+2*n+s]=1;B[off+s,E+n+s]=self.k+2
        B[off:off+n,E:E+n]=-(gamma*self.C-self.S)/(self.k[:,None]-2+beta)
        self.B=coo_matrix(B).tocsc();self.b=b;self.ba=ba
    def ra(self):return np.r_[np.zeros(len(self.i)*self.d),self.ba]
    def mult(self,coef,T):return (coef@T).reshape(-1,self.n,self.n)
    def ode(self,x,jac=False):
        n=self.n;c=self.c
        f,g,p=np.split(x,3,axis=1)
        B=c*self.I-self.mult(g,self.Gf);Q=self.mult(2*g+p,self.Qf)
        prod=lambda M,y:(M@y[...,None])[...,0]
        V=np.linalg.solve(B,(f-prod(Q,f))[...,None])[...,0]
        F=np.concatenate([V-f,p,-4*p+(self.k*self.k-4)*g-V@self.C.T+f@self.S.T],axis=1)
        if not jac:return F
        Qf=self.mult(f,self.Qt)
        D=np.linalg.solve(B,np.concatenate([self.I-Q,self.mult(V,self.Gt)-2*Qf,-Qf],axis=2))
        DF=np.zeros((len(x),3*n,3*n));DF[:,:n]=D;DF[:,:n,:n]-=self.I;DF[:,n:2*n,2*n:]=self.I
        DF[:,2*n:,:]=-self.C@D
        DF[:,2*n:,:n]+=self.S
        DF[:,2*n:,n:2*n]+=np.diag(self.k*self.k-4);DF[:,2*n:,2*n:]-=4*self.I
        return F,DF
    def ode_H(self,x,v,DFv):
        n=self.n
        f,g,p=np.split(x,3,axis=1);vf,vg,vp=np.split(v,3,axis=1)
        B=self.c*self.I-self.mult(g,self.Gf)
        H=np.linalg.solve(B,2*(self.mult(vg,self.Gf)@(vf+DFv[:,:n])[...,None]-self.mult(2*vg+vp,self.Qf)@vf[...,None]))[...,0]
        return np.c_[H,np.zeros_like(H),-H@self.C.T]
    def ode_at(self,x,jac,loc):
        if not getattr(self,'scale_ext',False):return self.ode(x,jac)
        sf,rate=self._scales[loc]
        if not jac:return self.ode(x*sf)/sf+rate*x
        F,D=self.ode(x*sf,True)
        return F/sf+rate*x,D+rate[...,None]*self.I3
    def ode_H_at(self,x,v,Dv,loc):
        if not getattr(self,'scale_ext',False):return self.ode_H(x,v,Dv)
        sf,rate=self._scales[loc]
        return sf*self.ode_H(x*sf,v,Dv-rate*v)
    def combined(self,x,a,jac=False,want_cache=False):
        x=np.asarray(x).reshape(-1,self.d)
        i=self.i;h=self.h
        if jac:F,D=self.ode_at(x,True,'node')
        else:F=self.ode_at(x,False,'node')
        xm=(x[i]+x[i+1])/2+h*(F[i]-F[i+1])/8
        if jac:Fm,Dm=self.ode_at(xm,True,'mid')
        else:Fm=self.ode_at(xm,False,'mid')
        r=np.r_[(x[i+1]-x[i]-h*(F[i]+4*Fm+F[i+1])/6).ravel(),self.B@x.ravel()+self.b+a*self.ba]
        if not jac:return r
        hh=h[...,None];E=self.I3
        A=-E-hh*(D[i]+4*Dm@(E/2+hh*D[i]/8))/6
        Z=E-hh*(D[i+1]+4*Dm@(E/2-hh*D[i+1]/8))/6
        M=coo_matrix((np.r_[A.ravel(),Z.ravel()],(self.rows2,self.cols2)),shape=(len(i)*self.d,self.N))
        M=vstack([M,self.B],format='csc');M.eliminate_zeros()
        if want_cache:return r,M,(x,xm,D,Dm)
        return r,M
    def residual(self,x,a):return self.combined(x,a)
    def jacobian(self,x,a):return self.combined(x,a,True)[1]
    def hessian_action(self,cache,v):
        x,xm,D,Dm=cache;i=self.i;h=self.h;v=v.reshape(-1,self.d)
        Dv=(D@v[...,None])[...,0];H=self.ode_H_at(x,v,Dv,'node')
        vm=(v[i]+v[i+1])/2+h*(Dv[i]-Dv[i+1])/8
        Dmvm=(Dm@vm[...,None])[...,0]
        Hm=self.ode_H_at(xm,vm,Dmvm,'mid')+(Dm@(h*(H[i]-H[i+1])/8)[...,None])[...,0]
        return np.r_[(-h*(H[i]+4*Hm+H[i+1])/6).ravel(),np.zeros(6*self.n)]
    def seed(self,guess=None):
        n=self.n;m=self.m
        x=np.zeros((len(self.z),self.d))
        if guess is None:
            x[:,n]=(1-self.c)/2
            x[m+1:,n]*=np.exp(-4*self.z[m+1:])
            x[m+1:,2*n]=-4*x[m+1:,n]
            return x
        g=guess;oldn=int(g['n']);oldm=int(g['m'])
        old_z=np.r_[np.linspace(-float(g['li']),0,oldm+1),np.linspace(0,float(g['lo']),oldm+1)]
        if 'z' in g:old_z=g['z']
        y=g['x']
        for side,(so,sn) in enumerate([(slice(None,oldm+1),slice(None,m+1)),(slice(oldm+1,None),slice(m+1,None))]):
            for kind in range(3):
                for k in range(min(n,oldn)):
                    x[sn,kind*n+k]=np.interp(self.z[sn],old_z[so],y[so,kind*oldn+k])
        return x
    def hvv(self,x,a,v):return self.hessian_action(self.combined(x,a,True,True)[2],v)
    def jump(self,x):return float(x[self.m+1,2*self.n]-x[self.m,2*self.n])
def solve(c,a,n=8,m=64,li=8.,lo=12.,guess=None,tol=1e-10,maxit=18,verbose=False):
    mod=Model(c,n,m,li,lo);x=mod.seed(guess)
    norm=lambda v:float(np.max(np.abs(v)))
    ok=False
    for it in range(maxit+1):
        r,M,cache=mod.combined(x,a,True,True);err=norm(r)
        if verbose:print('Newton',it,err,mod.jump(x),flush=True)
        if not np.isfinite(err):break
        if err<tol:ok=True;break
        if it==maxit:break
        try:dx=splu(M).solve(-r).reshape(x.shape)
        except RuntimeError:break
        best=err
        for ex in range(14):
            y=x+(2.**(-ex))*dx
            ey=norm(mod.residual(y,a))
            if ey<best:
                x=y;break
        else:break
    out=dict(c=c,a=a,n=n,m=m,li=li,lo=lo,x=x,z=mod.z,xdot=mod.ode(x),origin='naive',far_order=1,J=mod.jump(x),Jp=np.nan,Jpp=np.nan,res=err,it=it,ok=ok)
    if ok:
        lu=splu(M);ra=mod.ra();v=lu.solve(-ra)
        h=mod.hessian_action(cache,v);w=lu.solve(-h)
        out.update(xa=v.reshape(x.shape),xaa=w.reshape(x.shape),res1=norm(M@v+ra),res2=norm(M@w+h),
                Jp=mod.jump(v.reshape(x.shape)),Jpp=mod.jump(w.reshape(x.shape)))
    return out
