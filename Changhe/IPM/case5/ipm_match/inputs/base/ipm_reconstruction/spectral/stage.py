"""Eliminate each Poisson harmonic's 2p local Gauss stages analytically.
The remaining dense factor has p*nf rather than p*(nf+2*ng) rows.
"""
import numpy as np
from scipy.linalg import lu_factor,lu_solve
class Reduced:
 def __init__(self,A,J,D,h,j):
  f,g=A.f,A.g;p=len(D);k=A.k;q=2. if not j else 1+1/A.c;sig=q-1;I=np.eye(p);k=A.k
  Mp=np.linalg.inv(D[None,:,:]+h*(q-k[:,None,None])*I);Mm=np.linalg.inv(D[None,:,:]+h*(q+k[:,None,None])*I)
  vm=(Mp-Mm)/(2*k[:,None,None]);um=(Mp+Mm)/2
  JJ=J[:,:f];C1=A.S1-sig*A.S0;sch=np.kron(D,np.eye(f)).reshape(p,f,p,f);ii=np.arange(p)
  sch[ii,:,ii,:]-=h*JJ[:,:,:f]
  self.weights=[]
  for b in range(2):
   ids=np.arange(min(g,f-b));lf=ids+b;R=-D[None,:,:]*A.S0[ids,lf,None,None]+h*I*C1[ids,lf,None,None]
   Gf=vm[ids]@R;Uf=um[ids]@R
   for i in range(p):
    # for each stage t, Fourier column l is coupled to its neighbouring stream frequencies only
    for t in range(p):
     sch[i,:,t,:][:,lf]-=h*(JJ[i,:,f:f+g][:,ids]*Gf[ids,i,t]+JJ[i,:,f+g:][:,ids]*Uf[ids,i,t])
   self.weights.append((ids,lf,Gf,Uf))
  self.S=lu_factor(sch.reshape(p*f,p*f),overwrite_a=True,check_finite=False);self.Mp=Mp;self.Mm=Mm;self.p=p;self.f=f;self.g=g;self.JJ=JJ;self.h=h;self.s0=A.S0;self.k=k
 def solve(self,b):
  p,f,g=self.p,self.f,self.g;d=f+2*g;k=self.k[:,None,None];matrix=b.ndim>1;bb=b.reshape(p,d,-1);F,G,U=bb[:,:f],bb[:,f:f+g],bb[:,f+g:]
  u0=(U+self.s0@F).transpose(1,0,2);gv=G.transpose(1,0,2)
  wp=self.Mp@(u0+k*gv);wm=self.Mm@(u0-k*gv)
  g0=((wp-wm)/(2*k)).transpose(1,0,2);u0=((wp+wm)*.5).transpose(1,0,2)
  bf=F+self.h*(self.JJ[:,:,f:f+g]@g0+self.JJ[:,:,f+g:]@u0)
  dx=lu_solve(self.S,bf.reshape(p*f,-1),check_finite=False).reshape(p,f,-1)
  for ids,lf,Gf,Uf in self.weights:
   v=dx[:,lf].transpose(1,0,2);g0[:,ids]+=(Gf@v).transpose(1,0,2);u0[:,ids]+=(Uf@v).transpose(1,0,2)
  y=np.concatenate([dx,g0,u0],axis=1).reshape(p*d,-1);return y if matrix else y[:,0]
