"""Direct paired full-plane inversion of base and fitted fields on withheld points."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import ceil,isqrt,sqrt
import sys,json,time,hashlib,gc
import numpy as np
from numpy.polynomial.chebyshev import chebval2d,chebder
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'));sys.path.insert(0,str(ROOT.parent/'ritz-resolution/code'));sys.path.insert(0,str(ROOT.parent/'sampled-physical-actions/code'))
from collocation import NodalDensity
from density import gradient_fd
from linearized import MultiLinearGPU
from blocked_kernel import BlockedMultiSplit
pbytes=(ROOT/'verification/withheld_points.json').read_bytes();ps=json.loads(pbytes);points=ps['points'];fits=json.loads((ROOT/'verification/fits.json').read_text());assert fits['complete']
fitpoints=json.loads((ROOT.parent/'sampled-physical-actions/verification/points.json').read_text())['points'];check_indices=[11,34,35,50];allpoints=[fitpoints[i] for i in check_indices]+points
path=ROOT/'verification/withheld.json';config={'nang':4096,'order':28,'panel':.08,'rmax':'1e30','Cartesian_steps':[1/16000,1/32000]}
if path.exists():out=json.loads(path.read_text());assert out['config']==config and out['points_sha256']==hashlib.sha256(pbytes).hexdigest()
else:out={'date_start':datetime.now(timezone.utc).isoformat(),'config':config,'points_sha256':hashlib.sha256(pbytes).hexdigest(),'states':[],'scope':'Direct physical checks at4fitpoints and84withheldpoints. Finite samples only. Tail bounds separate from interior quadrature.'}
def save():
 tmp=path.with_suffix('.temporary');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(path)
def analytic(d,pts):
 x,y=np.array(pts).T;r2=x*x+y*y;D=d.L**2+r2;ell=np.log1p(r2/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell);s=d.map_inverse(np.arctan2(y,x));c=np.cos(2*s)
 b=chebval2d(2*q-1,c,d.co);bq=chebval2d(2*q-1,c,2*chebder(d.co,axis=0));bc=chebval2d(2*q-1,c,chebder(d.co,axis=1));dc=-2*np.sin(2*s)/(1+d.beta*np.cos(2*s));pref=x*x*y*np.exp((d.k-3)*ell/2)
 return np.stack([pref*((2/x+(d.k-3)*x/D)*b+bq*(1-d.k)*(1-q)*x/D-bc*dc*y/r2),pref*((1/y+(d.k-3)*y/D)*b+bq*(1-d.k)*(1-q)*y/D+bc*dc*x/r2)],axis=1)
for fs in fits['states']:
 tag=fs['tag'];basefile='dnB_n96m40S.npz' if tag=='n96m40S' else 'dnSB_n120m48.npz';ds=[NodalDensity(ROOT/'data'/basefile),NodalDensity(ROOT/'data'/fs['selected'])];d=ds[0];assert d.cl==ds[1].cl and d.C==ds[1].C
 old=next((s for s in out['states'] if s['tag']==tag),None)
 if old:st=old;assert st['md5s']==[z.md5 for z in ds]
 else:st={'tag':tag,'md5s':[z.md5 for z in ds],'files':[basefile,fs['selected']],'rows':[]};out['states'].append(st);save()
 if len(st['rows'])==len(allpoints):continue
 ag=np.array([analytic(z,allpoints) for z in ds]);tailC=[]
 for z in ds:
  H=isqrt(2*z.N*(2*z.M-1));H+=H*H<2*z.N*(2*z.M-1);tailC.append(int(z.L)**3*H*ceil(float(np.max(abs(z.b)))))
 st['tail_C']=tailC
 f=MultiLinearGPU(d,np.stack([z.co for z in ds],axis=2),np.zeros(2));print('BUILD',tag,datetime.now(timezone.utc).isoformat(),flush=True);ker=BlockedMultiSplit(f,4096,28,.08,rmax=1e30);begin=time.monotonic();print('READY',tag,flush=True)
 stored=np.load(ROOT/'verification'/(tag+'_fit_arrays.npz'))
 for i,pt in enumerate(allpoints):
  if i<len(st['rows']):assert st['rows'][i]['point']==pt;continue
  U=ker.velocity(pt);obs=ceil(sqrt(sum(x*x for x in pt)))
  while sum(F(x)**2 for x in pt)>obs*obs:obs+=1
  row={'point':pt,'set':'fit' if i<4 else 'withheld','index':check_indices[i] if i<4 else i-4,'fields':[]}
  for k,z in enumerate(ds):
   rho=float(z(*pt));gs=[gradient_fd(z,*pt,relative_step=h) for h in config['Cartesian_steps']];g=gs[-1];W=z.cl*np.array(pt)+U[k];R=float(W@g-rho);nf=float(abs(rho)+sum(abs(W*g)));nv=float(abs(rho)+abs(np.array(pt)@g)+abs(U[k]@g));tail=F(5*tailC[k]*obs,2*10**24)/(1-F(obs,10**30)**2)**2
   rr={'rho':rho,'U':U[k].tolist(),'gradient':g.tolist(),'R':R,'Nf':nf,'Nv':nv,'absR_Nf':abs(R)/nf,'absR_Nv':abs(R)/nv,'Cartesian_step_R_change_fixedNf':float(W@(gs[0]-g)/nf),'analytic_gradient_R_change_fixedNf':float(W@(ag[k,i]-g)/nf),'exact_tail_U':str(tail),'tail_R_using_numerical_gradient':float(tail)*sum(abs(g))/nf}
   if i<4 and k==1:
    j=check_indices[i];du=U[k]-stored['selected_U'][j];rr['direct_vs_quadratic_U']=du.tolist();rr['direct_vs_quadratic_R_fixed_base_Nf']=float((R-stored['selected_R'][j])/stored['denominator'][j])
   row['fields'].append(rr)
  st['rows'].append(row);save();print(tag,i+1,'/88',row['set'],[x['absR_Nf'] for x in row['fields']],'seconds',time.monotonic()-begin,flush=True)
 del ker,f,stored;gc.collect();torch.cuda.empty_cache();st['date_end']=datetime.now(timezone.utc).isoformat();save()
out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['date_end'],flush=True)
