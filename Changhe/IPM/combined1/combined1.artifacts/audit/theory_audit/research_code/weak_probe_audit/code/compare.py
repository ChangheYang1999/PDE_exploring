from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
from flint import arb,ctx
ctx.prec=1024
root=Path(__file__).resolve().parents[1]
a=root/'verification/d2_1024.json';b=root/'source/N4_d2_1024.json'
x=json.loads(a.read_text());y=json.loads(b.read_text())
assert x['source_sha256']==y['source_sha256']
checks=[]
for ours,peer in zip(x['probes'],y['probes']):
 assert ours['p']==peer['p']
 for field in ['pairing','N','A','B','C','denominator_without_d']:
  assert arb(ours[field]).overlaps(arb(peer[field])),(ours['p'],field)
  checks.append([ours['p'],field])
 for ob,pb in zip(ours['boxes'],peer['boxes']):
  assert ob['framework']==pb['framework']
  for field in ['necessary_upper','gap','L2_correction_lower_at_d']:
   assert arb(ob[field]).overlaps(arb(pb[field])),(ours['p'],ob['framework'],field)
   checks.append([ours['p'],ob['framework'],field])
  assert ob['excluded'] and pb['excluded'] and arb(ob['gap'])>0
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'checks':checks,'all_overlaps':True,
     'all_fifteen_gaps_positive':True,'independent_sha256':hashlib.sha256(a.read_bytes()).hexdigest(),
     'peer_sha256':hashlib.sha256(b.read_bytes()).hexdigest()}
(root/'verification/comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print('Confirmed',len(checks),'interval overlaps; all 15 gaps positive.')
for q in x['probes'][0]['boxes'][:2]:
 print(q['framework'],'gap',arb(q['gap']).str(24),'L2 lower',arb(q['L2_correction_lower_at_d']).str(24))
