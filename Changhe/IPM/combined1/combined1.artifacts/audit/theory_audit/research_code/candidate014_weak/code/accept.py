from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx,fmpq as Q
import json,hashlib
B=Path(__file__).resolve().parents[1];ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=B/'verification/014_n21_k522.json';b=B/'source/N4_result.json';x=json.loads(a.read_text());y=json.loads(b.read_text())
prep=B.parent/'candidate014_point/verification/preparation.json';binding=json.loads(prep.read_text());assert binding['exact_canonical_maps_equal'] and binding['source_binding_verified']
assert x['source_sha256']==sha(B.parent/'new_successor_weak/data/014/canonical.json')
assert y['canonical_sha256']==sha(B.parent/'candidate014_point/source/N4_canonical.json')
assert y['raw_sha256']==sha(B.parent/'candidate014_point/data/candidate014.json')
checks={k:arb(x[k]).overlaps(arb(y[k])) for k in ['pairing','pairing_by_parts','M','C','D','radius']}
checks.update({'M2':arb(x['normM2']).overlaps(arb(y['M2'])),'C2':arb(x['normC2']).overlaps(arb(y['C2']))})
assert all(checks.values()) and x['direct_parts_overlap'] and y['direct_parts_overlap']
assert Q(x['sup_certificate']['H_upper_exact'])==Q(y['H_upper_exact'])
floor=Q(y['strict_lower_exact']);assert arb(floor.numerator)/floor.denominator<arb(x['radius'])
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':y['candidate'],'checks':checks,'same_H':True,'canonical_source_binding':True,'peer_strict_floor_independently_verified':str(floor),'peer_probe_was_in_objective':y['probe_was_in_candidate014_optimization'],'own_runtime_seconds':x['elapsed_seconds'],'inputs':{str(p):sha(p) for p in [a,b,prep,Path(__file__),B/'PROOF.md',B/'code/check.py',B/'source/N4_PROOF.md',B/'source/N4_check.py']},'verdict':'CONFIRMED N4-214 by independent polar candidate-level reproduction'}
with (B/'verification/ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['verdict'],'strict floor',floor)
