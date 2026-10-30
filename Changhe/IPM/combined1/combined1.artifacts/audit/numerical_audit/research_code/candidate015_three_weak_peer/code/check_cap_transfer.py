from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip,time
from flint import fmpq as Q,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate015_three_weak_peer';start=time.monotonic();ctx.prec=1024;inputs={};checks={};sha=lambda p:sha256(p.read_bytes()).hexdigest()
def bind(p,h=None):
 p=Path(p);v=sha(p);assert h is None or h==v;inputs[str(p.relative_to(R))]=v;return p
def read(p,h=None):return json.loads(bind(p,h).read_text())
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
bind(B/'CAP_TRANSFER_PROOF.md');bind(Path(__file__));own=read(B/'verification/result.json','c9350681334bee416f3fa085203b3ebd3c4e383654d61e3c9a477f95288a5375');assert all(own['checks'].values())
for p,h in own['inputs'].items():bind(R/p,h)
accepted=read(R/'research/candidate016_weak_peer/verification/result.json','a9a568fd52a50a5a385f9ea698d06255f091e8e3873d9764b03134808a615941')
for p,h in accepted['own_inputs'].items():bind(R/p,h)
for p,z in accepted['frozen_or_retained_sources'].items():
 data=bind(R/p,z['stored_sha256']).read_bytes();raw=gzip.decompress(data) if z['gzip'] else data;assert sha256(raw).hexdigest()==z['sha256']
assert all(accepted['checks'].values()) and all(accepted['peer_input_bindings'].values());checks['accepted253_current_graph']=True
for k in ['23_2400_gradient_polynomial','23_2400_gradient_global','23_2400_gradient_roots','23_2400_same_H_floor']:assert accepted['checks'][k]
pr=next(z for z in accepted['rows'] if (z['n'],z['K'])==(23,2400));row=next(z for z in own['rows'] if (z['n'],z['K'])==(23,2400));H=Q(row['H_sharp_exact']);assert H==Q(pr['H_upper_exact'])==Q(134987820673508807,62500000000000000000000);checks['same_exact_probe_and_cap']=True
I=abs(arb(row['component_comparisons']['I']['own']));D=arb(row['component_comparisons']['M']['own'])+arb(row['component_comparisons']['C']['own']);root=2*I/(D+(D*D+4*ar(H)*I).sqrt());floor=Q(row['strict_sharp_floor']);assert floor==Q(758369800173081,250000000000000000) and ar(floor)<root and root.overlaps(arb(row['sharp_root'])) and floor>Q(25,54684);checks['own015_root_and_strict_floor']=True
assert all(sha(R/p)==h for p,h in inputs.items());checks['all_hashes_unchanged']=True
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'precision_bits':ctx.prec,'candidate':'C1-N1-015-pairQ-quot013','n':23,'K':2400,'H_upper_exact':str(H),'root':root.str(100),'strict_floor':str(floor),'accepted253_own_inputs':len(accepted['own_inputs']),'accepted253_frozen_peer_sources':len(accepted['frozen_or_retained_sources']),'new_gradient_optimization':False,'new_field_integration':False,'verdict':'CONFIRMED identical-probe transfer of independently accepted sharp gradient cap; complete015 sharp root accepted with its separate independent I/M/C comparison'}
p=B/'verification/cap_transfer_v01.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],'PASS',len(checks),'checks',len(inputs),'inputs','seconds',out['elapsed_seconds'],'sha256',sha(p),flush=True)
