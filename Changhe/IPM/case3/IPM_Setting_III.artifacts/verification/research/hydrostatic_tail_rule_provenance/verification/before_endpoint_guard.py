"""Independent selected tail-rule comparison; no producer code is executed."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from functools import lru_cache
import os,sys,json,hashlib,math,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import numpy as np
from scipy.special import roots_legendre
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';checks=[];bindings={}
now=lambda:datetime.now(timezone.utc).isoformat()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);hh=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),(h is None or hh==h)and(str(p)not in bindings or hh==bindings[str(p)]));bindings[str(p)]=hh;return p
@lru_cache(None)
def rule(n):
 if type(n)is not int or n<1:raise ValueError('positive integer order')
 z,w=roots_legendre(n);u=(z+1)/2;ww=w/2
 if not(np.all(np.diff(u)>0)and np.all((u>0)&(u<1))and np.all(ww>0)and abs(sum(map(float,ww))-1)<4e-14):raise ValueError('positive ordered Gauss rule')
 return u,ww

def nodes(y,q,n):
 if not math.isfinite(y)or y<0 or q not in(2,3):raise ValueError('tail domain/q')
 u,w=rule(n);r=u/(1-u);t=y+(1+y)*r**q;wt=w*(1+y)*q*u**(q-1)/(1-u)**(q+1)
 if not(np.isfinite(t).all()and np.isfinite(wt).all()and np.all(t>y)and np.all(wt>0)):raise ValueError('finite positive tail nodes')
 return t,wt

def tail(jet,x,y,q,n):
 t,w=nodes(y,q,n);j=np.asarray(jet(np.full(len(t),x),t))
 if j.shape!=(len(t),4)or not np.isfinite(j).all():raise ValueError('finite derivative jet')
 return [math.fsum(float(a)*float(b)for a,b in zip(w,j[:,k]))for k in [1,3]]

def delta(a,b,y,gx,gy):
 ax,axx,bx,bxx,yy,dx,dy=map(lambda z:Q(float(z)),[*a,*b,y,gx,gy]);v1=-(ax-bx);v2=yy*(axx-bxx);r=v1*dx+v2*dy
 return dict(deltaV1=float(v1),deltaV2=float(v2),deltaR=float(r),exact={k:str(v)for k,v in [('deltaV1',v1),('deltaV2',v2),('deltaR',r)]})

def rejects(n,fn):
 try:fn()
 except(ValueError,AssertionError):ck(n,True)
 else:raise AssertionError('manufacture did not reject '+n)

def manufacture():
 out=[]
 def gauss(x,t):
  a=np.exp(-x*x-t*t);return np.stack([t*a,-2*x*t*a,(1-2*t*t)*a,(4*x*x-2)*t*a],1)
 for x,y in [(.25,.1),(1.,.7),(.4,2.)]:
  truth=[-x*math.exp(-x*x-y*y),(2*x*x-1)*math.exp(-x*x-y*y)]
  for q in [2,3]:
   val=tail(gauss,x,y,q,400);error=max(abs(a-b)for a,b in zip(val,truth));ck('Gaussian exact tail '+str((x,y,q)),error<2e-12,error)
 for y in [.1,.7,4.]:
  true=2/math.sqrt(1+y)
  for q in [2,3]:
   vals=[]
   for n in [200,400,800,1600]:
    t,w=nodes(y,q,n);val=math.fsum(float(a)*float(b)for a,b in zip(w,(1+t)**-1.5));vals.append(dict(n=n,value=val,error=abs(val-true)))
   ck('algebraic endpoint exact '+str((y,q)),vals[-1]['error']<5e-8,vals)
   if q==3:ck('algebraic finite refinement '+str(y),vals[-1]['error']<vals[0]['error'],vals)
   out.append(dict(y=y,q=q,exact_formula_value=true,values=vals))
 for name,args in [('negative y',(-1,2,4)),('infinite y',(math.inf,2,4)),('q unsupported',(1,4,4)),('zero order',(1,2,0)),('boolean order',(1,2,True))]:rejects(name,lambda args=args:nodes(*args))
 ck('Gauss weights',abs(math.fsum(rule(40)[1])-1)<2e-15)
 a=delta([1,2],[3,5],2,7,11);ck('finite exact difference identity',a['exact']==dict(deltaV1='2',deltaV2='-6',deltaR='-52'))
 a=delta([1,2],[3,5],2,3,1);ck('finite difference cancellation',a['exact']['deltaR']=='0')
 for p in [__file__,R/'PROOF.md','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 return dict(status='PASS_TAIL_RULE_MANUFACTURES',utc=now(),count=len(checks),checks=checks,bindings=bindings,algebraic_tail=out,scope='Manufactured finite sums only; no convergence rate asserted.')

def run():
 # Enforce the standing one-heavy-process rule without signalling any other job.
 previous=Path('research/hydrostatic_larger_node_audit/verification')
 for p in [previous/'JOB.json',previous/'MP_JOB.json',Path('research/accurate_map_final_audit/verification/JOB.json')]:
  if not p.exists():continue
  job=json.loads(p.read_text());proc=Path('/proc')/str(job['pid'])
  if proc.exists():
   st=(proc/'stat').read_text().rsplit(') ',1)[1].split()[0];cmd=(proc/'cmdline').read_bytes();ck('other heavy ceased '+str(p),st=='Z'or not any(z in cmd for z in [b'run_larger_node_audit.py',b'launch_larger_node_mp.py',b'run_larger_node_mp.py',b'launch_accurate_map_audit.py',b'run_accurate_map_audit.py']))
 da=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());ck('accepted finite design',da['status']=='ACCEPTED_FINITE_SELECTED_TAIL_DIAGNOSTIC')
 for p,h in da['bindings'].items():bind(p,h)
 mf=json.loads(bind(V/'MANUFACTURES.json').read_text());ck('manufactured PASS',mf['status']=='PASS_TAIL_RULE_MANUFACTURES'and mf['count']==len(mf['checks'])and all(z['passed']for z in mf['checks']))
 for p,h in mf['bindings'].items():bind(p,h)
 base=Path('research/new_node_export_record_audit/verification');final=json.loads(bind(base/'FINAL_BINDINGS.json').read_text());ck('323 accepted',final['status']=='CONFIRMED_FINITE_NEW_NODE_EXPORT_RECORD_AUDIT')
 cfg=json.loads(bind(base/'EXPORT_INPUTS.json',final['bindings'][str(base/'EXPORT_INPUTS.json')]).read_text());out323=json.loads(bind(base/'CHECKS.json',final['bindings'][str(base/'CHECKS.json')]).read_text());cfg=cfg['states'][0];data=out323['states'][0];ck('S160 source',cfg['tag']==data['tag']=='S160'and cfg['N']==160 and cfg['M']==40)
 import torch
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(bind(cfg['state'],cfg['state_sha256']))
 jet=CartesianQJet(q).jet
 with np.load(bind(cfg['export'],cfg['export_sha256']),allow_pickle=False)as z:arrays={k:z[k]for k in z.files}
 ids=data['selected_jet_indices'];rows=[]
 for i in ids:
  x,y=map(float,[arrays['x'][i],arrays['y'][i]]);j=jet(np.array([x]),np.array([y]))[0];rules=[]
  for n in [200,400,800,1600]:
   t2=tail(jet,x,y,2,n);t3=tail(jet,x,y,3,n);dd=delta(t2,t3,y,j[1],j[2]);dd['deltaR_over_export_Nf']=abs(dd['deltaR'])/float(arrays['N_f'][i]);rules.append(dict(n=n,q2=t2,q3=t3,delta_q2_minus_q3=dd))
  rows.append(dict(index=i,x=x,y=y,jet=j.tolist(),export_Rh=float(arrays['R_h'][i]),export_Nf=float(arrays['N_f'][i]),rules=rules));print('selected tail',i,'of',len(ids),now(),flush=True)
 ck('complete selected indices',[z['index']for z in rows]==ids);ck('all finite tail outputs',all(math.isfinite(a)for z in rows for s in z['rules']for a in s['q2']+s['q3']))
 for p,h in list(bindings.items()):bind(p,h)
 return dict(status='PASS_FINITE_SELECTED_TAIL_RULES_REQUIRES_FINAL_REVIEW',utc=now(),count=len(checks),checks=checks,bindings=bindings,rows=rows,scope='Selected finite analytic-derivative tails; does not reproduce historical finite-difference runs. No all-node maxima, error enclosure, causality proof or primary endpoint.')
if __name__=='__main__':
 try:
  if sys.argv[1:]==['--manufactures']:d=manufacture();name='MANUFACTURES.json'
  elif sys.argv[1:]==[]:d=run();name='CHECKS.json'
  else:raise ValueError('unsupported argument')
  (V/name).write_text(json.dumps(d,indent=2)+'\n');print(d['status'],d['count'])
 except Exception:
  (V/('FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
