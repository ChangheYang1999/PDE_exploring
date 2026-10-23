"""Independent canonical DR compression. No producer module is imported."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,math,time
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import svd,eig
from scipy.special import roots_laguerre,roots_legendre,roots_jacobi
from log_radius_inverse import LogRadiusQCheckpoint
from complementary_inverse_charts import ComplementaryQ


def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class CanonicalCompression:
 coordinates_log=LogRadiusQCheckpoint.coordinates_log
 stable_coordinates=ComplementaryQ.stable_coordinates
 def __init__(self,N,M,C=3.,L=1.,threshold=1e-6,rcond=1e-13):
  self.N=N;self.M=M;self.C=C;self.L=L;self.kappa=1/(1-1/C);self.delta=1/self.kappa;self.log_core=math.log(L)-self.kappa*math.log(2.)
  self.threshold=threshold;self.rcond=rcond
  self.t=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1));self.s=(1+self.t)/2;self.w=(1-self.t)/2
  self.r=L*np.sqrt(self.s)/(1-self.t)**self.kappa;self.lr=np.log(self.r[1:]);self.theta=(np.arange(3*M)+.5)*np.pi/(6*M)
  self.angular=np.cos(2*np.arange(M)[:,None]*self.theta[None,:]);self.angular_d=-2*np.arange(M)[:,None]*np.sin(2*np.arange(M)[:,None]*self.theta[None,:])
  self.norm=np.r_[1.,np.full(M-1,2.)]/(3*M);self.blocks=[];self.offsets=[0];self.full_offsets=[0]
  for k in range(M):
   sk=(2*self.t-1-self.t[k])/(1-self.t[k]);A=self.s[:,None]**k*np.polynomial.chebyshev.chebvander(sk,N-k)
   U,S,Vh=svd(A,full_matrices=False,lapack_driver='gesvd');keep=S>=threshold*S[0];allkeep=S>rcond*S[0];V=Vh[keep].T
   self.blocks.append({'k':k,'A':A,'U':U,'S':S,'Vh':Vh,'keep':keep,'allkeep':allkeep,'V':V})
   self.offsets.append(self.offsets[-1]+int(keep.sum()));self.full_offsets.append(self.full_offsets[-1]+N+1-k)
  self.nd=self.offsets[-1];self.nu=self.full_offsets[-1]
  self.cw=.25/(C-1);self.cx=C*self.cw

 def polynomial(self,k,t,coef):
  t=np.asarray(t);z=(2*t-1-self.t[k])/(1-self.t[k]);z=z[...,None]
  b1=np.zeros(z.shape[:-1]+(coef.shape[1],),dtype=np.result_type(t,float));b2=np.zeros_like(b1)
  for c in coef[:0:-1]:b0=c+2*z*b1-b2;b2,b1=b1,b0
  return coef[0]+z*b1-b2

 def mode(self,k,t,coef):return ((1+np.asarray(t))/2)[...,None]**k*self.polynomial(k,t,coef)

 def mode_fields(self,k,t,coef):
  h=self.mode(k,t,coef);dt=np.imag(self.mode(k,np.asarray(t,dtype=complex)+1e-25j,coef))/1e-25
  return h,dt

 def laguerre_polar_inverse(self,k,coef,lr,theta,order):
  """U_r/r and U_theta/r for all coefficient directions in one angular block."""
  lr=np.asarray(lr,float);theta=np.asarray(theta,float);nn=coef.shape[1];shape=(len(lr),len(theta),nn)
  ur=np.zeros(shape);ut=np.zeros(shape);z,zw=roots_laguerre(order)
  t,s,w=self.stable_coordinates(lr);d=w[:,None]*self.mode(k,t,coef)
  harmonics=[(1,1.)] if k==0 else [(2*k-1,-.5),(2*k+1,.5)]
  for j,sign in harmonics:
   for exterior in [False,True]:
    m=j-1 if exterior else j+1
    if m<2:continue
    rate=m-2+self.delta if exterior else m+2
    v=z/rate;logs=lr[:,None]+(v[None,:] if exterior else -v[None,:])
    tt,ss,ww=self.stable_coordinates(logs);beta=self.polynomial(k,tt,coef)
    if exterior:
     scale=.5*np.exp(self.delta*(math.log(self.L)-lr))[:,None]*ss**(self.delta/2)
     radial=scale[...,None]*ss[...,None]**k*beta
    else:radial=ww[...,None]*ss[...,None]**k*beta
    moment=sign*np.einsum('iqd,q->id',radial,zw)/rate
    local=sign*d
    ur+=(-m/2 if exterior else m/2)*moment[:,None,:]*np.cos(m*theta)[None,:,None]
    ut+=(m*moment-local)[:,None,:]*np.sin(m*theta)[None,:,None]/2
  assert np.isfinite(ur).all() and np.isfinite(ut).all()
  return ur,ut

 def polar_inverse(self,k,coef,lr,theta,order):
  """Polynomial-exact exterior; composite interior including its infinite tail."""
  lr=np.asarray(lr,float);theta=np.asarray(theta,float);nn=coef.shape[1]
  ur=np.zeros((len(lr),len(theta),nn));ut=np.zeros_like(ur)
  t,s,w=self.stable_coordinates(lr);local=w[:,None]*s[:,None]**k*self.polynomial(k,t,coef)
  harmonics=[(1,1.)] if k==0 else [(2*k-1,-.5),(2*k+1,.5)]
  for j,sign in harmonics:
   for exterior in [False,True]:
    m=j-1 if exterior else j+1
    if m<2:continue
    if exterior:
     epower=k-m//2;assert epower in [0,1]
     degree=self.N-k+epower+1;q=max(order,(degree+2)//2)
     alpha=self.kappa*(m-2);z,ww=roots_jacobi(q,alpha,0.)
     u=(z+1)/2;qw=ww*2.**(-alpha-1)
     ss=s[:,None]+w[:,None]*u[None,:];tt=2*ss-1;wp=w[:,None]*(1-u[None,:]);Q=wp+2*self.kappa*ss
     val=ss[...,None]**epower*Q[...,None]*self.polynomial(k,tt,coef)
     moment=(w*s**(m/2-1)/2)[:,None]*np.einsum('iqd,q->id',val,qw)
    else:
     rate=m+2;panels=max(24,math.ceil(48/(rate*.125)));edges=np.linspace(0,48,panels+1)
     z,wz=roots_legendre(order);grid=((edges[1:]+edges[:-1])[:,None]/2+(edges[1:]-edges[:-1])[:,None]*z[None,:]/2).reshape(-1)
     weights=((edges[1:]-edges[:-1])[:,None]*wz[None,:]/2).reshape(-1)*np.exp(-grid)/rate
     logs=lr[:,None]-grid[None,:]/rate;tt,ss,wp=self.stable_coordinates(logs)
     val=wp[...,None]*ss[...,None]**k*self.polynomial(k,tt,coef)
     moment=np.einsum('iqd,q->id',val,weights)
     zz,zw=roots_laguerre(48);logs=lr[:,None]-(48+zz[None,:])/rate;tt,ss,wp=self.stable_coordinates(logs)
     val=wp[...,None]*ss[...,None]**k*self.polynomial(k,tt,coef)
     moment+=np.exp(-48)/rate*np.einsum('iqd,q->id',val,zw)
    moment*=sign;d=sign*local
    ur+=(-m/2 if exterior else m/2)*moment[:,None,:]*np.cos(m*theta)[None,:,None]
    ut+=(m*moment-d)[:,None,:]*np.sin(m*theta)[None,:,None]/2
  assert np.isfinite(ur).all() and np.isfinite(ut).all()
  return ur,ut

 def strain(self,k,coef):
  if k==0:return -self.polynomial(k,np.array([-1.]),coef)[0]/4
  if k>2:return np.zeros(coef.shape[1])
  t,w=roots_legendre((self.N+6)//2);s=(1+t)/2
  factor=((1-t)/16+self.kappa*s/4)*(1 if k==1 else -s)
  return np.einsum('i,id->d',w*factor,self.polynomial(k,t,coef))

 def base_fields(self,order):
  return self.polar_inverse(0,np.ones((1,1)),self.lr,self.theta,order)

 def project(self,F):
  # F has every radial node, angle, and directional column. Endpoint row supplied analytically.
  modes=np.einsum('iqd,kq->ikd',F,self.angular)*self.norm[None,:,None]
  compressed=[];full=[];field=[]
  for k,b in enumerate(self.blocks):
   U,S,Vh=b['U'],b['S'],b['Vh'];keep=b['keep'];ak=b['allkeep'];f=modes[:,k,:]
   compressed.append((U[:,keep].T@f)/S[keep,None])
   fc=Vh[ak].T@((U[:,ak].T@f)/S[ak,None]);full.append(fc)
   field.append(U[:,ak]@(U[:,ak].T@f))
  return np.vstack(compressed),np.vstack(full),np.stack(field,axis=1)

 def build(self,order):
  br,bt=self.base_fields(order);br=br[:,:,0];bt=bt[:,:,0]
  sig=self.s[1:];w=self.w[1:];Q=w+2*self.kappa*sig;Z=1-2*sig/Q;T=4*sig*w/Q;cot=1/np.tan(self.theta)
  mats={fb:np.empty((self.nd,self.nd))for fb in [True,False]};full={fb:np.empty((self.nu,self.nd))for fb in [True,False]}
  field={fb:np.empty((self.N+1,self.M,self.nd))for fb in [True,False]}
  for k,b in enumerate(self.blocks):
   coef=b['V'];lo,hi=self.offsets[k:k+2];H,Ht=self.mode_fields(k,self.t[1:],coef)
   h=H[:,None,:]*self.angular[k][None,:,None]
   dr=(Z[:,None]*H+T[:,None]*Ht)[:,None,:]*self.angular[k][None,:,None]
   da=H[:,None,:]*(cot*self.angular[k]+self.angular_d[k])[None,:,None]
   ur,ut=self.polar_inverse(k,coef,self.lr,self.theta,order);ch=self.strain(k,coef)
   transport=self.cw*h-(self.cx+br[:,:,None])*dr-bt[:,:,None]*da
   feedback=-ur*Z[:,None,None]-ut*cot[None,:,None]-ch[None,None,:]/(self.C-1)*(1-self.C*Z[:,None,None])
   for fb in [True,False]:
    F=np.zeros((self.N+1,len(self.theta),hi-lo));F[1:]=transport+(feedback if fb else 0.)
    jc,jfull,jfield=self.project(F);mats[fb][:,lo:hi]=jc;full[fb][:,lo:hi]=jfull;field[fb][:,:,lo:hi]=jfield
   print(json.dumps({'utc':utc(),'order':order,'k':k,'nd':hi-lo}),flush=True)
  return mats,full,field

 def evaluate(self,v):
  return np.stack([b['A']@v[self.full_offsets[k]:self.full_offsets[k+1]]for k,b in enumerate(self.blocks)],axis=1)

 def lift(self,z):return np.concatenate([b['V']@z[self.offsets[k]:self.offsets[k+1]]for k,b in enumerate(self.blocks)])

 def inspect(self,J,FJ,GJ,top=4):
  values,vectors=eig(J);ix=np.argsort(-values.real);values=values[ix];vectors=vectors[:,ix];rows=[]
  weight=self.r[:,None]*self.w[:,None]*np.sin(self.theta)[None,:]
  for i in range(min(top,len(values))):
   ev=values[i];z=vectors[:,i];v=self.lift(z);jv=FJ@z;res=jv-ev*v
   dens=weight*(self.evaluate(v)@self.angular);res_field=weight*((np.einsum('ikd,d->ik',GJ,z)-ev*self.evaluate(v))@self.angular)
   tot=np.sum(abs(dens)**2);shells=[(0.,.1),(.1,1.),(1.,10.),(10.,100.),(100.,np.inf)]
   frac=[float(np.sum(abs(dens[(self.r>lo)&(self.r<=hi)])**2)/tot)for lo,hi in shells]
   rows.append({'lambda':[float(ev.real),float(ev.imag)],'compressed_relative_residual':float(np.linalg.norm(J@z-ev*z)/(np.linalg.norm(J@z)+abs(ev)*np.linalg.norm(z))),
    'full_coefficient_residual_norm':float(np.linalg.norm(res)),'full_coefficient_relative_residual':float(np.linalg.norm(res)/(np.linalg.norm(jv)+abs(ev)*np.linalg.norm(v))),
    'field_density_sup':float(np.max(abs(dens))),'lift_residual_field_sup':float(np.max(abs(res_field))),'lift_residual_field_relative_sup':float(np.max(abs(res_field))/(abs(ev)*np.max(abs(dens)))) if abs(ev)>0 else None,
    'unweighted_node_squared_fractions':frac,'core_density_sup':float(np.max(abs(dens[self.r<=1]))),'core_lift_residual_sup':float(np.max(abs(res_field[self.r<=1]))),
    'radius_of_largest_node_squared_sum':float(self.r[np.argmax(np.sum(abs(dens)**2,axis=1))])})
  return {'leading_real':float(values[0].real),'spectral_radius':float(max(abs(values))),'positive_count':int(np.count_nonzero(values.real>1e-10)),'leading':rows},values,vectors


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--N',type=int,default=24);ap.add_argument('--M',type=int,default=6);ap.add_argument('--orders',default='12,20');ap.add_argument('--tag',default='constant24');ap.add_argument('--threshold',type=float,default=1e-6);args=ap.parse_args()
 root=Path('research/independent_dynamic_spectrum/verification')/args.tag;root.mkdir(parents=True,exist_ok=True)
 model=CanonicalCompression(args.N,args.M,threshold=args.threshold)
 out={'started_utc':utc(),'status':'RUNNING','code_sha256':sha(__file__),'proof_sha256':sha('research/independent_dynamic_spectrum/PROOF.md'),'N':args.N,'M':args.M,'dimension':model.nd,'coefficient_dimension':model.nu,'inverse_method':'Gauss-Jacobi polynomial-exact exterior plus composite log-interior and infinite-tail quadrature','threshold':model.threshold,'rcond':model.rcond,'cases':[],
  'scope':'Canonical finite coefficient-metric compression at a nonstationary constant-beta start; numerical quadrature only, no continuum spectral theorem.'}
 def save():(root/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
 save();previous=None
 for order in map(int,args.orders.split(',')):
  start=time.monotonic();mats,full,field=model.build(order);row={'order':order,'spectra':{}}
  for fb in [True,False]:
   desc,ev,evec=model.inspect(mats[fb],full[fb],field[fb]);row['spectra'][str(fb)]=desc
   np.savez_compressed(root/f'order{order}_feedback{fb}.npz',compressed=mats[fb],full_action=full[fb],projected_mode_action=field[fb],eigenvalues=ev,eigenvectors=evec,
    t=model.t,theta=model.theta,**{f'V{k}':b['V']for k,b in enumerate(model.blocks)})
  if previous is not None:row['max_entry_change']={str(fb):float(np.max(abs(mats[fb]-previous[fb])))for fb in [True,False]}
  previous=mats;row['elapsed_seconds']=time.monotonic()-start;out['cases'].append(row);save();print(json.dumps({'utc':utc(),'order':order,'full_leading':row['spectra']['True']['leading_real'],'off_leading':row['spectra']['False']['leading_real'],'elapsed':row['elapsed_seconds']}),flush=True)
 out.update(status='COMPUTED',finished_utc=utc());save()

if __name__=='__main__':main()
