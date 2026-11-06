"""Same finite Cartesian-origin polynomial chart, evaluated in polar harmonics.
Each homogeneous component remains a polynomial. Free coefficient e_j is the
derivative at theta=0 of the homogeneous angular stream polynomial because the
monomial x^(2j+1)y is its unique term linear in y.  Avoids cancellation of
Cartesian monomials of high total degree during their conversion to Fourier.
"""
import numpy as np
from scipy.linalg import lu_factor,lu_solve,qr,solve_triangular
class PolarOrigin:
 def __init__(self,M,c,a):
  self.M=M;self.c=c;self.a=a;self.order=M-1
  ng=4*M+8;theta=(np.arange(ng)+.5)*np.pi/(2*ng)
  odd=np.arange(1,2*M,2);even=odd+1;self.even=even;self.ngrid=ng
  self.so=np.sin(np.outer(theta,odd));self.co=np.cos(np.outer(theta,odd))*odd
  self.se=np.sin(np.outer(theta,even));self.ce=np.cos(np.outer(theta,even))*even
  self.po=(2/ng)*self.so.T;pe=(2/ng)*self.se.T
  proj=lambda op,w,tr: op@(w[:,None]*tr)
  S0=proj(pe,np.cos(theta),self.so);S1=proj(pe,np.sin(theta),self.co)
  t0=proj(self.po,(1-c)*np.cos(2*theta),self.so)
  t1=proj(self.po,(1-c)*np.sin(2*theta),self.co)
  t2=proj(self.po,np.sin(theta),self.ce);t3=proj(self.po,np.cos(theta),self.se)
  self.ops={};self.la={};J=[]
  self.base_origin=np.zeros(3*M);self.base_origin[[0,M,2*M]]=[a,(1-c)/2,1-c]
  for j in range(1,M):
   n=j+1;lam=2*j+1;q=lam+1;s=np.s_[:n,:n]
   top=np.c_[(c*lam-1)*np.eye(n)-lam*t0[s]+t1[s],a*(-t2[s]+q*t3[s])]
   bot=np.c_[lam*S0[s]-S1[s],np.diag(q*q-even[:n]**2)];bot[-1,:n]=0;bot[-1,n:]=even[:n]
   L=np.vstack([top,bot]);self.la[j]=-t2[s]+q*t3[s]
   self.ops[j]=lu_factor(L)
   rhs=np.zeros(2*n);rhs[-1]=1;fg=lu_solve(self.ops[j],rhs)
   col=np.zeros(3*M);col[:n]=fg[:n];col[M:M+n]=fg[n:];col[2*M:2*M+n]=q*fg[n:];J.append(col)
  self.origin_Q,r=qr(np.array(J).T,mode='economic');self.free_transform=solve_triangular(r,np.eye(M-1))
  self.tangent_condition=float(np.linalg.cond(r))
 def value_jet(self,raw,da=0.,dr=None,order=0,with_terms=False):
  """Return requested single derivative of the full origin trace."""
  M=self.M;h=order+1;dt=np.result_type(raw,da,float);da=float(da);y=np.zeros((h,3*M),dtype=dt);y[0]=self.base_origin
  if order:y[1,0]=da
  if with_terms:terms=np.zeros((M,3*M));terms[0]=y[order]
  # A,A_theta,G_theta,U for each homogeneous term and derivative order.
  W=np.zeros((4,h,M,self.ngrid),dtype=dt)
  for j in range(1,M):
   n=j+1; q=2*j+2
   R=np.zeros((2*n,h),dtype=dt);R[-1,0]=raw[j-1]
   if order:R[-1,1]=dr[j-1]
   def nonlin(b,k):
    if j==1:return 0.
    return np.sum(W[2,b,1:j]*W[0,k,j-1:0:-1]-W[3,b,1:j]*W[1,k,j-1:0:-1],axis=0)
   if j>1:
    S=[nonlin(0,0)]
    if order:S.append(nonlin(1,0)+nonlin(0,1))
    if order==2:S.append(nonlin(2,0)+2*nonlin(1,1)+nonlin(0,2))
    R[:n]=self.po[:n]@np.array(S).T
   FG=np.zeros_like(R)
   for k in range(h):
    if k:R[:n,k]-=k*da*(self.la[j]@FG[n:,k-1])
    FG[:,k]=lu_solve(self.ops[j],R[:,k],check_finite=False)
   F,G=FG[:n],FG[n:]
   y[:,:n]+=F.T;y[:,M:M+n]+=G.T;y[:,2*M:2*M+n]+=q*G.T
   if with_terms:terms[j,:n]=F[:,order];terms[j,M:M+n]=G[:,order];terms[j,2*M:2*M+n]=q*G[:,order]
   W[0,:,j]=(2*j+1)*(self.so[:,:n]@F).T;W[1,:,j]=(self.co[:,:n]@F).T
   W[2,:,j]=(self.ce[:,:n]@G).T;W[3,:,j]=q*(self.se[:,:n]@G).T
  return terms if with_terms else y[order]
 def origin_value(self,p):return self.value_jet(self.free_transform@p)
 def origin_jac(self,p):
  key=np.asarray(p).tobytes()
  if getattr(self,'_last_jac_key',None)==key:return self._last_jac
  raw=self.free_transform@p
  M=self.M;h=self.ngrid;X=self.value_jet(raw,with_terms=True)
  W=np.array([(2*np.arange(M)+1)[:,None]*(X[:,:M]@self.so.T),X[:,:M]@self.co.T,X[:,M:2*M]@self.ce.T,X[:,2*M:]@self.se.T])
  Jraw=np.zeros((3*M,M-1));V=np.zeros((4,M,h))
  for j0 in range(1,M):
   yy=Jraw[:,j0-1]
   for j in range(j0,M):
    n=j+1;q=2*j+2;r=np.zeros(2*n)
    if j==j0:r[-1]=1.
    else:
     vr=V[:,j0:j];w0=W[:,j-j0:0:-1]
     R=np.sum(vr[2]*w0[0]+w0[2]*vr[0]-vr[3]*w0[1]-w0[3]*vr[1],axis=0)
     r[:n]=self.po[:n]@R
    fg=lu_solve(self.ops[j],r,check_finite=False);F,G=fg[:n],fg[n:]
    yy[:n]+=F;yy[M:M+n]+=G;yy[2*M:2*M+n]+=q*G
    V[0,j]=(2*j+1)*(self.so[:,:n]@F);V[1,j]=self.co[:,:n]@F
    V[2,j]=self.ce[:,:n]@G;V[3,j]=q*(self.se[:,:n]@G)
  out=Jraw@self.free_transform;self._last_jac_key=key;self._last_jac=out
  return out
