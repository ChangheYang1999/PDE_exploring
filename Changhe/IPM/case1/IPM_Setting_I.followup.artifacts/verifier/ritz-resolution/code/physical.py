from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import isqrt
import copy,json,time,sys,hashlib
import numpy as np
import torch
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
from gpu import GPUField
from split_kernel import SplitKernel,radial_rule,outer_weight
from linearized import direction_coefficients,LinearDensity,MultiLinearGPU

torch.set_num_threads(1)
class MultiSplit(SplitKernel):
 @torch.no_grad()
 def velocity(self,point):
  x,y=map(float,point);X2=x*x+y*y;a=np.sqrt(1+X2/64);tx=x/self.rad[:,None];ty=y/self.rad[:,None];ex,ey=self.cx,self.sy
  ax=1+tx*tx+ty*ty;b=2*(tx*ex+ty*ey);dm=(tx-ex)**2+(ty-ey)**2;dp=(tx+ex)**2+(ty+ey)**2
  wm=outer_weight(self.rad[:,None]*torch.sqrt(dm)/a);wp=outer_weight(self.rad[:,None]*torch.sqrt(dp)/a)
  denm=torch.clamp(dm*dm,min=1e-100);denp=torch.clamp(dp*dp,min=1e-100)
  d1=-(tx-ex)*(ty-ey)*wm/denm+(tx+ex)*(ty+ey)*wp/denp
  d2=.5*(((tx-ex)**2-(ty-ey)**2)*wm/denm-((tx+ex)**2-(ty+ey)**2)*wp/denp)
  far=self.rad[:,None]>max(2*np.sqrt(X2)+4*a,1.);den=torch.clamp((ax*ax-b*b)**2,min=1e-100)
  m1=tx*ty+ex*ey;n1=tx*ey+ty*ex;m2=.5*(tx*tx-ty*ty+ex*ex-ey*ey);n2=tx*ex-ty*ey
  d1=torch.where(far,(-4*m1*ax*b+2*n1*(ax*ax+b*b))/den,d1)
  d2=torch.where(far,(4*m2*ax*b-2*n2*(ax*ax+b*b))/den,d2)
  grows=torch.einsum('rak,rai->rki',self.rh,torch.stack([d1,d2],dim=-1))*self.rw[:,None,None]/self.nang
  ed,rr,rw=radial_rule(self.rmin,2*a,self.order,self.panel);dx=rr[:,None]*ex;dy=rr[:,None]*ey;f0=self.f(x,y)
  loc=.5*(self.f(x+dx,y+dy)+self.f(x-dx,y-dy))-f0
  lrows=torch.einsum('rak,ia->rki',loc,self.kk)*(1-outer_weight(rr/a))[:,None,None]*rw[:,None,None]
  return (grows.sum(0)+lrows.sum(0)+torch.stack([torch.zeros_like(f0),-.5*f0],dim=-1)).cpu().numpy()

def tail_constants(d,V):
 H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
 ceil=lambda v:(v.numerator+v.denominator-1)//v.denominator
 B=ceil(max(abs(F(float(v))) for v in d.b.ravel()));eps=F(1,5)-1/F(d.cl);assert eps>0 and d.L==8
 out=[]
 for j in range(V.shape[1]):
  Bd=ceil(max(abs(F(float(v))) for v in V[:-2,j]));dc=abs(F(float(V[-2,j])));C=512*H*(Bd+dc/(2*F(d.cl)**2)*B*(1+2*d.N*d.N)*(1+2/eps));out.append(C)
 return 512*H*B,out

