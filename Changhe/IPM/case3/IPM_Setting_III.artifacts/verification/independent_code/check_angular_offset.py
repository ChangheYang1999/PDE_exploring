from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
import numpy as np
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_evaluator_sensitivity';V=R/'verification';checks=[];bindings={}
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();got=hashlib.sha256(b).hexdigest()
 if p.read_bytes()!=b or(h is not None and got!=h):raise AssertionError('binding '+str(p))
 bindings[str(p)]=got;return b
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def count(q):return sum(a*b<0 for a,b in zip(q,q[1:]))
for q,want in [([1,0,-1],0),([1,-1,0,1],1),([0,0],0),([1,-1,1,-1],3),([-1,-1,1],1)]:ck('manufactured adjacent '+str(q),count(list(map(F,q)))==want)
ck('manufactured mean shift',sum(map(F,[1,2,3]))/3==2)
d=json.loads(bind(V/'CHECKS.json'));ck('327finite pass',d['count']==191 and all(c['passed']for c in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
records=[]
for radius in [3,30]:
 p=V/'candidate'/('R'+str(radius)+'_B.npz');bind(p)
 with np.load(p,allow_pickle=False)as z:b={k:z[k]for k in z.files}
 q=[]
 for i in range(255):
  x,y=F(float(b['x'][i])),F(float(b['y'][i]));g,gx,gy=map(lambda a:F(float(a)),b['jet'][i,:3]);row=[]
  for vv in b['velocity'][i]:
   v1,v2=map(lambda a:F(float(a)),vv);a=(2*x+v1)*gx;c=(2*y+v2)*gy;nf=abs(a)+abs(c)+abs(g)
   if not nf:raise ArithmeticError('undefined ratio')
   row.append((a+c-g)/nf)
  q.append(row)
 q=list(map(list,zip(*q)));ref=next(x for x in d['results']if x['radius']==radius)
 for j,ee in enumerate(b['eps']):
  ck('exact original counts '+str((radius,j)),count(q[j])==ref['statistics'][j]['strict_sign_changes'])
  if not j:continue
  delta=[a-c for a,c in zip(q[j],q[0])];mean=sum(delta,F(0))/len(delta);counter=[v+mean for v in q[0]]
  ck('exact mean centering '+str((radius,j)),sum((v-mean for v in delta),F(0))==0)
  rec=dict(radius=radius,epsilon=float(ee),baseline_count=count(q[0]),actual_count=count(q[j]),constant_mean_counterfactual_count=count(counter),delta_min=float(min(delta)),delta_max=float(max(delta)),delta_mean=float(mean),delta_max_departure_from_mean=float(max(abs(a-mean)for a in delta)),actual_vs_constant_counterfactual_sign_disagreements=sum(a*b<0 for a,b in zip(q[j],counter)),exact_zero_counts=[sum(a==0 for a in q[j]),sum(a==0 for a in counter)])
  records.append(rec)
proof=R/'ARITHMETIC_PROOF.md';expected=d['bindings'][str(proof.resolve())];ck('corrected arithmetic proof SHA bound',hashlib.sha256(proof.read_bytes()).hexdigest()==expected)
ck('corrected proof records checker-relative chronology',b'before the separate results checker' in proof.read_bytes())
for p in [__file__,R/'OFFSET_DIAGNOSTIC_PROOF.md',R/'TAIL_DETAIL_PROOF.md']:bind(p)
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_FINITE_OFFSET_DIAGNOSTIC',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,arithmetic_proof_sha256=expected,records=records,scope='Exact mean constant-shift counterfactuals on stored operands; no causal conclusion or inverse enclosure.')
(V/'OFFSET_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','arithmetic_proof_sha256','records']},indent=2))
