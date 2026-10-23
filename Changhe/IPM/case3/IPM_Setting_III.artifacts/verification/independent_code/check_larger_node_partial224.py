"""Direct Fraction check of completed224 arithmetic, not final318 acceptance."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,math
import numpy as np
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';C=V/'candidate';checks=[];bindings={}
def load(name):
 p=C/name;bindings[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
 if p.suffix=='.json':return json.loads(p.read_text())
 with np.load(p,allow_pickle=False)as z:return {k:z[k].copy()for k in z}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def fields(xy,j,u):
 x,y=map(Q,map(float,xy));g,gx,gy=map(Q,map(float,j[:3]));v,w=map(Q,map(float,u));e=x*gx+y*gy;a=v*gx+w*gy;r=2*e+a-g;nf=abs(2*x*gx+v*gx)+abs(2*y*gy+w*gy)+abs(g);nv=abs(g)+abs(e)+abs(a)
 return r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None
T=load('N224_targets.npz');B=load('N224_B.npz');A=load('N224_A.npz');CC=load('N224_C.npz');report=load('N224_COMPLETE.json');ck('12544 all nodes',len(B['indices'])==12544 and np.array_equal(B['indices'],np.arange(12544)));ck('unchanged targets',np.array_equal(T['xy'],B['xy'])and np.array_equal(T['jets'],B['jets']))
for lab,z in [('A',A),('B',B),('C',CC)]:
 bad=[]
 for row,i in enumerate(z['indices']):
  exact=fields(T['xy'][i],T['jets'][i],z['velocity'][row]);rounded=[float(t)if t is not None else math.nan for t in exact]
  if not np.array_equal(rounded,z['residual'][row],equal_nan=True):bad.append(int(i))
 ck('distributed exact arithmetic '+lab,not bad,dict(rows=len(z['indices']),mismatches=bad))
r=np.hypot(T['xy'][:,0],T['xy'][:,1]);bounds=[0,.1,1,100,math.inf];out=[]
for k,reg in enumerate(report['region_summaries']):
 ids=np.flatnonzero((r>=bounds[k])&(r<bounds[k+1]));ck('regional population '+str(k),len(ids)==reg['count']);row=dict(region=reg['region'],count=len(ids),metrics={})
 for metric,col in [('absR',0),('Rf',3),('Rv',4)]:
  vals=np.abs(B['residual'][ids,col]);defined=np.isfinite(vals);valid=ids[defined];index=int(valid[np.argmax(vals[defined])]);value=float(abs(B['residual'][index,col]));d=reg['metrics'][metric];ck('regional maximum '+str(k)+metric,index==d['index']and value==d['value']and d['defined_count']==len(valid)and d['undefined_count']==len(ids)-len(valid));row['metrics'][metric]=dict(index=index,value=value,x=float(T['xy'][index,0]),y=float(T['xy'][index,1]),R_Nf_Nv_Rf_Rv=B['residual'][index].tolist())
 out.append(row)
ck('selected order',np.array_equal(A['indices'],CC['indices'])and A['indices'].tolist()==report['local_mp_indices']);sp=[]
for row,i in enumerate(A['indices']):
 a=fields(T['xy'][i],T['jets'][i],A['velocity'][row]);b=fields(T['xy'][i],T['jets'][i],B['velocity'][i]);c=fields(T['xy'][i],T['jets'][i],CC['velocity'][row]);spread=max(a[0],b[0],c[0])-min(a[0],b[0],c[0]);d=report['comparisons'][row];passed=spread<=abs(b[0])/100 and spread<=b[1]/10**8
 ck('exact three-rule spread '+str(i),Q(d['spread'])==spread and d['empirical_pass']==passed and d['index']==i);sp.append(dict(index=int(i),spread=float(spread),spread_over_abs_B_R=float(spread/abs(b[0]))if b[0]else None,spread_over_B_Nf=float(spread/b[1])if b[1]else None,empirical_pass=passed))
for p in [Path(__file__),R/'PARTIAL224_ARITHMETIC_PROOF.md']:bindings[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
d=dict(status='CONFIRMED_FINITE224_ARITHMETIC_ONLY_318_OPEN',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,regions=out,comparisons=sp,scope='No MP or final inverse acceptance.192 still incomplete at preparation. This verifies arithmetic on saved finite inverse outputs only. No primary IPM endpoint.');p=V/'PARTIAL224_ARITHMETIC.json';p.write_text(json.dumps(d,indent=2)+'\n');print(d['status'],d['count'],max(x['spread_over_abs_B_R']for x in sp),max(x['spread_over_B_Nf']for x in sp),all(x['empirical_pass']for x in sp))
