"""Freeze consumer method dependencies. Actual regional records are bound at execution."""
from pathlib import Path
import evidence_v01 as e
import method_v01 as v
if __name__=='__main__':
 files={}
 for topic in [e.ENERGY,e.ANNULUS,e.EXTERIOR]:
  n=topic+'/verification/manifest_v01.json';m=e.read(e.local(n))
  for name,h in m['files'].items():v.need(e.digest(e.local(name))==h,name);files[name]=h
  files[n]=e.digest(e.local(n))
  n=topic+'/verification/external_review_v01.json';r=e.read(e.local(n));v.need(r['status']=='BOUND');files[n]=e.digest(e.local(n))
  # The derivative deployment is frozen later, after its actual source exists.
 for p in [e.BASE/'PROOF.md',*(e.BASE/'code').glob('*.py'),e.BASE/'verification/fixtures_v01.json']:
  files[str(p.relative_to(e.ROOT))]=e.digest(p)
 fixture=e.read(e.BASE/'verification/fixtures_v01.json');v.need(fixture['status']=='PASS'and fixture['checks']>0)
 m={'schema':'source013-norm-consumer-method-v1','created_utc':e.stamp(),'files':dict(sorted(files.items())),'scope':'Conditional weighted/unweighted method. Same-source actual regional admission, own concrete execution review and both calculations required.'}
 e.put(e.BASE/'verification/manifest_v01.json',m);print('METHOD',e.digest(e.BASE/'verification/manifest_v01.json'),len(files),flush=True)
