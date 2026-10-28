import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=768;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def moments(a,b,n):
 out=[F(1),(a-b)/(a+b)]
 for j in range(1,n):out.append((2*(a-b)*out[j]+(j-a-b)*out[j-1])/(j+a+b))
 return out[:n+1]
def poly_next(p,q):
 # T_(n+1)(2u-1)=2(2u-1)T_n(2u-1)-T_(n-1)(2u-1).
 out=[F(0)]*(len(p)+1)
 for j,x in enumerate(p):out[j]-=2*x;out[j+1]+=4*x
 for j,x in enumerate(q):out[j]-=x
 return out
def beta_monomial(a,b,n):
 out=[F(1)]
 for j in range(n):out.append(out[-1]*(a+j)/(a+b+j))
 return out
moment_checks=[]
for a,b in [(F(9,10),F(3,2)),(F(1,2),F(3,2)),(F(1,4),F(3,2))]:
 rec=moments(a,b,25);mon=beta_monomial(a,b,25);prev=[F(1)];cur=[F(-1),F(2)];computed=[sum(x*mon[j] for j,x in enumerate(prev)),sum(x*mon[j] for j,x in enumerate(cur))]
 for n in range(1,25):prev,cur=cur,poly_next(cur,prev);computed.append(sum(x*mon[j] for j,x in enumerate(cur)))
 assert computed==rec
 moment_checks.append({'alpha':str(a),'beta':str(b),'count':26,'result':'PASS'})
prod=json.loads((TOP/'evidence/fresh_384.json').read_text());rep=json.loads((TOP/'evidence/replay_640.json').read_text())
assert prod['status']==rep['status']=='COMPUTED_PENDING_AUDIT'
assert prod['count']==rep['count']==8
assert prod['bits']==384 and rep['bits']==640 and rep['degree']>prod['degree']
assert prod['script_sha256']==rep['script_sha256']==sha(TOP/'code/check.py')
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert prod['source_sha256']==rep['source_sha256']==sha(source)
run=LANE/'proofs/134_residual_green_taylor/evidence/production_28'
for key,name in [('journal_sha256','leaves.jsonl'),('metadata_sha256','metadata.json')]:assert prod[key]==rep[key]==sha(run/name)
meta=json.loads((run/'metadata.json').read_text())
assert sha(LANE/'proofs/134_residual_green_taylor/code/integrate.py')==meta['code_sha256']
rows=[json.loads(x) for x in (run/'leaves.jsonl').read_text().splitlines()];old={x['leaf_id']:x for x in rows}
checks=[]
for data in [prod,rep]:
 total=arb(0);last=None
 for row in data['rows']:
  l,r=F(row['left']),F(row['right']);assert l<r and (last is None or last<=l);last=r
  prior=old[row['leaf_id']];assert prior['left']==row['left'] and prior['right']==row['right']
  assert row['axis_formula']==row['a4_tridiagonal_formula']==row['old_center_replay']=='PASS'
  fresh=row['fresh_window'];assert fresh['center_overlap']==fresh['velocity_derivative_overlap']=='PASS'
  assert fresh['left']==row['left'] and fresh['right']==row['right'] and fresh['degree']==data['degree']
  cn=F(row['new_center_norm']['lower_exact']);var=F(row['variation_upper_exact']);assert var==F(fresh['variation_bound']['upper_exact'])
  lower=max(F(0),cn-var);assert lower==F(row['interval_uniform_norm_lower_exact']) and lower>0
  assert arb(row['new_center_norm']['ball']).overlaps(arb(fresh['center_norm']['ball']))
  b=F(-1,2) if r<=0 else F(123,20);assert l>=0 or r<=0
  energy=aa(lower**2)*aa(b*l).exp()*aa(b*(r-l)).expm1()/aa(b)
  assert energy.overlaps(arb(row['new_energy_lower']['ball']));total+=energy
 assert total.overlaps(arb(data['energy_lower']['ball']))
 assert aa(F(327,100)**2)<total.lower()
 checks.append({'bits':data['bits'],'degree':data['degree'],'total_energy':str(total),'strict_lower':'327/100','result':'PASS'})
for x,y in zip(prod['rows'],rep['rows']):
 assert (x['left'],x['right'])==(y['left'],y['right'])
 for key in ['new_center_norm','a4_center_norm','old_center_norm']:assert arb(x[key]['ball']).overlaps(arb(y[key]['ball']))
out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','strict_norm_lower_exact':'327/100','strict_norm_lower_decimal':'3.270','uniform_a_interval':['18/5','4'],'moment_checks':moment_checks,'independent_arithmetic_checks':checks,'center_replays':'PASS','source_sha256':sha(source),'producer_sha256':sha(TOP/'code/check.py'),'audit_sha256':sha(Path(__file__)),'proof_sha256':sha(TOP/'PROOF.md'),'production_sha256':sha(TOP/'evidence/fresh_384.json'),'replay_sha256':sha(TOP/'evidence/replay_640.json'),'integrator_sha256':sha(LANE/'proofs/134_residual_green_taylor/code/integrate.py')}
(TOP/'evidence/final_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
