from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx,fmpq as Q
import json,hashlib
B=Path(__file__).resolve().parents[1];ctx.prec=1024
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=B/'verification/015_n23_k600.json';b=B/'source/N4_result.json';x=json.loads(a.read_text());y=json.loads(b.read_text())
raw=B.parent/'new_successor_weak/data/015/quot013_pairQ_cpu_m16_exact.json'
canonical=B.parent/'new_successor_weak/data/015/canonical.json'
assert y['raw_sha256']==sha(raw) and x['source_sha256']==sha(canonical)
assert x['angular_mode']==y['n']==23 and x['radial_power']==y['K']==600
checks={k:bool(arb(x[k]).overlaps(arb(y[k]))) for k in ['pairing','pairing_by_parts','M','C','D']}
checks.update({'M2':bool(arb(x['normM2']).overlaps(arb(y['M2']))),'C2':bool(arb(x['normC2']).overlaps(arb(y['C2'])))})
assert all(checks.values()) and x['direct_parts_overlap'] and y['direct_parts_overlap']
H=Q(y['H_upper_exact']);Hball=arb(H.numerator)/H.denominator
assert all(arb(v)<Hball for v in x['sup_certificate']['amplitude_caps'])
D=arb(x['D']);I=abs(arb(x['pairing']))
radius=2*I/(D+(D*D+4*Hball*I).sqrt())
assert radius.overlaps(arb(y['radius']))
floor=Q(y['strict_lower_exact']);assert arb(floor.numerator)/floor.denominator<radius
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':y['candidate'],'checks':checks,'peer_H_independently_verified':str(H),'radius_with_peer_H':radius.str(100),'peer_strict_floor_independently_verified':str(floor),'own_original_H':x['sup_certificate']['H_upper_exact'],'own_original_floor':x['strict_lower_exact'],'inputs':{str(p):sha(p) for p in [a,b,raw,canonical,Path(__file__),B/'PROOF.md',B/'code/check.py',B/'source/N4_PROOF.md',B/'source/N4_check.py',B/'source/N4_holdout.json']},'verdict':'CONFIRMED independent full-plane candidate-level reproduction; both rational gradient caps are valid'}
with (B/'verification/ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['verdict'],'strict floor',floor)
