from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
import numpy as np
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_quadrature_grid_audit';V=R/'verification';OLD=ROOT/'research/angular_evaluator_sensitivity/verification';checks=[];bindings={};scalar_count=0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest()
 if p.read_bytes()!=b or(h is not None and h!=a):raise AssertionError('binding '+str(p))
 bindings[str(p)]=a;return b
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError(n)
def ex(a):return F(float(a))
def fields(x,y,j,v):
 x,y=ex(x),ex(y);g,gx,gy=map(ex,j[:3]);v1,v2=map(ex,v);a=(2*x+v1)*gx;b=(2*y+v2)*gy;r=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
 return [r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None]
def sign(q):return (q>0)-(q<0)
def crossings(seq):return [i for i in range(len(seq)-1)if seq[i]*seq[i+1]<0]
def zero_mediated(seq):
 return [i for i in range(1,len(seq)-1)if seq[i]==0 and seq[i-1]*seq[i+1]<0]
def display(v):return float(v)if v is not None else float('nan')
def load(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
# Synthetic tests precede candidate reads.
for seq,want in [([1,0,-1],[]),([1,-1,0,1],[0]),([-1,1,-1],[0,1]),([0,0],[])]:ck('manufactured crossings '+str(seq),crossings(list(map(F,seq)))==want)
ck('manufactured zero-mediated sign change',zero_mediated(list(map(F,[1,0,-1])))==[1])
ck('manufactured three sign classes',[sign(F(a))for a in [-1,0,1]]==[-1,0,1])
for args,want in [((0,1,[1,0,1,0],[0,0]),[1,3,2,F(1,3),F(1,2)]),((0,1,[1,0,1,0],[0,1]),[2,4,3,F(1,2),F(2,3)]),((0,0,[0,0,0,0],[0,0]),[0,0,0,None,None]),((1,0,[0,1,0,0],[0,0]),[2,2,1,1,2])]:ck('manufactured finite fields '+str(args),fields(*args)==want)
ck('manufactured Nf depends on V2',fields(0,1,[1,0,1],[0,0])[1]!=fields(0,1,[1,0,1],[0,1])[1])
source_paths=[__file__,R/'PROOF.md',R/'REPLAY_PROTOCOL.md',R/'ARITHMETIC_PROOF.md',V/'REPLAY_LAUNCH_RESOLUTION.md',V/'REPLAY_CACHE_PREPARATION.json',V/'REPLAY_JOB.json']
for p in source_paths:bind(p)
old=json.loads(bind(OLD/'CHECKS.json'));ck('327checked',old['count']==191 and all(z['passed']for z in old['checks']))
for p,h in old['bindings'].items():bind(p,h)
first=json.loads(bind(V/'candidate/COMPLETE.json'));second=json.loads(bind(V/'candidate2/COMPLETE.json'))
for attempt,d,exitname in [('first',first,'JOB_EXIT.json'),('replay',second,'REPLAY_JOB_EXIT.json')]:
 ck('completed '+attempt,d['status']==('COMPLETE_FULL_ANGULAR_GRID_REQUIRES_FRACTION_CHECK_AND_REVIEW'if attempt=='first'else'COMPLETE_FULL_ANGULAR_GRID_REPLAY_REQUIRES_FRACTION_CHECK_AND_REVIEW')and d['count']==len(d['checks'])and all(c['passed']for c in d['checks']))
 exit=json.loads(bind(V/exitname));ck('worker exit0 '+attempt,exit['returncode']==0)
 for p,h in {**d['bindings'],**d['outputs']}.items():bind(p,h)
ck('exact replay module origins',second['module_paths']=={n:str(ROOT/'independent_code'/(n+'.py'))for n in ['angular_evaluator_sensitivity','node_export_inverse_stage','independent_hydrostatic','q_local_checkpoint','q_checkpoint_reader']})
ck('replay versions recorded',all(second['versions'][n]for n in ['python','numpy','torch']))
records=[];outputs={}
for radius in [3,30]:
 bp=OLD/'candidate'/('R'+str(radius)+'_B.npz');bind(bp);b=load(bp);arrays={'B':b};all_exact={};all_round={}
 for label in ['A','C']:
  name='R'+str(radius)+'_'+label+'.npz';p=V/'candidate'/name;q=V/'candidate2'/name;ck('listed output '+str((radius,label)),str(p.resolve())in first['outputs']and str(q.resolve())in second['outputs']);a=load(p);z=load(q)
  ck('all first/replay array identity '+str((radius,label)),set(a)==set(z)and all(a[k].dtype==z[k].dtype and a[k].shape==z[k].shape and a[k].tobytes()==z[k].tobytes()for k in a));arrays[label]=z
 for label in ['A','B','C']:
  a=arrays[label];ck('same coordinates/jet/eps '+str((radius,label)),all(np.array_equal(a[k],b[k])for k in ['x','y','theta','eps','jet'])and a['velocity'].shape==(255,4,2)and a['tail'].shape==(255,4)and a['meta'].shape==(255,10))
  ck('finite operands '+str((radius,label)),all(np.isfinite(a[k]).all()for k in ['x','y','theta','eps','jet','velocity','tail','meta']))
  ck('v1 constant across eps within rule '+str((radius,label)),np.array_equal(a['velocity'][:,:,0],np.repeat(a['velocity'][:,0:1,0],4,axis=1)))
  exact=[]
  for i in range(255):
   row=[]
   for e in range(4):
    z=fields(a['x'][i],a['y'][i],a['jet'][i],a['velocity'][i,e]);scalar_count+=5
    if not(abs(z[0])<=z[1]and abs(z[0])<=2*z[2]and(z[1]!=0 or z[0]==0)and(z[2]!=0 or z[0]==0)):raise AssertionError('triangle inequality')
    row.append(z)
   exact.append(row)
  all_exact[label]=exact;all_round[label]=np.array([[[display(v)for v in row]for row in point]for point in exact])
  ck('all exact finite identities '+str((radius,label)),True,255*4)
 for k,ee in enumerate(b['eps']):
  row=dict(radius=radius,epsilon=float(ee),rules={},pairs={},spreads={})
  for label in ['A','B','C']:
   z=[point[k]for point in all_exact[label]];rr=[a[0]for a in z];cross=crossings(rr);rf=[i for i,a in enumerate(z)if a[3]is not None];rv=[i for i,a in enumerate(z)if a[4]is not None]
   row['rules'][label]=dict(strict_sign_changes=len(cross),crossing_indices=cross,exact_zero_indices=[i for i,a in enumerate(rr)if not a],zero_mediated_sign_changes=zero_mediated(rr),residual_zero_with_positive_Nf=sum(a[0]==0 and a[1]>0 for a in z),Nf_undefined_count=255-len(rf),Nv_undefined_count=255-len(rv),max_abs_R=float(max(abs(a)for a in rr)),max_Rf=float(max(z[i][3]for i in rf))if rf else None,max_Rv=float(max(z[i][4]for i in rv))if rv else None)
  for a,c in [('A','B'),('A','C'),('B','C')]:
   ra=[p[k][0]for p in all_exact[a]];rc=[p[k][0]for p in all_exact[c]];ids=[i for i in range(255)if sign(ra[i])!=sign(rc[i])];ca=set(crossings(ra));cc=set(crossings(rc))
   row['pairs'][a+c]=dict(sign_class_disagreement_indices=ids,opposite_nonzero_sign_indices=[i for i in ids if ra[i]*rc[i]<0],crossings_only_first=sorted(ca-cc),crossings_only_second=sorted(cc-ca),witness_signed_ratios=[dict(index=i,first=display(ra[i]/all_exact[a][i][k][1])if all_exact[a][i][k][1]else None,second=display(rc[i]/all_exact[c][i][k][1])if all_exact[c][i][k][1]else None)for i in ids])
  nf_spread=[];r_spread=[];nf_changes=[]
  for i in range(255):
   zz=[all_exact[a][i][k]for a in ['A','B','C']];spread=max(z[0]for z in zz)-min(z[0]for z in zz);base=zz[1];nf_spread.append(spread/base[1]if base[1]else None);r_spread.append(spread/abs(base[0])if base[0]else None);nf_changes.append(max(z[1]for z in zz)-min(z[1]for z in zz))
  for name,seq in [('over_Nf_B',nf_spread),('over_abs_R_B',r_spread)]:
   valid=[i for i,a in enumerate(seq)if a is not None];arg=max(valid,key=lambda i:seq[i])if valid else None;row['spreads'][name]=dict(maximum=float(seq[arg])if arg is not None else None,argmax=arg,undefined_count=255-len(valid))
  row['Nf_different_across_rules_count']=sum(a!=0 for a in nf_changes);row['Nf_max_absolute_rule_spread']=float(max(nf_changes));records.append(row)
 path=V/('CHECKED_R'+str(radius)+'.npz');np.savez_compressed(path,x=b['x'],y=b['y'],theta=b['theta'],eps=b['eps'],A=all_round['A'],B=all_round['B'],C=all_round['C']);outputs[str(path.resolve())]=sha(path)
for p,h in bindings.items():ck('final stable '+Path(p).name,sha(p)==h)
out=dict(status='PASS_COMPLETE_FINITE_ANGULAR_QUADRATURE_AUDIT_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),scalar_values_recomputed=scalar_count,checks=checks,bindings=bindings,outputs=outputs,records=records,scope='Finite exact arithmetic, full first/replay identity and three-rule angular statistics; no continuum enclosure, global root count, historical causal attribution or primary endpoint.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','scalar_values_recomputed']},indent=2));print(json.dumps([dict(radius=z['radius'],epsilon=z['epsilon'],counts={k:a['strict_sign_changes']for k,a in z['rules'].items()},sign_disagreements={k:len(a['sign_class_disagreement_indices'])for k,a in z['pairs'].items()},spreads=z['spreads'],Nf_different=z['Nf_different_across_rules_count'])for z in records],indent=2))
