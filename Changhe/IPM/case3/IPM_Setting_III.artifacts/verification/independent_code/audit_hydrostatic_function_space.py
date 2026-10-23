"""Result276: independent Cartesian evaluations of saved auxiliary trial states."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,math,traceback
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from q_high_precision_density import MPQDensity
from exact_polynomial_275 import P
R=Path('research/hydrostatic_function_space_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[]
def ck(name,value,e=None):checks.append(dict(name=name,passed=bool(value),evidence=e))
def dump(path,obj):Path(path).write_text(json.dumps(obj,indent=2)+'\n')
class MPDirectLocal(MPQDensity):
 def __init__(self,q):
  super().__init__(q.coeff,q.L,q.kappa,q.cl);self.basis=q.basis;self.tk=[mp.mpf(float(t))for t in q.tk]
 def at(self,r,theta):
  sig,w=self.coords(r);t=2*sig-1 if sig<mp.mpf('.5')else 1-2*w;f=fs=ft=mp.mpf(0)
  for j,cc in enumerate(self.coeff):
   fac=2/(1-self.tk[j])if self.basis=='local'else 1;z=fac*t-(1+self.tk[j])/(1-self.tk[j])if self.basis=='local'else t
   val,der=self.clenshaw(cc,z);der*=fac;cs=mp.cos(2*j*theta);sn=mp.sin(2*j*theta);power=sig**j
   f+=power*val*cs;fs+=(j*sig**(j-1)*val+2*power*der if j else 2*der)*cs;ft-=2*j*power*val*sn
  sd=2*sig*w/(w+2*self.kappa*sig);sn=mp.sin(theta);cs=mp.cos(theta);rad=sn*(w*f+sd*(-f+w*fs));tan=w*(cs*f+sn*ft)
  return r*w*sn*f,cs*rad-sn*tan,sn*rad+cs*tan
bounds=[0,.1,1,100,1e4,1e7];labels=['inner','subunit','annulus','far','outer']
def maxrec(values,mask,x,y,numerator,denominator):
 valid=np.flatnonzero(mask&np.isfinite(values))
 if not len(valid):return None
 j=int(valid[np.argmax(values[valid])]);return dict(value=float(values[j]),index=j,x=float(x[j]),y=float(y[j]),numerator=float(numerator[j]),denominator=float(denominator[j]))
def compare(a,b,x,y,p,rr=None):
 r=np.hypot(x,y)if rr is None else rr;wf=(1+r)**p;wg=(1+r)**(p-1);dh=np.abs(a[:,0]-b[:,0]);dg=np.linalg.norm(a[:,1:3]-b[:,1:3],axis=1);gb=np.abs(b[:,0]);rat=np.divide(dh,gb,out=np.full_like(dh,np.nan),where=gb!=0);data={}
 for label,lo,hi in zip(labels,bounds,bounds[1:]):
  mask=(r>=lo)&(r<hi);data[label]=dict(count=int(mask.sum()),field=maxrec(dh/wf,mask,x,y,dh,wf),gradient=maxrec(dg/wg,mask,x,y,dg,wg),sum_norm=maxrec(dh/wf+dg/wg,mask,x,y,dh/wf+dg/wg,np.ones_like(r)),pointwise_relative=maxrec(rat,mask,x,y,dh,gb),zero_over_zero=int((mask&(gb==0)&(dh==0)).sum()),nonzero_over_zero=int((mask&(gb==0)&(dh!=0)).sum()),field_scale=float(np.max(gb[mask]/wf[mask])),gradient_scale=float(np.max(np.linalg.norm(b[mask,1:3],axis=1)/wg[mask])))
 return data
start=utc();out=dict(status='RUNNING',started_utc=start,pid=os.getpid(),states=[],pairs=[],checks=checks)
dump(V/'RUN.json',out)
try:
 inp=json.loads((V/'INPUTS.json').read_text())
 for f in inp['files']:ck('frozen '+Path(f['path']).name,sha(f['path'])==f['sha256'])
 gatepath=Path('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json');gate=json.loads(gatepath.read_text());ck('parent analytic jet manufacture gate',gate['status']=='PASS'and all(t['passed']for t in gate['checks'])and gate['evaluator_sha256']==sha('independent_code/independent_hydrostatic.py'))
 # Exact independent cubic expansion; no scalar value is substituted for a.
 a,d,e,B,y=[P.var(i,5)for i in range(5)]
 # Exact Fraction coefficients throughout.
 from fractions import Fraction as F
 exact=((1+d)*y-B*y**3*F(1,3))*(a+3*e*y*y)-(a*y+e*y**3)
 cubic=P({k:v for k,v in exact.a.items()if k[4]<=3},5);ck('C3 cubic identity exact',cubic==a*d*y+((2+3*d)*e-a*B*F(1,3))*y**3)
 radial=np.geomspace(1e-3,1e7,401);theta=np.linspace(0,np.pi/2,49);xx=(radial[:,None]*np.cos(theta)).ravel();yy=(radial[:,None]*np.sin(theta)).ravel();intended=np.repeat(radial,49)
 rr2=10**(-3+(np.arange(277)+.371)/277*10);th2=np.r_[0,(np.arange(39)+.271)/39*np.pi/2,np.pi/2];sx=(rr2[:,None]*np.cos(th2)).ravel();sy=(rr2[:,None]*np.sin(th2)).ravel();sy[::len(th2)]=0;sx[len(th2)-1::len(th2)]=0
 coords=None;arrays={};sparse={};params={}
 for item in inp['states']:
  t0=time.monotonic();tag=item['tag'];print('START',tag,utc(),flush=True)
  with np.load(item['export']['path'],allow_pickle=False)as data:ex={k:data[k].copy().ravel()for k in data.files}
  X,Y=ex['X'],ex['Y'];ck(tag+' exported length',len(X)==19649 and len(Y)==19649);ck(tag+' exported keys',{'X','Y','g','gx','gy'}.issubset(ex));ck(tag+' reconstructed radial grid',np.max(np.abs(np.hypot(X,Y)/intended-1))<2e-14);ck(tag+' reconstructed angles',np.max(np.abs(X-xx)/(1+intended))<2e-14 and np.max(np.abs(Y-yy)/(1+intended))<2e-14)
  if coords is None:coords=(X,Y)
  ck(tag+' identical common coordinates',np.array_equal(X,coords[0])and np.array_equal(Y,coords[1]))
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
  ck(tag+' positive auxiliary exponent',q.cl==item['c']and abs(q.p-1/item['c'])<5e-16);ck(tag+' exported metadata agrees coefficients',int(ex['N'][0])==q.N and int(ex['M'][0])==q.M and float(ex['c'][0])==q.cl)
  jet=CartesianQJet(q);ours=jet.jet(X,Y);sensitivity=jet.jet(sx,sy);ck(tag+' finite independent fields',np.isfinite(ours).all()and np.isfinite(sensitivity).all());p=q.p;rad=np.hypot(X,Y);errors={}
  for j,key in enumerate(['g','gx','gy']):
   scale=(1+rad)**(p if j==0 else p-1);err=np.abs(ours[:,j]-ex[key])/scale;ind=int(np.argmax(err));errors[key]=dict(max_weighted_error=float(err[ind]),x=float(X[ind]),y=float(Y[ind]));ck(tag+' producer export agreement '+key,float(err[ind])<2e-9,errors[key])
  exactzero=(Y==0);ck(tag+' exact x-axis parity',np.all(ours[exactzero,0]==0)and np.all(ours[exactzero,1]==0))
  center=jet.jet(0.,0.);ck(tag+' origin jet parity',center[0]==0 and center[1]==0 and center[2]!=0)
  np.savez_compressed(V/(tag+'_independent.npz'),X=X,Y=Y,jet=ours);arrays[tag]=ours;sparse[tag]=sensitivity;params[tag]=p
  probes=[(.037,.021),(.73,1.17),(0.,36.7),(1234.,3456.),(0.,1e7)]
  mp_rows=[]
  for px,py in probes:
   value=jet.jet(px,py)[:3];values=[]
   for digits in [70,100]:
    with mp.workdps(digits):
     m=MPDirectLocal(q);radmp=mp.sqrt(mp.mpf(px)**2+mp.mpf(py)**2);ang=mp.atan2(mp.mpf(py),mp.mpf(px));res=m.at(radmp,ang);values.append([mp.nstr(v,65)for v in res])
   scales=[(1+math.hypot(px,py))**p]+[(1+math.hypot(px,py))**(p-1)]*2
   err=max(abs(value[j]-float(values[-1][j]))/scales[j]for j in range(3));precision=max(abs(float(values[0][j])-float(values[1][j]))/scales[j]for j in range(3));ck(tag+' MP Cartesian comparison '+str((px,py)),err<2e-9,err);ck(tag+' 70vs100digits '+str((px,py)),precision<1e-35,precision);mp_rows.append(dict(x=px,y=py,weighted_error=err,values=values))
  row=dict(tag=tag,source_sha256=item['state']['sha256'],export_sha256=item['export']['sha256'],metadata=q.meta,center_slope=float(center[2]),producer_comparison=errors,mp_probes=mp_rows,wall_seconds=time.monotonic()-t0);out['states'].append(row);dump(V/'RUN.json',out);print('DONE',tag,row['wall_seconds'],flush=True)
 for c in [2,3]:
  tags=[r['tag']for r in inp['states']if r['c']==c]
  for old,new in zip(tags,tags[1:]):
   direct=compare(arrays[old],arrays[new],*coords,params[new]);nominal=compare(arrays[old],arrays[new],*coords,params[new],rr=intended);other=compare(sparse[old],sparse[new],sx,sy,params[new]);ck(old+'->'+new+' relativezero handling',all(t['nonzero_over_zero']==0 for t in direct.values()))
   mask=np.hypot(*coords)>=1e7;out['pairs'].append(dict(c=c,old=old,new=new,from_export_coordinates=direct,from_intended_radius_masks=nominal,independent_grid=other,outer_boundary_count=int(mask.sum())))
 out.update(status='PASS'if all(c['passed']for c in checks)else'FAIL',finished_utc=utc(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),input_sha256=sha(V/'INPUTS.json'),driver_sha256=sha(__file__),code_sha256={f:sha(Path('independent_code')/f)for f in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','q_high_precision_density.py','exact_polynomial_275.py']},scope='Independent sampled trial-function differences; no Cauchy, convergence, solution or regularity theorem.')
 dump(V/'CHECKS.json',out);dump(V/'RUN.json',out);print(out['status'],out['count']);print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
except Exception:
 out.update(status='ERROR',finished_utc=utc(),traceback=traceback.format_exc());dump(V/'RUN.json',out);raise
