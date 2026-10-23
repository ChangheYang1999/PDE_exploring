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
 p=Path(p).resolve();p.relative_to(Path.cwd().resolve());hh=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),(h is None or hh==h)and(str(p)not in bindings or hh==bindings[str(p)]));bindings[str(p)]=hh;return p
@lru_cache(None)
def rule(n):
 if type(n)is not int or n<1:raise ValueError('positive integer order')
 z,w=roots_legendre(n);u=(z+1)/2;ww=w/2
 if not(np.all(np.diff(u)>0)and np.all((u>0)&(u<1))and np.all(ww>0)and abs(sum(map(float,ww))-1)<4e-14):raise ValueError('positive ordered Gauss rule')
 return u,ww

def nodes(y,q,n):
 if not math.isfinite(y)or y<0 or q not in(2,3):raise ValueError('tail domain/q')
 u,w=rule(n);r=u/(1-u);inc=(1+y)*r**q;t=y+inc;wt=w*(1+y)*q*u**(q-1)/(1-u)**(q+1)
 if not(np.isfinite(t).all()and np.isfinite(wt).all()and np.all(inc>0)and np.isfinite(inc).all()and np.all(t>=y)and np.all(wt>0)):raise ValueError('finite positive tail nodes')
 return t,wt

def tail(jet,x,y,q,n):
 t,w=nodes(y,q,n);j=np.asarray(jet(np.full(len(t),x),t))
 if j.shape!=(len(t),4)or not np.isfinite(j).all():raise ValueError('finite derivative jet')
 out=sum_records([[float(a)*float(b)for a,b in zip(w,j[:,k])]for k in [1,3]]);out['endpoint_coincident_count']=int(np.sum(t==y));return out

def sum_records(columns):
 values=[];absolute=[]
 for col in columns:
  if not all(math.isfinite(z)for z in col):raise ValueError('finite tail products')
  values.append(math.fsum(col));absolute.append(math.fsum(abs(z)for z in col))
 if not all(math.isfinite(z)for z in values+absolute):raise ValueError('finite tail sums')
 return dict(value=values,absolute_sum=absolute)

def conditioning(a,b):
 ans=[]
 for k in range(2):
  d=abs(Q(a['value'][k])-Q(b['value'][k]));scale=(Q(a['absolute_sum'][k])+Q(b['absolute_sum'][k]))*Q(2)**-52
  if scale==0:
   if d:raise ValueError('nonzero difference with zero absolute sums')
   ans.append(dict(ratio=None,status='UNDEFINED_ZERO_SUM',exact_difference=str(d),exact_scale=str(scale)))
  else:ans.append(dict(ratio=float(d/scale),status='FINITE_CONDITIONING_SCALE_ONLY',exact_difference=str(d),exact_scale=str(scale)))
 return ans

def selected_domain(i,arrays):
 cols=[np.asarray(arrays[k])for k in ['x','y','N_f','R_h']]
 if not(all(z.ndim==1 for z in cols)and len({len(z)for z in cols})==1):raise ValueError('equal one-dimensional selected arrays')
 if type(i)is not int or i<0 or i>=len(arrays['x']):raise ValueError('selected index')
 x,y,nf=map(float,[arrays['x'][i],arrays['y'][i],arrays['N_f'][i]])
 if not(math.isfinite(x)and math.isfinite(y)and y>=0):raise ValueError('selected physical domain')
 if not math.isfinite(float(arrays['R_h'][i])):raise ValueError('finite recorded residual')
 if not(math.isfinite(nf)and nf>0):raise ValueError('selected positive finite denominator')
 return x,y,nf,dict(x_zero=x==0.,y_zero=y==0.)

def state_domain(q):
 if (q.N,q.M,q.cl,q.L,q.kappa,q.p)!=(160,40,2.,1.,2.,.5):raise ValueError('S160 fixed state parameters')