pts=[[5.403023058681398,8.414709848078965],[.20794827803092428,9.99783764189357],[8.6,.1],[8.6,1.]]
path=root/'verification/physical.json';out={'date_start':datetime.now(timezone.utc).isoformat(),'method':'Own physical derivative, own split real-space inverse, Cartesian finite differences; finite data, not a spectral certificate','points':pts,'states':[]}
for tag,state in [('n96m40S','dnB_n96m40S.npz'),('n120m48_S','dnSB_n120m48.npz')]:
 d=NodalDensity(root/'data'/state);dp=root/'data'/('directions_'+tag+'.npz');z=np.load(dp);V=z['V'];co=direction_coefficients(d,V);cpu=[LinearDensity(d,co[:,:,j],V[-2,j]) for j in range(V.shape[1])]
 baseC,deltaC=tail_constants(d,V);bound=lambda C:C*F(5,2)*10/F(10**24)/(1-F(1,10**29)**2)**2
 row={'tag':tag,'state_md5':d.md5,'direction_sha256':hashlib.sha256(dp.read_bytes()).hexdigest(),'labels':z['labels'].tolist(),'node_norms':np.linalg.norm(V,axis=0).tolist(),'dcl':V[-2].tolist(),'dC':V[-1].tolist(),'tail_base_C':str(baseC),'tail_delta_C':[str(c) for c in deltaC],'tail_max_observer':10,'tail_radius':'1e30','base_U_tail_bound':float(bound(baseC)),'delta_U_tail_bounds':[float(bound(c)) for c in deltaC],'evaluations':[],'parameter_checks':[]};out['states'].append(row)
 gpu=MultiLinearGPU(d,co,V[-2]);row['cpu_gpu_density_max_error']=max(float(abs(gpu(*pt).cpu().numpy()-np.array([f(*pt) for f in cpu])).max()) for pt in pts)
 for n,order,panel in [(2048,24,.1),(4096,28,.08)]:
  begin=time.monotonic();ker=MultiSplit(gpu,n,order,panel,rmax=1e30);bk=SplitKernel(GPUField(d),n,order,panel,rmax=1e30)
  for pt in pts:
   u=bk.velocity(pt);du=ker.velocity(pt);g=gradient_fd(d,*pt,relative_step=.0005);g2=gradient_fd(d,*pt,relative_step=.001);rho=float(d(*pt));W=d.cl*np.array(pt)+u
   dr=np.array([float(f(*pt)) for f in cpu]);dg=np.array([gradient_fd(f,*pt,relative_step=.0005) for f in cpu]);dg2=np.array([gradient_fd(f,*pt,relative_step=.001) for f in cpu])
   act=V[-2]*(np.array(pt)@g)+dg@W+du@g-dr;act2=V[-2]*(np.array(pt)@g2)+dg2@W+du@g2-dr;den=abs(rho)+np.sum(abs(W*g))
   err=np.array([float(bound(c))*np.sum(abs(g)) for c in deltaC])+float(bound(baseC))*np.sum(abs(dg),axis=1)
   item={'nang':n,'order':order,'panel':panel,'point':pt,'base_U':u.tolist(),'base_R':float(W@g-rho),'N_report_f':float(den),'delta_U':du.tolist(),'delta_R':act.tolist(),'delta_R_over_fixed_N_report_f':(act/den).tolist(),'spatial_step_change_fixed_units':(abs(act-act2)/den).tolist(),'omitted_delta_R_bound_fixed_units':(err/den).tolist(),'cumulative_seconds':time.monotonic()-begin};row['evaluations'].append(item)
   path.write_text(json.dumps(out,indent=2)+'\n');print(tag,n,pt,item['delta_R_over_fixed_N_report_f'],flush=True)
  del ker,bk;torch.cuda.empty_cache()
 pt=pts[1];ref=next(x for x in row['evaluations'] if x['nang']==4096 and x['point']==pt)
 for j in [0,4]:
  for h in [.003,.001]:
   vals=[]
   for sign in [-1,1]:
    f=copy.copy(d);f.cl=d.cl+sign*h*V[-2,j];f.k=1/f.cl;f.co=d.co+sign*h*co[:,:,j]
    bk=SplitKernel(GPUField(f),4096,28,.08,rmax=1e30);u=bk.velocity(pt);g=gradient_fd(f,*pt,relative_step=.0005);rho=float(f(*pt));R=float((f.cl*np.array(pt)+u)@g-rho);vals.append((u,R));del bk;torch.cuda.empty_cache()
   dv=(vals[1][0]-vals[0][0])/(2*h);dR=(vals[1][1]-vals[0][1])/(2*h)
   item={'direction':j,'h':h,'point':pt,'U_finite_difference':dv.tolist(),'U_difference_from_linear':(dv-ref['delta_U'][j]).tolist(),'R_finite_difference':dR,'R_difference_from_linear_in_fixed_units':float((dR-ref['delta_R'][j])/ref['N_report_f'])};row['parameter_checks'].append(item);path.write_text(json.dumps(out,indent=2)+'\n');print(tag,'parameter',item,flush=True)
 del gpu;torch.cuda.empty_cache()
out['date_end']=datetime.now(timezone.utc).isoformat();path.write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['date_end'],flush=True)
