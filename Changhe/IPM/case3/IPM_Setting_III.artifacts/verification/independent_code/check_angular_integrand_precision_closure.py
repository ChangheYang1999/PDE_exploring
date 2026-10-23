from pathlib import Path
from datetime import datetime,timezone
import json,gzip,re,hashlib,sys
import numpy as np
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/angular_integrand_precision';V=R/'verification';C=V/'candidate';bindings={};checks=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def read(p):
 p=Path(p).resolve();b=p.read_bytes();h=hashlib.sha256(b).hexdigest();ck('stable '+str(p),b==p.read_bytes());bindings[str(p)]=h;return b
def j(p):return json.loads(read(p))
for p in [__file__,R/'CLOSURE_CHECK_PROOF.md']:read(p)
d=j(V/'DISPLAY.json');s=j(V/'SUPPLEMENT_CHECKS.json');a=j(V/'CHECKS.json');result=read(R/'RESULTS.md').decode()
ck('supplement successful',s['status']=='PASS_SUPPLEMENT333_REVIEW_PENDING'and len(s['checks'])==s['count']==7140 and all(x['passed']for x in s['checks']))
ck('display top keys',set(d)=={'status','utc','input_sha256','records','scope'})
expected_rows=[]
for r in d['records']:
 ck('record keys '+str(r['radius']),set(r)=={'radius','nodes','local_MP_minus_double','scalar_minus_batch','precision_integrands','precision_local','component_changes','residuals'})
 for t in r['residuals']:
  ck('residual keys '+str((r['radius'],t['epsilon'])),set(t)=={'epsilon','fields','fixed_Nf_D','step_change_fixed_Nf_MM0','precision_change_to_step_magnitude'})
  ck('four fields',set(t['fields'])=={'DD','MD','DM','MM'})
  for f in t['fields'].values():ck('field keys',set(f)=={'R','Nf','Nv','Rf','Rv'})
  ck('decomposition keys',set(t['fixed_Nf_D'])=={'total','local','inverse','cross','inverse_integrand','inverse_arithmetic'})
  expected_rows.append(f"|{r['radius']}|{t['epsilon']:.0e}|{t['fields']['DD']['Rf']:.12g}|{t['fields']['MM']['Rf']:.12g}|{t['fixed_Nf_D']['total']:.12g}|{t['step_change_fixed_Nf_MM0']:.12g}|")
ck('six Markdown rows exact',re.findall(r'^\|(?:3|30)\|.*$',result,re.M)==expected_rows)
old=Path(j(V/'FRESH_ATTEMPT_PREPARATION.json')['failed_directory'])
with np.load(old/'R3_geometry.npz',allow_pickle=False)as z:og={k:z[k]for k in z.files}
with np.load(C/'R3_geometry.npz',allow_pickle=False)as z:ng={k:z[k]for k in z.files}
read(old/'R3_geometry.npz');read(C/'R3_geometry.npz')
ck('only added scalar baseline field',set(ng)-set(og)=={'scalar_local_jet'}and not set(og)-set(ng))
for k in og:ck('same radius3 shared input array '+k,np.array_equal(og[k],ng[k]))
scalars=0
for dd in [old,C]:
 for digits in [72,108]:
  for kind in ['local','integrands']:
   for p in sorted((dd/f'R3_{kind}_{digits}').glob('chunk_*.json.gz')):
    z=json.loads(gzip.decompress(read(p)))
    ck('schema four decimal fields '+str(p),z['width']==4 and all(isinstance(row,list)and len(row)==4 and all(isinstance(x,str)and re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',x)for x in row)for row in z['rows']))
    scalars+=sum(len(row)for row in z['rows'])
ck('both attempts scalar schema count',scalars==23568)
def dt(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
job=j(V/'JOB.json');design=j(V/'DESIGN_ACCEPTANCE.json');com=j(C/'COMPLETE.json');exit=j(V/'JOB_EXIT.json')
ck('actual datetime run order',dt(design['utc'])<=dt(job['utc'])<=dt(com['started_utc'])<=dt(com['finished_utc'])<=dt(exit['utc']))
ck('third wrapper PID recorded',job['pid']==3375144)
for p,h in {**a['bindings'],**s['bindings']}.items():ck('accepted dependency unchanged '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h);bindings[p]=h
for p,h in bindings.items():ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS333_CLOSURE_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,identical_shared_geometry_keys=sorted(og),added_geometry_keys=sorted(set(ng)-set(og)),schema_scalar_entries_both_attempts=scalars,scope='Finite source, row, geometry and Markdown verification; no continuum error or historical runtime attestation.')
(V/'CLOSURE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','identical_shared_geometry_keys','added_geometry_keys']}))