def empirical_spread(records,key):
 return [dict(value=float(max(Q(z[key]['value'][k])for z in records)-min(Q(z[key]['value'][k])for z in records)),exact=str(max(Q(z[key]['value'][k])for z in records)-min(Q(z[key]['value'][k])for z in records)))for k in range(2)]

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
   val=tail(gauss,x,y,q,400);error=max(abs(a-b)for a,b in zip(val['value'],truth));ck('Gaussian exact tail '+str((x,y,q)),error<2e-12,error)
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
 tt,ww=nodes(4.,3,1600);ck('positive increments may round to endpoint',int(np.sum(tt==4.))>0,int(np.sum(tt==4.)))
 ck('Gauss weights',abs(math.fsum(rule(40)[1])-1)<2e-15)
 a=delta([1,2],[3,5],2,7,11);ck('finite exact difference identity',a['exact']==dict(deltaV1='2',deltaV2='-6',deltaR='-52'))
 a=delta([1,2],[3,5],2,3,1);ck('finite difference cancellation',a['exact']['deltaR']=='0')
 a=sum_records([[1.,-1.,2.],[-4.,4.,0.]]);ck('signed absolute summation',a==dict(value=[2.,0.],absolute_sum=[4.,8.]))
 z=sum_records([[0.,0.],[0.]]);ck('zero conditioning undefined',all(v['status']=='UNDEFINED_ZERO_SUM'and v['ratio']is None for v in conditioning(z,z)))
 ck('exact cancellation nonzero scale',all(v['ratio']==0 for v in conditioning(a,a)))
 b=sum_records([[1.],[1.]]);c=sum_records([[2.],[2.]])
 ck('positive conditioning rational',all(v['ratio']==float(Q(2)**52/3)for v in conditioning(b,c)))
 rejects('nonfinite product',lambda:sum_records([[math.inf],[1.]]))
 rejects('inconsistent zero scale',lambda:conditioning(dict(value=[1.,0.],absolute_sum=[0.,0.]),z))
 rr=[dict(q2=b),dict(q2=c)];ck('empirical spread exact',[z['exact']for z in empirical_spread(rr,'q2')]==['1','1'])
 aa=dict(x=np.array([0.,1.]),y=np.array([0.,2.]),N_f=np.array([1.,1.]),R_h=np.array([0.,0.]))
 ck('axis flags',selected_domain(0,aa)[3]==dict(x_zero=True,y_zero=True))
 for i in [-1,2,True,1.5]:rejects('bad selected index '+str(i),lambda i=i:selected_domain(i,aa))
 for k,vals in [('x',[math.nan,math.inf]),('y',[-1.,math.nan,math.inf]),('N_f',[0.,-1.,math.inf,math.nan]),('R_h',[math.inf,math.nan])]:
  for v in vals:
   bb={kk:vv.copy()for kk,vv in aa.items()};bb[k][0]=v;rejects('bad domain '+str((k,v)),lambda bb=bb:selected_domain(0,bb))
 for k in aa:
  bb={kk:vv.copy()for kk,vv in aa.items()};bb[k]=bb[k][:1];rejects('unequal selected lengths '+k,lambda bb=bb:selected_domain(0,bb))
  bb={kk:vv.copy()for kk,vv in aa.items()};bb[k]=bb[k].reshape(1,2);rejects('selected dimension '+k,lambda bb=bb:selected_domain(0,bb))
 ct=tail(gauss,.25,4.,3,1600);ck('tail endpoint count retained',ct['endpoint_coincident_count']==2)
 from types import SimpleNamespace
 pars=dict(N=160,M=40,cl=2.,L=1.,kappa=2.,p=.5);state_domain(SimpleNamespace(**pars));ck('fixed state parameters',True)
 for k in pars:
  bb=pars.copy();bb[k]+=1;rejects('state parameter '+k,lambda bb=bb:state_domain(SimpleNamespace(**bb)))
 for p in [__file__,R/'PROOF.md',R/'ENDPOINT_ROUNDING_PROOF.md',R/'REVIEW_REPAIR_PROOF.md',R/'DESIGN_CLOSURE_PROOF.md','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 return dict(status='PASS_TAIL_RULE_MANUFACTURES',utc=now(),count=len(checks),checks=checks,bindings=bindings,algebraic_tail=out,scope='Manufactured finite sums only; no convergence rate asserted.')

def run():
 # Enforce the standing one-heavy-process rule without signalling any other job.
 previous=Path('research/hydrostatic_larger_node_audit/verification')
 for p in [previous/'JOB.json',previous/'MP_JOB.json',Path('research/accurate_map_final_audit/verification/JOB.json')]:
  ck('required preceding job record '+str(p),p.is_file())
  job=json.loads(p.read_text());proc=Path('/proc')/str(job['pid'])
  if proc.exists():
   st=(proc/'stat').read_text().rsplit(') ',1)[1].split()[0];cmd=(proc/'cmdline').read_bytes();ck('other heavy ceased '+str(p),st=='Z'or not any(z in cmd for z in [b'run_larger_node_audit.py',b'launch_larger_node_mp.py',b'run_larger_node_mp.py',b'launch_accurate_map_audit.py',b'run_accurate_map_audit.py']))
 for p,status in [(previous/'candidate/COMPLETE.json','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW'),(previous/'mp/COMPLETE.json','COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT'),(Path('research/accurate_map_final_audit/verification/candidate/COMPLETE.json'),'COMPLETE_FINITE_ACCURATE_MAP_REQUIRES_FINAL_AUDIT')]:
  d=json.loads(p.read_text());ck('required previous completion '+str(p),d['status']==status)
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
 state_domain(q);ck('fixed candidate state domain',True,q.meta)
 jet=CartesianQJet(q).jet
 with np.load(bind(cfg['export'],cfg['export_sha256']),allow_pickle=False)as z:arrays={k:z[k]for k in z.files}
 ids=data['selected_jet_indices'];rows=[]
 for i in ids:
  x,y,nf,axis=selected_domain(i,arrays);j=jet(np.array([x]),np.array([y]))[0];rules=[]
  for n in [200,400,800,1600]:
   t2=tail(jet,x,y,2,n);t3=tail(jet,x,y,3,n);dd=delta(t2['value'],t3['value'],y,j[1],j[2]);dd['deltaR_over_export_Nf']=float(abs(Q(dd['exact']['deltaR']))/Q(nf));rules.append(dict(n=n,q2=t2,q3=t3,conditioning=conditioning(t2,t3),delta_q2_minus_q3=dd))
  rows.append(dict(index=i,x=x,y=y,axis=axis,jet=j.tolist(),export_Rh=float(arrays['R_h'][i]),export_Nf=nf,q2_empirical_spread=empirical_spread(rules,'q2'),rules=rules));print('selected tail',i,'of',len(ids),now(),flush=True)
 ck('complete selected indices',[z['index']for z in rows]==ids);ck('all finite tail outputs',all(math.isfinite(a)for z in rows for s in z['rules']for a in s['q2']['value']+s['q3']['value']))
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
