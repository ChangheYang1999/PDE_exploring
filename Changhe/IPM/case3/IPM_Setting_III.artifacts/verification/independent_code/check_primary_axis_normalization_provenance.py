from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_axis_normalization_closure';V=R/'verification';dest=V/'SUPPLEMENT_CHECKS.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('identity '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'PROOF_CLARIFICATION.md',R/'RESULTS.md',V/'CHRONOLOGY.json']:bind(p)
initial=json.loads(bind(V/'CHECKS.json'));ck('initial40passed',initial['count']==len(initial['checks'])==40 and all(c['passed']for c in initial['checks']))
for p,h in initial['bindings'].items():bind(p,h)
refs={}
for name,path,h in [('334','research/primary_common_mp_sample/verification/FINAL_BINDINGS.json','0750932980dcee8cd6b52aa57f053718f1e8143941a2d931e71358fd6e5f33db'),('336','research/primary_fresh_sample/verification/FINAL_BINDINGS.json','8647310f5bf4595c0e2073859ec663103c53ae9cefbc1f32313afc9a3878d5bd'),('325','research/closing_endpoint_audit/verification/FINAL_MATRIX_BINDINGS.json','8ee7d0882d3a9eddf7b09482ce2ba5ab540c71663dd1a12adf153b9ce7e13955')]:
 d=json.loads(bind(ROOT/path,h));ck('accepted '+name,d['status'].startswith('CONFIRMED')and d['count']==len(d['checks'])and all(c['passed']for c in d['checks']));refs[name]=d
 if name=='334':
  for p,h0 in d['bindings'].items():bind(p,h0)
for tag,rel in [('334','research/primary_common_mp_sample/verification/CHECKS.json'),('336','research/primary_fresh_sample/verification/INPUTS.json'),('325','research/scaling/PROOF.md')]:
 p=ROOT/rel;bind(p,refs[tag]['bindings'][str(p)])
I=json.loads((ROOT/'research/primary_fresh_sample/verification/INPUTS.json').read_text())
for ent,row,upper in zip(I['states'],initial['rows'],['4.47e-13','1.45e-12','3.25e-12']):
 bind(ent['source'],ent['source_sha256']);bind(ent['exact_input'],ent['exact_input_sha256']);ck('row source identity '+str(row['N']),ent['N']==row['N']and ent['source_sha256']==row['source_sha256']and ent['exact_input_sha256']==row['exact_input_sha256']);ck('conservative bound '+str(row['N']),F(upper)>=F(row['L_axis_distance_from1_upper_bound_exact']))
for p,h in bindings.items():ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_PRIMARY_AXIS_PROVENANCE_SUPPLEMENT',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Raw NPZ and exact input identities; prior accepted334 checks and bindings; accepted336 inputs and325 scaling proof; exact upward finite-formula bounds. No endpoint.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
