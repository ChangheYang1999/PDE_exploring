"""Own free-beta chart and symbolic parity-factor residuals, packet114."""
from collections import OrderedDict
import numpy as np
from stream_basis import StreamBasis,evaluate_terms,derivative


def make_chart(beta,ni,nj,shifts=(0,1),a0=1.):
 b=StreamBasis(beta,ni,nj,shifts,a0)
 piv=[b.labels.index((0,0,0)),b.labels.index((0,1,0))]
 free=[j for j in range(b.n) if j not in piv]
 M=b.Cconstraint[:,piv]
 b.Cbase=np.zeros(b.n);b.Cbase[piv]=np.linalg.solve(M,b.Ctarget)
 b.Cnull=np.zeros((b.n,len(free)));b.Cnull[free,np.arange(len(free))]=1.;b.Cnull[piv,:]=-np.linalg.solve(M,b.Cconstraint[:,free])
 dp=b.labels.index((0,0,0));df=[j for j in range(b.n) if j!=dp]
 b.Dbase=np.zeros(b.n);b.Dbase[dp]=b.Dtarget[0]/b.Dconstraint[0,dp]
 b.Dnull=np.zeros((b.n,len(df)));b.Dnull[df,np.arange(len(df))]=1.;b.Dnull[dp,:]=-b.Dconstraint[0,df]/b.Dconstraint[0,dp]
 b.nc=len(free);b.nd=len(df);b.size=b.nc+b.nd;b.freeC=free;b.freeD=df
 return b


def divide_terms(terms,power):
 if any(a<power for a,y,ns,nc in terms):raise ValueError('requested factor does not divide every monomial')
 return {(a-power,y,ns,nc):c for (a,y,ns,nc),c in terms.items()}


def prepare_divided(basis,points):
 p=np.asarray(points,float);x,y=p.T;cp=[];dt=[]
 for row in basis.psi:
  g=divide_terms(row['Omega'],1)
  cp.append({'aV':divide_terms(row['U1'],1),'U2':row['U2'],'g':g,'gx':derivative(g,0,basis.s),'gy':derivative(g,1,basis.s)})
 for row in basis.theta:
  f=divide_terms(row['Theta'],2);dt.append({'f':f,'fx':derivative(f,0,basis.s),'fy':derivative(f,1,basis.s)})
 ev=lambda rows:{k:np.stack([evaluate_terms(row[k],x,y,basis.s) for row in rows],axis=1) for k in rows[0]}
 return {'points':p,'C':ev(cp),'D':ev(dt)}


def divided_fields(basis,data,C,D):
 p=data['points'];x,y=p.T
 q={k:m@C for k,m in data['C'].items()};q.update({k:m@D for k,m in data['D'].items()})
 q['A']=basis.beta+q['aV'];q['B']=basis.beta*y+q['U2']
 q['F_terms']=np.column_stack((q['A']*(2*q['f']+x*q['fx']),q['B']*q['fy'],-(basis.beta-2)*q['f']))
 q['G_terms']=np.column_stack((q['A']*(q['g']+x*q['gx']),q['B']*q['gy'],q['g'],-(2*q['f']+x*q['fx'])))
 q['RF']=q['F_terms'].sum(axis=1);q['RG']=q['G_terms'].sum(axis=1)
 q['NF']=abs(q['F_terms']).sum(axis=1);q['NG']=abs(q['G_terms']).sum(axis=1)
 return q


class DividedProblem:
 def __init__(self,basis,points,reference_beta,regularization=0.):
  self.basis=basis;self.data=prepare_divided(basis,points);self.C={k:m@basis.Cnull for k,m in self.data['C'].items()};self.D={k:m@basis.Dnull for k,m in self.data['D'].items()}
  r=np.sqrt(1+np.sum(np.asarray(points)**2,axis=1));s0=1/reference_beta
  self.wF=r**(1+3*s0)/basis.a0;self.wG=r**(1+2*s0)/basis.a0;self.scale=1/np.sqrt(len(r));self.reg=regularization;self.last=None
 def residual(self,z):
  C,D=self.basis.coefficients(z);q=divided_fields(self.basis,self.data,C,D);self.last=(z.copy(),q)
  out=np.r_[self.scale*self.wF*q['RF'],self.scale*self.wG*q['RG']]
  return np.r_[out,self.reg*z] if self.reg else out
 def jacobian(self,z):
  if self.last is None or not np.array_equal(z,self.last[0]):self.residual(z)
  q=self.last[1];x=self.data['points'][:,0,None];c=self.C;d=self.D
  col=lambda k:q[k][:,None]
  fc=c['aV']*(2*col('f')+x*col('fx'))+c['U2']*col('fy')
  fd=col('A')*(2*d['f']+x*d['fx'])+col('B')*d['fy']-(self.basis.beta-2)*d['f']
  gc=c['aV']*(col('g')+x*col('gx'))+col('A')*(c['g']+x*c['gx'])+c['U2']*col('gy')+col('B')*c['gy']+c['g']
  gd=-(2*d['f']+x*d['fx'])
  J=np.vstack((self.scale*self.wF[:,None]*np.hstack((fc,fd)),self.scale*self.wG[:,None]*np.hstack((gc,gd))))
  return np.vstack((J,self.reg*np.eye(self.basis.size))) if self.reg else J


