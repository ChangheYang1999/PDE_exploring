from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate015_holdout'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
p=BASE/'verification/result.json';d=json.loads(p.read_text())
for rel,h in d['inputs'].items():assert sha(ROOT/rel)==h
s=BASE/'verification/N1_screen_selection.json';sel=json.loads(s.read_text());assert sel['newly_selected_for_later_exact_evaluation']==[[23,2400],[1,6144]]
q=ROOT/sel['frozen'];assert sha(q)==sel['sha256']
raw=next(rel for rel in d['inputs'] if rel.endswith('quot013_pairQ_cpu_m16_exact.json'));meta=json.loads((ROOT/raw).read_text())['meta']
exponents=[q for q in meta['pair_k'] if isinstance(q,int)];assert max(exponents)==4096
K=6144;assert K>max(exponents)
d['probe_rows'].append({'n':1,'K':K,'objective_exponents_at_n':exponents,'coefficient_of_tK_in_objective_span':0,'outside_span':True,'pre_registered_family_member':False,'selection_utc':sel['utc']})
for row in d['probe_rows'][:-1]:row['pre_registered_family_member']=True
for p in [p,s,q,BASE/'PROOF_FIRST_MODE.md',Path(__file__)]:d['inputs'][str(p.relative_to(ROOT))]=sha(p)
d['utc']=datetime.now(timezone.utc).isoformat();d['scope_of_registration_time']='registration_utc concerns the25 original pairs only; (1,6144) was selected later'
with (BASE/'verification/extended_first_mode.json').open('x') as f:json.dump(d,f,indent=2);f.write('\n')
print('extended audit',sha(BASE/'verification/extended_first_mode.json'))
