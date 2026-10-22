"""Independent serialized r2-spline value reader; no fitting-lane imports.

The mathematical basis is specified in read-only source snapshots. SciPy's
BSpline evaluator is used instead of the fitting lane's Torch design matrices.
Cartesian differences and the Duffy full-plane inverse live in separate files.
"""
from pathlib import Path
import hashlib
import numpy as np
from scipy.interpolate import BSpline

class R2SourceField:
 """Native seed source with its own recorded geometry, independent of unknowns."""
 def __init__(self,meta,raw,default):
  get=lambda key:meta.get('seed_'+key,getattr(default,{'deg':'degree'}.get(key,key)))
  self.bb=float(meta['beta_seed']);self.L=float(get('L'))
  self.K=int(get('K'));self.Nt=int(get('Nt'));self.degree=int(get('deg'));self.grade=float(get('grade'))
  if str(meta.get('seed_rmap',meta.get('rmap')))!='r2':raise ValueError('Only explicit native r2 source geometry is supported')
  self.edges=np.linspace(0,1,self.Nt+1)**self.grade
  self.knots=np.r_[np.zeros(self.degree),self.edges,np.ones(self.degree)]
  self.nb=len(self.knots)-self.degree-1
  self.rawG=np.asarray(raw).copy()
  if self.rawG.size!=self.K*self.nb:raise ValueError('Seed source coefficients do not match native geometry')
  coeff=self.rawG.reshape(self.K,self.nb).copy()
  for k in range(self.K):coeff[k,:k//2]=0
  self.spline=BSpline(self.knots,coeff.T,self.degree,extrapolate=False)
 def radial(self,r):
  r=np.asarray(r,dtype=float);logz=-np.log1p((r/self.L)**2)/(2*self.bb);t=-np.expm1(logz)
  ans=self.spline(t)*np.exp((self.bb+1)*logz)[...,None]
  ans[...,1::2]*=(r/np.hypot(r,self.L))[...,None]
  return ans
 def strain(self):
  a=self.spline.integrate(0.,1.)
  return -self.bb*self.L*(a[1]-(a[3] if self.K>3 else 0))/4 if self.K>1 else 0.

class R2State:
 def __init__(self,path):
  self.path=Path(path);self.sha256=hashlib.sha256(self.path.read_bytes()).hexdigest()
  with np.load(path,allow_pickle=False) as z:
   self.meta={k:z[k].item() for k in z.files if z[k].ndim==0}
   self.rawF=z['cF'].copy();self.rawG=z['cG'].copy()
   self.extG=z['cG_ext'].copy() if 'cG_ext' in z.files and z['cG_ext'].size else None
   # New lambda archives retain the original seed-basis forcing separately.
   # Only the effective, already lambda-scaled stage coefficients enter V.
   self.seed_defectG=None
   seed_schema=('beta_seed' in z.files and float(z['beta_seed'])>0)
   if seed_schema:
    self.seed_defectG=z['cG_f'].copy() if 'cG_f' in z.files and z['cG_f'].size else None
   if 'cG_f_effective' in z.files:
    self.defectG=z['cG_f_effective'].copy() if z['cG_f_effective'].size else None
    self.forcing_schema='effective_stage_coefficients'
   elif seed_schema:
    self.defectG=None
    self.forcing_schema='seed_only_requires_explicit_reconstruction'
   else:
    self.defectG=z['cG_f'].copy() if 'cG_f' in z.files and z['cG_f'].size else None
    self.forcing_schema='legacy_stage_coefficients'
   self.code_hashes=z['code_sha256'].tolist() if 'code_sha256' in z.files else None
  if self.meta.get('rmap')!='r2':raise ValueError('Only explicit r2 snapshots accepted')
  self.beta=float(self.meta['beta']);self.bb=float(self.meta['beta_basis']);self.L=float(self.meta['L'])
  self.degree=int(self.meta['deg']);self.Nt=int(self.meta['Nt']);self.K=int(self.meta['K']);self.grade=float(self.meta['grade'])
  self.edges=np.linspace(0,1,self.Nt+1)**self.grade
  self.knots=np.r_[np.zeros(self.degree),self.edges,np.ones(self.degree)]
  self.nb=len(self.knots)-self.degree-1
  if self.rawF.size!=self.K*self.nb or self.rawG.size!=self.K*self.nb:raise ValueError('inconsistent dimensions')
  self.Fs=self.make_spline(self.rawF);self.Gs=self.make_spline(self.rawG)
  self.Es=self.make_spline(self.extG) if self.extG is not None else None
  self.Ds=self.make_spline(self.defectG) if self.defectG is not None else None
  self.native_source=(self.meta.get('source_mode')=='fixed_velocity_block')
  self.seed_field=R2SourceField(self.meta,self.seed_defectG,self) if self.native_source and self.seed_defectG is not None else None
  self.SDs=self.seed_field.spline if self.seed_field is not None else None
  if self.native_source:
   if self.SDs is None or float(self.meta.get('beta_seed',0))<=0:raise ValueError('Fixed source block requires seed coefficients and positive beta_seed')
   if self.Ds is not None:raise ValueError('Ambiguous fixed source block with effective stage forcing')
   self.forcing_schema='fixed_velocity_block_native_seed_basis'
 def make_spline(self,raw):
  c=np.array(raw).reshape(self.K,self.nb).copy()
  for k in range(self.K):c[k,:k//2]=0
  return BSpline(self.knots,c.T,self.degree,extrapolate=False)
 def radial(self,r,kind='G'):
  if kind=='native_seed':
   if self.seed_field is None:raise ValueError('No native seed source')
   return self.seed_field.radial(r)
  r=np.asarray(r,dtype=float)
  # These forms avoid subtracting two nearly equal endpoint powers.
  bb=float(self.meta['beta_seed']) if kind=='native_seed' else self.bb
  logz=-np.log1p((r/self.L)**2)/(2*bb);t=-np.expm1(logz)
  spline={'F':self.Fs,'G':self.Gs,'external':self.Es,'defect':self.Ds,'native_seed':self.SDs}[kind]
  if spline is None:raise ValueError('external coefficients unavailable')
  p=bb+(2 if kind=='F' else 1)
  values=spline(t)*np.exp(p*logz)[...,None]
  values[...,1::2]*=(r/np.hypot(r,self.L))[...,None]
  return values
 def divided(self,x,y,kind='G'):
  x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));r=np.hypot(x,y)
  eta=np.divide(-y,r,out=np.zeros_like(y),where=r!=0)
  count=self.seed_field.K if kind=='native_seed' else self.K
  ang=np.empty(r.shape+(count,));ang[...,0]=1
  if count>1:ang[...,1]=eta
  for k in range(2,count):ang[...,k]=2*eta*ang[...,k-1]-ang[...,k-2]
  return np.sum(self.radial(r,kind)*ang,axis=-1)
 def theta(self,x,y):return np.asarray(x)**2*self.divided(x,y,'F')
 def omega(self,x,y):return np.asarray(x)*self.divided(x,y,'G')
 def mixed_omega(self,x,y):
  eps=float(self.meta.get('eps',1.))
  if float(self.meta.get('lam',0.))!=0 and self.Ds is None and not self.native_source:
   raise ValueError('Nonzero lambda requires additive coefficients or an explicit separately verified S0 reconstruction')
  value=eps*self.omega(x,y)
  if eps!=1:value=value+(1-eps)*np.asarray(x)*self.divided(x,y,'external')
  if self.Ds is not None:value=value+np.asarray(x)*self.divided(x,y,'defect')
  if self.native_source:value=value+float(self.meta.get('lam',0.))*np.asarray(x)*self.divided(x,y,'native_seed')
  return value
 def strain(self,kind='G'):
  if kind=='native_seed':
   if self.seed_field is None:raise ValueError('No native seed source')
   return self.seed_field.strain()
  spl={'G':self.Gs,'external':self.Es,'defect':self.Ds,'native_seed':self.SDs}[kind]
  bb=float(self.meta['beta_seed']) if kind=='native_seed' else self.bb
  vals=spl.integrate(0.,1.)
  # Angular orthogonality and rho_odd*dr/dt*D_G=beta_basis*L.
  return -bb*self.L*(vals[1]-(vals[3] if self.K>3 else 0))/4
 def center(self):
  ans={}
  for kind,spl in [('F',self.Fs),('G',self.Gs)]:
   values=spl(0.);slopes=spl.derivative()(0.)
   p=self.bb+(2 if kind=='F' else 1)
   q0=(slopes[0]-p*values[0])/(2*self.bb*self.L**2)
   q2=slopes[2]/(2*self.bb*self.L**2) if self.K>2 else 0.
   ans[kind]={'value':float(values[0]),'dy':float(-values[1]/self.L) if self.K>1 else 0.,'x2_coefficient':float(q0-q2),'y2_coefficient':float(q0+q2)}
  eps=float(self.meta.get('eps',1.));cg=self.strain();ce=self.strain('external') if self.Es is not None else None
  cd=float(self.strain('defect')) if self.Ds is not None else 0.
  if self.native_source:cd+=float(self.meta.get('lam',0.))*float(self.strain('native_seed'))
  cm=(cg if eps==1 else eps*cg+(1-eps)*ce)+cd
  a=ans['F']['value'];b=ans['G']['value'];A=self.beta-cm
  ans.update(c_self=float(cg),c_external=float(ce) if ce is not None else None,c_mixed=float(cm),c_additive_defect=cd,a0_error=a-1.,b0_normalization_error=b-4/self.beta,strain_error=cm-1-self.beta/2,
             R_F_center=2*A*a-(self.beta-2)*a,R_G_center=(A+1)*b-2*a,
             b0_compatibility_error=b-4*a/self.beta,a0_metadata_error=a-float(self.meta.get('a0',a)))
  return ans