class FreeBetaProblem:
 def __init__(self,ni,nj,points,reference_beta,shifts=(0,1),a0=1.,regularization=0.):
  self.ni=ni;self.nj=nj;self.points=np.asarray(points,float);self.reference_beta=float(reference_beta);self.shifts=tuple(shifts);self.a0=a0;self.regularization=regularization;self.cache=OrderedDict();self.rebuilds=0
 def case(self,beta):
  beta=float(beta)
  if beta not in self.cache:
   b=make_chart(beta,self.ni,self.nj,self.shifts,self.a0);self.cache[beta]=DividedProblem(b,self.points,self.reference_beta,self.regularization);self.rebuilds+=1
  self.cache.move_to_end(beta)
  while len(self.cache)>3:self.cache.popitem(last=False)
  return self.cache[beta]
 def residual(self,z):return self.case(z[0]).residual(z[1:])
 def jacobian(self,z):
  beta=z[0];case=self.case(beta);jc=case.jacobian(z[1:]);h=min(1e-5*max(1.,abs(beta)),(beta-2)/4)
  jb=(self.case(beta+h).residual(z[1:])-self.case(beta-h).residual(z[1:]))/(2*h)
  return np.column_stack((jb,jc))


def metrics(R,N,points):
 R=np.asarray(R);N=np.asarray(N);q=np.divide(abs(R),N,out=np.where(R==0,0.,np.inf),where=N!=0);j=int(np.argmax(q));k=int(np.argmax(abs(R)))
 return {'max_ratio':float(q[j]),'max_ratio_point':np.asarray(points[j]).tolist(),'max_absolute':float(abs(R[k])),'max_absolute_point':np.asarray(points[k]).tolist(),'rms_absolute':float(np.sqrt(np.mean(R*R))),'zero_normalizers':int(np.sum(N==0)),'infinite_ratios':int(np.sum(np.isinf(q)))}


def diagnose(basis,C,D,points):
 p=np.asarray(points);q=divided_fields(basis,prepare_divided(basis,p),C,D);cart=basis.fields(basis.prepare(p),C,D)
 out={'divided_F':metrics(q['RF'],q['NF'],p),'divided_G':metrics(q['RG'],q['NG'],p),
      'Cartesian_Theta':metrics(cart['F'],cart['NF'],p),'Cartesian_Omega':metrics(cart['G'],cart['NG'],p),
      'minimum_Theta':float(cart['Theta'].min()),'maximum_absolute_Theta':float(abs(cart['Theta']).max()),'minimum_Omega':float(cart['Omega'].min()),'maximum_absolute_Omega':float(abs(cart['Omega']).max()),'max_absolute_C':float(abs(C).max()),'max_absolute_D':float(abs(D).max())}
 axis=p[:,0]==0
 if np.any(axis):out['axis']={'F':metrics(q['RF'][axis],q['NF'][axis],p[axis]),'G':metrics(q['RG'][axis],q['NG'][axis],p[axis])}
 out['Cartesian_vs_divided_absolute_difference']={'Theta':float(np.max(abs(cart['F']-p[:,0]**2*q['RF']))),'Omega':float(np.max(abs(cart['G']-p[:,0]*q['RG'])))}
 return out,{'points':p,**q,**{'Cartesian_'+k:v for k,v in cart.items()}}


def grid(radii,angles,origin=True):
 r=np.repeat(np.asarray(radii),len(angles));phi=np.tile(angles,len(radii));x=r*np.sin(phi);x[(phi==0)|(phi==np.pi)]=0.;y=-r*np.cos(phi)
 return np.vstack((np.column_stack((x,y)),[[0.,0.]])) if origin else np.column_stack((x,y))
