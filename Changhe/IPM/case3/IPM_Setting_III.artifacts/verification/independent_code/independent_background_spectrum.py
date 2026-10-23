"""Canonical DR compression at the literal encoded background, no producer imports."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Fr
import argparse,json,time
import numpy as np
from independent_dynamic_spectrum import CanonicalCompression,utc,sha
from q_local_checkpoint import QLocalCheckpoint,exact_affine_chebyshev

class FrozenBackgroundCompression(CanonicalCompression):
 def __init__(self,N,M,background,**kw):
  self.source=QLocalCheckpoint(background)
  super().__init__(N,M,C=self.source.cl,L=self.source.L,**kw)
  q=self.source
  if N<q.N or M<q.M or self.kappa!=q.kappa:raise ValueError('Exact embedding requires containing dimensions and identical map')
  self.base_coeff=[];self.base_conversion=[]
  global_coeff=q.exact_coefficients()
  for k in range(M):
   cc=np.zeros((N+1-k,1))
   if k<q.M:
    tk=Fr(float(self.t[k]));converted=exact_affine_chebyshev(global_coeff[k],(1-tk)/2,(1+tk)/2)
    cc[:len(converted),0]=list(map(float,converted))
    tt=np.unique(np.r_[self.t,np.linspace(-1,1,211)])
    ref=((1+tt)/2)**k*q.polynomial(k,tt);val=self.mode(k,tt,cc)[:,0]
    self.base_conversion.append(dict(k=k,mode_abs_error=float(max(abs(ref-val))),mode_relative_error=float(max(abs(ref-val))/(1+max(abs(ref))))))
   self.base_coeff.append(cc)
  self.base_c=float(sum(self.strain(k,c)[0]for k,c in enumerate(self.base_coeff)))
  self.base_a=float(self.polynomial(0,np.array([-1.]),self.base_coeff[0])[0,0]);self.cw=-self.base_c/(self.C-1);self.cx=self.C*self.cw

 def background_fields(self,order):
  shape=(self.N,len(self.theta));B=np.zeros(shape);Bt=np.zeros(shape);Ba=np.zeros(shape);br=np.zeros(shape);bt=np.zeros(shape)
  for k,c in enumerate(self.base_coeff):
   if not np.any(c):continue
   h,ht=self.mode_fields(k,self.t[1:],c);B+=h[:,0,None]*self.angular[k];Bt+=ht[:,0,None]*self.angular[k];Ba+=h[:,0,None]*self.angular_d[k]
   ur,ut=self.polar_inverse(k,c,self.lr,self.theta,order);br+=ur[:,:,0];bt+=ut[:,:,0]
  Q=self.w[1:]+2*self.kappa*self.s[1:];Z=(1-2*self.s[1:]/Q)[:,None];T=(4*self.s[1:]*self.w[1:]/Q)[:,None]
  return B,Z*B+T*Bt,1/np.tan(self.theta)*B+Ba,br,bt

 def build(self,order):
  B,DrB,DaB,br,bt=self.background_fields(order)
  weight=self.r[1:,None]*self.w[1:,None]*np.sin(self.theta)[None,:]
  rhs=self.cw*B-(self.cx+br)*DrB-bt*DaB
  self.background_summary=dict(a=self.base_a,c=self.base_c,cw=self.cw,cx=self.cx,core_abs_rhs=float(np.max(abs((weight*rhs)[self.r[1:]<=1]))),sampled_abs_rhs=float(np.max(abs(weight*rhs))),mode_embedding_checks=self.base_conversion)
  Q=self.w[1:]+2*self.kappa*self.s[1:];Z=1-2*self.s[1:]/Q;T=4*self.s[1:]*self.w[1:]/Q;cot=1/np.tan(self.theta)
  mats={fb:np.empty((self.nd,self.nd))for fb in [True,False]};full={fb:np.empty((self.nu,self.nd))for fb in [True,False]};field={fb:np.empty((self.N+1,self.M,self.nd))for fb in [True,False]}
  for k,b in enumerate(self.blocks):
   co=b['V'];lo,hi=self.offsets[k:k+2];H,Ht=self.mode_fields(k,self.t[1:],co)
   h=H[:,None,:]*self.angular[k][None,:,None];dr=(Z[:,None]*H+T[:,None]*Ht)[:,None,:]*self.angular[k][None,:,None]
   da=H[:,None,:]*(cot*self.angular[k]+self.angular_d[k])[None,:,None]
   ur,ut=self.polar_inverse(k,co,self.lr,self.theta,order);ch=self.strain(k,co)
   transport=self.cw*h-(self.cx+br[:,:,None])*dr-bt[:,:,None]*da
   feedback=-ur*DrB[:,:,None]-ut*DaB[:,:,None]-ch[None,None,:]/(self.C-1)*(B-self.C*DrB)[:,:,None]
   for fb in [True,False]:
    F=np.zeros((self.N+1,len(self.theta),hi-lo));F[1:]=transport+(feedback if fb else 0.)
    jc,jf,jg=self.project(F);mats[fb][:,lo:hi]=jc;full[fb][:,lo:hi]=jf;field[fb][:,:,lo:hi]=jg
   print(json.dumps(dict(utc=utc(),order=order,k=k,nd=hi-lo)),flush=True)
  return mats,full,field

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--background',required=True);ap.add_argument('--N',type=int,default=64);ap.add_argument('--M',type=int,default=16);ap.add_argument('--orders',default='12,20');ap.add_argument('--tag',default='frozen64');ap.add_argument('--rcond',type=float,default=1e-13);args=ap.parse_args()
 root=Path('research/independent_dynamic_spectrum/verification')/args.tag;root.mkdir(parents=True,exist_ok=True)
 m=FrozenBackgroundCompression(args.N,args.M,args.background,rcond=args.rcond)
 m.source.save_snapshot(root/'literal_background.npz')
 out=dict(started_utc=utc(),status='RUNNING',source=m.source.meta,source_sha256=sha(args.background),code_sha256=sha(__file__),inverse_code_sha256=sha('independent_code/independent_dynamic_spectrum.py'),proof_sha256=sha('research/independent_dynamic_spectrum/PROOF.md'),N=m.N,M=m.M,dimension=m.nd,coefficient_dimension=m.nu,threshold=m.threshold,rcond=m.rcond,cases=[],scope='Literal encoded background embedded algebraically, canonical inverse, coefficient-metric compression. No stationary or continuum spectral theorem.')
 def save():(root/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
 save();previous=None
 for order in map(int,args.orders.split(',')):
  start=time.monotonic();mats,full,field=m.build(order);row=dict(order=order,background=m.background_summary,spectra={})
  for fb in [True,False]:
   desc,ev,evec=m.inspect(mats[fb],full[fb],field[fb]);row['spectra'][str(fb)]=desc
   np.savez_compressed(root/f'order{order}_feedback{fb}.npz',compressed=mats[fb],eigenvalues=ev,leading_eigenvectors=evec[:,:8],leading_full_vectors=np.column_stack([m.lift(evec[:,i])for i in range(8)]),leading_full_residuals=np.column_stack([full[fb]@evec[:,i]-ev[i]*m.lift(evec[:,i])for i in range(8)]),t=m.t,theta=m.theta)
  if previous is not None:row['matrix_change_from_previous']={str(fb):float(np.max(abs(mats[fb]-previous[fb])))for fb in mats}
  previous=mats;row['elapsed_seconds']=time.monotonic()-start;out['cases'].append(row);save()
  print(json.dumps(dict(utc=utc(),order=order,full_leading=row['spectra']['True']['leading_real'],off_leading=row['spectra']['False']['leading_real'],elapsed=row['elapsed_seconds'])),flush=True)
 out.update(status='COMPUTED',finished_utc=utc());save()
if __name__=='__main__':main()
