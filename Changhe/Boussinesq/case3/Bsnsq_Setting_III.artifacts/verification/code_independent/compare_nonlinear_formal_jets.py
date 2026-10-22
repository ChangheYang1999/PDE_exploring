#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
V=Path('research/324_nonlinear_formal_jet_checks/verification');checks=[];start=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,t,d=None):
 checks.append(dict(name=n,passed=bool(t),detail=d))
 if not t:raise AssertionError((n,d))
def load(tag,suffix=''):return json.loads((V/(tag+suffix+'.json')).read_text())
for small,large,finalorder in [('n5w100','n8w160',5),('n8w160','n10w190',8)]:
 a=load(small,'_coefficients');b=load(large,'_coefficients');ca=load(small);cb=load(large);label=small+'__'+large
 for r in ca['records']:
  s=next(t for t in cb['records']if t['n']==r['n'])
  for key in ['E','F','fixed_residue_T','fixed_residue_O','theta_leading','omega_leading']:ck(label+f"_n{r['n']}_{key}",r[key]==s[key],dict(smaller=r[key],larger=s[key]))
 for field,maxn in [('theta',finalorder),('omega',finalorder-1),('v',finalorder)]:
  for name,j in a[field].items():
   if int(name)>maxn:continue
   k=b[field][name];h=min(j['known_high'],k['known_high']);ck(label+'_'+field+'_'+name+'_precision',h>=20)
   bad=[(i,j['coefficients'].get(str(i),'0'),k['coefficients'].get(str(i),'0'))for i in range(h)if j['coefficients'].get(str(i),'0')!=k['coefficients'].get(str(i),'0')]
   ck(label+'_'+field+'_'+name,not bad,dict(compared_powers=h,disagreements=bad[:3]))
a=load('n5w110_C2khalf')['records'][0];b=load('n2w50_v4_C2khalf')['records'][0]
for k in ['E','F','fixed_residue_T','fixed_residue_O']:ck('C2khalf_n2_v2_v4_'+k,a[k]==b[k],dict(v2=a[k],v4=b[k]))
counts=[]
for tag,src in [('n5w100','solver_v1_readonly.py'),('n8w160','solver_v1_readonly.py'),('n10w190','solver_v1_readonly.py'),('n5w110_C2khalf','solver_v2_readonly.py'),('n2w50_v3','solver_v3_readonly.py'),('n2w50_v4_C2khalf','solver_v4_readonly.py')]:
 d=load(tag);ck(tag+'_complete',d['status']=='COMPLETE');ck(tag+'_source_hash',d['code_sha256']==sha(V/src));ck(tag+'_arithmetic_hash',d['arithmetic_sha256']==sha(Path('code_independent/check_all_order_fraction_jets.py')))
 z=[c for c in d['checks']if isinstance(c.get('detail'),dict)and'tested_high'in c['detail']];minimum=min(c['detail'].get('tested_count',c['detail']['tested_high'])for c in z);ck(tag+'_nonvacuous_ranges',minimum>=20,dict(minimum_lower_bound=minimum,zero_checks=len(z)))
 counts.append(dict(tag=tag,source=src,source_sha256=d['code_sha256'],passed=d['passed'],total=d['total'],minimum_tested_range_lower_bound=minimum,zero_checks=len(z),thermal=sum('_full_T'in c['name']for c in d['checks']),vorticity=sum('_full_V'in c['name']for c in d['checks']),poisson_definitional=sum('Poisson'in c['name']or'poisson_update'in c['name']for c in d['checks']),negative=sum('_negative'in c['name']for c in d['checks']),analytic_jet=sum('analytic_jets'in c['name']for c in d['checks']),residue=sum('residue'in c['name']for c in d['checks'])))
(V/'range_and_provenance_audit.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),runs=counts,argument='Version1/2 lower=min(0,val)<=0, so tested_high is a lower bound. Version3/4 explicitly record counts. Every zero-check record is inspected.'),indent=2)+'\n')
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=sha(Path(__file__)),scope='Deterministic width consistency and source/range checks, not an independent implementation or convergence proof.')
(V/'precision_comparison.json').write_text(json.dumps(r,indent=2)+'\n');print('checks',r['passed'],r['total']);print(json.dumps(counts,indent=2))
