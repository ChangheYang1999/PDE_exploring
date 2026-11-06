"""Nonlinear finite Taylor origin chart + second-order far Robin correction.
Exploratory binary64 only; no certification of omitted Taylor or far tails.
"""
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.linalg import qr,solve_triangular
from scipy.interpolate import PPoly
from ipm_bvp import IPMProblem
from origin_manifold import evaluate_origin

class NonlinearOriginProblem(IPMProblem):
    def __init__(self,M,c,a,Lin=2.,T=40.,nang=0,far_order=2):
        super().__init__(M,c,a,Lin,T,nang,origin='naive')
        self.far_order=far_order
        self.order=M-1
        self.base_origin=evaluate_origin(c,a,np.zeros(self.order),self)
        J=np.column_stack([self._raw_column(k) for k in range(self.order)])
        self.origin_Q,rr=qr(J,mode='economic')
        self.free_transform=solve_triangular(rr,np.eye(self.order))
        self.tangent_condition=float(np.linalg.cond(rr))
        k=np.arange(1,4*M,2,dtype=float);ell=np.arange(2,4*M+1,2,dtype=float)
        th=(np.arange(max(8*M+8,96))+.5)*np.pi/(2*max(8*M+8,96))
        so=np.sin(th[:,None]*k);co=np.cos(th[:,None]*k)*k
        se=np.sin(th[:,None]*ell);ce=np.cos(th[:,None]*ell)*ell
        po=2/len(th)*so.T;pe=2/len(th)*se.T
        s0=pe@(np.cos(th)[:,None]*so);s1=pe@(np.sin(th)[:,None]*co)
        q1=self.q0;q2=2*self.gamma
        P1=(self.gamma*s0-s1)/(ell[:,None]**2-q1**2)
        P2=((2*self.gamma-1)*s0-s1)/(ell[:,None]**2-q2**2)
        self._far_data=(so,co,se,ce,po,P1,P2,ell,q2)
        self._linear_bc_jac=None

    def _raw_column(self,j):
        p=np.zeros(self.order,dtype=complex);p[j]=1e-25j
        return evaluate_origin(self.c,self.a,p,self).imag/1e-25

    def origin_value(self,p):
        return evaluate_origin(self.c,self.a,self.free_transform@p,self)

    def origin_jac(self,p):
        out=[]
        for j in range(self.order):
            pc=np.asarray(p,dtype=complex).copy();pc[j]+=1e-25j
            out.append(self.origin_value(pc).imag/1e-25)
        return np.column_stack(out)

    def far_second(self,f):
        so,co,se,ce,po,P1,P2,ell,q2=self._far_data
        full=np.zeros(2*self.M,dtype=np.result_type(f,float));full[:self.M]=f
        g=P1@full
        f2=po@(-self.gamma*(ce@g)*(so@full)+self.q0*(se@g)*(co@full))/(self.c-1)
        corr=(ell+q2)*(P2@f2)-(ell+self.q0)*(P1@f2)
        return corr[:self.M]

    def bc_full(self,ya,yb,p):
        M=self.M;n=3*M
        AI,GI,UI=yb[:M],yb[M:2*M],yb[2*M:n]
        AO,GO,UO=ya[n:n+M],ya[n+M:n+2*M],ya[n+2*M:]
        AF,GF,UF=yb[n:n+M],yb[n+M:n+2*M],yb[n+2*M:]
        far=UF+self.ell*GF-self.far@AF
        if self.far_order>=2:far=far-np.exp(-self.delta*self.T)*self.far_second(AF)
        return np.concatenate([ya[:n]-self.origin_value(p),AI-AO,GI-GO,UI[1:]-UO[1:],far])

    def bc_full_jac(self,ya,yb,p):
        M=self.M;n=3*M;nd=6*M;nb=nd+self.order
        if self._linear_bc_jac is None:
            A=np.zeros((nb,nd));B=np.zeros((nb,nd));eye=np.eye(M)
            A[:n,:n]=np.eye(n)
            k=n
            B[k:k+M,:M]=eye;A[k:k+M,n:n+M]=-eye;k+=M
            B[k:k+M,M:2*M]=eye;A[k:k+M,n+M:n+2*M]=-eye;k+=M
            B[k:k+M-1,2*M+1:n]=np.eye(M-1);A[k:k+M-1,n+2*M+1:]=-np.eye(M-1);k+=M-1
            B[k:k+M,n:n+M]=-self.far
            B[k:k+M,n+M:n+2*M]=np.diag(self.ell)
            B[k:k+M,n+2*M:]=eye
            self._linear_bc_jac=(A,B)
        A,B=self._linear_bc_jac
        B=B.copy()
        if self.far_order>=2:
            f=np.asarray(yb[n:n+M],dtype=complex)
            for j in range(M):
                fc=f.copy();fc[j]+=1e-25j
                B[-M:,n+j]-=np.exp(-self.delta*self.T)*self.far_second(fc).imag/1e-25
        C=np.zeros((nb,self.order));C[:n]=-self.origin_jac(p)
        return A,B,C

    def solve_full(self,previous=None,tol=1e-5,max_nodes=3500,verbose=0):
        if previous is None:
            x=np.unique(np.r_[np.linspace(0,1,121),np.geomspace(1e-5,.1,25),1-np.geomspace(1e-5,.1,25)])
            y=self.initial(x)
        else:
            x=previous.x;y=previous.sol(x)
        pp=self.origin_Q.T@(y[:3*self.M,0]-self.base_origin)
        def fun(x,y,p):return self.fun(x,y)
        def jac(x,y,p):return self.fun_jac(x,y),np.zeros((6*self.M,self.order,len(x)))
        return solve_bvp(fun,self.bc_full,x,y,p=pp,fun_jac=jac,bc_jac=self.bc_full_jac,
                         tol=tol,bc_tol=min(1e-10,tol),max_nodes=max_nodes,verbose=verbose)

    def summary_full(self,sol,nt=501):
        # Parent summary's legacy boundary residual is intentionally overwritten.
        r=super().summary(sol,nt)
        r['bc_max']=float(np.max(np.abs(self.bc_full(sol.sol(0),sol.sol(1),sol.p))))
        r.update(origin='nonlinear_taylor',origin_order=self.order,far_order=self.far_order,
                 tangent_condition=self.tangent_condition,
                 origin_parameters=sol.p.tolist(),
                 raw_origin_parameters=(self.free_transform@sol.p).tolist())
        return r

def save_full(path,p,s):
    np.savez_compressed(path,c=p.c,a=p.a,M=p.M,Lin=p.Lin,T=p.T,nang=p.nang,
       far_order=p.far_order,origin='nonlinear_taylor',x=s.x,y=s.y,poly=s.sol.c,
       status=s.status,rms=s.rms_residuals,niter=s.niter,p=s.p)

def load_full(path):
    d=np.load(path)
    p=NonlinearOriginProblem(int(d['M']),float(d['c']),float(d['a']),float(d['Lin']),float(d['T']),int(d['nang']),int(d['far_order']))
    s=SimpleNamespace(x=d['x'],y=d['y'],sol=PPoly.construct_fast(d['poly'],d['x'],axis=1),status=int(d['status']),
          success=int(d['status'])==0,rms_residuals=d['rms'],niter=int(d['niter']),p=d['p'])
    return p,s
