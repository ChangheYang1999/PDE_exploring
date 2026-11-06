"""Block cyclic reduction with orthogonal elimination, for a single endpoint BVP.
Intermediate endpoint unknowns are eliminated by QR, never by exponentially
growing forward transfer. Stored back-substitution uses two d*d matrices per
removed endpoint. This is an alternative to global sparse SuperLU.
"""
import os
import numpy as np
from scipy.linalg import qr,solve_triangular,solve
def endpoint(E,B,rs,elens):
 d=E[0].shape[0];I=np.eye(d);r0=0;nc=0;root=[];acts=[]
 for count in elens:
  active=[(nc+i,nc+i+1,E[r0+i],I,rs[r0+i]) for i in range(count)]
  for i in range(count):E[r0+i]=None
  while len(active)>1:
   nexts=[]
   for t in range(0,len(active)-1,2):
    left,mid,A1,B1,r1=active[t];j,right,A2,B2,r2=active[t+1];assert j==mid
    Q,R=qr(np.r_[B1,A2],mode='full',check_finite=False,overwrite_a=True)
    q1,q2=Q[:d],Q[d:];y=q1.T@r1+q2.T@r2
    QL=q1.T@A1;QR=q2.T@B2
    coeff=solve_triangular(R[:d],np.c_[-QL[:d],-QR[:d],y[:d]],check_finite=False,overwrite_b=True)
    acts.append((left,mid,right,coeff))
    nexts.append((left,right,QL[d:].copy(),QR[d:].copy(),y[d:].copy()))
    active[t]=active[t+1]=None
   if len(active)%2:nexts.append(active[-1])
   active=nexts
  root.append(active[0]);r0+=count;nc+=count+1
 n=B.shape[1];M=np.zeros((n,n));b=np.zeros(n)
 for i,(lo,hi,A0,B0,r) in enumerate(root):
  M[i*d:(i+1)*d,2*i*d:(2*i+1)*d]=A0;M[i*d:(i+1)*d,(2*i+1)*d:(2*i+2)*d]=B0;b[i*d:(i+1)*d]=r
 M[2*d:]=B;b[2*d:]=rs[-1]
 if os.environ.get('IPM_EQUIL_ENDPOINTS','0')=='1':
  from scipy.linalg import lu_factor,lu_solve
  A=M.copy();row=np.ones(n);col=np.ones(n)
  for _ in range(5):
   dr=1/np.sqrt(np.maximum(np.max(abs(A),axis=1),1e-150));A*=dr[:,None];row*=dr
   dc=1/np.sqrt(np.maximum(np.max(abs(A),axis=0),1e-150));A*=dc;col*=dc
  lu=lu_factor(A,overwrite_a=True,check_finite=False);del A
  z=col*lu_solve(lu,row*b,check_finite=False)
  # Long-double residual only, on the small final endpoint/BC dense problem.
  # Used for refinement, not a proof: all upstream collocation factors remain double.
  Mlong=np.asarray(M,dtype=np.longdouble);bL=np.asarray(b,dtype=np.longdouble)
  best=np.inf
  for _ in range(3):
   err=np.asarray(bL-Mlong@np.asarray(z,dtype=np.longdouble),dtype=float)
   if np.max(abs(err))>=best:break
   best=np.max(abs(err));dz=col*lu_solve(lu,row*err,check_finite=False);zz=z+dz
   new=np.max(np.abs(bL-Mlong@np.asarray(zz,dtype=np.longdouble)))
   if new>=best:break
   z=zz
 else:z=solve(M,b,assume_a='gen',check_finite=False)
 ends=np.zeros((nc,d));off=0
 for i,(lo,hi,*_) in enumerate(root):ends[lo]=z[(2*i)*d:(2*i+1)*d];ends[hi]=z[(2*i+1)*d:(2*i+2)*d]
 for lo,mid,hi,C in reversed(acts):ends[mid]=C[:,:d]@ends[lo]+C[:,d:2*d]@ends[hi]+C[:,-1]
 return np.r_[ends.ravel(),z[4*d:]]
