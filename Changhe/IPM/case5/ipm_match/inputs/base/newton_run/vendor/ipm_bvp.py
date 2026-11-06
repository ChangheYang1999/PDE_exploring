"""Independent exploratory Fourier-Galerkin/log-radius IPM BVP.
Not interval arithmetic; finite inner/outer boundaries must be refined.
Density uses odd sine modes 1,3,...,2M-1; psi uses even modes 2,...,2M.
Two radial domains: inner log r in [-Lin,0], exterior log r in [0,T].
"""
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly

@dataclass
class IPMProblem:
    M: int
    c: float
    a: float
    Lin: float = 8.
    T: float = 35.
    nang: int = 0
    origin: str = "naive"

    def __post_init__(self):
        if self.M<2 or self.c<=1 or self.Lin<=0 or self.T<=0:
            raise ValueError('Need M>=2,c>1,Lin>0,T>0')
        self.gamma=1/self.c; self.delta=1-self.gamma; self.q0=1+self.gamma
        self.k=np.arange(1,2*self.M,2,dtype=float)
        self.ell=np.arange(2,2*self.M+1,2,dtype=float)
        self.nang=max(self.nang,4*self.M+4)
        self.theta=(np.arange(self.nang)+.5)*np.pi/(2*self.nang)
        self.So=np.sin(self.theta[:,None]*self.k)
        self.Co=np.cos(self.theta[:,None]*self.k)*self.k
        self.Se=np.sin(self.theta[:,None]*self.ell)
        self.Ce=np.cos(self.theta[:,None]*self.ell)*self.ell
        self.Po=(2/self.nang)*self.So.T
        self.Pe=(2/self.nang)*self.Se.T
        self.S0=self.Pe@(np.cos(self.theta)[:,None]*self.So)
        self.S1=self.Pe@(np.sin(self.theta)[:,None]*self.Co)
        self.eye=np.eye(self.M)
        src=self.gamma*self.S0-self.S1
        self.P=src/(self.ell[:,None]**2-self.q0**2)
        self.far=(self.ell[:,None]+self.q0)*self.P
        self._bc_matrices=None
        if self.origin not in ('naive','analytic_tangent'):
            raise ValueError('Unknown origin closure')
        self.origin_equilibrium=np.zeros(3*self.M)
        self.origin_equilibrium[0]=self.a
        self.origin_equilibrium[self.M]=-(self.c-1)/2
        self.origin_equilibrium[2*self.M]=-(self.c-1)
        if self.origin=='analytic_tangent':
            J=self.rhs_piece(np.array([-self.Lin]),self.origin_equilibrium[:,None],False,True)[1][:,:,0]
            from scipy.linalg import null_space,qr
            vv=[]
            for k in range(1,self.M):
                inds=np.concatenate([np.arange(k+1)+b*self.M for b in range(3)])
                mat=(J-2*k*np.eye(3*self.M))[:,inds]
                _,sv,vh=np.linalg.svd(mat,full_matrices=False)
                v=np.zeros(3*self.M);v[inds]=vh[-1]
                if np.linalg.norm(J@v-2*k*v)>1e-7:
                    raise ArithmeticError('Polynomial eigenvector not resolved')
                vv.append(v)
            self.origin_basis=np.column_stack(vv)
            q,_=qr(self.origin_basis,mode='full')
            self.origin_matrix=q[:,self.M-1:].T

    def rhs_piece(self,t,y,exterior,jac=False):
        """t may include multiple nodes; exact projected transport equation.
        y=(rho/r,psi/r^2,psi_r/r) inside;
        y=(rho/r^gamma,psi/r^(1+gamma),psi_r/r^gamma) outside.
        """
        M=self.M; N=y.shape[1]
        A,G,U=y[:M],y[M:2*M],y[2*M:]
        z=np.exp(-self.delta*t) if exterior else np.ones_like(t)
        sigma=self.gamma if exterior else 1.
        av=self.So@A; atheta=self.Co@A
        kv=self.Ce@G; uv=self.Se@U
        # Matrix c-K for odd Galerkin modes.
        mass=self.c*self.eye[None,:,:]-np.einsum('ip,pt,pj,t->tij',self.Po,kv,self.So,z,optimize=True)
        rhs=z*(self.Po@(sigma*kv*av-uv*atheta))
        if not exterior: rhs+=(1-self.c)*A
        At=np.linalg.solve(mass,rhs.T[...,None])[...,0].T
        q=self.q0 if exterior else 2.
        Gt=U-q*G
        Ut=-q*U+(self.ell**2)[:,None]*G+(self.S1-sigma*self.S0)@A-self.S0@At
        val=np.vstack([At,Gt,Ut])
        if not jac: return val
        # Tangent equations, including the derivative of the mass matrix.
        JA=z[:,None,None]*(sigma*np.einsum('ip,pt,pj->tij',self.Po,kv,self.So,optimize=True)-np.einsum('ip,pt,pj->tij',self.Po,uv,self.Co,optimize=True))
        if not exterior: JA+=(1-self.c)*self.eye[None,:,:]
        aplus=sigma*av+self.So@At
        JG=z[:,None,None]*np.einsum('ip,pt,pj->tij',self.Po,aplus,self.Ce,optimize=True)
        JU=-z[:,None,None]*np.einsum('ip,pt,pj->tij',self.Po,atheta,self.Se,optimize=True)
        allj=np.linalg.solve(mass,np.concatenate([JA,JG,JU],axis=2))
        out=np.zeros((N,3*M,3*M),dtype=allj.dtype)
        out[:,:M,:]=allj
        out[:,M:2*M,M:2*M]=-q*self.eye
        out[:,M:2*M,2*M:]=self.eye
        out[:,2*M:,:]=-np.einsum('ij,tjk->tik',self.S0,allj)
        out[:,2*M:,:M]+=(self.S1-sigma*self.S0)
        out[:,2*M:,M:2*M]+=np.diag(self.ell**2)
        out[:,2*M:,2*M:]+=-q*self.eye
        return val,np.moveaxis(out,0,2)

    def fun(self,x,y):
        n=3*self.M
        return np.vstack([self.Lin*self.rhs_piece(-self.Lin+self.Lin*x,y[:n],False),
                          self.T*self.rhs_piece(self.T*x,y[n:],True)])

    def fun_jac(self,x,y):
        n=3*self.M
        ji=self.rhs_piece(-self.Lin+self.Lin*x,y[:n],False,True)[1]*self.Lin
        jo=self.rhs_piece(self.T*x,y[n:],True,True)[1]*self.T
        J=np.zeros((2*n,2*n,len(x)),dtype=y.dtype)
        J[:n,:n]=ji;J[n:,n:]=jo
        return J

    def bc(self,ya,yb):
        M=self.M; n=3*M
        Ai,Gi,Ui=ya[:M],ya[M:2*M],ya[2*M:n]
        Ao,Go,Uo=ya[n:n+M],ya[n+M:n+2*M],ya[n+2*M:]
        AI,GI,UI=yb[:M],yb[M:2*M],yb[2*M:n]
        AF,GF,UF=yb[n:n+M],yb[n+M:n+2*M],yb[n+2*M:]
        aorigin=Ai.copy();aorigin[0]-=self.a
        origin_bc=(np.concatenate([aorigin,Ui-self.ell*Gi,[Gi[0]+(self.c-1)/2]]) if self.origin=='naive' else self.origin_matrix@(ya[:n]-self.origin_equilibrium))
        return np.concatenate([origin_bc,
                               AI-Ao,GI-Go,UI[1:]-Uo[1:],UF+self.ell*GF-self.far@AF])

    def bc_jac(self,ya,yb):
        if self._bc_matrices is None:
            n=6*self.M;za=np.zeros(n);zb=np.zeros(n);base=self.bc(za,zb)
            A=np.column_stack([self.bc(np.eye(n)[j],zb)-base for j in range(n)])
            B=np.column_stack([self.bc(za,np.eye(n)[j])-base for j in range(n)])
            self._bc_matrices=(A,B)
        return self._bc_matrices

    def initial(self,x):
        M=self.M
        Ai=np.zeros((M,len(x)));Ai[0]=self.a
        Gi=np.zeros_like(Ai);Gi[0]=-(self.c-1)/2
        Ui=2*Gi
        Ao=Ai.copy();Pf=self.P@Ao
        Go=Pf+(Gi-Pf)*np.exp(-(self.ell[:,None]+self.q0)*(self.T*x))
        Uo=self.q0*Pf-self.ell[:,None]*(Gi-Pf)*np.exp(-(self.ell[:,None]+self.q0)*(self.T*x))
        return np.vstack([Ai,Gi,Ui,Ao,Go,Uo])

    def solve(self,previous=None,tol=1e-5,max_nodes=3500,verbose=0):
        if previous is None:
            # Enough initial nodes to resolve origin, interface and exterior fast layer.
            x=np.unique(np.r_[np.linspace(0,1,81),np.geomspace(1e-4,.1,25),1-np.geomspace(1e-4,.1,25)])
            y=self.initial(x)
        else:
            x=previous.x
            y=previous.sol(x)
            if y.shape[0]!=6*self.M: raise ValueError('different mode counts need explicit interpolation')
        return solve_bvp(self.fun,self.bc,x,y,fun_jac=self.fun_jac,bc_jac=self.bc_jac,
                         tol=tol,bc_tol=min(1e-9,tol),max_nodes=max_nodes,verbose=verbose)

    def summary(self,sol,nt=501):
        x=np.linspace(0,1,nt);y=sol.sol(x);M=self.M;n=3*M
        a=sol.sol(0);b=sol.sol(1)
        jump=a[n+2*M:]-b[2*M:n]
        ki=self.Ce@y[M:2*M]
        ko=(self.Ce@y[n+M:n+2*M])*np.exp(-self.delta*self.T*x)
        return dict(M=M,c=self.c,a=self.a,Lin=self.Lin,T=self.T,status=int(sol.status),success=bool(sol.success),
                    nodes=len(sol.x),niter=int(sol.niter),rms_max=float(max(sol.rms_residuals)),
                    bc_max=float(np.max(np.abs(self.bc(a,b)))),J2=float(jump[0]),
                    Jhigh_max=float(np.max(np.abs(jump[1:]))),
                    min_wr=float(min(np.min(self.c-ki),np.min(self.c-ko))),
                    far_scaled_amp=float(np.max(np.abs(y[n: n+M,-1]))),
                    far_nonlinearity=float(np.exp(-self.delta*self.T)),
                    H4=float(b[M+1]),Hmax=float(np.max(np.abs(b[M+1:2*M]))),
                    max_density_inner=float(np.max(np.abs(self.So@y[:M]))))

def save_solution(path,p,sol):
    np.savez_compressed(path,c=p.c,a=p.a,M=p.M,Lin=p.Lin,T=p.T,nang=p.nang,
                        origin=p.origin,x=sol.x,y=sol.y,poly=sol.sol.c,status=sol.status,
                        rms=sol.rms_residuals,niter=sol.niter)

def load_solution(path):
    from types import SimpleNamespace
    d=np.load(path)
    p=IPMProblem(int(d['M']),float(d['c']),float(d['a']),float(d['Lin']),float(d['T']),int(d['nang']),str(d['origin']) if 'origin' in d else 'naive')
    s=SimpleNamespace(x=d['x'],y=d['y'],sol=PPoly.construct_fast(d['poly'],d['x'],axis=1),status=int(d['status']),
                      success=int(d['status'])==0,rms_residuals=d['rms'],niter=int(d['niter']))
    return p,s
