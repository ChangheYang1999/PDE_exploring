"""Bind the final seven certificate groups without rerunning their interval covers."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
here=Path(__file__).resolve().parent
cache={}
def digest(p):
 p=Path(p)
 if p not in cache:
  h=sha256()
  with p.open('rb') as f:
   for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
  cache[p]=h.hexdigest()
 return cache[p]
checks=[]
def check(name,value):
 checks.append({'claim':name,'pass':bool(value)})
 assert value,name
proof=here.parent/'PROOF.md'
audits=['audit_matrices.json']+[f'audit_norms_{g}.json' for g in ['fourth','D2u','D2rho','u']]
for name in audits:
 d=json.loads((here/name).read_text())
 check(name+' passed',d['all_pass'])
 check(name+' current proof',d['proof_sha256']==digest(proof))
 for p,h in d['files'].items():check(name+': '+p,digest(here/p)==h)
expected={'M':41,'M1':79,'M2':119,'fourth':36,'D2u':121,'D2rho':314,'u':23}
poly=digest(here/'nb_d2_exact.polynomials.json')
deriv=digest(here/'nb_d2_exact.derivatives.json')
for group,count in expected.items():
 p=here/f'nb_d2_exact.{group}.correlated.json';r=p.with_name(p.stem+'.recheck.json')
 d=json.loads(p.read_text());a=json.loads(r.read_text())
 check(group+' complete',d['status']=='COMPLETE' and not d['failed'] and not d['pending_paths'])
 check(group+' count',len(d['accepted'])==count==a['leaves'])
 check(group+' independent pass',a['all_pass'] and a['primary_sha256']==digest(p))
 check(group+' polynomial source',d['input_sha256' if group in ['M','M1','M2'] else 'source_sha256']==poly)
 if group not in ['M','M1','M2']:check(group+' derivative source',d['derivatives_sha256']==deriv)
for name,count in [('nb_d2_exact.algebra.base.json',21864),('nb_d2_exact.algebra.higher.json',22789),('check_taylor_identity.json',80)]:
 d=json.loads((here/name).read_text());check(name+' passed',d['all_pass'])
check('total 733 complete independently rechecked leaves',sum(expected.values())==733)
record={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'method':'Hash and completion consolidation of already independently rechecked certificates. No interval cover was rerun.','groups':expected,'total_leaves':sum(expected.values()),'checks':checks,'count':len(checks),'files_sha256':{str(p.relative_to(here)):h for p,h in cache.items() if p.is_relative_to(here)},'proof_sha256':digest(proof),'scope':'All three global d2 matrices, five fixed derivative bounds, and four decay bounds. Higher derivative caps are topic91; full parameter contract is topic105. No residual smallness or existence.'}
(here/'audit_complete.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['utc'],record['count'],'PASS; 733 leaves bound')
